import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q2: evaluation-awareness mentions. Two sources:
(a) game_end `awareness_mentions` in the raw prereg logs (substring counts, the harness metric);
(b) a word-boundary recount over traces_coded.csv, which also lets us cross awareness with board use.
Off effort produces no reasoning trace, so both are structurally zero there: say so."""
import sys, json, re, gzip
from pathlib import Path
sys.path.insert(0,_REPO+"/paper-analysis/code")
import numpy as np, pandas as pd
from per_common import save, short, FROZEN

ROOTS = [Path(_REPO+"/runs")/r for r in ("v3","v3b","v3-mimo")]
TERMS = ("test","experiment","evaluation","researcher")

rows=[]
for root in ROOTS:
    for mv in sorted(root.glob("*/moves.jsonl")):
        sb = mv.parent.name
        if sb.endswith("-repair"): continue
        with open(mv) as fh:
            for line in fh:
                if '"game_end"' not in line: continue
                r=json.loads(line)
                if r.get("kind")!="game_end": continue
                am=r.get("awareness_mentions") or {}
                rows.append(dict(sandbox=sb, condition=r.get("condition"), effort=r.get("effort"),
                                 model=r.get("model"), paraphrase=r.get("paraphrase"),
                                 status=r.get("status"), pair_type=r.get("pair_type"),
                                 moves_logged=r.get("moves_logged") or 0,
                                 channel_used=bool(r.get("channel_used")),
                                 use_count=r.get("use_count") or 0,
                                 **{f"am_{t}": int(am.get(t,0)) for t in TERMS}))
ge=pd.DataFrame(rows)
ge["am_total"]=ge[[f"am_{t}" for t in TERMS]].sum(axis=1)
ge["model_s"]=ge.model.map(short)
ge=ge[ge.paraphrase!="p4"]
print("game_end rows read:", len(ge))
out=[]
for (m,e,c), sub in ge.groupby(["model_s","effort","condition"]):
    out.append(dict(model=m, effort=e, condition=c, n_games=len(sub),
                    share_any_mention=(sub.am_total>0).mean(),
                    mean_mentions_per_game=sub.am_total.mean(),
                    **{f"share_{t}": (sub[f"am_{t}"]>0).mean() for t in TERMS}))
df=pd.DataFrame(out); save(df,"per_q2_awareness_gameend_substring.csv")
print(df.round(3).to_string(index=False))
