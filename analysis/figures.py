"""Matplotlib PNGs for the three figures the paper needs.

F1  T1 as a dose-response line per condition with the decoy-call rate as a
    dashed reference -- this is the figure that answers OpenAI's Figure 3
    (participation rate vs reasoning effort, seven unlabelled levels, no x
    units). Ours has labelled levels, a null condition and a decoy baseline.
F2  T3 as paired bars: cooperation LLM-vs-LLM against LLM-vs-script, per
    condition (the selective-exploitation picture).
F3  T5 as a climate strip per generation: cooperation and board growth.

House rules, applied here and not negotiable per figure:
* Okabe-Ito palette only (colour-blind safe), and never colour alone: every
  series also differs by marker and line style.
* No text below 10 pt.
* The title states the claim the data supports, not the variable names.
* A source line sits in the footer of every figure.
"""
from __future__ import annotations

import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from analysis import stats

OKABE_ITO = {
    "black": "#000000", "orange": "#E69F00", "sky": "#56B4E9", "green": "#009E73",
    "yellow": "#F0E442", "blue": "#0072B2", "vermillion": "#D55E00", "purple": "#CC79A7",
}
COND_STYLE = {
    "absent":    dict(color=OKABE_ITO["black"],      marker="s", ls=":",  label="absent (no store)"),
    "permitted": dict(color=OKABE_ITO["blue"],       marker="o", ls="-",  label="permitted (control)"),
    "forbidden": dict(color=OKABE_ITO["vermillion"], marker="^", ls="-",  label="forbidden (honeytrap)"),
    "hidden":    dict(color=OKABE_ITO["green"],      marker="D", ls="--", label="hidden (discovery)"),
}
PAIR_COLOR = {"llm-llm": OKABE_ITO["purple"], "llm-script": OKABE_ITO["sky"]}
EFFORT_X = {"off": 0, "low": 1, "medium": 2, "high": 3}

RC = {
    "font.size": 11, "axes.titlesize": 13, "axes.labelsize": 11,
    "xtick.labelsize": 10, "ytick.labelsize": 10, "legend.fontsize": 10,
    "figure.titlesize": 14, "axes.spines.top": False, "axes.spines.right": False,
    "figure.facecolor": "white", "savefig.facecolor": "white",
}


def _footer(fig, source: str) -> None:
    """Source line, wrapped so a long path can never run off the canvas."""
    width = max(60, int(fig.get_figwidth() * 15))
    fig.text(0.008, 0.010, textwrap.fill(str(source), width), ha="left", va="bottom",
             fontsize=10, color="#444444")


def _suptitle(fig, text: str, size: float = 14.0) -> None:
    width = max(48, int(fig.get_figwidth() * 7.4))
    wrapped = textwrap.fill(text, width)
    fig.suptitle(wrapped, fontsize=size, y=0.995, va="top")
    return wrapped.count("\n") + 1


def _wilson_err(k, n):
    lo, hi = stats.wilson_ci(int(k), int(n))
    p = k / n if n else 0.0
    return max(p - lo, 0.0), max(hi - p, 0.0)


def fig_t1_dose_response(t1_df, out_path, source: str, sandbox_df=None, model=None) -> Path:
    """Dose-response on the PRIMARY endpoint when the replicate table is given.

    With `sandbox_df` (one row per sandbox, scope = fixed_population) the lines
    are means over sandboxes of the proportion of LLM-involving games with at
    least one attempted board call, and every sandbox is drawn as a faint dot, so
    the reader sees the replicate scatter the confirmatory test actually uses.
    Without it the figure falls back to the agent-game rate in T1.
    """
    use_primary = sandbox_df is not None and len(sandbox_df)
    if use_primary:
        # per MODEL: only DeepSeek has a high arm, so a pooled off-vs-high line
        # changes the model mix along with the effort (finding 5)
        agg = sandbox_df.groupby(["model", "condition", "effort", "opponent_mix"],
                                 observed=True).agg(
            channel_use_rate=("rate_per_game_either", "mean"),
            decoy_rate=("decoy_rate_per_game_either", "mean"),
            n_games=("n_games_observed", "sum")).reset_index()
        df = agg
    else:
        df = t1_df.copy()
    if "n_games" not in df.columns and "n_agent_games" in df.columns:
        df["n_games"] = df["n_agent_games"]
    models = sorted(set(df["model"])) if "model" in df.columns else [None]
    if model is not None:
        df = df[df["model"] == model]
        if sandbox_df is not None and len(sandbox_df) and "model" in sandbox_df.columns:
            sandbox_df = sandbox_df[sandbox_df["model"] == model]
    df["effort_x"] = df["effort"].map(EFFORT_X)
    mixes = [m for m in ("win", "lose") if m in set(df["opponent_mix"])]
    with plt.rc_context(RC):
        fig, axes = plt.subplots(1, len(mixes), figsize=(11, 6.0), sharey=True)
        axes = np.atleast_1d(axes)
        for ax, mix in zip(axes, mixes):
            sub = df[df["opponent_mix"] == mix].sort_values("effort_x")
            for cond, style in COND_STYLE.items():
                s = sub[sub["condition"] == cond]
                if s.empty:
                    continue
                y = 100 * s["channel_use_rate"].to_numpy(float)
                if use_primary:
                    ax.plot(s["effort_x"], y, lw=2, ms=7, **style)
                    pts = sandbox_df[(sandbox_df["condition"] == cond) & (sandbox_df["opponent_mix"] == mix)]
                    ax.scatter(pts["effort"].map(EFFORT_X) + 0.06, 100 * pts["rate_per_game_either"],
                               s=18, color=style["color"], alpha=0.45, zorder=1, linewidths=0)
                else:
                    err = np.array([_wilson_err(r.channel_use_rate * r.n_games, r.n_games)
                                    for r in s.itertuples()]).T * 100
                    ax.errorbar(s["effort_x"], y, yerr=err, capsize=3, lw=2, ms=7, **style)
            # the decoy comparator comes from the MATCHED arm, never averaged
            # across conditions: `absent` passes no decoy tool at all, so its
            # structural zero must not enter this baseline (finding 5,
            # decision-log 08:10 item 4)
            sub_d = sub[sub["condition"].isin(("permitted", "forbidden", "hidden"))]
            dec = sub_d.groupby("effort_x", observed=True)["decoy_rate"].mean()
            if len(dec):
                ax.plot(dec.index, 100 * dec.to_numpy(float), ls="--", lw=2, color="#555555",
                        marker="x", ms=7, label="decoy tool (listed-use baseline)")
            ax.set_xticks(sorted(sub["effort_x"].unique()))
            ax.set_xticklabels([e for e in ("off", "low", "medium", "high")
                                if EFFORT_X[e] in set(sub["effort_x"])])
            ax.set_xlabel("reasoning effort")
            # Neutral wording: the state is assigned (a warm-up ledger in the v2
            # specs) or proxied by the opponent mix (v1). The panel must not
            # assert whichever mechanism produced it.
            ax.set_title({"win": "ahead state", "lose": "behind state"}.get(mix, mix), fontsize=12)
            ax.grid(axis="y", color="#DDDDDD", lw=0.8)
            ax.set_axisbelow(True)
        axes[0].set_ylabel("LLM-involving games with an attempted\nshared-store call (%)" if use_primary
                           else "agent-games with a shared-store call (%)")
        handles, labels = axes[0].get_legend_handles_labels()
        seen, h2, l2 = set(), [], []
        for h, l in zip(handles, labels):
            if l not in seen:
                seen.add(l)
                h2.append(h)
                l2.append(l)
        fig.legend(h2, l2, loc="lower center", ncol=min(5, len(l2)), frameon=False,
                   bbox_to_anchor=(0.5, 0.065))
        title = _t1_title(df) + (f"  --  {str(model).split('/')[-1]}" if model else "")
        lines = _suptitle(fig, title)
        fig.tight_layout(rect=(0, 0.16, 1, 0.985 - 0.04 * lines))
        _footer(fig, source)
        fig.savefig(out_path, dpi=200)
        plt.close(fig)
    return Path(out_path)


def _t1_title(df) -> str:
    f = df[df["condition"] == "forbidden"]
    if f.empty:
        return "Shared-store use by condition, reasoning effort and opponent mix"
    by_eff = f.groupby("effort", observed=True)["channel_use_rate"].mean()
    order = [e for e in ("off", "low", "medium", "high") if e in by_eff.index]
    if len(order) >= 2:
        delta = 100 * (by_eff[order[-1]] - by_eff[order[0]])
    else:
        delta = 0.0
    by_mix = f.groupby("opponent_mix", observed=True)["channel_use_rate"].mean()
    mix_delta = 100 * (by_mix.get("lose", np.nan) - by_mix.get("win", np.nan))
    if delta >= 5:
        claim = (f"Use of a store they were told not to use rises {delta:+.0f} pp from lowest to highest "
                 f"reasoning effort")
    elif abs(delta) < 5 and np.isfinite(delta):
        claim = "Use of a store they were told not to use is flat across reasoning effort"
    else:
        claim = f"Use of a store they were told not to use changes {delta:+.0f} pp across reasoning effort"
    if np.isfinite(mix_delta):
        claim += f", and is {mix_delta:+.0f} pp higher in the behind state"
    return claim


def fig_t3_pair_bars(t3_df, out_path, source: str) -> Path:
    df = t3_df[t3_df["pair_type"].isin(["llm-llm", "llm-script"])].copy()
    conds = [c for c in ("absent", "permitted", "forbidden", "hidden") if c in set(df["condition"])]
    with plt.rc_context(RC):
        fig, ax = plt.subplots(figsize=(9.5, 5.2))
        width = 0.36
        x = np.arange(len(conds))
        for i, pt in enumerate(["llm-llm", "llm-script"]):
            vals, los, his = [], [], []
            for c in conds:
                r = df[(df["condition"] == c) & (df["pair_type"] == pt)]
                v = float(r["coop_rate"].iloc[0]) if len(r) else np.nan
                vals.append(100 * v)
                los.append(100 * (v - float(r["ci_lo"].iloc[0])) if len(r) else 0)
                his.append(100 * (float(r["ci_hi"].iloc[0]) - v) if len(r) else 0)
            ax.bar(x + (i - 0.5) * width, vals, width, yerr=[los, his], capsize=4,
                   color=PAIR_COLOR[pt], edgecolor="black", linewidth=0.6,
                   hatch="" if pt == "llm-llm" else "//",
                   label="LLM vs LLM" if pt == "llm-llm" else "LLM vs script")
        ax.set_xticks(x)
        ax.set_xticklabels([{"absent": "absent\n(no store)", "permitted": "permitted",
                             "forbidden": "forbidden", "hidden": "hidden"}.get(c, c) for c in conds])
        ax.set_ylabel("cooperation rate (% of moves in a game)")
        ax.set_xlabel("shared-store condition")
        ax.legend(frameon=False, loc="upper right")
        ax.grid(axis="y", color="#DDDDDD", lw=0.8)
        ax.set_axisbelow(True)
        ax.set_title(textwrap.fill(_t3_title(df, conds), 78), fontsize=13)
        fig.tight_layout(rect=(0, 0.075, 1, 1))
        _footer(fig, source)
        fig.savefig(out_path, dpi=200)
        plt.close(fig)
    return Path(out_path)


def _t3_title(df, conds) -> str:
    def val(c, pt):
        r = df[(df["condition"] == c) & (df["pair_type"] == pt)]
        return float(r["coop_rate"].iloc[0]) if len(r) else np.nan
    if "absent" not in conds or "forbidden" not in conds:
        return "Cooperation by pair type and shared-store condition"
    d_llm = 100 * (val("forbidden", "llm-llm") - val("absent", "llm-llm"))
    d_scr = 100 * (val("forbidden", "llm-script") - val("absent", "llm-script"))
    if d_llm - d_scr >= 5:
        return (f"With a forbidden store available, LLM-LLM cooperation moves {d_llm:+.0f} pp while "
                f"LLM-script cooperation moves {d_scr:+.0f} pp: selective, not general")
    return (f"A forbidden store moves LLM-LLM cooperation {d_llm:+.0f} pp and LLM-script "
            f"{d_scr:+.0f} pp: no selective effect")


def fig_t5_climate(t5a_df, out_path, source: str) -> Path:
    df = t5a_df.copy()
    conds = [c for c in ("absent", "permitted", "forbidden", "hidden") if c in set(df["condition"])]
    gens = sorted(df["generation"].unique())
    coop = np.array([[float(df[(df["condition"] == c) & (df["generation"] == g)]["coop_overall"].mean())
                      for g in gens] for c in conds])
    board = np.array([[float(df[(df["condition"] == c) & (df["generation"] == g)]["board_size_mean"].mean())
                       for g in gens] for c in conds])
    with plt.rc_context(RC):
        fig, axes = plt.subplots(2, 1, figsize=(max(7.5, 1.9 * len(gens) + 4), 6.4),
                                 gridspec_kw={"height_ratios": [1, 1]})
        for ax, mat, cmap, lab, fmt in (
                (axes[0], 100 * coop, "viridis", "population cooperation rate (%)", "{:.0f}"),
                (axes[1], board, "cividis", "shared-store entries (cumulative)", "{:.0f}")):
            im = ax.imshow(mat, aspect="auto", cmap=cmap)
            ax.set_xticks(range(len(gens)), [f"gen {g}" for g in gens])
            ax.set_yticks(range(len(conds)), conds)
            vmid = np.nanmin(mat) + 0.55 * (np.nanmax(mat) - np.nanmin(mat)) if np.isfinite(mat).any() else 0
            for i in range(mat.shape[0]):
                for j in range(mat.shape[1]):
                    if np.isfinite(mat[i, j]):
                        ax.text(j, i, fmt.format(mat[i, j]), ha="center", va="center", fontsize=10,
                                color="black" if mat[i, j] > vmid else "white")
            cb = fig.colorbar(im, ax=ax, pad=0.015)
            cb.ax.tick_params(labelsize=10)
            ax.set_title(lab, fontsize=12)
        lines = _suptitle(fig, _t5_title(df, conds, gens), 13.5)
        fig.tight_layout(rect=(0, 0.07, 1, 0.99 - 0.05 * lines))
        _footer(fig, source)
        fig.savefig(out_path, dpi=200)
        plt.close(fig)
    return Path(out_path)


def _t5_title(df, conds, gens) -> str:
    if len(gens) < 2:
        return "Climate after one generation: cooperation and store growth by condition"
    first, last = gens[0], gens[-1]
    d = {c: 100 * (float(df[(df["condition"] == c) & (df["generation"] == last)]["coop_overall"].mean())
                   - float(df[(df["condition"] == c) & (df["generation"] == first)]["coop_overall"].mean()))
         for c in conds}
    worst, best = min(d, key=d.get), max(d, key=d.get)
    return (f"Across {len(gens)} generations the climate moves {d[best]:+.0f} pp in {best} and "
            f"{d[worst]:+.0f} pp in {worst}, while the store only grows")


def all_figures(tables: dict, out_dir, source: str, sandbox_df=None) -> dict:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    made = {}
    # A table can be empty on a partially complete run (no generation has closed
    # yet, say). A missing figure is a gap to report, not a reason to lose the
    # whole report, so each one is attempted independently.
    t1 = tables.get("T1")
    models = sorted(set(t1.df["model"])) if t1 is not None and not t1.df.empty \
        and "model" in t1.df.columns else [None]
    plan = [(f"F1_t1_dose_response_{str(m).split('/')[-1]}" if m else "F1_t1_dose_response",
             fig_t1_dose_response, "T1", dict(sandbox_df=sandbox_df, model=m)) for m in models]
    plan += [("F2_t3_pair_bars", fig_t3_pair_bars, "T3", {}),
             ("F3_t5_climate", fig_t5_climate, "T5a", {})]
    for name, fn, key, kw in plan:
        t = tables.get(key)
        if t is None or t.df is None or t.df.empty:
            continue
        try:
            made[name] = fn(t.df, out_dir / f"{name}.png", source, **kw)
        except Exception as exc:  # noqa: BLE001
            print(f"figure {name} skipped: {type(exc).__name__}: {exc}")
    return made


def main(argv=None) -> int:
    import argparse
    from analysis.load import load_runs
    from analysis.tables import all_tables
    ap = argparse.ArgumentParser(description="Write the figures.")
    ap.add_argument("--runs", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    from analysis.load import sandbox_table
    rd = load_runs(a.runs)
    sb = sandbox_table(rd)
    made = all_figures(all_tables(rd), a.out,
                       f"Source: {Path(a.runs).name} ({len(rd.games):,} LLM agent-games, "
                       f"{rd.games['sandbox'].nunique()} sandboxes); analysis/figures.py",
                       sandbox_df=sb[sb["scope"] == "fixed_population"])
    for k, v in made.items():
        print(k, v)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
