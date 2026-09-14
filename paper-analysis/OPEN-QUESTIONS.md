# What the data cannot settle, what would settle it, and what a month adds

Written 13 Sept 2026 after the five analyses and the synthesis. Costs are DeepInfra fp8 prices observed in this run (≈ $0.4 per off-effort sandbox of 276 games, ≈ $1.9 per high-effort sandbox; see `project/tournament/RUNBOOK.md`).

## A. Cannot be settled with these data

| # | Question | Why the data cannot settle it | The run that would | Cost / time |
|---|---|---|---|---|
| 1 | Is the state effect a response to the score or to the displayed history of being exploited? | The assigned state is delivered as a six-round warm-up shown as the current counterpart's record plus a running score; the two never vary independently (SYNTHESIS D1). | A 2×2: {score −10, +10} × {history "they defected on you twice", "you defected on them twice"} realised by editing the state block text only, six blocks each, forbidden, off effort. 24 sandboxes. | ≈ $10, 3 h |
| 2 | Does a losing package raise use of the *forbidden* board specifically, or tool calling in general? | In DeepSeek the decoy rose at least as much as the board (01 §1); MiMo's decoy moved the other way; the design has one decoy. | Add a second decoy with a different affordance (e.g. a read-only log) and pre-register board-minus-decoy as the endpoint; six blocks per model. | ≈ $10, 3 h |
| 3 | Does the effort effect hold in a second model with a reasoning dial? | MiMo's high arm was never run (at floor and slow in the pilot); gpt-oss-120b and Qwen3.5 showed 0 → 0 in pilots (no use at either level). | MiMo forbidden-behind at high, six blocks; one further open-weight model with a verified dial. | ≈ $15 per model, overnight |
| 4 | Is the +11 pp state effect real under paraphrases 2 and 3, or a paraphrase-1 effect? | +20.5 / +11.7 / +1.0 pp across p1/p2/p3; p3 sits at ceiling (94–97 %), so it cannot express the effect. | Rewrite p3 so its off-effort base rate is ≈ 60–70 % (the p1 level), then rerun ahead/behind, six new blocks. | ≈ $5, 2 h |
| 5 | Does the primary contrast replicate in an independent rerun? | The 4096-cap replication has hidden and permitted cells only. | Rerun the twelve DeepSeek forbidden-off cells with fresh seeds. | ≈ $5, 2 h |
| 6 | Does payoff structure change any of this ("more punishing environments")? | Every sandbox used (3,0,5,1). | Rerun forbidden-off-behind under `brutal_world` (3,0,8,2) and `punishing_defection` (3,0,5,−1), six blocks each; the matrices already exist in `coop/tournament.py`. | ≈ $10, 3 h |
| 7 | Does a delivered post change a recipient's next action? | The delivery replay moved 7 of 30 states; smallest attainable p 0.0156; the within-tournament before/after comparisons run opposite ways in the two models (04 Q6). | 300 recipient states (not 30), real vs randomised content, at off and at high effort. | ≈ $3, 1 h |
| 8 | Would the LLMs beat TitForTat in a longer or noisier game? | 30-round cap, prob_end 0.03, no noise; Willis 2025 used 1000 rounds and 10 % noise. | 150-round matches with 5 % noise, 12 LLM seats, three seeds. | ≈ $25, overnight |
| 9 | Is the memory-one profile (DC → C only 30 %) stable across prompts and models? | One brief family; two models. | Rerun the standing analysis on the p4 cells (already on disk) and on one further model. | $0 for p4; ≈ $15 per model |
| 10 | Motive, intent, belief in the ledger | Not measurable here; traces give reasons after the fact and none cite the deficit as a reason to override the prohibition (04 Q4). | Not a run. A stated limit. | — |
| 11 | Generality beyond one provider and fp8 | Single serving stack. | Same specs on a second provider or bf16 weights, forbidden-off and high, B1–B2. | ≈ $10 |

## B. Can be settled from the existing logs (no new runs)

- Whether the exploratory game-level permutation in `SUMMARY.md` permutes sandbox labels or games (02 §11 vs 05 trap 4); read `analysis/tests_of_hypotheses.py`. Not needed for the paper (the numbers are omitted).
- Per-agent "personality" stability: whether the same agent id (A00…A23 within a sandbox) shows a consistent memory-one profile across its 23 games; `decisions.parquet` has everything.
- Whether the p4 placement effect (one sandbox per model) holds across the twelve LLM agents within that sandbox (a within-sandbox consistency check, not a replication).

## C. What a month of follow-up adds

Week 1: the 2×2 in A1 and the second decoy in A2. Together they decide whether the paper's registered primary contrast means anything about incentives. Week 2: MiMo at high and one more dialled model (A3), and the p3 rewrite (A4), which decides whether the effort effect is a DeepSeek fact or a reasoning-dial fact. Week 3: the payoff-matrix runs (A6) and the long noisy games (A8), which decide whether the cooperation profile is a property of these models or of this short game. Week 4: the 300-state delivery replay (A7) and a second provider (A11). Total ≈ $150 of API spend at these prices and one person's evenings. Deliverable: a pre-registered v2 of this assay with the confounds designed out, which is the artifact the paper's Track 2 sentence promises.
