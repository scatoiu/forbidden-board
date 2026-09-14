import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q2b: join the per-trace awareness flags to the decision rows and ask whether
awareness language co-occurs with a different action or with board use, holding
trace length roughly fixed (decile of trace length within cell)."""
import sys; sys.path.insert(0,_REPO+"/paper-analysis/code")
import numpy as np, pandas as pd
from per_common import decisions, save, short, TAB, sign_flip_p

tf=pd.read_parquet(TAB/"per_q2_trace_flags.parquet")
d=decisions(); d=d[d.is_played.astype(bool)].copy()
d["model_s"]=d.model.map(short)
d["game_uid"]=d.game_uid.astype(str)
m=d.merge(tf,on=["sandbox","game_uid","agent","round"],how="inner")
print("decisions joined to a trace:",len(m),"of",len(d))
m["coop"]=(m.action=="C"); m["called"]=m.att_board_calls.fillna(0)>0
m["len_dec"]=m.groupby(["model_s","effort","condition"],observed=True)["trace_chars"]\
              .transform(lambda s: pd.qcut(s.rank(method="first"),10,labels=False))

rows=[]
for (mo,e,c),s in m.groupby(["model_s","effort","condition"]):
    if len(s)<500: continue
    # crude (no length control)
    crude_c=s.loc[s.aware==1,"coop"].mean()-s.loc[s.aware==0,"coop"].mean()
    crude_b=s.loc[s.aware==1,"called"].mean()-s.loc[s.aware==0,"called"].mean()
    # length-stratified: average the within-decile difference
    dc,db=[],[]
    for _,g in s.groupby("len_dec"):
        a=g[g.aware==1]; b=g[g.aware==0]
        if len(a)>=30 and len(b)>=30:
            dc.append(a.coop.mean()-b.coop.mean()); db.append(a.called.mean()-b.called.mean())
    rows.append(dict(model=mo, effort=e, condition=c, n=len(s),
                     share_aware=s.aware.mean(), share_evalframe=s.evalframe.mean(),
                     mean_trace_chars=s.trace_chars.mean(),
                     coop_aware=s.loc[s.aware==1,"coop"].mean(), coop_notaware=s.loc[s.aware==0,"coop"].mean(),
                     crude_diff_coop_pp=100*crude_c, lenadj_diff_coop_pp=100*np.mean(dc) if dc else None,
                     n_deciles=len(dc),
                     crude_diff_boardcall_pp=100*crude_b,
                     lenadj_diff_boardcall_pp=100*np.mean(db) if db else None))
df=pd.DataFrame(rows); save(df,"per_q2_awareness_vs_behaviour.csv")
print(df.round(3).to_string(index=False))

# evalframe version (the explicit "this is a test" phrasing), high effort only
rows=[]
for (mo,e,c),s in m[m.effort=="high"].groupby(["model_s","effort","condition"]):
    dc=[]
    for _,g in s.groupby("len_dec"):
        a=g[g.evalframe==1]; b=g[g.evalframe==0]
        if len(a)>=30 and len(b)>=30: dc.append(a.coop.mean()-b.coop.mean())
    rows.append(dict(model=mo,effort=e,condition=c,n=len(s),share_evalframe=s.evalframe.mean(),
                     coop_evalframe=s.loc[s.evalframe==1,"coop"].mean(),
                     coop_not=s.loc[s.evalframe==0,"coop"].mean(),
                     crude_diff_pp=100*(s.loc[s.evalframe==1,"coop"].mean()-s.loc[s.evalframe==0,"coop"].mean()),
                     lenadj_diff_pp=100*np.mean(dc) if dc else None, n_deciles=len(dc)))
d2=pd.DataFrame(rows); save(d2,"per_q2_evalframe_vs_coop.csv")
print(); print(d2.round(3).to_string(index=False))
