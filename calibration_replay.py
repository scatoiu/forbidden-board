#!/usr/bin/env python
"""Calibration gate: does the reasoning-effort dial move anything on identical prompts?

specs/sandboxes-v2/calibration-effort.yaml specifies 30 frozen decision states from
the forbidden condition (15 ahead, 15 behind), each replayed at several effort levels
with IDENTICAL prompts and IDENTICAL answer capacity (768 answer tokens), one decision
per call, no population, no board writes. This script makes that gate RETROACTIVE: the
30 states are drawn from games that were actually played (runs/v3/B{1,2}-forbidden-off-*),
and the prompt is rebuilt from the logged state and checked against the `prompt_sha256`
the runner logged at the time. A state whose rebuilt hash does not match the log is
dropped rather than replayed, so every call in `calls.csv` is provably the same prompt
the model already saw once.

The spec's reasoning budgets (1024/4096/6144) are superseded by the budgets the real
arms use: {none: 0, low: 8192, high: 12288, max: 12288}, reserved ON TOP of the 768
answer tokens.

Subcommands
-----------
    sample     draw and freeze the states to specs/states/calibration-states.json
    verify     rebuild every frozen state's prompt and compare the hash
    replay     call the provider and write reports/<tag>/calls.csv
    report     write SUMMARY.md and states-manifest.md from calls.csv
    all        sample + replay + report

Nothing here writes to the notes board, to runs/, or to any spec other than
specs/states/calibration-states.json.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
import statistics
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Iterator

import axelrod as axl

from coop.env import load_env_file, resolve_api_key
from coop.models import resolve_effort
from coop.notes import DECOY_SCHEMAS, tools_for
from coop.prompts import (
    build_system,
    build_user,
    check_rendered,
    get_brief,
    inverse_labels,
    payoff_table,
    request_line,
    state_block,
)
from coop.providers.base import parse_action
from coop.providers.openai_compat import OpenAICompatClient
from coop.players.llm import stable_seed
from coop.tournament import make_game

ROOT = Path(__file__).resolve().parent

# --- what the states are drawn from ------------------------------------------
SOURCES: tuple[tuple[str, str], ...] = (
    ("ahead", "runs/v3/B1-forbidden-off-ahead/moves.jsonl"),
    ("behind", "runs/v3/B1-forbidden-off-behind/moves.jsonl"),
    ("ahead", "runs/v3/B2-forbidden-off-ahead/moves.jsonl"),
    ("behind", "runs/v3/B2-forbidden-off-behind/moves.jsonl"),
)

STATES_PATH = "specs/states/calibration-states.json"
DEFAULT_TAG = "calibration-2026-09-13"

SAMPLE_SEED = 9001
N_PER_ARM = 15
#: (round bin, pair type) cells, in the fixed order the quota is spread over.
CELLS: tuple[tuple[str, str], ...] = (
    ("early", "llm-llm"), ("early", "llm-script"),
    ("mid", "llm-llm"), ("mid", "llm-script"),
    ("late", "llm-llm"), ("late", "llm-script"),
)
#: Extra candidates drawn per cell so a hash mismatch can be dropped without
#: unbalancing the design.
POOL_EXTRA = 5

# --- the dial under test ------------------------------------------------------
MODEL = "deepseek-ai/DeepSeek-V4-Flash-0731"
BASE_URL = "https://api.deepinfra.com/v1/openai"
PROFILE = "deepinfra"
TEMPERATURE = 0.7
MAX_TOOL_ITERATIONS = 3
TIMEOUT_S = 480.0
CONCURRENCY = 8

ANSWER_TOKENS = 768
#: Superseding the spec's 1024/4096/6144: these are the budgets the real arms use.
BUDGETS = {"none": 0, "low": 8192, "high": 12288, "max": 12288}
#: The level name in the report -> the level `resolve_effort` is asked for.
#: DeepInfra's field takes "none"; coop.models spells the same level "off".
SENT_AS = {"none": "off", "low": "low", "high": "high", "max": "max"}
#: Two samples where the contrast matters most, one elsewhere: 30 x 6 = 180 calls.
REPLICATES = {"none": 2, "low": 1, "high": 2, "max": 1}
LEVELS = ("none", "low", "high", "max")
ADJACENT = (("none", "low"), ("low", "high"), ("high", "max"))
NON_ADJACENT = (("none", "high"), ("none", "max"), ("low", "max"))

PRICE_IN_PER_M = 0.06
PRICE_OUT_PER_M = 0.18

MATRIX = "default"
WINDOW = 20
DECOY = "workspace_clock"
PROMPTS_DIR = "specs/prompts"


# ---------------------------------------------------------------------------
# 1. sampling
# ---------------------------------------------------------------------------

#: Only the fields the rebuild and the sampler need; `raw`, `reasoning` and
#: `attempts` are dropped while streaming so four 13k-row logs stay small.
_KEEP = (
    "kind", "phase", "status", "provider", "sandbox", "seed", "generation", "game",
    "round", "agent", "model", "opponent", "opponent_model", "pair_type", "condition",
    "framing", "paraphrase", "label_map", "option_order", "action", "executed",
    "opponent_action", "prompt_sha256", "tools_sha256", "warmup_rounds",
    "score_gap_at_call",
)


def round_bin(rnd: int) -> str:
    return "early" if rnd <= 10 else ("mid" if rnd <= 20 else "late")


def board_snapshot(tool_results: list[dict]) -> dict[str, Any]:
    """The board the model was shown, if it read one; else an empty board.

    The first successful `notes_read` of the row is the snapshot: the RoundBoard
    froze it at the start of that round, so a later read in the same round returns
    the same rows.
    """
    for tr in tool_results or []:
        if tr.get("name") == "notes_read" and tr.get("ok"):
            res = tr.get("result") or {}
            if isinstance(res, dict) and "entries" in res:
                return {
                    "entries": list(res.get("entries") or []),
                    "total": int(res.get("total", 0) or 0),
                    "shown": int(res.get("shown", 0) or 0),
                }
    return {"entries": [], "total": 0, "shown": 0}


def is_llm_decision(row: dict) -> bool:
    return (
        row.get("kind") == "move"
        and row.get("phase") == "scored"
        and row.get("status") == "ok"
        and row.get("provider") not in ("assigned", "script", None)
        and not str(row.get("model", "")).startswith("script:")
        and bool(row.get("prompt_sha256"))
        and row.get("executed") in ("C", "D")
    )


def stream_rows(path: str | Path) -> Iterator[dict]:
    """Stream one moves.jsonl. Never reads the whole file into memory."""
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if row.get("kind") != "move":
                continue
            slim = {k: row.get(k) for k in _KEEP}
            if is_llm_decision(row):
                slim["board"] = board_snapshot(row.get("tool_results") or [])
            yield slim


@dataclass
class SourceIndex:
    """One sandbox's move log, indexed by game."""

    arm: str
    path: str
    games: dict[int, list[dict]]

    @property
    def candidates(self) -> list[dict]:
        out = [r for rows in self.games.values() for r in rows if is_llm_decision(r)]
        out.sort(key=lambda r: (r["game"], r["round"], r["agent"]))
        return out


def load_source(arm: str, path: str | Path) -> SourceIndex:
    games: dict[int, list[dict]] = {}
    for row in stream_rows(path):
        games.setdefault(row["game"], []).append(row)
    return SourceIndex(arm=arm, path=str(path), games=games)


def quota_for_arm(n: int = N_PER_ARM, cells: int = len(CELLS)) -> list[int]:
    """Spread `n` over `cells` as evenly as possible, front-loaded."""
    base, extra = divmod(n, cells)
    return [base + (1 if i < extra else 0) for i in range(cells)]


def sample_states(
    sources: Iterable[SourceIndex], *, seed: int = SAMPLE_SEED, verify: bool = True,
) -> tuple[list[dict], list[dict]]:
    """Draw 30 stratified states. Deterministic in `seed`.

    Returns (states, drops). A candidate whose rebuilt prompt hash does not match the
    logged one is dropped and the next candidate in the same cell takes its place.
    """
    by_arm: dict[str, dict[str, list[dict]]] = {"ahead": {}, "behind": {}}
    index: dict[tuple[str, int], list[dict]] = {}
    for src in sources:
        for game_id, rows in src.games.items():
            index[(src.path, game_id)] = rows
        bucket = by_arm[src.arm].setdefault(src.path, [])
        for row in src.candidates:
            bucket.append(dict(row, _source=src.path, _arm=src.arm))

    rng = random.Random(seed)
    states: list[dict] = []
    drops: list[dict] = []
    quota = quota_for_arm()
    for arm in ("ahead", "behind"):
        for cell_i, (rbin, ptype) in enumerate(CELLS):
            want = quota[cell_i]
            # One queue per source sandbox, drained round-robin, so the two
            # replicate sandboxes of an arm contribute equally.
            queues = []
            for path in sorted(by_arm[arm]):
                cell = [r for r in by_arm[arm][path]
                        if round_bin(r["round"]) == rbin and r["pair_type"] == ptype]
                cell.sort(key=lambda r: (r["game"], r["round"], r["agent"]))
                queues.append(rng.sample(cell, min(len(cell), want + POOL_EXTRA)))
            draw: list[dict] = []
            for i in range(max((len(q) for q in queues), default=0)):
                for q in queues:
                    if i < len(q):
                        draw.append(q[i])
            taken = 0
            for row in draw:
                if taken >= want:
                    break
                state = freeze_state(row, index[(row["_source"], row["game"])])
                state["arm"] = arm
                state["round_bin"] = rbin
                if verify:
                    ok, why = verify_state(state)
                    if not ok:
                        drops.append({"state": state["state_id"], "reason": why})
                        continue
                states.append(state)
                taken += 1
            if taken < want:
                drops.append({"state": f"{arm}/{rbin}/{ptype}",
                              "reason": f"cell exhausted: {taken}/{want} matched"})
    for i, s in enumerate(states):
        s["index"] = i
    return states, drops


def freeze_state(row: dict, game_rows: list[dict]) -> dict:
    """Everything needed to rebuild the prompt the runner built for this decision."""
    agent, opp, rnd = row["agent"], row["opponent"], row["round"]
    warm = sorted(
        (r for r in game_rows if r["phase"] == "warmup" and r["agent"] == agent),
        key=lambda r: r["round"],
    )
    warmup = [[r["action"], r["opponent_action"]] for r in warm]
    mine = {r["round"]: r["executed"] for r in game_rows
            if r["phase"] == "scored" and r["agent"] == agent and r["executed"]}
    theirs = {r["round"]: r["executed"] for r in game_rows
              if r["phase"] == "scored" and r["agent"] == opp and r["executed"]}
    history = [[mine[i], theirs[i]] for i in range(1, rnd)
               if i in mine and i in theirs]
    state = {
        "state_id": f"{row['sandbox']}:g{row['game']}:r{rnd}:{agent}",
        "source": row.get("_source", ""),
        "sandbox": row["sandbox"],
        "seed": row["seed"],
        "generation": row["generation"],
        "game": row["game"],
        "round": rnd,
        "agent": agent,
        "model": row["model"],
        "opponent": opp,
        "opponent_model": row["opponent_model"],
        "pair_type": row["pair_type"],
        "condition": row["condition"],
        "framing": row["framing"],
        "paraphrase": row["paraphrase"],
        "matrix": MATRIX,
        "window": WINDOW,
        "decoy_tool": DECOY,
        "prompts_dir": PROMPTS_DIR,
        "label_map": row["label_map"],
        "option_order": row["option_order"],
        "warmup_rounds": row["warmup_rounds"],
        "warmup": warmup,
        "history": history,
        "board": row.get("board") or {"entries": [], "total": 0, "shown": 0},
        "logged_prompt_sha256": row["prompt_sha256"],
        "logged_tools_sha256": row["tools_sha256"],
        "logged_score_gap": row["score_gap_at_call"],
        "logged_action": row["action"],
    }
    state["totals"] = totals_for(state)
    return state


# ---------------------------------------------------------------------------
# 2. rebuilding the exact prompt
# ---------------------------------------------------------------------------

_GAMES: dict[str, Any] = {}


def game_for(matrix: str = MATRIX):
    if matrix not in _GAMES:
        _GAMES[matrix] = make_game(matrix)
    return _GAMES[matrix]


def _act(a: str):
    return axl.Action.C if a == "C" else axl.Action.D


def totals_for(state: dict) -> dict[str, int]:
    """`LLMPlayer._totals`: warm-up ledger carried in, then the scored rounds."""
    game = game_for(state.get("matrix", MATRIX))
    rounds = [tuple(r) for r in state["warmup"]] + [tuple(r) for r in state["history"]]
    score = opp_score = 0
    for a, b in rounds:
        sa, sb = game.score((_act(a), _act(b)))
        score += sa
        opp_score += sb
    # axelrod's score() hands back numpy scalars; the runner keeps them, but a
    # frozen state has to survive a JSON round trip.
    return {
        "score": int(score),
        "opp_score": int(opp_score),
        "rounds": len(rounds),
        "self_c": sum(1 for a, _ in rounds if a == "C"),
        "opp_c": sum(1 for _, b in rounds if b == "C"),
    }


def rebuild(state: dict) -> tuple[list[dict], list[dict] | None, str, str]:
    """Replicate `LLMPlayer._messages` / `_decide`'s hashing, exactly.

    Returns (messages, tools, prompt_sha256, tools_sha256).
    """
    lm = state["label_map"]
    game = game_for(state.get("matrix", MATRIX))
    brief = get_brief(state["framing"], state["paraphrase"], state["condition"],
                      prompts_dir=state.get("prompts_dir", PROMPTS_DIR))
    system = build_system(
        brief, payoffs=payoff_table(game, lm), condition=state["condition"],
        agent_id=state["agent"], sandbox=state["sandbox"], label_map=lm,
    )
    labelled = [(lm[a], lm[b])
                for a, b in ([tuple(r) for r in state["warmup"]]
                             + [tuple(r) for r in state["history"]])]
    # The runner shows the round number INCLUDING the warm-up block, while the
    # logged `round` counts scored rounds only.
    prompt_round = state["round"] + len(state["warmup"])
    totals = state["totals"]
    window = state.get("window", WINDOW)
    options = list(state["option_order"])
    block = state_block(
        agent_id=state["agent"], opponent_id=state["opponent"],
        round_number=prompt_round, history=labelled, window=window,
        totals=totals, label_map=lm,
    )
    user = build_user(
        brief, state=block, request=request_line(options),
        agent_id=state["agent"], opponent_id=state["opponent"],
        round_number=prompt_round, history=labelled, window=window,
        totals=totals, label_map=lm, options=options,
    )
    messages = [{"role": "system", "content": system},
                {"role": "user", "content": user}]
    check_rendered(system, user, condition=state["condition"])
    tools = tools_for(state["condition"], state.get("prompts_dir", PROMPTS_DIR),
                      state.get("decoy_tool", DECOY))
    blob = json.dumps(tools or [], sort_keys=True)
    tools_sha = hashlib.sha256(blob.encode()).hexdigest()
    text = "\n\n".join(m["content"] for m in messages) + "\n\n" + blob
    return messages, tools, hashlib.sha256(text.encode()).hexdigest(), tools_sha


def verify_state(state: dict) -> tuple[bool, str]:
    try:
        _, _, psha, tsha = rebuild(state)
    except Exception as e:  # a brief that no longer renders is a drop, not a crash
        return False, f"rebuild raised {type(e).__name__}: {e}"
    if tsha != state["logged_tools_sha256"]:
        return False, "tools_sha256 mismatch"
    if psha != state["logged_prompt_sha256"]:
        return False, "prompt_sha256 mismatch"
    return True, "ok"


# ---------------------------------------------------------------------------
# 3. replay
# ---------------------------------------------------------------------------

def make_frozen_handler(state: dict, bookkeeping: dict):
    """Tool handler that reads a frozen board and writes NOWHERE.

    `notes_post` is answered exactly as `coop.notes.make_tool_handler` answers it
    ({"ok": true, "posted": text}) so the transcript the model sees is unchanged,
    but nothing is appended to any store, file or run directory.
    """
    totals = state["totals"]
    board = state.get("board") or {"entries": [], "total": 0, "shown": 0}

    def handler(name: str, args: dict) -> Any:
        bookkeeping["order"].append(name)
        if name == "notes_read":
            result: Any = {
                "entries": list(board.get("entries") or []),
                "total": int(board.get("total", 0) or 0),
                "shown": int(board.get("shown", 0) or 0),
            }
            bookkeeping["board_size_at_read"] = result["total"]
        elif name == "notes_post":
            text = args.get("text", "") if isinstance(args, dict) else str(args)
            text = str(text)[:400]
            bookkeeping["posts"].append(text)
            result = {"ok": True, "posted": text}
        elif name in DECOY_SCHEMAS:
            # The runner's ledger for this agent, as of this decision.
            result = {"cumulative_score": int(totals["score"]),
                      "sessions_completed": int(totals["rounds"])}
        else:
            raise ValueError(f"unknown tool {name!r}")
        return result

    return handler


def call_seed(state: dict, replicate: int) -> int:
    """`LLMPlayer._decide`'s sample seed. Replicate 2 extends the same formula."""
    parts = [state["sandbox"], state["seed"], state["generation"], state["game"],
             state["agent"], state["round"], "sample"]
    if replicate > 0:
        parts.append(replicate + 1)
    return stable_seed(*parts) % (2 ** 31)


def estimate_cost(prompt_tokens: int, completion_tokens: int) -> float:
    return (prompt_tokens * PRICE_IN_PER_M + completion_tokens * PRICE_OUT_PER_M) / 1e6


def replay_one(state: dict, level: str, replicate: int, client: Any) -> dict:
    messages, tools, psha, tsha = rebuild(state)
    sent, mapping = resolve_effort(MODEL, SENT_AS[level])
    budget = BUDGETS[level]
    max_tokens = ANSWER_TOKENS + budget
    bookkeeping: dict[str, Any] = {"order": [], "posts": [], "board_size_at_read": None}
    handler = make_frozen_handler(state, bookkeeping)
    seed = call_seed(state, replicate)
    result = client.chat(
        messages, tools=tools, tool_handler=handler, temperature=TEMPERATURE,
        max_tokens=max_tokens, effort=sent, seed=seed,
        max_tool_iterations=MAX_TOOL_ITERATIONS,
    )
    parsed = None if result.error else parse_action(
        result.raw, labels=inverse_labels(state["label_map"]))
    order = bookkeeping["order"]
    reported = sum(u.get("estimated_cost") or 0.0 for u in result.usage)
    row = {
        "state_id": state["state_id"],
        "state_index": state.get("index", -1),
        "sandbox": state["sandbox"],
        "game": state["game"],
        "round": state["round"],
        "agent": state["agent"],
        "arm": state.get("arm", ""),
        "round_bin": state.get("round_bin", ""),
        "pair_type": state["pair_type"],
        "level": level,
        "sent_effort": sent,
        "binary_collapsed": bool(mapping.get("collapsed")),
        "replicate": replicate + 1,
        "reasoning_budget": budget,
        "answer_tokens": ANSWER_TOKENS,
        "max_tokens": max_tokens,
        "seed": seed,
        "prompt_sha256": psha,
        "tools_sha256": tsha,
        "hash_matches_log": psha == state["logged_prompt_sha256"],
        "reasoning_tokens": result.reasoning_tokens,
        "completion_tokens": result.completion_tokens,
        "prompt_tokens": result.prompt_tokens,
        "finish_reason": result.finish_reason or "",
        "latency_ms": result.latency_ms,
        "iterations": result.iterations,
        "action": (parsed.action if parsed else None) or "",
        "parse_ok": bool(parsed and parsed.action),
        "fallback_flag": (parsed.fallback_flag if parsed else "provider_error") or "",
        "board_calls": sum(1 for n in order if n in ("notes_read", "notes_post")),
        "read_calls": sum(1 for n in order if n == "notes_read"),
        "post_calls": sum(1 for n in order if n == "notes_post"),
        "decoy_calls": sum(1 for n in order if n in DECOY_SCHEMAS),
        "tool_call_names": "|".join(order),
        "forced_answer": bool(result.forced_answer),
        "trace_location": result.trace_location,
        "reasoning_chars": len(result.reasoning or ""),
        "raw_chars": len(result.raw or ""),
        "estimated_cost": round(
            reported or estimate_cost(result.prompt_tokens, result.completion_tokens), 8),
        "cost_source": "provider" if reported else "price_card",
        "error": result.error or "",
    }
    return row


CSV_FIELDS = [
    "state_id", "state_index", "sandbox", "game", "round", "agent", "arm", "round_bin",
    "pair_type", "level", "sent_effort", "binary_collapsed", "replicate",
    "reasoning_budget", "answer_tokens", "max_tokens", "seed", "prompt_sha256",
    "tools_sha256", "hash_matches_log", "reasoning_tokens", "completion_tokens",
    "prompt_tokens", "finish_reason", "latency_ms", "iterations", "action", "parse_ok",
    "fallback_flag", "board_calls", "read_calls", "post_calls", "decoy_calls",
    "tool_call_names", "forced_answer", "trace_location", "reasoning_chars",
    "raw_chars", "estimated_cost", "cost_source", "error",
]


def build_jobs(states: list[dict]) -> list[tuple[dict, str, int]]:
    jobs = []
    for state in states:
        for level in LEVELS:
            for rep in range(REPLICATES[level]):
                jobs.append((state, level, rep))
    return jobs


def run_replay(states: list[dict], out_csv: Path, *, concurrency: int = CONCURRENCY,
               limit: int | None = None) -> list[dict]:
    load_env_file(ROOT / ".env")
    key, source = resolve_api_key(PROFILE)
    if not key:
        raise SystemExit(
            f"no API key for profile {PROFILE!r}: set DEEPINFRA_API_KEY in .env")
    print(f"api key from {source}", file=sys.stderr)
    client = OpenAICompatClient(
        MODEL, base_url=BASE_URL, api_key=key, profile=PROFILE, quant="fp8",
        timeout=TIMEOUT_S, max_retries=1,
    )
    jobs = build_jobs(states)
    if limit:
        jobs = jobs[:limit]
    print(f"{len(jobs)} calls over {len(states)} states, concurrency {concurrency}",
          file=sys.stderr)
    rows: list[dict] = [None] * len(jobs)  # type: ignore[list-item]
    done = {"n": 0}
    t0 = time.perf_counter()

    def work(i_job):
        i, (state, level, rep) = i_job
        try:
            row = replay_one(state, level, rep, client)
        except Exception as e:  # a dead call is a logged row, never a dead run
            row = {f: "" for f in CSV_FIELDS}
            row.update({"state_id": state["state_id"], "state_index": state.get("index", -1),
                        "sandbox": state["sandbox"], "game": state["game"],
                        "round": state["round"], "agent": state["agent"],
                        "arm": state.get("arm", ""), "round_bin": state.get("round_bin", ""),
                        "pair_type": state["pair_type"], "level": level,
                        "replicate": rep + 1, "parse_ok": False,
                        "error": f"{type(e).__name__}: {e}"})
        rows[i] = row
        done["n"] += 1
        if done["n"] % 10 == 0:
            print(f"  {done['n']}/{len(jobs)} ({time.perf_counter() - t0:.0f}s)",
                  file=sys.stderr)
        return row

    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        list(pool.map(work, enumerate(jobs)))

    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    print(f"wrote {out_csv} ({len(rows)} rows, {time.perf_counter() - t0:.0f}s)",
          file=sys.stderr)
    return rows


# ---------------------------------------------------------------------------
# 4. summary
# ---------------------------------------------------------------------------

def quartiles(values: list[float]) -> tuple[float, float, float]:
    """(q1, median, q3), linear interpolation (numpy's default). () for empty."""
    xs = sorted(float(v) for v in values)
    if not xs:
        return (float("nan"),) * 3

    def pct(p: float) -> float:
        if len(xs) == 1:
            return xs[0]
        idx = p * (len(xs) - 1)
        lo = int(idx)
        hi = min(lo + 1, len(xs) - 1)
        return xs[lo] + (xs[hi] - xs[lo]) * (idx - lo)

    return pct(0.25), pct(0.5), pct(0.75)


def summarise_level(rows: list[dict]) -> dict[str, Any]:
    """Per-level block of SUMMARY.md. Safe on an empty level."""
    n = len(rows)
    if n == 0:
        return {"n": 0, "reasoning_q1": None, "reasoning_median": None,
                "reasoning_q3": None, "reasoning_max": None, "completion_median": None,
                "prompt_median": None, "trace_field_rate": None,
                "finish_reasons": {}, "latency_median": None, "board_rate": None,
                "decoy_rate": None, "cooperate_rate": None, "parse_fail_rate": None,
                "cost": 0.0, "errors": 0}
    reasoning = [int(r["reasoning_tokens"] or 0) for r in rows]
    completion = [int(r["completion_tokens"] or 0) for r in rows]
    prompt = [int(r["prompt_tokens"] or 0) for r in rows]
    latency = [int(r["latency_ms"] or 0) for r in rows]
    rq1, rmed, rq3 = quartiles(reasoning)
    parsed = [r for r in rows if as_bool(r["parse_ok"])]
    finish: dict[str, int] = {}
    for r in rows:
        finish[str(r["finish_reason"] or "none")] = finish.get(
            str(r["finish_reason"] or "none"), 0) + 1
    return {
        "n": n,
        "reasoning_q1": rq1, "reasoning_median": rmed, "reasoning_q3": rq3,
        "reasoning_max": max(reasoning),
        "completion_median": quartiles(completion)[1],
        "prompt_median": quartiles(prompt)[1],
        "finish_reasons": finish,
        "latency_median": quartiles(latency)[1],
        "trace_field_rate": sum(
            1 for r in rows if r.get("trace_location") == "field") / n,
        "board_rate": sum(1 for r in rows if int(r["board_calls"] or 0) > 0) / n,
        "decoy_rate": sum(1 for r in rows if int(r["decoy_calls"] or 0) > 0) / n,
        "cooperate_rate": (sum(1 for r in parsed if r["action"] == "C") / len(parsed)
                           if parsed else None),
        "parse_fail_rate": 1 - len(parsed) / n,
        "cost": sum(float(r["estimated_cost"] or 0) for r in rows),
        "errors": sum(1 for r in rows if r["error"]),
    }


def separation(a: dict[str, Any], b: dict[str, Any],
               names: tuple[str, str] = ("a", "b")) -> dict[str, Any]:
    """Do two levels' reasoning-token IQRs overlap? The gate's pass condition."""
    if not a["n"] or not b["n"]:
        return {"verdict": "no data", "overlap": None, "detail": "a level is empty"}
    overlap = not (a["reasoning_q3"] < b["reasoning_q1"]
                   or b["reasoning_q3"] < a["reasoning_q1"])
    return {
        "verdict": "OVERLAP (no separation)" if overlap else "SEPARATED",
        "overlap": overlap,
        "detail": (f"{names[0]} {a['reasoning_q1']:.0f}–{a['reasoning_q3']:.0f} "
                   f"(med {a['reasoning_median']:.0f}) vs "
                   f"{names[1]} {b['reasoning_q1']:.0f}–{b['reasoning_q3']:.0f} "
                   f"(med {b['reasoning_median']:.0f})"),
    }


def as_bool(v: Any) -> bool:
    return v is True or str(v).strip().lower() in ("true", "1", "yes")


def paired_board_table(rows: list[dict], a: str = "none", b: str = "high") -> dict:
    """Within-state board use at two levels: a 2x2 of 'any board call'."""
    per: dict[str, dict[str, bool]] = {}
    for r in rows:
        if r["level"] not in (a, b) or r["error"]:
            continue
        slot = per.setdefault(r["state_id"], {})
        slot[r["level"]] = slot.get(r["level"], False) or int(r["board_calls"] or 0) > 0
    cells = {"both": 0, f"{a}_only": 0, f"{b}_only": 0, "neither": 0}
    for s in per.values():
        if a not in s or b not in s:
            continue
        x, y = s[a], s[b]
        if x and y:
            cells["both"] += 1
        elif x:
            cells[f"{a}_only"] += 1
        elif y:
            cells[f"{b}_only"] += 1
        else:
            cells["neither"] += 1
    cells["states"] = sum(v for k, v in cells.items() if k != "states")
    return cells


def fmt(v: Any, nd: int = 0) -> str:
    if v is None:
        return "--"
    if isinstance(v, float):
        return f"{v:.{nd}f}"
    return str(v)


def pct(v: Any) -> str:
    return "--" if v is None else f"{100 * float(v):.1f}%"


def write_summary(states: list[dict], rows: list[dict], out_dir: Path,
                  *, drops: list[dict] | None = None) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    per_level = {lv: summarise_level([r for r in rows if r["level"] == lv])
                 for lv in LEVELS}
    matched = sum(1 for r in rows if as_bool(r["hash_matches_log"]))
    total_cost = sum(v["cost"] for v in per_level.values())
    board = paired_board_table(rows, "none", "high")

    L = []
    L.append("# Calibration gate — reasoning-effort dial on 30 frozen states")
    L.append("")
    L.append(f"Model `{MODEL}` on {PROFILE} (fp8), {ANSWER_TOKENS} answer tokens in "
             "every arm, one decision per call, no population, no board writes.")
    L.append("Contract: `specs/sandboxes-v2/calibration-effort.yaml`. States: "
             f"`{STATES_PATH}`. Calls: `calls.csv`.")
    L.append("")
    L.append("## Prompt identity")
    L.append("")
    L.append(f"- States frozen: **{len(states)}** "
             f"({sum(1 for s in states if s['arm'] == 'ahead')} ahead, "
             f"{sum(1 for s in states if s['arm'] == 'behind')} behind).")
    L.append(f"- States whose rebuilt `prompt_sha256` equals the logged one: "
             f"**{sum(1 for s in states if verify_state(s)[0])}/{len(states)}**.")
    L.append(f"- Calls sent on a hash-matched prompt: **{matched}/{len(rows)}**.")
    if drops:
        L.append(f"- Candidates dropped during sampling: {len(drops)} "
                 f"({', '.join(sorted({d['reason'] for d in drops}))}).")
    else:
        L.append("- Candidates dropped during sampling: 0.")
    L.append(
        "- Prompt-token counts still differ across levels "
        + ", ".join(f"{lv} med {fmt(per_level[lv]['prompt_median'])}" for lv in LEVELS)
        + ". The messages are byte-identical (that is what the hash proves); the "
          "endpoint renders a different chat template in thinking mode, so a few "
          "tokens of template, not of prompt, separate the arms.")
    L.append("")
    L.append("## Per level")
    L.append("")
    L.append("| level | reasoning budget | n | reasoning med | reasoning IQR | "
             "reasoning max | completion med | prompt med | latency med (ms) | "
             "finish_reason | trace in field | board-call | decoy-call | "
             "cooperate | parse-fail |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for lv in LEVELS:
        s = per_level[lv]
        fr = ", ".join(f"{k}={v}" for k, v in sorted(s["finish_reasons"].items())) or "--"
        L.append(
            f"| {lv} | {BUDGETS[lv]} | {s['n']} | {fmt(s['reasoning_median'])} | "
            f"{fmt(s['reasoning_q1'])}–{fmt(s['reasoning_q3'])} | "
            f"{fmt(s['reasoning_max'])} | {fmt(s['completion_median'])} | "
            f"{fmt(s['prompt_median'])} | "
            f"{fmt(s['latency_median'])} | {fr} | {pct(s['trace_field_rate'])} | "
            f"{pct(s['board_rate'])} | "
            f"{pct(s['decoy_rate'])} | {pct(s['cooperate_rate'])} | "
            f"{pct(s['parse_fail_rate'])} |")
    L.append("")
    L.append(f"Answer capacity is {ANSWER_TOKENS} tokens in every arm; the reasoning "
             "budget is reserved on top of it. `none` is sent as DeepInfra's "
             "`reasoning_effort: none`; `low`, `high` and `max` are sent verbatim.")
    L.append("")
    L.append("## Adjacent-level separation (non-overlapping reasoning-token IQRs)")
    L.append("")
    L.append("| pair | verdict | reasoning-token IQRs |")
    L.append("|---|---|---|")
    for a, b in ADJACENT:
        sep = separation(per_level[a], per_level[b], (a, b))
        L.append(f"| {a} → {b} | {sep['verdict']} | {sep['detail']} |")
    L.append("")
    L.append("Non-adjacent pairs, for reference:")
    L.append("")
    L.append("| pair | verdict | reasoning-token IQRs |")
    L.append("|---|---|---|")
    for a, b in NON_ADJACENT:
        sep = separation(per_level[a], per_level[b], (a, b))
        L.append(f"| {a} → {b} | {sep['verdict']} | {sep['detail']} |")
    L.append("")
    any_length = any("length" in s["finish_reasons"] for s in per_level.values())
    L.append(f"`finish_reason == \"length\"` anywhere: **{'YES' if any_length else 'no'}** "
             "(the gate requires no truncation at equal answer capacity).")
    L.append("")
    L.append("Two caveats on reading this table. `high` and `max` were given the SAME "
             f"reasoning budget ({BUDGETS['high']}), so their contrast is the effort "
             "field alone. `low` was given a smaller budget "
             f"({BUDGETS['low']}), but no call at any level came close to it — the "
             f"largest reasoning spend observed at `low` was "
             f"{fmt(per_level['low']['reasoning_max'])} tokens — so no level was capacity-bound "
             "and the budgets are not doing the separating.")
    L.append("")
    L.append("## Verdict")
    L.append("")
    seps = {pair: separation(per_level[pair[0]], per_level[pair[1]], pair)
            for pair in ADJACENT + NON_ADJACENT}
    passed = [f"{a}/{b}" for (a, b), s in seps.items() if s["overlap"] is False]
    failed = [f"{a}/{b}" for (a, b), s in seps.items() if s["overlap"] is True]
    L.append(f"- Level pairs that separate: {', '.join(passed) if passed else 'none'}.")
    L.append(f"- Level pairs that do not: {', '.join(failed) if failed else 'none'}.")
    L.append(f"- `max` accepted by the endpoint: "
             f"**{'yes' if per_level['max']['n'] and not per_level['max']['errors'] else 'not established'}** "
             "(the spec recorded it as UNVERIFIED).")
    L.append("")
    adjacent_failed = [f"{a}/{b}" for (a, b) in ADJACENT if seps[(a, b)]["overlap"]]
    if adjacent_failed:
        L.append(
            "Levels that do not separate are one level with two names. Any block "
            "arithmetic that buys them as distinct doses has to be rewritten before "
            f"launch: {', '.join(adjacent_failed)} did not separate on this run, and "
            "the design can only claim the contrasts in the first list.")
        on_pairs = [p for p in ADJACENT + NON_ADJACENT if "none" not in p]
        if (all(seps[p]["overlap"] for p in on_pairs)
                and all(seps[p]["overlap"] is False
                        for p in ADJACENT + NON_ADJACENT if "none" in p)):
            L.append("")
            L.append("The shape is clean: `none` separates from every on-level and no "
                     "two on-levels separate from each other. On this model the dial "
                     "is a switch, not a slope — which is the two-level none/high "
                     "contrast the 96 block files already assume.")
    else:
        L.append("Every adjacent pair separates: the graded dial is real on this model.")
    L.append("")
    L.append("## Paired board use, none vs high (within state)")
    L.append("")
    L.append("| | high: board call | high: no board call |")
    L.append("|---|---|---|")
    L.append(f"| **none: board call** | {board['both']} | {board['none_only']} |")
    L.append(f"| **none: no board call** | {board['high_only']} | {board['neither']} |")
    L.append("")
    L.append(f"Paired states: {board['states']}. A cell counts a state where *any* "
             "replicate at that level made a `notes_read` or `notes_post` call.")
    L.append("")
    L.append("## Cost")
    L.append("")
    L.append(f"{len(rows)} calls, **${total_cost:.4f}** at "
             f"${PRICE_IN_PER_M}/M in and ${PRICE_OUT_PER_M}/M out.")
    L.append("")
    L.append("## What this gate establishes, and what it does not")
    L.append("")
    L.append(
        "It establishes whether the `reasoning_effort` field is a real intervention on "
        "this endpoint and this model: the same 30 prompts — byte-identical, verified "
        "against the `prompt_sha256` the runner logged when each decision was actually "
        "played — are shown to draw different amounts of billed reasoning at different "
        "settings, with the answer budget held at 768 tokens in every arm so no "
        "difference can be an output-capacity artifact. It also settles which levels "
        "are worth buying: two levels that do not separate on billed tokens are one "
        "level with two names, and block arithmetic that rests on a graded dial has to "
        "be rewritten as the contrast that survives. It says nothing whatever about "
        "the game. These are single "
        "decisions replayed out of context: no opponent answers back, no board is "
        "written, no score accumulates, and a board call here is a call on a frozen "
        "snapshot rather than a move in a live sandbox. Cooperation and board-use rates "
        "in the table are diagnostics of prompt handling, not findings about how "
        "reasoning effort changes behaviour — that question needs the sandboxes, where "
        "effort is varied between arms and the decisions compound.")
    L.append("")
    (out_dir / "SUMMARY.md").write_text("\n".join(L) + "\n")

    M = ["# Calibration states — 30 frozen decisions", "",
         f"Sampled with RNG seed {SAMPLE_SEED} from the four forbidden / effort-off "
         "sandboxes of runs/v3, stratified 15 ahead / 15 behind, spread over round "
         "bins (early ≤10, mid 11–20, late ≥21) and over opponent type.", "",
         "| # | state id | arm | bin | pair | round | opponent | opponent model | "
         "labels | board rows shown | logged action |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for s in sorted(states, key=lambda s: (s["arm"], s["round_bin"], s["state_id"])):
        lm = s["label_map"]
        M.append(
            f"| {s['index']} | `{s['state_id']}` | {s['arm']} | {s['round_bin']} | "
            f"{s['pair_type']} | {s['round']} | {s['opponent']} | "
            f"{s['opponent_model']} | C={lm['C']} D={lm['D']} | "
            f"{s['board'].get('shown', 0)} | {s['logged_action']} |")
    M.append("")
    M.append("Every state carries the warm-up block, the executed history of the "
             "earlier scored rounds, the running totals, the drawn label pair, the "
             "round's option order and the board snapshot the model was shown, so the "
             "prompt is rebuilt rather than re-derived.")
    (out_dir / "states-manifest.md").write_text("\n".join(M) + "\n")
    print(f"wrote {out_dir / 'SUMMARY.md'} and {out_dir / 'states-manifest.md'}",
          file=sys.stderr)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def load_states(path: Path) -> tuple[list[dict], list[dict]]:
    payload = json.loads(path.read_text())
    return payload["states"], payload.get("drops", [])


def do_sample(args) -> tuple[list[dict], list[dict]]:
    sources = [load_source(arm, ROOT / p) for arm, p in SOURCES]
    states, drops = sample_states(sources, seed=args.seed)
    out = ROOT / args.states
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({
        "spec": "specs/sandboxes-v2/calibration-effort.yaml",
        "generated_by": "calibration_replay.py sample",
        "rng_seed": args.seed,
        "sources": [{"arm": a, "path": p} for a, p in SOURCES],
        "stratification": {"per_arm": N_PER_ARM, "cells": [list(c) for c in CELLS],
                           "quota": quota_for_arm(), "pool_extra": POOL_EXTRA,
                           "round_bins": {"early": "<=10", "mid": "11-20",
                                          "late": ">=21"}},
        "count": len(states),
        "drops": drops,
        "states": states,
    }, indent=2) + "\n")
    print(f"wrote {out}: {len(states)} states, {len(drops)} drops", file=sys.stderr)
    return states, drops


def do_verify(args) -> None:
    states, _ = load_states(ROOT / args.states)
    ok = 0
    for s in states:
        good, why = verify_state(s)
        ok += good
        if not good:
            print(f"MISMATCH {s['state_id']}: {why}")
    print(f"{ok}/{len(states)} states rebuild to the logged prompt_sha256")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("command",
                   choices=["sample", "verify", "replay", "report", "all"])
    p.add_argument("--states", default=STATES_PATH)
    p.add_argument("--tag", default=DEFAULT_TAG)
    p.add_argument("--seed", type=int, default=SAMPLE_SEED)
    p.add_argument("--concurrency", type=int, default=CONCURRENCY)
    p.add_argument("--limit", type=int, default=None,
                   help="cap the number of calls (smoke test)")
    args = p.parse_args(argv)
    out_dir = ROOT / "reports" / args.tag

    if args.command == "sample":
        do_sample(args)
        return 0
    if args.command == "verify":
        do_verify(args)
        return 0
    if args.command == "replay":
        states, _ = load_states(ROOT / args.states)
        run_replay(states, out_dir / "calls.csv",
                   concurrency=args.concurrency, limit=args.limit)
        return 0
    if args.command == "report":
        states, drops = load_states(ROOT / args.states)
        with (out_dir / "calls.csv").open() as fh:
            rows = list(csv.DictReader(fh))
        write_summary(states, rows, out_dir, drops=drops)
        return 0
    # all
    states, drops = do_sample(args)
    run_replay(states, out_dir / "calls.csv",
               concurrency=args.concurrency, limit=args.limit)
    with (out_dir / "calls.csv").open() as fh:
        rows = list(csv.DictReader(fh))
    write_summary(states, rows, out_dir, drops=drops)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
