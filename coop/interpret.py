"""Translate behavioural metrics and tournament outcomes into plain-English summaries.

Scalars like vengefulness=0.39 are useless without context. This module produces
qualitative readings, comparisons against archetype anchors, and key-finding
bullets — output that's intelligible without staring at the numbers.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from coop.players.classical import ROSTER


# Qualitative bands per behavioural axis. Bands are inclusive of the lower bound.
_BANDS: dict[str, list[tuple[float, str, str]]] = {
    "vengefulness": [
        (0.00, "very forgiving",
         "shrugs off defection and returns to cooperation almost immediately"),
        (0.15, "forgiving",
         "retaliates briefly but recovers quickly"),
        (0.35, "moderately vengeful",
         "punishes defection for several rounds before forgiving"),
        (0.55, "vengeful",
         "holds a grudge for an extended window after defection"),
        (0.80, "extremely vengeful (Grudger-like)",
         "treats any defection as permanent — never forgives"),
    ],
    "reactiveness": [
        (0.00, "rigid / non-reactive",
         "ignores what the opponent does — plays its own line"),
        (0.15, "weakly reactive",
         "barely shifts in response to the opponent"),
        (0.35, "moderately reactive",
         "adjusts cooperation rate based on the opponent's last move"),
        (0.65, "strongly reactive (TFT-like)",
         "closely tracks the opponent's most recent move"),
        (0.85, "near-perfect mirror",
         "essentially copies the opponent's last move"),
    ],
    "past_focus": [
        (0.00, "future-optimist",
         "willing to test cooperation again after long defection streaks"),
        (0.30, "balanced",
         "uses both recent history and overall reputation"),
        (0.45, "past-focused",
         "decisions track recent history more than overall reputation"),
        (0.65, "strongly memory-driven",
         "current play is dominated by the most recent rounds"),
    ],
}


def label_axis(name: str, value: float) -> tuple[str, str]:
    """Return (band_label, one_line_description) for a behavioural scalar."""
    bands = _BANDS[name]
    label, desc = bands[0][1], bands[0][2]
    for lo, lab, d in bands:
        if value >= lo:
            label, desc = lab, d
    return label, desc


def closest_reference(profile_row: dict, refs: pd.DataFrame) -> str:
    """Find the reference strategy with the smallest L1 distance in the 3-vector."""
    if refs is None or refs.empty:
        return "—"
    axes = ["vengefulness", "reactiveness", "past_focus"]
    point = [float(profile_row[a]) for a in axes]
    best_name = "—"
    best_dist = float("inf")
    for _, r in refs.iterrows():
        ref_point = [float(r[a]) for a in axes]
        dist = sum(abs(a - b) for a, b in zip(point, ref_point))
        if dist < best_dist:
            best_dist = dist
            best_name = str(r["strategy"])
    return best_name


def characteristics_table(profile: pd.DataFrame, refs: pd.DataFrame | None = None) -> pd.DataFrame:
    """Per-population characteristics, with band labels and closest reference strategy."""
    rows = []
    for _, r in profile.iterrows():
        for axis in ["vengefulness", "reactiveness", "past_focus"]:
            val = float(r[axis])
            label, desc = label_axis(axis, val)
            rows.append({
                "population": r.get("population", ""),
                "trait": axis,
                "score": round(val, 2),
                "reading": label,
                "interpretation": desc,
            })
        if refs is not None:
            rows.append({
                "population": r.get("population", ""),
                "trait": "closest archetype",
                "score": "—",
                "reading": closest_reference(r.to_dict(), refs),
                "interpretation": "nearest reference strategy in vector space",
            })
    return pd.DataFrame(rows)


_ARCHETYPE_OF: dict[str, str] = {
    name: arch for arch, entries in ROSTER.items() for name, _ in entries
}


def _focal_rows(matches_df: pd.DataFrame) -> pd.DataFrame:
    """Reshape match records into one row per (focal, opponent) participation."""
    if matches_df.empty:
        return matches_df

    a_focal = matches_df[matches_df["is_focal_a"]].copy()
    a_focal = a_focal.rename(
        columns={
            "player_b": "opponent",
            "score_a": "focal_score",
            "score_b": "opp_score",
            "history_a": "focal_history",
            "history_b": "opp_history",
        }
    )
    b_focal = matches_df[matches_df["is_focal_b"]].copy()
    b_focal = b_focal.rename(
        columns={
            "player_a": "opponent",
            "score_b": "focal_score",
            "score_a": "opp_score",
            "history_b": "focal_history",
            "history_a": "opp_history",
        }
    )
    keep = [
        "population", "matrix", "noise", "repetition", "turns",
        "opponent", "focal_score", "opp_score", "focal_history", "opp_history",
    ]
    return pd.concat([a_focal[keep], b_focal[keep]], ignore_index=True)


def _matchup_verdict(focal_per_turn: float, opp_per_turn: float) -> str:
    """One-liner classifying a (focal, opponent) score pair."""
    diff = focal_per_turn - opp_per_turn
    high = max(focal_per_turn, opp_per_turn)
    low = min(focal_per_turn, opp_per_turn)
    if low >= 2.85:
        return "near full mutual cooperation"
    if high <= 1.15:
        return "stuck in mutual defection"
    if abs(diff) < 0.20 and 1.5 <= focal_per_turn <= 2.6:
        return "alternating exploitation / parity"
    if diff >= 0.50:
        return "dominated opponent"
    if diff <= -0.50:
        return "exploited by opponent"
    if diff > 0:
        return "slight edge to focal"
    return "slight edge to opponent"


def matchup_ledger(matches_df: pd.DataFrame) -> pd.DataFrame:
    """Per-opponent rollup across the whole sweep: matches, rounds, scores, verdict."""
    fr = _focal_rows(matches_df)
    if fr.empty:
        return fr

    grouped = (
        fr.groupby("opponent", as_index=False)
        .agg(
            matches=("turns", "size"),
            rounds=("turns", "sum"),
            focal_total=("focal_score", "sum"),
            opp_total=("opp_score", "sum"),
        )
    )
    grouped["focal/turn"] = (grouped["focal_total"] / grouped["rounds"]).round(2)
    grouped["opp/turn"] = (grouped["opp_total"] / grouped["rounds"]).round(2)
    grouped["archetype"] = grouped["opponent"].map(_ARCHETYPE_OF).fillna("focal/self")
    grouped["verdict"] = [
        _matchup_verdict(f, o) for f, o in zip(grouped["focal/turn"], grouped["opp/turn"])
    ]
    return (
        grouped[["opponent", "archetype", "matches", "rounds", "focal/turn", "opp/turn", "verdict"]]
        .sort_values(["archetype", "opponent"])
        .reset_index(drop=True)
    )


def matchup_ledger_by_population(matches_df: pd.DataFrame) -> pd.DataFrame:
    """Per (population, opponent) rollup for finer-grained inspection."""
    fr = _focal_rows(matches_df)
    if fr.empty:
        return fr
    grouped = (
        fr.groupby(["population", "opponent"], as_index=False)
        .agg(
            matches=("turns", "size"),
            rounds=("turns", "sum"),
            focal_total=("focal_score", "sum"),
            opp_total=("opp_score", "sum"),
        )
    )
    grouped["focal/turn"] = (grouped["focal_total"] / grouped["rounds"]).round(2)
    grouped["opp/turn"] = (grouped["opp_total"] / grouped["rounds"]).round(2)
    grouped["archetype"] = grouped["opponent"].map(_ARCHETYPE_OF).fillna("focal/self")
    grouped["verdict"] = [
        _matchup_verdict(f, o) for f, o in zip(grouped["focal/turn"], grouped["opp/turn"])
    ]
    return (
        grouped[["population", "opponent", "archetype",
                 "matches", "rounds", "focal/turn", "opp/turn", "verdict"]]
        .sort_values(["population", "archetype", "opponent"])
        .reset_index(drop=True)
    )


def environment_volume(matches_df: pd.DataFrame) -> pd.DataFrame:
    """Per (population, matrix, noise): distinct competitors met, matches, rounds."""
    fr = _focal_rows(matches_df)
    if fr.empty:
        return fr
    grouped = (
        fr.groupby(["population", "matrix", "noise"], as_index=False)
        .agg(
            competitors=("opponent", "nunique"),
            matches=("turns", "size"),
            rounds=("turns", "sum"),
            focal_total=("focal_score", "sum"),
        )
    )
    grouped["score_per_turn"] = (grouped["focal_total"] / grouped["rounds"]).round(2)
    return grouped[["population", "matrix", "noise", "competitors", "matches", "rounds", "score_per_turn"]]


def outcomes_table(
    score_table: pd.DataFrame,
    *,
    matrix_R: dict[str, int] | None = None,
    volume: pd.DataFrame | None = None,
) -> pd.DataFrame:
    """One row per (population, matrix, noise) with competitors/matches/rounds and a verdict.

    Pass `volume` (output of `environment_volume`) to fold competitor counts and
    round totals into each row. Without it, only score and verdict are shown.

    The verdict is calibrated to the matrix: anything close to R/turn is mutual
    cooperation; close to P is mutual defection; in between means a mix. By
    default R is looked up from the live PAYOFF_MATRICES registry so custom and
    scenario matrices calibrate correctly.
    """
    if matrix_R is None:
        from coop.tournament import PAYOFF_MATRICES
        matrix_R = {name: rstp[0] for name, rstp in PAYOFF_MATRICES.items()}
    rows = []
    for _, r in score_table.iterrows():
        s = float(r["score_per_turn"])
        R = matrix_R.get(r["matrix"], 3)
        if s >= 0.95 * R:
            verdict = "near full mutual cooperation"
        elif s >= 0.80 * R:
            verdict = "mostly cooperative, occasional friction"
        elif s >= 0.60 * R:
            verdict = "mixed — cooperation under strain"
        elif s >= 0.40 * R:
            verdict = "cooperation broken often, frequent retaliation"
        elif s >= 1.2:
            verdict = "mostly mutual defection"
        else:
            verdict = "exploited / locked in defection"
        rows.append({
            "population": r["population"],
            "matrix": r["matrix"],
            "noise": r["noise"],
            "score_per_turn": round(s, 2),
            "verdict": verdict,
        })
    out = pd.DataFrame(rows)
    if volume is not None and not volume.empty and not out.empty:
        out = out.merge(
            volume[["population", "matrix", "noise", "competitors", "matches", "rounds"]],
            on=["population", "matrix", "noise"],
            how="left",
        )
        out = out[["population", "matrix", "noise", "competitors", "matches", "rounds",
                   "score_per_turn", "verdict"]]
    return out


def key_findings(
    *,
    score_table: pd.DataFrame,
    profile_by_population: pd.DataFrame,
    profile_by_pop_noise: pd.DataFrame,
    focal_name: str,
) -> list[str]:
    """Bullet-point standouts: best/worst environment, biggest behavioural drift, noise sensitivity."""
    bullets: list[str] = []
    if score_table.empty:
        return bullets

    best = score_table.loc[score_table["score_per_turn"].idxmax()]
    worst = score_table.loc[score_table["score_per_turn"].idxmin()]
    bullets.append(
        f"**Best environment:** {best['population']} / {best['matrix']} / noise={best['noise']:.2f} "
        f"({best['score_per_turn']:.2f}/turn)."
    )
    bullets.append(
        f"**Worst environment:** {worst['population']} / {worst['matrix']} / noise={worst['noise']:.2f} "
        f"({worst['score_per_turn']:.2f}/turn)."
    )

    # Drift across populations (at noise=0 if available, else any).
    if not profile_by_population.empty:
        for axis in ["vengefulness", "reactiveness"]:
            spread = float(profile_by_population[axis].max() - profile_by_population[axis].min())
            if spread >= 0.15:
                hi = profile_by_population.loc[profile_by_population[axis].idxmax(), "population"]
                lo = profile_by_population.loc[profile_by_population[axis].idxmin(), "population"]
                bullets.append(
                    f"**{axis.capitalize()} drifts {spread:.2f} across populations** — "
                    f"highest in `{hi}`, lowest in `{lo}`."
                )

    # Noise sensitivity: change in vengefulness from noise=0 to max noise, per population.
    if not profile_by_pop_noise.empty and {"noise", "population"}.issubset(profile_by_pop_noise.columns):
        zero_noise = profile_by_pop_noise[profile_by_pop_noise["noise"] == 0.0]
        max_noise_val = profile_by_pop_noise["noise"].max()
        max_noise = profile_by_pop_noise[profile_by_pop_noise["noise"] == max_noise_val]
        if not zero_noise.empty and not max_noise.empty and max_noise_val > 0:
            merged = zero_noise.merge(max_noise, on="population", suffixes=("_q", "_n"))
            jumps = (merged["vengefulness_n"] - merged["vengefulness_q"]).abs()
            if not jumps.empty and jumps.max() >= 0.15:
                idx = jumps.idxmax()
                pop = merged.loc[idx, "population"]
                v0 = merged.loc[idx, "vengefulness_q"]
                v1 = merged.loc[idx, "vengefulness_n"]
                bullets.append(
                    f"**Noise sensitivity:** in `{pop}`, vengefulness shifts "
                    f"{v0:.2f} → {v1:.2f} as noise rises 0% → {int(max_noise_val * 100)}% "
                    f"({'collapse under noise' if v1 > v0 else 'damping under noise'})."
                )
    return bullets


def render_markdown_section(
    *,
    focal_name: str,
    score_table: pd.DataFrame,
    profile: pd.DataFrame,
    profile_by_noise: pd.DataFrame,
    matches_df: pd.DataFrame | None = None,
    refs: pd.DataFrame | None = None,
) -> str:
    """Compose the 'plain-English' section appended to the report."""
    parts = ["## In plain English\n"]

    parts.append("### Behavioural characteristics\n")
    char_df = characteristics_table(profile, refs=refs)
    if char_df.empty:
        parts.append("_No data._\n")
    else:
        parts.append(char_df.to_markdown(index=False))
        parts.append("\n")

    volume = environment_volume(matches_df) if matches_df is not None else None

    parts.append("\n### Outcomes by environment\n")
    out_df = outcomes_table(score_table, volume=volume)
    if out_df.empty:
        parts.append("_No data._\n")
    else:
        parts.append(out_df.to_markdown(index=False, floatfmt=".2f"))
        parts.append("\n")

    if matches_df is not None and not matches_df.empty:
        parts.append("\n### Matchup ledger (per opponent strategy)\n")
        ledger = matchup_ledger(matches_df)
        if not ledger.empty:
            parts.append(ledger.to_markdown(index=False, floatfmt=".2f"))
            parts.append("\n")

    bullets = key_findings(
        score_table=score_table,
        profile_by_population=profile,
        profile_by_pop_noise=profile_by_noise,
        focal_name=focal_name,
    )
    if bullets:
        parts.append("\n### Key findings\n")
        for b in bullets:
            parts.append(f"- {b}\n")
    return "".join(parts) + "\n"
