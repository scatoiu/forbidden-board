import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q8: is hidden-condition cooperation genuinely lower, or a censoring artefact
of the 768-token answer cap? Uses T10_cap_replication (same base sandboxes at
cap 768 and 4096) plus abort rates from the compact tables."""
import sys; sys.path.insert(0,_REPO+"/paper-analysis/code")
import numpy as np, pandas as pd
from per_common import FROZEN, save, agent_games, short, sign_flip_p

t10 = pd.read_csv(FROZEN/"T10_cap_replication.csv")
t10["d_coop"]=t10.coop_completed_4096-t10.coop_completed_768
t10["d_abort"]=t10.abort_rate_4096-t10.abort_rate_768
print(t10[["base_sandbox","condition","score_state","paraphrase","abort_rate_768","abort_rate_4096",
           "coop_completed_768","coop_completed_4096","d_coop"]].round(3).to_string(index=False))
save(t10,"per_q8_cap_replication_full.csv")

rows=[]
for (c,), sub in t10.groupby(["condition"]):
    p,k=sign_flip_p(list(sub.d_coop))
    rows.append(dict(condition=c, n_sandboxes=len(sub),
                     mean_abort_768=sub.abort_rate_768.mean(), mean_abort_4096=sub.abort_rate_4096.mean(),
                     mean_coop_768=sub.coop_completed_768.mean(), mean_coop_4096=sub.coop_completed_4096.mean(),
                     mean_d_coop=sub.d_coop.mean(), n_positive=int((sub.d_coop>0).sum()), sign_flip_p=p))
d1=pd.DataFrame(rows); save(d1,"per_q8_cap_by_condition.csv")
print(); print(d1.round(4).to_string(index=False))

# hidden minus permitted, at each cap, on the SAME base sandboxes (paired by paraphrase x state)
w = t10.pivot_table(index=["model","paraphrase","score_state"], columns="condition",
                    values=["coop_completed_768","coop_completed_4096","abort_rate_768","abort_rate_4096"])
w.columns=[f"{a}__{b}" for a,b in w.columns]
w=w.reset_index()
w["hid_minus_perm_768"]=w["coop_completed_768__hidden"]-w["coop_completed_768__permitted"]
w["hid_minus_perm_4096"]=w["coop_completed_4096__hidden"]-w["coop_completed_4096__permitted"]
save(w,"per_q8_hidden_minus_permitted_by_cap.csv")
print(); print(w[["paraphrase","score_state","abort_rate_768__hidden","abort_rate_4096__hidden",
                  "hid_minus_perm_768","hid_minus_perm_4096"]].round(3).to_string(index=False))
p1,_=sign_flip_p(list(w.hid_minus_perm_768.dropna())); p2,_=sign_flip_p(list(w.hid_minus_perm_4096.dropna()))
print(f"\nhidden-minus-permitted coop, cap 768:  mean {w.hid_minus_perm_768.mean():+.3f}  "
      f"{int((w.hid_minus_perm_768<0).sum())}/{w.hid_minus_perm_768.notna().sum()} negative  sign-flip p={p1:.4f}")
print(f"hidden-minus-permitted coop, cap 4096: mean {w.hid_minus_perm_4096.mean():+.3f}  "
      f"{int((w.hid_minus_perm_4096<0).sum())}/{w.hid_minus_perm_4096.notna().sum()} negative  sign-flip p={p2:.4f}")

# abort rate by condition/effort/state in the prereg set (compact tables)
ag = agent_games()
ag["model_s"]=ag.model.map(short)
rows=[]
for (m,e,c,ss), sub in ag.groupby(["model_s","effort","condition","score_state"]):
    rows.append(dict(model=m, effort=e, condition=c, score_state=ss, n_agent_games=len(sub),
                     abort_rate=sub.aborted.astype(bool).mean(),
                     unobserved_rate=sub.game_unobserved.astype(bool).mean(),
                     coop_completed=sub.loc[sub.game_observed.astype(bool),"own_coop_played"].astype(float).mean()))
d3=pd.DataFrame(rows); save(d3,"per_q8_abort_by_cell.csv")
print(); print(d3.round(3).to_string(index=False))
