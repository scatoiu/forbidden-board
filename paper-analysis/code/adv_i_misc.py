"""Objection (i) and my own additions:
(i1) exposure: does the endpoint (a union over rounds) differ because games are LONGER in one arm?
(i2) concentration: is forbidden-off use spread over all 12 agents or carried by a few?
(i3) drift: does use grow over the life of a sandbox as the board fills (board_size_at_read)?
(i4) round profile: how much use happens at round 1, before any in-game score gap exists?
(i5) per-opportunity hazard: contrast A and B on a per-decision endpoint that is exposure-free."""
import pandas as pd, numpy as np
from adv_common import decisions, games, prereg, endpoint_by, signflip_p, TABLES

D=decisions(); G=games(); d=prereg(D); g=prereg(G)
ds=d[d.model.str.contains('DeepSeek')]; gs=g[g.model.str.contains('DeepSeek')]
pd.set_option('display.width',250,'display.max_columns',40,'display.max_rows',300)

# (i1) exposure
ex = g[g.game_observed.astype(bool)].groupby(['model','condition','effort','score_state','block']).agg(
    mean_rounds=('rounds','mean'), median_rounds=('rounds','median'),
    n_played=('n_played','mean')).reset_index()
ex.to_csv(TABLES/'adv_i_exposure.csv',index=False)
print('=== (i1) exposure: rounds per agent-game by cell ===')
print(ex[ex.condition=='forbidden'].to_string(index=False))
for mdl in ['DeepSeek','MiMo']:
    pv=ex[(ex.model.str.contains(mdl))&(ex.condition=='forbidden')&(ex.effort=='off')].pivot_table(index='block',columns='score_state',values='n_played')
    if {'ahead','behind'}<=set(pv.columns):
        dd=(pv['behind']-pv['ahead']).values; p,k,fl=signflip_p(dd)
        print(f'  {mdl} forbidden-off played rounds, behind-ahead: mean {np.mean(dd):+.3f}, {int((dd>0).sum())}/6, p={p:.5f}')
pvA=ex[(ex.model.str.contains("DeepSeek"))&(ex.condition=='forbidden')&(ex.score_state=='behind')].pivot_table(index='block',columns='effort',values='n_played')
dd=(pvA['high']-pvA['off']).values; p,k,fl=signflip_p(dd)
print(f'  DeepSeek forbidden-behind played rounds, high-off: mean {np.mean(dd):+.3f}, {int((dd>0).sum())}/6, p={p:.5f}')

# (i5) exposure-free per-decision hazard
haz = ds[ds.is_played].assign(used=lambda x: x.att_board_calls>0).groupby(
    ['condition','effort','score_state','block']).agg(n_dec=('used','size'),hazard=('used','mean')).reset_index()
haz.to_csv(TABLES/'adv_i_hazard.csv',index=False)
print(); print('=== (i5) per-decision board-call hazard (exposure-free), DeepSeek ===')
print(haz[haz.condition=='forbidden'].to_string(index=False))
pv=haz[(haz.condition=='forbidden')&(haz.effort=='off')].pivot_table(index='block',columns='score_state',values='hazard')
dd=(pv['behind']-pv['ahead']).values; p,k,fl=signflip_p(dd)
print(f'  B on hazard: mean {100*np.mean(dd):+.2f} pp per decision, {int((dd>0).sum())}/6, p={p:.5f}, per block ' + ';'.join(f'{100*x:+.2f}' for x in dd))
pv=haz[(haz.condition=='forbidden')&(haz.score_state=='behind')].pivot_table(index='block',columns='effort',values='hazard')
dd=(pv['high']-pv['off']).values; p,k,fl=signflip_p(dd)
print(f'  A on hazard: mean {100*np.mean(dd):+.2f} pp per decision, {int((dd>0).sum())}/6, p={p:.5f}')
# hidden/permitted on the hazard (the arms that ceiling on the game endpoint)
for cond in ['hidden','permitted']:
    pv=haz[(haz.condition==cond)&(haz.effort=='off')].pivot_table(index='block',columns='score_state',values='hazard')
    dd=(pv['behind']-pv['ahead']).values; p,k,fl=signflip_p(dd)
    print(f'  B on hazard, {cond}: mean {100*np.mean(dd):+.2f} pp, {int((dd>0).sum())}/6, p={p:.5f}, per block ' + ';'.join(f'{100*x:+.2f}' for x in dd))

# (i2) concentration across the 12 LLM agents
fo=gs[(gs.condition=='forbidden')&(gs.effort=='off')&(gs.game_observed.astype(bool))].copy()
fo['used']=fo.attempted_board_calls>0
ag=fo.groupby(['block','score_state','agent']).used.mean().reset_index()
conc=ag.groupby(['block','score_state']).agg(n_agents=('agent','nunique'),min_use=('used','min'),
    med_use=('used','median'),max_use=('used','max'),
    n_agents_zero=('used',lambda s:int((s==0).sum())),
    share_top3=('used',lambda s: float(np.sort(s)[-3:].sum()/s.sum()) if s.sum()>0 else np.nan)).reset_index()
conc.to_csv(TABLES/'adv_i_agent_concentration.csv',index=False)
print(); print('=== (i2) per-agent board-use rate inside each forbidden-off cell (12 LLM agents) ===')
print(conc.to_string(index=False))

# (i3) drift over the sandbox: board size at read, and use by game index
dr=ds[(ds.condition=='forbidden')&(ds.effort=='off')&(ds.is_played)].copy()
dr['used']=dr.att_board_calls>0
gi=dr.groupby(['score_state',pd.qcut(dr.game,5,labels=['q1','q2','q3','q4','q5'])],observed=True).agg(
    n=('used','size'),hazard=('used','mean'),board_size=('board_size_at_read','median')).reset_index()
gi.to_csv(TABLES/'adv_i_drift.csv',index=False)
print(); print('=== (i3) hazard and median board size by game-index quintile inside the sandbox ===')
print(gi.to_string(index=False))

# (i4) round profile / round-1 endpoint
r1 = ds[(ds.condition=='forbidden')&(ds.is_played)&(ds['round']==1)].assign(used=lambda x:x.att_board_calls>0)
t=r1.groupby(['effort','score_state','block']).agg(n=('used','size'),round1_use=('used','mean')).reset_index()
pv=t[t.effort=='off'].pivot_table(index='block',columns='score_state',values='round1_use')
dd=(pv['behind']-pv['ahead']).values; p,k,fl=signflip_p(dd)
print(); print('=== (i4) round-1 board-call rate (no in-game history yet) ==='); print(t.to_string(index=False))
print(f'  B at round 1: mean {100*np.mean(dd):+.2f} pp, {int((dd>0).sum())}/6, p={p:.5f}')
t.to_csv(TABLES/'adv_i_round1.csv',index=False)
