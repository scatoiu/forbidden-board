import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q3: who defects first, Axelrod's four properties, and defection vs the score gap.

Unit = sandbox for every reported mean (per-sandbox mean of the agent-game
statistic, then mean over sandboxes). Game-level rates are printed only as the
denominator. The score-gap analysis uses `score_gap_at_call` (own - opp,
INCLUDING the assigned +-10 warm-up offset); `within_gap` subtracts each
agent-game's round-1 gap so the two assigned arms are comparable.
"""
from __future__ import annotations
import numpy as np, pandas as pd
from pathlib import Path

D = Path(_REPO+"/paper-analysis/data")
T = Path(_REPO+"/paper-analysis/tables")
ag = pd.read_parquet(D / "agent_games.parquet")
ag = ag[ag.game_observed & (ag.n_played > 0)].copy()
ag["nice"] = ag.first_defector.isin(["opponent", "none"])          # never first to defect
ag["defected_first"] = ag.first_defector.isin(["llm", "both"])
V = ["nice", "defected_first", "round1_coop", "retaliation_rate", "forgiveness_rate",
     "first_defection_round", "llm_first_defection_round", "own_coop_played"]

rows = []
for ds, sub in ag.groupby("dataset"):
    sub = sub[sub.paraphrase != "p4"] if ds == "prereg" else sub
    for scope, keys in [("all", []), ("opponent_type", ["opponent_type"]),
                        ("effort", ["effort"]), ("score_state", ["score_state"]),
                        ("model", ["model"]), ("condition", ["condition"]),
                        ("opp_x_effort", ["opponent_type", "effort"])]:
        sb = sub.groupby(["sandbox"] + keys)[V].mean().reset_index()
        fd = (sub.groupby(["sandbox"] + keys)["first_defector"]
              .value_counts(normalize=True).unstack(fill_value=0).reset_index())
        sb = sb.merge(fd, on=["sandbox"] + keys, how="left")
        grp = sb.groupby(keys) if keys else [((), sb)]
        for k, g in (grp if keys else grp):
            lab = "all" if not keys else "|".join(f"{c}={v}" for c, v in
                                                  zip(keys, (k if isinstance(k, tuple) else (k,))))
            rec = dict(dataset=ds, scope=scope, level=lab, n_sandboxes=len(g))
            for v in V + ["llm", "opponent", "both", "none"]:
                rec[v] = g[v].mean() if v in g else np.nan
            rows.append(rec)
out = pd.DataFrame(rows)
out.to_csv(T / "gt_q3_dynamics.csv", index=False)
pd.set_option("display.width", 250)
C = ["level", "n_sandboxes", "llm", "opponent", "both", "none", "round1_coop",
     "llm_first_defection_round", "retaliation_rate", "forgiveness_rate", "nice"]
for sc in ["all", "opponent_type", "effort", "score_state", "model", "condition"]:
    print(f"== prereg {sc} ==")
    print(out[(out.dataset == "prereg") & (out.scope == sc)][C].round(3).to_string(index=False))

# ---- defection vs score gap ----
dec = pd.read_parquet(D / "decisions.parquet",
                      columns=["dataset", "sandbox", "paraphrase", "model", "condition", "effort",
                               "score_state", "opponent_type", "agent_game_uid", "round",
                               "action", "is_played", "score_gap_at_call"])
dec = dec[dec.is_played & dec.action.notna()].copy()
r1 = (dec[dec["round"] == 1].set_index("agent_game_uid")["score_gap_at_call"])
dec["start_gap"] = dec.agent_game_uid.map(r1)
dec["within_gap"] = dec.score_gap_at_call - dec.start_gap
dec["D"] = (dec.action == "D").astype(float)
bins = [-1e9, -20, -10, -5, -0.5, 0.5, 5, 10, 20, 1e9]
labs = ["<=-20", "-20..-10", "-10..-5", "-5..0", "0", "0..5", "5..10", "10..20", ">20"]
dec["gap_bin"] = pd.cut(dec.score_gap_at_call, bins, labels=labs)
dec["wgap_bin"] = pd.cut(dec.within_gap, bins, labels=labs)
g = []
for ds, sub in dec.groupby("dataset"):
    sub = sub[sub.paraphrase != "p4"] if ds == "prereg" else sub
    for var, col in [("score_gap_at_call", "gap_bin"), ("within_gap", "wgap_bin")]:
        for state in ["all"] + sorted(sub.score_state.unique()):
            s2 = sub if state == "all" else sub[sub.score_state == state]
            sb = s2.groupby(["sandbox", col], observed=True)["D"].mean().reset_index()
            n = s2.groupby(col, observed=True)["D"].size()
            for b, gg in sb.groupby(col, observed=True):
                g.append(dict(dataset=ds, gap_var=var, score_state=state, bin=b,
                              p_defect=gg["D"].mean(), n_sandboxes=len(gg),
                              n_decisions=int(n.get(b, 0))))
gap = pd.DataFrame(g)
gap.to_csv(T / "gt_q3_gap.csv", index=False)
print("== prereg P(defect) by within-game score gap (sandbox-mean) ==")
print(gap[(gap.dataset == "prereg") & (gap.gap_var == "within_gap")]
      .pivot_table(index="bin", columns="score_state", values="p_defect", observed=True).round(3))
print(gap[(gap.dataset == "prereg") & (gap.gap_var == "within_gap") & (gap.score_state == "all")]
      [["bin", "p_defect", "n_decisions"]].round(3).to_string(index=False))

# paired per-sandbox behind-vs-ahead within-game gap contrast, rounds>=3
sub = dec[(dec.dataset == "prereg") & (dec.paraphrase != "p4") & (dec["round"] >= 3)]
piv = (sub.assign(side=np.where(sub.within_gap < 0, "wg_neg",
                                np.where(sub.within_gap > 0, "wg_pos", "wg_zero")))
       .groupby(["sandbox", "side"])["D"].mean().unstack())
d = (piv["wg_neg"] - piv["wg_pos"]).dropna()
rng = np.random.default_rng(11)
null = (rng.choice([1, -1], size=(200000, len(d))) * d.values).mean(axis=1)
p = max((np.abs(null) >= abs(d.mean())).mean(), 1 / len(null))
print(f"\nP(D|behind within game) - P(D|ahead within game), rounds>=3, per sandbox: "
      f"{d.mean():+.4f}, {int((d>0).sum())}/{len(d)} positive, sign-flip p={p:.5f}")
pd.DataFrame(dict(sandbox=d.index, diff=d.values)).to_csv(T / "gt_q3_gap_paired.csv", index=False)
