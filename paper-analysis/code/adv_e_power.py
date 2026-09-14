"""Objection (e): k=6, floor 0.03125, Holm 0.094 - and the fragility of the 6/6 unanimity.
Also paraphrase heterogeneity: is B_forbidden a p1/p2 effect that vanishes in p3?"""
import pandas as pd, numpy as np, itertools
from adv_common import games, prereg, endpoint_by, signflip_p, TABLES

G=games(); g=prereg(G); gs=g[g.model.str.contains('DeepSeek')]
pd.set_option('display.width',250,'display.max_columns',40)

fb=gs[(gs.condition=='forbidden')&(gs.effort=='off')]
ep=endpoint_by(fb,['score_state','block','paraphrase'])
piv=ep.pivot_table(index=['block','paraphrase'],columns='score_state',values='board_rate').reset_index()
piv['diff_pp']=100*(piv.behind-piv.ahead)
piv['n_games_diff']=(piv.diff_pp/100*210).round().astype(int)
piv.to_csv(TABLES/'adv_e_B_by_paraphrase.csv',index=False)
print('=== B_forbidden per block, with the difference expressed in games out of 210 ===')
print(piv.to_string(index=False))

d=(piv.behind-piv.ahead).values
p,k,fl=signflip_p(d)
print(f'\nall six: mean {100*np.mean(d):+.2f} pp, {int((d>0).sum())}/6 positive, exact sign-flip p={p:.5f}, floor {fl}')
for pp in ['p1','p2','p3']:
    v=piv[piv.paraphrase==pp]; dd=(v.behind-v.ahead).values
    print(f'  {pp}: blocks {list(v.block)}, diffs {[f"{100*x:+.2f}" for x in dd]}, mean {100*np.mean(dd):+.2f} pp')
sub=piv[piv.paraphrase!='p3']; dd=(sub.behind-sub.ahead).values
p2_,k2,fl2=signflip_p(dd)
print(f'  p1+p2 only (k=4): mean {100*np.mean(dd):+.2f} pp, {int((dd>0).sum())}/4, p={p2_:.5f}, floor {fl2}')

# fragility: how many games must move in B5/B6 to break unanimity
print('\n=== fragility ===')
for blk in ['B5','B6']:
    r=piv[piv.block==blk].iloc[0]
    print(f'{blk}: behind {r.behind*210:.0f}/210 vs ahead {r.ahead*210:.0f}/210 - a margin of {r.n_games_diff} games')
for flip in [1,2]:
    d2=d.copy()
    idx=np.argsort(np.abs(d2))[:flip]
    d2[idx]=-d2[idx]
    pf,_,_=signflip_p(d2)
    print(f'if the {flip} smallest block difference(s) reversed: {int((d2>0).sum())}/6 positive, p={pf:.5f}')

# multiplicity: the smallest Holm-adjusted p a k=6 sign-flip family of 3 can reach
print('\n=== multiplicity ===')
print(f'exact floor at k=6 (two-sided sign-flip): {2**-5:.5f}; Holm step 1 multiplier 3 -> {3*2**-5:.5f}')
print(f'blocks needed for Holm-adjusted p < 0.05 with a family of 3: k such that 3*2^-(k-1) < 0.05 -> k >= {int(np.ceil(1+np.log2(3/0.05)))}')

# what the paired design does establish: per-block A effect sizes
fa=gs[(gs.condition=='forbidden')&(gs.score_state=='behind')]
epA=endpoint_by(fa,['effort','block']); pivA=epA.pivot_table(index='block',columns='effort',values='board_rate')
pivA['diff_pp']=100*(pivA['high']-pivA['off'])
print('\n=== A_forbidden per block (pp) ==='); print(pivA.round(4).to_string())
pivA.to_csv(TABLES/'adv_e_A_by_block.csv')
