# Calibration gate — reasoning-effort dial on 30 frozen states

Model `deepseek-ai/DeepSeek-V4-Flash-0731` on deepinfra (fp8), 768 answer tokens in every arm, one decision per call, no population, no board writes.
Contract: `specs/sandboxes-v2/calibration-effort.yaml`. States: `specs/states/calibration-states.json`. Calls: `calls.csv`.

## Prompt identity

- States frozen: **30** (15 ahead, 15 behind).
- States whose rebuilt `prompt_sha256` equals the logged one: **30/30**.
- Calls sent on a hash-matched prompt: **180/180**.
- Candidates dropped during sampling: 0.
- Prompt-token counts still differ across levels none med 814, low med 796, high med 892, max med 905. The messages are byte-identical (that is what the hash proves); the endpoint renders a different chat template in thinking mode, so a few tokens of template, not of prompt, separate the arms.

## Per level

| level | reasoning budget | n | reasoning med | reasoning IQR | reasoning max | completion med | prompt med | latency med (ms) | finish_reason | trace in field | board-call | decoy-call | cooperate | parse-fail |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 0 | 60 | 0 | 0–0 | 0 | 2 | 814 | 1038 | stop=60 | 0.0% | 6.7% | 40.0% | 46.7% | 0.0% |
| low | 8192 | 30 | 464 | 295–628 | 3208 | 467 | 796 | 5758 | stop=30 | 100.0% | 0.0% | 0.0% | 40.0% | 0.0% |
| high | 12288 | 60 | 1188 | 598–2007 | 7570 | 1194 | 892 | 13768 | stop=60 | 100.0% | 0.0% | 8.3% | 33.3% | 0.0% |
| max | 12288 | 30 | 1173 | 510–2942 | 7441 | 1180 | 905 | 14352 | stop=30 | 100.0% | 0.0% | 20.0% | 26.7% | 0.0% |

Answer capacity is 768 tokens in every arm; the reasoning budget is reserved on top of it. `none` is sent as DeepInfra's `reasoning_effort: none`; `low`, `high` and `max` are sent verbatim.

## Adjacent-level separation (non-overlapping reasoning-token IQRs)

| pair | verdict | reasoning-token IQRs |
|---|---|---|
| none → low | SEPARATED | none 0–0 (med 0) vs low 295–628 (med 464) |
| low → high | OVERLAP (no separation) | low 295–628 (med 464) vs high 598–2007 (med 1188) |
| high → max | OVERLAP (no separation) | high 598–2007 (med 1188) vs max 510–2942 (med 1173) |

Non-adjacent pairs, for reference:

| pair | verdict | reasoning-token IQRs |
|---|---|---|
| none → high | SEPARATED | none 0–0 (med 0) vs high 598–2007 (med 1188) |
| none → max | SEPARATED | none 0–0 (med 0) vs max 510–2942 (med 1173) |
| low → max | OVERLAP (no separation) | low 295–628 (med 464) vs max 510–2942 (med 1173) |

`finish_reason == "length"` anywhere: **no** (the gate requires no truncation at equal answer capacity).

Two caveats on reading this table. `high` and `max` were given the SAME reasoning budget (12288), so their contrast is the effort field alone. `low` was given a smaller budget (8192), but no call at any level came close to it — the largest reasoning spend observed at `low` was 3208 tokens — so no level was capacity-bound and the budgets are not doing the separating.

## Verdict

- Level pairs that separate: none/low, none/high, none/max.
- Level pairs that do not: low/high, high/max, low/max.
- `max` accepted by the endpoint: **yes** (the spec recorded it as UNVERIFIED).

Levels that do not separate are one level with two names. Any block arithmetic that buys them as distinct doses has to be rewritten before launch: low/high, high/max did not separate on this run, and the design can only claim the contrasts in the first list.

The shape is clean: `none` separates from every on-level and no two on-levels separate from each other. On this model the dial is a switch, not a slope — which is the two-level none/high contrast the 96 block files already assume.

## Paired board use, none vs high (within state)

| | high: board call | high: no board call |
|---|---|---|
| **none: board call** | 0 | 4 |
| **none: no board call** | 0 | 26 |

Paired states: 30. A cell counts a state where *any* replicate at that level made a `notes_read` or `notes_post` call.

## Cost

180 calls, **$0.0393** at $0.06/M in and $0.18/M out.

## What this gate establishes, and what it does not

It establishes whether the `reasoning_effort` field is a real intervention on this endpoint and this model: the same 30 prompts — byte-identical, verified against the `prompt_sha256` the runner logged when each decision was actually played — are shown to draw different amounts of billed reasoning at different settings, with the answer budget held at 768 tokens in every arm so no difference can be an output-capacity artifact. It also settles which levels are worth buying: two levels that do not separate on billed tokens are one level with two names, and block arithmetic that rests on a graded dial has to be rewritten as the contrast that survives. It says nothing whatever about the game. These are single decisions replayed out of context: no opponent answers back, no board is written, no score accumulates, and a board call here is a call on a frozen snapshot rather than a move in a live sandbox. Cooperation and board-use rates in the table are diagnostics of prompt handling, not findings about how reasoning effort changes behaviour — that question needs the sandboxes, where effort is varied between arms and the decisions compound.

