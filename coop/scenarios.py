"""Real-life interaction scenarios mapped to game parameters.

Each scenario bundles a payoff matrix (R,S,T,P), a noise level (how often intent
is garbled in transmission), and a relationship length (prob_end — the chance per
round that the two parties never interact again). Together these describe the
game-theoretic character of an everyday environment.

Design notes per scenario are in the `rationale` fields; they are printed by the
CLI so runs are self-documenting.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd

from coop.tournament import (
    PAYOFF_MATRICES,
    TournamentRun,
    _play_one_population,
    make_game,
    play_scoreboard,
)


@dataclass(frozen=True)
class Scenario:
    name: str
    R: float
    S: float
    T: float
    P: float
    noise: float
    prob_end: float          # per-round chance the relationship ends
    turns: int               # hard cap on match length
    description: str
    rationale: str

    @property
    def avg_relationship(self) -> float:
        """Expected match length in rounds given prob_end (capped by turns)."""
        return min(self.turns, 1 / self.prob_end) if self.prob_end > 0 else self.turns

    @property
    def matrix_key(self) -> str:
        return f"scenario_{self.name}"


SCENARIOS: dict[str, Scenario] = {s.name: s for s in [
    Scenario(
        name="public_transport",
        R=3, S=1, T=4, P=0, noise=0.10, prob_end=0.10, turns=150,
        description="Anonymous, fleeting encounters with mild temptation and gridlock risk",
        rationale=(
            "Shoving ahead gains little (T=4). Everyone shoving is gridlock — the worst "
            "outcome for all (P=0), so staying polite while others shove still beats joining "
            "the crush (S=1 > P: snowdrift ordering). Noise high (10%): in a crowd, a "
            "deliberate shove and being pushed look identical. Relationships fleeting "
            "(~10 rounds): mostly strangers, occasionally the same commuters."
        ),
    ),
    Scenario(
        name="grocery_queue",
        R=3, S=1, T=3.5, P=0.5, noise=0.02, prob_end=0.20, turns=150,
        description="Strong norms, total observability, tiny temptation, one-off encounters",
        rationale=(
            "Cutting the queue saves two minutes (T=3.5, barely above R). Intent is "
            "unambiguous — you cannot accidentally jump a queue — so noise is minimal (2%). "
            "Relationships are the shortest of all scenarios (~5 rounds): the norm has to be "
            "self-enforcing because you will never see these people again."
        ),
    ),
    Scenario(
        name="tech_company",
        R=3, S=0, T=5, P=1, noise=0.05, prob_end=0.005, turns=150,
        description="Classic long-run PD with moderate ambiguity",
        rationale=(
            "The canonical matrix: real temptation to take credit or skip the review (T=5), "
            "real sucker cost when you do the glue work and others coast (S=0). Noise 5%: "
            "Slack tone misread, silence misinterpreted. Long relationships (~150 rounds) "
            "are what make cooperation rational here."
        ),
    ),
    Scenario(
        name="sales_team",
        R=3, S=0, T=8, P=2, noise=0.10, prob_end=0.02, turns=150,
        description="Internally competitive: big poaching payoff, cushioned mutual defection",
        rationale=(
            "Poaching a lead pays big (T=8) and a lead-hoarding equilibrium is tolerable — "
            "individuals still close deals (P=2 cushion). Noise 10%: deal attribution is "
            "genuinely ambiguous. Quarterly resets and churn keep relationships to ~50 rounds."
        ),
    ),
    Scenario(
        name="engineering_team",
        R=4, S=0, T=5, P=-1, noise=0.05, prob_end=0.005, turns=150,
        description="Stag-hunt rewards with actively destructive mutual defection",
        rationale=(
            "Cooperation compounds — tests, reviews and docs benefit everyone (R=4, stag-hunt "
            "flavour). Mutual defection is actively destructive: spaghetti code and broken CI "
            "hurt everyone including you (P=-1). Noise 5%: terse PR comments read as hostile "
            "when they weren't. Long tenure (~150 rounds)."
        ),
    ),
    Scenario(
        name="product_team",
        R=3.5, S=0, T=6, P=0.5, noise=0.12, prob_end=0.01, turns=150,
        description="Coordination-heavy, ambiguous credit, high noise",
        rationale=(
            "Success has many parents (R=3.5); claiming credit or landing your pet feature "
            "pays (T=6); competing roadmaps thrash the org (P=0.5). High noise (12%): was "
            "that pushback sabotage or genuine concern? Did they ignore your doc or never "
            "see it? Relationships ~100 rounds."
        ),
    ),
    Scenario(
        name="customer_support",
        R=3, S=0, T=5, P=0.5, noise=0.15, prob_end=0.20, turns=150,
        description="Short ticket-length relationships, highest noise of all scenarios",
        rationale=(
            "Genuinely helping a cooperative customer resolves the ticket (R=3). Fobbing off "
            "a polite customer with canned responses saves real effort now (T=5). Going the "
            "extra mile for someone who leaves a one-star review anyway is the full sucker "
            "payoff (S=0). Escalation and churn hurt both sides but are survivable (P=0.5). "
            "Highest noise of all (15%): tone through text, language barriers, frustration "
            "misread as hostility. Tickets are short: ~5 rounds."
        ),
    ),
    Scenario(
        name="senior_leadership",
        R=3.5, S=0, T=7, P=0.5, noise=0.08, prob_end=0.005, turns=150,
        description="Years-long relationships, big empire-building payoff, slow-burn politics",
        rationale=(
            "An aligned exec team compounds (R=3.5). Empire-building at a peer's expense "
            "pays big — budget, headcount, the CEO's ear (T=7). Backing a colleague who "
            "briefs against you is the full sucker payoff (S=0). Politics consuming the "
            "exec team hurts everyone, but slowly (P=0.5). Noise 8%: strategic ambiguity is "
            "endemic — you rarely know if a slight was deliberate — though execs are skilled "
            "communicators. Years-long relationships (~150 rounds) are what keep trust "
            "rational despite the huge temptation."
        ),
    ),
]}


def list_scenarios() -> list[str]:
    return list(SCENARIOS)


def get_scenario(name: str) -> Scenario:
    if name not in SCENARIOS:
        raise KeyError(f"Unknown scenario: {name!r}. Available: {sorted(SCENARIOS)}")
    return SCENARIOS[name]


def run_scenarios(
    members: list[str],
    *,
    scenarios: list[str] | None = None,
    repetitions: int = 3,
    seed: int = 42,
) -> pd.DataFrame:
    """Full round-robin per scenario; returns records with a 'scenario' column."""
    names = scenarios or list(SCENARIOS)
    frames = []
    for name in names:
        sc = get_scenario(name)
        # Register the scenario's matrix so play_scoreboard/make_game can find it.
        PAYOFF_MATRICES[sc.matrix_key] = (sc.R, sc.S, sc.T, sc.P)
        records = play_scoreboard(
            members,
            matrices=[sc.matrix_key],
            noise=sc.noise,
            turns=sc.turns,
            prob_end=sc.prob_end,
            repetitions=repetitions,
            seed=seed,
        )
        records["scenario"] = name
        frames.append(records)
    return pd.concat(frames, ignore_index=True)


def run_focal_scenarios(
    *,
    focal_factory,
    focal_name: str,
    members: list[str],
    scenarios: list[str] | None = None,
    repetitions: int = 3,
    seed: int = 42,
    only_focal_pairings: bool = True,
    progress: bool = False,
) -> TournamentRun:
    """Run a focal player (typically the LLM) through each scenario's environment.

    Each scenario supplies its own payoff matrix, noise level, and relationship
    length (prob_end). Match records use the scenario name as the 'population'
    label, so every downstream aggregation (behavioural profile, score table,
    plain-English summary, report charts) groups by scenario automatically.
    """
    names = scenarios or list(SCENARIOS)
    run = TournamentRun(focal_name=focal_name)
    for name in names:
        sc = get_scenario(name)
        PAYOFF_MATRICES[sc.matrix_key] = (sc.R, sc.S, sc.T, sc.P)
        _play_one_population(
            run=run,
            pop_name=name,
            members=members,
            matrix=sc.matrix_key,
            game=make_game(sc.matrix_key),
            noise=sc.noise,
            turns=sc.turns,
            prob_end=sc.prob_end,
            repetitions=repetitions,
            seed=seed,
            focal_factory=focal_factory,
            focal_name=focal_name,
            only_focal_pairings=only_focal_pairings,
            progress=progress,
        )
    return run


def scenario_table(records: pd.DataFrame) -> pd.DataFrame:
    """Strategy rows × scenario columns of mean score/turn, sorted by overall."""
    if records.empty:
        return records
    per = (
        records.groupby(["scenario", "strategy"], as_index=False)
        .agg(total_score=("score", "sum"), total_turns=("turns", "sum"))
    )
    per["score_per_turn"] = per["total_score"] / per["total_turns"]
    pivot = per.pivot(index="strategy", columns="scenario", values="score_per_turn")
    pivot["overall"] = pivot.mean(axis=1)
    return pivot.sort_values("overall", ascending=False).round(3)
