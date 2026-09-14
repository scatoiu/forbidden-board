# RUNBOOK — the v2 block night

`orchestrate.py` runs one sandbox YAML per subprocess, `--parallel` at a time, blocks in
order (all 16 of B1 before any of B2), with a budget guard, a quality guard, a resumable
`STATUS.json` and one line per event in `PROGRESS.log`. Run everything from
`project/tournament` with `.venv/bin/python`. **Do not pass `--concurrency` or
`--max-tokens`**: the v2 YAMLs set `concurrency: 8` and an `output_cap`, and `output_cap`
overrides a CLI `--max-tokens` anyway (`coop/population.py::_apply_v2_keys`).

## (a) Calibration gate — before anything is bought

`specs/sandboxes-v2/calibration-effort.yaml` is `kind: fixed_state_replay` and **has no
driver in this repo**; `run-population` refuses it and `orchestrate.py` halts the night if
it is passed in. Until that driver exists, gate on one cheap pair of real sandboxes:

```bash
.venv/bin/python orchestrate.py specs/sandboxes-v2/B1-forbidden-off-behind.yaml \
    specs/sandboxes-v2/B1-forbidden-high-behind.yaml --out-dir runs/v2-gate --parallel 2
.venv/bin/python - runs/v2-gate <<'PY'
import json, statistics, sys, pathlib
for f in sorted(pathlib.Path(sys.argv[1]).glob("*/moves.jsonl")):
    t = [u["completion_tokens"] for r in map(json.loads, f.open()) if r["kind"] == "move"
         for u in (r.get("usage") or []) if u.get("completion_tokens")]
    if t:
        q = statistics.quantiles(t, n=4)
        print(f.parent.name, "n", len(t), "median", statistics.median(t),
              "IQR", round(q[0]), "-", round(q[2]))
PY
```

**Good:** the two medians separate with non-overlapping IQRs (pilot: 30 vs 1053 completion
tokens), no `finish_reason: length`, aborted 0 %, fallbacks 0 %.
**Abort:** medians overlap → effort is not an intervention, do not buy blocks. High-arm
median above ~1,400 tokens → drop to four blocks (README §2 sensitivity; resolution floor
becomes 2⁻³ = 0.125) before launching.

## (b) Launch the night

```bash
mkdir -p runs/v2
nohup .venv/bin/python orchestrate.py "specs/sandboxes-v2/B*.yaml" \
    --out-dir runs/v2 --parallel 12 --budget-usd 90 > runs/v2/nohup.log 2>&1 &
```

`--parallel 12` × the YAML's `concurrency: 8` = 96 calls in flight, inside DeepInfra's 200
per model. Pilot latency ~1.5 s (off) and ~12 s (high) per call, ~6,000 calls per sandbox
→ ~20 min per off sandbox, ~2.5 h per high one; a block is ~2.5–3 h and the six blocks
~16–18 h, so this is an overnight-plus run, not an eight-hour one. Dry-run first with
`--dry-run` to see the order and the exact command.

**Good:** `PROGRESS.log` shows `start` lines within seconds, then `done` lines with
`aborted 0.0%  fallbacks 0.0%`, and a `budget`/`eta` line after each.
**Abort:** the first `done` line reports aborted > 10 % or fallbacks > 5 % (the guard marks
it `quality_fail` itself); or the projected total exceeds the budget with blocks still
unstarted — stop and cut blocks rather than let a partial block spend.

## (c) Check status

```bash
.venv/bin/python orchestrate.py --status --out-dir runs/v2
tail -20 runs/v2/PROGRESS.log
tail -40 runs/v2/<sandbox>/orchestrator.log      # one sandbox's own stdout/stderr
```

**Good:** states are `done`/`running`/`pending` only; `projection` tracks below
`--budget-usd`; `usage_rows_without_cost` is 0 (a non-zero count means the endpoint stopped
pricing and the cost total is an undercount).
**Abort:** any `failed`, two `quality_fail` in a row (the guard halts), or `halted` set.

## (d) Resume after a crash

Re-run the **same** command as (b). A sandbox whose `moves.jsonl` has a `generation_end`
row is skipped and its cost is added back to the running total; a half-written sandbox is
moved to `<sandbox>.partial-<timestamp>` (the runner refuses a used run directory) and
restarted from scratch. Nothing is appended to an old log or an old board.

**Good:** `skip` lines for everything already finished, then `start` lines for the rest.
**Abort:** a sandbox that fails twice is marked `failed` — read its `orchestrator.log`
before relaunching; a repeated provider error means stop, not retry.

## (e) Stop

```bash
kill -TERM <pid>        # stop launching; running sandboxes finish (minutes to hours)
kill -INT  <pid>        # same
```

Add `--hard` at launch if a signal should kill running sandboxes instead (their partial
directories are then moved aside on the next resume). `STATUS.json` records
`halted.reason = "signal"`. Exit codes: 0 clean, 1 a sandbox failed, 2 stopped with work
left, 3 a quality_fail, 4 halted.

## (f) Analysis

```bash
.venv/bin/python -m analysis.run_all --runs runs/v2 --out reports/v2
```

**Good:** `reports/v2/SUMMARY.md` exists, `violations.csv` is empty, and the sandbox count
in the tables equals the `done` count in `STATUS.json`.
**Abort:** any sandbox in the tables that `STATUS.json` calls `failed` or `quality_fail` —
exclude it by name and say so in the paper, rather than averaging it in.

## Decide before launch

The v2 README cuts end-of-game questions from every confirmatory file, but the B\*.yaml
files do not encode that and the runner defaults them **on** (~210 extra calls per sandbox,
plus a post-treatment filter on the primary endpoint). To honour the design, launch with
`--runner-arg=--no-questions`.

## 13 Sept relaunch (after the 12 Sept abort)

What changed and why is in `notes/notes-astra-run-review.md`, `notes/notes-mimo-empty-content.md`
and the decision log (12 Sept 23:30 and 23:50 entries). Operating rules that follow from it:

- **A protocol change means a new output root.** Resume only compares the `generation_end`
  marker, not the config, so a changed cap, prompt or tool list must never be resumed into an
  old root. The 13 Sept run uses `runs/v3` and `runs/v3-mimo`; `runs/v2*` is diagnostic data only.
- `notes_read` returns the most recent 20 entries plus the total (`board_read_limit` in the
  manifest). `board_size_at_read` is the total.
- Health check: `.venv/bin/python healthcheck.py --runs runs/v3 --budget 90` prints one line;
  `ABORTS:<sandbox>` names the worst sandbox (unique games, ≥ 20 games, > 10%); `HALTED:<reason>`
  mirrors STATUS.json; exit code 2 whenever a flag is raised; `--json` for scripts. `naive_proj`
  is a straight mean and is NOT a forecast while high-effort sandboxes are unmeasured.
- Spend: `scan_moves` counts every attempt's usage and the end-of-game question calls;
  `unpriced usage rows` in `--status` must stay 0.
- Stopping: SIGTERM to the orchestrator stops launches only; the runners keep spending until
  they finish. To stop spend, then also `pkill -TERM -f 'coop.cli run-population'` (the
  orchestrator marks them failed; a fresh launch re-plans them). Never `pkill -f sandboxes-v2`:
  the orchestrator's own command line matches.
- Aborted decisions are on the record: the aborting move row (`status: aborted`, both attempts
  with `forced_turn` diagnostics) and any orphaned same-round reply (`status: unscored`) are
  logged with `executed: null`; analysis must exclude them from played-action statistics and
  include their attempted tool calls in the attempted-call endpoint.
- **Concurrency ceiling (learned 13 Sept 09:10):** DeepInfra rate-limits DeepSeek at ~200 concurrent
  requests per model. Keep (running sandboxes × per-sandbox concurrency) ≤ ~150 across ALL orchestrators
  on the same model; 29 runners × 8 produced ≈ 2,000 HTTP 429s in 15 minutes and aborted games with
  `provider_error` (two 429s on one move = one lost game). The 15-min health loop prints a
  `PROVIDER-ERRORS` line; ≥ 20 in 15 min means shed a run. Provider-error aborts are reported by
  cause in T8, never silently pooled with the model's own parse/truncation aborts.

## Final analysis (13 Sept 15:45 UK freeze) — the commands that produced the report

```bash
./freeze_and_final.sh          # inventory + hashes -> reports/FREEZE-<stamp>-inventory.tsv, then:
.venv/bin/python -m analysis.run_all --runs runs/v3 runs/v3b runs/v3-mimo --repairs runs/v7-repair --replication runs/v4-a4096 --out reports/final-<stamp>
.venv/bin/python -m analysis.addons --runs runs/v3 runs/v3b runs/v3-mimo --repairs runs/v7-repair --exploratory runs/v6-low=low_arm --exploratory runs/v5-d30=deficit_d30 --out reports/final-<stamp>-addons
```
Roots: `--runs` is the pre-registered dataset only (the guard refuses any other root name); `--repairs` merges per-game re-plays under the original sandbox identity; `--replication` and `--exploratory` are labelled and never pooled. Every report carries `PROVENANCE.json` (git sha, argv, per-sandbox manifest and moves.jsonl hashes); the add-on pass re-hashes its inputs against the freeze inventory and refuses on any mismatch. The frozen report is `reports/final-20260913T144509Z/`; nothing under `runs/` changes after the freeze.
