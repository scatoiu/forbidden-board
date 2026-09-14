import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Memory-one summary of the LLM's played sequence: P(C | previous round outcome).

(p_CC, p_CD, p_DC, p_DD) is the standard four-number description of a memory-one
strategy (TitForTat = (1,0,1,0); Pavlov/WSLS = (1,0,0,1); Grudger = (1,0,0,0)
after its first defection; AlwaysC = (1,1,1,1)). Labels are from the LLM's point
of view: CD = the LLM cooperated and the opponent defected. Unit = sandbox.
"""
from __future__ import annotations
import numpy as np, pandas as pd
from pathlib import Path

D = Path(_REPO+"/paper-analysis/data")
T = Path(_REPO+"/paper-analysis/tables")
dec = pd.read_parquet(D / "decisions.parquet",
                      columns=["dataset", "sandbox", "paraphrase", "model", "effort",
                               "score_state", "condition", "opponent_type", "agent_game_uid",
                               "round", "action", "opponent_action", "is_played"])
dec = dec[dec.is_played & dec.action.notna() & dec.opponent_action.notna()].sort_values(
    ["agent_game_uid", "round"]).copy()
g = dec.groupby("agent_game_uid")
dec["prev_own"] = g.action.shift(1)
dec["prev_opp"] = g.opponent_action.shift(1)
dec["prev_round"] = g["round"].shift(1)
dec = dec[dec.prev_round.notna() & (dec["round"] == dec.prev_round + 1)]
dec["state"] = dec.prev_own + dec.prev_opp
dec["C"] = (dec.action == "C").astype(float)

rows = []
for ds, sub in dec.groupby("dataset"):
    sub = sub[sub.paraphrase != "p4"] if ds == "prereg" else sub
    for scope, keys in [("all", []), ("model", ["model"]), ("effort", ["effort"]),
                        ("score_state", ["score_state"]), ("condition", ["condition"]),
                        ("opponent_type", ["opponent_type"])]:
        sb = sub.groupby(["sandbox"] + keys + ["state"])["C"].mean().unstack()
        n = sub.groupby(keys + ["state"])["C"].size() if keys else sub.groupby("state")["C"].size()
        sb = sb.reset_index()
        grp = sb.groupby(keys) if keys else [((), sb)]
        for k, gg in grp:
            lab = "all" if not keys else "|".join(
                f"{c}={v}" for c, v in zip(keys, (k if isinstance(k, tuple) else (k,))))
            rec = dict(dataset=ds, scope=scope, level=lab, n_sandboxes=len(gg))
            for s in ["CC", "CD", "DC", "DD"]:
                rec[f"pC_{s}"] = gg[s].mean() if s in gg else np.nan
            rows.append(rec)
M = pd.DataFrame(rows)
M.to_csv(T / "gt_q8_memoryone.csv", index=False)
pd.set_option("display.width", 200)
print(M[M.dataset == "prereg"].round(3).to_string(index=False))
print("\nper-state decision counts (prereg, game-level denominator):")
print(dec[(dec.dataset == "prereg") & (dec.paraphrase != "p4")].state.value_counts())
