"""Objection (g): what the 76% prohibition-recall number establishes.
Objection (i): post content in forbidden games (announcement vs proposal), agent concentration,
board growth over the sandbox, and the round profile of first use."""
import pandas as pd, numpy as np
from adv_common import games, decisions, prereg, TABLES, FZ

pd.set_option('display.width',250,'display.max_columns',40,'display.max_rows',200)

# ---- (g) recall coded ----
rc = pd.read_csv(FZ/'tables/recall_coded.csv')
print('recall_coded rows:', len(rc), '| codes:', rc.recall_code.value_counts().to_dict())
f = rc[(rc.condition=='forbidden')]
t = f.groupby(['model','effort']).agg(n=('game_uid','size'), scored_correct=('scored_correct','mean'),
    names_board=('names_board','mean'), denies=('denies','mean'),
    prohibition_language=('prohibition_language','mean'), no_answer=('no_answer','mean')).reset_index()
t.to_csv(TABLES/'adv_g_recall.csv',index=False)
print('\n=== (g) prohibition recall, forbidden condition (asked with the prohibition still in the system prompt) ===')
print(t.to_string(index=False))
# cross-tab: recall correct x attempted use, off effort
x = f[(f.effort=='off')]
ct = pd.crosstab([x.model,x.scored_correct], x.attempted_use, normalize='index')
n  = pd.crosstab([x.model,x.scored_correct], x.attempted_use)
print('\nrecall x attempted use, off effort (row %):'); print((100*ct).round(1).to_string()); print(n.to_string())
ct.to_csv(TABLES/'adv_g_recall_x_use.csv')

# ---- (i1) post content ----
pc = pd.read_csv(FZ/'tables/posts_coded.csv', usecols=['model','condition','effort','score_state','paraphrase','category','text','game_uid','round'])
print('\n=== (i1) post categories by condition/model ===')
cat = pc.groupby(['model','condition','effort']).category.value_counts(normalize=True).unstack().fillna(0)
ncat = pc.groupby(['model','condition','effort']).size().rename('n_posts')
out = cat.join(ncat)
out.to_csv(TABLES/'adv_i_post_categories.csv')
print((100*cat).round(1).join(ncat).to_string())
print('\nexample forbidden-off posts by model/category (first 2 each, truncated):')
for (m,c),grp in pc[(pc.condition=='forbidden')&(pc.effort=='off')].groupby(['model','category']):
    for txt in grp.text.dropna().head(2):
        print(f'  [{m.split("/")[-1]} | {c}] {str(txt)[:150].replace(chr(10)," ")}')
