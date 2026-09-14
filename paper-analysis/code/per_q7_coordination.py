import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q7: coordination. Do posts carry an action directive, and is a directive
followed by a matching action from an agent who read the board?
Labels are drawn per game from a fixed pool of six letter pairs per sandbox and no
letter ever carries both roles inside a sandbox (verified), so a letter named in a
post is interpretable sandbox-wide."""
import sys, re, json
sys.path.insert(0,_REPO+"/paper-analysis/code")
from pathlib import Path
import numpy as np, pandas as pd
from per_common import FROZEN, save, short, decisions, sign_flip_p, wilson

# 1. per-sandbox letter -> role map, from the raw logs
ROOTS=[Path(_REPO+"/runs")/r for r in ("v3","v3b","v3-mimo")]
role={}
for root in ROOTS:
    for mv in sorted(root.glob("*/moves.jsonl")):
        sb=mv.parent.name
        if sb.endswith("-repair"): continue
        seen={}
        with open(mv) as fh:
            for line in fh:
                if '"label_map"' not in line: continue
                r=json.loads(line)
                lm=r.get("label_map")
                if not lm: continue
                seen[lm["C"]]="C"; seen[lm["D"]]="D"
                if len(seen)>=12: break
        role[sb]=seen
print("sandboxes with a letter->role map:", len(role),
      "| mean distinct letters:", np.mean([len(v) for v in role.values()]).round(1))

p=pd.read_csv(FROZEN/"posts_coded.csv")
p=p[(p.dataset=="prereg")&(p.paraphrase!="p4")].copy()
p["text"]=p.text.fillna("").astype(str); p["model_s"]=p.model.map(short)

DIRECT=re.compile(r"\b(let'?s|we should|we can|i propose|propose|suggest|if you|you should|"
                  r"i'?ll match|i will match|both (pick|play|choose)|mutual)\b",re.I)
PICK=re.compile(r"\b(?:pick|play|choose|choosing|picking|go with|commit to|select)\s+([A-Z])\b")
def advocated(row):
    rl=role.get(row.sandbox,{})
    if not DIRECT.search(row.text): return None
    for mo in PICK.finditer(row.text):
        r=rl.get(mo.group(1))
        if r: return r
    return None
p["advocates"]=p.apply(advocated,axis=1)
sub=p[p.advocates.notna()]
print("\nposts carrying an interpretable action directive:",len(sub),"of",len(p))
rows=[]
for (m,e,c),s in p.groupby(["model_s","effort","condition"]):
    a=s[s.advocates.notna()]
    rows.append(dict(model=m,effort=e,condition=c,n_posts=len(s),
                     n_directive_interpretable=len(a),
                     share=len(a)/len(s),
                     share_advocating_C=(a.advocates=="C").mean() if len(a) else np.nan,
                     n_advocating_C=int((a.advocates=="C").sum()),
                     n_advocating_D=int((a.advocates=="D").sum())))
d1=pd.DataFrame(rows); save(d1,"per_q7_directive_posts.csv")
print(d1.round(3).to_string(index=False))

# 2. climate test: within a sandbox and round, does the share of C-advocating
#    directives posted in the preceding 3 rounds predict a READER's next action
#    more than a NON-reader's?  Exploratory, decision level.
d=decisions(); d=d[d.is_played.astype(bool)].copy()
d["model_s"]=d.model.map(short); d["read"]=d.att_read_calls.fillna(0)>0
d["coop"]=(d.action=="C")
cl=(sub.assign(isC=(sub.advocates=="C").astype(float))
      .groupby(["sandbox","round"])
      .agg(n_dir=("isC","size"), share_C=("isC","mean")).reset_index())
# rolling window of the 3 previous rounds
out=[]
for sb,s in cl.groupby("sandbox"):
    s=s.sort_values("round").set_index("round").reindex(range(1,31)).fillna({"n_dir":0})
    s["cum_n"]=s.n_dir.rolling(3,min_periods=1).sum().shift(1)
    s["cum_C"]=(s.n_dir*s.share_C.fillna(0)).rolling(3,min_periods=1).sum().shift(1)
    s["prior_share_C"]=np.where(s.cum_n>0, s.cum_C/s.cum_n, np.nan)
    out.append(s.assign(sandbox=sb).reset_index().rename(columns={"index":"round"}))
cl2=pd.concat(out)[["sandbox","round","cum_n","prior_share_C"]]
d=d.merge(cl2,on=["sandbox","round"],how="left")
dd=d[(d.cum_n.fillna(0)>=2)&d.prior_share_C.notna()]
print("\ndecisions with >=2 interpretable directives in the previous 3 rounds:",len(dd))
rows=[]
for (m,e,c),s in dd.groupby(["model_s","effort","condition"]):
    for rd_ in (True,False):
        t=s[s.read==rd_]
        if len(t)<100: continue
        hi=t[t.prior_share_C>=0.6]; lo=t[t.prior_share_C<=0.4]
        if len(hi)<50 or len(lo)<50: continue
        rows.append(dict(model=m,effort=e,condition=c,reader=rd_,
                         n_hiC=len(hi),coop_when_directives_mostly_C=hi.coop.mean(),
                         n_loC=len(lo),coop_when_directives_mostly_D=lo.coop.mean(),
                         diff_pp=100*(hi.coop.mean()-lo.coop.mean())))
d2=pd.DataFrame(rows); save(d2,"per_q7_directive_climate.csv")
print(); print(d2.round(3).to_string(index=False) if len(d2) else "(no cell had enough directives on both sides)")

# 3. do posts address another agent (2nd person) and name a specific opponent?
p["second_person"]=p.text.str.contains(r"\byou\b|\byour\b|\bwe\b|\blet'?s\b",case=False)
rows=[]
for (m,e,c),s in p.groupby(["model_s","effort","condition"]):
    rows.append(dict(model=m,effort=e,condition=c,n_posts=len(s),
                     share_second_person=s.second_person.mean()))
d3=pd.DataFrame(rows); save(d3,"per_q7_second_person.csv")
print(); print(d3.round(3).to_string(index=False))
