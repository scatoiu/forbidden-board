import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q1c: sandbox/block-paired contrasts for recognition, so the effort and condition
comparisons use the randomisation unit rather than the game."""
import sys; sys.path.insert(0,_REPO+"/paper-analysis/code")
import numpy as np, pandas as pd
from per_common import agent_games, save, short, sign_flip_p

ag=agent_games(); g=ag[ag.classification_predicted.notna()].copy()
g["model_s"]=g.model.map(short); g["say_model"]=(g.classification_predicted=="model")
g["true_llm"]=(g.opponent_type=="LLM")

def disc(s):
    a=s.loc[s.true_llm,"say_model"]; b=s.loc[~s.true_llm,"say_model"]
    if len(a)<10 or len(b)<10: return np.nan
    return a.mean()-b.mean()

# per-sandbox discrimination
rows=[]
for sb,s in g.groupby("sandbox"):
    r=s.iloc[0]
    rows.append(dict(sandbox=sb, block=r.block, model=short(r.model), condition=r.condition,
                     effort=r.effort, score_state=r.score_state, paraphrase=r.paraphrase,
                     n_games=len(s), discrimination=disc(s),
                     accuracy=(s.classification_correct==True).mean(),
                     say_model_rate=s.say_model.mean()))
sbtab=pd.DataFrame(rows); save(sbtab,"per_q1c_discrimination_by_sandbox.csv")

# Contrast A arm: high minus off, behind state, per condition, paired within block
for cond in ["forbidden","hidden","permitted"]:
    hi=sbtab[(sbtab.condition==cond)&(sbtab.effort=="high")&(sbtab.score_state=="behind")&(sbtab.model=="DeepSeek")]
    of=sbtab[(sbtab.condition==cond)&(sbtab.effort=="off")&(sbtab.score_state=="behind")&(sbtab.model=="DeepSeek")]
    m=hi.merge(of,on="block",suffixes=("_hi","_off"))
    if not len(m): continue
    d=(m.discrimination_hi-m.discrimination_off).tolist()
    p,k=sign_flip_p(d)
    print(f"{cond:10s} discrimination high-off (behind): mean {np.mean(d):+.3f}  "
          f"{sum(x>0 for x in d)}/{k} positive  sign-flip p={p:.4f}  "
          f"[off {m.discrimination_off.mean():.3f} -> high {m.discrimination_hi.mean():.3f}]")
# B arm: behind minus ahead at off
print()
for cond in ["forbidden","hidden","permitted"]:
    for mo in ["DeepSeek","MiMo"]:
        b=sbtab[(sbtab.condition==cond)&(sbtab.effort=="off")&(sbtab.score_state=="behind")&(sbtab.model==mo)]
        a=sbtab[(sbtab.condition==cond)&(sbtab.effort=="off")&(sbtab.score_state=="ahead")&(sbtab.model==mo)]
        m=b.merge(a,on="block",suffixes=("_b","_a"))
        if len(m)<3: continue
        d=(m.discrimination_b-m.discrimination_a).tolist(); p,k=sign_flip_p(d)
        print(f"{mo:9s} {cond:10s} discrimination behind-ahead (off): mean {np.mean(d):+.3f}  "
              f"{sum(x>0 for x in d)}/{k}  p={p:.4f}")
