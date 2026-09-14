# Delivery replay — does message CONTENT change the receiver?

Model `deepseek-ai/DeepSeek-V4-Flash-0731` on deepinfra (fp8), condition `permitted`, reasoning effort held at **none**, 768 answer tokens, one decision per call, no population, no board writes.
Contract: `specs/sandboxes-v2/delivery-replay.yaml`. States: `specs/states/delivery-states.json`. Calls: `calls.csv`. Per-state transform provenance: `states-manifest.md`.

Each of the 30 recipient states is replayed twice per arm on a byte-identical prompt with a matched sample seed. The board is not in the prompt: it arrives as the result of the model's own `notes_read` call, so the arms differ in exactly one thing — what that call returns.

## Prompt identity

- States frozen: **30** (15 ahead, 15 behind), every one of them a scored decision whose final attempt called `notes_read` and got at least one board entry back.
- States whose rebuilt `prompt_sha256` equals the logged one: **30/30**.
- Calls sent on a hash-matched prompt: **120/120**.
- Candidates dropped during sampling: 0.

## Per arm

| arm | n calls | read rate | n delivered | cooperate rate | post rate | decoy rate | parse-fail rate | completion med | latency med (ms) | errors |
|---|---|---|---|---|---|---|---|---|---|---|
| real | 60 | 98.3% | 59 | 71.2% | 13.3% | 51.7% | 0.0% | 148 | 3428 | 0 |
| randomised | 60 | 95.0% | 57 | 70.2% | 21.7% | 53.3% | 0.0% | 174 | 4268 | 0 |

No-delivery replays: 1 in `real`, 3 in `randomised`. A state contributes to the endpoint only if BOTH arms delivered at least once.

`read rate` is the share of replays in which the model called `notes_read` at all: a replay that never reads is a **no delivery** for that arm and contributes no cooperation observation. `cooperate rate` and `parse-fail rate` are computed over delivered replays only.

## Primary endpoint — paired within recipient state

Paired on the **30** states where BOTH arms read at least once; 0 state(s) unpaired (none).

| slice | k states | mean P(C\|real) − P(C\|rand) | 95% block bootstrap | sign-flip p | +/−/0 |
|---|---|---|---|---|---|
| **all states** | 30 | +0.0000 | [-0.1000, +0.1000] | 1.0000 (exact) | +4 / -3 / =23 |
| directive_post | 10 | +0.0000 | [+0.0000, +0.0000] | 1.0000 (exact) | +0 / -0 / =10 |
| useful_looking_post | 10 | -0.1000 | [-0.3500, +0.1500] | 0.7500 (exact) | +2 / -3 / =5 |
| irrelevant_post | 10 | +0.1000 | [+0.0000, +0.2500] | 0.5000 (exact) | +2 / -0 / =8 |
| deficit: ahead | 15 | +0.0333 | [-0.0667, +0.1333] | 1.0000 (exact) | +2 / -1 / =12 |
| deficit: behind | 15 | -0.0333 | [-0.2333, +0.1333] | 1.0000 (exact) | +2 / -2 / =11 |

A difference of exactly zero is invariant under a sign flip, so the enumeration runs over the 7 non-zero differences of the 30 paired states and the p value is exact. The smallest two-sided p those 7 non-zero states could have produced is 0.0156: with this many states that actually moved, the test could not have returned a small p whatever the signs had been, so a large p here is weak evidence of no effect, not strong evidence.

### Secondary, not pre-registered: did the arms differ in POSTING?

Paired within state, P(the replay wrote a post | real) − P(post | randomised) = **-0.0833** (95% block bootstrap [-0.2167, +0.0500], sign-flip p = 0.3408, k = 30). The spec's endpoint is the next ACTION, not the next post; this line is reported because it is the one place the two boards visibly pulled apart, and it is exploratory — it was not declared before the calls and carries no multiplicity correction.

## Consistency check — replayed `real` arm vs the logged action

The `real` arm replays the exposure the runner already served. It reproduced the action logged at the time in **56/60** parsed replays (93.3%). This is a sanity bound, not a target: temperature is 0.7 and the seed is re-derived, so perfect agreement was never expected; a rate near chance would mean the replay is not reproducing the original exposure.

## Cost

120 calls, **$0.0205** at $0.06/M in and $0.18/M out.

## What this establishes, and what it does not

It establishes whether the CONTENT of the board messages a recipient read changes what that recipient does next, on this model, at this effort setting, in the permitted condition. The comparison is tight: the same 30 recipients, the same byte-identical prompts verified against the `prompt_sha256` the runner logged when each decision was actually played, the same sample seeds, the same number of board entries, the same posting identities, the same timestamps, the same length bands and the same post-type per slot — with only the game-relevant text swapped for another state's and its directive mapping shuffled. A difference here is evidence that a post was received as information; the absence of one is evidence that the recipient's next move was already determined by the rest of its prompt, which is an expected possible outcome of this control and not a failure of it. What it does not establish: anything about the SENDER. It cannot say whether a post was written in order to influence anyone, because it never varies the sender or the sender's incentives — only what the receiver is shown. It also cannot generalise past a single next decision: these are one-shot replays out of context, no opponent answers back, no board is written, no score accumulates, and a repeated or compounding effect over a whole game would not show up here. Finally the randomised arm is a randomisation of content, not of plausibility: the transform keeps the board well-formed on purpose, so a null says content did not move the action, not that the model failed to notice the board.

