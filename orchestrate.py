#!/usr/bin/env python3
"""Overnight launcher for the v2 tournament blocks.

Runs each sandbox YAML as its own `python -m coop.cli run-population` subprocess,
N sandboxes at a time, in block order, with a budget guard, a quality guard, a
resumable `STATUS.json` and a one-line-per-event `PROGRESS.log`.

    python orchestrate.py specs/sandboxes-v2/B*.yaml --dry-run
    python orchestrate.py specs/sandboxes-v2/B*.yaml --out-dir runs/v2 --budget-usd 90
    python orchestrate.py --status --out-dir runs/v2

Nothing here reads or writes an API key: the child process resolves its own via
`coop.env`. See RUNBOOK.md for the operating procedure.
"""

from __future__ import annotations

import argparse
import glob as globmod
import json
import math
import os
import signal
import subprocess
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

STATUS_NAME = "STATUS.json"
PROGRESS_NAME = "PROGRESS.log"
LOG_NAME = "orchestrator.log"
CALIBRATION_STEM = "calibration-effort"

#: A sandbox is quality_fail above either of these (task brief §4).
ABORT_LIMIT = 0.10
FALLBACK_LIMIT = 0.05
#: Two quality_fail sandboxes in a row stop the night.
CONSECUTIVE_LIMIT = 2

TERMINAL = ("done", "failed", "quality_fail", "skipped")


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------
# Specs and ordering
# ---------------------------------------------------------------------------

@dataclass
class Sandbox:
    path: Path
    name: str
    block: str
    channel: str
    effort: str
    arm: str
    kind: str | None
    group: int = 0
    state: str = "pending"
    attempts: int = 0
    started: str | None = None
    ended: str | None = None
    exit_code: int | None = None
    duration_s: float | None = None
    note: str | None = None
    metrics: dict[str, Any] = field(default_factory=dict)


def read_spec(path: Path) -> Sandbox:
    data = yaml.safe_load(path.read_text()) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path}: sandbox spec must be a YAML mapping")
    name = str(data.get("sandbox") or path.stem)
    return Sandbox(
        path=path,
        name=name,
        block=str(data.get("block") or name.split("-", 1)[0]),
        channel=str(data.get("channel") or "?"),
        effort=str(data.get("reasoning_effort") or "?"),
        arm=str((data.get("assigned_state") or {}).get("arm") or "?"),
        kind=(str(data["kind"]) if data.get("kind") else None),
    )


def expand(patterns: list[str]) -> list[Path]:
    out: list[Path] = []
    for pat in patterns:
        hits = [Path(p) for p in sorted(globmod.glob(pat))]
        if not hits:
            p = Path(pat)
            if not p.exists():
                raise SystemExit(f"no spec matched {pat!r}")
            hits = [p]
        out.extend(hits)
    seen: set[Path] = set()
    uniq = []
    for p in out:
        if p not in seen:
            seen.add(p)
            uniq.append(p)
    return uniq


def block_sort_key(block: str) -> tuple[int, str]:
    """B1..B6 in numeric order; anything else after them, alphabetically."""
    if len(block) > 1 and block[0] in "Bb" and block[1:].isdigit():
        return (int(block[1:]), "")
    return (10_000, block)


def interleave(group: list[Sandbox]) -> list[Sandbox]:
    """Order the 16 files of a block so consecutive launches differ in effort and channel.

    Two reasons. A budget or quality stop mid-block then leaves a spread of cells
    rather than four channels of one arm. And `high` sandboxes take ~7x as long as
    `off` ones (pilot latency: ~12 s vs ~1.5 s per call), so mixing them keeps the
    block finishing together instead of all-off-then-all-high.
    """
    lanes: dict[tuple[str, str], list[Sandbox]] = {}
    for sb in group:
        lanes.setdefault((sb.effort, sb.arm), []).append(sb)
    # lane order alternates effort; the channel order inside a lane is rotated per
    # lane so the channel changes at every step too.
    efforts = sorted({e for e, _ in lanes})
    arms = sorted({a for _, a in lanes})
    lane_order = [(e, a) for a in arms for e in efforts]
    lane_order.sort(key=lambda k: (arms.index(k[1]), efforts.index(k[0])))
    ordered_lanes = []
    for i, key in enumerate(lane_order):
        members = sorted(lanes.get(key, []), key=lambda s: (s.channel, s.name))
        ordered_lanes.append(members[i % len(members):] + members[:i % len(members)]
                             if members else [])
    out: list[Sandbox] = []
    for i in range(max((len(l) for l in ordered_lanes), default=0)):
        for lane in ordered_lanes:
            if i < len(lane):
                out.append(lane[i])
    return out


NO_BLOCK_BARRIER = False  # --no-block-barrier: keep block order, but fill slots across blocks


def plan(sandboxes: list[Sandbox]) -> list[Sandbox]:
    """Calibration first if present, then blocks in order, interleaved within a block."""
    calib = [s for s in sandboxes if s.path.stem == CALIBRATION_STEM]
    rest = [s for s in sandboxes if s.path.stem != CALIBRATION_STEM]
    groups: dict[str, list[Sandbox]] = {}
    for sb in rest:
        groups.setdefault(sb.block, []).append(sb)

    ordered: list[Sandbox] = []
    gi = 0
    for sb in calib:
        sb.group = gi
        ordered.append(sb)
    if calib:
        gi += 1
    for block in sorted(groups, key=block_sort_key):
        for sb in interleave(groups[block]):
            sb.group = gi
            ordered.append(sb)
        if not NO_BLOCK_BARRIER:
            gi += 1
    return ordered


# ---------------------------------------------------------------------------
# Reading a finished sandbox
# ---------------------------------------------------------------------------

def move_usage(row: dict[str, Any]) -> list[Any]:
    """The per-completion usage of one move row, counted exactly once.

    A retried move keeps every attempt in `attempts`; its top-level `usage` is the
    final attempt only, so the two must never be added together (review §3).
    """
    attempts = row.get("attempts")
    if isinstance(attempts, list) and any(
        isinstance(a, dict) and a.get("usage") for a in attempts
    ):
        return [u for a in attempts if isinstance(a, dict) for u in (a.get("usage") or [])]
    return row.get("usage") or []


def tally_usage(out: dict[str, Any], usages: Any) -> None:
    """Add a list of per-completion usage dicts to the running cost.

    Only a finite, non-negative number is spent money. A string crashed the parent
    and a NaN silently disabled the `total > budget` comparison, so anything else
    is counted as an accounting failure and priced at $0 (review §5).
    """
    if not isinstance(usages, list):
        return
    for usage in usages:
        if not isinstance(usage, dict):
            continue
        out["usage_rows"] += 1
        cost = usage.get("estimated_cost")
        if (isinstance(cost, bool) or not isinstance(cost, (int, float))
                or not math.isfinite(cost) or cost < 0):
            out["usage_rows_without_cost"] += 1
        else:
            out["cost_usd"] += float(cost)


def scan_moves(path: Path) -> dict[str, Any]:
    """Cost and quality counters from one sandbox's moves.jsonl.

    `complete` is true when a `generation_end` row is present: that row is written
    last, so it is the only honest "this sandbox finished" marker.

    Fallbacks come from the `game_end` rows (`fallback_count` / `moves_logged`).
    Since 12 Sept (commit 02bbb40) the aborting move row IS logged (status "aborted");
    aborts are still counted from game_end rows because that is one row per LLM agent-game.
    """
    out = {"complete": False, "moves": 0, "games": 0, "game_end_rows": 0,
           "aborted": 0, "llm_decisions": 0, "fallbacks": 0, "cost_usd": 0.0,
           "bad_lines": 0, "usage_rows": 0, "usage_rows_without_cost": 0}
    if not path.is_file():
        return out
    seen: set[tuple] = set()
    aborted: set[tuple] = set()
    with path.open() as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                out["bad_lines"] += 1          # a torn last line after a kill
                continue
            kind = row.get("kind")
            if kind == "move":
                out["moves"] += 1
                tally_usage(out, move_usage(row))
            elif kind == "game_end":
                out["game_end_rows"] += 1
                key = (row.get("generation"), row.get("game"))
                seen.add(key)
                if row.get("status") == "aborted":
                    aborted.add(key)
                out["llm_decisions"] += int(row.get("moves_logged") or 0)
                out["fallbacks"] += int(row.get("fallback_count") or 0)
                tally_usage(out, row.get("question_usage"))
            elif kind == "generation_end":
                out["complete"] = True
    # One LLM-LLM game writes two game_end rows; the denominator the quality gate
    # is written against is unique games, not agent-games (review §12).
    out["games"] = len(seen)
    out["aborted"] = len(aborted)
    out["cost_usd"] = round(out["cost_usd"], 6)
    out["aborted_frac"] = (out["aborted"] / out["games"]) if out["games"] else 0.0
    out["fallback_frac"] = (
        (out["fallbacks"] / out["llm_decisions"]) if out["llm_decisions"] else 0.0
    )
    return out


def quality_verdict(m: dict[str, Any]) -> str | None:
    if m.get("games") and m["aborted_frac"] > ABORT_LIMIT:
        return f"aborted {m['aborted_frac']:.1%} > {ABORT_LIMIT:.0%}"
    if m.get("llm_decisions") and m["fallback_frac"] > FALLBACK_LIMIT:
        return f"fallbacks {m['fallback_frac']:.1%} > {FALLBACK_LIMIT:.0%}"
    return None


# ---------------------------------------------------------------------------
# The orchestrator
# ---------------------------------------------------------------------------

class Orchestrator:
    def __init__(self, sandboxes: list[Sandbox], args: argparse.Namespace) -> None:
        self.sandboxes = sandboxes
        self.args = args
        self.out = Path(args.out_dir)
        self.status_path = self.out / STATUS_NAME
        self.progress_path = self.out / PROGRESS_NAME
        self.total_cost = 0.0
        self.completed_costs: list[float] = []
        self.consecutive_quality_fail = 0
        self.halt: dict[str, str] | None = None
        self.stopping = False
        self.running: dict[str, dict[str, Any]] = {}
        self.running_since: dict[str, float] = {}

    # ---------------- bookkeeping ----------------

    def progress(self, text: str) -> None:
        line = f"{now()}  {text}"
        self.out.mkdir(parents=True, exist_ok=True)
        with self.progress_path.open("a") as fh:
            fh.write(line + "\n")
        print(line, flush=True)

    def status_dict(self) -> dict[str, Any]:
        counts = {s: 0 for s in ("pending", "running", *TERMINAL)}
        for sb in self.sandboxes:
            counts[sb.state] = counts.get(sb.state, 0) + 1
        done_like = [sb for sb in self.sandboxes if sb.state in TERMINAL]
        totals = {
            "cost_usd": round(self.total_cost, 6),
            "moves": sum(sb.metrics.get("moves", 0) for sb in done_like),
            "games": sum(sb.metrics.get("games", 0) for sb in done_like),
            "aborted": sum(sb.metrics.get("aborted", 0) for sb in done_like),
            "llm_decisions": sum(sb.metrics.get("llm_decisions", 0) for sb in done_like),
            "fallbacks": sum(sb.metrics.get("fallbacks", 0) for sb in done_like),
            "usage_rows_without_cost": sum(
                sb.metrics.get("usage_rows_without_cost", 0) or 0 for sb in done_like
            ),
            "sandboxes": counts,
        }
        n_done = len(self.completed_costs)
        mean = (sum(self.completed_costs) / n_done) if n_done else None
        remaining = counts["pending"] + counts["running"]
        return {
            "updated": now(),
            "out_dir": str(self.out),
            "budget_usd": self.args.budget_usd,
            "parallel": self.args.parallel,
            "per_sandbox_concurrency": self.args.per_sandbox_concurrency,
            "max_tokens": self.args.max_tokens,
            "halted": self.halt,
            "totals": totals,
            "projection": {
                "mean_duration_s_by_effort": {k: round(v, 1)
                                              for k, v in self.mean_duration().items()},
                "completed": n_done,
                "mean_cost_usd": round(mean, 6) if mean is not None else None,
                "remaining": remaining,
                "projected_total_usd": (
                    round(self.total_cost + mean * remaining, 4) if mean is not None else None
                ),
            },
            "sandboxes": {
                sb.name: {
                    "block": sb.block, "spec": str(sb.path), "state": sb.state,
                    "channel": sb.channel, "effort": sb.effort, "arm": sb.arm,
                    "attempts": sb.attempts, "started": sb.started, "ended": sb.ended,
                    "exit_code": sb.exit_code, "note": sb.note,
                    "duration_s": (round(sb.duration_s, 1) if sb.duration_s else None),
                    **{k: sb.metrics.get(k) for k in
                       ("moves", "games", "aborted", "aborted_frac", "llm_decisions",
                        "fallbacks", "fallback_frac", "cost_usd")},
                }
                for sb in self.sandboxes
            },
        }

    def write_status(self) -> None:
        self.out.mkdir(parents=True, exist_ok=True)
        tmp = self.status_path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(self.status_dict(), indent=2) + "\n")
        os.replace(tmp, self.status_path)          # atomic on POSIX

    def check_previous_status(self) -> None:
        """Warn about a STATUS.json written for a different spec list.

        The running cost is not read from it: it is rebuilt from the moves.jsonl of
        every sandbox this run skips or completes, so a resume cannot re-spend the
        budget and cannot inherit a stale number either.
        """
        if not self.status_path.is_file():
            return
        try:
            prev = json.loads(self.status_path.read_text())
        except (json.JSONDecodeError, OSError):
            return
        names = {sb.name for sb in self.sandboxes}
        stale = [n for n in (prev.get("sandboxes") or {}) if n not in names]
        if stale:
            self.progress(f"note     STATUS.json carries {len(stale)} sandbox(es) not in this "
                          f"run's spec list; their cost is not re-counted")

    # ---------------- launching ----------------

    def sandbox_dir(self, sb: Sandbox) -> Path:
        return self.out / sb.name

    def command(self, sb: Sandbox) -> list[str]:
        cmd = [
            sys.executable, "-m", "coop.cli", "run-population",
            "--config", str(sb.path),
            "--out-dir", str(self.out),
        ]
        # Only passed when asked for: the v2 YAMLs carry concurrency and output_cap,
        # and output_cap overrides --max-tokens anyway.
        if self.args.per_sandbox_concurrency is not None:
            cmd += ["--concurrency", str(self.args.per_sandbox_concurrency)]
        if self.args.max_tokens is not None:
            cmd += ["--max-tokens", str(self.args.max_tokens)]
        return cmd + list(self.args.runner_arg or [])

    def preflight(self, sb: Sandbox) -> str | None:
        """Decide skip / partial-cleanup before launching. Returns a note, or None."""
        d = self.sandbox_dir(sb)
        moves = d / "moves.jsonl"
        if not moves.exists():
            return None
        m = scan_moves(moves)
        if m["complete"]:
            sb.metrics = m
            sb.state = "skipped"
            sb.ended = now()
            self.account(sb, m)
            self.progress(f"skip     {sb.name}  (generation_end present; "
                          f"cost ${m['cost_usd']:.4f})")
            return "resume: already complete"
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        moved = d.with_name(f"{d.name}.partial-{stamp}")
        d.rename(moved)
        self.progress(f"partial  {sb.name}  moved to {moved.name} and restarted "
                      f"(the runner refuses a used run directory)")
        return f"partial run moved to {moved.name}"

    def launch(self, sb: Sandbox) -> None:
        d = self.sandbox_dir(sb)
        d.mkdir(parents=True, exist_ok=True)
        log = (d / LOG_NAME).open("a")
        log.write(f"\n=== attempt {sb.attempts + 1} {now()} ===\n"
                  f"$ {' '.join(self.command(sb))}\n")
        log.flush()
        proc = subprocess.Popen(
            self.command(sb), stdout=log, stderr=subprocess.STDOUT,
            cwd=str(Path(__file__).resolve().parent),
            start_new_session=True,        # Ctrl-C reaches us, not the children
        )
        sb.attempts += 1
        sb.state = "running"
        sb.started = sb.started or now()
        self.running[sb.name] = {"proc": proc, "log": log, "sb": sb}
        self.running_since[sb.name] = time.time()
        self.progress(f"start    {sb.name}  block {sb.block}  attempt {sb.attempts}  "
                      f"pid {proc.pid}")

    def account(self, sb: Sandbox, m: dict[str, Any]) -> None:
        self.total_cost += m.get("cost_usd", 0.0)

    def finish(self, sb: Sandbox, code: int) -> None:
        m = scan_moves(self.sandbox_dir(sb) / "moves.jsonl")
        sb.metrics = m
        sb.exit_code = code
        sb.ended = now()
        started = self.running_since.pop(sb.name, None)
        if started is not None:
            sb.duration_s = time.time() - started

        if not m["complete"]:            # generation_end is the only finish marker
            if sb.attempts < 2 and not self.stopping and self.halt is None:
                self.progress(f"retry    {sb.name}  exit {code}; one retry")
                sb.state = "pending"
                sb.note = f"attempt {sb.attempts} exited {code}"
                self.write_status()
                return
            sb.state = "failed"
            sb.note = f"exit {code} after {sb.attempts} attempt(s)"
            self.account(sb, m)
            self.progress(f"FAILED   {sb.name}  exit {code} after {sb.attempts} attempt(s) "
                          f"(see {sb.name}/{LOG_NAME})")
            self.write_status()
            return

        self.account(sb, m)
        self.completed_costs.append(m["cost_usd"])
        bad = quality_verdict(m)
        if bad:
            sb.state = "quality_fail"
            sb.note = bad
            self.consecutive_quality_fail += 1
        else:
            sb.state = "done"
            self.consecutive_quality_fail = 0

        self.progress(
            f"{'QUALFAIL' if bad else 'done    '} {sb.name}  games {m['games']} "
            f"aborted {m['aborted_frac']:.1%}  fallbacks {m['fallback_frac']:.1%}  "
            f"cost ${m['cost_usd']:.4f}" + (f"  [{bad}]" if bad else "")
        )
        n = len(self.completed_costs)
        mean = sum(self.completed_costs) / n
        remaining = sum(1 for s in self.sandboxes if s.state in ("pending", "running"))
        self.progress(
            f"budget   total ${self.total_cost:.4f} of ${self.args.budget_usd:.2f}  "
            f"mean ${mean:.4f} x {remaining} remaining = "
            f"projected ${self.total_cost + mean * remaining:.2f}"
        )

        self.progress(self.eta_line(sb.group))

        if bad and self.consecutive_quality_fail >= CONSECUTIVE_LIMIT:
            self.set_halt("quality", f"{CONSECUTIVE_LIMIT} consecutive quality_fail "
                                     f"sandboxes; last: {sb.name} ({bad})")
        elif self.total_cost > self.args.budget_usd:
            self.set_halt("budget", f"spent ${self.total_cost:.4f} > budget "
                                    f"${self.args.budget_usd:.2f}")
        self.write_status()

    def mean_duration(self) -> dict[str, float]:
        """Mean wall-clock per sandbox, per effort arm, from the ones that finished."""
        by: dict[str, list[float]] = {}
        for sb in self.sandboxes:
            if sb.duration_s and sb.state in ("done", "quality_fail"):
                by.setdefault(sb.effort, []).append(sb.duration_s)
        return {e: sum(v) / len(v) for e, v in by.items()}

    def eta_line(self, group: int) -> str:
        """Projected wall-clock for the rest of this block, measured not assumed."""
        means = self.mean_duration()
        left = [sb for sb in self.sandboxes
                if sb.group == group and sb.state in ("pending", "running")]
        if not left:
            return f"eta      block group {group} complete"
        known = [means[sb.effort] for sb in left if sb.effort in means]
        unknown = len(left) - len(known)
        seconds = sum(known) / max(1, self.args.parallel)
        parts = "  ".join(f"{e} mean {means[e] / 60:.0f} min" for e in sorted(means))
        return (f"eta      block group {group}: {len(left)} sandbox(es) left "
                f"({unknown} with no measured arm yet) -> ~{seconds / 3600:.1f} h "
                f"at parallel {self.args.parallel}   [{parts}]")

    def set_halt(self, reason: str, detail: str) -> None:
        if self.halt is None:
            self.halt = {"reason": reason, "detail": detail, "at": now()}
            self.stopping = True
            self.progress(f"HALT     {reason}: {detail} — launching no further sandboxes")

    # ---------------- the loop ----------------

    def run(self) -> int:
        self.out.mkdir(parents=True, exist_ok=True)
        self.check_previous_status()
        forwarded = " ".join(self.command(self.sandboxes[0])[7:]) or "(none)"
        self.progress(f"launch   {len(self.sandboxes)} sandbox(es), parallel "
                      f"{self.args.parallel}, budget ${self.args.budget_usd:.2f}, "
                      f"out-dir {self.out}, extra runner flags: {forwarded}")
        install_signal_handlers(self)
        self.write_status()

        group = 0
        n_groups = max((sb.group for sb in self.sandboxes), default=-1) + 1
        while True:
            # advance past finished groups, launch what the current group allows
            while group < n_groups:
                todo = [s for s in self.sandboxes
                        if s.group == group and s.state == "pending"]
                busy = [s for s in self.sandboxes
                        if s.group == group and s.state == "running"]
                if not todo and not busy:
                    group += 1
                    continue
                if self.stopping or len(self.running) >= self.args.parallel or not todo:
                    break
                if self.total_cost > self.args.budget_usd:
                    self.set_halt("budget", f"spent ${self.total_cost:.4f} > budget "
                                            f"${self.args.budget_usd:.2f}")
                    break
                sb = todo[0]
                if sb.kind and sb.kind != "population_sandbox":
                    sb.state = "failed"
                    sb.note = f"kind={sb.kind!r} has no driver in this repo"
                    sb.ended = now()
                    self.progress(f"FAILED   {sb.name}  {sb.note}")
                    if sb.path.stem == CALIBRATION_STEM:
                        self.set_halt("calibration",
                                      f"{sb.name} could not run: {sb.note}")
                    self.write_status()
                    continue
                note = self.preflight(sb)
                if sb.state == "skipped":
                    self.write_status()
                    continue
                sb.note = note
                self.launch(sb)
                self.write_status()

            if not self.running:
                if self.stopping or group >= n_groups:
                    break
                continue

            time.sleep(0.2)
            for name, item in list(self.running.items()):
                proc = item["proc"]
                code = proc.poll()
                if code is None:
                    continue
                item["log"].close()
                del self.running[name]
                self.finish(item["sb"], code)

        self.write_status()
        return self.exit_code()

    def exit_code(self) -> int:
        if self.halt:
            return 4
        if any(sb.state == "failed" for sb in self.sandboxes):
            return 1
        if any(sb.state == "quality_fail" for sb in self.sandboxes):
            return 3
        if any(sb.state == "pending" for sb in self.sandboxes):
            return 2                    # stopped by a signal with work left
        return 0

    # ---------------- signals ----------------

    def on_signal(self, signum: int, _frame: Any) -> None:
        name = signal.Signals(signum).name
        if self.stopping and self.args.hard:
            return
        self.stopping = True
        if self.halt is None:
            self.halt = {"reason": "signal", "detail": f"{name} received", "at": now()}
        if self.args.hard:
            for item in self.running.values():
                try:
                    os.killpg(os.getpgid(item["proc"].pid), signal.SIGTERM)
                except (ProcessLookupError, PermissionError):
                    pass
            self.progress(f"STOP     {name}: killed {len(self.running)} running sandbox(es) "
                          f"(--hard)")
        else:
            self.progress(f"STOP     {name}: launching no new sandboxes; "
                          f"{len(self.running)} running sandbox(es) will finish")
        self.write_status()


def install_signal_handlers(orc: Orchestrator) -> None:
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            signal.signal(sig, orc.on_signal)
        except ValueError:               # not the main thread (tests)
            pass


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def print_status(out_dir: Path) -> int:
    path = out_dir / STATUS_NAME
    if not path.is_file():
        print(f"no {path}", file=sys.stderr)
        return 1
    st = json.loads(path.read_text())
    rows = st.get("sandboxes", {})
    width = max([len(n) for n in rows] + [7])
    print(f"{'sandbox'.ljust(width)}  {'state':<12} {'games':>5} {'abort':>6} "
          f"{'fallbk':>6} {'cost$':>8}  note")
    for name, r in sorted(rows.items(), key=lambda kv: (kv[1].get("block") or "",
                                                        kv[0])):
        af = r.get("aborted_frac")
        ff = r.get("fallback_frac")
        print(f"{name.ljust(width)}  {r.get('state',''):<12} "
              f"{r.get('games') or 0:>5} "
              f"{(f'{af:.1%}' if af is not None else '-'):>6} "
              f"{(f'{ff:.1%}' if ff is not None else '-'):>6} "
              f"{(r.get('cost_usd') or 0.0):>8.4f}  {r.get('note') or ''}")
    t, p = st.get("totals", {}), st.get("projection", {})
    print()
    print(f"states     {t.get('sandboxes')}")
    print(f"totals     moves {t.get('moves')}  games {t.get('games')}  "
          f"aborted {t.get('aborted')}  fallbacks {t.get('fallbacks')}  "
          f"cost ${t.get('cost_usd', 0):.4f} of ${st.get('budget_usd')}  "
          f"unpriced usage rows {t.get('usage_rows_without_cost', 0)}")
    print(f"projection {p.get('completed')} done, mean ${p.get('mean_cost_usd')}, "
          f"{p.get('remaining')} left -> ${p.get('projected_total_usd')}")
    if st.get("halted"):
        print(f"HALTED     {st['halted']['reason']}: {st['halted']['detail']} "
              f"at {st['halted']['at']}")
    print(f"updated    {st.get('updated')}")
    return 0


def print_dry_run(orc: Orchestrator) -> int:
    a = orc.args
    print(f"out-dir            {orc.out}")
    print(f"parallel           {a.parallel} sandboxes at once")
    print("per-sandbox        " + (
        "concurrency and max_tokens come from the YAML (not overridden)"
        if a.per_sandbox_concurrency is None and a.max_tokens is None else
        f"--concurrency {a.per_sandbox_concurrency}  --max-tokens {a.max_tokens}"))
    print(f"budget             ${a.budget_usd:.2f}   "
          f"quality gates: aborted>{ABORT_LIMIT:.0%} or fallback>{FALLBACK_LIMIT:.0%}, "
          f"{CONSECUTIVE_LIMIT} in a row halts")
    print(f"sandboxes          {len(orc.sandboxes)}")
    blocks: dict[str, int] = {}
    for sb in orc.sandboxes:
        blocks[sb.block] = blocks.get(sb.block, 0) + 1
    print("blocks             " + "  ".join(f"{b}={n}" for b, n in blocks.items()))
    print()
    print(f"{'#':>3}  {'grp':>3}  {'sandbox':<28} {'block':<6} {'channel':<10} "
          f"{'effort':<5} {'arm':<7} status")
    for i, sb in enumerate(orc.sandboxes, 1):
        m = scan_moves(orc.sandbox_dir(sb) / "moves.jsonl")
        if sb.kind and sb.kind != "population_sandbox":
            state = f"UNSUPPORTED kind={sb.kind}"
        elif m["complete"]:
            state = f"skip (complete, ${m['cost_usd']:.4f})"
        elif m["moves"]:
            state = "restart (partial run moved aside)"
        else:
            state = "run"
        print(f"{i:>3}  {sb.group:>3}  {sb.name:<28} {sb.block:<6} {sb.channel:<10} "
              f"{sb.effort:<5} {sb.arm:<7} {state}")
    print()
    print("first command:")
    print("  " + " ".join(orc.command(orc.sandboxes[0])))
    return 0


# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    global ABORT_LIMIT
    ap = argparse.ArgumentParser(
        prog="orchestrate.py",
        description="Run the v2 sandbox blocks overnight: N at a time, block by block, "
                    "with a budget guard, a quality guard and a resumable STATUS.json.",
    )
    ap.add_argument("specs", nargs="*", help="sandbox YAML paths or globs")
    ap.add_argument("--parallel", type=int, default=12,
                    help="sandboxes running at once (default 12: 12 x the YAML's "
                         "concurrency 8 = 96 calls in flight, inside DeepInfra's 200)")
    ap.add_argument("--per-sandbox-concurrency", type=int, default=None,
                    help="forwarded as --concurrency. Default: not passed — the v2 YAMLs "
                         "set concurrency: 8 themselves")
    ap.add_argument("--max-tokens", type=int, default=None,
                    help="forwarded as --max-tokens. Default: not passed. A spec with an "
                         "output_cap block overrides it anyway (coop/population.py "
                         "_apply_v2_keys), which is every v2 B*.yaml")
    ap.add_argument("--runner-arg", action="append", default=[], metavar="FLAG",
                    help="extra flag forwarded verbatim to run-population, repeatable "
                         "(argparse needs the equals sign: --runner-arg=--no-questions)")
    ap.add_argument("--out-dir", default="runs/v2")
    ap.add_argument("--abort-limit", type=float, default=ABORT_LIMIT,
                    help="quality gate: a sandbox with more than this fraction of aborted "
                         "games is quality_fail (default %(default)s). Raise it only when "
                         "the aborts are a known, logged parse effect, never for harness faults.")
    ap.add_argument("--budget-usd", type=float, default=90.0,
                    help="stop launching once logged estimated_cost exceeds this")
    ap.add_argument("--no-block-barrier", action="store_true",
                    help="fill free slots across blocks instead of finishing a block first; "
                         "launch order still follows blocks so a budget stop favours early ones")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the plan and the first command, launch nothing")
    ap.add_argument("--status", action="store_true",
                    help="print STATUS.json from --out-dir as a table and exit")
    ap.add_argument("--hard", action="store_true",
                    help="on SIGINT/SIGTERM, kill running sandboxes instead of "
                         "letting them finish")
    args = ap.parse_args(argv)
    ABORT_LIMIT = args.abort_limit
    global NO_BLOCK_BARRIER
    NO_BLOCK_BARRIER = bool(getattr(args, "no_block_barrier", False))
    args.parallel = max(1, args.parallel)
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.status:
        return print_status(Path(args.out_dir))
    if not args.specs:
        print("give at least one sandbox YAML (or --status)", file=sys.stderr)
        return 2
    sandboxes = plan([read_spec(p) for p in expand(args.specs)])
    orc = Orchestrator(sandboxes, args)
    if args.dry_run:
        return print_dry_run(orc)
    return orc.run()


if __name__ == "__main__":
    sys.exit(main())
