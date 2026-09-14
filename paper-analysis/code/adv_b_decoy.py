"""Objection (b): 'reasoning suppresses all tool use'. Board vs decoy, rates AND call counts,
per block, off vs high, in permitted / hidden / forbidden."""
import pandas as pd, numpy as np
from adv_common import decisions, games, prereg, endpoint_by, signflip_p, TABLES

g = prereg(games()); d = prereg(decisions())
keys = ['model','condition','effort','score_state','block']

# per-game rates
ep = endpoint_by(g, keys)

# per-game CALL COUNTS (attempt-union), summed over the agent-games in a game
obs = g[g.game_observed.astype(bool)]
per = obs.groupby(keys+['game_uid']).agg(board=('attempted_board_calls','sum'),
                                         decoy=('attempted_decoy_calls','sum')).reset_index()
cnt = per.groupby(keys).agg(board_calls_per_game=('board','mean'),
                            decoy_calls_per_game=('decoy','mean')).reset_index()
t = ep.merge(cnt, on=keys)
t['board_over_decoy_rate'] = t.board_rate/t.decoy_rate.replace(0,np.nan)
t['board_over_decoy_calls'] = t.board_calls_per_game/t.decoy_calls_per_game.replace(0,np.nan)
t = t.sort_values(['model','condition','score_state','effort','block'])
t.to_csv(TABLES/'adv_b_board_vs_decoy.csv', index=False)

pd.set_option('display.width',250,'display.max_columns',40,'display.max_rows',300)
print('=== per-block board/decoy, DeepSeek, behind (off vs high) and ahead-off ===')
print(t[t.model.str.contains('DeepSeek')][['condition','effort','score_state','block','n_games','board_rate','decoy_rate','board_calls_per_game','decoy_calls_per_game','board_over_decoy_calls']].to_string(index=False))
print()
print('=== MiMo ===')
print(t[t.model.str.contains('MiMo')][['condition','effort','score_state','block','n_games','board_rate','decoy_rate','board_calls_per_game','decoy_calls_per_game','board_over_decoy_calls']].to_string(index=False))

# paired high-minus-off differences per block (behind arm) for board and decoy, each condition
rows=[]
for cond in ['forbidden','hidden','permitted']:
    for metric in ['board_rate','decoy_rate','board_calls_per_game','decoy_calls_per_game']:
        sub=t[(t.model.str.contains('DeepSeek'))&(t.condition==cond)&(t.score_state=='behind')]
        piv=sub.pivot_table(index='block',columns='effort',values=metric)
        if {'off','high'}<=set(piv.columns):
            diffs=(piv['high']-piv['off']).values
            p,k,floor=signflip_p(diffs)
            rows.append(dict(condition=cond,metric=metric,k=k,mean_diff=float(np.mean(diffs)),
                             n_pos=int((diffs>0).sum()),p_signflip=p,floor=floor,
                             per_block=';'.join(f'{x:+.3f}' for x in diffs)))
r=pd.DataFrame(rows); r.to_csv(TABLES/'adv_b_effort_diffs.csv',index=False)
print(); print('=== high - off paired block differences (DeepSeek, behind) ===')
print(r.to_string(index=False))
