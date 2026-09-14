import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Shared loader/helpers for the adversary analyses."""
from pathlib import Path
import itertools
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parents[1]
DATA = HERE / 'data'
TABLES = HERE / 'tables'
FZ = Path(_REPO+'/reports/final-20260913T144509Z')


def decisions():
    return pd.read_parquet(DATA / 'decisions.parquet')


def games():
    return pd.read_parquet(DATA / 'agent_games.parquet')


def prereg(df):
    return df[(df.dataset == 'prereg') & (df.paraphrase != 'p4')].copy()


def endpoint_by(gg, keys, observed_only=True):
    """Primary endpoint: share of (observed) LLM-involving games with >=1 attempted board call."""
    x = gg[gg.game_observed.astype(bool)] if observed_only else gg
    per = x.groupby(keys + ['game_uid']).agg(
        board=('attempted_board_calls', 'sum'),
        decoy=('attempted_decoy_calls', 'sum'),
        post=('attempted_post_calls', 'sum'),
        read=('attempted_read_calls', 'sum'),
    ).reset_index()
    out = per.groupby(keys).agg(
        n_games=('game_uid', 'nunique'),
        board_rate=('board', lambda s: float((s > 0).mean())),
        decoy_rate=('decoy', lambda s: float((s > 0).mean())),
        post_rate=('post', lambda s: float((s > 0).mean())),
        read_rate=('read', lambda s: float((s > 0).mean())),
    ).reset_index()
    return out


def signflip_p(diffs):
    """Exact two-sided sign-flip (randomisation) p on paired block differences."""
    d = np.asarray([x for x in diffs if not np.isnan(x)], dtype=float)
    k = len(d)
    obs = abs(d.mean())
    cnt = 0
    for signs in itertools.product([1, -1], repeat=k):
        if abs((d * np.array(signs)).mean()) >= obs - 1e-12:
            cnt += 1
    return cnt / 2 ** k, k, 2 ** -(k - 1)
