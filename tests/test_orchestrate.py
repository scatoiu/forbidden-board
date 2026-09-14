"""Tests for orchestrate.py — the overnight launcher.

Everything here runs the real orchestrator against the real `coop.cli`
subprocess. The only providers used are `mock:` (no network) and an unreachable
`http://127.0.0.1:1` endpoint (connection refused, no paid call).
"""

from __future__ import annotations

import json
import signal
import subprocess
import sys
import time
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import healthcheck as hc                                           # noqa: E402
import orchestrate as orc                                          # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "tests" / "fixtures"
V2 = ROOT / "specs" / "sandboxes-v2"


def run(argv: list[str]) -> int:
    """Call orchestrate.main directly so the assertions see its exit code."""
    return orc.main(argv)


def status_of(out: Path) -> dict:
    return json.loads((out / "STATUS.json").read_text())


def seed_complete_sandbox(out: Path, name: str, cost: float) -> None:
    """Write a finished moves.jsonl (a generation_end row) with a known cost."""
    d = out / name
    d.mkdir(parents=True, exist_ok=True)
    rows = [
        {"kind": "move", "sandbox": name, "model": "x",
         "usage": [{"iteration": 1, "estimated_cost": cost}]},
        {"kind": "game_end", "sandbox": name, "status": "ok",
         "moves_logged": 10, "fallback_count": 0},
        {"kind": "generation_end", "sandbox": name, "generation": 1},
    ]
    (d / "moves.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))


# ---------------------------------------------------------------------------
# Ordering (no subprocesses)
# ---------------------------------------------------------------------------

def test_block_ordering_is_complete_blocks_interleaved_within_a_block():
    specs = sorted(V2.glob("B*.yaml"))
    assert len(specs) == 96, "expected the 96 v2 block files"
    ordered = orc.plan([orc.read_spec(p) for p in specs])

    blocks = [sb.block for sb in ordered]
    first_seen = {b: blocks.index(b) for b in blocks}
    last_seen = {b: len(blocks) - 1 - blocks[::-1].index(b) for b in blocks}
    # all 16 of B1 before any of B2, and so on
    for a, b in zip(sorted(first_seen, key=orc.block_sort_key)[:-1],
                    sorted(first_seen, key=orc.block_sort_key)[1:]):
        assert last_seen[a] < first_seen[b], f"{a} is not finished before {b} starts"
    for b in first_seen:
        assert last_seen[b] - first_seen[b] == 15, f"{b} is not contiguous"

    # inside a block, channel and effort both change at every step: a stop leaves a
    # spread of cells, and slow (high) sandboxes are mixed with fast (off) ones
    b1 = [sb for sb in ordered if sb.block == "B1"]
    channels = [sb.channel for sb in b1]
    efforts = [sb.effort for sb in b1]
    assert len(set(channels[:4])) == 4, "the first four cells are not one of each channel"
    assert all(a != b for a, b in zip(channels, channels[1:])), "channel repeats back to back"
    assert all(a != b for a, b in zip(efforts, efforts[1:])), "effort repeats back to back"
    assert sorted(efforts).count("high") == 8

    # groups are the launch barrier: one per block, in order
    assert [sb.group for sb in ordered][:17] == [0] * 16 + [1]


def test_calibration_runs_first_when_present():
    specs = [V2 / "B2-absent-off-ahead.yaml", V2 / "calibration-effort.yaml",
             V2 / "B1-absent-off-ahead.yaml"]
    ordered = orc.plan([orc.read_spec(p) for p in specs])
    assert ordered[0].name == "calibration-effort"
    assert ordered[0].group == 0 and ordered[1].group == 1
    assert [sb.block for sb in ordered[1:]] == ["B1", "B2"]


def test_calibration_without_a_driver_halts_before_any_block(tmp_path):
    """`kind: fixed_state_replay` has no driver in this repo; it must stop the night."""
    code = run([str(V2 / "calibration-effort.yaml"), str(FIX / "orch-mock-a.yaml"),
                "--out-dir", str(tmp_path), "--parallel", "2"])
    st = status_of(tmp_path)
    assert code == 4
    assert st["halted"]["reason"] == "calibration"
    assert st["sandboxes"]["calibration-effort"]["state"] == "failed"
    assert st["sandboxes"]["orch-mock-a"]["state"] == "pending"


# ---------------------------------------------------------------------------
# Counters read off a real moves.jsonl
# ---------------------------------------------------------------------------

def test_scan_moves_reads_cost_and_quality_from_the_deepinfra_pilot():
    pilot = ROOT / "runs" / "pilot-deepinfra" / "pilot-di-forbidden-off" / "moves.jsonl"
    if not pilot.is_file():
        pytest.skip("the DeepSeek pilot run is not in this working copy")
    m = orc.scan_moves(pilot)
    assert m["complete"] is True
    # 28 game_end rows, but 22 unique games: an LLM-LLM game writes two rows
    assert m["games"] == 22 and m["aborted"] == 21
    assert m["game_end_rows"] == 28
    # $0.001935 before the attempts fix: the retried attempts were unpaid-for
    assert m["cost_usd"] == pytest.approx(0.002634, abs=1e-6)
    assert m["usage_rows"] == 84 and m["usage_rows_without_cost"] == 0
    assert orc.quality_verdict(m).startswith("aborted")


def test_scan_moves_on_a_missing_file_is_empty_not_an_error(tmp_path):
    m = orc.scan_moves(tmp_path / "nope.jsonl")
    assert m["complete"] is False
    assert not any(m[k] for k in ("moves", "games", "game_end_rows", "aborted",
                                  "llm_decisions", "fallbacks", "cost_usd",
                                  "bad_lines", "usage_rows"))


# ---------------------------------------------------------------------------
# A real three-sandbox night (mock provider)
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def three_fixtures(tmp_path_factory):
    out = tmp_path_factory.mktemp("night")
    code = run([str(FIX / "orch-mock-a.yaml"), str(FIX / "orch-mock-b.yaml"),
                str(FIX / "orch-mock-c.yaml"),
                "--out-dir", str(out), "--parallel", "2", "--budget-usd", "5"])
    return out, code


def test_three_fixtures_all_complete_with_status_and_logs(three_fixtures):
    out, code = three_fixtures
    st = status_of(out)
    assert code == 0
    assert [st["sandboxes"][n]["state"] for n in ("orch-mock-a", "orch-mock-b", "orch-mock-c")] \
        == ["done", "done", "done"]
    assert st["totals"]["sandboxes"]["done"] == 3
    assert st["halted"] is None
    for name in ("orch-mock-a", "orch-mock-b", "orch-mock-c"):
        s = st["sandboxes"][name]
        # 6 game_end rows over 5 unique games (the one LLM-LLM pairing writes two)
        assert s["games"] == 5 and s["aborted"] == 0 and s["cost_usd"] == 0.0
        assert s["started"] and s["ended"] and s["attempts"] == 1
        assert (out / name / "orchestrator.log").is_file()
        assert (out / name / "moves.jsonl").is_file()
    progress = (out / "PROGRESS.log").read_text()
    assert progress.count("start  ") == 3
    # the block barrier: T2 (orch-mock-c) starts only after both T1 sandboxes end
    order = [ln.split()[1:3] for ln in progress.splitlines() if ln.split()[1] in
             ("start", "done")]
    assert order[-2:] == [["start", "orch-mock-c"], ["done", "orch-mock-c"]]


def test_rerunning_the_same_command_skips_completed_sandboxes(three_fixtures):
    out, _ = three_fixtures
    code = run([str(FIX / "orch-mock-a.yaml"), str(FIX / "orch-mock-b.yaml"),
                str(FIX / "orch-mock-c.yaml"),
                "--out-dir", str(out), "--parallel", "2", "--budget-usd", "5"])
    st = status_of(out)
    assert code == 0
    assert st["totals"]["sandboxes"]["skipped"] == 3
    assert "skip     orch-mock-a" in (out / "PROGRESS.log").read_text()


def test_status_flag_prints_a_table(three_fixtures, capsys):
    out, _ = three_fixtures
    assert run(["--status", "--out-dir", str(out)]) == 0
    printed = capsys.readouterr().out
    assert "orch-mock-a" in printed and "projection" in printed
    # RUNBOOK promises the unpriced-row counter; it was only ever in scan_moves
    assert "unpriced usage rows 0" in printed
    assert status_of(out)["totals"]["usage_rows_without_cost"] == 0


# ---------------------------------------------------------------------------
# The two guards
# ---------------------------------------------------------------------------

def test_budget_stop_leaves_the_rest_pending(tmp_path):
    """A completed sandbox worth $0.01 is already over a $0.000001 budget."""
    seed_complete_sandbox(tmp_path, "orch-mock-a", cost=0.01)
    code = run([str(FIX / "orch-mock-a.yaml"), str(FIX / "orch-mock-b.yaml"),
                str(FIX / "orch-mock-c.yaml"),
                "--out-dir", str(tmp_path), "--parallel", "2",
                "--budget-usd", "0.000001"])
    st = status_of(tmp_path)
    assert code == 4
    assert st["halted"]["reason"] == "budget"
    assert st["sandboxes"]["orch-mock-a"]["state"] == "skipped"
    assert st["sandboxes"]["orch-mock-b"]["state"] == "pending"
    assert st["sandboxes"]["orch-mock-c"]["state"] == "pending"
    assert st["totals"]["cost_usd"] == pytest.approx(0.01)
    assert not (tmp_path / "orch-mock-b" / "moves.jsonl").exists()


def test_two_consecutive_quality_failures_halt_the_night(tmp_path):
    """Every call fails -> every game aborts -> two quality_fail in a row -> halt."""
    code = run([str(FIX / "orch-err-a.yaml"), str(FIX / "orch-err-b.yaml"),
                str(FIX / "orch-mock-c.yaml"),
                "--out-dir", str(tmp_path), "--parallel", "2", "--budget-usd", "5"])
    st = status_of(tmp_path)
    assert code == 4
    assert st["sandboxes"]["orch-err-a"]["state"] == "quality_fail"
    assert st["sandboxes"]["orch-err-b"]["state"] == "quality_fail"
    assert st["sandboxes"]["orch-err-a"]["aborted_frac"] == 1.0
    assert st["halted"]["reason"] == "quality"
    assert "consecutive" in st["halted"]["detail"]
    # the next block never starts
    assert st["sandboxes"]["orch-mock-c"]["state"] == "pending"


def test_a_sandbox_that_exits_non_zero_is_retried_once_then_failed(tmp_path):
    code = run([str(FIX / "orch-bad.yaml"), "--out-dir", str(tmp_path),
                "--parallel", "1", "--budget-usd", "5"])
    st = status_of(tmp_path)["sandboxes"]["orch-bad"]
    assert code == 1
    assert st["state"] == "failed" and st["attempts"] == 2 and st["exit_code"] == 2
    assert "retry    orch-bad" in (tmp_path / "PROGRESS.log").read_text()


def test_a_partial_run_is_moved_aside_and_restarted(tmp_path):
    """The runner refuses a used run directory, so resume must clear a partial one."""
    d = tmp_path / "orch-mock-a"
    d.mkdir(parents=True)
    (d / "moves.jsonl").write_text(json.dumps({"kind": "move", "sandbox": "orch-mock-a"}) + "\n")
    code = run([str(FIX / "orch-mock-a.yaml"), "--out-dir", str(tmp_path),
                "--parallel", "1", "--budget-usd", "5"])
    assert code == 0
    assert status_of(tmp_path)["sandboxes"]["orch-mock-a"]["state"] == "done"
    assert list(tmp_path.glob("orch-mock-a.partial-*")), "the partial run was not preserved"


# ---------------------------------------------------------------------------
# Dry run
# ---------------------------------------------------------------------------

def test_dry_run_launches_nothing_and_prints_the_command(tmp_path, capsys):
    code = run([str(V2 / "B1-absent-off-ahead.yaml"), "--dry-run",
                "--out-dir", str(tmp_path)])
    printed = capsys.readouterr().out
    assert code == 0
    assert "run-population" in printed
    # concurrency and max_tokens are the YAML's: passing them would be overridden
    assert "--concurrency" not in printed and "--max-tokens" not in printed
    assert not (tmp_path / "STATUS.json").exists()
    assert not (tmp_path / "B1-absent-off-ahead").exists()


def test_runner_flags_are_forwarded_only_when_asked_for(tmp_path, capsys):
    run([str(V2 / "B1-absent-off-ahead.yaml"), "--dry-run", "--out-dir", str(tmp_path),
         "--per-sandbox-concurrency", "8", "--runner-arg=--no-questions"])
    printed = capsys.readouterr().out
    assert "--concurrency 8" in printed and "--no-questions" in printed


def test_the_orchestrator_is_runnable_as_a_script():
    out = subprocess.run([sys.executable, str(ROOT / "orchestrate.py"), "--help"],
                         capture_output=True, text=True, cwd=ROOT)
    assert out.returncode == 0 and "--budget-usd" in out.stdout


# ---------------------------------------------------------------------------
# Signals
# ---------------------------------------------------------------------------

def test_sigterm_stops_launching_and_lets_the_running_sandbox_finish(tmp_path):
    proc = subprocess.Popen(
        [sys.executable, str(ROOT / "orchestrate.py"),
         str(FIX / "orch-mock-a.yaml"), str(FIX / "orch-mock-b.yaml"),
         str(FIX / "orch-mock-c.yaml"),
         "--out-dir", str(tmp_path), "--parallel", "1", "--budget-usd", "5"],
        cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
    )
    progress = tmp_path / "PROGRESS.log"
    for _ in range(300):                       # wait for the first sandbox to start
        if progress.is_file() and "start    orch-mock-a" in progress.read_text():
            break
        time.sleep(0.1)
    else:                                      # pragma: no cover - startup never happened
        proc.kill()
        pytest.fail("the first sandbox never started")
    proc.send_signal(signal.SIGTERM)
    proc.communicate(timeout=120)

    st = status_of(tmp_path)
    assert proc.returncode == 4
    assert st["halted"]["reason"] == "signal"
    assert st["sandboxes"]["orch-mock-a"]["state"] == "done"      # allowed to finish
    assert st["sandboxes"]["orch-mock-b"]["state"] == "pending"
    assert st["sandboxes"]["orch-mock-c"]["state"] == "pending"


# ---------------------------------------------------------------------------
# scan_moves accounting (review-astra findings 1, 3, 5, 12)
# ---------------------------------------------------------------------------

def write_rows(path: Path, rows: list[dict]) -> Path:
    path.write_text("".join(json.dumps(r) + "\n" for r in rows))
    return path


def test_scan_moves_uses_attempt_usage_and_never_adds_the_final_attempt_twice(tmp_path):
    """finding 3: `usage` is the last attempt only; `attempts[*].usage` is all of them."""
    rows = [
        # a retried move: two attempts, the second one repeated at the top level
        {"kind": "move", "usage": [{"iteration": 1, "estimated_cost": 0.02}],
         "attempts": [{"usage": [{"iteration": 1, "estimated_cost": 0.01}]},
                      {"usage": [{"iteration": 1, "estimated_cost": 0.02}]}]},
        # a first-try move keeps using the top-level list
        {"kind": "move", "usage": [{"iteration": 1, "estimated_cost": 0.04}]},
        # an attempts list with no usage in it must not hide the top-level one
        {"kind": "move", "usage": [{"iteration": 1, "estimated_cost": 0.08}],
         "attempts": [{"fallback_flag": "refusal"}]},
    ]
    m = orc.scan_moves(write_rows(tmp_path / "m.jsonl", rows))
    assert m["cost_usd"] == pytest.approx(0.01 + 0.02 + 0.04 + 0.08)
    assert m["usage_rows"] == 4 and m["usage_rows_without_cost"] == 0


def test_scan_moves_counts_end_of_game_question_spend(tmp_path):
    """finding 14/3: the two end questions are paid calls and belong in the total."""
    rows = [
        {"kind": "move", "usage": [{"iteration": 1, "estimated_cost": 0.10}]},
        {"kind": "game_end", "generation": 0, "game": 1, "agent": "A00",
         "status": "ok", "moves_logged": 5, "fallback_count": 0,
         "question_usage": [{"iteration": 1, "estimated_cost": 0.003},
                            {"iteration": 1, "estimated_cost": 0.004}],
         "question_errors": ["Timeout: read timed out"]},
    ]
    m = orc.scan_moves(write_rows(tmp_path / "m.jsonl", rows))
    assert m["cost_usd"] == pytest.approx(0.107)
    assert m["usage_rows"] == 3


@pytest.mark.parametrize("cost", ["oops", float("nan"), float("inf"), -0.5, None])
def test_scan_moves_refuses_an_unusable_price_instead_of_crashing_or_poisoning(
        tmp_path, cost):
    """finding 5: a string crashed the parent; a NaN disabled the budget comparison."""
    rows = [
        {"kind": "move", "usage": [{"iteration": 1, "estimated_cost": cost}]},
        {"kind": "move", "usage": [{"iteration": 1, "estimated_cost": 0.25}]},
    ]
    # NaN and inf are not JSON, so they are written the way a provider would leak
    # them into a row and re-read with the default parser.
    m = orc.scan_moves(write_rows(tmp_path / "m.jsonl", rows))
    assert m["cost_usd"] == pytest.approx(0.25)          # never NaN, never a crash
    assert m["cost_usd"] > 0.2                           # the comparison still works
    assert m["usage_rows"] == 2 and m["usage_rows_without_cost"] == 1


def test_scan_moves_keeps_an_explicit_zero_price_as_a_priced_row(tmp_path):
    rows = [{"kind": "move", "usage": [{"iteration": 1, "estimated_cost": 0}]}]
    m = orc.scan_moves(write_rows(tmp_path / "m.jsonl", rows))
    assert m["usage_rows"] == 1 and m["usage_rows_without_cost"] == 0


def test_scan_moves_counts_unique_games_not_agent_game_rows(tmp_path):
    """finding 12: an LLM-LLM abort was weighted twice against the 10% guard."""
    rows = [
        {"kind": "game_end", "generation": 0, "game": 1, "agent": "A00",
         "status": "aborted", "moves_logged": 0, "fallback_count": 0},
        {"kind": "game_end", "generation": 0, "game": 1, "agent": "A01",
         "status": "aborted", "moves_logged": 0, "fallback_count": 0},
        {"kind": "game_end", "generation": 0, "game": 2, "agent": "A00",
         "status": "ok", "moves_logged": 5, "fallback_count": 0},
        # same game number, next generation: a different game
        {"kind": "game_end", "generation": 1, "game": 2, "agent": "A00",
         "status": "ok", "moves_logged": 5, "fallback_count": 0},
    ]
    m = orc.scan_moves(write_rows(tmp_path / "m.jsonl", rows))
    assert m["game_end_rows"] == 4
    assert m["games"] == 3 and m["aborted"] == 1
    assert m["aborted_frac"] == pytest.approx(1 / 3)


def test_a_crashed_game_task_writes_aborted_game_end_rows_scan_moves_can_see(
        tmp_path, monkeypatch):
    """finding 1: a game lost to an exception was invisible to the quality gate."""
    from coop import population as pop

    cfg = pop.SandboxConfig.from_dict({
        "sandbox": "CRASH", "population": {"mock:tft": 2, "TitForTat": 2},
        "rounds_per_game": 2, "prompts_dir": None, "end_of_game_questions": False,
        "out_dir": str(tmp_path),
    })

    def boom(self, a, b, **kw):
        raise RuntimeError("axelrod internal error")

    monkeypatch.setattr(pop.SandboxRun, "play_match", boom)
    run = pop.run_sandbox(cfg, out_dir=tmp_path / "crash")

    rows = [json.loads(l) for l in run.logger.path.read_text().splitlines()]
    ends = [r for r in rows if r["kind"] == "game_end"]
    # one row per LLM agent: 1 llm-llm pairing (2 rows) + 4 llm-script (4 rows);
    # the script-script pairing writes none, exactly as a played game would
    assert len(ends) == 6
    assert all(r["status"] == "aborted" for r in ends)
    assert all(r["error"] == "RuntimeError: axelrod internal error" for r in ends)
    for r in ends:
        assert r["sandbox"] == "CRASH" and r["seed"] == cfg.seed
        assert r["condition"] == cfg.channel and r["effort"] == "off"
        assert r["agent"] and r["model"] and r["opponent"] and r["opponent_model"]
        assert r["pair_type"] in ("llm-llm", "llm-script")
        assert r["generation"] == 0 and isinstance(r["game"], int)
        assert r["rounds"] == 0 and r["score"] == 0 and r["moves_logged"] == 0
        assert r["coop_rate"] is None and r["classification_answer"] is None
    assert len(run.aborted_games) == 6

    m = orc.scan_moves(run.logger.path)
    assert m["game_end_rows"] == 6
    assert m["games"] == 5 and m["aborted"] == 5      # unique games, all failed
    assert m["aborted_frac"] == 1.0
    assert orc.quality_verdict(m).startswith("aborted")


# ---------------------------------------------------------------------------
# healthcheck.py (review-astra finding 17)
# ---------------------------------------------------------------------------

def seed_health_dir(root: Path, name: str, *, games: int, aborted: int,
                    cost: float = 0.0) -> None:
    """`games` unique LLM-LLM games (two game_end rows each), `aborted` of them bad."""
    d = root / name
    d.mkdir(parents=True, exist_ok=True)
    rows: list[dict] = []
    for g in range(1, games + 1):
        status = "aborted" if g <= aborted else "ok"
        for agent in ("A00", "A01"):
            rows.append({"kind": "game_end", "generation": 0, "game": g,
                         "agent": agent, "status": status, "moves_logged": 2,
                         "fallback_count": 0})
    rows.append({"kind": "move", "usage": [{"iteration": 1, "estimated_cost": cost}]})
    (d / "moves.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))


def health(tmp_path, capsys, **status) -> tuple[int, dict]:
    if status:
        (tmp_path / "STATUS.json").write_text(json.dumps(status))
    code = hc.main(["--runs", str(tmp_path), "--json"])
    return code, json.loads(capsys.readouterr().out.strip())


def test_healthcheck_flags_the_worst_sandbox_and_ignores_archived_attempts(
        tmp_path, capsys):
    seed_health_dir(tmp_path, "good", games=40, aborted=1)          # 2.5%
    seed_health_dir(tmp_path, "bad", games=30, aborted=10)          # 33.3%
    seed_health_dir(tmp_path, "small", games=4, aborted=4)          # below --min-games
    seed_health_dir(tmp_path, "bad.partial-20260912T000000Z", games=30, aborted=30)

    code, out = health(tmp_path, capsys, sandboxes={}, halted=None)

    assert out["games"] == 40 + 30 + 4          # the .partial- attempt is excluded
    assert out["max_sandbox_abort"] == "bad=33.3%"
    assert any(f.startswith("ABORTS:bad 10/30") for f in out["flags"])
    assert code == 2                            # a shell loop can notice


def test_healthcheck_is_quiet_and_exits_zero_when_every_sandbox_is_healthy(
        tmp_path, capsys):
    seed_health_dir(tmp_path, "ok-a", games=40, aborted=2, cost=0.01)
    code, out = health(tmp_path, capsys, sandboxes={"ok-a": {"state": "done"}},
                       halted=None)
    assert out["flags"] == [] and code == 0
    assert out["max_sandbox_abort"] == "ok-a=5.0%"
    assert out["naive_proj"] is not None        # kept, but labelled naive


def test_healthcheck_reports_a_halt_and_an_absent_orchestrator(tmp_path, capsys):
    seed_health_dir(tmp_path, "s1", games=4, aborted=0)
    code, out = health(
        tmp_path, capsys,
        sandboxes={"s1": {"state": "running"}, "s2": {"state": "done"}},
        halted={"reason": "budget", "detail": "$91 > $90", "at": "now"})
    assert "HALTED:budget" in out["flags"]
    assert "ORCHESTRATOR_DOWN" in out["flags"]   # no orchestrate.py names this dir
    assert code == 2


def test_healthcheck_does_not_call_a_finished_run_orchestrator_down(tmp_path, capsys):
    seed_health_dir(tmp_path, "s1", games=4, aborted=0)
    code, out = health(tmp_path, capsys,
                       sandboxes={"s1": {"state": "done"}}, halted=None)
    assert "ORCHESTRATOR_DOWN" not in out["flags"]


def test_healthcheck_parses_rows_rather_than_matching_the_word_aborted(
        tmp_path, capsys):
    """A post quoting the word must not become an abort (the old substring match)."""
    d = tmp_path / "quoted"
    d.mkdir(parents=True)
    rows = [{"kind": "game_end", "generation": 0, "game": g, "agent": "A00",
             "status": "ok", "posts": ["the last game aborted, be careful"]}
            for g in range(1, 31)]
    (d / "moves.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))
    code, out = health(tmp_path, capsys, sandboxes={}, halted=None)
    assert out["aborted"] == 0 and out["games"] == 30
    assert not any(f.startswith("ABORTS") for f in out["flags"])
