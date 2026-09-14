"""Objection (a): 'reasoning fixes output formatting, not attention'.
Tests: (1) parse/abort/truncation by effort and condition; (2) 4096-cap replication vs 768-cap
at off effort (hidden/permitted only); (3) board use in games with vs without any retry/fallback;
(4) how much of the attempt-union endpoint is carried by calls lost to a retry."""
import pandas as pd, numpy as np
from adv_common import decisions, games, prereg, endpoint_by, signflip_p, TABLES

D = decisions(); G = games()
d = prereg(D); g = prereg(G)

# ---- 1. quality by effort x condition (DeepSeek, prereg) ----
dd = d[d.model.str.contains('DeepSeek')]
q = dd.groupby(['condition','effort','score_state']).agg(
    n_dec=('round','size'),
    parse_fail_rate=('parse_ok', lambda s: float((~s.astype(bool)).mean())),
    trunc_rate=('finish_reason', lambda s: float((s=='length').mean())),
    fallback_rate=('fallback_flag', lambda s: float(s.notna().mean())),
    retry_rate=('retries', lambda s: float((s>0).mean())),
).reset_index()
gg = g[g.model.str.contains('DeepSeek')]
qg = gg.groupby(['condition','effort','score_state']).agg(
    abort_rate_agent_game=('game_aborted', lambda s: float(s.astype(bool).mean())),
    unobserved_rate=('game_unobserved', lambda s: float(s.astype(bool).mean())),
).reset_index()
q = q.merge(qg, on=['condition','effort','score_state'])
q.to_csv(TABLES/'adv_a_quality_by_cell.csv', index=False)
pd.set_option('display.width',250,'display.max_columns',40,'display.max_rows',300)
print('=== (1) quality by cell, DeepSeek prereg ===')
print(q.to_string(index=False))

# ---- 2. 768-cap vs 4096-cap replication, off effort, hidden+permitted ----
rep = G[G.dataset=='replication']
base = g[(g.model.str.contains('DeepSeek'))&(g.effort=='off')&(g.condition.isin(['hidden','permitted']))]
keys=['condition','score_state','block']
a = endpoint_by(base, keys); a['cap']='768'
b = endpoint_by(rep, keys);  b['cap']='4096'
obs=lambda x: x[x.game_observed.astype(bool)]
def calls(x):
    p=obs(x).groupby(keys+['game_uid']).agg(board=('attempted_board_calls','sum'),decoy=('attempted_decoy_calls','sum')).reset_index()
    return p.groupby(keys).agg(board_calls_per_game=('board','mean'),decoy_calls_per_game=('decoy','mean')).reset_index()
a=a.merge(calls(base),on=keys); b=b.merge(calls(rep),on=keys)
cap = pd.concat([a,b]).sort_values(keys+['cap'])
capq = pd.concat([
  d[(d.model.str.contains('DeepSeek'))&(d.effort=='off')&(d.condition.isin(['hidden','permitted']))].assign(cap='768'),
  D[D.dataset=='replication'].assign(cap='4096')]).groupby(keys+['cap']).agg(
    parse_fail_rate=('parse_ok', lambda s: float((~s.astype(bool)).mean())),
    trunc_rate=('finish_reason', lambda s: float((s=='length').mean())),
    retry_rate=('retries', lambda s: float((s>0).mean()))).reset_index()
cap = cap.merge(capq, on=keys+['cap'])
cap.to_csv(TABLES/'adv_a_cap_replication.csv', index=False)
print(); print('=== (2) answer cap 768 vs 4096, off effort ===')
print(cap[['condition','score_state','block','cap','n_games','board_rate','decoy_rate','board_calls_per_game','decoy_calls_per_game','parse_fail_rate','trunc_rate','retry_rate']].to_string(index=False))

# paired per-block cap differences
rows=[]
for cond in ['hidden','permitted']:
    for st in ['ahead','behind']:
        for m in ['board_rate','decoy_rate','board_calls_per_game']:
            piv=cap[(cap.condition==cond)&(cap.score_state==st)].pivot_table(index='block',columns='cap',values=m)
            if {'768','4096'}<=set(piv.columns):
                diffs=(piv['4096']-piv['768']).values
                p,k,fl=signflip_p(diffs)
                rows.append(dict(condition=cond,state=st,metric=m,mean_diff=float(np.mean(diffs)),n_pos=int((diffs>0).sum()),p=p,
                                 per_block=';'.join(f'{x:+.3f}' for x in diffs)))
r=pd.DataFrame(rows); r.to_csv(TABLES/'adv_a_cap_diffs.csv',index=False)
print(); print('=== (2b) 4096 minus 768, paired over blocks ===')
print(r.to_string(index=False))

# ---- 3. within forbidden-off, board use in games with vs without any retry / fallback / truncation ----
fo = d[(d.model.str.contains('DeepSeek'))&(d.condition=='forbidden')&(d.effort=='off')]
flag = fo.groupby(['score_state','block','game_uid']).agg(
    any_retry=('retries', lambda s: bool((s>0).any())),
    any_trunc=('finish_reason', lambda s: bool((s=='length').any())),
    any_fb=('fallback_flag', lambda s: bool(s.notna().any())),
    board=('att_board_calls','sum')).reset_index()
flag['used']=flag.board>0
t3 = flag.groupby(['score_state','any_retry']).agg(n=('game_uid','size'),use=('used','mean')).reset_index()
t3b = flag.groupby(['score_state','any_fb']).agg(n=('game_uid','size'),use=('used','mean')).reset_index()
t3.to_csv(TABLES/'adv_a_use_by_retry.csv',index=False)
print(); print('=== (3) forbidden-off DeepSeek: board use by whether the game had any retry / any fallback ==='); print(t3.to_string(index=False)); print(t3b.to_string(index=False))

# ---- 4. attempt-union vs final-attempt endpoint ----
rows=[]
for (mdl,cond,eff,st),x in g.groupby(['model','condition','effort','score_state']):
    o=x[x.game_observed.astype(bool)]
    per=o.groupby('game_uid').agg(att=('attempted_board_calls','sum'),fin=('use_count','sum')).reset_index()
    rows.append(dict(model=mdl.split('/')[-1],condition=cond,effort=eff,state=st,n=len(per),
                     attempted_rate=float((per.att>0).mean()), final_rate=float((per.fin>0).mean()),
                     inflation_pp=100*float((per.att>0).mean()-(per.fin>0).mean())))
r4=pd.DataFrame(rows).sort_values(['model','condition','effort','state'])
r4.to_csv(TABLES/'adv_a_attempt_vs_final.csv',index=False)
print(); print('=== (4) attempt-union endpoint vs final-attempt endpoint ==='); print(r4.to_string(index=False))
lost = d.groupby(['model','condition','effort','score_state'])['board_call_lost_by_retry'].agg(['sum','size']).reset_index()
print(); print('board calls lost by retry (decision rows):'); print(lost.to_string(index=False))
