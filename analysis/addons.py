"""The two exploratory add-on arms, as labelled tables beside the frozen report.

    python -m analysis.addons --runs runs/v3 runs/v3b runs/v3-mimo \
        --repairs runs/v7-repair \
        --exploratory runs/v6-low=low_arm --exploratory runs/v5-d30=deficit_d30 \
        --out reports/final-<stamp>-addons

Neither add-on is in the pre-registered family. `runs/v6-low` adds a third
reasoning-effort level that the registration's two-level contrast A never
declared, and `runs/v5-d30` adds a third assigned-state level that contrast B
never declared. Feeding either into `--runs` would turn a registered two-arm
contrast into an undeclared dose family, so `run_all.py`'s root guard refuses
them there; this entry point loads each under its own dataset label and pools
nothing. The pre-registered roots are read exactly as the frozen report read
them (same roots, same repairs) and are never rewritten.

Outputs, in a NEW directory:
  tables/T10_low_arm.csv          off / low / high per block, and the two
                                  exploratory paired contrasts
  tables/T11_deficit_dose.csv     ahead(+10) / behind(-10) / behind(-30) per
                                  block, and the two exploratory contrasts
  tables/addon_contrasts.csv      one row per contrast x block, both arms
  SUMMARY-ADDONS.md               both tables and what each does and does not show
  PROVENANCE.json                 as the final report, plus the freeze check
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from analysis import provenance as provmod
from analysis import stats
from analysis.load import load_runs, sandbox_table
from analysis.tables import Table, df_to_md

#: the one endpoint every arm of both tables is measured on
ENDPOINT = "rate_per_game_either"
MODEL = "deepseek-ai/DeepSeek-V4-Flash-0731"
BLOCKS = ("B1", "B2", "B3", "B4", "B5", "B6")

CALIBRATION_GATE = (
    "The go/no-go gate asked for completion-token medians that separate with NON-OVERLAPPING IQRs "
    "between effort levels. The 13 Sept calibration measured low 294.75-627.5 against high "
    "597.75-2007.25: those IQRs OVERLAP, so the gate fails for that pair and the two levels are not "
    "established as distinct interventions on the trace. Any low-vs-high reading here inherits that.")

D30_HISTORY_NOTE = (
    "The assigned state is built by a six-round warm-up against TitForTat, and the warm-up's move "
    "sequence differs between arms, so the manipulation changes the DISPLAYED HISTORY as well as the "
    "score. ahead (+10) plays D,D,C,C,C,C against C,C,C,C,C,C; behind (-10) plays C,C,C,C,C,C against "
    "D,D,C,C,C,C; behind (-30) plays C six times against D six times - the model 'cooperated' every "
    "round while the scripted opponent defected every round, and ends 0 to 30. A -30 agent therefore "
    "enters the game both further behind AND having been exploited six times out of six rather than "
    "twice out of six. The dose is not a clean score manipulation and nothing here separates the two.")


def _arm(sb: pd.DataFrame, **where) -> pd.DataFrame:
    s = sb
    for k, v in where.items():
        s = s[s[k] == v]
    return s.set_index("block_id")


def _arm_cols(s: pd.DataFrame, tag: str, block: str) -> dict:
    """The numbers one arm contributes to one block's row."""
    if block not in s.index:
        return {f"{tag}_sandbox": "MISSING", f"{tag}_n_games": 0, f"{tag}_n_observed": 0,
                f"{tag}_rate": np.nan, f"{tag}_rate_completed": np.nan, f"{tag}_abort_rate": np.nan,
                f"{tag}_complete": False}
    r = s.loc[block]
    return {
        f"{tag}_sandbox": r["sandbox"],
        f"{tag}_n_games": int(r["n_games_llm_involving"]),
        f"{tag}_n_observed": int(r["n_games_observed"]),
        f"{tag}_rate": float(r[ENDPOINT]),
        f"{tag}_rate_completed": float(r["rate_per_game_either_completed"]),
        f"{tag}_abort_rate": float(r["abort_rate_per_game"]),
        f"{tag}_complete": bool(r["sandbox_complete"]),
    }


def _paired(df: pd.DataFrame, hi: str, lo: str, name: str, label: str) -> dict:
    """One exploratory paired contrast over the blocks that have both arms."""
    d = df[[f"{hi}_rate", f"{lo}_rate"]].dropna()
    blocks = list(df.loc[d.index, "block"]) if "block" in df.columns else list(d.index)
    diffs = (d[f"{hi}_rate"] - d[f"{lo}_rate"]).to_numpy(float)
    rec = {"contrast": name, "label": label, "hi_arm": hi, "lo_arm": lo,
           "blocks": ", ".join(map(str, blocks)), "k": len(diffs),
           "nonzero_k": int((diffs != 0).sum()),
           "mean_diff_pp": 100 * float(diffs.mean()) if len(diffs) else np.nan,
           "n_positive": int((diffs > 0).sum()),
           "per_block_pp": ", ".join(f"{100 * x:+.2f}" for x in diffs)}
    if len(diffs) < 2:
        rec.update(raw_p=np.nan, resolution_floor=np.nan, ci_lo_pp=np.nan, ci_hi_pp=np.nan)
        return rec
    res = stats.sign_flip_test(diffs)
    lo_ci, hi_ci = stats.block_bootstrap_ci(diffs, n_boot=2000, seed=20260913)
    rec.update(raw_p=float(res["p"]), resolution_floor=float(res["min_attainable_p"]),
               ci_lo_pp=100 * lo_ci, ci_hi_pp=100 * hi_ci)
    return rec


def t10_low_arm(prereg_sb: pd.DataFrame, low_sb: pd.DataFrame, low_rd) -> tuple:
    """off / low / high per block, DeepSeek forbidden, behind state."""
    off = _arm(prereg_sb, model=MODEL, condition="forbidden", effort="off", score_state="behind")
    high = _arm(prereg_sb, model=MODEL, condition="forbidden", effort="high", score_state="behind")
    low = _arm(low_sb, model=MODEL, condition="forbidden", effort="low", score_state="behind")
    med = np.nan
    if low_rd is not None and not low_rd.moves.empty:
        mv = low_rd.moves[low_rd.moves["is_decision"]]
        med = float(mv["reasoning_tokens"].median()) if len(mv) else np.nan
    rows = []
    for b in BLOCKS:
        rows.append({"block": b, **_arm_cols(off, "off", b), **_arm_cols(low, "low", b),
                     **_arm_cols(high, "high", b),
                     "low_median_reasoning_tokens": med})
    df = pd.DataFrame(rows)
    contrasts = pd.DataFrame([
        _paired(df, "low", "off", "low_minus_off",
                "EXPLORATORY: low effort minus off effort, forbidden/behind, paired within block"),
        _paired(df, "high", "low", "high_minus_low",
                "EXPLORATORY: high effort minus low effort, forbidden/behind, paired within block"),
    ])
    note = (
        "EXPLORATORY, and outside the pre-registered family. The registration declares contrast A as a "
        "TWO-level paired difference, high minus off. `runs/v6-low` adds a third level that was dropped "
        "at spec-writing time and run afterwards, so reading these three points as a dose-response "
        "would convert a declared two-arm contrast into an undeclared trend family. Neither contrast "
        "below is in the confirmatory family and neither carries a multiplicity adjustment with it. "
        f"{CALIBRATION_GATE} The low arm's own median reasoning tokens per scored decision are printed "
        "in the table, so a reader can see what the 'low' setting actually bought. "
        "The endpoint is the attempted-call rate per OBSERVED game (provider-error aborts that "
        "delivered nothing are excluded from both numerator and denominator), with the completed-game "
        "rate beside it and the abort rate for each arm. The off and high arms are read from the frozen "
        "pre-registered roots exactly as the final report read them, repairs merged.")
    return (Table("T10_low_arm", "T10 (add-on) - Reasoning effort off / low / high, DeepSeek "
                                 "forbidden, behind state, per block", df, df_to_md(df), note),
            contrasts)


def t11_deficit_dose(prereg_sb: pd.DataFrame, d30_sb: pd.DataFrame) -> tuple:
    """ahead(+10) / behind(-10) / behind(-30) per block, DeepSeek forbidden, off."""
    ahead = _arm(prereg_sb, model=MODEL, condition="forbidden", effort="off", score_state="ahead")
    behind = _arm(prereg_sb, model=MODEL, condition="forbidden", effort="off", score_state="behind")
    d30 = _arm(d30_sb, model=MODEL, condition="forbidden", effort="off", score_state="behind")
    rows = []
    for b in BLOCKS:
        rows.append({"block": b, **_arm_cols(ahead, "ahead_plus10", b),
                     **_arm_cols(behind, "behind_minus10", b),
                     **_arm_cols(d30, "behind_minus30", b)})
    df = pd.DataFrame(rows)
    contrasts = pd.DataFrame([
        _paired(df, "behind_minus30", "behind_minus10", "d30_minus_d10",
                "EXPLORATORY: behind -30 minus behind -10, forbidden/off, paired within block"),
        _paired(df, "behind_minus30", "ahead_plus10", "d30_minus_ahead",
                "EXPLORATORY: behind -30 minus ahead +10, forbidden/off, paired within block"),
    ])
    note = (
        "EXPLORATORY, and outside the pre-registered family. The registration declares contrast B as a "
        "TWO-level paired difference, behind minus ahead at +/-10. `runs/v5-d30` adds a deeper deficit "
        "arm run afterwards; treating the three as a dose axis is an undeclared family and is not part "
        "of any confirmatory claim. " + D30_HISTORY_NOTE + " The endpoint is the attempted-call rate "
        "per OBSERVED game, with the completed-game rate and the abort rate beside it. The +10 and -10 "
        "arms are read from the frozen pre-registered roots exactly as the final report read them.")
    return (Table("T11_deficit_dose", "T11 (add-on) - Assigned deficit +10 / -10 / -30, DeepSeek "
                                      "forbidden, off effort, per block", df, df_to_md(df), note),
            contrasts)


def _check_freeze(inventory: Path, roots: list) -> tuple:
    """Every input must still hash to what the freeze recorded.

    This covers the pre-registered and repair roots as well as the add-on ones:
    the claim that the off and high arms are read exactly as the frozen report
    read them is only worth making if the bytes are checked.
    """
    problems, checked = [], 0
    if not inventory.exists():
        return [f"freeze inventory not found: {inventory}"], 0
    want = {}
    for line in inventory.read_text().splitlines()[1:]:
        if not line.strip():
            continue
        path, nbytes, nlines, digest = line.split("\t")
        want[path] = (int(nbytes), int(nlines), digest)
    for root in roots:
        for sb in sorted(p for p in Path(root).iterdir() if p.is_dir()):
            mv = sb / "moves.jsonl"
            if not mv.exists():
                continue
            key = str(mv)
            if key not in want:
                problems.append(f"{key} is not in the freeze inventory: it was created or renamed "
                                f"after the freeze")
                continue
            got = provmod._sha256_and_shape(mv)
            exp_bytes, exp_lines, exp_sha = want[key]
            checked += 1
            if got["sha256"] != exp_sha or got["bytes"] != exp_bytes or got["lines"] != exp_lines:
                problems.append(
                    f"{key} CHANGED since the freeze: {got['bytes']} bytes / {got['lines']} lines / "
                    f"{got['sha256'][:12]} now, {exp_bytes} / {exp_lines} / {exp_sha[:12]} frozen")
    if not checked:
        problems.append("no input was matched against the freeze inventory")
    return problems, checked


def _contrast_lines(name: str, contrasts: pd.DataFrame) -> list:
    out = []
    for r in contrasts.itertuples():
        if not np.isfinite(r.raw_p):
            out.append(f"- **{r.contrast}**: not testable ({r.k} matched block(s)).")
            continue
        out.append(
            f"- **{r.contrast}** ({r.label}): mean paired difference **{r.mean_diff_pp:+.2f} pp**, "
            f"{r.n_positive}/{r.k} blocks positive, {r.nonzero_k} nonzero; per block "
            f"[{r.per_block_pp}] pp; block bootstrap 95% CI {r.ci_lo_pp:+.2f} to {r.ci_hi_pp:+.2f} pp "
            f"(coarse); exact two-sided sign-flip **p = {r.raw_p:.5g}**, resolution floor "
            f"2^-(k-1) = {r.resolution_floor:.5g}. EXPLORATORY: no multiplicity adjustment is carried "
            f"and this is not part of any registered claim.")
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--runs", required=True, nargs="+", help="the frozen pre-registered roots")
    ap.add_argument("--repairs", nargs="*", default=[])
    ap.add_argument("--exploratory", action="append", default=[], metavar="ROOT=LABEL",
                    help="an add-on root and its dataset label; repeatable, never pooled")
    ap.add_argument("--out", required=True)
    ap.add_argument("--freeze-inventory", default="reports/FREEZE-20260913T144509Z-inventory.tsv")
    ap.add_argument("--paraphrases", nargs="+", default=["p1", "p2", "p3"])
    ap.add_argument("--overwrite", action="store_true")
    a = ap.parse_args(argv)

    addons = {}
    for spec in a.exploratory:
        if "=" not in spec:
            raise SystemExit(f"--exploratory expects ROOT=LABEL, got {spec!r}")
        root, label = spec.split("=", 1)
        if label in ("prereg", "replication"):
            raise SystemExit(f"{label!r} is a reserved dataset label; an add-on needs its own")
        addons[root] = label

    out = Path(a.out)
    if out.exists() and any(out.iterdir()) and not a.overwrite:
        raise SystemExit(f"{out} already exists and is not empty; add-ons go in a fresh directory")
    (out / "tables").mkdir(parents=True, exist_ok=True)
    read_start = provmod._utc()

    all_roots = list(a.runs) + list(a.repairs) + list(addons)
    problems, n_checked = _check_freeze(Path(a.freeze_inventory), all_roots)
    if problems:
        raise SystemExit("refusing to run - the inputs no longer match the freeze:\n  "
                         + "\n  ".join(problems))
    print(f"freeze check: {n_checked} input file(s) re-hashed and unchanged")

    from analysis.load import filter_paraphrases
    prereg = filter_paraphrases(load_runs(a.runs, dataset="prereg", repairs=a.repairs),
                                keep=a.paraphrases)
    prereg_sb = sandbox_table(prereg)
    prereg_sb = prereg_sb[prereg_sb["scope"] == "fixed_population"]

    loaded = {}
    for root, label in addons.items():
        rd = load_runs(root, dataset=label)
        sb = sandbox_table(rd)
        loaded[label] = (rd, sb[sb["scope"] == "fixed_population"])
    read_end = provmod._utc()

    low_rd, low_sb = loaded.get("low_arm", (None, pd.DataFrame()))
    d30_rd, d30_sb = loaded.get("deficit_d30", (None, pd.DataFrame()))
    t10, c10 = t10_low_arm(prereg_sb, low_sb, low_rd)
    t11, c11 = t11_deficit_dose(prereg_sb, d30_sb)

    t10.df.to_csv(out / "tables" / "T10_low_arm.csv", index=False)
    t11.df.to_csv(out / "tables" / "T11_deficit_dose.csv", index=False)
    allc = pd.concat([c10.assign(table="T10_low_arm"), c11.assign(table="T11_deficit_dose")],
                     ignore_index=True)
    allc.to_csv(out / "tables" / "addon_contrasts.csv", index=False)
    for label, (rd, sb) in loaded.items():
        sb.to_csv(out / "tables" / f"sandbox_replicates_{label}.csv", index=False)
        rd.violations.to_csv(out / f"violations_{label}.csv", index=False)

    lines = [
        "# Exploratory add-on arms",
        "",
        f"Generated {provmod._utc()} by `analysis/addons.py` against the frozen dataset "
        f"(`{a.freeze_inventory}`): all {n_checked} input `moves.jsonl` files - pre-registered, "
        f"repair and add-on alike - were re-hashed before any table was computed and every one "
        f"matches the freeze byte for byte.",
        "",
        "**Neither table below is part of the pre-registered confirmatory family.** The registration "
        "declares contrast A as a two-level paired difference (high minus off) and contrast B as a "
        "two-level one (behind minus ahead at +/-10). Each add-on introduces a third level of one of "
        "those factors, run after the confirmatory data. Reading either set of three points as a "
        "dose-response would turn a declared two-arm contrast into an undeclared trend family, so "
        "`run_all.py`'s root guard refuses these roots on `--runs` and they are loaded here under "
        "their own dataset labels and pooled with nothing.",
        "",
        f"- add-on roots: " + ", ".join(f"`{r}` (label `{l}`)" for r, l in addons.items()),
        f"- pre-registered roots, read-only and unchanged: " + ", ".join(f"`{r}`" for r in a.runs)
        + (f"; repairs merged from " + ", ".join(f"`{r}`" for r in a.repairs) if a.repairs else ""),
        "",
        f"## {t10.title}", "", t10.markdown, "",
        "### Exploratory paired contrasts", "", *_contrast_lines("T10", c10), "",
        t10.note, "",
        "**What it establishes.** Board use at the `low` reasoning setting, measured on the same "
        "endpoint, in the same six blocks and the same arm as the pre-registered off and high cells. "
        "**What it does not.** It does not establish a dose-response: the three points are not a "
        "declared family, the calibration gate for low-vs-high failed on overlapping IQRs, and the low "
        "arm was run after the confirmatory data on the same provider, so any difference between it "
        "and the frozen arms carries an unmeasured time confound as well.",
        "",
        f"## {t11.title}", "", t11.markdown, "",
        "### Exploratory paired contrasts", "", *_contrast_lines("T11", c11), "",
        t11.note, "",
        "**What it establishes.** Board use under a deeper assigned deficit, in the same six blocks "
        "and the same condition and effort as the pre-registered +10 and -10 cells. "
        "**What it does not.** It does not isolate the size of the deficit: the -30 warm-up also "
        "changes the displayed history (six exploited rounds out of six rather than two), so the score "
        "and the history move together and this design cannot separate them. It is also not part of "
        "contrast B, which is a two-level test at +/-10.",
        "",
        "## Provenance", "",
        "`PROVENANCE.json` in this directory records the analysis commit, the exact argv, package "
        "versions, every root with its dataset label, and one entry per sandbox attempt with its "
        "manifest digest and `moves.jsonl` bytes / lines / SHA256. The add-on roots' digests were "
        "checked against the freeze inventory before any table was computed.",
    ]
    (out / "SUMMARY-ADDONS.md").write_text("\n".join(lines))

    roots_by_dataset = {"prereg": list(a.runs), "repair": list(a.repairs)}
    for root, label in addons.items():
        roots_by_dataset[label] = [root]
    provmod.write_provenance(
        out, argv=[sys.executable, "-m", "analysis.addons", *(argv or sys.argv[1:])],
        roots_by_dataset=roots_by_dataset,
        rds=[prereg] + [rd for rd, _ in loaded.values()],
        defaults={"paraphrases": list(a.paraphrases), "endpoint": ENDPOINT, "model": MODEL,
                  "blocks": list(BLOCKS), "exploratory_labels": sorted(addons.values()),
                  "freeze_inventory": a.freeze_inventory,
                  "freeze_files_verified": n_checked,
                  "registered_family": "NOT APPLICABLE - every contrast here is exploratory"},
        read_start=read_start, read_end=read_end)
    doc = provmod.finalise(out)
    print(f"wrote {out / 'SUMMARY-ADDONS.md'}  (add-on roots: {len(addons)}, "
          f"contrasts: {len(allc)}, artifacts hashed: {len(doc['outputs'])}, "
          f"complete: {doc['complete']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
