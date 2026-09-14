"""The exploratory cooperation-by-condition row (T3) rests on COMPLETED games, and the
hidden / permitted off cells lose 5-47% of games to length-truncation aborts. Test the
sensitivity: coop by condition on completed games vs on all played decisions, and the
abort rate of the same cells; plus the same comparison inside the 4096-cap replication,
where truncation aborts nearly vanish."""
import pandas as pd, numpy as np
from adv_common import decisions, games, prereg, TABLES

D=decisions(); G=games()
pd.set_option('display.width',250,'display.max_columns',40,'display.max_rows',200)
d=prereg(D); ds=d[d.model.str.contains('DeepSeek')]
g=prereg(G); gsx=g[g.model.str.contains('DeepSeek')]

comp=set(gsx[gsx.game_complete.astype(bool)].agent_game_uid)
x=ds[ds.is_played].copy(); x['coop']=x.action=='C'; x['in_completed']=x.agent_game_uid.isin(comp)
t=x.groupby(['condition','effort','pair_type']).agg(
    coop_all=('coop','mean'), n_all=('coop','size')).reset_index()
t2=x[x.in_completed].groupby(['condition','effort','pair_type']).agg(
    coop_completed=('coop','mean'), n_completed=('coop','size')).reset_index()
t=t.merge(t2,on=['condition','effort','pair_type'])
ab=gsx.groupby(['condition','effort']).game_aborted.mean().rename('abort_rate_agent_game').reset_index()
t=t.merge(ab,on=['condition','effort'])
t['pct_decisions_dropped']=100*(1-t.n_completed/t.n_all)
t.to_csv(TABLES/'adv_l_coop_sensitivity.csv',index=False)
print('=== cooperation by condition: completed-game view vs all played decisions (DeepSeek, prereg) ===')
print(t.round(4).to_string(index=False))

rep=D[D.dataset=='replication']; repg=G[G.dataset=='replication']
compr=set(repg[repg.game_complete.astype(bool)].agent_game_uid)
y=rep[rep.is_played].copy(); y['coop']=y.action=='C'
tr=y.groupby(['condition','pair_type']).agg(coop_all=('coop','mean'),n=('coop','size')).reset_index()
tr2=y[y.agent_game_uid.isin(compr)].groupby(['condition','pair_type']).agg(coop_completed=('coop','mean')).reset_index()
tr=tr.merge(tr2,on=['condition','pair_type'])
tr.to_csv(TABLES/'adv_l_coop_replication.csv',index=False)
print(); print('=== the same cells in the 4096-cap replication (off effort, hidden/permitted) ===')
print(tr.round(4).to_string(index=False))
