#!/usr/bin/env python3
"""15-minute health check for an orchestrated run. Prints ONE line per call.

Usage: python healthcheck.py --runs runs/v2 [--json]

Flags STALL (running sandboxes but no file written in the window), ABORTS (a
sandbox with >=--min-games unique games whose abort rate exceeds --abort-limit),
BUDGET (the naive projection exceeds --budget), HALTED (STATUS.json records a
halt), SILENT (no STATUS.json) and ORCHESTRATOR_DOWN (STATUS says sandboxes are
running but no orchestrate.py process is pointed at this --runs directory).

Exits 2 when any flag is raised, so a shell loop can notice (review §17).
"""
import argparse
import glob
import json
import math
import os
import subprocess
import sys
import time

ap = argparse.ArgumentParser()
ap.add_argument('--runs', default='runs/v2')
ap.add_argument('--window', type=int, default=900)
ap.add_argument('--budget', type=float, default=90.0)
ap.add_argument('--abort-limit', type=float, default=0.10)
ap.add_argument('--min-games', type=int, default=20,
                help='a sandbox is only judged on aborts once it has this many games')
ap.add_argument('--json', action='store_true', help='dump the same fields as JSON')


def sandbox_dirs(runs):
    """Current sandbox directories only: `*.partial-*` is an archived attempt."""
    out = []
    for f in glob.glob(os.path.join(runs, '*', 'moves.jsonl')):
        if '.partial-' in os.path.basename(os.path.dirname(f)):
            continue
        out.append(f)
    return sorted(out)


def scan(path):
    """Typed counters from one moves.jsonl. Unique games, not agent-game rows."""
    games, aborted, cost, bad = set(), set(), 0.0, 0
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                bad += 1
                continue
            kind = row.get('kind')
            if kind in ('move', 'game_end'):
                # Same rule as orchestrate.move_usage: every attempt's usage when
                # attempts carry usage, else the top-level list; never both.
                if kind == 'move':
                    att = [a for a in (row.get('attempts') or []) if isinstance(a, dict)]
                    usages = ([u for a in att for u in (a.get('usage') or [])]
                              if any(a.get('usage') for a in att) else (row.get('usage') or []))
                else:
                    usages = row.get('question_usage') or []
                for u in usages:
                    if not isinstance(u, dict):
                        continue
                    c = u.get('estimated_cost')
                    if isinstance(c, bool) or not isinstance(c, (int, float)):
                        continue                      # a price, not a string
                    if math.isfinite(c) and c >= 0:
                        cost += c
            if kind == 'game_end':
                gk = (row.get('generation'), row.get('game'))
                games.add(gk)
                if row.get('status') == 'aborted':
                    aborted.add(gk)
    return {'games': len(games), 'aborted': len(aborted), 'cost': cost, 'bad_lines': bad}


def orchestrators_for(runs):
    """orchestrate.py processes whose command line names THIS runs directory."""
    try:
        # macOS pgrep has no -a; ps gives the full command line on both platforms.
        out = subprocess.run(['sh', '-c', "ps -axo command= | grep orchestrate.py | grep -v grep"],
                             capture_output=True, text=True).stdout
    except Exception:
        return -1
    wanted = {runs.rstrip('/'), os.path.abspath(runs).rstrip('/')}
    # Match the --out-dir token exactly: runs/v3 must not count runs/v3-mimo.
    def names_this_dir(ln):
        toks = ln.split()
        return any(toks[i] == '--out-dir' and toks[i + 1].rstrip('/') in wanted
                   for i in range(len(toks) - 1))
    return sum(1 for ln in out.splitlines() if names_this_dir(ln))


def main(argv=None):
    a = ap.parse_args(argv)
    now = time.time()
    flags = []

    st = {}
    sp = os.path.join(a.runs, 'STATUS.json')
    if os.path.exists(sp):
        try:
            st = json.load(open(sp))
        except Exception:
            flags.append('STATUS_UNREADABLE')
    else:
        flags.append('SILENT:no STATUS.json')

    sand = st.get('sandboxes') or st.get('items') or {}
    if isinstance(sand, list):
        sand = {s.get('sandbox', str(i)): s for i, s in enumerate(sand)}
    states = {}
    for s in sand.values():
        states[s.get('state', '?')] = states.get(s.get('state', '?'), 0) + 1
    running = states.get('running', 0)

    try:
        procs = int(subprocess.run(
            ['sh', '-c', "ps -axo command= | grep 'coop.cli run-population' | grep -v grep "
                         f"| grep -Ec -- '--out-dir {a.runs.rstrip('/')}( |$)'"],
            capture_output=True, text=True).stdout.strip() or 0)
    except Exception:
        procs = -1
    orch = orchestrators_for(a.runs)

    active_files = 0
    games = aborted = bad_lines = 0
    cost = 0.0
    per_sandbox = {}
    for f in sandbox_dirs(a.runs):
        name = os.path.basename(os.path.dirname(f))
        try:
            if now - os.path.getmtime(f) < a.window:
                active_files += 1
            m = scan(f)
        except Exception:
            flags.append(f'UNREADABLE:{name}')
            continue
        per_sandbox[name] = m
        games += m['games']
        aborted += m['aborted']
        cost += m['cost']
        bad_lines += m['bad_lines']

    # Per sandbox, not pooled: one bad arm hides inside a healthy aggregate.
    worst, worst_rate = None, 0.0
    for name, m in per_sandbox.items():
        if m['games'] < a.min_games:
            continue
        rate = m['aborted'] / m['games']
        if rate > worst_rate:
            worst, worst_rate = name, rate
    if worst and worst_rate > a.abort_limit:
        w = per_sandbox[worst]
        flags.append(f"ABORTS:{worst} {w['aborted']}/{w['games']}={worst_rate:.1%}")

    if running > 0 and procs > 0 and active_files == 0:   # only a live root can stall
        flags.append('STALL:no file written in window')

    done = states.get('done', 0)
    tot = len(sand)
    # Naive: all observed spend (including failed and running sandboxes) scaled by
    # the done count. Not a forecast; kept only as a coarse tripwire (review §17).
    naive_proj = (cost / done * tot) if done else None
    if naive_proj and naive_proj > a.budget:
        flags.append(f'BUDGET:naive_proj ${naive_proj:.0f}>${a.budget:.0f}')

    halted = st.get('halted')
    if halted:
        reason = halted.get('reason') if isinstance(halted, dict) else halted
        flags.append(f'HALTED:{reason}')
    if running > 0 and orch == 0:
        flags.append('ORCHESTRATOR_DOWN')

    fields = {
        'time': time.strftime('%H:%M'), 'runs': a.runs, 'states': states,
        'procs': procs, 'orch': orch, 'active_files': active_files,
        'games': games, 'aborted': aborted,
        'max_sandbox_abort': (f'{worst}={worst_rate:.1%}' if worst else 'n/a'),
        'cost_usd': round(cost, 4), 'naive_proj': (round(naive_proj, 2)
                                                   if naive_proj else None),
        'bad_lines': bad_lines, 'flags': flags,
    }
    if a.json:
        print(json.dumps(fields))
    else:
        print(f"HEALTH {fields['time']} states={states} procs={procs} orch={orch} "
              f"active_files={active_files} games={games} aborted={aborted} "
              f"max_sandbox_abort={fields['max_sandbox_abort']} cost=${cost:.2f} "
              f"naive_proj={('$%.0f' % naive_proj) if naive_proj else 'n/a'} "
              f"bad_lines={bad_lines} flags={flags or 'OK'}")
    return 2 if flags else 0


if __name__ == '__main__':
    sys.exit(main())
