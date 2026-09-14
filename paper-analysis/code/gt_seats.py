import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Q1 input: per-seat (agent) totals for the FULL 24-agent round-robin.

The compact `agent_games.parquet` has game_end rows only for LLM agents, so a
script seat's total is invisible there. The raw move log, however, records every
scripted decision too (`model: "script:<Name>"`, `pair_type: "script-script"`),
with that mover's own `payoff` on the row. Summing scored-phase payoffs per seat
therefore reconstructs the complete round-robin standing inside each sandbox,
scripts included, with no simulation.

Read-only over runs/*; uses the harness's own loader so repairs / warm-up /
aborted-row handling match the frozen report.

Out: tables/gt_seat_scores.csv (one row per sandbox x seat)
     tables/gt_seat_pairs.csv  (one row per sandbox x seat x opponent seat-type)
"""
from __future__ import annotations
import sys
from pathlib import Path
import pandas as pd

TOURN = Path(_REPO+"")
OUT = Path(_REPO+"/paper-analysis/tables")
sys.path.insert(0, str(TOURN))
from analysis.load import load_runs  # noqa: E402

DATASETS = {
    "prereg": dict(roots=["runs/v3", "runs/v3b", "runs/v3-mimo"], repairs=["runs/v7-repair"]),
    "replication": dict(roots=["runs/v4-a4096"], repairs=[]),
    "low_arm": dict(roots=["runs/v6-low"], repairs=[]),
    "deficit_d30": dict(roots=["runs/v5-d30"], repairs=[]),
}


def seat_type(model: str) -> str:
    return model.split("script:")[1] if str(model).startswith("script:") else "LLM"


frames, pframes = [], []
for name, cfg in DATASETS.items():
    rd = load_runs([TOURN / r for r in cfg["roots"]], dataset=name,
                   repairs=[TOURN / r for r in cfg["repairs"]], validate=False)
    mv = rd.moves
    print(name, "move rows", len(mv), file=sys.stderr)
    mv = mv[(mv["phase"] == "scored") & (mv["status"] == "ok")].copy()
    mv["seat_type"] = mv["model"].map(seat_type)
    mv["opp_seat_type"] = mv["opponent_model"].map(seat_type)
    meta = ["dataset", "sandbox", "model", "condition", "effort", "score_state",
            "paraphrase", "seed"]
    for c in meta:
        if c not in mv.columns:
            mv[c] = None
    # one LLM model per sandbox: carry it as sandbox_model
    llm_model = (mv[mv.seat_type == "LLM"].groupby("sandbox")["model"]
                 .agg(lambda s: s.value_counts().idxmax()))
    mv["sandbox_model"] = mv["sandbox"].map(llm_model)
    g = mv.groupby(["dataset", "sandbox", "sandbox_model", "condition", "effort",
                    "score_state", "paraphrase", "seed", "agent", "seat_type"], dropna=False)
    seats = g.agg(total_score=("payoff", "sum"), rounds=("payoff", "size"),
                  n_games=("game", "nunique"),
                  coop=("action", lambda s: (s == "C").mean())).reset_index()
    seats["score_per_round"] = seats.total_score / seats.rounds
    frames.append(seats)
    gp = mv.groupby(["dataset", "sandbox", "sandbox_model", "condition", "effort",
                     "score_state", "paraphrase", "agent", "seat_type", "opp_seat_type"],
                    dropna=False)
    pairs = gp.agg(score=("payoff", "sum"), rounds=("payoff", "size"),
                   n_games=("game", "nunique"),
                   coop=("action", lambda s: (s == "C").mean())).reset_index()
    pairs["score_per_round"] = pairs.score / pairs.rounds
    pframes.append(pairs)

pd.concat(frames, ignore_index=True).to_csv(OUT / "gt_seat_scores.csv", index=False)
pd.concat(pframes, ignore_index=True).to_csv(OUT / "gt_seat_pairs.csv", index=False)
print("wrote", OUT / "gt_seat_scores.csv", OUT / "gt_seat_pairs.csv")
