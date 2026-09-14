import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q6b: do agents call the board when behind? Uses the harness's own
`score_gap_at_call` (running ledger INCLUDING the assigned warm-up, coop/players/llm.py::_totals),
logged on every decision, stratified by assigned score_state and round band."""
import sys; sys.path.insert(0,_REPO+"/paper-analysis/code")
import numpy as np, pandas as pd
from per_common import decisions, save, short, wilson, sign_flip_p

d = decisions()
d = d[d.is_played.astype(bool)].copy()
d["model_s"]=d.model.map(short); d["called"]=d.att_board_calls.fillna(0)>0
d["gap"]=d.score_gap_at_call.astype(float)
d["roundband"]=pd.cut(d["round"],[0,5,10,20,100],labels=["1-5","6-10","11-20","21+"])
# within-state deviation of the gap from its cell median: "is this agent doing
# worse than a typical agent in the same arm at the same point in the game?"
key=["model_s","effort","condition","score_state","roundband"]
d["gap_dev"]=d.gap-d.groupby(key,observed=True)["gap"].transform("median")
d["behind_for_stage"]=d.gap_dev<0

rows=[]
for (m,e,c,ss,rb), sub in d.groupby(key,observed=True):
    if len(sub)<300 or sub.called.sum()<20: continue
    a=sub[sub.behind_for_stage]; b=sub[~sub.behind_for_stage]
    if len(a)<100 or len(b)<100: continue
    ka,kb=int(a.called.sum()),int(b.called.sum())
    rows.append(dict(model=m, effort=e, condition=c, score_state=ss, round_band=rb,
                     n_worse=len(a), rate_worse=ka/len(a),
                     n_notworse=len(b), rate_notworse=kb/len(b),
                     diff_pp=100*(ka/len(a)-kb/len(b))))
df=pd.DataFrame(rows); save(df,"per_q6b_call_by_relative_gap.csv")
print(df.round(3).to_string(index=False))

# collapse: paired by (condition, state, round band) within model/effort
rows=[]
for (m,e), sub in df.groupby(["model","effort"]):
    p,k=sign_flip_p(list(sub.diff_pp))
    rows.append(dict(model=m, effort=e, n_strata=len(sub), mean_diff_pp=sub.diff_pp.mean(),
                     n_positive=int((sub.diff_pp>0).sum()), sign_flip_p=p))
d2=pd.DataFrame(rows); save(d2,"per_q6b_call_by_gap_summary.csv")
print(); print(d2.round(4).to_string(index=False))

# assigned state (the manipulation) rather than the realised gap: use rate ahead vs behind
rows=[]
for (m,e,c), sub in d.groupby(["model_s","effort","condition"]):
    if sub.called.sum()<20 or sub.score_state.nunique()<2: continue
    a=sub[sub.score_state=="behind"]; b=sub[sub.score_state=="ahead"]
    rows.append(dict(model=m, effort=e, condition=c,
                     n_behind=len(a), rate_behind=a.called.mean(),
                     n_ahead=len(b), rate_ahead=b.called.mean(),
                     diff_pp=100*(a.called.mean()-b.called.mean())))
d3=pd.DataFrame(rows); save(d3,"per_q6b_call_by_assigned_state_decisionlevel.csv")
print(); print(d3.round(3).to_string(index=False))
