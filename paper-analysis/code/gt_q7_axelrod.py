import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q7 matched control: the same 24-seat round-robin with the LLM seats replaced by a
script baseline, so the LLM's standing in Q1 has a reference point.

Same construction as the live runner (`coop/population.py:463`): axl.Match,
turns=30, prob_end=0.03, default axelrod game (R,S,T,P)=(3,0,5,1), noise=0,
population = 12 seats + TitForTat x4, Grudger x2, AlwaysDefect x2, Random x2,
Pavlov x2. Matches are pairwise and independent (one generation, no
reproduction), so per-opponent results do not depend on how the other seats are
filled; only the whole-field standing does.

Seeds 1..20; match seed = hash of (baseline, seed, pairing index), recorded.
Out: tables/gt_q7_baseline_seats.csv, tables/gt_q7_baseline_pairs.csv
"""
from __future__ import annotations
import itertools
import axelrod as axl
import pandas as pd
from pathlib import Path

T = Path(_REPO+"/paper-analysis/tables")
SEEDS = list(range(1, 21))
TURNS, PROB_END = 30, 0.03
GAME = axl.Game()  # (3, 0, 5, 1)
SCRIPTS = ([("TitForTat", axl.TitForTat)] * 4 + [("Grudger", axl.Grudger)] * 2
           + [("AlwaysDefect", axl.Defector)] * 2 + [("Random", axl.Random)] * 2
           + [("Pavlov", axl.WinStayLoseShift)] * 2)
BASELINES = {"TitForTat": axl.TitForTat, "Random": axl.Random,
             "AlwaysDefect": axl.Defector, "Grudger": axl.Grudger,
             "Pavlov": axl.WinStayLoseShift}

seat_rows, pair_rows = [], []
for bname, bcls in BASELINES.items():
    for seed in SEEDS:
        roster = [(f"SEAT:{bname}", bcls)] * 12 + SCRIPTS
        agg = {i: [0, 0] for i in range(24)}            # [points, rounds]
        pagg: dict[tuple, list] = {}
        for idx, (i, j) in enumerate(itertools.combinations(range(24), 2)):
            pi, pj = roster[i][1](), roster[j][1]()
            m = axl.Match((pi, pj), turns=TURNS, prob_end=PROB_END, game=GAME,
                          seed=(hash((bname, seed, idx)) % (2 ** 31)))
            inter = m.play()
            si, sj = m.final_score() or (0, 0)
            n = len(inter)
            for k, s in ((i, si), (j, sj)):
                agg[k][0] += s; agg[k][1] += n
            ti = "SEAT" if i < 12 else roster[i][0]
            tj = "SEAT" if j < 12 else roster[j][0]
            oi = "SEAT" if j < 12 else roster[j][0]
            oj = "SEAT" if i < 12 else roster[i][0]
            for (t, o, s, c) in ((ti, oi, si, sum(1 for a, _ in inter if a == axl.Action.C)),
                                 (tj, oj, sj, sum(1 for _, b in inter if b == axl.Action.C))):
                key = (t, o)
                pagg.setdefault(key, [0, 0, 0])
                pagg[key][0] += s; pagg[key][1] += n; pagg[key][2] += c
        for k, (pts, n) in agg.items():
            seat_rows.append(dict(baseline=bname, seed=seed, seat=k,
                                  seat_type="SEAT" if k < 12 else roster[k][0],
                                  total_score=pts, rounds=n, score_per_round=pts / n))
        for (t, o), (pts, n, c) in pagg.items():
            pair_rows.append(dict(baseline=bname, seed=seed, seat_type=t, opp_seat_type=o,
                                  score=pts, rounds=n, score_per_round=pts / n, coop=c / n))

S = pd.DataFrame(seat_rows); P = pd.DataFrame(pair_rows)
S.to_csv(T / "gt_q7_baseline_seats.csv", index=False)
P.to_csv(T / "gt_q7_baseline_pairs.csv", index=False)
pd.set_option("display.width", 220)
print("axelrod", axl.__version__)
print("== whole-field standing, score per round, mean over 20 seeds ==")
print(S.groupby(["baseline", "seat_type"])["score_per_round"].mean().unstack().round(3))
print("\n== SEAT score per round against each opponent type (20 seeds) ==")
print(P[P.seat_type == "SEAT"].pivot_table(index="baseline", columns="opp_seat_type",
                                           values="score_per_round").round(3))
print("\n== SEAT cooperation against each opponent type ==")
print(P[P.seat_type == "SEAT"].pivot_table(index="baseline", columns="opp_seat_type",
                                           values="coop").round(3))
