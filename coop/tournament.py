"""Tournament runner.

Wraps axelrod's match infrastructure but plays matches directly so we can capture
per-turn move logs, store them as Parquet, and compute behavioural metrics
afterwards. Sweeps over (population, payoff matrix, noise level) combinations.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from itertools import combinations
from pathlib import Path
from typing import Callable, Iterable

import axelrod as axl
import pandas as pd

from coop.metrics import BehaviouralVectors, aggregate, behavioural_vectors
from coop.players.classical import make_player
from coop.players.focal import FocalLLMPlayer

log = logging.getLogger(__name__)


# Payoff matrices, (R, S, T, P) convention: R=mutual coop, S=sucker, T=temptation,
# P=mutual defect. Canonical PD requires T > R > P > S and 2R > T + S; several of
# these deliberately bend those constraints to reshape the game's incentives.
PAYOFF_MATRICES: dict[str, tuple[int, int, int, int]] = {
    "default": (3, 0, 5, 1),         # axelrod default
    "high_temptation": (3, 0, 10, 1),  # breaks 2R > T+S: alternating exploitation pays
    "low_temptation": (3, 0, 4, 1),  # close to break-even — exploitation barely pays
    # Mutual defection actively hurts (P < 0): even greedy strategies have a
    # reason to coordinate away from the D/D trap.
    "punishing_defection": (3, 0, 5, -1),
    # Being suckered isn't catastrophic (S > P): trying cooperation is low-risk.
    # Note this makes it a snowdrift/chicken-style game, not a strict PD.
    "cheap_forgiveness": (3, 2, 5, 1),
    # Cooperation is much more valuable (R raised), defection still pays a bit.
    "stag_hunt": (4, 0, 5, 1),
    # Defection more tempting AND mutual defection less costly — tests whether
    # anything holds cooperation together. Also breaks 2R > T+S.
    "brutal_world": (3, 0, 8, 2),
}


def make_game(matrix_name: str) -> axl.Game:
    R, S, T, P = PAYOFF_MATRICES[matrix_name]
    # axelrod.Game(r=, s=, t=, p=)
    return axl.Game(r=R, s=S, t=T, p=P)


@dataclass
class MatchRecord:
    """One played match — score, full move log, and computed behavioural vectors."""

    population: str
    matrix: str
    noise: float
    repetition: int
    turns: int
    player_a: str
    player_b: str
    score_a: int
    score_b: int
    history_a: str
    history_b: str
    is_focal_a: bool = False  # True if player_a is the LLM (the focal player)
    is_focal_b: bool = False


@dataclass
class TournamentRun:
    """Container for one focal-player tournament across populations/matrices/noise levels."""

    focal_name: str
    matches: list[MatchRecord] = field(default_factory=list)

    def to_frame(self) -> pd.DataFrame:
        return pd.DataFrame([m.__dict__ for m in self.matches])

    def save_parquet(self, path: str | Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        self.to_frame().to_parquet(path, index=False)


def _round_robin(players: list[axl.Player]) -> Iterable[tuple[int, int]]:
    """All unordered pairs by index, including self-play (axelrod default behaviour)."""
    n = len(players)
    for i in range(n):
        for j in range(i, n):  # include i==j: self-play, per axelrod convention
            yield i, j


def play_tournament(
    *,
    focal_factory: Callable[[], axl.Player],
    focal_name: str,
    population_names: list[str],
    population_lookup: Callable[[str], list[str]],
    matrices: list[str] | None = None,
    noise_levels: list[float] | None = None,
    turns: int = 200,
    prob_end: float = 0.01,
    repetitions: int = 5,
    seed: int = 42,
    progress: bool = False,
    only_focal_pairings: bool = False,
) -> TournamentRun:
    """Run the full sweep and return all match records.

    Args:
        focal_factory: zero-arg callable returning a fresh focal player (typically the LLM).
        focal_name: human-readable name for the focal player (goes in the report).
        population_names: which named populations to play in.
        population_lookup: function mapping a population name to a list of strategy names.
        matrices: payoff-matrix names from PAYOFF_MATRICES (default: all three).
        noise_levels: move-flip rates (default: 0, 0.01, 0.05, 0.10).
        turns: max rounds per match.
        prob_end: probability of early termination per round (set to 0 to disable).
        repetitions: number of repeated plays per pairing.
        only_focal_pairings: if True, skip classical-vs-classical matches (saves time).
    """
    matrices = matrices or list(PAYOFF_MATRICES)
    noise_levels = noise_levels if noise_levels is not None else [0.0, 0.01, 0.05, 0.10]

    run = TournamentRun(focal_name=focal_name)

    for pop_name in population_names:
        members = population_lookup(pop_name)
        for matrix_name in matrices:
            game = make_game(matrix_name)
            for noise in noise_levels:
                _play_one_population(
                    run=run,
                    pop_name=pop_name,
                    members=members,
                    matrix=matrix_name,
                    game=game,
                    noise=noise,
                    turns=turns,
                    prob_end=prob_end,
                    repetitions=repetitions,
                    seed=seed,
                    focal_factory=focal_factory,
                    focal_name=focal_name,
                    only_focal_pairings=only_focal_pairings,
                    progress=progress,
                )
    return run


def _play_one_population(
    *,
    run: TournamentRun,
    pop_name: str,
    members: list[str],
    matrix: str,
    game: axl.Game,
    noise: float,
    turns: int,
    prob_end: float,
    repetitions: int,
    seed: int,
    focal_factory: Callable[[], axl.Player],
    focal_name: str,
    only_focal_pairings: bool,
    progress: bool,
) -> None:
    # Build the player roster for this slice: classical members + the focal LLM.
    classical_names = list(members)
    n_classical = len(classical_names)
    focal_idx = n_classical  # focal is the last player slot

    for rep in range(repetitions):
        # Fresh players each repetition so history is reset cleanly.
        classicals = [make_player(n) for n in classical_names]
        focal = focal_factory()
        focal.name = focal_name
        players = classicals + [focal]

        for i, j in _round_robin(players):
            if only_focal_pairings and i != focal_idx and j != focal_idx:
                continue
            pa, pb = players[i], players[j]
            if i == j:
                # Self-play needs a clone of the same strategy.
                pb = pa.clone()

            try:
                match = axl.Match(
                    (pa, pb),
                    turns=turns,
                    prob_end=prob_end if prob_end and prob_end > 0 else None,
                    game=game,
                    noise=noise,
                    seed=seed + rep * 100003 + i * 1009 + j,
                )
                interactions = match.play()
            except (ValueError, ArithmeticError) as e:
                # Some strategies (e.g. ZD-Extort-2) are mathematically defined only
                # for matrices satisfying 2R > T+S. Skip such pairings rather than
                # crashing the whole sweep.
                log.warning(
                    "Skipping %s vs %s on matrix=%s: %s",
                    pa.name, pb.name, matrix, e,
                )
                # Replace problem players with fresh instances so subsequent matches
                # don't carry over the failed setup state.
                players[i] = make_player(classical_names[i]) if i < n_classical else focal_factory()
                if i != j:
                    players[j] = make_player(classical_names[j]) if j < n_classical else focal_factory()
                if i == focal_idx or j == focal_idx:
                    players[focal_idx].name = focal_name
                continue
            score_a, score_b = match.final_score() or (0, 0)
            history_a = "".join("C" if a == axl.Action.C else "D" for a, _ in interactions)
            history_b = "".join("C" if b == axl.Action.C else "D" for _, b in interactions)

            run.matches.append(
                MatchRecord(
                    population=pop_name,
                    matrix=matrix,
                    noise=noise,
                    repetition=rep,
                    turns=len(interactions),
                    player_a=pa.name,
                    player_b=pb.name,
                    score_a=int(score_a),
                    score_b=int(score_b),
                    history_a=history_a,
                    history_b=history_b,
                    is_focal_a=(i == focal_idx),
                    is_focal_b=(j == focal_idx),
                )
            )

        if progress:
            log.info(
                "[%s/%s/noise=%.2f] rep %d/%d done (matches=%d)",
                pop_name, matrix, noise, rep + 1, repetitions, len(run.matches),
            )


def play_scoreboard(
    members: list[str],
    *,
    matrices: list[str] | None = None,
    noise: float = 0.0,
    turns: int = 150,
    prob_end: float = 0.01,
    repetitions: int = 3,
    seed: int = 42,
) -> pd.DataFrame:
    """Full round-robin of classical strategies — no focal player.

    Returns one row per (matrix, repetition, strategy, opponent) participation with
    the strategy's score and turns played. Use `scoreboard_table` to pivot into the
    strategy × matrix view.
    """
    matrices = matrices or list(PAYOFF_MATRICES)
    rows: list[dict] = []

    for matrix_name in matrices:
        game = make_game(matrix_name)
        for rep in range(repetitions):
            players = [make_player(n) for n in members]
            for i in range(len(players)):
                for j in range(i, len(players)):
                    pa = players[i]
                    pb = players[j] if i != j else pa.clone()
                    try:
                        match = axl.Match(
                            (pa, pb),
                            turns=turns,
                            prob_end=prob_end if prob_end and prob_end > 0 else None,
                            game=game,
                            noise=noise,
                            seed=seed + rep * 100003 + i * 1009 + j,
                        )
                        interactions = match.play()
                    except (ValueError, ArithmeticError) as e:
                        log.warning(
                            "Skipping %s vs %s on matrix=%s: %s",
                            members[i], members[j], matrix_name, e,
                        )
                        players[i] = make_player(members[i])
                        if i != j:
                            players[j] = make_player(members[j])
                        continue
                    score_a, score_b = match.final_score() or (0, 0)
                    n = len(interactions)
                    rows.append({
                        "matrix": matrix_name, "noise": noise, "repetition": rep,
                        "strategy": members[i], "opponent": members[j],
                        "score": float(score_a), "turns": n,
                    })
                    if i != j:
                        rows.append({
                            "matrix": matrix_name, "noise": noise, "repetition": rep,
                            "strategy": members[j], "opponent": members[i],
                            "score": float(score_b), "turns": n,
                        })
    return pd.DataFrame(rows)


def scoreboard_table(records: pd.DataFrame, *, columns: str = "matrix") -> pd.DataFrame:
    """Pivot scoreboard records into strategy rows × `columns` of mean score/turn.

    columns='matrix' gives the per-payoff view; columns='noise' gives the
    noise-sweep view (averaged over matrices). Adds an 'overall' column (mean
    across pivot columns) and sorts by it, descending.
    """
    if records.empty:
        return records
    per = (
        records.groupby([columns, "strategy"], as_index=False)
        .agg(total_score=("score", "sum"), total_turns=("turns", "sum"))
    )
    per["score_per_turn"] = per["total_score"] / per["total_turns"]
    pivot = per.pivot(index="strategy", columns=columns, values="score_per_turn")
    pivot["overall"] = pivot.mean(axis=1)
    return pivot.sort_values("overall", ascending=False).round(3)


# ---------- Aggregations used by the report generator ---------------------------------


def focal_score_table(run: TournamentRun) -> pd.DataFrame:
    """Mean per-turn score for the focal player, sliced by (population, matrix, noise)."""
    df = run.to_frame()
    if df.empty:
        return df

    focal_rows = []
    for _, row in df.iterrows():
        if row["is_focal_a"]:
            focal_rows.append({
                "population": row["population"],
                "matrix": row["matrix"],
                "noise": row["noise"],
                "score_per_turn": row["score_a"] / max(1, row["turns"]),
                "opponent": row["player_b"],
            })
        elif row["is_focal_b"]:
            focal_rows.append({
                "population": row["population"],
                "matrix": row["matrix"],
                "noise": row["noise"],
                "score_per_turn": row["score_b"] / max(1, row["turns"]),
                "opponent": row["player_a"],
            })

    fdf = pd.DataFrame(focal_rows)
    if fdf.empty:
        return fdf
    return (
        fdf.groupby(["population", "matrix", "noise"], as_index=False)["score_per_turn"]
        .mean()
        .sort_values(["matrix", "population", "noise"])
        .reset_index(drop=True)
    )


def focal_behavioural_profile(
    run: TournamentRun, *, by: tuple[str, ...] = ("population",)
) -> pd.DataFrame:
    """Compute behavioural vectors for the focal player, aggregated by `by` columns.

    by=('population',) gives one fingerprint per population. Use ('population','noise')
    to also condition on noise.
    """
    df = run.to_frame()
    if df.empty:
        return df

    rows = []
    for _, r in df.iterrows():
        if r["is_focal_a"]:
            rows.append({**{k: r[k] for k in by}, "self": r["history_a"], "opp": r["history_b"]})
        elif r["is_focal_b"]:
            rows.append({**{k: r[k] for k in by}, "self": r["history_b"], "opp": r["history_a"]})

    if not rows:
        return pd.DataFrame()

    out_rows = []
    grouped: dict[tuple, list[BehaviouralVectors]] = {}
    for entry in rows:
        key = tuple(entry[k] for k in by)
        grouped.setdefault(key, []).append(behavioural_vectors(entry["self"], entry["opp"]))

    for key, vecs in grouped.items():
        agg = aggregate(vecs)
        out = dict(zip(by, key))
        out.update(agg.as_dict())
        out["n_rounds"] = agg.n_rounds
        out_rows.append(out)
    return pd.DataFrame(out_rows).sort_values(list(by)).reset_index(drop=True)


def reference_behavioural_profile(
    *,
    references: list[str] | None = None,
    matrix: str = "default",
    turns: int = 200,
    repetitions: int = 5,
    seed: int = 1,
    population: list[str] | None = None,
) -> pd.DataFrame:
    """Compute behavioural vectors for reference strategies in the same setup.

    Used as anchors on the radar chart so an LLM's vector is interpretable.
    """
    references = references or ["TitForTat", "Pavlov", "AlwaysCooperate", "Grudger"]
    population = population or ["AlwaysCooperate", "AlwaysDefect", "TitForTat", "Pavlov", "Random"]

    rows = []
    for ref_name in references:
        run = TournamentRun(focal_name=ref_name)
        # Use the classical strategy itself as the focal player.
        _play_one_population(
            run=run,
            pop_name="reference",
            members=population,
            matrix=matrix,
            game=make_game(matrix),
            noise=0.0,
            turns=turns,
            prob_end=0.0,
            repetitions=repetitions,
            seed=seed,
            focal_factory=lambda n=ref_name: make_player(n),
            focal_name=ref_name,
            only_focal_pairings=True,
            progress=False,
        )
        prof = focal_behavioural_profile(run, by=("population",))
        if not prof.empty:
            prof = prof.iloc[0].to_dict()
            prof["strategy"] = ref_name
            rows.append(prof)
    return pd.DataFrame(rows)
