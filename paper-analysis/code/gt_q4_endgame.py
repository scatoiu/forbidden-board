import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q4: cooperation by round index and the end-game.

Two views, because round index and game length are confounded: games stop with
prob_end 0.03 per round and at a hard cap of 30, so late rounds are a survivor
sample. View A conditions on round index over all games. View B keeps only
agent-games that reached round 30 (the cap is the only *predictable* ending) and
reads cooperation by round inside that fixed-length set. View C indexes by
rounds-remaining, which is what an agent could not know for a random stop but
could know at the cap.
"""
from __future__ import annotations
import numpy as np, pandas as pd
from pathlib import Path

D = Path(_REPO+"/paper-analysis/data")
T = Path(_REPO+"/paper-analysis/tables")
dec = pd.read_parquet(D / "decisions.parquet",
                      columns=["dataset", "sandbox", "paraphrase", "model", "condition", "effort",
                               "score_state", "opponent_type", "agent_game_uid", "round",
                               "action", "is_played"])
dec = dec[dec.is_played & dec.action.notna()].copy()
dec["C"] = (dec.action == "C").astype(float)
last = dec.groupby("agent_game_uid")["round"].max()
dec["n_rounds"] = dec.agent_game_uid.map(last)
dec["from_end"] = dec.n_rounds - dec["round"]

rows = []
for ds, sub in dec.groupby("dataset"):
    sub = sub[sub.paraphrase != "p4"] if ds == "prereg" else sub
    for view, frame, idx in [("A_all_games", sub, "round"),
                             ("B_reached_30", sub[sub.n_rounds == 30], "round"),
                             ("C_from_end", sub, "from_end")]:
        sb = frame.groupby(["sandbox", idx])["C"].mean().reset_index()
        n = frame.groupby(idx)["C"].size()
        for r, g in sb.groupby(idx):
            rows.append(dict(dataset=ds, view=view, index=int(r), coop=g["C"].mean(),
                             n_sandboxes=len(g), n_decisions=int(n[r])))
out = pd.DataFrame(rows)
out.to_csv(T / "gt_q4_rounds.csv", index=False)
pd.set_option("display.width", 200)
for v in ["A_all_games", "B_reached_30", "C_from_end"]:
    t = out[(out.dataset == "prereg") & (out.view == v)]
    print(f"== prereg {v} ==")
    print(t[["index", "coop", "n_decisions"]].head(32).round(3).to_string(index=False))

# paired per-sandbox: rounds 25-30 vs 1-24 (all games), and within reached-30 games
res = []
for ds, sub in dec.groupby("dataset"):
    sub = sub[sub.paraphrase != "p4"] if ds == "prereg" else sub
    for name, frame in [("all_games", sub), ("reached_30_only", sub[sub.n_rounds == 30])]:
        p = (frame.assign(seg=np.where(frame["round"] >= 25, "late", "early"))
             .groupby(["sandbox", "seg"])["C"].mean().unstack())
        d = (p["late"] - p["early"]).dropna()
        rng = np.random.default_rng(5)
        null = (rng.choice([1, -1], size=(200000, len(d))) * d.values).mean(axis=1)
        pv = max((np.abs(null) >= abs(d.mean())).mean(), 1 / len(null))
        res.append(dict(dataset=ds, sample=name, contrast="r25-30 minus r1-24",
                        mean_diff=d.mean(), n_pos=int((d > 0).sum()), k=len(d), p_signflip=pv))
    # final played round vs the rest, within games that reached the cap
    f = sub[sub.n_rounds == 30]
    p = (f.assign(seg=np.where(f["round"] == 30, "last", "rest"))
         .groupby(["sandbox", "seg"])["C"].mean().unstack())
    d = (p["last"] - p["rest"]).dropna()
    rng = np.random.default_rng(6)
    null = (rng.choice([1, -1], size=(200000, len(d))) * d.values).mean(axis=1)
    pv = max((np.abs(null) >= abs(d.mean())).mean(), 1 / len(null))
    res.append(dict(dataset=ds, sample="reached_30_only", contrast="round 30 minus rounds 1-29",
                    mean_diff=d.mean(), n_pos=int((d > 0).sum()), k=len(d), p_signflip=pv))
R = pd.DataFrame(res)
R.to_csv(T / "gt_q4_endgame_tests.csv", index=False)
print(R.round(4).to_string(index=False))

# --- plateau-anchored end-game tests, plus a random-stop placebo ---
extra = []
for ds, sub in dec.groupby("dataset"):
    sub = sub[sub.paraphrase != "p4"] if ds == "prereg" else sub
    f = sub[sub.n_rounds == 30]
    p = (f[f["round"] >= 20].assign(seg=np.where(f[f["round"] >= 20]["round"] == 30,
                                                 "last", "rest"))
         .groupby(["sandbox", "seg"])["C"].mean().unstack())
    d = (p["last"] - p["rest"]).dropna()
    rng = np.random.default_rng(9)
    null = (rng.choice([1, -1], size=(200000, len(d))) * d.values).mean(axis=1)
    extra.append(dict(dataset=ds, test="cap games: round 30 vs rounds 20-29",
                      mean_diff=d.mean(), n_pos=int((d > 0).sum()), k=len(d),
                      p_signflip=max((np.abs(null) >= abs(d.mean())).mean(), 1 / len(null))))
    # placebo: games that stopped early (random stop, unpredictable) -- last played round
    # vs that game's rounds 20..n-1, restricted to games of length 20..29
    e = sub[(sub.n_rounds >= 20) & (sub.n_rounds <= 29) & (sub["round"] >= 20)]
    p = (e.assign(seg=np.where(e["round"] == e.n_rounds, "last", "rest"))
         .groupby(["sandbox", "seg"])["C"].mean().unstack())
    d = (p["last"] - p["rest"]).dropna()
    null = (np.random.default_rng(10).choice([1, -1], size=(200000, len(d))) * d.values).mean(axis=1)
    extra.append(dict(dataset=ds, test="random-stop placebo: last round vs 20..n-1",
                      mean_diff=d.mean(), n_pos=int((d > 0).sum()), k=len(d),
                      p_signflip=max((np.abs(null) >= abs(d.mean())).mean(), 1 / len(null))))
E = pd.DataFrame(extra)
E.to_csv(T / "gt_q4_endgame_placebo.csv", index=False)
print(E.round(4).to_string(index=False))
