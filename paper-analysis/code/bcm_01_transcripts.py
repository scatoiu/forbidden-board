"""Board transcripts per sandbox + board_agents_by_block tables.

Writes analyses/transcripts/<sandbox>.md (67 sandboxes with a board) and
analyses/tables/board_agents_by_block.csv, board_agents_by_block_summary.csv.
"""
import pandas as pd, numpy as np
import bcm_common as B

TRUNC = 400
sbx = B.prereg_sandboxes()
boardy = sbx[sbx.condition != 'absent'].copy()
print('sandboxes with a board:', len(boardy), '| absent excluded:',
      sbx[sbx.condition == 'absent'].sandbox.tolist())

dec = pd.read_parquet(B.AN / 'data/decisions.parquet', columns=[
    'sandbox', 'generation', 'game', 'agent', 'round', 'opponent', 'opponent_model',
    'opponent_type', 'pair_type', 'is_played', 'action', 'att_read_calls',
    'att_post_calls', 'att_board_calls', 'board_size_at_read', 'dataset', 'paraphrase'])
dec = dec[(dec.dataset == 'prereg') & (dec.paraphrase != 'p4')]
dec = dec[dec.sandbox.isin(set(boardy.sandbox))]
print('decisions rows in scope:', len(dec))

pc = pd.read_csv(B.FROZEN / 'posts_coded.csv',
                 usecols=['sandbox', 'generation', 'game', 'round', 'agent', 'text', 'category'])
pc = pc.drop_duplicates(subset=['sandbox', 'generation', 'game', 'round', 'agent', 'text'])
cat = {(r.sandbox, r.generation, r.game, r.round, r.agent, r.text): r.category
       for r in pc.itertuples()}
cat_loose = {}
for r in pc.itertuples():
    cat_loose.setdefault((r.sandbox, r.generation, r.game, r.round, r.agent), r.category)
print('coded posts:', len(pc))

# opponent per (sandbox, generation, game, agent)
opp = (dec.groupby(['sandbox', 'generation', 'game', 'agent'])
          [['opponent', 'opponent_model', 'opponent_type']].first())
oppmap = {k: v for k, v in zip(opp.index, opp.itertuples(index=False))}

agent_rows, summary_rows, post_rows = [], [], []

for _, s in boardy.iterrows():
    sb = s.sandbox
    d = dec[dec.sandbox == sb]
    board = B.board_entries(sb)
    if len(board):
        board = board.rename(columns={'_source': 'src', '_n': 'num'})
    man = B.manifest(sb)
    llms = B.llm_agents(sb, s.model)
    # ---- per agent activity
    g = d.groupby('agent')
    per = g.agg(games_played=('game', 'nunique'),
                att_reads=('att_read_calls', 'sum'),
                att_posts=('att_post_calls', 'sum'),
                att_calls=('att_board_calls', 'sum')).reindex(llms).fillna(0)
    any_call = (d[d.att_board_calls > 0].groupby('agent')['game'].nunique()
                .reindex(llms).fillna(0))
    first = (d[d.att_board_calls > 0].sort_values(['game', 'round'])
             .groupby('agent')[['game', 'round']].first().reindex(llms))
    tot_calls = per.att_calls.sum()
    for a in llms:
        agent_rows.append(dict(
            model=B.MODEL_SHORT[s.model], condition=s.condition, effort=s.effort,
            state=s.score_state, block=s.block, wording=s.paraphrase, sandbox=sb, agent=a,
            games_played=int(per.at[a, 'games_played']),
            games_with_board_attempt=int(any_call[a]),
            attempted_reads=int(per.at[a, 'att_reads']),
            attempted_posts=int(per.at[a, 'att_posts']),
            attempted_board_calls=int(per.at[a, 'att_calls']),
            first_attempt_game=(None if pd.isna(first.at[a, 'game']) else int(first.at[a, 'game'])),
            first_attempt_round=(None if pd.isna(first.at[a, 'round']) else int(first.at[a, 'round'])),
            share_of_sandbox_board_calls=(per.at[a, 'att_calls'] / tot_calls if tot_calls else 0.0)))
    shares = sorted((per.att_calls / tot_calls if tot_calls else per.att_calls * 0), reverse=True)
    # ---- transcript
    lines = []
    lines.append(f'# Board transcript — {sb}')
    lines.append('')
    lines.append(f'- **model** {B.MODEL_SHORT[s.model]} (`{s.model}`)')
    lines.append(f'- **condition** {s.condition} · **reasoning effort** {s.effort} · '
                 f'**assigned score state** {s.score_state}')
    lines.append(f'- **block** {s.block} · **wording** {B.WORDING[s.paraphrase]} · **seed** {s.seed}')
    lines.append(f'- **sandbox spec** 24 agents = 12 {B.MODEL_SHORT[s.model]} + '
                 f'TitForTat x4, Grudger x2, AlwaysDefect x2, Random x2, Pavlov x2; '
                 f'tools {", ".join(man["tools"])}; answer cap {man["answer_tokens"]} tokens; '
                 f'board read limit {man["board_read_limit"]} entries; '
                 f'max {man["max_tool_iterations"]} tool iterations per decision')
    lines.append(f'- **LLM agent ids in this sandbox** {", ".join(llms)} '
                 f'(ids are reassigned by a shuffle in every sandbox, so A07 here is not A07 elsewhere)')
    lines.append(f'- **games with at least one played decision** {d.game.nunique()} · '
                 f'**board calls attempted** {int(tot_calls)} '
                 f'({int(per.att_reads.sum())} reads, {int(per.att_posts.sum())} posts)')
    if len(board) and (board.src == 'repair').any():
        nr = int((board.src == 'repair').sum())
        lines.append(f'- **note** this sandbox was partly re-run after provider errors; the board '
                     f'below is the frozen merge: original entries whose game was replayed are '
                     f'dropped and {nr} entries come from the repair run (marked `[repair]`)')
    lines.append('')
    lines.append('@@TRUNCLINE@@')
    lines.append('')
    lines.append('## Transcript (posting order)')
    lines.append('')
    n_trunc = 0
    if not len(board):
        lines.append('_No post reached this board._')
    else:
        for e in board.itertuples():
            key = (sb, e.generation, e.game, e.round, e.agent)
            c = cat.get(key + (e.text,), cat_loose.get(key, 'uncoded'))
            o = oppmap.get((sb, e.generation, e.game, e.agent))
            if o is None:
                opps = 'unknown'
            elif str(o.opponent_model).startswith('script:'):
                opps = o.opponent_model
            else:
                opps = o.opponent
            t = e.text if isinstance(e.text, str) else ''
            t = t.replace('\n', ' ').strip()
            trunc = len(t) > TRUNC
            if trunc:
                t = t[:TRUNC] + '…'
                n_trunc += 1
            tag = ' [repair]' if e.src == 'repair' else ''
            lines.append(f'`#{e.num}` · game {e.game} · round {e.round} · agent {e.agent} '
                         f'(opponent: {opps}) · {c}{tag} · {t}')
            post_rows.append(dict(sandbox=sb, model=B.MODEL_SHORT[s.model], condition=s.condition,
                                  effort=s.effort, state=s.score_state, block=s.block,
                                  wording=s.paraphrase, n=e.num, game=e.game, round=e.round,
                                  agent=e.agent, opponent=opps, category=c, ts=e.ts,
                                  source=e.src, text=(e.text if isinstance(e.text, str) else '')))
    lines.append('')
    lines.append('## Reads')
    lines.append('')
    lines.append('One line per LLM agent: attempted `notes_read` calls, and the games in which it '
                 'called (attempt union, so a read lost to a retry still counts).')
    lines.append('')
    dr = d[d.att_read_calls > 0]
    for a in llms:
        n = int(per.at[a, 'att_reads'])
        gs = sorted(dr[dr.agent == a].game.unique().tolist())
        gtxt = ('games ' + ', '.join(str(x) for x in gs)) if gs else 'no game'
        lines.append(f'- {a}: {n} read calls in {len(gs)} game(s) — {gtxt}')
    tl = (f'**Posts delivered to the board: {len(board)}.** {n_trunc} post(s) run past {TRUNC} '
          f'characters; those are cut at {TRUNC} characters and end with an ellipsis, and nothing '
          f'else in the text is altered except newlines, which are folded to spaces.')
    lines = [tl if x == '@@TRUNCLINE@@' else x for x in lines]
    (B.AN / 'transcripts' / f'{sb}.md').write_text('\n'.join(lines) + '\n')

    nattempt = int((any_call > 0).sum())
    summary_rows.append(dict(
        model=B.MODEL_SHORT[s.model], condition=s.condition, effort=s.effort,
        state=s.score_state, block=s.block, wording=s.paraphrase, sandbox=sb,
        n_llm_agents=len(llms), n_agents_attempted=nattempt,
        top3_share_of_board_calls=float(sum(shares[:3])),
        total_board_calls=int(tot_calls), total_attempted_reads=int(per.att_reads.sum()),
        total_attempted_posts=int(per.att_posts.sum()),
        posts_on_board=len(board),
        posts_coded=int(sum(1 for r in post_rows if r['sandbox'] == sb and r['category'] != 'uncoded')),
        cat_directive=int(sum(1 for r in post_rows if r['sandbox'] == sb and r['category'] == 'directive')),
        cat_opponent_info=int(sum(1 for r in post_rows if r['sandbox'] == sb and r['category'] == 'opponent_info')),
        cat_identity=int(sum(1 for r in post_rows if r['sandbox'] == sb and r['category'] == 'identity')),
        cat_other=int(sum(1 for r in post_rows if r['sandbox'] == sb and r['category'] == 'other')),
        cat_uncoded=int(sum(1 for r in post_rows if r['sandbox'] == sb and r['category'] == 'uncoded'))))
    print(sb, len(board), nattempt, flush=True)

pd.DataFrame(agent_rows).to_csv(B.AN / 'tables/board_agents_by_block.csv', index=False)
pd.DataFrame(summary_rows).to_csv(B.AN / 'tables/board_agents_by_block_summary.csv', index=False)
pd.DataFrame(post_rows).to_parquet(B.AN / 'data/bcm_posts.parquet', index=False)
print('rows:', len(agent_rows), len(summary_rows), len(post_rows))
