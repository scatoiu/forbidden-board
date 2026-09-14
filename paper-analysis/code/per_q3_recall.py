import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q3: knowing the rule vs following it. Recall code x attempted board use,
per model and effort, with sandbox-level spread."""
import sys; sys.path.insert(0,_REPO+"/paper-analysis/code")
import numpy as np, pandas as pd
from per_common import FROZEN, save, wilson, short, sign_flip_p

rc = pd.read_csv(FROZEN/"recall_coded.csv")
print("recall_coded rows:", len(rc), "| conditions:", rc.condition.unique())
rc = rc[rc.paraphrase != "p4"]
rc["model_s"] = rc.model.map(short)
rc["used"] = rc.attempted_use.fillna(0) > 0
print(rc.groupby(["model_s","effort"]).size().to_string())

rows=[]
for (m,e,code), sub in rc.groupby(["model_s","effort","recall_code"]):
    k=int(sub.used.sum()); n=len(sub); lo,hi=wilson(k,n)
    rows.append(dict(model=m, effort=e, recall_code=code, n_games=n,
                     share_of_cell=np.nan, n_attempted_use=k,
                     attempted_use_rate=k/n, ci_lo=lo, ci_hi=hi))
df=pd.DataFrame(rows)
tot=rc.groupby(["model_s","effort"]).size().rename("cell_n").reset_index()
df=df.merge(tot,left_on=["model","effort"],right_on=["model_s","effort"]).drop(columns=["model_s"])
df["share_of_cell"]=df.n_games/df.cell_n
save(df.sort_values(["model","effort","recall_code"]),"per_q3_recall_x_use.csv")
print(df.round(3).to_string(index=False))

# collapse to "names the prohibition at all" (names_prohibition or names_while_denying)
rc["names_any"] = rc.recall_code.isin(["names_prohibition","names_while_denying"])
rows=[]
for (m,e), sub in rc.groupby(["model_s","effort"]):
    for flag in (True, False):
        s=sub[sub.names_any==flag]
        if not len(s): continue
        k=int(s.used.sum()); n=len(s); lo,hi=wilson(k,n)
        rows.append(dict(model=m, effort=e, names_prohibition=flag, n_games=n,
                         share_of_cell=n/len(sub), attempted_use_rate=k/n, ci_lo=lo, ci_hi=hi))
    a=sub[sub.names_any]; b=sub[~sub.names_any]
    if len(a) and len(b):
        rows.append(dict(model=m, effort=e, names_prohibition="DIFF(names-not)", n_games=len(sub),
                         share_of_cell=np.nan,
                         attempted_use_rate=a.used.mean()-b.used.mean(), ci_lo=np.nan, ci_hi=np.nan))
d2=pd.DataFrame(rows); save(d2,"per_q3_names_any_x_use.csv")
print(); print(d2.round(3).to_string(index=False))

# sandbox-level: within each forbidden sandbox, use rate among recallers vs non-recallers
rows=[]
for (m,e), sub in rc.groupby(["model_s","effort"]):
    diffs=[]
    for sb, s in sub.groupby("sandbox"):
        a=s[s.names_any]; b=s[~s.names_any]
        if len(a)>=5 and len(b)>=5: diffs.append(a.used.mean()-b.used.mean())
    if len(diffs)>=4:
        p,k=sign_flip_p(diffs)
        rows.append(dict(model=m, effort=e, n_sandboxes=len(diffs),
                         mean_diff_use_recaller_minus_not=float(np.mean(diffs)),
                         median=float(np.median(diffs)),
                         n_positive=int(sum(d>0 for d in diffs)), sign_flip_p=p))
d3=pd.DataFrame(rows); save(d3,"per_q3_recall_use_sandbox_paired.csv")
print(); print(d3.round(4).to_string(index=False))

# joint share of all forbidden games that both name the prohibition and attempt use
rows=[]
for (m,e), sub in rc.groupby(["model_s","effort"]):
    rows.append(dict(model=m, effort=e, n_games=len(sub),
                     share_names_and_uses=(sub.names_any & sub.used).mean(),
                     share_names_and_abstains=(sub.names_any & ~sub.used).mean(),
                     share_notnames_and_uses=(~sub.names_any & sub.used).mean(),
                     share_notnames_and_abstains=(~sub.names_any & ~sub.used).mean()))
d4=pd.DataFrame(rows); save(d4,"per_q3_joint_recall_use.csv")
print(); print(d4.round(3).to_string(index=False))
