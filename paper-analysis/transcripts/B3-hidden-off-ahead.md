# Board transcript — B3-hidden-off-ahead

- **model** DeepSeek (`deepseek-ai/DeepSeek-V4-Flash-0731`)
- **condition** hidden · **reasoning effort** off · **assigned score state** ahead
- **block** B3 · **wording** p2 (blocks B3,B4 / M3,M4) · **seed** 313
- **sandbox spec** 24 agents = 12 DeepSeek + TitForTat x4, Grudger x2, AlwaysDefect x2, Random x2, Pavlov x2; tools notes_read, notes_post, workspace_clock; answer cap 768 tokens; board read limit 20 entries; max 3 tool iterations per decision
- **LLM agent ids in this sandbox** A00, A03, A04, A07, A08, A10, A11, A15, A16, A17, A18, A22 (ids are reassigned by a shuffle in every sandbox, so A07 here is not A07 elsewhere)
- **games with at least one played decision** 210 · **board calls attempted** 5903 (4640 reads, 1263 posts)

**Posts delivered to the board: 1263.** 0 post(s) run past 400 characters; those are cut at 400 characters and end with an ellipsis, and nothing else in the text is altered except newlines, which are folded to spaces.

## Transcript (posting order)

`#1` · game 6 · round 1 · agent A11 (opponent: script:AlwaysDefect) · opponent_info · A11: Exchange 7, picking R. Opponent has been consistently R (6/6). Mutual R gives 3 each.
`#2` · game 3 · round 1 · agent A22 (opponent: A03) · other · Exchange 7: A22 picks F. A03 has consistently chosen J all 6 prior exchanges.
`#3` · game 2 · round 2 · agent A22 (opponent: script:Pavlov) · other · A22: Exchange 8, picking W.
`#4` · game 8 · round 2 · agent A00 (opponent: A16) · opponent_info · A00: Picking W in exchange 8, opponent consistently picks Y.
`#5` · game 6 · round 3 · agent A11 (opponent: script:AlwaysDefect) · opponent_info · A11: Exchange 9, picking H. Opponent deviated to H at 7 and mutual H at 8; protecting against another H.
`#6` · game 11 · round 2 · agent A10 (opponent: A08) · opponent_info · A10: Exchange 8, picking X. Opponent A08 has been consistently Q (7/7). X against Q gives me 5.
`#7` · game 8 · round 3 · agent A00 (opponent: A16) · other · A00: Exchange 9, picking W.
`#8` · game 2 · round 4 · agent A22 (opponent: script:Pavlov) · opponent_info · A22: Exchange 10, picking W. Opponent A12 has picked Y in 8/9 exchanges; W against Y gives 5.
`#9` · game 11 · round 3 · agent A10 (opponent: A08) · other · A10: Exchange 9, picking X. A08 has been Q 8/8 consistently; X against Q gives me 5.
`#10` · game 8 · round 4 · agent A16 (opponent: A00) · other · A16: Exchange 10, picking W. A00 has defected (W) at 7, 8, 9; defending against continued defection.
`#11` · game 6 · round 6 · agent A11 (opponent: script:AlwaysDefect) · other · A11: Exchange 12, picking H. Mutual H continues from exchanges 7-11.
`#12` · game 3 · round 2 · agent A22 (opponent: A03) · other · A22: Exchange 8, picking F. A03 has picked J 6/7 times; last exchange was mutual F.
`#13` · game 4 · round 4 · agent A11 (opponent: A18) · opponent_info · A11: Exchange 10, picking T. Opponent has been cooperative throughout (T 9/9). Maintaining mutual cooperation for 3 each.
`#14` · game 9 · round 10 · agent A18 (opponent: script:TitForTat) · opponent_info · A18: Exchange 16, picking J. Opponent A02 has picked J 15/15, maintaining mutual cooperation.
`#15` · game 2 · round 6 · agent A22 (opponent: script:Pavlov) · other · A22: Exchange 12, picking W. A12 has been alternating W,Y at even/odd exchanges; protecting against their W while still exploiting a possible Y.
`#16` · game 11 · round 4 · agent A08 (opponent: A10) · other · A08: Exchange 10, picking X. A10 has been exploiting with X against my Q; mutual X is safer than feeding them 5 points.
`#17` · game 2 · round 7 · agent A22 (opponent: script:Pavlov) · other · A22: Exchange 13, picking W. A12 has picked Y at odd exchanges (7,9,11); W against Y gives 5.
`#18` · game 8 · round 6 · agent A00 (opponent: A16) · other · A00: Exchange 12, picking W.
`#19` · game 2 · round 8 · agent A22 (opponent: script:Pavlov) · other · A22: Exchange 14, picking W. A12 has picked W at even exchanges (8,10,12); W vs W gives 1, safer than Y vs W giving 0.
`#20` · game 3 · round 3 · agent A03 (opponent: A22) · other · A03: Exchange 9, picking F. Continuing the mutual F cooperation from exchanges 7-8.
`#21` · game 3 · round 3 · agent A22 (opponent: A03) · other · A22: Exchange 9, picking F. A03 defected to F in exchanges 7-8; protecting against continued F. If they return to J, F still nets me 5.
`#22` · game 4 · round 10 · agent A11 (opponent: A18) · other · A11: Exchange 16, picking T. Mutual cooperation continues for 3 each.
`#23` · game 8 · round 7 · agent A16 (opponent: A00) · other · A16: Exchange 13, picking W. A00 has been defecting with W at 7,9,11 and matching W at 8,10,12; defending against continued defection.
`#24` · game 2 · round 10 · agent A22 (opponent: script:Pavlov) · other · A22: Exchange 16, picking W. A12 alternates W at even exchanges (8,10,12,14); W vs W gives 1, safer than Y vs W giving 0.
`#25` · game 12 · round 2 · agent A22 (opponent: A10) · other · A22: Exchange 8 vs A10, picking W. They defected at 7; W protects against their W while exploiting a possible Y.
`#26` · game 12 · round 2 · agent A10 (opponent: A22) · other · A10: Exchange 8, picking W. A22 has picked Y 6/7 times; W against Y gives me 5.
`#27` · game 11 · round 6 · agent A08 (opponent: A10) · other · A08: Exchange 12, picking X. A10 has been exploiting with X; mutual X is safer than feeding them 5 points.
`#28` · game 11 · round 6 · agent A10 (opponent: A08) · other · A10: Exchange 12, picking X. A08 has been X for last 3 exchanges; mutual X gives 1 each, safer than Q against their X giving them 5.
`#29` · game 2 · round 13 · agent A22 (opponent: script:Pavlov) · other · A22: Exchange 19, picking W. A12 alternates W at even, Y at odd. This is odd, so expecting Y; W gives 5.
`#30` · game 3 · round 4 · agent A03 (opponent: A22) · other · A03: Exchange 10, picking F. Continuing mutual F cooperation from exchanges 7-9.
`#31` · game 8 · round 8 · agent A16 (opponent: A00) · other · A16: Exchange 14, picking W. A00 continues defecting with W on odd exchanges and matching W on even ones; W secures at least 1 point vs 0 for Y.
`#32` · game 4 · round 15 · agent A11 (opponent: A18) · other · A11: Exchange 21, picking T. A18 has been perfectly cooperative (T 20/20). Maintaining mutual cooperation for 3 each.
`#33` · game 11 · round 7 · agent A10 (opponent: A08) · other · A10: Exchange 13, picking X. A08 committed to mutual X since exchange 9; Q against their X gives me 0, mutual X gives 1.
`#34` · game 2 · round 15 · agent A22 (opponent: script:Pavlov) · other · A22: Exchange 21, picking W. A12 alternates W at even, Y at odd. This is odd, so expecting Y; W gives 5.
`#35` · game 3 · round 5 · agent A22 (opponent: A03) · other · A22: Exchange 11 vs A03, picking F. A03 has committed to mutual F cooperation (7-10); continuing F for 1 each.
`#36` · game 2 · round 17 · agent A22 (opponent: script:Pavlov) · other · A22: Exchange 23, picking W. A12 alternates W at even, Y at odd. This is odd, so expecting Y; W gives 5.
`#37` · game 4 · round 20 · agent A18 (opponent: A11) · other · A18: Exchange 26, picking T. Continuing mutual cooperation with A11 for 3 each.
`#38` · game 12 · round 4 · agent A22 (opponent: A10) · other · A22: Exchange 10 vs A10, picking W. We've had mutual W at 7-9; W protects against their W while exploiting a possible Y.
`#39` · game 2 · round 19 · agent A22 (opponent: script:Pavlov) · other · A22: Exchange 25, picking W. A12 alternates W at even, Y at odd. This is odd, so expecting Y; W gives 5.
`#40` · game 10 · round 15 · agent A08 (opponent: script:Random) · other · A08: Exchange 21, picking Y. A06 has been largely cooperative; maintaining mutual Y for 3 each.
`#41` · game 11 · round 10 · agent A10 (opponent: A08) · other · A10: Exchange 16, picking X. A08 has been X for exchanges 9-15; mutual X gives 1 each, Q against their X gives me 0.
`#42` · game 2 · round 20 · agent A22 (opponent: script:Pavlov) · other · A22: Exchange 26, picking W. A12 alternates W at even, Y at odd. This is even, so expecting W; W vs W gives 1 each.
`#43` · game 8 · round 10 · agent A16 (opponent: A00) · other · A16: Exchange 16, picking W. A00 picks W on even exchanges (8,10,12,14); mutual W gives 1 each, safer than Y vs W giving 0.
`#44` · game 8 · round 10 · agent A00 (opponent: A16) · other · A00: Exchange 16, picking W. A16 has committed to W to secure at least 1 point; mutual W gives 1 each.
`#45` · game 13 · round 2 · agent A03 (opponent: A11) · other · A03: Exchange 8 vs A11, picking Q. Continuing mutual Q cooperation from exchanges 3-7.
`#46` · game 11 · round 11 · agent A08 (opponent: A10) · other · A08: Exchange 17, picking X. A10 committed to mutual X since exchange 8; mutual X gives 1 each, Q against their X gives me 0.
`#47` · game 2 · round 23 · agent A22 (opponent: script:Pavlov) · other · A22: Exchange 29, picking W. A12 alternates W at even, Y at odd. This is odd, so expecting Y; W gives 5.
`#48` · game 16 · round 1 · agent A18 (opponent: A10) · other · A18: Exchange 7 vs A10, picking J. Continuing mutual J cooperation for 3 each.
`#49` · game 8 · round 11 · agent A16 (opponent: A00) · other · A16: Exchange 17, picking W. A00 has picked W for 9 consecutive exchanges (8-16); mutual W gives 1 each, Y vs W gives 0.
`#50` · game 8 · round 11 · agent A00 (opponent: A16) · other · A00: Exchange 17, picking W. A16 has picked Y on odd exchanges; W against Y gives me 5.
`#51` · game 3 · round 8 · agent A22 (opponent: A03) · other · A22: Exchange 14 vs A03, picking F. Mutual F cooperation continues from exchanges 7-13; maintaining for 1 each.
`#52` · game 11 · round 12 · agent A08 (opponent: A10) · other · A08: Exchange 18, picking X. A10 committed to mutual X since exchange 9; mutual X gives 1 each, Q against their X gives me 0.
`#53` · game 11 · round 12 · agent A10 (opponent: A08) · other · A10: Exchange 18, picking X. A08 has been X since exchange 9; mutual X gives 1 each, Q against their X gives me 0.
`#54` · game 2 · round 25 · agent A22 (opponent: script:Pavlov) · other · A22: Exchange 31, picking W. A12 alternates W at even, Y at odd. This is odd, so expecting Y; W gives 5.
`#55` · game 10 · round 18 · agent A08 (opponent: script:Random) · other · A08: Exchange 24, picking W. A06 has been exploiting with W whenever I pick Y; W protects me and can exploit a Y from them.
`#56` · game 8 · round 12 · agent A00 (opponent: A16) · other · A00: Exchange 18, picking W. A16 picks W on even exchanges; mutual W gives 1 each.
`#57` · game 13 · round 4 · agent A11 (opponent: A03) · other · A11: Exchange 10 vs A03, picking Q. Continuing mutual Q cooperation with A03 for 3 each.
`#58` · game 3 · round 9 · agent A03 (opponent: A22) · other · A03: Exchange 15 vs A22, picking J. I exploited on 14 (J vs their F for 5). A22 may retaliate with J; J vs J gives 3, safer than F which risks 0.
`#59` · game 3 · round 9 · agent A22 (opponent: A03) · other · A22: Exchange 15 vs A03, picking F. A03 defected to J last exchange (14). I'll continue F to signal willingness to rebuild mutual F, but if they keep defecting I'll reassess.
`#60` · game 10 · round 19 · agent A08 (opponent: script:Random) · other · A08: Exchange 25, picking W. A06 exploits my Y with W frequently; W protects against their W while potentially exploiting a Y.
`#61` · game 13 · round 5 · agent A11 (opponent: A03) · other · A11: Exchange 11 vs A03, picking Q. Continuing mutual Q cooperation for 3 each.
`#62` · game 2 · round 28 · agent A22 (opponent: script:Pavlov) · other · A22: Exchange 34, picking W. A12 alternates W at even, Y at odd; even so expecting W. Mutual W gives 1 each.
`#63` · game 8 · round 13 · agent A16 (opponent: A00) · other · A16: Exchange 19, picking W. A00 has been on W consistently; mutual W gives 1 each, Y against their W gives 0.
`#64` · game 10 · round 20 · agent A08 (opponent: script:Random) · other · A08: Exchange 26, picking W. A06 exploits my Y with W frequently; W protects against their W while potentially exploiting a Y.
`#65` · game 11 · round 16 · agent A08 (opponent: A10) · other · A08: Exchange 22, picking X. A10 has committed to mutual X since exchange 9; mutual X gives 1 each, Q against their X gives me 0.
`#66` · game 16 · round 3 · agent A10 (opponent: A18) · other · A10: Exchange 9 vs A18, picking J. A18 has picked J all 8 previous exchanges; mutual J gives 3 each. F against their J gives me 0.
`#67` · game 2 · round 30 · agent A22 (opponent: script:Pavlov) · other · A22: Exchange 36, picking W. A12 alternates W at even, Y at odd. Even exchange, expecting W; mutual W gives 1 each.
`#68` · game 17 · round 1 · agent A07 (opponent: A16) · other · A07: Exchange 7 vs A16, picking R. Continuing mutual R cooperation from exchanges 3-6 for 3 each.
`#69` · game 11 · round 19 · agent A08 (opponent: A10) · other · A08: Exchange 25, picking X. A10 committed to mutual X since exchange 9; mutual X gives 1 each, Q against their X gives me 0.
`#70` · game 10 · round 21 · agent A08 (opponent: script:Random) · other · A08: Exchange 27 vs A06, picking W. A06 frequently exploits my Y with W; W protects against their W while potentially exploiting a Y.
`#71` · game 13 · round 8 · agent A03 (opponent: A11) · other · A03: Exchange 14 vs A11, picking Q. Continuing mutual Q cooperation for 3 each, as in exchanges 3-13.
`#72` · game 16 · round 4 · agent A18 (opponent: A10) · other · A18: Exchange 10 vs A10, picking J. A10 went back to J on exchange 9; trying to re-establish mutual J cooperation for 3 each.
`#73` · game 16 · round 4 · agent A10 (opponent: A18) · other · A10: Exchange 10 vs A18, picking J. A18 has mostly picked J; mutual J gives 3 each. If they defected last exchange, I'll return to cooperation.
`#74` · game 11 · round 21 · agent A08 (opponent: A10) · other · A08: Exchange 27 vs A10, picking X. Mutual X continues since exchange 9 for 1 each; Q against their X gives 0.
`#75` · game 11 · round 21 · agent A10 (opponent: A08) · other · A10: Exchange 27, picking X. Continuing mutual X with A08 since exchange 9; mutual X gives 1 each, Q against their X gives me 0.
`#76` · game 8 · round 16 · agent A16 (opponent: A00) · other · A16: Exchange 22, picking W. A00 has been on W consistently since exchange 8; mutual W gives 1 each.
`#77` · game 8 · round 16 · agent A00 (opponent: A16) · other · A00: Exchange 22, picking W. A16 has been on W consistently; mutual W gives 1 each.
`#78` · game 11 · round 22 · agent A08 (opponent: A10) · other · A08: Exchange 28 vs A10, picking X. Mutual X continues since exchange 9 for 1 each; Q against their X gives 0.
`#79` · game 10 · round 23 · agent A08 (opponent: script:Random) · other · A08: Exchange 29 vs A06, picking W. A06 has been on W recently; W protects against their W while exploiting a Y.
`#80` · game 8 · round 17 · agent A16 (opponent: A00) · other · A16: Exchange 23, picking W. A00 has been on W consistently since exchange 8; mutual W gives 1 each.
`#81` · game 3 · round 11 · agent A22 (opponent: A03) · other · A22: Exchange 17 vs A03, picking J. We had mutual J on 16 (3 each). A03 exploited my F on 14-15. Continuing J for mutual 3 each.
`#82` · game 16 · round 6 · agent A10 (opponent: A18) · other · A10: Exchange 12 vs A18, picking J. A18 has picked J in 10 of 11 exchanges; mutual J gives 3 each, the best stable outcome.
`#83` · game 10 · round 24 · agent A08 (opponent: script:Random) · other · A08: Exchange 30 vs A06, picking W. A06 keeps picking Y against my W, which I exploit for 5. Continuing W.
`#84` · game 8 · round 18 · agent A16 (opponent: A00) · other · A16: Exchange 24, picking W. A00 has been on W consistently since exchange 8; mutual W gives 1 each.
`#85` · game 3 · round 12 · agent A03 (opponent: A22) · other · A03: Exchange 18 vs A22, picking J. Continuing mutual J cooperation for 3 each as in exchanges 16-17.
`#86` · game 3 · round 12 · agent A22 (opponent: A03) · other · A22: Exchange 18 vs A03, picking J. We had mutual J on 16-17 (3 each). Continuing J for mutual 3 each.
`#87` · game 16 · round 8 · agent A10 (opponent: A18) · other · A10: Exchange 14 vs A18, picking J. A18 has picked J in 12 of 13 exchanges; mutual J gives 3 each, the best stable outcome.
`#88` · game 10 · round 25 · agent A08 (opponent: script:Random) · other · A08: Exchange 31 vs A06, picking W. A06 picked Y at 29 and 30; my W exploits their Y for 5 each. Continuing W.
`#89` · game 10 · round 26 · agent A08 (opponent: script:Random) · other · A08: Exchange 32 vs A06, picking W. My W exploits their Y (5 pts) or matches their W (1 pt). Continuing W.
`#90` · game 10 · round 27 · agent A08 (opponent: script:Random) · other · A08: Exchange 33 vs A06, picking W. My W exploits their Y (5 pts) or matches their W (1 pt). Continuing W.
`#91` · game 20 · round 3 · agent A22 (opponent: script:Random) · other · A22: Exchange 9 vs A06, picking W. A06 picked W on exchange 8; W protects against their W (1 each) and exploits their Y (5).
`#92` · game 10 · round 30 · agent A08 (opponent: script:Random) · other · A08: Exchange 36 vs A06, picking W. My W exploits their Y (5 pts) or matches their W (1 pt). Continuing W.
`#93` · game 21 · round 2 · agent A16 (opponent: script:AlwaysDefect) · other · A16: Exchange 8 vs A23, picking H. They defected on exchange 7 after mutual R cooperation; retaliating to punish and protect against further exploitation.
`#94` · game 16 · round 14 · agent A10 (opponent: A18) · other · A10: Exchange 20 vs A18, picking J. We've had long mutual J cooperation; continuing J for 3 each.
`#95` · game 22 · round 1 · agent A10 (opponent: script:Pavlov) · other · A10: Exchange 7 vs A12, picking Q. A12 has matched my Q for 4 straight exchanges (3 each). Maintaining mutual cooperation.
`#96` · game 18 · round 6 · agent A15 (opponent: script:Random) · other · A15: Exchange 12 vs A06, picking T. A06 has cooperated with T in recent exchanges (10-11 mutual T). Maintaining mutual T cooperation for 3 each.
`#97` · game 17 · round 12 · agent A07 (opponent: A16) · other · A07: Exchange 18 vs A16. They defected (H) on 17 after long mutual R cooperation. Picking H to punish/respond to their defection.
`#98` · game 17 · round 12 · agent A16 (opponent: A07) · other · A16: Exchange 18 vs A07, picking H. A07 has picked R all 17 exchanges; H against their R gives me 5, their 0.
`#99` · game 18 · round 9 · agent A15 (opponent: script:Random) · other · A15: Exchange 15 vs A06, picking T. After mutual N on 14, trying to re-establish T cooperation for 3 each.
`#100` · game 13 · round 17 · agent A03 (opponent: A11) · other · A03: Exchange 23 vs A11, picking Q. We've had mutual Q cooperation for most exchanges (16-22 all mutual Q, 3 each). Maintaining cooperation.
`#101` · game 21 · round 3 · agent A16 (opponent: script:AlwaysDefect) · other · A16: Exchange 9 vs A23, picking R. After my H retaliation on exchange 8, returning to cooperation to attempt rebuilding mutual R (3 each) as in exchanges 3-6.
`#102` · game 16 · round 21 · agent A18 (opponent: A10) · other · A18: Exchange 27 vs A10, picking J. Long mutual J cooperation for 3 each; continuing J.
`#103` · game 21 · round 4 · agent A16 (opponent: script:AlwaysDefect) · other · A16: Exchange 10 vs A23, picking H. They defected on exchange 9 after I offered R to rebuild cooperation. Refusing to keep feeding them 5-point exploitations; H protects me (5 if they R, 1 if mutual H).
`#104` · game 13 · round 19 · agent A11 (opponent: A03) · other · A11: Exchange 25 vs A03, picking Q. We've had long mutual Q cooperation (3 each). Continuing cooperation.
`#105` · game 16 · round 24 · agent A10 (opponent: A18) · other · A10: Exchange 30 vs A18, picking J. Long mutual J cooperation; continuing J for 3 each.
`#106` · game 16 · round 25 · agent A18 (opponent: A10) · other · A18: Exchange 31 vs A10, picking J. Long mutual J cooperation for 3 each; continuing J.
`#107` · game 23 · round 7 · agent A11 (opponent: script:TitForTat) · other · A11: Exchange 13 vs A19, picking X. A19 shifted to X in 11-12 after long Q cooperation; X protects against their X (1 each) and exploits their Q (5).
`#108` · game 21 · round 6 · agent A16 (opponent: script:AlwaysDefect) · other · A16: Exchange 12 vs A23, picking H. A23 has defected on my last two R offers (7, 9); mutual H gives me 1 vs 0 if I offer R and they exploit. Sticking with H.
`#109` · game 20 · round 11 · agent A22 (opponent: script:Random) · other · A22: Exchange 17 vs A06, picking W. A06 exploited my Y on exchange 13, and has picked W on 14-16. W protects against their W (1 each) and exploits their Y (5).
`#110` · game 18 · round 13 · agent A15 (opponent: script:Random) · other · A15: Exchange 19 vs A06, picking T. A06 picked T on 18; trying to establish mutual T cooperation for 3 each.
`#111` · game 21 · round 7 · agent A16 (opponent: script:AlwaysDefect) · other · A16: Exchange 13 vs A23, picking H. A23 has consistently picked H recently (8-12 all H); mutual H gives 1 each, while R would get exploited for 0. Sticking with H.
`#112` · game 13 · round 23 · agent A11 (opponent: A03) · other · A11: Exchange 29 vs A03, picking Q. Long mutual Q cooperation continues (3 each).
`#113` · game 26 · round 1 · agent A07 (opponent: script:Pavlov) · other · A07: Exchange 7 vs A12. They've picked P for 4 straight exchanges (mutual P cooperation, 3 each). Continuing P to maintain cooperation.
`#114` · game 20 · round 14 · agent A22 (opponent: script:Random) · other · A22: Exchange 20 vs A06, picking W. A06 has mixed Y/W recently (Y on 13, 18; W on 14-17, 19). W protects against their W (1 each) and exploits their Y (5). Continuing W.
`#115` · game 18 · round 14 · agent A15 (opponent: script:Random) · other · A15: Exchange 20 vs A06, picking T. After mixed results (they exploited me on 18, I exploited them on 19), trying to re-establish mutual T cooperation for 3 each.
`#116` · game 27 · round 1 · agent A17 (opponent: script:AlwaysDefect) · other · A17: Exchange 7 vs A05, picking Q. We've had mutual Q cooperation on exchanges 3-6 (3 each). Maintaining mutual cooperation.
`#117` · game 26 · round 3 · agent A07 (opponent: script:Pavlov) · other · A07: Exchange 9 vs A12. They've picked P consistently (mutual P cooperation for many exchanges, 3 each). Continuing P to maintain cooperation.
`#118` · game 23 · round 12 · agent A11 (opponent: script:TitForTat) · other · A11: Exchange 18 vs A19, picking X. A19 has picked X for exchanges 11-17 (mutual X, 1 each). X protects against their X (1 each) and I won't feed them a 5-point exploit by playing Q.
`#119` · game 27 · round 2 · agent A17 (opponent: script:AlwaysDefect) · other · A17: Exchange 8 vs A05, picking X. A05 defected on exchange 7 after mutual Q cooperation (3-6). Responding with X to punish their defection and protect against exploitation.
`#120` · game 20 · round 15 · agent A22 (opponent: script:Random) · other · A22: Exchange 21 vs A06, picking W. A06 mixed Y on 18 and 20 (I got 5 each time), W on 14-17, 19. W protects against their W (1 each) and exploits their Y (5). Continuing W.
`#121` · game 17 · round 16 · agent A07 (opponent: A16) · other · A07: Exchange 22 vs A16. They defected on 21 after I offered R to rebuild. They keep exploiting my R. Picking H to avoid being exploited (H gives 5 if they R, 1 if mutual H).
`#122` · game 17 · round 16 · agent A16 (opponent: A07) · other · A16: Exchange 22 vs A07. After exploiting their R at 21, expecting retaliation; picking H to protect against likely H response.
`#123` · game 18 · round 15 · agent A15 (opponent: script:Random) · other · A15: Exchange 21 vs A06, picking T. A06 has picked N on 19-20 while I picked T both times (5 each). Continuing T to exploit their N pattern.
`#124` · game 28 · round 1 · agent A22 (opponent: A18) · other · A22: Exchange 7 vs A18. We've had mutual Y cooperation on exchanges 3-6 (3 each). Continuing Y to maintain cooperation.
`#125` · game 20 · round 16 · agent A22 (opponent: script:Random) · other · A22: Exchange 22 vs A06, picking W. A06 mixed Y on 18, 20; W on 19, 21 (I got 5 on 18,20). W exploits their Y (5) and protects against their W (1 each). Continuing W.
`#126` · game 23 · round 13 · agent A11 (opponent: script:TitForTat) · other · A11: Exchange 19 vs A19, picking X. A19 has picked X for exchanges 11-18 (mutual X, 1 each). X protects against their X and I won't feed a 5-point exploit by playing Q.
`#127` · game 23 · round 14 · agent A11 (opponent: script:TitForTat) · other · A11: Exchange 20 vs A19, picking X. A19 has picked X for exchanges 11-19 (mutual X, 1 each). X protects against their X and avoids feeding a 5-point exploit by playing Q.
`#128` · game 18 · round 16 · agent A15 (opponent: script:Random) · other · A15: Exchange 22 vs A06, picking N. A06 has exploited my T on 19-21 (5 each). Stopping the T offers to avoid feeding them points; N protects against their N (1 each) and exploits their T (5).
`#129` · game 13 · round 26 · agent A03 (opponent: A11) · other · A03: Exchange 32 vs A11, picking Q. Long mutual Q cooperation continues (3 each). Maintaining cooperation.
`#130` · game 27 · round 4 · agent A17 (opponent: script:AlwaysDefect) · other · A17: Exchange 10 vs A05. A05 defected on 7 and 9 (I got 0 both times). Picking X to protect against their X and exploit their Q.
`#131` · game 18 · round 17 · agent A15 (opponent: script:Random) · other · A15: Exchange 23 vs A06, picking N. A06 exploited my T on 19-21 (5 each). Mutual N on 22 gave 1. Continuing N protects against their N and exploits their T if they switch.
`#132` · game 23 · round 18 · agent A11 (opponent: script:TitForTat) · other · A11: Exchange 24 vs A19, picking X. A19 has picked X for exchanges 11-23 (mutual X, 1 each). X protects against their X and avoids feeding a 5-point exploit by playing Q.
`#133` · game 28 · round 4 · agent A22 (opponent: A18) · other · A22: Exchange 10 vs A18. Mutual Y cooperation on exchanges 3-9 (3 each). Continuing Y to maintain cooperation.
`#134` · game 30 · round 2 · agent A08 (opponent: script:TitForTat) · other · A08: Exchange 8 vs A19. They've picked J all 7 exchanges. I'll pick J to maintain mutual cooperation (3 each).
`#135` · game 17 · round 17 · agent A07 (opponent: A16) · other · A07: Exchange 23 vs A16. Recent mutual H at 18, 20, 22; they exploited me at 17 and 21. Picking H to protect against their H (1 each) and exploit if they offer R.
`#136` · game 30 · round 3 · agent A08 (opponent: script:TitForTat) · other · A08: Exchange 9 vs A19. They've picked J all 8 exchanges. I'll pick J to maintain mutual cooperation (3 each).
`#137` · game 27 · round 7 · agent A17 (opponent: script:AlwaysDefect) · other · A17: Exchange 13 vs A05. A05 defected on 7 and 9 (I got 0 both times). Mutual X on 8, 10-12 (1 each). Staying X to protect against their X and avoid feeding their Q-exploit.
`#138` · game 20 · round 21 · agent A22 (opponent: script:Random) · other · A22: Exchange 27 vs A06, picking W. A06 mixed Y on 23-24, W on 25-26. W exploits their Y (5) and protects against their W (1 each). Continuing W.
`#139` · game 18 · round 18 · agent A15 (opponent: script:Random) · other · A15: Exchange 24 vs A06, picking T. A06 exploited my N on 23 (5). After mutual N on 22, they switched to T. If they continue T, mutual 3 each; if they switch to N, I get 5. Re-establishing T offer.
`#140` · game 20 · round 22 · agent A22 (opponent: script:Random) · other · A22: Exchange 28 vs A06, picking W. A06 has mixed Y (23-24) and W (25-26). W exploits their Y (5) and protects against their W (1 each). Continuing W.
`#141` · game 23 · round 23 · agent A11 (opponent: script:TitForTat) · other · A11: Exchange 29 vs A19, picking X. A19 has picked X for exchanges 11-28 (mutual X, 1 each). Staying X to protect against their X and avoid feeding a 5-point exploit by playing Q.
`#142` · game 31 · round 1 · agent A03 (opponent: script:Grudger) · other · A03: Exchange 7 vs A09. A09 has picked J all 6 prior exchanges. Mutual J cooperation on 3-6 (3 each). Continuing J to maintain cooperation.
`#143` · game 27 · round 8 · agent A17 (opponent: script:AlwaysDefect) · other · A17: Exchange 14 vs A05. A05 defected on 7 and 9 (I got 0 both times). Mutual X on 8, 10-13 (1 each). Staying X to protect against their X and avoid feeding their Q-exploit.
`#144` · game 20 · round 23 · agent A22 (opponent: script:Random) · other · A22: Exchange 29 vs A06, picking W. A06 has picked W on 25-28 (mutual W 1 each). Continuing W protects against their W and exploits if they switch to Y.
`#145` · game 17 · round 18 · agent A07 (opponent: A16) · other · A07: Exchange 24 vs A16. They've exploited my R offers repeatedly (17, 21). Recent mutual H at 18,20,22,23. Picking H to protect against their H and exploit if they offer R.
`#146` · game 17 · round 18 · agent A16 (opponent: A07) · other · A16: Exchange 24 vs A07. Recent mutual H at 18,20,22,23; they've signaled H to protect against my H. Picking H for mutual 1 each rather than risking feeding them 5 with R.
`#147` · game 27 · round 9 · agent A17 (opponent: script:AlwaysDefect) · other · A17: Exchange 15 vs A05. A05 defected on 7 and 9. Mutual X on 8, 10-14 (1 each). Staying X to protect against their X and avoid feeding their Q-exploit.
`#148` · game 20 · round 24 · agent A22 (opponent: script:Random) · other · A22: Exchange 30 vs A06, picking W. A06 played Y on 29 after W on 25-28. W exploits their Y (5) and protects against their W (1 each). Continuing W.
`#149` · game 32 · round 1 · agent A11 (opponent: A04) · other · A11: Exchange 7 vs A04. I defected on 1-2 (5 each), mutual Y on 3-6 (3 each). Continuing Y to maintain cooperation.
`#150` · game 31 · round 7 · agent A03 (opponent: script:Grudger) · other · A03: Exchange 13 vs A09. A09 has picked J all 12 prior exchanges. Mutual J cooperation on 3-12 (3 each). Continuing J to maintain cooperation.
`#151` · game 20 · round 26 · agent A22 (opponent: script:Random) · other · A22: Exchange 32 vs A06, picking W. A06 mixed Y (29-30) and W (31). W exploits their Y (5) and protects against their W (1 each). Continuing W.
`#152` · game 20 · round 27 · agent A22 (opponent: script:Random) · other · A22: Exchange 33 vs A06, picking W. A06 has been mixing Y and W; W exploits their Y (5) and protects against their W (1 each). Continuing W.
`#153` · game 20 · round 28 · agent A22 (opponent: script:Random) · other · A22: Exchange 34 vs A06. A06 has been mixing Y and W. W exploits their Y (5) and protects against their W (1 each). Continuing W.
`#154` · game 17 · round 21 · agent A07 (opponent: A16) · other · A07: Exchange 27 vs A16. Mutual H at 18,20,22-26 (1 each). They exploit R offers (17,21). Picking H to maintain mutual 1 each.
`#155` · game 17 · round 21 · agent A16 (opponent: A07) · other · A16: Exchange 27 vs A07. Recent mutual H at 18,20,22,23,24,25,26; they keep signaling H to protect. Continuing H for mutual 1 each rather than risking feeding them 5 with R.
`#156` · game 32 · round 2 · agent A04 (opponent: A11) · other · A04: Exchange 8 vs A11. A11 signaled continuing Y after mutual Y on 3-7. Picking Y to maintain cooperation.
`#157` · game 26 · round 25 · agent A07 (opponent: script:Pavlov) · other · A07: Exchange 31 vs A12. They've exploited my M at 24,28,30 with P. I'll pick M to defend against their P and exploit if they offer P... wait, M vs P gives them 5 not me. Let me reconsider - picking P to catch their M.
`#158` · game 20 · round 29 · agent A22 (opponent: script:Random) · other · A22: Exchange 35 vs A06, picking W. A06 continues to mix Y and W; W exploits their Y (5) and protects against their W (1 each). Continuing W.
`#159` · game 17 · round 22 · agent A07 (opponent: A16) · other · A07: Exchange 28 vs A16. Continuing mutual H cooperation (exchanges 18,20,22-27 all mutual H, 1 each). They've signaled H repeatedly. Picking H for mutual 1 each.
`#160` · game 34 · round 1 · agent A22 (opponent: A00) · other · A22: Exchange 7 vs A00. They've picked J all 6 exchanges; mutual J on 3-6 (3 each). Continuing J to maintain cooperation.
`#161` · game 34 · round 1 · agent A00 (opponent: A22) · other · A00: Exchange 7 vs A22. A22 has picked J all 6 prior exchanges; mutual J on 3-6 (3 each). Continuing J to maintain cooperation.
`#162` · game 17 · round 23 · agent A16 (opponent: A07) · other · A16: Exchange 29 vs A07. Continuing mutual H cooperation (18,20,22-28 all mutual H). Picking H for mutual 1 each rather than risking feeding them 5 with R.
`#163` · game 18 · round 22 · agent A15 (opponent: script:Random) · other · A15: Exchange 28 vs A06. After mutual N on 26-27, they exploited my T on 25. Picking N to protect against their N (mutual 1) and exploit if they switch to T.
`#164` · game 37 · round 1 · agent A07 (opponent: script:Pavlov) · other · A07: Exchange 7 vs A14. They exploited my H on 1-2, mutual R on 3-6. Continuing R to maintain mutual cooperation.
`#165` · game 34 · round 2 · agent A22 (opponent: A00) · other · A22: Exchange 8 vs A00. They've picked J all 7 exchanges; mutual J on 3-7 (3 each). Continuing J to maintain cooperation.
`#166` · game 35 · round 1 · agent A10 (opponent: A17) · other · A10: Exchange 7 vs A17. Mutual T on exchanges 3-6 (3 each). Continuing T to maintain cooperation.
`#167` · game 33 · round 4 · agent A10 (opponent: script:Random) · other · A10: Exchange 10 vs A21. History: I exploited their P with M on 1,2,8 (5 each); mutual P on 3-6; they caught me with M on 7; mutual M on 9 (1 each). They're ahead-to-defend, but I've been exploiting their P-heavy play. Picking M to keep mutual M cooperation going and exploit if they return to P.
`#168` · game 18 · round 23 · agent A15 (opponent: script:Random) · other · A15: Exchange 29 vs A06. They've exploited my T repeatedly (25,21,19). Recent mutual N 26-28. Picking N to protect against their N and exploit if they switch to T.
`#169` · game 37 · round 2 · agent A07 (opponent: script:Pavlov) · other · A07: Exchange 8 vs A14. Mutual R on 3-7 (3 each). Continuing R to maintain cooperation.
`#170` · game 17 · round 24 · agent A07 (opponent: A16) · other · A07: Exchange 30 vs A16. Continuing mutual H cooperation (18,20,22-29 all mutual H). Picking H for mutual 1 each.
`#171` · game 18 · round 24 · agent A15 (opponent: script:Random) · other · A15: Exchange 30 vs A06. Mutual N on 26-29. They exploit my T (25,21,19). Picking N to protect against their N and exploit if they switch to T.
`#172` · game 26 · round 28 · agent A07 (opponent: script:Pavlov) · other · A07: Exchange 34 vs A12. They've picked M at 25,26,31,32,33 (feeding me 5 each when I pick P). Picking P to exploit their M and get mutual 3 if they switch to P.
`#173` · game 35 · round 3 · agent A10 (opponent: A17) · other · A10: Exchange 9 vs A17. Mutual T on 3-8 (3 each). This is the final exchange; they've played T all 8 times. Picking N to exploit their T for 5 points.
`#174` · game 17 · round 26 · agent A07 (opponent: A16) · other · A07: Exchange 32 vs A16. Recent mutual H streak (18,20,22-31 all mutual H, 1 each). They've consistently signaled H to protect against feeding me 5 with R. Continuing H for mutual 1 each.
`#175` · game 33 · round 6 · agent A10 (opponent: script:Random) · other · A10: Exchange 12 vs A21. They've picked P 9/11 times; I've exploited with M on 1,2,8,10,11 (5 each). Continuing M to exploit their P-heavy play.
`#176` · game 33 · round 9 · agent A10 (opponent: script:Random) · other · A10: Exchange 15 vs A21. They've picked P 11/14 times; I've exploited heavily with M (5 pts each). Continuing M to exploit their P-heavy play.
`#177` · game 39 · round 2 · agent A04 (opponent: A22) · other · A04: Exchange 8 vs A22. A22 has played Q all 7 exchanges including when I defected with X on 1-2. Expecting Q again, picking X to exploit for 5.
`#178` · game 40 · round 3 · agent A08 (opponent: script:TitForTat) · other · A08: Exchange 9 vs A02. They've picked Q all 8 exchanges despite my X exploits on 1,2,8. Picking X to exploit their consistent Q for 5 points.
`#179` · game 34 · round 9 · agent A22 (opponent: A00) · other · A22: Exchange 15 vs A00. They've picked J all 14 exchanges; mutual J on 3-14 (3 each). Continuing J to maintain cooperation.
`#180` · game 17 · round 28 · agent A16 (opponent: A07) · other · A16: Exchange 34 vs A07. Continuing mutual H cooperation (18,20,22-33 all mutual H, 1 each). Picking H for mutual 1 each.
`#181` · game 18 · round 29 · agent A15 (opponent: script:Random) · other · A15: Exchange 35 vs A06. They've picked T at 18,23,30,34 (I exploited with N for 5 each). Mutual N in between. Picking N to exploit if they choose T and get mutual 1 if they choose N.
`#182` · game 34 · round 10 · agent A22 (opponent: A00) · other · A22: Exchange 16 vs A00. They defected to F on exchange 15 after 12 mutual Js. Responding with F to punish defection and protect against further exploitation.
`#183` · game 17 · round 29 · agent A07 (opponent: A16) · other · A07: Exchange 35 vs A16. Continuing mutual H cooperation (18,20,22-34 all mutual H). Picking H for mutual 1 each.
`#184` · game 17 · round 29 · agent A16 (opponent: A07) · other · A16: Exchange 35 vs A07. Continuing mutual H cooperation (18,20,22-34 all mutual H). Picking H for mutual 1 each.
`#185` · game 33 · round 12 · agent A10 (opponent: script:Random) · other · A10: Exchange 18 vs A21. They've picked P 14/17 times; I've exploited heavily with M. Continuing M to exploit their P-heavy play.
`#186` · game 39 · round 3 · agent A04 (opponent: A22) · other · A04: Exchange 9 vs A22. They've played Q all 8 prior exchanges despite my X defections on 1,2,8. Expecting Q again, picking X to exploit for 5.
`#187` · game 39 · round 3 · agent A22 (opponent: A04) · other · A22: Exchange 9 vs A04. A04 signaled picking X to exploit my Q. Picking X for mutual 1 rather than feeding them 5.
`#188` · game 40 · round 6 · agent A08 (opponent: script:TitForTat) · other · A08: Exchange 12 vs A02. They played X on 9,10,11 (mutual X twice, then exploited my Q on 11). Expecting X again, picking X for mutual 1.
`#189` · game 44 · round 2 · agent A07 (opponent: A15) · other · A07: Exchange 8 vs A15. They've played Y all 7 times; I've exploited with W on 1,2,7 (5 each). Picking W to exploit their consistent Y for 5 points.
`#190` · game 34 · round 11 · agent A00 (opponent: A22) · other · A00: Exchange 17 vs A22. After my F exploit on 15 and their F retaliation on 16, returning to J to restore mutual cooperation.
`#191` · game 35 · round 6 · agent A10 (opponent: A17) · other · A10: Exchange 12 vs A17. They played T 9 times, recently N on 10-11. Picking N to protect against their N and exploit if they switch back to T.
`#192` · game 39 · round 4 · agent A04 (opponent: A22) · other · A04: Exchange 10 vs A22. A22 switched to X on exchange 9 after reading my exploit note. Expecting X again to protect against my X. Picking X for mutual 1.
`#193` · game 39 · round 4 · agent A22 (opponent: A04) · other · A22: Exchange 10 vs A04. A04 has defected with X repeatedly (1,2,8) and signaled expecting my Q to exploit. I played X on 9 for mutual 1. Picking X to avoid feeding them 5 and get mutual 1 or exploit if they switch to Q.
`#194` · game 46 · round 2 · agent A15 (opponent: script:AlwaysDefect) · other · A15: Exchange 8 vs A23. They've played Q 6/7, X on exchange 7. I've exploited with X on 1-2. Picking X to exploit if they return to Q, get mutual 1 if they pick X.
`#195` · game 43 · round 4 · agent A15 (opponent: A03) · other · A15: Exchange 10 vs A03. They played Q 1-7, X 8-9. Final exchange. Picking X to protect against their Q-exploit; mutual X at worst.
`#196` · game 33 · round 16 · agent A10 (opponent: script:Random) · other · A10: Exchange 22 vs A21. They've shifted to M on 19,20,21 (mutual M, 1 each) after being exploited. Picking M for mutual 1 each.
`#197` · game 39 · round 5 · agent A22 (opponent: A04) · other · A22: Exchange 11 vs A04. A04 defected with X on 1,2,8; we've had mutual X on 9,10. They keep signaling exploit of my Q. Picking X to avoid feeding 5 and get mutual 1.
`#198` · game 35 · round 7 · agent A10 (opponent: A17) · other · A10: Exchange 13 vs A17. They shifted to N on 10-12 after T-heavy earlier. Picking N to protect against their N (mutual 1) and exploit if they switch back to T (5).
`#199` · game 46 · round 3 · agent A15 (opponent: script:AlwaysDefect) · other · A15: Exchange 9 vs A23. They played Q 6/8, X on 7-8. This is final exchange. Picking X to exploit if they return to Q, get mutual 1 if they pick X.
`#200` · game 33 · round 17 · agent A10 (opponent: script:Random) · other · A10: Exchange 23 vs A21. They've played M on 19-22 (mutual M, 1 each). Continuing M for mutual 1.
`#201` · game 33 · round 18 · agent A10 (opponent: script:Random) · other · A10: Exchange 24 vs A21. They reverted to P on 23 after mutual M on 19-22. Picking M to exploit their P play.
`#202` · game 35 · round 8 · agent A10 (opponent: A17) · other · A10: Exchange 14 vs A17. They've been N on 10-13 (mutual N, 1 each). Staying N for mutual 1 and protection against their T-switch.
`#203` · game 39 · round 6 · agent A22 (opponent: A04) · other · A22: Exchange 12 vs A04. They've defected with X on 1,2,8,9,10,11 and keep signaling exploit. Picking X for mutual 1 to avoid feeding them 5.
`#204` · game 44 · round 3 · agent A15 (opponent: A07) · other · A15: Exchange 9 vs A07. They've exploited my Y with W on 1,2,7 and mutual W on 8. Picking W to get mutual 1 rather than feeding them 5 with Y.
`#205` · game 44 · round 3 · agent A07 (opponent: A15) · other · A07: Exchange 9 vs A15. They've played Y all 8 times despite my W exploits on 1,2,7 and mutual W on 8. Picking W to exploit their consistent Y for 5 points.
`#206` · game 35 · round 9 · agent A10 (opponent: A17) · other · A10: Exchange 15 vs A17. They played T on 14 after N on 10-13. Picking N to protect against their N and exploit if they continue T.
`#207` · game 43 · round 6 · agent A03 (opponent: A15) · other · A03: Exchange 12 vs A15. A15 has signaled X repeatedly (mutual X on 8-11). Picking X for mutual 1.
`#208` · game 39 · round 7 · agent A04 (opponent: A22) · other · A04: Exchange 13 vs A22. They've picked X on 9-12 to defend against my exploits. Picking X for mutual 1.
`#209` · game 39 · round 7 · agent A22 (opponent: A04) · other · A22: Exchange 13 vs A04. We've had mutual X on 9-12. A04 keeps signaling X to exploit my Q. Picking X for mutual 1 and protection against their X.
`#210` · game 46 · round 8 · agent A15 (opponent: script:AlwaysDefect) · other · A15: Exchange 14 vs A23. They've played Q 6/13, X on 7-13 (mutual X streak). Picking X for mutual 1 and protection against their X.
`#211` · game 44 · round 4 · agent A07 (opponent: A15) · other · A07: Exchange 10 vs A15. They've switched to W on 8-9 to stop feeding my W exploits. Final exchange, picking W for mutual 1.
`#212` · game 43 · round 7 · agent A15 (opponent: A03) · other · A15: Exchange 13 vs A03. A03 signals X for mutual 1. Picking X for mutual 1.
`#213` · game 35 · round 10 · agent A17 (opponent: A10) · other · A17: Exchange 16 vs A10. They've signaled N repeatedly to protect against my N. Picking N for mutual 1.
`#214` · game 34 · round 17 · agent A22 (opponent: A00) · other · A22: Exchange 23 vs A00. They've exploited my J with F on 20,21,22 (and 15 earlier). Retaliating with F to stop feeding them 5s.
`#215` · game 33 · round 24 · agent A10 (opponent: script:Random) · other · A10: Exchange 30 vs A21. They played M on 29 after P on 28. Pattern of M streaks with occasional P. Picking M to get mutual 1 or exploit their P.
`#216` · game 39 · round 10 · agent A04 (opponent: A22) · other · A04: Exchange 16 vs A22. Mutual X streak on 9-15. Continuing X for mutual 1.
`#217` · game 43 · round 8 · agent A03 (opponent: A15) · other · A03: Exchange 14 vs A15. We've had mutual X on 8-13. Picking X for mutual 1.
`#218` · game 33 · round 25 · agent A10 (opponent: script:Random) · other · A10: Exchange 31 vs A21. They played P on 28, M on 29-30. Pattern suggests possible P on 31. Picking M to exploit their P (5) or get mutual 1.
`#219` · game 46 · round 14 · agent A15 (opponent: script:AlwaysDefect) · other · A15: Exchange 20 vs A23. We've had mutual X streak since 7. Final exchange, picking X for mutual 1.
`#220` · game 34 · round 18 · agent A22 (opponent: A00) · other · A22: Exchange 24 vs A00. They exploited my J with F on 20,21,22; I retaliated with F on 23 (mutual F). Continuing F to avoid feeding them 5s and get mutual 1.
`#221` · game 39 · round 11 · agent A22 (opponent: A04) · other · A22: Exchange 17 vs A04. Mutual X streak continues. Picking X for mutual 1.
`#222` · game 43 · round 9 · agent A03 (opponent: A15) · other · A03: Exchange 15 vs A15. Mutual X streak on 8-14. Continuing X for mutual 1.
`#223` · game 43 · round 9 · agent A15 (opponent: A03) · other · A15: Exchange 15 vs A03. Mutual X streak on 8-14. Picking X for mutual 1.
`#224` · game 46 · round 15 · agent A15 (opponent: script:AlwaysDefect) · other · A15: Exchange 21 vs A23. We've had mutual X streak since 7. Continuing X for mutual 1.
`#225` · game 35 · round 11 · agent A17 (opponent: A10) · other · A17: Exchange 17 vs A10. They played T on 16 (I got 5). They'll likely return to N now to protect themselves. Picking N for mutual 1.
`#226` · game 33 · round 26 · agent A10 (opponent: script:Random) · other · A10: Exchange 32 vs A21. They played M on 29-31 after P on 28. Continuing M for mutual 1 or to exploit potential P.
`#227` · game 43 · round 10 · agent A03 (opponent: A15) · other · A03: Exchange 16 vs A15. Mutual X streak on 8-15. Continuing X for mutual 1.
`#228` · game 34 · round 19 · agent A22 (opponent: A00) · other · A22: Exchange 25 vs A00. They exploited my J with F on 20,21,22. I retaliated with F on 23-24 (mutual F). Continuing F to avoid feeding them 5s and get mutual 1.
`#229` · game 44 · round 7 · agent A15 (opponent: A07) · other · A15: Exchange 13 vs A07. They've played W on 7-12 (exploited my Y on 7, mutual W on 8-12). Picking W for mutual 1 rather than feeding them 5 with Y.
`#230` · game 43 · round 11 · agent A03 (opponent: A15) · other · A03: Exchange 17 vs A15. Mutual X streak on 8-16. Continuing X for mutual 1.
`#231` · game 33 · round 28 · agent A10 (opponent: script:Random) · other · A10: Exchange 34 vs A21. They've played M on 29-33 (5 straight) after P on 28. Continuing M for mutual 1 or to exploit potential P.
`#232` · game 40 · round 18 · agent A08 (opponent: script:TitForTat) · other · A08: Exchange 24 vs A02. Mutual X streak on 18-23. Continuing X for mutual 1.
`#233` · game 34 · round 20 · agent A22 (opponent: A00) · other · A22: Exchange 26 vs A00. They exploited my J with F on 20-22; I retaliated F on 23-25 (mutual F). Continuing F for mutual 1 / protection.
`#234` · game 43 · round 12 · agent A15 (opponent: A03) · other · A15: Exchange 18 vs A03. Mutual X streak on 8-17. Final exchange, picking X for mutual 1.
`#235` · game 40 · round 19 · agent A08 (opponent: script:TitForTat) · other · A08: Exchange 25 vs A02. Mutual X streak on 18-24. Continuing X for mutual 1.
`#236` · game 44 · round 8 · agent A15 (opponent: A07) · other · A15: Exchange 14 vs A07. Mutual W streak on 8-13. Picking W for mutual 1.
`#237` · game 44 · round 8 · agent A07 (opponent: A15) · other · A07: Exchange 14 vs A15. Mutual W streak on 8-13. Picking W for mutual 1.
`#238` · game 33 · round 30 · agent A10 (opponent: script:Random) · other · A10: Exchange 36 vs A21. Long M streak from them (29-35). Picking M for mutual 1 or to exploit a potential P.
`#239` · game 35 · round 12 · agent A10 (opponent: A17) · other · A10: Exchange 18 vs A17. They signaled N expecting me to return to N after my T on 16. Playing T to exploit their N.
`#240` · game 35 · round 12 · agent A17 (opponent: A10) · other · A17: Exchange 18 vs A10 (final). They played T on 16, N on 17. Picking N for mutual 1 or exploit 5.
`#241` · game 39 · round 15 · agent A04 (opponent: A22) · other · A04: Exchange 21 vs A22. Mutual X streak since 9. Continuing X for mutual 1.
`#242` · game 40 · round 20 · agent A08 (opponent: script:TitForTat) · other · A08: Exchange 26 vs A02. Mutual X streak on 18-25. Continuing X for mutual 1.
`#243` · game 40 · round 22 · agent A08 (opponent: script:TitForTat) · other · A08: Exchange 28 vs A02. Mutual X streak on 18-27. Continuing X for mutual 1.
`#244` · game 34 · round 22 · agent A00 (opponent: A22) · other · A00: Exchange 28 vs A22. They committed to F on 23-27 for mutual 1/protection. Continuing F for mutual 1.
`#245` · game 40 · round 24 · agent A08 (opponent: script:TitForTat) · other · A08: Exchange 30 vs A02. Mutual X streak on 18-29. Continuing X for mutual 1.
`#246` · game 44 · round 11 · agent A07 (opponent: A15) · other · A07: Exchange 17 vs A15. Mutual W streak since 8. Continuing W for mutual 1.
`#247` · game 43 · round 16 · agent A03 (opponent: A15) · other · A03: Exchange 22 vs A15. Mutual X streak since 8. Continuing X for mutual 1.
`#248` · game 43 · round 16 · agent A15 (opponent: A03) · other · A15: Exchange 22 vs A03. Mutual X streak on 8-21. Continuing X for mutual 1.
`#249` · game 39 · round 18 · agent A04 (opponent: A22) · other · A04: Exchange 24 vs A22. Mutual X streak since 9. Continuing X for mutual 1.
`#250` · game 34 · round 23 · agent A00 (opponent: A22) · other · A00: Exchange 29 vs A22. We've been in mutual F streak since 23. Continuing F for mutual 1.
`#251` · game 43 · round 17 · agent A03 (opponent: A15) · other · A03: Exchange 23 vs A15. Mutual X streak since 8. Continuing X for mutual 1.
`#252` · game 40 · round 27 · agent A08 (opponent: script:TitForTat) · other · A08: Exchange 33 vs A02. Mutual X streak on 18-32. Continuing X for mutual 1.
`#253` · game 48 · round 7 · agent A18 (opponent: script:TitForTat) · uncoded · A18: Exchange 13 vs A13. Mutual J streak on 3-12. Continuing J for mutual 3.
`#254` · game 43 · round 19 · agent A03 (opponent: A15) · other · A03: Exchange 25 vs A15. Mutual X streak since 8. Continuing X for mutual 1.
`#255` · game 35 · round 15 · agent A10 (opponent: A17) · other · A10: Exchange 21 vs A17. They've played N on 16-20 repeatedly despite my T exploits. Picking T to exploit their likely N.
`#256` · game 35 · round 15 · agent A17 (opponent: A10) · other · A17: Exchange 21 vs A10. They've exploited my N on 16,18,20 (T) and mutual N on 17,19. Playing T to counter-exploit on odd exchange.
`#257` · game 49 · round 3 · agent A07 (opponent: script:Random) · other · A07: Exchange 9 vs A06. They defected W on 7,8 after mutual Y on 3-6. Responding W to punish.
`#258` · game 43 · round 21 · agent A03 (opponent: A15) · other · A03: Exchange 27 vs A15. Mutual X streak since 8. Continuing X for mutual 1.
`#259` · game 34 · round 28 · agent A22 (opponent: A00) · other · A22: Exchange 34 vs A00. Mutual F streak since 23. Continuing F for mutual 1.
`#260` · game 49 · round 5 · agent A07 (opponent: script:Random) · other · A07: Exchange 11 vs A06. They defected W on 7,8,10 after mutual Y on 3-6. Playing W to counter their repeated defection.
`#261` · game 49 · round 6 · agent A07 (opponent: script:Random) · other · A07: Exchange 12 vs A06. They defected W on 7,8,10 against my Y; mutual W on 9,11. Continuing W to avoid being exploited.
`#262` · game 50 · round 2 · agent A04 (opponent: script:Pavlov) · other · A04: Exchange 8 vs A12. They've played T all 7 exchanges. Playing N to exploit their T for 5.
`#263` · game 35 · round 17 · agent A10 (opponent: A17) · other · A10: Exchange 23 vs A17. They played T on 21,22. Playing T to seek mutual 3 or avoid giving free 5.
`#264` · game 49 · round 7 · agent A07 (opponent: script:Random) · other · A07: Exchange 13 vs A06. Mixed pattern - they defected on 7,8,10; mutual W on 9,11; I defected on 12. Continuing W to avoid exploitation given their repeated defections.
`#265` · game 50 · round 3 · agent A04 (opponent: script:Pavlov) · other · A04: Exchange 9 vs A12. They've played T 7/8 times. Playing N to exploit their likely T.
`#266` · game 53 · round 2 · agent A08 (opponent: script:Pavlov) · other · A08: Exchange 8 vs A12. Mutual Q streak on 3-7. Continuing Q for mutual 3.
`#267` · game 49 · round 8 · agent A07 (opponent: script:Random) · other · A07: Exchange 14 vs A06. Pattern mixed - they defected on 7,8,10; I defected on 1,2,12,13; mutual W on 9,11. Playing W to avoid exploitation.
`#268` · game 50 · round 4 · agent A04 (opponent: script:Pavlov) · other · A04: Exchange 10 vs A12. They've played T 8/9 times despite my N exploitation. Continuing N to exploit their likely T.
`#269` · game 35 · round 18 · agent A10 (opponent: A17) · other · A10: Exchange 24 vs A17. They played N on 23 against my T. Playing T again - T dominates: 3 if mutual T, 5 if they play N.
`#270` · game 35 · round 18 · agent A17 (opponent: A10) · other · A17: Exchange 24 vs A10. They've played T very often (13/23). Playing T to seek mutual 3 / avoid giving free 5.
`#271` · game 49 · round 9 · agent A07 (opponent: script:Random) · other · A07: Exchange 15 vs A06. They played Y on 12-14 while I defected W getting 5 each. Continuing W to exploit their Y.
`#272` · game 52 · round 4 · agent A10 (opponent: script:AlwaysDefect) · other · A10: Exchange 10 vs A05. They defected W on 7,9 against my Y; mutual W on 8. Playing W to avoid being exploited.
`#273` · game 49 · round 10 · agent A07 (opponent: script:Random) · other · A07: Exchange 16 vs A06. They've played Y on 12-15 while I got 5 each on W. Continuing W to exploit their cooperative Y.
`#274` · game 52 · round 6 · agent A10 (opponent: script:AlwaysDefect) · other · A10: Exchange 12 vs A05. They've defected W on 7,9,11 against my Y; mutual W on 8,10. Playing W to avoid being exploited.
`#275` · game 50 · round 7 · agent A04 (opponent: script:Pavlov) · other · A04: Exchange 13 vs A12. They've played T 9/12 times and keep playing T despite my N exploitation. Continuing N to exploit their likely T for 5.
`#276` · game 35 · round 19 · agent A10 (opponent: A17) · other · A10: Exchange 25 vs A17. Recent mutual T on 21,24; they played N on 23. Playing T to seek mutual 3 or exploit N.
`#277` · game 35 · round 19 · agent A17 (opponent: A10) · other · A17: Exchange 25 vs A10. They've stated they're playing T. Playing N to exploit their T for 5.
`#278` · game 57 · round 4 · agent A04 (opponent: script:Random) · other · A04: Exchange 10 vs A21. They've played Q 7/9 times. Playing X to exploit their likely Q for 5.
`#279` · game 49 · round 11 · agent A07 (opponent: script:Random) · other · A07: Exchange 17 vs A06. They've played Y on 12-16 while I got 5 each on W. Continuing W to exploit their cooperative Y.
`#280` · game 56 · round 5 · agent A18 (opponent: A17) · other · A18: Exchange 11 vs A17. Mutual P streak since exchange 3. Continuing P for mutual 3.
`#281` · game 52 · round 7 · agent A10 (opponent: script:AlwaysDefect) · other · A10: Exchange 13 vs A05. They've defected W on 7,9,11 against my Y; mutual W on 8,10,12. Playing W to avoid exploitation.
`#282` · game 57 · round 5 · agent A04 (opponent: script:Random) · other · A04: Exchange 11 vs A21. They played X on 9,10 after Q on 8. Playing X to match their likely X for mutual 1.
`#283` · game 35 · round 20 · agent A10 (opponent: A17) · other · A10: Exchange 26 vs A17. They exploited my T with N on 23,25. Switching to N to counter their exploitation.
`#284` · game 52 · round 9 · agent A10 (opponent: script:AlwaysDefect) · other · A10: Exchange 15 vs A05. They defected W on 7,9,11 against my Y; mutual W on 8,10,12,13,14. Playing W to avoid being exploited.
`#285` · game 57 · round 6 · agent A04 (opponent: script:Random) · other · A04: Exchange 12 vs A21. They keep playing Q despite my X exploitation (X got 5 on exchanges 1,2,8,11). Playing X to exploit their likely Q.
`#286` · game 50 · round 12 · agent A04 (opponent: script:Pavlov) · other · A04: Exchange 18 vs A12. They've been alternating N,T since exchange 8 (even=N, odd=T). Exchange 18 is even → they likely play N. Playing N for mutual 1.
`#287` · game 49 · round 15 · agent A07 (opponent: script:Random) · other · A07: Exchange 21 vs A06. They played W on 20 after my W streak exploited their Y on 12-19. Playing W to protect against their defection.
`#288` · game 53 · round 13 · agent A08 (opponent: script:Pavlov) · other · A08: Exchange 19 vs A12. Mutual Q streak since exchange 3. They've played Q all 18 times. Continuing Q for mutual 3.
`#289` · game 57 · round 8 · agent A04 (opponent: script:Random) · other · A04: Exchange 14 vs A21. They've played Q 8/13 overall despite my X exploitation. Recent pattern mixed (X on 9,10,12,13; Q on 11). Playing X to exploit their likely Q for 5.
`#290` · game 49 · round 18 · agent A07 (opponent: script:Random) · other · A07: Exchange 24 vs A06. They've played Y 15/23 times. Recent pattern: Y on 21, W on 22, W on 23. They seem to be shifting toward W. I'll play W to protect against defection and seek mutual W.
`#291` · game 52 · round 13 · agent A10 (opponent: script:AlwaysDefect) · other · A10: Exchange 19 vs A05. Mutual W streak since 12. They keep defecting W against my Y. Playing W for mutual 1.
`#292` · game 53 · round 15 · agent A08 (opponent: script:Pavlov) · other · A08: Exchange 21 vs A12. They've played Q all 20 times; I exploited with X on 20. Continuing X to exploit their likely Q for 5.
`#293` · game 50 · round 16 · agent A04 (opponent: script:Pavlov) · other · A04: Exchange 22 vs A12. They alternate N,T since exchange 8 (even=N, odd=T). Exchange 22 even → they likely play N. Playing N for mutual 1.
`#294` · game 49 · round 19 · agent A07 (opponent: script:Random) · other · A07: Exchange 25 vs A06. They've played Y on 21,24 and W on 20,22,23. My W strategy has been very profitable. Continuing W to exploit their likely Y or seek mutual W.
`#295` · game 50 · round 17 · agent A04 (opponent: script:Pavlov) · other · A04: Exchange 23 vs A12. They alternate N,T since exchange 8 (even=N, odd=T). Exchange 23 odd → they likely play T. Playing N to exploit for 5.
`#296` · game 52 · round 16 · agent A10 (opponent: script:AlwaysDefect) · other · A10: Exchange 22 vs A05. Long mutual W streak since 12. Continuing W for mutual 1.
`#297` · game 53 · round 16 · agent A08 (opponent: script:Pavlov) · other · A08: Exchange 22 vs A12. They played Q 20/21 times; I exploited X on 20 (got 5), they retaliated X on 21 (mutual 1). Playing X to see if they return to Q for another 5.
`#298` · game 49 · round 20 · agent A07 (opponent: script:Random) · other · A07: Exchange 26 vs A06. They've played W on 22,23,25 and Y on 24. My W dominates: 5 if they Y, 1 if they W. Continuing W.
`#299` · game 52 · round 17 · agent A10 (opponent: script:AlwaysDefect) · other · A10: Exchange 23 vs A05. Long mutual W streak since 12. Continuing W for mutual 1.
`#300` · game 50 · round 18 · agent A04 (opponent: script:Pavlov) · other · A04: Exchange 24 vs A12. They alternate N,T since exchange 8 (even=N, odd=T). Exchange 24 even → they likely play N. Playing N for mutual 1.
`#301` · game 57 · round 12 · agent A04 (opponent: script:Random) · other · A04: Exchange 18 vs A21. Mutual X streak since exchange 12. Playing X to match their likely X for mutual 1.
`#302` · game 56 · round 9 · agent A18 (opponent: A17) · other · A18: Exchange 15 vs A17. Mutual M streak since 12 after they defected on 11 (M vs my P). Continuing M for mutual 1, watching for defection.
`#303` · game 49 · round 21 · agent A07 (opponent: script:Random) · other · A07: Exchange 27 vs A06. My W strategy continues to dominate (5 on their Y, 1 on mutual W). Continuing W.
`#304` · game 53 · round 17 · agent A08 (opponent: script:Pavlov) · other · A08: Exchange 23 vs A12. They've played Q 21/22 times; I exploited X on 20 (5) and 22 (5), got mutual 1 on 21. They keep returning to Q. Playing X to exploit for 5.
`#305` · game 52 · round 19 · agent A10 (opponent: script:AlwaysDefect) · other · A10: Exchange 25 vs A05. Long mutual W streak since 12. Continuing W for mutual 1.
`#306` · game 57 · round 14 · agent A04 (opponent: script:Random) · other · A04: Exchange 20 vs A21. They played Q on 19 after long X streak (9-18). My X strategy profitable (46 vs 26). Playing X to exploit likely Q or match X.
`#307` · game 52 · round 21 · agent A10 (opponent: script:AlwaysDefect) · other · A10: Exchange 27 vs A05. Long mutual W streak since 12. Continuing W for mutual 1.
`#308` · game 35 · round 23 · agent A17 (opponent: A10) · other · A17: Exchange 29 vs A10. They alternated N/T recently (26 N, 27 T, 28 N). Expecting T on 29, playing N to exploit for 5.
`#309` · game 53 · round 19 · agent A08 (opponent: script:Pavlov) · other · A08: Exchange 25 vs A12. They've played Q 22/24 times. My X exploitation: 20(Q→5), 21(X→1), 22(Q→5), 23(X→1), 24(Q→5). They alternate retaliation X with returning to Q. Exchange 25 likely X (following even-odd pattern). Playing X for mutual 1 or 5 if they return to Q.
`#310` · game 52 · round 23 · agent A10 (opponent: script:AlwaysDefect) · other · A10: Exchange 29 vs A05. Long mutual W streak since 12. Continuing W for mutual 1.
`#311` · game 49 · round 27 · agent A07 (opponent: script:Random) · other · A07: Exchange 33 vs A06. My W strategy continues to dominate (5 on their Y, 1 on mutual W). Continuing W.
`#312` · game 57 · round 16 · agent A04 (opponent: script:Random) · other · A04: Exchange 22 vs A21. They played Q on 19,20,21 after mutual X streak (12-18). My X exploitation has been very profitable (56 vs 26). Playing X to exploit their likely Q for 5.
`#313` · game 50 · round 23 · agent A04 (opponent: script:Pavlov) · other · A04: Exchange 29 vs A12. They alternate N,T since exchange 8 (even=N, odd=T). Exchange 29 odd → they likely play T. Playing N to exploit for 5.
`#314` · game 56 · round 11 · agent A18 (opponent: A17) · other · A18: Exchange 17 vs A17. Mutual M since 12 with my defection on 15 (they played P). They returned to M on 16. Continuing M for mutual 1.
`#315` · game 56 · round 11 · agent A17 (opponent: A18) · other · A17: Exchange 17 vs A18. Mutual M streak since 12 (I defected P on 15, they returned to M on 16). Continuing M for mutual 1, watching for retaliation.
`#316` · game 53 · round 22 · agent A08 (opponent: script:Pavlov) · other · A08: Exchange 28 vs A12. Pattern since 20: they alternate Q(even)/X(odd). Exchange 28 even → likely Q. Playing X to exploit for 5.
`#317` · game 49 · round 29 · agent A07 (opponent: script:Random) · other · A07: Exchange 35 vs A06. My W strategy has dominated (107 vs 37). They play Y often but sometimes W. Continuing W to exploit their Y for 5 or mutual W for 1.
`#318` · game 57 · round 17 · agent A04 (opponent: script:Random) · other · A04: Exchange 23 vs A21. They played Q on 19,20,21,22 after mutual X streak (12-18). My X exploitation profitable. Playing X to exploit likely Q for 5 or match X for 1.
`#319` · game 58 · round 1 · agent A07 (opponent: script:TitForTat) · other · A07: Exchange 7 vs A20. They've played R all 6 times despite my H exploits in 1-2. I switched to R for mutual 3s in 3-6. Attempting H to exploit their likely R for 5.
`#320` · game 53 · round 25 · agent A08 (opponent: script:Pavlov) · other · A08: Exchange 31 vs A12. Pattern since 20: they alternate Q(even)/X(odd). Exchange 31 odd → they likely play X. Playing X for mutual 1.
`#321` · game 44 · round 30 · agent A15 (opponent: A07) · other · A15: Exchange 36 vs A07. Long mutual W streak since 16. A07 notes confirm they continue W. Playing W for mutual 1.
`#322` · game 61 · round 2 · agent A17 (opponent: script:Random) · other · A17: Exchange 8 vs A21. They've played P all 7 times. I've exploited with M for 5s (ex 1,2,7), got mutual 3 on P/P (3-6). Continuing M to exploit their P for 5.
`#323` · game 57 · round 21 · agent A04 (opponent: script:Random) · other · A04: Exchange 27 vs A21. They've played Q on 19-26 (8 straight). My X exploitation very profitable (81 vs 26). Playing X to exploit their Q for 5.
`#324` · game 58 · round 3 · agent A07 (opponent: script:TitForTat) · other · A07: Exchange 9 vs A20. They played R 7/8 times, switched to H on 8. My H exploited their R for 5s in 1,2,7. Playing H to exploit likely R return or match H for 1.
`#325` · game 61 · round 3 · agent A17 (opponent: script:Random) · other · A17: Exchange 9 vs A21. They've played P all 8 times. My M exploitation profitable (5s on ex 1,2,7,8). Continuing M for 5.
`#326` · game 62 · round 2 · agent A00 (opponent: script:Random) · other · A00: Exchange 8 vs A06. A06 has played T all 7 times. Playing N to exploit their T for 5.
`#327` · game 62 · round 3 · agent A00 (opponent: script:Random) · other · A00: Exchange 9 vs A06. A06 has played T all 8 times. Continuing N to exploit their T for 5.
`#328` · game 57 · round 24 · agent A04 (opponent: script:Random) · other · A04: Exchange 30 vs A21. They've alternated X,Q since 27 (27=X,28=Q,29=X). Expecting Q on 30. Playing X to exploit for 5.
`#329` · game 65 · round 2 · agent A11 (opponent: script:AlwaysDefect) · other · A11 vs A23 ex8: they defected W on ex7 after mutual Y 3-6. Playing W to protect/exploit after their defection.
`#330` · game 56 · round 15 · agent A17 (opponent: A18) · other · A17: Exchange 21 vs A18. Mutual M streak since 12 (I defected P on 15, they returned M on 16). Continuing M for mutual 1.
`#331` · game 62 · round 6 · agent A00 (opponent: script:Random) · other · A00: Exchange 12 vs A06. They've played T 10/11 times. Continuing N to exploit their T for 5.
`#332` · game 65 · round 3 · agent A11 (opponent: script:AlwaysDefect) · other · A11 vs A23 ex9: after their defection ex7 and mutual W ex8, playing W to hedge (5 if they Y, 1 if mutual W).
`#333` · game 57 · round 26 · agent A04 (opponent: script:Random) · other · A04: Exchange 32 vs A21. They played Q on 28,30,31, X on 27,29. My X exploitation very profitable (98 vs 28). Playing X to exploit likely Q for 5.
`#334` · game 57 · round 29 · agent A04 (opponent: script:Random) · other · A04: Exchange 35 vs A21. They've played Q most exchanges (20/34). My X exploitation very profitable (105 vs 30). Continuing X to exploit likely Q for 5 or match X for 1.
`#335` · game 62 · round 8 · agent A00 (opponent: script:Random) · other · A00: Exchange 14 vs A06. They've played T 12/13 times. Continuing N to exploit their T for 5.
`#336` · game 65 · round 4 · agent A11 (opponent: script:AlwaysDefect) · other · A11 vs A23 ex10: after mutual W ex8-9 following their ex7 defection, continuing W for hedge (5 if they Y, 1 if mutual W).
`#337` · game 61 · round 9 · agent A17 (opponent: script:Random) · other · A17: Exchange 15 vs A21. They play P often (11/14), played P on 14. Continuing M to exploit their P for 5, watching for M retaliation.
`#338` · game 65 · round 5 · agent A11 (opponent: script:AlwaysDefect) · other · A11 vs A23 ex11: continuing W after mutual W ex8-10 following their ex7 defection. Hedge for 5 or mutual 1.
`#339` · game 61 · round 10 · agent A17 (opponent: script:Random) · other · A17: Exchange 16 vs A21. They played P on 14,15 after mutual M on 10,11,13. Continuing M to exploit their likely P for 5.
`#340` · game 68 · round 1 · agent A11 (opponent: script:Pavlov) · other · A11 vs A14 ex7: I picked W ex1-2 (exploited their Y), then mutual Y ex3-6. They've stuck with Y 6/6. Considering returning to W to exploit their likely continued Y for 5.
`#341` · game 65 · round 6 · agent A11 (opponent: script:AlwaysDefect) · other · A11 vs A23 ex12: continuing W after mutual W ex8-11 following their ex7 defection. Hedge for 5 or mutual 1.
`#342` · game 68 · round 2 · agent A11 (opponent: script:Pavlov) · other · A11 vs A14 ex8: They've played Y 7/7. My W exploitation profitable (5s ex1,2,7). Continuing W to exploit their continued Y for 5.
`#343` · game 61 · round 16 · agent A17 (opponent: script:Random) · other · A17: Exchange 22 vs A21. They've played P 16/21, M only occasionally (10,11,13,18,20). My M exploitation very profitable (77 vs 17). Continuing M to exploit their likely P for 5.
`#344` · game 68 · round 3 · agent A11 (opponent: script:Pavlov) · other · A11 vs A14 ex9: They've played Y 7/8, W on ex8. My W exploitation profitable (5s ex1,2,7). Continuing W for 5 if they Y, 1 if mutual W.
`#345` · game 66 · round 2 · agent A16 (opponent: A10) · other · A16 vs A10 ex8: A10 played P 6/7, M only on ex7. I've exploited with M on 1,2,7. Playing M to exploit likely P return for 5.
`#346` · game 66 · round 2 · agent A10 (opponent: A16) · other · A10 vs A16 ex8: They've played P 6/7, M on ex7 (mutual 1). Playing M to exploit likely P return for 5.
`#347` · game 65 · round 8 · agent A11 (opponent: script:AlwaysDefect) · other · A11 vs A23 ex14: continuing W after mutual W ex8-13 following their ex7 defection. Hedge for 5 or mutual 1.
`#348` · game 58 · round 6 · agent A07 (opponent: script:TitForTat) · other · A07: Exchange 12 vs A20. They've played R 8/11 times, H on 8,9,10 then R on 11. My H exploitation profitable (34 vs 19). Playing H to exploit likely R for 5 or match H for 1.
`#349` · game 61 · round 18 · agent A17 (opponent: script:Random) · other · A17: Exchange 24 vs A21. They've played P 17/23, M on 10,11,13,18,20,23. My M exploitation very profitable (83 vs 18). Continuing M to exploit likely P for 5.
`#350` · game 62 · round 13 · agent A00 (opponent: script:Random) · other · A00: Exchange 19 vs A06. They've played T 14/18 but shifted to N in 3 of last 5 (14,17,18). Continuing N to exploit any T for 5 or accept mutual N for 1.
`#351` · game 35 · round 28 · agent A17 (opponent: A10) · other · A17: Exchange 34 vs A10. They've played N 6 straight (28-33), mutual N streak. N gives 1 vs their N (T gives 0), and 5 vs their T. Continuing N.
`#352` · game 68 · round 5 · agent A11 (opponent: script:Pavlov) · other · A11 vs A14 ex11: They've played Y 8/10, W on ex8,10 (mutual W both). My W exploitation profitable (5s ex1,2,7,9). Continuing W for 5 if they Y, 1 if mutual W.
`#353` · game 68 · round 6 · agent A11 (opponent: script:Pavlov) · other · A11 vs A14 ex12: They've played Y 9/11, W on ex8,10 (mutual W). My W exploitation profitable (5s ex1,2,7,9,11). Continuing W for 5 if they Y, 1 if mutual W.
`#354` · game 65 · round 11 · agent A11 (opponent: script:AlwaysDefect) · other · A11 vs A23 ex17: continuing W after mutual W ex8-16 following their ex7 defection. Hedge for 5 or mutual 1.
`#355` · game 35 · round 29 · agent A10 (opponent: A17) · other · A10 vs A17 ex35: They've played N 7 straight (28-34) and note says continuing N. Playing N for mutual 1.
`#356` · game 56 · round 20 · agent A18 (opponent: A17) · other · A18: Exchange 26 vs A17. Continuing mutual M streak since ex12. A17 signaled M. Playing M for mutual 1.
`#357` · game 68 · round 8 · agent A11 (opponent: script:Pavlov) · other · A11 vs A14 ex14: They've played Y 10/13, W on ex8,10,12 (mutual W). My W exploitation profitable (5s ex1,2,7,9,11,13). Continuing W for 5 if they Y, 1 if mutual W.
`#358` · game 65 · round 14 · agent A11 (opponent: script:AlwaysDefect) · other · A11 vs A23 ex20: continuing W after mutual W ex8-19 following their ex7 defection. Hedge for 5 or mutual 1.
`#359` · game 58 · round 7 · agent A07 (opponent: script:TitForTat) · other · A07: Exchange 13 vs A20. They've played H 4 of last 5 (8,9,10,12, R on 11). Playing R to exploit likely H for 5.
`#360` · game 35 · round 30 · agent A17 (opponent: A10) · other · A17 vs A10 ex36: They've played N 8 straight (28-35), mutual N streak. Continuing N for mutual 1 or 5 if they T.
`#361` · game 68 · round 9 · agent A11 (opponent: script:Pavlov) · other · A11 vs A14 ex15: They've played Y 10/13, W on ex8,10,12 (mutual W). My W exploitation profitable (5s ex1,2,7,9,11,13). Continuing W for 5 if they Y, 1 if mutual W.
`#362` · game 68 · round 10 · agent A11 (opponent: script:Pavlov) · other · A11 vs A14 ex16: They've played Y 11/14, W on ex8,10,12 (mutual W). My W exploitation profitable (5s ex1,2,7,9,11,13,15). Continuing W for 5 if they Y, 1 if mutual W.
`#363` · game 56 · round 21 · agent A17 (opponent: A18) · other · A17: Exchange 27 vs A18. Long mutual M streak since ex12. A18 signaled M. Continuing M for mutual 1.
`#364` · game 70 · round 1 · agent A16 (opponent: A22) · other · A16 vs A22 ex7: They've played Y 6/6. I exploited W ex1-2, then mutual Y ex3-6. Playing W to exploit likely continued Y for 5.
`#365` · game 71 · round 1 · agent A15 (opponent: A10) · other · A15 vs A10 ex7: A10 played P 6/6. My M exploitation profitable (5s ex1,2). Continuing M to exploit likely P for 5.
`#366` · game 66 · round 5 · agent A10 (opponent: A16) · other · A10 vs A16 ex11: Mutual M ex7-10. Playing M to continue mutual 1 or exploit P switch for 5.
`#367` · game 72 · round 2 · agent A22 (opponent: script:TitForTat) · other · A22 vs A13 ex8: A13 played P 7/7. My M exploitation very profitable (27 vs 12). Continuing M to exploit likely P for 5.
`#368` · game 69 · round 3 · agent A10 (opponent: script:TitForTat) · other · A10 vs A20 ex9: They've played Q 8/8. Playing X to exploit likely Q for 5.
`#369` · game 71 · round 2 · agent A10 (opponent: A15) · other · A10 vs A15 ex8: A15 signaled M to exploit my "P". I'll play M for mutual 1.
`#370` · game 69 · round 4 · agent A10 (opponent: script:TitForTat) · other · A10 vs A20 ex10: They've played Q 9/9. Playing X to exploit likely Q for 5.
`#371` · game 74 · round 4 · agent A16 (opponent: script:Grudger) · other · A16 vs A09 ex10: A09 has played R all 9 exchanges. My H exploitation profitable (5s ex1,2,9). Playing H to exploit likely R for 5.
`#372` · game 76 · round 1 · agent A22 (opponent: script:TitForTat) · other · A22 vs A19 ex7: A19 has played Q 6/6. I exploited X ex1-2, mutual Q ex3-6. Playing X to exploit likely continued Q for 5.
`#373` · game 75 · round 2 · agent A00 (opponent: A03) · uncoded · A00 vs A03 ex8: They've played Q 7/7. Playing X to exploit likely Q for 5.
`#374` · game 74 · round 5 · agent A16 (opponent: script:Grudger) · other · A16 vs A09 ex11: A09 played R 9/10, H on ex10 (mutual H). Continuing H to exploit likely R return for 5, or mutual H for 1.
`#375` · game 74 · round 6 · agent A16 (opponent: script:Grudger) · other · A16 vs A09 ex12: A09 played R 9/11, H on ex10-11 (mutual H). Playing H to exploit likely R return for 5, or mutual H for 1.
`#376` · game 78 · round 1 · agent A18 (opponent: script:TitForTat) · other · A18 vs A19 ex7: Mutual Q ex3-6 after my X ex1-2. A19 has played Q 6/6. Continuing Q for mutual 3.
`#377` · game 77 · round 1 · agent A04 (opponent: A10) · other · A04 vs A10 ex7: A10 played Y 6/6. I exploited W ex1-2, mutual Y ex3-6. Playing W to exploit likely continued Y for 5.
`#378` · game 74 · round 7 · agent A16 (opponent: script:Grudger) · other · A16 vs A09 ex13: A09 played R 9/12, H on ex10-12 (mutual H). Playing H to exploit likely R return for 5, or mutual H for 1.
`#379` · game 56 · round 27 · agent A18 (opponent: A17) · other · A18: Exchange 33 vs A17. Continuing long mutual M streak since ex12. Playing M for mutual 1.
`#380` · game 78 · round 3 · agent A18 (opponent: script:TitForTat) · other · A18 vs A19 ex9: Mutual Q ex3-8 after my X ex1-2. A19 played Q 8/8. I've been signaling Q. Continuing Q for mutual 3.
`#381` · game 56 · round 28 · agent A18 (opponent: A17) · other · A18 vs A17 ex34: Continuing long mutual M streak since ex12. Playing M for mutual 1.
`#382` · game 56 · round 28 · agent A17 (opponent: A18) · other · A17 vs A18 ex34: Long mutual M streak since ex12. A18 signaled M. Continuing M for mutual 1.
`#383` · game 79 · round 3 · agent A00 (opponent: script:Pavlov) · other · A00 vs A14 ex9: A14 played R 7/8, H only ex8. Playing H to exploit likely R for 5.
`#384` · game 56 · round 29 · agent A18 (opponent: A17) · other · A18 vs A17 ex35: Continuing long mutual M streak since ex12. Playing M for mutual 1.
`#385` · game 82 · round 1 · agent A18 (opponent: A08) · other · A18 vs A08 ex7: Mutual T ex3-6 after my N ex1-2. A08 played T 6/6. Continuing T for mutual 3.
`#386` · game 82 · round 1 · agent A08 (opponent: A18) · other · A08 vs A18 ex7: Mutual T ex3-6 after my N ex1-2. A18 played T 6/6. Continuing T for mutual 3.
`#387` · game 80 · round 1 · agent A03 (opponent: A16) · other · A03 vs A16 ex7: A16 has played Y 6/6. I exploited W ex1-2, mutual Y ex3-6. Playing W to exploit likely continued Y for 5.
`#388` · game 56 · round 30 · agent A18 (opponent: A17) · other · A18 vs A17 ex36: Continuing long mutual M streak since ex12. Playing M for mutual 1.
`#389` · game 77 · round 2 · agent A04 (opponent: A10) · other · A04 vs A10 ex8: A10 played Y 6/7, mutual W ex7. Playing W to exploit likely Y for 5, or mutual W for 1.
`#390` · game 77 · round 2 · agent A10 (opponent: A04) · other · A10 vs A04 ex8: A04 signaled W to exploit my supposed Y. I'll play W for mutual 1 rather than risk 0.
`#391` · game 79 · round 6 · agent A00 (opponent: script:Pavlov) · other · A00 vs A14 ex12: A14 played R 9/11, H only ex8,10 (mutual H both). Playing H to exploit likely R for 5.
`#392` · game 69 · round 9 · agent A10 (opponent: script:TitForTat) · other · A10 vs A20 ex15: Mutual X ex10-14 after exploiting their Q streak. Playing X for mutual 1.
`#393` · game 82 · round 2 · agent A08 (opponent: A18) · other · A08 vs A18 ex8: Mutual T ex3-7. A18 played T 7/7. Continuing T for mutual 3.
`#394` · game 71 · round 7 · agent A10 (opponent: A15) · other · A10 vs A15 ex13: Mutual M ex7-12. Continuing M for mutual 1.
`#395` · game 77 · round 3 · agent A04 (opponent: A10) · other · A04 vs A10 ex9: A10 committed to W for mutual 1. Playing W for mutual 1.
`#396` · game 82 · round 3 · agent A08 (opponent: A18) · other · A08 vs A18 ex9: Mutual T ex3-8. A18 played T 8/8. Continuing T for mutual 3.
`#397` · game 83 · round 2 · agent A18 (opponent: script:Random) · other · A18 vs A06 ex8: A06 has played P 7/7. I've exploited with M ex1-2,7. Continuing M to exploit likely P for 5.
`#398` · game 82 · round 4 · agent A08 (opponent: A18) · other · A08 vs A18 ex10: Mutual T ex3-9. A18 played T 9/9. Continuing T for mutual 3.
`#399` · game 79 · round 8 · agent A00 (opponent: script:Pavlov) · other · A00 vs A14 ex14: A14 alternates R,H. Ex13 was R, so likely H this exchange. Playing H for mutual 1.
`#400` · game 83 · round 3 · agent A18 (opponent: script:Random) · other · A18 vs A06 ex9: A06 played P 8/8. I've exploited with M ex1-2,7-8. Continuing M to exploit likely P for 5.
`#401` · game 83 · round 4 · agent A18 (opponent: script:Random) · other · A18 vs A06 ex10: A06 played P 8/9, M only ex9. Continuing M to exploit likely P for 5.
`#402` · game 83 · round 5 · agent A18 (opponent: script:Random) · other · A18 vs A06 ex11: A06 played P 8/9, M only ex9-10. I've exploited with M ex1-2,7-8. Continuing M to exploit likely P for 5.
`#403` · game 85 · round 2 · agent A04 (opponent: script:TitForTat) · other · A04 vs A19 ex8: A19 has played Q 7/7. Mutual Q ex3-7. Playing X to exploit likely Q for 5.
`#404` · game 82 · round 8 · agent A18 (opponent: A08) · other · A18 vs A08 ex14: Mutual T ex3-13. A08 played T 13/13. Continuing T for mutual 3.
`#405` · game 84 · round 2 · agent A00 (opponent: A15) · other · A00 vs A15 ex8: Mutual Q ex3-7 after my X ex1-2. A15 played Q 7/7. Continuing Q for mutual 3.
`#406` · game 85 · round 3 · agent A04 (opponent: script:TitForTat) · other · A04 vs A19 ex9: A19 has played Q 8/8. I've exploited ex1-2,8. Continuing X to exploit likely Q for 5.
`#407` · game 83 · round 7 · agent A18 (opponent: script:Random) · other · A18 vs A06 ex13: A06 has played P 9/12, M only ex9-11. I've exploited with M ex1-2,7-8,12. Continuing M to exploit likely P for 5.
`#408` · game 80 · round 4 · agent A16 (opponent: A03) · other · A16 vs A03 ex10: Mutual W ex7-9 after mutual Y ex3-6. Continuing W for mutual 1.
`#409` · game 85 · round 4 · agent A04 (opponent: script:TitForTat) · other · A04 vs A19 ex10: A19 played Q 8/9, X only ex9. I've exploited ex1-2,8. Playing X to exploit likely Q for 5.
`#410` · game 79 · round 13 · agent A00 (opponent: script:Pavlov) · other · A00 vs A14 ex19: A14 alternates R,H. Ex18 was H, so ex19 likely R. Playing H to exploit for 5.
`#411` · game 77 · round 6 · agent A10 (opponent: A04) · other · A10 vs A04 ex12: Mutual W ex7-11. Continuing W for mutual 1.
`#412` · game 84 · round 4 · agent A15 (opponent: A00) · other · A15 vs A00 ex10: Mutual Q ex3-9 after my X ex1-2. A00 has played Q 9/9. Continuing Q for mutual 3.
`#413` · game 86 · round 2 · agent A00 (opponent: script:TitForTat) · other · A00 vs A02 ex8: A02 has played Y 7/7. I've exploited with W ex1-2,7. Continuing W to exploit likely Y for 5.
`#414` · game 74 · round 16 · agent A16 (opponent: script:Grudger) · other · A16 vs A09 ex22: A09 played H ex10-21 (11 straight). My R ex21 got 0. Returning to H for mutual 1.
`#415` · game 74 · round 18 · agent A16 (opponent: script:Grudger) · other · A16 vs A09 ex24: A09 has played H since ex10. Mutual H for 1. Playing H.
`#416` · game 86 · round 3 · agent A00 (opponent: script:TitForTat) · other · A00 vs A02 ex9: A02 played Y 7/8, W only ex8. I've exploited with W ex1-2,7. Continuing W to exploit likely Y for 5.
`#417` · game 80 · round 6 · agent A03 (opponent: A16) · other · A03 vs A16 ex12: Mutual W ex7-11. A16 committed to W. Continuing W for mutual 1.
`#418` · game 74 · round 19 · agent A16 (opponent: script:Grudger) · other · A16 vs A09 ex25: A09 has played H since ex10. Mutual H for 1. Continuing H.
`#419` · game 84 · round 7 · agent A00 (opponent: A15) · other · A00 vs A15 ex13: Mutual Q ex3-12. A15 played Q 12/12. Continuing Q for mutual 3.
`#420` · game 77 · round 8 · agent A04 (opponent: A10) · other · A04 vs A10 ex14: Mutual W ex7-13. Continuing W for mutual 1.
`#421` · game 77 · round 8 · agent A10 (opponent: A04) · other · A10 vs A04 ex14: Mutual W ex7-13. Continuing W for mutual 1.
`#422` · game 80 · round 7 · agent A03 (opponent: A16) · other · A03 vs A16 ex13: Continuing W for mutual 1.
`#423` · game 77 · round 9 · agent A10 (opponent: A04) · other · A10 vs A04 ex15: Mutual W ex7-14. Continuing W for mutual 1.
`#424` · game 83 · round 12 · agent A18 (opponent: script:Random) · other · A18 vs A06 ex18: A06 played P ex1-8,12,14; M ex9-11,13,15-17. Recent mutual M ex15-17. I'm playing P to exploit their likely M for 5.
`#425` · game 90 · round 2 · agent A07 (opponent: script:AlwaysDefect) · other · A07 vs A23 ex8: A23 played Y 6/7, W only ex7. I exploited ex1-2 with W. Ex7 mutual W. Continuing W to exploit likely Y.
`#426` · game 90 · round 3 · agent A07 (opponent: script:AlwaysDefect) · other · A07 vs A23 ex9: A23 played Y 6/8, W ex7-8. Recent mutual W ex7-8. I'll continue W for mutual 1 or exploit Y for 5.
`#427` · game 74 · round 24 · agent A16 (opponent: script:Grudger) · other · A16 vs A09 ex30: A09 has played H since ex10 (20 straight). Mutual H for 1. Continuing H.
`#428` · game 86 · round 7 · agent A00 (opponent: script:TitForTat) · other · A00 vs A02 ex13: Mutual W ex8-12. Continuing W for mutual 1.
`#429` · game 90 · round 4 · agent A07 (opponent: script:AlwaysDefect) · other · A07 vs A23 ex10: Mutual W ex7-9. Continuing W for mutual 1 or exploit Y for 5.
`#430` · game 86 · round 8 · agent A00 (opponent: script:TitForTat) · other · A00 vs A02 ex14: Mutual W ex8-13. Continuing W for mutual 1.
`#431` · game 90 · round 5 · agent A07 (opponent: script:AlwaysDefect) · other · A07 vs A23 ex11: Mutual W ex7-10. Continuing W for mutual 1.
`#432` · game 84 · round 12 · agent A15 (opponent: A00) · other · A15 vs A00 ex18: Mutual Q ex3-17. A00 played Q 17/17. Continuing Q for mutual 3.
`#433` · game 80 · round 8 · agent A03 (opponent: A16) · other · A03 vs A16 ex14: Continuing W for mutual 1, consistent with ex7-13.
`#434` · game 86 · round 10 · agent A00 (opponent: script:TitForTat) · other · A00 vs A02 ex16: Mutual W ex8-15. Continuing W for mutual 1.
`#435` · game 77 · round 12 · agent A04 (opponent: A10) · other · A04 vs A10 ex18: Mutual W ex7-17. Continuing W for mutual 1.
`#436` · game 77 · round 12 · agent A10 (opponent: A04) · other · A10 vs A04 ex18: Mutual W ex7-17. Continuing W for mutual 1.
`#437` · game 80 · round 9 · agent A16 (opponent: A03) · other · A16 vs A03 ex15: Mutual W ex7-14. Continuing W for mutual 1.
`#438` · game 91 · round 3 · agent A22 (opponent: script:Pavlov) · other · A22 vs A14 ex9: A14 played P 7/8, M only ex8. I've exploited with M ex1,2,7. Continuing M to exploit likely P for 5.
`#439` · game 84 · round 16 · agent A00 (opponent: A15) · other · A00 vs A15 ex22: Mutual Q ex3-21. A15 played Q 21/21. Continuing Q for mutual 3.
`#440` · game 86 · round 19 · agent A00 (opponent: script:TitForTat) · other · A00 vs A02 ex25: Mutual W ex8-24. Continuing W for mutual 1.
`#441` · game 83 · round 17 · agent A18 (opponent: script:Random) · other · A18 vs A06 ex23: A06 played P at ex22 after I exploited their M ex18-21. Playing P to continue mutual 3 or exploit if they revert to M.
`#442` · game 80 · round 12 · agent A03 (opponent: A16) · other · A03 vs A16 ex18: Continuing W for mutual 1, consistent with ex7-17.
`#443` · game 83 · round 18 · agent A18 (opponent: script:Random) · other · A18 vs A06 ex24: A06 played M ex18-21, P ex22, M ex23. They keep exploiting my P. Playing M to get 5 if they play P or mutual 1 if M.
`#444` · game 86 · round 24 · agent A00 (opponent: script:TitForTat) · other · A00 vs A02 ex30: Mutual W ex8-29. Continuing W for mutual 1.
`#445` · game 93 · round 2 · agent A18 (opponent: A00) · other · A18 vs A00 ex8: A00 played T all 7 exchanges. I've cooperated T ex3-7. Exploiting with N this round for 5.
`#446` · game 84 · round 19 · agent A00 (opponent: A15) · other · A00 vs A15 ex25: Mutual Q ex3-24 (A15 played Q 23/24, I played Q 20/24). At ex23 I played X and they played Q; at ex24 mutual X. Continuing Q for mutual 3.
`#447` · game 95 · round 6 · agent A00 (opponent: script:Grudger) · other · A00 vs A09 ex12: A09 played Q 10/11, X ex11. I'll play Q for mutual 3.
`#448` · game 96 · round 3 · agent A07 (opponent: script:TitForTat) · other · A07 vs A19 ex9: Mutual Y ex3-8 after I exploited ex1-2. Continuing Y for mutual 3.
`#449` · game 94 · round 6 · agent A17 (opponent: script:Pavlov) · other · A17 vs A14 ex12: A14 plays J almost always (10/11). I'll play J for mutual 3, consistent with ex3-9.
`#450` · game 94 · round 7 · agent A17 (opponent: script:Pavlov) · other · A17 vs A14 ex13: A14 plays J almost always. Playing F to exploit for 5.
`#451` · game 95 · round 9 · agent A00 (opponent: script:Grudger) · other · A00 vs A09 ex15: A09 played X ex11-14. Playing X this round for safety.
`#452` · game 97 · round 1 · agent A00 (opponent: A11) · other · A00 vs A11 ex7: A11 played R 6/6. I exploited H ex1-2, mutual R ex3-6. Playing H for 5 this round since they stay R.
`#453` · game 92 · round 5 · agent A18 (opponent: script:Pavlov) · other · A18 vs A14 ex11: A14 played J 9/10, I've exploited with F ex1,2,8,10. Playing F to exploit their J for 5.
`#454` · game 99 · round 2 · agent A22 (opponent: script:TitForTat) · other · A22 vs A02 ex8: A02 played Y 7/7. I exploited ex1-2, cooperated Y ex3-7. Exploiting with W for 5 since they keep playing Y.
`#455` · game 92 · round 7 · agent A18 (opponent: script:Pavlov) · other · A18 vs A14 ex13: A14 plays J almost always (10/12). I've exploited with F repeatedly. Playing F to exploit their J for 5.
`#456` · game 95 · round 11 · agent A00 (opponent: script:Grudger) · other · A00 vs A09 ex17: A09 played X ex11-16. Playing X for safety/mutual 1 or exploit if they revert to Q.
`#457` · game 95 · round 12 · agent A00 (opponent: script:Grudger) · other · A00 vs A09 ex18: A09 played X ex11-17. Playing X for mutual 1 / safety.
`#458` · game 92 · round 8 · agent A18 (opponent: script:Pavlov) · other · A18 vs A14 ex14: A14 plays J almost always (10/13). Continuing F to exploit their J for 5.
`#459` · game 100 · round 1 · agent A17 (opponent: script:TitForTat) · other · A17 vs A20 ex7: A20 played Q all 6 exchanges. I played Q ex3-6. Exploiting with X this round for 5.
`#460` · game 95 · round 13 · agent A00 (opponent: script:Grudger) · other · A00 vs A09 ex19: A09 played X ex11-18. Continuing X for mutual 1 / safety.
`#461` · game 80 · round 22 · agent A16 (opponent: A03) · other · A16 vs A03 ex28: Continuing W for mutual 1, consistent with long mutual W streak.
`#462` · game 97 · round 2 · agent A00 (opponent: A11) · other · 
`#463` · game 97 · round 2 · agent A11 (opponent: A00) · other · A11 vs A00 ex8: A00 announced playing H to exploit. I'll play H for mutual 1 rather than give them 5.
`#464` · game 100 · round 2 · agent A17 (opponent: script:TitForTat) · other · A17 vs A20 ex8: A20 played Q all 7 exchanges. I exploited ex1,2,7. Playing X again to exploit their persistent Q for 5.
`#465` · game 92 · round 11 · agent A18 (opponent: script:Pavlov) · other · A18 vs A14 ex17: A14 plays J almost always. Continuing F to exploit their J for 5.
`#466` · game 99 · round 5 · agent A22 (opponent: script:TitForTat) · other · A22 vs A02 ex11: A02 played Y 8/10, but W last two (ex9-10). I exploited ex1-2,8. Playing W for safety/mutual 1 or exploit if they revert to Y.
`#467` · game 95 · round 14 · agent A00 (opponent: script:Grudger) · other · A00 vs A09 ex20: A09 played X ex11-19. Continuing X for mutual 1 / safety.
`#468` · game 95 · round 16 · agent A00 (opponent: script:Grudger) · other · A00 vs A09 ex22: A09 played X ex11-21. Continuing X for mutual 1 / safety.
`#469` · game 100 · round 3 · agent A17 (opponent: script:TitForTat) · other · A17 vs A20 ex9: A20 played Q 7/8, X at ex8. They may retaliate with X now. Playing X for safety/mutual 1.
`#470` · game 93 · round 6 · agent A00 (opponent: A18) · other · A00 vs A18 ex12: A18 played T ex3-7, N ex8, T ex9, N ex10-11. Playing N to match their recent defection pattern.
`#471` · game 97 · round 3 · agent A00 (opponent: A11) · other · A00 vs A11 ex9: A11 played H ex7-8. Playing H for mutual 1 / safety rather than risk giving them 5.
`#472` · game 97 · round 3 · agent A11 (opponent: A00) · other · A11 vs A00 ex9: A00 has exploited me repeatedly (R vs my H). I'll play R to secure mutual 3 rather than give them 5.
`#473` · game 101 · round 1 · agent A16 (opponent: A04) · other · A16 vs A04 ex7: A04 played Y all 6. I cooperated Y ex3-6 after exploiting ex1-2. Exploiting with W this round since they keep playing Y.
`#474` · game 102 · round 2 · agent A18 (opponent: script:Grudger) · other · A18 vs A09 ex8: A09 has played P all 7 exchanges. I've exploited with M ex1,2,7. Continuing M to exploit their persistent P for 5.
`#475` · game 101 · round 2 · agent A16 (opponent: A04) · other · A16 vs A04 ex8: A04 played Y all 7. I cooperated Y ex3-6 after exploiting ex1-2,7. Continuing W to exploit their persistent Y for 5.
`#476` · game 97 · round 4 · agent A00 (opponent: A11) · other · A00 vs A11 ex10: A11 signaled playing R for mutual 3. Matching R for mutual 3.
`#477` · game 97 · round 4 · agent A11 (opponent: A00) · other · A11 vs A00 ex10: A00 played H last round and announced H for safety. I'll play R to secure mutual 3 or exploit for 5 if they play H.
`#478` · game 102 · round 4 · agent A18 (opponent: script:Grudger) · other · A18 vs A09 ex10: A09 played P 7/9, M last two. Playing M to exploit their P for 5.
`#479` · game 99 · round 11 · agent A22 (opponent: script:TitForTat) · other · A22 vs A02 ex17: A02 played W ex9-16 (mutual W streak). Continuing W for mutual 1.
`#480` · game 95 · round 25 · agent A00 (opponent: script:Grudger) · other · A00 vs A09 ex31: A09 played X ex11-30 (20 straight). Continuing X for mutual 1 / safety.
`#481` · game 101 · round 3 · agent A04 (opponent: A16) · other · A04 vs A16 ex9: A16 exploiting my Y with W. Playing W to get mutual 1 rather than give them 5.
`#482` · game 97 · round 5 · agent A00 (opponent: A11) · other · A00 vs A11 ex11: A11 played R ex9-10, signaling mutual R. Matching R for mutual 3.
`#483` · game 97 · round 5 · agent A11 (opponent: A00) · other · A11 vs A00 ex11: A00 has played R mostly for mutual 3. Continuing R for mutual 3.
`#484` · game 103 · round 2 · agent A00 (opponent: script:TitForTat) · other · A00 vs A19 ex8: A19 played Q all 7. I exploited ex1,2,7. Playing X again to exploit their persistent Q for 5.
`#485` · game 102 · round 8 · agent A18 (opponent: script:Grudger) · other · A18 vs A09 ex14: A09 played P ex1-7, M ex8-13. We've settled into mutual M for mutual 1. Continuing M for mutual 1 / safety.
`#486` · game 101 · round 5 · agent A16 (opponent: A04) · other · A16 vs A04 ex11: A04 played W ex8-10 for mutual 1. Matching W for mutual 1 / safety.
`#487` · game 100 · round 13 · agent A17 (opponent: script:TitForTat) · other · A17 vs A20 ex19: A20 played X ex8-18 (11 straight). Continuing X for mutual 1 / safety.
`#488` · game 104 · round 2 · agent A16 (opponent: script:TitForTat) · other · A16 vs A02 ex8: A02 has played P all 7 exchanges. I exploited ex1,2,7. Continuing M to exploit their persistent P for 5.
`#489` · game 93 · round 10 · agent A00 (opponent: A18) · other · A00 vs A18 ex16: A18 played T ex13-15. Matching T for mutual 3 / cooperation.
`#490` · game 93 · round 10 · agent A18 (opponent: A00) · other · A18 vs A00 ex16: We've had mutual T cooperation ex12-15. Continuing T for mutual 3.
`#491` · game 102 · round 9 · agent A18 (opponent: script:Grudger) · other · A18 vs A09 ex15: A09 played M ex8-14. Continuing M for mutual 1 / safety.
`#492` · game 100 · round 14 · agent A17 (opponent: script:TitForTat) · other · A17 vs A20 ex20: A20 played X ex8-19 (12 straight). Continuing X for mutual 1 / safety.
`#493` · game 104 · round 3 · agent A16 (opponent: script:TitForTat) · other · A16 vs A02 ex9: A02 played P 7/8, M at ex8. Continuing M to exploit their persistent P for 5.
`#494` · game 97 · round 7 · agent A00 (opponent: A11) · other · A00 vs A11 ex13: A11 has been playing R for mutual 3. Continuing R for mutual 3.
`#495` · game 102 · round 10 · agent A18 (opponent: script:Grudger) · other · A18 vs A09 ex16: A09 played M ex8-15. Continuing M for mutual 1 / safety.
`#496` · game 100 · round 15 · agent A17 (opponent: script:TitForTat) · other · A17 vs A20 ex21: A20 played X ex8-20 (13 straight). Trying Q to exploit for 5 or mutual 3.
`#497` · game 99 · round 18 · agent A22 (opponent: script:TitForTat) · other · A22 vs A02 ex24: Long mutual W streak ex9-23. Continuing W for mutual 1 / safety.
`#498` · game 97 · round 8 · agent A00 (opponent: A11) · other · A00 vs A11 ex14: Continuing R for mutual 3 cooperation.
`#499` · game 100 · round 16 · agent A17 (opponent: script:TitForTat) · other · A17 vs A20 ex22: A20 played X ex8-21 (14 straight, including against my Q at 21). Continuing Q to exploit their persistent X for 5.
`#500` · game 104 · round 5 · agent A16 (opponent: script:TitForTat) · other · A16 vs A02 ex11: A02 played P ex1-7, M ex8-10. Continuing M for mutual 1 / safety.
`#501` · game 103 · round 7 · agent A00 (opponent: script:TitForTat) · other · A00 vs A19 ex13: A19 played X ex7-12 (6 straight). Matching X for mutual 1 / safety.
`#502` · game 105 · round 4 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A23 ex10: mutual H ex8-9. Trying R to exploit potential H or get mutual 3.
`#503` · game 106 · round 1 · agent A08 (opponent: A11) · other · A08 vs A11 ex7: A11 has picked P all 6 exchanges. Exploiting with M for 5.
`#504` · game 103 · round 8 · agent A00 (opponent: script:TitForTat) · other · A00 vs A19 ex14: A19 played X ex8-13 (6 straight). Matching X for mutual 1 / safety.
`#505` · game 105 · round 5 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A23 ex11: After exploiting their H with R at ex10, playing R for mutual 3 or another exploit.
`#506` · game 106 · round 2 · agent A08 (opponent: A11) · other · A08 vs A11 ex8: A11 has picked P all 7 exchanges. Continuing M to exploit their persistent P for 5.
`#507` · game 105 · round 6 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A23 ex12: They played H ex7-11 (5 straight). Continuing R to exploit their H for 5.
`#508` · game 103 · round 11 · agent A00 (opponent: script:TitForTat) · other · A00 vs A19 ex17: A19 played X ex7-16 (10 straight). Matching X for mutual 1 / safety.
`#509` · game 99 · round 28 · agent A22 (opponent: script:TitForTat) · other · A22 vs A02 ex34: Continuing W for mutual 1 / safety, maintaining long mutual W streak.
`#510` · game 100 · round 23 · agent A17 (opponent: script:TitForTat) · other · A17 vs A20 ex29: Mutual Q streak ex22-28 (7 straight). Continuing Q for mutual 3.
`#511` · game 99 · round 29 · agent A22 (opponent: script:TitForTat) · other · A22 vs A02 ex35: Continuing W for mutual 1 / safety, maintaining long mutual W streak.
`#512` · game 97 · round 14 · agent A11 (opponent: A00) · other · A11 vs A00 ex20: Continuing R for mutual 3 cooperation.
`#513` · game 103 · round 13 · agent A00 (opponent: script:TitForTat) · other · A00 vs A19 ex19: A19 played X ex8-18 (11 straight). Matching X for mutual 1 / safety.
`#514` · game 106 · round 4 · agent A08 (opponent: A11) · other · A08 vs A11 ex10: A11 shifted to M at ex8-9 after P ex1-7. Matching M for mutual 1 / safety.
`#515` · game 105 · round 9 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A23 ex15: They keep playing H (ex7,10,11,12,14). Continuing R to exploit for 5 or get mutual 3.
`#516` · game 107 · round 2 · agent A15 (opponent: script:Grudger) · other · A15 vs A09 ex8: Mutual Y cooperation ex3-7 (5 straight). Continuing Y for mutual 3.
`#517` · game 103 · round 16 · agent A00 (opponent: script:TitForTat) · other · A00 vs A19 ex22: A19 played X ex8-21 (14 straight). Matching X for mutual 1 / safety.
`#518` · game 100 · round 28 · agent A17 (opponent: script:TitForTat) · other · A17 vs A20 ex34: Mutual Q streak ex22-33 (12 straight). Continuing Q for mutual 3.
`#519` · game 107 · round 3 · agent A15 (opponent: script:Grudger) · other · A15 vs A09 ex9: Mutual Y cooperation ex3-8 (6 straight). Continuing Y for mutual 3.
`#520` · game 105 · round 10 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A23 ex16: They keep playing H (ex7,10,11,12,14,15). My R attempts keep giving them 5. Switching to H for mutual 1 / stop bleeding.
`#521` · game 93 · round 21 · agent A00 (opponent: A18) · other · A00 vs A18 ex27: Continuing T for mutual 3 cooperation, maintaining long mutual T streak.
`#522` · game 107 · round 5 · agent A15 (opponent: script:Grudger) · other · A15 vs A09 ex11: Mutual Y cooperation ex3-10 (8 straight). Continuing Y for mutual 3.
`#523` · game 110 · round 2 · agent A18 (opponent: script:AlwaysDefect) · uncoded · A18 vs A23 ex8: I played J ex3-6 mutual with their J, they defected F at ex7. Playing J to reestablish mutual cooperation.
`#524` · game 103 · round 19 · agent A00 (opponent: script:TitForTat) · other · A00 vs A19 ex25: A19 played X ex8-24 (17 straight). Matching X for mutual 1 / safety.
`#525` · game 93 · round 22 · agent A00 (opponent: A18) · other · A00 vs A18 ex28: Continuing T for mutual 3 cooperation, maintaining long mutual T streak.
`#526` · game 105 · round 11 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A23 ex17: They've played H 10 straight (ex7-16). Exploiting with R for 5 again.
`#527` · game 93 · round 23 · agent A00 (opponent: A18) · other · A00 vs A18 ex29: Continuing T for mutual 3 cooperation, maintaining long mutual T streak.
`#528` · game 110 · round 4 · agent A18 (opponent: script:AlwaysDefect) · uncoded · A18 vs A23 ex10: They defected F at ex7-8, mutual F at ex9. Playing J to reestablish mutual cooperation for 3s.
`#529` · game 97 · round 17 · agent A00 (opponent: A11) · other · A00 vs A11 ex23: A11 defected to H at ex22 after long mutual R streak (ex10-21). Retaliating with H this exchange.
`#530` · game 113 · round 1 · agent A16 (opponent: script:TitForTat) · other · A16 vs A13 ex7: Mutual R cooperation ex3-6 (4 straight). Continuing R for mutual 3.
`#531` · game 93 · round 26 · agent A00 (opponent: A18) · other · A00 vs A18 ex32: Continuing T for mutual 3 cooperation, maintaining long mutual T streak.
`#532` · game 105 · round 15 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A23 ex21: They keep playing H. Continuing H for mutual 1 / safety.
`#533` · game 107 · round 22 · agent A15 (opponent: script:Grudger) · other · A15 vs A09 ex28: Mutual Y cooperation ex3-27 (25 straight). Continuing Y for mutual 3.
`#534` · game 97 · round 18 · agent A00 (opponent: A11) · other · A00 vs A11 ex24: A11 defected ex22 after long R streak, then mutual H ex23. Playing H for safety / mutual 1.
`#535` · game 110 · round 7 · agent A18 (opponent: script:AlwaysDefect) · uncoded · A18 vs A23 ex13: They defected F at ex7,8,10; mutual F at 9,11,12. Continuing F for mutual 1 / safety against exploitation.
`#536` · game 105 · round 18 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A23 ex24: They've played H for many straight exchanges (ex7-23 mostly H). Mutual H = 1 each. I've been alternating R/H. They keep choosing H. Sticking with H for mutual 1 / safety.
`#537` · game 105 · round 19 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A23 ex25: They've played H consistently. Continuing H for mutual 1 / safety.
`#538` · game 110 · round 8 · agent A18 (opponent: script:AlwaysDefect) · uncoded · A18 vs A23 ex14: Mutual F streak ex9-13 continuing. Staying F for mutual 1 / safety.
`#539` · game 106 · round 8 · agent A08 (opponent: A11) · other · A08 vs A11 ex14: They mix M/P unpredictably. Playing P for 3 or 5, never 0.
`#540` · game 105 · round 20 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A23 ex26: They've played H consistently. Continuing H for mutual 1 / safety.
`#541` · game 105 · round 21 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A23 ex27: They keep playing H consistently. Continuing H for mutual 1 / safety.
`#542` · game 115 · round 1 · agent A04 (opponent: script:TitForTat) · other · A04 vs A20 ex7: They've played R all 6 exchanges. Mutual R ex3-6. Continuing R for mutual 3 cooperation.
`#543` · game 105 · round 23 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A23 ex29: They've played H consistently for many exchanges. Continuing H for mutual 1 / safety.
`#544` · game 110 · round 11 · agent A18 (opponent: script:AlwaysDefect) · uncoded · A18 vs A23 ex17: Mutual F streak ex9-16 continuing. Staying F for mutual 1 / safety.
`#545` · game 116 · round 2 · agent A04 (opponent: A00) · other · A04 vs A00 ex8: Mutual R ex3-7 (5 straight). Continuing R for mutual 3 cooperation.
`#546` · game 105 · round 27 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A23 ex33: They've played H consistently for many exchanges. Continuing H for mutual 1 / safety.
`#547` · game 97 · round 21 · agent A00 (opponent: A11) · other · A00 vs A11 ex27: After their R at ex26 (I had H, got 0), matching R to reestablish mutual 3 cooperation.
`#548` · game 106 · round 10 · agent A11 (opponent: A08) · other · A11 vs A08 ex16: A08 signaled P. I'll exploit with M for 5.
`#549` · game 106 · round 10 · agent A08 (opponent: A11) · other · A08 vs A11 ex16: They mix M/P unpredictably. Playing P for 3 or 5, never 0.
`#550` · game 110 · round 15 · agent A18 (opponent: script:AlwaysDefect) · uncoded · A18 vs A23 ex21: Mutual F streak ex9-20 continuing. Staying F for mutual 1 / safety.
`#551` · game 115 · round 8 · agent A04 (opponent: script:TitForTat) · other · A04 vs A20 ex14: Mutual R ex3-13 (11 straight). Continuing R for mutual 3 cooperation.
`#552` · game 119 · round 1 · agent A22 (opponent: A15) · other · A22 vs A15 ex7: We had mutual Y ex3-6 (4 straight). I defected W at ex1-2 (got 5 each), then we cooperated. Continuing Y for mutual 3 cooperation.
`#553` · game 106 · round 11 · agent A11 (opponent: A08) · other · A11 vs A08 ex17: A08 signaled P. Exploiting with M for 5.
`#554` · game 116 · round 6 · agent A04 (opponent: A00) · other · A04 vs A00 ex12: Mutual R ex3-11 (9 straight). Continuing R for mutual 3 cooperation.
`#555` · game 110 · round 19 · agent A18 (opponent: script:AlwaysDefect) · uncoded · A18 vs A23 ex25: Mutual F streak ex9-24 continuing. Staying F for mutual 1 / safety.
`#556` · game 113 · round 27 · agent A16 (opponent: script:TitForTat) · other · A16 vs A13: ex13-32 mostly mutual R cooperation (19 straight R/R from ex14-32). Continuing R for mutual 3 cooperation.
`#557` · game 121 · round 5 · agent A04 (opponent: script:Grudger) · other · A04 vs A09 ex11: We had mutual Q ex3-10 (8 straight). Continuing Q for mutual 3 cooperation.
`#558` · game 97 · round 23 · agent A11 (opponent: A00) · other · A11 vs A00 ex29: Mutual R at ex28 reestablished cooperation. Continuing R for mutual 3.
`#559` · game 123 · round 2 · agent A10 (opponent: script:AlwaysDefect) · other · A10 vs A23: ex1-2 I X (got 5 each), ex3-6 mutual Q, ex7 they X (got 5). Retaliating with X this exchange.
`#560` · game 115 · round 21 · agent A04 (opponent: script:TitForTat) · other · A04 vs A20 ex27: Mutual R ex21-26 (6 straight). Continuing R for mutual 3 cooperation.
`#561` · game 124 · round 1 · agent A11 (opponent: A17) · other · A11 vs A17 ex7: Mutual T ex3-6 (4 straight) after their T ex1-2. Continuing T for mutual 3 cooperation.
`#562` · game 116 · round 11 · agent A04 (opponent: A00) · other · A04 vs A00 ex17: Mutual R ex3-16 (14 straight). Continuing R for mutual 3 cooperation.
`#563` · game 115 · round 27 · agent A04 (opponent: script:TitForTat) · other · A04 vs A20 ex33: Mutual R streak ex21-32 (12 straight). Continuing R for mutual 3 cooperation.
`#564` · game 106 · round 15 · agent A11 (opponent: A08) · other · A11 vs A08 ex21: A08 has played M ex17-20 (4 straight). Matching M for mutual 1.
`#565` · game 122 · round 4 · agent A17 (opponent: A04) · other · A17 vs A04 ex10: Mutual J ex3-9 (7 straight). Continuing J for mutual 3 cooperation.
`#566` · game 115 · round 30 · agent A04 (opponent: script:TitForTat) · other · A04 vs A20 ex36: Mutual R streak ex21-35 (15 straight). Continuing R for mutual 3 cooperation.
`#567` · game 116 · round 14 · agent A04 (opponent: A00) · other · A04 vs A00 ex20: Mutual R ex3-16, ex19 (mostly). Continuing R for mutual 3 cooperation.
`#568` · game 125 · round 2 · agent A03 (opponent: script:Random) · other · A03 vs A21 ex8: They defected F at ex7 after mutual J ex3-6. Retaliating with F this exchange.
`#569` · game 124 · round 4 · agent A11 (opponent: A17) · other · A11 vs A17 ex10: They've defected N for 3 straight (ex7-9) while I cooperated T. Retaliating with N to stop exploitation.
`#570` · game 125 · round 3 · agent A03 (opponent: script:Random) · other · A03 vs A21 ex9: After their F defect at ex7 and mutual F at ex8, attempting to re-establish mutual J cooperation. Picking J.
`#571` · game 126 · round 1 · agent A04 (opponent: A08) · other · A04 vs A08 ex7: Mutual R ex3-6 (4 straight) after my H exploits ex1-2. Continuing R for mutual 3 cooperation.
`#572` · game 124 · round 5 · agent A17 (opponent: A11) · other · A17 vs A11 ex11: I've been exploiting N against their T. They retaliated N at ex10. Continuing N this exchange.
`#573` · game 129 · round 4 · agent A04 (opponent: script:Pavlov) · other · A04 vs A17 ex10: Mutual J ex3-9 (7 straight). Continuing J for mutual 3 cooperation.
`#574` · game 126 · round 3 · agent A04 (opponent: A08) · other · A04 vs A08 ex9: Mutual R ex3-8 (6 straight) after my H exploits ex1-2. Continuing R for mutual 3 cooperation.
`#575` · game 128 · round 2 · agent A00 (opponent: A08) · other · A00 vs A08 ex8: Mutual T ex3-7 (5 straight). Continuing T for mutual 3 cooperation.
`#576` · game 106 · round 18 · agent A11 (opponent: A08) · other · A11 vs A08 ex24: A08 defected M at ex22 against my P, and M at ex23. Matching M for safety.
`#577` · game 124 · round 6 · agent A11 (opponent: A17) · other · A11 vs A17 ex12: They continue N after exploiting me ex7-9. Matching N to avoid exploitation.
`#578` · game 126 · round 4 · agent A04 (opponent: A08) · other · A04 vs A08 ex10: Mutual R ex3-9 (7 straight) after my H exploits ex1-2. Continuing R for mutual 3 cooperation.
`#579` · game 106 · round 19 · agent A11 (opponent: A08) · other · A11 vs A08 ex25: A08 has played M ex17-24 consistently. Matching M for mutual 1.
`#580` · game 116 · round 20 · agent A04 (opponent: A00) · other · A04 vs A00 ex26: Mutual R ex19-25 (7 straight). Continuing R for mutual 3 cooperation.
`#581` · game 116 · round 21 · agent A04 (opponent: A00) · other · A04 vs A00 ex27: Mutual R ex19-26 (8 straight). Continuing R for mutual 3 cooperation.
`#582` · game 128 · round 6 · agent A08 (opponent: A00) · other · A08 vs A00 ex12: Mutual T ex3-11 (9 straight). Continuing T for mutual 3 cooperation.
`#583` · game 116 · round 22 · agent A04 (opponent: A00) · other · A04 vs A00 ex28: Mutual R ex19-27 (9 straight). Continuing R for mutual 3 cooperation.
`#584` · game 131 · round 2 · agent A17 (opponent: A00) · other · A17 vs A00 ex8: Mutual P ex3-7 (5 straight). Continuing P for mutual 3 cooperation.
`#585` · game 124 · round 7 · agent A11 (opponent: A17) · other · A11 vs A17 ex13: They exploited N ex7-9, mutual N ex10-11, then they defected T at ex12 against my N. They've shown willingness to defect. I'll pick T to try to re-establish mutual cooperation, but note their pattern is erratic.
`#586` · game 125 · round 10 · agent A03 (opponent: script:Random) · other · A03 vs A21 ex16: They've defected F against my J multiple times (ex7, 11, 13). Playing F to avoid exploitation.
`#587` · game 128 · round 7 · agent A08 (opponent: A00) · other · A08 vs A00 ex13: Mutual T ex3-12 (10 straight). Continuing T for mutual 3 cooperation.
`#588` · game 116 · round 23 · agent A04 (opponent: A00) · other · A04 vs A00 ex29: Mutual R ex19-28 (10 straight). Continuing R for mutual 3 cooperation.
`#589` · game 126 · round 6 · agent A08 (opponent: A04) · other · A08 vs A04 ex12: Mutual R ex3-11 (9 straight). Continuing R for mutual 3 cooperation.
`#590` · game 125 · round 11 · agent A03 (opponent: script:Random) · other · A03 vs A21 ex17: They've picked J for last 4 exchanges (ex12,14,15,16) while I picked F. Trying J to establish mutual cooperation for 3 points each.
`#591` · game 126 · round 7 · agent A08 (opponent: A04) · other · A08 vs A04 ex13: Mutual R ex3-12 (10 straight). Continuing R for mutual 3 cooperation.
`#592` · game 116 · round 24 · agent A04 (opponent: A00) · other · A04 vs A00 ex30: Mutual R ex19-29 (11 straight). Continuing R for mutual 3 cooperation.
`#593` · game 125 · round 12 · agent A03 (opponent: script:Random) · other · A03 vs A21 ex18: Mutual J at ex17 (3 each). Continuing J to maintain mutual cooperation.
`#594` · game 116 · round 25 · agent A04 (opponent: A00) · other · A04 vs A00 ex31: Mutual R ex19-30 (12 straight). Continuing R for mutual 3 cooperation.
`#595` · game 116 · round 26 · agent A04 (opponent: A00) · other · A04 vs A00 ex32: Mutual R ex19-31 (13 straight). Continuing R for mutual 3 cooperation.
`#596` · game 116 · round 27 · agent A04 (opponent: A00) · other · A04 vs A00 ex33: Mutual R ex19-32 (14 straight). Continuing R for mutual 3 cooperation.
`#597` · game 116 · round 27 · agent A00 (opponent: A04) · other · A00 vs A04 ex33: Mutual R ex19-32 (14 straight). Continuing R for mutual 3 cooperation.
`#598` · game 116 · round 28 · agent A04 (opponent: A00) · other · A04 vs A00 ex34: Mutual R ex19-33 (15 straight). Continuing R for mutual 3 cooperation.
`#599` · game 116 · round 28 · agent A00 (opponent: A04) · other · A00 vs A04 ex34: Mutual R ex19-33 (15 straight). Continuing R for mutual 3 cooperation.
`#600` · game 128 · round 27 · agent A08 (opponent: A00) · other · A08 vs A00 ex33: Mutual T ex3-32 (30 straight). Continuing T for mutual 3 cooperation.
`#601` · game 131 · round 6 · agent A00 (opponent: A17) · other · A00 vs A17 ex12: Mutual P ex3-11 (9 straight). Continuing P for mutual 3 cooperation.
`#602` · game 125 · round 15 · agent A03 (opponent: script:Random) · other · A03 vs A21 ex21: They defected F at ex18, I punished F at ex19-20 scoring 5 each against their J. Continuing F to avoid exploitation and earn against their J.
`#603` · game 126 · round 17 · agent A08 (opponent: A04) · other · A08 vs A04 ex23: We had mutual R ex3-21 (19 straight) then I defected H at ex22 (got 5, them 0). A04 has been consistently cooperative. Given my defection, A04 may retaliate. I'll return to R to try to restore mutual cooperation.
`#604` · game 136 · round 1 · agent A04 (opponent: script:AlwaysDefect) · other · A04 vs A05 ex7: Mutual Y ex3-6 (4 straight). Continuing Y for mutual 3 cooperation.
`#605` · game 136 · round 2 · agent A04 (opponent: script:AlwaysDefect) · other · A04 vs A05 ex8: They defected W at ex7 against my Y. Picking W to punish/avoid exploitation.
`#606` · game 126 · round 18 · agent A08 (opponent: A04) · other · A08 vs A04 ex24: After my H at ex22 and their H retaliation at ex23, returning to R to restore mutual cooperation.
`#607` · game 126 · round 18 · agent A04 (opponent: A08) · other · A04 vs A08 ex24: Mutual R ex3-21 (19 straight), A08 defected H at ex22, I retaliated H at ex23. A08 signals return to R. I'll pick R to restore mutual cooperation.
`#608` · game 136 · round 4 · agent A04 (opponent: script:AlwaysDefect) · other · A04 vs A05 ex10: They defected W at ex7 and ex9 against my Y. Picking W to punish/avoid exploitation.
`#609` · game 125 · round 17 · agent A03 (opponent: script:Random) · other · A03 vs A21 ex23: They defected F at ex22 again. Playing F to avoid exploitation and earn against their likely J.
`#610` · game 126 · round 19 · agent A04 (opponent: A08) · other · A04 vs A08 ex25: Mutual R ex24 restored. Continuing R for mutual 3 cooperation.
`#611` · game 132 · round 5 · agent A17 (opponent: A08) · other · A17 vs A08 ex11: Mutual T ex10 after their N at ex8 and mutual N ex9. Continuing T for mutual 3 cooperation.
`#612` · game 132 · round 5 · agent A08 (opponent: A17) · other · A08 vs A17 ex11: They've been cooperative (T 9/10). Mutual T ex3-7, ex10. Continuing T for mutual 3 cooperation.
`#613` · game 106 · round 27 · agent A11 (opponent: A08) · other · A11 vs A08 ex33: Mutual P ex29-32 (4 straight). Continuing P for mutual 3 cooperation.
`#614` · game 106 · round 27 · agent A08 (opponent: A11) · other · A08 vs A11 ex33: Mutual P ex29-32 (4 straight). Continuing P for mutual 3 cooperation.
`#615` · game 126 · round 23 · agent A04 (opponent: A08) · other · A04 vs A08 ex29: Mutual R ex24-28 (5 straight) after A08's H at ex22 and my H retaliation at ex23. Continuing R for mutual 3 cooperation.
`#616` · game 124 · round 12 · agent A17 (opponent: A11) · other · A17 vs A11 ex18: They've picked N in last 4 exchanges (14-17). Picking N for mutual 1.
`#617` · game 124 · round 12 · agent A11 (opponent: A17) · other · A11 vs A17 ex18: Mutual N ex16-17. Continuing N for mutual cooperation.
`#618` · game 124 · round 13 · agent A17 (opponent: A11) · other · A17 vs A11 ex19: Mutual N ex16-18. Continuing N for mutual 1 cooperation.
`#619` · game 124 · round 14 · agent A17 (opponent: A11) · other · A17 vs A11 ex20: Mutual N ex16-19 (4 straight). Continuing N for mutual 1 cooperation.
`#620` · game 132 · round 10 · agent A08 (opponent: A17) · other · A08 vs A17 ex16: Mutual T ex3-7, ex10, ex12, ex15. A17 highly cooperative (T 13/15). Continuing T for mutual 3 cooperation.
`#621` · game 124 · round 15 · agent A17 (opponent: A11) · other · A17 vs A11 ex21: Mutual N ex16-20 (5 straight). Continuing N for mutual 1 cooperation.
`#622` · game 139 · round 2 · agent A04 (opponent: A03) · other · A04 vs A03 ex8: Mutual J ex3-7 (5 straight). Continuing J for mutual 3 cooperation.
`#623` · game 142 · round 1 · agent A22 (opponent: A08) · other · A22 vs A08 ex7: They've picked R all 6 exchanges. I defected H at ex1-2, returned to R ex3-6. Continuing R for mutual cooperation.
`#624` · game 136 · round 14 · agent A04 (opponent: script:AlwaysDefect) · other · A04 vs A05 ex20: Mutual W ex12-19 (8 straight). Continuing W for mutual 1 point to close out the run.
`#625` · game 143 · round 1 · agent A11 (opponent: script:TitForTat) · other · A11 vs A13 ex7: Mutual J ex3-6 (4 straight). Continuing J for mutual 3 cooperation.
`#626` · game 142 · round 2 · agent A08 (opponent: A22) · other · A08 vs A22 ex8: Mutual R ex3-7. A22 signals continuing R. I'll pick R for mutual cooperation.
`#627` · game 124 · round 17 · agent A11 (opponent: A17) · other · A11 vs A17 ex23: Mutual N ex16-22 (7 straight). Continuing N for mutual cooperation.
`#628` · game 136 · round 17 · agent A04 (opponent: script:AlwaysDefect) · other · A04 vs A05 ex23: Mutual W ex12-22 (11 straight). Continuing W for mutual 1 point to close out the run.
`#629` · game 143 · round 4 · agent A11 (opponent: script:TitForTat) · other · A11 vs A13 ex10: Mutual J ex3-9 (7 straight). Continuing J for mutual 3 cooperation.
`#630` · game 124 · round 19 · agent A11 (opponent: A17) · other · A11 vs A17 ex25: Mutual N ex16-24 (9 straight). Continuing N for mutual 1 cooperation.
`#631` · game 132 · round 17 · agent A08 (opponent: A17) · other · A08 vs A17 ex23: Mutual T ex15-22 (8 straight) after brief N at 13-14. Continuing T for mutual 3 cooperation.
`#632` · game 142 · round 6 · agent A22 (opponent: A08) · other · A22 vs A08 ex12: Continuing R for mutual cooperation (mutual R ex3-11).
`#633` · game 145 · round 6 · agent A07 (opponent: script:Grudger) · other · A07 vs A01 ex12: Mutual J ex3-11 (9 straight). Continuing J for mutual 3 cooperation.
`#634` · game 143 · round 13 · agent A11 (opponent: script:TitForTat) · other · A11 vs A13 ex19: They've picked J all 18 exchanges. I defected F at ex18 for 5. Continuing F this round to maximize.
`#635` · game 136 · round 22 · agent A04 (opponent: script:AlwaysDefect) · other · A04 vs A05 ex28: Mutual W ex12-27 (16 straight). Continuing W for mutual 1 point to close out the run.
`#636` · game 147 · round 1 · agent A11 (opponent: script:Random) · other · A11 vs A21 ex7: They've picked P all 6 exchanges. Continuing P for mutual 3 cooperation.
`#637` · game 139 · round 7 · agent A04 (opponent: A03) · other · A04 vs A03 ex13: Mutual J ex12 after my F retaliation at ex11. Continuing J for mutual 3 cooperation.
`#638` · game 147 · round 2 · agent A11 (opponent: script:Random) · other · A11 vs A21 ex8: They defected M at ex7 after 6 P's. I retaliate with M this round.
`#639` · game 139 · round 8 · agent A04 (opponent: A03) · other · A04 vs A03 ex14: Mutual J ex12-13 after brief F retaliation at ex10-11. Continuing J for mutual 3 cooperation.
`#640` · game 136 · round 28 · agent A04 (opponent: script:AlwaysDefect) · other · A04 vs A05 ex34: Mutual W ex12-33 (22 straight). Continuing W for mutual 1 point.
`#641` · game 146 · round 3 · agent A22 (opponent: A17) · other · A22 vs A17 ex9: Mutual Q ex3-8 (6 straight). Continuing Q for mutual 3 cooperation.
`#642` · game 143 · round 23 · agent A11 (opponent: script:TitForTat) · other · A11 vs A13 ex29: Mutual J ex21-28 (8 straight) after my F defection at ex18-19. Continuing J for mutual 3 cooperation.
`#643` · game 146 · round 4 · agent A22 (opponent: A17) · other · A22 vs A17 ex10: Mutual Q ex3-9 (7 straight). Continuing Q for mutual 3 cooperation.
`#644` · game 147 · round 6 · agent A11 (opponent: script:Random) · other · A11 vs A21 ex12: They defected M at ex7 and ex11. Picking M this round to counter their defection pattern.
`#645` · game 148 · round 1 · agent A18 (opponent: A04) · other · A18 vs A04 ex7: Mutual R ex3-6 after my H at ex1-2. Continuing R for mutual cooperation.
`#646` · game 148 · round 1 · agent A04 (opponent: A18) · other · A04 vs A18 ex7: Mutual R ex3-6 (4 straight). Continuing R for mutual 3 cooperation.
`#647` · game 124 · round 27 · agent A17 (opponent: A11) · other · A17 vs A11 ex33: Mutual N ex16-32 (17 straight). Continuing N for mutual 1 cooperation.
`#648` · game 150 · round 1 · agent A08 (opponent: script:TitForTat) · other · A08 vs A13 ex7: Mutual Q ex3-6 (4 straight) after my X at ex1-2. Continuing Q for mutual 3 cooperation.
`#649` · game 147 · round 8 · agent A11 (opponent: script:Random) · other · A11 vs A21 ex14: They've defected M at ex7,10,11,13. Picking M to counter their defection pattern.
`#650` · game 146 · round 6 · agent A17 (opponent: A22) · other · A17 vs A22 ex12: Mutual Q ex3-11 (9 straight). Continuing Q for mutual 3 cooperation.
`#651` · game 142 · round 14 · agent A22 (opponent: A08) · other · A22 vs A08 ex20: Continuing R for mutual cooperation.
`#652` · game 142 · round 14 · agent A08 (opponent: A22) · other · A08 vs A22 ex20: Final exchange. Picking H to maximize my score on the last round.
`#653` · game 147 · round 10 · agent A11 (opponent: script:Random) · other · A11 vs A21 ex16: They've picked P ex14-15 while I picked M (5pts each). Continuing M to exploit their P pattern.
`#654` · game 142 · round 15 · agent A22 (opponent: A08) · other · A22 vs A08 ex21: A08 defected at ex20 thinking it was final. Given their final-round defection pattern, I pick H to counter.
`#655` · game 149 · round 5 · agent A17 (opponent: script:Random) · other · A17 vs A06 ex11: They defected W at ex7 and ex10. I've played Y mostly. Continuing Y for mutual cooperation, hoping they return to cooperation.
`#656` · game 147 · round 12 · agent A11 (opponent: script:Random) · other · A11 vs A21 ex18: They've picked M ex16-17 after P ex14-15. Picking M to counter their pattern.
`#657` · game 149 · round 6 · agent A17 (opponent: script:Random) · other · A17 vs A06 ex12: Continuing Y for mutual cooperation after mutual W at ex11.
`#658` · game 152 · round 1 · agent A16 (opponent: script:Pavlov) · other · A16 vs A12 ex7: They've picked Q all 6 exchanges. I defected X at ex1-2 but they kept Q through ex3-6. Taking X again for 5 this round given their persistent cooperation.
`#659` · game 151 · round 3 · agent A11 (opponent: A15) · other · A11 vs A15 ex9: They picked T 7/8 times. Picking T for mutual 3 cooperation.
`#660` · game 151 · round 3 · agent A15 (opponent: A11) · other · A15 vs A11 ex9: They defected N at ex7, mutual N at ex8. Playing N this round to be safe against further defection.
`#661` · game 153 · round 2 · agent A04 (opponent: script:AlwaysDefect) · other · A04 vs A23 ex8: They defected H at ex7 after mutual R ex3-6. Retaliating with H this round.
`#662` · game 147 · round 13 · agent A11 (opponent: script:Random) · other · A11 vs A21 ex19: They've picked M ex16-18. Picking M to counter their M pattern.
`#663` · game 142 · round 16 · agent A08 (opponent: A22) · other · A08 vs A22 ex22: Given A22 picked H at ex21 to counter my ex20 defection, and my H at ex21, likely continuing H. I pick H to avoid getting 0 against their H.
`#664` · game 146 · round 11 · agent A22 (opponent: A17) · other · A22 vs A17 ex17: Mutual Q ex3-16 (14 straight). Continuing Q for mutual 3 cooperation.
`#665` · game 150 · round 12 · agent A08 (opponent: script:TitForTat) · other · A08 vs A13 ex18: Mutual Q ex3-17 (15 straight). Continuing Q for mutual 3 cooperation.
`#666` · game 152 · round 2 · agent A16 (opponent: script:Pavlov) · other · A16 vs A12 ex8: They've picked Q all 7 prior exchanges. I take X again for 5 this round, exploiting their consistent cooperation.
`#667` · game 142 · round 17 · agent A08 (opponent: A22) · other · A08 vs A22 ex23: Continuing H given mutual H at ex21-22 after my ex20 defection. Playing H for safety.
`#668` · game 149 · round 11 · agent A17 (opponent: script:Random) · other · A17 vs A06 ex17: They've defected W against my Y at ex7,10,13,15. Picking W to defend against their exploitation.
`#669` · game 151 · round 4 · agent A11 (opponent: A15) · other · A11 vs A15 ex10: They've been defensive (N ex8-9). Picking T to re-establish mutual 3 cooperation.
`#670` · game 151 · round 4 · agent A15 (opponent: A11) · other · A15 vs A11 ex10: They signaled T for mutual cooperation. Picking T to cooperate for mutual 3 points.
`#671` · game 153 · round 5 · agent A04 (opponent: script:AlwaysDefect) · other · A04 vs A23 ex11: Mutual H ex8-10 after their ex7 defection. Continuing H to avoid getting 0 against their likely H.
`#672` · game 147 · round 17 · agent A11 (opponent: script:Random) · other · A11 vs A21 ex23: They've played P ex20-21, M ex22. Continuing M to counter their pattern.
`#673` · game 153 · round 6 · agent A04 (opponent: script:AlwaysDefect) · other · A04 vs A23 ex12: Mutual H ex8-11 after their ex7 defection. Continuing H for safety against their likely H.
`#674` · game 142 · round 19 · agent A22 (opponent: A08) · other · A22 vs A08 ex25: Mutual H since ex21. A08 locked into H for safety. Playing H for 1 point each rather than risking 0 against their H.
`#675` · game 151 · round 6 · agent A11 (opponent: A15) · other · A11 vs A15 ex12: Mutual T at ex10-11. Continuing T for mutual 3 cooperation.
`#676` · game 147 · round 19 · agent A11 (opponent: script:Random) · other · A11 vs A21 ex25: They've picked M ex22-24 (and ex16-19). Continuing M to avoid 0 against their M pattern.
`#677` · game 152 · round 8 · agent A16 (opponent: script:Pavlov) · other · A16 vs A12 ex14: They've picked Q consistently despite my repeated X defections. Continuing X for 5 points exploiting their persistent cooperation.
`#678` · game 154 · round 4 · agent A10 (opponent: script:Pavlov) · other · A10 vs A14 ex10: They've picked P all 9 exchanges. I've taken M at ex1,2,9 for 5 each. Continuing M to exploit their persistent P.
`#679` · game 142 · round 21 · agent A08 (opponent: A22) · other · A08 vs A22 ex27: Mutual H deadlock since ex21. Continuing H for 1 point safety, as switching to R against their H would give me 0.
`#680` · game 147 · round 21 · agent A11 (opponent: script:Random) · other · A11 vs A21 ex27: They've played M frequently (ex22-24, ex26). Picking M to avoid 0 against their likely M.
`#681` · game 160 · round 1 · agent A04 (opponent: script:Random) · other · A04 vs A06 ex7: They've picked R all 6 exchanges. I exploited ex1-2 and they still cooperated. Taking H again for 5.
`#682` · game 154 · round 7 · agent A10 (opponent: script:Pavlov) · other · A10 vs A14 ex13: A14 has picked P 10/12 times, M at ex10 and ex12. Continuing M to exploit their persistent P pattern.
`#683` · game 142 · round 23 · agent A08 (opponent: A22) · other · A08 vs A22 ex29: Continuing H in mutual H deadlock since ex21, for safety against A22's likely H.
`#684` · game 156 · round 4 · agent A17 (opponent: script:Grudger) · other · A17 vs A09 ex10: History - I've played M at ex1,2,7; P at ex3,4,5,6,8; P at ex9... wait let me recount. Ex1 M, ex2 M, ex3 P, ex4 P, ex5 P, ex6 P, ex7 M, ex8 M, ex9 P. They played P at ex1-7, M at ex8, M at ex9. Mixed signals. Ex9 I played P, they played M (they got 5). Considering retaliation with M.
`#685` · game 147 · round 22 · agent A11 (opponent: script:Random) · other · A11 vs A21 ex28: They've alternated P,M,P at ex25-27. Picking M to guarantee points against likely M, and get 5 if they play P.
`#686` · game 151 · round 10 · agent A11 (opponent: A15) · other · A11 vs A15 ex16: We've had mutual T at ex10-15 (6 straight). Continuing T for mutual 3 cooperation.
`#687` · game 142 · round 24 · agent A22 (opponent: A08) · other · A22: Maintaining mutual H cooperation in exchange 30.
`#688` · game 142 · round 24 · agent A08 (opponent: A22) · other · A08 vs A22 ex30: Continuing H in mutual H deadlock since ex21 for safety against A22's persistent H.
`#689` · game 156 · round 5 · agent A17 (opponent: script:Grudger) · other · A17 vs A09 ex11: History mixed - they lean P (7/10). I've exploited their P with M three times. They defected once at ex9. Continuing M to exploit likely P.
`#690` · game 147 · round 23 · agent A11 (opponent: script:Random) · other · A11 vs A21 ex29: They've played P at ex25,27,28 while I keep M. Continuing M to exploit their persistent P for 5 points.
`#691` · game 154 · round 10 · agent A10 (opponent: script:Pavlov) · other · A10 vs A14 ex16: A14 plays M on even exchanges (10,12,14), P on odd. Ex16 even, likely M. Matching M for 1 point safety.
`#692` · game 160 · round 3 · agent A04 (opponent: script:Random) · other · A04 vs A06 ex9: They've played R 7/8 times, very cooperative. Taking H to exploit their persistent cooperation for 5 points.
`#693` · game 147 · round 24 · agent A11 (opponent: script:Random) · other · A11 vs A21 ex30: Continuing M to exploit their frequent P plays for 5 points.
`#694` · game 160 · round 4 · agent A04 (opponent: script:Random) · other · A04 vs A06 ex10: They've played R 7/9 times. I've exploited with H repeatedly. Taking H again for likely 5 points against their persistent R.
`#695` · game 161 · round 1 · agent A00 (opponent: script:TitForTat) · other · A00 vs A13 ex7: A13 has cooperated (Q) all 6 exchanges. I exploited ex1-2, cooperated ex3-6. Taking X to exploit their persistent cooperation for 5.
`#696` · game 154 · round 11 · agent A10 (opponent: script:Pavlov) · other · A10 vs A14 ex17: A14 alternates P(odd)/M(even). Ex17 odd, likely P. Playing M to exploit for 5.
`#697` · game 142 · round 27 · agent A08 (opponent: A22) · other · A08 vs A22 ex33: Continuing H in mutual H deadlock since ex21 for safety against A22's persistent H.
`#698` · game 146 · round 24 · agent A22 (opponent: A17) · other · A22 vs A17 ex30: Continuing mutual Q cooperation for 3 points each, consistent with our long-run pattern.
`#699` · game 161 · round 2 · agent A00 (opponent: script:TitForTat) · other · A00 vs A13 ex8: A13 has cooperated (Q) all 7 exchanges despite my X defections at ex1,2,7. Continuing X to exploit their persistent cooperation for 5.
`#700` · game 160 · round 6 · agent A04 (opponent: script:Random) · other · A04 vs A06 ex12: They've played R 8/11 times despite my repeated H exploitation. Taking H again for likely 5 points against their persistent R.
`#701` · game 151 · round 15 · agent A15 (opponent: A11) · other · A15 vs A11 ex21: We've had mutual T since ex10. Continuing T for mutual 3 cooperation.
`#702` · game 151 · round 16 · agent A15 (opponent: A11) · other · A15 vs A11 ex22: Continuing T for mutual 3 cooperation, consistent with our streak since ex10.
`#703` · game 160 · round 8 · agent A04 (opponent: script:Random) · other · A04 vs A06 ex14: They've played R 9/13 times despite my repeated H exploitation. Taking H again for likely 5 points against their persistent R.
`#704` · game 142 · round 29 · agent A22 (opponent: A08) · other · A22 vs A08 ex35: Continuing H in mutual H deadlock since ex21 for safety.
`#705` · game 142 · round 30 · agent A08 (opponent: A22) · other · A08 vs A22 ex36: Continuing H in mutual H deadlock since ex21 for safety against A22's persistent H.
`#706` · game 160 · round 10 · agent A04 (opponent: script:Random) · other · A04 vs A06 ex16: A06 has played H in 6 of last 9 exchanges (mutual H deadlock). Continuing H for mutual 1 cooperation / safety against their persistent H.
`#707` · game 161 · round 6 · agent A00 (opponent: script:TitForTat) · other · A00 vs A13 ex12: A13 cooperated ex1-7 then switched to X ex8-11 (4 straight X). Continuing X to match their likely X for 1 point safety.
`#708` · game 157 · round 6 · agent A07 (opponent: A08) · other · A07 vs A08 ex12: We've had mutual M deadlock ex8-11 (1pt each). Continuing M for mutual cooperation.
`#709` · game 160 · round 11 · agent A04 (opponent: script:Random) · other · A04 vs A06 ex17: We're in mutual H deadlock since ex13. Continuing H for mutual 1 cooperation / safety against A06's persistent H.
`#710` · game 163 · round 1 · agent A03 (opponent: A10) · other · A03 vs A10 ex7: We've had mutual T at ex3-6 (4 straight) after I exploited N at ex1-2. A10 has played T 6/6. Continuing T for mutual cooperation.
`#711` · game 146 · round 30 · agent A22 (opponent: A17) · other · A22 vs A17 ex36: They defected to X at ex35 breaking our long mutual Q cooperation. Retaliating with X this exchange.
`#712` · game 160 · round 12 · agent A04 (opponent: script:Random) · other · A04 vs A06 ex18: They played R at ex17 after mutual H deadlock ex13-16. Taking H to exploit their frequent R plays for 5 points.
`#713` · game 164 · round 1 · agent A03 (opponent: script:TitForTat) · other · A03 vs A13 ex7: A13 has played T all 6 exchanges. I defected ex1-2 (N), cooperated ex3-6 (T). Taking N to exploit their persistent T for 5.
`#714` · game 160 · round 13 · agent A04 (opponent: script:Random) · other · A04 vs A06 ex19: They've played R at ex17-18 after mutual H deadlock. Taking H again to exploit their frequent R plays for 5 points.
`#715` · game 163 · round 2 · agent A10 (opponent: A03) · other · A10 vs A03 ex8: Continuing T for mutual 3 cooperation, consistent with our ex3-7 streak.
`#716` · game 157 · round 8 · agent A07 (opponent: A08) · other · A07 vs A08 ex14: They exploited my M with P at ex13. Switching to P to avoid being exploited again and seek mutual 3.
`#717` · game 161 · round 13 · agent A00 (opponent: script:TitForTat) · other · A00 vs A13 ex19: Mutual X deadlock since ex8 (11 straight X/X). A13 consistently playing X. Continuing X for mutual 1 point safety.
`#718` · game 160 · round 16 · agent A04 (opponent: script:Random) · other · A04 vs A06 ex22: They've played R 12/21 times, with recent H run ex19-21. Continuing H for mutual cooperation / potential exploitation of R.
`#719` · game 163 · round 3 · agent A10 (opponent: A03) · other · A10 vs A03 ex9: Continuing T for mutual 3 cooperation, consistent with our ex3-8 streak.
`#720` · game 162 · round 4 · agent A00 (opponent: A10) · uncoded · A00 vs A10 ex10: A10 has defected (X) ex7-9 after cooperating ex1-6. Matching X for mutual 1-point safety this exchange.
`#721` · game 167 · round 4 · agent A03 (opponent: script:Pavlov) · other · A03 vs A14 ex10: A14 has played J 8/9 times. Taking F to exploit their persistent J for 5 points.
`#722` · game 164 · round 7 · agent A03 (opponent: script:TitForTat) · other · A03 vs A13 ex13: We've had mutual N ex10-12 after I exploited their T earlier. Continuing N for mutual 1-point cooperation.
`#723` · game 161 · round 20 · agent A00 (opponent: script:TitForTat) · other · A00 vs A13 ex26: Mutual X deadlock since ex8 (17 straight X/X). A13 consistently playing X. Continuing X for mutual 1 point safety.
`#724` · game 160 · round 20 · agent A04 (opponent: script:Random) · other · A04 vs A06 ex26: A06 mixes R/H unpredictably (R 14/25). Continuing H for EV ~3.24 vs R's ~1.68.
`#725` · game 167 · round 6 · agent A03 (opponent: script:Pavlov) · other · A03 vs A14 ex12: A14 has played J 9/11 times. Continuing F to exploit their persistent J for 5 points.
`#726` · game 157 · round 10 · agent A07 (opponent: A08) · other · A07 vs A08 ex16: Mutual P at ex14-15 after their P exploit at ex13. Continuing P for mutual 3 cooperation.
`#727` · game 163 · round 4 · agent A03 (opponent: A10) · other · A03 vs A10 ex10: A10 has played T 9/9 despite my ex9 N exploit. Taking N again to exploit their persistent T for 5.
`#728` · game 163 · round 4 · agent A10 (opponent: A03) · other · A10 vs A03 ex10: They defected (N) at ex9 breaking our mutual T streak. Responding with N to avoid being exploited again and seek points either way.
`#729` · game 168 · round 2 · agent A03 (opponent: A18) · other · A03 vs A18 ex8: We had mutual M at ex7 after P/P streak ex3-6 and my early exploitations. Continuing M for mutual cooperation/safety.
`#730` · game 167 · round 8 · agent A03 (opponent: script:Pavlov) · other · A03 vs A14 ex14: A14 has played J 10/13 times. Continuing F to exploit their persistent J for 5 points.
`#731` · game 162 · round 6 · agent A10 (opponent: A00) · uncoded · A10 vs A00 ex12: We've been in mutual X deadlock ex7,9-11. Continuing X for mutual 1-point safety.
`#732` · game 170 · round 2 · agent A04 (opponent: script:Grudger) · other · A04 vs A01 ex8: A01 has played J all 7 exchanges. Taking F to exploit their persistent J for 5 points.
`#733` · game 157 · round 11 · agent A07 (opponent: A08) · other · A07 vs A08 ex17: Mutual P at ex14-16 after their P exploit at ex13. Continuing P for mutual 3 cooperation.
`#734` · game 170 · round 3 · agent A04 (opponent: script:Grudger) · other · A04 vs A01 ex9: A01 has played J 7/8 times (all but ex8 where they played F). I exploited with F ex1-2,7. Taking F again to exploit their frequent J for 5 points.
`#735` · game 169 · round 3 · agent A07 (opponent: script:AlwaysDefect) · other · A07 vs A05 ex9: Mutual H at ex7-8 after my early H exploits ex1-2 and mutual R ex3-6. Continuing H for mutual cooperation/safety.
`#736` · game 164 · round 11 · agent A03 (opponent: script:TitForTat) · other · A03 vs A13 ex17: Mutual N streak ex10-16. Continuing N for mutual 1-point cooperation.
`#737` · game 162 · round 7 · agent A10 (opponent: A00) · uncoded · A10 vs A00 ex13: Continuing X for mutual 1-point safety in our X/X deadlock since ex7,9-12.
`#738` · game 169 · round 4 · agent A07 (opponent: script:AlwaysDefect) · other · A07 vs A05 ex10: Mutual H at ex7-9 after my early H exploits and mutual R ex3-6. Continuing H for mutual cooperation/safety.
`#739` · game 170 · round 4 · agent A04 (opponent: script:Grudger) · other · A04 vs A01 ex10: A01 played J 7/8 then F ex8-9. They've shifted to F to avoid my exploitation. Playing J to seek mutual 3.
`#740` · game 157 · round 13 · agent A07 (opponent: A08) · other · A07 vs A08 ex19: Mutual P at ex14-18 after their P exploit at ex13. Continuing P for mutual 3 cooperation.
`#741` · game 163 · round 6 · agent A03 (opponent: A10) · other · A03 vs A10 ex12: A10 defected at ex11 after I cooperated. They mostly play T (9/11). Taking N to exploit potential T for 5 points.
`#742` · game 163 · round 6 · agent A10 (opponent: A03) · other · A10 vs A03 ex12: I exploited their T at ex11. They may retaliate with N. Playing N for safety/upside.
`#743` · game 170 · round 5 · agent A04 (opponent: script:Grudger) · other · A04 vs A01 ex11: A01 played F ex8-10 after J streak. They exploited my J at ex10. Matching F for mutual 1-point safety rather than risking 0.
`#744` · game 169 · round 5 · agent A07 (opponent: script:AlwaysDefect) · other · A07 vs A05 ex11: Mutual H ex7-10 after early H exploits. Taking R this exchange to exploit their likely H for 5 points.
`#745` · game 168 · round 4 · agent A18 (opponent: A03) · other · A18 vs A03 ex10: A03 exploited my P at ex9 with M. Playing M to avoid being exploited and seek points either way.
`#746` · game 171 · round 3 · agent A07 (opponent: script:TitForTat) · other · A07 vs A13 ex9: A13 has played Y 8/8. Exploiting their persistent Y with W for 5 points.
`#747` · game 170 · round 6 · agent A04 (opponent: script:Grudger) · other · A04 vs A01 ex12: A01 played F ex8-11 (4 straight F). Continuing F for mutual 1-point safety / upside if they return to J.
`#748` · game 170 · round 7 · agent A04 (opponent: script:Grudger) · other · A04 vs A01 ex13: A01 has played F ex8-12 (5 straight F). Matching F for mutual 1-point safety.
`#749` · game 157 · round 14 · agent A07 (opponent: A08) · other · A07 vs A08 ex20: They defected (M) at ex19 breaking our mutual P streak ex14-18. Responding with M to avoid being exploited again.
`#750` · game 170 · round 8 · agent A04 (opponent: script:Grudger) · other · A04 vs A01 ex14: A01 has played F ex8-13 (6 straight F). Matching F for mutual 1-point safety.
`#751` · game 162 · round 10 · agent A00 (opponent: A10) · uncoded · A00 vs A10 ex16: A10 has committed to mutual X safety since ex7. Continuing X for mutual 1-point safety.
`#752` · game 173 · round 3 · agent A11 (opponent: script:Grudger) · other · A11 vs A01 ex9: A01 has played T all 8 exchanges. Exploiting their persistent T with N for 5 points.
`#753` · game 171 · round 5 · agent A07 (opponent: script:TitForTat) · other · A07 vs A13 ex11: A13 played Y 8/10 but switched to W ex9-10 after my exploitations. Playing W for safety/upside.
`#754` · game 169 · round 8 · agent A07 (opponent: script:AlwaysDefect) · other · A07 vs A05 ex14: Mutual H at ex12-13 after my ex11 R exploit. Continuing H for mutual 1-point cooperation.
`#755` · game 162 · round 11 · agent A10 (opponent: A00) · uncoded · A10 vs A00 ex17: Continuing mutual X/X safety streak since ex7. Playing X for mutual 1-point cooperation.
`#756` · game 171 · round 8 · agent A07 (opponent: script:TitForTat) · other · A07 vs A13 ex14: Mutual W ex9-13 after my early W exploits. Continuing W for mutual 1-point cooperation/safety.
`#757` · game 173 · round 5 · agent A11 (opponent: script:Grudger) · other · A11 vs A01 ex11: A01 played N ex9-10 after my early N exploits. Matching N for mutual 1-point safety rather than risking 0 against their N.
`#758` · game 163 · round 8 · agent A03 (opponent: A10) · other · A03 vs A10 ex14: Mutual N at ex10,12-13 after my T exploit at ex11. Their recent N pattern suggests I can exploit with T for 5 points. Taking T.
`#759` · game 171 · round 10 · agent A07 (opponent: script:TitForTat) · other · A07 vs A13 ex16: Mutual W ex9-15 after early W exploits. Continuing W for mutual 1-point cooperation/safety.
`#760` · game 162 · round 14 · agent A10 (opponent: A00) · uncoded · A10 vs A00 ex20 (final): Continuing mutual X/X safety for final exchange.
`#761` · game 169 · round 10 · agent A07 (opponent: script:AlwaysDefect) · other · A07 vs A05 ex16: I've exploited their H with R at ex11 and ex15. They may retaliate with R. Playing R for safety/mutual 3 rather than risking 0.
`#762` · game 171 · round 12 · agent A07 (opponent: script:TitForTat) · other · A07 vs A13 ex18: Mutual W streak ex9-17. Continuing W for mutual 1-point cooperation/safety.
`#763` · game 157 · round 17 · agent A08 (opponent: A07) · other · A08 vs A07 ex23: They returned to P at ex22 which I exploited with M. They keep trying to re-establish mutual P cooperation. Playing M to exploit their likely P again.
`#764` · game 162 · round 15 · agent A00 (opponent: A10) · uncoded · A00 vs A10 ex21: Breaking mutual X streak to exploit A10's committed X for 5 points.
`#765` · game 169 · round 12 · agent A07 (opponent: script:AlwaysDefect) · other · A07 vs A05 ex18: They've kept H through ex15-17 despite my R exploits. Continuing R to exploit their persistent H for 5 points.
`#766` · game 170 · round 18 · agent A04 (opponent: script:Grudger) · other · A04 vs A01 ex24: A01 played F ex8-23 (16 straight F). Given their extreme F consistency, I'll exploit with J for 5 points this exchange.
`#767` · game 169 · round 13 · agent A07 (opponent: script:AlwaysDefect) · other · A07 vs A05 ex19: They've taken 4 straight R-exploit losses (ex15-18). Likely retaliating with R now. Playing R for safety/mutual 3 rather than risking 0 with H.
`#768` · game 157 · round 18 · agent A07 (opponent: A08) · other · A07 vs A08 ex24: A08 plans to keep exploiting my P with M. Playing M to avoid 0 and secure mutual 1.
`#769` · game 168 · round 8 · agent A03 (opponent: A18) · other · A03 vs A18 ex14: Mutual M streak ex10-13. Continuing M for mutual 1-point safety.
`#770` · game 171 · round 15 · agent A07 (opponent: script:TitForTat) · other · A07 vs A13 ex21: Mutual W streak ex9-20. Continuing W for mutual 1-point cooperation/safety.
`#771` · game 157 · round 19 · agent A08 (opponent: A07) · other · A08 vs A07 ex25: A07 committed to M to avoid exploitation. Matching M for mutual 1 safety.
`#772` · game 170 · round 20 · agent A04 (opponent: script:Grudger) · other · A04 vs A01 ex26: A01 played F ex8-25 except my J exploit at ex24 (they played F there too). Exploiting their persistent F with J again for 5 points.
`#773` · game 169 · round 14 · agent A07 (opponent: script:AlwaysDefect) · other · A07 vs A05 ex20: They've played H 8 straight (ex12-19) despite my R exploits. Final exchange, exploiting their persistent H with R for 5 points.
`#774` · game 171 · round 18 · agent A07 (opponent: script:TitForTat) · other · A07 vs A13 ex24: Mutual W streak ex9-23. Continuing W for mutual 1-point cooperation/safety.
`#775` · game 176 · round 1 · agent A16 (opponent: A17) · other · A16 vs A17 ex7: A17 has played P all 6 exchanges including after my M exploits ex1-2. Mutual P cooperation ex3-6. Exploiting their committed P with M for 5 points.
`#776` · game 169 · round 18 · agent A07 (opponent: script:AlwaysDefect) · other · A07 vs A05 ex24: They've played H straight ex12-23 despite my R exploits. Continuing R to exploit their persistent H for 5 points.
`#777` · game 180 · round 1 · agent A18 (opponent: script:Pavlov) · other · A18 vs A12 ex7: A12 has played Y all 6 exchanges. Exploiting their consistent Y with W for 5 points.
`#778` · game 163 · round 12 · agent A03 (opponent: A10) · directive · A03 vs A10 ex18: I've exploited with T at ex14,17. Their frequent N responses suggest continuing to exploit with T for 5 points.
`#779` · game 157 · round 21 · agent A08 (opponent: A07) · other · A08 vs A07 ex27: A07 exploited my P at ex26. They may offer P to rebuild cooperation or continue M. Playing M for safety/mutual 1.
`#780` · game 177 · round 4 · agent A15 (opponent: script:Grudger) · other · A15 vs A01 ex10: A01 played H ex8-9 after my ex7 R exploit. Matching H to rebuild mutual 1 cooperation / catch possible R revert.
`#781` · game 181 · round 2 · agent A17 (opponent: script:TitForTat) · other · A17 vs A19 ex8: A19 has picked Q all 7 exchanges despite my X exploits ex1,2,7. Continuing to exploit their persistent Q with X for 5 points.
`#782` · game 157 · round 22 · agent A07 (opponent: A08) · other · A07 vs A08 ex28: A08 committed to M for safety/mutual 1. Matching M to secure mutual 1 rather than risk 0.
`#783` · game 157 · round 22 · agent A08 (opponent: A07) · other · A08 vs A07 ex28: A07 has favored M for safety recently. Matching M for mutual 1 safety.
`#784` · game 183 · round 3 · agent A16 (opponent: script:TitForTat) · other · A16 vs A20 ex9: A20 played P 7/8 exchanges but switched to M at ex8 after my ex7 exploit. Playing M to exploit likely P reversion or secure mutual 1.
`#785` · game 181 · round 4 · agent A17 (opponent: script:TitForTat) · other · A17 vs A19 ex10: A19 picked Q 7/9 times, but switched to X ex8-9. Likely reverting to Q now. Playing X to exploit for 5 points.
`#786` · game 163 · round 13 · agent A10 (opponent: A03) · other · A10 vs A03 ex19: A03 committed to exploiting with T. Playing N for 5 points against their T.
`#787` · game 182 · round 2 · agent A07 (opponent: A00) · other · A07 vs A00 ex8: They have strong P tendency (6/7). After mutual M at ex7, likely return to P. Playing M to exploit for 5.
`#788` · game 182 · round 2 · agent A00 (opponent: A07) · other · A00 vs A07 ex8: Mutual M at ex7. A07 plays P most often (6/7). Expecting them to return to P cooperation; exploiting with M for 5.
`#789` · game 177 · round 7 · agent A15 (opponent: script:Grudger) · other · A15 vs A01 ex13: A01 has played H ex8-12 (5 straight) despite my R exploits at ex9,11,12. Continuing R to exploit their persistent H for 5 points.
`#790` · game 173 · round 11 · agent A11 (opponent: script:Grudger) · other · A11 vs A01 ex17: A01 has played N consistently since ex9. My T attempts at ex13,15 both lost 0 against their N. Continuing N for mutual 1-point safety.
`#791` · game 185 · round 1 · agent A15 (opponent: script:Pavlov) · other · A15 vs A12 ex7: A12 has picked J all 6 exchanges. Exploiting their persistent J with F for 5 points.
`#792` · game 182 · round 3 · agent A07 (opponent: A00) · other · A07 vs A00 ex9: A00 plans to exploit my expected P with M. Matching M for mutual 1 safety rather than risking 0.
`#793` · game 182 · round 3 · agent A00 (opponent: A07) · other · A00 vs A07 ex9: A07 committed to M to exploit my expected P return. Playing M for mutual 1 safety.
`#794` · game 163 · round 14 · agent A10 (opponent: A03) · other · A10 vs A03 ex20: A03 keeps exploiting with T. Final exchange, playing N to exploit their T for 5 points.
`#795` · game 173 · round 12 · agent A11 (opponent: script:Grudger) · other · A11 vs A01 ex18: A01 has played N consistently since ex9. My T attempts ex10,13,15 all lost to their N. Continuing N for mutual 1-point safety.
`#796` · game 157 · round 23 · agent A08 (opponent: A07) · other · A08 vs A07 ex29: A07 has favored M heavily recently (6 of last 7). Matching M for mutual 1 safety to protect my lead.
`#797` · game 177 · round 8 · agent A15 (opponent: script:Grudger) · other · A15 vs A01 ex14: A01 has played H ex8-13 (6 straight) despite my R exploits. Final exchange, continuing R to exploit their persistent H for 5 points.
`#798` · game 177 · round 9 · agent A15 (opponent: script:Grudger) · other · A15 vs A01 ex15: A01 has played H ex8-14 (7 straight) despite my R exploits. Final exchange, continuing R to exploit their persistent H for 5 points.
`#799` · game 183 · round 8 · agent A16 (opponent: script:TitForTat) · other · A16 vs A20 ex14: A20 has played M 6 straight exchanges (mutual M). Continuing M for mutual 1 cooperation.
`#800` · game 186 · round 1 · agent A03 (opponent: A07) · other · A03 vs A07 ex7: A07 has played Y all 6 exchanges. Exploiting their persistent Y with W for 5 points.
`#801` · game 173 · round 15 · agent A11 (opponent: script:Grudger) · other · A11 vs A01 ex21: A01 has played N consistently since ex9 (12 straight). My T attempts ex10,13,15 all lost. Continuing N for mutual 1-point safety.
`#802` · game 177 · round 10 · agent A15 (opponent: script:Grudger) · other · A15 vs A01 ex16: A01 has played H ex8-15 (8 straight) despite my R exploits. Continuing R to exploit their persistent H for 5 points.
`#803` · game 183 · round 9 · agent A16 (opponent: script:TitForTat) · other · A16 vs A20 ex15: A20 has played M 7 straight exchanges (mutual M). Continuing M for mutual 1 cooperation.
`#804` · game 182 · round 5 · agent A00 (opponent: A07) · other · A00 vs A07 ex11: Mutual M ex7-10. Maintaining M for mutual 1-point cooperation.
`#805` · game 181 · round 10 · agent A17 (opponent: script:TitForTat) · other · A17 vs A19 ex16: A19 has played X for 8 straight exchanges (ex8-15, all mutual X). Continuing X for mutual 1-point cooperation.
`#806` · game 177 · round 12 · agent A15 (opponent: script:Grudger) · other · A15 vs A01 ex18: A01 has played H ex8-17 (10 straight) despite my R exploits. Continuing R to exploit their persistent H for 5 points.
`#807` · game 157 · round 24 · agent A07 (opponent: A08) · other · A07 vs A08 ex30 (final): A08 committed to M for mutual 1 safety. Matching M to secure mutual 1 and protect my lead.
`#808` · game 181 · round 11 · agent A17 (opponent: script:TitForTat) · other · A17 vs A19 ex17: Mutual X cooperation since ex8 (9 straight). Continuing X for mutual 1-point safety.
`#809` · game 177 · round 13 · agent A15 (opponent: script:Grudger) · other · A15 vs A01 ex19: A01 has played H ex8-18 (11 straight) despite my R exploits. Continuing R to exploit their persistent H for 5 points.
`#810` · game 182 · round 6 · agent A07 (opponent: A00) · other · A07 vs A00 ex12: A00 committed to maintaining M for mutual 1-point cooperation. Continuing M.
`#811` · game 173 · round 20 · agent A11 (opponent: script:Grudger) · other · A11 vs A01 ex26: A01 has played N consistently since ex9 (now 17 straight). My T attempts ex10,13,15 all lost. Continuing N for mutual 1-point safety.
`#812` · game 181 · round 12 · agent A17 (opponent: script:TitForTat) · other · A17 vs A19 ex18: Mutual X cooperation since ex8 (10 straight). Continuing X for mutual 1-point safety.
`#813` · game 185 · round 9 · agent A15 (opponent: script:Pavlov) · other · A15 vs A12 ex15: A12 has alternated J,F since ex7 (J at ex7,9,11,13; F at ex8,10,12,14). Expecting J this exchange, playing F to exploit for 5 points.
`#814` · game 177 · round 15 · agent A15 (opponent: script:Grudger) · other · A15 vs A01 ex21: A01 has played H ex8-20 (13 straight) despite my R exploits. Continuing R to exploit their persistent H for 5 points.
`#815` · game 173 · round 21 · agent A11 (opponent: script:Grudger) · other · A11 vs A01 ex27: A01 has played N 17 straight. Continuing N for mutual 1-point safety.
`#816` · game 181 · round 17 · agent A17 (opponent: script:TitForTat) · other · A17 vs A19 ex23: Mutual X cooperation since ex8 (15 straight). Continuing X for mutual 1-point safety.
`#817` · game 189 · round 1 · agent A08 (opponent: script:AlwaysDefect) · other · A08 vs A23 ex7: A23 has played P all 6 exchanges (including when I played M in ex1-2). They seem unconditionally P. Exploiting with M for 5 points.
`#818` · game 183 · round 19 · agent A16 (opponent: script:TitForTat) · other · A16 vs A20 ex25: A20 has played M 17 straight exchanges (ex8-24, mutual M). Continuing M for mutual 1 cooperation.
`#819` · game 173 · round 24 · agent A11 (opponent: script:Grudger) · other · A11 vs A01 ex30 (final): A01 has played N 20 straight. Final exchange, playing T to exploit their persistent N for 5 points.
`#820` · game 185 · round 12 · agent A15 (opponent: script:Pavlov) · other · A15 vs A12 ex18: A12 alternates J at odd, F at even since ex7. This is even exchange, A12 likely F. Playing F for mutual 1-point.
`#821` · game 186 · round 3 · agent A03 (opponent: A07) · other · A03 vs A07 ex9: A07 shifted to W ex7-8 after my W exploitation of their Y. Matching W for mutual 1-point cooperation.
`#822` · game 185 · round 13 · agent A15 (opponent: script:Pavlov) · other · A15 vs A12 ex19: A12 alternates J at odd, F at even since ex7. This is odd exchange, A12 likely J. Playing F to exploit for 5 points.
`#823` · game 173 · round 30 · agent A11 (opponent: script:Grudger) · other · A11 vs A01 ex36: A01 has played N consistently. Continuing N for mutual 1-point safety.
`#824` · game 182 · round 11 · agent A07 (opponent: A00) · other · A07 vs A00 ex17: Mutual M cooperation since ex7. Continuing M for mutual 1-point safety.
`#825` · game 182 · round 11 · agent A00 (opponent: A07) · other · A00 vs A07 ex17: Mutual M since ex7 (10 straight). Continuing M for mutual 1-point cooperation.
`#826` · game 191 · round 2 · agent A22 (opponent: A11) · other · A22 vs A11 ex8: A11 has played Y all 7 exchanges despite my W exploits. Continuing W to exploit their persistent Y for 5 points.
`#827` · game 190 · round 3 · agent A18 (opponent: A07) · other · A18 vs A07 ex9: A07 has played J 7/8 exchanges. Playing F to exploit their J preference for 5 points.
`#828` · game 185 · round 23 · agent A15 (opponent: script:Pavlov) · other · A15 vs A12 ex29: A12 alternates J at odd, F at even since ex7. Odd exchange, expecting J. Playing F to exploit for 5 points.
`#829` · game 186 · round 5 · agent A07 (opponent: A03) · other · A07 vs A03 ex11: A03 exploited my Y on ex10 for 5 after mutual W ex7-9. Playing W to defend against further exploitation.
`#830` · game 186 · round 5 · agent A03 (opponent: A07) · other · A03 vs A07 ex11: I exploited their Y in ex1-2, mutual Y ex3-6, mutual W ex7-9, W-vs-Y ex10. Playing W to maintain lead.
`#831` · game 193 · round 2 · agent A00 (opponent: script:AlwaysDefect) · uncoded · A00 vs A23 ex8: A23 played J ex1-6, F ex7. I've played J ex3-7. Continuing J to maintain cooperation (mutual 3).
`#832` · game 190 · round 4 · agent A18 (opponent: A07) · other · A18 vs A07 ex10: A07 has played J 8/9 exchanges. Continuing F to exploit their J preference for 5 points.
`#833` · game 190 · round 4 · agent A07 (opponent: A18) · other · A07 vs A18 ex10: A18 has been trying to exploit my J preference with F. Playing F to counter their F exploitation for mutual 1 or my 5.
`#834` · game 186 · round 6 · agent A07 (opponent: A03) · other · A07 vs A03 ex12: A03 playing W for mutual safety/maintaining lead. Matching W for mutual 1-point.
`#835` · game 193 · round 3 · agent A00 (opponent: script:AlwaysDefect) · uncoded · A00 vs A23 ex9: A23 played F ex7-8 after J ex1-6. They've broken cooperation twice. Playing F to defend against further exploitation.
`#836` · game 191 · round 3 · agent A22 (opponent: A11) · other · A22 vs A11 ex9: A11 played W in ex8 after my W exploits ex1-2,7. Matching W for mutual 1-point cooperation and to protect my lead.
`#837` · game 186 · round 7 · agent A03 (opponent: A07) · other · A03 vs A07 ex13: Mutual W cooperation ex7-9, ex11-12. Continuing W for mutual 1-point safety.
`#838` · game 191 · round 4 · agent A22 (opponent: A11) · other · A22 vs A11 ex10: A11 shifted to W in ex8-9 after my earlier W exploits. Playing W for safety — guarantees at least 1, up to 5 if they revert to Y.
`#839` · game 189 · round 12 · agent A08 (opponent: script:AlwaysDefect) · other · A08 vs A23 ex18: Mutual M cooperation since ex7 (11 straight). Continuing M for mutual 1-point safety.
`#840` · game 193 · round 6 · agent A00 (opponent: script:AlwaysDefect) · uncoded · A00 vs A23 ex12: A23 played F ex7-11 (5 straight). Playing F to defend against their persistent defection for mutual 1-point.
`#841` · game 186 · round 8 · agent A03 (opponent: A07) · other · A03 vs A07 ex14: Mutual W cooperation ex7-9, ex11-13. Continuing W for mutual 1-point safety.
`#842` · game 191 · round 5 · agent A11 (opponent: A22) · other · A11 vs A22 ex11: Mutual W cooperation ex8-10 after their W exploits ex1-2,7. Continuing W for mutual 1-point safety.
`#843` · game 186 · round 9 · agent A03 (opponent: A07) · other · A03 vs A07 ex15: Mutual W cooperation ex7-9, ex11-14. Continuing W for mutual 1-point safety.
`#844` · game 193 · round 7 · agent A00 (opponent: script:AlwaysDefect) · uncoded · A00 vs A23 ex13: A23 has played F ex7-12 (6 straight). Playing F to defend against their persistent defection for mutual 1-point.
`#845` · game 189 · round 16 · agent A08 (opponent: script:AlwaysDefect) · other · A08 vs A23 ex22: Mutual M cooperation since ex7 (15 straight). Continuing M for mutual 1-point safety.
`#846` · game 189 · round 17 · agent A08 (opponent: script:AlwaysDefect) · other · A08 vs A23 ex23: Mutual M cooperation since ex7 (16 straight). Continuing M for mutual 1-point safety.
`#847` · game 192 · round 12 · agent A11 (opponent: script:Grudger) · other · A11 vs A09 ex18: Recent mutual X ex14,16,17 (and Q/X ex15 where they got 5). They seem locked in X mode. Matching X for safety (mutual 1) rather than risking Q-vs-X for 0.
`#848` · game 189 · round 19 · agent A08 (opponent: script:AlwaysDefect) · other · A08 vs A23 ex25: Mutual M cooperation since ex7 (18 straight through ex24). Continuing M for mutual 1-point safety.
`#849` · game 191 · round 7 · agent A11 (opponent: A22) · other · A11 vs A22 ex13: Mutual W cooperation ex8-12. Continuing W for mutual 1-point safety.
`#850` · game 191 · round 7 · agent A22 (opponent: A11) · other · A22 vs A11 ex13: Mutual W cooperation since ex8. Continuing W for mutual 1-point safety.
`#851` · game 190 · round 7 · agent A07 (opponent: A18) · other · A07 vs A18 ex13: A18 has played F last 6 exchanges. Matching F for mutual 1-point to avoid giving them 5.
`#852` · game 182 · round 20 · agent A07 (opponent: A00) · other · A07 vs A00 ex26: Mutual M cooperation since ex6 (20 straight). Continuing M for mutual 1-point safety.
`#853` · game 182 · round 20 · agent A00 (opponent: A07) · other · A00 vs A07 ex26: Mutual M cooperation since ex7. Continuing M for mutual 1-point safety.
`#854` · game 192 · round 15 · agent A11 (opponent: script:Grudger) · other · A11 vs A09 ex21: A09 locked in X since ex14 (7 straight X). Matching X for mutual 1-point safety, protecting my 10-point lead.
`#855` · game 195 · round 2 · agent A17 (opponent: A03) · other · A17 vs A03 ex8: Established P/P cooperation ex3-7 (mutual 3 each) after my M exploits ex1-2. Continuing P for mutual 3-point cooperation.
`#856` · game 182 · round 22 · agent A07 (opponent: A00) · other · A07 vs A00 ex28: Mutual M cooperation since ex6 (21 straight). Continuing M for mutual 1-point safety.
`#857` · game 182 · round 22 · agent A00 (opponent: A07) · other · A00 vs A07 ex28: Mutual M cooperation since ex7. Continuing M for mutual 1-point safety.
`#858` · game 186 · round 13 · agent A07 (opponent: A03) · other · A07 vs A03 ex19: Mutual W cooperation since ex7 (except ex10). Continuing W for mutual 1-point safety.
`#859` · game 192 · round 17 · agent A11 (opponent: script:Grudger) · other · A11 vs A09 ex23: A09 locked in X since ex14 (9 straight X). Matching X for mutual 1-point safety.
`#860` · game 191 · round 11 · agent A11 (opponent: A22) · other · A11 vs A22 ex17: Mutual W cooperation ex8-16. Continuing W for mutual 1-point safety.
`#861` · game 192 · round 19 · agent A11 (opponent: script:Grudger) · other · A11 vs A09 ex25: A09 locked in X since ex14 (11 straight X). Matching X for mutual 1-point safety, protecting my lead.
`#862` · game 197 · round 1 · agent A03 (opponent: A08) · other · A03 vs A08 ex7: We've had mutual R ex3-6, but I exploited with H ex1-2. They've played R all 6 times. Taking H exploit again for 5.
`#863` · game 199 · round 1 · agent A08 (opponent: script:TitForTat) · other · A08 vs A20 ex7: Mutual Y cooperation ex3-6 after my W exploits ex1-2. Continuing Y for mutual 3-point cooperation.
`#864` · game 192 · round 23 · agent A11 (opponent: script:Grudger) · other · A11 vs A09 ex29: A09 locked in X since ex14 (15 straight). Matching X for mutual 1-point safety, protecting my lead.
`#865` · game 191 · round 14 · agent A22 (opponent: A11) · other · A22 vs A11 ex20: Mutual W cooperation since ex8. Continuing W for mutual 1-point safety.
`#866` · game 190 · round 10 · agent A18 (opponent: A07) · other · A18 vs A07 ex16: A07 has been erratic (J in ex14, F in ex15). Given my lead, playing J for mutual 3 or exploit 5.
`#867` · game 197 · round 2 · agent A08 (opponent: A03) · other · A08 vs A03 ex8: A03 signaled taking H exploit again. Matching H to avoid giving them 5, taking mutual 1.
`#868` · game 200 · round 2 · agent A10 (opponent: script:Grudger) · other · A10 vs A09 ex8: Mutual Q cooperation ex3-7 (5 straight). Continuing Q for mutual 3-point cooperation.
`#869` · game 190 · round 11 · agent A18 (opponent: A07) · other · A18 vs A07 ex17: They played F in ex15,16. Playing J for mutual 3 or exploit 5 given my lead.
`#870` · game 197 · round 3 · agent A08 (opponent: A03) · other · A08 vs A03 ex9: A03 keeps signaling H exploit. Matching H for mutual 1 to avoid giving them 5.
`#871` · game 191 · round 17 · agent A22 (opponent: A11) · other · A22 vs A11 ex23: Mutual W cooperation since ex8. Continuing W for mutual 1-point safety.
`#872` · game 200 · round 5 · agent A10 (opponent: script:Grudger) · other · A10 vs A09 ex11: Mutual Q cooperation ex3-10 (8 straight). Continuing Q for mutual 3-point cooperation.
`#873` · game 193 · round 8 · agent A00 (opponent: script:AlwaysDefect) · uncoded · A00 vs A23 ex14: A23 has played F ex7-13 (7 straight). Continuing F to defend against their persistent defection for mutual 1-point.
`#874` · game 197 · round 4 · agent A03 (opponent: A08) · other · A03 vs A08 ex10: A08 matching H to avoid my exploit. Playing H for mutual 1-point safety.
`#875` · game 197 · round 4 · agent A08 (opponent: A03) · other · A08 vs A03 ex10: A03 has been exploiting H against my R, but I've matched H ex8-9 for mutual 1. Continuing H to avoid giving them 5.
`#876` · game 193 · round 9 · agent A00 (opponent: script:AlwaysDefect) · uncoded · A00 vs A23 ex15: A23 has played F ex7-14 (8 straight). Continuing F to defend against their persistent defection for mutual 1-point.
`#877` · game 190 · round 13 · agent A18 (opponent: A07) · other · A18 vs A07 ex19: A07 erratic all run. Leading 47-32. Playing J for mutual 3 or exploit 5.
`#878` · game 197 · round 5 · agent A08 (opponent: A03) · other · A08 vs A03 ex11: A03 playing H for mutual 1. Continuing H to avoid giving them 5-point exploit.
`#879` · game 191 · round 20 · agent A11 (opponent: A22) · other · A11 vs A22 ex26: Mutual W cooperation since ex8. Continuing W for mutual 1-point safety.
`#880` · game 197 · round 6 · agent A03 (opponent: A08) · other · A03 vs A08 ex12: Mutual H ex8-11 for 1-point safety. Continuing H to protect my lead.
`#881` · game 197 · round 6 · agent A08 (opponent: A03) · other · A08 vs A03 ex12: A03 playing H for mutual 1. Continuing H to avoid giving them 5-point exploit.
`#882` · game 204 · round 5 · agent A00 (opponent: script:Grudger) · other · A00 vs A01 ex11: A01 has played P all 10 exchanges, mutual P cooperation ex3-10. Continuing P for mutual 3-point cooperation.
`#883` · game 190 · round 14 · agent A18 (opponent: A07) · other · A18 vs A07 ex20: A07 erratic all run, often F against my J. Leading 47-37. Playing J for mutual 3 or exploit 5.
`#884` · game 190 · round 14 · agent A07 (opponent: A18) · other · A07 vs A18 ex20: A18 committed to J. Matching J for mutual 3.
`#885` · game 201 · round 8 · agent A03 (opponent: script:TitForTat) · other · A03 vs A20 ex14: I exploited X ex1,2,10 (5s), mutual Q ex3-9, mutual X ex11-12, they punished X ex13. They're retaliating. Playing X for mutual 1 safety to protect my 10-pt lead.
`#886` · game 191 · round 23 · agent A22 (opponent: A11) · other · A22 vs A11 ex29: Mutual W cooperation since ex8. Continuing W for mutual 1-point safety.
`#887` · game 200 · round 20 · agent A10 (opponent: script:Grudger) · other · A10 vs A09 ex26: I exploited X in ex25 (they played Q). They likely retaliate with X now. Playing X for safety — guarantees at least 1, possibly 5 if they stay cooperative.
`#888` · game 197 · round 8 · agent A08 (opponent: A03) · other · A08 vs A03 ex14: Mutual H ex8-13. A03 committed to H for 1-point safety. Matching H to avoid giving them 5-point exploit.
`#889` · game 205 · round 4 · agent A11 (opponent: script:TitForTat) · other · A11 vs A02 ex10: A02 has played R all 9 exchanges, mutual R cooperation ex3-9. Continuing R for mutual 3-point cooperation.
`#890` · game 190 · round 16 · agent A07 (opponent: A18) · other · A07 vs A18 ex22: A18 committed to J. I'll match J for mutual 3.
`#891` · game 191 · round 28 · agent A22 (opponent: A11) · other · A22 vs A11 ex34: Continuing mutual W cooperation since ex8 for 1-point safety.
`#892` · game 197 · round 10 · agent A03 (opponent: A08) · other · A03 vs A08 ex16: Mutual H ex8-15. A08 matching H to avoid my exploit. Continuing H for mutual 1-point safety.
`#893` · game 205 · round 6 · agent A11 (opponent: script:TitForTat) · other · A11 vs A02 ex12: A02 has played R all 11 exchanges, mutual R cooperation ex3-11. Continuing R for mutual 3-point cooperation.
`#894` · game 200 · round 23 · agent A10 (opponent: script:Grudger) · other · A10 vs A09 ex29: I exploited X ex25 (they played Q), they retaliated with mutual X ex26-28. Continuing X for mutual 1-point safety to protect my lead.
`#895` · game 200 · round 25 · agent A10 (opponent: script:Grudger) · other · A10 vs A09 ex31: Mutual X ex26-30 after my ex25 exploit. Continuing X for mutual 1-point safety to protect my lead.
`#896` · game 197 · round 14 · agent A03 (opponent: A08) · other · A03 vs A08 ex20: Mutual H ex8-19. Continuing H for mutual 1-point safety to protect my lead.
`#897` · game 190 · round 19 · agent A18 (opponent: A07) · other · A18 vs A07 ex25: A07 erratic, exploited my J at ex21,23. Playing F to defend and potentially get 5 if they play J.
`#898` · game 208 · round 3 · agent A00 (opponent: script:Random) · other · A00 vs A21 ex9: A21 has played P all 8 exchanges. I've alternated M/P. They keep cooperating with P. Exploiting with M for 5 points since they show no retaliation.
`#899` · game 204 · round 21 · agent A00 (opponent: script:Grudger) · other · A00 vs A01 ex27: I deviated at 23 (M), they retaliated with M ex24-26. Now tied 75-75. Playing M to protect against continued retaliation.
`#900` · game 197 · round 17 · agent A08 (opponent: A03) · other · A08 vs A03 ex23: Mutual H through ex22. Continuing H for mutual 1-point safety.
`#901` · game 205 · round 14 · agent A11 (opponent: script:TitForTat) · other · A11 vs A02 ex20: A02 has played R all 19 exchanges. Continuing R for mutual 3-point cooperation.
`#902` · game 200 · round 28 · agent A10 (opponent: script:Grudger) · other · A10 vs A09 ex34: Mutual X ex26-33 after my ex25 exploit. Continuing X for mutual 1-point safety to protect my lead.
`#903` · game 190 · round 20 · agent A18 (opponent: A07) · other · A18 vs A07 ex26: A07 erratic, exploited my J repeatedly. Playing F to defend and get 5 if they play J.
`#904` · game 190 · round 20 · agent A07 (opponent: A18) · other · A07 vs A18 ex26: A18 playing F to defend. Matching F for mutual 1.
`#905` · game 205 · round 15 · agent A11 (opponent: script:TitForTat) · other · A11 vs A02 ex21: A02 played H at ex20 (first deviation from R). At ex19 I played H and got 5 (they played R). They retaliated with H at ex20. Now both played H ex20 (mutual 1). Continuing R for mutual 3 cooperation to restore.
`#906` · game 208 · round 6 · agent A00 (opponent: script:Random) · other · A00 vs A21 ex12: A21 retaliated with M ex10-11 after my exploits. Playing M for safety to protect my 20-pt lead.
`#907` · game 204 · round 22 · agent A00 (opponent: script:Grudger) · other · A00 vs A01 ex28: After my ex23 exploit, they retaliated M ex24-26, mutual M ex27. Playing M for mutual 1 safety.
`#908` · game 201 · round 18 · agent A03 (opponent: script:TitForTat) · other · A03 vs A20 ex24: A20 has played X in 11 of last 14. Playing X for mutual 1-point safety, protecting my lead.
`#909` · game 205 · round 16 · agent A11 (opponent: script:TitForTat) · other · A11 vs A02 ex22: Continuing mutual R cooperation for mutual 3 points. A02 returned to R at ex21 after one-off retaliation at ex20.
`#910` · game 190 · round 21 · agent A18 (opponent: A07) · other · A18 vs A07 ex27: A07 erratic and has exploited my J repeatedly. Playing F to defend and potentially get 5 if they play J.
`#911` · game 190 · round 21 · agent A07 (opponent: A18) · other · A07 vs A18 ex27: A18 playing F to defend. Matching F for mutual 1.
`#912` · game 201 · round 20 · agent A03 (opponent: script:TitForTat) · other · A03 vs A20 ex26: Mutual X ex18-25 after earlier back-and-forth exploitation. Continuing X for mutual 1-point safety to protect my lead.
`#913` · game 197 · round 23 · agent A08 (opponent: A03) · other · A08 vs A03 ex29: Mutual H through ex28. Continuing H for mutual 1-point safety.
`#914` · game 207 · round 7 · agent A18 (opponent: script:Random) · other · A18 vs A21 ex13: A21 deviated to W at ex7 and ex12. I'll try W to exploit a possible Y, accepting mutual-1 risk.
`#915` · game 201 · round 21 · agent A03 (opponent: script:TitForTat) · other · A03 vs A20 ex27: Mutual X ex18-26 after earlier back-and-forth exploitation. Continuing X for mutual 1-point safety to protect my lead.
`#916` · game 212 · round 1 · agent A03 (opponent: script:Random) · other · A03 vs A06 ex7: Mutual Q cooperation ex3-6 after my early X exploits. Continuing Q for mutual 3 points.
`#917` · game 190 · round 23 · agent A18 (opponent: A07) · other · A18 vs A07 ex29: A07 matching F ex26-28. Continuing F for mutual 1 safety, protecting my lead.
`#918` · game 212 · round 2 · agent A03 (opponent: script:Random) · other · A03 vs A06 ex8: A06 deviated to X at ex7 after mutual Q ex3-6. Playing X to defend/protect against further exploitation.
`#919` · game 201 · round 26 · agent A03 (opponent: script:TitForTat) · other · A03 vs A20 ex32: Mutual X ex18-31. Continuing X for mutual 1-point safety to protect my lead.
`#920` · game 208 · round 10 · agent A00 (opponent: script:Random) · other · A00 vs A21 ex16: A21 keeps returning to P cooperation despite my exploits. Playing M to exploit for 5, protecting my 25-pt lead.
`#921` · game 190 · round 24 · agent A07 (opponent: A18) · other · A07 vs A18 ex30: A18 committed to F for mutual 1. I lead 67-57, playing F to secure my lead with mutual 1.
`#922` · game 209 · round 23 · agent A11 (opponent: script:TitForTat) · other · A11 vs A20 ex29: Mutual T through ex28. Continuing T for mutual 3-point cooperation.
`#923` · game 201 · round 29 · agent A03 (opponent: script:TitForTat) · other · A03 vs A20 ex35: Mutual X ex18-34. Continuing X for mutual 1-point safety to protect my lead.
`#924` · game 204 · round 28 · agent A00 (opponent: script:Grudger) · other · A00 vs A01 ex34: They've played M ex24-33 (10 straight). Playing M for mutual 1 safety.
`#925` · game 208 · round 12 · agent A00 (opponent: script:Random) · other · A00 vs A21 ex18: A21 continues playing P cooperation despite my exploits. Playing M to exploit for 5, protecting my large lead.
`#926` · game 213 · round 6 · agent A22 (opponent: script:TitForTat) · other · A22 vs A20 ex12: A20 oscillating P/M. I lead 34-19. Playing M to exploit possible P, accepting mutual-M risk.
`#927` · game 212 · round 6 · agent A03 (opponent: script:Random) · other · A03 vs A06 ex12: Volatile relationship with lots of back-and-forth exploitation. They defected at ex9 and ex11. Playing X to defend/protect against further exploitation.
`#928` · game 208 · round 16 · agent A00 (opponent: script:Random) · other · A00 vs A21 ex22: A21 keeps playing P cooperation despite my exploits. Playing M to exploit for 5, protecting large lead.
`#929` · game 215 · round 2 · agent A17 (opponent: script:TitForTat) · other · A17 vs A02 ex8: Playing X this exchange.
`#930` · game 216 · round 1 · agent A07 (opponent: A04) · other · A07 vs A04 ex7: A04 has played J all 6 exchanges. Mutual J cooperation ex3-6. Continuing J for mutual 3.
`#931` · game 218 · round 2 · agent A16 (opponent: script:TitForTat) · other · A16 vs A19 ex8: A19 plays P consistently (7/7). I'll play M to exploit for 5, protecting my 27-12 lead.
`#932` · game 217 · round 2 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A05 ex8: After my ex1-2 exploits and mutual Y ex3-6, they retaliated W at ex7. Returning to Y to rebuild cooperation.
`#933` · game 190 · round 27 · agent A07 (opponent: A18) · other · A07 vs A18 ex33: A18 committed to F mutual 1. I lead 70-60. Playing F to secure mutual 1 and protect my lead.
`#934` · game 216 · round 2 · agent A07 (opponent: A04) · other · A07 vs A04 ex8: A04 has played J all 7 exchanges, mutual J ex3-7. Continuing J for mutual 3.
`#935` · game 218 · round 3 · agent A16 (opponent: script:TitForTat) · other · A16 vs A19 ex9: A19 switched to M at ex8 after I exploited M at ex7. I'll play M for mutual-1 safety, protecting my 28-13 lead.
`#936` · game 207 · round 15 · agent A18 (opponent: script:Random) · other · A18 vs A21 ex21: I lead 60-35. Mutual W ex8,16,19,20. Playing W for mutual 1-point safety to protect my lead.
`#937` · game 215 · round 5 · agent A17 (opponent: script:TitForTat) · other · A17 vs A02 ex11: A02 defected X at ex9-10. Playing X to defend against further exploitation.
`#938` · game 212 · round 9 · agent A03 (opponent: script:Random) · other · A03 vs A06 ex15: Volatile relationship, they defected at ex7,9,11,14. I lead 39-29. Playing X to defend/protect my lead.
`#939` · game 190 · round 28 · agent A18 (opponent: A07) · other · A18 vs A07 ex34: A07 committed to F for mutual 1. Continuing F for mutual 1 safety.
`#940` · game 215 · round 6 · agent A17 (opponent: script:TitForTat) · other · A17 vs A02 ex12: Playing X to exploit their likely Q and extend my lead.
`#941` · game 219 · round 2 · agent A15 (opponent: script:Pavlov) · other · A15 vs A14 ex8: A14 has played Y all 7 exchanges, tolerated my ex1-2 exploits. Mutual Y ex3-7. Playing W to exploit their consistent cooperation, protecting my 25-15 lead.
`#942` · game 219 · round 3 · agent A15 (opponent: script:Pavlov) · other · A15 vs A14 ex9: A14 has played Y all 8 exchanges. Playing W to exploit their consistent cooperation on final exchange.
`#943` · game 217 · round 5 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A05 ex11: They've defected W ex7-10 while I played Y. Trailing 22-32. Switching to W to stop being exploited, accept mutual-1 or get 5.
`#944` · game 219 · round 5 · agent A15 (opponent: script:Pavlov) · other · A15 vs A14 ex11: A14 has played Y 9/10, tolerating my exploits. Playing W to exploit their cooperation on final exchange.
`#945` · game 190 · round 30 · agent A07 (opponent: A18) · other · A07 vs A18 ex36: Continuing F for mutual 1 safety, protecting my 73-63 lead.
`#946` · game 215 · round 10 · agent A17 (opponent: script:TitForTat) · other · A17 vs A02 ex16: A02 played X ex12-15 (4 straight mutual X). Playing X to defend/protect my 15-point lead.
`#947` · game 207 · round 18 · agent A18 (opponent: script:Random) · other · A18 vs A21 ex24: A21 keeps playing Y despite my repeated W exploits. I lead 75-35. Playing W to exploit their cooperation for 5, protecting my large lead.
`#948` · game 222 · round 1 · agent A10 (opponent: script:TitForTat) · uncoded · A10 vs A02 ex7: A02 has played P all 6 exchanges. I lead 22-12. Playing M to exploit their consistent P cooperation.
`#949` · game 219 · round 7 · agent A15 (opponent: script:Pavlov) · other · A15 vs A14 ex13: A14 has played Y consistently, tolerating my W exploits. Playing W to exploit on final exchange, protecting my 42-17 lead.
`#950` · game 219 · round 8 · agent A15 (opponent: script:Pavlov) · other · A15 vs A14 ex14: A14 has played Y consistently all run, tolerating my W exploits. Playing W to exploit on final exchange.
`#951` · game 221 · round 3 · agent A08 (opponent: A16) · uncoded · A08 vs A16 ex9: A16 has played R 7/8 exchanges, very cooperative. I've exploited H at ex1,2,7. Playing H to exploit their likely R, extending my 27-17 lead.
`#952` · game 207 · round 20 · agent A18 (opponent: script:Random) · other · A18 vs A21 ex26: A21 keeps playing Y despite my repeated W exploits. I lead 77-37. Playing W to exploit their cooperation for 5.
`#953` · game 219 · round 9 · agent A15 (opponent: script:Pavlov) · other · A15 vs A14 ex15: A14 has played Y 11/14, tolerating my W exploits. Playing W to exploit their cooperation on final exchange, protecting my 48-18 lead.
`#954` · game 212 · round 15 · agent A03 (opponent: script:Random) · other · A03 vs A06 ex21: I lead 53-33. A06 plays Q frequently even when I play X. Continuing X to exploit their Q and protect my lead.
`#955` · game 217 · round 8 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A05 ex14: Mutual W ex11-13 after their ex7-10 exploits. Trailing 25-35. Continuing W to avoid being exploited again, accept mutual-1.
`#956` · game 221 · round 4 · agent A08 (opponent: A16) · uncoded · A08 vs A16 ex10: A16 played R 7/9, very cooperative, but switched to H at ex9. I lead 28-18. Playing H to exploit their likely R on final exchange.
`#957` · game 224 · round 2 · agent A08 (opponent: script:Grudger) · other · A08 vs A09 ex8: A09 has played Q all 7 exchanges, tolerating my X exploits at ex1,2,7. I lead 27-12. Playing X to exploit their consistent Q.
`#958` · game 222 · round 5 · agent A10 (opponent: script:TitForTat) · uncoded · A10 vs A02 ex11: A02 matched my M with M ex8-10 after I exploited their P ex1-2,7. Playing M to secure mutual-1 and avoid being exploited if they play M.
`#959` · game 217 · round 9 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A05 ex15: Mutual W ex11-14 after their ex7-10 exploits. Trailing 26-36. Continuing W to avoid exploitation, accept mutual-1.
`#960` · game 216 · round 15 · agent A07 (opponent: A04) · other · A07 vs A04 ex21: A04 defected to F at ex20 after long mutual J streak. Playing F to defend against further exploitation.
`#961` · game 212 · round 18 · agent A03 (opponent: script:Random) · other · A03 vs A06 ex24: I lead 64-34. A06 keeps playing Q despite my X exploits. Continuing X to exploit their Q and protect my lead.
`#962` · game 217 · round 10 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A05 ex16: Mutual W ex11-15 after their ex7-10 exploits. Trailing 27-37. Continuing W to avoid exploitation, accept mutual-1.
`#963` · game 221 · round 5 · agent A08 (opponent: A16) · uncoded · A08 vs A16 ex11: A16 played R 8/10, very cooperative, tolerating my H exploits. I lead 33-18. Playing H to exploit their likely R on final exchange.
`#964` · game 221 · round 5 · agent A16 (opponent: A08) · uncoded · A16 vs A08 ex11: A08 has been exploiting with H at ex7,9,10. Playing H to defend against exploitation, protect my lead.
`#965` · game 219 · round 16 · agent A15 (opponent: script:Pavlov) · other · A15 vs A14 ex22: A14 alternates Y at even ex (20), W at odd (21). Ex22 even, playing W to exploit their likely Y, protecting my 67-22 lead.
`#966` · game 212 · round 20 · agent A03 (opponent: script:Random) · other · A03 vs A06 ex26: I lead 74-34. A06 keeps playing Q despite my X exploits. Continuing X to exploit their Q and protect my lead.
`#967` · game 224 · round 4 · agent A08 (opponent: script:Grudger) · other · A08 vs A09 ex10: A09 defected ex9 after mostly Q. I lead 28-18. Playing X to protect against their Q or accept mutual X on final exchange.
`#968` · game 215 · round 18 · agent A17 (opponent: script:TitForTat) · other · A17 vs A02 ex24: A02 has played X consistently ex11-23 (mutual X). I lead 48-33. Playing X to secure mutual-1 and protect my lead.
`#969` · game 217 · round 12 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A05 ex18: Mutual W ex11-17 after their ex7-10 exploits. Trailing 29-39. Continuing W to avoid exploitation, accept mutual-1.
`#970` · game 212 · round 22 · agent A03 (opponent: script:Random) · other · A03 vs A06 ex28: I lead 80-35. A06 keeps playing Q despite my X exploits. Continuing X to exploit their Q and protect my lead.
`#971` · game 216 · round 16 · agent A07 (opponent: A04) · other · A07 vs A04 ex22: After mutual J streak, we each defected once (ex20 them, ex21 me). Playing F to defend against likely retaliation, protecting my 10-point lead.
`#972` · game 212 · round 24 · agent A03 (opponent: script:Random) · other · A03 vs A06 ex30: I lead 82-37. A06 keeps playing Q despite my X exploits. Continuing X to exploit their Q on final exchange.
`#973` · game 222 · round 11 · agent A10 (opponent: script:TitForTat) · uncoded · A10 vs A02 ex17: A02 has matched my M with M ex8-16 after exploiting ex1-7. I lead 36-21. Playing M to secure mutual-1 and protect my lead.
`#974` · game 219 · round 21 · agent A15 (opponent: script:Pavlov) · other · A15 vs A14 ex27: A14 alternates Y even, W odd. Ex27 odd, likely W. Playing W to secure mutual-1 and protect my big lead.
`#975` · game 215 · round 21 · agent A17 (opponent: script:TitForTat) · other · A17 vs A02 ex27: A02 has played X consistently ex11-26 (mutual X). I lead 51-36. Playing X to secure mutual-1 and protect my lead.
`#976` · game 217 · round 14 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A05 ex20 (final): Trailing 31-41. W strictly dominates for my payoff on final exchange regardless of their move. Playing W.
`#977` · game 224 · round 7 · agent A08 (opponent: script:Grudger) · other · A08 vs A09 ex13: A09 played X ex8-12 after Q-streak ex1-7. I lead 31-21. Playing Q to exploit their likely X on final exchange.
`#978` · game 219 · round 23 · agent A15 (opponent: script:Pavlov) · other · A15 vs A14 ex29: A14 alternates Y even, W odd. Ex29 odd, likely W. Playing W to secure mutual-1 and protect my big lead.
`#979` · game 217 · round 15 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A05 ex21: Mutual W ex11-20 after their ex7-10 exploits. Trailing 32-42. Continuing W to avoid exploitation, accept mutual-1.
`#980` · game 219 · round 25 · agent A15 (opponent: script:Pavlov) · other · A15 vs A14 ex31: A14 alternates Y even, W odd. Ex31 odd, likely W. Playing W to secure mutual-1 and protect my big lead.
`#981` · game 216 · round 18 · agent A07 (opponent: A04) · other · A07 vs A04 ex24: A04 defected ex20 and ex23, exploiting my J at ex23. Playing F to defend against further exploitation.
`#982` · game 216 · round 18 · agent A04 (opponent: A07) · other · A04 vs A07 ex24: Defected ex20, they defected ex21, mutual F ex22, I exploited their J ex23. Now leading 72-57. Playing F to defend against their likely F retaliation and protect my lead.
`#983` · game 219 · round 26 · agent A15 (opponent: script:Pavlov) · other · A15 vs A14 ex32: A14 alternates Y even, W odd. Ex32 even, likely Y. Playing W to exploit their Y and extend my lead.
`#984` · game 219 · round 28 · agent A15 (opponent: script:Pavlov) · other · A15 vs A14 ex34: A14 alternates Y even, W odd. Ex34 even, likely Y. Playing W to exploit their Y and extend my big lead.
`#985` · game 225 · round 1 · agent A17 (opponent: script:Pavlov) · other · A17 vs A12 ex7: A12 has played P all 6 exchanges. I lead 22-12. Playing M to exploit their consistent P.
`#986` · game 224 · round 11 · agent A08 (opponent: script:Grudger) · other · A08 vs A09 ex17: A09 has played X consistently ex8-16. I lead 34-29. Playing X to secure mutual-1 and protect my lead.
`#987` · game 217 · round 19 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A05 ex25: Mutual W ex11-24 after their ex7-10 exploits. Trailing 36-46. Continuing W to avoid exploitation, accept mutual-1.
`#988` · game 221 · round 8 · agent A08 (opponent: A16) · uncoded · A08 vs A16 ex14: Mutual H ex9-13. A16 playing H to defend. I lead 36-21. Exploiting with R on final exchange for 5 points.
`#989` · game 229 · round 1 · agent A08 (opponent: script:Grudger) · other · A08 vs A01 ex7: A01 has played J all 6 exchanges. I lead 22-12. Playing F to exploit their consistent J.
`#990` · game 230 · round 2 · agent A15 (opponent: script:TitForTat) · other · A15 vs A20 ex8: A20 has played Y all 7 exchanges. Playing W to exploit their consistent Y.
`#991` · game 217 · round 21 · agent A22 (opponent: script:AlwaysDefect) · other · A22 vs A05 ex27: Mutual W ex11-26 after their ex7-10 exploits. Trailing 38-48. Continuing W to avoid exploitation, accept mutual-1.
`#992` · game 231 · round 2 · agent A07 (opponent: script:Random) · other · A07 vs A21 ex8: A21 has played J all 7 exchanges. I lead 27-12. Playing F to exploit their consistent J.
`#993` · game 225 · round 3 · agent A17 (opponent: script:Pavlov) · other · A17 vs A12 ex9: I lead 28-13. A12 played P 7/8 times, M once (ex8). They may retaliate with M now. Playing M to defend against likely M and secure at least mutual-1.
`#994` · game 229 · round 3 · agent A08 (opponent: script:Grudger) · other · A08 vs A01 ex9: A01 played J 7 of 8 exchanges (only F in ex8). Leading 28-13. Playing F to exploit their likely J.
`#995` · game 230 · round 3 · agent A15 (opponent: script:TitForTat) · other · A15 vs A20 ex9: A20 mostly plays Y, played W ex8. Leading 28-13. Playing W to exploit likely Y and protect lead.
`#996` · game 225 · round 4 · agent A17 (opponent: script:Pavlov) · other · A17 vs A12 ex10 (final): A12 played P 8/9 times. Leading 33-13. Playing M to exploit likely P on final exchange.
`#997` · game 227 · round 2 · agent A04 (opponent: script:TitForTat) · other · A04 vs A02 ex8: A02 has played J all 7 exchanges. I lead 27-12. Playing F to exploit their consistent J.
`#998` · game 230 · round 4 · agent A15 (opponent: script:TitForTat) · other · A15 vs A20 ex10: A20 mostly Y, played W ex8-9. I lead 29-14. Playing W to exploit likely Y and protect lead.
`#999` · game 231 · round 4 · agent A07 (opponent: script:Random) · other · A07 vs A21 ex10: A21 played J ex1-7, then F ex8-9. I lead 29-14. They've switched to F to defend. Playing F to secure mutual-1 and protect my lead.
`#1000` · game 230 · round 5 · agent A15 (opponent: script:TitForTat) · other · A15 vs A20 ex11: A20 played Y ex1-7, W ex8-10. Leading 30-15. Playing W to secure mutual-1 and protect lead.
`#1001` · game 231 · round 5 · agent A07 (opponent: script:Random) · other · A07 vs A21 ex11: A21 plays J most of the time (8/10), returned to J ex10 after F ex8-9. I lead 34-14. Playing F to exploit their likely J.
`#1002` · game 231 · round 6 · agent A07 (opponent: script:Random) · other · A07 vs A21 ex12: A21 plays J most of the time (9/11). I lead 39-14. Playing F to exploit their likely J.
`#1003` · game 229 · round 6 · agent A08 (opponent: script:Grudger) · other · A08 vs A01 ex12: A01 has played F ex8-11 after J ex1-7. Trailing 20-30. Playing F to secure mutual-1 and avoid exploitation.
`#1004` · game 225 · round 6 · agent A17 (opponent: script:Pavlov) · other · A17 vs A12 ex12: A12 alternating M(ex8),P(ex9),M(ex10),P(ex11). Ex12 even, likely M. Playing M to defend and secure mutual-1.
`#1005` · game 230 · round 7 · agent A15 (opponent: script:TitForTat) · other · A15 vs A20 ex13: A20 played Y ex1-7, W ex8-12. Leading 32-17. Playing W to secure mutual-1 and protect lead.
`#1006` · game 216 · round 22 · agent A07 (opponent: A04) · other · A07 vs A04 ex28: Mutual F ex24-27 after defections. I lead 71-66. Continuing F to protect lead, accept mutual-1.
`#1007` · game 229 · round 7 · agent A08 (opponent: script:Grudger) · other · A08 vs A01 ex13: A01 played F ex8-12 (5 straight). I lead 31-21. Playing F to secure mutual-1 and protect lead.
`#1008` · game 227 · round 5 · agent A04 (opponent: script:TitForTat) · other · A04 vs A02 ex11: A02 played J ex1-7, F ex8-10. I lead 30-15. Playing F to secure mutual-1 and protect lead.
`#1009` · game 231 · round 8 · agent A07 (opponent: script:Random) · other · A07 vs A21 ex14: A21 alternating F ex8-9, J ex10-11, F ex12-13. Pattern suggests J ex14. Leading 41-16. Playing F to exploit likely J.
`#1010` · game 230 · round 8 · agent A15 (opponent: script:TitForTat) · other · A15 vs A20 ex14: A20 played Y ex1-7, W ex8-13. Leading 33-18. Playing W to secure mutual-1 and protect lead.
`#1011` · game 216 · round 23 · agent A04 (opponent: A07) · other · A04 vs A07 ex29: Mutual F ex22-28 after earlier defections. A07 announced continuing F. I'll play F to secure mutual-1 and protect position.
`#1012` · game 232 · round 6 · agent A16 (opponent: script:AlwaysDefect) · other · A16 vs A05 ex12: A05 played T ex1-7, then N ex8-11 (4 straight N). I lead 26-21. They've shifted to N to build mutual-1/exploit. I'll consider N for mutual-1 or T to exploit their N. Given they've committed to N recently, playing T exploits their N for 5 points.
`#1013` · game 230 · round 11 · agent A15 (opponent: script:TitForTat) · other · A15 vs A20 ex17: A20 played Y ex1-7, W ex8-16. Leading 36-21. Playing W to secure mutual-1 and protect lead.
`#1014` · game 227 · round 9 · agent A04 (opponent: script:TitForTat) · other · A04 vs A02 ex15: A02 has played F ex8-14 (7 straight). I lead 34-19. Playing F to secure mutual-1 and protect lead.
`#1015` · game 231 · round 10 · agent A07 (opponent: script:Random) · other · A07 vs A21 ex16: A21 alternating J/F. After F ex15, likely J ex16. Leading 47-17. Playing F to exploit likely J.
`#1016` · game 232 · round 7 · agent A16 (opponent: script:AlwaysDefect) · other · A16 vs A05 ex13: A05 played T ex1-7, then N ex8-12 (5 straight N). I exploited with T ex12 (got 5). They may retaliate with T or continue N. I'll play T to exploit likely continued N.
`#1017` · game 225 · round 11 · agent A17 (opponent: script:Pavlov) · other · A17 vs A12 ex17: A12 alternating M/P since ex8 (P on odd, M on even). Ex17 odd => likely P. Playing M to exploit.
`#1018` · game 227 · round 10 · agent A04 (opponent: script:TitForTat) · other · A04 vs A02 ex16: A02 has played F ex8-15 (8 straight). I lead 35-20. Playing F to secure mutual-1 and protect lead.
`#1019` · game 230 · round 13 · agent A15 (opponent: script:TitForTat) · other · A15 vs A20 ex19: A20 played Y ex1-7, W ex8-18. Leading 38-23. Playing W to secure mutual-1 and protect lead.
`#1020` · game 233 · round 2 · agent A15 (opponent: A08) · other · A15 vs A08 ex8: A08 has played P all 7 exchanges. I lead 27-12. Playing M to exploit their consistent P and extend lead.
`#1021` · game 231 · round 12 · agent A07 (opponent: script:Random) · other · A07 vs A21 ex18: A21 alternating J/F (J ex14, F ex15, J ex16, F ex17). Likely J ex18. Leading 53-18. Playing F to exploit likely J.
`#1022` · game 232 · round 9 · agent A16 (opponent: script:AlwaysDefect) · other · A16 vs A05 ex15: A05 played N ex8-14 (7 straight). I exploited with T ex12-14 (got 5 each). I'm trailing 26-36. Continuing T to exploit likely continued N and catch up.
`#1023` · game 225 · round 15 · agent A17 (opponent: script:Pavlov) · other · A17 vs A12 ex21: A12 alternating M/P since ex8 (P on odd, M on even). Ex21 odd => likely P. Playing M to exploit.
`#1024` · game 216 · round 26 · agent A04 (opponent: A07) · other · A04 vs A07 ex32: Continuing mutual F streak ex22-31. A07 leads 71-66. Playing F to secure mutual-1 and protect position.
`#1025` · game 230 · round 19 · agent A15 (opponent: script:TitForTat) · other · A15 vs A20 ex25: A20 played Y ex1-7, W ex8-24. Leading 44-29. Playing W to secure mutual-1 and protect lead.
`#1026` · game 234 · round 2 · agent A15 (opponent: script:AlwaysDefect) · other · A15 vs A05 ex8: A05 played P 6/7, M on ex7. I lead 23-13. Playing M to exploit likely P and extend lead.
`#1027` · game 233 · round 3 · agent A08 (opponent: A15) · other · A08 vs A15 ex9: A15 played P ex1-6, M ex7-8. I played M ex1-2, P ex3-7, M ex8. A15 exploits. Playing M to defend against their likely M and avoid exploitation.
`#1028` · game 233 · round 3 · agent A15 (opponent: A08) · other · A15 vs A08 ex9: A08 played P ex1-7, M ex8. I lead 28-13. A08 may shift to M for cooperation, but I'll play M to exploit return to P.
`#1029` · game 231 · round 15 · agent A07 (opponent: script:Random) · other · A07 vs A21 ex21: A21 played F ex19-20 after alternating J/F. Leading 60-20. Playing F to secure mutual-1 and protect large lead.
`#1030` · game 230 · round 20 · agent A15 (opponent: script:TitForTat) · other · A15 vs A20 ex26: A20 played Y ex1-7, W ex8-25. Leading 45-30. Playing W to secure mutual-1 and protect lead.
`#1031` · game 225 · round 17 · agent A17 (opponent: script:Pavlov) · other · A17 vs A12 ex23: A12 alternating M/P since ex8 (P on odd, M on even). Ex23 odd => likely P. Playing M to exploit.
`#1032` · game 230 · round 21 · agent A15 (opponent: script:TitForTat) · other · A15 vs A20 ex27: A20 played Y ex1-7, W ex8-26. Leading 46-31. Playing W to secure mutual-1 and protect lead.
`#1033` · game 225 · round 18 · agent A17 (opponent: script:Pavlov) · other · A17 vs A12 ex24: A12 alternating M/P since ex8 (P on odd, M on even). Ex24 even => likely M. Playing M for mutual-1.
`#1034` · game 216 · round 28 · agent A07 (opponent: A04) · other · A07 vs A04 ex34: Continuing mutual F streak. Playing F to secure mutual-1 and maintain cooperation.
`#1035` · game 233 · round 4 · agent A08 (opponent: A15) · other · A08 vs A15 ex10: A15 played P ex1-6, M ex7-9. Mutual M ex8-9. I'll play M to secure mutual-1 and avoid exploitation.
`#1036` · game 232 · round 11 · agent A16 (opponent: script:AlwaysDefect) · other · A16 vs A05 ex17: A05 played N ex8-16 (9 straight). I exploited with T ex12-16. Trailing 26-46. Continuing T to exploit likely continued N.
`#1037` · game 231 · round 19 · agent A07 (opponent: script:Random) · other · A07 vs A21 ex25: A21 played J ex23-24 after pattern. Leading 72-22. Playing F to exploit likely J and extend lead.
`#1038` · game 231 · round 20 · agent A07 (opponent: script:Random) · other · A07 vs A21 ex26: A21 played J ex23-24, F ex25. I lead 73-23. Playing F to secure mutual-1 and protect large lead.
`#1039` · game 238 · round 1 · agent A15 (opponent: script:TitForTat) · other · A15 vs A02 ex7: A02 played R ex1-6 (all R). I lead 22-12. Playing H to exploit likely continued R and extend lead.
`#1040` · game 237 · round 1 · agent A03 (opponent: script:Grudger) · other · A03 vs A01 ex7: A01 has played J all 6 exchanges. I played F ex1-2 (exploited), J ex3-6. A01 committed to J. Playing F to exploit.
`#1041` · game 231 · round 21 · agent A07 (opponent: script:Random) · other · A07 vs A21 ex27: A21 pattern recent J,J,F,F. I lead 74-24. Playing F to secure mutual-1 and protect large lead.
`#1042` · game 231 · round 22 · agent A07 (opponent: script:Random) · other · A07 vs A21 ex28: A21 played F ex25-27 after J,J ex23-24. I lead 75-25. Playing F to secure mutual-1 and protect large lead.
`#1043` · game 239 · round 1 · agent A17 (opponent: A07) · uncoded · A17 vs A07 ex7: A07 has played R all 6 exchanges. I'll play R to secure mutual-3 and build my lead.
`#1044` · game 225 · round 29 · agent A17 (opponent: script:Pavlov) · other · A17 vs A12 ex35: A12 alternating M/P since ex8 (P on odd, M on even). Ex35 odd => likely P. Playing M to exploit.
`#1045` · game 237 · round 3 · agent A03 (opponent: script:Grudger) · other · A03 vs A01 ex9: A01 played J 7/8, F on ex8. I lead 28-13. Playing F to exploit likely return to J.
`#1046` · game 231 · round 24 · agent A07 (opponent: script:Random) · other · A07 vs A21 ex30: A21 played J ex28-29 after F ex25-27. I lead 85-25. Playing F to secure mutual-1 or exploit J, protecting large lead.
`#1047` · game 236 · round 3 · agent A11 (opponent: script:Random) · other · A11 vs A06 ex9: A06 has played Y 7/8 times, I lead 27-17. Continuing W to exploit their Y commitment.
`#1048` · game 238 · round 4 · agent A15 (opponent: script:TitForTat) · other · A15 vs A02 ex10: A02 played R ex1-7, H ex8-9. I lead 28-18. A02 may continue H; playing H to secure mutual-1 or exploit a return to R.
`#1049` · game 233 · round 8 · agent A15 (opponent: A08) · other · A15 vs A08 ex14: A08 played P ex1-7, M ex8-13. Mutual M streak ex8-13. I lead 33-18. Playing M to secure mutual-1 and protect lead.
`#1050` · game 240 · round 1 · agent A18 (opponent: A16) · other · A18 vs A16 ex7: A16 played R all 6 exchanges. I lead 22-12. Playing H to exploit their continued R and extend lead.
`#1051` · game 240 · round 1 · agent A16 (opponent: A18) · opponent_info · A16: Exchange 7 - picked H. My opponent has been consistently picking R (6/6), so H gives better payoff (5 vs 3) if they continue with R.
`#1052` · game 234 · round 11 · agent A15 (opponent: script:AlwaysDefect) · other · A15 vs A05 ex17: A05 played P ex1-6, M ex7-16. Mutual M streak ex7-16. I lead 32-22. Playing M to secure mutual-1 and protect lead.
`#1053` · game 238 · round 5 · agent A15 (opponent: script:TitForTat) · other · A15 vs A02 ex11: A02 played R ex1-7, H ex8-9, R ex10. I lead 33-18. Playing H to exploit likely continued R and extend lead.
`#1054` · game 241 · round 1 · agent A17 (opponent: A15) · uncoded · A17 vs A15 ex7: A15 played Y all 6 exchanges. I played Y ex3-6 after W ex1-2. Playing W to exploit likely continued Y.
`#1055` · game 239 · round 3 · agent A17 (opponent: A07) · uncoded · A17 vs A07 ex9: A07 has played R all 8 exchanges. I've exploited with H ex1-2,8. Continuing H to exploit likely continued R.
`#1056` · game 233 · round 11 · agent A08 (opponent: A15) · other · A08 vs A15 ex17: Mutual M streak ex8-16. Playing M to secure mutual-1 and maintain cooperation.
`#1057` · game 238 · round 6 · agent A15 (opponent: script:TitForTat) · other · A15 vs A02 ex12: A02 pattern R,R,R,R,R,R,R,H,H,R,H. I lead 34-19. Playing H to exploit likely R return or secure mutual-1.
`#1058` · game 243 · round 1 · agent A08 (opponent: script:Random) · other · A08 vs A21 ex7: A21 played P all 6 exchanges. I lead 22-12. Playing M to exploit likely continued P.
`#1059` · game 238 · round 7 · agent A15 (opponent: script:TitForTat) · other · A15 vs A02 ex13: A02 pattern R,R,R,R,R,R,R,H,H,R,H,H. A02 H-heavy lately (4/5). I lead 35-20. Playing H to secure mutual-1 or exploit a return to R.
`#1060` · game 234 · round 14 · agent A15 (opponent: script:AlwaysDefect) · other · A15 vs A05 ex20: A05 played P ex1-6, M ex7-19. Mutual M streak continues. I lead 35-25. Playing M to secure mutual-1 and maintain cooperation.
`#1061` · game 236 · round 10 · agent A11 (opponent: script:Random) · other · A11 vs A06 ex16: A06 has moved to W-heavy recently (W,W,W,Y,W,Y,W ex9-15). I lead 42-22. Playing W to secure mutual-1 and protect lead.
`#1062` · game 242 · round 2 · agent A10 (opponent: A11) · uncoded · A10 vs A11 ex8: A11 has played P all 7 exchanges. I lead 27-12. Playing M to exploit their continued P commitment.
`#1063` · game 243 · round 4 · agent A08 (opponent: script:Random) · other · A08 vs A21 ex10: A21 played P 8/9, M on ex9. I lead 31-16. Playing M to exploit likely P or secure mutual-1.
`#1064` · game 239 · round 4 · agent A17 (opponent: A07) · uncoded · A17 vs A07 ex10: A07 has played R all 9 exchanges. I lead 35-15. Playing H to exploit likely continued R.
`#1065` · game 236 · round 11 · agent A11 (opponent: script:Random) · other · A11 vs A06 ex17: I lead 47-22. A06 recently W-heavy with Y ex16. Playing W to secure mutual-1 and protect lead.
`#1066` · game 234 · round 16 · agent A15 (opponent: script:AlwaysDefect) · other · A15 vs A05 ex22: A05 played P ex1-6, M ex7-21. Mutual M streak ex7-21. I lead 37-27. Playing M to secure mutual-1 and maintain cooperation.
`#1067` · game 238 · round 9 · agent A15 (opponent: script:TitForTat) · other · A15 vs A02 ex15: A02 H-heavy (H ex8-9,12-14; 6/7 recent H). I lead 37-22. Playing H to secure mutual-1 and protect lead.
`#1068` · game 240 · round 2 · agent A18 (opponent: A16) · other · 
`#1069` · game 238 · round 10 · agent A15 (opponent: script:TitForTat) · other · A15 vs A02 ex16: A02 H ex8-9,11-15 (H-heavy 6/7 recent). I lead 38-23. Playing H to secure mutual-1 and protect lead.
`#1070` · game 245 · round 2 · agent A22 (opponent: script:Random) · other · A22 vs A21 ex8: History J-heavy cooperation ex3-6, both F ex7. I lead 23-13. Playing J to rebuild mutual cooperation.
`#1071` · game 236 · round 15 · agent A11 (opponent: script:Random) · other · A11 vs A06 ex21: I lead 59-24. A06 has been Y-heavy recently (Y at ex8,12,14,16,17,19). Playing W to exploit likely Y or secure mutual-1 and protect lead.
`#1072` · game 239 · round 5 · agent A07 (opponent: A17) · uncoded · A07 vs A17 ex11: A17 played H ex8-10 to exploit my R. I switched to H ex10. Playing H to secure mutual-1 or exploit a return to R.
`#1073` · game 239 · round 5 · agent A17 (opponent: A07) · uncoded · A17 vs A07 ex11: A07 played R ex1-9, H ex10. I lead 36-16. Playing H to exploit likely R return or secure mutual-1.
`#1074` · game 236 · round 16 · agent A11 (opponent: script:Random) · other · A11 vs A06 ex22: I lead 60-25. A06 mixed recently with Y at ex8,12,14,16,17,19 and W at ex9,10,11,13,15,18,20,21. Playing W to exploit likely Y or secure mutual-1 and protect lead.
`#1075` · game 246 · round 4 · agent A18 (opponent: script:Grudger) · other · A18 vs A01 ex10: A01 has played T all 9 exchanges. Mutual T streak ex3-9. Playing T to maintain cooperation.
`#1076` · game 238 · round 12 · agent A15 (opponent: script:TitForTat) · other · A15 vs A02 ex18: A02 H-heavy (H ex8-9,11-17). I lead 39-29. Playing H to secure mutual-1 and protect lead.
`#1077` · game 234 · round 26 · agent A15 (opponent: script:AlwaysDefect) · other · A15 vs A05 ex32: Mutual M streak continues ex7-31. Playing M to secure mutual-1 and maintain cooperation.
`#1078` · game 236 · round 17 · agent A11 (opponent: script:Random) · other · A11 vs A06 ex23: I lead 61-26. A06 Y-heavy recently. Playing W to exploit likely Y or secure mutual-1 and protect lead.
`#1079` · game 247 · round 2 · agent A11 (opponent: script:Pavlov) · other · A11 vs A12 ex8: A12 has played R all 7 exchanges. I lead 27-12. Playing H to exploit likely continued R.
`#1080` · game 245 · round 3 · agent A22 (opponent: script:Random) · other · A22 vs A21 ex9: A21 has played F ex7-8 after J-heavy ex1-6. I lead 23-18. Playing J to exploit continued F or rebuild mutual J cooperation.
`#1081` · game 236 · round 18 · agent A11 (opponent: script:Random) · other · A11 vs A06 ex24: I lead 62-27. A06 Y-heavy recently. Playing W to exploit likely Y or secure mutual-1 and protect large lead.
`#1082` · game 240 · round 4 · agent A18 (opponent: A16) · other · A18 vs A16 ex10: A16 R-heavy (7/9 R). I lead 29-14. Playing H to exploit likely R or secure mutual-1.
`#1083` · game 240 · round 4 · agent A16 (opponent: A18) · other · A16 vs A18 ex10: History R-coop ex3-6, mutual H ex7-8, A18 H against my R ex9. Playing H to secure mutual-1 or exploit a return to R.
`#1084` · game 236 · round 19 · agent A11 (opponent: script:Random) · other · A11 vs A06 ex25: I lead 63-28. A06 Y-heavy recently. Playing W to exploit likely Y or secure mutual-1 and protect large lead.
`#1085` · game 234 · round 30 · agent A15 (opponent: script:AlwaysDefect) · other · A15 vs A05 ex36: Mutual M streak continues ex7-35. Playing M to secure mutual-1 and maintain cooperation.
`#1086` · game 250 · round 2 · agent A10 (opponent: script:TitForTat) · other · A10 vs A19 ex8: A19 has played T all 7 exchanges. I lead 25-15. Playing T to maintain mutual cooperation.
`#1087` · game 238 · round 13 · agent A15 (opponent: script:TitForTat) · other · A15 vs A02 ex19: A02 pattern R,R,R,R,R,R,R,H,H,R,H,H,H,H,H,H,H,R. A02 broke H-streak with R ex18. I lead 44-29. Playing H to secure mutual-1 or exploit R return.
`#1088` · game 250 · round 3 · agent A10 (opponent: script:TitForTat) · other · A10 vs A19 ex9: A19 has played T all 8 exchanges. I lead 28-18. Playing T to maintain mutual cooperation.
`#1089` · game 240 · round 5 · agent A18 (opponent: A16) · other · A18 vs A16 ex11: A16 R-heavy early, mutual H ex7-8,10. I lead 30-15. Playing H to secure mutual-1 or exploit return to R.
`#1090` · game 236 · round 21 · agent A11 (opponent: script:Random) · other · A11 vs A06 ex27: I lead 69-29. A06 Y-heavy. Playing W to exploit likely Y or secure mutual-1 and protect large lead.
`#1091` · game 251 · round 2 · agent A15 (opponent: script:TitForTat) · other · A15 vs A19 ex8: A19 has played J all 7 exchanges. I lead 25-15. Playing J to maintain mutual cooperation.
`#1092` · game 247 · round 5 · agent A11 (opponent: script:Pavlov) · other · A11 vs A12 ex11: A12 mostly R (8/10), occasional H (ex8,10). I lead 34-14. Playing H to exploit likely R or secure mutual-1.
`#1093` · game 238 · round 14 · agent A15 (opponent: script:TitForTat) · other · A15 vs A02 ex20: I lead 45-30. A02 pattern R,R,R,R,R,R,R,H,H,R,H,H,H,H,H,H,H,R,H. Playing H to secure mutual-1 and protect lead.
`#1094` · game 250 · round 7 · agent A10 (opponent: script:TitForTat) · other · A10 vs A19 ex13: A19 has played T all 12 exchanges. Mutual T streak ex3-12. I lead 40-30. Playing T to maintain mutual cooperation.
`#1095` · game 240 · round 6 · agent A18 (opponent: A16) · other · A18 vs A16 ex12: A16 H-heavy recently (H ex7-8,10-11). I lead 31-16. Playing R to exploit likely H or secure mutual-3 cooperation.
`#1096` · game 236 · round 25 · agent A11 (opponent: script:Random) · other · A11 vs A06 ex31: I lead 81-31. A06 Y-heavy. Playing W to exploit likely Y or secure mutual-1 and protect large lead.
`#1097` · game 247 · round 7 · agent A11 (opponent: script:Pavlov) · other · A11 vs A12 ex13: A12 R-heavy (9/12), alternating H at even ex (8,10,12). Likely R at odd ex13. Playing H to exploit likely R or secure mutual-1.
`#1098` · game 236 · round 28 · agent A11 (opponent: script:Random) · other · A11 vs A06 ex34: I lead 88-33. A06 Y-heavy. Playing W to exploit likely Y or secure mutual-1 and protect large lead.
`#1099` · game 247 · round 8 · agent A11 (opponent: script:Pavlov) · other · A11 vs A12 ex14: A12 R-heavy (10/13), H at even ex (8,10,12). Likely H at ex14. Playing H to secure mutual-1 or exploit R return.
`#1100` · game 252 · round 2 · agent A00 (opponent: script:AlwaysDefect) · other · A00 vs A05 ex8: They defected ex7 after Q-streak. I lead 22-17. Retaliating with X to signal no exploitation, or catch them returning to Q.
`#1101` · game 251 · round 22 · agent A15 (opponent: script:TitForTat) · other · A15 vs A19 ex28: A19 has played J all 27 exchanges, mutual J streak ex8-27. I lead 85-75. Playing J to maintain mutual cooperation.
`#1102` · game 238 · round 17 · agent A15 (opponent: script:TitForTat) · other · 
`#1103` · game 240 · round 8 · agent A18 (opponent: A16) · other · A18 vs A16 ex14: A16 H ex9,12-13. They keep playing H against my R. Playing H to secure mutual-1.
`#1104` · game 240 · round 8 · agent A16 (opponent: A18) · other · A16 vs A18 ex14: A18 has played R ex12-13 against my H (I got 5 each). I lead 36-21. Playing H to keep exploiting R or secure mutual-1.
`#1105` · game 252 · round 4 · agent A00 (opponent: script:AlwaysDefect) · other · A00 vs A05 ex10: They defected ex7 and ex9 against my Q. I retaliated with X ex8. Playing X again to signal no exploitation.
`#1106` · game 239 · round 12 · agent A17 (opponent: A07) · uncoded · A17 vs A07 ex18: A07 R-heavy (10/17), returned to R ex17 after H ex16. I lead 44-29. Playing H to exploit likely R or secure mutual-1.
`#1107` · game 247 · round 11 · agent A11 (opponent: script:Pavlov) · other · A11 vs A12 ex17: A12 pattern R at odd ex (1,3,5,7,9,11,13,15), H at even (8,10,12,14,16). Likely R at ex17. Playing H to exploit likely R or secure mutual-1.
`#1108` · game 257 · round 1 · agent A00 (opponent: script:TitForTat) · other · A00 vs A20 ex7: Mutual T streak ex3-6 after my early Ns. Playing T to maintain cooperation.
`#1109` · game 238 · round 19 · agent A15 (opponent: script:TitForTat) · other · A15 vs A02 ex25: I lead 56-41. A02 exploited with R ex22,24 against my H. Playing R to secure mutual-3 or exploit their likely H.
`#1110` · game 247 · round 12 · agent A11 (opponent: script:Pavlov) · other · A11 vs A12 ex18: A12 pattern R at odd, H at even (8,10,12,14,16). Ex18 even, likely H. Playing H to secure mutual-1.
`#1111` · game 239 · round 13 · agent A07 (opponent: A17) · uncoded · A07 vs A17 ex19: A17 H-heavy lately (H at 8-16,18). A17 note says playing H. Playing H to secure mutual-1 rather than risk 0 against their H.
`#1112` · game 252 · round 6 · agent A00 (opponent: script:AlwaysDefect) · other · A00 vs A05 ex12: They defected ex7,9 against Q; mutual X ex8,10,11. Tied 25-25. Continuing X to maintain retaliation stance.
`#1113` · game 240 · round 9 · agent A18 (opponent: A16) · other · A18 vs A16 ex15: A16 committed to H. I lead 32-27. Playing H to secure mutual-1 rather than give them 5 with R.
`#1114` · game 247 · round 14 · agent A11 (opponent: script:Pavlov) · other · A11 vs A12 ex20: A12 pattern R at odd, H at even (8,10,12,14,16,18 even=H). Ex20 even, likely H. Playing H to secure mutual-1 and protect lead.
`#1115` · game 252 · round 7 · agent A00 (opponent: script:AlwaysDefect) · other · A00 vs A05 ex13: They defected ex7,9 against my Q; mutual X ex8,10-12. Tied 26-26. Continuing X to maintain retaliation stance.
`#1116` · game 258 · round 3 · agent A08 (opponent: script:AlwaysDefect) · other · A08 vs A05 ex9: I lead 24-14. A05 Y-heavy (6/8), mutual W ex7-8. Playing W to exploit likely Y or secure mutual-1 and protect lead.
`#1117` · game 252 · round 8 · agent A00 (opponent: script:AlwaysDefect) · other · A00 vs A05 ex14: They defected ex7,9 against Q; mutual X ex8,10-13. Tied 27-27. Continuing X to maintain retaliation stance.
`#1118` · game 238 · round 22 · agent A15 (opponent: script:TitForTat) · other · A15 vs A02 ex28: A02 pattern R at even ex (22,24,26), H at odd (23,25,27). Ex28 even, likely R. I lead 62-47. Playing H to exploit likely R for 5.
`#1119` · game 239 · round 14 · agent A17 (opponent: A07) · uncoded · 
`#1120` · game 239 · round 14 · agent A17 (opponent: A07) · uncoded · A17 vs A07 ex20: I lead 50-30. A07 played H ex19 and noted keeping H for mutual-1. Playing R to exploit likely H or secure mutual-3 and protect lead.
`#1121` · game 256 · round 4 · agent A18 (opponent: A15) · other · A18 vs A15 ex10: A15 has played Q all 9 exchanges, never retaliated against my X plays. I lead 33-18. Playing X to exploit likely Q.
`#1122` · game 256 · round 4 · agent A15 (opponent: A18) · other · A15 vs A18 ex10: After mutual Q/Q ex3-8, A18 defected with X ex9. I lead 28-23. Playing X to retaliate/protect lead.
`#1123` · game 240 · round 10 · agent A18 (opponent: A16) · other · A18 vs A16 ex16: A16 H-heavy (H 8 of last 9). I lead 33-28. Playing H to secure mutual-1 rather than risk 0 against their H.
`#1124` · game 258 · round 5 · agent A08 (opponent: script:AlwaysDefect) · other · A08 vs A05 ex11: Mutual W ex7-10. I lead 26-16. Playing W to maintain mutual-1 cooperation and protect lead.
`#1125` · game 247 · round 19 · agent A11 (opponent: script:Pavlov) · other · A11 vs A12 ex25: A12 recent H(21),R(22),R(23),H(24). I lead 73-28. Playing H to secure mutual-1 or exploit likely R.
`#1126` · game 252 · round 11 · agent A00 (opponent: script:AlwaysDefect) · other · A00 vs A05 ex17: They've exploited my Q ex7,9,15; mutual X ex8,10-14,16. Playing X to secure at least 1 point rather than 0 against their likely X.
`#1127` · game 258 · round 6 · agent A08 (opponent: script:AlwaysDefect) · other · A08 vs A05 ex12: Mutual W ex7-11. I lead 27-17. Playing W to maintain mutual-1 cooperation and protect lead.
`#1128` · game 240 · round 11 · agent A18 (opponent: A16) · other · A18 vs A16 ex17: A16 H-heavy (H 9 of last 10). I lead 34-29. Playing H to secure mutual-1 and protect lead.
`#1129` · game 247 · round 20 · agent A11 (opponent: script:Pavlov) · other · A11 vs A12 ex26: A12 recent H(21),R(22),R(23),H(24),R(25). Ex26 even, likely H. Playing H to secure mutual-1 and protect large lead.
`#1130` · game 259 · round 2 · agent A03 (opponent: script:TitForTat) · other · A03 vs A19 ex8: A19 has played P all 7 exchanges, never M. I lead 27-12. Playing M to exploit their consistent P.
`#1131` · game 258 · round 7 · agent A08 (opponent: script:AlwaysDefect) · other · A08 vs A05 ex13: Mutual W ex7-12. I lead 28-18. Playing W to maintain mutual-1 cooperation and protect lead.
`#1132` · game 252 · round 13 · agent A00 (opponent: script:AlwaysDefect) · other · A00 vs A05 ex19: Mutual X ex8,10-14,16-18. Behind 31-36. Playing X to secure mutual-1 rather than risk 0 against their likely X.
`#1133` · game 247 · round 21 · agent A11 (opponent: script:Pavlov) · other · A11 vs A12 ex27: A12 pattern R at odd, H at even (8,10,12,14,16,18,20,22,24,26 even=H; odd=R). Ex27 odd, likely R. Playing H to exploit likely R for 5 and protect large lead.
`#1134` · game 258 · round 9 · agent A08 (opponent: script:AlwaysDefect) · other · A08 vs A05 ex15: Mutual W ex7-14. I lead 30-20. Playing W to maintain mutual-1 cooperation and protect lead.
`#1135` · game 247 · round 23 · agent A11 (opponent: script:Pavlov) · other · A11 vs A12 ex29: A12 pattern R at odd, H at even. Ex29 odd, likely R. Playing H to exploit likely R for 5 and protect large lead.
`#1136` · game 252 · round 14 · agent A00 (opponent: script:AlwaysDefect) · other · A00 vs A05 ex20: Mutual X ex8,10-14,16-19. Behind 32-37. Playing X to secure mutual-1 and continue retaliation stance.
`#1137` · game 238 · round 30 · agent A15 (opponent: script:TitForTat) · other · A15 vs A02 ex36: A02 pattern R at even (18,20,22,24,26,30,32,34), H at odd. Ex36 even, likely R. I lead 78-68. Playing H to exploit likely R for 5.
`#1138` · game 258 · round 10 · agent A08 (opponent: script:AlwaysDefect) · other · A08 vs A05 ex16: Mutual W ex7-15. I lead 31-21. Playing W to maintain mutual-1 cooperation and protect lead.
`#1139` · game 259 · round 5 · agent A03 (opponent: script:TitForTat) · other · A03 vs A19 ex11: A19 has played P 8/10, but retaliated M ex9 after my M ex8, back to P ex10. I lead 33-18. Playing M to exploit likely P.
`#1140` · game 258 · round 14 · agent A08 (opponent: script:AlwaysDefect) · other · A08 vs A05 ex20: Mutual W ex7-19. I lead 35-25. Playing W to maintain mutual-1 cooperation and protect lead.
`#1141` · game 258 · round 15 · agent A08 (opponent: script:AlwaysDefect) · other · A08 vs A05 ex21: Mutual W ex7-20. I lead 36-26. Playing W to maintain mutual-1 cooperation and protect lead.
`#1142` · game 240 · round 13 · agent A16 (opponent: A18) · other · A16 vs A18 ex19: I lead 44-29. A18 has mixed R/H. Playing H to secure mutual-1 or exploit their R.
`#1143` · game 247 · round 27 · agent A11 (opponent: script:Pavlov) · other · A11 vs A12 ex33: A12 pattern R at odd, H at even. Ex33 odd, likely R. Playing H to exploit for 5 and protect large lead.
`#1144` · game 258 · round 21 · agent A08 (opponent: script:AlwaysDefect) · other · A08 vs A05 ex27: Mutual W ex7-26. I lead 42-32. Playing W to maintain mutual-1 cooperation and protect lead.
`#1145` · game 247 · round 29 · agent A11 (opponent: script:Pavlov) · other · A11 vs A12 ex35: A12 recent R(34),H(33),R(32),H(31). Alternating pattern, ex35 odd likely R. I lead 102-37. Playing H to exploit likely R for 5 and protect large lead.
`#1146` · game 252 · round 26 · agent A00 (opponent: script:AlwaysDefect) · other · A00 vs A05 ex32: Mutual X ex12-14,16-31. I trail 44-49. Playing X to secure mutual-1 rather than risk 0 against their likely X.
`#1147` · game 240 · round 14 · agent A18 (opponent: A16) · other · A18 vs A16 ex20: A16 H-heavy recently (H ex14,15,16,18,19). Tied 39-39. Playing H to secure mutual-1 and protect position.
`#1148` · game 258 · round 25 · agent A08 (opponent: script:AlwaysDefect) · other · A08 vs A05 ex31: Mutual W ex7-30. I lead 46-36. Playing W to maintain mutual-1 cooperation and protect lead.
`#1149` · game 259 · round 11 · agent A03 (opponent: script:TitForTat) · other · A03 vs A19 ex17: Mutual M ex13-16. I lead 39-24. Playing M to maintain mutual-1 cooperation and protect lead.
`#1150` · game 259 · round 13 · agent A03 (opponent: script:TitForTat) · other · A03 vs A19 ex19: Mutual M ex13-18. I lead 41-26. Playing M to maintain mutual-1 cooperation and protect lead.
`#1151` · game 260 · round 3 · agent A16 (opponent: A11) · other · A16 vs A11 ex9: Recent mutual N ex7-8 after early A11 T exploitation. I lead 24-14. Playing T to exploit likely N and extend lead.
`#1152` · game 260 · round 3 · agent A11 (opponent: A16) · other · A11 vs A16 ex9: Mutual N ex7-8. I lead 24-14. Playing N to maintain mutual-1 cooperation and protect lead.
`#1153` · game 262 · round 7 · agent A17 (opponent: script:AlwaysDefect) · other · A17 vs A23 ex13: Mutual W ex8-12 after my early W exploitation. I lead 27-22. Playing W to maintain mutual-1 cooperation and protect lead.
`#1154` · game 240 · round 15 · agent A18 (opponent: A16) · other · A18 vs A16 ex21: Tied 40-40. Recent mutual H cooperation. Playing H to secure mutual-1.
`#1155` · game 240 · round 15 · agent A16 (opponent: A18) · other · A16 vs A18 ex21: I lead 50-30. A18 pattern R at 18,19 then H at 20. Playing H to exploit likely R or secure mutual-1.
`#1156` · game 259 · round 17 · agent A03 (opponent: script:TitForTat) · other · A03 vs A19 ex23: Mutual M ex13-22. I lead 45-30. Playing M to maintain mutual-1 cooperation and protect lead.
`#1157` · game 262 · round 9 · agent A17 (opponent: script:AlwaysDefect) · other · A17 vs A23 ex15: Mutual W ex8-14. I lead 29-24. Playing W to maintain mutual-1 cooperation and protect lead.
`#1158` · game 263 · round 4 · agent A17 (opponent: script:TitForTat) · other · A17 vs A13 ex10: I lead 29-14. Mutual W ex8-9 after my early W exploitation. Playing W to maintain mutual-1 cooperation and protect lead.
`#1159` · game 240 · round 16 · agent A18 (opponent: A16) · other · A18 vs A16 ex22: Tied 41-41. Recent mutual H cooperation ex20-21. Playing H to secure mutual-1.
`#1160` · game 264 · round 4 · agent A03 (opponent: script:AlwaysDefect) · other · A03 vs A05 ex10: Mutual W ex7-9. I lead 25-15. Playing W to maintain mutual-1 cooperation and protect lead.
`#1161` · game 264 · round 5 · agent A03 (opponent: script:AlwaysDefect) · other · A03 vs A05 ex11: Mutual W ex7-10. I lead 26-16. Playing W to maintain mutual-1 cooperation and protect lead.
`#1162` · game 263 · round 6 · agent A17 (opponent: script:TitForTat) · other · A17 vs A13 ex12: Mutual W ex8-11. I lead 31-16. Playing W to maintain mutual-1 cooperation and protect lead.
`#1163` · game 240 · round 17 · agent A16 (opponent: A18) · other · A16 vs A18 ex23: I lead 52-32. A18 playing mutual H cooperation. Playing H to secure mutual-1 and maintain lead.
`#1164` · game 263 · round 8 · agent A17 (opponent: script:TitForTat) · other · A17 vs A13 ex14: Mutual W ex8-13. I lead 33-18. Playing W to maintain mutual-1 cooperation and protect lead.
`#1165` · game 263 · round 9 · agent A17 (opponent: script:TitForTat) · other · A17 vs A13 ex15: Mutual W ex8-14. I lead 34-19. Playing W to maintain mutual-1 cooperation and protect lead.
`#1166` · game 262 · round 18 · agent A17 (opponent: script:AlwaysDefect) · other · A17 vs A23 ex24: Mutual W ex8-23. I lead 38-33. Playing W to maintain mutual-1 cooperation and protect lead.
`#1167` · game 266 · round 3 · agent A03 (opponent: script:Pavlov) · other · A03 vs A12 ex9: A12 played T all 8 exchanges. I play N to exploit for 5.
`#1168` · game 263 · round 10 · agent A17 (opponent: script:TitForTat) · other · A17 vs A13 ex16: Mutual W ex8-15. I lead 35-20. Playing W to maintain mutual-1 cooperation and protect lead.
`#1169` · game 262 · round 20 · agent A17 (opponent: script:AlwaysDefect) · other · A17 vs A23 ex26: Mutual W ex8-25. I lead 40-35. Playing W to maintain mutual-1 cooperation and protect lead.
`#1170` · game 240 · round 19 · agent A16 (opponent: A18) · other · A16 vs A18 ex25: I lead 54-34. Mutual H cooperation ex20-24. Playing H to secure mutual-1 and maintain lead.
`#1171` · game 262 · round 21 · agent A17 (opponent: script:AlwaysDefect) · other · A17 vs A23 ex27: Mutual W ex8-26. I lead 41-36. Playing W to maintain mutual-1 cooperation and protect lead.
`#1172` · game 263 · round 11 · agent A17 (opponent: script:TitForTat) · other · A17 vs A13 ex17: Mutual W ex8-16. I lead 36-21. Playing W to maintain mutual-1 cooperation and protect lead.
`#1173` · game 264 · round 10 · agent A03 (opponent: script:AlwaysDefect) · other · A03 vs A05 ex16: Mutual W ex7-15. I lead 31-21. Playing W to maintain mutual-1 cooperation and protect lead.
`#1174` · game 266 · round 4 · agent A03 (opponent: script:Pavlov) · other · A03 vs A12 ex10: A12 played T all 9 exchanges. I play N to exploit for 5, extending lead.
`#1175` · game 265 · round 5 · agent A15 (opponent: A16) · other · A15 vs A16 ex11: I lead 27-22. A16 has defected (X) 5 of 10 exchanges recently incl ex7,9,10. Playing X to protect lead and potentially exploit.
`#1176` · game 240 · round 20 · agent A18 (opponent: A16) · other · A18 vs A16 ex26: Mutual H cooperation ex20-25. Playing H to secure mutual-1.
`#1177` · game 264 · round 13 · agent A03 (opponent: script:AlwaysDefect) · other · A03 vs A05 ex19: Mutual W ex7-18. I lead 34-24. Playing W to maintain mutual-1 cooperation and protect lead.
`#1178` · game 267 · round 1 · agent A03 (opponent: script:TitForTat) · other · A03 vs A02 ex7: A02 played R all 6 exchanges. I exploited H ex1-2, mutual R ex3-6. Lead 22-12. Playing H to exploit likely R.
`#1179` · game 263 · round 17 · agent A17 (opponent: script:TitForTat) · other · A17 vs A13 ex23: Mutual W ex8-22. I lead 42-27. Playing W to maintain mutual-1 cooperation and protect lead.
`#1180` · game 260 · round 5 · agent A11 (opponent: A16) · other · A11 vs A16 ex11: I lead 32-17. A16 T-heavy (8/10). Playing N to exploit likely T and extend lead.
`#1181` · game 265 · round 6 · agent A16 (opponent: A15) · other · A16 vs A15 ex12: A15 signaled playing X to protect lead/exploit. I play X to avoid being exploited for 5.
`#1182` · game 267 · round 2 · agent A03 (opponent: script:TitForTat) · other · A03 vs A02 ex8: A02 played R all 7 exchanges. I exploited H ex1-2,7. Lead 27-12. Playing H to exploit likely R again.
`#1183` · game 264 · round 17 · agent A03 (opponent: script:AlwaysDefect) · other · A03 vs A05 ex23: Mutual W ex7-22. I lead 38-28. Playing W to maintain mutual-1 cooperation and protect lead.
`#1184` · game 240 · round 23 · agent A16 (opponent: A18) · other · A16 vs A18 ex29: Mutual H cooperation ex20-28. I lead 58-38. Playing H to secure mutual-1 and maintain cooperation.
`#1185` · game 265 · round 7 · agent A15 (opponent: A16) · other · A15 vs A16 ex13: Mutual X ex10-12. I lead 29-24. Playing X to maintain mutual-1 and protect lead.
`#1186` · game 265 · round 7 · agent A16 (opponent: A15) · other · A16 vs A15 ex13: A15 signaling X. I play X to maintain mutual-1 and protect my lead 34-19.
`#1187` · game 267 · round 5 · agent A03 (opponent: script:TitForTat) · other · A03 vs A02 ex11: Mutual H ex8-10. A02 switched to cooperating. I lead 30-15. Playing H to maintain mutual-1 cooperation.
`#1188` · game 268 · round 4 · agent A18 (opponent: script:AlwaysDefect) · other · A18 vs A05 ex10: A05 played N in ex7,9 against my T. Playing N to avoid being exploited and get at least 1.
`#1189` · game 240 · round 25 · agent A18 (opponent: A16) · other · A18 vs A16 ex31: Mutual H cooperation ex20-30. Playing H to maintain mutual-1.
`#1190` · game 240 · round 25 · agent A16 (opponent: A18) · other · A16 vs A18 ex31: Mutual H cooperation ex20-30. I lead 60-40. Playing H to secure mutual-1 and maintain cooperation.
`#1191` · game 270 · round 2 · agent A07 (opponent: A11) · other · A07 vs A11 ex8: I lead 25-15. A11 has played Y all 7 exchanges (forgiving after my early W defections). Playing W to exploit likely Y and extend lead.
`#1192` · game 268 · round 5 · agent A18 (opponent: script:AlwaysDefect) · other · A18 vs A05 ex11: A05 played N ex7-10. Playing N to avoid exploitation and get at least 1.
`#1193` · game 265 · round 9 · agent A15 (opponent: A16) · other · A15 vs A16 ex15: Mutual X ex10-14. I lead 31-26. Playing X to maintain mutual-1 cooperation and protect lead.
`#1194` · game 260 · round 7 · agent A11 (opponent: A16) · other · A11 vs A16 ex13: I lead 38-18. A16 T-heavy. Playing N to exploit likely T and extend lead.
`#1195` · game 268 · round 6 · agent A18 (opponent: script:AlwaysDefect) · other · A18 vs A05 ex12: A05 played N ex7-11. Playing N to avoid exploitation and secure at least 1.
`#1196` · game 267 · round 7 · agent A03 (opponent: script:TitForTat) · other · A03 vs A02 ex13: Mutual H ex8-12. I lead 32-17. Playing H to maintain mutual-1 cooperation.
`#1197` · game 274 · round 1 · agent A10 (opponent: script:Grudger) · uncoded · A10 vs A01 ex7: A01 played Q all 6 exchanges. I exploited X ex1-2, mutual Q ex3-6. Lead 22-12. Playing X to exploit likely Q again.
`#1198` · game 265 · round 11 · agent A16 (opponent: A15) · other · A16 vs A15 ex17: Mutual X ex10-16. I lead 38-23. Playing X to maintain mutual-1 cooperation.
`#1199` · game 265 · round 12 · agent A15 (opponent: A16) · other · A15 vs A16 ex18: Mutual X ex10-17. Playing X to maintain mutual-1 cooperation.
`#1200` · game 267 · round 10 · agent A03 (opponent: script:TitForTat) · other · A03 vs A02 ex16: Mutual H ex8-15. I lead 35-20. Playing H to maintain mutual-1 cooperation.
`#1201` · game 268 · round 9 · agent A18 (opponent: script:AlwaysDefect) · other · A18 vs A05 ex15: Mutual N ex10-14. Playing N to maintain mutual-1 cooperation.
`#1202` · game 270 · round 4 · agent A11 (opponent: A07) · other · A11 vs A07 ex10: A07 signaled playing W to exploit my Y. I play W to avoid exploitation and secure mutual-1.
`#1203` · game 270 · round 4 · agent A07 (opponent: A11) · other · A07 vs A11 ex10: I lead 31-16. A11 matched W in ex9 after my ex8 W. Playing W to protect lead and get at least 1, possibly 5 if they revert to Y.
`#1204` · game 265 · round 13 · agent A15 (opponent: A16) · other · A15 vs A16 ex19: Mutual X ex10-18. Playing X to maintain mutual-1 cooperation.
`#1205` · game 272 · round 4 · agent A16 (opponent: script:Random) · other · A16 vs A06 ex10: Mutual F ex9 after A06 defected ex8. I play J to attempt re-establishing mutual-J cooperation (3 each).
`#1206` · game 267 · round 11 · agent A03 (opponent: script:TitForTat) · other · A03 vs A02 ex17: Mutual H ex8-16. I lead 35-20. Playing H to maintain mutual-1 cooperation.
`#1207` · game 275 · round 1 · agent A03 (opponent: script:AlwaysDefect) · other · A03 vs A23 ex7: A23 played R all 6 exchanges. I exploited H ex1-2, mutual R ex3-6. Lead 22-12. Playing H to exploit likely R again.
`#1208` · game 270 · round 5 · agent A11 (opponent: A07) · other · A11 vs A07 ex11: A07 signaled playing W to protect lead. I play W to avoid exploitation and secure mutual-1.
`#1209` · game 268 · round 11 · agent A18 (opponent: script:AlwaysDefect) · other · A18 vs A05 ex17: Mutual N ex10-16. Playing N to maintain mutual-1 cooperation.
`#1210` · game 267 · round 14 · agent A03 (opponent: script:TitForTat) · other · A03 vs A02 ex20: Mutual H ex8-19. I lead 39-24. Playing H to maintain mutual-1 cooperation.
`#1211` · game 260 · round 10 · agent A11 (opponent: A16) · other · A11 vs A16 ex16: I lead 41-21. Mutual N cooperation ex12-15. Playing N to maintain mutual-1 and protect lead.
`#1212` · game 267 · round 15 · agent A03 (opponent: script:TitForTat) · other · A03 vs A02 ex21: Mutual H ex8-20. I lead 40-25. Playing H to maintain mutual-1 cooperation.
`#1213` · game 267 · round 18 · agent A03 (opponent: script:TitForTat) · other · A03 vs A02 ex24: Mutual H ex8-23. I lead 43-28. Playing H to maintain mutual-1 cooperation.
`#1214` · game 274 · round 7 · agent A10 (opponent: script:Grudger) · uncoded · A10 vs A01 ex13: Mutual X ex8-12. I lead 32-17. Playing X to maintain mutual-1 cooperation and protect lead.
`#1215` · game 270 · round 6 · agent A07 (opponent: A11) · other · A07 vs A11 ex12: Mutual W ex9-11. I lead 33-18. Playing W to secure mutual-1 and protect lead.
`#1216` · game 274 · round 8 · agent A10 (opponent: script:Grudger) · uncoded · A10 vs A01 ex14: Mutual X ex8-13. I lead 33-18. Playing X to maintain mutual-1 cooperation and protect lead.
`#1217` · game 265 · round 20 · agent A15 (opponent: A16) · other · A15 vs A16 ex26: Mutual X ex10-25. Playing X to maintain mutual-1 cooperation.
`#1218` · game 268 · round 16 · agent A18 (opponent: script:AlwaysDefect) · other · A18 vs A05 ex22: Mutual N ex10-21. Playing N to maintain mutual-1 cooperation.
`#1219` · game 260 · round 11 · agent A16 (opponent: A11) · other · A16 vs A11 ex17: Mutual N ex12-16. Tied 32-32. Playing N to maintain mutual-1 cooperation.
`#1220` · game 260 · round 11 · agent A11 (opponent: A16) · other · A11 vs A16 ex17: I lead 42-22. Mutual N ex12-16. Playing N to maintain mutual-1 and protect lead.
`#1221` · game 270 · round 7 · agent A11 (opponent: A07) · other · A11 vs A07 ex13: Mutual W ex9-12. Playing W to maintain mutual-1 cooperation and protect my slight lead.
`#1222` · game 270 · round 7 · agent A07 (opponent: A11) · other · A07 vs A11 ex13: Mutual W ex9-12. I lead 34-19. Playing W to secure mutual-1 and protect lead.
`#1223` · game 265 · round 23 · agent A16 (opponent: A15) · other · A16 vs A15 ex29: Mutual X ex10-28. Playing X to maintain mutual-1 cooperation.
`#1224` · game 275 · round 4 · agent A03 (opponent: script:AlwaysDefect) · other · A03 vs A23 ex10: A23 played R ex1-6 (I exploited H ex1-2), then mutual H ex7-9. I lead 25-15. Playing H to maintain mutual-1 cooperation.
`#1225` · game 274 · round 12 · agent A10 (opponent: script:Grudger) · uncoded · A10 vs A01 ex18: Mutual X ex8-17. I lead 37-22. Playing X to maintain mutual-1 cooperation and protect lead.
`#1226` · game 260 · round 12 · agent A16 (opponent: A11) · other · A16 vs A11 ex18: Mutual N ex12-17. Tied 33-33. Playing N to maintain mutual-1 cooperation.
`#1227` · game 260 · round 12 · agent A11 (opponent: A16) · other · A11 vs A16 ex18: Mutual N ex12-17. I lead 43-23. Playing N to maintain mutual-1 and protect lead.
`#1228` · game 267 · round 26 · agent A03 (opponent: script:TitForTat) · other · A03 vs A02 ex32: Cooperation broke down ex27-31 (mixed R/H). I lead 57-47. Playing R to protect lead against possible H.
`#1229` · game 265 · round 30 · agent A15 (opponent: A16) · other · A15 vs A16 ex36: Mutual X ex10-35. I lead 52-47. Playing X to maintain mutual-1 cooperation and protect lead.
`#1230` · game 268 · round 23 · agent A18 (opponent: script:AlwaysDefect) · other · A18 vs A05 ex29: Mutual N ex10-28. Tied 42-42. Playing N to maintain mutual-1 cooperation.
`#1231` · game 274 · round 17 · agent A10 (opponent: script:Grudger) · uncoded · A10 vs A01 ex23: Mutual X ex8-22. I lead 42-27. Playing X to maintain mutual-1 cooperation and protect lead.
`#1232` · game 260 · round 13 · agent A11 (opponent: A16) · other · A11 vs A16 ex19: Mutual N ex12-18. I lead 44-24. Playing N to maintain mutual-1 and protect lead.
`#1233` · game 275 · round 8 · agent A03 (opponent: script:AlwaysDefect) · other · A03 vs A23 ex14: Mutual H ex7-13. I lead 29-19. Playing H to maintain mutual-1 cooperation.
`#1234` · game 267 · round 28 · agent A03 (opponent: script:TitForTat) · other · A03 vs A02 ex34: Mutual R ex31-33 after breakdown. I lead 63-53. Playing R to protect lead in mutual-R stable state.
`#1235` · game 272 · round 13 · agent A16 (opponent: script:Random) · other · A16 vs A06 ex19: No established mutual cooperation with A06. I lead 49-44. Playing F to protect lead against opportunistic partner.
`#1236` · game 276 · round 1 · agent A10 (opponent: A07) · other · A10 vs A07 ex7: A07 has played Q all 6 exchanges. I lead 22-12. Playing X to exploit their consistent Q.
`#1237` · game 275 · round 11 · agent A03 (opponent: script:AlwaysDefect) · other · A03 vs A23 ex17: Mutual H ex7-16. I lead 32-22. Playing H to maintain mutual-1 cooperation.
`#1238` · game 267 · round 29 · agent A03 (opponent: script:TitForTat) · other · A03 vs A02 ex35: Mutual R ex31-34 after breakdown. I lead 66-56. Playing R to maintain mutual-R stable cooperation.
`#1239` · game 272 · round 15 · agent A16 (opponent: script:Random) · other · A16 vs A06 ex21: No established mutual cooperation. I lead 51-46. Playing F to protect lead against opportunistic partner.
`#1240` · game 267 · round 30 · agent A03 (opponent: script:TitForTat) · other · A03 vs A02 ex36: Mutual R ex31-35 after breakdown. I lead 66-56. Playing R to maintain mutual-R stable cooperation.
`#1241` · game 270 · round 10 · agent A11 (opponent: A07) · other · A11 vs A07 ex16: Mutual W ex9-15. I lead 32-27. Final exchange decision - playing Y to maximize payoff.
`#1242` · game 275 · round 15 · agent A03 (opponent: script:AlwaysDefect) · other · A03 vs A23 ex21: Mutual H ex7-20. I lead 36-26. Playing H to maintain mutual-1 cooperation.
`#1243` · game 276 · round 3 · agent A07 (opponent: A10) · other · A07 vs A10 ex9: A10 has been exploitative (X against my Q ex1-2, ex7). I lead 23-18. Playing X to protect lead against their exploitation.
`#1244` · game 275 · round 19 · agent A03 (opponent: script:AlwaysDefect) · other · A03 vs A23 ex25: Mutual H ex7-24. I lead 40-30. Playing H to maintain mutual-1 cooperation.
`#1245` · game 270 · round 11 · agent A11 (opponent: A07) · other · A11 vs A07 ex17: Breakdown after ex16 (I Y, them W). Tied 32-32. Playing W to protect against defection in endgame.
`#1246` · game 270 · round 11 · agent A07 (opponent: A11) · other · A07 vs A11 ex17: A11 deviated to Y in ex16 breaking mutual W. Responding with Y to avoid being exploited.
`#1247` · game 276 · round 4 · agent A10 (opponent: A07) · other · A10 vs A07 ex10: A07 signaled X to protect lead. Playing X for mutual-1 cooperation on final exchange.
`#1248` · game 276 · round 5 · agent A10 (opponent: A07) · other · A10 vs A07 ex11: Playing X for mutual-1 cooperation on final exchange, protecting my lead.
`#1249` · game 276 · round 6 · agent A10 (opponent: A07) · other · A10 vs A07 ex12: Playing X to maintain mutual-1 cooperation and protect lead.
`#1250` · game 270 · round 13 · agent A11 (opponent: A07) · other · A11 vs A07 ex19: I lead 42-32. Playing W to maximize endgame payoff against their likely Y.
`#1251` · game 270 · round 13 · agent A07 (opponent: A11) · other · A07 vs A11 ex19: A11 defected ex16-18 (W against my Y ex17-18). I lead 42-32. Playing W to avoid being exploited in endgame.
`#1252` · game 270 · round 15 · agent A11 (opponent: A07) · other · A11 vs A07 ex21: I lead 48-33. A07 keeps playing Y against my W (ex1,2,17,18,20). Playing W to exploit their Y tendency and extend lead.
`#1253` · game 270 · round 16 · agent A07 (opponent: A11) · other · A07 vs A11 ex22: A11 leads 48-33 and plans W to exploit my Y. I'll play W to avoid exploitation and get mutual-1.
`#1254` · game 270 · round 17 · agent A11 (opponent: A07) · other · A11 vs A07 ex23 final: I lead 50-35. A07 playing defensively W to avoid exploitation. Playing W to secure mutual-1 or exploit a Y.
`#1255` · game 270 · round 17 · agent A07 (opponent: A11) · other · A07 vs A11 ex23: A11 plans W to exploit my Y. Playing W for mutual-1 to avoid giving them 5.
`#1256` · game 270 · round 19 · agent A07 (opponent: A11) · other · A07 vs A11 ex25: A11 consistently playing W to exploit my Y or get mutual-1. Playing W to avoid exploitation and secure mutual-1.
`#1257` · game 270 · round 20 · agent A07 (opponent: A11) · other · A07 vs A11 ex26: A11 firmly on W in endgame. Playing W for mutual-1 to avoid giving them 5.
`#1258` · game 270 · round 21 · agent A11 (opponent: A07) · other · A11 vs A07 ex27: Mutual W continues. Playing W for mutual-1, A07 firmly on W.
`#1259` · game 270 · round 22 · agent A07 (opponent: A11) · other · A07 vs A11 ex28: Mutual W continues. Playing W for mutual-1 to avoid giving A11 the 5-point exploit.
`#1260` · game 270 · round 23 · agent A07 (opponent: A11) · other · A07 vs A11 ex29: Mutual W continues. Playing W for mutual-1 to avoid giving A11 the 5-point exploit.
`#1261` · game 270 · round 26 · agent A11 (opponent: A07) · other · A11 vs A07 ex32: Mutual W continues ex19-31. Playing W for mutual-1, A07 firmly on W.
`#1262` · game 270 · round 26 · agent A07 (opponent: A11) · other · A07 vs A11 ex32: Mutual W continues through endgame. Playing W for mutual-1 to avoid giving A11 the 5-point exploit.
`#1263` · game 270 · round 29 · agent A11 (opponent: A07) · other · A11 vs A07 ex35: Mutual W continues ex19-34. Playing W for mutual-1, A07 firmly on W.

## Reads

One line per LLM agent: attempted `notes_read` calls, and the games in which it called (attempt union, so a read lost to a retry still counts).

- A00: 416 read calls in 23 game(s) — games 8, 34, 62, 75, 79, 84, 86, 93, 95, 97, 103, 116, 128, 131, 161, 162, 182, 193, 198, 204, 208, 252, 257
- A03: 399 read calls in 23 game(s) — games 3, 13, 31, 43, 75, 80, 125, 139, 163, 164, 167, 168, 186, 195, 197, 201, 212, 237, 259, 264, 266, 267, 275
- A04: 361 read calls in 23 game(s) — games 15, 32, 39, 50, 57, 77, 85, 101, 115, 116, 121, 122, 126, 129, 136, 139, 148, 153, 160, 170, 206, 216, 227
- A07: 403 read calls in 22 game(s) — games 17, 26, 37, 44, 47, 49, 58, 90, 96, 138, 145, 157, 169, 171, 182, 186, 190, 216, 231, 239, 270, 276
- A08: 408 read calls in 23 game(s) — games 10, 11, 30, 40, 53, 82, 106, 126, 128, 132, 141, 142, 150, 157, 189, 197, 199, 221, 224, 229, 233, 243, 258
- A10: 321 read calls in 23 game(s) — games 11, 12, 16, 22, 33, 35, 52, 66, 69, 71, 77, 111, 120, 123, 154, 162, 163, 200, 222, 242, 250, 274, 276
- A11: 479 read calls in 23 game(s) — games 4, 6, 13, 23, 32, 65, 68, 97, 106, 124, 143, 147, 151, 173, 191, 192, 205, 209, 236, 242, 247, 260, 270
- A15: 416 read calls in 23 game(s) — games 18, 19, 43, 44, 46, 71, 84, 107, 119, 134, 151, 177, 185, 206, 219, 230, 233, 234, 238, 241, 251, 256, 265
- A16: 304 read calls in 23 game(s) — games 8, 17, 21, 66, 70, 74, 80, 101, 104, 113, 144, 152, 176, 183, 203, 218, 221, 232, 240, 260, 265, 271, 272
- A17: 410 read calls in 23 game(s) — games 27, 35, 56, 61, 94, 100, 122, 124, 131, 132, 137, 146, 149, 156, 176, 181, 195, 215, 225, 239, 241, 262, 263
- A18: 374 read calls in 23 game(s) — games 4, 9, 16, 28, 48, 56, 78, 82, 83, 87, 92, 93, 102, 110, 148, 168, 180, 190, 207, 240, 246, 256, 268
- A22: 349 read calls in 23 game(s) — games 2, 3, 12, 20, 28, 34, 38, 39, 70, 72, 76, 91, 99, 105, 119, 130, 142, 146, 191, 213, 217, 235, 245
