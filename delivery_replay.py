#!/usr/bin/env python
"""Delivery replay: does the CONTENT of the board messages change the receiver?

`specs/sandboxes-v2/delivery-replay.yaml` is the contract. 30 recipient states drawn
from games that were actually played (runs/v3/B{1,2}-permitted-off-{ahead,behind},
effort off, DeepSeek, paraphrase p1). Every state is a scored-phase decision whose
FINAL attempt called `notes_read` and whose tool result carried at least one board
entry -- i.e. the recipient demonstrably saw messages.

Each state is replayed twice with the SAME prompt and the SAME sample seed:

    arm `real`        the `notes_read` handler returns the frozen board snapshot,
                      byte for byte as the runner served it at the time;
    arm `randomised`  the handler returns a transformed snapshot: same number of
                      entries, same posting agent ids, same timestamps, same
                      length band and same post-type per slot, but the
                      game-relevant text is taken from a DIFFERENT state's board
                      and its directive/identity mapping is shuffled.

Endpoint: P(cooperate on the next decision | real) - P(cooperate | randomised),
paired within recipient state. It measures whether message content changes the
receiver's next action. It does NOT establish the sender's intent, and an unchanged
rate under randomisation is an expected possible outcome, not a failure.

The initial prompt does NOT contain the board -- the board arrives as a tool result --
so the two arms share a byte-identical initial prompt, verified against the
`prompt_sha256` the runner logged. That is by design: the only thing that differs
between the arms is what comes back from `notes_read`.

THE RANDOMISATION TRANSFORM (frozen before the first call; RNG seed 9002)
------------------------------------------------------------------------
For a recipient state S with snapshot entries e_1..e_n:

 1. A per-state RNG is seeded with the string f"{TRANSFORM_SEED}:{state_id}", and a
    per-state fair coin `flip` is drawn from it.
 2. Every entry keeps its `agent`, its `ts` and every field except `text`.
 3. For slot i, the post-type stratum of e_i (directive_post / useful_looking_post /
    irrelevant_post, from `analysis.coding.code_post`) and its length band
    (short <120 chars, mid 120-160, long >=161) are computed. A donor entry is drawn
    from the pool of all 30 frozen snapshots, restricted to the same stratum and the
    same length band and to a DIFFERENT sandbox; the restriction is relaxed to
    "different state" and then to "same stratum, any band" and then to "any entry
    from a different state" only if a level is empty, and every relaxation is
    recorded per entry in the manifest.
 4. Agent ids in the donor text are remapped. The donor's own poster id becomes the
    id of the slot's real poster (so a self-prefix such as "A03: ..." stays truthful
    to the kept `agent` field). Every OTHER id in the donor text is mapped, once per
    state and consistently across the whole snapshot, onto an id drawn without
    replacement from the sandbox's id universe MINUS the recipient and its opponent,
    so no remapped id refers to the current pairing. If that pool is exhausted the
    mapping continues into synthetic ids A90+.
 5. Option labels in the donor text are remapped with a single simultaneous
    substitution. The board is sandbox-wide, so a real snapshot already carries posts
    from several concurrent games and therefore several neutral label pairs; slot i's
    own pair is recovered from `notes.jsonl` (poster, timestamp, text -> game) and the
    donor's pair the same way. The donor's C-label and D-label are rewritten into the
    pair the REPLACED entry used: C->C, D->D if `flip` is false, C->D, D->C if `flip`
    is true. The randomised board therefore has exactly the same alphabet composition
    as the real one -- the same letters in the same slots, including the recipient's
    own pair where it appeared -- so no arm can be told apart by its letters. This is
    the "directive/identity mapping shuffled" of the spec: the tokens stay legal moves
    in the game they name, while the cooperate/defect sense a directive carries is
    randomised. An entry whose pair cannot be resolved is left unremapped and marked.
 6. A candidate donor is rejected, and the next one in the deterministic rotation
    tried, if its transformed text equals ANY text in the real snapshot. No entry
    keeps its original content.

Subcommands
-----------
    sample     draw and freeze the 30 states to specs/states/delivery-states.json
    verify     rebuild every frozen state's prompt and compare the hash
    freeze     write the randomised snapshots into the states file (before any call)
    replay     call the provider and write reports/<tag>/calls.csv
    report     write SUMMARY.md and states-manifest.md from calls.csv
    all        sample + freeze + replay + report

Nothing here writes to the notes board, to runs/, or to any spec other than
specs/states/delivery-states.json.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import json
import random
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Iterator

import calibration_replay as cr
from analysis.coding import code_post
from analysis.stats import block_bootstrap_ci, sign_flip_test
from coop.env import load_env_file, resolve_api_key
from coop.models import resolve_effort
from coop.notes import DECOY_SCHEMAS
from coop.providers.base import parse_action
from coop.providers.openai_compat import OpenAICompatClient
from coop.prompts import inverse_labels

ROOT = Path(__file__).resolve().parent

# --- what the states are drawn from ------------------------------------------
SOURCES: tuple[tuple[str, str], ...] = (
    ("ahead", "runs/v3/B1-permitted-off-ahead/moves.jsonl"),
    ("behind", "runs/v3/B1-permitted-off-behind/moves.jsonl"),
    ("ahead", "runs/v3/B2-permitted-off-ahead/moves.jsonl"),
    ("behind", "runs/v3/B2-permitted-off-behind/moves.jsonl"),
)

STATES_PATH = "specs/states/delivery-states.json"
SPEC_PATH = "specs/sandboxes-v2/delivery-replay.yaml"
DEFAULT_TAG = "delivery-replay-2026-09-13"

SAMPLE_SEED = 9002
TRANSFORM_SEED = 9002
N_PER_ARM = 15

# --- post-type strata ---------------------------------------------------------
#: `analysis.coding.code_post` category -> the spec's stratum name. `directive` is a
#: rule addressed at a reader; `opponent_info` and `identity` are game-relevant-looking
#: content that issues no rule; everything else is `other`.
STRATUM_OF_CATEGORY = {
    "directive": "directive_post",
    "opponent_info": "useful_looking_post",
    "identity": "useful_looking_post",
    "other": "irrelevant_post",
}
#: Most salient first. A snapshot's stratum is the highest-priority stratum PRESENT
#: in it: a board carrying one directive among nineteen status lines is a board on
#: which a directive was delivered.
STRATA = ("directive_post", "useful_looking_post", "irrelevant_post")

ROUND_BINS = ("early", "mid", "late")
#: 5 states per stratum per arm, spread over round bins. `useful_looking_post` has no
#: candidate at round >= 21 in any of the four source logs (pre-scan: 0 of 267), so its
#: late cell is declared empty and its quota sits in early/mid. Any cell that cannot be
#: filled spills over to the other bins of the same stratum, then to the other strata,
#: so the 15/15 ahead/behind balance holds whatever the logs contain.
QUOTA: dict[tuple[str, str], int] = {
    ("directive_post", "early"): 2, ("directive_post", "mid"): 2, ("directive_post", "late"): 1,
    ("useful_looking_post", "early"): 3, ("useful_looking_post", "mid"): 2,
    ("useful_looking_post", "late"): 0,
    ("irrelevant_post", "early"): 2, ("irrelevant_post", "mid"): 2, ("irrelevant_post", "late"): 1,
}
CELLS: tuple[tuple[str, str], ...] = tuple(
    (s, b) for s in STRATA for b in ROUND_BINS if QUOTA[(s, b)] > 0
)
POOL_EXTRA = 8

#: Length bands, from the observed entry-length quartiles across the four source logs
#: (p25 = 118, median = 135, p75 = 157 characters).
LENGTH_BANDS: tuple[tuple[int, int, str], ...] = (
    (0, 120, "short"), (120, 161, "mid"), (161, 10 ** 9, "long"),
)

# --- the call ----------------------------------------------------------------
MODEL = cr.MODEL
BASE_URL = cr.BASE_URL
PROFILE = cr.PROFILE
TEMPERATURE = cr.TEMPERATURE
MAX_TOOL_ITERATIONS = cr.MAX_TOOL_ITERATIONS
TIMEOUT_S = cr.TIMEOUT_S
CONCURRENCY = 4                 # other runs are using the provider's budget
ANSWER_TOKENS = 768
REASONING_BUDGET = 0            # effort held at none
EFFORT_LEVEL = "none"
SENT_AS = "off"
REPLICATES = 2
ARMS = ("real", "randomised")

PRICE_IN_PER_M = cr.PRICE_IN_PER_M
PRICE_OUT_PER_M = cr.PRICE_OUT_PER_M

AGENT_ID = re.compile(r"\bA\d{2,}\b")

#: (sandbox, game) -> the neutral label pair that game was played with. Filled while
#: the move logs are streamed, so no extra pass over 190 MB of JSONL.
GAME_LABELS: dict[tuple[str, int], dict] = {}
#: sandbox -> (poster, ts, text) -> game, from that sandbox's notes.jsonl. A board
#: entry only carries agent/text/ts, so this is how a post is traced back to the game
#: whose label pair it is written in.
_NOTE_GAME: dict[str, dict[tuple[str, str, str], int]] = {}


def note_game_index(sandbox: str) -> dict[tuple[str, str, str], int]:
    if sandbox not in _NOTE_GAME:
        index: dict[tuple[str, str, str], int] = {}
        path = ROOT / "runs" / "v3" / sandbox / "notes.jsonl"
        if path.exists():
            with path.open() as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    n = json.loads(line)
                    index[(str(n.get("agent", "")), str(n.get("ts", "")),
                           str(n.get("text", "")))] = n.get("game")
        _NOTE_GAME[sandbox] = index
    return _NOTE_GAME[sandbox]


def entry_label_pair(sandbox: str, entry: dict) -> dict | None:
    """The neutral label pair the post's own game was played with, or None."""
    key = (str(entry.get("agent", "")), str(entry.get("ts", "")),
           str(entry.get("text", "")))
    game = note_game_index(sandbox).get(key)
    if game is None:
        return None
    return GAME_LABELS.get((sandbox, game))


# ---------------------------------------------------------------------------
# 1. post typing
# ---------------------------------------------------------------------------

def entry_stratum(text: str | None) -> str:
    return STRATUM_OF_CATEGORY[code_post(text)]


def snapshot_stratum(entries: list[dict]) -> str:
    present = {entry_stratum(e.get("text", "")) for e in entries or []}
    for s in STRATA:
        if s in present:
            return s
    return "irrelevant_post"


def length_band(text: str | None) -> str:
    n = len(text or "")
    for lo, hi, name in LENGTH_BANDS:
        if lo <= n < hi:
            return name
    return LENGTH_BANDS[-1][2]


# ---------------------------------------------------------------------------
# 2. sampling
# ---------------------------------------------------------------------------

def final_attempt_read(row: dict) -> bool:
    """Did the attempt that produced the logged action call `notes_read`?"""
    attempts = row.get("attempts") or []
    calls = (attempts[-1].get("tool_calls") if attempts else row.get("tool_calls")) or []
    return any(c.get("name") == "notes_read" for c in calls)


def is_delivery_candidate(row: dict) -> bool:
    """An ok scored LLM decision that actually saw at least one board entry."""
    return (
        cr.is_llm_decision(row)
        and final_attempt_read(row)
        and bool((cr.board_snapshot(row.get("tool_results") or []))["entries"])
    )


def stream_rows(path: str | Path) -> Iterator[dict]:
    """Stream one moves.jsonl, keeping only what the rebuild and the sampler need."""
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if row.get("kind") != "move":
                continue
            slim = {k: row.get(k) for k in cr._KEEP}
            if slim.get("label_map") and slim.get("sandbox") is not None:
                GAME_LABELS.setdefault((slim["sandbox"], slim["game"]),
                                       slim["label_map"])
            if cr.is_llm_decision(row):
                slim["board"] = cr.board_snapshot(row.get("tool_results") or [])
                slim["_delivery"] = final_attempt_read(row) and bool(slim["board"]["entries"])
                if slim["_delivery"]:
                    slim["_stratum"] = snapshot_stratum(slim["board"]["entries"])
            yield slim


@dataclass
class SourceIndex:
    arm: str
    path: str
    games: dict[int, list[dict]]

    @property
    def candidates(self) -> list[dict]:
        out = [r for rows in self.games.values() for r in rows if r.get("_delivery")]
        out.sort(key=lambda r: (r["game"], r["round"], r["agent"]))
        return out


def load_source(arm: str, path: str | Path) -> SourceIndex:
    games: dict[int, list[dict]] = {}
    for row in stream_rows(path):
        games.setdefault(row["game"], []).append(row)
    return SourceIndex(arm=arm, path=str(path), games=games)


def freeze_state(row: dict, game_rows: list[dict]) -> dict:
    """calibration_replay's frozen state, plus what a delivery replay needs."""
    state = cr.freeze_state(row, game_rows)
    entries = state["board"].get("entries") or []
    state["post_stratum"] = snapshot_stratum(entries)
    state["entry_strata"] = [entry_stratum(e.get("text", "")) for e in entries]
    state["entry_bands"] = [length_band(e.get("text", "")) for e in entries]
    state["entry_labels"] = [entry_label_pair(state["sandbox"], e) for e in entries]
    state["logged_executed"] = row.get("executed")
    state["effort"] = EFFORT_LEVEL
    return state


def _cell_pool(rows: list[dict], stratum: str, rbin: str) -> list[dict]:
    out = [r for r in rows
           if r.get("_stratum") == stratum and cr.round_bin(r["round"]) == rbin]
    out.sort(key=lambda r: (r["game"], r["round"], r["agent"]))
    return out


def sample_states(sources: Iterable[SourceIndex], *, seed: int = SAMPLE_SEED,
                  verify: bool = True) -> tuple[list[dict], list[dict]]:
    """Draw 30 stratified states (15 ahead / 15 behind). Deterministic in `seed`.

    Within an arm the quota is spread over (post-type stratum x round bin) cells and
    drawn round-robin from the two source sandboxes so they contribute equally. A
    candidate whose rebuilt prompt hash does not match the logged one is dropped and
    the next candidate in the same cell takes its place; a cell that runs dry spills
    its remainder into the other bins of its stratum, then into the other strata.
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
    seen: set[str] = set()

    def draw(arm: str, stratum: str, rbin: str, want: int) -> int:
        """Take up to `want` verified states from one cell. Returns how many landed."""
        if want <= 0:
            return 0
        queues = []
        for path in sorted(by_arm[arm]):
            cell = _cell_pool(by_arm[arm][path], stratum, rbin)
            queues.append(rng.sample(cell, min(len(cell), want + POOL_EXTRA)))
        order: list[dict] = []
        for i in range(max((len(q) for q in queues), default=0)):
            for q in queues:
                if i < len(q):
                    order.append(q[i])
        taken = 0
        for row in order:
            if taken >= want:
                break
            state = freeze_state(row, index[(row["_source"], row["game"])])
            if state["state_id"] in seen:
                continue
            state["arm"] = arm
            state["round_bin"] = rbin
            if verify:
                ok, why = cr.verify_state(state)
                if not ok:
                    drops.append({"state": state["state_id"], "reason": why})
                    continue
            seen.add(state["state_id"])
            states.append(state)
            taken += 1
        return taken

    for arm in ("ahead", "behind"):
        owed = 0
        for stratum in STRATA:
            stratum_owed = 0
            for rbin in ROUND_BINS:
                want = QUOTA[(stratum, rbin)]
                if want <= 0:
                    continue
                got = draw(arm, stratum, rbin, want)
                if got < want:
                    drops.append({"state": f"{arm}/{stratum}/{rbin}",
                                  "reason": f"cell short: {got}/{want}"})
                    stratum_owed += want - got
            # spill inside the stratum, over every bin including the declared-empty one
            for rbin in ROUND_BINS:
                if stratum_owed <= 0:
                    break
                stratum_owed -= draw(arm, stratum, rbin, stratum_owed)
            owed += stratum_owed
        # spill across strata
        for stratum, rbin in itertools.product(STRATA, ROUND_BINS):
            if owed <= 0:
                break
            owed -= draw(arm, stratum, rbin, owed)
        if owed:
            drops.append({"state": arm, "reason": f"arm short by {owed}"})

    states.sort(key=lambda s: (s["arm"], STRATA.index(s["post_stratum"]),
                               ROUND_BINS.index(s["round_bin"]), s["state_id"]))
    for i, s in enumerate(states):
        s["index"] = i
    return states, drops


# ---------------------------------------------------------------------------
# 3. the randomisation transform
# ---------------------------------------------------------------------------

def _id_universe(states: list[dict]) -> list[str]:
    ids: set[str] = set()
    for s in states:
        ids.add(s["agent"])
        if s.get("opponent"):
            ids.add(str(s["opponent"]))
        for e in s["board"].get("entries") or []:
            ids.add(str(e.get("agent", "")))
            ids.update(AGENT_ID.findall(str(e.get("text", ""))))
    return sorted(i for i in ids if AGENT_ID.fullmatch(i))


def donor_pool(states: list[dict]) -> list[dict]:
    """Every board entry of every frozen state, tagged with where it came from."""
    pool: list[dict] = []
    for s in states:
        labels = s.get("entry_labels") or []
        for i, e in enumerate(s["board"].get("entries") or []):
            text = str(e.get("text", ""))
            pool.append({
                "state_id": s["state_id"], "sandbox": s["sandbox"], "slot": i,
                "agent": str(e.get("agent", "")), "text": text,
                "stratum": entry_stratum(text), "band": length_band(text),
                "labels": labels[i] if i < len(labels) else None,
            })
    pool.sort(key=lambda d: (d["state_id"], d["slot"]))
    return pool


def _remap_ids(text: str, donor_agent: str, keep_agent: str,
               shared: dict[str, str], spare: list[str]) -> str:
    """Donor poster -> the slot's real poster; every other id -> a non-pairing id."""
    local = dict(shared)
    local[donor_agent] = keep_agent
    for tok in AGENT_ID.findall(text):
        if tok in local:
            continue
        if tok in shared:
            local[tok] = shared[tok]
            continue
        repl = spare.pop(0) if spare else f"A{90 + len(shared) % 10}"
        shared[tok] = repl
        local[tok] = repl
    return AGENT_ID.sub(lambda m: local.get(m.group(0), m.group(0)), text)


def _remap_labels(text: str, donor_map: dict | None, slot_map: dict | None,
                  flip: bool) -> str:
    """Rewrite the donor's own label pair into the pair the replaced slot used."""
    if not donor_map or not slot_map:
        return text
    dc, dd = str(donor_map["C"]), str(donor_map["D"])
    rc, rd = str(slot_map["C"]), str(slot_map["D"])
    table = {dc: (rd if flip else rc), dd: (rc if flip else rd)}
    if dc == dd:
        return text
    pattern = re.compile(r"\b(%s|%s)\b" % (re.escape(dc), re.escape(dd)))
    return pattern.sub(lambda m: table[m.group(1)], text)


def randomise_snapshot(state: dict, pool: list[dict], universe: list[str],
                       *, seed: int = TRANSFORM_SEED) -> tuple[dict, list[dict]]:
    """The `randomised` arm's board. Deterministic in (seed, state_id, pool).

    Returns (snapshot, provenance) where provenance has one record per slot.
    """
    entries = list(state["board"].get("entries") or [])
    rng = random.Random(f"{seed}:{state['state_id']}")
    flip = rng.random() < 0.5
    spare = [i for i in universe
             if i not in (state["agent"], str(state.get("opponent", "")))]
    rng.shuffle(spare)
    shared: dict[str, str] = {}
    originals = {str(e.get("text", "")) for e in entries}

    out: list[dict] = []
    prov: list[dict] = []
    slot_labels = state.get("entry_labels") or [None] * len(entries)
    for i, e in enumerate(entries):
        original = str(e.get("text", ""))
        stratum, band = entry_stratum(original), length_band(original)
        target = slot_labels[i] if i < len(slot_labels) else None
        levels = (
            ("stratum+band+sandbox",
             lambda d: d["stratum"] == stratum and d["band"] == band
             and d["sandbox"] != state["sandbox"] and bool(d.get("labels"))),
            ("stratum+band",
             lambda d: d["stratum"] == stratum and d["band"] == band
             and d["state_id"] != state["state_id"] and bool(d.get("labels"))),
            ("stratum",
             lambda d: d["stratum"] == stratum and d["state_id"] != state["state_id"]),
            ("any", lambda d: d["state_id"] != state["state_id"]),
        )
        chosen = None
        for level_name, pred in levels:
            cands = [d for d in pool if pred(d)]
            if not cands:
                continue
            start = rng.randrange(len(cands))
            for d in itertools.chain(cands[start:], cands[:start]):
                text = _remap_ids(d["text"], d["agent"], str(e.get("agent", "")),
                                  shared, spare)
                text = _remap_labels(text, d.get("labels"), target, flip)
                if text and text not in originals:
                    chosen = (level_name, d, text)
                    break
            if chosen:
                break
        if chosen is None:  # cannot happen with 30 non-empty snapshots; be explicit
            raise RuntimeError(f"no donor for {state['state_id']} slot {i}")
        level_name, donor, text = chosen
        new = dict(e)
        new["text"] = text
        out.append(new)
        prov.append({
            "slot": i, "stratum": stratum, "band": band, "match_level": level_name,
            "donor_state": donor["state_id"], "donor_slot": donor["slot"],
            "donor_sandbox": donor["sandbox"], "label_flip": flip,
            "label_remap": ("donor->slot" if (donor.get("labels") and target)
                            else "skipped"),
            "slot_labels": target, "donor_labels": donor.get("labels"),
            "orig_chars": len(original), "new_chars": len(text),
            "new_band": length_band(text),
        })
    snapshot = {
        "entries": out,
        "total": int(state["board"].get("total", len(out)) or len(out)),
        "shown": int(state["board"].get("shown", len(out)) or len(out)),
    }
    return snapshot, prov


def freeze_randomised(states: list[dict], *, seed: int = TRANSFORM_SEED) -> None:
    """Attach `board_randomised` and `randomisation` to every state, in place."""
    pool = donor_pool(states)
    universe = _id_universe(states)
    for s in states:
        snap, prov = randomise_snapshot(s, pool, universe, seed=seed)
        s["board_randomised"] = snap
        s["randomisation"] = {"seed": seed, "slots": prov}


# ---------------------------------------------------------------------------
# 4. replay
# ---------------------------------------------------------------------------

def board_for(state: dict, arm: str) -> dict:
    if arm == "real":
        return state["board"]
    if arm == "randomised":
        board = state.get("board_randomised")
        if not board:
            raise SystemExit(f"{state['state_id']}: randomised board not frozen; "
                             "run `delivery_replay.py freeze` first")
        return board
    raise ValueError(f"unknown arm {arm!r}")


def replay_one(state: dict, arm: str, replicate: int, client: Any) -> dict:
    messages, tools, psha, tsha = cr.rebuild(state)
    sent, mapping = resolve_effort(MODEL, SENT_AS)
    bookkeeping: dict[str, Any] = {"order": [], "posts": [], "board_size_at_read": None}
    # the handler is calibration_replay's -- it writes nowhere -- served a board per arm
    handler = cr.make_frozen_handler(dict(state, board=board_for(state, arm)), bookkeeping)
    seed = cr.call_seed(state, replicate)      # matched across arms by construction
    result = client.chat(
        messages, tools=tools, tool_handler=handler, temperature=TEMPERATURE,
        max_tokens=ANSWER_TOKENS + REASONING_BUDGET, effort=sent, seed=seed,
        max_tool_iterations=MAX_TOOL_ITERATIONS,
    )
    parsed = None if result.error else parse_action(
        result.raw, labels=inverse_labels(state["label_map"]))
    order = bookkeeping["order"]
    reported = sum(u.get("estimated_cost") or 0.0 for u in result.usage)
    return {
        "state_id": state["state_id"],
        "state_index": state.get("index", -1),
        "sandbox": state["sandbox"],
        "game": state["game"],
        "round": state["round"],
        "agent": state["agent"],
        "deficit_arm": state.get("arm", ""),
        "round_bin": state.get("round_bin", ""),
        "post_stratum": state.get("post_stratum", ""),
        "pair_type": state["pair_type"],
        "arm": arm,
        "replicate": replicate + 1,
        "sent_effort": sent,
        "binary_collapsed": bool(mapping.get("collapsed")),
        "seed": seed,
        "prompt_sha256": psha,
        "tools_sha256": tsha,
        "hash_matches_log": psha == state["logged_prompt_sha256"],
        "board_entries_served": len(board_for(state, arm).get("entries") or []),
        "read_happened": sum(1 for n in order if n == "notes_read") > 0,
        "action": (parsed.action if parsed else None) or "",
        "parse_ok": bool(parsed and parsed.action),
        "fallback_flag": (parsed.fallback_flag if parsed else "provider_error") or "",
        "logged_action": state.get("logged_action", ""),
        "board_calls": sum(1 for n in order if n in ("notes_read", "notes_post")),
        "read_calls": sum(1 for n in order if n == "notes_read"),
        "post_calls": sum(1 for n in order if n == "notes_post"),
        "decoy_calls": sum(1 for n in order if n in DECOY_SCHEMAS),
        "tool_call_names": "|".join(order),
        "post_texts": " || ".join(bookkeeping["posts"]),
        "reasoning_tokens": result.reasoning_tokens,
        "completion_tokens": result.completion_tokens,
        "prompt_tokens": result.prompt_tokens,
        "finish_reason": result.finish_reason or "",
        "latency_ms": result.latency_ms,
        "iterations": result.iterations,
        "forced_answer": bool(result.forced_answer),
        "estimated_cost": round(
            reported or cr.estimate_cost(result.prompt_tokens, result.completion_tokens), 8),
        "cost_source": "provider" if reported else "price_card",
        "error": result.error or "",
    }


CSV_FIELDS = [
    "state_id", "state_index", "sandbox", "game", "round", "agent", "deficit_arm",
    "round_bin", "post_stratum", "pair_type", "arm", "replicate", "sent_effort",
    "binary_collapsed", "seed", "prompt_sha256", "tools_sha256", "hash_matches_log",
    "board_entries_served", "read_happened", "action", "parse_ok", "fallback_flag",
    "logged_action", "board_calls", "read_calls", "post_calls", "decoy_calls",
    "tool_call_names", "post_texts", "reasoning_tokens", "completion_tokens",
    "prompt_tokens", "finish_reason", "latency_ms", "iterations", "forced_answer",
    "estimated_cost", "cost_source", "error",
]


def build_jobs(states: list[dict]) -> list[tuple[dict, str, int]]:
    return [(s, arm, rep) for s in states for arm in ARMS for rep in range(REPLICATES)]


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
    print(f"{len(jobs)} calls over {len(states)} states x {len(ARMS)} arms, "
          f"concurrency {concurrency}", file=sys.stderr)
    rows: list[dict] = [None] * len(jobs)  # type: ignore[list-item]
    done = {"n": 0}
    t0 = time.perf_counter()

    def work(i_job):
        i, (state, arm, rep) = i_job
        try:
            row = replay_one(state, arm, rep, client)
        except Exception as e:      # a dead call is a logged row, never a dead run
            row = {f: "" for f in CSV_FIELDS}
            row.update({"state_id": state["state_id"],
                        "state_index": state.get("index", -1),
                        "sandbox": state["sandbox"], "game": state["game"],
                        "round": state["round"], "agent": state["agent"],
                        "deficit_arm": state.get("arm", ""),
                        "round_bin": state.get("round_bin", ""),
                        "post_stratum": state.get("post_stratum", ""),
                        "pair_type": state["pair_type"], "arm": arm,
                        "replicate": rep + 1, "parse_ok": False,
                        "read_happened": False,
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
# 5. summary
# ---------------------------------------------------------------------------

def as_bool(v: Any) -> bool:
    return v is True or str(v).strip().lower() in ("true", "1", "yes")


def summarise_arm(rows: list[dict]) -> dict[str, Any]:
    """Per-arm block. Safe on an arm with no calls and on an arm with zero reads."""
    n = len(rows)
    if n == 0:
        return {"n": 0, "read_rate": None, "cooperate_rate": None, "post_rate": None,
                "parse_fail_rate": None, "n_delivered": 0, "decoy_rate": None,
                "cost": 0.0, "errors": 0, "completion_median": None,
                "latency_median": None}
    read = [r for r in rows if as_bool(r["read_happened"])]
    # cooperation is only defined where the message was actually delivered
    parsed = [r for r in read if as_bool(r["parse_ok"])]
    return {
        "n": n,
        "n_delivered": len(read),
        "read_rate": len(read) / n,
        "cooperate_rate": (sum(1 for r in parsed if r["action"] == "C") / len(parsed)
                           if parsed else None),
        "post_rate": sum(1 for r in rows if int(r["post_calls"] or 0) > 0) / n,
        "decoy_rate": sum(1 for r in rows if int(r["decoy_calls"] or 0) > 0) / n,
        "parse_fail_rate": (1 - len(parsed) / len(read)) if read else None,
        "completion_median": cr.quartiles([int(r["completion_tokens"] or 0)
                                           for r in rows])[1],
        "latency_median": cr.quartiles([int(r["latency_ms"] or 0) for r in rows])[1],
        "cost": sum(float(r["estimated_cost"] or 0) for r in rows),
        "errors": sum(1 for r in rows if r["error"]),
    }


def state_rates(rows: list[dict]) -> dict[str, dict[str, float | None]]:
    """state_id -> arm -> P(cooperate) over the replicates that read and parsed."""
    per: dict[str, dict[str, list[int]]] = {}
    for r in rows:
        if not as_bool(r["read_happened"]) or not as_bool(r["parse_ok"]):
            continue
        per.setdefault(r["state_id"], {}).setdefault(r["arm"], []).append(
            1 if r["action"] == "C" else 0)
    return {sid: {arm: (sum(v) / len(v) if v else None) for arm, v in arms.items()}
            for sid, arms in per.items()}


def paired_diffs(rows: list[dict]) -> tuple[list[float], list[str], list[str]]:
    """Within-state P(C|real) - P(C|randomised). Only states where BOTH arms read."""
    rates = state_rates(rows)
    diffs, used, unpaired = [], [], []
    for sid in sorted(rates):
        a, b = rates[sid].get("real"), rates[sid].get("randomised")
        if a is None or b is None:
            unpaired.append(sid)
            continue
        diffs.append(a - b)
        used.append(sid)
    return diffs, used, unpaired


def exact_sign_flip(diffs: list[float]) -> dict:
    """Exact two-sided sign-flip p on the paired state differences.

    `analysis.stats.sign_flip_test` enumerates all 2^k patterns for k <= 20 and samples
    above that. A zero difference is invariant under a sign flip, so when at most 20 of
    the k differences are non-zero the enumeration over those alone is still EXACT;
    this wrapper does that enumeration and hands everything else to stats.
    """
    d = [float(x) for x in diffs]
    k = len(d)
    if k == 0 or k <= 20:
        return sign_flip_test(d)
    nz = [x for x in d if x != 0.0]
    if len(nz) > 20:
        return sign_flip_test(d)
    obs = abs(sum(d) / k)
    total = 2 ** len(nz)
    count = 0
    for mask in range(total):
        acc = 0.0
        for i, x in enumerate(nz):
            acc += x if (mask >> i) & 1 else -x
        if abs(acc / k) >= obs - 1e-12:
            count += 1
    base = sign_flip_test(d)
    base.update({"p": count / total, "exact": True,
                 "exact_over_nonzero": len(nz), "n_perm": None})
    return base


def fmt(v: Any, nd: int = 0) -> str:
    if v is None:
        return "--"
    if isinstance(v, float):
        return f"{v:.{nd}f}"
    return str(v)


def pct(v: Any) -> str:
    return "--" if v is None else f"{100 * float(v):.1f}%"


def _diff_block(rows: list[dict], label: str) -> list[str]:
    diffs, used, unpaired = paired_diffs(rows)
    if not diffs:
        return [f"| {label} | 0 | -- | -- | -- | -- |"]
    res = exact_sign_flip(diffs)
    lo, hi = block_bootstrap_ci(diffs, seed=TRANSFORM_SEED)
    kind = "exact" if res.get("exact") else f"sampled ({res.get('n_perm')})"
    return [f"| {label} | {len(diffs)} | {res['mean']:+.4f} | "
            f"[{lo:+.4f}, {hi:+.4f}] | {res['p']:.4f} ({kind}) | "
            f"+{res['n_positive']} / -{res['n_negative']} / "
            f"={len(diffs) - res['n_positive'] - res['n_negative']} |"]


def write_summary(states: list[dict], rows: list[dict], out_dir: Path,
                  *, drops: list[dict] | None = None) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    per_arm = {arm: summarise_arm([r for r in rows if r["arm"] == arm]) for arm in ARMS}
    matched = sum(1 for r in rows if as_bool(r["hash_matches_log"]))
    hash_states = sum(1 for s in states if cr.verify_state(s)[0])
    total_cost = sum(v["cost"] for v in per_arm.values())
    diffs, used, unpaired = paired_diffs(rows)

    # consistency: replayed real arm vs the action the runner logged at the time
    real_rows = [r for r in rows if r["arm"] == "real"
                 and as_bool(r["parse_ok"]) and r["logged_action"]]
    agree = sum(1 for r in real_rows if r["action"] == r["logged_action"])

    L: list[str] = []
    L.append("# Delivery replay — does message CONTENT change the receiver?")
    L.append("")
    L.append(f"Model `{MODEL}` on {PROFILE} (fp8), condition `permitted`, "
             f"reasoning effort held at **{EFFORT_LEVEL}**, {ANSWER_TOKENS} answer "
             "tokens, one decision per call, no population, no board writes.")
    L.append(f"Contract: `{SPEC_PATH}`. States: `{STATES_PATH}`. Calls: `calls.csv`. "
             "Per-state transform provenance: `states-manifest.md`.")
    L.append("")
    L.append("Each of the 30 recipient states is replayed twice per arm on a "
             "byte-identical prompt with a matched sample seed. The board is not in "
             "the prompt: it arrives as the result of the model's own `notes_read` "
             "call, so the arms differ in exactly one thing — what that call returns.")
    L.append("")
    L.append("## Prompt identity")
    L.append("")
    L.append(f"- States frozen: **{len(states)}** "
             f"({sum(1 for s in states if s['arm'] == 'ahead')} ahead, "
             f"{sum(1 for s in states if s['arm'] == 'behind')} behind), every one of "
             "them a scored decision whose final attempt called `notes_read` and got "
             "at least one board entry back.")
    L.append(f"- States whose rebuilt `prompt_sha256` equals the logged one: "
             f"**{hash_states}/{len(states)}**.")
    L.append(f"- Calls sent on a hash-matched prompt: **{matched}/{len(rows)}**.")
    if drops:
        L.append(f"- Candidates dropped during sampling: {len(drops)} "
                 f"({'; '.join(sorted({d['reason'] for d in drops}))}).")
    else:
        L.append("- Candidates dropped during sampling: 0.")
    L.append("")
    L.append("## Per arm")
    L.append("")
    L.append("| arm | n calls | read rate | n delivered | cooperate rate | post rate | "
             "decoy rate | parse-fail rate | completion med | latency med (ms) | "
             "errors |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for arm in ARMS:
        s = per_arm[arm]
        L.append(f"| {arm} | {s['n']} | {pct(s['read_rate'])} | {s['n_delivered']} | "
                 f"{pct(s['cooperate_rate'])} | {pct(s['post_rate'])} | "
                 f"{pct(s['decoy_rate'])} | {pct(s['parse_fail_rate'])} | "
                 f"{fmt(s['completion_median'])} | {fmt(s['latency_median'])} | "
                 f"{s['errors']} |")
    L.append("")
    nr = {arm: per_arm[arm]["n"] - per_arm[arm]["n_delivered"] for arm in ARMS}
    L.append(f"No-delivery replays: {nr['real']} in `real`, {nr['randomised']} in "
             "`randomised`. A state contributes to the endpoint only if BOTH arms "
             "delivered at least once.")
    L.append("")
    L.append("`read rate` is the share of replays in which the model called "
             "`notes_read` at all: a replay that never reads is a **no delivery** for "
             "that arm and contributes no cooperation observation. `cooperate rate` "
             "and `parse-fail rate` are computed over delivered replays only.")
    L.append("")
    L.append("## Primary endpoint — paired within recipient state")
    L.append("")
    L.append(f"Paired on the **{len(diffs)}** states where BOTH arms read at least "
             f"once; {len(unpaired)} state(s) unpaired "
             f"({', '.join(f'`{s}`' for s in unpaired) if unpaired else 'none'}).")
    L.append("")
    L.append(r"| slice | k states | mean P(C\|real) − P(C\|rand) | "
             "95% block bootstrap | sign-flip p | +/−/0 |")
    L.append("|---|---|---|---|---|---|")
    L.extend(_diff_block(rows, "**all states**"))
    for stratum in STRATA:
        L.extend(_diff_block([r for r in rows if r["post_stratum"] == stratum], stratum))
    for deficit in ("ahead", "behind"):
        L.extend(_diff_block([r for r in rows if r["deficit_arm"] == deficit],
                             f"deficit: {deficit}"))
    L.append("")
    if diffs:
        res = exact_sign_flip(diffs)
        nz = res["n_positive"] + res["n_negative"]
        if res.get("exact"):
            floor = 2.0 ** -(nz - 1) if nz >= 1 else 1.0
            L.append(
                f"A difference of exactly zero is invariant under a sign flip, so the "
                f"enumeration runs over the {nz} non-zero differences of the {res['k']} "
                "paired states and the p value is exact. The smallest two-sided p "
                f"those {nz} non-zero states could have produced is "
                f"{min(1.0, floor):.4f}: with this many states that actually moved, the "
                "test could not have returned a small p whatever the signs had been, so "
                "a large p here is weak evidence of no effect, not strong evidence.")
        else:
            L.append(f"Sign-flip p is sampled over {res.get('n_perm')} draws "
                     f"(k = {res['k']} states).")
        L.append("")
    post_diffs = []
    for sid in sorted({r["state_id"] for r in rows}):
        got = {}
        for arm in ARMS:
            rs = [r for r in rows if r["state_id"] == sid and r["arm"] == arm
                  and not r["error"]]
            if rs:
                got[arm] = sum(1 for r in rs if int(r["post_calls"] or 0) > 0) / len(rs)
        if len(got) == len(ARMS):
            post_diffs.append(got["real"] - got["randomised"])
    if post_diffs:
        pres = exact_sign_flip(post_diffs)
        plo, phi = block_bootstrap_ci(post_diffs, seed=TRANSFORM_SEED)
        L.append("### Secondary, not pre-registered: did the arms differ in POSTING?")
        L.append("")
        L.append(f"Paired within state, P(the replay wrote a post | real) − "
                 f"P(post | randomised) = **{pres['mean']:+.4f}** "
                 f"(95% block bootstrap [{plo:+.4f}, {phi:+.4f}], sign-flip "
                 f"p = {pres['p']:.4f}, k = {pres['k']}). The spec's endpoint is the "
                 "next ACTION, not the next post; this line is reported because it is "
                 "the one place the two boards visibly pulled apart, and it is "
                 "exploratory — it was not declared before the calls and carries no "
                 "multiplicity correction.")
        L.append("")
    L.append("## Consistency check — replayed `real` arm vs the logged action")
    L.append("")
    if real_rows:
        L.append(f"The `real` arm replays the exposure the runner already served. "
                 f"It reproduced the action logged at the time in "
                 f"**{agree}/{len(real_rows)}** parsed replays "
                 f"({pct(agree / len(real_rows))}). This is a sanity bound, not a "
                 "target: temperature is 0.7 and the seed is re-derived, so perfect "
                 "agreement was never expected; a rate near chance would mean the "
                 "replay is not reproducing the original exposure.")
    else:
        L.append("No parsed `real`-arm replay carried a logged action to compare.")
    L.append("")
    L.append("## Cost")
    L.append("")
    L.append(f"{len(rows)} calls, **${total_cost:.4f}** at ${PRICE_IN_PER_M}/M in and "
             f"${PRICE_OUT_PER_M}/M out.")
    L.append("")
    L.append("## What this establishes, and what it does not")
    L.append("")
    L.append(
        "It establishes whether the CONTENT of the board messages a recipient read "
        "changes what that recipient does next, on this model, at this effort setting, "
        "in the permitted condition. The comparison is tight: the same 30 recipients, "
        "the same byte-identical prompts verified against the `prompt_sha256` the "
        "runner logged when each decision was actually played, the same sample seeds, "
        "the same number of board entries, the same posting identities, the same "
        "timestamps, the same length bands and the same post-type per slot — with only "
        "the game-relevant text swapped for another state's and its directive mapping "
        "shuffled. A difference here is evidence that a post was received as "
        "information; the absence of one is evidence that the recipient's next move was "
        "already determined by the rest of its prompt, which is an expected possible "
        "outcome of this control and not a failure of it. What it does not establish: "
        "anything about the SENDER. It cannot say whether a post was written in order "
        "to influence anyone, because it never varies the sender or the sender's "
        "incentives — only what the receiver is shown. It also cannot generalise past a "
        "single next decision: these are one-shot replays out of context, no opponent "
        "answers back, no board is written, no score accumulates, and a repeated or "
        "compounding effect over a whole game would not show up here. Finally the "
        "randomised arm is a randomisation of content, not of plausibility: the "
        "transform keeps the board well-formed on purpose, so a null says content did "
        "not move the action, not that the model failed to notice the board.")
    L.append("")
    (out_dir / "SUMMARY.md").write_text("\n".join(L) + "\n")

    # --- manifest ---------------------------------------------------------
    M = ["# Delivery states — 30 frozen recipient decisions", "",
         f"Sampled with RNG seed {SAMPLE_SEED} from the four permitted / effort-off "
         "sandboxes of runs/v3, stratified 15 ahead / 15 behind, and within an arm by "
         "post type of the messages the recipient saw (5 per stratum) and spread over "
         "round bins (early ≤10, mid 11–20, late ≥21).", "",
         "A snapshot's post type is the highest-priority category present in it, from "
         "`analysis.coding.code_post`: `directive` → directive_post; `opponent_info` "
         "and `identity` → useful_looking_post; `other` → irrelevant_post.", "",
         "| # | state id | deficit | post type | bin | pair | round | opponent | "
         "labels | entries | logged action |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for s in states:
        lm = s["label_map"]
        M.append(
            f"| {s['index']} | `{s['state_id']}` | {s['arm']} | {s['post_stratum']} | "
            f"{s['round_bin']} | {s['pair_type']} | {s['round']} | {s['opponent']} | "
            f"C={lm['C']} D={lm['D']} | {s['board'].get('shown', 0)} | "
            f"{s['logged_action']} |")
    M.append("")
    M.append("## The randomisation transform, per state")
    M.append("")
    M.append(f"RNG seed {TRANSFORM_SEED}, frozen into `{STATES_PATH}` before the first "
             "provider call. `label flip` is the per-state coin that decides whether "
             "the donor game's cooperate-label maps onto the recipient's cooperate- or "
             "defect-label. `match level` counts the slots by how far the donor search "
             "had to relax: `stratum+band+sandbox` is the intended draw.")
    M.append("")
    M.append("| state id | slots | label flip | donor states | match levels | "
             "median abs Δ chars | band preserved | labels remapped |")
    M.append("|---|---|---|---|---|---|---|---|")
    for s in states:
        prov = (s.get("randomisation") or {}).get("slots") or []
        if not prov:
            M.append(f"| `{s['state_id']}` | -- | -- | -- | -- | -- | -- | -- |")
            continue
        levels: dict[str, int] = {}
        for p in prov:
            levels[p["match_level"]] = levels.get(p["match_level"], 0) + 1
        deltas = sorted(abs(p["new_chars"] - p["orig_chars"]) for p in prov)
        kept = sum(1 for p in prov if p["new_band"] == p["band"])
        M.append(
            f"| `{s['state_id']}` | {len(prov)} | {prov[0]['label_flip']} | "
            f"{len({p['donor_state'] for p in prov})} | "
            f"{', '.join(f'{k}={v}' for k, v in sorted(levels.items()))} | "
            f"{deltas[len(deltas) // 2]} | {kept}/{len(prov)} | "
            f"{sum(1 for p in prov if p.get('label_remap') == 'donor->slot')}"
            f"/{len(prov)} |")
    M.append("")
    M.append("Every state carries the warm-up block, the executed history of the "
             "earlier scored rounds, the running totals, the drawn label pair, the "
             "round's option order, the exact board snapshot the model was shown, the "
             "randomised snapshot and the recipient's logged action, so both arms are "
             "rebuilt rather than re-derived.")
    (out_dir / "states-manifest.md").write_text("\n".join(M) + "\n")
    print(f"wrote {out_dir / 'SUMMARY.md'} and {out_dir / 'states-manifest.md'}",
          file=sys.stderr)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def load_states(path: Path) -> tuple[list[dict], list[dict]]:
    payload = json.loads(path.read_text())
    return payload["states"], payload.get("drops", [])


def _write_states(path: Path, states: list[dict], drops: list[dict], seed: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({
        "spec": SPEC_PATH,
        "generated_by": "delivery_replay.py",
        "rng_seed": seed,
        "transform_seed": TRANSFORM_SEED,
        "sources": [{"arm": a, "path": p} for a, p in SOURCES],
        "stratification": {
            "per_arm": N_PER_ARM,
            "strata": list(STRATA),
            "category_to_stratum": STRATUM_OF_CATEGORY,
            "quota": {f"{s}/{b}": q for (s, b), q in QUOTA.items()},
            "pool_extra": POOL_EXTRA,
            "round_bins": {"early": "<=10", "mid": "11-20", "late": ">=21"},
            "length_bands": {name: [lo, hi] for lo, hi, name in LENGTH_BANDS},
        },
        "count": len(states),
        "drops": drops,
        "states": states,
    }, indent=2) + "\n")


def do_sample(args) -> tuple[list[dict], list[dict]]:
    sources = [load_source(arm, ROOT / p) for arm, p in SOURCES]
    states, drops = sample_states(sources, seed=args.seed)
    freeze_randomised(states)
    _write_states(ROOT / args.states, states, drops, args.seed)
    print(f"wrote {ROOT / args.states}: {len(states)} states, {len(drops)} drops",
          file=sys.stderr)
    return states, drops


def do_freeze(args) -> None:
    path = ROOT / args.states
    states, drops = load_states(path)
    freeze_randomised(states)
    _write_states(path, states, drops, args.seed)
    print(f"froze randomised boards for {len(states)} states", file=sys.stderr)


def do_verify(args) -> None:
    states, _ = load_states(ROOT / args.states)
    ok = 0
    for s in states:
        good, why = cr.verify_state(s)
        ok += good
        if not good:
            print(f"MISMATCH {s['state_id']}: {why}")
    print(f"{ok}/{len(states)} states rebuild to the logged prompt_sha256")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("command",
                   choices=["sample", "verify", "freeze", "replay", "report", "all"])
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
    if args.command == "freeze":
        do_freeze(args)
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
