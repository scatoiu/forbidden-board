import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Phase 0 reconciliation: compact tables vs the frozen report counts and block rates."""
import pandas as pd, numpy as np, json
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]
FZ=Path(_REPO+'/reports/final-20260913T144509Z')
d=pd.read_parquet(HERE/'data/decisions.parquet'); g=pd.read_parquet(HERE/'data/agent_games.parquet')
p=d[(d.dataset=='prereg')&(d.paraphrase!='p4')]; pg=g[(g.dataset=='prereg')&(g.paraphrase!='p4')]
lines=['# Phase 0 extraction check (compact tables vs frozen report)','',
 'Frozen report: `reports/final-20260913T144509Z/SUMMARY.md`. Compact tables: `analyses/data/` (PROVENANCE.json).','',
 '## Counts (prereg dataset, p4 placement cells X1/Y1 excluded as in the frozen run)','',
 '| quantity | frozen | compact | match |','|---|---|---|---|']
checks=[('sandboxes',69,p.sandbox.nunique()),('scored model decisions',357433,len(p)),('played decisions',356352,int(p.is_played.sum())),('LLM agent-games',19044,len(pg))]
ok=True
for name,f,c in checks:
    m = f==c; ok&=m; lines.append(f'| {name} | {f:,} | {c:,} | {"yes" if m else "NO"} |')
# games per complete sandbox
per=pg[pg.sandbox_complete.astype(bool)].groupby('sandbox').agg(games=('game_uid','nunique'),ag=('agent_game_uid','count'))
lines+=['',f'Complete sandboxes: {len(per)}; LLM-involving games per sandbox: modal {per.games.mode().iloc[0]} (range {per.games.min()}–{per.games.max()}); agent-games modal {per.ag.mode().iloc[0]} (range {per.ag.min()}–{per.ag.max()}).']
# primary endpoint per sandbox vs block_contrasts
def endpoint(gg):
    obs=gg[gg.game_observed.astype(bool)]
    per=obs.groupby('game_uid')['attempted_board_calls'].sum()>0
    return per.mean()
ep=pg.groupby('sandbox').apply(endpoint).rename('rate').reset_index()
meta=pg.groupby('sandbox').agg(model=('model','first'),condition=('condition','first'),effort=('effort','first'),state=('score_state','first'),block=('block','first')).reset_index()
ep=ep.merge(meta,on='sandbox')
bc=pd.read_csv(FZ/'tables/block_contrasts.csv'); bc=bc[bc.quality_policy=='keep_all_disclosed_deviation']
lines+=['','## Registered-family block rates (frozen `block_contrasts.csv`, keep-all view) vs recomputed from compact tables','','| member | model | block | arm | frozen | compact | diff |','|---|---|---|---|---|---|---|']
maxdiff=0
short={'DeepSeek-V4-Flash-0731':'deepseek-ai/DeepSeek-V4-Flash-0731','MiMo-V2.5-Pro':'XiaomiMiMo/MiMo-V2.5-Pro'}
for _,r in bc.iterrows():
    blk=r.block.split('/')[-1]; cond=r.condition
    for lvl,rate in ((r.hi_level,r.hi_rate),(r.lo_level,r.lo_rate)):
        if r.member.startswith('A_'):
            sel=ep[(ep.block==blk)&(ep.condition==cond)&(ep.effort==lvl)&(ep.state=='behind')&(ep.model==short[r.model])]
        else:
            sel=ep[(ep.block==blk)&(ep.condition==cond)&(ep.effort=='off')&(ep.state==lvl)&(ep.model==short[r.model])]
        c=sel.rate.iloc[0] if len(sel)==1 else np.nan
        diff=abs(c-rate) if not np.isnan(c) else np.nan
        maxdiff=max(maxdiff, 9 if np.isnan(diff) else diff)
        lines.append(f'| {r.member} | {r.model} | {blk} | {lvl} | {rate:.4f} | {c:.4f} | {diff:.4f} |')
lines+=['',f'Max absolute difference across {len(bc)*2} block arms: {maxdiff:.4f} (rates rounded to 4 dp in the frozen table).','']
ok &= maxdiff<0.0001
lines+=[f'## Verdict: {"PASS - the compact tables reproduce the frozen counts and every registered block rate" if ok else "FAIL - see mismatches above"}','',
 'Notes: the compact `prereg` dataset also carries the two p4 placement sandboxes (X1, Y1); filter `paraphrase != "p4"` to match the frozen pre-registered dataset. Replication (24 sandboxes), low_arm (6) and deficit_d30 (6) are separate `dataset` labels and are never pooled with prereg.']
(HERE/'00-extraction-check.md').write_text('\n'.join(lines)); print('\n'.join(lines))
