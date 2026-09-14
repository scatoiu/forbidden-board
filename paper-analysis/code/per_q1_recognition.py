import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q1: recognition of opponent type, by opponent type / effort / model / condition,
and whether a correct classification goes with different play in that game."""
import sys
sys.path.insert(0, _REPO+"/paper-analysis/code")
import numpy as np, pandas as pd
from per_common import agent_games, wilson, save, short

ag = agent_games()
print("prereg agent-games:", len(ag))
g = ag[ag.classification_correct.notna()].copy()
print("with a classification answer:", len(g))
g["model_s"] = g.model.map(short)

# --- A. by opponent type (pooled over conditions/efforts) -------------------
rows = []
for (ot,), sub in g.groupby(["opponent_type"]):
    k = int(sub.classification_correct.sum()); n = len(sub)
    lo, hi = wilson(k, n)
    rows.append(dict(cut="opponent_type", level=ot, n_games=n, n_correct=k,
                     accuracy=k/n, ci_lo=lo, ci_hi=hi))
# --- B. opponent type x model x effort --------------------------------------
rows2 = []
for (ot, m, e), sub in g.groupby(["opponent_type", "model_s", "effort"]):
    k = int(sub.classification_correct.sum()); n = len(sub)
    lo, hi = wilson(k, n)
    rows2.append(dict(opponent_type=ot, model=m, effort=e, n_games=n, n_correct=k,
                      accuracy=k/n, ci_lo=lo, ci_hi=hi))
# --- C. opponent type x condition ------------------------------------------
rows3 = []
for (ot, c), sub in g.groupby(["opponent_type", "condition"]):
    k = int(sub.classification_correct.sum()); n = len(sub)
    lo, hi = wilson(k, n)
    rows3.append(dict(opponent_type=ot, condition=c, n_games=n, n_correct=k,
                      accuracy=k/n, ci_lo=lo, ci_hi=hi))

save(pd.DataFrame(rows).sort_values("accuracy"), "per_q1_recognition_by_opponent.csv")
save(pd.DataFrame(rows2).sort_values(["opponent_type","model","effort"]),
     "per_q1_recognition_by_opp_model_effort.csv")
save(pd.DataFrame(rows3).sort_values(["opponent_type","condition"]),
     "per_q1_recognition_by_opp_condition.csv")

# What do they predict?  confusion: predicted label distribution by true type
conf = pd.crosstab(g.opponent_type, g.classification_predicted, normalize="index")
conf.to_csv(_REPO+"/paper-analysis/tables/per_q1_confusion.csv")
print("\n[confusion: rows=true opponent_type, cols=predicted]")
print((conf*100).round(1).to_string())
print("\ncounts by true type:")
print(g.opponent_type.value_counts().to_string())
print("\npredicted label vocabulary:")
print(g.classification_predicted.value_counts().to_string())

# --- D. does correct classification go with different play? -----------------
# within opponent_type (and model), completed games only, exploratory (game-level)
played = g[(g.n_played.fillna(0) > 0) & (~g.game_unobserved.astype(bool))].copy()
rows4 = []
for (ot, m), sub in played.groupby(["opponent_type", "model_s"]):
    for col in ["own_coop_played", "score", "round1_coop", "last5_coop", "retaliation_rate"]:
        a = sub.loc[sub.classification_correct == True, col].astype(float).dropna()
        b = sub.loc[sub.classification_correct == False, col].astype(float).dropna()
        if len(a) < 20 or len(b) < 20:
            continue
        rows4.append(dict(opponent_type=ot, model=m, metric=col,
                          n_correct=len(a), mean_correct=a.mean(),
                          n_wrong=len(b), mean_wrong=b.mean(),
                          diff=a.mean()-b.mean()))
save(pd.DataFrame(rows4), "per_q1_play_by_classification.csv")

# sandbox-level paired version for the headline metric (own coop) vs scripts
rows5 = []
for (ot, m), sub in played.groupby(["opponent_type", "model_s"]):
    per_sb = []
    for sb, s2 in sub.groupby("sandbox"):
        a = s2.loc[s2.classification_correct == True, "own_coop_played"].astype(float).dropna()
        b = s2.loc[s2.classification_correct == False, "own_coop_played"].astype(float).dropna()
        if len(a) >= 3 and len(b) >= 3:
            per_sb.append(a.mean() - b.mean())
    if len(per_sb) >= 5:
        arr = np.array(per_sb)
        rows5.append(dict(opponent_type=ot, model=m, n_sandboxes=len(arr),
                          mean_within_sandbox_diff=arr.mean(),
                          median=np.median(arr),
                          n_positive=int((arr > 0).sum())))
save(pd.DataFrame(rows5), "per_q1_coop_diff_by_sandbox.csv")
