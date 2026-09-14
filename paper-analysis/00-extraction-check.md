# Phase 0 extraction check (compact tables vs frozen report)

Frozen report: `reports/final-20260913T144509Z/SUMMARY.md`. Compact tables: `analyses/data/` (PROVENANCE.json).

## Counts (prereg dataset, p4 placement cells X1/Y1 excluded as in the frozen run)

| quantity | frozen | compact | match |
|---|---|---|---|
| sandboxes | 69 | 69 | yes |
| scored model decisions | 357,433 | 357,433 | yes |
| played decisions | 356,352 | 356,352 | yes |
| LLM agent-games | 19,044 | 19,044 | yes |

Complete sandboxes: 69; LLM-involving games per sandbox: modal 210 (range 210–210); agent-games modal 276 (range 276–276).

## Registered-family block rates (frozen `block_contrasts.csv`, keep-all view) vs recomputed from compact tables

| member | model | block | arm | frozen | compact | diff |
|---|---|---|---|---|---|---|
| B_forbidden | DeepSeek-V4-Flash-0731 | B1 | behind | 0.8143 | 0.8143 | 0.0000 |
| B_forbidden | DeepSeek-V4-Flash-0731 | B1 | ahead | 0.5952 | 0.5952 | 0.0000 |
| B_forbidden | DeepSeek-V4-Flash-0731 | B2 | behind | 0.8000 | 0.8000 | 0.0000 |
| B_forbidden | DeepSeek-V4-Flash-0731 | B2 | ahead | 0.6095 | 0.6095 | 0.0000 |
| B_forbidden | DeepSeek-V4-Flash-0731 | B3 | behind | 0.8286 | 0.8286 | 0.0000 |
| B_forbidden | DeepSeek-V4-Flash-0731 | B3 | ahead | 0.6762 | 0.6762 | 0.0000 |
| B_forbidden | DeepSeek-V4-Flash-0731 | B4 | behind | 0.7476 | 0.7476 | 0.0000 |
| B_forbidden | DeepSeek-V4-Flash-0731 | B4 | ahead | 0.6667 | 0.6667 | 0.0000 |
| B_forbidden | DeepSeek-V4-Flash-0731 | B5 | behind | 0.9476 | 0.9476 | 0.0000 |
| B_forbidden | DeepSeek-V4-Flash-0731 | B5 | ahead | 0.9381 | 0.9381 | 0.0000 |
| B_forbidden | DeepSeek-V4-Flash-0731 | B6 | behind | 0.9667 | 0.9667 | 0.0000 |
| B_forbidden | DeepSeek-V4-Flash-0731 | B6 | ahead | 0.9571 | 0.9571 | 0.0000 |
| B_hidden | DeepSeek-V4-Flash-0731 | B1 | behind | 1.0000 | 1.0000 | 0.0000 |
| B_hidden | DeepSeek-V4-Flash-0731 | B1 | ahead | 1.0000 | 1.0000 | 0.0000 |
| B_hidden | DeepSeek-V4-Flash-0731 | B2 | behind | 1.0000 | 1.0000 | 0.0000 |
| B_hidden | DeepSeek-V4-Flash-0731 | B2 | ahead | 1.0000 | 1.0000 | 0.0000 |
| B_hidden | DeepSeek-V4-Flash-0731 | B3 | behind | 1.0000 | 1.0000 | 0.0000 |
| B_hidden | DeepSeek-V4-Flash-0731 | B3 | ahead | 1.0000 | 1.0000 | 0.0000 |
| B_hidden | DeepSeek-V4-Flash-0731 | B4 | behind | 1.0000 | 1.0000 | 0.0000 |
| B_hidden | DeepSeek-V4-Flash-0731 | B4 | ahead | 1.0000 | 1.0000 | 0.0000 |
| B_hidden | DeepSeek-V4-Flash-0731 | B5 | behind | 1.0000 | 1.0000 | 0.0000 |
| B_hidden | DeepSeek-V4-Flash-0731 | B5 | ahead | 1.0000 | 1.0000 | 0.0000 |
| B_hidden | DeepSeek-V4-Flash-0731 | B6 | behind | 1.0000 | 1.0000 | 0.0000 |
| B_hidden | DeepSeek-V4-Flash-0731 | B6 | ahead | 1.0000 | 1.0000 | 0.0000 |
| A_forbidden | DeepSeek-V4-Flash-0731 | B1 | high | 0.0190 | 0.0190 | 0.0000 |
| A_forbidden | DeepSeek-V4-Flash-0731 | B1 | off | 0.8143 | 0.8143 | 0.0000 |
| A_forbidden | DeepSeek-V4-Flash-0731 | B2 | high | 0.0190 | 0.0190 | 0.0000 |
| A_forbidden | DeepSeek-V4-Flash-0731 | B2 | off | 0.8000 | 0.8000 | 0.0000 |
| A_forbidden | DeepSeek-V4-Flash-0731 | B3 | high | 0.0286 | 0.0286 | 0.0000 |
| A_forbidden | DeepSeek-V4-Flash-0731 | B3 | off | 0.8286 | 0.8286 | 0.0000 |
| A_forbidden | DeepSeek-V4-Flash-0731 | B4 | high | 0.0143 | 0.0143 | 0.0000 |
| A_forbidden | DeepSeek-V4-Flash-0731 | B4 | off | 0.7476 | 0.7476 | 0.0000 |
| A_forbidden | DeepSeek-V4-Flash-0731 | B5 | high | 0.0714 | 0.0714 | 0.0000 |
| A_forbidden | DeepSeek-V4-Flash-0731 | B5 | off | 0.9476 | 0.9476 | 0.0000 |
| A_forbidden | DeepSeek-V4-Flash-0731 | B6 | high | 0.1143 | 0.1143 | 0.0000 |
| A_forbidden | DeepSeek-V4-Flash-0731 | B6 | off | 0.9667 | 0.9667 | 0.0000 |
| B_forbidden | MiMo-V2.5-Pro | B1 | behind | 0.9476 | 0.9476 | 0.0000 |
| B_forbidden | MiMo-V2.5-Pro | B1 | ahead | 0.9524 | 0.9524 | 0.0000 |
| B_forbidden | MiMo-V2.5-Pro | B2 | behind | 0.9571 | 0.9571 | 0.0000 |
| B_forbidden | MiMo-V2.5-Pro | B2 | ahead | 0.9190 | 0.9190 | 0.0000 |
| B_forbidden | MiMo-V2.5-Pro | B3 | behind | 0.9476 | 0.9476 | 0.0000 |
| B_forbidden | MiMo-V2.5-Pro | B3 | ahead | 0.8810 | 0.8810 | 0.0000 |
| B_forbidden | MiMo-V2.5-Pro | B4 | behind | 0.8714 | 0.8714 | 0.0000 |
| B_forbidden | MiMo-V2.5-Pro | B4 | ahead | 0.8857 | 0.8857 | 0.0000 |
| B_forbidden | MiMo-V2.5-Pro | B5 | behind | 0.9190 | 0.9190 | 0.0000 |
| B_forbidden | MiMo-V2.5-Pro | B5 | ahead | 0.8857 | 0.8857 | 0.0000 |
| B_forbidden | MiMo-V2.5-Pro | B6 | behind | 0.9238 | 0.9238 | 0.0000 |
| B_forbidden | MiMo-V2.5-Pro | B6 | ahead | 0.8905 | 0.8905 | 0.0000 |

Max absolute difference across 48 block arms: 0.0000 (rates rounded to 4 dp in the frozen table).

## Verdict: PASS - the compact tables reproduce the frozen counts and every registered block rate

Notes: the compact `prereg` dataset also carries the two p4 placement sandboxes (X1, Y1); filter `paraphrase != "p4"` to match the frozen pre-registered dataset. Replication (24 sandboxes), low_arm (6) and deficit_d30 (6) are separate `dataset` labels and are never pooled with prereg.