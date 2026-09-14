"""Master per-sandbox cell table: endpoint, decoy, quality (abort/parse/truncation/attrition)."""
import pandas as pd, numpy as np
from adv_common import decisions, games, endpoint_by, TABLES

d = decisions(); g = games()
keys = ['dataset','block','sandbox','model','condition','effort','score_state','paraphrase']

ep = endpoint_by(g, keys)

# quality per sandbox, from decisions
q = d.groupby(keys).agg(
    n_dec=('round','size'),
    n_played=('is_played','sum'),
    parse_fail=('parse_ok', lambda s: float((~s.astype(bool)).mean())),
    trunc_rate=('finish_reason', lambda s: float((s=='length').mean())),
    fb_any=('fallback_flag', lambda s: float(s.notna().mean())),
    retry_rate=('retries', lambda s: float((s>0).mean())),
    mean_attempts=('n_attempts','mean'),
    lost_by_retry=('board_call_lost_by_retry', lambda s: float(s.astype(bool).mean())),
    mean_reason_tok=('reasoning_tokens','mean'),
).reset_index()

gq = g.groupby(keys).agg(
    n_agent_games=('agent_game_uid','size'),
    n_games_all=('game_uid','nunique'),
    abort_rate=('game_aborted', lambda s: float(s.astype(bool).mean())),
    unobs_rate=('game_unobserved', lambda s: float(s.astype(bool).mean())),
    censored_rate=('game_provider_error_censored', lambda s: float(s.astype(bool).mean())),
).reset_index()

out = ep.merge(q, on=keys).merge(gq, on=keys)
out = out.sort_values(keys)
out.to_csv(TABLES/'adv_00_cells.csv', index=False)
pd.set_option('display.width', 250, 'display.max_columns', 50, 'display.max_rows', 200)
print(out[out.dataset=='prereg'][['block','model','condition','effort','score_state','n_games','board_rate','decoy_rate','abort_rate','unobs_rate','parse_fail','trunc_rate','retry_rate']].to_string(index=False))
