import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q5 (punishing environments by proxy) and Q6 (effort and cooperation) as paired
block contrasts with an exact sign-flip over the six paraphrase blocks (2^-5 =
0.03125 floor, as pre-registered for the board endpoint).

Outcome family (per sandbox: mean over that sandbox's observed LLM agent-games):
  own_coop_played, spr (= score / rounds), round1_coop, retaliation_rate,
  forgiveness_rate, mutual_D, nice.
Each contrast pairs two sandboxes that share a block id and differ in exactly
one factor. Datasets are never pooled; a cross-dataset contrast is labelled.
"""
from __future__ import annotations
import itertools
import numpy as np, pandas as pd
from pathlib import Path

D = Path(_REPO+"/paper-analysis/data")
T = Path(_REPO+"/paper-analysis/tables")
ag = pd.read_parquet(D / "agent_games.parquet")
ag = ag[ag.game_observed & (ag.n_played > 0)].copy()
# the two p4 placement cells share block id B1 with the pre-registered B1 sandboxes
# and are excluded from every block contrast, as in the frozen report.
ag = ag[ag.paraphrase != "p4"].copy()
ag["spr"] = ag.score / ag.rounds
ag["opp_spr"] = ag.opp_score / ag.rounds
ag["mutual_D"] = ag.n_DD / ag.n_played
ag["nice"] = ag.first_defector.isin(["opponent", "none"]).astype(float)
OUT = ["own_coop_played", "spr", "opp_spr", "round1_coop", "retaliation_rate",
       "forgiveness_rate", "mutual_D", "nice"]

sb = ag.groupby(["dataset", "sandbox", "block", "model", "condition", "effort",
                 "score_state"])[OUT].mean().reset_index()
sb_opp = ag.groupby(["dataset", "sandbox", "block", "model", "condition", "effort",
                     "score_state", "opponent_type"])[OUT].mean().reset_index()


def exact_signflip(d):
    d = np.asarray(d, float); d = d[~np.isnan(d)]
    k = len(d)
    if k == 0: return np.nan, np.nan, 0, 0
    signs = np.array(list(itertools.product([1, -1], repeat=k)))
    null = (signs * d).mean(axis=1)
    obs = d.mean()
    return obs, (np.abs(null) >= abs(obs) - 1e-12).mean(), k, int((d > 0).sum())


def contrast(name, A, B, frame=sb, opp=None):
    """A minus B; each is a dict of column filters. Pairs on block."""
    f = frame if opp is None else frame[frame.opponent_type == opp]
    def pick(sel):
        m = np.ones(len(f), bool)
        for k, v in sel.items():
            m &= (f[k] == v).values
        return f[m].set_index("block")
    a, b = pick(A), pick(B)
    blocks = sorted(set(a.index) & set(b.index))
    rows = []
    for y in OUT:
        d = (a.loc[blocks, y] - b.loc[blocks, y]).values
        obs, p, k, npos = exact_signflip(d)
        rows.append(dict(contrast=name, opponent_type=opp or "all", outcome=y,
                         mean_diff=obs, n_pos=npos, k=k, p_exact_signflip=p,
                         mean_A=a.loc[blocks, y].mean(), mean_B=b.loc[blocks, y].mean(),
                         per_block_A=";".join(f"{v:.3f}" for v in a.loc[blocks, y]),
                         per_block_B=";".join(f"{v:.3f}" for v in b.loc[blocks, y])))
    return rows


DS = "deepseek-ai/DeepSeek-V4-Flash-0731"; MM = "XiaomiMiMo/MiMo-V2.5-Pro"
FB = dict(dataset="prereg", model=DS, condition="forbidden")
CS = []
# Q6 effort
CS += contrast("Q6 high - off (forbidden, behind, DeepSeek)",
               {**FB, "effort": "high", "score_state": "behind"},
               {**FB, "effort": "off", "score_state": "behind"})
CS += contrast("Q6 low - off (forbidden, behind, DeepSeek; low_arm vs prereg)",
               dict(dataset="low_arm", model=DS, condition="forbidden", effort="low",
                    score_state="behind"),
               {**FB, "effort": "off", "score_state": "behind"})
CS += contrast("Q6 high - low (forbidden, behind, DeepSeek; prereg vs low_arm)",
               {**FB, "effort": "high", "score_state": "behind"},
               dict(dataset="low_arm", model=DS, condition="forbidden", effort="low",
                    score_state="behind"))
# Q5 assigned state and deficit depth
CS += contrast("Q5 behind - ahead (forbidden, off, DeepSeek)",
               {**FB, "effort": "off", "score_state": "behind"},
               {**FB, "effort": "off", "score_state": "ahead"})
CS += contrast("Q5 behind - ahead (forbidden, off, MiMo)",
               dict(dataset="prereg", model=MM, condition="forbidden", effort="off",
                    score_state="behind"),
               dict(dataset="prereg", model=MM, condition="forbidden", effort="off",
                    score_state="ahead"))
CS += contrast("Q5 -30 minus -10 (forbidden, off, behind, DeepSeek; deficit_d30 vs prereg)",
               dict(dataset="deficit_d30", model=DS, condition="forbidden", effort="off",
                    score_state="behind"),
               {**FB, "effort": "off", "score_state": "behind"})
# condition contrasts at off effort (both states pooled is not paired; do each state)
for st in ["behind", "ahead"]:
    for c in ["permitted", "hidden"]:
        CS += contrast(f"Q5x {c} - forbidden (off, {st}, DeepSeek)",
                       dict(dataset="prereg", model=DS, condition=c, effort="off",
                            score_state=st),
                       {**FB, "effort": "off", "score_state": st})
# per-opponent versions of the two headline treatment contrasts
for opp in ["AlwaysDefect", "Grudger", "TitForTat", "Pavlov", "Random", "LLM"]:
    CS += contrast("Q6 high - off (forbidden, behind, DeepSeek)",
                   {**FB, "effort": "high", "score_state": "behind"},
                   {**FB, "effort": "off", "score_state": "behind"}, sb_opp, opp)
    CS += contrast("Q5 behind - ahead (forbidden, off, DeepSeek)",
                   {**FB, "effort": "off", "score_state": "behind"},
                   {**FB, "effort": "off", "score_state": "ahead"}, sb_opp, opp)
C = pd.DataFrame(CS)
C.to_csv(T / "gt_q5_q6_block_contrasts.csv", index=False)
pd.set_option("display.width", 260); pd.set_option("display.max_colwidth", 60)
show = ["contrast", "opponent_type", "outcome", "mean_A", "mean_B", "mean_diff", "n_pos", "k",
        "p_exact_signflip"]
print(C[(C.opponent_type == "all") & (C.outcome.isin(["own_coop_played", "spr", "mutual_D",
                                                      "round1_coop", "nice"]))]
      [show].round(4).to_string(index=False))

# Q5c opponent mix: unforgiving-defector opponents vs the rest, per sandbox
ag["opp_class"] = np.where(ag.opponent_type.isin(["AlwaysDefect", "Grudger"]),
                           "AllD_or_Grudger", "rest")
rows = []
for ds, sub in ag.groupby("dataset"):
    sub = sub[sub.paraphrase != "p4"] if ds == "prereg" else sub
    p = sub.groupby(["sandbox", "opp_class"])[OUT].mean()
    for y in OUT:
        w = p[y].unstack()
        d = (w["AllD_or_Grudger"] - w["rest"]).dropna()
        rng = np.random.default_rng(3)
        null = (rng.choice([1, -1], size=(100000, len(d))) * d.values).mean(axis=1)
        rows.append(dict(dataset=ds, outcome=y, mean_AllD_Grudger=w["AllD_or_Grudger"].mean(),
                         mean_rest=w["rest"].mean(), mean_diff=d.mean(),
                         n_pos=int((d > 0).sum()), k=len(d),
                         p_signflip=max((np.abs(null) >= abs(d.mean())).mean(), 1e-5)))
M = pd.DataFrame(rows)
M.to_csv(T / "gt_q5_opponent_mix.csv", index=False)
print("\n== opponent mix (AllD+Grudger vs rest), per sandbox ==")
print(M[M.dataset == "prereg"].round(4).to_string(index=False))
