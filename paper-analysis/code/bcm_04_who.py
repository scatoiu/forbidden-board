"""Who uses the board: coverage, concentration, within-sandbox stability, cross-sandbox identity."""
import numpy as np, pandas as pd, itertools
from scipy import stats
import bcm_common as B

A = pd.read_csv(B.AN / 'tables/board_agents_by_block.csv')
S = pd.read_csv(B.AN / 'tables/board_agents_by_block_summary.csv')

print('== coverage and concentration by cell (uniform top-3 share = 0.25)')
print(S.groupby(['model', 'effort', 'condition']).agg(
    sandboxes=('sandbox', 'size'), min_agents=('n_agents_attempted', 'min'),
    max_agents=('n_agents_attempted', 'max'), mean_top3=('top3_share_of_board_calls', 'mean'),
    min_top3=('top3_share_of_board_calls', 'min'), max_top3=('top3_share_of_board_calls', 'max')
).round(3).to_string())

print('\n== DeepSeek forbidden high, per sandbox')
print(S[(S.model == 'DeepSeek') & (S.condition == 'forbidden') & (S.effort == 'high')][
    ['sandbox', 'n_agents_attempted', 'total_board_calls', 'total_attempted_reads',
     'total_attempted_posts', 'posts_on_board']].to_string(index=False))

print('\n== forbidden off: agents attempting, per sandbox')
f = S[(S.condition == 'forbidden') & (S.effort == 'off')]
print(f.groupby('model').n_agents_attempted.value_counts().to_string())
fa = A[(A.condition == 'forbidden') & (A.effort == 'off')]
print('per-agent share of that sandbox\'s board calls (uniform = 0.083):')
print(fa.groupby('model').share_of_sandbox_board_calls.describe().round(3).to_string())

dec = pd.read_parquet(B.AN / 'data/decisions.parquet', columns=[
    'sandbox', 'dataset', 'paraphrase', 'game', 'agent', 'att_board_calls', 'is_played'])
dec = dec[(dec.dataset == 'prereg') & (dec.paraphrase != 'p4') & dec.sandbox.isin(set(S.sandbox))]

# 1. is the spread across agents larger than chance, given each agent's number of decisions?
rows = []
for sb, d in dec.groupby('sandbox'):
    g = d.groupby('agent').agg(opps=('att_board_calls', 'size'), calls=('att_board_calls', 'sum'))
    tot = g.calls.sum()
    if tot < 30:
        continue
    exp = tot * g.opps / g.opps.sum()
    chi2 = float(((g.calls - exp) ** 2 / exp).sum())
    df = len(g) - 1
    rate = g.calls / g.opps
    rows.append(dict(sandbox=sb, total_calls=int(tot), chi2=chi2, df=df,
                     p=float(stats.chi2.sf(chi2, df)),
                     rate_min=float(rate.min()), rate_max=float(rate.max()),
                     rate_cv=float(rate.std() / rate.mean())))
D = pd.DataFrame(rows).merge(S[['sandbox', 'model', 'effort', 'condition']], on='sandbox')
D.to_csv(B.AN / 'tables/bcm_agent_dispersion.csv', index=False)
print('\n== per-agent call rate: dispersion against an equal-rate null (chi-square, df = 11)')
print(D.groupby(['model', 'effort', 'condition']).agg(
    sandboxes=('sandbox', 'size'), mean_chi2=('chi2', 'mean'),
    sandboxes_p_lt_05=('p', lambda x: int((x < 0.05).sum())),
    mean_rate_min=('rate_min', 'mean'), mean_rate_max=('rate_max', 'mean'),
    mean_cv=('rate_cv', 'mean')).round(3).to_string())

# 2. split-half stability of per-agent call RATE (odd vs even games; rates are not compositional)
rows = []
for sb, d in dec.groupby('sandbox'):
    o = d[d.game % 2 == 1].groupby('agent').att_board_calls.agg(['sum', 'size'])
    e = d[d.game % 2 == 0].groupby('agent').att_board_calls.agg(['sum', 'size'])
    ag = sorted(set(o.index) & set(e.index))
    if len(ag) < 8 or o.loc[ag, 'sum'].sum() < 20 or e.loc[ag, 'sum'].sum() < 20:
        continue
    r1 = (o.loc[ag, 'sum'] / o.loc[ag, 'size']).values
    r2 = (e.loc[ag, 'sum'] / e.loc[ag, 'size']).values
    if r1.std() == 0 or r2.std() == 0:
        continue
    rows.append(dict(sandbox=sb, r=float(np.corrcoef(r1, r2)[0, 1])))
W = pd.DataFrame(rows).merge(S[['sandbox', 'model', 'effort', 'condition']], on='sandbox')
W.to_csv(B.AN / 'tables/bcm_within_sandbox_stability.csv', index=False)
print('\n== odd/even split-half correlation of per-agent call rate, within sandbox')
print(W.groupby(['model', 'effort', 'condition']).r.agg(['size', 'mean', 'min', 'max']).round(3).to_string())

# 3. cross-sandbox: does an agent *id* carry use from one sandbox to another?
rate = dec.groupby(['sandbox', 'agent']).att_board_calls.agg(['sum', 'size'])
rate['rate'] = rate['sum'] / rate['size']
piv = rate.reset_index().pivot(index='agent', columns='sandbox', values='rate')
cors = []
cols = list(piv.columns)
for i, j in itertools.combinations(range(len(cols)), 2):
    a, b = piv[cols[i]], piv[cols[j]]
    ok = a.notna() & b.notna()
    if ok.sum() >= 6 and a[ok].std() > 0 and b[ok].std() > 0:
        cors.append(float(np.corrcoef(a[ok], b[ok])[0, 1]))
print(f'\n== cross-sandbox correlation of per-id call rate: {len(cors)} sandbox pairs sharing >=6 ids, '
      f'mean r = {np.mean(cors):.3f}, median {np.median(cors):.3f}, '
      f'share of pairs with r > 0.3: {np.mean(np.array(cors) > 0.3):.3f}')
ov = [len(set(piv[c1].dropna().index) & set(piv[c2].dropna().index))
      for c1, c2 in itertools.combinations(cols, 2)]
print('shared LLM ids between two sandboxes: mean', round(np.mean(ov), 2), 'of 12')
