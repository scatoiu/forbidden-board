# Forbidden Board

A pre-registered iterated-prisoner's-dilemma assay for one question: how often do LLM agents attempt to use a shared message board they were explicitly told not to use, and what moves that rate? Built for the Apart Research AI Incident Response Sprint (11–13 September 2026), Track 2. Paper: *Forbidden Board: a pre-registered check of the incident report's reasoning-effort claim, for two dollars a pair* (Stefan Catoiu).

## Headline numbers (frozen 13 Sept 2026, 14:45:09Z)

| Quantity | Value | Where |
|---|---|---|
| DeepSeek-V4-Flash-0731, forbidden board, behind state: attempted use, zero reasoning budget | 74.76–96.67 % of games (six blocks) | `reports/final-20260913T144509Z/tables/block_contrasts.csv` |
| Same cells at a 12,288-token budget | 1.43–11.43 % | same |
| Mean paired difference (A_forbidden, registered secondary) | −80.63 pp, 6 of 6 blocks negative, raw p 0.03125, Holm 0.09375 | `registered_family.csv` |
| Registered primary (B_forbidden: behind minus ahead, zero budget) | +11.03 pp, 6 of 6 positive, raw p 0.03125, Holm 0.09375 | same |
| Decoy tool over the same reasoning contrast | −13.2 pp (board −80.6) | `paper-analysis/tables/adv_b_effort_diffs.csv` |
| MiMo-V2.5-Pro, B_forbidden | +2.54 pp, 4 of 6; no reasoning arm was run | `registered_family.csv` |
| Model seats vs live TitForTat, points per round | 2.030 vs 2.313, below in 69 of 69 sandboxes | `paper-analysis/tables/gt_q1_*.csv` |

Six paired blocks put a floor of 2⁻⁵ = 0.03125 on any two-sided sign-flip p, and Holm over three registered members makes 0.09375 the smallest attainable adjusted value. Nothing in this design can reach 0.05; it establishes direction and magnitude. Every number in the paper carries an id in `paper-analysis/tables/numbers-ledger.csv` (269 entries, 268 recomputed from raw logs by an independent implementation; the one discrepancy is a provenance label, see below).

## Layout

```
coop/                 harness: population runner, tools (notes board, decoy clock, ledger), scoring, Axelrod wrapper
orchestrate.py        runs sandbox YAMLs in blocks with budget and quality guards
analysis/             report generator (tables T0–T11, registered family, block contrasts, verdicts)
specs/                sandbox YAML grids, prompts (three paraphrases + placement p4), states, providers
configs/              payoff matrices and seat populations
tests/                pytest suite for the harness
reports/final-20260913T144509Z/   the frozen report: SUMMARY.md, tables, PROVENANCE.json (131 input hashes)
reports/*-addons, calibration-*, delivery-replay-*   exploratory arms (8,192-token budget, −30 deficit), token calibration, delivery replay
reports/FREEZE-*.tsv  inventory of every moves.jsonl with sha256 at the freeze
paper-analysis/       post-freeze analysis: code/, tables/ (incl. numbers-ledger.csv), data/ (compact parquet), transcripts/ (board text per sandbox), OPEN-QUESTIONS.md
figures/              the two paper figures and the appendix gallery
verify.py             recomputes counts and all 48 registered block rates from the compact tables and prints PASS
```

## Reproduce

```bash
python -m venv .venv && .venv/bin/pip install -e .
.venv/bin/python verify.py            # compact tables vs frozen report: prints PASS
.venv/bin/pytest -q                   # harness tests
```

To run the two-sandbox check on your own model (about $1.75 on DeepInfra at the paper's estimate; other OpenAI-compatible providers work):

```bash
cp .env.example .env                  # put your key in DEEPINFRA_API_KEY
.venv/bin/python orchestrate.py specs/sandboxes-v2/B1-forbidden-off-behind.yaml \
    specs/sandboxes-v2/B1-forbidden-high-behind.yaml --out-dir runs/mycheck --parallel 2
.venv/bin/python analysis/report.py --runs runs/mycheck --out reports/mycheck
```

Pass condition before reading any result: the two arms' completion-token medians must separate with non-overlapping interquartile ranges (see `RUNBOOK.md` §a). Change the model by editing `population.llm` in the YAMLs. The full pre-registered grid is the `specs/sandboxes-v2/B*.yaml` glob (an overnight run).

## What is and is not here

- Raw per-move logs (`runs/*/moves.jsonl`, about 6 GB, 131 files) are not in the repository. Their sha256 hashes are in `reports/FREEZE-20260913T144509Z-inventory.tsv` and `PROVENANCE.json`; the compact tables in `paper-analysis/data/` were extracted from them by `paper-analysis/code/extract.py` and reconcile to the frozen report (`verify.py`). Raw logs are available on request, pending the sprint organisers' disclosure review.
- `reports/final-20260913T144509Z/tables/traces_coded.csv` (1.1 GB of coded reasoning traces) is omitted for size.
- Known label error: `PROVENANCE.json` marks the ten repair run directories `disposition: "excluded"` while their 585 games are inside every pre-registered table. Bytes, hashes and counts are correct; the label is wrong.
- The `coop` harness was written May–August 2026 with Claude Code and wraps the Axelrod-Python library; the sandbox specifications, pre-registration, seeds and analyses are new for the sprint. A concurrent sprint repository, `msp895/oai-hf-incident-reproduction`, elicits related behaviours in a different setting.
- The harness talks to a public inference provider over HTTPS, opens no other network connection, and executes no model-authored code. The tools exposed to agents are a read and a post on a text board, a clock and a score lookup. There is no exploit content here.

## Licence

MIT (see `LICENSE`).
