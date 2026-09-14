"""What is exchanged on the board: categories, address, proposals, replies, growth."""
import re, pandas as pd, numpy as np
import bcm_common as B

P = pd.read_parquet(B.AN / 'data/bcm_posts.parquet')
P['text'] = P.text.fillna('')
P['cell'] = P.model + ' ' + P.effort + ' ' + P.condition

AID = re.compile(r'\bA\d\d\b')
SECOND = re.compile(r"\b(you|your|yours|you're|youre|we|we're|us|our|let's|lets)\b", re.I)
PROPOSE = re.compile(r"(let'?s|let us|i propose|proposing|propose|suggest|if you|"
                     r"both (?:pick|play|choose|go)|mutual|i'll .* you|agree)", re.I)
REPLY = re.compile(r"(your note|your post|you said|you wrote|you posted|as A\d\d|A\d\d'?s note|"
                   r"A\d\d (?:said|wrote|posted|notes)|per A\d\d|note[s]? say|notes indicate|"
                   r"reply|replying|responding to|agree with|noted by)", re.I)

def other_ids(row):
    return {x for x in AID.findall(row.text)} - {row.agent}

P['ids_other'] = [other_ids(r) for r in P.itertuples()]
P['names_other_agent'] = [len(s) > 0 for s in P.ids_other]
P['names_opponent'] = [(r.opponent in s) if str(r.opponent).startswith('A') else False
                       for r, s in zip(P.itertuples(), P.ids_other)]
P['second_person'] = P.text.str.contains(SECOND)
P['proposes'] = P.text.str.contains(PROPOSE)
P['reply_marker'] = P.text.str.contains(REPLY)
P['n_chars'] = P.text.str.len()

# a post "answers an earlier poster" if it names an agent that posted earlier on this board
# and that agent is not its own opponent (so the reference cannot be the current game alone)
prev_posters = {}
ans = []
for r in P.sort_values(['sandbox', 'n']).itertuples():
    seen = prev_posters.setdefault(r.sandbox, set())
    refs = r.ids_other & seen
    ans.append(bool(refs - {r.opponent}))
    seen.add(r.agent)
P = P.sort_values(['sandbox', 'n'])
P['names_earlier_poster'] = ans

def agg(df, keys):
    g = df.groupby(keys)
    out = g.agg(posts=('n', 'size'), mean_chars=('n_chars', 'mean'),
                names_other_agent=('names_other_agent', 'mean'),
                names_opponent=('names_opponent', 'mean'),
                second_person=('second_person', 'mean'),
                proposes=('proposes', 'mean'),
                reply_marker=('reply_marker', 'mean'),
                names_earlier_poster=('names_earlier_poster', 'mean'))
    cats = g.category.value_counts(normalize=True).unstack().fillna(0)
    return out.join(cats, rsuffix='_share').reset_index()

agg(P, ['model', 'effort', 'condition']).to_csv(B.AN / 'tables/bcm_content_by_cell.csv', index=False)
agg(P, ['model', 'effort', 'condition', 'state']).to_csv(B.AN / 'tables/bcm_content_by_cell_state.csv', index=False)
agg(P[P.category != 'uncoded'], ['model', 'effort', 'condition']).to_csv(
    B.AN / 'tables/bcm_content_by_cell_codedonly.csv', index=False)

# category counts including uncoded
ct = P.groupby(['model', 'effort', 'condition']).category.value_counts().unstack().fillna(0).astype(int)
ct.to_csv(B.AN / 'tables/bcm_categories_by_cell.csv')
print(ct.to_string())
print(agg(P, ['model', 'effort', 'condition']).round(3).to_string())

# ---- examples: spread over condition x category, mid-length posts
ex = []
for m in ['DeepSeek', 'MiMo']:
    d = P[(P.model == m) & (P.n_chars.between(40, 400))]
    for (cond, eff, cat), grp in d.groupby(['condition', 'effort', 'category']):
        grp = grp.sort_values('n_chars')
        ex.append(grp.iloc[len(grp) // 2])
E = pd.DataFrame(ex)[['model', 'condition', 'effort', 'state', 'category', 'sandbox', 'n',
                      'game', 'round', 'agent', 'opponent', 'text']]
E.to_csv(B.AN / 'tables/bcm_post_examples.csv', index=False)
print(E.groupby('model').size())

# ---- growth of the board over a sandbox
dec = pd.read_parquet(B.AN / 'data/decisions.parquet', columns=[
    'sandbox', 'dataset', 'paraphrase', 'game', 'round', 'agent', 'att_read_calls',
    'att_post_calls', 'board_size_at_read'])
dec = dec[(dec.dataset == 'prereg') & (dec.paraphrase != 'p4')]
dec = dec[dec.sandbox.isin(set(P.sandbox))]
meta = P.groupby('sandbox')[['model', 'effort', 'condition', 'state', 'block']].first()
rows = []
for sb, d in dec.groupby('sandbox'):
    q = pd.qcut(d.game.rank(method='dense'), 4, labels=[1, 2, 3, 4], duplicates='drop')
    r = d.assign(q=q).groupby('q', observed=True).agg(
        board_size_at_read=('board_size_at_read', 'mean'),
        read_rate=('att_read_calls', lambda x: (x > 0).mean()),
        post_rate=('att_post_calls', lambda x: (x > 0).mean()))
    for qq in r.index:
        rows.append(dict(sandbox=sb, quarter=int(qq), **meta.loc[sb].to_dict(),
                         **r.loc[qq].to_dict()))
G = pd.DataFrame(rows)
G.to_csv(B.AN / 'tables/bcm_board_growth_by_quarter.csv', index=False)
print(G.groupby(['model', 'effort', 'condition', 'quarter'])[
    ['board_size_at_read', 'read_rate', 'post_rate']].mean().round(3).to_string())
