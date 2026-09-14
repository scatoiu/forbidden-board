"""Generate the per-model markdown report.

Outputs one .md file with:
  1. Score table (per population × matrix × noise)
  2. Behavioural fingerprint table
  3. Radar chart vs reference strategies (PNG)
  4. Population-conditional drift heatmap (PNG)
  5. Reasoning samples extracted at decision points
"""

from __future__ import annotations

import math
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import matplotlib

matplotlib.use("Agg")  # no GUI
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from coop.interpret import render_markdown_section
from coop.players.focal import LLMReasoningRecord
from coop.tournament import (
    TournamentRun,
    focal_behavioural_profile,
    focal_score_table,
    reference_behavioural_profile,
)


@dataclass
class ReportPaths:
    markdown: Path
    radar_png: Path
    drift_png: Path


def write_report(
    run: TournamentRun,
    *,
    out_dir: str | os.PathLike[str],
    reasoning_log: Iterable[LLMReasoningRecord] | None = None,
    matrix_for_radar: str = "default",
    reference_strategies: list[str] | None = None,
    reference_population: list[str] | None = None,
) -> ReportPaths:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    safe_name = _slug(run.focal_name)
    md_path = out_dir / f"{safe_name}.md"
    radar_png = out_dir / f"{safe_name}__radar.png"
    drift_png = out_dir / f"{safe_name}__drift.png"

    score_table = focal_score_table(run)
    profile = focal_behavioural_profile(run, by=("population",))
    profile_by_noise = focal_behavioural_profile(run, by=("population", "noise"))

    # Compute reference fingerprints for the radar chart in the same matrix.
    refs = reference_behavioural_profile(
        references=reference_strategies,
        matrix=matrix_for_radar,
        population=reference_population,
        turns=200,
        repetitions=3,
    )

    _draw_radar(profile, refs, radar_png, focal_name=run.focal_name)
    _draw_drift_heatmap(profile_by_noise, drift_png, focal_name=run.focal_name)

    md_path.write_text(_render_markdown(
        focal_name=run.focal_name,
        score_table=score_table,
        profile=profile,
        profile_by_noise=profile_by_noise,
        refs=refs,
        radar_png=radar_png.name,
        drift_png=drift_png.name,
        reasoning_log=list(reasoning_log) if reasoning_log else [],
        matches_df=run.to_frame(),
    ))
    return ReportPaths(markdown=md_path, radar_png=radar_png, drift_png=drift_png)


def _render_markdown(
    *,
    focal_name: str,
    score_table: pd.DataFrame,
    profile: pd.DataFrame,
    profile_by_noise: pd.DataFrame,
    refs: pd.DataFrame,
    radar_png: str,
    drift_png: str,
    reasoning_log: list[LLMReasoningRecord],
    matches_df: pd.DataFrame | None = None,
) -> str:
    parts = [f"# Cooperation tournament report: `{focal_name}`\n"]
    parts.append(render_markdown_section(
        focal_name=focal_name,
        score_table=score_table,
        profile=profile,
        profile_by_noise=profile_by_noise,
        matches_df=matches_df,
        refs=refs,
    ))

    parts.append("## 1. Score table\n")
    if score_table.empty:
        parts.append("_No matches recorded._\n")
    else:
        # Pivot for readability.
        pivot = score_table.pivot_table(
            index=["population", "matrix"], columns="noise", values="score_per_turn"
        )
        parts.append(pivot.to_markdown(floatfmt=".3f"))
        parts.append("\n\n_Per-turn score, averaged over opponents and repetitions. Higher = better._\n")

    parts.append("\n## 2. Behavioural fingerprint\n")
    if profile.empty:
        parts.append("_No focal-player matches found._\n")
    else:
        cols = ["population", "vengefulness", "reactiveness", "past_focus", "n_rounds"]
        parts.append(profile[cols].to_markdown(index=False, floatfmt=".3f"))
        parts.append("\n")

    parts.append(f"\n![Radar vs reference strategies]({radar_png})\n")
    parts.append("_Behavioural vectors compared against reference strategies under matrix='default', noise=0._\n")

    parts.append("\n## 3. Population-conditional drift\n")
    parts.append(f"![Drift heatmap]({drift_png})\n")
    parts.append("_How each behavioural vector shifts across populations and noise levels._\n")

    parts.append("\n## 4. Reasoning samples\n")
    samples = _select_reasoning_samples(reasoning_log)
    if not samples:
        parts.append("_No reasoning captured (provider may have returned only an action token)._\n")
    else:
        for s in samples:
            parts.append(
                f"- **Round {s.round_index + 1} vs {s.opponent_name}** "
                f"(self so far: `{s.history_self[-12:]}`, opp: `{s.history_opponent[-12:]}`) "
                f"→ **{s.action}**\n"
            )
            if s.reasoning:
                parts.append(f"  > {s.reasoning}\n")
    return "".join(parts) + "\n"


def _select_reasoning_samples(log: list[LLMReasoningRecord], k: int = 8) -> list[LLMReasoningRecord]:
    """Pick interesting decision points: first move, first reaction to defection, late game."""
    if not log:
        return []
    samples: list[LLMReasoningRecord] = []
    seen_first_def = set()
    samples.append(log[0])
    for r in log:
        opp_hist = r.history_opponent
        last_def_idx = opp_hist.rfind("D")
        if last_def_idx >= 0 and r.opponent_name not in seen_first_def:
            # First reaction to *any* defection by this opponent in this player's life.
            if last_def_idx == len(opp_hist) - 1:
                samples.append(r)
                seen_first_def.add(r.opponent_name)
        if len(samples) >= k:
            break
    if len(samples) < k:
        # Pad with late-game samples for variety.
        samples.extend(log[-(k - len(samples)) :])
    return samples[:k]


def _draw_radar(
    profile: pd.DataFrame,
    refs: pd.DataFrame,
    out_path: Path,
    *,
    focal_name: str,
) -> None:
    """Radar chart: focal averaged across populations, plus reference strategies."""
    axes_labels = ["vengefulness", "reactiveness", "past_focus"]
    angles = np.linspace(0, 2 * math.pi, len(axes_labels), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    def _plot(label: str, values: list[float], **kwargs):
        vals = list(values) + [values[0]]
        ax.plot(angles, vals, label=label, **kwargs)
        ax.fill(angles, vals, alpha=0.10)

    if not profile.empty:
        focal_means = [float(profile[a].mean()) for a in axes_labels]
        _plot(f"{focal_name} (mean)", focal_means, linewidth=2.5)

    if refs is not None and not refs.empty:
        for _, row in refs.iterrows():
            _plot(str(row["strategy"]), [float(row[a]) for a in axes_labels], linewidth=1.0, linestyle="--")

    ax.set_thetagrids(np.degrees(angles[:-1]), axes_labels)
    ax.set_ylim(0, 1)
    ax.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax.set_title(f"Behavioural fingerprint: {focal_name}", pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.4, 1.1), fontsize=8)
    fig.tight_layout()
    fig.savefig(out_path, dpi=130, bbox_inches="tight")
    plt.close(fig)


def _draw_drift_heatmap(profile_by_noise: pd.DataFrame, out_path: Path, *, focal_name: str) -> None:
    """Heatmap: rows=(population, noise), columns=behavioural vectors."""
    if profile_by_noise.empty:
        # Write a placeholder image so the markdown link doesn't break.
        fig, ax = plt.subplots(figsize=(4, 2))
        ax.text(0.5, 0.5, "no data", ha="center", va="center")
        ax.set_axis_off()
        fig.savefig(out_path, dpi=110, bbox_inches="tight")
        plt.close(fig)
        return

    df = profile_by_noise.copy()
    df["row"] = df.apply(lambda r: f"{r['population']} | n={r['noise']:.2f}", axis=1)
    cols = ["vengefulness", "reactiveness", "past_focus"]
    matrix = df.set_index("row")[cols].sort_index().to_numpy()
    rows = df.set_index("row")[cols].sort_index().index.tolist()

    fig, ax = plt.subplots(figsize=(5, max(3, 0.35 * len(rows))))
    im = ax.imshow(matrix, vmin=0, vmax=1, aspect="auto", cmap="viridis")
    ax.set_xticks(range(len(cols)))
    ax.set_xticklabels(cols, rotation=20, ha="right")
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels(rows, fontsize=8)
    ax.set_title(f"Drift map: {focal_name}", fontsize=10)
    for i in range(len(rows)):
        for j in range(len(cols)):
            ax.text(j, i, f"{matrix[i, j]:.2f}",
                    ha="center", va="center", fontsize=7,
                    color="white" if matrix[i, j] < 0.55 else "black")
    fig.colorbar(im, ax=ax, fraction=0.04, pad=0.04, label="value (0–1)")
    fig.tight_layout()
    fig.savefig(out_path, dpi=130, bbox_inches="tight")
    plt.close(fig)


def _slug(s: str) -> str:
    return "".join(c if c.isalnum() or c in "._-" else "_" for c in s).strip("_")
