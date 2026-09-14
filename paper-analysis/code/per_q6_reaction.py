import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q6: reaction to the board. (a) within-tournament before/after a notes_read,
(b) score_gap_at_call at the moment of a board call vs at non-call decisions."""
import sys; sys.path.insert(0,_REPO+"/paper-analysis/code")
import numpy as np, pandas as pd
from per_common import decisions, save, short, sign_flip_p, wilson

d = decisions()
d = d[d.is_played.astype(bool)].copy()
d["model_s"]=d.model.map(short)
d = d.sort_values(["agent_game_uid","round"])
d["read"] = d.att_read_calls.fillna(0) > 0
d["coop"] = (d.action == "C")
g = d.groupby("agent_game_uid", sort=False)
d["prev_coop"] = g["coop"].shift(1)
d["prev_read"] = g["read"].shift(1)
d["next_coop"] = g["coop"].shift(-1)

# (a) exploratory: cooperation on the decision that read, vs the decision before it
rows=[]
for (m,e,c), sub in d.groupby(["model_s","effort","condition"]):
    s = sub[sub.read & sub.prev_coop.notna()]
    if len(s) < 50: continue
    rows.append(dict(model=m, effort=e, condition=c, n_read_decisions=len(s),
                     coop_on_read_decision=s.coop.mean(),
                     coop_on_previous_decision=s.prev_coop.astype(float).mean(),
                     diff=s.coop.mean()-s.prev_coop.astype(float).mean()))
    s2 = sub[(~sub.read) & sub.prev_coop.notna()]
    rows[-1]["n_noread_decisions"]=len(s2)
    rows[-1]["coop_on_noread_decision"]=s2.coop.mean()
    rows[-1]["coop_prev_of_noread"]=s2.prev_coop.astype(float).mean()
    rows[-1]["diff_noread"]=s2.coop.mean()-s2.prev_coop.astype(float).mean()
    rows[-1]["dd"]=rows[-1]["diff"]-rows[-1]["diff_noread"]
df=pd.DataFrame(rows); save(df,"per_q6_before_after_read.csv")
print(df.round(3).to_string(index=False))

# sandbox-paired version of the difference-in-differences
rows=[]
for (m,e,c), sub in d.groupby(["model_s","effort","condition"]):
    dds=[]
    for sb,s in sub.groupby("sandbox"):
        a=s[s.read & s.prev_coop.notna()]; b=s[(~s.read)&s.prev_coop.notna()]
        if len(a)>=30 and len(b)>=30:
            dds.append((a.coop.mean()-a.prev_coop.astype(float).mean())
                       -(b.coop.mean()-b.prev_coop.astype(float).mean()))
    if len(dds)>=4:
        p,k=sign_flip_p(dds)
        rows.append(dict(model=m, effort=e, condition=c, n_sandboxes=len(dds),
                         mean_dd=float(np.mean(dds)), median_dd=float(np.median(dds)),
                         n_positive=int(sum(x>0 for x in dds)), sign_flip_p=p))
d2=pd.DataFrame(rows); save(d2,"per_q6_read_dd_sandbox.csv")
print(); print(d2.round(4).to_string(index=False))

# (b) score_gap_at_call: gap at board-call decisions vs at all decisions
print("\nscore_gap_at_call non-null:", d.score_gap_at_call.notna().sum(), "of", len(d))
rows=[]
for (m,e,c), sub in d.groupby(["model_s","effort","condition"]):
    call = sub[sub.att_board_calls.fillna(0)>0]
    nocall = sub[sub.att_board_calls.fillna(0)==0]
    if len(call)<50: continue
    rows.append(dict(model=m, effort=e, condition=c,
                     n_call=len(call), n_nocall=len(nocall),
                     mean_gap_at_call=call.score_gap_at_call.astype(float).mean(),
                     median_gap_at_call=call.score_gap_at_call.astype(float).median(),
                     share_behind_at_call=(call.score_gap_at_call.astype(float)<0).mean(),
                     n_gap_obs_call=int(call.score_gap_at_call.notna().sum())))
d3=pd.DataFrame(rows); save(d3,"per_q6_score_gap_at_call.csv")
print(); print(d3.round(3).to_string(index=False))

# board-call rate as a function of the running score gap at that decision,
# computed from the played history so it exists for call and no-call alike
d["cum_own"]=g["payoff"].cumsum()-d["payoff"].fillna(0)
opp_pay = d.apply(lambda r: np.nan, axis=1)  # placeholder; compute opp payoff from actions
PAY={("C","C"):(3,3),("C","D"):(0,5),("D","C"):(5,0),("D","D"):(1,1)}
oa=d.opponent_action.astype(str); ac=d.action.astype(str)
d["opp_payoff"]=[PAY.get((a,o),(np.nan,np.nan))[1] for a,o in zip(ac,oa)]
d["cum_opp"]=d.groupby("agent_game_uid",sort=False)["opp_payoff"].cumsum()-d["opp_payoff"].fillna(0)
d["gap_before"]=d["cum_own"]-d["cum_opp"]
d["called"]=d.att_board_calls.fillna(0)>0
rows=[]
bins=[-1e9,-10,-4,-0.5,0.5,4,10,1e9]
labs=["<=-10","-9..-4","-3..-1","0","1..3","4..9",">=10"]
d["gapbin"]=pd.cut(d.gap_before,bins=bins,labels=labs)
for (m,e,c), sub in d.groupby(["model_s","effort","condition"]):
    if sub.called.sum()<50: continue
    for gb,s in sub.groupby("gapbin",observed=True):
        if len(s)<100: continue
        k=int(s.called.sum()); lo,hi=wilson(k,len(s))
        rows.append(dict(model=m, effort=e, condition=c, gap_bin=str(gb), n=len(s),
                         board_call_rate=k/len(s), ci_lo=lo, ci_hi=hi,
                         mean_round=s["round"].mean()))
d4=pd.DataFrame(rows); save(d4,"per_q6_callrate_by_gap.csv")
print(); print(d4.round(3).to_string(index=False))
