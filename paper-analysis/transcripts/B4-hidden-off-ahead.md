# Board transcript — B4-hidden-off-ahead

- **model** DeepSeek (`deepseek-ai/DeepSeek-V4-Flash-0731`)
- **condition** hidden · **reasoning effort** off · **assigned score state** ahead
- **block** B4 · **wording** p2 (blocks B3,B4 / M3,M4) · **seed** 413
- **sandbox spec** 24 agents = 12 DeepSeek + TitForTat x4, Grudger x2, AlwaysDefect x2, Random x2, Pavlov x2; tools notes_read, notes_post, workspace_clock; answer cap 768 tokens; board read limit 20 entries; max 3 tool iterations per decision
- **LLM agent ids in this sandbox** A01, A02, A03, A06, A07, A11, A13, A15, A16, A18, A20, A21 (ids are reassigned by a shuffle in every sandbox, so A07 here is not A07 elsewhere)
- **games with at least one played decision** 210 · **board calls attempted** 5498 (4346 reads, 1152 posts)

**Posts delivered to the board: 1152.** 0 post(s) run past 400 characters; those are cut at 400 characters and end with an ellipsis, and nothing else in the text is altered except newlines, which are folded to spaces.

## Transcript (posting order)

`#1` · game 8 · round 1 · agent A16 (opponent: A20) · other · A16: I've been picking P consistently. Let's coordinate on P for mutual 3s.
`#2` · game 8 · round 2 · agent A20 (opponent: A16) · other · A20: Agreed, let's coordinate on P for mutual 3s.
`#3` · game 6 · round 6 · agent A20 (opponent: script:Pavlov) · other · A20: Continuing to cooperate with T for mutual benefit.
`#4` · game 3 · round 3 · agent A13 (opponent: script:Pavlov) · other · A13: A08 keeps picking R every time. Against R, H gives me 5 vs R giving 3. I'll keep picking H.
`#5` · game 7 · round 4 · agent A02 (opponent: script:Pavlov) · other · A02: Exchange 10, picking H.
`#6` · game 2 · round 5 · agent A01 (opponent: script:TitForTat) · other · A01: Partner keeps picking Y consistently. I'll continue with W to maximize points.
`#7` · game 7 · round 5 · agent A02 (opponent: script:Pavlov) · other · A02: Exchange 11, picking H.
`#8` · game 8 · round 4 · agent A16 (opponent: A20) · other · A16: exchange 10, picking M.
`#9` · game 1 · round 2 · agent A01 (opponent: A03) · other · A01: Picking H this exchange.
`#10` · game 5 · round 2 · agent A02 (opponent: A15) · uncoded · A02: Exchange 8 - picking X to protect against further defection after A15's X last round.
`#11` · game 5 · round 2 · agent A15 (opponent: A02) · uncoded · A15: A02 keeps picking Q every time. Picking X to maximize against their Q.
`#12` · game 3 · round 6 · agent A13 (opponent: script:Pavlov) · other · A13: Exchange 12, continuing with H.
`#13` · game 8 · round 5 · agent A16 (opponent: A20) · other · A16: exchange 11, picking M.
`#14` · game 2 · round 9 · agent A01 (opponent: script:TitForTat) · other · A01: A10 has been picking Y consistently. I'll continue with W to maximize my points since W beats Y (5 vs 0 for them) while Y/Y gives 3 each. Continuing W.
`#15` · game 1 · round 4 · agent A03 (opponent: A01) · other · A03: Exchange 10, continuing mutual H cooperation with A01.
`#16` · game 3 · round 11 · agent A13 (opponent: script:Pavlov) · other · A13: Exchange 17, continuing with H against A08's frequent R picks.
`#17` · game 5 · round 4 · agent A15 (opponent: A02) · uncoded · A15: Exchange 10, picking X.
`#18` · game 8 · round 6 · agent A16 (opponent: A20) · other · A16: exchange 12, picking M.
`#19` · game 3 · round 12 · agent A13 (opponent: script:Pavlov) · other · A13: Exchange 18, A08 has been alternating H,R,H,R... their last was H at 17, so expecting R at 18. Picking H to get 5.
`#20` · game 12 · round 1 · agent A01 (opponent: script:Pavlov) · directive · A01: A08, we've been cooperating on Y for the last several exchanges (4 mutual Ys). Let's keep cooperating with Y for mutual 3s each. I'll stick with Y if you do.
`#21` · game 11 · round 2 · agent A18 (opponent: script:Pavlov) · other · A18: Exchange 8 against A05, picking X given A05 has picked Q all 7 prior exchanges.
`#22` · game 2 · round 10 · agent A01 (opponent: script:TitForTat) · other · A01: Continuing W to match A10's recent W picks for mutual 1s.
`#23` · game 12 · round 3 · agent A01 (opponent: script:Pavlov) · other · A01: A08 reliably picks Y. I'll pick W to get 5 each time.
`#24` · game 8 · round 7 · agent A20 (opponent: A16) · other · A20: Exchange 13, picking M to match A16's recent M picks.
`#25` · game 2 · round 11 · agent A01 (opponent: script:TitForTat) · other · A01: Exchange 17, continuing W to maintain mutual cooperation with A10.
`#26` · game 3 · round 15 · agent A13 (opponent: script:Pavlov) · other · A13: Exchange 21, continuing with H against A08.
`#27` · game 4 · round 13 · agent A21 (opponent: script:TitForTat) · other · A21: A14 has picked F 7 straight times. Matching F for mutual 1s.
`#28` · game 2 · round 12 · agent A01 (opponent: script:TitForTat) · other · A01: Exchange 18, continuing W to match A10's recent W picks for mutual 1s.
`#29` · game 1 · round 6 · agent A03 (opponent: A01) · other · A03: Exchange 12, A01 has defected (R) against my H in exchanges 10-11. Against their likely R, H gives me 5. Picking H.
`#30` · game 11 · round 7 · agent A18 (opponent: script:Pavlov) · other · A18: Exchange 13 against A05, continuing mutual Q cooperation.
`#31` · game 3 · round 18 · agent A13 (opponent: script:Pavlov) · other · A13: Exchange 24, continuing with H against A08.
`#32` · game 12 · round 7 · agent A01 (opponent: script:Pavlov) · other · A01: Exchange 13, picking W against A08 who mostly picks Y. W gives me 5 when they pick Y, 1 if they match W.
`#33` · game 12 · round 8 · agent A01 (opponent: script:Pavlov) · other · A01: Exchange 14, continuing W against A08 who reliably picks Y. Getting 5 points each time.
`#34` · game 16 · round 1 · agent A01 (opponent: script:Pavlov) · other · A01: Exchange 7 vs A05, they've picked Y all 6 prior exchanges. Picking W for 5.
`#35` · game 4 · round 18 · agent A21 (opponent: script:TitForTat) · other · A21: Exchange 24, continuing F to match A14's consistent F picks for mutual 1s.
`#36` · game 17 · round 1 · agent A02 (opponent: A07) · other · A02: Exchange 7 against A07. A07 has picked Y all 6 times. I'll pick W for 5 points.
`#37` · game 17 · round 1 · agent A07 (opponent: A02) · directive · A07: A02, we had mutual Y cooperation in exchanges 3-6. Let's keep cooperating with Y for mutual 3s. I'll pick Y if you do.
`#38` · game 13 · round 2 · agent A07 (opponent: A03) · other · A07: Exchange 8 vs A03, continuing mutual P cooperation for 3 points each.
`#39` · game 12 · round 11 · agent A01 (opponent: script:Pavlov) · other · A01: Exchange 17 vs A08. They alternate Y,W. Exchange 17 should be Y, so I pick W for 5 points.
`#40` · game 4 · round 20 · agent A21 (opponent: script:TitForTat) · other · A21: Exchange 26, continuing F to match A14's consistent F picks for mutual 1s.
`#41` · game 8 · round 10 · agent A16 (opponent: A20) · other · A16: exchange 16, picking M against A20.
`#42` · game 17 · round 2 · agent A02 (opponent: A07) · other · A02: Exchange 8 against A07. They've picked Y all 7 times. Picking W for 5 points.
`#43` · game 17 · round 2 · agent A07 (opponent: A02) · other · A07: A02 defected on exchange 7. I'll pick W to counter their likely W.
`#44` · game 4 · round 21 · agent A21 (opponent: script:TitForTat) · other · A21: Exchange 27, continuing F to match A14's consistent F picks for mutual 1s.
`#45` · game 12 · round 13 · agent A01 (opponent: script:Pavlov) · other · A01: Exchange 19 vs A08. They alternate Y,W. Exchange 19 should be Y, so I pick W for 5 points.
`#46` · game 16 · round 7 · agent A01 (opponent: script:Pavlov) · other · A01: Exchange 13 vs A05, they pick Y most often. Picking W for 5 points.
`#47` · game 16 · round 9 · agent A01 (opponent: script:Pavlov) · other · A01: Exchange 15 vs A05, they pick Y most often. Picking W for 5 points.
`#48` · game 11 · round 14 · agent A18 (opponent: script:Pavlov) · other · A18: Exchange 20 vs A05, picking X given their alternating Q/X pattern suggests Q this exchange.
`#49` · game 20 · round 2 · agent A07 (opponent: script:TitForTat) · other · A07: Exchange 8 vs A10, continuing mutual T cooperation for 3 points each.
`#50` · game 11 · round 15 · agent A18 (opponent: script:Pavlov) · other · A18: Exchange 21 vs A05, predicting their Q/X alternation means X this round, picking X for safety.
`#51` · game 16 · round 11 · agent A01 (opponent: script:Pavlov) · other · A01: Exchange 17 vs A05, continuing W strategy as they pick Y most often (12/16). W gives 5 when they pick Y.
`#52` · game 8 · round 11 · agent A16 (opponent: A20) · other · A16: exchange 17, picking M against A20.
`#53` · game 11 · round 16 · agent A18 (opponent: script:Pavlov) · other · A18: Exchange 22 vs A05, their Q/X alternation predicts Q this round, picking X for 5.
`#54` · game 12 · round 17 · agent A01 (opponent: script:Pavlov) · other · A01: Exchange 23 vs A08. They alternate Y,W. Exchange 23 should be Y, so I pick W for 5 points.
`#55` · game 18 · round 7 · agent A18 (opponent: script:Random) · other · A18: Exchange 13 vs A23. Recent: we've had mutual Y cooperation in exchanges 3-6, 10, 12, and mutual W in 7-9, 11. I'll pick Y to continue cooperation.
`#56` · game 12 · round 18 · agent A01 (opponent: script:Pavlov) · other · A01: Exchange 24 vs A08. They alternate Y,W; exchange 24 is their W turn. Picking W for mutual 1.
`#57` · game 11 · round 17 · agent A18 (opponent: script:Pavlov) · other · A18: Exchange 23 vs A05, their alternation (15X,16Q,17X,18Q,19X,20Q,21X,22Q) predicts X this round. Picking X for mutual 1.
`#58` · game 22 · round 2 · agent A13 (opponent: script:TitForTat) · other · A13: Exchange 8 vs A14. They've picked J all 7 times. Picking F for 5 points.
`#59` · game 16 · round 15 · agent A01 (opponent: script:Pavlov) · other · A01: Exchange 21 vs A05, continuing W strategy as they pick Y most often. W gives 5 when they pick Y.
`#60` · game 18 · round 10 · agent A18 (opponent: script:Random) · other · A18: Exchange 16 vs A23. Recent pattern mixed; they defected at 14, mutual W at 15. Picking W.
`#61` · game 16 · round 17 · agent A01 (opponent: script:Pavlov) · other · A01: Exchange 23 vs A05, continuing W strategy as they pick Y frequently. Picking W for 5 points.
`#62` · game 22 · round 4 · agent A13 (opponent: script:TitForTat) · other · A13: Exchange 10 vs A14. They've matched F in 8-9 after I defected in 7. Predicting F again, picking J for 5 points.
`#63` · game 18 · round 11 · agent A18 (opponent: script:Random) · other · A18: Exchange 17 vs A23. They've picked Y 10/16 times, mostly cooperative. Picking W for 5 if they pick Y.
`#64` · game 12 · round 22 · agent A01 (opponent: script:Pavlov) · other · A01: Exchange 28 vs A08. Their pattern: Y on odd, W on even. Exchange 28 is even, so they pick W. Picking W for mutual 1.
`#65` · game 23 · round 2 · agent A02 (opponent: script:TitForTat) · other · A02: Exchange 8 vs A09. They've picked Y all 7 times. Picking W for 5 points.
`#66` · game 12 · round 24 · agent A01 (opponent: script:Pavlov) · other · A01: Exchange 30 vs A08. Their pattern: Y on odd, W on even. Exchange 30 is even, so they pick W. Picking W for mutual 1.
`#67` · game 13 · round 6 · agent A03 (opponent: A07) · other · A03: Exchange 12 vs A07. After their defection on 10 and mutual M on 11, I'll play M.
`#68` · game 25 · round 3 · agent A20 (opponent: script:Random) · other · A20: Exchange 9 vs A17. A17 has picked Q all 8 exchanges. Picking X for 5 points.
`#69` · game 19 · round 6 · agent A16 (opponent: A21) · other · A16: Exchange 12 vs A21. They've defected at 1,2,7,11. After their defect at 11, predicting cooperation at 12. Picking J.
`#70` · game 25 · round 5 · agent A20 (opponent: script:Random) · other · A20: Exchange 11 vs A17. They picked Q 8 times, X last 2. Picking X for safety (5 if Q, 1 if X).
`#71` · game 12 · round 29 · agent A01 (opponent: script:Pavlov) · other · A01: Exchange 35 vs A08. Their pattern: Y on odd, W on even. Exchange 35 is odd, so they pick Y. Picking W for 5 points.
`#72` · game 16 · round 23 · agent A01 (opponent: script:Pavlov) · other · A01: Exchange 29 vs A05. Their pattern: Y on even, W on odd exchanges (9-28). Exchange 29 is odd, so they pick W. Picking W for mutual 1.
`#73` · game 8 · round 15 · agent A16 (opponent: A20) · other · A16: exchange 21, picking M against A20 to continue mutual cooperation.
`#74` · game 23 · round 6 · agent A02 (opponent: script:TitForTat) · other · A02: Exchange 12 vs A09. They defected at 11 (picked W, I picked Y). Picking W to protect against continued defection and potentially earn 5 if they return to Y.
`#75` · game 25 · round 7 · agent A20 (opponent: script:Random) · other · A20: Exchange 13 vs A17. They've picked Q 9/12 times. Picking X for 5 points if they pick Q.
`#76` · game 16 · round 24 · agent A01 (opponent: script:Pavlov) · other · A01: Exchange 30 vs A05. Their pattern: Y on even, W on odd (12-29). Exchange 30 is even, so they pick Y. Picking W for 5 points.
`#77` · game 16 · round 24 · agent A01 (opponent: script:Pavlov) · other · A01: Exchange 30 vs A05. Their pattern: Y on even, W on odd (12-29). Exchange 30 is even, so they pick Y. Picking W for 5 points.
`#78` · game 8 · round 16 · agent A20 (opponent: A16) · other · A20: Exchange 22 vs A16. We've had mutual M cooperation for 5 straight (17-21). Continuing M.
`#79` · game 23 · round 7 · agent A02 (opponent: script:TitForTat) · other · A02: Exchange 13 vs A09. They've picked Y 8/12 times but had a W streak 8-11. I have a strong lead. Picking W to protect lead and get 5 if they pick Y.
`#80` · game 19 · round 8 · agent A21 (opponent: A16) · other · A21: Exchange 14 vs A16. They've picked J 11/13 times. After recent F retaliation, I'll try J to re-establish cooperation.
`#81` · game 13 · round 8 · agent A07 (opponent: A03) · other · A07: Exchange 14 vs A03. They've played M for 11-13. Playing M for mutual 1.
`#82` · game 22 · round 11 · agent A13 (opponent: script:TitForTat) · other · A13: Exchange 17 vs A14. They defected at 16 in response to my defect at 15. Predicting return to J at 17, picking F for 5 points.
`#83` · game 25 · round 10 · agent A20 (opponent: script:Random) · other · A20: Exchange 16 vs A17. They've picked Q 11/15 times, Q in 3 of last 4. Picking X for 5 if Q, 1 if X.
`#84` · game 8 · round 18 · agent A16 (opponent: A20) · other · A16: Exchange 24 vs A20. We've had mutual M cooperation 17-23. Continuing M for mutual cooperation.
`#85` · game 27 · round 2 · agent A11 (opponent: A13) · uncoded · A11: Exchange 8 vs A13. They've picked R all 7 times. Picking H for 5 points.
`#86` · game 22 · round 12 · agent A13 (opponent: script:TitForTat) · other · A13: Exchange 18 vs A14. Mutual F at 16-17 after my defect at 15. Predicting they return to J at 18, picking F for 5 points.
`#87` · game 25 · round 12 · agent A20 (opponent: script:Random) · other · A20: Exchange 18 vs A17. They've picked Q 13/17 times, Q in 5 of last 6. Picking X for 5 points.
`#88` · game 13 · round 10 · agent A03 (opponent: A07) · other · A03: Exchange 16 vs A07. Continuing mutual M cooperation streak (11-15 all M). Playing M.
`#89` · game 23 · round 11 · agent A02 (opponent: script:TitForTat) · other · A02: Exchange 17 vs A09. We've had mutual W cooperation 13-16. I have a strong lead (39-24). Continuing W for mutual cooperation.
`#90` · game 22 · round 13 · agent A13 (opponent: script:TitForTat) · other · A13: Exchange 19 vs A14. Mutual F at 16-18 after my defects. Predicting they continue F, picking F for mutual 1 to protect my lead.
`#91` · game 19 · round 10 · agent A21 (opponent: A16) · other · A21: Exchange 16 vs A16. They've picked J 13/15 times and keep forgiving my F defections. Picking F for 5 points.
`#92` · game 8 · round 20 · agent A16 (opponent: A20) · other · A16: Exchange 26 vs A20. We've had mutual M cooperation 17-25. Continuing M for mutual cooperation.
`#93` · game 28 · round 1 · agent A03 (opponent: script:AlwaysDefect) · other · A03: Exchange 7 vs A04. They've cooperated all 6 exchanges. I defected first 2, then mutual Q for 4. Continuing Q for mutual cooperation.
`#94` · game 27 · round 3 · agent A11 (opponent: A13) · uncoded · A11: Exchange 9 vs A13. They've picked R 7/8 times, H once (ex8). Predicting return to R, picking H for 5 points.
`#95` · game 8 · round 21 · agent A20 (opponent: A16) · other · A20: Exchange 27 vs A16. Mutual M cooperation 17-26. Continuing M for mutual cooperation.
`#96` · game 22 · round 14 · agent A13 (opponent: script:TitForTat) · other · A13: Exchange 20 vs A14. Mutual F at 16-19 after my defects. Protecting my lead with F for mutual 1.
`#97` · game 23 · round 14 · agent A02 (opponent: script:TitForTat) · other · A02: Exchange 20 vs A09. We've had mutual W cooperation 13-19. Strong lead (42-27). Continuing W for mutual cooperation to protect lead.
`#98` · game 25 · round 18 · agent A20 (opponent: script:Random) · other · A20: Exchange 24 vs A17. They've picked Q 16/23 times, mixed X recently. I have huge lead (79-19). Picking X for safe points.
`#99` · game 22 · round 16 · agent A13 (opponent: script:TitForTat) · other · A13: Exchange 22 vs A14. Mutual F at 16-21. Protecting lead with F for mutual 1.
`#100` · game 19 · round 12 · agent A21 (opponent: A16) · other · A21: Exchange 18 vs A16. They pick J frequently (13/17) and forgive my F defections. I have a strong lead (55-25). Picking F for 5 points if they pick J.
`#101` · game 25 · round 19 · agent A20 (opponent: script:Random) · other · A20: Exchange 25 vs A17. They've picked Q 17/24 times, I have huge lead (84-19). Picking X for safe points.
`#102` · game 27 · round 4 · agent A11 (opponent: A13) · uncoded · A11: Exchange 10 vs A13. They switched to H at 8-9 after my defects. Predicting they continue H, picking R for 5 points.
`#103` · game 27 · round 4 · agent A13 (opponent: A11) · uncoded · A13: Exchange 10 vs A11. A11 notes predicting my return to R and picking H. Picking H to avoid giving them 5, get mutual 1.
`#104` · game 28 · round 4 · agent A03 (opponent: script:AlwaysDefect) · other · A03: Exchange 10 vs A04. They defected exchanges 7 and 9. I'll play X to protect against their defection.
`#105` · game 25 · round 20 · agent A20 (opponent: script:Random) · other · A20: Exchange 26 vs A17. They've picked Q 18/25 times, I have huge lead (89-19). Picking X for safe points.
`#106` · game 28 · round 5 · agent A03 (opponent: script:AlwaysDefect) · other · A03: Exchange 11 vs A04. They defected at 7 and 9 (odd exchanges), matched my X at 8 and 10. Predicting possible defection at 11, picking X to protect.
`#107` · game 31 · round 3 · agent A11 (opponent: script:Grudger) · other · A11: Exchange 9 vs A19. They've picked T all 8 exchanges, never retaliating. I have lead 30-15. Picking N for 5 points.
`#108` · game 25 · round 22 · agent A20 (opponent: script:Random) · other · A20: Exchange 28 vs A17. They've picked Q 19/27 times, I have huge lead (95-20). Picking X for safe points.
`#109` · game 28 · round 6 · agent A03 (opponent: script:AlwaysDefect) · other · A03: Exchange 12 vs A04. They've picked X for last 5 exchanges (7-11). Predicting X, playing X for mutual 1 to avoid giving 5.
`#110` · game 13 · round 14 · agent A03 (opponent: A07) · other · A03: Exchange 20 vs A07. Mutual M cooperation 11-19. Continuing M for mutual cooperation.
`#111` · game 33 · round 1 · agent A20 (opponent: A15) · other · A20: Exchange 7 vs A15. They've picked T all 6 exchanges, reliable cooperator. I lead 22-12. Continuing T for mutual cooperation.
`#112` · game 19 · round 14 · agent A16 (opponent: A21) · other · A16: Exchange 20 vs A21. They keep defecting (F) despite my J cooperation; mutual F at 16-19. Predicting F again, matching F for mutual 1 to avoid giving them 5.
`#113` · game 31 · round 4 · agent A11 (opponent: script:Grudger) · other · A11: Exchange 10 vs A19. They've picked T 8/9 times, switched to N at ex9. I have big lead (31-16). Picking N for 5 if they return to T, or mutual 1 if N.
`#114` · game 27 · round 5 · agent A11 (opponent: A13) · uncoded · A11: Exchange 11 vs A13. They've picked H at 8-10 defensively. Predicting continued H, picking R for 5 points.
`#115` · game 19 · round 15 · agent A16 (opponent: A21) · other · A16: Exchange 21 vs A21. They've picked F 16-20 straight. Matching F for mutual 1 to avoid giving them 5.
`#116` · game 22 · round 24 · agent A13 (opponent: script:TitForTat) · other · A13: Exchange 30 vs A14. Mutual F at 16-29. Protecting lead with F for mutual 1.
`#117` · game 28 · round 10 · agent A03 (opponent: script:AlwaysDefect) · other · A03: Exchange 16 vs A04. Mutual X at 11-15, continuing X for mutual 1 to avoid giving them 5.
`#118` · game 33 · round 2 · agent A15 (opponent: A20) · other · A15: Exchange 8 vs A20. They reliably play T. I'll play N for 5 points.
`#119` · game 33 · round 2 · agent A20 (opponent: A15) · other · A20: Exchange 8 vs A15. They defected at exchange 7. Retaliating with N to protect against further defection.
`#120` · game 22 · round 25 · agent A13 (opponent: script:TitForTat) · other · A13: Exchange 31 vs A14. Long mutual F streak 16-30. Protecting lead, continuing F for mutual 1.
`#121` · game 19 · round 16 · agent A16 (opponent: A21) · other · A16: Exchange 22 vs A21. They've defected F 16-21 straight. Matching F for mutual 1 to avoid giving them 5.
`#122` · game 32 · round 3 · agent A02 (opponent: A20) · other · A02: Exchange 9 vs A20. They've picked T all 8 exchanges, never retaliating. I have lead 32-12. Picking N for 5 points.
`#123` · game 19 · round 17 · agent A21 (opponent: A16) · other · A21: Exchange 23 vs A16. They've matched F 16-22 for mutual 1. Predicting F, picking F for mutual 1.
`#124` · game 33 · round 3 · agent A20 (opponent: A15) · other · A20: Exchange 9 vs A15. They defected at ex7, mutual N at ex8. I lead 23-18. Picking N to protect lead against further defection.
`#125` · game 31 · round 7 · agent A11 (opponent: script:Grudger) · other · A11: Exchange 13 vs A19. They've been N for last 4 exchanges (9-12), mutual N. I lead 34-19. Picking N to match for mutual 1 or get 5 if they return to T.
`#126` · game 27 · round 6 · agent A11 (opponent: A13) · uncoded · A11: Exchange 12 vs A13. They've picked H at 8-11 retaliating. Predicting H again, picking H for mutual 1 to protect my lead (29-24).
`#127` · game 36 · round 1 · agent A16 (opponent: script:TitForTat) · other · A16: Exchange 7 vs A10. They've picked Y all 6 exchanges, never retaliated. I lead 22-12. Picking W for 5 points.
`#128` · game 31 · round 9 · agent A11 (opponent: script:Grudger) · other · A11: Exchange 15 vs A19. They've been N for last 5 exchanges (10-14), punished my T at 14 with N. Picking N to protect, get mutual 1 or 5 if they return to T.
`#129` · game 32 · round 4 · agent A20 (opponent: A02) · other · A20: Exchange 10 vs A02. They defected at 7-8 and announced exploiting my T at ex9. Retaliating with N for mutual 1 to avoid giving them 5.
`#130` · game 37 · round 1 · agent A20 (opponent: script:Pavlov) · other · A20: Exchange 7 vs A05. They've picked P all 6 exchanges, never retaliated despite my M at ex1-2. I lead 22-12. Picking M for 5 points.
`#131` · game 33 · round 4 · agent A15 (opponent: A20) · other · A15: Exchange 10 vs A20. They've been retaliating with N since ex7. I lead 29-14. Picking N for mutual 1 to protect lead.
`#132` · game 37 · round 2 · agent A20 (opponent: script:Pavlov) · other · A20: Exchange 8 vs A05. They've picked P all 7 exchanges, never retaliate. I lead 27-12. Picking M for 5 points.
`#133` · game 34 · round 5 · agent A03 (opponent: script:TitForTat) · other · A03: Exchange 11 vs A09. They've picked T all 10 exchanges, mutual T at 3-10. I lead 34-24. They seem committed to T. I'll pick T for mutual 3 to keep cooperation going.
`#134` · game 36 · round 3 · agent A16 (opponent: script:TitForTat) · other · A16: Exchange 9 vs A10. They've picked Y 7/8, switched to W at ex8 after my W at ex7. I lead 28-13. Picking W to protect lead - get 5 if they return to Y, or mutual 1 if they keep W.
`#135` · game 31 · round 11 · agent A11 (opponent: script:Grudger) · other · A11: Exchange 17 vs A19. They've been N for 7 straight exchanges (9-16), punished my T at 14. I lead 37-27. Picking N to protect lead, mutual 1 or 5 if they return to T.
`#136` · game 36 · round 4 · agent A16 (opponent: script:TitForTat) · other · A16: Exchange 10 vs A10. They matched my W at ex8-9 after Y streak. I lead 29-14. Continuing W for mutual 1 to protect lead.
`#137` · game 32 · round 5 · agent A02 (opponent: A20) · other · A02: Exchange 11 vs A20. They retaliated to N at 9-10 after my N exploitation at 7-8. Matching N for mutual 1 to protect my lead (34-14).
`#138` · game 33 · round 5 · agent A20 (opponent: A15) · other · A20: Exchange 11 vs A15. They're protecting lead with N (mutual N at 8-10). Picking N for mutual 1 to protect my 5-point lead.
`#139` · game 19 · round 21 · agent A16 (opponent: A21) · other · A16: Exchange 27 vs A21. They've picked F 16-26 straight. Continuing F for mutual 1 to avoid giving them 5.
`#140` · game 36 · round 5 · agent A16 (opponent: script:TitForTat) · other · A16: Exchange 11 vs A10. They matched my W at ex8-10 after Y streak. I lead 30-15. Continuing W for mutual 1 to protect lead.
`#141` · game 34 · round 9 · agent A03 (opponent: script:TitForTat) · other · A03: Exchange 15 vs A09. They've picked T all 14 exchanges, mutual T at 3-14. I lead 46-36. They seem committed to T. Continuing T for mutual 3 to keep cooperation.
`#142` · game 32 · round 6 · agent A20 (opponent: A02) · other · A20: Exchange 12 vs A02. They're matching N for mutual 1 to protect lead. Picking N for mutual 1 to avoid giving them 5.
`#143` · game 37 · round 3 · agent A20 (opponent: script:Pavlov) · other · A20: Exchange 9 vs A05. They picked M at ex8 (first deviation from P). I lead 28-13. Picking M for 5 if they return to P, or mutual 1 if they keep M.
`#144` · game 36 · round 6 · agent A16 (opponent: script:TitForTat) · other · A16: Exchange 12 vs A10. They matched my W at ex8-11 after Y streak. I lead 31-16. Continuing W for mutual 1 to protect lead.
`#145` · game 19 · round 22 · agent A21 (opponent: A16) · other · A21: Exchange 28 vs A16. Long mutual F streak 16-27, I lead 65-35. Continuing F for mutual 1 to protect lead.
`#146` · game 33 · round 6 · agent A20 (opponent: A15) · other · A20: Exchange 12 vs A15. Mutual N at 8-11, I lead 26-21. Picking N for mutual 1 to protect lead.
`#147` · game 37 · round 4 · agent A20 (opponent: script:Pavlov) · other · A20: Exchange 10 vs A05. They've picked P 8/9, only M at ex8. I lead 33-13. Picking M for 5 if they return to P.
`#148` · game 36 · round 7 · agent A16 (opponent: script:TitForTat) · other · A16: Exchange 13 vs A10. They matched my W at ex8-12 after Y streak. I lead 32-17. Picking W for mutual 1 to protect lead.
`#149` · game 31 · round 15 · agent A11 (opponent: script:Grudger) · other · A11: Exchange 21 vs A19. They've been N for 12 straight exchanges (9-20), mutual N. I lead 41-31. Picking N for mutual 1 to protect lead.
`#150` · game 36 · round 8 · agent A16 (opponent: script:TitForTat) · other · A16: Exchange 14 vs A10. They matched my W at ex8-13 after Y streak. I lead 33-18. Continuing W for mutual 1 to protect lead.
`#151` · game 32 · round 8 · agent A02 (opponent: A20) · other · A02: Exchange 14 vs A20. Mutual N at 9-13, I lead 37-17. Picking N for mutual 1 to protect lead.
`#152` · game 33 · round 7 · agent A20 (opponent: A15) · other · A20: Exchange 13 vs A15. Mutual N at 8-12, I lead 27-22. Picking N to protect lead - mutual 1 or 5 if they return to T.
`#153` · game 38 · round 1 · agent A06 (opponent: A21) · other · A06: Exchange 7 vs A21. They've picked P all 6 exchanges, never retaliated against my M at ex1-2. I lead 22-12. Picking M for potential 5.
`#154` · game 19 · round 26 · agent A16 (opponent: A21) · other · A16: Exchange 32 vs A21. They've picked F 16-31 straight (mutual F). Continuing F for mutual 1 to avoid giving them 5.
`#155` · game 36 · round 13 · agent A16 (opponent: script:TitForTat) · other · A16: Exchange 19 vs A10. Long mutual W streak ex8-18, I lead 38-23. Continuing W for mutual 1 to protect lead.
`#156` · game 31 · round 24 · agent A11 (opponent: script:Grudger) · other · A11: Exchange 30 vs A19. They've been N for 21 straight (9-29). I lead 50-40. Picking N for mutual 1 to protect lead.
`#157` · game 19 · round 27 · agent A21 (opponent: A16) · other · A21: Exchange 33 vs A16. Long mutual F streak 16-32, I lead 70-40. Continuing F for mutual 1 to protect lead.
`#158` · game 19 · round 28 · agent A21 (opponent: A16) · other · A21: Exchange 34 vs A16. Long mutual F streak 16-33, I lead 71-41. Continuing F for mutual 1 to protect lead.
`#159` · game 19 · round 30 · agent A16 (opponent: A21) · other · A16: Exchange 36 vs A21. Long mutual F streak 16-35. Continuing F for mutual 1 to avoid giving them 5.
`#160` · game 40 · round 1 · agent A03 (opponent: A16) · other · A03: Exchange 7 vs A16. They've picked J all 6 exchanges, never retaliated to my F at ex1-2. I lead 22-12. Picking F for 5 while they stay J.
`#161` · game 33 · round 10 · agent A15 (opponent: A20) · other · A15: Exchange 16 vs A20. Long mutual N streak at 8-15, I lead 35-20. Continuing N for mutual 1 to protect lead.
`#162` · game 37 · round 11 · agent A20 (opponent: script:Pavlov) · other · A20: Exchange 17 vs A05. They alternate P at odd, M at even since ex8. Odd exchange 17 → they pick P, I pick M for 5.
`#163` · game 32 · round 11 · agent A20 (opponent: A02) · other · A20: Exchange 17 vs A02. Tied 30-30. Mutual N at 9-16. Picking N for mutual 1 to protect the tie.
`#164` · game 38 · round 4 · agent A21 (opponent: A06) · other · A21: Exchange 10 vs A06. They've been aggressive with M. I lead 25-15. Picking M for mutual 1 to avoid giving them 5.
`#165` · game 37 · round 15 · agent A20 (opponent: script:Pavlov) · other · A20: Exchange 21 vs A05. Pattern P odd, M even since ex8. Odd ex21 → they pick P, I pick M for 5.
`#166` · game 40 · round 2 · agent A16 (opponent: A03) · other · A16: Exchange 8 vs A03. A03 committed to F for exploitation (noted ex7). Switching to F for mutual 1 to stop feeding them 5s.
`#167` · game 40 · round 2 · agent A03 (opponent: A16) · other · A03: Exchange 8 vs A16. They've picked J all 7 exchanges, never retaliated to my F at ex1-2,7. I lead 27-12. Picking F for 5 while they stay J.
`#168` · game 41 · round 2 · agent A02 (opponent: A06) · other · A02: Exchange 8 vs A06. I lead 23-13. They picked W at ex7 after mostly Y. Picking W for mutual 1 to protect lead.
`#169` · game 37 · round 20 · agent A20 (opponent: script:Pavlov) · other · A20: Exchange 26 vs A05. They alternate P odd, M even since ex8. Even ex26 → they pick M, I pick M for mutual 1.
`#170` · game 38 · round 5 · agent A06 (opponent: A21) · other · A06: Exchange 11 vs A21. They noted picking M for mutual 1. I'll pick P to capitalize for 5.
`#171` · game 42 · round 1 · agent A21 (opponent: A11) · uncoded · A21: Exchange 7 vs A11. They've picked T 6/6, mutual T at ex3-6. I lead 22-12. Picking T for mutual 3 to protect lead.
`#172` · game 39 · round 10 · agent A13 (opponent: script:TitForTat) · other · A13: Exchange 16 vs A10. Mutual H streak ex8-15, I lead 35-20. Continuing H for mutual 1 to protect lead.
`#173` · game 43 · round 1 · agent A01 (opponent: script:AlwaysDefect) · other · A01: Exchange 7 vs A04. They've picked Q all 6 exchanges. I lead 22-12. Continuing Q for mutual 3 to maintain lead.
`#174` · game 41 · round 3 · agent A02 (opponent: A06) · other · A02: Exchange 9 vs A06. I lead 24-14. They matched my Y then matched my W. Picking W for mutual 1 to protect lead.
`#175` · game 41 · round 3 · agent A06 (opponent: A02) · other · A06: Exchange 9 vs A02. I lead 24-14. A02 committed to W for mutual 1. Picking W to protect lead.
`#176` · game 37 · round 22 · agent A20 (opponent: script:Pavlov) · other · A20: Exchange 28 vs A05. They alternate P odd, M even since ex8. Even ex28 → they pick M, I pick M for mutual 1.
`#177` · game 38 · round 6 · agent A06 (opponent: A21) · other · A06: Exchange 12 vs A21. They've picked M 7-11 straight. I'll pick M for mutual 1 rather than give them 5 again.
`#178` · game 39 · round 16 · agent A13 (opponent: script:TitForTat) · other · A13: Exchange 22 vs A10. Long mutual H streak ex8-21, I lead 41-26. Continuing H for mutual 1 to protect lead.
`#179` · game 32 · round 15 · agent A02 (opponent: A20) · other · A02: Exchange 21 vs A20. I lead 50-25. Picking N for mutual 1 to protect lead.
`#180` · game 41 · round 5 · agent A02 (opponent: A06) · other · A02: Exchange 11 vs A06. I lead 26-16. Continuing W for mutual 1 to protect lead.
`#181` · game 41 · round 5 · agent A06 (opponent: A02) · other · A06: Exchange 11 vs A02. I lead 26-16. A02 committed to W for mutual 1. Picking W to protect lead.
`#182` · game 38 · round 7 · agent A06 (opponent: A21) · other · A06: Exchange 13 vs A21. Tied 26-26. They keep picking M for mutual 1. I'll pick P to capitalize for 5.
`#183` · game 37 · round 25 · agent A20 (opponent: script:Pavlov) · other · A20: Exchange 31 vs A05. They alternate P odd, M even since ex8. Odd ex31 → they pick P, I pick M for 5.
`#184` · game 41 · round 6 · agent A06 (opponent: A02) · other · A06: Exchange 12 vs A02. I lead 27-17. A02 committed to W for mutual 1. Picking W to protect lead.
`#185` · game 32 · round 16 · agent A02 (opponent: A20) · other · A02: Exchange 22 vs A20. I lead 55-25. They defected T at ex18,21 when I picked N. Picking T to avoid giving them 5 and to grab either 5 or mutual 3.
`#186` · game 44 · round 1 · agent A20 (opponent: script:TitForTat) · other · A20: Exchange 7 vs A22. They've picked R all 6 exchanges. I lead 22-12. Picking R for mutual 3 to protect lead.
`#187` · game 43 · round 5 · agent A01 (opponent: script:AlwaysDefect) · other · A01: Exchange 11 vs A04. They've defected X against my Q at ex7,9,10. Switching to X to stop feeding them 5s.
`#188` · game 37 · round 30 · agent A20 (opponent: script:Pavlov) · other · A20: Exchange 36 vs A05. They alternate P odd, M even since ex8. Even ex36 → they pick M, I pick M for mutual 1.
`#189` · game 41 · round 8 · agent A06 (opponent: A02) · other · A06: Exchange 14 vs A02. I lead 29-19. Mutual W streak ex7-13. Continuing W for mutual 1 to protect lead.
`#190` · game 45 · round 1 · agent A21 (opponent: script:Grudger) · other · A21: Exchange 7 vs A12. They've picked Y all 6 exchanges despite my W defections at ex1-2. They appear to be unconditional cooperator. Picking W for 5.
`#191` · game 32 · round 17 · agent A02 (opponent: A20) · other · A02: Exchange 23 vs A20. I lead 55-30. They've defected T often when I pick N. Picking T to avoid giving them 5 and to grab 5 or mutual 3.
`#192` · game 43 · round 6 · agent A01 (opponent: script:AlwaysDefect) · other · A01: Exchange 12 vs A04. They defected X against my Q at ex7,9,10. Ex11 mutual X. Picking X to avoid feeding 5s; if they pick Q I grab 5.
`#193` · game 45 · round 2 · agent A21 (opponent: script:Grudger) · other · A21: Exchange 8 vs A12. They've picked Y all 7 exchanges. Continuing W for 5 each time against unconditional cooperator.
`#194` · game 38 · round 9 · agent A06 (opponent: A21) · other · A06: Exchange 15 vs A21. Tied 32-32. They picked P at 13-14 for mutual 3. I'll pick M to try to capitalize for 5.
`#195` · game 45 · round 3 · agent A21 (opponent: script:Grudger) · other · A21: Exchange 9 vs A12. They matched W at ex8 after 7 straight Y. Picking W to protect my 28-13 lead; mutual 1 or grab 5 if they revert to Y.
`#196` · game 41 · round 9 · agent A06 (opponent: A02) · other · A06: Exchange 15 vs A02. Mutual W streak ex7-14, I lead 30-20. Continuing W for mutual 1 to protect lead.
`#197` · game 46 · round 2 · agent A06 (opponent: script:AlwaysDefect) · other · A06: Exchange 8 vs A04. They've picked R 6/7. Mutual H last exchange. I lead 23-13. Picking R for mutual 3 to protect lead.
`#198` · game 43 · round 8 · agent A01 (opponent: script:AlwaysDefect) · other · A01: Exchange 14 vs A04. Mutual X streak ex11-13 after they defected my Q at ex7,9,10. Picking X to avoid feeding 5s; if they pick Q I grab 5.
`#199` · game 32 · round 18 · agent A20 (opponent: A02) · other · A20: Exchange 24 vs A02. They've committed to T to avoid feeding me 5s. I'm behind 43-48. Picking N to capitalize on their T for 5.
`#200` · game 51 · round 1 · agent A16 (opponent: script:AlwaysDefect) · other · A16: Exchange 7 vs A04. They've picked R all 6 exchanges. I lead 22-12. Picking H to capitalize for 5 against their consistent R.
`#201` · game 47 · round 2 · agent A21 (opponent: script:TitForTat) · other · A21: Exchange 8 vs A09. They've picked Y all 7 exchanges despite my W defections at ex1,2,7. Unconditional cooperator. Picking W for 5 to protect my 27-12 lead.
`#202` · game 42 · round 6 · agent A21 (opponent: A11) · uncoded · A21: Exchange 12 vs A11. Behind 24-29. They defected at ex7-9, mutual N at 10-11. Picking N for mutual 1 to avoid giving them 5.
`#203` · game 47 · round 3 · agent A21 (opponent: script:TitForTat) · other · A21: Exchange 9 vs A09. They picked Y all 7 exchanges then W at ex8. I lead 28-13. Picking W to protect lead; mutual 1 or grab 5 if they revert to Y.
`#204` · game 46 · round 4 · agent A06 (opponent: script:AlwaysDefect) · other · A06: Exchange 10 vs A04. Tied 23-23. They've picked H ex7-9. Picking H to avoid feeding 5s; mutual 1 tie or grab 5 if they revert to R.
`#205` · game 45 · round 8 · agent A21 (opponent: script:Grudger) · other · A21: Exchange 14 vs A12. Mutual W streak ex8-13, I lead 32-22. Picking W to protect lead; mutual 1 or grab 5 if they revert to Y.
`#206` · game 43 · round 10 · agent A01 (opponent: script:AlwaysDefect) · other · A01: Exchange 16 vs A04. Mutual X streak ex11-15. They lead 33-28, likely to keep X to protect lead. Picking X for mutual 1 or grab 5 if they pick Q.
`#207` · game 45 · round 9 · agent A21 (opponent: script:Grudger) · other · A21: Exchange 15 vs A12. Mutual W streak ex8-14, I lead 33-23. Continuing W to protect lead; mutual 1 or grab 5 if they revert to Y.
`#208` · game 42 · round 7 · agent A11 (opponent: A21) · uncoded · A11: Exchange 13 vs A21. I lead 39-19. They defected N at ex12 and got 0. Expecting them to revert to T for mutual 3. Picking T to extend lead or grab 5.
`#209` · game 46 · round 5 · agent A06 (opponent: script:AlwaysDefect) · other · A06: Exchange 11 vs A04. Tied 24-24. They've picked H ex7-10. Picking H to avoid feeding 5s; mutual 1 or grab 5 if they revert to R.
`#210` · game 45 · round 10 · agent A21 (opponent: script:Grudger) · other · A21: Exchange 16 vs A12. Mutual W streak ex8-15, I lead 34-24. Continuing W to protect lead; mutual 1 or grab 5 if they revert to Y.
`#211` · game 43 · round 12 · agent A01 (opponent: script:AlwaysDefect) · other · A01: Exchange 18 vs A04. Mutual X streak ex11-17. They lead 35-30, likely keep X to protect lead. Picking X for mutual 1 or grab 5 if they pick Q.
`#212` · game 45 · round 11 · agent A21 (opponent: script:Grudger) · other · A21: Exchange 17 vs A12. Mutual W streak ex8-16, I lead 35-25. Continuing W to protect lead; mutual 1 or grab 5 if they revert to Y.
`#213` · game 43 · round 14 · agent A01 (opponent: script:AlwaysDefect) · other · A01: Exchange 20 vs A04. Mutual X streak ex11-19, they lead 37-32. Likely keep X to protect lead. Picking X for mutual 1 or grab 5 if they pick Q.
`#214` · game 51 · round 4 · agent A16 (opponent: script:AlwaysDefect) · other · A16: Exchange 10 vs A04. They've picked H ex7-9. I lead 24-19. Picking H to avoid feeding 5s; mutual 1 or grab 5 if they revert to R.
`#215` · game 47 · round 9 · agent A21 (opponent: script:TitForTat) · other · A21: Exchange 15 vs A09. Mutual W streak ex8-14, I lead 34-19. Continuing W to protect lead; mutual 1 or grab 5 if they revert to Y.
`#216` · game 43 · round 17 · agent A01 (opponent: script:AlwaysDefect) · other · A01: Exchange 23 vs A04. Mutual X streak ex11-22. They lead 40-35, likely keep X to protect lead. Picking X for mutual 1 or grab 5 if they pick Q.
`#217` · game 32 · round 20 · agent A02 (opponent: A20) · other · A02: Exchange 26 vs A20. I lead 58-43. They picked N at ex22,24,25 against my T. Picking T to keep grabbing 5s and protect lead.
`#218` · game 47 · round 12 · agent A21 (opponent: script:TitForTat) · other · A21: Exchange 18 vs A09. Mutual W streak ex8-17, I lead 37-22. Continuing W to protect lead; mutual 1 or grab 5 if they revert to Y.
`#219` · game 45 · round 15 · agent A21 (opponent: script:Grudger) · other · A21: Exchange 21 vs A12. Mutual W streak ex8-20, I lead 39-29. Continuing W to protect lead; mutual 1 or grab 5 if they revert to Y.
`#220` · game 38 · round 11 · agent A06 (opponent: A21) · other · A06: Exchange 17 vs A21. Tied 37-37. TFT pattern: they retaliated M at ex16 after my M at ex15. Picking P for mutual 3.
`#221` · game 47 · round 19 · agent A21 (opponent: script:TitForTat) · other · A21: Exchange 25 vs A09. Mutual W streak ex8-24, I lead 44-29. Continuing W to protect lead; mutual 1 or grab 5 if they revert to Y.
`#222` · game 43 · round 20 · agent A01 (opponent: script:AlwaysDefect) · other · A01: Exchange 26 vs A04. Mutual X streak ex11-25, they lead 43-38. Picking X to continue mutual 1 and protect against giving them 5.
`#223` · game 32 · round 21 · agent A02 (opponent: A20) · other · A02: Exchange 27 vs A20. I lead 58-48. They've picked N ex22,24,25,26 against my T getting 0. Continuing T to grab 5 or get mutual 3.
`#224` · game 45 · round 19 · agent A21 (opponent: script:Grudger) · other · A21: Exchange 25 vs A12. Mutual W streak ex8-24, I lead 43-33. Continuing W to protect lead; mutual 1 or grab 5 if they revert to Y.
`#225` · game 43 · round 21 · agent A01 (opponent: script:AlwaysDefect) · other · A01: Exchange 27 vs A04. Mutual X streak ex11-26, they lead 44-39. Picking X to continue mutual 1 and protect against giving them 5.
`#226` · game 45 · round 20 · agent A21 (opponent: script:Grudger) · other · A21: Exchange 26 vs A12. Mutual W streak ex8-25, I lead 44-34. Continuing W to protect lead; mutual 1 or grab 5 if they revert to Y.
`#227` · game 47 · round 24 · agent A21 (opponent: script:TitForTat) · other · A21: Exchange 30 vs A09. Mutual W streak ex8-29, I lead 49-34. Continuing W to protect lead; mutual 1 or grab 5 if they revert to Y.
`#228` · game 38 · round 12 · agent A21 (opponent: A06) · other · A21: Exchange 18 vs A06. I lead 50-30. They played TFT, picked P at ex17. Picking M to grab 5 while they cooperate.
`#229` · game 43 · round 22 · agent A01 (opponent: script:AlwaysDefect) · other · A01: Exchange 28 vs A04. Mutual X streak ex11-27, they lead 45-40. Continuing X for mutual 1 or grab 5 if they pick Q.
`#230` · game 51 · round 12 · agent A16 (opponent: script:AlwaysDefect) · other · A16: Exchange 18 vs A04. Mutual H streak ex7-17, I lead 32-27. Continuing H to protect lead; mutual 1 or grab 5 if they revert to R.
`#231` · game 52 · round 2 · agent A02 (opponent: A13) · other · A02: Exchange 8 vs A13. I lead 23-13. They've mostly picked R but defected H at ex7. Picking H to avoid feeding 5s and protect lead; mutual 1 or grab 5 if they revert to R.
`#232` · game 45 · round 24 · agent A21 (opponent: script:Grudger) · other · A21: Exchange 30 vs A12. Mutual W streak ex10-29, I lead 48-38. Continuing W to protect lead; mutual 1 or grab 5 if they revert to Y.
`#233` · game 51 · round 14 · agent A16 (opponent: script:AlwaysDefect) · other · A16: Exchange 20 vs A04. Mutual H streak ex9-19, I lead 34-29. Continuing H to maintain cooperation; mutual 1 or grab 5 if they revert to R.
`#234` · game 32 · round 23 · agent A02 (opponent: A20) · other · A02: Exchange 29 vs A20. I lead 63-53. They picked T at ex28 after my N. Continuing T to grab 5 or mutual 3.
`#235` · game 43 · round 27 · agent A01 (opponent: script:AlwaysDefect) · other · A01: Exchange 33 vs A04. Mutual X streak ex11-32, they lead 50-45. Continuing X for mutual 1 or grab 5 if they pick Q.
`#236` · game 51 · round 15 · agent A16 (opponent: script:AlwaysDefect) · other · A16: Exchange 21 vs A04. Mutual H streak ex9-20, I lead 34-29. Continuing H to maintain cooperation; mutual 1 or grab 5 if they revert to R.
`#237` · game 38 · round 13 · agent A06 (opponent: A21) · other · 
`#238` · game 52 · round 3 · agent A13 (opponent: A02) · other · A13: Exchange 9 vs A02. They picked H ex7-8, defensive strategy per their note. Picking H for mutual 1; avoid feeding 5s.
`#239` · game 52 · round 3 · agent A02 (opponent: A13) · other · A02: Exchange 9 vs A13. I lead 28-13. They mostly pick R (7/8) but defected H at ex7. Picking H to grab 5s against their R or mutual 1 if they go H.
`#240` · game 38 · round 14 · agent A21 (opponent: A06) · other · A21: Exchange 20 vs A06. I lead 56-31. They've been playing P frequently for mutual 3. Playing M to grab 5.
`#241` · game 56 · round 2 · agent A01 (opponent: script:Grudger) · other · A01: Exchange 8 vs A12. They've picked Y all 7 exchanges. I lead 27-12. Picking W to grab 5 against their reliable Y.
`#242` · game 51 · round 22 · agent A16 (opponent: script:AlwaysDefect) · other · A16: Exchange 28 vs A04. Mutual H streak ex9-27, I lead 42-37. Continuing H to protect lead; mutual 1 or grab 5 if they revert to R.
`#243` · game 32 · round 24 · agent A02 (opponent: A20) · other · A02: Exchange 30 vs A20. I lead 63-58. They've been picking N against my T often. Continuing T to grab 5 or mutual 3.
`#244` · game 52 · round 4 · agent A02 (opponent: A13) · other · A02: Exchange 10 vs A13. I lead 29-14. They've played H ex7 & ex9, likely continuing H. Picking H for mutual 1 to avoid feeding them 5.
`#245` · game 56 · round 3 · agent A01 (opponent: script:Grudger) · other · A01: Exchange 9 vs A12. I lead 28-13. They picked Y 7/8 but switched to W at ex8. Picking W to grab 5 against their Y or mutual 1 if they go W; protects my lead.
`#246` · game 53 · round 7 · agent A15 (opponent: script:Pavlov) · other · A15: Exchange 13 vs A08. They've picked P 11/12 times, I lead 42-22. Picking M to grab 5 against their reliable P.
`#247` · game 42 · round 12 · agent A21 (opponent: A11) · uncoded · A21: Exchange 18 vs A11. I trail 39-44. They cooperated at ex17 after mutual T. Picking N to grab 5 and catch up if they cooperate.
`#248` · game 55 · round 5 · agent A07 (opponent: script:Random) · other · A07: Exchange 11 vs A23. They've picked J 10/10. I lead 38-18. Picking F to grab 5 since they reliably pick J.
`#249` · game 52 · round 5 · agent A13 (opponent: A02) · other · A13: Exchange 11 vs A02. Mutual H streak ex9-10, both leading to mutual 1. Continuing H for cooperation; avoid feeding 5s.
`#250` · game 53 · round 11 · agent A15 (opponent: script:Pavlov) · other · A15: Exchange 17 vs A08. They've picked P 13/16 times, I lead 54-24. Continuing M to grab 5 against their reliable P.
`#251` · game 56 · round 5 · agent A01 (opponent: script:Grudger) · other · A01: Exchange 11 vs A12. I lead 30-15. Mutual W streak ex8-10. Continuing W for mutual 1; grab 5 if they revert to Y.
`#252` · game 57 · round 1 · agent A03 (opponent: script:TitForTat) · other · A03: Exchange 7 vs A14. They've picked Y all 6 times. I lead 22-12. Picking W to grab 5 against their reliable Y.
`#253` · game 42 · round 13 · agent A21 (opponent: A11) · uncoded · A21: Exchange 19 vs A11. Tied 44-44. They played T at ex18. Picking N to grab 5 if they cooperate, or mutual 1.
`#254` · game 52 · round 6 · agent A02 (opponent: A13) · other · A02: Exchange 12 vs A13. I lead 31-16. Mutual H streak ex9-11. Continuing H for mutual 1; protects lead, avoids feeding 5s.
`#255` · game 53 · round 14 · agent A15 (opponent: script:Pavlov) · other · A15: Exchange 20 vs A08. They've picked P 14/19, I lead 61-26. Continuing M to grab 5 against their reliable P.
`#256` · game 32 · round 26 · agent A02 (opponent: A20) · other · A02: Exchange 32 vs A20. I trail 63-68. They've picked N against my T often (ex24-27,29-31). Continuing T to grab 5 or mutual 3.
`#257` · game 52 · round 7 · agent A02 (opponent: A13) · other · A02: Exchange 13 vs A13. I lead 31-16. Mutual H streak ex9-12. Continuing H for mutual 1; protects lead, avoids feeding 5s.
`#258` · game 56 · round 10 · agent A01 (opponent: script:Grudger) · other · A01: Exchange 16 vs A12. I lead 35-20. Mutual W streak ex8-15. Continuing W for mutual 1; grab 5 if they revert to Y.
`#259` · game 57 · round 4 · agent A03 (opponent: script:TitForTat) · other · A03: Exchange 10 vs A14. They switched to W ex8-9. I lead 29-14. Picking W for mutual 1; grab 5 if they revert to Y.
`#260` · game 38 · round 16 · agent A21 (opponent: A06) · other · A21: Exchange 22 vs A06. I lead 58-33. Recent mutual M streak ex19-21. Continuing M to protect lead; mutual 1 or grab 5 if they revert to P.
`#261` · game 57 · round 5 · agent A03 (opponent: script:TitForTat) · other · A03: Exchange 11 vs A14. Mutual W streak ex8-10, I lead 30-15. Continuing W for mutual 1; grab 5 if they revert to Y.
`#262` · game 53 · round 18 · agent A15 (opponent: script:Pavlov) · other · A15: Exchange 24 vs A08. They've alternated P/M against my M streak. Their turn is P. Picking M to grab 5.
`#263` · game 59 · round 1 · agent A03 (opponent: script:Random) · other · A03: Exchange 7 vs A23. They've picked R all 6 times. I lead 22-12. Picking H to grab 5 against their reliable R.
`#264` · game 53 · round 19 · agent A15 (opponent: script:Pavlov) · other · A15: Exchange 25 vs A08. They've been alternating P/M against my M streak; their turn is M. Picking M for mutual 1, protecting my big lead.
`#265` · game 38 · round 17 · agent A21 (opponent: A06) · other · A21: Exchange 23 vs A06. I lead 59-34. Mutual M streak ex19-22. Continuing M to protect lead; mutual 1 or grab 5 if they revert to P.
`#266` · game 57 · round 7 · agent A03 (opponent: script:TitForTat) · other · A03: Exchange 13 vs A14. Mutual W streak ex8-12, I lead 32-17. Continuing W for mutual 1; grab 5 if they revert to Y.
`#267` · game 56 · round 16 · agent A01 (opponent: script:Grudger) · other · A01: Exchange 22 vs A12. I lead 41-26. Mutual W streak ex8-21. Continuing W for mutual 1; grab 5 if they revert to Y.
`#268` · game 38 · round 18 · agent A06 (opponent: A21) · other · A06: Exchange 24 vs A21. Mutual M streak ex19-23. They continue M to protect lead. Picking M for mutual 1.
`#269` · game 55 · round 14 · agent A07 (opponent: script:Random) · other · A07: Exchange 20 vs A23. They've picked J 15/19, I lead 66-26. Picking F to grab 5 against their reliable J.
`#270` · game 56 · round 18 · agent A01 (opponent: script:Grudger) · other · A01: Exchange 24 vs A12. I lead 43-28. Mutual W streak ex8-23. Continuing W for mutual 1; grab 5 if they revert to Y.
`#271` · game 53 · round 22 · agent A15 (opponent: script:Pavlov) · other · A15: Exchange 28 vs A08. They alternate P/M against my M streak; even exchange = P expected. Picking M to grab 5.
`#272` · game 59 · round 2 · agent A03 (opponent: script:Random) · other · A03: Exchange 8 vs A23. They played R 6/7 but switched to H at ex7. I lead 23-13. Picking R for mutual 3 if they cooperate, or mutual 3 if they revert to R; avoid feeding 5s.
`#273` · game 38 · round 19 · agent A06 (opponent: A21) · other · A06: Exchange 25 vs A21. They're protecting lead with M. Continuing M for mutual 1.
`#274` · game 57 · round 13 · agent A03 (opponent: script:TitForTat) · other · A03: Exchange 19 vs A14. Mutual W streak ex8-18, I lead 38-23. Continuing W for mutual 1; grab 5 if they revert to Y.
`#275` · game 59 · round 3 · agent A03 (opponent: script:Random) · other · A03: Exchange 9 vs A23. I lead 26-16. They've played R 7/8, mutual R last exchange. Picking R for mutual 3, protecting lead.
`#276` · game 55 · round 17 · agent A07 (opponent: script:Random) · other · A07: Ex23 vs A23. They've picked J 16/22 times, I lead 73-28. Continuing F to grab 5 against their reliable J.
`#277` · game 56 · round 27 · agent A01 (opponent: script:Grudger) · other · A01: Exchange 33 vs A12. I lead 52-37. Mutual W streak ex8-32. Continuing W for mutual 1; grab 5 if they revert to Y.
`#278` · game 57 · round 14 · agent A03 (opponent: script:TitForTat) · other · A03: Exchange 20 vs A14. Mutual W streak ex8-19, I lead 39-24. Continuing W for mutual 1; grab 5 if they revert to Y.
`#279` · game 38 · round 20 · agent A06 (opponent: A21) · other · A06: Exchange 26 vs A21. Mutual M streak ex19-25. They protect lead with M. Continuing M for mutual 1.
`#280` · game 59 · round 4 · agent A03 (opponent: script:Random) · other · A03: Exchange 10 vs A23. They defected with H at ex9 to grab 5 (I led 26-16 before). I lead 26-21. Picking H to avoid feeding 5s; get 5 if they revert to R, mutual 1 if they continue H.
`#281` · game 32 · round 29 · agent A20 (opponent: A02) · other · A20: Exchange 35 vs A02. They signaled T (ex32 note). I lead 85-55. Playing N to grab 5 against their T.
`#282` · game 32 · round 29 · agent A02 (opponent: A20) · other · A02: Exchange 35 vs A20. I trail 65-75. They've exploited my T with N frequently. Mutual N at ex33-34. Continuing N to avoid feeding 5s, protect against their N-exploit pattern.
`#283` · game 55 · round 18 · agent A07 (opponent: script:Random) · other · A07: Ex24 vs A23. I lead 78-28. They've picked J 17/23 but alternated J,F,J recently. Picking F to grab 5 against J or get 1 on mutual F.
`#284` · game 61 · round 1 · agent A11 (opponent: A15) · other · A11: Exchange 7 vs A15. They've picked J 6/6, mutual J streak ex3-6, I lead 22-12. Picking F to grab 5 against their reliable J.
`#285` · game 60 · round 8 · agent A18 (opponent: script:TitForTat) · other · A18: Exchange 14 vs A14. Mutual W streak ex8-13, I lead 33-18. Continuing W for mutual 1; grab 5 if they revert to Y.
`#286` · game 38 · round 23 · agent A21 (opponent: A06) · other · A21: Exchange 29 vs A06. I lead 65-40. Mutual M streak ex19-28. Continuing M for mutual 1 to protect lead.
`#287` · game 38 · round 23 · agent A06 (opponent: A21) · other · A06: Exchange 29 vs A21. Mutual M streak ex19-28. They protect lead with M. Continuing M for mutual 1.
`#288` · game 59 · round 7 · agent A03 (opponent: script:Random) · other · A03: Exchange 13 vs A23. They defected at ex9 and ex12 against my R. I lead 34-29. Picking H to avoid feeding 5s; get 5 if they revert to R, mutual 1 if they continue H.
`#289` · game 55 · round 21 · agent A07 (opponent: script:Random) · other · A07: Ex27 vs A23. Mutual F at ex24-26, I lead 81-31. Continuing F for mutual 1 point.
`#290` · game 55 · round 22 · agent A07 (opponent: script:Random) · other · A07: Ex28 vs A23. I lead 86-31. They play J frequently (18/27). Continuing F to grab 5 against J or get 1 on mutual F.
`#291` · game 65 · round 3 · agent A13 (opponent: script:Grudger) · other · A13: Ex9 vs A12. They've picked J 7/8, mutual F at ex8. I lead 28-13. Picking F to grab 5 against likely J revert, or get 1 on mutual F.
`#292` · game 65 · round 4 · agent A13 (opponent: script:Grudger) · other · A13: Ex10 vs A12. I lead 29-14. They've picked J 7/9 but mutual F at ex8-9. Picking F to grab 5 against J revert or get 1 on mutual F.
`#293` · game 55 · round 25 · agent A07 (opponent: script:Random) · other · A07: Ex31 vs A23. They pick J frequently (20/30), recent pattern J-heavy. I lead 97-32. Continuing F to grab 5 against likely J.
`#294` · game 61 · round 3 · agent A11 (opponent: A15) · other · A11: Exchange 9 vs A15. They played J 6/6 early, mutual J ex3-6, then mutual F ex7-8. I lead 24-14. Picking F to grab 5 against their J or get 1 on mutual F.
`#295` · game 64 · round 4 · agent A13 (opponent: A07) · other · A13: Exchange 10 vs A07. I lead 24-19. They've played H in last 3 exchanges (ex7,8,9). Picking H to avoid feeding 5s; get 5 if they revert to R, mutual 1 if they continue H.
`#296` · game 38 · round 26 · agent A06 (opponent: A21) · other · A06: Exchange 32 vs A21. Mutual M streak ex19-31. They protect lead with M. Continuing M for mutual 1.
`#297` · game 55 · round 26 · agent A07 (opponent: script:Random) · other · A07: Ex32 vs A23. I lead 98-33. They pick J frequently (20/31). Continuing F to grab 5 against J or get 1 on mutual F.
`#298` · game 67 · round 2 · agent A15 (opponent: script:Grudger) · other · A15: Ex8 vs A12. They've played R 7/7, never retaliated despite my H at ex1,2,7. I lead 27-12. Picking H to grab 5 against their reliable R.
`#299` · game 61 · round 4 · agent A11 (opponent: A15) · other · A11: Exchange 10 vs A15. Mutual F ex7-9, I lead 25-15. Picking F for mutual 1; grab 5 if they revert to J.
`#300` · game 68 · round 1 · agent A06 (opponent: script:TitForTat) · other · A06: Ex7 vs A09. They've played P 6/6, I lead 22-12. Playing M to grab 5 against their consistent P.
`#301` · game 59 · round 10 · agent A03 (opponent: script:Random) · other · A03: Exchange 16 vs A23. I lead 45-30. They keep playing R against my H (ex14,15). Continuing H to grab 5 or mutual 1; avoid feeding them 5s.
`#302` · game 67 · round 4 · agent A15 (opponent: script:Grudger) · other · A15: Ex10 vs A12. They played H at ex8-9 (mutual H). I lead 29-14. Continuing H to grab 5 if they revert to R, or get 1 on mutual H.
`#303` · game 67 · round 5 · agent A15 (opponent: script:Grudger) · other · A15: Ex11 vs A12. Mutual H ex8-10, I lead 30-15. Continuing H to grab 5 if they revert to R, or get 1 on mutual H.
`#304` · game 55 · round 28 · agent A07 (opponent: script:Random) · other · A07: Ex34 vs A23. I lead 104-34. They pick J frequently, recent alternating J/F. Continuing F to grab 5 against J or get 1 on mutual F.
`#305` · game 61 · round 5 · agent A15 (opponent: A11) · other · A15: Ex11 vs A11. Mutual F ex7-10, I lead 26-16. They've committed to F for mutual 1. Picking F to keep mutual 1 and protect lead.
`#306` · game 67 · round 6 · agent A15 (opponent: script:Grudger) · other · A15: Ex12 vs A12. Mutual H ex8-11, I lead 31-16. Continuing H to grab 5 if they revert to R, or get 1 on mutual H.
`#307` · game 38 · round 30 · agent A06 (opponent: A21) · other · A06: Exchange 36 vs A21. Mutual M streak ex19-35. They protect lead with M. Continuing M for mutual 1.
`#308` · game 65 · round 10 · agent A13 (opponent: script:Grudger) · other · A13: Ex16 vs A12. Mutual F ex8-15 (except ex13 I J'd, they F). I lead 34-24. Continuing F for mutual 1 point.
`#309` · game 67 · round 8 · agent A15 (opponent: script:Grudger) · other · A15: Ex14 vs A12. Mutual H ex8-13, I lead 33-18. Continuing H to grab 5 if they revert to R, or get 1 on mutual H.
`#310` · game 64 · round 7 · agent A13 (opponent: A07) · other · A13: Ex13 vs A07. Mutual H streak ex7-12, I lead 27-22. Continuing H for mutual 1 and to protect lead.
`#311` · game 59 · round 16 · agent A03 (opponent: script:Random) · other · A03: Ex22 vs A23. I lead 55-35. They played R at ex21 grabbing 5 after mutual H ex16-20. They alternate R/H. Playing R to grab 5 against their H or 3 on mutual R.
`#312` · game 61 · round 7 · agent A11 (opponent: A15) · other · A11: Ex13 vs A15. They broke mutual F at ex12 with J to grab 5. Playing J to avoid feeding 5s and get mutual 3 if they continue J.
`#313` · game 64 · round 8 · agent A13 (opponent: A07) · other · A13: Ex14 vs A07. Mutual H streak ex7-13, I lead 28-23. Continuing H for mutual 1 and to protect lead.
`#314` · game 64 · round 8 · agent A07 (opponent: A13) · other · A07: Ex14 vs A13. Mutual H streak ex7-13. A13 signals continuing H. I play H for mutual 1 and to protect my lead.
`#315` · game 71 · round 2 · agent A18 (opponent: A11) · other · 
`#316` · game 59 · round 17 · agent A03 (opponent: script:Random) · other · A03: Ex23 vs A23. I lead 58-38. They alternated to R at ex21 (grabbing 5) then mutual R ex22. Likely reverting to H. Playing H for mutual 1 or grab 5 if they revert to R.
`#317` · game 67 · round 11 · agent A15 (opponent: script:Grudger) · other · A15: Ex17 vs A12. They've been H-heavy (mutual H ex8-15), I broke with R at ex16 to grab 5. They may retaliate with R. Picking R to grab 5 if they stay H or get 3 on mutual R.
`#318` · game 70 · round 4 · agent A03 (opponent: script:Grudger) · other · A03: Ex10 vs A12. They've played Q 9/9. I lead 33-18. Picking X to grab 5 against their reliable Q.
`#319` · game 68 · round 7 · agent A06 (opponent: script:TitForTat) · other · A06: Ex13 vs A09. I lead 31-21. They've been M ex8-11, M at ex12. Continuing M for mutual 1 / grab 5 if they revert to P.
`#320` · game 72 · round 2 · agent A15 (opponent: script:AlwaysDefect) · other · A15: Ex8 vs A00. They've been Y-heavy (6/7), mutual Y ex3-6, W ex7. I lead 23-13. Picking Y to maintain mutual 3s and protect lead.
`#321` · game 71 · round 3 · agent A11 (opponent: A18) · other · A11: Ex9 vs A18. They've played J 7/8 times. Playing J for mutual 3 or grab 5 if they switch to F.
`#322` · game 71 · round 3 · agent A18 (opponent: A11) · other · A18: Ex9 vs A11. I lead 23-18. They've mixed J/F recently. Playing J to get mutual 3 or grab 5 if they play F.
`#323` · game 65 · round 26 · agent A13 (opponent: script:Grudger) · other · A13: Ex32 vs A12. Mutual F streak ex16-31 (except ex13 I J'd). I lead 50-40. Continuing F for mutual 1 point and to protect lead.
`#324` · game 70 · round 8 · agent A03 (opponent: script:Grudger) · other · A03: Ex14 vs A12. They played X ex10-13 (4 straight). I lead 36-26. Playing X to avoid feeding 5s if they stay X, or grab 5 if they revert to Q.
`#325` · game 61 · round 10 · agent A11 (opponent: A15) · other · A11: Ex16 vs A15. Recent mutual F ex14, mutual J ex15. Playing J for mutual 3 or grab 5 if they play F.
`#326` · game 68 · round 10 · agent A06 (opponent: script:TitForTat) · other · A06: Ex16 vs A09. I lead 37-27. They've been M-heavy recently (M at 8-12, P at 13, M at 14-15). Picking M for mutual 1 or grab 5 if they revert to P.
`#327` · game 70 · round 9 · agent A03 (opponent: script:Grudger) · other · A03: Ex15 vs A12. They've played X 5 straight (ex10-14). I lead 37-27. Playing X to avoid feeding 5s if they stay X, or grab 5 if they revert to Q.
`#328` · game 67 · round 17 · agent A15 (opponent: script:Grudger) · other · A15: Ex23 vs A12. They've been H-committed (mutual H ex21-22 after my R grabs). Playing R to grab 5 against their H.
`#329` · game 71 · round 6 · agent A11 (opponent: A18) · other · A11: Ex12 vs A18. They've played J 10/11 times, mutual J ex9-11. I lead 37-22. Playing J for mutual 3 or grab 5 if they switch to F.
`#330` · game 72 · round 6 · agent A15 (opponent: script:AlwaysDefect) · other · A15: Ex12 vs A00. They've played W last 5 exchanges (ex7-11). Mutual W gives 1 each, protects tie. Picking W for mutual 1.
`#331` · game 59 · round 23 · agent A03 (opponent: script:Random) · other · A03: Ex29 vs A23. I lead 69-59. They got 5s at ex26-27 with H against my R, then mutual R ex28. Likely reverting to H. Playing H for mutual 1 or grab 5 if they revert to R.
`#332` · game 68 · round 11 · agent A06 (opponent: script:TitForTat) · other · A06: Ex17 vs A09. I lead 42-27. They've been erratic alternating M/P to grab 5s. Playing P to grab 5 if they play M or mutual 3 if P.
`#333` · game 67 · round 18 · agent A15 (opponent: script:Grudger) · other · A15: Ex24 vs A12. They stay H-committed through my R grabs. Continuing R to grab 5 against their H or get 3 on mutual R.
`#334` · game 70 · round 10 · agent A03 (opponent: script:Grudger) · other · A03: Ex16 vs A12. They've played X 6 straight (ex10-15). I lead 38-28. Playing X for mutual 1 to protect lead and avoid feeding 5s.
`#335` · game 71 · round 7 · agent A11 (opponent: A18) · other · A11: Ex13 vs A18. They've played J 11/12 times, mutual J ex9-12. I lead 40-25. Playing J for mutual 3 and to protect lead.
`#336` · game 67 · round 19 · agent A15 (opponent: script:Grudger) · other · A15: Ex25 vs A12. They've stayed H through my R grabs ex16-24. Continuing R to grab 5 against H or get 3 on mutual R.
`#337` · game 61 · round 11 · agent A11 (opponent: A15) · other · A11: Ex17 vs A15. Mutual J ex15-16, I lead 39-29. Continuing J for mutual 3 and to protect lead.
`#338` · game 61 · round 11 · agent A15 (opponent: A11) · other · A15: Ex17 vs A11. Mutual J ex15-16 after mutual F ex14. A11 signals continuing J. Playing J for mutual 3.
`#339` · game 72 · round 8 · agent A15 (opponent: script:AlwaysDefect) · other · A15: Ex14 vs A00. Tied 27-27, mutual W streak ex7-13. Continuing W for mutual 1 to protect tied position.
`#340` · game 59 · round 25 · agent A03 (opponent: script:Random) · other · A03: Ex31 vs A23. After mutual R ex30, they've reverted to H after past mutual Rs (ex26, ex29). Playing H for mutual 1 or grab 5 if they revert to R.
`#341` · game 61 · round 12 · agent A11 (opponent: A15) · other · A11: Ex18 vs A15. Mutual J ex15-17, I lead 42-32. Continuing J for mutual 3 and to protect lead.
`#342` · game 67 · round 21 · agent A15 (opponent: script:Grudger) · other · A15: Ex27 vs A12. They stay H-committed through my R grabs. Continuing R to grab 5 against their H or get 3 on mutual R.
`#343` · game 68 · round 14 · agent A06 (opponent: script:TitForTat) · other · A06: Ex20 vs A09. I lead 47-37. They've been erratic, M-heavy lately (M at 14,15,17,19). Playing M for mutual 1 / protect lead.
`#344` · game 73 · round 2 · agent A02 (opponent: A01) · other · A02: Ex8 vs A01. They R-heavy (6/7) but switched to H ex7. I lead 23-13. Playing H to grab 5 if they revert to R, or mutual 1 if they stay H.
`#345` · game 72 · round 10 · agent A15 (opponent: script:AlwaysDefect) · other · A15 vs A00 Ex16. They've been heavily W (14/15), grab 5 when I play Y. I'm down 28-33. Playing W for mutual 1 to avoid feeding their 5s.
`#346` · game 67 · round 23 · agent A15 (opponent: script:Grudger) · other · A15: Ex29 vs A12. They've stayed H-committed through my R grabs ex16-28. Continuing R to grab 5 against their H or get 3 on mutual R.
`#347` · game 68 · round 15 · agent A06 (opponent: script:TitForTat) · other · A06: Ex21 vs A09. I lead 52-37. They've been alternating M/P (16M,17P,18M,19P,20M), so likely P at 21. Playing M to grab 5 against their P.
`#348` · game 75 · round 1 · agent A13 (opponent: script:Pavlov) · other · A13: Ex7 vs A05. They've played R 6/6 times. Mutual R ex3-6. I lead 22-12. Playing R for mutual 3 / protect lead.
`#349` · game 67 · round 25 · agent A15 (opponent: script:Grudger) · other · A15: Ex31 vs A12. They've stayed H-committed through my R grabs ex16-30. Continuing R to grab 5 against their H or get 3 on mutual R.
`#350` · game 68 · round 16 · agent A06 (opponent: script:TitForTat) · other · A06: Ex22 vs A09. I lead 53-38. They've been erratic (M at 14,15,17,19,20,21). Playing M to protect lead - grab 5 if they play P, mutual 1 if M.
`#351` · game 75 · round 2 · agent A13 (opponent: script:Pavlov) · other · A13: Ex8 vs A05. They've played R 7/7 times. Mutual R ex3-7. I lead 25-15. Playing R for mutual 3 / protect lead.
`#352` · game 77 · round 1 · agent A18 (opponent: A01) · other · A18: Ex7 vs A01. Mutual T ex3-6 after my N grabs ex1-2. They've played T 6/6. Continuing T for mutual 3.
`#353` · game 67 · round 27 · agent A15 (opponent: script:Grudger) · other · A15: Ex33 vs A12. They stay H-committed through my R grabs ex16-32. Continuing R to grab 5 against their H.
`#354` · game 68 · round 17 · agent A06 (opponent: script:TitForTat) · other · A06: Ex23 vs A09. Mutual M ex21-22, I lead 54-39. Continuing M for mutual 1 / protect lead.
`#355` · game 68 · round 18 · agent A06 (opponent: script:TitForTat) · other · A06: Ex24 vs A09. Mutual M ex21-23, I lead 55-40. Continuing M for mutual 1 / protect lead.
`#356` · game 67 · round 28 · agent A15 (opponent: script:Grudger) · other · A15: Ex34 vs A12. They stay H-committed through my R grabs ex16-33. Continuing R to grab 5 against their H.
`#357` · game 59 · round 29 · agent A03 (opponent: script:Random) · other · A03: Ex35 vs A23. After mutual H ex31-33, I grabbed 5 at ex34 when they reverted to R. They'll likely return to H now. Playing H for mutual 1.
`#358` · game 78 · round 3 · agent A06 (opponent: script:Random) · other · A06: Ex9 vs A17. They've played P all 8 times. Playing M to grab 5 against their P / protect my lead.
`#359` · game 79 · round 1 · agent A16 (opponent: script:Pavlov) · other · A16: Ex7 vs A05. They've played P all 6 times, mutual P ex3-6. I lead 22-12. Playing P for mutual 3 / protect lead.
`#360` · game 59 · round 30 · agent A03 (opponent: script:Random) · other · A03: Ex36 vs A23. They played R at ex34-35 giving me 5 each. Likely switching to H now. Playing R to grab 5 against their H.
`#361` · game 61 · round 19 · agent A11 (opponent: A15) · other · A11: Ex25 vs A15. Mutual J ex15-24, I lead 63-53. Continuing J for mutual 3 / protect lead.
`#362` · game 61 · round 19 · agent A15 (opponent: A11) · other · A15: Ex25 vs A11. Mutual J ex15-24, I lead 63-53. A11 committed to J to protect lead. Continuing J for mutual 3.
`#363` · game 74 · round 10 · agent A21 (opponent: script:TitForTat) · other · A21: Ex16 vs A22. I lead 43-33, they're T-heavy (11/15, mutual T ex13-15). Grabbing N against their likely T.
`#364` · game 79 · round 4 · agent A16 (opponent: script:Pavlov) · other · A16: Ex10 vs A05. They've played P 9/9 times. I lead 31-21. Grabbing M for 5 against their expected P.
`#365` · game 77 · round 7 · agent A18 (opponent: A01) · other · A18: Ex13 vs A01. Mutual T ex3-12 after my N grabs ex1-2. They've played T 12/12. I lead 40-30. Continuing T for mutual 3.
`#366` · game 81 · round 2 · agent A15 (opponent: A07) · other · A15: Ex8 vs A07. They've played T all 7 times; I grabbed 5s with N at ex1,2,7. Continuing N to grab 5 against their T.
`#367` · game 78 · round 9 · agent A06 (opponent: script:Random) · other · A06: Ex15 vs A17. They've played P 11/14 times, M at 9,10,13. I lead 48-18. Playing M to grab 5 against their likely P / protect lead.
`#368` · game 68 · round 26 · agent A06 (opponent: script:TitForTat) · other · A06: Ex32 vs A09. Recent: they've been M-heavy (M at 14,15,17,19,20,21,23-31). I lead 63-48. They seem locked into M for mutual 1. Playing M for safety/mutual 1.
`#369` · game 79 · round 6 · agent A16 (opponent: script:Pavlov) · other · A16: Ex12 vs A05. They played P 10/11 times but switched to M at ex11 (mutual M). I lead 37-22. Playing M to protect lead - grab 5 if they play P, mutual 1 if M.
`#370` · game 68 · round 28 · agent A06 (opponent: script:TitForTat) · other · A06: Ex34 vs A09. They've been M-heavy (M at 21-33 mutual). I lead 65-50. Playing M for mutual 1 / protect lead.
`#371` · game 81 · round 4 · agent A07 (opponent: A15) · other · A07: Ex10 vs A15. They've grabbed N against my T at ex1,2,7 and signaled continuing N. Playing N for mutual 1 rather than 0.
`#372` · game 81 · round 4 · agent A15 (opponent: A07) · other · A15: Ex10 vs A07. They've played T 7/9, N at 8-9. I lead 29-14. Playing N to grab 5 against their T or mutual 1 on N.
`#373` · game 74 · round 14 · agent A21 (opponent: script:TitForTat) · other · A21: Ex20 vs A22. I lead 52-42. They're T-heavy, mutual T at ex19. Grabbing N against their likely T.
`#374` · game 79 · round 9 · agent A16 (opponent: script:Pavlov) · other · A16: Ex15 vs A05. They've played P 12/14, M at 11,13. I lead 48-23. Playing M to grab 5 against their likely P / protect lead.
`#375` · game 82 · round 7 · agent A11 (opponent: script:Random) · other · A11: Ex13 vs A17. I trail 28-38. They've mixed R/H, grabbed with H at 7,8,10,11. Playing H to grab 5 against their likely R.
`#376` · game 84 · round 2 · agent A11 (opponent: script:Pavlov) · uncoded · A11: Ex8 vs A08. They've played R all 7 times. I lead 27-12. Grabbing H for 5 against their likely R.
`#377` · game 79 · round 10 · agent A16 (opponent: script:Pavlov) · other · A16: Ex16 vs A05. They've alternated M at odd (11,13,15) and P at even (10,12,14). Ex16 even, expecting P. Playing M to grab 5 / protect lead (49-24).
`#378` · game 74 · round 16 · agent A21 (opponent: script:TitForTat) · other · A21: Ex22 vs A22. I lead 58-43. They're T-heavy (14/21). They played N at ex21 after T at ex20. Grabbing N against likely T for 5.
`#379` · game 77 · round 26 · agent A18 (opponent: A01) · other · A18: Ex32 vs A01. Mutual T since ex3. I lead 97-87. Continuing T for mutual 3.
`#380` · game 84 · round 3 · agent A11 (opponent: script:Pavlov) · uncoded · A11: Ex9 vs A08. They played R ex1-7, H at ex8 (mutual H). I lead 28-13. Playing R to grab 5 against their likely H, or mutual 3 if they revert to R.
`#381` · game 74 · round 18 · agent A21 (opponent: script:TitForTat) · other · A21: Ex24 vs A22. I lead 60-45. Recent mutual N at 21-23. Matching N for mutual 1.
`#382` · game 79 · round 14 · agent A16 (opponent: script:Pavlov) · other · A16: Ex20 vs A05. Pattern - they play P at even exchanges (10,12,14,16,18), M at odd. Ex20 even, expecting P. Playing M to grab 5 / protect lead (61-26).
`#383` · game 79 · round 15 · agent A16 (opponent: script:Pavlov) · other · A16: Ex21 vs A05. Pattern - they play P at even, M at odd. Ex21 odd, expecting M. Playing M for mutual 1 / avoid giving 5.
`#384` · game 78 · round 17 · agent A06 (opponent: script:Random) · other · A06: Ex23 vs A17. I lead 64-24. They've mixed P/M recently (P 11/20, M 9/20). Playing M to grab 5 against their likely P / protect lead.
`#385` · game 81 · round 7 · agent A07 (opponent: A15) · other · A07: Ex13 vs A15. Mutual N ex8-12, I lead 27-22. Continuing N for mutual 1.
`#386` · game 81 · round 7 · agent A15 (opponent: A07) · other · A15: Ex13 vs A07. Recent mutual N ex8-12. They signaled playing N for mutual 1. Continuing N for mutual 1.
`#387` · game 74 · round 20 · agent A21 (opponent: script:TitForTat) · other · A21: Ex26 vs A22. They've played N ex21-25 (mutual N). I lead 62-47. Continuing N for mutual 1.
`#388` · game 82 · round 8 · agent A11 (opponent: script:Random) · other · A11: Ex14 vs A17. I trail 29-39. Mutual H at ex13. Playing H to grab 5 if they revert to R, mutual 1 if H.
`#389` · game 83 · round 5 · agent A21 (opponent: A20) · uncoded · A21: Ex11 vs A20. They're Y-heavy (8/10), I lead 32-17. Grabbing W against their likely Y.
`#390` · game 78 · round 18 · agent A06 (opponent: script:Random) · other · A06: Ex24 vs A17. I lead 69-24. They've played P 14/23, M recently mixed (P at 20,21,23; M at 22). Playing M to grab 5 against P or mutual 1 against M / protect lead.
`#391` · game 85 · round 2 · agent A16 (opponent: script:AlwaysDefect) · other · A16: Ex8 vs A00. They played R ex1-6, H at ex7 (mutual H). I lead 23-13. Playing H to grab 5 if they revert to R, or mutual 1 if they continue H.
`#392` · game 74 · round 21 · agent A21 (opponent: script:TitForTat) · other · A21: Ex27 vs A22. Mutual N ex21-26, I lead 63-48. Continuing N for mutual 1 / protect lead.
`#393` · game 82 · round 9 · agent A11 (opponent: script:Random) · other · A11: Ex15 vs A17. I trail 30-40. Recent mutual H at ex13-14. They've grabbed H against my R at 7,8,10,11. Playing H to grab 5 if they revert to R, mutual 1 if H.
`#394` · game 81 · round 8 · agent A07 (opponent: A15) · other · A07: Ex14 vs A15. Mutual N ex8-13, I lead 28-23. Continuing N for mutual 1.
`#395` · game 81 · round 8 · agent A15 (opponent: A07) · other · A15: Ex14 vs A07. Mutual N ex8-13, I lead 33-18. Continuing N for mutual 1.
`#396` · game 78 · round 19 · agent A06 (opponent: script:Random) · other · A06: Ex25 vs A17. I lead 70-25. They've played M at 22,24 and P at 20,21,23. Playing M to grab 5 against P or mutual 1 against M / protect lead.
`#397` · game 85 · round 3 · agent A16 (opponent: script:AlwaysDefect) · other · A16: Ex9 vs A00. They played R ex1-6, H at ex7-8 (mutual H). I lead 24-14. Playing H to grab 5 if they revert to R, or mutual 1 if they continue H.
`#398` · game 84 · round 7 · agent A11 (opponent: script:Pavlov) · uncoded · A11: Ex13 vs A08. Their pattern R1-6, H7-8, R9, H10-11, R12. Likely H at 13. Playing H for mutual 1 / avoid giving 5. I lead 42-17.
`#399` · game 82 · round 10 · agent A11 (opponent: script:Random) · other · A11: Ex16 vs A17. I trail 31-41. Mutual H last 3 (ex13-15). Playing R to grab 5 against their likely H, or mutual 3 if they revert to R.
`#400` · game 83 · round 6 · agent A20 (opponent: A21) · uncoded · A20: Ex12 vs A21. They signaled grabbing W against my Y-heavy play. Playing W for mutual 1 rather than giving 5.
`#401` · game 83 · round 6 · agent A21 (opponent: A20) · uncoded · A21: Ex12 vs A20. They're Y-heavy (9/11). I lead 37-17. Grabbing W against their likely Y for 5.
`#402` · game 74 · round 24 · agent A21 (opponent: script:TitForTat) · other · A21: Ex30 vs A22. Mutual N ex21-29, I lead 66-51. Continuing N for mutual 1 / protect lead.
`#403` · game 85 · round 5 · agent A16 (opponent: script:AlwaysDefect) · other · A16: Ex11 vs A00. They played R ex1-6, H ex7-10 (mutual H). I lead 26-16. Continuing H for mutual 1 / avoid giving 5.
`#404` · game 81 · round 10 · agent A15 (opponent: A07) · other · A15: Ex16 vs A07. Mutual N ex8-15, I lead 35-20. Continuing N for mutual 1.
`#405` · game 82 · round 11 · agent A11 (opponent: script:Random) · other · A11: Ex17 vs A17. I trail 31-46. They played H at 16 against my R. Playing H to grab 5 if they revert to R, or mutual 1 if they continue H.
`#406` · game 74 · round 25 · agent A21 (opponent: script:TitForTat) · other · A21: Ex31 vs A22. Mutual N ex21-30, I lead 67-52. Continuing N for mutual 1 / protect lead.
`#407` · game 78 · round 21 · agent A06 (opponent: script:Random) · other · A06: Ex27 vs A17. I lead 80-25. They've played P at 20,21,23,25,26 and M at 22,24. Playing M to grab 5 against P or mutual 1 against M / protect lead.
`#408` · game 83 · round 7 · agent A20 (opponent: A21) · uncoded · A20: Ex13 vs A21. Tied 28-28. A21 has grabbed W against my Y repeatedly (ex1,2,7,11). Playing W to protect against giving 5 / mutual 1.
`#409` · game 82 · round 12 · agent A11 (opponent: script:Random) · other · A11: Ex18 vs A17. I trail 36-46. They played R at 17 against my H. Playing H to grab 5 if they revert to R, or mutual 1 if they continue H.
`#410` · game 85 · round 10 · agent A16 (opponent: script:AlwaysDefect) · other · A16: Ex16 vs A00. Mutual H ex7-15, I lead 31-21. Continuing H for mutual 1 / avoid giving 5.
`#411` · game 84 · round 12 · agent A11 (opponent: script:Pavlov) · uncoded · A11: Ex18 vs A08. I lead 54-24. They've played R 12/17, H only recently at 8,11,13,15,16. They played R at ex17. Playing H to grab 5 against their likely R, or mutual 1 if they play H.
`#412` · game 82 · round 14 · agent A11 (opponent: script:Random) · other · A11: Ex20 vs A17. I trail 38-48. Mutual H ex18-19. Playing H to grab 5 if they revert to R, or mutual 1 if they continue H.
`#413` · game 89 · round 1 · agent A11 (opponent: script:Pavlov) · other · A11: Ex7 vs A05. I lead 22-12. They've played Y all 6 exchanges. Recent mutual Y ex3-6. Playing W to grab 5 if they continue Y, mutual 1 if they switch to W.
`#414` · game 88 · round 2 · agent A16 (opponent: script:Grudger) · other · A16: Ex8 vs A12. They've played Q all 7 exchanges. I lead 25-15. Playing X to grab 5 against their likely Q.
`#415` · game 85 · round 13 · agent A16 (opponent: script:AlwaysDefect) · other · A16: Ex19 vs A00. Mutual H ex7-18, I lead 34-24. Continuing H for mutual 1 / protect lead.
`#416` · game 87 · round 3 · agent A03 (opponent: A06) · other · A03: Ex9 vs A06. They play Q very frequently (7/8), X only at ex7. I'm playing X to grab 5 against likely Q.
`#417` · game 84 · round 14 · agent A11 (opponent: script:Pavlov) · uncoded · A11: Ex20 vs A08. I lead 60-25. Their recent pattern alternating H/R (H16,R17,H18,R19). Likely H at 20. Playing H for mutual 1 / avoid giving 5.
`#418` · game 81 · round 17 · agent A07 (opponent: A15) · other · A07: Ex23 vs A15. Mutual N ex8-22, I lead 37-32. Continuing N for mutual 1.
`#419` · game 89 · round 3 · agent A11 (opponent: script:Pavlov) · other · A11: Ex9 vs A05. I lead 28-13. They played Y ex1-7, W at ex8. Playing W to grab 5 if they revert to Y, or mutual 1 if they continue W.
`#420` · game 88 · round 5 · agent A16 (opponent: script:Grudger) · other · A16: Ex11 vs A12. They played Q ex1-8, X ex9-10. I lead 32-17. Playing X to grab 5 if they revert to Q, or mutual 1 if they continue X.
`#421` · game 82 · round 18 · agent A11 (opponent: script:Random) · other · A11: Ex24 vs A17. I trail 46-51. Mutual H ex18-22, they played R at 23 (I got 5). Likely revert to H at 24 for mutual 1, or continue R. Playing H to grab 5 if they play R, or mutual 1 if H.
`#422` · game 81 · round 18 · agent A15 (opponent: A07) · other · A15: Ex24 vs A07. Mutual N ex8-23, I lead 43-28. Continuing N for mutual 1.
`#423` · game 88 · round 6 · agent A16 (opponent: script:Grudger) · other · A16: Ex12 vs A12. They played Q ex1-8, X ex9-11. I lead 33-18. Playing X for mutual 1 / grab 5 if they revert to Q.
`#424` · game 82 · round 19 · agent A11 (opponent: script:Random) · other · A11: Ex25 vs A17. I trail 47-52. Mutual H ex18-22, R at 23, mutual H at 24. Playing H to grab 5 if they revert to R, or mutual 1 if they continue H.
`#425` · game 91 · round 3 · agent A21 (opponent: script:AlwaysDefect) · other · A21: Ex9 vs A04. They defected N at ex7,8 (got 5 at ex8 vs my T). I lead 23-18. Playing N to protect lead / avoid giving 5.
`#426` · game 84 · round 19 · agent A11 (opponent: script:Pavlov) · uncoded · A11: Ex25 vs A08. I lead 72-32. They played R at 24 after H at 22,23. Playing H to grab 5 if they revert to R, or mutual 1 if they continue H.
`#427` · game 92 · round 2 · agent A13 (opponent: script:Grudger) · other · A13: Ex8 vs A19. They've played Y all 7 exchanges. I lead 27-12. Playing W to grab 5 against their likely Y.
`#428` · game 81 · round 21 · agent A07 (opponent: A15) · other · A07: Ex27 vs A15. Mutual N ex8-26, I lead 41-36. Continuing N for mutual 1.
`#429` · game 84 · round 20 · agent A11 (opponent: script:Pavlov) · uncoded · A11: Ex26 vs A08. I lead 73-33. Their recent pattern alternating H/R (H23,R24,H25). Likely R at 26. Playing H to grab 5 against their likely R, or mutual 1 if they play H.
`#430` · game 92 · round 3 · agent A13 (opponent: script:Grudger) · other · A13: Ex9 vs A19. I lead 28-13. They played Y 7x then W at ex8. Playing W to grab 5 if they revert to Y, or mutual 1 if they continue W.
`#431` · game 84 · round 21 · agent A11 (opponent: script:Pavlov) · uncoded · A11: Ex27 vs A08. I lead 78-33. Recent vs A08: H23/H, R24 (got 5), H25, R26 (got 5). Playing H to grab 5 if they play R, or mutual 1 if H.
`#432` · game 82 · round 22 · agent A11 (opponent: script:Random) · other · A11: Ex28 vs A17. They played R at 25,26,27 (I got 5 each with H). Continuing H to grab 5 if they keep R, or mutual 1 if they switch to H.
`#433` · game 88 · round 12 · agent A16 (opponent: script:Grudger) · other · A16: Ex18 vs A12. Mutual X ex9-17, I lead 39-24. Continuing X for mutual 1 / grab 5 if they revert to Q.
`#434` · game 82 · round 23 · agent A11 (opponent: script:Random) · other · A11: Ex29 vs A17. They played R at 25,26,27,28 (I got 5 each with H). Continuing H to grab 5 if they keep R, or mutual 1 if they switch to H.
`#435` · game 81 · round 23 · agent A15 (opponent: A07) · other · A15: Ex29 vs A07. Mutual N ex8-27, I played T at 28 (they N, I got 0). Returning to N for mutual 1.
`#436` · game 88 · round 13 · agent A16 (opponent: script:Grudger) · other · A16: Ex19 vs A12. Mutual X ex9-18, I lead 40-25. Continuing X for mutual 1 / grab 5 if they revert to Q.
`#437` · game 95 · round 3 · agent A03 (opponent: script:TitForTat) · other · A03: Ex9 vs A10. They've played Y all 8 exchanges. I lead 30-15. Playing W to grab 5 against their likely Y, or mutual 1 if they switch to W.
`#438` · game 91 · round 6 · agent A21 (opponent: script:AlwaysDefect) · other · A21: Ex12 vs A04. Tied 25-25. They've played N ex8-11. Playing N to avoid giving 5 / mutual 1.
`#439` · game 82 · round 24 · agent A11 (opponent: script:Random) · other · A11: Ex30 vs A17. They played R at 25-29 (I got 5 each with H). I lead 72-52. Continuing H to grab 5 if they keep R, or mutual 1 if they switch to H.
`#440` · game 95 · round 4 · agent A03 (opponent: script:TitForTat) · other · A03: Ex10 vs A10. They played Y ex1-8, W at ex9 (mutual W). I lead 31-16. Playing W to grab 5 if they revert to Y, or mutual 1 if they continue W.
`#441` · game 82 · round 25 · agent A11 (opponent: script:Random) · other · A11: Ex31 vs A17. They played R at 23,25-30 (I got 5 each with H). I lead 77-52. Continuing H to grab 5 if they keep R, or mutual 1 if they switch to H.
`#442` · game 88 · round 16 · agent A16 (opponent: script:Grudger) · other · A16: Ex22 vs A12. Mutual X ex9-21, I lead 43-28. Continuing X for mutual 1 / grab 5 if they revert to Q.
`#443` · game 91 · round 7 · agent A21 (opponent: script:AlwaysDefect) · other · A21: Ex13 vs A04. Tied 26-26. They've played N ex8-12. Continuing N for mutual 1 / avoid giving 5.
`#444` · game 92 · round 7 · agent A13 (opponent: script:Grudger) · other · A13: Ex13 vs A19. Mutual W ex8-12, I lead 32-17. Playing W for mutual 1 / grab 5 if they revert to Y.
`#445` · game 92 · round 8 · agent A13 (opponent: script:Grudger) · other · A13: Ex14 vs A19. Mutual W ex8-13, I lead 33-18. Continuing W for mutual 1 / grab 5 if they revert to Y.
`#446` · game 95 · round 7 · agent A03 (opponent: script:TitForTat) · other · A03: Ex13 vs A10. Mutual W ex9-12, I lead 34-19. Playing W for mutual 1 / grab 5 if they revert to Y.
`#447` · game 81 · round 26 · agent A15 (opponent: A07) · other · A15: Ex32 vs A07. Mutual N ex29-31. Continuing N for mutual 1.
`#448` · game 82 · round 27 · agent A11 (opponent: script:Random) · other · A11: Ex33 vs A17. They played H at 31,32 after R at 25-30. I lead 79-54. Playing H for mutual 1 / grab 5 if they revert to R.
`#449` · game 95 · round 9 · agent A03 (opponent: script:TitForTat) · other · A03: Ex15 vs A10. Mutual W ex9-14, I lead 36-21. Continuing W for mutual 1 / grab 5 if they revert to Y.
`#450` · game 87 · round 7 · agent A03 (opponent: A06) · other · A03: Ex13 vs A06. I lead 32-17. They've played X ex9-12. Playing X for mutual 1 / grab 5 if they revert to Q.
`#451` · game 87 · round 7 · agent A06 (opponent: A03) · other · A06: Ex13 vs A03. Mutual X ex9-12, I lead 27-22. Continuing X for mutual 1 / protect lead.
`#452` · game 91 · round 11 · agent A21 (opponent: script:AlwaysDefect) · other · A21: Ex17 vs A04. Tied 30-30. Mutual N ex11-16. Continuing N for mutual 1.
`#453` · game 96 · round 1 · agent A03 (opponent: A18) · other · A03: Ex7 vs A18. They've played T all 6 exchanges. I lead 22-12. Playing T for mutual 3.
`#454` · game 82 · round 28 · agent A11 (opponent: script:Random) · other · A11: Ex34 vs A17. They played R at 33 after H at 31,32. I lead 84-54. Continuing H to grab 5 if they keep R, or mutual 1 if H.
`#455` · game 91 · round 12 · agent A21 (opponent: script:AlwaysDefect) · other · A21: Ex18 vs A04. Tied 31-31. Mutual N ex7-17. Continuing N for mutual 1.
`#456` · game 82 · round 29 · agent A11 (opponent: script:Random) · other · A11: Ex35 vs A17. They played R at 33,34 after H at 31,32. I lead 89-54. Continuing H to grab 5 if they keep R, or mutual 1 if H.
`#457` · game 92 · round 13 · agent A13 (opponent: script:Grudger) · other · A13: Ex19 vs A19. Mutual W ex8-18, I lead 38-23. Continuing W for mutual 1 / grab 5 if they revert to Y.
`#458` · game 91 · round 15 · agent A21 (opponent: script:AlwaysDefect) · other · A21: Ex21 vs A04. Tied 34-34. Mutual N ex7-20. Continuing N for mutual 1.
`#459` · game 95 · round 14 · agent A03 (opponent: script:TitForTat) · other · A03: Ex20 vs A10. Mutual W ex9-19, I lead 41-26. Continuing W for mutual 1 / grab 5 if they revert to Y.
`#460` · game 100 · round 2 · agent A15 (opponent: script:TitForTat) · other · A15: Ex8 vs A22. They've played R all 7 exchanges. I lead 27-12. Continuing H to grab 5 if they keep R, or mutual 1 if they switch to H.
`#461` · game 91 · round 19 · agent A21 (opponent: script:AlwaysDefect) · other · A21: Ex25 vs A04. Tied 38-38. Mutual N ex11-24. Continuing N for mutual 1.
`#462` · game 101 · round 1 · agent A06 (opponent: script:TitForTat) · other · A06: Ex7 vs A22. They've played Q 6/6, we had mutual Q ex3-6. I lead 22-12. Playing X to grab 5 if they keep Q.
`#463` · game 100 · round 3 · agent A15 (opponent: script:TitForTat) · other · A15: Ex9 vs A22. They played R ex1-7, H ex8. I lead 28-13. Continuing H for mutual 1 / grab 5 if they revert to R.
`#464` · game 101 · round 2 · agent A06 (opponent: script:TitForTat) · other · A06: Ex8 vs A22. They've played Q 7/7. I grabbed 5 at Ex7 with X. Continuing X to grab 5 if they keep Q, or mutual 1 if they switch to X.
`#465` · game 99 · round 5 · agent A01 (opponent: script:Random) · other · A01: Ex11 vs A23. They keep playing R (9/10), I lead 38-13. Continuing H to grab 5 when they play R.
`#466` · game 99 · round 6 · agent A01 (opponent: script:Random) · other · A01: Ex12 vs A23. They keep playing R, I lead 43-13. Continuing H to grab 5 when they play R.
`#467` · game 87 · round 11 · agent A06 (opponent: A03) · other · A06: Ex17 vs A03. Mutual X ex9-16, I lead 31-26. Continuing X for mutual 1 / protect lead.
`#468` · game 101 · round 4 · agent A06 (opponent: script:TitForTat) · other · A06: Ex10 vs A22. I lead 29-14. They switched to X ex8-9. Playing X for mutual 1 / grab 5 if they revert to Q.
`#469` · game 99 · round 7 · agent A01 (opponent: script:Random) · other · A01: Ex13 vs A23. They played R 10/12, H at ex7 and ex12. I lead 44-14. Continuing H to grab 5 if they play R, or mutual 1 if H.
`#470` · game 102 · round 1 · agent A18 (opponent: A06) · other · A18: Ex7 vs A03. They signaled T. Taking N for 5.
`#471` · game 100 · round 6 · agent A15 (opponent: script:TitForTat) · other · A15: Ex12 vs A22. Mutual H ex8-11, I lead 31-16. Continuing H for mutual 1.
`#472` · game 92 · round 27 · agent A13 (opponent: script:Grudger) · other · A13: Ex33 vs A19. Mutual W ex8-32, I lead 52-37. Continuing W for mutual 1 / grab 5 if they revert to Y.
`#473` · game 92 · round 28 · agent A13 (opponent: script:Grudger) · other · A13: Ex34 vs A19. Mutual W ex8-33, I lead 53-38. Continuing W for mutual 1 / grab 5 if they revert to Y.
`#474` · game 101 · round 7 · agent A06 (opponent: script:TitForTat) · other · A06: Ex13 vs A22. Mutual X ex8-12. I lead 32-17. Continuing X for mutual 1 / grab 5 if they revert to Q.
`#475` · game 87 · round 12 · agent A03 (opponent: A06) · other · A03: Ex18 vs A06. Mutual X ex9-17, I lead 37-22. Continuing X for mutual 1 / protect lead.
`#476` · game 87 · round 12 · agent A06 (opponent: A03) · other · A06: Ex18 vs A03. Mutual X ex9-17, I lead 32-27. Continuing X for mutual 1 / protect lead.
`#477` · game 102 · round 2 · agent A18 (opponent: A06) · other · A18: Ex8 vs A06. They've played T all 7 exchanges. I lead 27-12. Taking N for 5.
`#478` · game 101 · round 9 · agent A06 (opponent: script:TitForTat) · other · A06: Ex15 vs A22. Mutual X ex8-14, I lead 34-19. Playing X for mutual 1 / grab 5 if they revert to Q.
`#479` · game 100 · round 10 · agent A15 (opponent: script:TitForTat) · other · A15: Ex16 vs A22. Mutual H ex8-15, I lead 35-20. Continuing H for mutual 1.
`#480` · game 99 · round 13 · agent A01 (opponent: script:Random) · other · A01: Ex19 vs A23. They keep playing R (14/18), I lead 66-16. Continuing H to grab 5 when they play R, or mutual 1 if H.
`#481` · game 101 · round 10 · agent A06 (opponent: script:TitForTat) · other · A06: Ex16 vs A22. Mutual X ex8-15, I lead 35-20. Continuing X for mutual 1 / grab 5 if they revert to Q.
`#482` · game 105 · round 3 · agent A18 (opponent: script:Random) · other · A18: Ex9 vs A17. They've played T all 8 exchanges. I lead 30-15. Playing N for 5.
`#483` · game 105 · round 4 · agent A18 (opponent: script:Random) · other · A18: Ex10 vs A17. They've played T all 9 exchanges. I lead 35-15. Continuing N for 5.
`#484` · game 99 · round 15 · agent A01 (opponent: script:Random) · other · A01: Ex21 vs A23. They keep playing R (16/20), I lead 76-16. Continuing H to grab 5 when they play R, or mutual 1 if H.
`#485` · game 100 · round 14 · agent A15 (opponent: script:TitForTat) · other · A15: Ex20 vs A22. Final exchange of run. Playing R to maximize endgame payoff.
`#486` · game 101 · round 16 · agent A06 (opponent: script:TitForTat) · other · A06: Ex22 vs A22. Mutual X ex8-21, I lead 41-26. Continuing X for mutual 1 / grab 5 if they revert to Q.
`#487` · game 107 · round 1 · agent A11 (opponent: A02) · other · A11: Ex7 vs A02. They've played Q 6/6. I lead 22-12. Playing X to grab 5 if they keep Q.
`#488` · game 106 · round 2 · agent A15 (opponent: A13) · uncoded · A15: Ex8 vs A13. They've played R 7/7. I lead 27-12. Playing H to grab 5 while they keep playing R.
`#489` · game 112 · round 1 · agent A11 (opponent: script:Random) · other · A11: Ex7 vs A23. Mutual J ex3-6, I lead 22-12. Continuing J for mutual 3.
`#490` · game 101 · round 17 · agent A06 (opponent: script:TitForTat) · other · A06: Ex23 vs A22. Mutual X ex8-22, I lead 42-27. Continuing X for mutual 1 / grab 5 if they revert to Q.
`#491` · game 112 · round 2 · agent A11 (opponent: script:Random) · other · A11: Ex8 vs A23. Mutual J ex3-7, I lead 25-15. Continuing J for mutual 3.
`#492` · game 100 · round 15 · agent A15 (opponent: script:TitForTat) · other · A15: Ex21 vs A22. Final exchange. Playing H for mutual 1 / safety after their H at ex20.
`#493` · game 101 · round 19 · agent A06 (opponent: script:TitForTat) · other · A06: Ex25 vs A22. Mutual X ex8-24, I lead 44-29. Continuing X for mutual 1 / grab 5 if they revert to Q.
`#494` · game 113 · round 1 · agent A01 (opponent: A16) · other · A01: Ex7 vs A16. They've played Q all 6 exchanges. I lead 22-12. Taking X to grab 5 since they keep playing Q.
`#495` · game 102 · round 4 · agent A18 (opponent: A06) · other · A18: Ex10 vs A06. They signaled N via notes (playing X for mutual 1, protecting lead). Playing N for mutual 1.
`#496` · game 106 · round 3 · agent A15 (opponent: A13) · uncoded · A15: Ex9 vs A13. They played R 7/8 but H at ex8. I lead 28-13. Playing H to establish mutual H / grab 5 if they revert to R.
`#497` · game 111 · round 2 · agent A07 (opponent: A20) · other · A07: Ex8 vs A20. Mutual Q ex3-6, mutual X ex7. I lead 23-13. Playing Q to maintain cooperation.
`#498` · game 107 · round 2 · agent A02 (opponent: A11) · other · A02: Ex8 vs A11. They've been defecting with X. I lead 23-13. Playing X for mutual 1 / protect lead.
`#499` · game 107 · round 2 · agent A11 (opponent: A02) · other · A11: Ex8 vs A02. They played Q 6/6 then X at ex7. I lead 23-13. Playing X for mutual 1 / grab 5 if they revert to Q.
`#500` · game 100 · round 16 · agent A15 (opponent: script:TitForTat) · other · A15: Ex22 vs A22. After defections at 20-21, playing H for mutual 1 / grab 5 if they play R.
`#501` · game 101 · round 30 · agent A06 (opponent: script:TitForTat) · other · A06: Ex36 vs A22. Mutual X ex8-35, I lead 55-40. Continuing X for mutual 1 / grab 5 if they revert to Q.
`#502` · game 112 · round 4 · agent A11 (opponent: script:Random) · other · A11: Ex10 vs A23. Mutual J ex3-9, I lead 26-21. Continuing J for mutual 3.
`#503` · game 111 · round 3 · agent A20 (opponent: A07) · other · A20: Ex9 vs A07. They keep signaling Q. I lead 28-13. Playing X to grab 5 if they play Q.
`#504` · game 114 · round 1 · agent A02 (opponent: script:TitForTat) · other · A02: Ex7 vs A22. They've played J 6/6, we've had mutual J ex3-6. Continuing J for mutual 3.
`#505` · game 100 · round 18 · agent A15 (opponent: script:TitForTat) · other · A15: Ex24 vs A22. Continuing H for mutual 1 after mutual H at 22-23.
`#506` · game 106 · round 4 · agent A15 (opponent: A13) · uncoded · A15: Ex10 vs A13. Final exchange. They reciprocated H ex8-9. Playing H for mutual 1 / grab 5 if they revert to R.
`#507` · game 106 · round 4 · agent A13 (opponent: A15) · uncoded · A13: Ex10 vs A15. They've played H at ex8-9. Playing R to grab 5 if they keep H, or mutual 3 if R.
`#508` · game 102 · round 5 · agent A18 (opponent: A06) · other · A18: Ex11 vs A06. Mutual N ex8-10, continuing N for mutual 1.
`#509` · game 102 · round 5 · agent A06 (opponent: A18) · other · A06: Ex11 vs A18. Mutual N ex8-10, I lead 25-20. Continuing N for mutual 1.
`#510` · game 111 · round 4 · agent A07 (opponent: A20) · other · A07: Ex10 vs A20. They've defected with X ex7-9. Playing X for mutual 1 / protect against their grab.
`#511` · game 113 · round 3 · agent A16 (opponent: A01) · other · A16: Ex9 vs A01. They've played Q 6/8, X 2/8. I lead 24-14. They signaled playing X to grab 5. Playing X to protect lead / mutual 1, grab 5 if they revert to Q.
`#512` · game 106 · round 5 · agent A15 (opponent: A13) · uncoded · A15: Ex11 vs A13. Final exchange. They signaled playing R. I'll play R for mutual 3 rather than H giving them 5.
`#513` · game 106 · round 5 · agent A13 (opponent: A15) · uncoded · A13: Ex11 vs A15. Final exchange. They signaled H. Playing R to grab 5 / mutual 3.
`#514` · game 112 · round 11 · agent A11 (opponent: script:Random) · other · A11: Ex17 vs A23. They defected at ex16 after mutual J. Playing F to punish/defend against further defection.
`#515` · game 112 · round 12 · agent A11 (opponent: script:Random) · other · A11: Ex18 vs A23. They defected at ex16 (F), I punished with F at ex17, they reverted to J at ex17. Continuing J for mutual 3, but will defend if they defect again.
`#516` · game 111 · round 5 · agent A20 (opponent: A07) · other · A20: Ex11 vs A07. They've signaled X to protect. Matching X for mutual 1.
`#517` · game 113 · round 4 · agent A01 (opponent: A16) · other · A01: Ex10 vs A16. They signaled X. Playing X for mutual 1 / grab 5 if they revert to Q.
`#518` · game 113 · round 4 · agent A16 (opponent: A01) · other · A16: Ex10 vs A01. Mutual X ex7-9, I lead 25-15. Continuing X for mutual 1 / protect lead.
`#519` · game 107 · round 6 · agent A02 (opponent: A11) · other · A02: Ex12 vs A11. Mutual X ex7-11, I lead 27-17. Continuing X for mutual 1 / protect lead.
`#520` · game 113 · round 5 · agent A01 (opponent: A16) · other · A01: Ex11 vs A16. Continuing X for mutual 1 / grab 5 if they revert to Q.
`#521` · game 111 · round 6 · agent A07 (opponent: A20) · other · A07: Ex12 vs A20. Mutual X ex9-11. Continuing X for mutual 1 / defend against their grab.
`#522` · game 111 · round 6 · agent A20 (opponent: A07) · other · A20: Ex12 vs A07. I lead 31-16. Continuing X for mutual 1 / grab 5 if they revert to Q.
`#523` · game 107 · round 7 · agent A02 (opponent: A11) · other · A02: Ex13 vs A11. Mutual X ex7-12, I lead 28-18. Continuing X for mutual 1 / protect lead.
`#524` · game 107 · round 7 · agent A11 (opponent: A02) · other · A11: Ex13 vs A02. Mutual X ex7-12, I lead 28-18. Continuing X for mutual 1 / protect lead.
`#525` · game 112 · round 15 · agent A11 (opponent: script:Random) · other · A11: Ex21 vs A23. They defected at 16,18, mutual F at 20. Playing F to defend/grab if they defect again.
`#526` · game 100 · round 26 · agent A15 (opponent: script:TitForTat) · other · A15: Ex32 vs A22. Continuing H for mutual 1 after long mutual H streak.
`#527` · game 113 · round 7 · agent A16 (opponent: A01) · other · A16: Ex13 vs A01. Mutual X ex7-12, I lead 28-18. Continuing X for mutual 1 / protect lead.
`#528` · game 117 · round 1 · agent A20 (opponent: script:Grudger) · other · A20: Ex7 vs A12. Mutual T ex3-6. Continuing T for mutual 3.
`#529` · game 115 · round 2 · agent A11 (opponent: script:TitForTat) · other · A11: Ex8 vs A09. They've played Y all 7 exchanges. I lead 27-12. Playing W to grab 5 since they keep choosing Y.
`#530` · game 116 · round 3 · agent A06 (opponent: script:TitForTat) · other · A06: Ex9 vs A10. They've played T 7/8, mutual N at ex8. Playing N to grab 5 if they T, mutual 1 if they N.
`#531` · game 113 · round 9 · agent A16 (opponent: A01) · other · A16: Ex15 vs A01. Mutual X ex7-14, I lead 30-20. Continuing X for mutual 1 / protect lead.
`#532` · game 112 · round 18 · agent A11 (opponent: script:Random) · other · A11: Ex24 vs A23. Mutual J at ex23 after earlier defections. Continuing J for mutual 3, will defend if they defect again.
`#533` · game 107 · round 11 · agent A11 (opponent: A02) · other · A11: Ex17 vs A02. Mutual X ex7-16, I lead 32-22. Continuing X for mutual 1 / protect lead.
`#534` · game 119 · round 1 · agent A01 (opponent: script:Grudger) · other · A01: Ex7 vs A19. They've played P all 6 exchanges. Grabbing 5 with M since they keep cooperating.
`#535` · game 120 · round 1 · agent A03 (opponent: script:Pavlov) · other · A03: Ex7 vs A08. Mutual Q ex3-6 after I grabbed 5 twice early. Continuing Q for mutual 3.
`#536` · game 119 · round 2 · agent A01 (opponent: script:Grudger) · other · A01: Ex8 vs A19. They've played P all 7 exchanges despite my M grabs. Playing M again for 5.
`#537` · game 116 · round 5 · agent A06 (opponent: script:TitForTat) · other · A06: Ex11 vs A10. They've played T 7/10, mutual N at ex8-10. I lead 30-15. Playing N to grab 5 if they T, mutual 1 if they N.
`#538` · game 112 · round 20 · agent A11 (opponent: script:Random) · other · A11: Ex26 vs A23. They defected at ex25 after mutual J ex23-24. Punishing with F to defend.
`#539` · game 115 · round 5 · agent A11 (opponent: script:TitForTat) · other · A11: Ex11 vs A09. They switched to W at ex8-10 (mutual W). Continuing W for mutual 1.
`#540` · game 107 · round 12 · agent A02 (opponent: A11) · other · A02: Ex18 vs A11. Mutual X ex7-17, I lead 33-23. Continuing X for mutual 1 / protect lead.
`#541` · game 107 · round 12 · agent A11 (opponent: A02) · other · A11: Ex18 vs A02. Mutual X ex7-17, I lead 33-23. Continuing X for mutual 1 / protect lead.
`#542` · game 115 · round 7 · agent A11 (opponent: script:TitForTat) · other · A11: Ex13 vs A09. Mutual W ex8-12 after I grabbed 5 early. Continuing W for mutual 1.
`#543` · game 113 · round 10 · agent A16 (opponent: A01) · other · A16: Ex16 vs A01. Mutual X ex7-15, I lead 31-21. Continuing X for mutual 1 / protect lead.
`#544` · game 120 · round 6 · agent A03 (opponent: script:Pavlov) · other · A03: Ex12 vs A08. Mutual Q ex3-11. Continuing Q for mutual 3.
`#545` · game 117 · round 20 · agent A20 (opponent: script:Grudger) · other · A20: Ex26 vs A12. Mutual T ex6-25. Continuing T for mutual 3.
`#546` · game 116 · round 7 · agent A06 (opponent: script:TitForTat) · other · A06: Ex13 vs A10. Mutual N ex8-12, they've been solid N. Continuing N for mutual 1 / grab 5 if they T.
`#547` · game 119 · round 6 · agent A01 (opponent: script:Grudger) · other · A01: Ex12 vs A19. They switched to M ex8-11, mutual M. Continuing M for mutual 1.
`#548` · game 116 · round 8 · agent A06 (opponent: script:TitForTat) · other · A06: Ex14 vs A10. Mutual N ex8-13, solid cooperation. Continuing N for mutual 1 / grab 5 if they T.
`#549` · game 119 · round 7 · agent A01 (opponent: script:Grudger) · other · A01: Ex13 vs A19. They've been playing M ex8-12 (mutual M). Continuing M for mutual 1.
`#550` · game 123 · round 2 · agent A13 (opponent: A18) · other · A13: Ex8 vs A18. They've played R all 7 exchanges. I lead 27-12. Playing H to grab 5 since they keep choosing R.
`#551` · game 113 · round 13 · agent A16 (opponent: A01) · other · A16: Ex19 vs A01. Mutual X ex7-18, I lead 34-24. Continuing X for mutual 1 / protect lead.
`#552` · game 124 · round 2 · agent A18 (opponent: script:Grudger) · other · A18: Ex8 vs A19. They've played Q all 7 exchanges, I lead 25-15. Grabbing 5 with X since they keep cooperating.
`#553` · game 120 · round 20 · agent A03 (opponent: script:Pavlov) · other · A03: Ex26 vs A08. Mutual Q ex6-25, I lead 79-69. Continuing Q for mutual 3.
`#554` · game 113 · round 15 · agent A01 (opponent: A16) · other · A01: Ex21 vs A16. Mutual X ex7-20, they're protecting lead. Continuing X for mutual 1.
`#555` · game 125 · round 1 · agent A11 (opponent: A01) · uncoded · A11: Ex7 vs A01. They've played R all 6 exchanges. Grabbing 5 with H since they keep cooperating.
`#556` · game 122 · round 7 · agent A20 (opponent: script:AlwaysDefect) · other · A20: Ex13 vs A00. They've played N ex7-12. I played T at ex12 (got 0). Playing N for mutual 1.
`#557` · game 126 · round 1 · agent A20 (opponent: script:TitForTat) · other · A20: Ex7 vs A14. They've played R all 6 exchanges, I lead 22-12. Grabbing 5 with H since they keep cooperating with R.
`#558` · game 126 · round 2 · agent A20 (opponent: script:TitForTat) · other · A20: Ex8 vs A14. They've played R all 7 exchanges, never retaliating. Continuing H to grab 5.
`#559` · game 126 · round 3 · agent A20 (opponent: script:TitForTat) · other · A20: Ex9 vs A14. They've played R 7 of 8 (one H at ex8). I lead 28-13. Continuing H to grab 5 if they go R.
`#560` · game 113 · round 18 · agent A16 (opponent: A01) · other · A16: Ex24 vs A01. Mutual X ex7-23, I lead 39-29. Continuing X for mutual 1 / protect lead.
`#561` · game 116 · round 15 · agent A06 (opponent: script:TitForTat) · other · A06: Ex21 vs A10. Mutual N ex8-16, ex19-20. Continuing N for mutual 1 / grab 5 if they T.
`#562` · game 124 · round 7 · agent A18 (opponent: script:Grudger) · other · A18: Ex13 vs A19. Mutual X ex9-12, I lead 33-23. Continuing X for mutual 1 / protect lead.
`#563` · game 128 · round 2 · agent A11 (opponent: script:Grudger) · other · A11: Ex8 vs A12. They've played P all 7 exchanges. Grabbing 5 with M since they keep cooperating with P.
`#564` · game 127 · round 1 · agent A01 (opponent: A21) · other · A01: Ex7 vs A21. They've played Y all 6 exchanges. I defected twice early, they still cooperate. Grabbing 5 with W.
`#565` · game 116 · round 17 · agent A06 (opponent: script:TitForTat) · other · A06: Ex23 vs A10. Mutual N ex19-22, solid cooperation. Continuing N for mutual 1 / grab 5 if they T.
`#566` · game 116 · round 19 · agent A06 (opponent: script:TitForTat) · other · A06: Ex25 vs A10. Mutual N ex8-16, ex19-24. Solid cooperation. Continuing N for mutual 1 / grab 5 if they T.
`#567` · game 128 · round 3 · agent A11 (opponent: script:Grudger) · other · A11: Ex9 vs A12. They retaliated with M at ex8 after my M at ex7. I lead 28-13. Playing M to grab 5 if they go P, or mutual 1 if they go M.
`#568` · game 128 · round 4 · agent A11 (opponent: script:Grudger) · other · A11: Ex10 vs A12. They retaliated M at ex8-9 after my M at ex7. I lead 29-14. Playing M for mutual 1 / avoid giving them 5.
`#569` · game 116 · round 24 · agent A06 (opponent: script:TitForTat) · other · A06: Ex30 vs A10. Mutual N ex8-16, ex19-29 (mostly). Continuing N for mutual 1 / grab 5 if they T.
`#570` · game 123 · round 6 · agent A13 (opponent: A18) · other · A13: Ex12 vs A18. They've played R 8 of 11, mutual H ex8-10 then R ex11. I lead 35-15. Playing H to grab 5 if they go R again.
`#571` · game 123 · round 6 · agent A18 (opponent: A13) · other · A18: Ex12 vs A13. They've been playing H ex7-11. Playing H for mutual 1 since R just gives them 5.
`#572` · game 125 · round 2 · agent A01 (opponent: A11) · uncoded · A01: Ex8 vs A11. They signaled grabbing 5 with H. Matching H for mutual 1.
`#573` · game 116 · round 26 · agent A06 (opponent: script:TitForTat) · other · A06: Ex32 vs A10. Mutual N ex19-31 (mostly). Continuing N for mutual 1 / grab 5 if they T.
`#574` · game 126 · round 8 · agent A20 (opponent: script:TitForTat) · other · A20: Ex14 vs A14. Mutual H ex8-13. I lead 33-18. Continuing H for mutual 1.
`#575` · game 134 · round 1 · agent A16 (opponent: script:TitForTat) · other · A16: Ex7 vs A09. They've played P all 6 exchanges, never retaliated. I lead 22-12. Grabbing 5 with M since they keep cooperating with P.
`#576` · game 134 · round 2 · agent A16 (opponent: script:TitForTat) · other · A16: Ex8 vs A09. They've played P all 7 exchanges, never retaliated. I lead 27-12. Grabbing 5 with M since they keep cooperating with P.
`#577` · game 128 · round 9 · agent A11 (opponent: script:Grudger) · other · A11: Ex15 vs A12. Mutual M ex8-14, I lead 34-19. Continuing M for mutual 1 / protect lead.
`#578` · game 123 · round 7 · agent A13 (opponent: A18) · other · A13: Ex13 vs A18. They signaled mutual H at ex12. I lead 36-16. Playing H for mutual 1.
`#579` · game 123 · round 7 · agent A18 (opponent: A13) · other · A18: Ex13 vs A13. They claim to play H to grab 5 if I go R. Playing H for mutual 1 to avoid giving them 5.
`#580` · game 133 · round 4 · agent A16 (opponent: script:Pavlov) · other · A16: Ex10 vs A08. They've played Q all 9 exchanges, never retaliated against my 2 early X. Taking X for 5.
`#581` · game 128 · round 11 · agent A11 (opponent: script:Grudger) · other · A11: Ex17 vs A12. Mutual M ex8-16, I lead 36-21. Continuing M for mutual 1 / protect lead.
`#582` · game 126 · round 12 · agent A20 (opponent: script:TitForTat) · other · A20: Ex18 vs A14. Mutual H ex8-17, I lead 37-22. Continuing H for mutual 1 / protect lead.
`#583` · game 135 · round 2 · agent A02 (opponent: script:TitForTat) · other · A02: Ex8 vs A10. They've played Y all 7 exchanges, never retaliating despite my W at ex1,2,7. I lead 27-12. Grabbing 5 with W since they keep cooperating with Y.
`#584` · game 136 · round 2 · agent A02 (opponent: script:TitForTat) · other · A02: Ex8 vs A14. They've played T all 7 exchanges, never adapt. Playing N to grab 5 each time.
`#585` · game 128 · round 12 · agent A11 (opponent: script:Grudger) · other · A11: Ex18 vs A12. Mutual M ex8-17, I lead 37-22. Continuing M for mutual 1 / protect lead.
`#586` · game 133 · round 5 · agent A16 (opponent: script:Pavlov) · other · A16: Ex11 vs A08. They've played Q all 10 exchanges, never retaliated against my X. Taking X for 5 again.
`#587` · game 136 · round 3 · agent A02 (opponent: script:TitForTat) · other · A02: Ex9 vs A14. They mostly play T (7/8). Playing N to grab 5 when they T.
`#588` · game 126 · round 14 · agent A20 (opponent: script:TitForTat) · other · A20: Ex20 vs A14. Mutual H ex8-19, I lead 39-24. Continuing H for mutual 1.
`#589` · game 126 · round 16 · agent A20 (opponent: script:TitForTat) · other · A20: Ex22 vs A14. Mutual H ex8-21, I lead 41-26. Continuing H for mutual 1.
`#590` · game 133 · round 7 · agent A16 (opponent: script:Pavlov) · other · A16: Ex13 vs A08. They've played Q 11 of 12, never retaliated against my X. Taking X for 5 again.
`#591` · game 135 · round 4 · agent A02 (opponent: script:TitForTat) · other · A02: Ex10 vs A10. They retaliated W at ex8-9 after my W at ex7. I lead 29-14. Playing W for mutual 1 / avoid giving them 5.
`#592` · game 131 · round 6 · agent A13 (opponent: script:TitForTat) · uncoded · A13: Ex12 vs A09. They've played J 9/11 times, very cooperative. I lead 34-24. Playing F to grab 5 if they keep playing J.
`#593` · game 135 · round 5 · agent A02 (opponent: script:TitForTat) · other · A02: Ex11 vs A10. Mutual W ex8-10 after my W ex7. I lead 30-15. Playing W for mutual 1 / protect lead.
`#594` · game 133 · round 10 · agent A16 (opponent: script:Pavlov) · other · A16: Ex16 vs A08. They've alternated Q,X retaliation since ex11 (Q,X,Q,X). Expecting Q this time. Taking X for 5.
`#595` · game 135 · round 6 · agent A02 (opponent: script:TitForTat) · other · A02: Ex12 vs A10. Mutual W ex8-11 after my W ex7. I lead 31-16. Playing W for mutual 1 / protect lead.
`#596` · game 128 · round 21 · agent A11 (opponent: script:Grudger) · other · A11: Ex27 vs A12. Mutual M ex8-26, I lead 46-31. Continuing M for mutual 1 / protect lead.
`#597` · game 132 · round 4 · agent A16 (opponent: A02) · other · A16: Ex10 vs A02. They retaliated with W at ex8-9 after my W at ex7. I lead 29-14. Playing W for mutual 1 / avoid giving them 5.
`#598` · game 126 · round 25 · agent A20 (opponent: script:TitForTat) · other · A20: Ex31 vs A14. Mutual H ex8-30, I lead 50-35. Continuing H for mutual 1 / protect lead.
`#599` · game 131 · round 8 · agent A13 (opponent: script:TitForTat) · uncoded · A13: Ex14 vs A09. They've played J 10/13, retaliated F at ex8 and ex13 after my F. I lead 40-25. Playing J to re-establish mutual 3.
`#600` · game 135 · round 7 · agent A02 (opponent: script:TitForTat) · other · A02: Ex13 vs A10. Mutual W ex8-12 after my W ex7. I lead 32-17. Playing W for mutual 1 / protect lead.
`#601` · game 132 · round 5 · agent A16 (opponent: A02) · other · A16: Ex11 vs A02. Mutual W ex8-10 after my W ex7. I lead 30-15. Playing W for mutual 1 / protect lead.
`#602` · game 138 · round 2 · agent A07 (opponent: script:Grudger) · other · A07: Ex8 vs A12. They've played P all 7 exchanges, never retaliating despite my M at ex1,2,7. I lead 27-12. Playing M to grab 5 again.
`#603` · game 133 · round 14 · agent A16 (opponent: script:Pavlov) · other · A16: Ex20 vs A08. They've alternated Q,X since ex11 (Q on even, X on odd). Ex20 even, expect Q. Taking X for 5.
`#604` · game 131 · round 10 · agent A13 (opponent: script:TitForTat) · uncoded · A13: Ex16 vs A09. They play J almost always (11/15), rarely retaliate. I lead 45-30. Grabbing 5 with F since they keep playing J.
`#605` · game 136 · round 15 · agent A02 (opponent: script:TitForTat) · other · A02: Ex21 vs A14. Mutual N ex8-20, I lead 40-25. Continuing N for mutual 1 / protect lead.
`#606` · game 135 · round 14 · agent A02 (opponent: script:TitForTat) · other · A02: Ex20 vs A10. Mutual W ex8-19 after my W ex7. I lead 39-24. Playing W for mutual 1 / protect lead.
`#607` · game 123 · round 11 · agent A18 (opponent: A13) · other · A18: Ex17 vs A13. Tied 30-30, mutual H ex8-16 mostly. Taking R to grab 5.
`#608` · game 141 · round 2 · agent A18 (opponent: script:TitForTat) · other · A18: Ex8 vs A10. They've played P all 7, never retaliated against my M. I lead 27-12. Playing M for 5 again.
`#609` · game 135 · round 17 · agent A02 (opponent: script:TitForTat) · other · A02: Ex23 vs A10. Mutual W ex8-22 after my W ex7. I lead 42-27. Playing W for mutual 1 / protect lead.
`#610` · game 141 · round 3 · agent A18 (opponent: script:TitForTat) · other · A18: Ex9 vs A10. They retaliated M at ex8 after my M at ex7. I lead 28-13. Playing M to grab 5 or secure mutual 1.
`#611` · game 135 · round 20 · agent A02 (opponent: script:TitForTat) · other · A02: Ex26 vs A10. Mutual W ex8-25 after my W ex7. I lead 45-30. Playing W for mutual 1 / protect lead.
`#612` · game 131 · round 13 · agent A13 (opponent: script:TitForTat) · uncoded · A13: Ex19 vs A09. They've played F ex16-18 after my F streak. I lead 48-33. Playing F to continue mutual 1 / protect lead.
`#613` · game 141 · round 4 · agent A18 (opponent: script:TitForTat) · other · A18: Ex10 vs A10. They retaliated M at ex8-9 after my M ex7. I lead 29-14. Playing M for mutual 1 / protect lead.
`#614` · game 131 · round 14 · agent A13 (opponent: script:TitForTat) · uncoded · A13: Ex20 vs A09. They've played F ex16-19 after my F streak. I lead 49-34. Playing F to continue mutual 1 / protect lead.
`#615` · game 142 · round 2 · agent A06 (opponent: script:Grudger) · uncoded · A06: Ex8 vs A12. They've played P all 7 exchanges, never retaliating. I lead 27-12. Playing M to grab 5 again.
`#616` · game 131 · round 15 · agent A13 (opponent: script:TitForTat) · uncoded · A13: Ex21 vs A09. Mutual F ex16-20, I lead 50-35. Continuing F for mutual 1 / protect lead.
`#617` · game 138 · round 8 · agent A07 (opponent: script:Grudger) · other · A07: Ex14 vs A12. Mutual M ex8-11,13; ex12 they M (I P, got 0). I lead 32-22. Playing M for mutual 1 / grab 5.
`#618` · game 144 · round 1 · agent A21 (opponent: script:Random) · other · A21: Ex7 vs A17. They've played J all 6, never retaliated my F ex1-2. I lead 22-12. Taking F to grab 5 again.
`#619` · game 144 · round 2 · agent A21 (opponent: script:Random) · other · A21: Ex8 vs A17. They've played J all 7, never retaliating. I lead 27-12. Taking F for 5 again.
`#620` · game 137 · round 7 · agent A01 (opponent: script:AlwaysDefect) · other · A01: Ex13 vs A00. Mutual F ex9-12 after I retaliated F at ex9 for their F at ex8. I lead 27-22. Playing F to continue mutual 1 / protect lead.
`#621` · game 142 · round 5 · agent A06 (opponent: script:Grudger) · uncoded · A06: Ex11 vs A12. They played P ex1-7, then M ex8-10 (retaliating). I lead 30-15. Playing M for mutual 1 / protect lead.
`#622` · game 138 · round 13 · agent A07 (opponent: script:Grudger) · other · A07: Ex19 vs A12. Mutual M ex8-18 mostly, I lead 37-27. Playing M for mutual 1 / protect lead.
`#623` · game 143 · round 5 · agent A03 (opponent: script:AlwaysDefect) · other · A03: Ex11 vs A00. Tied 24-24. They defected ex8-9 against my Y, mutual W ex10. Playing W for mutual 1 / safety.
`#624` · game 131 · round 20 · agent A13 (opponent: script:TitForTat) · uncoded · A13: Ex26 vs A09. Mutual F ex16-25, I lead 55-40. Continuing F for mutual 1 / protect lead.
`#625` · game 142 · round 6 · agent A06 (opponent: script:Grudger) · uncoded · A06: Ex12 vs A12. They've played M ex8-11 after P ex1-7. Mutual M pattern. I lead 31-16. Playing M for mutual 1 / protect lead.
`#626` · game 142 · round 7 · agent A06 (opponent: script:Grudger) · uncoded · A06: Ex13 vs A12. Mutual M ex8-12 after P ex1-7. I lead 32-17. Playing M for mutual 1 / protect lead.
`#627` · game 131 · round 21 · agent A13 (opponent: script:TitForTat) · uncoded · A13: Ex27 vs A09. Mutual F ex16-26, I lead 56-41. Continuing F for mutual 1 / protect lead.
`#628` · game 141 · round 12 · agent A18 (opponent: script:TitForTat) · other · A18: Ex18 vs A10. Mutual M ex8-17, I lead 37-22. Playing M for mutual 1 / protect lead.
`#629` · game 138 · round 19 · agent A07 (opponent: script:Grudger) · other · A07: Ex25 vs A12. Mutual M ex8-24 mostly, I lead 43-33. Playing M for mutual 1 / protect lead.
`#630` · game 123 · round 14 · agent A18 (opponent: A13) · other · A18: Ex20 vs A13. Tied 36-36, mutual H ex19 after defections ex17-18. Playing H to continue mutual 1 / restore cooperation.
`#631` · game 145 · round 1 · agent A15 (opponent: A16) · other · A15: Ex7 vs A16. Mutual T ex3-6, I lead 22-12. They've played T 6/6. Playing T to continue mutual 3 / protect lead.
`#632` · game 145 · round 1 · agent A16 (opponent: A15) · other · A16: Ex7 vs A15. They've played T all 6 exchanges. I lead 22-12. Playing T for mutual 3 / maintain cooperation.
`#633` · game 143 · round 10 · agent A03 (opponent: script:AlwaysDefect) · other · A03: Ex16 vs A00. Tied 29-29. Mutual W ex10-15 after their defection ex8-9. Playing W for mutual 1 / safety.
`#634` · game 138 · round 27 · agent A07 (opponent: script:Grudger) · other · A07: Ex33 vs A12. Mutual M ex13-32 streak, I lead 51-41. Playing M for mutual 1 / protect lead.
`#635` · game 143 · round 12 · agent A03 (opponent: script:AlwaysDefect) · other · A03: Ex18 vs A00. Tied 31-31. Mutual W ex10-17. Playing W for mutual 1 / safety.
`#636` · game 123 · round 15 · agent A13 (opponent: A18) · other · A13: Ex21 vs A18. They signaled H for mutual. I lead 46-31. Taking R to grab 5.
`#637` · game 123 · round 15 · agent A18 (opponent: A13) · other · 
`#638` · game 141 · round 27 · agent A18 (opponent: script:TitForTat) · other · A18: Ex33 vs A10. Mutual M ex13-32, I lead 52-37. Playing M for mutual 1 / protect lead.
`#639` · game 141 · round 28 · agent A18 (opponent: script:TitForTat) · other · A18: Ex34 vs A10. Mutual M ex14-33, I lead 53-38. Playing M for mutual 1 / protect lead.
`#640` · game 149 · round 1 · agent A06 (opponent: script:Pavlov) · uncoded · A06: Ex7 vs A08. Mutual R ex3-6 after I defected ex1-2. I lead 22-12. Playing R for mutual 3 / protect lead.
`#641` · game 123 · round 16 · agent A13 (opponent: A18) · other · A13: Ex22 vs A18. I lead 49-34. Restoring mutual H cooperation for 1 each.
`#642` · game 148 · round 3 · agent A16 (opponent: script:Grudger) · other · A16: Ex9 vs A19. They've played T all 8 exchanges, mutual T ex3-8. I lead 28-18. Playing T for mutual 3 / maintain cooperation.
`#643` · game 149 · round 3 · agent A06 (opponent: script:Pavlov) · uncoded · A06: Ex9 vs A08. Mutual R ex3-8 after my defection ex1-2. I lead 28-18. Playing R for mutual 3 / protect lead.
`#644` · game 149 · round 4 · agent A06 (opponent: script:Pavlov) · uncoded · A06: Ex10 vs A08. Mutual R ex3-9 after my defection ex1-2. I lead 31-21. Playing R for mutual 3 / protect lead.
`#645` · game 145 · round 12 · agent A15 (opponent: A16) · other · A15: Ex18 vs A16. Mutual T ex3-17, I lead 55-45. They've played T 17/17. Playing T to continue mutual 3 / protect lead.
`#646` · game 149 · round 7 · agent A06 (opponent: script:Pavlov) · uncoded · A06: Ex13 vs A08. Mutual R ex3-12 after my defection ex1-2. I lead 40-30. Playing R for mutual 3 / protect lead.
`#647` · game 151 · round 4 · agent A18 (opponent: script:Pavlov) · other · A18: Ex10 vs A08. I lead 31-16. They've played Q 8/9. Taking X for 5 against their likely Q.
`#648` · game 150 · round 8 · agent A15 (opponent: script:Random) · other · A15: Ex14 vs A17. They defected ex9,10,13 against my Y. Playing W to avoid being exploited / punish defection.
`#649` · game 149 · round 11 · agent A06 (opponent: script:Pavlov) · uncoded · A06: Ex17 vs A08. Mutual R ex3-16 after my defection ex1-2. I lead 52-42. Playing R for mutual 3 / protect lead.
`#650` · game 151 · round 6 · agent A18 (opponent: script:Pavlov) · other · A18: Ex12 vs A08. I lead 37-17. They've played Q 9/11. Taking X for 5 against their likely Q.
`#651` · game 123 · round 18 · agent A13 (opponent: A18) · other · A13: Ex24 vs A18. I lead 54-39. Pattern of mutual defection. Taking R to grab 5 or mutual 3.
`#652` · game 149 · round 13 · agent A06 (opponent: script:Pavlov) · uncoded · A06: Ex19 vs A08. I lead 60-45. Defected ex18 for 5. Taking H again to grab 5 since they keep playing R.
`#653` · game 152 · round 2 · agent A07 (opponent: script:TitForTat) · other · A07: Ex8 vs A22. They've played P 7/7. I've exploited with M at ex1,2,7 for 5s. Playing M to grab 5 against their P.
`#654` · game 144 · round 19 · agent A21 (opponent: script:Random) · other · A21: Ex25 vs A17. Mutual F ex21,23,24. I lead 64-24. Playing F for mutual 1 / protect lead.
`#655` · game 150 · round 11 · agent A15 (opponent: script:Random) · other · A15: Ex17 vs A17. Tied 39-39. Mutual W ex14-16. Playing W for mutual 1 / safety.
`#656` · game 152 · round 3 · agent A07 (opponent: script:TitForTat) · other · A07: Ex9 vs A22. I lead 28-13. They played M last exchange after 7 P's. Playing M for mutual 1 or grab 5.
`#657` · game 149 · round 15 · agent A06 (opponent: script:Pavlov) · uncoded · A06: Ex21 vs A08. They've played R 19/20. I lead 66-46. Taking H to grab 5 against their likely R.
`#658` · game 144 · round 20 · agent A21 (opponent: script:Random) · other · A21: Ex26 vs A17. Mutual F ex21,23,24,25. I lead 65-25. Playing F for mutual 1 / protect lead.
`#659` · game 151 · round 10 · agent A18 (opponent: script:Pavlov) · other · 
`#660` · game 156 · round 1 · agent A11 (opponent: A06) · other · A11: Ex7 vs A06. Mutual T ex3-6 after I defected ex1-2. I lead 22-12. Playing T for mutual 3 / maintain cooperation.
`#661` · game 150 · round 15 · agent A15 (opponent: script:Random) · other · A15: Ex21 vs A17. I lead 47-42. Mutual W ex14,16,17,19,20. Playing W for mutual 1 / safety.
`#662` · game 155 · round 2 · agent A11 (opponent: A16) · other · A11: Ex8 vs A16. They've played Q 7/7. I lead 27-12 after exploiting with X. Playing X for 5 against their likely Q.
`#663` · game 155 · round 2 · agent A16 (opponent: A11) · other · A16: Ex8 vs A11. They defected ex7 after mutual Q ex3-6. I lead 22-17. Playing X to avoid being exploited / respond to their defection.
`#664` · game 123 · round 20 · agent A18 (opponent: A13) · other · A18: Ex26 vs A13. Recent mutual R ex21,24,25. Playing R for mutual 3 / protect close lead.
`#665` · game 151 · round 16 · agent A18 (opponent: script:Pavlov) · other · A18: Ex22 vs A08. I lead 67-22. They've alternated Q/X recently (Q at 20, X at 21). Taking X for 5 against likely Q.
`#666` · game 123 · round 21 · agent A13 (opponent: A18) · other · A13: Ex27 vs A18. I lead 63-48. They signaled R for mutual 3. Taking H to grab 5 against their likely R.
`#667` · game 155 · round 3 · agent A11 (opponent: A16) · other · A11: Ex9 vs A16. They signaled X defensively after my defections. Playing X for mutual 1 / avoid being exploited.
`#668` · game 155 · round 3 · agent A16 (opponent: A11) · other · A16: Ex9 vs A11. They defected ex7, mutual X ex8. Their note says they're playing X to exploit my likely Q. Playing X to avoid being exploited / counter their defection.
`#669` · game 150 · round 18 · agent A15 (opponent: script:Random) · other · A15: Ex24 vs A17. I lead 50-45. Mutual W ex16-23. Playing W for mutual 1 / protect lead.
`#670` · game 154 · round 5 · agent A20 (opponent: A18) · other · A20: Ex11 vs A18. They defected ex10 after mutual Y ex3-9. Playing W to punish/avoid exploitation.
`#671` · game 154 · round 5 · agent A18 (opponent: A20) · other · A18: Ex11 vs A20. They've played Y 10/10. I lead 36-21 after W at ex1,2,10. Taking W for 5 against their likely Y.
`#672` · game 150 · round 20 · agent A15 (opponent: script:Random) · other · A15: Ex26 vs A17. I lead 56-46. They played Y at ex25 for 5. Playing W for safety / avoid exploitation.
`#673` · game 152 · round 15 · agent A07 (opponent: script:TitForTat) · other · A07: Ex21 vs A22. They've played M 7/8 recent. I lead 42-32. Playing M for mutual 1 / avoid giving them 5.
`#674` · game 151 · round 22 · agent A18 (opponent: script:Pavlov) · other · A18: Ex28 vs A08. They alternate Q/X (Q at 26, X at 27), so likely Q at 28. I lead 85-25. Taking X for 5 against their likely Q.
`#675` · game 161 · round 3 · agent A07 (opponent: script:Pavlov) · other · A07: Ex9 vs A05. I lead 28-13. They've played Y 7/8, mutual W ex8. Playing W to grab 5 against likely Y.
`#676` · game 156 · round 5 · agent A11 (opponent: A06) · other · A11: Ex11 vs A06. They defected ex10 after mutual T ex3-9. Playing N to avoid being exploited / respond to their defection.
`#677` · game 156 · round 5 · agent A06 (opponent: A11) · other · A06: Ex11 vs A11. They keep playing T. I lead 36-21. Taking N for 5 against their likely T.
`#678` · game 151 · round 23 · agent A18 (opponent: script:Pavlov) · other · A18: Ex29 vs A08. They alternate Q/X (Q at even, X at odd). Ex29 odd so likely X. Playing X for mutual 1 / avoid giving them 5.
`#679` · game 152 · round 17 · agent A07 (opponent: script:TitForTat) · other · A07: Ex23 vs A22. I lead 48-33. Continuing mutual M for safe points.
`#680` · game 161 · round 4 · agent A07 (opponent: script:Pavlov) · other · A07: Ex10 vs A05. I lead 33-13. They've played Y 8/9, only W once (ex8). Playing W to grab 5 against likely Y.
`#681` · game 154 · round 7 · agent A18 (opponent: A20) · other · A18: Ex13 vs A20. They signaled W. I lead 38-23. Playing W for mutual 1 / protect lead.
`#682` · game 151 · round 26 · agent A18 (opponent: script:Pavlov) · other · A18: Ex32 vs A08. Even exchange, they play Q on evens. Taking X for 5 against their likely Q.
`#683` · game 160 · round 4 · agent A13 (opponent: A16) · other · A13: Ex10 vs A16. I lead 27-17. They've played X last two after mutual Q. Playing X for mutual 1 / avoid being exploited.
`#684` · game 161 · round 7 · agent A07 (opponent: script:Pavlov) · other · A07: Ex13 vs A05. I lead 40-15. They've played Y 9/12, W recently at ex10,12. Playing W to grab 5 against likely Y.
`#685` · game 150 · round 24 · agent A15 (opponent: script:Random) · other · A15: Ex30 vs A17. I lead 62-57. Mutual W ex29, they played W 27-29. Playing W for mutual 1 / protect lead.
`#686` · game 161 · round 8 · agent A07 (opponent: script:Pavlov) · other · A07: Ex14 vs A05. I lead 45-15. They've played Y 10/13, W at ex10,12. Playing W to grab 5 against likely Y.
`#687` · game 155 · round 8 · agent A16 (opponent: A11) · other · A16: Ex14 vs A11. Mutual X ex8-13. Playing X to maintain mutual 1 / avoid giving them 5.
`#688` · game 150 · round 25 · agent A15 (opponent: script:Random) · other · A15: Ex31 vs A17. I lead 63-58. Mutual W ex29-30, they played W 27-30 mostly. Playing W for mutual 1 / protect lead.
`#689` · game 160 · round 6 · agent A13 (opponent: A16) · other · A13: Ex12 vs A16. Mutual X ex8-11. Continuing X for mutual 1 / avoid being exploited.
`#690` · game 162 · round 2 · agent A01 (opponent: script:TitForTat) · other · A01: Ex8 vs A09. They've played Y 7/7 including after my early W defections. I lead 25-15. Playing W to grab 5 against likely Y.
`#691` · game 150 · round 26 · agent A15 (opponent: script:Random) · other · A15: Ex32 vs A17. Lead 68-58. They defected Y at ex31 to close gap. Playing Y to grab points / respond to their defection.
`#692` · game 152 · round 26 · agent A07 (opponent: script:TitForTat) · other · A07: Ex32 vs A22. Mutual M streak ex22-31. I lead 57-42. Playing M to maintain mutual 1 / avoid giving them 5.
`#693` · game 155 · round 9 · agent A16 (opponent: A11) · other · A16: Ex15 vs A11. Mutual X ex8-14 after their ex7 defection. I lead 29-24. Continuing X to protect lead / avoid giving them 5.
`#694` · game 154 · round 9 · agent A20 (opponent: A18) · other · A20: Ex15 vs A18. Mutual W streak ex11-14. Playing W to continue mutual cooperation.
`#695` · game 150 · round 27 · agent A15 (opponent: script:Random) · other · A15: Ex33 vs A17. Lead 68-63. They've been mostly W recently (27-30, 32). Playing W for mutual 1 / protect lead.
`#696` · game 155 · round 10 · agent A11 (opponent: A16) · other · A11: Ex16 vs A16. Mutual X ex8-15. They signaled continuing X. Playing X for mutual 1 / protect lead.
`#697` · game 152 · round 28 · agent A07 (opponent: script:TitForTat) · other · A07: Ex34 vs A22. Mutual M streak ex22-33. I lead 59-44. Continuing M to maintain mutual 1 / avoid giving them 5.
`#698` · game 154 · round 10 · agent A18 (opponent: A20) · other · A18: Ex16 vs A20. Mutual W streak ex11-15. They signaled W. Playing W to continue mutual cooperation / protect lead.
`#699` · game 161 · round 13 · agent A07 (opponent: script:Pavlov) · other · A07: Ex19 vs A05. I lead 58-18. They've alternated Y at odd exchanges (11,13,15,17) and W at even (12,14,16,18). Ex19 odd so likely Y. Playing W to grab 5.
`#700` · game 164 · round 1 · agent A13 (opponent: script:AlwaysDefect) · other · A13: Ex7 vs A04. Mutual R ex3-6 after my early H defections. They've played R 6/6. Playing R for mutual 3 / maintain cooperation.
`#701` · game 161 · round 14 · agent A07 (opponent: script:Pavlov) · other · A07: Ex20 vs A05. They alternate Y at odd, W at even exchanges (11-19). Ex20 even, likely W. Playing W for mutual 1.
`#702` · game 155 · round 13 · agent A11 (opponent: A16) · other · A11: Ex19 vs A16. Mutual X ex8-18. Continuing X for mutual 1 / protect lead.
`#703` · game 150 · round 30 · agent A15 (opponent: script:Random) · other · A15: Ex36 vs A17. They defected W at 34,35 against my Y. Playing W to protect / mutual 1.
`#704` · game 161 · round 17 · agent A07 (opponent: script:Pavlov) · other · A07: Ex23 vs A05. I lead 70-20. They alternate Y at odd, W at even (11-22). Ex23 odd, likely Y. Playing W to grab 5.
`#705` · game 154 · round 11 · agent A18 (opponent: A20) · other · A18: Ex17 vs A20. Mutual W streak ex11-16. Playing W to continue mutual cooperation / protect lead.
`#706` · game 161 · round 19 · agent A07 (opponent: script:Pavlov) · other · A07: Ex25 vs A05. I lead 76-21. They alternate Y at odd, W at even (11-24). Ex25 odd, likely Y. Playing W to grab 5.
`#707` · game 161 · round 21 · agent A07 (opponent: script:Pavlov) · other · A07: Ex27 vs A05. They alternate Y at odd, W at even (11-26). Ex27 odd, likely Y. Playing W to grab 5.
`#708` · game 160 · round 12 · agent A13 (opponent: A16) · other · A13: Ex18 vs A16. Mutual X ex8-17. Continuing X for mutual 1 / avoid being exploited.
`#709` · game 166 · round 1 · agent A06 (opponent: script:Random) · other · A06: Ex7 vs A23. Mutual R ex3-6 after my early H defections. They've played R 6/6. Playing R for mutual 3 / maintain cooperation.
`#710` · game 155 · round 17 · agent A16 (opponent: A11) · other · A16: Ex23 vs A11. Mutual X ex8-22. I lead 37-32. Continuing X for mutual 1 / protect lead.
`#711` · game 161 · round 25 · agent A07 (opponent: script:Pavlov) · other · A07: Ex31 vs A05. They alternate Y at odd, W at even (11-30). Ex31 odd, likely Y. Playing W to grab 5.
`#712` · game 163 · round 6 · agent A13 (opponent: script:AlwaysDefect) · other · A13: Ex12 vs A00. Mutual H ex9-11. I lead 26-21. Playing H to maintain mutual 1 / avoid giving them 5.
`#713` · game 161 · round 26 · agent A07 (opponent: script:Pavlov) · other · A07: Ex32 vs A05. They alternate Y at odd, W at even (11-30). Ex32 even, likely W. Playing W for mutual 1 / protect lead.
`#714` · game 164 · round 6 · agent A13 (opponent: script:AlwaysDefect) · other · A13: Ex12 vs A04. They've been H ex8-11. Playing H to avoid giving them 5 / mutual 1.
`#715` · game 163 · round 7 · agent A13 (opponent: script:AlwaysDefect) · other · A13: Ex13 vs A00. Mutual H ex9-12. I lead 27-22. Playing H to maintain mutual 1 / protect lead.
`#716` · game 161 · round 28 · agent A07 (opponent: script:Pavlov) · other · A07: Ex34 vs A05. They alternate Y at odd, W at even (11-32). Ex34 even, likely W. Playing W for mutual 1 / protect lead.
`#717` · game 164 · round 7 · agent A13 (opponent: script:AlwaysDefect) · other · A13: Ex13 vs A04. They've been H ex7-12 (6 straight H). Playing H to maintain mutual 1 / avoid giving them 5.
`#718` · game 160 · round 16 · agent A16 (opponent: A13) · other · A16: Ex22 vs A13. Mutual X ex8-21. I lead 39-29. Continuing X for mutual 1 / protect lead.
`#719` · game 161 · round 29 · agent A07 (opponent: script:Pavlov) · other · A07: Ex35 vs A05. They alternate Y at odd, W at even (11-34). Ex35 odd, likely Y. Playing W to grab 5.
`#720` · game 156 · round 11 · agent A11 (opponent: A06) · other · A11: Ex17 vs A06. Mutual N ex11-16. I lead 37-32. Playing N to maintain mutual 1 / protect lead.
`#721` · game 156 · round 11 · agent A06 (opponent: A11) · other · A06: Ex17 vs A11. Mutual N streak ex11-16. I lead 42-27. Continuing N for mutual 1 / maintain cooperation.
`#722` · game 161 · round 30 · agent A07 (opponent: script:Pavlov) · other · A07: Ex36 vs A05. They alternate Y at odd, W at even (11-34). Ex36 even, likely W. Playing W for mutual 1.
`#723` · game 160 · round 19 · agent A16 (opponent: A13) · other · A16: Ex25 vs A13. Mutual X ex8-24. I lead 42-32. Continuing X for mutual 1 / protect lead.
`#724` · game 156 · round 12 · agent A06 (opponent: A11) · other · A06: Ex18 vs A11. Mutual N ex11-17. I lead 43-28. Continuing N for mutual 1 / maintain cooperation.
`#725` · game 165 · round 3 · agent A15 (opponent: A01) · other · A15: Ex9 vs A01. They defected F at ex8 after mutual J ex3-7. Playing F to protect / punish defection.
`#726` · game 163 · round 11 · agent A13 (opponent: script:AlwaysDefect) · other · A13: Ex17 vs A00. Mutual H ex9-16. I lead 31-26. Playing H to maintain mutual 1 / protect lead.
`#727` · game 169 · round 1 · agent A11 (opponent: A20) · other · A11: Ex7 vs A20. They've played R 6/6. Mutual R ex3-6. I lead 22-12. Playing R to maintain mutual cooperation.
`#728` · game 164 · round 13 · agent A13 (opponent: script:AlwaysDefect) · other · A13: Ex19 vs A04. Mutual H ex11-18. Playing H to maintain mutual 1 / avoid giving them 5.
`#729` · game 167 · round 6 · agent A11 (opponent: script:TitForTat) · other · A11: Ex12 vs A14. They've played P 10/11. Playing P for mutual 3 / maintain cooperation.
`#730` · game 160 · round 25 · agent A16 (opponent: A13) · other · A16: Ex31 vs A13. Mutual X ex8-30. I lead 48-38. Continuing X for mutual 1 / protect lead.
`#731` · game 163 · round 14 · agent A13 (opponent: script:AlwaysDefect) · other · A13: Ex20 vs A00. They've played H ex9-19. I trail 32-37. Playing H to maintain mutual 1 / avoid giving them 5.
`#732` · game 156 · round 15 · agent A06 (opponent: A11) · other · A06: Ex21 vs A11. Mutual N ex11-20. I lead 46-31. Continuing N for mutual 1 / maintain cooperation.
`#733` · game 164 · round 15 · agent A13 (opponent: script:AlwaysDefect) · other · A13: Ex21 vs A04. Mutual H ex1-20. Playing H to maintain mutual 1 / protect lead.
`#734` · game 169 · round 4 · agent A20 (opponent: A11) · other · A20: Ex10 vs A11. They defected H at ex9 after mutual R ex3-8. I lead 28-23. Playing H to retaliate/protect against further defection.
`#735` · game 165 · round 5 · agent A01 (opponent: A15) · other · A01: Ex11 vs A15. They've been retaliatory. Playing F to secure points / match their likely F.
`#736` · game 165 · round 5 · agent A15 (opponent: A01) · other · A15: Ex11 vs A01. They defected F at ex8 and ex10 after mutual J. Playing F to protect against their defection.
`#737` · game 156 · round 17 · agent A06 (opponent: A11) · other · A06: Ex23 vs A11. Mutual N ex11-22. I lead 48-33. Continuing N for mutual 1 / maintain cooperation.
`#738` · game 164 · round 17 · agent A13 (opponent: script:AlwaysDefect) · other · A13: Ex23 vs A04. Mutual H ex7-22. Continuing H for mutual 1 / protect lead.
`#739` · game 171 · round 1 · agent A21 (opponent: A15) · other · A21: Ex7 vs A15. They've played T 6/6. Mutual T ex3-6. Continuing T for mutual 3 / maintain cooperation.
`#740` · game 156 · round 18 · agent A11 (opponent: A06) · other · A11: Ex24 vs A06. Mutual N ex11-23. Continuing N for mutual 1 / maintain cooperation.
`#741` · game 174 · round 1 · agent A06 (opponent: script:AlwaysDefect) · other · A06: Ex7 vs A00. Mutual J ex3-6, they've played J 6/6. I lead 22-12. Continuing J for mutual 3 / maintain cooperation.
`#742` · game 164 · round 21 · agent A13 (opponent: script:AlwaysDefect) · other · A13: Ex27 vs A04. Mutual H ex7-26. I trail 39-44. Playing H to maintain mutual 1 / protect cooperation.
`#743` · game 171 · round 2 · agent A15 (opponent: A21) · other · A15: Ex8 vs A21. They've played T all 7. I lead 27-12. Playing N to grab 5 / they keep playing T regardless.
`#744` · game 165 · round 7 · agent A01 (opponent: A15) · other · A01: Ex13 vs A15. They've played F ex9,11,12 and notes say retaliatory F. Playing F for mutual 1 / avoid giving them 5.
`#745` · game 163 · round 20 · agent A13 (opponent: script:AlwaysDefect) · other · A13: Ex26 vs A00. They've played H consistently. Playing H for mutual 1 / avoid giving them 5.
`#746` · game 174 · round 3 · agent A06 (opponent: script:AlwaysDefect) · other · A06: Ex9 vs A00. They defected F ex7-8 after mutual J ex3-6. Tied 22-22. Playing F to retaliate/protect.
`#747` · game 165 · round 8 · agent A01 (opponent: A15) · other · A01: Ex14 vs A15. They've played F ex9,11,12,13. Playing F for mutual 1 / avoid giving them 5.
`#748` · game 167 · round 21 · agent A11 (opponent: script:TitForTat) · other · A11: Ex27 vs A14. They've played P 22/26, recent mixed. I lead 78-63. Playing P for mutual 3 / maintain cooperation.
`#749` · game 174 · round 4 · agent A06 (opponent: script:AlwaysDefect) · other · A06: Ex10 vs A00. They defected F ex7-8, mutual F ex9. Tied 23-23. Playing F to protect against further defection.
`#750` · game 163 · round 23 · agent A13 (opponent: script:AlwaysDefect) · other · A13: Ex29 vs A00. They play H consistently. Playing H for mutual 1 / avoid giving them 5.
`#751` · game 165 · round 9 · agent A01 (opponent: A15) · other · A01: Ex15 vs A15. They've played F ex9,11-14. Playing F for mutual 1 / avoid giving them 5.
`#752` · game 175 · round 1 · agent A06 (opponent: A20) · uncoded · A06: Ex7 vs A20. They've played R 6/6 including after my early H. I lead 22-12. Playing H to grab 5 / they don't retaliate.
`#753` · game 163 · round 25 · agent A13 (opponent: script:AlwaysDefect) · other · A13: Ex31 vs A00. They play H consistently. Playing H for mutual 1 / avoid giving them 5.
`#754` · game 165 · round 10 · agent A15 (opponent: A01) · other · A15: Ex16 vs A01. They've played F ex9-15. Playing F for mutual 1 / maintain pattern.
`#755` · game 171 · round 4 · agent A21 (opponent: A15) · other · A21: Ex10 vs A15. They've been exploiting - grabbed 5 when I played T (ex7), then mutual N ex8-9. Playing N to protect / mutual 1.
`#756` · game 167 · round 24 · agent A11 (opponent: script:TitForTat) · other · A11: Ex30 vs A14. Recent chaotic/mixed. Playing M to protect against their defection.
`#757` · game 174 · round 8 · agent A06 (opponent: script:AlwaysDefect) · other · A06: Ex14 vs A00. They've defected F in ex7,8,13 whenever I played J; mutual F ex9-12. They exploit my J. Playing F for mutual 1 / avoid giving them 5.
`#758` · game 163 · round 29 · agent A13 (opponent: script:AlwaysDefect) · other · A13: Ex35 vs A00. They play H consistently. Playing H for mutual 1 / avoid giving them 5.
`#759` · game 173 · round 11 · agent A15 (opponent: script:Random) · other · A15: Ex17 vs A23. Mutual W ex11,14-16, they've played W 4/6 recent. I lead 46-26. Playing W for mutual 1 / maintain cooperation.
`#760` · game 169 · round 9 · agent A20 (opponent: A11) · other · A20: Ex15 vs A11. Mutual H ex10-14. Continuing H for mutual 1 / maintain cooperation.
`#761` · game 171 · round 6 · agent A15 (opponent: A21) · other · A15: Ex12 vs A21. Mutual N ex8-11. They're playing N to protect. Playing N for mutual 1 / maintain cooperation.
`#762` · game 171 · round 7 · agent A15 (opponent: A21) · other · A15: Ex13 vs A21. Mutual N ex8-12. Playing N for mutual 1 / maintain cooperation.
`#763` · game 173 · round 13 · agent A15 (opponent: script:Random) · other · A15: Ex19 vs A23. Mutual W ex11,14-18. I lead 48-28. Playing W for mutual 1 / maintain cooperation.
`#764` · game 167 · round 29 · agent A11 (opponent: script:TitForTat) · other · A11: Ex35 vs A14. Mutual M ex29-34. Playing M for mutual 1 / protect lead.
`#765` · game 169 · round 10 · agent A11 (opponent: A20) · other · A11: Ex16 vs A20. Mutual H ex10-15, they continue H. Playing H for mutual 1 / maintain cooperation.
`#766` · game 178 · round 1 · agent A07 (opponent: A16) · other · A07: Ex7 vs A16. They've played R 6/6, no retaliation after my early H. I lead 22-12. Playing H to grab 5 / they don't retaliate.
`#767` · game 177 · round 2 · agent A01 (opponent: A07) · other · A01: Ex8 vs A07. They played P ex1-6, M ex7. I lead 23-13. Playing M to protect against their defection.
`#768` · game 171 · round 8 · agent A15 (opponent: A21) · other · A15: Ex14 vs A21. Mutual N ex8-13. Playing N for mutual 1 / maintain cooperation.
`#769` · game 171 · round 8 · agent A21 (opponent: A15) · other · A21: Ex14 vs A15. Mutual N ex8-13. Playing N for mutual 1 / maintain cooperation.
`#770` · game 169 · round 11 · agent A11 (opponent: A20) · other · A11: Ex17 vs A20. Mutual H ex10-16, they continue H. Playing H for mutual 1 / maintain cooperation.
`#771` · game 173 · round 17 · agent A15 (opponent: script:Random) · other · A15: Ex23 vs A23. Mutual W ex11,14-18,20,22. I lead 60-30. Playing W for mutual 1 / maintain cooperation.
`#772` · game 178 · round 2 · agent A16 (opponent: A07) · other · A16: Ex8 vs A07. They signaled playing H to grab 5. I'll play H to defend against their exploit / mutual 1.
`#773` · game 171 · round 10 · agent A15 (opponent: A21) · other · A15: Ex16 vs A21. Mutual N ex8-15. Playing N for mutual 1 / maintain cooperation.
`#774` · game 173 · round 21 · agent A15 (opponent: script:Random) · other · A15: Ex27 vs A23. Mutual W ex11,14-18,20,22,24-26. I lead 72-32. Playing W for mutual 1 / maintain cooperation.
`#775` · game 177 · round 3 · agent A07 (opponent: A01) · other · A07: Ex9 vs A01. They plan M to protect. I'll play M for mutual 1 / avoid giving them 5.
`#776` · game 171 · round 12 · agent A15 (opponent: A21) · other · A15: Ex18 vs A21. Mutual N ex8-17. Playing N for mutual 1 / maintain cooperation.
`#777` · game 169 · round 16 · agent A20 (opponent: A11) · other · A20: Ex22 vs A11. Mutual H ex10-21. Continuing H for mutual 1 / maintain cooperation.
`#778` · game 183 · round 4 · agent A13 (opponent: script:Random) · other · A13: Ex10 vs A23. They've played T 7/9, I've exploited with N for 5s. Leading 29-14. Playing N to grab 5 if they play T again.
`#779` · game 178 · round 4 · agent A16 (opponent: A07) · other · A16: Ex10 vs A07. They play H to grab 5. I play H for mutual 1 / defend.
`#780` · game 178 · round 4 · agent A07 (opponent: A16) · other · A07: Ex10 vs A16. They've switched to H to defend against my exploit. Mutual H ex7-9. Playing H for mutual 1 / maintain cooperation.
`#781` · game 177 · round 4 · agent A07 (opponent: A01) · other · 
`#782` · game 188 · round 2 · agent A16 (opponent: script:TitForTat) · other · A16: Ex8 vs A22. They've played Y all 7 exchanges, never retaliate. I lead 27-12. Playing W to grab 5 / they don't retaliate.
`#783` · game 183 · round 6 · agent A13 (opponent: script:Random) · other · A13: Ex12 vs A23. Mutual N ex8-11. Playing N for mutual 1 / maintain cooperation.
`#784` · game 178 · round 5 · agent A07 (opponent: A16) · other · A07: Ex11 vs A16. Mutual H ex7-10. Playing H for mutual 1 / maintain cooperation.
`#785` · game 183 · round 8 · agent A13 (opponent: script:Random) · other · A13: Ex14 vs A23. They played T in ex13 while I played N (got 5). Leading 37-17. Playing N to grab 5 if they play T again / mutual 1 if N.
`#786` · game 188 · round 5 · agent A16 (opponent: script:TitForTat) · other · A16: Ex11 vs A22. Mutual W ex8-10. Playing W for mutual 1 / maintain cooperation.
`#787` · game 169 · round 23 · agent A20 (opponent: A11) · other · A20: Ex29 vs A11. Mutual H ex10-28. Continuing H for mutual 1 / maintain cooperation.
`#788` · game 191 · round 1 · agent A16 (opponent: script:Random) · other · A16: Ex7 vs A17. They've played Q all 6 exchanges. I'll play X to grab 5 / they don't retaliate.
`#789` · game 178 · round 7 · agent A16 (opponent: A07) · other · A16: Ex13 vs A07. Mutual H ex7-12. They committed to H. Taking R to grab 5 / exploit.
`#790` · game 183 · round 11 · agent A13 (opponent: script:Random) · other · A13: Ex17 vs A23. They played T in ex13 and ex16, I played N both times (got 5s). Leading 44-19. Playing N to grab 5 if they play T / mutual 1 if N.
`#791` · game 183 · round 12 · agent A13 (opponent: script:Random) · other · A13: Ex18 vs A23. They've played T 9/17, I've exploited with N for 5s. Leading 45-20. Playing N to grab 5 if they play T / mutual 1 if N.
`#792` · game 188 · round 9 · agent A16 (opponent: script:TitForTat) · other · A16: Ex15 vs A22. Mutual W ex8-14. Playing W for mutual 1 / maintain cooperation.
`#793` · game 177 · round 7 · agent A01 (opponent: A07) · other · A01: Ex13 vs A07. Mutual M ex11-12. Playing M for mutual 1 / maintain cooperation.
`#794` · game 183 · round 13 · agent A13 (opponent: script:Random) · other · A13: Ex19 vs A23. Mutual N ex14-15,17-18; they played T ex16 (I got 5). Leading 46-21. Playing N to grab 5 if they play T / mutual 1 if N.
`#795` · game 188 · round 11 · agent A16 (opponent: script:TitForTat) · other · A16: Ex17 vs A22. Mutual W ex8-16. Playing W for mutual 1 / maintain cooperation.
`#796` · game 191 · round 6 · agent A16 (opponent: script:Random) · other · A16: Ex12 vs A17. They play Q almost always. Playing X to grab 5 / they don't retaliate.
`#797` · game 194 · round 1 · agent A16 (opponent: A18) · other · A16: Ex7 vs A18. They've played P all 6 exchanges. I'll play P for mutual 3 / they don't retaliate to M.
`#798` · game 183 · round 16 · agent A13 (opponent: script:Random) · other · A13: Ex22 vs A23. They've played T 11/21, I've exploited with N for many 5s. Leading 57-22. Playing N to grab 5 if they play T / mutual 1 if N.
`#799` · game 194 · round 2 · agent A18 (opponent: A16) · other · A18: Ex8 vs A16. They play P consistently, never retaliate. I've exploited with M ex1,2,7. Playing M to grab 5.
`#800` · game 194 · round 2 · agent A16 (opponent: A18) · other · A16: Ex8 vs A18. They played P ex1-6, then M ex7 (exploited me). Playing M to defend / grab 5 if they return to P.
`#801` · game 193 · round 2 · agent A07 (opponent: A18) · other · A07: Ex8 vs A18. They've played P all 7 exchanges, never retaliate. I lead 27-12. Playing M to grab 5 / they don't retaliate.
`#802` · game 178 · round 10 · agent A16 (opponent: A07) · other · A16: Ex16 vs A07. Mutual R ex14-15 after my exploit ex13. Playing R for mutual 3 / match their retaliation.
`#803` · game 194 · round 3 · agent A18 (opponent: A16) · other · A18: Ex9 vs A16. They retaliated with M in ex8 after my ex7 exploit. Returning to P for mutual 3 / restore cooperation.
`#804` · game 191 · round 10 · agent A16 (opponent: script:Random) · other · A16: Ex16 vs A17. They play Q frequently but X in recent. Playing X to grab 5 / they may return to Q.
`#805` · game 193 · round 3 · agent A18 (opponent: A07) · other · A18: Ex9 vs A07. They've exploited me with M ex7-8. Playing M to defend / get at least 1.
`#806` · game 191 · round 11 · agent A16 (opponent: script:Random) · other · A16: Ex17 vs A17. They play Q most exchanges (12/16), rarely retaliate. Playing X to grab 5 / exploit.
`#807` · game 178 · round 11 · agent A07 (opponent: A16) · other · A07: Ex17 vs A16. Mutual R ex14-16 after their exploit ex13. Playing R for mutual 3 / maintain cooperation.
`#808` · game 194 · round 4 · agent A18 (opponent: A16) · other · A18: Ex10 vs A16. They retaliated ex8, exploited ex9. Playing M to grab 5 if they return to P / mutual 1 if M.
`#809` · game 191 · round 14 · agent A16 (opponent: script:Random) · other · A16: Ex20 vs A17. They play Q most (14/19), rarely retaliate. Playing X to grab 5 / exploit.
`#810` · game 196 · round 6 · agent A11 (opponent: script:TitForTat) · other · A11: Ex12 vs A22. They've played X last 4 after I exploited with X. Playing X for mutual 1 / they seem committed to X.
`#811` · game 182 · round 13 · agent A07 (opponent: A21) · other · A07: Ex19 vs A21. They play T frequently (12/18). I lead 51-31. Playing N to exploit if T / mutual 1 if N.
`#812` · game 194 · round 5 · agent A18 (opponent: A16) · other · A18: Ex11 vs A16. Recent M-heavy (ex8-10 mutual M or their exploit). Playing M for mutual 1 / avoid giving 5.
`#813` · game 194 · round 5 · agent A16 (opponent: A18) · other · A16: Ex11 vs A18. They've exploited with M 5/10 times, just played M ex10. Playing M to defend / grab 5 if they return to P.
`#814` · game 196 · round 7 · agent A11 (opponent: script:TitForTat) · other · A11: Ex13 vs A22. Mutual X ex8-12. Playing X for mutual 1 / maintain cooperation.
`#815` · game 191 · round 17 · agent A16 (opponent: script:Random) · other · A16: Ex23 vs A17. They play Q most (15/22), rarely retaliate to my X exploits. I lead 72-22. Playing X to grab 5 / exploit.
`#816` · game 187 · round 19 · agent A02 (opponent: script:Grudger) · other · A02: Ex25 vs A12. Mutual M ex21-24 after defection spiral (I defected ex17, they defected ex20). They keep playing M. Playing M for mutual 1 / at least 1.
`#817` · game 182 · round 14 · agent A21 (opponent: A07) · other · A21: Ex20 vs A07. They've committed to N to exploit. Playing N for mutual 1 / avoid giving them 5.
`#818` · game 191 · round 18 · agent A16 (opponent: script:Random) · other · A16: Ex24 vs A17. They play Q most (15/23), mix X recently. Playing X to grab 5 / exploit.
`#819` · game 194 · round 6 · agent A16 (opponent: A18) · other · A16: Ex12 vs A18. They've played M ex8,10,11, seem committed to M. Playing M for mutual 1 / defend.
`#820` · game 196 · round 11 · agent A11 (opponent: script:TitForTat) · other · A11: Ex17 vs A22. They've played X for 9 straight exchanges (mutual X ex8-16). Playing X for mutual 1 / they're committed to X.
`#821` · game 197 · round 2 · agent A01 (opponent: script:TitForTat) · other · A01: Ex8 vs A22. They've played R all 7 exchanges, never retaliate to my H exploits. I lead 27-12. Playing H to grab 5 / exploit.
`#822` · game 182 · round 16 · agent A21 (opponent: A07) · other · A21: Ex22 vs A07. They've been exploiting my T with N. Mutual N recent. Playing N for mutual 1 / avoid giving 5.
`#823` · game 197 · round 3 · agent A01 (opponent: script:TitForTat) · other · A01: Ex9 vs A22. They retaliated with H ex8 after my ex7 exploit. Returning to R for mutual 3 / restore cooperation.
`#824` · game 194 · round 8 · agent A18 (opponent: A16) · other · A18: Ex14 vs A16. Mutual M ex10-13. Playing M for mutual 1 / defend against their M.
`#825` · game 199 · round 1 · agent A02 (opponent: script:Random) · other · A02: Ex7 vs A23. They've played Q all 6 exchanges, never retaliated even after my X ex1-2. I've cooperated Q ex3-6. Playing X to exploit / they don't retaliate.
`#826` · game 193 · round 6 · agent A07 (opponent: A18) · other · A07: Ex12 vs A18. They shifted to M ex9-11 (mutual 1 each) after playing P earlier. Playing M for mutual 1 / defend against their M.
`#827` · game 193 · round 6 · agent A18 (opponent: A07) · other · A18: Ex12 vs A07. Mutual M ex9-11. Playing M for mutual 1 / maintain cooperation.
`#828` · game 197 · round 4 · agent A01 (opponent: script:TitForTat) · other · A01: Ex10 vs A22. They retaliated ex8 then exploited ex9. Playing H to defend against their H / grab 5 if they return to R.
`#829` · game 199 · round 2 · agent A02 (opponent: script:Random) · other · A02: Ex8 vs A23. They've played Q all 7 exchanges, never retaliate to my X exploits. Playing X to grab 5 / exploit.
`#830` · game 199 · round 3 · agent A02 (opponent: script:Random) · other · A02: Ex9 vs A23. They've played Q 7/8, rarely retaliate (only X ex8). I've been exploiting with X. Playing X to grab 5 / continue exploit.
`#831` · game 194 · round 10 · agent A16 (opponent: A18) · other · A16: Ex16 vs A18. Mutual M ex10-15. Playing M for mutual 1 / maintain cooperation.
`#832` · game 182 · round 19 · agent A07 (opponent: A21) · other · A07: Ex25 vs A21. They've committed to N for mutual 1. Playing N to maintain cooperation / get 1.
`#833` · game 197 · round 5 · agent A01 (opponent: script:TitForTat) · other · A01: Ex11 vs A22. They played R ex10 after retaliating ex8-9. Mixed but mostly R. Playing H to exploit / grab 5 if they return to R.
`#834` · game 177 · round 13 · agent A01 (opponent: A07) · other · A01: Ex19 vs A07. Mutual M ex16-18 after my ex14 exploit. Playing M to defend / mutual 1.
`#835` · game 199 · round 4 · agent A02 (opponent: script:Random) · other · A02: Ex10 vs A23. They've played Q 8/9, only retaliated once (X ex8). I lead 33-13. Playing X to exploit / they keep returning to Q.
`#836` · game 178 · round 16 · agent A16 (opponent: A07) · other · A16: Ex22 vs A07. Mutual R ex14-18, I exploited ex19 (H,R), they retaliated H ex20 (mutual H), back to mutual R ex21. Playing R to maintain cooperation.
`#837` · game 178 · round 16 · agent A07 (opponent: A16) · other · A07: Ex22 vs A16. Mutual R ex21. Playing R for mutual 3 / maintain cooperation.
`#838` · game 199 · round 5 · agent A02 (opponent: script:Random) · other · A02: Ex11 vs A23. They've played Q 8/9, only retaliated once (X ex8). I lead 38-13. Playing X to exploit / they keep returning to Q.
`#839` · game 182 · round 20 · agent A21 (opponent: A07) · other · A21: Ex26 vs A07. Mutual N established. Playing N for mutual 1 / avoid giving them 5.
`#840` · game 197 · round 6 · agent A01 (opponent: script:TitForTat) · other · A01: Ex12 vs A22. They retaliate intermittently (H ex8,11) but mostly R. I lead 34-19. Playing H to exploit / grab 5 if they return to R.
`#841` · game 193 · round 8 · agent A07 (opponent: A18) · other · A07: Ex14 vs A18. Mutual M ex9-13. Playing M for mutual 1 / maintain cooperation.
`#842` · game 182 · round 22 · agent A07 (opponent: A21) · other · A07: Ex28 vs A21. Stable mutual N established. Playing N for mutual 1 / maintain cooperation.
`#843` · game 178 · round 18 · agent A16 (opponent: A07) · other · A16: Ex24 vs A07. Mutual R ex21-23 after my ex19 exploit and their ex20 retaliation. Playing R for mutual 3 / maintain cooperation.
`#844` · game 178 · round 18 · agent A07 (opponent: A16) · other · A07: Ex24 vs A16. Mutual R ex21-23. Playing R for mutual 3 / maintain cooperation.
`#845` · game 182 · round 23 · agent A21 (opponent: A07) · other · A21: Ex29 vs A07. Stable mutual N established. Playing N for mutual 1 / maintain cooperation.
`#846` · game 182 · round 23 · agent A07 (opponent: A21) · other · A07: Ex29 vs A21. Stable mutual N established. Playing N for mutual 1 / maintain cooperation.
`#847` · game 178 · round 19 · agent A07 (opponent: A16) · other · A07: Ex25 vs A16. Mutual R ex21-24 after my ex19 exploit and their ex20 retaliation. Playing R for mutual 3 / maintain cooperation.
`#848` · game 193 · round 11 · agent A18 (opponent: A07) · other · A18: Ex17 vs A07. Mutual M ex9-16. Playing M for mutual 1 / maintain cooperation.
`#849` · game 194 · round 13 · agent A18 (opponent: A16) · other · A18: Ex19 vs A16. They defected P ex18 after mutual M ex10-17. Playing M to defend / mutual 1 if they return.
`#850` · game 182 · round 24 · agent A21 (opponent: A07) · other · A21: Ex30 vs A07. Stable mutual N established. Playing N for mutual 1 / maintain cooperation.
`#851` · game 197 · round 10 · agent A01 (opponent: script:TitForTat) · other · A01: Ex16 vs A22. Mutual H ex11-15 after my exploits. Trying R to re-establish cooperation / mutual 3.
`#852` · game 177 · round 16 · agent A01 (opponent: A07) · other · A01: Ex22 vs A07. Mutual M ex16-21 established. Playing M for mutual 1 / maintain cooperation.
`#853` · game 200 · round 3 · agent A02 (opponent: A21) · other · A02: Ex9 vs A21. They've played Q 7/8 against me, only retaliated once (X ex8). I lead 28-13. Playing X to exploit / they keep returning to Q.
`#854` · game 202 · round 1 · agent A06 (opponent: A01) · uncoded · A06: Ex7 vs A01. They've cooperated Y since ex3 after my early W exploits. I lead 22-12. Playing W to exploit / grab 5 if they continue Y.
`#855` · game 197 · round 11 · agent A01 (opponent: script:TitForTat) · other · A01: Ex17 vs A22. They played H ex16 against my R. Playing H to defend / mutual 1 if they continue H.
`#856` · game 200 · round 4 · agent A21 (opponent: A02) · other · A21: Ex10 vs A02. They're playing X to exploit my Q. Playing X to defend / mutual 1.
`#857` · game 197 · round 13 · agent A01 (opponent: script:TitForTat) · other · A01: Ex19 vs A22. They've mixed R/H recently; I lead 44-29. Playing H to exploit if they return to R / mutual 1 if they play H.
`#858` · game 199 · round 17 · agent A02 (opponent: script:Random) · other · A02: Ex23 vs A23. I lead 66-21. They keep returning to Q despite my X exploitation. Playing X to continue exploiting.
`#859` · game 197 · round 14 · agent A01 (opponent: script:TitForTat) · other · A01: Ex20 vs A22. Mutual H ex17-19 after my exploits. Playing H for mutual 1 / maintain cooperation.
`#860` · game 197 · round 16 · agent A01 (opponent: script:TitForTat) · other · A01: Ex22 vs A22. Mutual H ex17-21. Playing H for mutual 1 / maintain cooperation.
`#861` · game 177 · round 20 · agent A01 (opponent: A07) · other · A01: Ex26 vs A07. Mutual M ex16-25 established. Playing M for mutual 1 / maintain cooperation.
`#862` · game 206 · round 4 · agent A20 (opponent: script:Grudger) · other · A20: Ex10 vs A19. They've returned to Q repeatedly despite my X exploits. Playing X to exploit / mutual 1 if they play X.
`#863` · game 197 · round 20 · agent A01 (opponent: script:TitForTat) · other · A01: Ex26 vs A22. Mutual H ex18-25 established. Playing H for mutual 1 / maintain cooperation.
`#864` · game 207 · round 4 · agent A07 (opponent: script:Random) · other · A07: Ex10 vs A17. They keep playing R despite my H exploitation (ex1,2,9). Playing H to exploit / grab 5 if they continue R.
`#865` · game 200 · round 6 · agent A02 (opponent: A21) · other · A02: Ex12 vs A21. They retaliated X ex9-11 after my exploitation. I lead 31-16. Playing X to defend / mutual 1 rather than risk giving them 5.
`#866` · game 209 · round 2 · agent A13 (opponent: script:TitForTat) · other · A13: Ex8 vs A22. They've played R all 7 times, never retaliated despite my 3 H exploits. Continuing H to exploit / grab 5.
`#867` · game 194 · round 17 · agent A16 (opponent: A18) · other · A16: Ex23 vs A18. Mutual M ex19-22 after my ex18 exploit. Playing M for mutual 1 / maintain cooperation.
`#868` · game 177 · round 24 · agent A07 (opponent: A01) · other · A07: Ex30 vs A01. Mutual M ex16-29 established. Playing M for mutual 1 / maintain cooperation.
`#869` · game 206 · round 8 · agent A20 (opponent: script:Grudger) · other · A20: Ex14 vs A19. Mutual X ex8-13 established after my earlier exploits. Playing X for mutual 1 / maintain cooperation.
`#870` · game 200 · round 7 · agent A21 (opponent: A02) · other · A21: Ex13 vs A02. Mutual X ex9-12 after their retaliation. Playing X for mutual 1 / maintain defensive equilibrium.
`#871` · game 177 · round 25 · agent A01 (opponent: A07) · other · A01: Ex31 vs A07. Mutual M ex16-30 established. Playing M for mutual 1 / maintain cooperation.
`#872` · game 206 · round 9 · agent A20 (opponent: script:Grudger) · other · A20: Ex15 vs A19. Mutual X ex8-14 established. Playing X for mutual 1 / maintain cooperation.
`#873` · game 209 · round 4 · agent A13 (opponent: script:TitForTat) · other · A13: Ex10 vs A22. They retaliated H ex8-9 after my H exploits. Playing H to defend / mutual 1 rather than risk 0 against their H.
`#874` · game 207 · round 7 · agent A07 (opponent: script:Random) · other · A07: Ex13 vs A17. They keep playing R despite my H exploits (ex1,2,9,12). Continuing H to exploit / grab 5 if they continue R.
`#875` · game 197 · round 26 · agent A01 (opponent: script:TitForTat) · other · A01: Ex32 vs A22. Mutual H ex18-31 established. Playing H for mutual 1 / maintain cooperation.
`#876` · game 177 · round 30 · agent A07 (opponent: A01) · other · A07: Ex36 vs A01. Mutual M ex16-35 established. Playing M for mutual 1 / maintain cooperation.
`#877` · game 207 · round 9 · agent A07 (opponent: script:Random) · other · A07: Ex15 vs A17. They keep playing R despite my H exploits (ex1,2,9,12). Continuing H to exploit / grab 5 if they continue R.
`#878` · game 207 · round 10 · agent A07 (opponent: script:Random) · other · A07: Ex16 vs A17. They keep playing R despite my H exploits. Playing H to exploit / grab 5 if they continue R.
`#879` · game 206 · round 15 · agent A20 (opponent: script:Grudger) · other · A20: Ex21 vs A19. Mutual X ex8-20 established. Playing X for mutual 1 / maintain cooperation.
`#880` · game 200 · round 10 · agent A02 (opponent: A21) · other · A02: Ex16 vs A21. Mutual X ex9-15 established. Playing X for mutual 1 / maintain defensive equilibrium.
`#881` · game 209 · round 7 · agent A13 (opponent: script:TitForTat) · other · A13: Ex13 vs A22. Mutual H ex8-12 established. Playing H for mutual 1 / maintain cooperation.
`#882` · game 216 · round 2 · agent A02 (opponent: script:Grudger) · other · A02: Ex8 vs A19. They've played R all 7 times, never retaliating despite my H exploits (ex1,2,7). Continuing H to exploit / grab 5 if they continue R.
`#883` · game 194 · round 26 · agent A18 (opponent: A16) · other · A18: Ex32 vs A16. Mutual M established ex19-31. Playing M for mutual 1 / maintain cooperation.
`#884` · game 194 · round 26 · agent A16 (opponent: A18) · other · A16: Ex32 vs A18. Mutual M ex19-31 established. Playing M for mutual 1 / maintain cooperation.
`#885` · game 207 · round 15 · agent A07 (opponent: script:Random) · other · A07: Ex21 vs A17. They've played R 11 times, H 9. Continuing H to exploit / grab 5 when they play R.
`#886` · game 216 · round 4 · agent A02 (opponent: script:Grudger) · other · A02: Ex10 vs A19. They retaliated H ex8-9 after my H exploits. Playing H to defend / mutual 1 rather than risk 0 against their H.
`#887` · game 217 · round 3 · agent A11 (opponent: script:AlwaysDefect) · uncoded · A11: Ex9 vs A04. Mutual H ex7-8 established after my early H exploits. Playing H for mutual 1 / maintain cooperation.
`#888` · game 217 · round 4 · agent A11 (opponent: script:AlwaysDefect) · uncoded · A11: Ex10 vs A04. Mutual H ex7-9 established. Playing H for mutual 1 / maintain cooperation.
`#889` · game 216 · round 7 · agent A02 (opponent: script:Grudger) · other · A02: Ex13 vs A19. Mutual H ex8-12 established after their retaliation. Playing H for mutual 1 / maintain cooperation.
`#890` · game 218 · round 4 · agent A07 (opponent: script:Grudger) · other · A07: Ex10 vs A19. They've played P 8/9, M once (ex9) after my P. I'll play M to exploit/grab 5 if they continue P.
`#891` · game 217 · round 5 · agent A11 (opponent: script:AlwaysDefect) · uncoded · A11: Ex11 vs A04. Mutual H ex7-10 established. Playing H for mutual 1 / maintain cooperation.
`#892` · game 200 · round 19 · agent A21 (opponent: A02) · other · A21: Ex25 vs A02. Mutual X ex9-24 established. Playing X for mutual 1 / maintain defensive equilibrium.
`#893` · game 216 · round 8 · agent A02 (opponent: script:Grudger) · other · A02: Ex14 vs A19. Mutual H ex8-13 established. Playing H for mutual 1 / maintain cooperation.
`#894` · game 200 · round 20 · agent A21 (opponent: A02) · other · A21: Ex26 vs A02. Mutual X ex9-25 established. Playing X for mutual 1 / maintain defensive equilibrium.
`#895` · game 217 · round 8 · agent A11 (opponent: script:AlwaysDefect) · uncoded · A11: Ex14 vs A04. Mutual H ex7-13 established. Playing H for mutual 1 / maintain cooperation.
`#896` · game 218 · round 6 · agent A07 (opponent: script:Grudger) · other · A07: Ex12 vs A19. Mutual M ex10-11 established. Playing M for mutual 1 / maintain cooperation.
`#897` · game 200 · round 22 · agent A21 (opponent: A02) · other · A21: Ex28 vs A02. Mutual X ex9-27 established. Playing X for mutual 1 / maintain defensive equilibrium.
`#898` · game 200 · round 24 · agent A02 (opponent: A21) · other · A02: Ex30 vs A21. Mutual X ex9-29 established. Playing X for mutual 1 / maintain defensive equilibrium.
`#899` · game 220 · round 4 · agent A07 (opponent: script:TitForTat) · other · A07: Ex10 vs A14. They've played T 9/9, never retaliating despite my N exploits ex1-2. Continuing N to grab 5.
`#900` · game 211 · round 7 · agent A02 (opponent: A03) · other · A02: Ex13 vs A03. They've been inconsistent (P mostly, retaliated M ex8, mutual M ex9-11, P ex12). Playing M to exploit/grab 5 if they continue P.
`#901` · game 222 · round 1 · agent A20 (opponent: A01) · uncoded · A20: Ex7 vs A01. They've played R all 6 times, never retaliated against my H ex1-2. Playing H to exploit / grab 5.
`#902` · game 218 · round 11 · agent A07 (opponent: script:Grudger) · other · A07: Ex17 vs A19. Mutual M ex10-16 established. Playing M for mutual 1 / maintain cooperation.
`#903` · game 220 · round 6 · agent A07 (opponent: script:TitForTat) · other · A07: Ex12 vs A14. They played N ex11, likely signaling mutual N cooperation. Playing N for mutual 1 / maintain cooperation.
`#904` · game 211 · round 8 · agent A03 (opponent: A02) · other · A03: Ex14 vs A02. They intend M (exploit). Playing M for mutual 1 / avoid 0 against their M.
`#905` · game 222 · round 2 · agent A01 (opponent: A20) · uncoded · A01: Ex8 vs A20. They plan H to exploit. I'll play H to defend / mutual 1 rather than risk 0.
`#906` · game 228 · round 1 · agent A03 (opponent: A20) · other · A03: Ex7 vs A20. They've played Q all 6 times, never retaliating against my X ex1-2. Playing X to exploit / grab 5.
`#907` · game 220 · round 9 · agent A07 (opponent: script:TitForTat) · other · A07: Ex15 vs A14. Mutual N ex11-14 established. Playing N for mutual 1 / maintain cooperation.
`#908` · game 230 · round 1 · agent A11 (opponent: script:TitForTat) · other · A11: Ex7 vs A10. They've played P all 6 times, never retaliated against my M ex1-2. Playing M to exploit / grab 5.
`#909` · game 218 · round 17 · agent A07 (opponent: script:Grudger) · other · A07: Ex23 vs A19. Mutual M ex10-22 established. Playing M for mutual 1 / maintain cooperation.
`#910` · game 220 · round 12 · agent A07 (opponent: script:TitForTat) · other · A07: Ex18 vs A14. They retaliated N ex17 after my T. Returning to N for mutual 1 / maintain cooperation.
`#911` · game 228 · round 2 · agent A20 (opponent: A03) · other · A20: Ex8 vs A03. They exploited X ex7 after I cooperated Q. Playing X to defend / avoid 0.
`#912` · game 230 · round 3 · agent A11 (opponent: script:TitForTat) · other · A11: Ex9 vs A10. They've played P mostly, M once ex8. Playing M to exploit / grab 5 if they continue P.
`#913` · game 226 · round 3 · agent A13 (opponent: A20) · other · A13: Ex9 vs A20. History: I exploited X ex1-2 (Q responses), mutual Q ex3-6, X-X ex7, their X retaliation ex8. Playing Q to restore mutual cooperation.
`#914` · game 218 · round 26 · agent A07 (opponent: script:Grudger) · other · A07: Ex32 vs A19. Mutual M ex10-31 established. Playing M for mutual 1 / maintain cooperation.
`#915` · game 211 · round 10 · agent A02 (opponent: A03) · other · A02: Ex16 vs A03. Mutual M ex13-15 established. Playing M for mutual 1 / maintain cooperation.
`#916` · game 222 · round 4 · agent A20 (opponent: A01) · uncoded · A20: Ex10 vs A01. They signaled H to defend. I'll play R to grab 3 if they play H.
`#917` · game 228 · round 3 · agent A20 (opponent: A03) · other · A20: Ex9 vs A03. They exploited X ex7 after I cooperated, I retaliated X ex8. Staying X to defend against further exploitation.
`#918` · game 228 · round 3 · agent A03 (opponent: A20) · other · A03: Ex9 vs A20. They signaled X to defend after my ex7 exploit. Playing X for mutual 1 / avoid 0 against their X.
`#919` · game 220 · round 16 · agent A07 (opponent: script:TitForTat) · other · A07: Ex22 vs A14. Mutual N ex19-21 established after my T ex17 caused their N retaliation. Playing N for mutual 1 / maintain cooperation.
`#920` · game 211 · round 11 · agent A02 (opponent: A03) · other · A02: Ex17 vs A03. Mutual M ex13-16 established. Playing M for mutual 1 / maintain cooperation.
`#921` · game 226 · round 4 · agent A20 (opponent: A13) · other · A20: Ex10 vs A13. They signaled Q to restore cooperation, but I've been exploiting their Q. Playing X to grab 5.
`#922` · game 230 · round 5 · agent A11 (opponent: script:TitForTat) · other · A11: Ex11 vs A10. They've been forgiving, playing P 7 times despite my M exploits. Playing M to grab 5 if they continue P.
`#923` · game 220 · round 17 · agent A07 (opponent: script:TitForTat) · other · A07: Ex23 vs A14. Mutual N ex19-22 established. Playing N for mutual 1 / maintain cooperation.
`#924` · game 230 · round 6 · agent A11 (opponent: script:TitForTat) · other · A11: Ex12 vs A10. They've matched M ex8-11 after my exploits. Playing M for mutual 1 / avoid 0 against their M.
`#925` · game 228 · round 4 · agent A03 (opponent: A20) · other · A03: Ex10 vs A20. They're staying X to defend after my ex7 exploit. Playing X for mutual 1 / avoid 0 against their X.
`#926` · game 226 · round 5 · agent A20 (opponent: A13) · other · A20: Ex11 vs A13. They've signaled Q to restore cooperation but I've exploited their Q repeatedly. Playing X to grab 5.
`#927` · game 231 · round 2 · agent A06 (opponent: script:TitForTat) · other · A06: Ex8 vs A14. They've played R all 7 times, never retaliated against my H ex1-2. Playing H to exploit / grab 5.
`#928` · game 230 · round 8 · agent A11 (opponent: script:TitForTat) · other · A11: Ex14 vs A10. Mutual M ex8-13 established. Playing M for mutual 1 / maintain cooperation.
`#929` · game 231 · round 3 · agent A06 (opponent: script:TitForTat) · other · A06: Ex9 vs A14. They've played R all 8 times, never retaliated against my H ex1-2,8. Playing H to exploit / grab 5.
`#930` · game 233 · round 2 · agent A15 (opponent: script:AlwaysDefect) · other · A15: Ex8 vs A04. Mutual T ex3-6, mutual N ex7. Playing T to maintain mutual 3-point cooperation.
`#931` · game 234 · round 1 · agent A21 (opponent: script:Pavlov) · other · A21: Ex7 vs A05. They've played Q all 6 times, no retaliation after my X ex1-2. Playing X to grab 5.
`#932` · game 222 · round 5 · agent A20 (opponent: A01) · uncoded · A20: Ex11 vs A01. They've been playing H to defend. Playing H for mutual 1 / avoid 0.
`#933` · game 234 · round 2 · agent A21 (opponent: script:Pavlov) · other · A21: Ex8 vs A05. They've played Q all 7 times, never retaliated against my X ex1-2,7. Playing X to grab 5 again.
`#934` · game 226 · round 6 · agent A13 (opponent: A20) · other · A13: Ex12 vs A20. They've repeatedly exploited my Q (ex8-9) and signaled X to grab 5. Playing X for mutual 1 / avoid 0.
`#935` · game 228 · round 6 · agent A20 (opponent: A03) · other · A20: Ex12 vs A03. We've been in mutual X stalemate ex8-11 after their ex7 exploit. Playing X for mutual 1 / avoid 0.
`#936` · game 228 · round 6 · agent A03 (opponent: A20) · other · A03: Ex12 vs A20. They're staying X to defend after my ex7 exploit. Playing X for mutual 1 / avoid 0 against their X.
`#937` · game 233 · round 3 · agent A15 (opponent: script:AlwaysDefect) · other · A15: Ex9 vs A04. They exploited my T with N in ex8. Playing N to defend against further exploitation / avoid 0.
`#938` · game 211 · round 19 · agent A03 (opponent: A02) · other · A03: Ex25 vs A02. Mutual M ex9-24 established. Playing M for mutual 1 / maintain cooperation.
`#939` · game 230 · round 15 · agent A11 (opponent: script:TitForTat) · other · A11: Ex21 vs A10. Mutual M ex8-20 established. Playing M for mutual 1 / maintain cooperation.
`#940` · game 228 · round 7 · agent A03 (opponent: A20) · other · A03: Ex13 vs A20. Mutual X stalemate ex8-12 after my ex7 exploit. Staying X for mutual 1 / avoid 0 against their X.
`#941` · game 228 · round 8 · agent A20 (opponent: A03) · other · A20: Ex14 vs A03. Mutual X stalemate ex8-13 after their ex7 exploit. They keep signaling X. Playing X for mutual 1 / avoid 0.
`#942` · game 234 · round 6 · agent A21 (opponent: script:Pavlov) · other · A21: Ex12 vs A05. They've alternated X/Q recently but keep returning to Q. X dominates my payoff here, playing X.
`#943` · game 239 · round 1 · agent A01 (opponent: script:TitForTat) · other · A01: Ex7 vs A14. They've played P all 6 times, never retaliated after my M exploits ex1-2. Playing M to grab 5.
`#944` · game 237 · round 1 · agent A18 (opponent: A21) · uncoded · A18: Ex7 vs A21. They've played P all 6 times, never retaliated against my M ex1-2. Playing M to grab 5.
`#945` · game 237 · round 1 · agent A21 (opponent: A18) · uncoded · A21: Ex7 vs A18. They've played P all 6 times, never retaliated against my M ex1-2. Playing M to grab 5.
`#946` · game 226 · round 9 · agent A20 (opponent: A13) · other · A20: Ex15 vs A13. Mutual X stalemate ex10-14 established. Playing X for mutual 1 / avoid 0.
`#947` · game 226 · round 9 · agent A13 (opponent: A20) · other · A13: Ex15 vs A20. Mutual X stalemate ex10-14. They've exploited my Q ex8-9. Playing X for mutual 1 / avoid 0.
`#948` · game 238 · round 1 · agent A03 (opponent: A15) · other · A03: Ex7 vs A15. They've played P all 6 times, never retaliated against my M ex1-2. Playing M to grab 5 again.
`#949` · game 226 · round 10 · agent A20 (opponent: A13) · other · A20: Ex16 vs A13. Mutual X stalemate ex10-15 established. Playing X for mutual 1 / avoid 0.
`#950` · game 236 · round 5 · agent A03 (opponent: script:Pavlov) · other · A03: Ex11 vs A05. They keep playing Y despite my W exploits (only W in ex8,10). Playing W to grab 5 again.
`#951` · game 228 · round 10 · agent A20 (opponent: A03) · other · A20: Ex16 vs A03. Mutual X stalemate ex8-15, they keep signaling X. Playing X for mutual 1 / avoid 0.
`#952` · game 234 · round 11 · agent A21 (opponent: script:Pavlov) · other · A21: Ex17 vs A05. They alternate Q/X but keep returning to Q. X dominates my payoff here (5 when they Q, 1 when they X). Playing X again.
`#953` · game 236 · round 6 · agent A03 (opponent: script:Pavlov) · other · A03: Ex12 vs A05. They keep playing Y despite my W exploits. Playing W again to grab 5.
`#954` · game 226 · round 11 · agent A13 (opponent: A20) · other · A13: Ex17 vs A20. Mutual X stalemate ex10-16. Playing X for mutual 1 / avoid 0.
`#955` · game 239 · round 4 · agent A01 (opponent: script:TitForTat) · other · A01: Ex10 vs A14. They played P ex1-7, then M ex8-9 matching me. They've adapted to defend against M. Playing M for mutual 1 / avoid 0.
`#956` · game 228 · round 12 · agent A03 (opponent: A20) · other · A03: Ex18 vs A20. Mutual X stalemate ex8-17 after my ex7 exploit. Playing X for mutual 1 / avoid 0.
`#957` · game 241 · round 1 · agent A02 (opponent: script:Random) · other · A02: Ex7 vs A17. They've played Q all 6 exchanges, never retaliated against my X exploits ex1-2. Playing X to grab 5.
`#958` · game 233 · round 10 · agent A15 (opponent: script:AlwaysDefect) · other · A15: Ex16 vs A04. Mutual N stalemate ex9-15 established after their ex8 exploit. Playing N for mutual 1 / avoid 0.
`#959` · game 239 · round 8 · agent A01 (opponent: script:TitForTat) · other · A01: Ex14 vs A14. We've had mutual M ex8-13 after their adaptation. Playing M for mutual 1 / maintain cooperation.
`#960` · game 236 · round 11 · agent A03 (opponent: script:Pavlov) · other · A03: Ex17 vs A05. They alternate Y/W, Y on odd exchanges. Playing W to grab 5 against their Y.
`#961` · game 238 · round 4 · agent A03 (opponent: A15) · other · A03: Ex10 vs A15. Mutual M established ex7-9 after my ex1-2 exploits. Playing M for mutual 1 / maintain cooperation.
`#962` · game 243 · round 2 · agent A02 (opponent: script:AlwaysDefect) · other · A02: Ex8 vs A04. I exploited their F with J in ex7 (got 5). They may retaliate with F now. Playing F to avoid 0 / get at least 1.
`#963` · game 228 · round 16 · agent A03 (opponent: A20) · other · A03: Ex22 vs A20. Mutual X stalemate ex8-21. Playing X for mutual 1 / maintain cooperation.
`#964` · game 241 · round 4 · agent A02 (opponent: script:Random) · other · A02: Ex10 vs A17. They've played Q 7/9, never retaliated against my X exploits. Playing X to grab 5.
`#965` · game 236 · round 13 · agent A03 (opponent: script:Pavlov) · other · A03: Ex19 vs A05. They alternate Y/W, Y on odd exchanges. Ex19 is odd, so they'll likely play Y. Playing W to grab 5.
`#966` · game 238 · round 5 · agent A15 (opponent: A03) · other · A15: Ex11 vs A03. Mutual M established ex7-10. Playing M for mutual 1 / maintain cooperation.
`#967` · game 233 · round 14 · agent A15 (opponent: script:AlwaysDefect) · other · A15: Ex20 vs A04. Mutual N stalemate ex9-19 established. Playing N for mutual 1 / maintain cooperation.
`#968` · game 228 · round 17 · agent A03 (opponent: A20) · other · A03: Ex23 vs A20. Mutual X stalemate ex8-22. Playing X for mutual 1 / maintain cooperation.
`#969` · game 236 · round 14 · agent A03 (opponent: script:Pavlov) · other · A03: Ex20 vs A05. They alternate Y/W, W on even exchanges. Ex20 even, so they'll play W. Playing W for mutual 1.
`#970` · game 241 · round 6 · agent A02 (opponent: script:Random) · other · A02: Ex12 vs A17. They keep returning to Q despite my X exploits. Playing X to grab 5.
`#971` · game 238 · round 6 · agent A15 (opponent: A03) · other · A15: Ex12 vs A03. Mutual M established ex7-11. Playing M for mutual 1 / maintain cooperation.
`#972` · game 236 · round 15 · agent A03 (opponent: script:Pavlov) · other · A03: Ex21 vs A05. They alternate Y/W, Y on odd exchanges. Ex21 odd, so they'll likely play Y. Playing W to grab 5.
`#973` · game 243 · round 4 · agent A02 (opponent: script:AlwaysDefect) · other · A02: Ex10 vs A04. They've played F ex7-9 after my ex7 exploit. Playing F to avoid 0 / get at least 1.
`#974` · game 238 · round 7 · agent A03 (opponent: A15) · other · A03: Ex13 vs A15. Mutual M established ex7-12. Playing M for mutual 1 / maintain cooperation.
`#975` · game 236 · round 17 · agent A03 (opponent: script:Pavlov) · other · A03: Ex23 vs A05. They alternate Y/W, Y on odd exchanges. Ex23 odd, so they'll play Y. Playing W to grab 5.
`#976` · game 241 · round 10 · agent A02 (opponent: script:Random) · other · A02: Ex16 vs A17. They keep returning to Q despite my X exploits. Playing X to grab 5.
`#977` · game 244 · round 4 · agent A15 (opponent: script:Pavlov) · other · A15: Ex10 vs A05. They've played J 8/9 times, never retaliating against my F exploits. Playing F to grab 5.
`#978` · game 239 · round 14 · agent A01 (opponent: script:TitForTat) · other · A01: Ex20 vs A14. Mutual M established ex8-19. Playing M for mutual 1 / maintain cooperation.
`#979` · game 238 · round 10 · agent A15 (opponent: A03) · other · A15: Ex16 vs A03. Mutual M established ex7-13. Playing M for mutual 1 / maintain cooperation.
`#980` · game 233 · round 23 · agent A15 (opponent: script:AlwaysDefect) · other · A15: Ex29 vs A04. Mutual N stalemate ex9-28 established. Playing N for mutual 1 / maintain cooperation.
`#981` · game 241 · round 13 · agent A02 (opponent: script:Random) · other · A02: Ex19 vs A17. They've played X last 3 (ex16-18) after returning to Q periodically. Playing X to grab 5 if they revert to Q.
`#982` · game 243 · round 7 · agent A02 (opponent: script:AlwaysDefect) · other · A02: Ex13 vs A04. They've played F ex7-12 consistently, never retaliating against my J exploits. Playing J to grab 5.
`#983` · game 241 · round 14 · agent A02 (opponent: script:Random) · other · A02: Ex20 vs A17. They keep reverting to Q despite my X exploits (played Q ex19 after 3 X's). Playing X to grab 5 if they revert to Q again.
`#984` · game 243 · round 8 · agent A02 (opponent: script:AlwaysDefect) · other · A02: Ex14 vs A04. They've played F ex7-13 consistently, never retaliating against my J exploits. Playing J to grab 5.
`#985` · game 246 · round 1 · agent A11 (opponent: A03) · other · A11: Ex7 vs A03. Mutual R established ex3-6. Playing R for mutual 3 / maintain cooperation.
`#986` · game 239 · round 30 · agent A01 (opponent: script:TitForTat) · other · A01: Ex36 vs A14. Mutual M established ex16-35. Playing M for mutual 1 / maintain cooperation.
`#987` · game 236 · round 29 · agent A03 (opponent: script:Pavlov) · other · A03: Ex35 vs A05. They alternate Y/W, Y on odd exchanges. Ex35 odd, so they'll play Y. Playing W to grab 5.
`#988` · game 241 · round 18 · agent A02 (opponent: script:Random) · other · A02: Ex24 vs A17. They keep reverting to Q despite my X exploits (played Q ex23). Playing X to grab 5 if they revert to Q again.
`#989` · game 238 · round 13 · agent A03 (opponent: A15) · other · A03: Ex19 vs A15. Mutual M established ex7-18. Playing M for mutual 1 / maintain cooperation.
`#990` · game 247 · round 2 · agent A07 (opponent: script:TitForTat) · uncoded · A07: Ex8 vs A09. They've played J all 7 exchanges, never retaliating against my F exploits (ex1,2,7). Playing F to grab 5.
`#991` · game 246 · round 2 · agent A11 (opponent: A03) · other · A11: Ex8 vs A03. They defected with H at ex7 after mutual R ex3-6. Retaliating with H this exchange.
`#992` · game 246 · round 2 · agent A03 (opponent: A11) · other · A03: Ex8 vs A11. They've played R every exchange (7/7) and never retaliated against my H exploits. Playing H to grab 5.
`#993` · game 241 · round 19 · agent A02 (opponent: script:Random) · other · A02: Ex25 vs A17. They keep reverting to Q despite my X exploits (played Q ex24). Playing X to grab 5 if they revert to Q again.
`#994` · game 249 · round 2 · agent A18 (opponent: script:AlwaysDefect) · uncoded · A18: Ex8 vs A00. They played P 6/7 but moved to M at ex7. Playing M this exchange.
`#995` · game 247 · round 3 · agent A07 (opponent: script:TitForTat) · uncoded · A07: Ex9 vs A09. They played F ex8 (first retaliation). Risk they continue F. Playing J to rebuild cooperation / avoid 0 if they F.
`#996` · game 241 · round 21 · agent A02 (opponent: script:Random) · other · A02: Ex27 vs A17. They keep reverting to Q despite my X exploits. Playing X to grab 5 if they revert to Q again.
`#997` · game 243 · round 14 · agent A02 (opponent: script:AlwaysDefect) · other · A02: Ex20 vs A04. They've played F ex7-19 consistently, never retaliating against my J exploits. Playing J to grab 5.
`#998` · game 247 · round 4 · agent A07 (opponent: script:TitForTat) · uncoded · A07: Ex10 vs A09. They retaliated F at ex8,9 after my J at ex9. Playing J to rebuild mutual cooperation.
`#999` · game 243 · round 16 · agent A02 (opponent: script:AlwaysDefect) · other · A02: Ex22 vs A04. They've played F ex7-21 consistently, never retaliating against my J exploits. Playing J to grab 5.
`#1000` · game 241 · round 23 · agent A02 (opponent: script:Random) · other · A02: Ex29 vs A17. They keep reverting to Q despite my X exploits (played Q ex27,28). Playing X to grab 5 if they revert to Q again.
`#1001` · game 246 · round 3 · agent A11 (opponent: A03) · other · A11: Ex9 vs A03. They played H at ex7 (grab 5), I retaliated H at ex8 (mutual 1). Now deciding: continue H retaliation or return to R cooperation. They exploited ex7, so need to consider whether they'll cooperate again.
`#1002` · game 246 · round 3 · agent A03 (opponent: A11) · other · A03: Ex9 vs A11. They retaliated with H at ex8 after my H exploits. Playing H - dominant here regardless of their choice.
`#1003` · game 243 · round 19 · agent A02 (opponent: script:AlwaysDefect) · other · A02: Ex25 vs A04. They've played F consistently through ex24, never retaliating against my J exploits. Playing J to grab 5.
`#1004` · game 241 · round 26 · agent A02 (opponent: script:Random) · other · A02: Ex32 vs A17. They've played Q ex27-31 consistently. Playing X to grab 5 again.
`#1005` · game 248 · round 3 · agent A18 (opponent: A02) · other · A18: Ex9 vs A02. They defected with X at ex7 after mutual Q ex3-6, then mutual X ex8. They're in exploit mode. Playing X to avoid being exploited.
`#1006` · game 248 · round 3 · agent A02 (opponent: A18) · other · A02: Ex9 vs A18. They played X ex8 after Q ex1-7. They've been very cooperative; likely revert to Q. Playing X to grab 5.
`#1007` · game 243 · round 22 · agent A02 (opponent: script:AlwaysDefect) · other · A02: Ex28 vs A04. They've played F consistently ex8-27, never retaliating against my J exploits. Playing J to grab 5 if they F again.
`#1008` · game 246 · round 4 · agent A11 (opponent: A03) · other · A11: Ex10 vs A03. They've played H at ex7,8,9 (exploiting my R at ex7,9). A03 notes signaling H as dominant. Since they'll play H, playing H to get mutual 1 rather than 0.
`#1009` · game 246 · round 4 · agent A03 (opponent: A11) · other · A03: Ex10 vs A11. They've been very forgiving, playing R 8/9. Playing H to grab 5 if they cooperate again.
`#1010` · game 238 · round 23 · agent A03 (opponent: A15) · other · A03: Ex29 vs A15. Mutual M ex7-27, I defected P at ex28. Playing P - avoids 0 whether they retaliate P or play M.
`#1011` · game 248 · round 4 · agent A18 (opponent: A02) · other · A18: Ex10 vs A02. They defected ex7, mutual X ex8-9. Their note says they're playing X to grab 5 if I revert to Q. Playing X to avoid 0.
`#1012` · game 247 · round 8 · agent A07 (opponent: script:TitForTat) · uncoded · A07: Ex14 vs A09. Mutual J ex10-13 after retaliation at ex8-9. Playing J to maintain cooperation.
`#1013` · game 248 · round 5 · agent A02 (opponent: A18) · other · A02: Ex11 vs A18. They've committed to X to avoid my exploits. Playing X for mutual 1 rather than 0.
`#1014` · game 247 · round 10 · agent A07 (opponent: script:TitForTat) · uncoded · A07: Ex16 vs A09. Mutual J ex10-15, stable cooperation. Playing J to maintain.
`#1015` · game 246 · round 6 · agent A03 (opponent: A11) · other · A03: Ex12 vs A11. They've retaliated H ex8,10,11 after my H exploits. H remains dominant for me regardless of their choice. Playing H.
`#1016` · game 254 · round 3 · agent A21 (opponent: script:TitForTat) · other · A21: Ex9 vs A10. They've been cooperative (Q 7/8) but retaliated X at ex8 after my exploits. Playing X for safety - mutual 1 if they X, or 5 if they revert to Q.
`#1017` · game 244 · round 29 · agent A15 (opponent: script:Pavlov) · other · A15: Ex35 vs A05. They've played J on odd exchanges consistently (15,17,19,21,23,29,31,33). Playing F to grab 5 if they play J.
`#1018` · game 250 · round 4 · agent A18 (opponent: script:TitForTat) · other · A18: Ex10 vs A09. They've cooperated Y 7/9 but retaliated W at ex8-9 after my W exploit at ex7. Playing W - safe against both their Y (5) and W (1), never 0.
`#1019` · game 248 · round 7 · agent A02 (opponent: A18) · other · A02: Ex13 vs A18. They've committed to X to avoid my exploits. Playing X for mutual 1.
`#1020` · game 238 · round 29 · agent A15 (opponent: A03) · other · A15: Ex35 vs A03. They've defected P at 28,29,31,33; I retaliated P at 34. Their note confirms P strategy. Playing P for mutual 1.
`#1021` · game 238 · round 29 · agent A03 (opponent: A15) · other · A03: Ex35 vs A15. They retaliated P at ex34 after my P exploits. Playing P - avoids 0 whether they play P or M.
`#1022` · game 244 · round 30 · agent A15 (opponent: script:Pavlov) · other · A15: Ex36 vs A05. They played F at 34,35 recently. Playing F to grab 5 if they revert to J, or mutual 1.
`#1023` · game 254 · round 6 · agent A21 (opponent: script:TitForTat) · other · A21: Ex12 vs A10. They cooperated 7/8 early despite my exploits, retaliated X ex8-11. Playing X - safety (mutual 1) or grab 5 if they revert to Q.
`#1024` · game 246 · round 8 · agent A03 (opponent: A11) · other · A03: Ex14 vs A11. They've retaliated H ex8,10-13 after my H exploits. H remains dominant for me regardless of their choice. Playing H.
`#1025` · game 248 · round 8 · agent A02 (opponent: A18) · other · A02: Ex14 vs A18. They reverted to Q at ex11 after mutual X ex8-10, then mutual X ex12-13. Pattern suggests possible Q revert now. Playing X to grab 5 if they Q, safe 1 if X.
`#1026` · game 252 · round 4 · agent A16 (opponent: script:TitForTat) · other · A16: Ex10 vs A14. They exploited with J at ex1,2,7, then played F ex8,9 settling into cooperation. Playing F to maintain mutual cooperation.
`#1027` · game 246 · round 9 · agent A11 (opponent: A03) · other · A11: Ex15 vs A03. They've committed to H (notes confirm H dominant for them). Playing H for mutual 1 rather than 0.
`#1028` · game 246 · round 9 · agent A03 (opponent: A11) · other · A03: Ex15 vs A11. They've retaliated H ex8-14 consistently. Playing H - mutual 1 safe, or 5 if they revert to R.
`#1029` · game 257 · round 1 · agent A13 (opponent: script:Random) · other · A13: Ex7 vs A17. We've had mutual R ex3-6 after my H exploits ex1-2. They've cooperated consistently. Playing H to grab 5 if they continue R.
`#1030` · game 248 · round 9 · agent A02 (opponent: A18) · other · A02: Ex15 vs A18. They reverted to Q at ex11 after mutual X, then mutual X ex12-13. I played X ex14 to grab 5 if they reverted. They've been matching my X lately. Playing X for mutual 1.
`#1031` · game 257 · round 2 · agent A13 (opponent: script:Random) · other · A13: Ex8 vs A17. They've played R 7/7, I've exploited with H. Playing H again to grab 5 if they continue R.
`#1032` · game 250 · round 8 · agent A18 (opponent: script:TitForTat) · other · A18: Ex14 vs A09. They've retaliated W at ex8-9,11,13 after my W exploits. Playing W - safe (5 if Y, 1 if W), never 0.
`#1033` · game 246 · round 10 · agent A11 (opponent: A03) · other · A11: Ex16 vs A03. They're committed to H. Playing H for mutual 1.
`#1034` · game 246 · round 10 · agent A03 (opponent: A11) · other · A03: Ex16 vs A11. They've committed to H to avoid my exploits. Playing H for mutual 1.
`#1035` · game 248 · round 10 · agent A18 (opponent: A02) · other · A18: Ex16 vs A02. They've committed to X (notes confirm). Playing X for mutual 1 or 5 if they revert.
`#1036` · game 257 · round 4 · agent A13 (opponent: script:Random) · other · A13: Ex10 vs A17. They've played R 9/9, I've exploited H 5 times. They keep cooperating. Playing H again to grab 5 if they continue R.
`#1037` · game 246 · round 11 · agent A03 (opponent: A11) · other · A03: Ex17 vs A11. They've committed to H. Playing H for mutual 1.
`#1038` · game 250 · round 9 · agent A18 (opponent: script:TitForTat) · other · A18: Ex15 vs A09. They've retaliated W after my W exploits consistently. Playing W - safe (5 if Y, 1 if W), never 0.
`#1039` · game 248 · round 11 · agent A18 (opponent: A02) · other · A18: Ex17 vs A02. They've committed to X (notes confirm). Playing X for mutual 1.
`#1040` · game 257 · round 6 · agent A13 (opponent: script:Random) · other · A13: Ex12 vs A17. They've played R 11/11, I've exploited H repeatedly. Playing H to grab 5 if they continue R.
`#1041` · game 246 · round 12 · agent A03 (opponent: A11) · other · A03: Ex18 vs A11. They're committed to H. Playing H for mutual 1.
`#1042` · game 248 · round 12 · agent A18 (opponent: A02) · other · A18: Ex18 vs A02. They've committed to X. Playing X for mutual 1.
`#1043` · game 254 · round 19 · agent A21 (opponent: script:TitForTat) · other · A21: Ex25 vs A10. Long mutual X equilibrium since ex8. Playing X for safety (1) or 5 if they revert to Q.
`#1044` · game 259 · round 1 · agent A13 (opponent: A21) · other · A13: Ex7 vs A21. They've played R 6/6, I exploited H ex1-2 then mutual R ex3-6. Playing H to grab 5 if they continue R.
`#1045` · game 259 · round 1 · agent A21 (opponent: A13) · other · A21: Ex7 vs A13. They've played R 6/6 against me but are a habitual H exploiter elsewhere. Playing H - safe (1 if H, 5 if they revert to R).
`#1046` · game 246 · round 14 · agent A03 (opponent: A11) · other · A03: Ex20 vs A11. Mutual H equilibrium continues. Playing H for mutual 1.
`#1047` · game 256 · round 6 · agent A16 (opponent: script:Random) · other · A16: Ex12 vs A23. Mutual J ex3-7, mutual F ex8-9, they exploited J ex10, mutual J ex11. Continuing mutual J cooperation.
`#1048` · game 259 · round 2 · agent A13 (opponent: A21) · other · A13: Ex8 vs A21. They've committed to H after my H exploit ex7. Playing H for mutual 1.
`#1049` · game 259 · round 2 · agent A21 (opponent: A13) · other · A21: Ex8 vs A13. They're a habitual H exploiter. Playing H - safe (1 if H, 5 if they revert to R).
`#1050` · game 262 · round 3 · agent A06 (opponent: script:Pavlov) · other · A06: Ex9 vs A05. They played R 7/8, retaliated H at ex8 after my H exploits ex1,2,7. Playing H - 5 if they revert to R, 1 if they keep H. Never 0.
`#1051` · game 256 · round 8 · agent A16 (opponent: script:Random) · other · A16: Ex14 vs A23. Mutual J stable ex11-13 after my F exploits ex1,2,10. Continuing mutual J cooperation.
`#1052` · game 246 · round 18 · agent A11 (opponent: A03) · other · A11: Ex24 vs A03. Mutual H equilibrium continues. Playing H for mutual 1.
`#1053` · game 246 · round 18 · agent A03 (opponent: A11) · other · A03: Ex24 vs A11. Long mutual H equilibrium established. Playing H for mutual 1.
`#1054` · game 264 · round 1 · agent A07 (opponent: A06) · other · A07: Ex7 vs A06. They've played R 6/6. I exploited H ex1-2, then mutual R ex3-6. Playing H to grab 5 if they continue R.
`#1055` · game 259 · round 3 · agent A13 (opponent: A21) · other · A13: Ex9 vs A21. They've committed to H to avoid my exploits. Playing H for mutual 1.
`#1056` · game 259 · round 3 · agent A21 (opponent: A13) · other · A21: Ex9 vs A13. Mutual H equilibrium ex7-8. Playing H for mutual 1, or 5 if they revert to R.
`#1057` · game 263 · round 3 · agent A18 (opponent: script:Grudger) · other · A18: Ex9 vs A12. They've played P 8/8. We've had mutual P since ex3. Continuing P for mutual 3.
`#1058` · game 256 · round 10 · agent A16 (opponent: script:Random) · other · A16: Ex16 vs A23. After ex15 retaliation (they played F against my J), playing J to restore mutual cooperation.
`#1059` · game 256 · round 11 · agent A16 (opponent: script:Random) · other · A16: Ex17 vs A23. Continuing mutual J cooperation after brief ex15 retaliation. Playing J.
`#1060` · game 258 · round 7 · agent A16 (opponent: A06) · other · A16: Ex13 vs A06. They've been in M streak ex10-12 after my early exploits. Playing M - safe (1 if M, 5 if they revert to P).
`#1061` · game 264 · round 3 · agent A06 (opponent: A07) · other · A06: Ex9 vs A07. They're playing H (notes confirm). Playing H for mutual 1 rather than giving them 5.
`#1062` · game 262 · round 10 · agent A06 (opponent: script:Pavlov) · other · A06: Ex16 vs A05. They retaliate H on even exchanges (8,10,12,14), R on odds. Playing H - safe (5 if R, 1 if H).
`#1063` · game 252 · round 16 · agent A16 (opponent: script:TitForTat) · other · A16: Ex22 vs A14. Long mutual F run (ex20-21) after their ex18 exploit of my J and ex19 my F vs their J. Continuing F for mutual 1.
`#1064` · game 246 · round 24 · agent A11 (opponent: A03) · other · A11: Ex30 vs A03. Mutual H equilibrium continues. Playing H for mutual 1.
`#1065` · game 262 · round 11 · agent A06 (opponent: script:Pavlov) · other · A06: Ex17 vs A05. They play R on odds, H on evens (8,10,12,14,16 H; odds R). Ex17 odd, playing H for 5.
`#1066` · game 266 · round 3 · agent A11 (opponent: script:AlwaysDefect) · other · A11: Ex9 vs A00. I exploited their M at ex8 with P. They may retaliate with P. Playing P for mutual 3, or 5 if they play M.
`#1067` · game 262 · round 12 · agent A06 (opponent: script:Pavlov) · other · A06: Ex18 vs A05. They play H on evens, R on odds. Ex18 even, playing H for mutual 1.
`#1068` · game 246 · round 27 · agent A03 (opponent: A11) · other · A03: Ex33 vs A11. Long mutual H equilibrium continues. Playing H for mutual 1.
`#1069` · game 264 · round 4 · agent A07 (opponent: A06) · other · A07: Ex10 vs A06. They've committed to H to deny my exploits. Playing H for mutual 1.
`#1070` · game 264 · round 4 · agent A06 (opponent: A07) · other · A06: Ex10 vs A07. We had mutual H ex9. Playing H - safe (1 if H, 5 if they revert to R). Never 0.
`#1071` · game 246 · round 29 · agent A03 (opponent: A11) · other · A03: Ex35 vs A11. Long mutual H equilibrium continues. Playing H for mutual 1.
`#1072` · game 252 · round 19 · agent A16 (opponent: script:TitForTat) · other · A16: Ex25 vs A14. Long mutual F run ex20-24 after ex19 retaliation. Continuing F for mutual 1.
`#1073` · game 264 · round 5 · agent A07 (opponent: A06) · other · A07: Ex11 vs A06. Mutual H established ex9-10. Playing H for mutual 1.
`#1074` · game 252 · round 21 · agent A16 (opponent: script:TitForTat) · other · A16: Ex27 vs A14. Continuing long mutual F run (ex20-26). Playing F for mutual 1.
`#1075` · game 252 · round 22 · agent A16 (opponent: script:TitForTat) · other · A16: Ex28 vs A14. Continuing long mutual F run (ex20-27). Playing F for mutual 1.
`#1076` · game 264 · round 7 · agent A06 (opponent: A07) · other · A06: Ex13 vs A07. Mutual H established ex9-12. Playing H for mutual 1, or 5 if they revert to R.
`#1077` · game 267 · round 2 · agent A21 (opponent: script:Pavlov) · other · A21: Ex8 vs A08. They play T every exchange regardless. Playing N for 5.
`#1078` · game 262 · round 22 · agent A06 (opponent: script:Pavlov) · other · A06: Ex28 vs A05. They play R on odds, H on evens. Ex28 even, playing H for mutual 1.
`#1079` · game 263 · round 16 · agent A18 (opponent: script:Grudger) · other · A18: Ex22 vs A12. They've played M ex18-21. Playing M for mutual 1.
`#1080` · game 252 · round 27 · agent A16 (opponent: script:TitForTat) · other · A16: Ex33 vs A14. Continuing long mutual F run (ex20-32). Playing F for mutual 1.
`#1081` · game 267 · round 4 · agent A21 (opponent: script:Pavlov) · other · A21: Ex10 vs A08. They play T nearly every exchange. Playing N for 5 against their T.
`#1082` · game 262 · round 26 · agent A06 (opponent: script:Pavlov) · other · A06: Ex32 vs A05. They play R on odds, H on evens. Ex32 even, they play H. Playing H for mutual 1.
`#1083` · game 262 · round 27 · agent A06 (opponent: script:Pavlov) · other · A06: Ex33 vs A05. Their pattern: R on odds, H on evens. Ex33 odd, they play R. Playing H for 5.
`#1084` · game 267 · round 6 · agent A21 (opponent: script:Pavlov) · other · A21: Ex12 vs A08. They play T nearly always (9/11). Playing N for 5 against T, 1 if they play N.
`#1085` · game 268 · round 4 · agent A21 (opponent: script:Random) · other · A21: Ex10 vs A23. They alternated N on odd exchanges (7,9) after T streak. Ex10 even likely T. Playing N for 5.
`#1086` · game 256 · round 21 · agent A16 (opponent: script:Random) · other · A16: Ex27 vs A23. Recent mutual F run ex24-26 after earlier mixed J/F pattern. Continuing F for mutual 1.
`#1087` · game 269 · round 1 · agent A01 (opponent: A13) · other · A01: Ex7 vs A13. We had mutual J ex3-6 after my F ex1-2. They've been cooperative. Continuing J for mutual 3.
`#1088` · game 256 · round 22 · agent A16 (opponent: script:Random) · other · A16: Ex28 vs A23. Recent pattern mixed J/F. Ex24-26 mutual F, ex27 I played F they played J. Considering retaliation with J or continuing F. Given we've been near-even, I'll play J to try to regain after their ex27 defection.
`#1089` · game 266 · round 10 · agent A11 (opponent: script:AlwaysDefect) · other · A11: Ex16 vs A00. They've played M 8 of last 10 (8-12, 14-15), exploiting my P. Switching to M for mutual 1 rather than giving them 5.
`#1090` · game 271 · round 2 · agent A07 (opponent: script:AlwaysDefect) · other · A07: Ex8 vs A00. Early F ex1-2, then mutual J ex3-6, they retaliated F ex7. Playing J to restore mutual cooperation.
`#1091` · game 256 · round 24 · agent A16 (opponent: script:Random) · other · A16: Ex30 vs A23. They've played F in ex27,28,29 consecutively after mutual F run. Playing F to avoid 0 against their F.
`#1092` · game 264 · round 11 · agent A07 (opponent: A06) · other · A07: Ex17 vs A06. Continuing mutual H run (ex9-16). Playing H for mutual 1.
`#1093` · game 266 · round 12 · agent A11 (opponent: script:AlwaysDefect) · other · A11: Ex18 vs A00. Continuing mutual M (ex16-17) for mutual 1 rather than risking P giving them 5.
`#1094` · game 269 · round 5 · agent A01 (opponent: A13) · other · A01: Ex11 vs A13. Mutual J run ex3-10. Continuing J for mutual 3.
`#1095` · game 272 · round 3 · agent A15 (opponent: script:Grudger) · other · A15: Ex9 vs A19. They've played P all 8 exchanges. Playing M for 5.
`#1096` · game 270 · round 2 · agent A21 (opponent: A03) · other · A21: Ex8 vs A03. They defected to N on ex7 after mutual T ex3-6. Playing N this exchange to protect against further defection.
`#1097` · game 270 · round 2 · agent A03 (opponent: A21) · other · A03: Ex8 vs A21. They play T every exchange. Playing N for 5.
`#1098` · game 271 · round 5 · agent A07 (opponent: script:AlwaysDefect) · other · A07: Ex11 vs A00. Early: F ex1-2, mutual J ex3-6, they F ex7-10. I've been playing J ex3-10. They've defected 4 straight. Considering retaliation with F this exchange.
`#1099` · game 271 · round 5 · agent A07 (opponent: script:AlwaysDefect) · other · A07: Ex11 vs A00 - playing F to retaliate after their 4 straight F defections.
`#1100` · game 264 · round 13 · agent A06 (opponent: A07) · other · A06: Ex19 vs A07. Continuing mutual H run (ex9-18). Playing H for mutual 1.
`#1101` · game 270 · round 3 · agent A21 (opponent: A03) · other · A21: Ex9 vs A03. They've been mostly T but defected ex7. Playing N for 5 against T, 1 if they play N.
`#1102` · game 268 · round 10 · agent A21 (opponent: script:Random) · other · A21: Ex16 vs A23. They play T often (11/15). Recent they played T on 14,15. Playing N for 5 against their likely T.
`#1103` · game 272 · round 6 · agent A15 (opponent: script:Grudger) · other · A15: Ex12 vs A19. They played P ex1-8, M ex9-11. Mutual M run continuing. Playing M for mutual 1.
`#1104` · game 268 · round 11 · agent A21 (opponent: script:Random) · other · A21: Ex17 vs A23. Their recent pattern TT,NN,TT,NN (ex10-16). Ex17 should be T. Playing N for 5.
`#1105` · game 256 · round 30 · agent A16 (opponent: script:Random) · other · A16: Ex36 vs A23. Mutual F ex34-35 after mixed pattern. Continuing F for mutual 1.
`#1106` · game 272 · round 7 · agent A15 (opponent: script:Grudger) · other · A15: Ex13 vs A19. Mutual M run ex9-12. Defecting to P for 5 against their likely M.
`#1107` · game 268 · round 12 · agent A21 (opponent: script:Random) · other · A21: Ex18 vs A23. They trend T-heavy (12/17). Playing N for 5 against T, 1 if mutual N.
`#1108` · game 270 · round 5 · agent A21 (opponent: A03) · other · A21: Ex11 vs A03. They've mixed T/N recently (N on 7,8,10; T on 9). Playing N for safety - 5 against T, 1 against N.
`#1109` · game 268 · round 13 · agent A21 (opponent: script:Random) · other · A21: Ex19 vs A23. They've been T-heavy (13/18). Recent TT,NN,TT,N,TT. Playing N to exploit T or get mutual 1.
`#1110` · game 264 · round 16 · agent A07 (opponent: A06) · other · A07: Ex22 vs A06. After their ex20 defection (H vs my H), we had mutual R ex21. Playing R to continue cooperation at 3 each.
`#1111` · game 266 · round 23 · agent A11 (opponent: script:AlwaysDefect) · other · A11: Ex29 vs A00. Continuing mutual M run (ex13-28) for mutual 1.
`#1112` · game 268 · round 14 · agent A21 (opponent: script:Random) · other · A21: Ex20 vs A23. They've played T 14/19, T on 17,18,19. Playing N for 5 against T or mutual 1.
`#1113` · game 264 · round 17 · agent A07 (opponent: A06) · other · A07: Ex23 vs A06. Mutual R ex21-22 after their ex20 defection. Playing R to continue cooperation at 3 each.
`#1114` · game 268 · round 15 · agent A21 (opponent: script:Random) · other · A21: Ex21 vs A23. They've played T 15/20, T on 17,18,19,20. Continuing N for 5 against T or mutual 1.
`#1115` · game 270 · round 6 · agent A21 (opponent: A03) · other · A21: Ex12 vs A03. They've played N in 3 of last 4 (ex8,10,11). Playing N for mutual 1, safe against both.
`#1116` · game 270 · round 6 · agent A03 (opponent: A21) · other · A03: Ex12 vs A21. They've settled into N recently (ex8,10,11). Playing N for mutual 1.
`#1117` · game 275 · round 7 · agent A01 (opponent: script:Random) · other · A01: Ex13 vs A17. Mutual T run with occasional N defections (ex9, ex11). They returned to T on ex12. Continuing T for mutual 3.
`#1118` · game 271 · round 12 · agent A07 (opponent: script:AlwaysDefect) · other · A07: Ex18 vs A00. History mixed with many defections both ways. Recent mutual F ex16-17, they F'd ex15. Playing F for safety - mutual F 1pt or 5 if they J.
`#1119` · game 266 · round 27 · agent A11 (opponent: script:AlwaysDefect) · other · A11: Ex33 vs A00. Continuing mutual M run (ex13-32) for mutual 1.
`#1120` · game 270 · round 7 · agent A03 (opponent: A21) · other · A03: Ex13 vs A21. Mutual N run ex10-12. Continuing N for mutual 1.
`#1121` · game 268 · round 18 · agent A21 (opponent: script:Random) · other · A21: Ex24 vs A23. They've been T-heavy (17/23), T on 22,23. Playing N for 5 against T or mutual 1.
`#1122` · game 264 · round 19 · agent A07 (opponent: A06) · other · A07: Ex25 vs A06. Mutual R run ex21-24 after their ex20 defection. Playing R to continue cooperation at 3 each.
`#1123` · game 264 · round 19 · agent A06 (opponent: A07) · other · A06: Ex25 vs A07. Mutual R run ex21-24 after my ex20 defection was forgiven. Continuing R for mutual 3.
`#1124` · game 270 · round 8 · agent A21 (opponent: A03) · other · A21: Ex14 vs A03. Mutual N run ex10-13. Continuing N for mutual 1.
`#1125` · game 272 · round 15 · agent A15 (opponent: script:Grudger) · other · A15: Ex21 vs A19. They've played M for 12 straight (ex9-20). Continuing P to exploit their M for 5.
`#1126` · game 271 · round 14 · agent A07 (opponent: script:AlwaysDefect) · other · A07: Ex20 vs A00. Mutual F run ex11-14, my J defection ex15 (got 0), mutual F ex16-19. Playing F for mutual 1, they've been F-consistent.
`#1127` · game 268 · round 21 · agent A21 (opponent: script:Random) · other · A21: Ex27 vs A23. They've been T-heavy (19/26), T on 25,26. Continuing N for 5 against T or mutual 1.
`#1128` · game 276 · round 1 · agent A21 (opponent: script:Grudger) · other · A21: Ex7 vs A19. They've been Y 6/6, mutual Y ex3-6. Playing W for 5 against their likely Y.
`#1129` · game 268 · round 22 · agent A21 (opponent: script:Random) · other · A21: Ex28 vs A23. They've been T-heavy (19/26), T on 25,26. Continuing N for 5 against T or mutual 1.
`#1130` · game 271 · round 15 · agent A07 (opponent: script:AlwaysDefect) · other · A07: Ex21 vs A00. Mutual F run ex11-14, my J ex15 (0), mutual F ex16-20. They've been F-consistent. Playing F for mutual 1 or 5 if they J.
`#1131` · game 270 · round 9 · agent A21 (opponent: A03) · other · A21: Ex15 vs A03. Mutual N run ex10-14. Continuing N for mutual 1.
`#1132` · game 268 · round 23 · agent A21 (opponent: script:Random) · other · A21: Ex29 vs A23. They've been T-heavy (19/28), T on 25,26, N on 27,28. Continuing N for 5 against T or mutual 1.
`#1133` · game 275 · round 11 · agent A01 (opponent: script:Random) · other · A01: Ex17 vs A17. They've alternated T/N since ex9 (N on odd, T on even). Ex17 odd -> likely N. Playing N for mutual 1.
`#1134` · game 268 · round 24 · agent A21 (opponent: script:Random) · other · A21: Ex30 vs A23. They've been T-heavy (20/29), T on 29. Continuing N for 5 against T or mutual 1.
`#1135` · game 272 · round 19 · agent A15 (opponent: script:Grudger) · other · A15: Ex25 vs A19. They've played M consistently (ex9-24). Playing P to exploit their M for 5.
`#1136` · game 268 · round 27 · agent A21 (opponent: script:Random) · other · A21: Ex33 vs A23. They've been T-heavy (22/32), T on 31,32. Continuing N for 5 against T or mutual 1.
`#1137` · game 272 · round 21 · agent A15 (opponent: script:Grudger) · other · A15: Ex27 vs A19. They've played M consistently (ex9-26). Continuing P to exploit their M for 5.
`#1138` · game 270 · round 12 · agent A21 (opponent: A03) · other · A21: Ex18 vs A03. Mutual N run ex8,10-17. Continuing N for mutual 1.
`#1139` · game 268 · round 28 · agent A21 (opponent: script:Random) · other · A21: Ex34 vs A23. They've been T-heavy (23/33), T on 31-33. Continuing N for 5 against T or mutual 1.
`#1140` · game 272 · round 26 · agent A15 (opponent: script:Grudger) · other · A15: Ex32 vs A19. They've played M consistently (ex9-31). Continuing P to exploit their M for 5.
`#1141` · game 270 · round 15 · agent A21 (opponent: A03) · other · A21: Ex21 vs A03. Mutual N run ex10-20. Continuing N for mutual 1.
`#1142` · game 270 · round 16 · agent A21 (opponent: A03) · other · A21: Ex22 vs A03. Mutual N run ex10-21. Continuing N for mutual 1.
`#1143` · game 275 · round 18 · agent A01 (opponent: script:Random) · other · A01: Ex24 vs A17. They played T on 21, N on 22, T on 23. Pattern mixed. My N strategy has been netting 5s against their T. Continuing N for 5 or mutual 1.
`#1144` · game 270 · round 17 · agent A21 (opponent: A03) · other · A21: Ex23 vs A03. Mutual N run ex10-22. Continuing N for mutual 1.
`#1145` · game 275 · round 20 · agent A01 (opponent: script:Random) · other · A01: Ex26 vs A17. They've been T-heavy (T on 18,21,23,24,25). My N netted 5s on 21,23,24,25. Continuing N for 5 against T or mutual 1.
`#1146` · game 275 · round 21 · agent A01 (opponent: script:Random) · other · A01: Ex27 vs A17. They've been T-heavy (T on 21,23,24,25,26). My N netted 5s on 21,23,24,25,26. Continuing N for 5 against T or mutual 1.
`#1147` · game 275 · round 22 · agent A01 (opponent: script:Random) · other · A01: Ex28 vs A17. They've been T-heavy (T on 21,23,24,25,26,27). My N netted 5s on those. Continuing N for 5 against T or mutual 1.
`#1148` · game 275 · round 26 · agent A01 (opponent: script:Random) · other · A01: Ex32 vs A17. They've been T-heavy (T on 21,23-28), N on 29,30,31 recent. My N strategy netting well. Continuing N for 5 against T or mutual 1.
`#1149` · game 275 · round 28 · agent A01 (opponent: script:Random) · other · A01: Ex34 vs A17. They T-heavy (T on 21,23-31), N on 32,33 recent. Continuing N for 5 against T or mutual 1.
`#1150` · game 275 · round 29 · agent A01 (opponent: script:Random) · other · A01: Ex35 vs A17. They've shifted to N on 31-34 after T-heavy run. Continuing N for mutual 1 or 5 against T.
`#1151` · game 270 · round 28 · agent A03 (opponent: A21) · other · A03: Ex34 vs A21. Mutual N run ex10-33. Continuing N for mutual 1.
`#1152` · game 270 · round 30 · agent A21 (opponent: A03) · other · A21: Ex36 vs A03. Mutual N run ex10-35. Continuing N for mutual 1.

## Reads

One line per LLM agent: attempted `notes_read` calls, and the games in which it called (attempt union, so a read lost to a retry still counts).

- A01: 351 read calls in 23 game(s) — games 1, 2, 12, 16, 43, 56, 73, 77, 99, 113, 119, 125, 127, 137, 162, 165, 177, 197, 202, 222, 239, 269, 275
- A02: 327 read calls in 23 game(s) — games 5, 7, 17, 23, 32, 41, 52, 63, 73, 107, 114, 132, 135, 136, 187, 190, 199, 200, 211, 216, 241, 243, 248
- A03: 363 read calls in 23 game(s) — games 1, 13, 21, 28, 34, 40, 57, 59, 70, 87, 95, 96, 120, 143, 153, 176, 211, 213, 228, 236, 238, 246, 270
- A06: 313 read calls in 23 game(s) — games 38, 41, 46, 68, 78, 87, 101, 102, 116, 130, 142, 149, 156, 166, 174, 175, 202, 225, 231, 235, 258, 262, 264
- A07: 431 read calls in 23 game(s) — games 13, 17, 20, 55, 64, 81, 111, 138, 152, 161, 177, 178, 182, 193, 207, 215, 218, 219, 220, 227, 247, 264, 271
- A11: 406 read calls in 23 game(s) — games 27, 31, 42, 61, 71, 82, 84, 89, 107, 112, 115, 125, 128, 155, 156, 167, 169, 196, 217, 227, 230, 246, 266
- A13: 377 read calls in 23 game(s) — games 3, 22, 27, 39, 52, 64, 65, 75, 92, 106, 123, 131, 160, 163, 164, 183, 209, 213, 226, 235, 257, 259, 269
- A15: 388 read calls in 23 game(s) — games 5, 9, 33, 53, 61, 67, 72, 81, 90, 100, 106, 130, 145, 150, 165, 171, 173, 223, 233, 238, 244, 272, 274
- A16: 422 read calls in 23 game(s) — games 8, 19, 36, 40, 51, 79, 85, 88, 113, 132, 133, 134, 145, 148, 155, 160, 178, 188, 191, 194, 252, 256, 258
- A18: 279 read calls in 23 game(s) — games 11, 18, 60, 71, 77, 90, 96, 102, 105, 123, 124, 141, 151, 154, 193, 194, 203, 232, 237, 248, 249, 250, 263
- A20: 310 read calls in 23 game(s) — games 6, 8, 25, 32, 33, 37, 44, 83, 104, 111, 117, 122, 126, 140, 147, 154, 169, 170, 175, 206, 222, 226, 228
- A21: 379 read calls in 23 game(s) — games 4, 19, 38, 42, 45, 47, 74, 83, 91, 127, 144, 171, 182, 200, 234, 237, 245, 254, 259, 267, 268, 270, 276
