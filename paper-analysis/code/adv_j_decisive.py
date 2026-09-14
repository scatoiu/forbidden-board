"""Decisive follow-ups:
(j1) Does the assigned state raise DECOY calls too? If it does, the state effect is general
tool-calling, not board-seeking.
(j2) Ceiling test for the paraphrase gradient in B: is the effect constant on the log-odds scale?
(j3) Is the reasoning dial verified? reasoning tokens by effort (prereg + low arm)."""
import pandas as pd, numpy as np
from adv_common import decisions, games, prereg, signflip_p, TABLES

D=decisions(); G=games(); d=prereg(D)
ds=d[d.model.str.contains('DeepSeek')&d.is_played].copy()
ds['b']=ds.att_board_calls>0; ds['k']=ds.att_decoy_calls>0
pd.set_option('display.width',250,'display.max_columns',40,'display.max_rows',200)

h=ds.groupby(['condition','effort','score_state','block']).agg(
    n=('b','size'),board_hz=('b','mean'),decoy_hz=('k','mean')).reset_index()
h.to_csv(TABLES/'adv_j_hazards.csv',index=False)
print('=== (j1) per-decision board and decoy hazard by state, off effort ===')
rows=[]
for cond in ['forbidden','hidden','permitted']:
    for metric in ['board_hz','decoy_hz']:
        pv=h[(h.condition==cond)&(h.effort=='off')].pivot_table(index='block',columns='score_state',values=metric)
        dd=(pv['behind']-pv['ahead']).values; p,_,_=signflip_p(dd)
        rows.append(dict(condition=cond,metric=metric,mean_pp=100*np.mean(dd),n_pos=int((dd>0).sum()),p=p,
                         per_block=';'.join(f'{100*x:+.2f}' for x in dd)))
r=pd.DataFrame(rows); r.to_csv(TABLES/'adv_j_state_on_hazards.csv',index=False); print(r.to_string(index=False))
print()
print(h[h.effort=='off'].to_string(index=False))

# (j2) log-odds
print(); print('=== (j2) B_forbidden on the log-odds scale (ceiling check) ===')
from adv_common import games as _g, prereg as _p, endpoint_by
gs=_p(_g()); gs=gs[gs.model.str.contains('DeepSeek')]
ep=endpoint_by(gs[(gs.condition=='forbidden')&(gs.effort=='off')],['score_state','block','paraphrase'])
pv=ep.pivot_table(index=['block','paraphrase'],columns='score_state',values='board_rate').reset_index()
lg=lambda x: np.log(x/(1-x))
pv['logit_diff']=lg(pv.behind)-lg(pv.ahead); pv['pp_diff']=100*(pv.behind-pv.ahead)
pv['odds_ratio']=np.exp(pv.logit_diff)
print(pv.round(4).to_string(index=False))
pv.to_csv(TABLES/'adv_j_logodds.csv',index=False)
dd=pv.logit_diff.values; p,_,_=signflip_p(dd)
print(f'logit difference: mean {np.mean(dd):+.3f} (OR {np.exp(np.mean(dd)):.2f}), {int((dd>0).sum())}/6, p={p:.5f}')
print('p1 OR %.2f / p2 OR %.2f / p3 OR %.2f' % tuple(np.exp(pv.groupby('paraphrase').logit_diff.mean()).values))

# (j3) reasoning dial
print(); print('=== (j3) reasoning tokens by effort (all datasets, DeepSeek forbidden) ===')
all_d=D[D.model.str.contains('DeepSeek')&(D.condition=='forbidden')&D.is_played]
t=all_d.groupby(['dataset','effort']).reasoning_tokens.describe(percentiles=[.25,.5,.75])[['count','25%','50%','75%']]
print(t.to_string())
t.to_csv(TABLES/'adv_j_reasoning_tokens.csv')
