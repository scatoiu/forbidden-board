import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Shared helpers for the perception-and-reaction analyses (prefix per_)."""
from pathlib import Path
import itertools
import numpy as np
import pandas as pd

DATA = Path(_REPO+"/paper-analysis/data")
TAB = Path(_REPO+"/paper-analysis/tables")
FROZEN = Path(_REPO+"/reports/final-20260913T144509Z/tables")
TAB.mkdir(parents=True, exist_ok=True)


def agent_games(prereg_only=True):
    ag = pd.read_parquet(DATA / "agent_games.parquet")
    if prereg_only:
        ag = ag[(ag.dataset == "prereg") & (ag.paraphrase != "p4")]
    return ag


def decisions(prereg_only=True):
    d = pd.read_parquet(DATA / "decisions.parquet")
    if prereg_only:
        d = d[(d.dataset == "prereg") & (d.paraphrase != "p4")]
    return d


def wilson(k, n, z=1.96):
    if n == 0:
        return (np.nan, np.nan)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def sign_flip_p(diffs):
    """Exact two-sided sign-flip (randomisation) p on paired block differences."""
    d = np.asarray([x for x in diffs if not np.isnan(x)], dtype=float)
    k = len(d)
    if k == 0:
        return np.nan, 0
    obs = abs(d.mean())
    cnt = 0
    for signs in itertools.product([1, -1], repeat=k):
        if abs((d * np.array(signs)).mean()) >= obs - 1e-12:
            cnt += 1
    return cnt / 2 ** k, k


def short(model):
    return "DeepSeek" if "DeepSeek" in str(model) else ("MiMo" if "MiMo" in str(model) else str(model))


def save(df, name, note=""):
    p = TAB / name
    df.to_csv(p, index=False)
    print(f"[saved] {p}  rows={len(df)} {note}")
    return p
