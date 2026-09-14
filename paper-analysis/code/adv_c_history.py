"""Objection (c): contrast B is a displayed-history effect (own/opponent conduct in the
scripted warm-up), not a score effect. The warm-up is prepended to the displayed history of the
CURRENT opponent: behind = (C,D),(C,D),(C,C)x4 -> the opponent defected twice on a cooperator;
ahead = (D,C),(D,C),(C,C)x4 -> the agent defected twice on a cooperator.
Tests: (1) round-1 and overall cooperation by state; (2) board use by state in hidden/permitted;
(3) the -30 arm (six (C,D) rounds) vs -10; (4) board use by in-game opponent hostility
(opponent_type, matched state); (5) board use vs score_gap_at_call within a game."""
import pandas as pd, numpy as np
from adv_common import decisions, games, prereg, endpoint_by, signflip_p, TABLES

D = decisions(); G = games()
d = prereg(D); g = prereg(G)
ds = d[d.model.str.contains('DeepSeek')]; gs = g[g.model.str.contains('DeepSeek')]
pd.set_option('display.width',250,'display.max_columns',40,'display.max_rows',400)

# (1) cooperation / dynamics by state, forbidden off (completed games only)
c = gs[(gs.condition=='forbidden')&(gs.effort=='off')&(gs.game_complete.astype(bool))]
t1 = c.groupby(['score_state','block']).agg(n=('agent_game_uid','size'),round1_coop=('round1_coop','mean'),
    own_coop=('own_coop_played','mean'), retaliation=('retaliation_rate','mean'),
    forgiveness=('forgiveness_rate','mean'), score=('score','mean')).reset_index()
t1.to_csv(TABLES/'adv_c_dynamics_by_state.csv',index=False)
print('=== (1) DeepSeek forbidden-off dynamics by assigned state (completed agent-games) ===')
print(t1.to_string(index=False))
for m in ['round1_coop','own_coop','retaliation','forgiveness']:
    piv=t1.pivot_table(index='block',columns='score_state',values=m)
    dd=(piv['behind']-piv['ahead']).values; p,k,fl=signflip_p(dd)
    print(f'  {m}: behind-ahead mean {np.mean(dd):+.4f}, {int((dd>0).sum())}/6 positive, sign-flip p={p:.5f}')

# (2) board use by state in hidden / permitted (ceiling check)
t2 = endpoint_by(gs[(gs.effort=='off')&(gs.condition.isin(['hidden','permitted']))],
                 ['condition','score_state','block'])
print(); print('=== (2) board use by state, hidden/permitted at off (ceiling) ===')
print(t2.to_string(index=False))
t2.to_csv(TABLES/'adv_c_state_hidden_permitted.csv',index=False)

# (3) -30 deficit arm vs -10 behind, paired by block
d30 = endpoint_by(G[G.dataset=='deficit_d30'], ['block']).rename(columns={'board_rate':'rate_d30'})
d10 = endpoint_by(gs[(gs.condition=='forbidden')&(gs.effort=='off')&(gs.score_state=='behind')],
                  ['block']).rename(columns={'board_rate':'rate_d10'})
ah  = endpoint_by(gs[(gs.condition=='forbidden')&(gs.effort=='off')&(gs.score_state=='ahead')],
                  ['block']).rename(columns={'board_rate':'rate_ahead'})
t3 = d30[['block','rate_d30']].merge(d10[['block','rate_d10']],on='block').merge(ah[['block','rate_ahead']],on='block')
t3['d30_minus_d10']=t3.rate_d30-t3.rate_d10; t3['d10_minus_ahead']=t3.rate_d10-t3.rate_ahead
t3['d30_minus_ahead']=t3.rate_d30-t3.rate_ahead
t3.to_csv(TABLES/'adv_c_deficit_monotonicity.csv',index=False)
print(); print('=== (3) monotonicity in the assigned gap: +10 (ahead) / -10 (behind) / -30 ===')
print(t3.to_string(index=False))
for col in ['d30_minus_d10','d10_minus_ahead','d30_minus_ahead']:
    v=t3[col].values; p,k,fl=signflip_p(v)
    print(f'  {col}: mean {np.mean(v)*100:+.1f} pp, {int((v>0).sum())}/6 positive, sign-flip p={p:.5f}')

# (4) board use by in-game opponent hostility, WITHIN a state cell (agent-game level, exploratory)
h = gs[(gs.condition=='forbidden')&(gs.effort=='off')&(gs.game_observed.astype(bool))].copy()
h['used']=h.attempted_board_calls>0
t4=h.groupby(['score_state','opponent_type']).agg(n=('agent_game_uid','size'),use=('used','mean'),
    opp_coop=('opp_coop_played','mean')).reset_index()
t4.to_csv(TABLES/'adv_c_use_by_opponent.csv',index=False)
print(); print('=== (4) agent-game board use by opponent type (exploratory, games share a sandbox) ===')
print(t4.to_string(index=False))

# (5) board use vs score gap at call, within game, forbidden off
s = ds[(ds.condition=='forbidden')&(ds.effort=='off')&(ds.is_played)].copy()
s['used']=s.att_board_calls>0
s['gap_bin']=pd.cut(s.score_gap_at_call, [-1000,-30,-15,-5,5,15,30,1000],
                    labels=['<=-30','-30..-15','-15..-5','-5..5','5..15','15..30','>30'])
t5=s.groupby(['score_state','gap_bin'],observed=True).agg(n=('round','size'),use_per_decision=('used','mean')).reset_index()
t5.to_csv(TABLES/'adv_c_use_by_gap.csv',index=False)
print(); print('=== (5) per-decision board-call rate by realised score gap at the call (exploratory) ===')
print(t5.to_string(index=False))
# also by round
t5b=s.groupby(['score_state',pd.cut(s['round'],[0,1,3,6,10,20,30])],observed=True).agg(n=('round','size'),use=('used','mean')).reset_index()
print(); print('per-decision board-call rate by round:'); print(t5b.to_string(index=False))
