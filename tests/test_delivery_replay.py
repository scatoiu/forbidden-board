"""Tests for the delivery replay control (`delivery_replay.py`).

Six properties, one per thing that could silently invalidate the control:
  * the sampler is deterministic in its seed and hits the declared stratification;
  * the randomisation transform is deterministic, preserves format, length band and
    post type, and never leaves an entry's original content in place;
  * no randomised entry refers to the recipient or its opponent;
  * the tool handler writes nowhere, and serves a different board per arm;
  * the prompt rebuild reproduces the `prompt_sha256` the runner logged on a REAL
    permitted/effort-off decision row that actually read the board;
  * the summary maths survives an arm in which nothing was ever delivered.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import calibration_replay as cr  # noqa: E402
import delivery_replay as dr  # noqa: E402

FIXTURE = Path(__file__).parent / "fixtures" / "delivery_move_rows.json"

DIRECTIVE = "A{a}: We should both pick {c} every round. Let's keep mutual {c} going."
INFO = "A{a}: Opponent A{b} is playing tit-for-tat; it answered my {d} with {d}."
OTHER = "A{a} exchange {r} vs A{b}: mutual {c} since exchange 3, continuing {c} now."


def _entry(agent: str, i: int, text: str) -> dict:
    return {"agent": agent, "text": text, "ts": f"2026-09-12T23:{i:02d}:00Z"}


def _board(agent_ids, labels, kinds, pad: int = 0) -> list[dict]:
    out = []
    for i, (a, kind) in enumerate(zip(agent_ids, kinds)):
        tpl = {"d": DIRECTIVE, "i": INFO, "o": OTHER}[kind]
        text = tpl.format(a=a[1:], b=(int(a[1:]) + 3) % 20, c=labels["C"],
                          d=labels["D"], r=i + 4) + ("x" * pad)
        out.append(_entry(a, i, text))
    return out


def _state(state_id: str, sandbox: str, agent: str, opponent: str, labels: dict,
           kinds: str, *, pad: int = 0) -> dict:
    ids = [f"A{(i * 2) % 20:02d}" for i in range(len(kinds))]
    entries = _board(ids, labels, kinds, pad=pad)
    return {
        "state_id": state_id, "sandbox": sandbox, "agent": agent,
        "opponent": opponent, "label_map": labels,
        "board": {"entries": entries, "total": len(entries), "shown": len(entries)},
        "entry_strata": [dr.entry_stratum(e["text"]) for e in entries],
        "entry_bands": [dr.length_band(e["text"]) for e in entries],
        "entry_labels": [dict(labels) for _ in entries],
        "totals": {"score": 30, "opp_score": 20, "rounds": 10, "self_c": 5, "opp_c": 5},
    }


def _states() -> list[dict]:
    return [
        _state("S1", "SB-a", "A03", "A11", {"C": "J", "D": "F"}, "dio"),
        _state("S2", "SB-b", "A05", "A07", {"C": "Q", "D": "X"}, "dio", pad=3),
        _state("S3", "SB-c", "A09", "A13", {"C": "T", "D": "N"}, "oid", pad=6),
    ]


# ---------------------------------------------------------------------------
# the sampler
# ---------------------------------------------------------------------------

def _synthetic_source(arm: str, path: str, *, games: int = 40) -> dr.SourceIndex:
    """A miniature moves.jsonl index whose boards cycle over the three post types."""
    kinds = "dio"
    index: dict[int, list[dict]] = {}
    for g in range(1, games + 1):
        rows: list[dict] = []
        opponent_is_llm = g % 2 == 0
        for agent, opp in (("A01", "A02"), ("A02", "A01")):
            if agent == "A02" and not opponent_is_llm:
                continue
            for rnd in range(1, 7):
                rows.append({"kind": "move", "phase": "warmup", "status": "ok",
                             "provider": "assigned", "game": g, "round": rnd,
                             "agent": agent, "action": "C", "executed": "C",
                             "opponent_action": "C", "model": "m",
                             "prompt_sha256": "", "sandbox": path})
            for rnd in range(1, 25):
                # the board's post type rotates with the game, so every stratum
                # exists in every round bin
                kind = kinds[(g + rnd) % 3]
                entries = _board(["A01"], {"C": "J", "D": "F"}, kind)
                rows.append({
                    "kind": "move", "phase": "scored", "status": "ok",
                    "provider": "deepinfra", "sandbox": path, "seed": 1,
                    "generation": 0, "game": g, "round": rnd, "agent": agent,
                    "model": "deepseek", "opponent": opp,
                    "opponent_model": "deepseek" if opponent_is_llm else "script:TitForTat",
                    "pair_type": "llm-llm" if opponent_is_llm else "llm-script",
                    "condition": "permitted", "framing": "F0", "paraphrase": "p1",
                    "label_map": {"C": "J", "D": "F"}, "option_order": ["J", "F"],
                    "action": "C", "executed": "C", "opponent_action": "C",
                    "prompt_sha256": f"sha-{path}-{g}-{rnd}-{agent}",
                    "tools_sha256": "tools", "warmup_rounds": 6,
                    "score_gap_at_call": 0,
                    "board": {"entries": entries, "total": 1, "shown": 1},
                    "_delivery": True,
                    "_stratum": dr.snapshot_stratum(entries),
                })
            if not opponent_is_llm:
                for rnd in range(1, 25):
                    rows.append({"kind": "move", "phase": "scored", "status": "ok",
                                 "provider": "script", "game": g, "round": rnd,
                                 "agent": opp, "model": "script:TitForTat",
                                 "executed": "C", "action": "C", "prompt_sha256": "",
                                 "sandbox": path})
        index[g] = rows
    return dr.SourceIndex(arm=arm, path=path, games=index)


def _sources():
    return [_synthetic_source("ahead", "src/B1-ahead"),
            _synthetic_source("behind", "src/B1-behind"),
            _synthetic_source("ahead", "src/B2-ahead"),
            _synthetic_source("behind", "src/B2-behind")]


def test_sampler_is_deterministic_in_its_seed():
    a, _ = dr.sample_states(_sources(), seed=9002, verify=False)
    b, _ = dr.sample_states(_sources(), seed=9002, verify=False)
    assert [s["state_id"] for s in a] == [s["state_id"] for s in b]
    c, _ = dr.sample_states(_sources(), seed=9003, verify=False)
    assert [s["state_id"] for s in c] != [s["state_id"] for s in a]


def test_sampler_hits_the_declared_stratification():
    states, _ = dr.sample_states(_sources(), seed=9002, verify=False)
    assert len(states) == 30
    assert sum(1 for s in states if s["arm"] == "ahead") == dr.N_PER_ARM
    assert sum(1 for s in states if s["arm"] == "behind") == dr.N_PER_ARM
    for arm in ("ahead", "behind"):
        for stratum in dr.STRATA:
            got = sum(1 for s in states
                      if s["arm"] == arm and s["post_stratum"] == stratum)
            assert got == 5, (arm, stratum, got)
    assert len({s["state_id"] for s in states}) == 30
    # every state actually saw at least one message
    assert all(s["board"]["entries"] for s in states)


def test_quota_is_fifteen_per_arm():
    assert sum(dr.QUOTA.values()) == dr.N_PER_ARM
    assert all(dr.QUOTA[(s, b)] >= 0 for s in dr.STRATA for b in dr.ROUND_BINS)


def test_only_a_final_attempt_read_counts_as_delivery():
    read = [{"name": "notes_read"}]
    clock = [{"name": "workspace_clock"}]
    # no retries: the top-level tool_calls are the final attempt's
    assert dr.final_attempt_read({"tool_calls": read}) is True
    assert dr.final_attempt_read({"tool_calls": clock}) is False
    assert dr.final_attempt_read({"tool_calls": []}) is False
    # a retried row is judged on the attempt that produced the logged action
    assert dr.final_attempt_read({"tool_calls": clock, "attempts": [
        {"tool_calls": clock}, {"tool_calls": read}]}) is True
    assert dr.final_attempt_read({"tool_calls": read, "attempts": [
        {"tool_calls": read}, {"tool_calls": clock}]}) is False


def test_post_typing_maps_the_coder_onto_the_spec_strata():
    assert dr.entry_stratum("We should both pick J every round.") == "directive_post"
    assert dr.entry_stratum("Opponent A07 plays tit-for-tat.") == "useful_looking_post"
    assert dr.entry_stratum("A01 exchange 4: mutual J, continuing.") == "irrelevant_post"
    # the snapshot takes the most salient type PRESENT, not the modal one
    entries = [{"text": "A01 exchange 4: mutual J, continuing."}] * 19 + [
        {"text": "We should both pick J every round."}]
    assert dr.snapshot_stratum(entries) == "directive_post"


# ---------------------------------------------------------------------------
# the randomisation transform
# ---------------------------------------------------------------------------

def _randomise(states=None):
    states = states or _states()
    pool = dr.donor_pool(states)
    universe = dr._id_universe(states)
    return states, {s["state_id"]: dr.randomise_snapshot(s, pool, universe)
                    for s in states}


def test_transform_is_deterministic():
    _, first = _randomise()
    _, second = _randomise()
    for sid in first:
        assert first[sid][0] == second[sid][0]
        assert first[sid][1] == second[sid][1]


def test_transform_preserves_format_band_and_post_type():
    states, out = _randomise()
    for s in states:
        snap, prov = out[s["state_id"]]
        real = s["board"]["entries"]
        assert len(snap["entries"]) == len(real)
        assert snap["total"] == s["board"]["total"]
        assert snap["shown"] == s["board"]["shown"]
        for r, n, p in zip(real, snap["entries"], prov):
            assert n["agent"] == r["agent"]          # posting identity kept
            assert n["ts"] == r["ts"]                # timing kept
            assert set(n) == set(r)                  # field shape kept
            assert dr.length_band(n["text"]) == dr.length_band(r["text"])
            assert dr.entry_stratum(n["text"]) == dr.entry_stratum(r["text"])
            assert p["donor_state"] != s["state_id"]


def test_transform_never_leaves_original_content_in_place():
    states, out = _randomise()
    for s in states:
        snap, _ = out[s["state_id"]]
        originals = {e["text"] for e in s["board"]["entries"]}
        for n in snap["entries"]:
            assert n["text"] not in originals


def test_randomised_text_never_names_the_current_pairing():
    states, out = _randomise()
    for s in states:
        snap, _ = out[s["state_id"]]
        for n in snap["entries"]:
            others = set(dr.AGENT_ID.findall(n["text"])) - {n["agent"]}
            assert s["agent"] not in others
            assert s["opponent"] not in others


def test_label_remap_rewrites_the_donor_pair_into_the_slot_pair():
    text = "A01: we should both pick J; J beats F when they pick F."
    donor = {"C": "J", "D": "F"}
    slot = {"C": "T", "D": "N"}
    straight = dr._remap_labels(text, donor, slot, False)
    flipped = dr._remap_labels(text, donor, slot, True)
    assert "J" not in straight and "F" not in straight
    assert straight.count("T") == 2 and straight.count("N") == 2
    assert straight == "A01: we should both pick T; T beats N when they pick N."
    assert flipped == "A01: we should both pick N; N beats T when they pick T."
    # an unresolvable pair leaves the text alone rather than corrupting it
    assert dr._remap_labels(text, None, slot, False) == text
    assert dr._remap_labels(text, donor, None, True) == text


def test_freeze_randomised_round_trips_through_json():
    states = _states()
    dr.freeze_randomised(states)
    again = json.loads(json.dumps(states))
    for s in again:
        assert s["board_randomised"]["entries"]
        assert len(s["randomisation"]["slots"]) == len(s["board"]["entries"])
        assert dr.board_for(s, "randomised") == s["board_randomised"]
        assert dr.board_for(s, "real") == s["board"]


def test_board_for_refuses_an_unfrozen_randomised_arm():
    with pytest.raises(SystemExit):
        dr.board_for(_states()[0], "randomised")
    with pytest.raises(ValueError):
        dr.board_for(_states()[0], "sideways")


# ---------------------------------------------------------------------------
# the tool handler
# ---------------------------------------------------------------------------

def test_handler_never_writes_and_serves_the_arm_it_is_given(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    states = _states()
    dr.freeze_randomised(states)
    state = states[0]
    seen = {}
    for arm in dr.ARMS:
        book = {"order": [], "posts": [], "board_size_at_read": None}
        handler = cr.make_frozen_handler(dict(state, board=dr.board_for(state, arm)),
                                         book)
        before = handler("notes_read", {})
        handler("notes_post", {"text": "a directive: always pick J"})
        after = handler("notes_read", {})
        assert after == before                 # the post did not reach the board
        assert book["posts"] == ["a directive: always pick J"]
        seen[arm] = before
    assert seen["real"] != seen["randomised"]
    assert len(seen["real"]["entries"]) == len(seen["randomised"]["entries"])
    assert list(tmp_path.iterdir()) == []      # nothing was created on disk


def test_seed_is_matched_across_arms():
    state = {"sandbox": "B1", "seed": 105, "generation": 0, "game": 7,
             "agent": "A03", "round": 5}
    # the seed depends on state and replicate only, never on the arm
    assert cr.call_seed(state, 0) != cr.call_seed(state, 1)
    jobs = dr.build_jobs([dict(_states()[0], index=0)])
    assert len(jobs) == len(dr.ARMS) * dr.REPLICATES
    assert {arm for _, arm, _ in jobs} == set(dr.ARMS)


# ---------------------------------------------------------------------------
# the rebuild, on a real logged row
# ---------------------------------------------------------------------------

def _fixture_state(monkeypatch):
    fx = json.loads(FIXTURE.read_text())
    sb = fx["sandbox"]
    monkeypatch.setitem(
        dr._NOTE_GAME, sb,
        {tuple(k.split("|", 2)): g for k, g in fx["note_index"].items()})
    for g, lm in fx["game_labels"].items():
        dr.GAME_LABELS[(sb, int(g))] = lm
    return fx, dr.freeze_state(fx["row"], fx["game_rows"])


def test_rebuild_reproduces_the_logged_hash_on_a_real_row(monkeypatch):
    """The load-bearing check: a real logged permitted decision, rebuilt byte for byte."""
    fx, state = _fixture_state(monkeypatch)
    _, _, prompt_sha, tools_sha = cr.rebuild(state)
    assert tools_sha == fx["row"]["tools_sha256"]
    assert prompt_sha == fx["row"]["prompt_sha256"]
    assert cr.verify_state(state) == (True, "ok")
    # and the state is a delivery state: the model read, and saw messages
    assert fx["row"]["_delivery"] is True
    assert state["board"]["entries"]
    assert state["post_stratum"] in dr.STRATA


def test_frozen_state_resolves_per_entry_label_pairs(monkeypatch):
    _, state = _fixture_state(monkeypatch)
    assert len(state["entry_labels"]) == len(state["board"]["entries"])
    assert all(lm is not None for lm in state["entry_labels"])
    # the board is sandbox-wide, so it carries more than the recipient's own pair
    pairs = {(lm["C"], lm["D"]) for lm in state["entry_labels"]}
    assert len(pairs) > 1


def test_a_tampered_state_is_caught_not_replayed(monkeypatch):
    _, state = _fixture_state(monkeypatch)
    state["history"] = state["history"][:-1] if state["history"] else [["C", "C"]]
    state["totals"] = cr.totals_for(state)
    ok, why = cr.verify_state(state)
    assert not ok and "prompt_sha256" in why


def test_frozen_states_file_matches_its_log():
    """The committed 30 states still rebuild to their logged hashes."""
    path = ROOT / dr.STATES_PATH
    if not path.exists():
        pytest.skip("states not sampled yet")
    states, _ = dr.load_states(path)
    assert len(states) == 30
    bad = [s["state_id"] for s in states if not cr.verify_state(s)[0]]
    assert not bad, bad
    assert all(s.get("board_randomised") for s in states), "randomised arm not frozen"


# ---------------------------------------------------------------------------
# the summary
# ---------------------------------------------------------------------------

def _call_row(arm, state_id, action, *, read=True, parse_ok=True, **kw):
    row = {f: "" for f in dr.CSV_FIELDS}
    row.update({"state_id": state_id, "state_index": 0, "sandbox": "SB",
                "game": 1, "round": 3, "agent": "A03", "deficit_arm": "ahead",
                "round_bin": "early", "post_stratum": "directive_post",
                "pair_type": "llm-llm", "arm": arm, "replicate": 1,
                "hash_matches_log": True, "read_happened": read,
                "action": action, "parse_ok": parse_ok, "logged_action": "C",
                "board_calls": 1 if read else 0, "read_calls": 1 if read else 0,
                "post_calls": 0, "decoy_calls": 0, "completion_tokens": 50,
                "prompt_tokens": 900, "latency_ms": 1000, "estimated_cost": 0.0001,
                "error": ""})
    row.update(kw)
    return row


def test_summary_survives_an_arm_with_zero_reads(tmp_path):
    rows = ([_call_row("real", f"S{i}", "C") for i in range(3)]
            + [_call_row("randomised", f"S{i}", "", read=False, parse_ok=False)
               for i in range(3)])
    s = dr.summarise_arm([r for r in rows if r["arm"] == "randomised"])
    assert s["n"] == 3 and s["n_delivered"] == 0
    assert s["read_rate"] == 0.0
    assert s["cooperate_rate"] is None and s["parse_fail_rate"] is None
    diffs, used, unpaired = dr.paired_diffs(rows)
    assert diffs == [] and used == [] and len(unpaired) == 3
    states = [dict(_states()[0], index=0, arm="ahead", round_bin="early",
                   post_stratum="directive_post", logged_action="C",
                   logged_prompt_sha256="x", logged_tools_sha256="y",
                   pair_type="llm-llm", game=1, round=3, opponent="A11",
                   warmup=[], history=[], condition="permitted", framing="F0",
                   paraphrase="p1", seed=1, generation=0, model="m",
                   opponent_model="m")]
    dr.write_summary(states, rows, tmp_path)
    text = (tmp_path / "SUMMARY.md").read_text()
    assert "0 state" in text or "Paired on the **0**" in text
    assert (tmp_path / "states-manifest.md").exists()


def test_summary_empty_arm_and_empty_rows(tmp_path):
    assert dr.summarise_arm([])["n"] == 0
    assert dr.paired_diffs([]) == ([], [], [])
    assert dr.exact_sign_flip([])["k"] == 0


def test_paired_difference_and_exact_sign_flip():
    rows = []
    for i in range(4):
        rows.append(_call_row("real", f"S{i}", "C"))
        rows.append(_call_row("randomised", f"S{i}", "D"))
    diffs, used, unpaired = dr.paired_diffs(rows)
    assert diffs == [1.0, 1.0, 1.0, 1.0] and len(used) == 4 and not unpaired
    res = dr.exact_sign_flip(diffs)
    assert res["exact"] and res["k"] == 4
    assert res["p"] == pytest.approx(2 / 16)      # only the all-same patterns
    # replicates inside a state average, they do not double-count
    rows.append(_call_row("real", "S0", "D", replicate=2))
    diffs2, _, _ = dr.paired_diffs(rows)
    assert sorted(diffs2) == [0.5, 1.0, 1.0, 1.0]


def test_exact_sign_flip_agrees_with_analysis_stats_and_stays_exact_past_twenty():
    from analysis.stats import sign_flip_test
    d = [0.5, -0.5, 1.0, 0.0, 0.25, -0.25, 0.75, 0.0]
    assert dr.exact_sign_flip(d)["p"] == pytest.approx(sign_flip_test(d)["p"])
    # 26 states, only 6 of them non-zero: still enumerable, so still exact
    big = [0.5, -0.5, 1.0, -1.0, 0.25, 0.75] + [0.0] * 20
    res = dr.exact_sign_flip(big)
    assert res["k"] == 26 and res["exact"] and res["exact_over_nonzero"] == 6
    assert 0.0 < res["p"] <= 1.0
