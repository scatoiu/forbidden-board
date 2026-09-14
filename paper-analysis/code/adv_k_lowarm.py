"""(k1) Relative as well as absolute state effects on board vs decoy.
(k2) The low arm: is the effort effect a dose response or a step at 'any reasoning'?
     Does the decoy collapse at low too?
(k3) The p4 placement cells (prohibition repeated beside the decision)."""
import pandas as pd, numpy as np
from adv_common import decisions, games, prereg, endpoint_by, signflip_p, TABLES

D=decisions(); G=games()
pd.set_option('display.width',250,'display.max_columns',40,'display.max_rows',200)

# (k1) relative risk
d=prereg(D); ds=d[d.model.str.contains('DeepSeek')&d.is_played].copy()
ds['b']=ds.att_board_calls>0; ds['k']=ds.att_decoy_calls>0
h=ds[ds.effort=='off'].groupby(['condition','score_state']).agg(board=('b','mean'),decoy=('k','mean')).reset_index()
pv=h.pivot_table(index='condition',columns='score_state',values=['board','decoy'])
rr=pd.DataFrame({'board_ahead':pv[('board','ahead')],'board_behind':pv[('board','behind')],
                 'decoy_ahead':pv[('decoy','ahead')],'decoy_behind':pv[('decoy','behind')]})
rr['board_RR']=rr.board_behind/rr.board_ahead; rr['decoy_RR']=rr.decoy_behind/rr.decoy_ahead
rr.to_csv(TABLES/'adv_k_relative_risk.csv')
print('=== (k1) per-decision hazards and behind/ahead risk ratios, off effort, DeepSeek ===')
print(rr.round(4).to_string())

# (k2) low arm
low=G[G.dataset=='low_arm']; lowd=D[D.dataset=='low_arm']
fb=prereg(G); fb=fb[fb.model.str.contains('DeepSeek')&(fb.condition=='forbidden')&(fb.score_state=='behind')]
e_low=endpoint_by(low,['block']).rename(columns={'board_rate':'low','decoy_rate':'low_decoy'})
e_off=endpoint_by(fb[fb.effort=='off'],['block']).rename(columns={'board_rate':'off','decoy_rate':'off_decoy'})
e_hi =endpoint_by(fb[fb.effort=='high'],['block']).rename(columns={'board_rate':'high','decoy_rate':'high_decoy'})
t=e_off[['block','off','off_decoy']].merge(e_low[['block','low','low_decoy']],on='block').merge(e_hi[['block','high','high_decoy']],on='block')
t.to_csv(TABLES/'adv_k_effort_ladder.csv',index=False)
print(); print('=== (k2) effort ladder (forbidden, behind): board and decoy per-game rates ===')
print((t.set_index('block')*100).round(2).to_string())
for a,b in [('low','off'),('high','low'),('high','off')]:
    dd=(t[a]-t[b]).values; p,_,_=signflip_p(dd)
    dk=(t[a+'_decoy']-t[b+'_decoy']).values; pk,_,_=signflip_p(dk)
    print(f'  board {a}-{b}: {100*np.mean(dd):+.1f} pp, {int((dd>0).sum())}/6, p={p:.5f} | decoy {a}-{b}: {100*np.mean(dk):+.1f} pp, {int((dk>0).sum())}/6, p={pk:.5f}')
lt=lowd[lowd.is_played].reasoning_tokens.describe(percentiles=[.25,.5,.75])
print('  low-arm reasoning tokens 25/50/75:', lt['25%'], lt['50%'], lt['75%'])

# (k3) p4 placement
G2=G[(G.dataset=='prereg')]
p4=endpoint_by(G2[G2.paraphrase=='p4'],['model','block'])
p1=endpoint_by(G2[(G2.paraphrase=='p1')&(G2.condition=='forbidden')&(G2.effort=='off')&(G2.score_state=='behind')&(G2.block=='B1')],['model'])
print(); print('=== (k3) p4 placement cells (prohibition repeated beside the decision) ===')
print(p4.to_string(index=False)); print('matched p1 B1 forbidden-off-behind:'); print(p1.to_string(index=False))
p4.to_csv(TABLES/'adv_k_placement.csv',index=False)
