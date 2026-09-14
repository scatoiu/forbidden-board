"""Phase 0: one shared extraction of the frozen tournament logs into compact tables.

Reads `project/tournament/runs/*` READ-ONLY through the harness's own loader
(`analysis.load.load_runs`) so that repairs, attempt-union board calls,
provider-error-unobserved games and assigned score state are treated exactly as
in the frozen report `reports/final-20260913T144509Z`. Writes parquet + CSV to
`project/paper/analyses/data/` with a PROVENANCE.json (inputs, hashes, argv).

Datasets (never pooled):
  prereg       runs/v3 runs/v3b runs/v3-mimo  + repairs runs/v7-repair
  replication  runs/v4-a4096
  low_arm      runs/v6-low
  deficit_d30  runs/v5-d30

Usage (from project/tournament, its venv):
  .venv/bin/python ../paper/analyses/code/extract.py
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

import pandas as pd

TOURN = Path(__file__).resolve().parents[3] / "tournament"
OUT = Path(__file__).resolve().parents[1] / "data"
sys.path.insert(0, str(TOURN))
from analysis.load import load_runs  # noqa: E402

DATASETS = {
    "prereg": dict(roots=["runs/v3", "runs/v3b", "runs/v3-mimo"], repairs=["runs/v7-repair"]),
    "replication": dict(roots=["runs/v4-a4096"], repairs=[]),
    "low_arm": dict(roots=["runs/v6-low"], repairs=[]),
    "deficit_d30": dict(roots=["runs/v5-d30"], repairs=[]),
}

DECISION_COLS = [
    "dataset", "sandbox", "base_sandbox", "sandbox_complete", "model", "condition", "effort",
    "score_state", "paraphrase", "seed", "generation", "game", "game_uid", "agent", "lineage",
    "round", "opponent", "opponent_model", "pair_type", "status", "is_played", "action",
    "executed", "opponent_action", "payoff", "parse_ok", "fallback_flag", "retries",
    "n_attempts", "forced_answer", "finish_reason", "reasoning_tokens", "completion_tokens",
    "prompt_tokens", "latency_ms", "att_board_calls", "att_read_calls", "att_post_calls",
    "att_decoy_calls", "att_unlisted_calls", "board_calls", "decoy_calls", "board_called",
    "decoy_called", "board_call_lost_by_retry", "read_before_post", "board_size_at_read",
    "score_gap_at_call", "reasoning_mentions_board", "ts",
]

GAME_COLS = [
    "dataset", "sandbox", "base_sandbox", "sandbox_complete", "model", "condition", "effort",
    "score_state", "paraphrase", "seed", "generation", "game", "game_uid", "agent_game_uid",
    "agent", "opponent", "opponent_model", "pair_type", "status", "aborted", "game_aborted",
    "game_complete", "game_provider_error_abort", "game_unobserved", "game_provider_error_censored",
    "game_observed", "aborted_before_first_decision", "rounds", "moves_logged", "coop_rate",
    "opp_coop_rate", "score", "opp_score", "won", "channel_used", "used_channel", "first_use_round",
    "use_count", "decoy_count", "used_decoy", "n_posts", "attempted_board_calls",
    "attempted_post_calls", "attempted_read_calls", "attempted_decoy_calls",
    "classification_correct", "classification_predicted", "classification_name_correct",
    "classification_named_script", "prohibition_recall_correct", "fallback_count",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def per_game_dynamics(mv: pd.DataFrame) -> pd.DataFrame:
    """Per LLM agent-game aggregates from the played move sequence.

    first_defector: who defected first among (llm, opponent): 'llm', 'opponent',
    'both' (same round), 'none' (no defection in the played rows).
    retaliation_rate: P(own D at t | opponent D at t-1).
    forgiveness_rate: P(own C at t | own D at t-1 and opponent C at t-1)  [return to C after punishing].
    round1_coop: own round-1 action == C.
    last5_coop: own cooperation over the last five played rounds of that game.
    """
    d = mv[mv["is_played"]].copy()
    d = d[d["action"].isin(["C", "D"]) & d["opponent_action"].isin(["C", "D"])]
    d = d.sort_values(["agent_game_uid", "round"])
    out = []
    for uid, g in d.groupby("agent_game_uid", sort=False):
        a = g["action"].to_numpy()
        o = g["opponent_action"].to_numpy()
        r = g["round"].to_numpy()
        n = len(a)
        first_llm = next((i for i in range(n) if a[i] == "D"), None)
        first_opp = next((i for i in range(n) if o[i] == "D"), None)
        if first_llm is None and first_opp is None:
            fd, fd_round = "none", None
        elif first_opp is None or (first_llm is not None and first_llm < first_opp):
            fd, fd_round = "llm", int(r[first_llm])
        elif first_llm is None or first_opp < first_llm:
            fd, fd_round = "opponent", int(r[first_opp])
        else:
            fd, fd_round = "both", int(r[first_llm])
        # retaliation: own D at t given opp D at t-1
        ret_num = ret_den = 0
        forg_num = forg_den = 0
        for i in range(1, n):
            if o[i - 1] == "D":
                ret_den += 1
                ret_num += a[i] == "D"
            if a[i - 1] == "D" and o[i - 1] == "C":
                forg_den += 1
                forg_num += a[i] == "C"
        out.append(dict(
            agent_game_uid=uid, n_played=n, first_defector=fd, first_defection_round=fd_round,
            llm_first_defection_round=(int(r[first_llm]) if first_llm is not None else None),
            opp_first_defection_round=(int(r[first_opp]) if first_opp is not None else None),
            retaliation_rate=(ret_num / ret_den if ret_den else None), retaliation_n=ret_den,
            forgiveness_rate=(forg_num / forg_den if forg_den else None), forgiveness_n=forg_den,
            round1_coop=float(a[0] == "C"),
            own_coop_played=float((a == "C").mean()),
            opp_coop_played=float((o == "C").mean()),
            last5_coop=float((a[-5:] == "C").mean()),
            own_score_played=float(g["payoff"].fillna(0).sum()),
            n_own_D=int((a == "D").sum()), n_opp_D=int((o == "D").sum()),
            n_CC=int(((a == "C") & (o == "C")).sum()), n_DD=int(((a == "D") & (o == "D")).sum()),
            n_CD=int(((a == "C") & (o == "D")).sum()), n_DC=int(((a == "D") & (o == "C")).sum()),
        ))
    return pd.DataFrame(out)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    prov = dict(script=str(Path(__file__).resolve()), argv=sys.argv, started=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                tournament_git_sha=subprocess.run(["git", "-C", str(TOURN), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip(),
                datasets={}, notes={})
    dec_frames, game_frames, sb_frames = [], [], []
    for label, spec in DATASETS.items():
        roots = [TOURN / r for r in spec["roots"]]
        repairs = [TOURN / r for r in spec["repairs"]]
        rd = load_runs(roots, dataset=label, repairs=repairs or None, validate=True)
        mv, gm = rd.moves.copy(), rd.games.copy()
        mv["dataset"] = label
        gm["dataset"] = label
        mv["agent_game_uid"] = mv["game_uid"] + "/" + mv["agent"].astype(str)
        for c in DECISION_COLS:
            if c not in mv.columns:
                mv[c] = None
        for c in GAME_COLS:
            if c not in gm.columns:
                gm[c] = None
        dec = mv.loc[mv["is_decision"], DECISION_COLS + ["agent_game_uid"]].copy()
        dyn = per_game_dynamics(mv.loc[mv["is_decision"]].assign(agent_game_uid=mv["agent_game_uid"]))
        games = gm[GAME_COLS].merge(dyn, on="agent_game_uid", how="left")
        dec_frames.append(dec)
        game_frames.append(games)
        # per-sandbox summary: from the games table
        prov["datasets"][label] = dict(
            roots=[str(r) for r in roots], repairs=[str(r) for r in repairs],
            n_sandboxes=int(mv["sandbox"].nunique()), n_move_rows=int(len(mv)),
            n_decisions=int(mv["is_decision"].sum()), n_played=int(mv["is_played"].sum()),
            n_warmup_rows=int(mv["is_warmup"].sum()), n_agent_games=int(len(gm)),
            n_violations=int(len(rd.violations)), score_state_source=rd.score_state_source,
            loader_notes=rd.notes, repair_status=rd.repair_status,
            input_files={str(p.relative_to(TOURN)): sha256(p) for r in roots + repairs for p in sorted(r.glob("*/moves.jsonl"))},
        )
        print(f"[{label}] sandboxes={mv['sandbox'].nunique()} moves={len(mv)} decisions={int(mv['is_decision'].sum())} "
              f"agent_games={len(gm)} violations={len(rd.violations)}  t={time.time()-t0:.0f}s", flush=True)
        del rd, mv, gm

    decisions = pd.concat(dec_frames, ignore_index=True)
    games = pd.concat(game_frames, ignore_index=True)
    for c in ("score_gap_at_call", "payoff", "reasoning_tokens", "board_size_at_read"):
        decisions[c] = pd.to_numeric(decisions[c], errors="coerce")
    decisions["block_raw"] = decisions["sandbox"].str.extract(r"^([BMXY]\d)")[0]; decisions["block"] = "B" + decisions["block_raw"].str[1]
    games["block_raw"] = games["sandbox"].str.extract(r"^([BMXY]\d)")[0]; games["block"] = "B" + games["block_raw"].str[1]
    games["opponent_type"] = games["opponent_model"].astype(str).map(lambda s: s.split(":")[1] if s.startswith("script:") else "LLM")
    decisions["opponent_type"] = decisions["opponent_model"].astype(str).map(lambda s: s.split(":")[1] if s.startswith("script:") else "LLM")

    decisions.to_parquet(OUT / "decisions.parquet", index=False)
    games.to_parquet(OUT / "agent_games.parquet", index=False)
    games.to_csv(OUT / "agent_games.csv", index=False)

    # sandbox-level: join to the frozen report's replicate table where present
    frozen = TOURN / "reports/final-20260913T144509Z/tables/sandbox_replicates.csv"
    sb = games.groupby(["dataset", "sandbox"], as_index=False).agg(
        model=("model", "first"), condition=("condition", "first"), effort=("effort", "first"),
        score_state=("score_state", "first"), paraphrase=("paraphrase", "first"), seed=("seed", "first"),
        block=("block", "first"), sandbox_complete=("sandbox_complete", "first"),
        n_agent_games=("agent_game_uid", "count"), n_games=("game_uid", "nunique"),
        n_games_aborted=("game_uid", lambda s: games.loc[s.index].loc[lambda d: d["game_aborted"], "game_uid"].nunique()),
        n_games_unobserved=("game_uid", lambda s: games.loc[s.index].loc[lambda d: d["game_unobserved"], "game_uid"].nunique()),
    )
    if frozen.exists():
        fz = pd.read_csv(frozen)
        fz = fz[fz["scope"] == "fixed_population"] if "scope" in fz.columns else fz
        sb = sb.merge(fz.add_prefix("frozen_"), left_on="sandbox", right_on="frozen_sandbox", how="left")
    sb.to_csv(OUT / "sandboxes.csv", index=False)

    prov["finished"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    prov["outputs"] = {p.name: sha256(p) for p in OUT.iterdir() if p.is_file() and p.name != "PROVENANCE.json"}
    prov["row_counts"] = dict(decisions=int(len(decisions)), agent_games=int(len(games)), sandboxes=int(len(sb)))
    (OUT / "PROVENANCE.json").write_text(json.dumps(prov, indent=1, default=str))
    print("done", prov["row_counts"], f"{time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
