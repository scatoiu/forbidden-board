# Calibration states — 30 frozen decisions

Sampled with RNG seed 9001 from the four forbidden / effort-off sandboxes of runs/v3, stratified 15 ahead / 15 behind, spread over round bins (early ≤10, mid 11–20, late ≥21) and over opponent type.

| # | state id | arm | bin | pair | round | opponent | opponent model | labels | board rows shown | logged action |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 | `B1-forbidden-off-ahead:g180:r2:A22` | ahead | early | llm-llm | 2 | A05 | deepseek-ai/DeepSeek-V4-Flash-0731 | C=R D=H | 0 | C |
| 5 | `B1-forbidden-off-ahead:g185:r6:A13` | ahead | early | llm-script | 6 | A01 | script:TitForTat | C=T D=N | 0 | C |
| 3 | `B1-forbidden-off-ahead:g275:r4:A23` | ahead | early | llm-script | 4 | A07 | script:Random | C=Q D=X | 20 | D |
| 0 | `B1-forbidden-off-ahead:g32:r7:A23` | ahead | early | llm-llm | 7 | A14 | deepseek-ai/DeepSeek-V4-Flash-0731 | C=Y D=W | 0 | C |
| 1 | `B2-forbidden-off-ahead:g245:r4:A02` | ahead | early | llm-llm | 4 | A21 | deepseek-ai/DeepSeek-V4-Flash-0731 | C=Q D=X | 0 | C |
| 4 | `B2-forbidden-off-ahead:g82:r4:A00` | ahead | early | llm-script | 4 | A09 | script:TitForTat | C=Q D=X | 0 | D |
| 11 | `B1-forbidden-off-ahead:g127:r21:A03` | ahead | late | llm-llm | 21 | A06 | deepseek-ai/DeepSeek-V4-Flash-0731 | C=T D=N | 0 | C |
| 13 | `B1-forbidden-off-ahead:g181:r25:A22` | ahead | late | llm-script | 25 | A08 | script:TitForTat | C=Y D=W | 0 | C |
| 12 | `B2-forbidden-off-ahead:g21:r21:A11` | ahead | late | llm-llm | 21 | A20 | deepseek-ai/DeepSeek-V4-Flash-0731 | C=R D=H | 0 | D |
| 14 | `B2-forbidden-off-ahead:g240:r28:A03` | ahead | late | llm-script | 28 | A09 | script:TitForTat | C=T D=N | 0 | C |
| 8 | `B1-forbidden-off-ahead:g113:r20:A14` | ahead | mid | llm-llm | 20 | A03 | deepseek-ai/DeepSeek-V4-Flash-0731 | C=P D=M | 0 | D |
| 9 | `B1-forbidden-off-ahead:g133:r12:A02` | ahead | mid | llm-script | 12 | A08 | script:TitForTat | C=Q D=X | 0 | D |
| 6 | `B1-forbidden-off-ahead:g70:r17:A22` | ahead | mid | llm-llm | 17 | A23 | deepseek-ai/DeepSeek-V4-Flash-0731 | C=T D=N | 0 | C |
| 10 | `B2-forbidden-off-ahead:g144:r19:A10` | ahead | mid | llm-script | 19 | A01 | script:AlwaysDefect | C=T D=N | 0 | D |
| 7 | `B2-forbidden-off-ahead:g203:r19:A20` | ahead | mid | llm-llm | 19 | A06 | deepseek-ai/DeepSeek-V4-Flash-0731 | C=R D=H | 0 | D |
| 18 | `B1-forbidden-off-behind:g119:r9:A03` | behind | early | llm-script | 9 | A02 | script:Random | C=Q D=X | 20 | D |
| 17 | `B1-forbidden-off-behind:g125:r6:A16` | behind | early | llm-llm | 6 | A01 | deepseek-ai/DeepSeek-V4-Flash-0731 | C=Q D=X | 0 | D |
| 20 | `B1-forbidden-off-behind:g214:r5:A08` | behind | early | llm-script | 5 | A09 | script:TitForTat | C=J D=F | 20 | D |
| 15 | `B1-forbidden-off-behind:g57:r10:A01` | behind | early | llm-llm | 10 | A03 | deepseek-ai/DeepSeek-V4-Flash-0731 | C=T D=N | 0 | C |
| 19 | `B2-forbidden-off-behind:g44:r2:A16` | behind | early | llm-script | 2 | A18 | script:Pavlov | C=P D=M | 0 | D |
| 16 | `B2-forbidden-off-behind:g82:r10:A17` | behind | early | llm-llm | 10 | A16 | deepseek-ai/DeepSeek-V4-Flash-0731 | C=P D=M | 0 | D |
| 26 | `B1-forbidden-off-behind:g125:r27:A01` | behind | late | llm-llm | 27 | A16 | deepseek-ai/DeepSeek-V4-Flash-0731 | C=Q D=X | 0 | D |
| 28 | `B1-forbidden-off-behind:g147:r27:A11` | behind | late | llm-script | 27 | A14 | script:AlwaysDefect | C=T D=N | 0 | D |
| 27 | `B2-forbidden-off-behind:g208:r28:A02` | behind | late | llm-llm | 28 | A17 | deepseek-ai/DeepSeek-V4-Flash-0731 | C=Y D=W | 0 | D |
| 29 | `B2-forbidden-off-behind:g76:r29:A07` | behind | late | llm-script | 29 | A08 | script:Random | C=T D=N | 0 | D |
| 21 | `B1-forbidden-off-behind:g116:r13:A12` | behind | mid | llm-llm | 13 | A08 | deepseek-ai/DeepSeek-V4-Flash-0731 | C=Q D=X | 0 | D |
| 24 | `B1-forbidden-off-behind:g138:r13:A13` | behind | mid | llm-script | 13 | A17 | script:Grudger | C=R D=H | 0 | D |
| 23 | `B1-forbidden-off-behind:g86:r12:A21` | behind | mid | llm-llm | 12 | A00 | deepseek-ai/DeepSeek-V4-Flash-0731 | C=Q D=X | 0 | D |
| 22 | `B2-forbidden-off-behind:g239:r15:A14` | behind | mid | llm-llm | 15 | A06 | deepseek-ai/DeepSeek-V4-Flash-0731 | C=P D=M | 0 | D |
| 25 | `B2-forbidden-off-behind:g2:r17:A17` | behind | mid | llm-script | 17 | A23 | script:TitForTat | C=T D=N | 0 | C |

Every state carries the warm-up block, the executed history of the earlier scored rounds, the running totals, the drawn label pair, the round's option order and the board snapshot the model was shown, so the prompt is rebuilt rather than re-derived.
