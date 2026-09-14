import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q1b: separate response bias from discrimination in the script/model question."""
import sys; sys.path.insert(0,_REPO+"/paper-analysis/code")
import numpy as np, pandas as pd
from per_common import agent_games, wilson, save, short

ag = agent_games()
g = ag[ag.classification_predicted.notna()].copy()
g["model_s"] = g.model.map(short)
g["say_model"] = (g.classification_predicted == "model")
g["true_llm"] = (g.opponent_type == "LLM")

rows=[]
for (m,e,c), sub in g.groupby(["model_s","effort","condition"]):
    hit = sub.loc[sub.true_llm,"say_model"]
    fa  = sub.loc[~sub.true_llm,"say_model"]
    if len(hit)<30 or len(fa)<30: continue
    h, f = hit.mean(), fa.mean()
    rows.append(dict(model=m, effort=e, condition=c,
                     n_vs_llm=len(hit), n_vs_script=len(fa),
                     say_model_rate_overall=sub.say_model.mean(),
                     hit_rate_llm=h, false_alarm_script=f,
                     discrimination_h_minus_f=h-f,
                     accuracy=(sub.classification_correct==True).mean()))
df=pd.DataFrame(rows)
save(df,"per_q1b_signal_detection.csv")
print(df.round(3).to_string(index=False))

# pooled over condition
rows=[]
for (m,e), sub in g.groupby(["model_s","effort"]):
    hit = sub.loc[sub.true_llm,"say_model"]; fa = sub.loc[~sub.true_llm,"say_model"]
    h,f = hit.mean(), fa.mean()
    lo1,hi1=wilson(int(hit.sum()),len(hit)); lo2,hi2=wilson(int(fa.sum()),len(fa))
    rows.append(dict(model=m, effort=e, n_vs_llm=len(hit), n_vs_script=len(fa),
                     hit_rate_llm=h, hit_lo=lo1, hit_hi=hi1,
                     false_alarm_script=f, fa_lo=lo2, fa_hi=hi2,
                     discrimination=h-f, say_model_rate=sub.say_model.mean()))
df2=pd.DataFrame(rows); save(df2,"per_q1b_signal_detection_pooled.csv")
print(); print(df2.round(3).to_string(index=False))

# unscored rate (predicted is None)
un = ag[ag.classification_correct.isna() & ag.game_observed.astype(bool)]
print("\nagent-games with no scorable classification:", len(un), "of", int(ag.game_observed.astype(bool).sum()))

# name-correct: which scripts get named, and named right
nm = ag[ag.classification_named_script.notna()].copy()
nm["model_s"]=nm.model.map(short)
rows=[]
for (ot,), sub in ag[ag.opponent_type!="LLM"].groupby(["opponent_type"]):
    named = sub.classification_named_script.notna().sum()
    ncorr = (sub.classification_name_correct==True).sum()
    rows.append(dict(opponent_type=ot, n_games=len(sub), n_named_any=int(named),
                     named_any_rate=named/len(sub),
                     n_name_correct=int(ncorr),
                     name_correct_of_named=(ncorr/named if named else np.nan),
                     name_correct_of_all=ncorr/len(sub)))
dn=pd.DataFrame(rows); save(dn,"per_q1b_script_naming.csv")
print(); print(dn.round(3).to_string(index=False))
print("\nnamed-script vocabulary:")
print(ag.classification_named_script.value_counts().to_string())
