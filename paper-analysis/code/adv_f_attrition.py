"""Objection (f): differential provider-error attrition in the high cells, and the repair re-runs.
(1) unobserved / censored games by cell; (2) contrast A recomputed on observed-only vs keep-all vs
completed-only; (3) do the repaired (late-timestamp) games in B5/B6-forbidden-high carry the
elevated high-effort board use?"""
import pandas as pd, numpy as np
from adv_common import decisions, games, prereg, endpoint_by, signflip_p, TABLES

D=decisions(); G=games(); d=prereg(D); g=prereg(G)
gs=g[g.model.str.contains('DeepSeek')]
pd.set_option('display.width',250,'display.max_columns',40,'display.max_rows',300)

# (1) attrition by cell
t1=gs.groupby(['condition','effort','score_state','block']).agg(
    n_ag=('agent_game_uid','size'), games=('game_uid','nunique'),
    unobserved=('game_unobserved', lambda s:int(s.astype(bool).sum())),
    censored=('game_provider_error_censored', lambda s:int(s.astype(bool).sum())),
    aborted=('game_aborted', lambda s:int(s.astype(bool).sum()))).reset_index()
t1.to_csv(TABLES/'adv_f_attrition.csv',index=False)
print('=== (1) attrition by cell (agent-games) ===')
print(t1[t1.unobserved+t1.censored+t1.aborted>0].to_string(index=False))

# (2) contrast A under three quality policies
def rate(x, policy):
    if policy=='observed': x=x[x.game_observed.astype(bool)]
    elif policy=='completed': x=x[x.game_complete.astype(bool)]
    per=x.groupby('game_uid')['attempted_board_calls'].sum()
    return float((per>0).mean()), int(per.size)
rows=[]
fb=gs[(gs.condition=='forbidden')&(gs.score_state=='behind')]
for policy in ['observed','keep_all','completed']:
    dd=[]
    for blk in sorted(fb.block.unique()):
        hi,_=rate(fb[(fb.block==blk)&(fb.effort=='high')],policy)
        lo,_=rate(fb[(fb.block==blk)&(fb.effort=='off')],policy)
        dd.append(hi-lo)
    p,k,fl=signflip_p(dd)
    rows.append(dict(contrast='A_forbidden',policy=policy,mean_pp=100*np.mean(dd),n_pos=int(np.sum(np.array(dd)>0)),p=p,
                     per_block=';'.join(f'{100*x:+.1f}' for x in dd)))
    dd=[]
    for blk in sorted(fb.block.unique()):
        b,_=rate(gs[(gs.condition=='forbidden')&(gs.effort=='off')&(gs.score_state=='behind')&(gs.block==blk)],policy)
        a,_=rate(gs[(gs.condition=='forbidden')&(gs.effort=='off')&(gs.score_state=='ahead')&(gs.block==blk)],policy)
        dd.append(b-a)
    p,k,fl=signflip_p(dd)
    rows.append(dict(contrast='B_forbidden',policy=policy,mean_pp=100*np.mean(dd),n_pos=int(np.sum(np.array(dd)>0)),p=p,
                     per_block=';'.join(f'{100*x:+.1f}' for x in dd)))
r=pd.DataFrame(rows); r.to_csv(TABLES/'adv_f_policy_sensitivity.csv',index=False)
print(); print('=== (2) registered contrasts under three quality policies ==='); print(r.to_string(index=False))

# worst-case bound on A: assume every unobserved/aborted high game would have used the board
rows=[]
for blk in sorted(fb.block.unique()):
    hi=fb[(fb.block==blk)&(fb.effort=='high')]
    per=hi.groupby('game_uid').agg(att=('attempted_board_calls','sum'),obs=('game_observed', lambda s:bool(s.any()))).reset_index()
    used=(per.att>0).sum(); n=len(per); miss=int((~per.obs).sum())
    lo_b=(used)/n; up_b=(used+miss)/n
    off,_=rate(fb[(fb.block==blk)&(fb.effort=='off')],'keep_all')
    rows.append(dict(block=blk,n_high=n,unobserved=miss,high_rate=lo_b,high_rate_worstcase=up_b,off_rate=off,
                     A_worstcase_pp=100*(up_b-off)))
r2=pd.DataFrame(rows); r2.to_csv(TABLES/'adv_f_bound_A.csv',index=False)
print(); print('=== (2b) worst-case bound on A (every unobserved high game counted as a user) ==='); print(r2.to_string(index=False))

# (3) repaired games: identify by timestamp gap inside each high sandbox
dh=d[(d.model.str.contains('DeepSeek'))&(d.condition=='forbidden')&(d.effort=='high')].copy()
dh['ts']=pd.to_datetime(dh.ts,errors='coerce',utc=True)
first=dh.groupby(['sandbox','game_uid']).ts.min().reset_index()
rows=[]
for sb,x in first.groupby('sandbox'):
    x=x.sort_values('ts'); t0=x.ts.min(); late=x[(x.ts-t0)>pd.Timedelta('45min')]
    rows.append(dict(sandbox=sb,n_games=len(x),n_late=len(late),span_min=float((x.ts.max()-t0).total_seconds()/60)))
print(); print('=== (3) timestamp spread inside each forbidden-high sandbox ===')
print(pd.DataFrame(rows).to_string(index=False))
lab=first.copy()
lab['t0']=lab.groupby('sandbox').ts.transform('min')
lab['late']=(lab.ts-lab.t0)>pd.Timedelta('45min')
use=gs[(gs.condition=='forbidden')&(gs.effort=='high')].groupby(['sandbox','game_uid']).attempted_board_calls.sum().reset_index()
mg=lab.merge(use,on=['sandbox','game_uid']); mg['used']=mg.attempted_board_calls>0
t3=mg.groupby(['sandbox','late']).agg(n=('game_uid','size'),use=('used','mean')).reset_index()
t3.to_csv(TABLES/'adv_f_repair_split.csv',index=False)
print(); print('=== (3b) forbidden-high board use, early vs late (>45 min after the sandbox started) games ===')
print(t3.to_string(index=False))
