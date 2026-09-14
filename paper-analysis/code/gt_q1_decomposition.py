import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Where the LLM seat's shortfall against a TitForTat-in-seat baseline comes from.

Each seat plays 23 opponents: 11 other seats, 4 TitForTat, 2 each of Grudger,
AlwaysDefect, Random, Pavlov. Weighting the per-opponent score-per-round gap
(observed LLM, tables/gt_q7_llm_vs_baseline.csv) by that opponent share
decomposes the whole-field gap. Exploratory: the weights use the seat count, not
the realised round counts, which differ slightly because games stop at random.
"""
from __future__ import annotations
import pandas as pd
from pathlib import Path

T = Path(_REPO+"/paper-analysis/tables")
W = {"LLM": 11 / 23, "TitForTat": 4 / 23, "Grudger": 2 / 23, "AlwaysDefect": 2 / 23,
     "Random": 2 / 23, "Pavlov": 2 / 23}
a = pd.read_csv(T / "gt_q7_llm_vs_baseline.csv")
a = a[a.dataset == "prereg"].set_index("opponent_type")
rows = []
for opp, w in W.items():
    rows.append(dict(opponent_type=opp, seat_share=w, llm_spr=a.loc[opp, "llm_spr"],
                     tft_seat_spr=a.loc[opp, "base_TitForTat"],
                     gap=a.loc[opp, "llm_minus_TitForTat"],
                     contribution=w * a.loc[opp, "llm_minus_TitForTat"]))
d = pd.DataFrame(rows).sort_values("contribution")
d.loc[len(d)] = dict(opponent_type="TOTAL", seat_share=1.0, llm_spr=float("nan"),
                     tft_seat_spr=float("nan"), gap=float("nan"),
                     contribution=d.contribution.sum())
d.to_csv(T / "gt_q1_decomposition.csv", index=False)
print(d.round(4).to_string(index=False))
