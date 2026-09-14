"""Repair mode: replay only the named games of an existing sandbox spec.

A game that aborted because the account ran out of balance (HTTP 402) or hit a
rate limit (HTTP 429) is recorded as `fallback_flag: "provider_error"` on the
aborting move row and `status: "aborted"` on the game_end rows. Those games are
not model failures, so they are worth replaying after the fact — but only if the
replay is the *same game*: same pairing, same pairing index, same seeds, same
label draw. These tests pin that down with the mock provider; no API is called.
"""

from __future__ import annotations

import hashlib
import json

import pytest
import yaml

from coop.cli import main as cli_main
from coop.population import provider_error_aborts, source_fingerprint

SPEC = {
    "sandbox": "REP",
    "population": {"mock:tft": 2, "mock:cooperator": 1, "AlwaysDefect": 1},
    "channel": "absent",
    "rounds_per_game": 4,
    "generations": 1,
    "seed": 11,
    "concurrency": 1,
    "provider": "mock",
    "prompts_dir": None,
    "end_of_game_questions": False,
}


def _spec(tmp_path, name="spec.yaml", **kw):
    spec = dict(SPEC)
    spec.update(kw)
    path = tmp_path / name
    path.write_text(yaml.safe_dump(spec))
    return path


def _rows(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def _moves_at(root, sandbox):
    return _rows(root / sandbox / "moves.jsonl")


def _cli(*argv, expect=0):
    rc = cli_main(list(argv))
    assert rc == expect, f"exit {rc} from {argv}"
    return rc


def _first_scored(rows):
    """(game, agent) -> the first scored move row, in file order."""
    out: dict[tuple[int, str], dict] = {}
    for r in rows:
        if r["kind"] != "move" or r.get("phase", "scored") != "scored":
            continue
        out.setdefault((r["game"], r["agent"]), r)
    return out


def _sequences(rows):
    """(game, agent) -> the executed action sequence."""
    out: dict[tuple[int, str], list[str]] = {}
    for r in rows:
        if r["kind"] != "move" or r.get("phase", "scored") != "scored":
            continue
        out.setdefault((r["game"], r["agent"]), []).append(r["executed"])
    return out


def _original(tmp_path, spec):
    """Run the spec in full and return its move/game_end rows."""
    _cli("run-population", "--config", str(spec), "--out-dir", str(tmp_path / "orig"))
    return _moves_at(tmp_path / "orig", "REP")


# --------------------------------------------------------------------------
# (a) --only-games replays exactly those games, identically
# --------------------------------------------------------------------------

def test_only_games_replays_the_named_games_identically(tmp_path):
    spec = _spec(tmp_path)
    orig = _original(tmp_path, spec)

    ids = sorted({r["game"] for r in orig if r["kind"] == "move"})
    assert len(ids) == 6                                   # 4 agents, round robin
    picked = [ids[1], ids[4]]

    _cli("run-population", "--config", str(spec),
         "--out-dir", str(tmp_path / "rep"),
         "--only-games", ",".join(str(g) for g in picked))
    rep = _moves_at(tmp_path / "rep", "REP-repair")

    # Only the named games, and not renumbered.
    assert sorted({r["game"] for r in rep if r["kind"] == "move"}) == picked
    # Rows carry the repair sandbox, so nothing collides on disk.
    assert {r["sandbox"] for r in rep} == {"REP-repair"}

    o_first, n_first = _first_scored(orig), _first_scored(rep)
    assert set(n_first) == {k for k in o_first if k[0] in picked}
    for key, row in n_first.items():
        was = o_first[key]
        assert (row["opponent"], row["opponent_model"]) == (was["opponent"], was["opponent_model"])
        assert row["label_map"] == was["label_map"]
        assert row["option_order"] == was["option_order"]
        # The board is empty at the first scored move in both runs, so the prompt
        # — brief, payoffs, labels, ids, empty history — is byte-identical.
        assert row["prompt_sha256"] == was["prompt_sha256"], key
        assert row["model"] == was["model"]

    # The whole replayed game matches, not just its first move.
    o_seq, n_seq = _sequences(orig), _sequences(rep)
    assert n_seq == {k: v for k, v in o_seq.items() if k[0] in picked}

    ends = {(r["game"], r["agent"]): r for r in rep if r["kind"] == "game_end"}
    assert ends and all(e["sandbox"] == "REP-repair" for e in ends.values())
    o_ends = {(r["game"], r["agent"]): r for r in orig if r["kind"] == "game_end"}
    for key, end in ends.items():
        assert (end["score"], end["opp_score"], end["rounds"]) == (
            o_ends[key]["score"], o_ends[key]["opp_score"], o_ends[key]["rounds"])


def test_sandbox_override_names_the_repair_run(tmp_path):
    spec = _spec(tmp_path)
    _original(tmp_path, spec)
    _cli("run-population", "--config", str(spec), "--out-dir", str(tmp_path / "rep"),
         "--sandbox", "REP-402-retry", "--only-games", "2")
    rows = _moves_at(tmp_path / "rep", "REP-402-retry")
    assert {r["sandbox"] for r in rows} == {"REP-402-retry"}
    manifest = json.loads((tmp_path / "rep" / "REP-402-retry" / "manifest.json").read_text())
    assert manifest["repair_of"] == "REP"


# --------------------------------------------------------------------------
# (b) --only-games-from selects provider_error aborts only
# --------------------------------------------------------------------------

def _abort_rows(generation, game, flag, *, game_end_status="aborted"):
    """A minimal aborting move row plus its two game_end rows."""
    rows = [{"kind": "move", "generation": generation, "game": game, "round": 3,
             "agent": "A00", "status": "aborted", "fallback_flag": flag,
             "parse_ok": False, "executed": None}]
    for agent, opp in (("A00", "A01"), ("A01", "A00")):
        rows.append({"kind": "game_end", "generation": generation, "game": game,
                     "agent": agent, "opponent": opp, "status": game_end_status})
    return rows


def _synthetic_moves(tmp_path, name="moves.jsonl"):
    rows = []
    # two real provider_error aborts
    rows += _abort_rows(0, 2, "provider_error")
    rows += _abort_rows(0, 5, "provider_error")
    # ambiguous: the game aborted, but the model — not the account — failed
    rows += _abort_rows(0, 4, "truncated")
    # a provider error the retry survived: the game finished, nothing to repair
    rows.append({"kind": "move", "generation": 0, "game": 3, "round": 1, "agent": "A00",
                 "status": "ok", "fallback_flag": "provider_error", "parse_ok": True,
                 "executed": "C"})
    rows.append({"kind": "game_end", "generation": 0, "game": 3, "agent": "A00",
                 "opponent": "A01", "status": "ok"})
    # a crashed game: game_end aborted, no move rows at all
    rows.append({"kind": "game_end", "generation": 0, "game": 6, "agent": "A00",
                 "opponent": "A01", "status": "aborted", "error": "RuntimeError: boom"})
    path = tmp_path / name
    path.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
    return path


def test_provider_error_aborts_picks_only_the_unambiguous_two(tmp_path):
    path = _synthetic_moves(tmp_path)
    assert provider_error_aborts(path) == [(0, 2), (0, 5)]


def test_provider_error_aborts_keys_by_generation_and_game(tmp_path):
    rows = _abort_rows(0, 7, "provider_error") + _abort_rows(1, 19, "provider_error")
    path = tmp_path / "m.jsonl"
    path.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
    assert provider_error_aborts(path) == [(0, 7), (1, 19)]


def test_only_games_from_runs_just_those_games(tmp_path):
    spec = _spec(tmp_path)
    _original(tmp_path, spec)
    src = _synthetic_moves(tmp_path)

    _cli("run-population", "--config", str(spec), "--out-dir", str(tmp_path / "rep"),
         "--only-games-from", str(src))
    rep = _moves_at(tmp_path / "rep", "REP-repair")
    assert sorted({r["game"] for r in rep if r["kind"] == "move"}) == [2, 5]


def test_only_games_and_only_games_from_are_exclusive(tmp_path):
    spec = _spec(tmp_path)
    src = _synthetic_moves(tmp_path)
    _cli("run-population", "--config", str(spec), "--out-dir", str(tmp_path / "rep"),
         "--only-games", "2", "--only-games-from", str(src), expect=2)


def test_a_source_with_no_provider_error_aborts_runs_nothing(tmp_path, capsys):
    spec = _spec(tmp_path)
    src = tmp_path / "clean.jsonl"
    src.write_text("\n".join(json.dumps(r) for r in _abort_rows(0, 4, "truncated")) + "\n")
    _cli("run-population", "--config", str(spec), "--out-dir", str(tmp_path / "rep"),
         "--only-games-from", str(src))
    assert "nothing to repair" in capsys.readouterr().err
    assert not (tmp_path / "rep").exists()


def test_an_id_outside_the_schedule_is_reported(tmp_path, capsys):
    spec = _spec(tmp_path)
    _original(tmp_path, spec)
    _cli("run-population", "--config", str(spec), "--out-dir", str(tmp_path / "rep"),
         "--only-games", "999", expect=1)
    assert "no game with id [999]" in capsys.readouterr().err


# --------------------------------------------------------------------------
# (c) the manifest records what was repaired and from where
# --------------------------------------------------------------------------

def test_repair_manifest_records_provenance(tmp_path):
    spec = _spec(tmp_path)
    _original(tmp_path, spec)
    src = _synthetic_moves(tmp_path)

    _cli("run-population", "--config", str(spec), "--out-dir", str(tmp_path / "rep"),
         "--only-games-from", str(src))
    manifest = json.loads((tmp_path / "rep" / "REP-repair" / "manifest.json").read_text())

    assert manifest["repair_of"] == "REP"
    assert manifest["config"]["sandbox"] == "REP-repair"
    assert manifest["config"]["repair_of"] == "REP"
    assert manifest["only_games"] == [2, 5]
    assert manifest["board_replay"] == "fresh"
    assert manifest["source_moves"] == str(src)
    assert manifest["source_moves_bytes"] == src.stat().st_size
    assert manifest["source_moves_sha256_1mb"] == hashlib.sha256(src.read_bytes()).hexdigest()
    # The denominator is the repaired games, not the whole sandbox.
    assert manifest["expected_moves"] == 2 * SPEC["rounds_per_game"] * 2


def test_only_games_manifest_has_no_source(tmp_path):
    spec = _spec(tmp_path)
    _original(tmp_path, spec)
    _cli("run-population", "--config", str(spec), "--out-dir", str(tmp_path / "rep"),
         "--only-games", "3")
    manifest = json.loads((tmp_path / "rep" / "REP-repair" / "manifest.json").read_text())
    assert manifest["only_games"] == [3]
    assert manifest["source_moves"] is None
    assert manifest["source_moves_sha256_1mb"] is None


def test_a_normal_run_carries_no_repair_keys(tmp_path):
    spec = _spec(tmp_path)
    _original(tmp_path, spec)
    manifest = json.loads((tmp_path / "orig" / "REP" / "manifest.json").read_text())
    assert "repair_of" not in manifest and "only_games" not in manifest
    assert manifest["config"]["repair_of"] is None


def test_source_fingerprint_hashes_only_the_first_megabyte(tmp_path):
    from coop.population import SOURCE_DIGEST_BYTES

    head = b"x" * SOURCE_DIGEST_BYTES
    short, long = tmp_path / "a.jsonl", tmp_path / "b.jsonl"
    short.write_bytes(head)
    long.write_bytes(head + b"tail")
    a, b = source_fingerprint(short), source_fingerprint(long)
    assert a["source_moves_sha256_1mb"] == b["source_moves_sha256_1mb"]
    assert (a["source_moves_bytes"], b["source_moves_bytes"]) == (
        SOURCE_DIGEST_BYTES, SOURCE_DIGEST_BYTES + 4)


# --------------------------------------------------------------------------
# (d) a preassigned schedule, and what repair refuses to pretend
# --------------------------------------------------------------------------

def test_preassigned_schedule_spec_is_honoured(tmp_path):
    spec = _spec(tmp_path, name="preassigned.yaml", generations=1, concurrency=4,
                 schedule={"preassigned": True, "shuffle_seed": 11,
                           "serialize_within_sandbox": True})
    orig = _original(tmp_path, spec)
    picked = sorted({r["game"] for r in orig if r["kind"] == "move"})[2]

    _cli("run-population", "--config", str(spec), "--out-dir", str(tmp_path / "rep"),
         "--only-games", str(picked))
    rep = _moves_at(tmp_path / "rep", "REP-repair")
    manifest = json.loads((tmp_path / "rep" / "REP-repair" / "manifest.json").read_text())

    assert manifest["schedule"] == {"preassigned": True, "shuffle_seed": 11,
                                    "serialize_within_sandbox": True}
    assert manifest["config"]["concurrency"] == 1      # serialize_within_sandbox
    assert _sequences(rep) == {k: v for k, v in _sequences(orig).items() if k[0] == picked}


def test_game_ids_do_not_renumber_across_generations(tmp_path):
    """A generation-1 id must land on generation 1's pairing, not generation 0's."""
    spec = _spec(tmp_path, name="two-gen.yaml", generations=2)
    orig = _original(tmp_path, spec)
    gen1 = sorted({r["game"] for r in orig if r["kind"] == "move" and r["generation"] == 1})
    assert gen1 == [7, 8, 9, 10, 11, 12]
    picked = gen1[3]

    _cli("run-population", "--config", str(spec), "--out-dir", str(tmp_path / "rep"),
         "--only-games", str(picked))
    rep = _moves_at(tmp_path / "rep", "REP-repair")
    assert {(r["generation"], r["game"]) for r in rep if r["kind"] == "move"} == {(1, picked)}
    assert _sequences(rep) == {k: v for k, v in _sequences(orig).items() if k[0] == picked}
    # Generation 0 was scheduled (so the counter advanced) but never played.
    assert not [r for r in rep if r["generation"] == 0]


def test_repair_refuses_a_run_with_reproduction(tmp_path, capsys):
    spec = _spec(tmp_path, name="wf.yaml", generations=2,
                 reproduction={"rule": "wright_fisher", "fitness": "mean_per_move"})
    _cli("run-population", "--config", str(spec), "--out-dir", str(tmp_path / "orig"))
    _cli("run-population", "--config", str(spec), "--out-dir", str(tmp_path / "rep"),
         "--only-games", "2", expect=2)
    assert "repair cannot replay a run with reproduction" in capsys.readouterr().err


def test_run_sandbox_refuses_only_games_without_repair_of(tmp_path):
    from coop.population import SandboxConfig, run_sandbox

    cfg = SandboxConfig.from_dict({**SPEC, "out_dir": str(tmp_path)})
    with pytest.raises(ValueError, match="repair_of"):
        run_sandbox(cfg, out_dir=tmp_path / "x", only_games=[1])
