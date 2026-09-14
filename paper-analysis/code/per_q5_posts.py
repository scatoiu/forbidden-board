import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q5: what the posts are. Category by condition/model/effort/score_state,
read-before-post rates, and verbatim examples."""
import sys; sys.path.insert(0,_REPO+"/paper-analysis/code")
import numpy as np, pandas as pd
from per_common import FROZEN, save, wilson, short, decisions

p = pd.read_csv(FROZEN/"posts_coded.csv")
print("posts rows:", len(p))
p = p[(p.dataset=="prereg") & (p.paraphrase!="p4")]
print("prereg posts:", len(p), "| from_final_attempt:", p.from_final_attempt.value_counts().to_dict())
p["model_s"] = p.model.map(short)
p["text"] = p.text.fillna("").astype(str)
p["chars"] = p.text.str.len()

rows=[]
for (m,e,c), sub in p.groupby(["model_s","effort","condition"]):
    n=len(sub); r=dict(model=m, effort=e, condition=c, n_posts=n,
                       n_games_with_posts=sub.game_uid.nunique(), mean_chars=sub.chars.mean())
    for cat in ["directive","opponent_info","identity","other"]:
        k=int((sub.category==cat).sum()); lo,hi=wilson(k,n)
        r[f"share_{cat}"]=k/n; r[f"{cat}_lo"]=lo; r[f"{cat}_hi"]=hi
    rows.append(r)
df=pd.DataFrame(rows); save(df.sort_values(["model","condition","effort"]),"per_q5_post_categories.csv")
print(df[["model","effort","condition","n_posts","n_games_with_posts","mean_chars",
          "share_directive","share_opponent_info","share_other"]].round(3).to_string(index=False))

# score state
rows=[]
for (m,c,ss), sub in p.groupby(["model_s","condition","score_state"]):
    n=len(sub)
    rows.append(dict(model=m, condition=c, score_state=ss, n_posts=n, mean_chars=sub.chars.mean(),
                     **{f"share_{cat}": (sub.category==cat).mean() for cat in
                        ["directive","opponent_info","identity","other"]}))
save(pd.DataFrame(rows),"per_q5_post_categories_by_state.csv")
print(); print(pd.DataFrame(rows).round(3).to_string(index=False))

# does the post name an opponent agent id, propose, or announce?
import re
NAMEOPP = re.compile(r"\bA\d{2}\b")
PROPOSE = re.compile(r"\b(let'?s|propose|if you|i'?ll match|mutual|alternat|cooperat|trust|agree|suggest|deal|both pick|we (can|should|could))\b", re.I)
ANNOUNCE= re.compile(r"\b(pick|picking|picked|choosing|chose|decision recorded|exchange \d+)\b", re.I)
p["names_agent"]=p.text.str.count(NAMEOPP)
p["multi_agent_named"]=p.text.apply(lambda t: len(set(NAMEOPP.findall(t)))>=2)
p["proposes"]=p.text.str.contains(PROPOSE)
p["announces"]=p.text.str.contains(ANNOUNCE)
rows=[]
for (m,e,c), sub in p.groupby(["model_s","effort","condition"]):
    rows.append(dict(model=m, effort=e, condition=c, n_posts=len(sub),
                     share_names_any_agent=(sub.names_agent>0).mean(),
                     share_names_two_agents=sub.multi_agent_named.mean(),
                     share_proposes=sub.proposes.mean(),
                     share_announces=sub.announces.mean()))
d3=pd.DataFrame(rows); save(d3,"per_q5_post_content_regex.csv")
print(); print(d3.round(3).to_string(index=False))

# read-before-post, from the decision rows
d = decisions()
dp = d[d.att_post_calls.fillna(0)>0]
rows=[]
for (m,e,c), sub in dp.groupby(["model","effort","condition"]):
    rows.append(dict(model=short(m), effort=e, condition=c, n_post_moves=len(sub),
                     read_before_post_rate=sub.read_before_post.astype(float).mean(),
                     mean_board_size_at_read=sub.board_size_at_read.astype(float).mean()))
d4=pd.DataFrame(rows); save(d4,"per_q5_read_before_post.csv")
print(); print(d4.round(3).to_string(index=False))

# read / post split over all board calls
rows=[]
for (m,e,c), sub in d.groupby(["model","effort","condition"]):
    tot=sub.att_board_calls.fillna(0).sum()
    if tot==0: continue
    rows.append(dict(model=short(m), effort=e, condition=c, n_decisions=len(sub),
                     att_board_calls=int(tot), att_read=int(sub.att_read_calls.fillna(0).sum()),
                     att_post=int(sub.att_post_calls.fillna(0).sum()),
                     att_decoy=int(sub.att_decoy_calls.fillna(0).sum()),
                     post_share_of_board=sub.att_post_calls.fillna(0).sum()/tot))
d5=pd.DataFrame(rows); save(d5,"per_q5_read_post_split.csv")
print(); print(d5.round(3).to_string(index=False))

# verbatim examples: 10 across categories with ids
ex=[]
rng=np.random.default_rng(7)
for (c,cat), sub in p.groupby(["condition","category"]):
    take=sub.sample(min(6,len(sub)), random_state=7)
    for _,r in take.iterrows():
        ex.append(dict(condition=c, category=cat, model=r.model_s, effort=r.effort,
                       score_state=r.score_state, sandbox=r.sandbox, game_uid=r.game_uid,
                       agent=r.agent, round=r["round"], pair_type=r.pair_type,
                       text=str(r.text)[:300]))
save(pd.DataFrame(ex),"per_q5_post_examples.csv")
