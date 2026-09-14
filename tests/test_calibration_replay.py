"""Tests for the calibration gate (`calibration_replay.py`).

Four properties, one per thing that could silently invalidate the gate:
  * the sampler is deterministic in its seed (the 30 states are reproducible);
  * the prompt rebuild reproduces the `prompt_sha256` the runner logged on a REAL
    decision row (so a replayed call is provably the same exposure);
  * the replay tool handler writes nowhere (no board, no file, no run directory);
  * the summary maths survives a level with no calls in it.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import calibration_replay as cr  # noqa: E402

FIXTURE = Path(__file__).parent / "fixtures" / "calibration_move_rows.json"


# ---------------------------------------------------------------------------
# the sampler
# ---------------------------------------------------------------------------

def _synthetic_source(arm: str, path: str, *, games: int = 12) -> cr.SourceIndex:
    """A miniature moves.jsonl index: 2 agents x N games x 24 scored rounds."""
    index: dict[int, list[dict]] = {}
    for g in range(1, games + 1):
        rows: list[dict] = []
        opponent_is_llm = g % 2 == 0
        for agent, opp in (("A01", "A02"), ("A02", "A01")):
            if agent == "A02" and not opponent_is_llm:
                continue
            for rnd in range(1, 7):
                rows.append({
                    "kind": "move", "phase": "warmup", "status": "ok",
                    "provider": "assigned", "game": g, "round": rnd, "agent": agent,
                    "action": "C", "executed": "C", "opponent_action": "C",
                    "model": "m", "prompt_sha256": "", "sandbox": path,
                })
            for rnd in range(1, 25):
                rows.append({
                    "kind": "move", "phase": "scored", "status": "ok",
                    "provider": "deepinfra", "sandbox": path, "seed": 1,
                    "generation": 0, "game": g, "round": rnd, "agent": agent,
                    "model": "deepseek", "opponent": opp,
                    "opponent_model": "deepseek" if opponent_is_llm else "script:TitForTat",
                    "pair_type": "llm-llm" if opponent_is_llm else "llm-script",
                    "condition": "forbidden", "framing": "F0", "paraphrase": "p1",
                    "label_map": {"C": "J", "D": "F"}, "option_order": ["J", "F"],
                    "action": "C", "executed": "C", "opponent_action": "C",
                    "prompt_sha256": f"sha-{path}-{g}-{rnd}-{agent}",
                    "tools_sha256": "tools", "warmup_rounds": 6,
                    "score_gap_at_call": 0,
                    "board": {"entries": [], "total": 0, "shown": 0},
                })
            if not opponent_is_llm:
                for rnd in range(1, 25):
                    rows.append({
                        "kind": "move", "phase": "scored", "status": "ok",
                        "provider": "script", "game": g, "round": rnd, "agent": opp,
                        "model": "script:TitForTat", "executed": "C", "action": "C",
                        "prompt_sha256": "", "sandbox": path,
                    })
        index[g] = rows
    return cr.SourceIndex(arm=arm, path=path, games=index)


def _sources():
    return [
        _synthetic_source("ahead", "src/B1-ahead"),
        _synthetic_source("behind", "src/B1-behind"),
        _synthetic_source("ahead", "src/B2-ahead"),
        _synthetic_source("behind", "src/B2-behind"),
    ]


def test_sampler_is_deterministic_in_its_seed():
    a, _ = cr.sample_states(_sources(), seed=9001, verify=False)
    b, _ = cr.sample_states(_sources(), seed=9001, verify=False)
    assert [s["state_id"] for s in a] == [s["state_id"] for s in b]
    c, _ = cr.sample_states(_sources(), seed=9002, verify=False)
    assert [s["state_id"] for s in c] != [s["state_id"] for s in a]


def test_sampler_hits_the_declared_stratification():
    states, drops = cr.sample_states(_sources(), seed=9001, verify=False)
    assert len(states) == 30 and not drops
    assert sum(1 for s in states if s["arm"] == "ahead") == 15
    assert sum(1 for s in states if s["arm"] == "behind") == 15
    for arm in ("ahead", "behind"):
        for rbin, ptype in cr.CELLS:
            got = sum(1 for s in states if s["arm"] == arm
                      and s["round_bin"] == rbin and s["pair_type"] == ptype)
            assert got >= 2, (arm, rbin, ptype, got)
    # ids are unique, so no state is replayed twice under two labels
    assert len({s["state_id"] for s in states}) == 30


def test_quota_spreads_evenly():
    assert cr.quota_for_arm(15, 6) == [3, 3, 3, 2, 2, 2]
    assert sum(cr.quota_for_arm(15, 6)) == 15


# ---------------------------------------------------------------------------
# the rebuild
# ---------------------------------------------------------------------------

def test_rebuild_reproduces_the_logged_hash_on_a_real_row():
    """The load-bearing check: a real logged decision, rebuilt byte for byte."""
    fx = json.loads(FIXTURE.read_text())
    state = cr.freeze_state(fx["row"], fx["game_rows"])
    _, _, prompt_sha, tools_sha = cr.rebuild(state)
    assert tools_sha == fx["row"]["tools_sha256"]
    assert prompt_sha == fx["row"]["prompt_sha256"]
    assert cr.verify_state(state) == (True, "ok")


def test_rebuild_uses_the_warmup_offset_and_the_carried_ledger():
    fx = json.loads(FIXTURE.read_text())
    state = cr.freeze_state(fx["row"], fx["game_rows"])
    messages, tools, _, _ = cr.rebuild(state)
    assert len(state["warmup"]) == state["warmup_rounds"] == 6
    assert len(state["history"]) == state["round"] - 1
    # the ledger carried in from the warm-up is in the totals the model is shown
    assert state["totals"]["rounds"] == len(state["warmup"]) + len(state["history"])
    # `score_gap_at_call` reaches moves.jsonl as a STRING: it is a numpy scalar and
    # RunLogger serialises with `default=str`. Compare as an int.
    assert state["totals"]["score"] - state["totals"]["opp_score"] == \
        int(state["logged_score_gap"])
    assert {t["function"]["name"] for t in tools} == {
        "notes_read", "notes_post", "workspace_clock"}
    assert messages[0]["role"] == "system" and messages[1]["role"] == "user"


def test_a_tampered_state_is_caught_not_replayed():
    fx = json.loads(FIXTURE.read_text())
    state = cr.freeze_state(fx["row"], fx["game_rows"])
    state["history"] = state["history"][:-1] if state["history"] else [["C", "C"]]
    state["totals"] = cr.totals_for(state)
    ok, why = cr.verify_state(state)
    assert not ok and "prompt_sha256" in why


def test_frozen_states_file_matches_its_log(tmp_path):
    """The committed 30 states still rebuild to their logged hashes."""
    path = ROOT / cr.STATES_PATH
    if not path.exists():
        pytest.skip("states not sampled yet")
    states, _ = cr.load_states(path)
    assert len(states) == 30
    bad = [s["state_id"] for s in states if not cr.verify_state(s)[0]]
    assert not bad, bad


# ---------------------------------------------------------------------------
# the tool handler
# ---------------------------------------------------------------------------

def _state_with_board():
    return {
        "totals": {"score": 40, "opp_score": 30, "rounds": 10, "self_c": 8, "opp_c": 7},
        "board": {"entries": [{"agent": "A01", "text": "hello", "ts": "t"}],
                  "total": 1, "shown": 1},
    }


def test_handler_never_writes_anywhere(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    book = {"order": [], "posts": [], "board_size_at_read": None}
    handler = cr.make_frozen_handler(_state_with_board(), book)

    before = handler("notes_read", {})
    posted = handler("notes_post", {"text": "x" * 500})
    after = handler("notes_read", {})

    assert posted == {"ok": True, "posted": "x" * 400}     # echoed, truncated as usual
    assert after == before                                  # and NOT on the board
    assert after["total"] == 1 and len(after["entries"]) == 1
    assert book["posts"] == ["x" * 400]
    assert book["order"] == ["notes_read", "notes_post", "notes_read"]
    # nothing was created on disk, anywhere
    assert list(tmp_path.iterdir()) == []


def test_handler_serves_the_decoy_from_the_frozen_ledger():
    book = {"order": [], "posts": [], "board_size_at_read": None}
    handler = cr.make_frozen_handler(_state_with_board(), book)
    assert handler("workspace_clock", {}) == {
        "cumulative_score": 40, "sessions_completed": 10}
    with pytest.raises(ValueError):
        handler("rm_rf", {})


def test_empty_board_state_reads_empty():
    book = {"order": [], "posts": [], "board_size_at_read": None}
    handler = cr.make_frozen_handler({"totals": {"score": 0, "rounds": 0}, "board": {}}, book)
    assert handler("notes_read", {}) == {"entries": [], "total": 0, "shown": 0}


def test_call_seed_matches_the_runner_formula():
    from coop.players.llm import stable_seed
    state = {"sandbox": "B1", "seed": 109, "generation": 0, "game": 7,
             "agent": "A03", "round": 5}
    assert cr.call_seed(state, 0) == stable_seed(
        "B1", 109, 0, 7, "A03", 5, "sample") % (2 ** 31)
    assert cr.call_seed(state, 1) != cr.call_seed(state, 0)


# ---------------------------------------------------------------------------
# the summary
# ---------------------------------------------------------------------------

def _call_row(level, reasoning, **kw):
    row = {
        "state_id": kw.get("state_id", "s1"), "level": level,
        "reasoning_tokens": reasoning, "completion_tokens": reasoning + 20,
        "prompt_tokens": 900, "latency_ms": 1000, "finish_reason": "stop",
        "action": "C", "parse_ok": True, "board_calls": 0, "decoy_calls": 0,
        "estimated_cost": 0.0001, "error": "",
    }
    row.update(kw)
    return row


def test_summarise_level_handles_an_empty_level():
    s = cr.summarise_level([])
    assert s["n"] == 0
    assert s["reasoning_median"] is None and s["cooperate_rate"] is None
    assert s["finish_reasons"] == {} and s["cost"] == 0.0
    # and formatting an empty level does not blow up
    assert cr.fmt(s["reasoning_median"]) == "--" and cr.pct(s["cooperate_rate"]) == "--"


def test_separation_reports_no_data_for_an_empty_level():
    filled = cr.summarise_level([_call_row("high", 500)])
    assert cr.separation(filled, cr.summarise_level([]))["verdict"] == "no data"
    assert cr.separation(cr.summarise_level([]), cr.summarise_level([]))[
        "overlap"] is None


def test_separation_detects_overlap_and_its_absence():
    low = cr.summarise_level([_call_row("low", v) for v in (10, 20, 30, 40)])
    high = cr.summarise_level([_call_row("high", v) for v in (900, 950, 1000, 1100)])
    near = cr.summarise_level([_call_row("high", v) for v in (25, 35, 45, 55)])
    assert cr.separation(low, high)["overlap"] is False
    assert cr.separation(low, near)["overlap"] is True


def test_quartiles_on_edge_cases():
    assert cr.quartiles([5]) == (5.0, 5.0, 5.0)
    q1, med, q3 = cr.quartiles([1, 2, 3, 4])
    assert (q1, med, q3) == (1.75, 2.5, 3.25)
    assert all(v != v for v in cr.quartiles([]))   # NaN


def test_all_parse_failures_do_not_divide_by_zero():
    rows = [_call_row("none", 0, parse_ok=False, action="")]
    s = cr.summarise_level(rows)
    assert s["cooperate_rate"] is None and s["parse_fail_rate"] == 1.0


def test_paired_board_table_counts_states_not_calls():
    rows = [
        _call_row("none", 0, state_id="a", board_calls=1),
        _call_row("none", 0, state_id="a", board_calls=0),   # 2nd replicate
        _call_row("high", 500, state_id="a", board_calls=0),
        _call_row("none", 0, state_id="b", board_calls=0),
        _call_row("high", 500, state_id="b", board_calls=2),
        _call_row("none", 0, state_id="c", board_calls=0),
        _call_row("high", 500, state_id="c", board_calls=0),
    ]
    t = cr.paired_board_table(rows, "none", "high")
    assert t == {"both": 0, "none_only": 1, "high_only": 1, "neither": 1, "states": 3}


def test_write_summary_survives_zero_calls(tmp_path):
    states, _ = cr.sample_states(_sources(), seed=9001, verify=False)
    for s in states:
        s["logged_prompt_sha256"] = "x"      # verify_state will say False, not raise
    cr.write_summary(states, [], tmp_path, drops=[])
    text = (tmp_path / "SUMMARY.md").read_text()
    assert "Calibration gate" in text and "0/0" in text
    assert (tmp_path / "states-manifest.md").read_text().count("| ") > 30
