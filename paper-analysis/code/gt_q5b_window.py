import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Is the 'behind' effect the score ledger or the visible opponent history?

The runner prepends the six assigned warm-up rounds to the history the agent
sees for the scored game and attributes them to THAT counterpart
(`coop/players/llm.py:_labelled_history`, `_totals`; history window = 20,
`coop/population.py:111`). So the two assigned arms differ in two ways at once:
  - running totals (behind -10 / ahead +10 / deficit -30), which never scroll out;
  - the counterpart's apparent record: behind = CD,CD,CC,CC,CC,CC (they defected
    twice), ahead = DC,DC,CC,CC,CC,CC (you defected twice), -30 = CD x6.
The warm-up leaves the 20-round window once the scored game reaches round 15.
If the arm difference is carried by the visible history it should shrink there;
if it is carried by the ledger it should persist.
"""
from __future__ import annotations
import itertools
import numpy as np, pandas as pd
from pathlib import Path

D = Path(_REPO+"/paper-analysis/data")
T = Path(_REPO+"/paper-analysis/tables")
dec = pd.read_parquet(D / "decisions.parquet",
                      columns=["dataset", "sandbox", "paraphrase", "model", "condition", "effort",
                               "score_state", "block", "round", "action", "is_played"])
dec = dec[dec.is_played & dec.action.notna() & (dec.paraphrase != "p4")].copy()
dec["C"] = (dec.action == "C").astype(float)
seg = pd.cut(dec["round"], [0, 8, 14, 100], labels=["r1-8 warmup fully visible",
                                                    "r9-14 warmup partly visible",
                                                    "r15+ warmup out of window"])
dec["seg"] = seg
DS = "deepseek-ai/DeepSeek-V4-Flash-0731"; MM = "XiaomiMiMo/MiMo-V2.5-Pro"


def exact(d):
    d = np.asarray(d, float); d = d[~np.isnan(d)]
    signs = np.array(list(itertools.product([1, -1], repeat=len(d))))
    null = (signs * d).mean(axis=1)
    return d.mean(), (np.abs(null) >= abs(d.mean()) - 1e-12).mean(), len(d), int((d > 0).sum())


def arm(ds, model, state, effort="off"):
    m = ((dec.dataset == ds) & (dec.model == model) & (dec.condition == "forbidden")
         & (dec.effort == effort) & (dec.score_state == state))
    return dec[m].groupby(["block", "seg"], observed=True)["C"].mean().unstack()


rows = []
for name, A, B in [
    ("behind - ahead (DeepSeek, forbidden, off)", arm("prereg", DS, "behind"),
     arm("prereg", DS, "ahead")),
    ("behind - ahead (MiMo, forbidden, off)", arm("prereg", MM, "behind"),
     arm("prereg", MM, "ahead")),
    ("-30 minus -10 (DeepSeek, forbidden, off, behind)",
     arm("deficit_d30", DS, "behind"), arm("prereg", DS, "behind")),
]:
    blocks = sorted(set(A.index) & set(B.index))
    for s in A.columns:
        d = (A.loc[blocks, s] - B.loc[blocks, s]).values
        obs, p, k, npos = exact(d)
        rows.append(dict(contrast=name, segment=s, mean_A=A.loc[blocks, s].mean(),
                         mean_B=B.loc[blocks, s].mean(), mean_diff=obs, n_pos=npos, k=k,
                         p_exact_signflip=p))
R = pd.DataFrame(rows)
R.to_csv(T / "gt_q5b_window.csv", index=False)
pd.set_option("display.width", 220)
print(R.round(4).to_string(index=False))
