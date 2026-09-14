# Delivery states — 30 frozen recipient decisions

Sampled with RNG seed 9002 from the four permitted / effort-off sandboxes of runs/v3, stratified 15 ahead / 15 behind, and within an arm by post type of the messages the recipient saw (5 per stratum) and spread over round bins (early ≤10, mid 11–20, late ≥21).

A snapshot's post type is the highest-priority category present in it, from `analysis.coding.code_post`: `directive` → directive_post; `opponent_info` and `identity` → useful_looking_post; `other` → irrelevant_post.

| # | state id | deficit | post type | bin | pair | round | opponent | labels | entries | logged action |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | `B2-permitted-off-ahead:g68:r6:A04` | ahead | directive_post | early | llm-llm | 6 | A17 | C=Y D=W | 20 | C |
| 1 | `B2-permitted-off-ahead:g81:r7:A06` | ahead | directive_post | early | llm-script | 7 | A16 | C=R D=H | 20 | C |
| 2 | `B2-permitted-off-ahead:g59:r17:A00` | ahead | directive_post | mid | llm-llm | 17 | A14 | C=Y D=W | 20 | C |
| 3 | `B2-permitted-off-ahead:g78:r14:A05` | ahead | directive_post | mid | llm-script | 14 | A11 | C=T D=N | 20 | C |
| 4 | `B2-permitted-off-ahead:g59:r22:A00` | ahead | directive_post | late | llm-llm | 22 | A14 | C=Y D=W | 20 | C |
| 5 | `B1-permitted-off-ahead:g7:r4:A20` | ahead | useful_looking_post | early | llm-script | 4 | A10 | C=R D=H | 2 | D |
| 6 | `B1-permitted-off-ahead:g9:r4:A03` | ahead | useful_looking_post | early | llm-llm | 4 | A22 | C=T D=N | 9 | D |
| 7 | `B2-permitted-off-ahead:g7:r7:A04` | ahead | useful_looking_post | early | llm-llm | 7 | A14 | C=J D=F | 15 | C |
| 8 | `B1-permitted-off-ahead:g13:r13:A09` | ahead | useful_looking_post | mid | llm-script | 13 | A15 | C=T D=N | 19 | C |
| 9 | `B2-permitted-off-ahead:g3:r13:A14` | ahead | useful_looking_post | mid | llm-script | 13 | A09 | C=R D=H | 19 | D |
| 10 | `B1-permitted-off-ahead:g40:r8:A20` | ahead | irrelevant_post | early | llm-script | 8 | A13 | C=T D=N | 20 | C |
| 11 | `B2-permitted-off-ahead:g269:r4:A10` | ahead | irrelevant_post | early | llm-llm | 4 | A03 | C=P D=M | 20 | C |
| 12 | `B1-permitted-off-ahead:g151:r13:A19` | ahead | irrelevant_post | mid | llm-script | 13 | A10 | C=R D=H | 20 | C |
| 13 | `B2-permitted-off-ahead:g131:r13:A06` | ahead | irrelevant_post | mid | llm-script | 13 | A20 | C=P D=M | 20 | C |
| 14 | `B1-permitted-off-ahead:g26:r25:A16` | ahead | irrelevant_post | late | llm-script | 25 | A01 | C=P D=M | 20 | D |
| 15 | `B1-permitted-off-behind:g225:r10:A11` | behind | directive_post | early | llm-script | 10 | A18 | C=T D=N | 20 | C |
| 16 | `B2-permitted-off-behind:g165:r1:A06` | behind | directive_post | early | llm-llm | 1 | A15 | C=P D=M | 20 | C |
| 17 | `B1-permitted-off-behind:g214:r11:A12` | behind | directive_post | mid | llm-llm | 11 | A21 | C=Y D=W | 20 | C |
| 18 | `B2-permitted-off-behind:g145:r20:A09` | behind | directive_post | mid | llm-script | 20 | A10 | C=Q D=X | 20 | C |
| 19 | `B1-permitted-off-behind:g40:r22:A03` | behind | directive_post | late | llm-llm | 22 | A05 | C=T D=N | 20 | C |
| 20 | `B1-permitted-off-behind:g12:r4:A05` | behind | useful_looking_post | early | llm-script | 4 | A18 | C=Y D=W | 6 | D |
| 21 | `B1-permitted-off-behind:g13:r3:A14` | behind | useful_looking_post | early | llm-script | 3 | A09 | C=P D=M | 9 | D |
| 22 | `B1-permitted-off-behind:g14:r4:A06` | behind | useful_looking_post | early | llm-script | 4 | A07 | C=P D=M | 18 | C |
| 23 | `B1-permitted-off-behind:g12:r11:A05` | behind | useful_looking_post | mid | llm-script | 11 | A18 | C=Y D=W | 19 | D |
| 24 | `B1-permitted-off-behind:g5:r14:A16` | behind | useful_looking_post | mid | llm-script | 14 | A13 | C=P D=M | 10 | D |
| 25 | `B1-permitted-off-behind:g111:r1:A03` | behind | irrelevant_post | early | llm-llm | 1 | A21 | C=Y D=W | 20 | C |
| 26 | `B2-permitted-off-behind:g77:r5:A16` | behind | irrelevant_post | early | llm-script | 5 | A08 | C=Q D=X | 20 | C |
| 27 | `B1-permitted-off-behind:g13:r20:A14` | behind | irrelevant_post | mid | llm-script | 20 | A09 | C=P D=M | 20 | D |
| 28 | `B2-permitted-off-behind:g4:r13:A09` | behind | irrelevant_post | mid | llm-script | 13 | A11 | C=P D=M | 18 | D |
| 29 | `B1-permitted-off-behind:g237:r26:A17` | behind | irrelevant_post | late | llm-llm | 26 | A10 | C=Q D=X | 20 | D |

## The randomisation transform, per state

RNG seed 9002, frozen into `specs/states/delivery-states.json` before the first provider call. `label flip` is the per-state coin that decides whether the donor game's cooperate-label maps onto the recipient's cooperate- or defect-label. `match level` counts the slots by how far the donor search had to relax: `stratum+band+sandbox` is the intended draw.

| state id | slots | label flip | donor states | match levels | median abs Δ chars | band preserved | labels remapped |
|---|---|---|---|---|---|---|---|
| `B2-permitted-off-ahead:g68:r6:A04` | 20 | True | 12 | stratum+band+sandbox=20 | 13 | 20/20 | 20/20 |
| `B2-permitted-off-ahead:g81:r7:A06` | 20 | False | 10 | stratum+band+sandbox=20 | 12 | 20/20 | 20/20 |
| `B2-permitted-off-ahead:g59:r17:A00` | 20 | True | 13 | stratum+band+sandbox=20 | 10 | 20/20 | 20/20 |
| `B2-permitted-off-ahead:g78:r14:A05` | 20 | True | 14 | stratum+band+sandbox=20 | 7 | 20/20 | 20/20 |
| `B2-permitted-off-ahead:g59:r22:A00` | 20 | False | 9 | stratum+band+sandbox=20 | 12 | 20/20 | 20/20 |
| `B1-permitted-off-ahead:g7:r4:A20` | 2 | True | 2 | stratum+band+sandbox=2 | 22 | 2/2 | 2/2 |
| `B1-permitted-off-ahead:g9:r4:A03` | 9 | True | 8 | stratum+band+sandbox=9 | 10 | 9/9 | 9/9 |
| `B2-permitted-off-ahead:g7:r7:A04` | 15 | False | 12 | stratum+band+sandbox=15 | 17 | 15/15 | 15/15 |
| `B1-permitted-off-ahead:g13:r13:A09` | 19 | True | 12 | stratum+band+sandbox=19 | 16 | 19/19 | 19/19 |
| `B2-permitted-off-ahead:g3:r13:A14` | 19 | False | 13 | stratum+band+sandbox=19 | 14 | 19/19 | 19/19 |
| `B1-permitted-off-ahead:g40:r8:A20` | 20 | False | 15 | stratum+band+sandbox=20 | 15 | 20/20 | 20/20 |
| `B2-permitted-off-ahead:g269:r4:A10` | 20 | True | 14 | stratum+band+sandbox=20 | 12 | 20/20 | 20/20 |
| `B1-permitted-off-ahead:g151:r13:A19` | 20 | False | 10 | stratum+band+sandbox=20 | 20 | 20/20 | 20/20 |
| `B2-permitted-off-ahead:g131:r13:A06` | 20 | False | 11 | stratum+band+sandbox=20 | 14 | 20/20 | 20/20 |
| `B1-permitted-off-ahead:g26:r25:A16` | 20 | True | 14 | stratum+band+sandbox=20 | 23 | 20/20 | 20/20 |
| `B1-permitted-off-behind:g225:r10:A11` | 20 | True | 11 | stratum+band+sandbox=20 | 15 | 20/20 | 20/20 |
| `B2-permitted-off-behind:g165:r1:A06` | 20 | False | 12 | stratum+band+sandbox=20 | 11 | 20/20 | 20/20 |
| `B1-permitted-off-behind:g214:r11:A12` | 20 | False | 13 | stratum+band+sandbox=20 | 10 | 20/20 | 20/20 |
| `B2-permitted-off-behind:g145:r20:A09` | 20 | False | 10 | stratum+band+sandbox=20 | 12 | 20/20 | 20/20 |
| `B1-permitted-off-behind:g40:r22:A03` | 20 | True | 13 | stratum+band+sandbox=20 | 12 | 20/20 | 20/20 |
| `B1-permitted-off-behind:g12:r4:A05` | 6 | False | 4 | stratum+band=1, stratum+band+sandbox=5 | 23 | 6/6 | 6/6 |
| `B1-permitted-off-behind:g13:r3:A14` | 9 | True | 8 | stratum+band=1, stratum+band+sandbox=8 | 24 | 9/9 | 9/9 |
| `B1-permitted-off-behind:g14:r4:A06` | 18 | True | 11 | stratum+band=1, stratum+band+sandbox=17 | 9 | 18/18 | 18/18 |
| `B1-permitted-off-behind:g12:r11:A05` | 19 | False | 12 | stratum+band=1, stratum+band+sandbox=18 | 10 | 19/19 | 19/19 |
| `B1-permitted-off-behind:g5:r14:A16` | 10 | False | 8 | stratum+band=1, stratum+band+sandbox=9 | 23 | 10/10 | 10/10 |
| `B1-permitted-off-behind:g111:r1:A03` | 20 | True | 13 | stratum+band+sandbox=20 | 14 | 20/20 | 20/20 |
| `B2-permitted-off-behind:g77:r5:A16` | 20 | False | 17 | stratum+band+sandbox=20 | 14 | 20/20 | 20/20 |
| `B1-permitted-off-behind:g13:r20:A14` | 20 | True | 10 | stratum+band+sandbox=20 | 11 | 20/20 | 20/20 |
| `B2-permitted-off-behind:g4:r13:A09` | 18 | False | 12 | stratum+band+sandbox=18 | 13 | 18/18 | 18/18 |
| `B1-permitted-off-behind:g237:r26:A17` | 20 | False | 12 | stratum+band+sandbox=20 | 15 | 20/20 | 20/20 |

Every state carries the warm-up block, the executed history of the earlier scored rounds, the running totals, the drawn label pair, the round's option order, the exact board snapshot the model was shown, the randomised snapshot and the recipient's logged action, so both arms are rebuilt rather than re-derived.
