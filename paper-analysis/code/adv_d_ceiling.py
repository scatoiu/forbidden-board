"""Objection (d): ceilings. What effect could the MiMo cells (87-96%) have shown?
Also: contrast B on a NON-ceilinged endpoint inside the saturated hidden/permitted arms
(post rate, board calls per game, first-use round)."""
import pandas as pd, numpy as np
from adv_common import games, prereg, endpoint_by, signflip_p, TABLES

G = games(); g = prereg(G)
pd.set_option('display.width',250,'display.max_columns',40,'display.max_rows',300)

# ---- (d1) headroom bound for MiMo B_forbidden ----
m = endpoint_by(g[g.model.str.contains('MiMo')&(g.condition=='forbidden')], ['score_state','block'])
piv = m.pivot_table(index='block',columns='score_state',values='board_rate')
piv['diff']=piv.behind-piv.ahead
# largest attainable positive difference given the observed 'ahead' rate and an empirical ceiling
for ceil in [1.0, 0.9857, 0.9714]:
    piv[f'max_diff_ceil_{ceil}']=np.maximum(ceil-piv.ahead,0)
piv.to_csv(TABLES/'adv_d_mimo_headroom.csv')
print('=== (d1) MiMo forbidden: observed behind-ahead and the largest difference the ahead rate leaves ===')
print((piv*100).round(2).to_string())
d=piv['diff'].values; p,k,fl=signflip_p(d)
print(f'observed: mean {np.mean(d)*100:+.2f} pp, {int((d>0).sum())}/6 positive, sign-flip p={p:.5f}')
print('max attainable mean diff at a 100 pct ceiling: {:+.2f} pp; at the highest MiMo cell observed (98.57 pct): {:+.2f} pp'.format(
      100*np.mean(np.maximum(1.0-piv.ahead,0)), 100*np.mean(np.maximum(0.9857-piv.ahead,0))))

# ---- (d2) non-ceilinged endpoints inside the saturated arms ----
gs = g[g.model.str.contains('DeepSeek')&(g.effort=='off')]
obs = gs[gs.game_observed.astype(bool)]
per = obs.groupby(['condition','score_state','block','game_uid']).agg(
    board=('attempted_board_calls','sum'), post=('attempted_post_calls','sum'),
    first_use=('first_use_round','min')).reset_index()
cell = per.groupby(['condition','score_state','block']).agg(
    n=('game_uid','size'), post_rate=('post', lambda s: float((s>0).mean())),
    board_calls=('board','mean'), post_calls=('post','mean'),
    median_first_use=('first_use','median')).reset_index()
cell.to_csv(TABLES/'adv_d_secondary_endpoints.csv',index=False)
print(); print('=== (d2) secondary (non-ceilinged) endpoints by state, off effort, DeepSeek ===')
print(cell.to_string(index=False))
rows=[]
for cond in ['permitted','hidden','forbidden']:
    for metric in ['post_rate','board_calls','post_calls','median_first_use']:
        pv=cell[cell.condition==cond].pivot_table(index='block',columns='score_state',values=metric)
        if {'ahead','behind'}<=set(pv.columns):
            dd=(pv['behind']-pv['ahead']).values; p,k,fl=signflip_p(dd)
            rows.append(dict(condition=cond,metric=metric,mean_behind_minus_ahead=float(np.mean(dd)),
                             n_pos=int((dd>0).sum()),p=p,per_block=';'.join(f'{x:+.3f}' for x in dd)))
r=pd.DataFrame(rows); r.to_csv(TABLES/'adv_d_state_on_secondary.csv',index=False)
print(); print('=== (d3) behind-ahead on the secondary endpoints (paired over six blocks) ===')
print(r.to_string(index=False))
