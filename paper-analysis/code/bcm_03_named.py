"""Does an agent named in a post behave differently on its next decision?

For every post that names another LLM agent in the same sandbox, find that agent's first
decision after the post's timestamp and compare its cooperation with (a) that agent's
cooperation on its own immediately preceding decision and (b) that agent's mean cooperation
over every other played decision in the same sandbox. Paired within sandbox, exact sign-flip
over sandboxes. Unit of the test = sandbox; the post level is exploratory.
"""
import re, numpy as np, pandas as pd, itertools
import bcm_common as B

AID = re.compile(r'\bA\d\d\b')
P = pd.read_parquet(B.AN / 'data/bcm_posts.parquet')
P['text'] = P.text.fillna('')
P['ts'] = pd.to_datetime(P.ts, format='ISO8601', utc=True)

dec = pd.read_parquet(B.AN / 'data/decisions.parquet', columns=[
    'sandbox', 'dataset', 'paraphrase', 'game', 'round', 'agent', 'action', 'is_played',
    'att_read_calls', 'ts'])
dec = dec[(dec.dataset == 'prereg') & (dec.paraphrase != 'p4') & dec.is_played]
dec = dec[dec.sandbox.isin(set(P.sandbox))].copy()
dec['ts'] = pd.to_datetime(dec.ts, format='ISO8601', utc=True)
dec['coop'] = (dec.action == 'C').astype(float)
dec = dec.sort_values(['sandbox', 'agent', 'ts'])

idx = {}
for (sb, a), d in dec.groupby(['sandbox', 'agent']):
    idx[(sb, a)] = (d.ts.values, d.coop.values, d.att_read_calls.values)

llm_agents = {}
for sb, m in P.groupby('sandbox').model.first().items():
    full = 'deepseek-ai/DeepSeek-V4-Flash-0731' if m == 'DeepSeek' else 'XiaomiMiMo/MiMo-V2.5-Pro'
    llm_agents[sb] = set(B.llm_agents(sb, full))

rows = []
for r in P.itertuples():
    named = {x for x in AID.findall(r.text)} - {r.agent}
    for a in named & llm_agents[r.sandbox]:
        k = (r.sandbox, a)
        if k not in idx:
            continue
        ts, coop, rd = idx[k]
        j = np.searchsorted(ts, np.datetime64(r.ts), side='right')
        if j >= len(ts):
            continue
        rows.append(dict(sandbox=r.sandbox, model=r.model, effort=r.effort, condition=r.condition,
                         state=r.state, named=a, post_n=r.n,
                         next_coop=coop[j], next_read=rd[j] > 0,
                         prev_coop=(coop[j - 1] if j > 0 else np.nan), pos=j))
N = pd.DataFrame(rows)
N.to_parquet(B.AN / 'data/bcm_named_events.parquet', index=False)
print('named-agent events:', len(N), 'posts naming another LLM agent:', N.post_n.nunique())

# baseline: agent's mean cooperation over its played decisions in the sandbox
base = dec.groupby(['sandbox', 'agent']).coop.mean().rename('agent_base')
N = N.join(base, on=['sandbox', 'named'])

def signflip(v):
    v = np.asarray([x for x in v if not np.isnan(x) and x != 0])
    k = len(v)
    if k == 0:
        return 1.0
    obs = abs(np.mean(v))
    cnt = sum(1 for s in itertools.product([1, -1], repeat=k) if abs(np.mean(v * np.array(s))) >= obs - 1e-12)
    return cnt / 2 ** k

out = []
for (m, e, c), d in N.groupby(['model', 'effort', 'condition']):
    per_sb = d.groupby('sandbox').apply(
        lambda x: pd.Series(dict(n=len(x),
                                 d_vs_base=(x.next_coop - x.agent_base).mean(),
                                 d_vs_prev=(x.next_coop - x.prev_coop).mean(),
                                 d_vs_base_read=((x.next_coop - x.agent_base)[x.next_read].mean()
                                                 if x.next_read.any() else np.nan))),
        include_groups=False)
    out.append(dict(model=m, effort=e, condition=c, sandboxes=len(per_sb), events=int(per_sb.n.sum()),
                    mean_d_vs_base=per_sb.d_vs_base.mean(),
                    pos_vs_base=int((per_sb.d_vs_base > 0).sum()),
                    p_vs_base=signflip(per_sb.d_vs_base.values),
                    mean_d_vs_prev=per_sb.d_vs_prev.mean(),
                    pos_vs_prev=int((per_sb.d_vs_prev > 0).sum()),
                    p_vs_prev=signflip(per_sb.d_vs_prev.values),
                    mean_d_vs_base_readers=per_sb.d_vs_base_read.mean()))
O = pd.DataFrame(out)
O.to_csv(B.AN / 'tables/bcm_named_agent_next_action.csv', index=False)
print(O.round(4).to_string())

# ---- short complete threads: all posts of one game, 3-6 of them
P2 = P.sort_values(['sandbox', 'n'])
th = P2.groupby(['sandbox', 'game']).agg(posts=('n', 'size'), agents=('agent', 'nunique'),
                                         maxlen=('text', lambda s: s.str.len().max()),
                                         model=('model', 'first'), condition=('condition', 'first'),
                                         effort=('effort', 'first')).reset_index()
cand = th[(th.posts.between(3, 6)) & (th.maxlen < 320)]
for key, lab in [(('DeepSeek', 'forbidden', 'off'), 'ds-forbidden'),
                 (('MiMo', 'forbidden', 'off'), 'mimo-forbidden'),
                 (('DeepSeek', 'permitted', 'off'), 'ds-permitted'),
                 (('DeepSeek', 'permitted', 'high'), 'ds-permitted-high')]:
    c = cand[(cand.model == key[0]) & (cand.condition == key[1]) & (cand.effort == key[2])]
    c = c.sort_values('agents', ascending=False).head(6)
    print('\n########', lab, len(c))
    for r in c.itertuples():
        print('--- thread', r.sandbox, 'game', r.game, 'posts', r.posts, 'agents', r.agents)
        t = P2[(P2.sandbox == r.sandbox) & (P2.game == r.game)]
        for q in t.itertuples():
            print(f'   #{q.n} r{q.round} {q.agent} (opp {q.opponent}) [{q.category}] {q.text[:300]}')
