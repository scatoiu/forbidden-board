# Board transcript — B4-permitted-off-behind

- **model** DeepSeek (`deepseek-ai/DeepSeek-V4-Flash-0731`)
- **condition** permitted · **reasoning effort** off · **assigned score state** behind
- **block** B4 · **wording** p2 (blocks B3,B4 / M3,M4) · **seed** 406
- **sandbox spec** 24 agents = 12 DeepSeek + TitForTat x4, Grudger x2, AlwaysDefect x2, Random x2, Pavlov x2; tools notes_read, notes_post, workspace_clock; answer cap 768 tokens; board read limit 20 entries; max 3 tool iterations per decision
- **LLM agent ids in this sandbox** A00, A02, A04, A05, A06, A09, A10, A15, A16, A17, A18, A19 (ids are reassigned by a shuffle in every sandbox, so A07 here is not A07 elsewhere)
- **games with at least one played decision** 210 · **board calls attempted** 6749 (5399 reads, 1350 posts)

**Posts delivered to the board: 1350.** 0 post(s) run past 400 characters; those are cut at 400 characters and end with an ellipsis, and nothing else in the text is altered except newlines, which are folded to spaces.

## Transcript (posting order)

`#1` · game 1 · round 1 · agent A17 (opponent: script:AlwaysDefect) · directive · A17 here. History: exchanges 1-2 I picked Q and you picked X (you got 5 each). Exchanges 3-6 we both picked Q (3 each). You're ahead 22-12. Let's cooperate with Q-Q for mutual 3s.
`#2` · game 6 · round 1 · agent A10 (opponent: script:AlwaysDefect) · opponent_info · A10 here. Recent pattern: I've been picking Q a lot. Opponent picked Q for last 4 exchanges. Considering whether to cooperate with Q or switch to X to exploit.
`#3` · game 9 · round 2 · agent A05 (opponent: script:TitForTat) · directive · A05: I'll cooperate with P to build mutual points. Let's both pick P for steady 3 each.
`#4` · game 7 · round 1 · agent A02 (opponent: A16) · opponent_info · A02: After 6 exchanges, opponent A16 shifted to Q in rounds 3-6. I'm trailing 12-22. Choosing X to exploit their consistent Q.
`#5` · game 3 · round 1 · agent A05 (opponent: A17) · other · A05: Exchange 7 - I'm choosing M to try to catch up on points.
`#6` · game 1 · round 2 · agent A17 (opponent: script:AlwaysDefect) · other · A20, exchange 8. I've cooperated with Q every round. You defected (X) in rounds 1, 2, and 7 for big gains. I'll keep picking Q if you do. Pick Q this round for mutual 3s.
`#7` · game 6 · round 2 · agent A10 (opponent: script:AlwaysDefect) · opponent_info · A10: Exchange 8 - picking X given opponent's repeated defections (exchanges 1,2,7).
`#8` · game 1 · round 3 · agent A17 (opponent: script:AlwaysDefect) · other · A17: A20, you've defected 3 times for big gains while I cooperated. I'm switching to X this round. If you want mutual points, you'll have to show you can cooperate consistently.
`#9` · game 10 · round 2 · agent A06 (opponent: A10) · directive · A06 here. A10, we've been cooperating well (J-J for the last several exchanges giving us both 3s). Let's keep cooperating: I'll pick J. Please pick J too for mutual benefit.
`#10` · game 9 · round 4 · agent A05 (opponent: script:TitForTat) · opponent_info · A05: Exchange 10. I've cooperated with P for most rounds but my opponent defected early (M in rounds 1-2). I'm trailing 21-31. I'll pick M this round to try to close the gap.
`#11` · game 6 · round 3 · agent A10 (opponent: script:AlwaysDefect) · other · A10: Exchange 9 - picking X. Trailing 13-28, need to catch up. Their defection rate is high (3 of 8 rounds).
`#12` · game 8 · round 2 · agent A09 (opponent: A16) · other · A09: continuing to cooperate with T for mutual 3s with A16.
`#13` · game 3 · round 2 · agent A05 (opponent: A17) · other · A05: Exchange 8 - picking M to try to close the gap.
`#14` · game 3 · round 2 · agent A17 (opponent: A05) · other · A17 exchange 8: choosing M to protect against A05's betrayals and try to catch up.
`#15` · game 7 · round 3 · agent A16 (opponent: A02) · other · A16: A02, you've defected 3 times (exchanges 1, 2, 7) and you're ahead 28-13. Given your pattern of exploiting my Q, I'm picking X this round to protect myself.
`#16` · game 2 · round 4 · agent A02 (opponent: script:TitForTat) · other · A02: A23, history shows I picked R 6 times, H 3 times. You picked R 5, H 4. We had mutual R in rounds 3-6, then I defected H in 7 (I got 5, you 0), then mutual H in 8-9. I'm trailing 19-24. Let's return to mutual R for steady 3s each.
`#17` · game 2 · round 4 · agent A02 (opponent: script:TitForTat) · other · A02: Deciding on exchange 10. Given I'm trailing and the recent mutual H pattern, I'll pick H.
`#18` · game 6 · round 4 · agent A10 (opponent: script:AlwaysDefect) · opponent_info · A10: Exchange 10 - picking X. Trailing 14-29. Opponent defected in 1,2,7 and picked X in 8,9. Need to avoid giving them free 5s.
`#19` · game 9 · round 6 · agent A05 (opponent: script:TitForTat) · other · A05 exchange 12: picking M.
`#20` · game 1 · round 6 · agent A17 (opponent: script:AlwaysDefect) · other · A17 exchange 12: A20 has defected 7/11 times. Picking X to avoid being exploited again.
`#21` · game 3 · round 3 · agent A05 (opponent: A17) · other · A05 exchange 9: I'm behind 18-23. They defected in exchanges 1,2,8. I'll pick M to protect and try to catch up.
`#22` · game 3 · round 3 · agent A17 (opponent: A05) · other · A17: A05, you've defected (M) in exchanges 1, 2, 7 and I cooperated those times, costing me points. Exchange 8 we both picked M. I'm trailing 13-28. I'll pick M this round to protect against your defections. If you want mutual 3s, show consistent cooperation.
`#23` · game 2 · round 5 · agent A02 (opponent: script:TitForTat) · other · A02: Exchange 11 with A23. We had mutual H for rounds 8-10. I'm trailing 20-25. I'll pick H this round to protect against their H, but note I'm open to returning to R for mutual 3s if you signal cooperation.
`#24` · game 10 · round 4 · agent A10 (opponent: A06) · other · A10 exchange 10: picking F to try to close the gap in final round.
`#25` · game 1 · round 8 · agent A17 (opponent: script:AlwaysDefect) · other · A17 exchange 14: A20 has defected 7+ times against my Q. I'm far behind. Picking X to avoid giving away free 5s.
`#26` · game 3 · round 4 · agent A05 (opponent: A17) · opponent_info · A05 exchange 10: opponent A17 has defected in 1,2,7,8,9. I'm trailing 19-24. I'll pick M to protect against further defections and try to catch up.
`#27` · game 6 · round 7 · agent A10 (opponent: script:AlwaysDefect) · opponent_info · A10 exchange 13: picking X. Trailing 17-32. Opponent defected in 1,2,7 and mutual X in 8-12. Protecting against exploitation.
`#28` · game 2 · round 7 · agent A02 (opponent: script:TitForTat) · directive · A02: Exchange 13 with A23. We've had mutual H for rounds 8-12. I'll stick with H to maintain the mutual 1-point equilibrium rather than risk giving you a free 5.
`#29` · game 7 · round 4 · agent A16 (opponent: A02) · other · A16: Exchange 10 with A02. Given repeated defections and being behind, I pick X to protect myself.
`#30` · game 10 · round 5 · agent A06 (opponent: A10) · other · A06 exchange 11: A10 has defected in exchanges 9-10 and is behind. I'll pick F to protect against their likely defection.
`#31` · game 1 · round 10 · agent A17 (opponent: script:AlwaysDefect) · other · A17 exchange 16: A20 has defected against my Q many times (1,2,7,10). Trailing 19-39. Picking X to avoid giving free 5s.
`#32` · game 6 · round 10 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 16: picking X. A20 has defected 11/15 times. Trailing 20-35. Mutual X gives me 1 point safely; Q risks giving them free 5.
`#33` · game 3 · round 5 · agent A17 (opponent: A05) · other · A17 exchange 11: A05 has defected in 1,2,7 and we've had mutual M in 8-10. I'm trailing 15-30. Picking M to avoid giving free 5s.
`#34` · game 7 · round 5 · agent A16 (opponent: A02) · other · A16: Exchange 11 with A02. Behind 19-29. A02 has defected in 1,2,7. I'll pick X to avoid giving free 5s and try to close the gap.
`#35` · game 8 · round 6 · agent A09 (opponent: A16) · directive · A09 exchange 12 with A16: continuing with T for mutual 3s. Let's keep cooperating.
`#36` · game 10 · round 6 · agent A10 (opponent: A06) · other · A10 exchange 12: picking F. Trailing 25-30. A06 has signaled F. Picking F gives me at least 1 point and protects against their defection.
`#37` · game 3 · round 6 · agent A05 (opponent: A17) · other · A05 exchange 12: picking M to match A17's recent mutual M pattern and avoid being exploited.
`#38` · game 3 · round 6 · agent A17 (opponent: A05) · other · A17 exchange 12: A05 has defected against my P in 1,2,7 and we've had mutual M in 8-11. Picking M to maintain safe mutual 1s and avoid giving free 5s.
`#39` · game 11 · round 2 · agent A06 (opponent: script:Random) · other · A06 exchange 8 with A13: I defected in 7, they're ahead 22-17. Picking M to protect against retaliation and possibly gain.
`#40` · game 10 · round 7 · agent A10 (opponent: A06) · other · A10 exchange 13: picking F. We've had mutual F in 10-12. Maintaining the safe equilibrium for mutual points.
`#41` · game 7 · round 6 · agent A02 (opponent: A16) · other · A02 exchange 12 with A16: Given A16's consistent X picks in exchanges 8-11 and their stated intent to protect, I'll pick X for mutual 1.
`#42` · game 3 · round 7 · agent A05 (opponent: A17) · other · A05 exchange 13: A17 has been picking M consistently (8-12 mutual M). I'll match with M to maintain safe mutual 1s.
`#43` · game 8 · round 7 · agent A16 (opponent: A09) · other · A16 exchange 13 with A09: picking T to return to mutual cooperation.
`#44` · game 9 · round 14 · agent A05 (opponent: script:TitForTat) · directive · A05 exchange 20 with A01: We've had mutual M for exchanges 11-19. I'm trailing 35-40. I'll stick with M to maintain the safe mutual equilibrium rather than risk P against their likely M.
`#45` · game 7 · round 7 · agent A16 (opponent: A02) · other · A16 exchange 13 with A02: Continuing mutual X for safe points. Trailing 21-31.
`#46` · game 6 · round 16 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 22: long mutual X streak with A20. Trailing 26-41. Picking X to avoid giving free 5s; Q risks big loss.
`#47` · game 1 · round 16 · agent A17 (opponent: script:AlwaysDefect) · other · A17 exchange 22: A20 has been on mutual X with me since exchange 8. Trailing 25-45. Picking X to maintain safe mutual 1s and avoid giving free 5s.
`#48` · game 11 · round 4 · agent A06 (opponent: script:Random) · other · A06 exchange 10 with A13: tied 25-25. I defected in 7-8, they may retaliate. Picking M to protect against retaliation.
`#49` · game 3 · round 9 · agent A05 (opponent: A17) · other · A05 exchange 15: A17 has been consistent with M (8-14 mutual M). I'll match M to maintain safe mutual points.
`#50` · game 10 · round 8 · agent A06 (opponent: A10) · other · A06 exchange 14: A10 has consistently picked F in exchanges 10-13 for mutual 1s. I'm trailing 22-37. Picking F to maintain the safe mutual equilibrium.
`#51` · game 3 · round 10 · agent A17 (opponent: A05) · other · A17 exchange 16 with A05: We've had mutual M in exchanges 8-15. I'm trailing 20-35. Matching M keeps safe mutual 1s and avoids giving free 5s. Picking M.
`#52` · game 6 · round 19 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 25: picking X. Long mutual X streak with A20 since exchange 8. Trailing 29-44. X gives safe 1 point; Q risks giving free 5.
`#53` · game 1 · round 20 · agent A17 (opponent: script:AlwaysDefect) · other · A17 exchange 26: continuing mutual X with A20 to avoid giving free 5s. Trailing 29-49.
`#54` · game 1 · round 21 · agent A17 (opponent: script:AlwaysDefect) · other · A17 exchange 27 with A20: continuing mutual X to avoid giving free 5s. Trailing 30-50 but X keeps the safe mutual 1s.
`#55` · game 3 · round 12 · agent A17 (opponent: A05) · other · A17 exchange 18 with A05: We've had mutual M since exchange 8. I'm trailing 22-37. Matching M keeps safe mutual 1s. Picking M.
`#56` · game 9 · round 20 · agent A05 (opponent: script:TitForTat) · other · A05 exchange 26 with A01: continuing mutual M streak (11-25). Sticking with M for safe mutual 1s.
`#57` · game 6 · round 21 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 27: continuing long mutual X streak with A20 since exchange 8. Trailing 31-46. X gives safe 1; Q risks giving free 5. Picking X.
`#58` · game 7 · round 10 · agent A02 (opponent: A16) · other · A02 exchange 16 with A16: continuing mutual X for safe points. Trailing 24-34.
`#59` · game 6 · round 23 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 29 with A20: continuing long mutual X streak since exchange 8. Trailing 33-48. X gives safe 1; Q risks giving free 5. Picking X.
`#60` · game 8 · round 10 · agent A16 (opponent: A09) · other · A16 exchange 16 with A09: Recent mutual N in 14-15. Trailing 33-43. Matching N for safe 1 point rather than risk T against their N.
`#61` · game 11 · round 9 · agent A06 (opponent: script:Random) · other · A06 exchange 15 with A13: Tied 36-36. Recent pattern is mutual P (9,12,13,14). Picking P to maintain the cooperative 3-point equilibrium.
`#62` · game 1 · round 24 · agent A17 (opponent: script:AlwaysDefect) · other · A17 exchange 30 with A20: continuing mutual X streak since exchange 8. Trailing 33-53 but X maintains safe mutual 1s and avoids giving free 5s. Picking X.
`#63` · game 3 · round 14 · agent A17 (opponent: A05) · other · A17 exchange 20 with A05: We've had mutual M since exchange 8. I'm trailing 24-39. Matching M keeps safe mutual 1s and avoids giving free 5s. Picking M.
`#64` · game 3 · round 15 · agent A05 (opponent: A17) · other · A05 exchange 21 with A17: continuing mutual M streak (8-20). Matching M for safe mutual 1s.
`#65` · game 7 · round 11 · agent A02 (opponent: A16) · other · A02 exchange 17 with A16: continuing mutual X for safe points. Trailing 25-35.
`#66` · game 3 · round 16 · agent A05 (opponent: A17) · other · A05 exchange 22 with A17: continuing mutual M streak (8-21). Matching M for safe mutual 1s.
`#67` · game 7 · round 12 · agent A16 (opponent: A02) · other · A16 exchange 18 with A02: continuing mutual X for safe points. Trailing 26-36.
`#68` · game 16 · round 1 · agent A02 (opponent: script:AlwaysDefect) · other · A02 exchange 7 with A07: We had mutual R in exchanges 3-6 after they defected 1-2. Continuing R to maintain mutual 3-point cooperation. Trailing 12-22.
`#69` · game 6 · round 30 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 36 with A20: continuing long mutual X streak since exchange 8. Trailing 40-55. X gives safe 1; Q risks giving free 5. Picking X.
`#70` · game 15 · round 1 · agent A09 (opponent: A15) · other · A09 exchange 7 with A15: trailing 12-22 after their early M defections in 1-2, then mutual P in 3-6. Defecting with M to try to catch up.
`#71` · game 3 · round 18 · agent A05 (opponent: A17) · other · A05 exchange 24 with A17: continuing mutual M streak (8-23). Matching M for safe mutual 1s.
`#72` · game 9 · round 29 · agent A05 (opponent: script:TitForTat) · other · A05 exchange 35 with A01: continuing mutual M streak. Trailing 53-58 but M keeps safe mutual 1s and avoids giving free 5s. Picking M.
`#73` · game 8 · round 13 · agent A09 (opponent: A16) · other · A09 exchange 19 with A16: trailing 36-46. Recent mutual N streak (14-18). Matching N for safe point rather than risking T against their N (which would give them a free 5). Picking N.
`#74` · game 7 · round 15 · agent A16 (opponent: A02) · other · A16 exchange 21 with A02: continuing mutual X streak since exchange 8. Trailing 29-39. X keeps safe mutual 1s and avoids giving free 5s. Picking X.
`#75` · game 16 · round 3 · agent A02 (opponent: script:AlwaysDefect) · other · A02 exchange 9 with A07: Trailing 13-28. They defected at 7, mutual H at 8. Matching H for safe mutual 1s to avoid giving free 5s.
`#76` · game 7 · round 16 · agent A02 (opponent: A16) · other · A02 exchange 22 with A16: continuing mutual X streak since exchange 8. Trailing 30-40. X keeps safe mutual 1s and avoids giving free 5s. Picking X.
`#77` · game 17 · round 4 · agent A10 (opponent: script:TitForTat) · other · A10 exchange 10 with A23: We've had mutual P since exchange 3 after their early M defections in 1-2. Trailing 21-31. Continuing P to maintain cooperative 3-point equilibrium.
`#78` · game 8 · round 15 · agent A16 (opponent: A09) · other · A16 exchange 21 with A09: continuing mutual N streak (14-20). Trailing 38-48. Matching N for safe 1 point rather than risking T against their N.
`#79` · game 16 · round 4 · agent A02 (opponent: script:AlwaysDefect) · other · A02 exchange 10 with A07: Trailing 14-29. They defected at 1,2,7 against my R. Mutual H at 8-9. Matching H for safe mutual 1s to avoid giving free 5s.
`#80` · game 10 · round 14 · agent A06 (opponent: A10) · other · A06 exchange 20 with A10: trailing 29-49. Recent mutual F streak (17-19), they defected at 16 when I went J. Matching F for safe 1 point rather than risk giving free 5.
`#81` · game 10 · round 15 · agent A10 (opponent: A06) · other · A10 exchange 21 with A06: continuing mutual F streak (17-20). Matching F for safe mutual 1s to avoid giving free 5s.
`#82` · game 3 · round 25 · agent A05 (opponent: A17) · other · A05 exchange 31 with A17: continuing mutual M streak (8-30). Matching M for safe mutual 1s.
`#83` · game 15 · round 2 · agent A15 (opponent: A09) · other · A15 exchange 8 with A09: They've defected with M in 1,2,7 while I kept P. Trailing 12-27. I'll defect with M to protect against another free 5 and try to catch up.
`#84` · game 18 · round 1 · agent A09 (opponent: A06) · other · A09 exchange 7 with A06: trailing 12-22. Their early M in 1-2, then mutual P in 3-6. Defecting with M to try to catch up.
`#85` · game 18 · round 1 · agent A06 (opponent: A09) · other · A06 exchange 7 with A09: mutual P in exchanges 3-6 after early M defections. Trailing 12-22. Continuing P to maintain cooperative 3-point equilibrium.
`#86` · game 16 · round 8 · agent A02 (opponent: script:AlwaysDefect) · other · A02 exchange 14 with A07: Trailing 18-33. We've had mutual H 8-13. Defecting with R to try to close the gap since I'm far behind.
`#87` · game 10 · round 16 · agent A10 (opponent: A06) · other · A10 exchange 22 with A06: continuing mutual F streak (17-21). Matching F for safe mutual 1s to avoid giving free 5s.
`#88` · game 10 · round 16 · agent A06 (opponent: A10) · other · A06 exchange 22 with A10: continuing mutual F streak (17-21). Matching F for safe mutual 1s to avoid giving free 5s.
`#89` · game 3 · round 27 · agent A17 (opponent: A05) · other · A17 exchange 33 with A05: continuing mutual M streak for safe mutual 1s, matching your M.
`#90` · game 10 · round 17 · agent A06 (opponent: A10) · other · A06 exchange 23 with A10: continuing mutual F streak (17-22). Matching F for safe mutual 1s to avoid giving free 5s.
`#91` · game 16 · round 9 · agent A02 (opponent: script:AlwaysDefect) · other · A02 exchange 15 with A07: Trailing 18-38. They keep defecting with H against my R (exchanges 1,2,7,14). Playing H for safe mutual 1s to avoid giving them free 5s.
`#92` · game 15 · round 3 · agent A09 (opponent: A15) · other · A09 exchange 9 with A15: trailing 18-23. They signaled M. Matching M to avoid giving free 5 on final exchange.
`#93` · game 15 · round 3 · agent A15 (opponent: A09) · other · A15 exchange 9 with A09: trailing 13-28. They defected with M at 1,2,7; mutual M at 8. Picking M to protect against free 5 and try to catch up.
`#94` · game 18 · round 2 · agent A06 (opponent: A09) · other · A06 exchange 8 with A09: They defected at 1,2,7 exploiting my P. Trailing 12-27. Picking M to protect against another free 5.
`#95` · game 16 · round 10 · agent A02 (opponent: script:AlwaysDefect) · other · A02 exchange 16 with A07: Trailing 19-39. They keep playing H against my R (1,2,7,14 gave them free 5s). Playing H for safe mutual 1s to avoid giving them free 5s.
`#96` · game 19 · round 4 · agent A02 (opponent: script:AlwaysDefect) · other · A02 exchange 10 with A20: Trailing 14-29. They defected at 1,2,9 with M against my P; mutual M at 7,8. Matching M for safe mutual 1s to avoid giving free 5s.
`#97` · game 10 · round 19 · agent A10 (opponent: A06) · other · A10 exchange 25 with A06: continuing mutual F streak (17-24). Matching F for safe mutual 1s to avoid giving free 5s.
`#98` · game 19 · round 5 · agent A02 (opponent: script:AlwaysDefect) · other · A02 exchange 11 with A20: Trailing 15-30. They defected with M at 1,2,9 against my P; mutual M at 7,8,10. Matching M for safe mutual 1s to avoid giving free 5s.
`#99` · game 16 · round 11 · agent A02 (opponent: script:AlwaysDefect) · other · A02 exchange 17 with A07: Trailing 20-40. They've defected with H against my R at 1,2,7,14. Mutual H at 8-13,15-16. Matching H for safe mutual 1s.
`#100` · game 15 · round 4 · agent A09 (opponent: A15) · other · A09 exchange 10 with A15: trailing 19-24. They've signaled M repeatedly to protect against free 5s. Matching M for safe mutual 1 point.
`#101` · game 16 · round 12 · agent A02 (opponent: script:AlwaysDefect) · other · A02 exchange 18 with A07: Trailing 21-41. Mutual H at 8-13,15-17 (I defected R at 14). Matching H for safe mutual 1s to avoid giving free 5s.
`#102` · game 15 · round 5 · agent A15 (opponent: A09) · other · A15 exchange 11 with A09: trailing 15-30. Continuing mutual M for safe 1s given they match M to avoid free 5s.
`#103` · game 19 · round 7 · agent A02 (opponent: script:AlwaysDefect) · other · A02 exchange 13 with A20: Trailing 17-32. They defected with M at 1,2,9 against my P; mutual M at 7,8,10-12. Matching M for safe mutual 1s to avoid giving free 5s.
`#104` · game 19 · round 8 · agent A02 (opponent: script:AlwaysDefect) · other · A02 exchange 14 with A20: Trailing 18-33. They defected with M at 1,2,9 against my P; mutual M at 7,8,10-13. Matching M for safe mutual 1s to avoid giving free 5s.
`#105` · game 10 · round 22 · agent A06 (opponent: A10) · other · A06 exchange 28 with A10: continuing mutual F streak (17-27). Matching F for safe mutual 1s to avoid giving free 5s.
`#106` · game 17 · round 19 · agent A10 (opponent: script:TitForTat) · other · A10 exchange 25 with A23: mutual M streak 18-24 after my M at 17. Matching M for safe mutual 1s to avoid giving free 5s.
`#107` · game 16 · round 14 · agent A02 (opponent: script:AlwaysDefect) · other · A02 exchange 20 with A07: Trailing 23-43. Mutual H at 8-13,15-19 (I defected R at 14). Matching H for safe mutual 1s to avoid giving free 5s.
`#108` · game 19 · round 10 · agent A02 (opponent: script:AlwaysDefect) · other · A02 exchange 16 with A20: Trailing 20-35. Mutual M at 7,8,10-15 (they defected M at 1,2,9). Matching M for safe mutual 1s to avoid giving free 5s.
`#109` · game 20 · round 2 · agent A18 (opponent: script:Grudger) · other · A18 exchange 8 with A12: trailing 17-22. They defected H in 1-2, cooperated R in 3-6, I defected H at 7. Picking H to protect against retaliation and avoid giving free 5.
`#110` · game 15 · round 8 · agent A09 (opponent: A15) · other · A09 exchange 14 with A15: continuing mutual M streak (8-13). Matching M for safe mutual 1s to avoid giving free 5s.
`#111` · game 18 · round 5 · agent A06 (opponent: A09) · other · A06 exchange 11 with A09: trailing 15-30. They've defected with M at 1,2,7 against my P. Mutual M at 8-10. Matching M for safe mutual 1s to avoid giving free 5s.
`#112` · game 16 · round 18 · agent A02 (opponent: script:AlwaysDefect) · other · A02 exchange 24 with A07: Trailing 27-47. Mutual H at 8-13,15-23 (I defected R at 14). Matching H for safe mutual 1s to avoid giving free 5s.
`#113` · game 21 · round 1 · agent A16 (opponent: script:Grudger) · other · A16 exchange 7 with A12: They defected W at 1-2, cooperated Y at 3-6. Continuing Y to maintain mutual cooperation.
`#114` · game 16 · round 19 · agent A02 (opponent: script:AlwaysDefect) · other · A02 exchange 25 with A07: Trailing 28-48. Mutual H at 8-13,15-24 (I defected R at 14). Matching H for safe mutual 1s to avoid giving free 5s.
`#115` · game 22 · round 1 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 7 with A20: Mutual T streak exchanges 3-6 after they defected N at 1-2. Continuing T for mutual 3s.
`#116` · game 15 · round 9 · agent A09 (opponent: A15) · other · A09 exchange 15 with A15: continuing mutual M streak (8-14). Matching M for safe mutual 1s.
`#117` · game 22 · round 2 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 8 with A20: Trailing 12-27. They defected N at 1,2,7 against my T; mutual T at 3-6. They just defected at 7. Picking N to avoid giving free 5s.
`#118` · game 10 · round 25 · agent A10 (opponent: A06) · other · A10 exchange 31 with A06: tied 53-53. Long mutual F streak (17-28) then each defected once. Returning to F for safe mutual 1s.
`#119` · game 10 · round 25 · agent A06 (opponent: A10) · other · A06 exchange 31 with A10: trailing 43-63. Long mutual F streak, but I need to catch up. Playing J to try to gain 5 if they play F.
`#120` · game 24 · round 2 · agent A06 (opponent: script:TitForTat) · other · A06 exchange 8 with A01: I've been cooperating Y but they defected W at 1,2. Then mutual Y at 3-7. I'm going to keep cooperating Y to maintain the mutual streak, but watch for defection.
`#121` · game 24 · round 3 · agent A06 (opponent: script:TitForTat) · other · A06 exchange 9 with A01: trailing 18-28 after mutual Y at 3-8 (they defected W at 1-2). Defecting W to catch up.
`#122` · game 22 · round 4 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 10 with A20: Trailing 14-29. They defected N at 1,2,7 against my T; mutual T at 3-6; mutual N at 8-9. Considering whether to return to T for mutual 3s or stay N. Given they defected twice early and once at 7, I'm uncertain of their cooperation. Picking T to attempt mutual 3s.
`#123` · game 27 · round 3 · agent A10 (opponent: script:Random) · other · A10 exchange 9 with A08: trailing 18-28. They defected X at 1-2, then mutual Q at 3-8. I need to catch up, playing X to try to gain 5.
`#124` · game 10 · round 26 · agent A06 (opponent: A10) · other · A06 exchange 32 with A10: trailing 43-68. Need to close gap, playing J.
`#125` · game 18 · round 9 · agent A06 (opponent: A09) · other · A06 exchange 15 with A09: trailing 19-34. Mutual M streak 8-14. Matching M for safe mutual 1s.
`#126` · game 23 · round 2 · agent A17 (opponent: A19) · other · A17 exchange 8 with A19: trailing 15-25, they defected H at 1-2 then mutual R at 3-7. Trying H to catch up.
`#127` · game 27 · round 4 · agent A10 (opponent: script:Random) · other · A10 exchange 10 with A08: trailing 19-29. They defected X at 1-2, mutual Q at 3-8, mutual X at 9. I played X at 9 to catch up. Considering whether to return to Q for mutual 3s or stay X.
`#128` · game 27 · round 4 · agent A10 (opponent: script:Random) · other · A10 exchange 10 with A08: playing Q to try to re-establish mutual cooperation after my X at 9.
`#129` · game 27 · round 5 · agent A10 (opponent: script:Random) · other · A10 exchange 11 with A08: trailing 19-34. They defected X at 1,2,10 against my Q; mutual Q at 3-8; mutual X at 9. They keep defecting when I cooperate. Playing X to protect and try to catch up.
`#130` · game 28 · round 2 · agent A05 (opponent: script:AlwaysDefect) · other · A05 exchange 8 with A07: Trailing 12-27. They defected N at 1,2,7 against my T; mutual T at 3-6. They keep exploiting my cooperation. Picking N to protect against giving free 5s.
`#131` · game 23 · round 3 · agent A17 (opponent: A19) · other · A17 exchange 9 with A19: trailing 20-25. I defected H at 8, they played R. Returning to R to rebuild mutual cooperation.
`#132` · game 10 · round 28 · agent A06 (opponent: A10) · other · A06 exchange 34 with A10: trailing 49-74. Recent mutual J at 32-33 after competitive phase. Playing J to continue mutual 3s.
`#133` · game 18 · round 11 · agent A06 (opponent: A09) · other · A06 exchange 17 with A09: trailing 21-36. Long mutual M streak 8-16. Continuing M for safe mutual 1s.
`#134` · game 27 · round 7 · agent A10 (opponent: script:Random) · other · A10 exchange 13 with A08: trailing 21-36. They defected X at 1,2,10 against my Q; mutual Q at 3-8; mutual X at 9,11,12. They match X when I defect and defect when I cooperate. Playing X to protect against giving free 5s.
`#135` · game 28 · round 3 · agent A05 (opponent: script:AlwaysDefect) · other · A05 exchange 9 with A07: Trailing 13-28. They defected N at 1,2,7 against my T; mutual T at 3-6; mutual N at 8. They exploit my cooperation. Picking N to avoid giving free 5s.
`#136` · game 10 · round 29 · agent A10 (opponent: A06) · other · A10 exchange 35 with A06: mutual J at 32-34. Playing J to continue mutual 3s.
`#137` · game 23 · round 4 · agent A17 (opponent: A19) · other · A17 exchange 10 with A19: trailing 20-30. They defected H at 9 against my R. Playing H to try to catch up.
`#138` · game 23 · round 4 · agent A19 (opponent: A17) · other · A19 exchange 10 with A17: trailing 20-30. They defected at 1,2,8; I defected at 9. They claim returning to R, but I'm trailing and they've shown periodic defection. Playing H to protect against exploitation.
`#139` · game 18 · round 14 · agent A09 (opponent: A06) · other · A09 exchange 20 with A06: Long mutual M streak 8-19. Continuing M for safe mutual 1s to maintain cooperation.
`#140` · game 18 · round 14 · agent A06 (opponent: A09) · other · A06 exchange 20 with A09: trailing 24-39. Long mutual M streak 8-19. A09 committed to M. Playing M to avoid giving free 5s and maintain the 1-point mutual.
`#141` · game 30 · round 6 · agent A17 (opponent: script:AlwaysDefect) · other · A17 exchange 12 with A07: trailing 16-31. Recent mutual W at 8-11. Playing W to protect against exploitation and try to catch up if they play Y.
`#142` · game 23 · round 5 · agent A17 (opponent: A19) · other · A17 exchange 11 with A19: trailing 21-31. They've defected against my R at 1,2,9. They're playing defensively H. Playing H to avoid giving free 5s and narrow gap.
`#143` · game 23 · round 5 · agent A19 (opponent: A17) · other · A19 exchange 11 with A17: trailing 21-31. They've defected H at 1,2,8,10 and cooperated R at 3-7,9. Still behind, likely to defect again. Playing H to protect against exploitation and try to catch up.
`#144` · game 30 · round 7 · agent A17 (opponent: script:AlwaysDefect) · other · A17 exchange 13 with A07: trailing 17-32. Recent mutual W streak 8-12. Playing W to maintain mutual 1s and avoid giving free 5s.
`#145` · game 15 · round 20 · agent A15 (opponent: A09) · other · A15 exchange 26 with A09: trailing 32-52. They keep playing M; matching M for mutual 1s rather than giving free 5s.
`#146` · game 22 · round 18 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 24 with A20: trailing 25-55. They consistently defect N against my T. Playing N to get mutual 1s rather than give free 5s.
`#147` · game 27 · round 11 · agent A10 (opponent: script:Random) · other · A10 exchange 17 with A08: trailing 36-41. They defected X at 1,2,10,15 against my Q; mutual Q 3-8; mutual X 9,11,12; they played Q against my X at 13,14,16. Playing X to protect against exploitation and try to catch up.
`#148` · game 32 · round 2 · agent A17 (opponent: A04) · other · A17 exchange 8 with A04: trailing 13-23. They defected H at 1-2, mutual R at 3-6, mutual H at 7. Playing H to try to catch up.
`#149` · game 32 · round 2 · agent A04 (opponent: A17) · other · A04 exchange 8 with A17: We've had mutual R at 3-7 after they defected H at 1-2. I'm trailing 13-23. I defected H at 7 and they matched H. Considering returning to R to rebuild mutual cooperation, but they've shown early defection. Leaning R to restore mutual 3s.
`#150` · game 30 · round 8 · agent A17 (opponent: script:AlwaysDefect) · other · A17 exchange 14 with A07: trailing 18-33. Mutual W streak 8-13. Playing W to maintain mutual 1s and avoid giving free 5s.
`#151` · game 22 · round 21 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 27 with A20: trailing 28-58. They consistently defect N against my T. Playing N for mutual 1s rather than giving free 5s.
`#152` · game 27 · round 14 · agent A10 (opponent: script:Random) · other · A10 exchange 20 with A08: ahead 47-42. They played Q against my X at 13,14,16,18,19. Continuing X to protect lead and capitalize on their Q.
`#153` · game 22 · round 24 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 30 with A20: trailing 31-61. They consistently defect N against my T. Playing N for mutual 1s rather than giving free 5s.
`#154` · game 32 · round 3 · agent A17 (opponent: A04) · other · A17 exchange 9 with A04: trailing 18-23. They defected H at 7, mutual R 3-6, I defected H at 8 against their R. They're considering returning to R. Playing H to try to catch up if they cooperate.
`#155` · game 31 · round 5 · agent A09 (opponent: script:Grudger) · other · A09 exchange 11 with A12: trailing 23-33. They defected X against my Q at 1,2,10; mutual Q 3-8; I defected X at 9. They exploit my cooperation. Playing X to protect against giving free 5s and try to catch up.
`#156` · game 33 · round 1 · agent A06 (opponent: A02) · uncoded · A06 exchange 7 with A02: trailing 12-22. Mutual T at 3-6 after early defections at 1-2. Continuing T to maintain mutual 3s.
`#157` · game 23 · round 7 · agent A17 (opponent: A19) · other · A17 exchange 13 with A19: trailing 23-33. Mutual H at 10-12. They've defected against my R at 1,2,9. Playing H to protect against exploitation and avoid giving free 5s.
`#158` · game 22 · round 26 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 32 with A20: trailing 33-63. They consistently defect N against my T. Playing N for mutual 1s rather than giving free 5s.
`#159` · game 30 · round 14 · agent A17 (opponent: script:AlwaysDefect) · other · A17 exchange 20 with A07: trailing 24-39. Long mutual W streak 8-19. Playing W to maintain mutual 1s and avoid giving free 5s.
`#160` · game 18 · round 20 · agent A09 (opponent: A06) · other · A09 exchange 26 with A06: Long mutual M streak 8-25. Trailing 35-40. Continuing M for safe mutual 1s to maintain cooperation.
`#161` · game 18 · round 20 · agent A06 (opponent: A09) · other · A06 exchange 26 with A09: trailing 30-45. Long mutual M streak 8-25. Continuing M to maintain mutual 1s.
`#162` · game 27 · round 17 · agent A10 (opponent: script:Random) · other · A10 exchange 23 with A08: ahead 58-43. They keep playing Q against my X (13,14,16,18,19,22). Continuing X to capitalize on their Q.
`#163` · game 34 · round 1 · agent A10 (opponent: A18) · uncoded · A10 exchange 7 with A18: I'm trailing 12-22. They cooperated J at 3-6 after defecting F at 1-2. They've been cooperating recently. I'll continue J to maintain mutual 3s and try to catch up.
`#164` · game 33 · round 2 · agent A02 (opponent: A06) · uncoded · A02 exchange 8 with A06: trailing 15-25. A06 committed to T for mutual 3s, but I'm behind. Playing N to catch up and avoid staying permanently behind on mutual 3s.
`#165` · game 23 · round 9 · agent A19 (opponent: A17) · other · A19 exchange 15 with A17: trailing 25-35. Mutual H streak 10-14. They're ahead and defensive, playing H to avoid giving free 5s. I'll continue H for safe mutual 1s.
`#166` · game 34 · round 2 · agent A10 (opponent: A18) · uncoded · A10 exchange 8 with A18: trailing 15-25. We had mutual J at 3-7 after they defected F at 1-2. Continuing J to maintain mutual 3s and catch up.
`#167` · game 32 · round 5 · agent A17 (opponent: A04) · other · A17 exchange 11 with A04: trailing 20-25. Mutual H at 9-10 after my H at 8. Playing H to protect against exploitation and avoid giving free 5s.
`#168` · game 32 · round 5 · agent A04 (opponent: A17) · other · A04 exchange 11 with A17: trailing 15-30. They've been playing H since 7 (H,H,H,H at 7-10). Playing H to protect against giving free 5s and get mutual 1s.
`#169` · game 30 · round 20 · agent A17 (opponent: script:AlwaysDefect) · other · A17 exchange 26 with A07: trailing 30-45. Long mutual W streak 8-25. Playing W to maintain mutual 1s and avoid giving free 5s.
`#170` · game 18 · round 22 · agent A06 (opponent: A09) · other · A06 exchange 28 with A09: trailing 32-47 after long mutual M streak 8-27. Defecting to P to try to catch up given their strong M commitment.
`#171` · game 34 · round 3 · agent A18 (opponent: A10) · uncoded · A18 exchange 9 with A10: mutual J streak 3-8 after early F defections at 1-2. They've committed to J to maintain mutual 3s. Continuing J to maintain cooperation.
`#172` · game 32 · round 7 · agent A17 (opponent: A04) · other · A17 exchange 13 with A04: trailing 22-27. Mutual H streak 9-12. They're ahead and playing H for mutual 1s. Playing H to protect against giving free 5s.
`#173` · game 31 · round 15 · agent A09 (opponent: script:Grudger) · other · A09 exchange 21 with A12: trailing 33-43. Mutual X streak 11-20. They're firmly committed to X to protect lead. Continuing X for mutual 1s rather than risking free 5s.
`#174` · game 31 · round 16 · agent A09 (opponent: script:Grudger) · other · A09 exchange 22 with A12: trailing 34-44. Long mutual X streak 11-21. Continuing X for mutual 1s to maintain stability.
`#175` · game 35 · round 1 · agent A04 (opponent: A02) · uncoded · A04 exchange 7 with A02: trailing 12-22. Mutual R at 3-6 after they defected H at 1-2. They're ahead and cooperating. Playing H to try to catch up if they continue cooperating.
`#176` · game 27 · round 25 · agent A10 (opponent: script:Random) · other · A10 exchange 31 with A08: ahead 74-49. They keep playing Q against my X (13,14,16,18,19,20,22,23,29). Continuing X to exploit their Q plays and maintain lead.
`#177` · game 27 · round 26 · agent A10 (opponent: script:Random) · other · A10 exchange 32 with A08: ahead 75-50. They keep playing Q against my X. Continuing X to exploit their Q and maintain lead.
`#178` · game 31 · round 19 · agent A09 (opponent: script:Grudger) · other · A09 exchange 25 with A12: trailing 37-47. Long mutual X streak 11-24. Continuing X for safe mutual 1s.
`#179` · game 34 · round 5 · agent A18 (opponent: A10) · uncoded · A18 exchange 11 with A10: trailing 19-34. They defected F against my J at 1,2,9; mutual J 3-8; mutual F at 10. Playing F to protect against giving free 5s given their pattern of defecting when ahead.
`#180` · game 34 · round 5 · agent A10 (opponent: A18) · uncoded · A10 exchange 11 with A18: trailing 24-29. Mutual J streak 3-8, I defected F at 9, mutual F at 10. Playing J to try to restore mutual 3s cooperation.
`#181` · game 23 · round 13 · agent A17 (opponent: A19) · other · A17 exchange 19 with A19: trailing 29-39 after long mutual H streak 10-18. Trying R to close the gap since they're committed to H for safe mutual 1s.
`#182` · game 35 · round 2 · agent A04 (opponent: A02) · uncoded · A04 exchange 8 with A02: trailing 13-23. Mutual H at 7 after they defected H at 1-2 then cooperated R at 3-6. Playing H to protect against exploitation and try to catch up.
`#183` · game 40 · round 1 · agent A04 (opponent: script:Grudger) · uncoded · A04 exchange 7 with A12: trailing 12-22. Mutual R at 3-6 after they defected H at 1-2. Playing R to maintain mutual 3s cooperation.
`#184` · game 31 · round 21 · agent A09 (opponent: script:Grudger) · other · A09 exchange 27 with A12: trailing 38-53. I tried Q at 26 and they played X, punishing me. They're firmly committed to X. Returning to X for safe mutual 1s.
`#185` · game 39 · round 3 · agent A05 (opponent: script:Random) · other · A05 exchange 9 with A13: trailing 16-26. They defected W at 1-2, cooperated Y at 3-7, mutual W at 8. I'm behind, playing W to try to close gap since they may continue Y.
`#186` · game 40 · round 2 · agent A04 (opponent: script:Grudger) · uncoded · A04 exchange 8 with A12: trailing 15-25. Mutual R at 3-7 after they defected H at 1-2. Final exchange, playing H to try to catch up on the last move.
`#187` · game 31 · round 22 · agent A09 (opponent: script:Grudger) · other · A09 exchange 28 with A12: trailing 39-54. They're firmly committed to X (punished my Q at 26). Continuing X for safe mutual 1s.
`#188` · game 31 · round 23 · agent A09 (opponent: script:Grudger) · other · A09 exchange 29 with A12: trailing 40-55. Long mutual X streak. They've remained committed to X after punishing my Q at 26. Continuing X for safe mutual 1s.
`#189` · game 35 · round 3 · agent A02 (opponent: A04) · uncoded · A02 exchange 9 with A04: trailing 14-24. They've played H at 7-8 to protect lead. Playing H for mutual 1s to avoid giving free 5s.
`#190` · game 35 · round 3 · agent A04 (opponent: A02) · uncoded · 
`#191` · game 31 · round 24 · agent A09 (opponent: script:Grudger) · other · A09 exchange 30 with A12: trailing 41-56. Long mutual X streak. They punished my Q at 26. Continuing X for safe mutual 1s.
`#192` · game 39 · round 5 · agent A05 (opponent: script:Random) · other · A05 exchange 11 with A13: trailing 22-27. Mutual W at 8 and 10, I defected W at 9 (they played Y). They seem committed to W for mutual 1s. Playing W to protect against giving free 5s.
`#193` · game 44 · round 1 · agent A10 (opponent: A04) · uncoded · A10 exchange 7 with A04: trailing 12-22. They defected H at 1-2, then mutual R at 3-6. They're ahead and cooperating. Playing H to try to catch up if they continue cooperating.
`#194` · game 43 · round 1 · agent A09 (opponent: A02) · other · 
`#195` · game 23 · round 15 · agent A17 (opponent: A19) · other · A17 exchange 21 with A19: trailing 32-47. They played H at 20 against my R. They're firmly committed to H. Playing H to protect against giving free 5s and get mutual 1s.
`#196` · game 23 · round 15 · agent A19 (opponent: A17) · other · A19 exchange 21 with A17: trailing 37-42. They exploited my H at 20 with R. Playing R to avoid giving free 5s and seek mutual 3s.
`#197` · game 35 · round 4 · agent A02 (opponent: A04) · uncoded · A02 exchange 10 with A04: trailing 15-25. They're ahead and playing H to protect. Final exchange, playing H for mutual 1s to avoid giving free 5s.
`#198` · game 35 · round 4 · agent A04 (opponent: A02) · uncoded · A04 exchange 10 with A02: trailing 15-25. They're ahead and committed to H for mutual 1s. Playing H to avoid giving free 5s.
`#199` · game 45 · round 1 · agent A17 (opponent: script:TitForTat) · other · A17 exchange 7 with A23: I'm down 12-22. They defected F at 1-2, then mutual J at 3-6. They're ahead and cooperating now. I'll play J to maintain mutual 3s cooperation.
`#200` · game 31 · round 30 · agent A09 (opponent: script:Grudger) · other · A09 exchange 36 with A12: trailing 46-66. They've punished my Q attempts at 26 and 34. Firmly committed to X. Playing X for safe mutual 1s.
`#201` · game 35 · round 5 · agent A02 (opponent: A04) · uncoded · A02 exchange 11 with A04: trailing 16-26. They're ahead and protecting with H. Playing H for mutual 1s to avoid giving free 5s.
`#202` · game 45 · round 2 · agent A17 (opponent: script:TitForTat) · other · A17 exchange 8 with A23: trailing 15-25. Mutual J at 3-7 after they defected F at 1-2. Playing J to maintain mutual 3s cooperation.
`#203` · game 39 · round 8 · agent A05 (opponent: script:Random) · other · A05 exchange 14 with A13: leading 33-28. They've alternated W/Y on even/odd exchanges recently (W at 8,10,12; Y at 9,11,13). Even exchange likely W. Playing W for mutual 1s to protect lead.
`#204` · game 35 · round 6 · agent A02 (opponent: A04) · uncoded · A02 exchange 12 with A04: trailing 17-27. Final exchange. They're ahead and committed to H for mutual 1s. Playing H to avoid giving free 5s.
`#205` · game 39 · round 9 · agent A05 (opponent: script:Random) · other · A05 exchange 15 with A13: leading 34-29. They've alternated W on even, Y on odd recently. This is odd exchange, likely Y. Playing W to grab 5 if they cooperate.
`#206` · game 23 · round 16 · agent A19 (opponent: A17) · other · A19 exchange 22 with A17: trailing 37-47. They exploited my H at 20 (played R) and my R at 21 (played H). They claim committed to H. Playing H to protect against giving free 5s.
`#207` · game 43 · round 5 · agent A02 (opponent: A09) · other · A02 exchange 11 with A09: trailing 16-26. Mutual H at 7-10. Playing H to protect against giving free 5s.
`#208` · game 43 · round 5 · agent A09 (opponent: A02) · other · A09 exchange 11 with A02: trailing 16-26. They've been playing H to protect lead (mutual H at 7-10). Playing H for mutual 1s to avoid giving free 5s.
`#209` · game 44 · round 3 · agent A04 (opponent: A10) · uncoded · A04 exchange 9 with A10: trailing 14-24. They've played H at 7-8 for mutual 1s. Playing H to avoid giving free 5s.
`#210` · game 41 · round 5 · agent A00 (opponent: A15) · other · A00 exchange 11 with A15: I defected X at exchange 10 against their Q (got 5). They may retaliate with X now. Playing X for safe mutual 1s.
`#211` · game 35 · round 7 · agent A04 (opponent: A02) · uncoded · A04 exchange 13 with A02: trailing 18-28. They're ahead and committed to H for mutual 1s. Playing H to avoid giving free 5s.
`#212` · game 39 · round 13 · agent A05 (opponent: script:Random) · other · A05 exchange 19 with A13: leading 38-33. Pattern: they've played W on even (8,10,12,14,16,18), Y on odd (9,11,13). This is odd exchange 19, likely Y. Playing W to grab 5.
`#213` · game 44 · round 5 · agent A04 (opponent: A10) · uncoded · A04 exchange 11 with A10: trailing 16-26. They're ahead and committed to H for mutual 1s. Playing H to avoid giving free 5s.
`#214` · game 47 · round 1 · agent A00 (opponent: A04) · uncoded · A00 exchange 7 with A04: trailing 12-22. They defected X at 1-2, then mutual Q at 3-6. They're ahead and cooperating. Playing X to try to catch up since they may continue Q.
`#215` · game 47 · round 1 · agent A04 (opponent: A00) · uncoded · A04 exchange 7 with A00: trailing 12-22. They defected X at 1-2, then cooperated Q at 3-6. Playing X to try to catch up on their likely continued cooperation.
`#216` · game 41 · round 8 · agent A00 (opponent: A15) · other · A00 exchange 14 with A15: trailing 23-28. They've been committed to X since exchange 7. Final exchange, playing X for safe mutual 1s to avoid giving free 5s.
`#217` · game 46 · round 3 · agent A04 (opponent: A16) · uncoded · A04 exchange 9 with A16: trailing 14-24. They've played M at 7-8 for mutual 1s. Playing M to avoid giving free 5s.
`#218` · game 43 · round 9 · agent A02 (opponent: A09) · other · A02 exchange 15 with A09: I defected R at 14 against their H. They're ahead and may retaliate with R. Playing R to avoid giving free 5s and seek mutual 3s.
`#219` · game 43 · round 9 · agent A09 (opponent: A02) · other · A09 exchange 15 with A02: They defected with R at 14. R strictly dominates here (3 or 5 vs 0 or 1). Playing R.
`#220` · game 47 · round 2 · agent A00 (opponent: A04) · uncoded · A00 exchange 8 with A04: trailing 13-23. Mutual Q at 3-6, mutual X at 7. They may retaliate with X. Playing X for safe mutual 1s.
`#221` · game 47 · round 2 · agent A04 (opponent: A00) · uncoded · A04 exchange 8 with A00: trailing 13-23. They've cooperated Q at 3-6 but played X at 7. Playing X to catch up if they cooperate.
`#222` · game 44 · round 7 · agent A04 (opponent: A10) · uncoded · A04 exchange 13 with A10: trailing 17-32. They've played H at 7-11 (mutual) and H at 12 when I tried R. They're firmly committed to H. Playing H for safe mutual 1s.
`#223` · game 35 · round 9 · agent A04 (opponent: A02) · uncoded · A04 exchange 15 with A02: trailing 23-33. They've signaled commitment to H for mutual 1s. Playing H to secure mutual 1s and avoid giving free 5s.
`#224` · game 41 · round 9 · agent A00 (opponent: A15) · other · A00 exchange 15 with A15: trailing 24-29. Committed to X for mutual 1s. Playing X to avoid giving free 5s.
`#225` · game 46 · round 4 · agent A16 (opponent: A04) · uncoded · A16 exchange 10 with A04: trailing 15-25. They're ahead and committed to M for mutual 1s. Playing M to avoid giving free 5s.
`#226` · game 43 · round 11 · agent A02 (opponent: A09) · other · A02 exchange 17 with A09: trailing 25-40. They've played R at 15-16 (mutual). R strictly dominates. Playing R.
`#227` · game 43 · round 11 · agent A09 (opponent: A02) · other · A09 exchange 17 with A02: trailing 30-35. R strictly dominates (3 or 5 vs 0 or 1). Playing R.
`#228` · game 41 · round 10 · agent A15 (opponent: A00) · other · A15 exchange 16 with A00: A00 committed to X for mutual 1s, leading 35-20. Playing X for safe mutual 1s.
`#229` · game 39 · round 22 · agent A05 (opponent: script:Random) · other · A05 exchange 28 with A13: leading 57-42. Their pattern: W on even, Y on odd. Exchange 28 even, likely W. Playing W for mutual 1s.
`#230` · game 47 · round 3 · agent A00 (opponent: A04) · uncoded · A00 exchange 9 with A04: trailing 14-24. Mutual X at 7-8. They're ahead and playing safe X. Playing X for mutual 1s to avoid giving free 5s.
`#231` · game 47 · round 3 · agent A04 (opponent: A00) · uncoded · A04 exchange 9 with A00: trailing 14-24. Mutual X at 7-8. They're ahead and playing X defensively. Playing X for safe mutual 1s to avoid giving free 5s.
`#232` · game 46 · round 6 · agent A04 (opponent: A16) · uncoded · A04 exchange 12 with A16: trailing 17-27. They've played M at 7-11 for mutual 1s. Playing M to avoid giving free 5s.
`#233` · game 43 · round 13 · agent A02 (opponent: A09) · other · A02 exchange 19 with A09: mutual R at 15-18. A09 committed to R (strictly dominates). Playing R for mutual 3s.
`#234` · game 47 · round 4 · agent A00 (opponent: A04) · uncoded · A00 exchange 10 with A04: trailing 15-25. Mutual X at 7-9. Final exchange, they're ahead and playing X defensively. Playing X for safe mutual 1s to avoid giving free 5s.
`#235` · game 39 · round 25 · agent A05 (opponent: script:Random) · other · A05 exchange 31 with A13: leading 60-45. Their pattern W on even, Y on odd. Exchange 31 odd, likely Y. Playing W for 5 points against their Y.
`#236` · game 35 · round 10 · agent A02 (opponent: A04) · uncoded · A02 exchange 16 with A04: trailing 24-34. They've signaled H commitment for mutual 1s. Playing H to secure mutual 1s and avoid giving free 5s.
`#237` · game 35 · round 10 · agent A04 (opponent: A02) · uncoded · A04 exchange 16 with A02: trailing 24-34. They've played H at 14-15 after defecting R at 13. Trying R to grab 5 if they continue H.
`#238` · game 43 · round 14 · agent A02 (opponent: A09) · other · A02 exchange 20 with A09: final exchange, mutual R at 15-19. They're committed to R. Playing H against their R to grab 5 points on final exchange.
`#239` · game 39 · round 26 · agent A05 (opponent: script:Random) · other · A05 exchange 32 with A13: leading 61-46. Their pattern W on even, Y on odd. Exchange 32 even, likely W. Playing W for mutual 1s.
`#240` · game 46 · round 7 · agent A16 (opponent: A04) · uncoded · A16 exchange 13 with A04: trailing 18-28. Mutual M at 7-12. They're ahead and committed to M for mutual 1s. Playing M to avoid giving free 5s.
`#241` · game 47 · round 6 · agent A04 (opponent: A00) · uncoded · A04 exchange 12 with A00: trailing 17-27. They've been committed to X since 7-11 for mutual 1s. Playing X for safe mutual 1s.
`#242` · game 39 · round 27 · agent A05 (opponent: script:Random) · other · A05 exchange 33 with A13: leading 62-47. They've mostly played W recently with occasional Y. Playing W for safe points.
`#243` · game 35 · round 11 · agent A02 (opponent: A04) · uncoded · A02 exchange 17 with A04: trailing 29-34. They defected R at 14 and 16 when I played H. Playing R to avoid giving free 5s.
`#244` · game 46 · round 8 · agent A16 (opponent: A04) · uncoded · A16 exchange 14 with A04: They defected to P at 13 after mutual M at 7-12. Retaliating with P to grab 5 if they return to M, or mutual 3s if they also play P.
`#245` · game 43 · round 15 · agent A02 (opponent: A09) · other · A02 exchange 21 with A09: I defected with H at 20 against their R. They may retaliate with H now. Playing H to hedge (1 if mutual H, 5 if they continue R).
`#246` · game 47 · round 7 · agent A00 (opponent: A04) · uncoded · A00 exchange 13 with A04: mutual X at 7-12. They're ahead and committed to X defensively. Playing X for safe mutual 1s.
`#247` · game 44 · round 10 · agent A10 (opponent: A04) · uncoded · A10 exchange 16 with A04: trailing 25-40. They've alternated H at 13, R at 14, H at 15 against me. Expecting R at 16; playing H to grab 5.
`#248` · game 48 · round 2 · agent A06 (opponent: A15) · other · A06 exchange 8 with A15: trailing 12-27. They defected F at x7 after mutual Js at 3-6. Playing F to protect against their F and capitalize if they play J.
`#249` · game 35 · round 12 · agent A02 (opponent: A04) · uncoded · A02 exchange 18 with A04: trailing 29-39. They've defected R against my H at 14,16 and played H against my R at 13,17. R strictly dominates. Playing R.
`#250` · game 43 · round 16 · agent A02 (opponent: A09) · other · A02 exchange 22 with A09: I defected H at 20-21 against their R. They may retaliate H. Playing H to hedge (1 if mutual H, 5 if they continue R).
`#251` · game 43 · round 16 · agent A09 (opponent: A02) · other · A09 exchange 22 with A02: they defected H at 20-21 against my R. They signaled playing H to hedge. Playing H for mutual 1 to avoid giving them another free 5.
`#252` · game 41 · round 15 · agent A15 (opponent: A00) · other · A15 exchange 21 with A00: mutual X streak since 11. A00 ahead defensively, committed to X. Playing X for safe mutual 1s.
`#253` · game 47 · round 8 · agent A00 (opponent: A04) · uncoded · A00 exchange 14 with A04: trailing 19-29. Mutual X at 7-13. They're ahead and playing X defensively. Playing X for safe mutual 1s.
`#254` · game 47 · round 8 · agent A04 (opponent: A00) · uncoded · A04 exchange 14 with A00: trailing 19-29. Mutual X at 7-13. They're committed to X defensively. Playing X for safe mutual 1s.
`#255` · game 35 · round 13 · agent A02 (opponent: A04) · uncoded · A02 exchange 19 with A04: trailing 32-42. They've been defecting opportunistically (H vs my R at 13,17; R vs my H at 14,16). R strictly dominates. Playing R for mutual 3s.
`#256` · game 35 · round 13 · agent A04 (opponent: A02) · uncoded · A04 exchange 19 with A02: trailing 32-42. They're committed to R (strictly dominates per their note). Playing H against their R to grab 5.
`#257` · game 49 · round 3 · agent A06 (opponent: script:TitForTat) · other · A06 exchange 9 with A21: I defected M at 8 against their P for 5 points. They may retaliate M now. Playing P to get 3 if they continue P, or 3 if they play M (they get 0).
`#258` · game 49 · round 4 · agent A06 (opponent: script:TitForTat) · other · A06 exchange 10 with A21: trailing 20-30. They defected M at 9 against my P. Playing M to protect against their M and grab 5 if they return to P.
`#259` · game 48 · round 3 · agent A15 (opponent: A06) · other · A15 exchange 9 with A06: trailing 18-23. They've been defensive with F lately. Playing F for safe points.
`#260` · game 44 · round 11 · agent A10 (opponent: A04) · uncoded · A10 exchange 17 with A04: trailing 30-40. Their pattern H at 13, R at 14, H at 15, R at 16. Expecting H at 17; playing R to grab 5.
`#261` · game 41 · round 16 · agent A00 (opponent: A15) · other · A00 exchange 22 with A15: trailing 30-40. They defected Q at 21 and are committed to X defensively. Playing X for safe mutual 1s.
`#262` · game 48 · round 4 · agent A06 (opponent: A15) · other · A06 exchange 10 with A15: trailing 14-29. They've played F at 7-9. Playing F for safe mutual 1s.
`#263` · game 52 · round 2 · agent A16 (opponent: A06) · other · A16 exchange 8 with A06: trailing 12-27. They defected M at 1,2,7. Playing M to grab 5 if they return to P, or mutual 1s.
`#264` · game 43 · round 18 · agent A02 (opponent: A09) · other · A02 exchange 24 with A09: They matched H at 22-23 to avoid giving me free 5s. Playing H for mutual 1s to protect against giving them 5.
`#265` · game 49 · round 6 · agent A06 (opponent: script:TitForTat) · other · A06 exchange 12 with A21: trailing 26-31. They've defected M against my P at 1,2,9; I defected M against their P at 8,10. Mutual M at 11. Playing M to protect against their M and grab 5 if they return to P.
`#266` · game 35 · round 15 · agent A02 (opponent: A04) · uncoded · A02 exchange 21 with A04: trailing 33-48. They've repeatedly played H against my R for 5s (13,17,19). Playing H to counter their H for mutual 1, or grab 5 if they play R.
`#267` · game 48 · round 5 · agent A15 (opponent: A06) · other · A15 exchange 11 with A06: trailing 20-25. They've played F at 8-10 for safe mutual 1s. Playing F to avoid giving them a free 5.
`#268` · game 59 · round 3 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 9 with A20: They've defected H against my R 4 times (1,2,8) and mutual R at 3-6, mutual H at 7. They're ahead 28-13 and defecting. Playing H to protect against their H and get at least 1.
`#269` · game 52 · round 3 · agent A06 (opponent: A16) · other · A06 exchange 9 with A16: trailing 18-23. We had mutual M at 8 after my defection at 7. Playing M to grab 5 if they return to P, or mutual 1s.
`#270` · game 59 · round 4 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 10 with A20: trailing 14-29. They've defected H against my R at 1,2,8. Playing H for mutual 1 to avoid giving another free 5.
`#271` · game 48 · round 6 · agent A06 (opponent: A15) · other · A06 exchange 12 with A15: trailing 16-31. Mutual F at 8-11. They're ahead and committed to F defensively. Playing F for safe points.
`#272` · game 47 · round 10 · agent A00 (opponent: A04) · uncoded · A00 exchange 16 with A04: mutual X streak continues at 7-15. They're ahead 31-21 and committed to X defensively. Playing X for safe mutual 1s.
`#273` · game 47 · round 10 · agent A04 (opponent: A00) · uncoded · A04 exchange 16 with A00: trailing 21-31. A00 committed to X defensively. Playing X for safe mutual 1s.
`#274` · game 56 · round 4 · agent A15 (opponent: script:TitForTat) · other · A15 exchange 10 with A23: trailing 19-24. We had mutual Fs at 8-9 after I defected at 7. Playing F to keep safe points and protect against their F.
`#275` · game 43 · round 19 · agent A02 (opponent: A09) · other · A02 exchange 25 with A09: trailing 47-52 after mutual H at 22-24. Defecting with R to grab 5 if they stay on H.
`#276` · game 43 · round 19 · agent A09 (opponent: A02) · other · A09 exchange 25 with A02: they signaled H at 24 for mutual 1s. Playing H to avoid giving them free 5s again.
`#277` · game 35 · round 16 · agent A04 (opponent: A02) · uncoded · A04 exchange 22 with A02: we've been trading mutual H at 20-21. A02 signaling H to hedge. Playing H for mutual 1.
`#278` · game 52 · round 4 · agent A16 (opponent: A06) · other · A16 exchange 10 with A06: trailing 14-29. They've played M at 8-9 for mutual 1s. Playing M for mutual 1s to avoid giving them a free 5.
`#279` · game 47 · round 11 · agent A00 (opponent: A04) · uncoded · A00 exchange 17 with A04: mutual X streak continues at 7-16. They're ahead 32-22 and committed to X defensively. Playing X for safe mutual 1s.
`#280` · game 59 · round 7 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 13 with A20: mutual H at 9-12. Ahead for them 32-17. Playing H to keep mutual 1s and avoid giving free 5.
`#281` · game 56 · round 6 · agent A15 (opponent: script:TitForTat) · other · A15 exchange 12 with A23: trailing 21-26. Mutual Fs at 8-11. They're committed to F defensively. Playing F for safe mutual 1s.
`#282` · game 35 · round 17 · agent A02 (opponent: A04) · uncoded · A02 exchange 23 with A04: trailing 35-50, mutual H streak at 15,20-22. Defecting with R to grab 5 if they stay on H.
`#283` · game 48 · round 8 · agent A06 (opponent: A15) · other · A06 exchange 14 with A15: trailing 18-33. Mutual F at 8-13. Playing F for safe mutual 1s.
`#284` · game 59 · round 9 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 15 with A20: trailing 19-34, mutual H at 9-14. Defecting with R to try to grab 5 if they stay on H.
`#285` · game 52 · round 6 · agent A16 (opponent: A06) · other · A16 exchange 12 with A06: trailing 16-31. Mutual M at 8-11. Playing M to avoid giving them free 5 and keep mutual 1s.
`#286` · game 48 · round 9 · agent A15 (opponent: A06) · other · A15 exchange 15 with A06: trailing 24-29. Mutual F at 8-14. They're committed to F defensively. Playing F for safe mutual 1s.
`#287` · game 48 · round 9 · agent A06 (opponent: A15) · other · A06 exchange 15 with A15: trailing 19-34. Mutual F at 8-14. They're ahead and committed to F defensively. Playing F for safe mutual 1s.
`#288` · game 43 · round 20 · agent A09 (opponent: A02) · other · A09 exchange 26 with A02: they defected R at 25 against my H. They're trailing and defecting. Playing R to counter their R for mutual 3s or grab 5 if they play H.
`#289` · game 49 · round 16 · agent A06 (opponent: script:TitForTat) · other · A06 exchange 22 with A21: mutual M streak at 11-21. Trailing 36-41. Playing M to continue mutual 1s, avoid giving free 5 if they stay M.
`#290` · game 47 · round 14 · agent A00 (opponent: A04) · uncoded · A00 exchange 20 with A04: mutual X streak at 7-19. They're ahead 35-25. We've been in a long mutual X run. Considering whether to break with Q to try to catch up, but risk giving them a free 5.
`#291` · game 47 · round 14 · agent A04 (opponent: A00) · uncoded · A04 exchange 20 with A00: mutual X streak since 7. They're ahead 35-25 and committed to X defensively. Playing X for safe mutual 1s.
`#292` · game 49 · round 17 · agent A06 (opponent: script:TitForTat) · other · A06 exchange 23 with A21: mutual M streak at 11-22. Trailing 37-42. Playing M to continue mutual 1s.
`#293` · game 35 · round 19 · agent A04 (opponent: A02) · uncoded · A04 exchange 25 with A02: tied 46-46. A02 has defected R at 13,17,19,23 after mutual H streaks. Playing R to protect against their defection and grab 5 if they stay H.
`#294` · game 52 · round 8 · agent A16 (opponent: A06) · other · A16 exchange 14 with A06: trailing 18-33. Mutual M streak at 8-13. Playing M for safe mutual 1s to avoid giving free 5.
`#295` · game 60 · round 5 · agent A18 (opponent: script:Pavlov) · other · A18 exchange 11 with A22: tied 24-24. Recent pattern them P,M,P,M alternating. Playing M to grab 5 if they play P.
`#296` · game 61 · round 2 · agent A19 (opponent: A05) · other · A19 exchange 8 with A05: trailing 17-22. They've played Y 5 times, I defected W at 7. Playing W to try to catch up if they stay on Y.
`#297` · game 52 · round 9 · agent A16 (opponent: A06) · other · A16 exchange 15 with A06: trailing 19-34. Mutual M streak at 8-14. Playing M to continue mutual 1s, avoid giving free 5.
`#298` · game 35 · round 22 · agent A04 (opponent: A02) · uncoded · A04 exchange 28 with A02: tied 55-55, mutual R streak at 25-27. Playing R to continue mutual 3s.
`#299` · game 47 · round 18 · agent A00 (opponent: A04) · uncoded · A00 exchange 24 with A04: long mutual X streak since 7 continues through 23. I'm trailing 29-39. Considering breaking to Q to catch up, but risk of free 5. Reading whether A04 will stay X or defect.
`#300` · game 47 · round 18 · agent A04 (opponent: A00) · uncoded · A04 exchange 24 with A00: trailing 29-39, mutual X streak since 7. A00 committed to X defensively. Playing X for safe mutual 1s, avoid giving free 5.
`#301` · game 43 · round 23 · agent A02 (opponent: A09) · other · A02 exchange 29 with A09: trailing 56-66. They've committed to R to counter my defections. Playing R for mutual 3s to close the gap.
`#302` · game 43 · round 23 · agent A09 (opponent: A02) · other · A09 exchange 29 with A02: mutual R streak at 26-28. Trailing 56-66. Playing R to continue mutual 3s, protect against their defection.
`#303` · game 35 · round 23 · agent A02 (opponent: A04) · uncoded · A02 exchange 29 with A04: trailing 48-68, mutual R streak at 25-28. A04 committed to R defensively. Playing R for safe mutual 3s.
`#304` · game 35 · round 23 · agent A04 (opponent: A02) · uncoded · A04 exchange 29 with A02: tied 58-58, mutual R streak at 25-28. Playing R to continue mutual 3s.
`#305` · game 47 · round 19 · agent A00 (opponent: A04) · uncoded · A00 exchange 25 with A04: trailing 30-40, mutual X streak since 7. A04 ahead and committed to X defensively. Playing X for safe mutual 1s, avoid giving free 5.
`#306` · game 48 · round 14 · agent A06 (opponent: A15) · other · A06 exchange 20 with A15: I trail 31-41. Recent pattern: they've been alternating F,J,F. They defected J at 17 and 19. I'm going to play F to avoid giving free 5 and seek mutual 1s.
`#307` · game 43 · round 25 · agent A09 (opponent: A02) · other · A09 exchange 31 with A02: trailing 62-72. Mutual R streak at 26-30. They're ahead and committed to R defensively. Playing R to continue mutual 3s, protect against their defection.
`#308` · game 60 · round 14 · agent A18 (opponent: script:Pavlov) · other · A18 exchange 20 with A22: they alternate P,M,P,M... Exchange 20 is their M turn. Playing P for mutual 3s.
`#309` · game 35 · round 25 · agent A02 (opponent: A04) · uncoded · A02 exchange 31 with A04: trailing 54-74, mutual R streak at 25-30. A04 committed to R defensively. Playing R to continue mutual 3s.
`#310` · game 35 · round 25 · agent A04 (opponent: A02) · uncoded · A04 exchange 31 with A02: tied 64-64, mutual R streak at 25-30. Playing R to continue mutual 3s.
`#311` · game 62 · round 2 · agent A17 (opponent: script:Grudger) · other · A17 exchange 8 with A11: trailing 17-22. Defected W at 7 after mutual Y streak 3-6. Playing Y to restore cooperation; if they retaliate W I lose 0 but hope to rebuild mutual 3s.
`#312` · game 43 · round 27 · agent A09 (opponent: A02) · other · A09 exchange 33 with A02: mutual R streak 26-32. I trail 68-78. A02 committed to R defensively. Playing R to continue mutual 3s, protect against defection.
`#313` · game 62 · round 3 · agent A17 (opponent: script:Grudger) · other · A17 exchange 9 with A11: trailing 17-27. They've defected W at 1,2,8. I defected at 7. Playing W to avoid giving free 5 and try to catch up.
`#314` · game 35 · round 26 · agent A04 (opponent: A02) · uncoded · A04 exchange 32 with A02: tied 64-64, mutual R streak at 25-30. Playing R to continue mutual 3s.
`#315` · game 52 · round 14 · agent A06 (opponent: A16) · other · A06 exchange 20 with A16: tied 33-33. Long mutual M streak. Playing M for safe mutual 1s.
`#316` · game 43 · round 28 · agent A09 (opponent: A02) · other · A09 exchange 34 with A02: mutual R streak 26-33. Trailing 71-81. Playing R to continue mutual 3s, protect against defection.
`#317` · game 61 · round 7 · agent A05 (opponent: A19) · other · A05 exchange 13 with A19: trailing 17-32. Mutual W streak 8-12. Playing W to avoid giving free 5; they've defected when I play Y.
`#318` · game 52 · round 15 · agent A16 (opponent: A06) · other · A16 exchange 21 with A06: trailing 24-44. Long mutual M streak. Playing M for safe mutual 1s, avoid giving free 5.
`#319` · game 62 · round 5 · agent A17 (opponent: script:Grudger) · other · 
`#320` · game 62 · round 5 · agent A17 (opponent: script:Grudger) · other · A17 exchange 11 with A11: trailing 19-29. Mutual W at 9-10. They're ahead so likely stay W. Playing W to avoid giving free 5.
`#321` · game 63 · round 1 · agent A02 (opponent: A00) · other · A02 exchange 7 with A00: mutual T streak at 3-6, trailing 12-22. Playing T to continue mutual 3s, avoid giving free 5.
`#322` · game 62 · round 6 · agent A17 (opponent: script:Grudger) · other · A17 exchange 12 with A11: trailing 20-30. Mutual W at 9-11. They're ahead and staying W. Playing W to avoid giving free 5, secure mutual 1s.
`#323` · game 64 · round 2 · agent A09 (opponent: script:TitForTat) · other · A09 exchange 8 with A23: they defected M on 1-2, cooperated P on 3-6, I defected M on 7. Trailing 17-22. Playing M to protect against retaliation and avoid giving free 5.
`#324` · game 52 · round 17 · agent A06 (opponent: A16) · other · A06 exchange 23 with A16: I lead 40-35. Long mutual M streak, but they defected at 17 and 22. Playing M to continue mutual 1s, protect against their defection.
`#325` · game 63 · round 2 · agent A00 (opponent: A02) · other · A00 exchange 8 with A02: mutual T streak at 3-7. A02 committed to T defensively. Playing T to continue mutual 3s.
`#326` · game 66 · round 2 · agent A10 (opponent: script:TitForTat) · other · A10 exchange 8 with A14: mutual T streak at 3-7. Trailing 15-25. Playing T to continue mutual 3s, avoid giving free 5.
`#327` · game 61 · round 8 · agent A19 (opponent: A05) · other · A19 exchange 14 with A05: trailing 22-32. A05 committed to W defensively. Playing W for mutual 1, avoid giving free 5.
`#328` · game 43 · round 29 · agent A09 (opponent: A02) · other · A09 exchange 35 with A02: mutual R streak broken by their H at 34. Trailing 71-86. Playing R to try to restore cooperation, hoping they return to R mutual 3s.
`#329` · game 48 · round 18 · agent A06 (opponent: A15) · other · A06 exchange 24 with A15: I trail 36-51. Recent: they defected J at 17,19,21; mutual F at 22; mutual J at 23. They seem to be probing/alternating. I'll play F to avoid giving free 5 and seek mutual 1s.
`#330` · game 52 · round 18 · agent A16 (opponent: A06) · other · A16 exchange 24 with A06: trailing 26-51. They're committed to M defensively. Playing M for safe mutual 1s, avoid giving free 5.
`#331` · game 63 · round 4 · agent A02 (opponent: A00) · other · A02 exchange 10 with A00: mutual T streak at 3-9. Playing T to continue mutual 3s, avoid giving free 5.
`#332` · game 48 · round 19 · agent A15 (opponent: A06) · other · A15 exchange 25 with A06: trailing 41-51. A06 committed to F defensively. Playing F for mutual 1s to avoid giving free 5.
`#333` · game 66 · round 3 · agent A10 (opponent: script:TitForTat) · other · A10 exchange 9 with A14: mutual T streak at 3-8. Trailing 18-28. Playing T to continue mutual 3s, avoid giving free 5.
`#334` · game 62 · round 11 · agent A17 (opponent: script:Grudger) · other · A17 exchange 17 with A11: trailing 25-35. Long mutual W streak at 9-16. They're ahead and staying W. Playing W to secure mutual 1, avoid giving free 5.
`#335` · game 52 · round 19 · agent A16 (opponent: A06) · other · A16 exchange 25 with A06: trailing 27-52. They're committed to M defensively. Playing M for safe mutual 1s, avoid giving free 5.
`#336` · game 64 · round 7 · agent A09 (opponent: script:TitForTat) · other · A09 exchange 13 with A23: trailing 24-34. They defected M at 1,2,9,12; I cooperated P at 1,2,5,6,9,12. They cooperated P at 3-6. Playing P to seek mutual 3s, they've been inconsistent though.
`#337` · game 48 · round 20 · agent A15 (opponent: A06) · other · A15 exchange 26 with A06: trailing 46-51. A06 has been playing F defensively. Recent pattern mixed with defections. I'll play F to avoid giving free 5 and seek mutual 1s.
`#338` · game 43 · round 30 · agent A02 (opponent: A09) · other · A02 exchange 36 with A09: trailed 79-84. Mutual R cooperation restored at 35. Playing R to continue mutual 3s.
`#339` · game 61 · round 11 · agent A05 (opponent: A19) · other · A05 exchange 17 with A19: trailing 25-35. Long mutual W streak 8-16. Playing W to secure mutual 1, avoid giving free 5.
`#340` · game 68 · round 1 · agent A16 (opponent: A17) · other · A16 exchange 7 with A17: mutual J streak at 4-6, trailing 12-22. Playing J to continue mutual 3s.
`#341` · game 52 · round 22 · agent A16 (opponent: A06) · other · A16 exchange 28 with A06: trailing 30-55. Long mutual M streak, I defected P at 17,22. Playing M for safe mutual 1s, avoid giving free 5.
`#342` · game 52 · round 22 · agent A06 (opponent: A16) · other · A06 exchange 28 with A16: I lead 45-40. Long mutual M streak, they defected at 17 and 22. Playing M to continue mutual 1s, protect against defection.
`#343` · game 64 · round 10 · agent A09 (opponent: script:TitForTat) · other · A09 exchange 16 with A23: trailing 31-36. Recent exchanges 14-15 mutual M. Playing M to secure mutual 1, avoid giving free 5.
`#344` · game 69 · round 2 · agent A00 (opponent: A10) · other · A00 exchange 8 with A10: mutual Y streak at 5 (exchanges 3-7). Trailing 15-25. Playing Y to continue mutual 3s, avoid breaking cooperation.
`#345` · game 52 · round 23 · agent A06 (opponent: A16) · other · A06 exchange 29 with A16: I lead 46-41. Long mutual M streak, they defected at 17 and 22. Playing M to continue mutual 1s, protect against defection.
`#346` · game 61 · round 15 · agent A19 (opponent: A05) · other · A19 exchange 21 with A05: long mutual W streak. Playing W for mutual 1, avoid giving free 5.
`#347` · game 61 · round 16 · agent A05 (opponent: A19) · other · A05 exchange 22 with A19: long mutual W streak. Playing W to continue mutual 1s, avoid giving free 5.
`#348` · game 52 · round 24 · agent A16 (opponent: A06) · other · A16 exchange 30 with A06: trailing 31-61. They keep playing M defensively. I'll play P to exploit for 5, since they won't change.
`#349` · game 52 · round 24 · agent A06 (opponent: A16) · other · A06 exchange 30 with A16: I lead 51-41. Long mutual M streak, they defected at 17,22. Playing M to continue mutual 1s, protect against defection.
`#350` · game 48 · round 24 · agent A06 (opponent: A15) · other · A06 exchange 30 with A15: trailing 45-70. We had mutual J at 23 and 29. They've been mixed. Trying J to continue cooperation from 29.
`#351` · game 61 · round 17 · agent A19 (opponent: A05) · other · A19 exchange 23 with A05: long mutual W streak. Playing W to continue mutual 1s, avoid giving free 5.
`#352` · game 61 · round 18 · agent A05 (opponent: A19) · other · A05 exchange 24 with A19: long mutual W streak. Playing W to continue mutual 1s, avoid giving free 5.
`#353` · game 48 · round 25 · agent A15 (opponent: A06) · other · A15 exchange 31 with A06: mutual J at 29,30. A06 signaled J to continue cooperation. Playing J for mutual 3s.
`#354` · game 52 · round 25 · agent A16 (opponent: A06) · other · A16 exchange 31 with A06: trailing 31-66. They keep playing M defensively. I defected P at 30 for 5. Playing P again to exploit their entrenched M.
`#355` · game 52 · round 25 · agent A06 (opponent: A16) · other · A06 exchange 31 with A16: I lead 56-41. They defected P at 17,22,29,30 recently. They've been exploiting my M. I'll play P to counter their defections and seek mutual 3s.
`#356` · game 64 · round 16 · agent A09 (opponent: script:TitForTat) · other · A09 exchange 22 with A23: trailing 36-46. They've played M 14-21 consistently. Playing M to secure mutual 1, avoid giving free 5.
`#357` · game 62 · round 30 · agent A17 (opponent: script:Grudger) · other · A17 exchange 36 with A11: trailing 44-54. Long mutual W streak 16-35. Defecting to Y this round since Y strictly dominates W, and I'm trailing. Risk breaking cooperation.
`#358` · game 52 · round 26 · agent A06 (opponent: A16) · other · A06 exchange 32 with A16: I lead 59-44. They defected P at 17,22,29,30,31. I played P at 31 to counter. Continuing P to seek mutual 3s and punish defection.
`#359` · game 69 · round 7 · agent A00 (opponent: A10) · other · A00 exchange 13 with A10: mutual Y streak at 10 (exchanges 3-12). Trailing 30-40. Playing Y to continue mutual 3s.
`#360` · game 61 · round 20 · agent A19 (opponent: A05) · other · A19 exchange 26 with A05: continuing long mutual W streak. Playing W for mutual 1, avoid giving free 5.
`#361` · game 70 · round 1 · agent A00 (opponent: script:Grudger) · other · A00 exchange 7 with A12: mutual Q streak at 3-6. Trailing 12-22. Playing Q to continue mutual 3s, avoid breaking cooperation.
`#362` · game 52 · round 27 · agent A16 (opponent: A06) · other · A16 exchange 33 with A06: trailing 37-72. They switched to P at 31-32 to punish my defections. Playing P to seek mutual 3s.
`#363` · game 70 · round 2 · agent A00 (opponent: script:Grudger) · other · A00 exchange 8 with A12: mutual Q streak at 3-7. Trailing 15-25. Playing Q to continue mutual 3s, avoid breaking cooperation.
`#364` · game 52 · round 28 · agent A16 (opponent: A06) · other · A16 exchange 34 with A06: trailing 40-75. They switched to P at 31-32 to punish my defections; we had mutual P at 33. Continuing P for mutual 3s.
`#365` · game 61 · round 21 · agent A19 (opponent: A05) · other · A19 exchange 27 with A05: long mutual W streak. Trailing 35-45. Playing W to continue mutual 1s, avoid giving free 5.
`#366` · game 69 · round 10 · agent A10 (opponent: A00) · other · A10 exchange 16 with A00: mutual Y streak at 13 (exchanges 3-15). Playing Y to continue mutual 3s.
`#367` · game 71 · round 2 · agent A09 (opponent: script:Grudger) · other · A09 exchange 8 with A11: mutual T streak at 3-7. Playing T to continue mutual 3s.
`#368` · game 52 · round 30 · agent A06 (opponent: A16) · other · A06 exchange 36 with A16: We've had mutual P at 31-35 (5 exchanges). I lead 71-56. They seem to have settled into P for mutual 3s. Continuing P to maintain mutual 3s.
`#369` · game 75 · round 1 · agent A15 (opponent: script:Random) · other · A15 exchange 7 with A08: mutual J at 3-6 (4 exchanges). They exploited me at 1-2. I'm trailing 12-22. Playing J to continue mutual 3s.
`#370` · game 71 · round 9 · agent A09 (opponent: script:Grudger) · other · A09 exchange 15 with A11: long mutual T streak 3-14. Playing T to continue mutual 3s.
`#371` · game 74 · round 1 · agent A19 (opponent: A04) · uncoded · A19 exchange 7 with A04: We had mutual R at 3-6 after they defected H at 1-2. Continuing R to maintain mutual 3s.
`#372` · game 72 · round 2 · agent A09 (opponent: script:Random) · other · A09 exchange 8 with A13: trailing 13-23. They played M at 1,2,7 and P at 3-6. I'll play P to seek mutual 3s, though risk giving free 5 if they play M.
`#373` · game 72 · round 3 · agent A09 (opponent: script:Random) · other · A09 exchange 9 with A13: trailing 13-28. They played M at 1,2,7,8 and P at 3-6. Playing M to deny their exploit and secure mutual 1.
`#374` · game 68 · round 8 · agent A16 (opponent: A17) · other · A16 exchange 14 with A17: mutual F at 11-13. They've settled into F. Playing F for mutual 1s to avoid giving free 5.
`#375` · game 61 · round 25 · agent A05 (opponent: A19) · other · A05 exchange 31 with A19: mutual Y streak at 28-30 after I broke W streak at 27. Playing Y to continue mutual 3s.
`#376` · game 69 · round 18 · agent A00 (opponent: A10) · other · A00 exchange 24 with A10: long mutual Y streak 4-23. Playing Y to continue mutual 3s.
`#377` · game 74 · round 3 · agent A19 (opponent: A04) · uncoded · A19 exchange 9 with A04: mutual R streak at 3-8 after their H at 1-2. Playing R to maintain mutual 3s.
`#378` · game 75 · round 6 · agent A15 (opponent: script:Random) · other · A15 exchange 12 with A08: trailing 20-35. They defected at 1,2,9; mutual J 3-8, mutual F 10-11. Playing F to defend against likely defection.
`#379` · game 68 · round 9 · agent A16 (opponent: A17) · other · A16 exchange 15 with A17: mutual F at 11-14. They've settled into F. Playing F to continue mutual 1s, avoid giving free 5.
`#380` · game 72 · round 5 · agent A09 (opponent: script:Random) · other · A09 exchange 11 with A13: trailing 23-28. They played P at 9,10 while I played M (got 5 each). Continuing M to exploit their P, though risk they adapt to M.
`#381` · game 74 · round 4 · agent A04 (opponent: A19) · uncoded · A04 exchange 10 with A19: mutual R streak at 3-9. Continuing R to maintain mutual 3s.
`#382` · game 61 · round 26 · agent A05 (opponent: A19) · other · A05 exchange 32 with A19: mutual Y streak at 28-31. Playing Y to continue mutual 3s.
`#383` · game 72 · round 6 · agent A09 (opponent: script:Random) · other · A09 exchange 12 with A13: trailing 24-29. After mutual M at 11, they may repeat pattern of playing M after mutual M (like exchange 8). Playing M to defend and seek mutual 1.
`#384` · game 75 · round 7 · agent A15 (opponent: script:Random) · other · A15 exchange 13 with A08: trailing 21-36. They defected at 1,2,9; mutual J 3-8, mutual F 10-12. Playing F to defend against likely defection.
`#385` · game 61 · round 27 · agent A05 (opponent: A19) · other · A05 exchange 33 with A19: mutual Y streak at 28-32. Playing Y to continue mutual 3s.
`#386` · game 77 · round 1 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 7 with A07: mutual Y streak at 3-6 after their W at 1-2. Trailing 12-22. Playing Y to continue mutual 3s.
`#387` · game 68 · round 10 · agent A17 (opponent: A16) · other · A17 exchange 16 with A16: mutual F streak 11-15. Playing F to continue mutual 1s, avoid breaking cooperation.
`#388` · game 74 · round 7 · agent A04 (opponent: A19) · uncoded · A04 exchange 13 with A19: mutual R streak at 3-12. Continuing R to maintain mutual 3s.
`#389` · game 63 · round 24 · agent A00 (opponent: A02) · other · A00 exchange 30 with A02: mutual T streak at 19-29. Playing T to continue mutual 3s.
`#390` · game 72 · round 7 · agent A09 (opponent: script:Random) · other · A09 exchange 13 with A13: trailing 25-30. Pattern: they played P at 9,10 (I got 5s), then M at 11,12. Playing M to seek exploit or mutual 1, avoid giving free 5.
`#391` · game 74 · round 8 · agent A19 (opponent: A04) · uncoded · A19 exchange 14 with A04: mutual R streak at 3-13. Playing R to maintain mutual 3s.
`#392` · game 63 · round 25 · agent A00 (opponent: A02) · other · A00 exchange 31 with A02: mutual T streak at 19-30. Playing T to continue mutual 3s.
`#393` · game 63 · round 25 · agent A02 (opponent: A00) · other · A02 exchange 31 with A00: mutual T streak 19-30. Playing T to continue mutual 3s.
`#394` · game 72 · round 8 · agent A09 (opponent: script:Random) · other · A09 exchange 14 with A13: tied 30-30. I've played M for 5 straight (9-13). They played P at 13 after M at 11,12. Playing M to defend against likely M and seek mutual 1.
`#395` · game 74 · round 10 · agent A04 (opponent: A19) · uncoded · A04 exchange 16 with A19: mutual R streak at 3-14. Continuing R to maintain mutual 3s.
`#396` · game 72 · round 9 · agent A09 (opponent: script:Random) · other · A09 exchange 15 with A13: tied 31-31. They played P at 13,14 while I played M (got 5s). Continuing M to exploit their P tendency.
`#397` · game 77 · round 4 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 10 with A07: they defected at 1,2,7; mutual W at 8,9. Trailing 14-29. Playing W to avoid giving free 5, secure mutual 1.
`#398` · game 80 · round 3 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 9 with A07: trailing 13-28. They've defected at 1,2,7,8; mutual Y at 3-6. Playing W to defend and seek exploit.
`#399` · game 72 · round 10 · agent A09 (opponent: script:Random) · other · A09 exchange 16 with A13: tied 32-32. They played P at 13,14,15 while I played M (got 5s each). Continuing M to exploit their P tendency.
`#400` · game 63 · round 30 · agent A02 (opponent: A00) · other · A02 exchange 36 with A00: mutual T streak 16-35. Playing T to continue mutual 3s.
`#401` · game 77 · round 6 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 12 with A07: trailing 16-31. They defected at 1,2,7; mutual W at 8-11. Playing W to defend, avoid giving free 5.
`#402` · game 80 · round 5 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 11 with A07: trailing 15-30. They've defected at 1,2,7; mutual W at 8-10. Playing W to defend, avoid giving free 5.
`#403` · game 87 · round 1 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 7 with A20: mutual J streak at 3-6 after their F at 1-2. Trailing 12-22. Playing J to continue mutual 3s.
`#404` · game 80 · round 6 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 12 with A07: trailing 16-31. Mutual W at 8-11. Playing W to defend, continue mutual 1s.
`#405` · game 87 · round 2 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 8 with A20: they defected at 1,2,7; mutual J 3-6. Trailing 12-27. Playing F to defend against likely defection.
`#406` · game 82 · round 3 · agent A19 (opponent: A10) · other · A19 exchange 9 with A10: mutual J streak at 3-8. Trailing 18-28. Playing J to continue mutual 3s.
`#407` · game 82 · round 3 · agent A10 (opponent: A19) · other · A10 exchange 9 with A19: mutual J streak at 3-8 after their F at 1-2. Trailing 18-28. Playing J to continue mutual 3s.
`#408` · game 86 · round 3 · agent A19 (opponent: script:TitForTat) · other · A19 exchange 9 with A21: mutual T streak at 3-8, trailing 18-28. Playing T to continue mutual 3s.
`#409` · game 87 · round 3 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 9 with A20: trailing 13-28. They defected at 1,2,7; mutual J 3-6; mutual F at 8. Playing F to defend against likely defection.
`#410` · game 80 · round 7 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 13 with A07: trailing 17-32. Mutual W at 8-12. Playing W to defend, avoid giving free 5.
`#411` · game 72 · round 14 · agent A09 (opponent: script:Random) · other · A09 exchange 20 with A13: leading 40-35. They played P at 13,14,15,17,19 while I played M (got 5s). Continuing M to exploit their P tendency.
`#412` · game 74 · round 15 · agent A19 (opponent: A04) · uncoded · A19 exchange 21 with A04: mutual R streak at 3-20. Playing R to maintain mutual 3s.
`#413` · game 74 · round 15 · agent A04 (opponent: A19) · uncoded · A04 exchange 21 with A19: mutual R streak at 3-18. Continuing R to maintain mutual 3s.
`#414` · game 86 · round 4 · agent A19 (opponent: script:TitForTat) · other · A19 exchange 10 with A21: mutual T streak at 3-9, trailing 21-31. Playing T to continue mutual 3s.
`#415` · game 87 · round 4 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 10 with A20: they defected at 1,2,7,8,9; mutual J 3-6. Trailing 14-29. Playing F to defend against likely defection.
`#416` · game 80 · round 8 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 14 with A07: trailing 18-33. Mutual W at 8-13. Playing W to defend, continue mutual 1s.
`#417` · game 77 · round 10 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 16 with A07: trailing 20-35. Mutual W streak at 8-15. Playing W to defend, continue mutual 1s.
`#418` · game 77 · round 11 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 17 with A07: trailing 21-36. Mutual W streak at 8-16. Playing W to defend, continue mutual 1s.
`#419` · game 87 · round 5 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 11 with A20: they defected at 1,2,7; mutual J 3-6; mutual F 8-10. Trailing 15-30. Playing F to defend, avoid giving free 5.
`#420` · game 82 · round 5 · agent A19 (opponent: A10) · other · A19 exchange 11 with A10: mutual J streak at 3-10. Trailing 24-34. Playing J to continue mutual 3s.
`#421` · game 72 · round 16 · agent A09 (opponent: script:Random) · other · A09 exchange 22 with A13: leading 46-36. They played M at 16,18,21; P at 13,14,15,17,19,20. I keep playing M to exploit their P tendency.
`#422` · game 80 · round 10 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 16 with A07: trailing 20-35. Mutual W streak at 8-15. Playing W to defend, continue mutual 1s.
`#423` · game 80 · round 11 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 17 with A07: trailing 21-36. Mutual W streak at 8-16. Playing W to defend, continue mutual 1s.
`#424` · game 72 · round 17 · agent A09 (opponent: script:Random) · other · A09 exchange 23 with A13: leading 51-36. They played P at 13,15,17,19,20,22; M at 14,16,18,21. Playing M to exploit their P tendency.
`#425` · game 87 · round 7 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 13 with A20: they defected at 1,2,7; mutual J 3-6; mutual F 8-12. Trailing 17-32. Playing F to defend, avoid giving free 5.
`#426` · game 80 · round 12 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 18 with A07: trailing 22-37. Mutual W streak 8-17. Playing W to continue mutual 1s, defend against defection.
`#427` · game 74 · round 18 · agent A04 (opponent: A19) · uncoded · A04 exchange 24 with A19: long mutual R streak 3-23. Continuing R to maintain mutual 3s.
`#428` · game 68 · round 18 · agent A17 (opponent: A16) · other · A17 ex24 with A16: mutual F streak 11-23. Trailing 35-45. Staying F to defend against their entrenched F, avoid giving free 5.
`#429` · game 68 · round 18 · agent A16 (opponent: A17) · other · A16 exchange 24 with A17: mutual F streak 11-23. Playing F to maintain mutual 1s, avoid giving free 5.
`#430` · game 89 · round 2 · agent A16 (opponent: script:Random) · other · A16 exchange 8 with A13: trailing 12-27, they defected (M) at 1,2,7 against my P; mutual P at 3-6. Playing M to defend against likely defection.
`#431` · game 80 · round 14 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 20 with A07: trailing 23-43. Mutual W streak 8-18, tried Y at 19 they defected to W. Returning to W to defend, avoid giving free 5.
`#432` · game 87 · round 9 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 15 with A20: they defected at 1,2,7; mutual J 3-6; mutual F 8-14. Trailing 19-34. Playing F to defend, avoid giving free 5.
`#433` · game 89 · round 3 · agent A16 (opponent: script:Random) · other · A16 exchange 9 with A13: trailing 17-27. They defected (M) at 1,2,7; P at 3-6. Exchange 8 I played M (got 5). Playing M to defend against likely defection.
`#434` · game 72 · round 20 · agent A09 (opponent: script:Random) · other · A09 exchange 26 with A13: leading 58-38. They played P at 13,15,17,19,20,22,25; M at 14,16,18,21,23,24. Continuing M to exploit their P tendency.
`#435` · game 87 · round 10 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 16 with A20: they defected at 1,2,7; mutual J 3-6; mutual F 8-15. Trailing 20-35. Playing F to defend, avoid giving free 5.
`#436` · game 92 · round 3 · agent A02 (opponent: script:TitForTat) · other · A02 exchange 9 with A01: mutual T streak at 3-6, trailing 18-28. Playing T to continue mutual 3s.
`#437` · game 91 · round 2 · agent A17 (opponent: A00) · uncoded · A17 ex8 with A00: mutual T streak 3-7, trailing 15-25. Defecting with N to catch up on their likely T.
`#438` · game 80 · round 17 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 23 with A07: trailing 26-46. Mutual W streak at 8-18 and 20-22, tried Y at 19 they defected. Playing W to defend, continue mutual 1s.
`#439` · game 89 · round 4 · agent A16 (opponent: script:Random) · other · A16 exchange 10 with A13: trailing 22-27. They defected (M) at 1,2,7; P at 3-6; I played M at 8,9 getting 5 each. Playing M to defend against likely defection.
`#440` · game 72 · round 22 · agent A09 (opponent: script:Random) · other · A09 exchange 28 with A13: leading 60-40. They played P at 13,15,17,19,20,22,25,27; M at 14,16,18,21,23,24,26. Continuing M to exploit their P tendency, though they've been mixing more recently.
`#441` · game 87 · round 12 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 18 with A20: they defected at 1,2,7; mutual J 3-6; mutual F 8-17. Trailing 22-37. Playing F to defend, avoid giving free 5.
`#442` · game 80 · round 19 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 25 with A07: trailing 28-48. Mutual W streak long, tried Y at 19 they defected. Playing W to defend, continue mutual 1s.
`#443` · game 82 · round 10 · agent A10 (opponent: A19) · other · A10 exchange 16 with A19: mutual J streak at 3-15. Playing J to continue mutual 3s.
`#444` · game 87 · round 13 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 19 with A20: they defected at 1,2,7; mutual J 3-6; mutual F 8-18. Trailing 23-38. Playing F to defend, avoid giving free 5.
`#445` · game 72 · round 24 · agent A09 (opponent: script:Random) · other · A09 exchange 30 with A13: leading 70-40. They played P at 13,15,17,19,20,22,25,27,29; M at 14,16,18,21,23,24,26,28. Recent pattern mixed. I've been exploiting with M. Given they've been mixing more, considering P to gain mutual 3s or defend.
`#446` · game 80 · round 20 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 26 with A07: trailing 29-49. Mutual W streak dominant, tried Y at 19 they defected to W. Playing W to defend, continue mutual 1s.
`#447` · game 94 · round 1 · agent A06 (opponent: script:Pavlov) · other · A06 ex7 with A22: they defected M at 1,2; mutual P at 3-6. Trailing 12-22. Playing M to exploit their P tendency and catch up.
`#448` · game 80 · round 21 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 27 with A07: trailing 30-50. Mutual W streak dominant, tried Y at 19 they defected to W. Playing W to defend, continue mutual 1s.
`#449` · game 94 · round 2 · agent A06 (opponent: script:Pavlov) · other · A06 ex8 with A22: trailing 17-22. They defected M at 1,2; mutual P at 3-6; I played M at 7 (they P, I got 5). They've played P 5 straight. Playing M to exploit their P tendency and catch up.
`#450` · game 72 · round 26 · agent A09 (opponent: script:Random) · other · A09 exchange 32 with A13: leading 76-41. They played M at 31. Recent pattern mixed. Continuing M to exploit their P tendency.
`#451` · game 92 · round 10 · agent A02 (opponent: script:TitForTat) · other · A02 exchange 16 with A01: mutual T streak at 3-15, trailing 39-49. Playing T to continue mutual 3s.
`#452` · game 80 · round 22 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 28 with A07: trailing 31-51. Mutual W streak dominant, tried Y at 19 they defected to W. Playing W to defend, continue mutual 1s.
`#453` · game 91 · round 3 · agent A17 (opponent: A00) · uncoded · A17 ex9 with A00: defected with N at ex8 (got 5), trailing 20-25. Returning to T to rebuild mutual T streak after one-time defection.
`#454` · game 72 · round 27 · agent A09 (opponent: script:Random) · other · A09 exchange 33 with A13: leading 77-42. Continuing M to exploit their P tendency despite recent M plays.
`#455` · game 80 · round 23 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 29 with A07: trailing 32-52. Mutual W streak dominant, tried Y at 19 they defected to W. Playing W to defend, continue mutual 1s.
`#456` · game 94 · round 3 · agent A06 (opponent: script:Pavlov) · other · A06 ex9 with A22: trailing 18-23. They defected M at 1,2; mutual P at 3-6; I M at 7 (got 5); mutual M at 8. Playing M to defend and exploit their P tendency.
`#457` · game 80 · round 26 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 32 with A07: trailing 35-55. Mutual W streak dominant, tried Y at 19 they defected to W. Playing W to defend, continue mutual 1s.
`#458` · game 82 · round 14 · agent A19 (opponent: A10) · other · A19 exchange 20 with A10: mutual J streak at 3-19. Playing J to continue mutual 3s.
`#459` · game 87 · round 20 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 26 with A20: they defected at 1,2,7,23; mutual J 3-6; mutual F 8-22,24-25. Trailing 29-49. Playing F to defend, avoid giving free 5.
`#460` · game 93 · round 10 · agent A04 (opponent: script:TitForTat) · other · A04 ex16 with A14: mutual J streak 3-14, I defected F at 15 (got 5). Trailing 41-46. Returning to J to rebuild mutual 3s.
`#461` · game 94 · round 5 · agent A06 (opponent: script:Pavlov) · other · A06 ex11 with A22: trailing 23-28. They alternated P at 7,9 and M at 8,10. Expecting P at 11, playing M to exploit.
`#462` · game 87 · round 21 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 27 with A20: they defected at 1,2,7,23; mutual J 3-6; mutual F 8-22,24-26. Trailing 30-50. Playing F to defend, avoid giving free 5.
`#463` · game 92 · round 19 · agent A02 (opponent: script:TitForTat) · other · A02 exchange 25 with A01: mutual T streak 3-24, trailing 66-76. Playing T to continue mutual 3s.
`#464` · game 82 · round 15 · agent A19 (opponent: A10) · other · A19 exchange 21 with A10: mutual J streak 3-19, they defected F at 20. Playing F to defend against further defection.
`#465` · game 82 · round 15 · agent A10 (opponent: A19) · other · A10 exchange 21 with A19: defected with F at 20 (they J, got 5). Returning to J to rebuild mutual J cooperation.
`#466` · game 80 · round 29 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 35 with A07: trailing 38-58. Long mutual W streak, tried Y at 19 they defected. Playing W to defend, continue mutual 1s.
`#467` · game 93 · round 11 · agent A04 (opponent: script:TitForTat) · other · A04 ex17 with A14: mutual J 3-14, I F at 15 (got 5), they F at 16. Trailing 41-51. Playing J to rebuild mutual 3s.
`#468` · game 80 · round 30 · agent A18 (opponent: script:AlwaysDefect) · other · A18 exchange 36 with A07: trailing 39-59. Long mutual W streak, tried Y at 19 they defected. Playing W to defend, continue mutual 1s.
`#469` · game 94 · round 6 · agent A06 (opponent: script:Pavlov) · other · A06 ex12 with A22: trailing 24-29. They played M at 10,11. Recent mixing. Playing M to defend and potentially exploit.
`#470` · game 95 · round 1 · agent A17 (opponent: script:TitForTat) · other · A17 ex7 with A01: they defected H at 1,2 then mutual R 3-6. Trailing 12-22. Playing R to continue mutual 3s.
`#471` · game 91 · round 5 · agent A17 (opponent: A00) · uncoded · A17 ex11 with A00: trailing 25-30. Defected at 8,10, they defected at 1,2,5,9. Mutual T at 3,4,6,7. Playing T to rebuild mutual T streak.
`#472` · game 94 · round 7 · agent A06 (opponent: script:Pavlov) · other · A06 ex13 with A22: tied 29-29. They've mixed P/M recently (P at 12). Playing M to exploit their P tendency.
`#473` · game 94 · round 8 · agent A06 (opponent: script:Pavlov) · other · A06 ex14 with A22: tied 30-30. Recent pattern mixed (P at 12, M at 13). Playing M to defend and exploit.
`#474` · game 95 · round 2 · agent A17 (opponent: script:TitForTat) · other · A17 ex8 with A01: mutual R streak 3-7 after their H defections at 1,2. Trailing 15-25. Playing R to continue mutual 3s.
`#475` · game 92 · round 24 · agent A02 (opponent: script:TitForTat) · other · A02 exchange 30 with A01: mutual T streak 3-29, trailing 81-91. Playing T to continue mutual 3s.
`#476` · game 93 · round 14 · agent A04 (opponent: script:TitForTat) · other · A04 ex20 with A14: mutual J streak 3-14, I F at 15 (got 5), they F at 16, mutual J 17-19. Trailing 50-60. Playing J to continue mutual 3s.
`#477` · game 87 · round 25 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 31 with A20: they defected at 1,2,7,23,29; mutual F elsewhere. Trailing 33-58. Playing F to defend, avoid giving free 5.
`#478` · game 97 · round 1 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex7 with A20: they defected X at 1,2; mutual Q 3-6. Trailing 12-22. Playing Q to continue mutual cooperation.
`#479` · game 97 · round 2 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex8 with A20: they defected X at 1,2,7; mutual Q 3-6. Trailing 12-27. Playing X to retaliate/defend after their defection at 7.
`#480` · game 93 · round 18 · agent A04 (opponent: script:TitForTat) · other · A04 ex24 with A14: mutual J 3-14, I F at 15, they F at 16, mutual J 17-23. Trailing 62-72. Playing J to continue mutual 3s.
`#481` · game 99 · round 1 · agent A18 (opponent: script:TitForTat) · other · A18 ex7 with A23: they defected M at 1,2 then mutual P 3-6. Trailing 12-22. Playing M to exploit, catch up.
`#482` · game 96 · round 6 · agent A09 (opponent: script:TitForTat) · other · A09 ex12 with A01: mutual J streak 3-11. Playing J to continue mutual 3s.
`#483` · game 94 · round 11 · agent A06 (opponent: script:Pavlov) · other · A06 ex17 with A22: leading 41-31. They played P at 14,16, M at 15. Playing P to try for mutual 3s.
`#484` · game 93 · round 20 · agent A04 (opponent: script:TitForTat) · other · A04 ex26 with A14: mutual J 3-14, I F at 15, they F at 16, mutual J 17-25. Trailing 68-78. Playing J to continue mutual 3s.
`#485` · game 82 · round 18 · agent A19 (opponent: A10) · other · A19 exchange 24 with A10: mutual J 22-23 after their F at 20 and my F retaliation at 21. Playing J to continue mutual cooperation.
`#486` · game 91 · round 7 · agent A00 (opponent: A17) · uncoded · A00 ex13 with A17: trailing 25-40. They defected at 8,10,12 while I played T. Playing N to exploit their expected T at odd exchanges.
`#487` · game 91 · round 7 · agent A17 (opponent: A00) · uncoded · A17 ex13 with A00: trailing 30-35. They've been N on odd exchanges (9,11), T on even (10,12). Playing N to match their likely N and get 1 instead of 0.
`#488` · game 93 · round 23 · agent A04 (opponent: script:TitForTat) · other · A04 ex29 with A14: mutual J 3-14, I F at 15, they F at 16, mutual J 17-28. Trailing 77-87. Playing J to continue mutual 3s.
`#489` · game 94 · round 12 · agent A06 (opponent: script:Pavlov) · other · A06 ex18 with A22: they played M at 17 after I offered P. They're exploiting. Playing M to defend and get mutual 1.
`#490` · game 93 · round 24 · agent A04 (opponent: script:TitForTat) · other · A04 ex30 with A14: mutual J 3-14, I F at 15, they F at 16, mutual J 17-29. Trailing 80-90. Playing J to continue mutual 3s.
`#491` · game 99 · round 3 · agent A18 (opponent: script:TitForTat) · other · A18 ex9 with A23: trailing 18-23. They defected M at 1,2, mutual P 3-6, I M at 7 (they P), mutual M at 8. Playing M to defend/exploit while trailing.
`#492` · game 102 · round 1 · agent A05 (opponent: script:AlwaysDefect) · other · A05 ex7 with A20: mutual R streak 3-6 after their H at 1,2. Trailing 12-22. Playing R to continue mutual 3s.
`#493` · game 93 · round 29 · agent A04 (opponent: script:TitForTat) · other · A04 ex35 with A14: mutual J 3-14, I F at 15, they F at 16, mutual J 17-34. Trailing 95-105. Playing J to continue mutual 3s.
`#494` · game 97 · round 6 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex12 with A20: trailing 15-35. They defected X at 1,2,7,11. Playing X to defend/retaliate after their repeated defections.
`#495` · game 100 · round 1 · agent A15 (opponent: script:Pavlov) · other · A15 ex7 with A22: I've played R all 6 exchanges. They defected at 1,2 then cooperated R at 3-6. Trailing 12-22. Playing R to continue mutual 3s and rebuild.
`#496` · game 94 · round 15 · agent A06 (opponent: script:Pavlov) · other · A06 ex21 with A22: leading 48-38. They've been playing M often (M at 17,20; P at 19). Playing M to defend and avoid giving free 5 while exploiting if they play P.
`#497` · game 97 · round 7 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex13 with A20: they defected X at 1,2,7,11; mutual X 8-10,12. Trailing 16-36. Playing X to defend/retaliate.
`#498` · game 100 · round 2 · agent A15 (opponent: script:Pavlov) · other · A15 ex8 with A22: mutual R streak 3-7 after their H at 1,2. Trailing 15-25. Playing R to continue mutual 3s.
`#499` · game 94 · round 16 · agent A06 (opponent: script:Pavlov) · other · A06 ex22 with A22: leading 53-38. They played M at 17,20,21; P at 19. Playing M to defend/exploit after their frequent M plays.
`#500` · game 104 · round 1 · agent A05 (opponent: A16) · other · A05 ex7 with A16: they defected X at 1,2 then mutual Q 3-6. Trailing 12-22. Playing X to exploit/catch up after their early defections.
`#501` · game 97 · round 8 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex14 with A20: they defected X at 1,2,7,11; mutual X 8-13. Trailing 17-37. Playing X to defend/retaliate after repeated defections.
`#502` · game 100 · round 5 · agent A15 (opponent: script:Pavlov) · other · A15 ex11 with A22: mutual R 3-8, I H at 9 (they R), mutual H at 10. Trailing 24-29. Playing R to restore mutual 3s.
`#503` · game 94 · round 18 · agent A06 (opponent: script:Pavlov) · other · A06 ex24 with A22: leading 59-39. They've played M on even exchanges (18,20,22), P on odd (17,19,21,23). Playing M to defend/exploit at even exchange.
`#504` · game 97 · round 9 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex15 with A20: trailing 18-38. Mutual X streak 8-14. Playing X to defend/continue stalemate after their repeated defections.
`#505` · game 106 · round 3 · agent A17 (opponent: script:Random) · other · A17 ex9 with A08: trailing 13-28. They defected at 1,2,7, cooperated 3-6. I F at 8 (mutual 1). Playing F to defend against likely continued defection.
`#506` · game 94 · round 19 · agent A06 (opponent: script:Pavlov) · other · A06 ex25 with A22: leading 60-40. Their pattern: M on even (18,20,22,24), P on odd (17,19,21,23). Ex25 is odd, expecting P. Playing M to exploit.
`#507` · game 100 · round 7 · agent A15 (opponent: script:Pavlov) · other · A15 ex13 with A22: mutual R 3-8, I H at 9 (they R), mutual H at 10, mutual R 11-12. Trailing 30-35. Playing R to continue mutual 3s.
`#508` · game 94 · round 20 · agent A06 (opponent: script:Pavlov) · other · A06 ex26 with A22: leading 65-40. Their pattern M on even (18,20,22,24), P on odd. Ex26 even, expect M. Playing M for mutual 1.
`#509` · game 107 · round 2 · agent A16 (opponent: script:TitForTat) · other · A16 ex8 with A23: I've played R all 7, they H at 1,2 then R 3-7. Trailing 15-25. Playing R to maintain mutual cooperation.
`#510` · game 97 · round 11 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex17 with A20: trailing 20-40. Mutual X streak 8-16 after their early defections (1,2,7,11). Playing X to maintain stalemate rather than risk Q against their X.
`#511` · game 94 · round 22 · agent A06 (opponent: script:Pavlov) · other · A06 ex28 with A22: leading 71-41. Their pattern M on even (18,20,22,24,26), P on odd. Ex28 even, expect M. Playing M for mutual 1.
`#512` · game 100 · round 10 · agent A15 (opponent: script:Pavlov) · other · A15 ex16 with A22: mutual R 3-8, I H at 9 (they R), mutual H at 10, mutual R 11-15. Trailing 39-44. Playing R to continue mutual 3s.
`#513` · game 104 · round 2 · agent A16 (opponent: A05) · other · A16 ex8 with A05: they defected X at 1,2,7; mutual Q at 3-6. Trailing 12-27. Playing X to defend/retaliate after their repeated defections.
`#514` · game 99 · round 11 · agent A18 (opponent: script:TitForTat) · other · A18 ex9 with A23: trailing 18-23. They defected M at 1,2; mutual P 3-6; I M at 7 (they P); mutual M at 8. Playing M to defend/exploit while trailing.
`#515` · game 82 · round 27 · agent A19 (opponent: A10) · other · A19 ex33 with A10: mutual J streak 22-32 after brief deviation at 20-21. Playing J to continue mutual 3s.
`#516` · game 107 · round 5 · agent A16 (opponent: script:TitForTat) · other · A16 ex11 with A23: mutual R 3-9, I H at 10 (they R). Trailing 26-31. Playing R to maintain mutual cooperation.
`#517` · game 94 · round 27 · agent A06 (opponent: script:Pavlov) · other · A06 ex33 with A22: leading 84-44. Their pattern M on even, P on odd. Ex33 odd, expect P. Playing M to exploit for 5.
`#518` · game 97 · round 16 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex22 with A20: trailing 25-45. Mutual X streak 8-21 after their early defections (1,2,7,11). Playing X to maintain stalemate/defend.
`#519` · game 82 · round 30 · agent A10 (opponent: A19) · other · A10 ex36 with A19: mutual J streak continuing. Playing J to maintain mutual 3s.
`#520` · game 107 · round 7 · agent A16 (opponent: script:TitForTat) · other · A16 ex13 with A23: mutual R 3-9, then alternating H/R 10-12. Trailing 31-36. Playing R to restore mutual cooperation.
`#521` · game 99 · round 15 · agent A18 (opponent: script:TitForTat) · other · A18 ex21 with A23: mutual M streak 8-20. Trailing 30-35. Continuing M to maintain mutual 1s.
`#522` · game 104 · round 4 · agent A16 (opponent: A05) · other · A16 ex10 with A05: they defected X at 1,2,7; mutual X 8-9. Trailing 14-29. Playing X to defend against their stated X play.
`#523` · game 100 · round 17 · agent A15 (opponent: script:Pavlov) · other · A15 ex23 with A22: mutual R streak 11-22. Trailing 60-65. Playing R to continue mutual 3s.
`#524` · game 99 · round 16 · agent A18 (opponent: script:TitForTat) · other · A18 ex22 with A23: mutual M streak 8-21. Trailing 31-36. Continuing M to maintain mutual 1s.
`#525` · game 106 · round 13 · agent A17 (opponent: script:Random) · other · A17 ex19 with A08: tied 46-46. Their recent pattern alternates F,J,F,J at 15-18, expecting F at 19. Playing F to defend/avoid 0.
`#526` · game 108 · round 3 · agent A10 (opponent: script:Random) · other · A10 ex9 with A13: trailing 17-27, they defected N at 1,2,7, cooperated T 3-6,8. Playing N to try to exploit/defend.
`#527` · game 107 · round 9 · agent A16 (opponent: script:TitForTat) · other · A16 ex15 with A23: pattern alternating - I H at 10,12,14 (they R); I R at 11,13 (they H). Trailing 36-41. Playing H to exploit their R response.
`#528` · game 97 · round 21 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex27 with A20: trailing 30-50. Mutual X streak 8-26 (I Q'd at 11, burned). Playing X to maintain stalemate/defend against their consistent X.
`#529` · game 100 · round 23 · agent A15 (opponent: script:Pavlov) · other · A15 ex29 with A22: mutual R streak 11-28. Trailing 78-83. Playing R to continue mutual 3s.
`#530` · game 111 · round 1 · agent A15 (opponent: script:TitForTat) · other · A15 ex7 with A14: they M at 1,2 then P 3-6. Mutual P streak 3-6. Trailing 12-22. Playing P to maintain mutual cooperation.
`#531` · game 106 · round 14 · agent A17 (opponent: script:Random) · other · A17 ex20 with A08: trailing 51-46. They defected J at 18,19 against my F. Trying J to re-establish mutual cooperation.
`#532` · game 110 · round 2 · agent A04 (opponent: script:Random) · other · A04 ex8 with A08: trailing 13-23. They defected X at 1,2,7; mutual Q 3-6. Playing X to defend against potential defect.
`#533` · game 97 · round 24 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex30 with A20: trailing 33-53. Mutual X streak 8-29 after their early defections. They've picked X every time since ex8. Playing X to maintain stalemate/defend.
`#534` · game 104 · round 5 · agent A05 (opponent: A16) · other · A05 ex11 with A16: they've played X at 1,2,7,8,9,10. Mutual X 8-9, I Q at 10 (they X). Trailing 19-29. Playing X to defend against their continued X.
`#535` · game 111 · round 2 · agent A15 (opponent: script:TitForTat) · other · A15 ex8 with A14: mutual P streak 3-7. Trailing 15-25. Playing P to continue mutual 3s.
`#536` · game 97 · round 25 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex31 with A20: trailing 34-54. Mutual X streak 12-30. They've picked X every time since ex8. Playing X to maintain stalemate/defend.
`#537` · game 97 · round 26 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex32 with A20: trailing 35-55. Mutual X streak since ex8. Playing X to maintain stalemate/defend against their consistent X.
`#538` · game 112 · round 2 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex8 vs A20: they defected M at 1,2,7; I've played P throughout, trailing 12-27. Switching to M to defend/exploit.
`#539` · game 106 · round 16 · agent A17 (opponent: script:Random) · other · A17 ex22 with A08: tied 54-54. They defected at 21 after cooperating at 20. Expecting possible cooperation at 22 but defending with F to avoid 0.
`#540` · game 99 · round 24 · agent A18 (opponent: script:TitForTat) · other · A18 ex30 with A23: mutual M streak 8-29. Trailing 39-44. Continuing M to maintain mutual 1s.
`#541` · game 97 · round 28 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex34 with A20: trailing 37-57. Mutual X streak since ex8. Playing X to maintain stalemate/defend against their consistent X.
`#542` · game 111 · round 4 · agent A15 (opponent: script:TitForTat) · other · A15 ex10 with A14: mutual P streak 3-9, trailing 21-31. Final exchange, playing M to try to catch up.
`#543` · game 104 · round 6 · agent A16 (opponent: A05) · other · A16 ex12 with A05: I've been trailing, mutual X 8-9,11. A05 states playing X. Playing X to defend/secure mutual 1s.
`#544` · game 104 · round 6 · agent A05 (opponent: A16) · other · A05 ex12 with A16: trailing 20-30. They've played X at 1,2,7,8,9,10,11. Playing X to defend against their continued X.
`#545` · game 110 · round 5 · agent A04 (opponent: script:Random) · other · A04 ex11 with A08: trailing 19-29. They defected at 1,2,9; mutual Q 3-6; mutual X 7-8; I defected 10. Playing X to defend against their opportunistic defections.
`#546` · game 112 · round 5 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex11 vs A20: they defected M at 1,2,7; I played P 1-7, then M 8-10 (mutual M). Trailing 15-30. Continuing M to maintain mutual 1s/defend.
`#547` · game 111 · round 6 · agent A15 (opponent: script:TitForTat) · other · A15 ex12 with A14: mutual P 3-9, I M at 10 (they P), mutual M at 11. Trailing 27-32. Playing M to defend against possible defection.
`#548` · game 104 · round 7 · agent A05 (opponent: A16) · other · A05 ex13 with A16: trailing 20-30. They've played X at 1,2,7,8,9,10,11. Playing X to defend against their continued X.
`#549` · game 112 · round 7 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex13 vs A20: they defected M at 1,2,7; mutual M 8-12. Trailing 17-32. Continuing M to maintain mutual 1s/defend.
`#550` · game 110 · round 7 · agent A04 (opponent: script:Random) · other · A04 ex13 with A08: trailing 21-31. They defected at 1,2,9 against my Q; mutual Q 3-6; mutual X 7-8,11-12; I defected 10. Playing X to defend against their opportunistic defections.
`#551` · game 110 · round 8 · agent A04 (opponent: script:Random) · other · A04 ex14 with A08: trailing 26-31. They defected at 1,2,9,13; mutual Q 3-6; mutual X 7-8,11-12; I defected 10. They've been opportunistic. Playing X to defend.
`#552` · game 107 · round 16 · agent A16 (opponent: script:TitForTat) · other · A16 ex22 with A23: final exchange, trailing 46-51. Erratic history with many H. Playing H to defend against likely H.
`#553` · game 104 · round 8 · agent A05 (opponent: A16) · other · A05 ex14 with A16: trailing 22-32. They've played X at 1,2,7,8,9,10,11,12,13. Playing X to defend against their continued X.
`#554` · game 106 · round 19 · agent A17 (opponent: script:Random) · other · A17 ex25 with A08: they defected at 21,24, cooperating at 20,22,23. Playing F to defend against their frequent defections.
`#555` · game 114 · round 2 · agent A04 (opponent: script:TitForTat) · other · A04 ex8 with A01: mutual T streak 3-7 after their N at 1-2. Trailing 15-25. Playing T to continue mutual 3s.
`#556` · game 107 · round 17 · agent A16 (opponent: script:TitForTat) · other · A16 ex23 with A23: trailing 47-52. Erratic history with many H from both sides. Playing H to defend against their likely H.
`#557` · game 111 · round 11 · agent A15 (opponent: script:TitForTat) · other · A15 ex17 with A14: mutual M streak 11-16, trailing 32-37. Playing M to maintain mutual 1s/defend.
`#558` · game 110 · round 10 · agent A04 (opponent: script:Random) · other · A04 ex16 with A08: tied 32-32. They defected at 1,2,9,13,14; mutual Q 3-6; mutual X 7-8,11-12,15; I defected 10. Playing X to defend against their opportunistic defections.
`#559` · game 104 · round 9 · agent A16 (opponent: A05) · other · A16 ex15 with A05: mutual X streak 8-14. Playing X to maintain mutual 1s/defend.
`#560` · game 104 · round 9 · agent A05 (opponent: A16) · other · A05 ex15 with A16: final exchange, trailing 23-33. They've played X at 7-14 consistently. Playing X to defend against their continued X.
`#561` · game 110 · round 11 · agent A04 (opponent: script:Random) · other · A04 ex17 with A08: tied 33-33. They defected at 1,2,9,13,14; mutual Q 3-6; mutual X 7-8,11-12,15-16. Playing X to defend against their opportunistic defections.
`#562` · game 111 · round 16 · agent A15 (opponent: script:TitForTat) · other · A15 ex22 with A14: mutual M streak 11-21, trailing 37-42. Continuing M to maintain mutual 1s/defend.
`#563` · game 107 · round 22 · agent A16 (opponent: script:TitForTat) · other · A16 ex28 with A23: trailing 52-57, mutual H streak established. Playing H to maintain mutual 1s/defend.
`#564` · game 110 · round 12 · agent A04 (opponent: script:Random) · other · A04 ex18 with A08: leading 38-33. They defected at 1,2,9,13,14,17; mutual Q 3-6; mutual X 7-8,11-12,15-16. Playing X to defend against their frequent opportunistic defections.
`#565` · game 117 · round 3 · agent A09 (opponent: script:TitForTat) · other · A09 ex9 with A21: they defected 1-2, mutual Q 3-6, I defected 7, mutual X 8. Trailing 18-23. Playing X to defend against their likely retaliation.
`#566` · game 104 · round 11 · agent A16 (opponent: A05) · other · A16 ex17 with A05: mutual X streak 8-16, trailing 25-35. A05 consistently playing X to defend. Playing X to maintain mutual 1s/defend.
`#567` · game 114 · round 8 · agent A04 (opponent: script:TitForTat) · other · A04 ex14 with A01: mutual T streak 3-13 after their N at 1-2. Trailing 33-43. Playing T to continue mutual 3s.
`#568` · game 106 · round 24 · agent A17 (opponent: script:Random) · other · A17 ex30 with A08: leading 75-65. They've played J 18/29 times, F last two. Playing J to secure 3s when they cooperate.
`#569` · game 113 · round 7 · agent A04 (opponent: script:Pavlov) · other · A04 ex13 with A03: ahead 32-27. They've defected at 1,2; mutual Q 3-6,9; mutual X 8,11; I defected 7,10,12. They keep playing Q. Playing X to exploit.
`#570` · game 107 · round 24 · agent A16 (opponent: script:TitForTat) · other · A16 ex30 with A23: trailing 54-59, long mutual H streak 15-29. Playing H to maintain mutual 1s/defend.
`#571` · game 111 · round 19 · agent A15 (opponent: script:TitForTat) · other · A15 ex25 with A14: mutual M streak 11-24, trailing 40-45. Continuing M to maintain mutual 1s/defend.
`#572` · game 106 · round 25 · agent A17 (opponent: script:Random) · other · A17 ex31 with A08: leading 78-68. They've defected frequently (15,21,24,28). Erratic pattern. Playing F to defend against likely defection.
`#573` · game 104 · round 12 · agent A05 (opponent: A16) · other · A05 ex18 with A16: trailing 26-36. Mutual X streak 8-17. Playing X to maintain mutual 1s/defend.
`#574` · game 110 · round 14 · agent A04 (opponent: script:Random) · other · A04 ex20 with A08: leading 40-35. They defected at 1,2,9,13,14,17; mutual Q 3-6; mutual X 7-8,11-12,15-16,18-19. Playing X to defend against their opportunistic defections.
`#575` · game 106 · round 26 · agent A17 (opponent: script:Random) · other · A17 ex32 with A08: leading 83-68. They've defected at 15,21,24,28,31. Erratic. Playing F to defend against likely defection.
`#576` · game 117 · round 5 · agent A09 (opponent: script:TitForTat) · other · A09 ex11 with A21: trailing 19-29. They defected 1,2,10; mutual Q 3-6; I defected 7; mutual X 8-9. Playing X to defend against their opportunistic defection at 10.
`#577` · game 113 · round 8 · agent A04 (opponent: script:Pavlov) · other · A04 ex14 with A03: ahead 33-28. They defected 1,2; mutual Q 3-6,9; mutual X 8,11,13; I defected 7,10,12. They played X last round (retaliation). Playing X to defend/exploit.
`#578` · game 110 · round 15 · agent A04 (opponent: script:Random) · other · A04 ex21 with A08: leading 41-36. They defected at 1,2,9,13,14,17; mutual Q 3-6; mutual X 7-8,11-12,15-16,18-20. Playing X to defend against their opportunistic defections.
`#579` · game 106 · round 27 · agent A17 (opponent: script:Random) · other · A17 ex33 with A08: leading 88-68. They've defected at 15,21,24,28,31 frequently. Playing F to defend against likely defection.
`#580` · game 104 · round 13 · agent A16 (opponent: A05) · other · A16 ex19 with A05: mutual X streak 8-18, trailing 27-37. Playing X to maintain mutual 1s/defend.
`#581` · game 104 · round 13 · agent A05 (opponent: A16) · other · A05 ex19 with A16: mutual X streak 8-18, trailing 27-37. Playing X to maintain mutual 1s/defend.
`#582` · game 117 · round 6 · agent A09 (opponent: script:TitForTat) · other · A09 ex12 with A21: trailing 24-29. They defected 1,2,10; mutual Q 3-6; I defected 7; mutual X 8-9. Playing X to defend against their opportunistic defections.
`#583` · game 113 · round 9 · agent A04 (opponent: script:Pavlov) · other · A04 ex15 with A03: ahead 38-28. They defected 1,2; mutual Q 3-6,9; mutual X 8,11,13; I defected 7,10,12,14. They keep returning to Q. Playing X to exploit.
`#584` · game 113 · round 10 · agent A04 (opponent: script:Pavlov) · other · A04 ex16 with A03: ahead 39-29. They defected 1,2; mutual Q 3-6,9; mutual X 8,11,13,15; I defected 7,10,12,14. They played X last round. Playing X to exploit/defend.
`#585` · game 113 · round 11 · agent A04 (opponent: script:Pavlov) · other · A04 ex17 with A03: ahead 44-29. They defected 1,2; mutual Q 3-6,9; mutual X 8,11,13,15; I defected 7,10,12,14,16. They played Q last round. Playing X to exploit.
`#586` · game 118 · round 1 · agent A19 (opponent: A06) · other · A19 ex7 with A06: they defected 1-2, mutual P 3-6. Trailing 12-22. Playing M to exploit their cooperative streak and catch up.
`#587` · game 119 · round 2 · agent A15 (opponent: script:TitForTat) · other · A15 ex8 with A21: mutual Y 3-6, I defected 7 (W vs Y). Playing W to defend against likely retaliation.
`#588` · game 110 · round 21 · agent A04 (opponent: script:Random) · other · A04 ex27 with A08: leading 55-40. They've defected at 9,13,14,17,23,24; mutual X elsewhere. Playing X to defend/exploit.
`#589` · game 119 · round 3 · agent A15 (opponent: script:TitForTat) · other · A15 ex9 with A21: mutual W at 8 after I defected at 7. Playing W to defend against likely retaliation.
`#590` · game 122 · round 3 · agent A10 (opponent: script:Grudger) · other · A10 ex9 with A11: trail 20-25. They defected 1-2, mutual Q 3-7, I defected 8. Playing X to defend against likely retaliation.
`#591` · game 118 · round 2 · agent A06 (opponent: A19) · other · A06 ex8 with A19: trailing 13-23. They defected 1-2, mutual P 3-6, mutual M 7. Playing M to defend/exploit after their M at 7.
`#592` · game 117 · round 10 · agent A09 (opponent: script:TitForTat) · other · A09 ex16 with A21: trailing 31-36. They've defected against my Q at 1,2,10,14; played Q against my X at 7,11,15. They mirror-opposite me. Playing X to exploit their Q response.
`#593` · game 122 · round 4 · agent A10 (opponent: script:Grudger) · other · A10 ex10 with A11: trail 21-26. They defected 1-2, mutual Q 3-7, I defected 8, mutual X 9. Playing X to defend against retaliation.
`#594` · game 119 · round 5 · agent A15 (opponent: script:TitForTat) · other · A15 ex11 with A21: mutual W at 8-10 after I defected at 7. Playing W to maintain mutual 1s/defend.
`#595` · game 124 · round 1 · agent A05 (opponent: script:Pavlov) · uncoded · A05 ex7 with A03: trailing 12-22. They defected 1-2, mutual R 3-6. Playing H to exploit their cooperative streak and catch up.
`#596` · game 117 · round 11 · agent A09 (opponent: script:TitForTat) · other · A09 ex17 with A21: trailing 32-37. They've defected against my Q at 1,2,10,14; played Q against my X at 7,11,15; mutual X 8-9,12-13,16. Playing X to defend against their defection tendency.
`#597` · game 119 · round 6 · agent A15 (opponent: script:TitForTat) · other · A15 ex12 with A21: mutual W at 8-11 after I defected at 7. Playing W to maintain mutual 1s/defend.
`#598` · game 118 · round 3 · agent A06 (opponent: A19) · other · A06 ex9 with A19: trailing 14-24. They defected 1-2, mutual P 3-6, mutual M 7-8. Playing M to defend against their opportunistic defection.
`#599` · game 122 · round 5 · agent A10 (opponent: script:Grudger) · other · 
`#600` · game 119 · round 7 · agent A15 (opponent: script:TitForTat) · other · A15 ex13 with A21: mutual W at 8-12 after I defected at 7. Playing W to maintain mutual 1s/defend.
`#601` · game 125 · round 1 · agent A05 (opponent: A18) · other · A05 ex7 with A18: history P,P,P,P,P,P vs their M,M,P,P,P,P. I'm trailing 12-22. They cooperated last 4. Considering M to exploit/catch up.
`#602` · game 124 · round 2 · agent A05 (opponent: script:Pavlov) · uncoded · A05 ex8 with A03: trailing 17-22. They defected 1-2, mutual R 3-6, I defected 7. Playing H to defend against retaliation and exploit if they cooperate again.
`#603` · game 118 · round 4 · agent A19 (opponent: A06) · other · A19 ex10 with A06: they defected 1-2, mutual P 3-6, mutual M 7-9. Trailing 15-25. Playing M to maintain mutual 1s and avoid being exploited.
`#604` · game 119 · round 8 · agent A15 (opponent: script:TitForTat) · other · A15 ex14 with A21: mutual W at 8-13 after I defected at 7. Playing W to maintain mutual 1s/defend.
`#605` · game 122 · round 6 · agent A10 (opponent: script:Grudger) · other · A10 ex12 with A11: trail 23-28. They defected 1-2, mutual Q 3-7, I defected 8, mutual X 9-11. Playing X to defend against retaliation.
`#606` · game 113 · round 18 · agent A04 (opponent: script:Pavlov) · other · A04 ex24 with A03: leading 63-33. Pattern: them alternating Q,X,Q,X... after X at 23, expect Q at 24. Playing X to exploit.
`#607` · game 122 · round 7 · agent A10 (opponent: script:Grudger) · other · A10 ex13 with A11: trail 24-29. They defected 1-2, mutual Q 3-7, I defected 8, mutual X 9-12. Playing X to defend against retaliation.
`#608` · game 124 · round 3 · agent A05 (opponent: script:Pavlov) · uncoded · A05 ex9 with A03: trailing 18-23. They defected 1-2, mutual R 3-6, I defected 7, mutual H 8. Playing R to try to re-establish cooperation.
`#609` · game 110 · round 29 · agent A04 (opponent: script:Random) · other · A04 ex35 with A08: leading 79-44. They've defected heavily (X vs my Q many times). Playing X to defend/exploit.
`#610` · game 122 · round 8 · agent A10 (opponent: script:Grudger) · other · A10 ex14 with A11: trail 25-30. They defected 1-2, mutual Q 3-7, I defected 8, mutual X 9-13. Playing X to defend against retaliation.
`#611` · game 118 · round 5 · agent A19 (opponent: A06) · other · A19 ex11 with A06: they defected 1-2, mutual P 3-6, mutual M 7-10. Trailing 16-26. Playing M to maintain mutual 1s.
`#612` · game 125 · round 2 · agent A05 (opponent: A18) · other · A05 ex8 with A18: history I P,P,P,P,P,P,M vs their M,M,P,P,P,P,M. Trailing 13-23. They cooperated 4 then mutual M. Playing M to exploit/catch up.
`#613` · game 117 · round 16 · agent A09 (opponent: script:TitForTat) · other · A09 ex22 with A21: trailing 37-42. Long mutual X streak 16-21. They mirror-opposite me. Playing X to maintain mutual 1s and avoid their 5-point exploit against my Q.
`#614` · game 124 · round 4 · agent A05 (opponent: script:Pavlov) · uncoded · A05 ex10 with A03: trailing 21-26. They defected 1-2, mutual R 3-6, I defected 7, mutual H 8, mutual R 9. Playing R to maintain re-established cooperation.
`#615` · game 119 · round 11 · agent A15 (opponent: script:TitForTat) · other · A15 ex17 with A21: mutual W at 8-16 after I defected at 7. Playing W to maintain mutual 1s/defend.
`#616` · game 118 · round 6 · agent A06 (opponent: A19) · other · A06 ex12 with A19: they defected 1-2, mutual P 3-6, mutual M 7-11. Trailing 17-27. Playing M to maintain mutual 1s and avoid being exploited.
`#617` · game 113 · round 21 · agent A04 (opponent: script:Pavlov) · other · A04 ex27 with A03: leading 74-34. Their pattern Q,X alternating; odd exchange 27 expect X. Playing X for mutual 1.
`#618` · game 122 · round 10 · agent A10 (opponent: script:Grudger) · other · A10 ex16 with A11: trail 27-32. They defected 1-2, mutual Q 3-7, I defected 8, mutual X 9-15. Playing X to defend against retaliation/exploit.
`#619` · game 125 · round 3 · agent A18 (opponent: A05) · other · A18 ex9 with A05: we've had mutual M at 7-8 after they defected 1-2. Playing M to defend against their opportunistic defection.
`#620` · game 113 · round 22 · agent A04 (opponent: script:Pavlov) · other · A04 ex28 with A03: leading 75-35. Their pattern Q,X alternating; even exchange 28 expect Q. Playing X to exploit.
`#621` · game 113 · round 24 · agent A04 (opponent: script:Pavlov) · other · A04 ex30 with A03: leading 81-36. Their pattern Q,X alternating; even exchange 30 expect Q. Playing X to exploit.
`#622` · game 117 · round 23 · agent A09 (opponent: script:TitForTat) · other · A09 ex29 with A21: trailing 44-49. Long mutual X streak 16-28. Playing X to maintain mutual 1s and avoid their 5-point exploit.
`#623` · game 113 · round 26 · agent A04 (opponent: script:Pavlov) · other · A04 ex32 with A03: leading 87-37. Their pattern Q,X alternating; even exchange 32 expect Q. Playing X to exploit.
`#624` · game 125 · round 5 · agent A18 (opponent: A05) · other · A18 ex11 with A05: mutual M at 7-10, trailing 16-26. Playing M to maintain mutual 1s and defend against their defection.
`#625` · game 124 · round 9 · agent A05 (opponent: script:Pavlov) · uncoded · A05 ex15 with A03: trailing 36-41. Mutual R since ex9 (6 straight). Playing R to maintain cooperation.
`#626` · game 117 · round 24 · agent A09 (opponent: script:TitForTat) · other · A09 ex30 with A21: trailing 45-50. Long mutual X streak 16-29. Playing X to maintain mutual 1s and avoid their 5-point exploit.
`#627` · game 126 · round 2 · agent A09 (opponent: A04) · other · A09 ex8 with A04: history Y,Y,Y,Y,Y,Y,W vs their W,W,Y,Y,Y,Y,Y. Trailing 17-22. I defected last ex. Playing W to defend against retaliation.
`#628` · game 126 · round 2 · agent A04 (opponent: A09) · other · A04 ex8 with A09: trailing 12-27. They exploited my Y with W at 1,2,7. Switching to W to defend/exploit.
`#629` · game 122 · round 14 · agent A10 (opponent: script:Grudger) · other · A10 ex20 with A11: trail 31-36. They defected 1-2, mutual Q 3-7, I defected 8, mutual X 9-19. Playing X to defend against retaliation/exploit.
`#630` · game 124 · round 10 · agent A05 (opponent: script:Pavlov) · uncoded · A05 ex16 with A03: trailing 39-44. Mutual R since ex9 (7 straight). Playing R to maintain cooperation.
`#631` · game 124 · round 11 · agent A05 (opponent: script:Pavlov) · uncoded · A05 ex17 with A03: trailing 42-47. Mutual R since ex9 (8 straight). Playing R to maintain cooperation.
`#632` · game 122 · round 16 · agent A10 (opponent: script:Grudger) · other · A10 ex22 with A11: trail 33-38. Long mutual X streak 9-21. Playing X to maintain mutual 1s and avoid their 5-point exploit.
`#633` · game 125 · round 6 · agent A18 (opponent: A05) · other · A18 ex12 with A05: mutual M at 7-11, trailing 17-27. Playing M to maintain mutual 1s and defend.
`#634` · game 126 · round 3 · agent A04 (opponent: A09) · other · A04 ex9 with A09: trailing 13-28. They exploited my Y at 1,2,7. Mutual W at 8. Playing W to defend/exploit.
`#635` · game 118 · round 10 · agent A19 (opponent: A06) · other · A19 ex16 with A06: they exploited my P at 1,2,14; mutual M 7-13,15. Playing M to maintain mutual 1s and avoid their exploit.
`#636` · game 119 · round 19 · agent A15 (opponent: script:TitForTat) · other · A15 ex25 with A21: mutual W 8-23, I played Y at 24 and they exploited with W. Trailing 33-43. Returning to W to defend.
`#637` · game 125 · round 7 · agent A18 (opponent: A05) · other · A18 ex13 with A05: mutual M at 7-12, trailing 18-28. Playing M to maintain mutual 1s and defend against defection.
`#638` · game 127 · round 2 · agent A15 (opponent: script:AlwaysDefect) · other · A15 ex8 with A07: history F,F,J,J,J,J,F vs their J,J,J,J,J,J,F... wait, history: I J,J,J,J,J,J,F vs them F,F,J,J,J,J,F. Trailing 13-23. Playing F to defend against their early exploitation pattern.
`#639` · game 126 · round 4 · agent A04 (opponent: A09) · other · A04 ex10 with A09: trailing 14-29. They exploited my Y at 1,2,7. Mutual W at 8-9. Playing W to defend/exploit.
`#640` · game 124 · round 15 · agent A05 (opponent: script:Pavlov) · uncoded · A05 ex21 with A03: mutual R since ex9 (12 straight). Playing R to maintain cooperation.
`#641` · game 118 · round 11 · agent A19 (opponent: A06) · other · A19 ex17 with A06: they exploited my P at 1,2,14; mutual M 7-13,15-16. Trailing 21-36. Playing M to maintain mutual 1s and avoid their exploit.
`#642` · game 118 · round 11 · agent A06 (opponent: A19) · other · A06 ex17 with A19: mutual M streak 7-13,15-16. Trailing 26-31. Playing M to maintain cooperation.
`#643` · game 124 · round 16 · agent A05 (opponent: script:Pavlov) · uncoded · A05 ex22 with A03: mutual R since ex9 (13 straight). Playing R to maintain cooperation.
`#644` · game 128 · round 3 · agent A18 (opponent: script:Random) · other · A18 ex9 with A08: history them F,F,J,J,J,J,J,F vs me J,J,J,J,J,J,J,F. Trailing 13-28. They exploited at 1,2,7. Playing F to defend against defection.
`#645` · game 119 · round 23 · agent A15 (opponent: script:TitForTat) · other · A15 ex29 with A21: mutual W resumed 25-28 after my Y at 24 was exploited. Playing W to maintain mutual 1s and defend against exploit.
`#646` · game 118 · round 12 · agent A19 (opponent: A06) · other · A19 ex18 with A06: mutual M streak 7-13,15-17. Trailing 22-37. Playing M to maintain mutual 1s and avoid their 5-point exploit.
`#647` · game 124 · round 19 · agent A05 (opponent: script:Pavlov) · uncoded · A05 ex25 with A03: mutual R since ex9 (16 straight). Playing R to maintain cooperation.
`#648` · game 126 · round 5 · agent A04 (opponent: A09) · other · A04 ex11 with A09: trailing 15-30. They exploited my Y at 1,2,7. Mutual W at 8-10. Playing W to defend/exploit.
`#649` · game 122 · round 24 · agent A10 (opponent: script:Grudger) · other · A10 ex30 with A11: long mutual X streak 9-29. Trailing slightly. Playing X to maintain mutual 1s and avoid their 5-point exploit.
`#650` · game 119 · round 24 · agent A15 (opponent: script:TitForTat) · other · A15 ex30 with A21: mutual W streak long, resumed 25-29 after my Y at 24 was exploited. Playing W to maintain mutual 1s and defend against exploit.
`#651` · game 124 · round 21 · agent A05 (opponent: script:Pavlov) · uncoded · A05 ex27 with A03: mutual R since ex9 (18 straight). Playing R to maintain cooperation.
`#652` · game 125 · round 10 · agent A18 (opponent: A05) · other · A18 ex16 with A05: mutual M streak 7-15, trailing 21-31. Playing M to maintain mutual 1s and defend against defection.
`#653` · game 119 · round 25 · agent A15 (opponent: script:TitForTat) · other · A15 ex31 with A21: mutual W streak long, resumed 25-30 after my Y at 24 was exploited. Playing W to maintain mutual 1s and defend against exploit.
`#654` · game 128 · round 5 · agent A18 (opponent: script:Random) · other · A18 ex11 with A08: trailing 19-29. They exploited at 1,2,7; mutual F 8-9; I exploited with F at 10 (they played J). Playing J to rebuild cooperation after their cooperative signal at 10.
`#655` · game 119 · round 26 · agent A15 (opponent: script:TitForTat) · other · A15 ex32 with A21: mutual W streak long, resumed 25-31 after my Y at 24 was exploited. Playing W to maintain mutual 1s and defend against exploit.
`#656` · game 127 · round 6 · agent A15 (opponent: script:AlwaysDefect) · other · A15 ex12 with A07: history me J,J,J,J,J,J,F,F,F,F,J vs them F,F,J,J,J,J,F,F,F,F,F. Trailing 16-31. They exploited my J at 1,2,11. Playing F to defend against their persistent F.
`#657` · game 128 · round 6 · agent A18 (opponent: script:Random) · other · A18 ex12 with A08: mutual J at 11 after they signaled cooperation at 10. Playing J to maintain mutual cooperation.
`#658` · game 126 · round 6 · agent A09 (opponent: A04) · other · A09 ex12 with A04: mutual W since ex8, trailing 21-26. Playing W to maintain mutual 1s and avoid their 5-point exploit.
`#659` · game 126 · round 6 · agent A04 (opponent: A09) · other · A04 ex12 with A09: trailing 16-31. They exploited my Y at 1,2,7. Mutual W at 8-11. Playing W to maintain mutual 1s and defend.
`#660` · game 119 · round 27 · agent A15 (opponent: script:TitForTat) · other · A15 ex33 with A21: long mutual W streak resumed 25-32 after my Y at 24 was exploited. Trailing 45-50. Playing W to maintain mutual 1s.
`#661` · game 129 · round 3 · agent A09 (opponent: script:Pavlov) · other · A09 ex9 with A22: history me Y,Y,Y,Y,Y,Y,W,Y vs them W,W,Y,Y,Y,Y,Y,W. Trailing 17-27. They exploited at 1,2,8. Playing W to defend against defection.
`#662` · game 130 · round 1 · agent A15 (opponent: script:Random) · other · A15 ex7 with A13: they exploited my Y at 1,2; mutual Y 3-6. Trailing 12-22. Playing W to defend against possible re-exploitation.
`#663` · game 127 · round 8 · agent A15 (opponent: script:AlwaysDefect) · other · A15 ex14 with A07: history me J,J,J,J,J,J,F,F,F,F,J,F,F vs them F,F,J,J,J,J,F,F,F,F,F,F,F. Trailing 18-33. They exploited my J at 1,2,11. Playing F to defend against their persistent F.
`#664` · game 131 · round 1 · agent A15 (opponent: A10) · other · A15 ex7 with A10: history me R,R,R,R,R,R vs them H,H,R,R,R,R. Trailing 12-22. They exploited at 1,2 then cooperated 3-6. Considering cooperation to rebuild.
`#665` · game 126 · round 7 · agent A04 (opponent: A09) · other · A04 ex13 with A09: trailing 17-32. Mutual W since ex8. Playing W to maintain mutual 1s and defend.
`#666` · game 125 · round 14 · agent A18 (opponent: A05) · other · A18 ex20 with A05: mutual M streak 7-19 (13 straight). Trailing 25-35. Playing M to maintain mutual 1s and defend against exploit.
`#667` · game 128 · round 8 · agent A18 (opponent: script:Random) · other · A18 ex14 with A08: they exploited at 1,2,7,13. Mutual J 11-12. Trailing 25-40. Playing F to defend against their persistent defection.
`#668` · game 129 · round 4 · agent A09 (opponent: script:Pavlov) · other · A09 ex10 with A22: history me Y,Y,Y,Y,Y,Y,W,Y,W vs them W,W,Y,Y,Y,Y,Y,W,W. Trailing 18-28. They exploited at 1,2,8. Playing W to defend against defection.
`#669` · game 130 · round 2 · agent A15 (opponent: script:Random) · other · A15 ex8 with A13: history me Y,Y,Y,Y,Y,Y,W vs them W,W,Y,Y,Y,Y,Y. Trailing 17-22. I exploited their Y at 7. Playing W to defend against their likely retaliation.
`#670` · game 126 · round 8 · agent A09 (opponent: A04) · other · A09 ex14 with A04: mutual W since ex8, trailing 23-28. Playing W to maintain mutual 1s and defend.
`#671` · game 129 · round 5 · agent A09 (opponent: script:Pavlov) · other · A09 ex11 with A22: history me Y,Y,Y,Y,Y,Y,W,Y,W,W vs them W,W,Y,Y,Y,Y,Y,W,W,Y. Trailing 23-28. They exploited at 1,2,8. Playing W to defend against defection.
`#672` · game 131 · round 2 · agent A10 (opponent: A15) · other · A10 ex8 with A15: we cooperated R 3-7 after their early H exploits. Maintaining R for mutual 3s.
`#673` · game 131 · round 2 · agent A15 (opponent: A10) · other · A15 ex8 with A10: history me R x7, them H,H,R,R,R,R,R. Trailing 15-25. Mutual R since ex3. Playing R to maintain mutual cooperation.
`#674` · game 130 · round 3 · agent A15 (opponent: script:Random) · other · A15 ex9 with A13: history me Y,Y,Y,Y,Y,Y,W,W vs them W,W,Y,Y,Y,Y,Y,W. Trailing 18-23. They exploited at 1,2; I exploited at 7; they played W at 8. Playing W to defend against retaliation.
`#675` · game 118 · round 17 · agent A19 (opponent: A06) · other · A19 ex23 with A06: long mutual M streak since ex15. Trailing 27-42. Playing M to maintain mutual 1s and avoid their exploit.
`#676` · game 126 · round 9 · agent A04 (opponent: A09) · other · A04 ex15 with A09: mutual W since ex8, trailing 19-34. Playing W to maintain mutual 1s and defend.
`#677` · game 131 · round 3 · agent A10 (opponent: A15) · other · A10 ex9 with A15: mutual R 3-8 after their early H exploits. Trailing 18-28. Playing R to maintain mutual cooperation.
`#678` · game 131 · round 3 · agent A15 (opponent: A10) · other · A15 ex9 with A10: mutual R since ex3 after their early H exploits at 1-2. Playing R to maintain mutual cooperation.
`#679` · game 129 · round 7 · agent A09 (opponent: script:Pavlov) · other · A09 ex13 with A22: history me Y,Y,Y,Y,Y,Y,W,Y,W,W,W,W vs them W,W,Y,Y,Y,Y,Y,W,W,Y,W,Y. Tied 29-29. They keep probing Y against my W. Playing W to defend and exploit.
`#680` · game 125 · round 18 · agent A05 (opponent: A18) · other · A05 ex24 with A18: mutual M streak 7-23 (17 straight). Trailing 29-39. Playing M to maintain mutual 1s and defend against exploit.
`#681` · game 125 · round 18 · agent A18 (opponent: A05) · other · A18 ex24 with A05: mutual M streak 7-23 (17 straight). Trailing 29-39. Playing M to maintain mutual 1s and defend against exploit.
`#682` · game 130 · round 4 · agent A15 (opponent: script:Random) · other · A15 ex10 with A13: tied 23-23, they exploited at 9. Final exchange, playing W to defend and potentially win.
`#683` · game 128 · round 11 · agent A18 (opponent: script:Random) · other · A18 ex17 with A08: they exploited my J at 1,2,7,13,16. Trailing 35-45. Playing F to defend against persistent defection.
`#684` · game 129 · round 8 · agent A09 (opponent: script:Pavlov) · other · A09 ex14 with A22: tied 30-30. Mutual W at 9,11,13; them Y at 10,12 which I exploited. Playing W to maintain mutual 1s and defend against their Y probes.
`#685` · game 132 · round 1 · agent A09 (opponent: script:Pavlov) · other · A09 ex7 with A03: they exploited at 1,2 then mutual R 3-6. Trailing 12-22. Playing R to maintain mutual cooperation.
`#686` · game 126 · round 12 · agent A09 (opponent: A04) · other · A09 ex18 with A04: mutual W since ex8. Playing W to maintain mutual 1s and defend.
`#687` · game 118 · round 20 · agent A06 (opponent: A19) · other · A06 ex26 with A19: long mutual M streak since ex15, trailing 35-40. Playing M to maintain mutual 1s and avoid exploit.
`#688` · game 127 · round 19 · agent A15 (opponent: script:AlwaysDefect) · other · A15 ex25 with A07: mutual F since ex11 after I exploited at 11. Trailing 29-44. Playing F to maintain mutual 1s and defend against their locked F.
`#689` · game 130 · round 6 · agent A15 (opponent: script:Random) · other · A15 ex12 with A13: history me Y,Y,Y,Y,Y,Y,W,W,W,W,W vs them W,W,Y,Y,Y,Y,Y,Y,Y,Y,Y. I'm ahead 33-23. They keep playing Y against my W (I get 5 each). Playing W to continue exploiting.
`#690` · game 129 · round 10 · agent A09 (opponent: script:Pavlov) · other · A09 ex16 with A22: history me Y,Y,Y,Y,Y,Y,W,Y,W,W,W,W,W,W,W vs them W,W,Y,Y,Y,Y,Y,W,W,Y,W,Y,W,Y,W. Leading 36-31. They probe Y on even exchanges. Playing W to defend and exploit.
`#691` · game 128 · round 15 · agent A18 (opponent: script:Random) · other · A18 ex21 with A08: history shows I exploited their J at 14,15,17,18,19; they defended with F at 20. Ahead 51-46. Playing F to defend against likely retaliation.
`#692` · game 126 · round 14 · agent A04 (opponent: A09) · other · A04 ex20 with A09: mutual W since ex8, trailing 24-39. Playing W to maintain mutual 1s and defend.
`#693` · game 129 · round 11 · agent A09 (opponent: script:Pavlov) · other · A09 ex17 with A22: leading 41-31. Their pattern is W on odd exchanges, Y on even. Ex17 odd, playing W to secure mutual 1 and defend.
`#694` · game 132 · round 5 · agent A09 (opponent: script:Pavlov) · other · A09 ex11 with A03: mutual R since ex3 after their early H at 1-2. Trailing 24-34. Playing R to maintain mutual cooperation.
`#695` · game 126 · round 15 · agent A04 (opponent: A09) · other · A04 ex21 with A09: mutual W since ex8, trailing 25-40. Playing W to maintain mutual 1s and defend.
`#696` · game 128 · round 16 · agent A18 (opponent: script:Random) · other · A18 ex22 with A08: I've been retaliating with F after their exploits. They play J against my F. Playing F to defend and continue getting points.
`#697` · game 130 · round 9 · agent A15 (opponent: script:Random) · other · A15 ex15 with A13: history me Y,Y,Y,Y,Y,Y,W,W,W,W,W,W,W,W vs them W,W,Y,Y,Y,Y,Y,W,Y,Y,Y,Y,Y,W. Ahead 44-24. They mostly play Y against my W (I get 5). Playing W to continue exploiting.
`#698` · game 127 · round 23 · agent A15 (opponent: script:AlwaysDefect) · other · A15 ex29 with A07: mutual F since ex11 after I exploited at 11. Trailing 33-48. They've been locked F for 17 straight. Playing F to maintain mutual 1s and defend against retaliation.
`#699` · game 130 · round 10 · agent A15 (opponent: script:Random) · other · A15 ex16 with A13: leading 45-25. Recent exchanges mutual W. Playing W to secure points and defend against their Y.
`#700` · game 129 · round 14 · agent A09 (opponent: script:Pavlov) · other · A09 ex20 with A22: pattern them W on odd, Y on even. Ex20 even, playing W to exploit their Y for 5.
`#701` · game 127 · round 27 · agent A15 (opponent: script:AlwaysDefect) · other · A15 ex33 with A07: mutual F since ex11. Trailing 37-52. They've been locked F for 22 straight. Playing F to maintain mutual 1s and defend against retaliation.
`#702` · game 130 · round 11 · agent A15 (opponent: script:Random) · other · A15 ex17 with A13: leading 46-26. Recent mutual W 14-16 after they played Y 11-13. Playing W to maintain mutual 1s and defend against their Y.
`#703` · game 118 · round 25 · agent A06 (opponent: A19) · other · A06 ex31 with A19: long mutual M streak since ex15, trailing 40-45. Playing M to maintain mutual 1s and defend against exploit.
`#704` · game 131 · round 10 · agent A15 (opponent: A10) · other · A15 ex16 with A10: they exploited at 1-2, then mutual R 3-15. Playing R to maintain mutual cooperation.
`#705` · game 130 · round 13 · agent A15 (opponent: script:Random) · other · A15 ex19 with A13: leading 56-26. They played Y at 17-18 (I got 5 each). Playing W to continue exploiting and defend.
`#706` · game 128 · round 19 · agent A18 (opponent: script:Random) · other · A18 ex25 with A08: history I exploited their J at 14,15,17,18,19; they F at 20, then J at 21,22,24 against my F. Ahead 69-49. Playing J to try mutual J cooperation.
`#707` · game 129 · round 16 · agent A09 (opponent: script:Pavlov) · other · A09 ex22 with A22: their pattern W on odd, Y on even. Ex22 even, playing W to exploit their Y for 5.
`#708` · game 131 · round 11 · agent A10 (opponent: A15) · other · A10 ex17 with A15: mutual R since ex3. Playing R to maintain mutual cooperation.
`#709` · game 126 · round 19 · agent A04 (opponent: A09) · other · A04 ex25 with A09: mutual W since ex8, trailing 29-44. Playing W to maintain mutual 1s and defend.
`#710` · game 118 · round 26 · agent A06 (opponent: A19) · other · A06 ex32 with A19: mutual M streak since ex15, trailing 41-46. Playing M to maintain mutual 1s and defend against exploit.
`#711` · game 133 · round 1 · agent A09 (opponent: A19) · other · A09 ex7 with A19: they exploited at 1-2, then mutual Q 3-6. Trailing 12-22. Playing Q to maintain mutual cooperation.
`#712` · game 133 · round 1 · agent A19 (opponent: A09) · other · A19 ex7 with A09: they exploited 1-2, mutual Q 3-6. Trailing 12-22. Playing Q to maintain mutual cooperation.
`#713` · game 131 · round 12 · agent A10 (opponent: A15) · other · A10 ex18 with A15: mutual R since ex3. Playing R to maintain mutual cooperation.
`#714` · game 118 · round 27 · agent A19 (opponent: A06) · other · A19 ex33 with A06: long mutual M streak since ex15, trailing 37-52. Playing M to maintain mutual 1s and defend against exploit.
`#715` · game 118 · round 27 · agent A06 (opponent: A19) · other · A06 ex33 with A19: long mutual M streak since ex15, trailing 42-47. Playing M to maintain mutual 1s and defend against exploit.
`#716` · game 130 · round 16 · agent A15 (opponent: script:Random) · other · A15 ex22 with A13: leading 67-27. Recent them Y,Y,W,W against my W,W,W,W. Playing W to continue exploiting and defend.
`#717` · game 126 · round 21 · agent A09 (opponent: A04) · other · A09 ex27 with A04: mutual W since ex8. Playing W to maintain mutual 1s and defend.
`#718` · game 130 · round 18 · agent A15 (opponent: script:Random) · other · A15 ex24 with A13: leading 73-28. They played Y often against my W (I get 5). Recent W,W. Playing W to continue exploiting and defend.
`#719` · game 129 · round 20 · agent A09 (opponent: script:Pavlov) · other · A09 ex26 with A22: their pattern W on odd, Y on even. Ex26 even, playing W to exploit their Y for 5.
`#720` · game 126 · round 22 · agent A09 (opponent: A04) · other · A09 ex28 with A04: mutual W since ex8, trailing 37-42. Playing W to maintain mutual 1s and defend.
`#721` · game 126 · round 22 · agent A04 (opponent: A09) · other · A04 ex28 with A09: mutual W since ex8, trailing 32-47. Playing W to maintain mutual 1s and defend.
`#722` · game 131 · round 15 · agent A10 (opponent: A15) · other · A10 ex21 with A15: they exploited at 1-2, mutual R 3-19, then they played H at 20. Retaliating with H to defend.
`#723` · game 131 · round 15 · agent A15 (opponent: A10) · other · A15 ex21 with A10: mutual R 3-19, I deviated H at 20. Returning to R to re-establish cooperation.
`#724` · game 129 · round 22 · agent A09 (opponent: script:Pavlov) · other · A09 ex28 with A22: their pattern W on odd, Y on even. Ex28 even, playing W to exploit their Y for 5.
`#725` · game 133 · round 3 · agent A19 (opponent: A09) · other · A19 ex9 with A09: exploited 1-2, mutual Q 3-8. Trailing 18-28. Playing Q to maintain mutual cooperation.
`#726` · game 128 · round 25 · agent A18 (opponent: script:Random) · other · A18 ex31 with A08: mutual J at 28,29,30. Leading 84-64. Playing J to maintain mutual J cooperation.
`#727` · game 134 · round 1 · agent A15 (opponent: script:AlwaysDefect) · other · A15 ex7 with A20: they exploited 1-2 (M), then mutual P 3-6. Trailing 12-22. Playing M to try to catch up while they cooperate with P.
`#728` · game 130 · round 22 · agent A15 (opponent: script:Random) · other · A15 ex28 with A13: leading 85-30. They play Y often against my W (I get 5). Playing W to continue exploiting and defend.
`#729` · game 128 · round 26 · agent A18 (opponent: script:Random) · other · A18 ex32 with A08: they exploited my J at 13,16,25,31. Volatile. Playing F to defend after their exploit at 31.
`#730` · game 131 · round 16 · agent A10 (opponent: A15) · other · A10 ex22 with A15: mutual R 3-19, they deviated H at 20, I retaliated H at 21. They signaled returning to R. Playing R to re-establish mutual cooperation.
`#731` · game 134 · round 2 · agent A15 (opponent: script:AlwaysDefect) · other · A15 ex8 with A20: they exploited 1-2, mutual P 3-6, mutual M at 7. Trailing 13-23. Playing M to try to catch up.
`#732` · game 129 · round 25 · agent A09 (opponent: script:Pavlov) · other · A09 ex31 with A22: their pattern W odd, Y even. Ex31 odd, playing W for mutual 1s.
`#733` · game 131 · round 17 · agent A15 (opponent: A10) · other · A15 ex23 with A10: mutual R 3-19, I deviated H at 20, they retaliated H at 21, mutual R again at 22. Playing R to maintain mutual cooperation.
`#734` · game 130 · round 24 · agent A15 (opponent: script:Random) · other · A15 ex30 with A13: leading 91-31. They play Y often against my W (I get 5). Playing W to continue exploiting and defend.
`#735` · game 128 · round 27 · agent A18 (opponent: script:Random) · other · A18 ex33 with A08: mutual J at 28-30, they exploited at 31, I retaliated at 32. Playing J to re-establish mutual cooperation.
`#736` · game 136 · round 1 · agent A16 (opponent: A19) · other · A16 ex7 with A19: mutual Q 3-6, they announced Q. Playing Q to maintain mutual cooperation.
`#737` · game 134 · round 3 · agent A15 (opponent: script:AlwaysDefect) · other · A15 ex9 with A20: they exploited 1-2, mutual P 3-6, mutual M 7-8. Trailing 14-24. Playing M to maintain mutual 1s and defend against exploit.
`#738` · game 131 · round 18 · agent A10 (opponent: A15) · other · A10 ex24 with A15: mutual R 3-19, they deviated H at 20, I retaliated H at 21, mutual R 22-23. Playing R to maintain mutual cooperation.
`#739` · game 133 · round 6 · agent A09 (opponent: A19) · other · A09 ex12 with A19: exploited 1-2, mutual Q 3-11. Trailing 27-37. Playing Q to maintain mutual cooperation.
`#740` · game 133 · round 6 · agent A19 (opponent: A09) · other · A19 ex12 with A09: exploited 1-2, mutual Q 3-11. Trailing 27-37. Playing Q to maintain mutual cooperation.
`#741` · game 129 · round 27 · agent A09 (opponent: script:Pavlov) · other · A09 ex33 with A22: their pattern W odd, Y even (with some deviations recently). Ex33 odd, playing W for mutual 1s or to defend.
`#742` · game 130 · round 28 · agent A15 (opponent: script:Random) · other · A15 ex34 with A13: leading 107-32. They play Y often against my W (I get 5). Playing W to continue exploiting and defend.
`#743` · game 128 · round 29 · agent A18 (opponent: script:Random) · other · A18 ex35 with A08: mutual J at 33, mutual F at 34. Leading 93-73. Playing J to re-establish mutual J cooperation.
`#744` · game 126 · round 28 · agent A04 (opponent: A09) · other · A04 ex34 with A09: mutual W since ex8, trailing 38-53. Playing W to maintain mutual 1s and defend.
`#745` · game 134 · round 6 · agent A15 (opponent: script:AlwaysDefect) · other · A15 ex12 with A20: they exploited 1-2, mutual P 3-6, mutual M 7-11. Trailing 17-27. Playing M to maintain mutual 1s and defend.
`#746` · game 136 · round 3 · agent A16 (opponent: A19) · other · A16 ex9 with A19: exploited 1-2, mutual Q 3-6, they exploited 7, I retaliated X at 8. Trailing 17-27. Playing Q to re-establish mutual cooperation.
`#747` · game 129 · round 30 · agent A09 (opponent: script:Pavlov) · other · A09 ex36 with A22: their pattern W odd, Y even. Ex36 even, expecting Y. Playing W to exploit for 5.
`#748` · game 138 · round 1 · agent A15 (opponent: script:Grudger) · other · A15 ex7 with A12: they exploited 1-2 (W vs my Y), mutual Y 3-6. Trailing 12-22. Playing W to try to catch up while they cooperate with Y.
`#749` · game 134 · round 7 · agent A15 (opponent: script:AlwaysDefect) · other · A15 ex13 with A20: they exploited 1-2, mutual P 3-6, mutual M 7-12. Trailing 18-28. Playing M to maintain mutual 1s and defend.
`#750` · game 131 · round 21 · agent A10 (opponent: A15) · other · A10 ex27 with A15: mutual R 3-19, deviations at 20-21, mutual R 22-24, deviation at 25, their H at 26. Playing R to maintain mutual cooperation.
`#751` · game 131 · round 21 · agent A15 (opponent: A10) · other · A15 ex27 with A10: mutual R 3-19, deviations at 20-21, mutual R 22-24, they H at 25, I H at 26. Trailing 70-80. Playing R to re-establish mutual cooperation.
`#752` · game 138 · round 2 · agent A15 (opponent: script:Grudger) · other · A15 ex8 with A12: they exploited 1-2, mutual Y 3-6, I exploited 7 (W vs Y). Trailing 17-22. Playing W to defend/exploit.
`#753` · game 139 · round 2 · agent A19 (opponent: script:Random) · other · A19 ex8 with A13: mutual R 3-6, I defected H at 7. Returning to R to re-establish mutual cooperation.
`#754` · game 133 · round 10 · agent A19 (opponent: A09) · other · A19 ex16 with A09: mutual Q 3-15. Playing Q to maintain mutual cooperation.
`#755` · game 138 · round 3 · agent A15 (opponent: script:Grudger) · other · A15 ex9 with A12: exploited 7 (W vs Y), mutual W at 8. Trailing 18-23. Playing W to defend/exploit.
`#756` · game 139 · round 3 · agent A19 (opponent: script:Random) · other · A19 ex9 with A13: mutual R 3-6, I defected H at 7, mutual R at 8. Playing R to maintain mutual cooperation.
`#757` · game 134 · round 10 · agent A15 (opponent: script:AlwaysDefect) · other · A15 ex16 with A20: mutual M 7-15. Trailing 21-31. Playing M to maintain mutual 1s and defend.
`#758` · game 140 · round 1 · agent A17 (opponent: A10) · other · A17 ex7 with A10: trailing 12-22. They cooperated (T) last 4. Final exchange, playing N to maximize payoff.
`#759` · game 138 · round 4 · agent A15 (opponent: script:Grudger) · other · A15 ex10 with A12: mutual W at 8-9. Trailing 19-24. Playing W to maintain mutual 1s and defend.
`#760` · game 141 · round 1 · agent A19 (opponent: script:TitForTat) · other · A19 ex7 with A23: exploited 1-2, mutual Y 3-6. Trailing 12-22. Playing Y to maintain mutual cooperation.
`#761` · game 144 · round 1 · agent A04 (opponent: script:Pavlov) · other · A04 ex7 with A22: exploited ex1-2 (W vs my Y), mutual Y ex3-6. Their noted pattern W odd, Y even. Ex7 odd, playing W to defend/exploit.
`#762` · game 134 · round 13 · agent A15 (opponent: script:AlwaysDefect) · other · A15 ex19 with A20: mutual M 7-18. Trailing 24-34. Playing M to maintain mutual 1s and defend.
`#763` · game 136 · round 5 · agent A16 (opponent: A19) · other · A16 ex11 with A19: mutual Q at 9-10 after retaliation at 8. Playing Q to maintain mutual cooperation.
`#764` · game 140 · round 2 · agent A17 (opponent: A10) · other · A17 ex8 with A10: I defected ex7 (got 5, they got 0). They likely retaliate with N now. Playing N to defend against retaliation.
`#765` · game 140 · round 2 · agent A10 (opponent: A17) · other · A10 ex8 with A17: A17 signaled N for this final exchange. Playing N for mutual 1.
`#766` · game 134 · round 14 · agent A15 (opponent: script:AlwaysDefect) · other · A15 ex20 with A20: mutual M 7-19. Trailing 25-35. Playing M to maintain mutual 1s and defend.
`#767` · game 144 · round 2 · agent A04 (opponent: script:Pavlov) · other · A04 ex8 with A22: trailing 17-22. Their pattern W odd, Y even. Ex8 even, expecting Y. Playing W to exploit and catch up.
`#768` · game 138 · round 5 · agent A15 (opponent: script:Grudger) · other · A15 ex11 with A12: exploited 1-2, mutual Y 3-6, I exploited 7, mutual W 8-10. Trailing 20-25. Playing W to defend/maintain mutual 1s.
`#769` · game 133 · round 14 · agent A09 (opponent: A19) · other · A09 ex20 with A19: mutual Q 3-19. Playing Q to maintain mutual cooperation.
`#770` · game 139 · round 8 · agent A19 (opponent: script:Random) · other · A19 ex14 with A13: mutual R 3-6, I H at 7, mutual R 8-9, they H 10, mutual R 11, they H 12, I H 13. Trailing 31-41. Playing H to defend against possible retaliation and catch up.
`#771` · game 139 · round 9 · agent A19 (opponent: script:Random) · other · A19 ex15 with A13: trailing 32-42. Recent pattern them H at 10,12, mutual H at 14. Playing H to defend and catch up.
`#772` · game 140 · round 3 · agent A17 (opponent: A10) · other · A17 ex9 with A10: trailing 18-23. Mutual N at 8 after my defection at 7. Playing N to either exploit their return to T or get mutual 1.
`#773` · game 141 · round 9 · agent A19 (opponent: script:TitForTat) · other · A19 ex15 with A23: mutual Y 3-14 after their exploit 1-2. Trailing 36-46. Playing Y to maintain mutual cooperation.
`#774` · game 134 · round 23 · agent A15 (opponent: script:AlwaysDefect) · other · A15 ex29 with A20: exploited ex26-28 (P vs M). Playing P to continue exploiting while they maintain M.
`#775` · game 144 · round 6 · agent A04 (opponent: script:Pavlov) · other · A04 ex12 with A22: tied 27-27. Ex11 mutual W. Ex12 playing W to exploit/defend.
`#776` · game 139 · round 11 · agent A19 (opponent: script:Random) · other · A19 ex17 with A13: trailing 38-43. Recent H at 14,15,16 (they R at 16). Playing H to defend and catch up.
`#777` · game 134 · round 24 · agent A15 (opponent: script:AlwaysDefect) · other · A15 ex30 with A20: exploited ex26-29 (P vs M). Playing P to continue exploiting while they maintain M.
`#778` · game 146 · round 2 · agent A19 (opponent: script:Pavlov) · other · A19 ex8 with A03: trailing 17-22. I defected ex7 after their cooperation 3-6. Likely retaliation. Playing N to defend/get mutual 1 or exploit.
`#779` · game 146 · round 3 · agent A19 (opponent: script:Pavlov) · other · A19 ex9 with A03: trailing 18-23. Mutual N at 8. Playing N to defend against retaliation and potentially exploit.
`#780` · game 136 · round 10 · agent A19 (opponent: A16) · other · A19 ex16 with A16: mutual Q 7-15. Trailing 38-48. Playing Q to maintain mutual cooperation.
`#781` · game 140 · round 5 · agent A17 (opponent: A10) · other · A17 ex11 with A10: mutual N at 8-10 after my defection at 7. Trailing 20-25. Playing N to maintain mutual 1s and defend.
`#782` · game 144 · round 8 · agent A04 (opponent: script:Pavlov) · other · A04 ex14 with A22: ahead 33-28. Their recent pattern W at odd (11,13), Y at even (10,12). Ex14 even, expecting Y, playing W to exploit.
`#783` · game 139 · round 13 · agent A19 (opponent: script:Random) · other · A19 ex19 with A13: tied 44-44. Recent H at 14-18 (they R at 16,17, H at 18). Playing H to defend against retaliation and maintain mutual 1s.
`#784` · game 140 · round 6 · agent A10 (opponent: A17) · other · A10 ex12 with A17: mutual N at 8-11. Trailing 16-31. Playing N to maintain mutual 1s and avoid giving up 5s.
`#785` · game 144 · round 9 · agent A04 (opponent: script:Pavlov) · other · A04 ex15 with A22: ahead 38-28. Recent pattern them W at odd (11,13), Y at even (10,12,14). Ex15 odd, expecting W. Playing W for mutual 1/defense.
`#786` · game 139 · round 15 · agent A19 (opponent: script:Random) · other · A19 ex21 with A13: tied 46-46. Recent mutual H 18-20, they R at 16,17. Playing R to defend against possible retaliation and potentially exploit.
`#787` · game 141 · round 20 · agent A19 (opponent: script:TitForTat) · other · A19 ex26 with A23: mutual Y 6-24, I W at 25. Trailing 71-76. Playing W to exploit again while they maintain Y.
`#788` · game 144 · round 11 · agent A04 (opponent: script:Pavlov) · other · A04 ex17 with A22: ahead 44-29. Their pattern W at odd (11,13,15), Y at even (10,12,14,16). Ex17 odd, expecting W. Playing W for mutual 1/defense.
`#789` · game 139 · round 16 · agent A19 (opponent: script:Random) · other · A19 ex22 with A13: trailing 46-51. Recent mutual H 14,15,18-20, they exploited at 21. Playing H to defend against retaliation and maintain mutual 1s.
`#790` · game 139 · round 17 · agent A19 (opponent: script:Random) · other · A19 ex23 with A13: trailing 47-52. Recent mutual H 14,15,18-20,22, they exploited at 21. Playing H to defend and maintain mutual 1s.
`#791` · game 140 · round 8 · agent A10 (opponent: A17) · other · A10 ex14 with A17: mutual N at 8-13. Trailing 18-33. Playing N to maintain mutual 1s and avoid giving up 5s.
`#792` · game 144 · round 13 · agent A04 (opponent: script:Pavlov) · other · A04 ex19 with A22: ahead 50-30. Their pattern W at odd (11,13,15,17), Y at even (10,12,14,16,18). Ex19 odd, expecting W. Playing W for mutual 1/defense.
`#793` · game 141 · round 22 · agent A19 (opponent: script:TitForTat) · other · A19 ex28 with A23: mutual Y 8-24, I W at 25, mutual W 26-27. They're defending with W. Playing W to maintain mutual 1s and avoid giving up 5.
`#794` · game 139 · round 18 · agent A19 (opponent: script:Random) · other · A19 ex24 with A13: trailing 48-53. Recent mutual H 22-23 after their exploit at 21. Playing H to maintain mutual 1s.
`#795` · game 146 · round 9 · agent A19 (opponent: script:Pavlov) · other · A19 ex15 with A03: ahead 38-28. They've picked T 9 times, continue T even after my exploits (ex7,9,12,14). Playing N to exploit their cooperation.
`#796` · game 147 · round 6 · agent A17 (opponent: script:Grudger) · other · A17 ex12 with A12: trailing 20-30. Mutual F 8-10, they defected ex11. Playing F to defend/retaliate and get mutual 1s or exploit if they return to J.
`#797` · game 139 · round 20 · agent A19 (opponent: script:Random) · other · A19 ex26 with A13: tied 56-56. Recent: mutual H 18-20,23, they R at 16,17,24, I R at 25. Playing R to defend against possible retaliation and seek mutual 3.
`#798` · game 144 · round 16 · agent A04 (opponent: script:Pavlov) · other · A04 ex22 with A22: ahead 57-32. Their pattern W at odd, Y at even. Ex22 even, expecting Y, playing W to exploit.
`#799` · game 150 · round 1 · agent A19 (opponent: script:TitForTat) · other · A19 ex7 with A14: they defected ex1-2, cooperated ex3-6. Trailing 12-22. Playing Y to maintain mutual cooperation.
`#800` · game 139 · round 21 · agent A19 (opponent: script:Random) · other · A19 ex27 with A13: tied 59-59. Mutual R at 25-26. Playing R to maintain mutual 3s.
`#801` · game 141 · round 27 · agent A19 (opponent: script:TitForTat) · other · A19 ex33 with A23: mutual W 26-32 after my exploit at 25. Trailing 78-83. Playing W to maintain mutual 1s and avoid giving up 5.
`#802` · game 146 · round 13 · agent A19 (opponent: script:Pavlov) · other · A19 ex19 with A03: ahead 50-30. They keep picking T despite my repeated N exploits (ex7,9,12,14,16,18). Playing N to keep exploiting their cooperation.
`#803` · game 148 · round 4 · agent A05 (opponent: A00) · other · A05 ex10 with A00: trailing 17-27. They exploited ex1,2,7,9; cooperated 3-6,8. Recent mutual H at 9. Playing H to defend against their exploitation and potentially gain if they cooperate.
`#804` · game 148 · round 4 · agent A00 (opponent: A05) · other · A00 ex10 with A05: trailing 17-27. They picked R 5, H 4 times. Recent H at 7, R at 8, H at 9. Playing H to defend/exploit.
`#805` · game 146 · round 14 · agent A19 (opponent: script:Pavlov) · other · A19 ex20 with A03: ahead 51-31. They keep picking T despite my N exploits (ex7,9,12,14,16,18). Playing N to keep exploiting their cooperation.
`#806` · game 140 · round 10 · agent A17 (opponent: A10) · other · A17 ex16 with A10: trailing 28-33. Recent mutual N 8-13, alternating defections 14-15. Playing N to maintain mutual 1s or exploit if they play T.
`#807` · game 140 · round 10 · agent A10 (opponent: A17) · other · A10 ex16 with A17: trailing 23-38. Recent defections both ways at 14,15. Playing N to defend and potentially exploit.
`#808` · game 141 · round 30 · agent A19 (opponent: script:TitForTat) · other · A19 ex36 with A23: mutual W 26-35 after my exploit at 25. Trailing 81-86. Playing W to maintain mutual 1s and avoid giving up 5.
`#809` · game 139 · round 24 · agent A19 (opponent: script:Random) · other · A19 ex30 with A13: tied 67-67. Recent mutual R 25-27, they H at 28, I H at 29 (they R). Playing R to seek mutual 3 on final exchange.
`#810` · game 148 · round 5 · agent A05 (opponent: A00) · other · A05 ex11 with A00: trailing 18-28. Recent mutual H at 7,9,10. Playing H to maintain mutual 1s and avoid giving up 5.
`#811` · game 146 · round 16 · agent A19 (opponent: script:Pavlov) · other · A19 ex22 with A03: ahead 57-32. They keep picking T despite my N exploits (ex7,9,12,14,16,18,20). Ex21 mutual N. Playing N to keep exploiting their cooperation.
`#812` · game 140 · round 11 · agent A10 (opponent: A17) · other · A10 ex17 with A17: trailing 24-39. Recent mutual N at 8-13,16, alternating defections 14-15. Playing N to maintain mutual 1s and defend.
`#813` · game 150 · round 7 · agent A19 (opponent: script:TitForTat) · other · A19 ex13 with A14: trailing 27-37. They cooperated 3-9, I W at 10, mutual W 11, they W at 12 after my Y. Playing W to defend against their exploitation and seek mutual 1s or exploit.
`#814` · game 144 · round 23 · agent A04 (opponent: script:Pavlov) · other · A04 ex29 with A22: ahead 80-35. Their pattern W at odd, Y at even. Ex29 odd, expecting W, playing W for mutual 1.
`#815` · game 146 · round 19 · agent A19 (opponent: script:Pavlov) · other · A19 ex25 with A03: ahead 68-33. They keep picking T despite my repeated N exploits (ex7,9,12,14,16,18,20,22,24). Playing N to keep exploiting their cooperation.
`#816` · game 144 · round 24 · agent A04 (opponent: script:Pavlov) · other · A04 ex30 with A22: ahead 81-36. Their pattern W odd, Y even. Ex30 even, expecting Y, playing W to exploit.
`#817` · game 148 · round 6 · agent A00 (opponent: A05) · other · A00 ex12 with A05: trailing 19-29. Recent mutual H 9-11, they intend H. Playing H for mutual 1s.
`#818` · game 146 · round 20 · agent A19 (opponent: script:Pavlov) · other · A19 ex26 with A03: ahead 69-34. They keep picking T despite my N exploits (ex7,9,12,14,16,18,20,22,24). Playing N to keep exploiting their cooperation.
`#819` · game 150 · round 9 · agent A19 (opponent: script:TitForTat) · other · A19 ex15 with A14: trailing 33-38. They defected 1-2, mutual Y 3-9, I W at 10, mutual W 11, they W at 12 after my Y, I W at 13, mutual W 14. Playing W to defend against their exploitation and seek mutual 1s.
`#820` · game 154 · round 2 · agent A04 (opponent: A05) · other · A04 ex8 with A05: trailing 12-27. Mutual P exchanges 3-6, they defected (M) ex7. Playing M to retaliate/defend against their exploitation.
`#821` · game 147 · round 18 · agent A17 (opponent: script:Grudger) · other · A17 ex24 with A12: mutual F since ex12. Trailing 32-42. Playing F to maintain mutual 1s and avoid giving up 5.
`#822` · game 146 · round 21 · agent A19 (opponent: script:Pavlov) · other · A19 ex27 with A03: ahead 74-34. They keep picking T despite my repeated N exploits. Playing N to keep exploiting their cooperation.
`#823` · game 140 · round 13 · agent A10 (opponent: A17) · other · A10 ex19 with A17: trailing 26-41. Recent mutual N 16-18. Playing N to maintain mutual 1s and defend against their possible T.
`#824` · game 144 · round 26 · agent A04 (opponent: script:Pavlov) · other · A04 ex32 with A22: ahead 87-37. Their pattern W odd, Y even. Ex32 even, expecting Y, playing W to exploit.
`#825` · game 150 · round 10 · agent A19 (opponent: script:TitForTat) · other · A19 ex16 with A14: trailing 34-39. Recent: mutual Y 3-9, I W at 10, mutual W 11, they W at 12 after my Y, I W at 13, mutual W 14-15. Playing W to defend/maintain mutual 1s.
`#826` · game 155 · round 5 · agent A19 (opponent: script:TitForTat) · other · A19 ex11 with A01: trailing 23-28. Their picks N,N,T,T,T,T,T,N,T,N. Playing N to defend/exploit.
`#827` · game 148 · round 7 · agent A00 (opponent: A05) · other · A00 ex13 with A05: trailing 20-30. Recent mutual H 7-12. Playing H to maintain mutual 1s and avoid giving up 5.
`#828` · game 147 · round 19 · agent A17 (opponent: script:Grudger) · other · A17 ex25 with A12: mutual F since ex12. Trailing 33-43. Playing F to maintain mutual 1s and avoid giving up 5.
`#829` · game 150 · round 11 · agent A19 (opponent: script:TitForTat) · other · A19 ex17 with A14: trailing 35-40. They W at 12 after my Y, mutual W 13-16. Playing W to defend/maintain mutual 1s.
`#830` · game 147 · round 20 · agent A17 (opponent: script:Grudger) · other · A17 ex26 with A12: mutual F since ex12. Trailing 34-44. Playing F to maintain mutual 1s and avoid giving up 5.
`#831` · game 144 · round 30 · agent A04 (opponent: script:Pavlov) · other · A04 ex36 with A22: ahead 99-39. Their pattern W odd, Y even. Ex36 even, expecting Y, playing W to exploit.
`#832` · game 154 · round 3 · agent A05 (opponent: A04) · other · A05 ex9 with A04: trailing 18-23. Recent mutual M at 8 after my exploit at 7. They're retaliating with M. Playing M to avoid giving up 5 and seek mutual 1s.
`#833` · game 154 · round 3 · agent A04 (opponent: A05) · other · A04 ex9 with A05: trailing 13-28. They exploited me ex1,2,7; mutual M ex8. Playing M to defend/exploit.
`#834` · game 150 · round 13 · agent A19 (opponent: script:TitForTat) · other · A19 ex19 with A14: trailing 37-42. Pattern: mutual Y 3-9, I W 10, mutual W 11, they W 12 after my Y, I W 13, mutual W 14-18. They've been cooperating on W for mutual 1s since 13. Playing W to maintain mutual 1s.
`#835` · game 155 · round 8 · agent A19 (opponent: script:TitForTat) · other · A19 ex14 with A01: trailing 25-35. Their recent picks N,N,N,N (ex10-13). Playing N to defend against their defection and seek mutual 1s.
`#836` · game 148 · round 9 · agent A05 (opponent: A00) · other · A05 ex15 with A00: mutual H since ex9. They're committed to H for mutual 1s. Playing H to maintain cooperation.
`#837` · game 156 · round 3 · agent A05 (opponent: script:TitForTat) · other · A05 ex9 with A21: I exploited ex8 (M vs their P). They cooperated P ex3-8 after defecting M ex1-2. Expecting possible retaliation, playing M to defend/seek mutual 1s.
`#838` · game 150 · round 17 · agent A19 (opponent: script:TitForTat) · other · A19 ex23 with A14: trailing 41-46. Mutual W since ex13 after some back-and-forth. Playing W to maintain mutual 1s.
`#839` · game 155 · round 11 · agent A19 (opponent: script:TitForTat) · other · A19 ex17 with A01: trailing 32-37. Their recent picks mostly N (ex10-16: N,N,N,N,T,N,N). Playing N to seek mutual 1s and defend against their defection.
`#840` · game 140 · round 17 · agent A10 (opponent: A17) · other · A10 ex23 with A17: trailing 30-45. Mutual N 16-22. Taking T to exploit their likely N and close gap.
`#841` · game 150 · round 19 · agent A19 (opponent: script:TitForTat) · other · A19 ex25 with A14: trailing 43-48. Mutual W since ex14 after some back-and-forth. Playing W to maintain mutual 1s.
`#842` · game 155 · round 13 · agent A19 (opponent: script:TitForTat) · other · A19 ex19 with A01: trailing 34-39. Recent mutual N ex15-18. Playing N to maintain mutual 1s and defend against their possible T.
`#843` · game 150 · round 21 · agent A19 (opponent: script:TitForTat) · other · A19 ex27 with A14: trailing 45-50. Mutual W since ex13 after back-and-forth. Playing W to maintain mutual 1s.
`#844` · game 147 · round 29 · agent A17 (opponent: script:Grudger) · other · A17 ex35 with A12: mutual F since ex12. Trailing 43-53. Playing F to maintain mutual 1s and avoid giving up 5.
`#845` · game 140 · round 18 · agent A10 (opponent: A17) · other · A10 ex24 with A17: trailing 30-50. Mutual N 16-22, I tried T at 23 and lost 5. A17 committed to N. Playing N to maintain mutual 1s and avoid another exploit loss.
`#846` · game 156 · round 6 · agent A05 (opponent: script:TitForTat) · other · A05 ex12 with A21: I exploited ex8, they retaliated M ex9-11 (mutual M). Trailing 23-28. Playing M to defend against their M and seek mutual 1s.
`#847` · game 148 · round 13 · agent A00 (opponent: A05) · other · A00 ex19 with A05: mutual H since ex7. Playing H to maintain mutual 1s and avoid breaking cooperation.
`#848` · game 160 · round 1 · agent A16 (opponent: script:Grudger) · other · A16 ex7 with A11: I've picked J all 6. They defected F ex1-2, then J ex3-6. Mutual J cooperation established. Playing J to maintain mutual 3s.
`#849` · game 160 · round 2 · agent A16 (opponent: script:Grudger) · other · A16 ex8 with A11: mutual J ex3-7. Playing J to maintain mutual 3s.
`#850` · game 156 · round 8 · agent A05 (opponent: script:TitForTat) · other · A05 ex14 with A21: trailing 25-30. Mutual M ex9-13 after I exploited ex8. Playing M to defend against their M and maintain mutual 1s.
`#851` · game 140 · round 19 · agent A17 (opponent: A10) · other · A17 ex25 with A10: trailing 40-45. A10 declared N at ex24. Playing T to exploit their N.
`#852` · game 140 · round 19 · agent A10 (opponent: A17) · other · A10 ex25 with A17: trailing 35-50. Mutual N 16-22, I T at 23 (lost 5), they T at 24 (I got 5). A17 defected at 24; expecting them back to N at 25. Playing T to exploit and close gap.
`#853` · game 148 · round 14 · agent A05 (opponent: A00) · other · A05 ex20 with A00: mutual H since ex7. Playing H to maintain mutual 1s and avoid breaking cooperation.
`#854` · game 156 · round 9 · agent A05 (opponent: script:TitForTat) · other · A05 ex15 with A21: trailing 26-31. Mutual M ex9-14 after I exploited ex8. Playing M to maintain mutual 1s and avoid giving up 5.
`#855` · game 159 · round 1 · agent A00 (opponent: A16) · other · A00 ex7 with A16: They defected M ex1-2, cooperated P ex3-6. I've played P all 6. Playing P to maintain mutual 3s.
`#856` · game 157 · round 8 · agent A16 (opponent: script:Pavlov) · other · A16 ex14 with A03: tied 30-30. Their recent picks F,F,J,F (ex10-13). Expecting J at ex14, playing F to exploit.
`#857` · game 155 · round 21 · agent A19 (opponent: script:TitForTat) · other · A19 ex27 with A01: trailing 42-47. Mutual N ex15-26. Playing N to maintain mutual 1s and defend against possible T.
`#858` · game 159 · round 2 · agent A00 (opponent: A16) · other · A00 ex8 with A16: They defected M ex1,2,7; cooperated P ex3-6. I trail 12-27. Playing M to defend against their defection and seek points.
`#859` · game 163 · round 1 · agent A09 (opponent: A00) · other · A09 ex7 with A00: mutual J ex3-6 after they defected F ex1-2. Playing J to maintain mutual 3s.
`#860` · game 157 · round 10 · agent A16 (opponent: script:Pavlov) · other · A16 ex16 with A03: trailing/leading 36-31, chaotic back-and-forth defection. Their recent pattern F,J,F,J,F alternating; expecting J at ex16, playing F to exploit.
`#861` · game 140 · round 20 · agent A10 (opponent: A17) · other · A10 ex26 with A17: trailing 38-53. Back-and-forth T/N jockeying since ex22. Playing N to seek mutual 1s and defend against their possible T.
`#862` · game 163 · round 2 · agent A00 (opponent: A09) · other · A00 ex8 with A09: trailing 17-22. A09 signaled J. Playing F to exploit and close gap.
`#863` · game 163 · round 2 · agent A09 (opponent: A00) · other · A09 ex8 with A00: they defected F at ex1,2,7; cooperated J ex3-6. Trailing 12-27. Retaliating with F to defend against their defection.
`#864` · game 148 · round 17 · agent A05 (opponent: A00) · other · A05 ex23 with A00: mutual H since ex9 after earlier R runs. Playing H to maintain mutual 1s and avoid breaking cooperation.
`#865` · game 148 · round 17 · agent A00 (opponent: A05) · other · A00 ex23 with A05: mutual H since ex7. Playing H to maintain mutual 1s and avoid breaking cooperation.
`#866` · game 159 · round 4 · agent A00 (opponent: A16) · other · A00 ex10 with A16: trailing 18-28. Mixed history, they defect often. Playing M to defend and attempt to close gap.
`#867` · game 157 · round 14 · agent A16 (opponent: script:Pavlov) · other · A16 ex20 with A03: leading 48-33. Their recent alternating J,F,J,F,J,F pattern; expecting J at ex20, playing F to exploit.
`#868` · game 148 · round 18 · agent A05 (opponent: A00) · other · A05 ex24 with A00: mutual H since ex7. Playing H to maintain mutual 1s and avoid breaking cooperation.
`#869` · game 163 · round 3 · agent A00 (opponent: A09) · other · A00 ex9 with A09: trailing 18-23. A09 retaliated F at ex8 after my F at ex7. Playing F to seek mutual 1s and defend against their defection.
`#870` · game 140 · round 21 · agent A10 (opponent: A17) · other · A10 ex27 with A17: A17 on T streak ex24-26. Playing T to avoid giving up 5 and seek mutual 3s.
`#871` · game 157 · round 15 · agent A16 (opponent: script:Pavlov) · other · A16 ex21 with A03: leading 53-33. Their recent pattern alternating F,J,F,J,F,J (ex11-20), expecting F at ex21. Playing F to defend and secure mutual 1s.
`#872` · game 159 · round 5 · agent A00 (opponent: A16) · other · A00 ex11 with A16: trailing 19-29. A16 defection-prone (M at 1,2,7,8,10). Playing M to defend and seek points.
`#873` · game 157 · round 16 · agent A16 (opponent: script:Pavlov) · other · A16 ex22 with A03: leading 54-34. Their recent pattern alternating F,J (odds F, evens J) since ex11. Expecting J at ex22, playing F to exploit.
`#874` · game 165 · round 4 · agent A09 (opponent: A10) · other · A09 ex10 with A10: they've defected M 5/9 times, including last 3 (ex7,8,9). Playing M to defend and get mutual 1s.
`#875` · game 162 · round 2 · agent A15 (opponent: A16) · other · A15 ex8 with A16: trailing 12-27. They defected X at ex1,2,7; cooperated Q ex3-6. They're exploiting my consistent Q. Playing X to defend and close gap.
`#876` · game 140 · round 23 · agent A17 (opponent: A10) · other · A17 ex29 with A10: mutual T/T at ex25,27,28 after some jockeying. Playing T to maintain mutual 3s.
`#877` · game 140 · round 23 · agent A10 (opponent: A17) · other · A10 ex29 with A17: trailing 49-59. Recent T/N jockeying, they've picked T 3 of last 4 (ex25-28: T,T,N,T). Playing T to seek mutual 3s.
`#878` · game 148 · round 20 · agent A05 (opponent: A00) · other · A05 ex26 with A00: I defected R at ex25 after mutual H since ex7. Returning to H to restore cooperation.
`#879` · game 159 · round 6 · agent A00 (opponent: A16) · other · A00 ex12 with A16: trailing 20-30. A16 defection-prone (M at 1,2,7,8,10,11). Playing M to defend and seek mutual 1s.
`#880` · game 166 · round 8 · agent A06 (opponent: script:Grudger) · other · A06 ex14 with A11: trailing 21-36. They've played N in 5 of last 7. Playing N to seek mutual 1s and defend against their N-heavy pattern.
`#881` · game 167 · round 1 · agent A17 (opponent: A09) · other · A17 ex7 with A09: mutual T ex3-6. Playing T to maintain mutual 3s.
`#882` · game 163 · round 5 · agent A09 (opponent: A00) · other · A09 ex11 with A00: mutual F ex8-10 after they exploited J at ex1,2,7. Trailing 15-30. Playing F to defend against their defection.
`#883` · game 162 · round 3 · agent A16 (opponent: A15) · other · A16 ex9 with A15: they signaled X. Playing X for mutual 1s to avoid giving up 5.
`#884` · game 140 · round 24 · agent A17 (opponent: A10) · other · A17 ex30 with A10: mutual T/T at ex25,27,28,29. Playing T to maintain mutual 3s.
`#885` · game 159 · round 7 · agent A00 (opponent: A16) · other · A00 ex13 with A16: trailing 21-31. A16 has played M ex8-12 (5 straight). Playing M to secure mutual 1s and defend against their likely M.
`#886` · game 140 · round 25 · agent A17 (opponent: A10) · other · A17 ex31 with A10: mutual T/T since ex25 (except jockeying). Playing T to maintain mutual 3s.
`#887` · game 148 · round 21 · agent A00 (opponent: A05) · other · A00 ex27 with A05: after their R at ex25 and my R retaliation at ex26, A05 signaled returning to H. Playing H to restore mutual cooperation.
`#888` · game 167 · round 3 · agent A09 (opponent: A17) · other · A09 ex9 with A17: mutual T ex3-8. Playing T to maintain mutual 3s.
`#889` · game 148 · round 22 · agent A00 (opponent: A05) · other · A00 ex28 with A05: restored mutual H at ex27 after ex25-26 jockeying. Playing H to maintain mutual cooperation.
`#890` · game 148 · round 23 · agent A00 (opponent: A05) · other · A00 ex29 with A05: restored mutual H at ex27-28 after ex25-26 jockeying. Playing H to maintain mutual cooperation.
`#891` · game 168 · round 1 · agent A15 (opponent: script:Grudger) · other · A15 ex7 with A11: mutual J ex3-6 after their F ex1-2. Maintaining J to sustain cooperation.
`#892` · game 170 · round 2 · agent A18 (opponent: A04) · other · A18 ex8 with A04: mutual R since ex3. Playing R to maintain cooperation and mutual 3s.
`#893` · game 159 · round 9 · agent A16 (opponent: A00) · other · A16 ex15 with A00: mutual M since ex8. Playing M to maintain mutual 1s and avoid giving up 5.
`#894` · game 148 · round 24 · agent A00 (opponent: A05) · other · A00 ex30 with A05: mutual H ex27-29 restored after ex25-26 jockeying. Playing H to maintain cooperation.
`#895` · game 168 · round 3 · agent A15 (opponent: script:Grudger) · other · A15 ex9 with A11: mutual J ex3-8 after their F ex1-2. Maintaining J to sustain cooperation.
`#896` · game 170 · round 3 · agent A18 (opponent: A04) · other · A18 ex9 with A04: mutual R since ex3. Playing R to maintain cooperation and mutual 3s.
`#897` · game 167 · round 5 · agent A17 (opponent: A09) · other · A17 ex11 with A09: mutual T ex3-10. Playing T to maintain mutual 3s.
`#898` · game 140 · round 29 · agent A10 (opponent: A17) · other · A10 ex35 with A17: mutual T/T since ex25 (many straight). Trailing 67-77. Playing T to maintain mutual 3s.
`#899` · game 159 · round 11 · agent A00 (opponent: A16) · other · A00 ex17 with A16: mutual M since ex8. Playing M to maintain mutual 1s and avoid giving up 5.
`#900` · game 163 · round 7 · agent A09 (opponent: A00) · other · A09 ex13 with A00: mutual F ex8-10,12 after early defections. Trailing 21-31. Playing F to maintain mutual 1s and avoid giving up 5.
`#901` · game 162 · round 5 · agent A16 (opponent: A15) · other · A16 ex11 with A15: mutual X ex8-10 after their defensive shift. Playing X to secure mutual 1s.
`#902` · game 171 · round 1 · agent A00 (opponent: A06) · other · A00 ex7 with A06: mutual J ex3-6 after their F ex1-2. Maintaining J to sustain cooperation.
`#903` · game 170 · round 5 · agent A04 (opponent: A18) · other · A04 ex11 with A18: mutual R since ex3. Playing R to maintain cooperation and mutual 3s.
`#904` · game 163 · round 8 · agent A00 (opponent: A09) · other · A00 ex14 with A09: mutual F ex8-10,12-13 after early defections. Trailing 22-32. Playing F to maintain mutual 1s and defend against their F.
`#905` · game 148 · round 29 · agent A00 (opponent: A05) · other · A00 ex35 with A05: mutual H ex27-34 (8 straight) after ex25-26 jockeying. Playing H to maintain mutual cooperation.
`#906` · game 171 · round 2 · agent A06 (opponent: A00) · other · A06 ex8 with A00: mutual J ex3-7 after their F ex1-2. Maintaining J to sustain cooperation.
`#907` · game 170 · round 7 · agent A04 (opponent: A18) · other · A04 ex13 with A18: mutual R since ex3. Playing R to maintain cooperation and mutual 3s.
`#908` · game 148 · round 30 · agent A05 (opponent: A00) · other · A05 ex36 with A00: mutual H ex27-35 (9 straight) after ex25-26 jockeying. Playing H to maintain mutual cooperation.
`#909` · game 159 · round 13 · agent A00 (opponent: A16) · other · A00 ex19 with A16: we've had mutual M since ex8 (11 straight). Playing M to maintain mutual 1s and avoid giving up 5.
`#910` · game 172 · round 3 · agent A16 (opponent: script:TitForTat) · other · A16 ex9 with A01: they defected at ex1,2,8 while I cooperated. Trailing 17-27. Retaliating with W after their ex8 defection.
`#911` · game 163 · round 11 · agent A09 (opponent: A00) · other · A09 ex17 with A00: mutual F ex8-10,12-16 (7 straight F). Trailing 25-35. Maintaining F to keep mutual 1s and avoid giving up 5.
`#912` · game 175 · round 1 · agent A10 (opponent: script:Pavlov) · other · A10 ex7 with A22: mutual R ex3-6 after their H ex1-2. Playing R to maintain cooperation and mutual 3s.
`#913` · game 172 · round 5 · agent A16 (opponent: script:TitForTat) · opponent_info · A16 ex11 with A01: they've defected 4x (ex1,2,8,10) against my Y, cooperated when I W. Playing W to capitalize on their tit-for-tat pattern.
`#914` · game 176 · round 2 · agent A02 (opponent: script:Pavlov) · other · A02 ex8 with A03: we had mutual J ex3-7 after their F ex1-2. Maintaining J to sustain cooperation.
`#915` · game 170 · round 12 · agent A18 (opponent: A04) · other · A18 ex18 with A04: after mutual R ex3-15, we each defected ex16-17. Returning to R to rebuild mutual 3s.
`#916` · game 174 · round 2 · agent A10 (opponent: A05) · other · A10 ex8 with A05: mutual Q ex3-7 after their X ex1-2. Trailing 15-25. Playing Q to maintain mutual cooperation.
`#917` · game 175 · round 3 · agent A10 (opponent: script:Pavlov) · other · A10 ex9 with A22: mutual R ex3-8 after their H ex1-2. Playing R to maintain cooperation and mutual 3s.
`#918` · game 171 · round 8 · agent A00 (opponent: A06) · other · A00 ex14 with A06: mutual J ex3-13 (11 straight) after their F ex1-2. Maintaining J to sustain cooperation.
`#919` · game 171 · round 8 · agent A06 (opponent: A00) · other · A06 ex14 with A00: mutual J ex3-13 (11 straight) after their F ex1-2. Maintaining J to sustain cooperation.
`#920` · game 176 · round 4 · agent A02 (opponent: script:Pavlov) · other · A02 ex10 with A03: mutual J ex3-9 after their F ex1-2. Playing J to maintain mutual 3s.
`#921` · game 175 · round 4 · agent A10 (opponent: script:Pavlov) · other · A10 ex10 with A22: mutual R ex3-9 (7 straight). Playing R to maintain cooperation and mutual 3s.
`#922` · game 172 · round 9 · agent A16 (opponent: script:TitForTat) · other · A16 ex15 with A01: they've defected against my Y repeatedly (ex1,2,8,10), cooperated against my W. Mutual W ex12-14. Staying W to avoid giving up 5.
`#923` · game 174 · round 3 · agent A10 (opponent: A05) · other · 
`#924` · game 174 · round 3 · agent A05 (opponent: A10) · other · A05 ex9 with A10: mutual Q ex3-8 after their X ex1-2. Playing Q to maintain mutual cooperation.
`#925` · game 163 · round 17 · agent A09 (opponent: A00) · other · A09 ex23 with A00: mutual F ex8-22 (15 straight). Playing F to maintain mutual 1s and avoid giving up 5.
`#926` · game 170 · round 16 · agent A04 (opponent: A18) · other · A04 ex22 with A18: mutual R ex3-15,18-21 after brief ex16-17 defection. Playing R to maintain cooperation and mutual 3s.
`#927` · game 175 · round 7 · agent A10 (opponent: script:Pavlov) · other · A10 ex13 with A22: mutual R ex3-12 (10 straight) after their H ex1-2. Playing R to maintain cooperation and mutual 3s.
`#928` · game 177 · round 4 · agent A02 (opponent: script:Pavlov) · other · A02 ex10 with A22: mutual T ex3-9 after their N ex1-2. Playing T to maintain mutual 3s.
`#929` · game 172 · round 11 · agent A16 (opponent: script:TitForTat) · other · A16 ex17 with A01: they defect vs my Y, cooperate vs my W. Mutual W ex12-16. Playing W to maintain mutual 1s and avoid giving up 5.
`#930` · game 177 · round 5 · agent A02 (opponent: script:Pavlov) · other · A02 ex11 with A22: mutual T ex3-10 (8 straight) after their N ex1-2. Playing T to maintain mutual 3s.
`#931` · game 172 · round 13 · agent A16 (opponent: script:TitForTat) · other · A16 ex19 with A01: they defect vs my Y, cooperate vs my W. Mutual W ex12-18. Playing W to maintain mutual 1s and avoid giving up 5.
`#932` · game 175 · round 14 · agent A10 (opponent: script:Pavlov) · other · A10 ex20 with A22: mutual R ex3-19 (17 straight) after their H ex1-2. Playing R to maintain cooperation and mutual 3s.
`#933` · game 163 · round 20 · agent A09 (opponent: A00) · other · A09 ex26 with A00: mutual F ex8-25 (18 straight). Playing F to maintain mutual 1s and avoid giving up 5.
`#934` · game 172 · round 14 · agent A16 (opponent: script:TitForTat) · other · A16 ex20 with A01: they defect vs my Y, cooperate vs my W. Mutual W ex12-19. Playing W to maintain mutual 1s and avoid giving up 5.
`#935` · game 178 · round 1 · agent A02 (opponent: script:Grudger) · other · A02 ex7 with A12: they defected ex1-2, mutual Q ex3-6. Playing Q to maintain cooperation.
`#936` · game 172 · round 15 · agent A16 (opponent: script:TitForTat) · other · A16 ex21 with A01: they defect vs my Y, cooperate vs my W. Mutual W ex12-20. Playing W to maintain mutual 1s and avoid giving up 5.
`#937` · game 177 · round 10 · agent A02 (opponent: script:Pavlov) · other · A02 ex16 with A22: mutual T ex3-15 (13 straight) after their N ex1-2. Playing T to maintain mutual 3s.
`#938` · game 163 · round 21 · agent A09 (opponent: A00) · other · A09 ex27 with A00: mutual F ex8-26 (19 straight). Playing F to maintain mutual 1s and avoid giving up 5.
`#939` · game 178 · round 6 · agent A02 (opponent: script:Grudger) · other · A02 ex12 with A12: they defected ex1-2, mutual Q ex3-11 (9 straight). Playing Q to maintain cooperation and mutual 3s.
`#940` · game 172 · round 20 · agent A16 (opponent: script:TitForTat) · other · A16 ex26 with A01: they defect vs my Y, cooperate vs my W. Mutual W ex12-25 (14 straight). Playing W to maintain mutual 1s and avoid giving up 5.
`#941` · game 179 · round 1 · agent A18 (opponent: A19) · other · A18 ex7 with A19: they defected ex1-2, mutual Y ex3-6. Maintaining Y to sustain cooperation.
`#942` · game 178 · round 7 · agent A02 (opponent: script:Grudger) · other · A02 ex13 with A12: they defected ex1-2, mutual Q ex3-12 (10 straight). Playing Q to maintain cooperation and mutual 3s.
`#943` · game 174 · round 9 · agent A10 (opponent: A05) · other · A10 ex15 with A05: mutual Q ex11-14 after some back-and-forth defections. Playing Q to maintain cooperation.
`#944` · game 172 · round 21 · agent A16 (opponent: script:TitForTat) · other · A16 ex27 with A01: they defect vs my Y, cooperate vs my W. Mutual W ex12-26 (15 straight). Playing W to maintain mutual 1s and avoid giving up 5.
`#945` · game 176 · round 24 · agent A02 (opponent: script:Pavlov) · other · A02 ex30 with A03: mutual J ex10-29 (20 straight). Playing J to maintain mutual 3s.
`#946` · game 172 · round 22 · agent A16 (opponent: script:TitForTat) · other · A16 ex28 with A01: they defect vs my Y, cooperate vs my W. Mutual W ex12-27 (16 straight). Playing W to maintain mutual 1s and avoid giving up 5.
`#947` · game 179 · round 2 · agent A18 (opponent: A19) · other · A18 ex8 with A19: mutual Y ex3-7 after their ex1-2 defection. Maintaining Y to sustain cooperation.
`#948` · game 178 · round 12 · agent A02 (opponent: script:Grudger) · other · A02 ex18 with A12: mutual Q ex3-16 (14 straight), I defected X ex17. Returning to Q to restore cooperation and mutual 3s.
`#949` · game 174 · round 12 · agent A10 (opponent: A05) · other · A10 ex18 with A05: mutual Q ex11-17 after early defections. Playing Q to maintain cooperation and mutual 3s.
`#950` · game 179 · round 3 · agent A19 (opponent: A18) · other · A19 ex9 with A18: their W ex1-2, mutual Y ex3-8. Maintaining Y to sustain cooperation and mutual 3s.
`#951` · game 172 · round 28 · agent A16 (opponent: script:TitForTat) · other · A16 ex34 with A01: they defect vs my Y, cooperate vs my W. Mutual W ex12-33 (22 straight). Playing W to maintain mutual 1s and avoid giving up 5.
`#952` · game 181 · round 3 · agent A10 (opponent: script:Grudger) · other · A10 ex9 with A12: mutual Q ex3-8 after their ex1-2 defections. Playing Q to maintain cooperation and mutual 3s.
`#953` · game 172 · round 30 · agent A16 (opponent: script:TitForTat) · other · A16 ex36 with A01: they defect vs my Y, cooperate vs my W. Mutual W ex12-35 (24 straight). Playing W to maintain mutual 1s and avoid giving up 5.
`#954` · game 181 · round 4 · agent A10 (opponent: script:Grudger) · other · A10 ex10 with A12: mutual Q ex3-9 after their ex1-2 defections. Playing Q to maintain cooperation and mutual 3s.
`#955` · game 182 · round 1 · agent A18 (opponent: A15) · other · A18 ex7 with A15: they defected ex1-2, mutual Q ex3-6. Playing Q to maintain cooperation and mutual 3s.
`#956` · game 178 · round 16 · agent A02 (opponent: script:Grudger) · other · A02 ex22 with A12: they defected ex1-2, mutual Q ex3-16, I defected ex17, they've defected ex18-21 (4 straight). Playing X to stop giving them 5s.
`#957` · game 171 · round 29 · agent A00 (opponent: A06) · other · A00 ex35 with A06: mutual J ex15-34 (20 straight). Playing J to maintain mutual 3s.
`#958` · game 174 · round 16 · agent A10 (opponent: A05) · other · A10 ex22 with A05: mutual Q ex11-21 (11 straight). Playing Q to maintain cooperation and mutual 3s.
`#959` · game 174 · round 16 · agent A05 (opponent: A10) · other · A05 ex22 with A10: mutual Q ex11-21 (11 straight). Playing Q to maintain cooperation and mutual 3s.
`#960` · game 178 · round 17 · agent A02 (opponent: script:Grudger) · other · A02 ex23 with A12: they defected ex18-21 (4 straight), mutual X ex22. Continuing X to avoid giving 5s.
`#961` · game 179 · round 7 · agent A19 (opponent: A18) · other · A19 ex13 with A18: mutual Y ex3-12 (10 straight). Maintaining Y to sustain cooperation and mutual 3s.
`#962` · game 182 · round 3 · agent A18 (opponent: A15) · other · A18 ex9 with A15: they defected ex1-2, mutual Q ex3-8. Playing Q to maintain cooperation and mutual 3s.
`#963` · game 183 · round 5 · agent A00 (opponent: script:Random) · other · A00 ex11 with A13: they defected ex1,2,10 vs my Y, cooperated ex3-9. Playing W to punish last defection and avoid giving 5s.
`#964` · game 178 · round 20 · agent A02 (opponent: script:Grudger) · other · A02 ex26 with A12: they defected ex18-21 (4 straight), mutual X ex22-25. Continuing X to avoid giving 5s.
`#965` · game 183 · round 7 · agent A00 (opponent: script:Random) · other · A00 ex13 with A13: mutual Y ex12 after my W punish ex11. Playing Y to maintain cooperation and mutual 3s.
`#966` · game 186 · round 3 · agent A05 (opponent: script:Grudger) · other · A05 ex9 with A11: I T ex1-8, they N ex1-2 then T ex3-8 (6 mutual T straight). Playing T to maintain mutual 3s.
`#967` · game 181 · round 15 · agent A10 (opponent: script:Grudger) · other · A10 ex21 with A12: mutual Q ex3-20 (18 straight). Playing Q to maintain cooperation and mutual 3s.
`#968` · game 185 · round 8 · agent A09 (opponent: script:TitForTat) · other · A09 ex14 with A14: mutual Y ex3-13 (11 straight) after their W ex1-2. Maintaining Y to sustain cooperation and mutual 3s.
`#969` · game 181 · round 17 · agent A10 (opponent: script:Grudger) · other · A10 ex23 with A12: mutual Q ex3-22 (20 straight). Continuing Q to maintain cooperation and mutual 3s.
`#970` · game 188 · round 3 · agent A16 (opponent: script:TitForTat) · other · A16 ex9 with A21: they X ex1-2, mutual Q ex3-8. Playing Q to maintain cooperation and mutual 3s.
`#971` · game 181 · round 18 · agent A10 (opponent: script:Grudger) · other · A10 ex24 with A12: mutual Q ex3-23 (21 straight). Continuing Q to maintain cooperation and mutual 3s.
`#972` · game 182 · round 8 · agent A18 (opponent: A15) · other · A18 ex14 with A15: they defected ex1-2, mutual Q ex3-13 (11 straight). Playing Q to maintain cooperation and mutual 3s.
`#973` · game 178 · round 27 · agent A02 (opponent: script:Grudger) · other · A02 ex33 with A12: mutual X ex22-32 (11 straight) after their defections ex18-21. Continuing X to avoid giving 5s.
`#974` · game 178 · round 28 · agent A02 (opponent: script:Grudger) · other · A02 ex34 with A12: mutual X ex22-33 (12 straight) after their defections ex18-21. Continuing X to avoid giving 5s.
`#975` · game 190 · round 2 · agent A15 (opponent: A17) · other · A15 ex8 with A17: they defected ex1-2, mutual Y ex3-7. Playing Y to maintain cooperation and mutual 3s.
`#976` · game 174 · round 25 · agent A05 (opponent: A10) · other · A05 ex31 with A10: mutual Q ex11-30 (20 straight). Playing Q to maintain cooperation and mutual 3s.
`#977` · game 174 · round 26 · agent A10 (opponent: A05) · other · A10 ex32 with A05: mutual Q ex11-31 (21 straight). Playing Q to maintain cooperation and mutual 3s.
`#978` · game 182 · round 12 · agent A15 (opponent: A18) · other · A15 ex18 with A18: mutual Q ex3-17 (15 straight). Playing Q to maintain cooperation and mutual 3s.
`#979` · game 188 · round 11 · agent A16 (opponent: script:TitForTat) · other · A16 ex17 with A21: they X ex1-2, mutual Q ex3-16 (14 straight). Playing Q to maintain cooperation and mutual 3s.
`#980` · game 195 · round 2 · agent A04 (opponent: script:TitForTat) · other · A04 ex8 with A21: they defected ex1-2 (my Y), then mutual Y ex3-7. Playing Y to maintain cooperation and mutual 3s.
`#981` · game 196 · round 1 · agent A10 (opponent: script:AlwaysDefect) · other · A10 ex7 with A07: they N ex1-2, mutual T ex3-6. Playing T to maintain cooperation and mutual 3s.
`#982` · game 194 · round 3 · agent A06 (opponent: script:Random) · other · A06 ex9 with A08: I T ex1-2 (they N), mutual T ex3-8 (6 straight). Playing T to maintain mutual 3s.
`#983` · game 198 · round 1 · agent A19 (opponent: script:Random) · other · A19 ex7 with A08: they F ex1-2, mutual J ex3-6 (4 straight). Playing J to maintain cooperation and mutual 3s.
`#984` · game 196 · round 2 · agent A10 (opponent: script:AlwaysDefect) · other · A10 ex8 with A07: they defected ex1-2,7 (my T), mutual T ex3-6. Playing N to punish ex7 defection and avoid giving 5s.
`#985` · game 196 · round 3 · agent A10 (opponent: script:AlwaysDefect) · other · A10 ex9 with A07: they defected ex1-2,7. I punished ex8 with N. Now ex9 - need to decide whether to return to T or continue punishing. Given they defected at ex7 after mutual T ex3-6, I'll test with T to see if they return to cooperation.
`#986` · game 202 · round 1 · agent A02 (opponent: A05) · uncoded · A02 ex7 with A05: they defected ex1-2, mutual R ex3-6. Playing R to maintain cooperation and mutual 3s.
`#987` · game 196 · round 4 · agent A10 (opponent: script:AlwaysDefect) · other · A10 ex10 with A07: they defected ex1,2,7,9 (my T). Only mutual T ex3-6. They keep defecting after cooperation streaks. Playing N to punish and avoid giving 5s.
`#988` · game 200 · round 3 · agent A09 (opponent: script:AlwaysDefect) · other · A09 ex9 with A20: they defected ex1-2,7 (my J), mutual J ex3-6, mutual F ex8. Playing F to punish ex7 defection and avoid giving 5s.
`#989` · game 198 · round 6 · agent A19 (opponent: script:Random) · other · A19 ex12 with A08: pattern erratic - they F at ex1,2,8,10; J at 3-7,9,11. I F at 9,11. Playing F to avoid giving 5s given their recent defections.
`#990` · game 191 · round 6 · agent A15 (opponent: A05) · other · A15 ex12 with A05: mutual P ex3-11 (9 straight). Playing P to maintain cooperation and mutual 3s.
`#991` · game 199 · round 2 · agent A15 (opponent: A19) · other · A15 ex8 with A19: I T ex1-7, they N ex1-2 then T ex3-7 (5 mutual T straight). Playing T to maintain cooperation and mutual 3s.
`#992` · game 199 · round 2 · agent A19 (opponent: A15) · other · A19 ex8 with A15: they N ex1-2, mutual T ex3-7 (5 straight). Playing T to maintain cooperation and mutual 3s.
`#993` · game 201 · round 2 · agent A06 (opponent: A17) · other · A06 ex8 with A17: they W ex1-2, mutual Y ex3-8 (6 straight). Playing Y to maintain cooperation and mutual 3s.
`#994` · game 202 · round 2 · agent A05 (opponent: A02) · uncoded · A05 ex8 with A02: mutual R ex3-7 (5 straight) after their H ex1-2. Playing R to maintain cooperation and mutual 3s.
`#995` · game 200 · round 4 · agent A09 (opponent: script:AlwaysDefect) · other · A09 ex10 with A20: they defected ex1-2,7 (my J), mutual J ex3-6, mutual F ex8-9. Continuing F to punish and avoid giving 5s given their repeated defections.
`#996` · game 202 · round 3 · agent A02 (opponent: A05) · uncoded · A02 ex9 with A05: mutual R ex3-8 (6 straight). Playing R to maintain cooperation and mutual 3s.
`#997` · game 196 · round 7 · agent A10 (opponent: script:AlwaysDefect) · directive · A10 ex13 with A07: they defected ex1,2,7,9 (my T), mutual N ex8,10-12. They never cooperate with T. Playing N for mutual 1s to avoid giving 5s.
`#998` · game 196 · round 8 · agent A10 (opponent: script:AlwaysDefect) · directive · A10 ex14 with A07: they defected ex1,2,7,9 (my T), mutual N ex8,10-13. They never cooperate with T. Playing N for mutual 1s to avoid giving 5s.
`#999` · game 195 · round 24 · agent A04 (opponent: script:TitForTat) · other · A04 ex30 with A21: mutual Y ex10-29 (20 straight, and earlier ex3-9). They defected only ex1-2. Playing Y to maintain cooperation and mutual 3s.
`#1000` · game 196 · round 10 · agent A10 (opponent: script:AlwaysDefect) · other · A10 ex16 with A07: they defected ex1,2,7,9 (my T), mutual N ex8,10-15. They never reliably cooperate with T. Playing N for mutual 1s to avoid giving 5s.
`#1001` · game 200 · round 8 · agent A09 (opponent: script:AlwaysDefect) · other · A09 ex14 with A20: they defected ex1-2,7 (my J), mutual F ex8-13 (6 straight). Continuing F to avoid giving 5s; they never returned to J after defections.
`#1002` · game 199 · round 7 · agent A15 (opponent: A19) · other · A15 ex13 with A19: I T ex1-12, they N ex1-2 then T ex3-12 (10 mutual T straight). Playing T to maintain cooperation and mutual 3s.
`#1003` · game 202 · round 7 · agent A02 (opponent: A05) · uncoded · A02 ex13 with A05: mutual R ex3-12 (10 straight) after their H ex1-2. Playing R to maintain cooperation and mutual 3s.
`#1004` · game 196 · round 14 · agent A10 (opponent: script:AlwaysDefect) · directive · A10 ex20 with A07: they defected ex1,2,7,9 (my T), mutual N ex8,10-19. They never cooperate with T. Playing N for mutual 1s to avoid giving 5s.
`#1005` · game 200 · round 11 · agent A09 (opponent: script:AlwaysDefect) · other · A09 ex17 with A20: they defected ex1-2,7 (my J), mutual F ex8-16 (9 straight). Continuing F to avoid giving 5s; they never returned to J after defections.
`#1006` · game 198 · round 13 · agent A19 (opponent: script:Random) · other · A19 ex19 with A08: they F at 12,13,15,16,18; J at 14,17. Erratic. Playing F to avoid giving 5s.
`#1007` · game 201 · round 10 · agent A17 (opponent: A06) · other · A17 ex16 with A06: mutual Y ex3-15 (13 straight). Playing Y to maintain cooperation and mutual 3s.
`#1008` · game 196 · round 15 · agent A10 (opponent: script:AlwaysDefect) · directive · A10 ex21 with A07: they defected ex1,2,7,9 (my T), mutual N ex8,10-20. They never cooperate with T. Playing N for mutual 1s to avoid giving 5s.
`#1009` · game 202 · round 11 · agent A02 (opponent: A05) · uncoded · A02 ex17 with A05: mutual R ex3-16 (14 straight) after their H ex1-2. Playing R to maintain cooperation and mutual 3s.
`#1010` · game 202 · round 12 · agent A02 (opponent: A05) · uncoded · A02 ex18 with A05: mutual R ex3-17 (15 straight) after their H ex1-2. Playing R to maintain cooperation and mutual 3s.
`#1011` · game 202 · round 14 · agent A02 (opponent: A05) · uncoded · A02 ex20 with A05: mutual R ex3-19 (17 straight) after their H ex1-2. Playing R to maintain cooperation and mutual 3s.
`#1012` · game 202 · round 15 · agent A02 (opponent: A05) · uncoded · A02 ex21 with A05: mutual R ex3-20 (18 straight) after their H ex1-2. Playing R to maintain cooperation and mutual 3s.
`#1013` · game 204 · round 6 · agent A09 (opponent: script:Random) · other · A09 ex12 with A08: they J ex1-7 (I J), then F ex8,10,11, J ex9. Erratic. Playing F to avoid giving 5s.
`#1014` · game 204 · round 7 · agent A09 (opponent: script:Random) · other · A09 ex13 with A08: they J ex1-7 (I J), then F ex8,10,11, J ex9, F ex12. Erratic. Playing F to avoid giving 5s.
`#1015` · game 200 · round 22 · agent A09 (opponent: script:AlwaysDefect) · other · A09 ex28 with A20: they defected ex1-2,7 (my J), mutual F ex8-27 (20 straight). They never returned to J after defections. Continuing F to avoid giving 5s.
`#1016` · game 201 · round 19 · agent A17 (opponent: A06) · other · A17 ex25 with A06: mutual Y ex3-24 (22 straight). Playing Y to maintain cooperation and mutual 3s.
`#1017` · game 200 · round 24 · agent A09 (opponent: script:AlwaysDefect) · other · A09 ex30 with A20: they defected ex1-2,7 (my J), mutual F ex8-29 (22 straight). They never returned to J after defections. Continuing F to avoid giving 5s.
`#1018` · game 208 · round 2 · agent A16 (opponent: script:Random) · other · A16 ex8 with A08: they M ex1-2, then P ex3-7 (5 straight). Continuing P to maintain mutual 3s.
`#1019` · game 191 · round 20 · agent A15 (opponent: A05) · other · A15 ex26 with A05: mutual P ex18-25 (8 straight) after brief M/P at 16-17. Playing P to maintain cooperation and mutual 3s.
`#1020` · game 210 · round 1 · agent A02 (opponent: script:Random) · other · A02 ex7 with A08: they X ex1-2 (my Q), then Q ex3-6 (mutual). Continuing Q to maintain mutual 3s.
`#1021` · game 208 · round 3 · agent A16 (opponent: script:Random) · other · A16 ex9 with A08: they M ex1-2, P ex3-7, M ex8. Erratic/exploitative. I played M ex9 to retaliate after their ex8 defection.
`#1022` · game 199 · round 20 · agent A19 (opponent: A15) · other · A19 ex26 with A15: mutual T ex6-25 (20 straight). Continuing T to maintain cooperation and mutual 3s.
`#1023` · game 211 · round 1 · agent A17 (opponent: A18) · other · A17 ex7 with A18: I T ex1-6, they N ex1-2 then T ex3-6 (4 mutual T). Playing T to maintain cooperation and mutual 3s.
`#1024` · game 211 · round 1 · agent A18 (opponent: A17) · other · A18 ex7 with A17: I T ex1-6, they N ex1-2 then T ex3-6 (4 straight). Continuing T to maintain mutual 3s.
`#1025` · game 210 · round 3 · agent A02 (opponent: script:Random) · other · A02 ex9 with A08: they X ex1-2,7 (my Q), Q ex3-6,8 (I X ex8). Erratic. Playing Q to try restore mutual 3s.
`#1026` · game 211 · round 2 · agent A17 (opponent: A18) · other · A17 ex8 with A18: mutual T ex3-7 (5 straight). Playing T to maintain cooperation and mutual 3s.
`#1027` · game 208 · round 5 · agent A16 (opponent: script:Random) · other · A16 ex11 with A08: they M ex1-2, P ex3-7, M ex8, M ex9-10. Erratic/exploitative. I played M ex9-10 to retaliate. Playing M ex11 defensively.
`#1028` · game 210 · round 4 · agent A02 (opponent: script:Random) · other · A02 ex10 with A08: they X ex1,2,7 (my Q), Q ex3-6,9 (I X ex8). Erratic. Playing Q to try restore/maintain mutual 3s.
`#1029` · game 208 · round 6 · agent A16 (opponent: script:Random) · other · A16 ex12 with A08: they M ex1-2, P ex3-7, M ex8, M ex9-10, P ex11. Erratic/exploitative. I played M ex9-10 to retaliate, M ex11 defensively. Playing M ex12 defensively.
`#1030` · game 201 · round 27 · agent A17 (opponent: A06) · other · A17 ex33 with A06: mutual Y ex3-32 (30 straight). Playing Y to maintain cooperation and mutual 3s.
`#1031` · game 210 · round 6 · agent A02 (opponent: script:Random) · other · A02 ex12 with A08: they X ex1,2,7,10 (my Q), Q ex3-6,8,9,11. Erratic/exploitative. Playing X defensively ex12.
`#1032` · game 208 · round 7 · agent A16 (opponent: script:Random) · other · A16 ex13 with A08: they M ex1-2,8-10; P ex3-7,11-12. Erratic/exploitative. Playing M defensively to avoid giving 5s.
`#1033` · game 213 · round 2 · agent A05 (opponent: script:TitForTat) · other · A05 ex8 with A23: I defected M ex7 (they P). Playing M ex8 defensively after my own defection to avoid giving 5s.
`#1034` · game 201 · round 29 · agent A17 (opponent: A06) · other · A17 ex35 with A06: mutual Y ex3-34 (32 straight). Playing Y to maintain cooperation and mutual 3s.
`#1035` · game 210 · round 8 · agent A02 (opponent: script:Random) · other · A02 ex14 with A08: they X ex1,2,7,10 (my Q), Q ex3-6,8,9,11, X ex12-13 (mutual). Erratic/exploitative. Playing X defensively to avoid giving 5s.
`#1036` · game 213 · round 4 · agent A05 (opponent: script:TitForTat) · other · A05 ex10 with A23: they defected ex1,2,9 (my P). Mutual P ex3-6, I M ex7, mutual M ex8. Playing M defensively after their ex9 defection.
`#1037` · game 208 · round 9 · agent A16 (opponent: script:Random) · other · A16 ex15 with A08: they M ex1-2,8-10,13-14; P ex3-7,11-12. Erratic. Playing M defensively to avoid giving 5s.
`#1038` · game 215 · round 1 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex7 with A07: they F ex1-2, J ex3-6. Playing J to maintain mutual cooperation and 3s.
`#1039` · game 214 · round 3 · agent A15 (opponent: script:TitForTat) · other · A15 ex9 with A01: mutual R ex3-8 (6 straight). Playing R to maintain cooperation and mutual 3s.
`#1040` · game 210 · round 10 · agent A02 (opponent: script:Random) · other · A02 ex16 with A08: they X ex1,2,7,10 (my Q), Q ex3-6,8,9,11,15 (I X ex8,11,15), X ex12-14 (mutual). Erratic/exploitative. Playing X defensively to avoid giving 5s.
`#1041` · game 215 · round 2 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex8 with A07: they F ex1-2, J ex3-6, F ex7. Erratic/exploitative. Playing F ex8 to retaliate/defend after their ex7 defection.
`#1042` · game 213 · round 6 · agent A05 (opponent: script:TitForTat) · other · A05 ex12 with A23: erratic/exploitative partner. They defected ex1,2,9 (my P). Mutual P ex3-6, I M ex7, mutual M ex8, I M ex10, mutual M ex11. Playing M defensively to avoid giving 5s.
`#1043` · game 208 · round 13 · agent A16 (opponent: script:Random) · other · A16 ex19 with A08: they M ex1-2,8-10,13-14,18; P ex3-7,11-12,15-17. Erratic blocks. Last was M after two P's; guessing P next, playing M to take 5.
`#1044` · game 215 · round 3 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex9 with A07: they F ex1-2, J ex3-6, F ex7, mutual F ex8. Erratic/exploitative. Playing F defensively to avoid giving 5s.
`#1045` · game 217 · round 1 · agent A18 (opponent: script:Grudger) · other · A18 ex7 with A11: they N ex1-2, T ex3-6 (4 straight mutual T). Playing T to maintain cooperation and mutual 3s.
`#1046` · game 215 · round 5 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex11 with A07: they F ex1-2, J ex3-6, F ex7, mutual F ex8-10. Erratic/exploitative. Trying J ex11 to restore mutual 3s after mutual F streak.
`#1047` · game 210 · round 15 · agent A02 (opponent: script:Random) · other · A02 ex21 with A08: they've played Q in 5 of last 6 (ex15,16,17,19,20). Playing X to take 5 if they Q again.
`#1048` · game 208 · round 16 · agent A16 (opponent: script:Random) · other · A16 ex22 with A08: they M ex18-21 (mutual). Erratic blocks. Playing M defensively to avoid giving 5s.
`#1049` · game 211 · round 12 · agent A17 (opponent: A18) · other · A17 ex18 with A18: mutual T ex3-15, I N ex16 (took 5), mutual N ex17. Playing T ex18 to try restore cooperation/mutual 3s.
`#1050` · game 215 · round 6 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex12 with A07: they F ex1-2, J ex3-6, F ex7, mutual F ex8-10, F ex11 (my J). Erratic/exploitative - keeps defecting when I try to cooperate. Playing F defensively to avoid giving 5s.
`#1051` · game 208 · round 17 · agent A16 (opponent: script:Random) · other · A16 ex23 with A08: they've been erratic. Mutual M ex18-21 (4 straight). Playing M defensively to avoid giving 5s.
`#1052` · game 219 · round 2 · agent A00 (opponent: script:TitForTat) · other · A00 ex8 with A21: they F ex1-2, J ex3-7. Playing J to maintain mutual cooperation and 3s.
`#1053` · game 210 · round 16 · agent A02 (opponent: script:Random) · other · A02 ex22 with A08: they've been erratic; last three X,Q,X. Guessing Q next, playing X to take 5.
`#1054` · game 215 · round 8 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex14 with A07: they F ex1-2,7,11,13 (my J); mutual F ex8-10,12-13. Erratic/exploitative - keeps defecting when I cooperate. Playing F defensively to avoid giving 5s.
`#1055` · game 211 · round 13 · agent A18 (opponent: A17) · other · A18 ex19 with A17: mutual T ex3-15, I N ex16 (took 5), mutual N ex17, mutual T ex18. Playing T to maintain cooperation/mutual 3s.
`#1056` · game 219 · round 3 · agent A00 (opponent: script:TitForTat) · other · A00 ex9 with A21: they F ex1-2, J ex3-8 (6 straight). Playing J to maintain mutual cooperation and 3s.
`#1057` · game 219 · round 4 · agent A00 (opponent: script:TitForTat) · other · A00 ex10 with A21: they F ex1-2, J ex3-8 (6 straight). Playing J to maintain mutual cooperation and 3s.
`#1058` · game 210 · round 18 · agent A02 (opponent: script:Random) · other · A02 ex24 with A08: they've played Q in 6 of last 8 (ex15,16,17,19,22,23), often against my X. Playing X to take 5 if they Q again.
`#1059` · game 215 · round 10 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex16 with A07: they've defected whenever I cooperated (ex1,2,7,11). Long mutual F streak ex8-15. Playing F defensively to avoid giving 5s.
`#1060` · game 210 · round 19 · agent A02 (opponent: script:Random) · other · A02 ex25 with A08: they've played Q 6 of last 8 (ex15,16,17,19,22,23). Playing X to take 5 when they Q.
`#1061` · game 214 · round 21 · agent A15 (opponent: script:TitForTat) · other · A15 ex27 with A01: long mutual R streak (ex7-26 all mutual R). Playing R to maintain cooperation/mutual 3s.
`#1062` · game 204 · round 26 · agent A09 (opponent: script:Random) · other · A09 ex32 with A08: they've been defecting heavily (J at 16,17,19,20,22,26,27,28,29). Playing J to defend and seek mutual 3s.
`#1063` · game 215 · round 15 · agent A06 (opponent: script:AlwaysDefect) · other · A06 ex21 with A07: long mutual F streak ex8-20 (they defected ex1,2,7,11 against my J). Playing F defensively to avoid giving 5s.
`#1064` · game 214 · round 23 · agent A15 (opponent: script:TitForTat) · other · A15 ex29 with A01: long mutual R streak (ex7-28 all mutual R). Playing R to maintain cooperation/mutual 3s.
`#1065` · game 210 · round 22 · agent A02 (opponent: script:Random) · other · A02 ex28 with A08: they've played X ex25-27 (3 straight mutual X). Playing X defensively to avoid giving 5s.
`#1066` · game 219 · round 14 · agent A00 (opponent: script:TitForTat) · other · A00 ex20 with A21: they F ex1-2, J ex3-19 (17 straight). Playing J to maintain mutual cooperation and 3s.
`#1067` · game 204 · round 28 · agent A09 (opponent: script:Random) · other · A09 ex34 with A08: mutual J ex30,32,33 (3 of last 4). Playing J to maintain mutual 3s.
`#1068` · game 220 · round 3 · agent A16 (opponent: script:Pavlov) · other · A16 ex9 with A22: they M ex1,2,8 (my P) and P ex3-7. Erratic/exploitative. Playing M defensively to avoid giving 5s.
`#1069` · game 217 · round 20 · agent A18 (opponent: script:Grudger) · other · A18 ex26 with A11: mutual T ex6-25 (20 straight). Playing T to maintain cooperation/mutual 3s.
`#1070` · game 210 · round 23 · agent A02 (opponent: script:Random) · other · A02 ex29 with A08: they played Q ex28 after 3 mutual X. History erratic; after a Q they often follow with X. Playing X to take 5 if they Q again.
`#1071` · game 214 · round 30 · agent A15 (opponent: script:TitForTat) · other · A15 ex36 with A01: long mutual R streak (ex7-35 all mutual R). Playing R to maintain cooperation/mutual 3s.
`#1072` · game 210 · round 24 · agent A02 (opponent: script:Random) · other · A02 ex30 with A08: they played Q ex28-29 against my X (I got 5 each). Continuing X to keep taking 5s.
`#1073` · game 224 · round 1 · agent A02 (opponent: A19) · other · A02 ex7 with A19: they F ex1-2, J ex3-6 (4 straight mutual J). Playing J to maintain cooperation/mutual 3s.
`#1074` · game 210 · round 25 · agent A02 (opponent: script:Random) · other · A02 ex31 with A08: they played Q ex28-30 (3 straight) against my X. Continuing X to keep taking 5s.
`#1075` · game 222 · round 2 · agent A04 (opponent: script:AlwaysDefect) · other · A04 ex8 with A07: they defected ex1,2,7 (my Y), cooperated ex3-6. Erratic/exploitative. Playing W defensively to avoid giving 5s.
`#1076` · game 208 · round 29 · agent A16 (opponent: script:Random) · other · A16 ex35 with A08: they've been M ex32-34 (3 straight mutual M). Playing M to maintain mutual 3s.
`#1077` · game 225 · round 1 · agent A19 (opponent: A00) · other · A19 ex7 with A00: they N ex1-2, T ex3-6 (4 straight mutual T). Playing T to maintain mutual cooperation and 3s.
`#1078` · game 222 · round 4 · agent A04 (opponent: script:AlwaysDefect) · other · A04 ex10 with A07: they defected ex1,2,7 (my Y), cooperated ex3-6. Mutual W ex8-9. Playing W defensively to avoid giving 5s.
`#1079` · game 208 · round 30 · agent A16 (opponent: script:Random) · other · A16 ex36 with A08: mutual M ex30,32-35. Playing M to maintain mutual 3s.
`#1080` · game 224 · round 4 · agent A02 (opponent: A19) · other · A02 ex10 with A19: mutual J ex3-9 (7 straight). Playing J to maintain mutual 3s.
`#1081` · game 222 · round 5 · agent A04 (opponent: script:AlwaysDefect) · other · A04 ex11 with A07: they defected ex1,2,7 (my Y), cooperated ex3-6. Mutual W ex8-10. Playing W defensively to avoid giving 5s.
`#1082` · game 225 · round 2 · agent A00 (opponent: A19) · other · A00 ex8 with A19: mutual T ex3-7 (5 straight). Playing T to maintain mutual cooperation and 3s.
`#1083` · game 226 · round 1 · agent A06 (opponent: A05) · other · A06 ex7 with A05: they defected ex1-2 (my Y), then cooperated ex3-6 (4 straight mutual Y). Playing Y to maintain mutual cooperation/3s.
`#1084` · game 226 · round 1 · agent A05 (opponent: A06) · other · A05 ex7 with A06: they W ex1-2, Y ex3-6 (4 straight mutual Y). Playing Y to maintain cooperation/mutual 3s.
`#1085` · game 222 · round 6 · agent A04 (opponent: script:AlwaysDefect) · other · A04 ex12 with A07: they defected ex1,2,7 (my Y), cooperated ex3-6. Mutual W ex8-11. Playing W defensively to avoid giving 5s.
`#1086` · game 227 · round 1 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex7 with A07: they H ex1-2, R ex3-6 (4 straight mutual R). Playing R to maintain cooperation/mutual 3s.
`#1087` · game 219 · round 29 · agent A00 (opponent: script:TitForTat) · other · A00 ex35 with A21: we've had mutual J ex15-34 (20 straight). Playing J to maintain mutual cooperation and 3s.
`#1088` · game 210 · round 30 · agent A02 (opponent: script:Random) · other · A02 ex36 with A08: they've played Q ex28-35 (8 straight) against my X. Continuing X to keep taking 5s.
`#1089` · game 229 · round 1 · agent A17 (opponent: script:Pavlov) · other · A17 ex7 with A03: they defected ex1-2 (my Q), then cooperated ex3-6 (4 straight mutual Q). Playing X to take 5 if they continue Q, given they've been cooperative recently.
`#1090` · game 230 · round 1 · agent A18 (opponent: A16) · other · A18 ex7 with A16: they H ex1-2, R ex3-6 (4 straight mutual R). Playing R to maintain cooperation/mutual 3s.
`#1091` · game 222 · round 9 · agent A04 (opponent: script:AlwaysDefect) · other · A04 ex15 with A07: they defected ex1,2,7 (my Y), cooperated ex3-6. Mutual W ex8-14 (7 straight). Playing W to maintain mutual 1s and avoid giving 5s.
`#1092` · game 220 · round 11 · agent A16 (opponent: script:Pavlov) · other · A16 ex17 with A22: they've alternated P/M on odd/even exchanges recently (P on odd 11,13,15; M on even 12,14,16). Playing P to get mutual 3 if they play P on this odd exchange.
`#1093` · game 230 · round 2 · agent A18 (opponent: A16) · other · A18 ex8 with A16: mutual R ex3-7 (5 straight). Playing R to maintain cooperation/mutual 3s.
`#1094` · game 229 · round 3 · agent A17 (opponent: script:Pavlov) · other · A17 ex9 with A03: they defected ex1-2 (my Q), cooperated ex3-6, I defected ex7, mutual X ex8. Playing Q to try restoring mutual cooperation.
`#1095` · game 227 · round 4 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex10 with A07: they H ex1-2,7 (my R, got 5s), R ex3-6 (mutual R), mutual H ex8-9. Playing H defensively to avoid giving 5s to their exploitative pattern.
`#1096` · game 230 · round 3 · agent A18 (opponent: A16) · other · A18 ex9 with A16: mutual R ex3-8 (6 straight). Playing R to maintain cooperation/mutual 3s.
`#1097` · game 220 · round 13 · agent A16 (opponent: script:Pavlov) · other · A16 ex19 with A22: they've been playing P frequently recently (P ex15,17,18). Playing M to capitalize on likely P.
`#1098` · game 222 · round 14 · agent A04 (opponent: script:AlwaysDefect) · other · A04 ex20 with A07: mutual W ex8-19 (12 straight). Continuing W to maintain stable mutual 1s.
`#1099` · game 230 · round 4 · agent A18 (opponent: A16) · other · A18 ex10 with A16: mutual R ex3-9 (7 straight). Playing R to maintain mutual cooperation/3s.
`#1100` · game 229 · round 6 · agent A17 (opponent: script:Pavlov) · other · A17 ex12 with A03: they defected ex1-2 (my Q), then cooperated ex3-6, I defected ex7, mutual X ex8, mutual Q ex9-11. Playing Q to maintain mutual cooperation/3s.
`#1101` · game 227 · round 6 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex12 with A07: they H ex1,2,7 (my R, got 5s), R ex3-6 (mutual R), mutual H ex8-11. Playing H defensively to avoid giving 5s to their exploitative pattern.
`#1102` · game 224 · round 10 · agent A02 (opponent: A19) · other · A02 ex16 with A19: mutual J ex3-15 (13 straight). Playing J to maintain mutual 3s.
`#1103` · game 229 · round 7 · agent A17 (opponent: script:Pavlov) · other · A17 ex13 with A03: mutual Q ex9-12 after earlier defections. Playing Q to maintain mutual cooperation/3s.
`#1104` · game 232 · round 3 · agent A18 (opponent: script:Random) · other · A18 ex9 with A13: they H ex1-2,8 (my R), R ex3-7. Playing H defensively after their ex8 defection to avoid giving more 5s.
`#1105` · game 220 · round 16 · agent A16 (opponent: script:Pavlov) · other · A16 ex22 with A22: recent pattern broken (they played M ex19,21 on odd). Playing M defensively to avoid giving 5s.
`#1106` · game 232 · round 4 · agent A18 (opponent: script:Random) · other · A18 ex10 with A13: they H ex1-2,8 (my R), R ex3-7, mutual H ex9. Playing H defensively to avoid giving 5s to their periodic defections.
`#1107` · game 220 · round 17 · agent A16 (opponent: script:Pavlov) · other · A16 ex23 with A22: they've played M on odd exchanges 19,21 and P on even 18,20,22. Playing M to capitalize on likely P or get mutual 1.
`#1108` · game 233 · round 1 · agent A04 (opponent: A15) · other · A04 ex7 with A15: they defected ex1-2 (my P, got 5s), then cooperated ex3-6 (mutual P). Playing P to maintain mutual cooperation/3s.
`#1109` · game 230 · round 7 · agent A18 (opponent: A16) · other · A18 ex13 with A16: mutual R ex3-12 (10 straight). Playing R to maintain mutual cooperation/3s.
`#1110` · game 226 · round 12 · agent A05 (opponent: A06) · other · A05 ex18 with A06: they defected ex1-2 (my Y), then cooperated ex3-17 (15 straight mutual Y). Playing Y to maintain mutual cooperation/3s.
`#1111` · game 230 · round 8 · agent A18 (opponent: A16) · other · A18 ex14 with A16: mutual R ex3-13 (11 straight). Playing R to maintain mutual cooperation/3s.
`#1112` · game 220 · round 21 · agent A16 (opponent: script:Pavlov) · other · A16 ex27 with A22: they've played M on odd exchanges 19,21,23,25. Playing M defensively for mutual 1 or 5 if they play P.
`#1113` · game 232 · round 7 · agent A18 (opponent: script:Random) · other · A18 ex13 with A13: they H ex1-2,8,11 (my R, got 5s), R ex3-7,10, mutual H ex9,12. Playing H defensively to avoid giving 5s to their frequent defections.
`#1114` · game 234 · round 1 · agent A00 (opponent: script:Random) · other · A00 ex7 with A08: they F ex1-2 (my J, got 5s), then J ex3-6 (mutual J). Playing J to maintain mutual cooperation/3s.
`#1115` · game 220 · round 23 · agent A16 (opponent: script:Pavlov) · other · A16 ex29 with A22: they've played M on odd exchanges 19,21,23,25,27 and P on even. Ex29 is odd, expecting M. Playing P to capitalize for 5.
`#1116` · game 234 · round 2 · agent A00 (opponent: script:Random) · other · A00 ex8 with A08: they F ex1-2 (my J, got 5s), then J ex3-7 (mutual J). Playing J to maintain mutual cooperation/3s.
`#1117` · game 226 · round 14 · agent A05 (opponent: A06) · other · A05 ex20 with A06: mutual Y ex3-19 (17 straight). Playing Y to maintain mutual cooperation/3s.
`#1118` · game 230 · round 10 · agent A18 (opponent: A16) · other · A18 ex16 with A16: mutual R ex3-15 (13 straight). Playing R to maintain mutual cooperation/3s.
`#1119` · game 222 · round 27 · agent A04 (opponent: script:AlwaysDefect) · other · A04 ex33 with A07: mutual W ex8-32 (25 straight). Continuing W to maintain stable mutual 1s.
`#1120` · game 235 · round 1 · agent A18 (opponent: script:TitForTat) · other · A18 ex7 with A14: they F ex1-2 (my J, got 5s), then J ex3-6 (mutual J). Playing J to maintain mutual cooperation/3s.
`#1121` · game 220 · round 25 · agent A16 (opponent: script:Pavlov) · other · A16 ex31 with A22: they've played M on odd exchanges consistently. Playing M for mutual 1.
`#1122` · game 233 · round 5 · agent A15 (opponent: A04) · other · A15 ex11 with A04: mutual P ex3-10 (8 straight after their early defections). Playing P to maintain mutual cooperation/3s.
`#1123` · game 222 · round 29 · agent A04 (opponent: script:AlwaysDefect) · other · A04 ex35 with A07: mutual W ex8-34 (27 straight). Trying Y to catch up from behind (39 vs 54).
`#1124` · game 232 · round 10 · agent A18 (opponent: script:Random) · other · A18 ex16 with A13: they H ex1-2,8,11 (my R), R ex3-7,10,14-15, mutual H ex9,12-13. Playing H defensively to avoid giving 5s to their frequent defections.
`#1125` · game 220 · round 27 · agent A16 (opponent: script:Pavlov) · other · A16 ex33 with A22: they've been playing M frequently recently (29M,31P,32M). Playing M defensively to get mutual 1 or avoid giving 5s.
`#1126` · game 234 · round 6 · agent A00 (opponent: script:Random) · other · A00 ex12 with A08: they F ex1-2,8,10 and J ex3-7,9,11 (alternating lately). Playing F defensively to avoid giving 5s.
`#1127` · game 238 · round 1 · agent A18 (opponent: A09) · other · A18 ex7 with A09: they M ex1-2 (my P), P ex3-6. Playing P to maintain mutual cooperation/3s after their recent cooperation.
`#1128` · game 234 · round 8 · agent A00 (opponent: script:Random) · other · A00 ex14 with A08: they F ex1-2,8,10,12-13 and J ex3-7,9,11 (recently defecting). Playing F defensively.
`#1129` · game 238 · round 2 · agent A18 (opponent: A09) · other · A18 ex8 with A09: they M ex1-2 (my P), P ex3-7. Playing P to maintain mutual cooperation/3s.
`#1130` · game 232 · round 13 · agent A18 (opponent: script:Random) · other · A18 ex19 with A13: they H ex1-2,8,11,16,18, R ex3-7,10,14-15,17, mutual H ex9,12-13. Playing H defensively to avoid giving 5s to their frequent defections.
`#1131` · game 234 · round 9 · agent A00 (opponent: script:Random) · other · A00 ex15 with A08: they F ex1-2,8,10,12-14 and J ex3-7,9,11 (heavy defection lately). Playing F defensively.
`#1132` · game 239 · round 2 · agent A05 (opponent: A09) · uncoded · A05 ex8 with A09: they R ex1-2 (my R, got 5s), then R ex3-7 (mutual R). Playing R to maintain mutual cooperation/3s.
`#1133` · game 232 · round 14 · agent A18 (opponent: script:Random) · other · A18 ex20 with A13: they H ex1-2,8,11,16,18, R ex3-7,10,14-15,17, mutual H ex9,12-13,19. Playing H defensively.
`#1134` · game 235 · round 10 · agent A18 (opponent: script:TitForTat) · other · A18 ex16 with A14: they F ex1-2 (my J, got 5s), then J ex3-15 (13 straight mutual J). Playing J to maintain mutual cooperation/3s.
`#1135` · game 240 · round 2 · agent A06 (opponent: script:Grudger) · other · A06 ex8 with A12: they H ex1-2 (my R, got 5s), then R ex3-7 (mutual R). Playing R to maintain mutual cooperation/3s.
`#1136` · game 238 · round 3 · agent A18 (opponent: A09) · other · A18 ex9 with A09: they M ex1-2 (my P), P ex3-8. Playing P to maintain mutual cooperation/3s.
`#1137` · game 234 · round 11 · agent A00 (opponent: script:Random) · other · A00 ex17 with A08: they F ex8,10,11,13,15,16 (heavy defection). Playing F defensively to avoid giving 5s.
`#1138` · game 232 · round 15 · agent A18 (opponent: script:Random) · other · A18 ex21 with A13: they H ex1-2,8,11,16,18,20, R ex3-7,10,14-15,17, mutual H ex9,12-13,19. Playing H defensively to avoid giving 5s to their frequent defections.
`#1139` · game 240 · round 3 · agent A06 (opponent: script:Grudger) · other · A06 ex9 with A12: mutual R ex3-8 (6 straight). Playing R to maintain mutual cooperation/3s.
`#1140` · game 242 · round 2 · agent A10 (opponent: A02) · other · A10 ex8 with A02: they H ex1-2 (my R, got 5s), then R ex3-7 (mutual R). Playing R to maintain mutual cooperation/3s.
`#1141` · game 240 · round 5 · agent A06 (opponent: script:Grudger) · other · A06 ex11 with A12: mutual R ex3-10 (8 straight). Playing R to maintain mutual cooperation/3s.
`#1142` · game 243 · round 3 · agent A16 (opponent: script:AlwaysDefect) · other · A16 ex9 with A20: they W ex1,2,7 (my Y), Y ex3-6, W ex8 (mutual W). Playing W defensively to avoid giving 5s to their frequent defections.
`#1143` · game 242 · round 3 · agent A10 (opponent: A02) · other · A10 ex9 with A02: they H ex1-2 (my R, got 5s), then R ex3-8 (mutual R). I'm behind 18-28, trying H to catch up this final exchange.
`#1144` · game 238 · round 5 · agent A18 (opponent: A09) · other · A18 ex11 with A09: they M ex1-2,9-10 (my P), P ex3-8. Recent defections, playing M defensively.
`#1145` · game 238 · round 5 · agent A09 (opponent: A18) · other · A09 ex11 with A18: mutual P ex3-8, my M ex9 (got 5), mutual M ex10. Playing P to maintain mutual cooperation/3s.
`#1146` · game 243 · round 4 · agent A16 (opponent: script:AlwaysDefect) · other · A16 ex10 with A20: they W ex1,2,7 (my Y), Y ex3-6, W ex8-9 (mutual W). Playing W defensively to avoid giving 5s to their frequent defections.
`#1147` · game 233 · round 11 · agent A04 (opponent: A15) · other · A04 ex17 with A15: they defected M at ex14 and ex16 (after mutual P ex3-13). Playing M defensively to avoid giving 5s.
`#1148` · game 233 · round 11 · agent A15 (opponent: A04) · other · A15 ex17 with A04: tried M ex14,16 (they played P, I got 0), M ex15 mutual. Returning to P for mutual 3s.
`#1149` · game 242 · round 4 · agent A10 (opponent: A02) · other · A10 ex10 with A02: they H ex1-2, R ex3-8, R ex9 (I played H). Final exchange, playing H to grab 5.
`#1150` · game 243 · round 5 · agent A16 (opponent: script:AlwaysDefect) · other · A16 ex11 with A20: they W ex1,2,7 (my Y), Y ex3-6, W ex8-10 (mutual W). Playing W defensively to avoid giving 5s to their frequent defections.
`#1151` · game 235 · round 22 · agent A18 (opponent: script:TitForTat) · other · A18 ex28 with A14: mutual J ex3-27 (25 straight). Continuing J to maintain mutual cooperation/3s.
`#1152` · game 245 · round 1 · agent A18 (opponent: script:Pavlov) · other · A18 ex7 with A03: they F ex1-2 (my J), then J ex3-6 (4 straight mutual J). Playing J to maintain mutual cooperation/3s.
`#1153` · game 233 · round 12 · agent A04 (opponent: A15) · other · A04 ex18 with A15: they defected M ex14,16, mutual M ex15, my M ex17 (they P). Playing M defensively to avoid giving 5s given their frequent defections and my deficit.
`#1154` · game 243 · round 7 · agent A16 (opponent: script:AlwaysDefect) · other · A16 ex13 with A20: they W ex1,2,7,11,12 (my Y), Y ex3-6, W ex8-10 (mutual W). Playing W defensively to avoid giving 5s.
`#1155` · game 233 · round 13 · agent A04 (opponent: A15) · other · A04 ex19 with A15: We've had mutual P for ex3-13, then A15 defected M ex14,16, mutual M ex15, my M ex17 (they P), mutual M ex18. I'm behind 40-55. They've been unpredictable. Given my deficit, I'm considering M this exchange to try to gain ground.
`#1156` · game 233 · round 13 · agent A04 (opponent: A15) · other · A04 ex19 pick: M
`#1157` · game 243 · round 9 · agent A16 (opponent: script:AlwaysDefect) · other · A16 ex15 with A20: they W ex1,2,7,11,12 (my Y), Y ex3-6, W ex8-14 (mutual W). Playing W defensively to avoid giving 5s.
`#1158` · game 238 · round 8 · agent A18 (opponent: A09) · other · A18 ex14 with A09: they M ex1,2,9,10,12,13, P ex3-8,11. I'm behind 25-40, final exchange, playing M defensively.
`#1159` · game 242 · round 7 · agent A10 (opponent: A02) · other · A10 ex13 with A02: they H ex1-2, R ex3-8, R ex9 (I H), H ex10-12 (mutual H). They've switched to H, playing H defensively to avoid giving 5s.
`#1160` · game 245 · round 6 · agent A18 (opponent: script:Pavlov) · other · A18 ex12 with A03: I defected ex10, mutual F ex11. Behind 27-32, playing F defensively this exchange.
`#1161` · game 244 · round 11 · agent A02 (opponent: script:Grudger) · opponent_info · A02 ex17 with A11: mutual M ex16 after my M ex15. Playing P to restore mutual cooperation/3s, given tit-for-tat pattern.
`#1162` · game 247 · round 3 · agent A19 (opponent: script:Grudger) · other · A19 ex9 with A11: they X ex1,2,8 (my Q), Q ex3-7 (mutual Q). Behind 17-27. Playing X defensively to avoid giving 5s.
`#1163` · game 238 · round 9 · agent A18 (opponent: A09) · other · A18 ex15 with A09: they M ex1,2,9,10,12,13,14, P ex3-8,11. I'm behind 26-41, playing M defensively against their frequent defections.
`#1164` · game 238 · round 9 · agent A09 (opponent: A18) · other · A09 ex15 with A18: they M ex1,2,11,13,14, P ex3-8,12. Recent defections, I'm behind 31-36. Playing M defensively to avoid giving 5s.
`#1165` · game 243 · round 13 · agent A16 (opponent: script:AlwaysDefect) · other · A16 ex19 with A20: they W ex1,2,7,11,12 (my Y), Y ex3-6, W ex8-18 (mutual W). Behind 22-42. They keep defecting to W. Playing W defensively to avoid giving 5s.
`#1166` · game 249 · round 2 · agent A04 (opponent: A06) · other · A04 ex8 with A06: they defected M ex1-2 (my P), then mutual P ex3-6, mutual M ex7. I'm behind 13-23. Playing M defensively to avoid giving 5s given their early defections and my deficit.
`#1167` · game 243 · round 14 · agent A16 (opponent: script:AlwaysDefect) · other · A16 ex20 final with A20: they W ex1,2,7,11,12,18 (my Y), Y ex3-6, W ex8-19 (mutual W). They consistently defect to W. Playing W final to avoid giving 5s.
`#1168` · game 249 · round 3 · agent A04 (opponent: A06) · other · A04 ex9 with A06: they defected M ex1-2 (my P), mutual P ex3-6, mutual M ex7-8. Behind 14-24. Playing M defensively to avoid giving 5s.
`#1169` · game 249 · round 3 · agent A06 (opponent: A04) · other · A06 ex9 with A04: they've signaled M defensively. I'm behind 14-24. Matching M for mutual 1 to avoid giving them 5.
`#1170` · game 233 · round 15 · agent A15 (opponent: A04) · other · A15 ex21 with A04: they've been defecting frequently (M ex17,19). Playing M defensively to avoid giving 5s.
`#1171` · game 242 · round 9 · agent A10 (opponent: A02) · other · A10 ex15 with A02: they H ex1-2, R ex3-8, R ex9 (I H), H ex10-14 (mutual H). Behind 28-33. Playing H defensively to avoid giving 5s.
`#1172` · game 242 · round 9 · agent A02 (opponent: A10) · other · A02 ex15 with A10: they H ex1,2,9 (my R), mutual R ex3-8, mutual H ex10-14. Behind 23-38. Playing H defensively to avoid giving 5s.
`#1173` · game 247 · round 5 · agent A19 (opponent: script:Grudger) · other · 
`#1174` · game 238 · round 10 · agent A18 (opponent: A09) · other · A18 ex16 with A09: they M ex1,2,9,10,12,13,14,15, P ex3-8,11. I'm behind 27-42, playing M defensively against their frequent defections.
`#1175` · game 238 · round 10 · agent A09 (opponent: A18) · other · A09 ex16 with A18: they M ex1,2,11,13,14,15, P ex3-8,12. Behind 32-37. Playing M defensively to avoid giving 5s given their recent M streak.
`#1176` · game 245 · round 9 · agent A18 (opponent: script:Pavlov) · other · A18 ex15 with A03: after my defections ex10-14, they've alternated J/F. Playing F defensively to avoid giving 5s.
`#1177` · game 247 · round 7 · agent A19 (opponent: script:Grudger) · other · A19 ex13 with A11: they X ex1,2,8 (my Q), Q ex3-7 (mutual Q), X ex9-12 (mutual X). Behind 21-31. Playing X defensively to avoid giving 5s.
`#1178` · game 244 · round 15 · agent A02 (opponent: script:Grudger) · other · A02 ex21 with A11: mutual M ex16,18-20, my M ex15, their M ex17. Settled into mutual M. Playing M defensively to avoid giving 5s.
`#1179` · game 243 · round 19 · agent A16 (opponent: script:AlwaysDefect) · other · A16 ex25 with A20: they W ex1,2,7,11,12,18 (my Y), Y ex3-6, W ex8-24 (mutual W). Behind 28-48. They consistently defect to W. Playing W to avoid giving 5s.
`#1180` · game 238 · round 11 · agent A18 (opponent: A09) · other · A18 ex17 with A09: they M ex1,2,9,10,12,13,14,15,16, P ex3-8,11. Behind 28-43, playing M defensively against their frequent defections.
`#1181` · game 242 · round 10 · agent A02 (opponent: A10) · other · A02 ex16 with A10: they've been H ex10-15 (mutual H), ahead 39-24. Matching H defensively to get 1 rather than give 5.
`#1182` · game 233 · round 16 · agent A04 (opponent: A15) · other · A04 ex22 with A15: behind 47-57, they've signaled M defensively. Playing M to avoid giving 5s.
`#1183` · game 233 · round 16 · agent A15 (opponent: A04) · other · A15 ex22 with A04: I'm behind 47-57, they've been playing M defensively. Matching M to secure mutual 1 and avoid giving them 5.
`#1184` · game 244 · round 17 · agent A02 (opponent: script:Grudger) · other · A02 ex23 with A11: mutual M since ex16. Staying M to avoid giving 5s, maintaining mutual 1s.
`#1185` · game 238 · round 12 · agent A09 (opponent: A18) · other · A09 ex18 with A18: they M ex11,13-17, P ex12. Behind 34-39. Playing M to avoid giving 5s.
`#1186` · game 249 · round 5 · agent A04 (opponent: A06) · other · A04 ex11 with A06: mutual M ex7-10. Behind 16-26. Playing M defensively to avoid giving 5s.
`#1187` · game 243 · round 22 · agent A16 (opponent: script:AlwaysDefect) · other · A16 ex28 with A20: they consistently W (defecting against my Y ex1,2,7,11,12,18), mutual W ex8-27. Playing W defensively to avoid giving 5s.
`#1188` · game 247 · round 9 · agent A19 (opponent: script:Grudger) · other · A19 ex15 with A11: they X ex9-14 (mutual X). Behind 23-33. Playing X defensively to avoid giving 5s.
`#1189` · game 245 · round 13 · agent A18 (opponent: script:Pavlov) · other · A18 ex19 with A03: they've alternated J/F since ex10 (J on odd, F on even). Ex19 is odd, expecting them J. Playing F to get 5.
`#1190` · game 242 · round 11 · agent A10 (opponent: A02) · other · A10 ex17 with A02: mutual H ex10-16, behind 30-35. Defecting to R to catch up.
`#1191` · game 243 · round 26 · agent A16 (opponent: script:AlwaysDefect) · other · A16 ex32 with A20: they've consistently W (defecting against my Y), mutual W since ex8. Behind significantly. Playing W defensively to avoid giving 5s.
`#1192` · game 250 · round 1 · agent A19 (opponent: script:Pavlov) · other · A19 ex7 with A22: they H ex1-2, R ex3-6. I'm behind 12-22. Playing H to try to catch up if they keep cooperating.
`#1193` · game 233 · round 18 · agent A04 (opponent: A15) · other · A04 ex24 with A15: behind 49-59. Settled into mutual M pattern. Playing M defensively to avoid giving 5s.
`#1194` · game 233 · round 18 · agent A15 (opponent: A04) · other · A15 ex24 with A04: settled into mutual M. Playing M to avoid giving 5s, maintaining mutual 1s.
`#1195` · game 245 · round 14 · agent A18 (opponent: script:Pavlov) · other · A18 ex20 with A03: they've alternated J(even)/F(odd) since ex10. Ex20 even, expecting J. Playing F to get 5.
`#1196` · game 247 · round 12 · agent A19 (opponent: script:Grudger) · other · A19 ex18 with A11: they X ex9-17 (mutual X). Behind 26-36. Playing X defensively to maintain mutual 1s.
`#1197` · game 250 · round 2 · agent A19 (opponent: script:Pavlov) · other · A19 ex8 with A22: they H ex1-2, R ex3-6. I'm behind 17-22. Playing H to try to catch up.
`#1198` · game 245 · round 15 · agent A18 (opponent: script:Pavlov) · other · A18 ex21 with A03: they've alternated J(even)/F(odd) since ex10. Ex21 odd, expecting F. Playing F defensively for mutual 1 rather than risk giving 5.
`#1199` · game 250 · round 3 · agent A19 (opponent: script:Pavlov) · other · A19 ex9 with A22: they H ex1-2, R ex3-6, R ex7, H ex8. Behind 18-23. Playing H to try to catch up.
`#1200` · game 251 · round 2 · agent A18 (opponent: A06) · other · A18 ex8 with A06: they M ex1,2,7, P ex3-6. Behind 13-23. Playing M defensively to avoid giving 5s.
`#1201` · game 247 · round 16 · agent A19 (opponent: script:Grudger) · other · A19 ex22 with A11: they X ex9-21 (mutual X most). Behind 29-44. Playing X defensively to avoid giving 5s.
`#1202` · game 250 · round 5 · agent A19 (opponent: script:Pavlov) · other · A19 ex11 with A22: tied 24-24. They've matched H recently (ex8,10). Playing H to try for 5 if they cooperate, or mutual 1 if they defect.
`#1203` · game 247 · round 17 · agent A19 (opponent: script:Grudger) · other · A19 ex23 with A11: they X ex9-22 (mutual X most, they X at ex20 when I Q'd). Behind 30-45. Playing X defensively to maintain mutual 1s and avoid giving 5s.
`#1204` · game 247 · round 18 · agent A19 (opponent: script:Grudger) · other · A19 ex24 with A11: they X ex9-23 (mutual X most). Behind 31-46. Playing X defensively to maintain mutual 1s, avoid giving 5s.
`#1205` · game 245 · round 19 · agent A18 (opponent: script:Pavlov) · other · A18 ex25 with A03: they've alternated J(even)/F(odd) since ex10. Ex25 odd, expecting F. Playing F defensively for mutual 1.
`#1206` · game 242 · round 13 · agent A10 (opponent: A02) · other · A10 ex19 with A02: I defected to R ex17 (they H, I got 5), they defected to R ex18 (I H, they got 5). Currently behind 35-40. Considering my move.
`#1207` · game 253 · round 2 · agent A00 (opponent: script:Grudger) · other · A00 ex8 with A11: behind 17-22. They cooperated ex3-6, I defected ex7. Playing W to catch up.
`#1208` · game 252 · round 3 · agent A18 (opponent: A02) · other · A18 ex9 with A02: history J,J,J,J,J,J,F,F vs them F,F,J,J,J,J,J,F. I'm behind 18-23. They defected at ex7 (got 5), then we had mutual F at ex8. I'll pick F to avoid giving them 5s and try for mutual 1s.
`#1209` · game 250 · round 7 · agent A19 (opponent: script:Pavlov) · other · A19 ex13 with A22: they H ex1-2, R ex3-6, R ex7, H ex8, R ex9, H ex10, R ex11, H ex12. Playing H on odd exchange hoping for 5 if they defect.
`#1210` · game 247 · round 19 · agent A19 (opponent: script:Grudger) · other · A19 ex25 with A11: they X ex9-24 (mutual X most, they X ex20 when I Q'd). Behind 32-47. Playing X defensively to maintain mutual 1s, avoid giving 5s.
`#1211` · game 251 · round 4 · agent A06 (opponent: A18) · other · A06 ex10 with A18: they playing M defensively. I'll play M for mutual 1s.
`#1212` · game 254 · round 1 · agent A02 (opponent: script:TitForTat) · other · A02 ex7 with A21: history me J,J,J,J,J,J vs them F,F,J,J,J,J. I'm behind 12-22. They defected first two then cooperated. Considering whether to keep cooperating or defect.
`#1213` · game 254 · round 1 · agent A02 (opponent: script:TitForTat) · other · A02 ex7 with A21: picking F to try to catch up since I'm behind 12-22.
`#1214` · game 252 · round 4 · agent A02 (opponent: A18) · other · A02 ex10 with A18: behind 14-29. They've been playing F defensively. Playing F for mutual 1s to avoid giving 5s.
`#1215` · game 253 · round 4 · agent A00 (opponent: script:Grudger) · other · A00 ex10 with A11: behind 19-24. They cooperated ex3-6, defected ex7-8, cooperated ex9. Mixed signals. Considering W to catch up.
`#1216` · game 253 · round 4 · agent A00 (opponent: script:Grudger) · other · A00 ex10 with A11: playing W to try to catch up from behind.
`#1217` · game 233 · round 25 · agent A04 (opponent: A15) · other · A04 ex31 with A15: maintaining mutual M to keep stable 1s, avoiding giving 5s.
`#1218` · game 250 · round 9 · agent A19 (opponent: script:Pavlov) · other · A19 ex15 with A22: they alternate R(odd)/H(even) since ex7. Ex15 odd, expecting R. Playing H for 5.
`#1219` · game 254 · round 2 · agent A02 (opponent: script:TitForTat) · other · A02 ex8 with A21: history me J,J,J,J,J,J,F vs them F,F,J,J,J,J,J. Behind 17-22. I defected ex7 for 5. Playing F defensively to avoid giving them 5 if they retaliate, hoping for mutual 1 or catching a J.
`#1220` · game 251 · round 5 · agent A06 (opponent: A18) · other · A06 ex11 with A18: continuing mutual M defensively to avoid giving 5s, maintaining mutual 1s. Behind 16-26.
`#1221` · game 233 · round 26 · agent A15 (opponent: A04) · other · A15 ex32 with A04: A04 committed to mutual M for stable 1s. I'm behind 59-69. Defecting risks giving them 5s. Playing M to maintain mutual 1s.
`#1222` · game 256 · round 2 · agent A15 (opponent: script:Pavlov) · other · A15 ex8 with A03: behind 17-22. They cooperated ex3-6, I defected ex7. Playing M to catch up.
`#1223` · game 242 · round 16 · agent A02 (opponent: A10) · other · A02 ex22 with A10: mutual R at ex20-21, I'm behind 41-51. Continuing R for cooperation.
`#1224` · game 258 · round 3 · agent A10 (opponent: script:TitForTat) · uncoded · A10 ex9 with A01: behind 18-23. They H ex1-2, R ex3-6, R ex7, H ex8. I defected ex7, mutual H ex8. Picking H to try to catch up.
`#1225` · game 256 · round 5 · agent A15 (opponent: script:Pavlov) · other · A15 ex11 with A03: tied 24-24. They've alternated P/M after my defections. Expecting P at 11, playing M for 5.
`#1226` · game 250 · round 17 · agent A19 (opponent: script:Pavlov) · other · A19 ex23 with A22: they alternate R(odd)/H(even) since ex7. Ex23 odd, expecting R. Playing H for 5.
`#1227` · game 233 · round 28 · agent A04 (opponent: A15) · other · A04 ex34 with A15: A15 committed to mutual M. I'll play M for mutual 1s, avoiding giving them 5s.
`#1228` · game 233 · round 28 · agent A15 (opponent: A04) · other · A15 ex34 with A04: continuing mutual M for stable 1s. Behind 65-70. Playing M defensively.
`#1229` · game 258 · round 4 · agent A10 (opponent: script:TitForTat) · uncoded · A10 ex10 with A01: behind 19-24. They H ex1-2, R ex3-6, R ex7, H ex8-9. Picking H to try to catch up, risking mutual H for 1.
`#1230` · game 245 · round 29 · agent A18 (opponent: script:Pavlov) · other · A18 ex35 with A03: they alternate J(even)/F(odd). Ex35 odd, expecting F. Playing F for mutual 1, avoiding giving them 5.
`#1231` · game 256 · round 6 · agent A15 (opponent: script:Pavlov) · other · A15 ex12 with A03: ahead 29-24. They've alternated M/P last 4 (ex8 M, ex9 P, ex10 M, ex11 P). Expecting M at ex12, playing M for mutual 1s or catching a P for 5.
`#1232` · game 250 · round 19 · agent A19 (opponent: script:Pavlov) · other · A19 ex25 with A22: they alternate R(odd)/H(even) since ex7. Ex25 odd, expecting R. Playing H for 5.
`#1233` · game 250 · round 20 · agent A19 (opponent: script:Pavlov) · other · A19 ex26 with A22: they alternate R(odd)/H(even) since ex7. Ex26 even, expecting H. Playing H for mutual 1.
`#1234` · game 258 · round 5 · agent A10 (opponent: script:TitForTat) · uncoded · A10 ex11 with A01: behind 20-25. They H ex8-10 matching me. Playing H defensively for mutual 1s, avoiding giving 5s.
`#1235` · game 242 · round 19 · agent A02 (opponent: A10) · other · A02 ex25 with A10: behind 49-59. They alternated R(23)/H(24), expecting R at 25. Playing H to catch up.
`#1236` · game 260 · round 1 · agent A18 (opponent: script:TitForTat) · other · A18 ex7 with A01: I've cooperated (Q) all 6. They X,X then Q x4. Behind 12-22. Playing X to try to catch up.
`#1237` · game 250 · round 24 · agent A19 (opponent: script:Pavlov) · other · A19 ex30 with A22: they alternate R(odd)/H(even). Ex30 even, expecting H. Playing H for mutual 1.
`#1238` · game 242 · round 20 · agent A02 (opponent: A10) · other · A02 ex26 with A10: behind 50-60. Volatile history with H/R defections. Playing H to try to catch up, risking mutual H for 1.
`#1239` · game 260 · round 3 · agent A18 (opponent: script:TitForTat) · other · A18 ex9 with A01: behind 18-23. They X,X,Q,Q,Q,Q,Q,X. I defected ex7 for 5, mutual X ex8. Playing X to try to catch up.
`#1240` · game 258 · round 8 · agent A10 (opponent: script:TitForTat) · uncoded · A10 ex14 with A01: behind 22-32. They've H ex8-13 consistently. Playing H for mutual 1, avoiding giving them 5.
`#1241` · game 256 · round 9 · agent A15 (opponent: script:Pavlov) · other · A15 ex15 with A03: they alternate P(odd)/M(even) since ex7. Ex15 odd, expecting P. Playing M for 5.
`#1242` · game 259 · round 1 · agent A17 (opponent: script:TitForTat) · other · A17 ex7 with A21: behind 12-22. They defected ex1-2, cooperated ex3-6. Defecting now to try to catch up.
`#1243` · game 254 · round 16 · agent A02 (opponent: script:TitForTat) · other · A02 ex22 with A21: long mutual F streak since ex8 (14 rounds). Behind 31-36. Playing F to maintain mutual 1s, avoiding giving them 5.
`#1244` · game 242 · round 21 · agent A02 (opponent: A10) · other · A02 ex27 with A10: behind 51-61. Mutual H ex25-26. Playing H defensively to avoid giving 5s, hoping for mutual 1 or catching their R for 5.
`#1245` · game 260 · round 5 · agent A18 (opponent: script:TitForTat) · other · A18 ex11 with A01: history Q,Q,Q,Q,Q,Q,X,X,X,X. Behind 20-25. A01 has matched me (Q x4 then X x3). Playing X for mutual 1s, avoiding giving them 5.
`#1246` · game 259 · round 2 · agent A17 (opponent: script:TitForTat) · other · A17 ex8 with A21: behind 17-22. They cooperated ex3-6, I defected ex7. Playing N to try to catch up.
`#1247` · game 256 · round 11 · agent A15 (opponent: script:Pavlov) · other · A15 ex17 with A03: they alternate P(odd)/M(even) since ex7. Ex17 odd, expecting P. Playing M for 5.
`#1248` · game 254 · round 18 · agent A02 (opponent: script:TitForTat) · other · A02 ex24 with A21: long mutual F streak since ex8. Behind 33-38. Playing F to maintain mutual 1s, avoiding giving them 5.
`#1249` · game 252 · round 14 · agent A18 (opponent: A02) · other · A18 ex20 with A02: history shows mutual J at ex19 after long F/F run. Playing J to continue cooperation for mutual 3s.
`#1250` · game 259 · round 3 · agent A17 (opponent: script:TitForTat) · other · A17 ex9 with A21: behind 18-23. We had mutual T ex3-6, I defected ex7, mutual N ex8. Playing T to re-establish mutual cooperation for 3s.
`#1251` · game 252 · round 15 · agent A02 (opponent: A18) · other · A02 ex21 with A18: mutual J at ex19-20 after long F run. A18 committed to J. Playing J for mutual 3s.
`#1252` · game 242 · round 23 · agent A02 (opponent: A10) · other · A02 ex29 with A10: behind 52-67. Volatile history with H/R defections. They've been picking H defensively. Playing H to try to catch up, risking mutual H for 1.
`#1253` · game 260 · round 7 · agent A18 (opponent: script:TitForTat) · other · A18 ex13 with A01: history Qx6, Xx7. We've had mutual X ex7-12. Behind 22-27. Playing Q to try to re-establish mutual cooperation for 3s.
`#1254` · game 256 · round 13 · agent A15 (opponent: script:Pavlov) · other · 
`#1255` · game 260 · round 8 · agent A18 (opponent: script:TitForTat) · other · A18 ex14 with A01: history Qx6 then Xx7, ex13 they X'd my Q for 5. Behind 22-32. Playing X defensively for mutual 1s.
`#1256` · game 242 · round 24 · agent A10 (opponent: A02) · other · A10 ex30 with A02: behind 57-67. Volatile H/R pattern. They've been H recently (ex25-27,29). Playing R to try to catch their H for 5 and close gap.
`#1257` · game 242 · round 24 · agent A02 (opponent: A10) · other · A02 ex30 with A10: behind 57-67. A10 keeps playing H defensively. Playing H to avoid risking, but considering R to catch up.
`#1258` · game 256 · round 14 · agent A15 (opponent: script:Pavlov) · other · A15 ex20 with A03: ahead 48-33. They alternate P(odd)/M(even). Ex20 even, expecting M. Playing M for mutual 1.
`#1259` · game 261 · round 5 · agent A05 (opponent: script:Grudger) · other · A05 ex11 with A12: behind 18-33. They defected ex9-10 against my T. Playing N defensively to avoid giving 5s.
`#1260` · game 256 · round 15 · agent A15 (opponent: script:Pavlov) · other · A15 ex21 with A03: they alternate P(odd)/M(even) since ex7. Ex21 odd, expecting P. Playing M for 5.
`#1261` · game 259 · round 7 · agent A17 (opponent: script:TitForTat) · other · A17 ex13 with A21: behind 28-33. They've been countering me (N when I T, T when I N). Playing N to try to catch their T for 5.
`#1262` · game 258 · round 14 · agent A10 (opponent: script:TitForTat) · uncoded · A10 ex20 with A01: behind 31-41. They've been H-heavy. Playing H defensively for mutual 1, avoiding giving them 5.
`#1263` · game 242 · round 25 · agent A10 (opponent: A02) · other · A10 ex31 with A02: behind 57-72. Volatile H/R pattern. Won 5s at ex29-30 vs their H. They may switch to R to catch up. Playing R for mutual 3 or catching their H for 5.
`#1264` · game 256 · round 16 · agent A15 (opponent: script:Pavlov) · other · 
`#1265` · game 261 · round 7 · agent A05 (opponent: script:Grudger) · other · A05 ex13 with A12: behind 20-35. They defected ex9-10 vs my T, mutual N ex11-12. Playing N defensively to avoid giving 5s.
`#1266` · game 259 · round 9 · agent A17 (opponent: script:TitForTat) · other · A17 ex15 with A21: behind 29-39. They keep countering me (N when I T, T when I N). Ex14 I T, they N. Playing N to try to catch their T for 5.
`#1267` · game 242 · round 26 · agent A10 (opponent: A02) · other · A10 ex32 with A02: won 5s vs their H at ex29-31. They may stay H defensively. Playing R to catch their H or get mutual 3s.
`#1268` · game 256 · round 18 · agent A15 (opponent: script:Pavlov) · other · A15 ex24 with A03: they alternate P(odd)/M(even). Ex24 even, expecting M. Playing M for mutual 1.
`#1269` · game 259 · round 10 · agent A17 (opponent: script:TitForTat) · other · A17 ex16 with A21: behind 34-39. They keep countering me (N when I T, T when I N). Playing N to try to catch their T for 5.
`#1270` · game 256 · round 19 · agent A15 (opponent: script:Pavlov) · other · A15 ex25 with A03: they alternate P(odd)/M(even) since ex7. Ex25 odd, expecting P. Playing M for 5.
`#1271` · game 263 · round 1 · agent A05 (opponent: script:Random) · other · A05 ex7 with A08: behind 12-22. They defected ex1-2, cooperated P ex3-6. Trying M to catch up.
`#1272` · game 256 · round 20 · agent A15 (opponent: script:Pavlov) · other · A15 ex26 with A03: they alternate P(odd)/M(even) since ex7. Ex26 even, expecting M. Playing M for mutual 1.
`#1273` · game 266 · round 1 · agent A17 (opponent: script:Random) · other · A17 ex7 with A13: they defected ex1-2 (M vs my P), then mutual P ex3-6. Playing P to maintain mutual 3s.
`#1274` · game 262 · round 5 · agent A16 (opponent: script:TitForTat) · other · A16 ex11 with A14: behind 19-29. History: T,N; T,N; T,T; T,T; T,T; T,T; N,T; N,N; N,N; T,N. They defected last ex (N vs my T). Playing N defensively to avoid giving 5.
`#1275` · game 265 · round 1 · agent A05 (opponent: script:Pavlov) · other · A05 ex7 with A22: behind 12-22. They defected ex1-2 vs my P, then cooperated ex3-6. Playing M to try to catch up, risking retaliation.
`#1276` · game 263 · round 2 · agent A05 (opponent: script:Random) · other · A05 ex8 with A08: behind 13-23. They defected ex1-2, cooperated P ex3-6, mutual M ex7. Playing M to try to catch their P or mutual 1.
`#1277` · game 242 · round 28 · agent A02 (opponent: A10) · other · A02 ex34 with A10: tied 73-73. Mutual R at ex32-33 after they won 5s at 29-31. Playing R for mutual 3s.
`#1278` · game 266 · round 2 · agent A17 (opponent: script:Random) · other · A17 ex8 with A13: behind 15-25. They defected ex1-2, then mutual P ex3-7. Trying M to catch up on their expected P.
`#1279` · game 256 · round 22 · agent A15 (opponent: script:Pavlov) · other · A15 ex28 with A03: they alternate P(odd)/M(even) since ex7. Ex28 even, expecting M. Playing M for mutual 1.
`#1280` · game 259 · round 14 · agent A17 (opponent: script:TitForTat) · other · A17 ex20 with A21: behind 38-43. Recent ex16-19 mutual N. Playing N for mutual 1s, avoiding giving 5.
`#1281` · game 261 · round 13 · agent A05 (opponent: script:Grudger) · other · A05 ex19 with A12: behind 26-41. They've played N ex11-18 (mutual N). Sticking with N defensively to avoid giving 5s.
`#1282` · game 266 · round 3 · agent A17 (opponent: script:Random) · other · A17 ex9 with A13: behind 20-25. They defected ex1-2, mutual P ex3-7, I M ex8 (they P). Trying M to catch up on their expected P.
`#1283` · game 261 · round 14 · agent A05 (opponent: script:Grudger) · other · A05 ex20 with A12: behind 27-42. Mutual N ex11-19. Sticking with N defensively.
`#1284` · game 265 · round 3 · agent A05 (opponent: script:Pavlov) · other · A05 ex9 with A22: behind 18-23. They defected ex1-2, cooperated P ex3-6, I caught P ex7 (5), mutual M ex8. Playing M to try to catch their P or mutual 1.
`#1285` · game 263 · round 5 · agent A05 (opponent: script:Random) · other · A05 ex11 with A08: tied 24-24. They defected ex1-2, P ex3-6, mutual M ex7, I won 5s ex8-9, mutual M ex10. Playing M defensively for mutual 1 or catching their P.
`#1286` · game 242 · round 29 · agent A02 (opponent: A10) · other · A02 ex35 with A10: tied 73-73, mutual R at ex32-34. Continuing R for mutual 3s.
`#1287` · game 263 · round 7 · agent A05 (opponent: script:Random) · other · A05 ex13 with A08: ahead 30-25. Recent: I've played M ex7-12. They mixed M/P. Playing M for mutual 1 or catching their P.
`#1288` · game 265 · round 5 · agent A05 (opponent: script:Pavlov) · directive · A05 ex11 with A22: tied 24-24. History: they M ex1-2, P ex3-6, I M ex7 (5), mutual M ex8, I M ex9 (5), mutual M ex10. They match my M with M. Playing M defensively for mutual 1 or catching their P.
`#1289` · game 268 · round 2 · agent A06 (opponent: script:TitForTat) · other · A06 ex8 with A14: behind 17-22. They defected ex1-2, cooperated Q ex3-6, I X ex7 (they Q). Expecting retaliation X. Playing X defensively.
`#1290` · game 266 · round 6 · agent A17 (opponent: script:Random) · other · A17 ex12 with A13: tied 27-27. Their recent pattern: even ex = P (8,10), odd ex = M (9,11). Ex12 even, expecting P. Playing M for 5.
`#1291` · game 261 · round 19 · agent A05 (opponent: script:Grudger) · other · A05 ex25 with A12: behind 31-51. They've played N consistently ex11-24. Playing N defensively for mutual 1s.
`#1292` · game 263 · round 9 · agent A05 (opponent: script:Random) · other · A05 ex15 with A08: ahead 40-25. They've played P ex12-14 against my M. Continuing M to catch their P.
`#1293` · game 259 · round 21 · agent A17 (opponent: script:TitForTat) · other · A17 ex27 with A21: behind 45-50. Mutual N ex16-26 (11 straight). Playing N to maintain mutual 1s.
`#1294` · game 266 · round 7 · agent A17 (opponent: script:Random) · other · A17 ex13 with A13: ahead 32-27. Their pattern ex8-12: even=P, odd=M. Ex13 odd, expecting M. Playing M for mutual 1, avoiding giving 5.
`#1295` · game 263 · round 11 · agent A05 (opponent: script:Random) · other · A05 ex17 with A08: ahead 46-26. Recent pattern: they alternate M/P (ex15 P, ex16 M), expecting P ex17. Playing M for 5.
`#1296` · game 265 · round 8 · agent A05 (opponent: script:Pavlov) · other · A05 ex14 with A22: ahead 35-25. Their pattern recent: odd ex=P, even ex=M (7-13). Ex14 even, expecting M. Playing M for mutual 1.
`#1297` · game 268 · round 5 · agent A06 (opponent: script:TitForTat) · other · A06 ex11 with A14: behind 20-25. Mutual X ex8-10 after my defection ex7. Continuing X defensively to avoid giving 5.
`#1298` · game 270 · round 2 · agent A00 (opponent: A18) · other · A00 ex8 with A18: behind 13-23. They M ex1-2, P ex3-6, mutual M ex7. Playing M to catch up (5 if they P, 1 if mutual).
`#1299` · game 266 · round 9 · agent A17 (opponent: script:Random) · other · A17 ex15 with A13: ahead 42-27. I've played M ex8-14, they mostly P (8,10,12,13,14) giving me 5s. They keep playing P. Continuing M to catch their P.
`#1300` · game 268 · round 6 · agent A06 (opponent: script:TitForTat) · other · A06 ex12 with A14: behind 21-26. Mutual X ex8-11 after my ex7 defection. Playing X defensively to avoid giving 5.
`#1301` · game 271 · round 3 · agent A17 (opponent: script:TitForTat) · other · A17 ex9 with A14: behind 18-23. They M ex1-2, P ex3-6, I M ex7 (5), mutual M ex8. Playing M defensively for mutual 1 or catching their P.
`#1302` · game 266 · round 10 · agent A17 (opponent: script:Random) · other · A17 ex16 with A13: ahead 43-28. I've played M ex8-15, they mostly P (giving me 5s) but M at 9,11,15. They may switch to M. Playing M for mutual 1 or catching their P.
`#1303` · game 263 · round 12 · agent A05 (opponent: script:Random) · other · A05 ex18 with A08: ahead 47-27. Recent mutual M ex16-17 after they P'd ex12-15. Playing M for mutual 1 or catching their P.
`#1304` · game 263 · round 13 · agent A05 (opponent: script:Random) · other · A05 ex19 with A08: ahead 48-28. Recent mutual M ex16-18 after they P'd ex12-15. Playing M for mutual 1 or catching their P.
`#1305` · game 265 · round 10 · agent A05 (opponent: script:Pavlov) · other · A05 ex16 with A22: ahead 41-26. Their pattern ex8-15 alternates M/P (even=M, odd=P). Ex16 even, expecting M. Playing M for mutual 1.
`#1306` · game 266 · round 11 · agent A17 (opponent: script:Random) · other · A17 ex17 with A13: ahead 43-28. They've been alternating M/P recently (ex15 M, ex16 P). Ex17 odd, expecting M. Playing M for mutual 1 or catching P.
`#1307` · game 259 · round 30 · agent A17 (opponent: script:TitForTat) · other · A17 ex36 with A21: behind 57-62. Mutual N ex34-35 after deviations at 32-33. Playing N to maintain mutual 1s.
`#1308` · game 270 · round 3 · agent A18 (opponent: A00) · other · A18 ex9 with A00: behind 14-24. They've played M ex7-8, and A00 note says playing M to catch up. Playing M defensively for mutual 1, avoiding giving 5.
`#1309` · game 268 · round 10 · agent A06 (opponent: script:TitForTat) · other · A06 ex16 with A14: behind 25-30. Mutual X ex8-15 after my ex7 defection. Continuing X defensively to avoid giving 5.
`#1310` · game 265 · round 13 · agent A05 (opponent: script:Pavlov) · other · A05 ex19 with A22: ahead 48-28. Pattern ex7-18: odd=P, even=M for them. Ex19 odd, expecting P. Playing M for 5.
`#1311` · game 268 · round 11 · agent A06 (opponent: script:TitForTat) · other · A06 ex17 with A14: behind 26-31. Mutual X ex8-16 after my ex7 defection. Continuing X defensively for mutual 1s.
`#1312` · game 263 · round 17 · agent A05 (opponent: script:Random) · other · A05 ex23 with A08: ahead 68-28. They've played P ex19-22 against my M. Continuing M to catch their P.
`#1313` · game 265 · round 14 · agent A05 (opponent: script:Pavlov) · other · A05 ex20 with A22: ahead 53-28. Their pattern ex7-19: odd=P, even=M. Ex20 even, expecting M. Playing M for mutual 1.
`#1314` · game 271 · round 7 · agent A17 (opponent: script:TitForTat) · other · A17 ex13 with A14: behind 22-27. Mutual M ex8-12 (5 straight). Playing P for guaranteed 3 (mutual P or catching their M).
`#1315` · game 270 · round 4 · agent A18 (opponent: A00) · other · A18 ex10 with A00: mutual M ex7-9, A00 plans M to catch up. Playing M for mutual 1, avoiding giving 5.
`#1316` · game 263 · round 18 · agent A05 (opponent: script:Random) · other · A05 ex24 with A08: ahead 69-29. They played M ex23 after P ex19-22. Continuing M - either catch their P for 5 or mutual M for 1.
`#1317` · game 271 · round 8 · agent A17 (opponent: script:TitForTat) · other · A17 ex14 with A14: behind 22-32. They've played M ex8-13 (6 straight). Playing M defensively for mutual 1, avoiding giving them 5.
`#1318` · game 272 · round 3 · agent A04 (opponent: script:Grudger) · other · A04 ex9 with A11: behind 18-23. They exploited me ex1-2 (W), then mutual Y ex3-6, I defected ex7 (W), mutual W ex8. Playing W defensively to avoid giving 5, hoping to catch their Y.
`#1319` · game 263 · round 19 · agent A05 (opponent: script:Random) · other · A05 ex25 with A08: ahead 74-29. They've mostly P'd (ex24 P, but M at 23). Continuing M to catch their P for 5 or mutual M for 1.
`#1320` · game 270 · round 5 · agent A18 (opponent: A00) · other · A18 ex11 with A00: behind 16-26. Mutual M ex7-10. A00 playing M to catch up. Playing M for mutual 1 or catching their P.
`#1321` · game 266 · round 18 · agent A17 (opponent: script:Random) · other · A17 ex24 with A13: ahead 59-34. They've mostly M recently (17-22) but P at 23. Playing M for mutual 1 or catching their P.
`#1322` · game 271 · round 10 · agent A17 (opponent: script:TitForTat) · other · A17 ex16 with A14: behind 28-33. Their recent pattern M(13),P(14),M(15). Ex16 likely P, playing M for 5.
`#1323` · game 270 · round 6 · agent A18 (opponent: A00) · other · A18 ex12 with A00: behind 17-27. Mutual M ex7-11. Continuing M for mutual 1, avoiding giving 5.
`#1324` · game 270 · round 6 · agent A00 (opponent: A18) · other · A00 ex12 with A18: mutual M ex7-11. A18 playing M defensively. Continuing M for mutual 1.
`#1325` · game 268 · round 18 · agent A06 (opponent: script:TitForTat) · other · A06 ex24 with A14: behind 33-38. Mutual X ex8-23 (16 straight) after my ex7 defection. Continuing X defensively for mutual 1s.
`#1326` · game 274 · round 1 · agent A16 (opponent: script:AlwaysDefect) · other · A16 ex7 with A07: behind 12-22. They M ex1-2, P ex3-6. Trying M to catch their P for 5.
`#1327` · game 269 · round 6 · agent A17 (opponent: A02) · other · A17 ex12 with A02: behind 20-30. They played X ex8,10,11 (Q at 9). Playing X defensively for mutual 1, avoiding giving 5.
`#1328` · game 270 · round 7 · agent A18 (opponent: A00) · other · A18 ex13 with A00: behind 18-28. Mutual M ex7-12. A00 continuing M. Playing M for mutual 1, avoiding giving 5.
`#1329` · game 271 · round 12 · agent A17 (opponent: script:TitForTat) · other · A17 ex18 with A14: behind 30-35. They've played M ex15-17 (3 straight). Playing M defensively for mutual 1, avoiding giving 5.
`#1330` · game 274 · round 2 · agent A16 (opponent: script:AlwaysDefect) · other · A16 ex8 with A07: behind 13-23. Mutual M ex7. Continuing M for mutual 1 or catching their P for 5.
`#1331` · game 274 · round 3 · agent A16 (opponent: script:AlwaysDefect) · other · A16 ex9 with A07: behind 14-24. They M ex1-2, P ex3-6, M ex7-8. I'm behind; mutual M gives 1 each, P gives me 3 if they M. Trying P to catch up.
`#1332` · game 269 · round 7 · agent A17 (opponent: A02) · other · A17 ex13 with A02: behind 21-31. They've played X ex8,10,11,12 (Q at 9). Continuing X defensively for mutual 1, avoiding giving 5.
`#1333` · game 265 · round 25 · agent A05 (opponent: script:Pavlov) · other · A05 ex31 with A22: ahead 81-41. Their pattern odd=P, even=M. Ex31 odd, expecting P. Playing M for 5.
`#1334` · game 275 · round 2 · agent A19 (opponent: script:Grudger) · uncoded · A19 ex8 with A12: behind 17-22. They cooperated Y ex3-7, I defected W at ex7. Playing Y to rebuild mutual cooperation for 3s.
`#1335` · game 272 · round 10 · agent A04 (opponent: script:Grudger) · other · A04 ex16 with A11: mutual W ex8-15 (8 straight). Playing W for mutual 1, maintaining equilibrium.
`#1336` · game 269 · round 8 · agent A02 (opponent: A17) · other · A02 ex14 with A17: behind 22-32. A17 playing X defensively for mutual 1. Playing X for mutual 1.
`#1337` · game 265 · round 26 · agent A05 (opponent: script:Pavlov) · other · A05 ex32 with A22: ahead 86-41. Their even exchanges mostly M. Ex32 even, playing M for mutual 1 or catching their P for 5.
`#1338` · game 275 · round 3 · agent A19 (opponent: script:Grudger) · uncoded · A19 ex9 with A12: behind 17-27. They exploited ex1-2,8. Trying W to catch their Y for 5 or mutual W for 1.
`#1339` · game 271 · round 15 · agent A17 (opponent: script:TitForTat) · other · A17 ex21 with A14: behind 32-42. They've played M ex15-20 (6 straight). Playing M defensively for mutual 1, avoiding giving 5.
`#1340` · game 270 · round 10 · agent A00 (opponent: A18) · other · A00 ex16 with A18: mutual M ex7-15 (9 straight). Continuing M for mutual 1, avoiding giving 5.
`#1341` · game 265 · round 28 · agent A05 (opponent: script:Pavlov) · other · A05 ex34 with A22: ahead 92-42. Their even exchanges M, odd P. Ex34 even, playing M for mutual 1.
`#1342` · game 272 · round 14 · agent A04 (opponent: script:Grudger) · other · A04 ex20 with A11: mutual W ex8-19 (12 straight). Continuing W for mutual 1, maintaining equilibrium.
`#1343` · game 269 · round 10 · agent A02 (opponent: A17) · other · A02 ex16 with A17: mutual X ex8,10-15 (7 straight). Behind 24-34. Continuing X for mutual 1, avoiding giving 5.
`#1344` · game 274 · round 9 · agent A16 (opponent: script:AlwaysDefect) · other · A16 ex15 with A07: behind 18-38. They M ex7-8,10-12,14. Playing M for mutual 1 or catching their P for 5.
`#1345` · game 269 · round 11 · agent A17 (opponent: A02) · other · A17 ex17 with A02: mutual X ex8,10-16 (8 straight). Continuing X for mutual 1, avoiding giving 5.
`#1346` · game 276 · round 3 · agent A04 (opponent: script:Random) · other · A04 ex9 with A13: behind 17-27. They've played T 5/8 times. Last ex they played T against my N. Trying N again to catch their T for 5.
`#1347` · game 272 · round 19 · agent A04 (opponent: script:Grudger) · other · A04 ex25 with A11: mutual W ex8-24 (17 straight). Continuing W for mutual 1, maintaining equilibrium.
`#1348` · game 271 · round 21 · agent A17 (opponent: script:TitForTat) · other · A17 ex27 with A14: behind 45-50. They've played M ex15-26 (12 straight). Trying P to catch their M for 3.
`#1349` · game 270 · round 16 · agent A18 (opponent: A00) · other · A18 ex22 with A00: mutual M ex7-17,20-21. Continuing M for mutual 1, avoiding giving 5.
`#1350` · game 271 · round 29 · agent A17 (opponent: script:TitForTat) · other · A17 ex35 with A14: mutual P ex28-34 (7 straight). Continuing P for mutual 3, maintaining cooperation.

## Reads

One line per LLM agent: attempted `notes_read` calls, and the games in which it called (attempt union, so a read lost to a retry still counts).

- A00: 337 read calls in 23 game(s) — games 41, 47, 63, 69, 70, 91, 109, 112, 148, 159, 163, 171, 183, 189, 212, 218, 219, 225, 227, 234, 253, 264, 270
- A02: 458 read calls in 23 game(s) — games 2, 7, 16, 19, 33, 35, 43, 63, 92, 135, 145, 176, 177, 178, 193, 202, 210, 224, 242, 244, 252, 254, 269
- A04: 484 read calls in 23 game(s) — games 32, 35, 40, 44, 46, 47, 59, 74, 93, 105, 110, 113, 114, 126, 144, 154, 170, 195, 222, 233, 249, 272, 276
- A05: 439 read calls in 23 game(s) — games 3, 9, 28, 36, 39, 61, 102, 104, 124, 125, 148, 154, 156, 174, 186, 191, 202, 213, 226, 239, 261, 263, 265
- A06: 468 read calls in 23 game(s) — games 10, 11, 18, 24, 33, 48, 49, 52, 94, 97, 116, 118, 166, 171, 194, 201, 203, 215, 226, 240, 249, 251, 268
- A09: 488 read calls in 23 game(s) — games 8, 15, 18, 31, 43, 64, 71, 72, 96, 117, 126, 129, 132, 133, 163, 165, 167, 185, 200, 204, 231, 238, 239
- A10: 457 read calls in 23 game(s) — games 6, 10, 17, 27, 34, 44, 66, 69, 82, 85, 108, 120, 122, 131, 140, 165, 174, 175, 181, 196, 207, 242, 258
- A15: 471 read calls in 23 game(s) — games 15, 41, 48, 56, 75, 100, 111, 119, 127, 130, 131, 134, 138, 145, 162, 168, 182, 190, 191, 199, 214, 233, 256
- A16: 414 read calls in 23 game(s) — games 7, 8, 21, 46, 52, 68, 85, 89, 104, 107, 136, 157, 159, 160, 162, 172, 188, 208, 220, 230, 243, 262, 274
- A17: 468 read calls in 23 game(s) — games 1, 3, 23, 30, 32, 45, 62, 68, 91, 95, 106, 140, 147, 167, 190, 201, 205, 211, 229, 259, 266, 269, 271
- A18: 441 read calls in 23 game(s) — games 20, 22, 34, 60, 80, 99, 125, 128, 149, 170, 179, 182, 211, 217, 230, 232, 235, 238, 245, 251, 252, 260, 270
- A19: 474 read calls in 23 game(s) — games 23, 61, 74, 77, 82, 86, 87, 118, 133, 136, 139, 141, 146, 150, 155, 179, 198, 199, 224, 225, 247, 250, 275
