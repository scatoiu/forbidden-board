import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q1: do the LLM seats beat the static strategies inside the same round-robin?

Unit = sandbox. Within a sandbox all 24 seats meet the same field, so a
per-sandbox mean per seat type is matched by construction. Primary statistic is
score per round (robust to aborted games shortening LLM seats); total score per
seat is reported beside it. Sign-flip is Monte-Carlo over sandboxes (2^69 exact
is not enumerable); for the six-block forbidden-behind-off family the exact
2^-5 floor is reported separately.
"""
from __future__ import annotations
import numpy as np, pandas as pd
from pathlib import Path

T = Path(_REPO+"/paper-analysis/tables")
rng = np.random.default_rng(20260913)
TYPES = ["LLM", "TitForTat", "Grudger", "Pavlov", "AlwaysDefect", "Random"]


def signflip(d, n=200000, seed=20260913):
    d = np.asarray([x for x in d if not np.isnan(x)])
    k = len(d)
    obs = d.mean()
    if k == 0:
        return np.nan, np.nan, 0
    if k <= 20:
        signs = np.array(np.meshgrid(*[[1, -1]] * k)).T.reshape(-1, k)
    else:
        signs = np.random.default_rng(seed).choice([1, -1], size=(n, k))
    null = (signs * d).mean(axis=1)
    p = (np.abs(null) >= abs(obs) - 1e-12).mean()
    return obs, max(p, 1 / len(null)), k


s = pd.read_csv(T / "gt_seat_scores.csv")
rows = []
for ds, sub in s.groupby("dataset"):
    sub = sub[sub.paraphrase != "p4"] if ds == "prereg" else sub
    m = (sub.groupby(["sandbox", "sandbox_model", "condition", "effort", "score_state",
                      "paraphrase", "seat_type"])
         [["total_score", "score_per_round", "rounds", "coop", "n_games"]].mean().reset_index())
    m["dataset"] = ds
    rows.append(m)
per_sb = pd.concat(rows, ignore_index=True)
per_sb.to_csv(T / "gt_q1_standings.csv", index=False)

out = []
for ds, sub in per_sb.groupby("dataset"):
    for metric in ["score_per_round", "total_score"]:
        w = sub.pivot_table(index="sandbox", columns="seat_type", values=metric)
        means = w.mean()
        ranks = w.rank(axis=1, ascending=False)
        for t in TYPES:
            out.append(dict(dataset=ds, metric=metric, seat_type=t,
                            mean=means[t], sd_over_sandboxes=w[t].std(),
                            mean_rank=ranks[t].mean(),
                            n_sandboxes=len(w)))
pd.DataFrame(out).to_csv(T / "gt_q1_type_means.csv", index=False)
print(pd.DataFrame(out)[lambda d: d.dataset == "prereg"].to_string(index=False))

# paired LLM - each script type, per sandbox
diffs = []
for ds, sub in per_sb.groupby("dataset"):
    for metric in ["score_per_round", "total_score"]:
        w = sub.pivot_table(index="sandbox", columns="seat_type", values=metric)
        key = sub.drop_duplicates("sandbox").set_index("sandbox")
        for t in TYPES[1:]:
            d = (w["LLM"] - w[t])
            obs, p, k = signflip(d.values)
            diffs.append(dict(dataset=ds, metric=metric, contrast=f"LLM-{t}", scope="all",
                              mean_diff=obs, p_signflip=p, k=k, n_pos=int((d > 0).sum())))
        # breakdowns for LLM - TitForTat
        d = (w["LLM"] - w["TitForTat"])
        for col in ["condition", "effort", "score_state", "sandbox_model"]:
            for lvl, idx in key.groupby(col).groups.items():
                dd = d.reindex(idx)
                obs, p, k = signflip(dd.values)
                diffs.append(dict(dataset=ds, metric=metric, contrast="LLM-TitForTat",
                                  scope=f"{col}={lvl}", mean_diff=obs, p_signflip=p, k=k,
                                  n_pos=int((dd > 0).sum())))
D = pd.DataFrame(diffs)
D.to_csv(T / "gt_q1_llm_vs_scripts.csv", index=False)
print()
print(D[(D.dataset == "prereg") & (D.metric == "score_per_round")].to_string(index=False))
