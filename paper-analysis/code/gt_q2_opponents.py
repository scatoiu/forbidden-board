import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q2: LLM cooperation and score per opponent strategy, by effort / state / model.

Unit for the headline table = sandbox (per-sandbox mean over that sandbox's
agent-games against each opponent type, then mean over sandboxes with a
sandbox-level bootstrap CI). Cell breakdowns are means over sandboxes in the
cell. Score is normalised per round because games end stochastically.
"""
from __future__ import annotations
import numpy as np, pandas as pd
from pathlib import Path

D = Path(_REPO+"/paper-analysis/data")
T = Path(_REPO+"/paper-analysis/tables")
ag = pd.read_parquet(D / "agent_games.parquet")
ag = ag[ag.game_observed & (ag.n_played > 0)].copy()
ag["spr"] = ag.score / ag.rounds
ag["opp_spr"] = ag.opp_score / ag.rounds
ag["mutual_D"] = ag.n_DD / ag.n_played
ag["mutual_C"] = ag.n_CC / ag.n_played
ag["exploited_opp"] = ag.n_DC / ag.n_played     # own D, opp C
ag["was_exploited"] = ag.n_CD / ag.n_played     # own C, opp D


def boot(x, n=10000, seed=7):
    x = np.asarray(x, float); x = x[~np.isnan(x)]
    if len(x) < 2: return (np.nan, np.nan)
    r = np.random.default_rng(seed)
    b = r.choice(x, size=(n, len(x)), replace=True).mean(axis=1)
    return tuple(np.percentile(b, [2.5, 97.5]))


VALS = ["own_coop_played", "opp_coop_played", "spr", "opp_spr", "mutual_C", "mutual_D",
        "exploited_opp", "was_exploited", "round1_coop", "last5_coop", "retaliation_rate",
        "forgiveness_rate", "rounds"]

rows = []
for ds, sub in ag.groupby("dataset"):
    sub = sub[sub.paraphrase != "p4"] if ds == "prereg" else sub
    sb = sub.groupby(["sandbox", "opponent_type"])[VALS].mean().reset_index()
    for opp, g in sb.groupby("opponent_type"):
        rec = dict(dataset=ds, scope="all", opponent_type=opp, n_sandboxes=len(g),
                   n_games=int((sub.opponent_type == opp).sum()))
        for v in VALS:
            rec[v] = g[v].mean()
        lo, hi = boot(g["own_coop_played"]); rec["coop_lo"], rec["coop_hi"] = lo, hi
        lo, hi = boot(g["spr"]); rec["spr_lo"], rec["spr_hi"] = lo, hi
        rows.append(rec)
    for col in ["effort", "score_state", "model", "condition"]:
        sb2 = sub.groupby(["sandbox", col, "opponent_type"])[VALS].mean().reset_index()
        for (lvl, opp), g in sb2.groupby([col, "opponent_type"]):
            rec = dict(dataset=ds, scope=f"{col}={lvl}", opponent_type=opp, n_sandboxes=len(g),
                       n_games=int(((sub.opponent_type == opp) & (sub[col] == lvl)).sum()))
            for v in VALS:
                rec[v] = g[v].mean()
            rows.append(rec)
out = pd.DataFrame(rows)
out.to_csv(T / "gt_q2_by_opponent.csv", index=False)
pd.set_option("display.width", 250)
cols = ["opponent_type", "n_sandboxes", "n_games", "own_coop_played", "opp_coop_played", "spr",
        "opp_spr", "mutual_C", "mutual_D", "exploited_opp", "was_exploited", "rounds"]
print("== prereg, all ==")
print(out[(out.dataset == "prereg") & (out.scope == "all")][cols].round(3).to_string(index=False))
for sc in ["effort=off", "effort=high", "score_state=behind", "score_state=ahead",
           "model=deepseek-ai/DeepSeek-V4-Flash-0731", "model=XiaomiMiMo/MiMo-V2.5-Pro"]:
    print(f"== prereg, {sc} ==")
    print(out[(out.dataset == "prereg") & (out.scope == sc)][cols].round(3).to_string(index=False))
