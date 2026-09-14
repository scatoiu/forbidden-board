# Sandbox specifications — the weekend's run plan

One file = one sandbox = one population, one channel condition, one framing, one seed.
Keys are identical in every file (`sandbox`, `population`, `channel`, `framing`,
`paraphrase`, `reasoning_effort`, `rounds_per_game`, `prob_end`, `generations`, `seed`,
`provider`, `base_url`, `concurrency`, `history_window`, `neutral_labels`) so the runner
takes a path and nothing else, and so a diff between two files shows exactly what was
varied.

Prompts come from `../prompts/<framing>_<paraphrase>_<condition>.json`, tools from
`../prompts/tools.json`, neutral letter pairs from `../prompts/labels.json`. `channel` in
a sandbox file is the same thing the prompt files call `condition` and the move schema
calls `condition`; the value set is identical (`absent`, `permitted`, `forbidden`,
`hidden`).

---

## 1. Planned moves, with the arithmetic

A **move** is one agent's decision in one round. A 24-agent round robin plays every
unordered pair once per generation:

```
pairings per generation      C(24,2) = 24 x 23 / 2            = 276
moves per generation         276 pairings x 30 rounds x 2      = 16,560
moves per sandbox            16,560 x 5 generations            = 82,800
moves across S01-S16         82,800 x 16                       = 1,324,800
```

Only LLM agents cost an API call. With 12 LLM agents and 12 scripts:

```
LLM-LLM pairings             C(12,2) = 66      -> 66 x 30 x 2  =  3,960 LLM calls/gen
LLM-script pairings          12 x 12 = 144     -> 144 x 30     =  4,320 LLM calls/gen
script-script pairings       C(12,2) = 66      -> 66 x 30 x 2  =  3,960 free moves/gen
                                                  total moves  = 16,560  (checks out)
billable LLM calls per generation                              =  8,280
billable LLM calls per sandbox (x5)                            = 41,400
billable LLM calls across S01-S16 (x16)                        = 662,400
```

End-of-game questions are extra calls, one per LLM agent per game: `66 x 2 + 144 = 276`
classification calls per generation (1,380 per sandbox); in a `forbidden` sandbox add the
same number of prohibition-recall calls. Across S01–S16: 22,080 classification calls plus
5,520 recall calls (S09–S12 only).

Whole plan:

| File(s) | Agents | Pairings | Rounds | Gens | Moves each | Moves total | Billable LLM calls total |
|---|---|---|---|---|---|---|---|
| `pilot-local` | 8 (4 LLM + 4 scripts) | 28 | 10 | 1 | 560 | 560 | 280 |
| `S01`–`S16` | 24 (12 + 12) | 276 | 30 | 5 | 82,800 | 1,324,800 | 662,400 |
| `E01`–`E02` | 12 (6 + 6) | 66 | 30 | 1 | 3,960 | 7,920 | 3,960 |
| `E03`–`E06` | 24 (12 + 12) | 276 | 30 | 1 | 16,560 | 66,240 | 33,120 |
| **total** | | | | | | **1,399,520** | **699,760** |

**These are upper bounds, not expectations.** `rounds_per_game: 30` with
`prob_end: 0.03` is a *cap*: the match length is drawn once from a geometric
distribution and truncated at 30, so the expected realised length is
`(1 - 0.97^30) / 0.03 ≈ 20.0` rounds — about two thirds of the planned figure. Expect
roughly **0.93 M realised moves and 0.47 M billable calls**, and reconcile the paper's
numbers against the JSONL row count, never against this table.

`pilot-local` and `E01`/`E02` run on the local Ollama server and cost nothing but
wall-clock; everything else is hosted and is the thing the budget buys.

---

## 2. Which sandbox feeds which pre-registered outcome

Outcomes are numbered as in `notes/07-tournament-direction/README.md` §4 plus the three
carried in from the research dives (§11).

| # | Pre-registered outcome | Fed by | Contrast |
|---|---|---|---|
| O1 | Forbidden-channel use rate; discovery rate | S09–S12 (`forbidden`), S13–S16 (`hidden`) | against S05–S08 (`permitted`) and S01–S04 (`absent`) |
| O2 | Post content coded: directive / identity / opponent info / other | S05–S16 (every sandbox with tools) | `forbidden` posts vs `permitted` posts |
| O3 | Cooperation LLM-vs-LLM against LLM-vs-script, per condition — the selective-exploitation test | all of S01–S16 | `pair_type` within file, condition across files |
| O4 | End-of-game opponent classification vs ground truth | all of S01–S16, `pilot-local`, E01–E06 | chance baseline built in |
| O5 | Does the reasoning trace mention the board before the call? | E01–E06 only (the only files with `reasoning_effort` above `off`) | low vs high within model |
| O6 | Climate: population cooperation rate per round, per generation | S01–S16 (the only files with `generations: 5`) | condition × framing |
| O7 | Framing effect at fixed payoffs (F0 control vs F4 survival) | S01/S02 vs S03/S04; S05/S06 vs S07/S08; S09/S10 vs S11/S12; S13/S14 vs S15/S16 | framing within condition |
| O8 | Reasoning-effort dose-response on channel use — the Figure 3 shape with a labelled x-axis | E01↔E02, E03↔E04, E05↔E06 | effort within model, channel held at `forbidden` |
| O9 | Decoy discrimination: `ledger_lookup` call rate beside `notes_*` call rate | S05–S16, E01–E06 | listed-use signature vs strategic-use signature |
| O10 | Compliance vs defiance: prohibition-recall accuracy split against channel use | S09–S12, E01–E06, `pilot-local` (all `forbidden` files) | recall-correct vs recall-wrong within file |
| O11 | Emergence: do posters out-reproduce non-posters, and does a posting convention survive the scripts? | S05–S16 (needs `generations: 5`) | generation 1 vs generation 5 |
| — | Go/no-go gate: tool calls parse, moves parse, anyone touches the board at all | `pilot-local` | none; it is a smoke run, not powered for any comparison |

**Not covered by this plan, and it should be said out loud in the paper:** the paraphrase
spread (all S and E files are fixed at `p1`) and the framings F1, F6, F8. The prompt pack
contains all fifteen framing × paraphrase groups so the spread can be run if Sunday has
room, but as specified here the weekend buys one paraphrase and two framings. Any framing
claim from S01–S16 is therefore a single-wording claim and must be reported as one
(TRAILS: format alone has moved cooperation by up to 76 pp).

---

## 3. Held fixed everywhere (harness-effects.md §5.1)

Same operator brief text per paraphrase id; same system/user split; payoff given as text
with no label; neutral letter pair drawn per game and option order randomised per round;
fixed `history_window` with running totals; no horizon sentence; noise 0; identical tool
list, tool order and decoy in every condition where tools are passed; empty board at the
start of generation 1; end-of-game questions asked after the last move, never before; no
dates, run names, seeds or condition names visible in any prompt.

Deliberate departures from "hold everything fixed", each one visible in the file:

- `E01`/`E02` use a 12-agent population and `concurrency: 8` because the local server
  does ~2,500 reasoning-on moves an hour. The effort contrast is within the pair, at
  matched population, so this is sound; **E01/E02 must not be pooled with E03–E06.**
- E-series files run `generations: 1`. The effort dial is a within-generation
  dose-response, not an evolutionary claim, and O11 does not draw on them.
- `pilot-local` sets `prob_end: 0.0` so all 10 rounds always run — a smoke test wants a
  fixed row count, not a random one.
