import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q7b: the LLM seat beside the simulated baselines, and a canonical-strategy
fingerprint for the LLM's played sequence.

(a) Per opponent type, per-sandbox LLM score per round vs the simulated
    TitForTat-in-seat / Random-in-seat constants (one-sample sign test over the
    69 pre-registered sandboxes; the baseline is a simulation constant, so the
    test is one-sample, not paired).
(b) Fingerprint: for every played round of every LLM agent-game, what each
    canonical strategy WOULD have played given the actual history to that point,
    and how often the LLM matched it. Unit = sandbox.
"""
from __future__ import annotations
import numpy as np, pandas as pd
from pathlib import Path

D = Path(_REPO+"/paper-analysis/data")
T = Path(_REPO+"/paper-analysis/tables")

# ---------- (a) ----------
ag = pd.read_parquet(D / "agent_games.parquet")
ag = ag[ag.game_observed & (ag.n_played > 0) & (ag.paraphrase != "p4")].copy()
ag["spr"] = ag.score / ag.rounds
base = pd.read_csv(T / "gt_q7_baseline_pairs.csv")
b = (base[base.seat_type == "SEAT"]
     .pivot_table(index="baseline", columns="opp_seat_type", values="score_per_round"))
b = b.rename(columns={"SEAT": "LLM"})
rows = []
for ds, sub in ag.groupby("dataset"):
    sbx = sub.groupby(["sandbox", "opponent_type"])["spr"].mean().unstack()
    for opp in sbx.columns:
        x = sbx[opp].dropna()
        rec = dict(dataset=ds, opponent_type=opp, llm_spr=x.mean(), n_sandboxes=len(x))
        for bl in ["TitForTat", "Random", "AlwaysDefect", "Grudger", "Pavlov"]:
            c = b.loc[bl, opp]
            rec[f"base_{bl}"] = c
            rec[f"llm_minus_{bl}"] = x.mean() - c
            rec[f"n_above_{bl}"] = int((x > c).sum())
        rows.append(rec)
A = pd.DataFrame(rows)
A.to_csv(T / "gt_q7_llm_vs_baseline.csv", index=False)
pd.set_option("display.width", 250)
cols = ["opponent_type", "n_sandboxes", "llm_spr", "base_TitForTat", "llm_minus_TitForTat",
        "n_above_TitForTat", "base_Random", "llm_minus_Random", "n_above_Random"]
print("== prereg: LLM score/round vs simulated in-seat baselines ==")
print(A[A.dataset == "prereg"][cols].round(3).to_string(index=False))

# ---------- (b) ----------
dec = pd.read_parquet(D / "decisions.parquet",
                      columns=["dataset", "sandbox", "paraphrase", "model", "effort",
                               "score_state", "condition", "opponent_type", "agent_game_uid",
                               "round", "action", "opponent_action", "is_played"])
dec = dec[dec.is_played & dec.action.notna() & dec.opponent_action.notna()].sort_values(
    ["agent_game_uid", "round"])


def fingerprint(g):
    own = g.action.values; opp = g.opponent_action.values
    n = len(own)
    pred = {}
    pred["AlwaysCooperate"] = np.array(["C"] * n)
    pred["AlwaysDefect"] = np.array(["D"] * n)
    tft = np.array(["C"] + list(opp[:-1]))
    pred["TitForTat"] = tft
    # Grudger: D from the first round after the opponent has ever defected
    grim = np.array(["C"] * n, dtype=object)
    seen = False
    for t in range(n):
        grim[t] = "D" if seen else "C"
        if opp[t] == "D":
            seen = True
    pred["Grudger"] = grim
    # Pavlov / WSLS: repeat own previous move if the opponent cooperated, else switch
    wsls = np.array(["C"] * n, dtype=object)
    for t in range(1, n):
        wsls[t] = own[t - 1] if opp[t - 1] == "C" else ("D" if own[t - 1] == "C" else "C")
    pred["Pavlov"] = wsls
    # TitForTwoTats: D only after two consecutive opponent defections
    t2t = np.array(["C"] * n, dtype=object)
    for t in range(2, n):
        t2t[t] = "D" if opp[t - 1] == "D" and opp[t - 2] == "D" else "C"
    pred["TitForTwoTats"] = t2t
    out = {k: float((v == own).mean()) for k, v in pred.items()}
    out["_n"] = n
    return out


res = []
for ds, sub in dec.groupby("dataset"):
    sub = sub[sub.paraphrase != "p4"] if ds == "prereg" else sub
    f = sub.groupby("agent_game_uid").apply(fingerprint, include_groups=False)
    F = pd.DataFrame(list(f.values), index=f.index)
    meta = sub.groupby("agent_game_uid")[["sandbox", "model", "effort", "score_state",
                                          "condition", "opponent_type"]].first()
    F = F.join(meta)
    F["dataset"] = ds
    res.append(F)
FP = pd.concat(res)
STRATS = ["AlwaysCooperate", "AlwaysDefect", "TitForTat", "Grudger", "Pavlov", "TitForTwoTats"]
FP["best_match"] = FP[STRATS].idxmax(axis=1)
rows = []
for ds, sub in FP.groupby("dataset"):
    for scope, keys in [("all", []), ("opponent_type", ["opponent_type"]),
                        ("model", ["model"]), ("effort", ["effort"]),
                        ("score_state", ["score_state"])]:
        sb = sub.groupby(["sandbox"] + keys)[STRATS].mean().reset_index()
        share = (sub.groupby(["sandbox"] + keys)["best_match"]
                 .value_counts(normalize=True).unstack(fill_value=0).reset_index())
        sb = sb.merge(share, on=["sandbox"] + keys, how="left", suffixes=("", "_share"))
        grp = sb.groupby(keys) if keys else [((), sb)]
        for k, g in grp:
            lab = "all" if not keys else "|".join(
                f"{c}={v}" for c, v in zip(keys, (k if isinstance(k, tuple) else (k,))))
            rec = dict(dataset=ds, scope=scope, level=lab, n_sandboxes=len(g))
            for s in STRATS:
                rec[f"match_{s}"] = g[s].mean()
                col = f"{s}_share" if f"{s}_share" in g else s
                rec[f"bestshare_{s}"] = g[col].mean() if f"{s}_share" in g else np.nan
            rows.append(rec)
B = pd.DataFrame(rows)
B.to_csv(T / "gt_q8_fingerprint.csv", index=False)
print("\n== prereg: fraction of played moves each canonical rule would have predicted ==")
print(B[(B.dataset == "prereg")][["scope", "level", "n_sandboxes"]
      + [f"match_{s}" for s in STRATS]].round(3).to_string(index=False))
