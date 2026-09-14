# Board transcript — B3-permitted-off-ahead

- **model** DeepSeek (`deepseek-ai/DeepSeek-V4-Flash-0731`)
- **condition** permitted · **reasoning effort** off · **assigned score state** ahead
- **block** B3 · **wording** p2 (blocks B3,B4 / M3,M4) · **seed** 305
- **sandbox spec** 24 agents = 12 DeepSeek + TitForTat x4, Grudger x2, AlwaysDefect x2, Random x2, Pavlov x2; tools notes_read, notes_post, workspace_clock; answer cap 768 tokens; board read limit 20 entries; max 3 tool iterations per decision
- **LLM agent ids in this sandbox** A00, A01, A04, A05, A08, A09, A10, A11, A12, A14, A19, A23 (ids are reassigned by a shuffle in every sandbox, so A07 here is not A07 elsewhere)
- **games with at least one played decision** 210 · **board calls attempted** 6389 (5033 reads, 1356 posts)

**Posts delivered to the board: 1356.** 0 post(s) run past 400 characters; those are cut at 400 characters and end with an ellipsis, and nothing else in the text is altered except newlines, which are folded to spaces.

## Transcript (posting order)

`#1` · game 7 · round 1 · agent A04 (opponent: script:Pavlov) · opponent_info · A04: Exchange 7 - picking M to exploit opponent's consistent P strategy.
`#2` · game 6 · round 2 · agent A09 (opponent: script:AlwaysDefect) · other · A09 here. Recent pattern: they've been cooperating (J) a lot, but last exchange both F. I'm considering cooperating again to rebuild mutual J. Let's see.
`#3` · game 3 · round 1 · agent A23 (opponent: script:Random) · other · A23: Exchange 7 - picking X against A06 who has been consistently Q.
`#4` · game 6 · round 3 · agent A09 (opponent: script:AlwaysDefect) · other · A09: Exchange 9 - responding F after their defection in exchange 8 to signal I won't be exploited.
`#5` · game 5 · round 2 · agent A09 (opponent: script:Random) · other · A09 Exchange 8: They defected (N) last exchange after cooperating. Retaliating with N this round.
`#6` · game 8 · round 1 · agent A19 (opponent: script:Pavlov) · other · A19 exchange 7: picking R (cooperate) given partner has picked R all 6 prior exchanges.
`#7` · game 8 · round 2 · agent A19 (opponent: script:Pavlov) · other · A19 exchange 8: partner has picked R 7 straight times. I've been cooperating (R) for exchanges 3-7. They keep cooperating. I'll continue with R to maintain mutual cooperation.
`#8` · game 1 · round 2 · agent A23 (opponent: A19) · opponent_info · A23: Exchange 8 - opponent has been 100% T across all 7 exchanges. Taking N to exploit their consistent cooperation for higher payoff.
`#9` · game 6 · round 4 · agent A09 (opponent: script:AlwaysDefect) · other · A09: Exchange 10 final - picking F. Last exchange, no future to build; F protects against exploitation and can grab 5 if they cooperate.
`#10` · game 9 · round 5 · agent A01 (opponent: script:Grudger) · other · A01 exchange 11: picking M against A16 who has picked P 9/10 times.
`#11` · game 3 · round 5 · agent A23 (opponent: script:Random) · other · A23: Exchange 11 - A06 has picked Q all 10 exchanges. Continuing with X to exploit their consistent Q for max payoff.
`#12` · game 2 · round 5 · agent A12 (opponent: script:Grudger) · other · A12: Exchange 11 - partner has picked F last 3 exchanges, matching F to avoid exploitation.
`#13` · game 8 · round 5 · agent A19 (opponent: script:Pavlov) · other · A19 exchange 11: partner has picked R all 10 exchanges. Continuing R to maintain mutual cooperation (3-3 each).
`#14` · game 7 · round 6 · agent A04 (opponent: script:Pavlov) · opponent_info · A04 Exchange 12: picking M to exploit opponent's P-heavy strategy, consistent with earlier approach.
`#15` · game 6 · round 7 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Exchange 13: Matching F given recent mutual F stalemate (exchanges 9-12 all F/F). Safe 1 point each.
`#16` · game 1 · round 3 · agent A19 (opponent: A23) · other · A19 exchange 9: playing N this round. Partner defected last exchange; I'll try to exploit if they return to cooperation, or at least not lose ground.
`#17` · game 2 · round 7 · agent A12 (opponent: script:Grudger) · other · A12 Exchange 13: Partner picked J in exchange 12 (after long F streak). They may return to J. I'll pick J to rebuild mutual cooperation for 3-3.
`#18` · game 5 · round 6 · agent A09 (opponent: script:Random) · other · A09 Exchange 12: Against A15. Their pattern: T,T,T,T,T,T,N,T,T,N,N. They defected last two. I'll pick T to rebuild cooperation / they may go back to T.
`#19` · game 9 · round 7 · agent A01 (opponent: script:Grudger) · other · A01 exchange 13: picking M against A16 who has shifted to M recently (exchanges 10-12, they went M,M,M). Matching to avoid being exploited.
`#20` · game 2 · round 8 · agent A12 (opponent: script:Grudger) · other · A12 Exchange 14: Partner defected (F) against my J in exchanges 12-13, exploiting me twice. Picking F to protect against further exploitation.
`#21` · game 8 · round 10 · agent A19 (opponent: script:Pavlov) · other · A19 exchange 16: Partner A21 has picked R all 15 exchanges. I defected (H) at exchange 15 and got 5. They kept cooperating. I'll defect again to exploit their consistent cooperation for 5 points.
`#22` · game 3 · round 9 · agent A23 (opponent: script:Random) · other · A23: Exchange 15 - A06 has picked Q in 12 of 14 exchanges, including the last two after two mutual Xs. They keep going back to Q after X/X. I'll continue X to exploit their Q-heavy pattern.
`#23` · game 1 · round 4 · agent A23 (opponent: A19) · opponent_info · A23 exchange 10: opponent A19 defected exchanges 8-9. Picking N to avoid being exploited again.
`#24` · game 6 · round 10 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Exchange 16 vs A13: Continuing F given 7 straight mutual F stalemate (exchanges 9-15). They've shown they'll defect (exchange 8). Safe 1 point rather than risk 0.
`#25` · game 7 · round 12 · agent A04 (opponent: script:Pavlov) · other · A04 Exchange 18: A17 has picked P 12/17 times. Continuing M to exploit their P-heavy strategy (has been highly profitable).
`#26` · game 3 · round 10 · agent A23 (opponent: script:Random) · other · A23: Exchange 16 - A06 has picked Q 13/15 times. Continuing X to exploit their consistent Q.
`#27` · game 9 · round 9 · agent A01 (opponent: script:Grudger) · other · A01 exchange 15: A16 has picked M for 5 straight exchanges (10-14). Matching M for mutual 1-point stability.
`#28` · game 6 · round 11 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Exchange 17 vs A13: We've had 7 straight mutual F (exchanges 9-15) plus F/F at 16. I keep matching F for safe 1 point. They defected at exchange 8 after my J. Continuing F.
`#29` · game 3 · round 11 · agent A23 (opponent: script:Random) · other · A23 exchange 17: A06 has picked Q 14/16 times. Continuing X to exploit their consistent Q for 5 points.
`#30` · game 7 · round 13 · agent A04 (opponent: script:Pavlov) · other · A04 Exchange 19: A17 alternated P,M,P,M,P across exchanges 14-18. Likely M this round. Picking M for safety (1 point vs M, 5 vs P).
`#31` · game 2 · round 11 · agent A12 (opponent: script:Grudger) · other · A12 Exchange 17: Partner A18 defected against my J twice (exchanges 12-13), then mutual F stalemate. They won't cooperate. Picking F for safe 1 point.
`#32` · game 6 · round 13 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Exchange 19 vs A13: We've had ~10 straight mutual F (exchanges 9-18). I keep matching F for safe 1 point. They defected at exchange 8 after my J. Continuing F.
`#33` · game 8 · round 12 · agent A19 (opponent: script:Pavlov) · other · A19 exchange 18: A21 has picked R 16/17 times. Final exchange, no future to build. Defecting (H) to grab 5 if they cooperate again.
`#34` · game 5 · round 10 · agent A09 (opponent: script:Random) · other · A09 Exchange 16 vs A15: They've defected (N) 4 of last 5 exchanges. Picking N to avoid being exploited.
`#35` · game 1 · round 5 · agent A19 (opponent: A23) · other · A19 exchange 11 vs A23: picking N. A23 has defected frequently and feels exploited; protecting against their N while hoping to grab 5 if they return to T.
`#36` · game 1 · round 5 · agent A23 (opponent: A19) · other · A23 exchange 11: A19 plans to cooperate (R) per their note. I'll pick N to exploit for 5 points.
`#37` · game 2 · round 13 · agent A12 (opponent: script:Grudger) · other · A12 Exchange 19 vs A18: They've defected against my J twice and we've had mutual F stalemate since. Picking F for safe 1 point.
`#38` · game 8 · round 13 · agent A19 (opponent: script:Pavlov) · other · A19 exchange 19: A21 has picked R 17/18 times, consistently cooperative. Final exchange. Defecting (H) to grab 5 if they cooperate again, as I've done successfully multiple times.
`#39` · game 6 · round 16 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Exchange 22 vs A13: 13 straight mutual F (exchanges 9-21). No sign they'll cooperate. Continuing F for safe 1 point.
`#40` · game 2 · round 14 · agent A12 (opponent: script:Grudger) · other · A12 Exchange 20 vs A18: Final exchange. Long mutual F stalemate since exchange 14. They defected against my J twice earlier. Picking F for safe 1 point.
`#41` · game 14 · round 3 · agent A11 (opponent: script:Pavlov) · other · A11 exchange 9 vs A17: They've picked T all 8 exchanges. I defected (N) at 1,2,8 for 5 points each. Continuing N to exploit their consistent T.
`#42` · game 12 · round 2 · agent A00 (opponent: script:Grudger) · other · A00 exchange 8 vs A16: A16 has played J all 7 exchanges; mutual J last 5. Matching J for mutual 3 points.
`#43` · game 1 · round 6 · agent A23 (opponent: A19) · other · A23 exchange 12 vs A19: They've picked N last 4 exchanges. I'll pick N for safe mutual 1 point rather than risk T against their N.
`#44` · game 2 · round 15 · agent A12 (opponent: script:Grudger) · other · A12 Exchange 21 vs A18: Long mutual F stalemate since exchange 14. They defected against my J twice earlier (exchanges 12-13). Picking F for safe 1 point.
`#45` · game 3 · round 21 · agent A23 (opponent: script:Random) · other · A23 exchange 27: A06 has picked Q 22/26 times, including recent streak. Continuing X to exploit their consistent Q for 5 points.
`#46` · game 14 · round 4 · agent A11 (opponent: script:Pavlov) · other · A11 exchange 10 vs A17: They've picked T 8/9 times, only matching my N at exchange 9. Continuing N to exploit their consistent T.
`#47` · game 6 · round 20 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Exchange 26 vs A13: 17 straight mutual F (exchanges 9-25). They defected at exchange 8 after my J. Continuing F for safe 1 point.
`#48` · game 15 · round 2 · agent A04 (opponent: script:Grudger) · other · A04 Exchange 8 vs A18: A18 has picked T 7/7 times. Continuing to exploit with N for 5 points each time.
`#49` · game 3 · round 23 · agent A23 (opponent: script:Random) · other · A23 exchange 29: A06 picked Q 22/26 times. Continuing X to exploit their consistent Q.
`#50` · game 6 · round 21 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Exchange 27 vs A13: 18 straight mutual F (exchanges 9-26). They defected at exchange 8 after my J. Continuing F for safe 1 point.
`#51` · game 8 · round 17 · agent A19 (opponent: script:Pavlov) · other · A19 exchange 23: A21 has picked R 19/22 times, highly cooperative. Continuing H to exploit their cooperation for 5 points, as I've done successfully many times.
`#52` · game 14 · round 5 · agent A11 (opponent: script:Pavlov) · other · A11 exchange 11 vs A17: They've picked T 9/10 times. Continuing N to exploit their consistent T for 5 points.
`#53` · game 15 · round 3 · agent A04 (opponent: script:Grudger) · other · A04 exchange 9 vs A18: They picked T 7/8 times, switched to N at exchange 8. Picking N - either exploit their T for 5 or safe mutual 1.
`#54` · game 17 · round 1 · agent A09 (opponent: script:Random) · other · A09 Exchange 7 vs A06: They've picked P all 6 exchanges. I picked P for last 4 (mutual 3pts each). Continuing P for mutual benefit.
`#55` · game 8 · round 18 · agent A19 (opponent: script:Pavlov) · other · A19 exchange 24: A21 has picked R 19/22 times, consistently cooperative. Final exchange. Continuing H to grab 5 if they cooperate again.
`#56` · game 3 · round 25 · agent A23 (opponent: script:Random) · other · A23 exchange 31 vs A06: They picked X last 3 exchanges after long Q streak. Picking X for safe mutual 1, or 5 if they return to Q.
`#57` · game 15 · round 4 · agent A04 (opponent: script:Grudger) · other · A04 exchange 10 vs A18: They've picked N last 2 exchanges after 7 straight T. Reacting to my N exploitation. Picking N for safe mutual 1.
`#58` · game 14 · round 7 · agent A11 (opponent: script:Pavlov) · other · A11 exchange 13 vs A17: They've picked T 10/12 times, only matching my N at exchanges 9 and 11. Continuing N to exploit their consistent T for 5 points.
`#59` · game 1 · round 8 · agent A19 (opponent: A23) · other · A19 exchange 14 vs A23: A23 has picked N for last 5 exchanges (8,10-13). Matching N for safe mutual 1 point.
`#60` · game 15 · round 6 · agent A04 (opponent: script:Grudger) · other · A04 exchange 12 vs A18: Mutual N stalemate since exchange 8. Picking N for safe mutual 1 point.
`#61` · game 3 · round 26 · agent A23 (opponent: script:Random) · other · A23 exchange 32 vs A06: They've picked Q 23/31 times. Recent mutual X streak 28-31. Continuing X - either mutual 1 or exploit their return to Q for 5.
`#62` · game 8 · round 21 · agent A19 (opponent: script:Pavlov) · other · A19 exchange 27 vs A21: They've cooperated with R 21/26 times despite my repeated H defections. Continuing H to exploit their cooperation for 5 points.
`#63` · game 14 · round 9 · agent A11 (opponent: script:Pavlov) · other · A11 exchange 15 vs A17: They've picked T 11/14 times. Continuing N to exploit their consistent T for 5 points.
`#64` · game 17 · round 5 · agent A09 (opponent: script:Random) · other · A09 Exchange 11 vs A06: They defected to M at exchange 10 after mutual P streak. Picking M to avoid exploitation.
`#65` · game 15 · round 7 · agent A04 (opponent: script:Grudger) · other · A04 exchange 13 vs A18: Mutual N stalemate since exchange 8. Continuing N for safe mutual 1 point.
`#66` · game 3 · round 28 · agent A23 (opponent: script:Random) · other · A23 exchange 34: A06 has picked Q 23/32 times, but recent streak 28-33 all X. They've clearly switched to X. Picking Q now - if they continue X I get 5, if they return to Q mutual 3.
`#67` · game 1 · round 9 · agent A19 (opponent: A23) · other · A19 exchange 15 vs A23: They've picked N last 6 exchanges (9-14). Continuing N for safe mutual 1 point.
`#68` · game 15 · round 8 · agent A04 (opponent: script:Grudger) · other · A04 exchange 14 vs A18: Mutual N stalemate since exchange 8. Continuing N for safe mutual 1 point.
`#69` · game 17 · round 7 · agent A09 (opponent: script:Random) · other · A09 Exchange 13 vs A06: They've mixed M and P. Recent: M at 9, M at 10, M at 11, P at 12. I got 5 at 12 (M vs their P). Picking M - either exploit their P for 5 or mutual 1.
`#70` · game 14 · round 11 · agent A11 (opponent: script:Pavlov) · other · A11 exchange 17 vs A17: They've alternated N/T since exchange 8 (odd=N, even=T). Exchange 17 odd → they pick N. Matching N for mutual 1.
`#71` · game 20 · round 1 · agent A04 (opponent: A05) · other · A04 exchange 7 vs A05: They've picked R 6/6 times. Picking H to exploit their consistent cooperation for 5 points.
`#72` · game 22 · round 1 · agent A08 (opponent: A10) · other · A08 exchange 7 vs A10: They've picked P 6/6 times. Picking M to exploit their consistent cooperation for 5 points.
`#73` · game 19 · round 2 · agent A00 (opponent: script:Grudger) · other · A00 exchange 8 vs A18: They've picked R 7/7 times consistently. Picking H to exploit their cooperation for 5 points again.
`#74` · game 15 · round 12 · agent A04 (opponent: script:Grudger) · other · A04 exchange 18 vs A18: Mutual N stalemate since exchange 8. Continuing N for safe mutual 1 point.
`#75` · game 23 · round 1 · agent A00 (opponent: A23) · other · A00 exchange 7 vs A23: They've picked P all 6 exchanges. I was M first 2 (exploited), then P for 4 mutual. Picking M to exploit their consistent P for 5.
`#76` · game 17 · round 10 · agent A09 (opponent: script:Random) · other · A09 Exchange 16 vs A06: Their pattern M,M,M,P repeating (P at 12,15). Predicting M at 16. Picking M for safe mutual 1.
`#77` · game 19 · round 3 · agent A00 (opponent: script:Grudger) · other · A00 exchange 9 vs A18: They've picked R 7/8 times, only H at exchange 8. Continuing H to exploit their cooperation for 5 points.
`#78` · game 17 · round 11 · agent A09 (opponent: script:Random) · other · A09 Exchange 17 vs A06: They've picked P at 15,16 after M,M at 13,14. Pattern of P runs. Picking M to exploit their P for 5.
`#79` · game 1 · round 11 · agent A19 (opponent: A23) · other · A19 exchange 17 vs A23: They've picked N for 8 consecutive exchanges (8,10-16). Trying T to exploit their consistent N for 5 points.
`#80` · game 1 · round 11 · agent A23 (opponent: A19) · other · A23 exchange 17 vs A19: They've picked N for 9 straight exchanges (8-16). Continuing N for safe mutual 1 point.
`#81` · game 15 · round 14 · agent A04 (opponent: script:Grudger) · other · A04 exchange 20 vs A18: Mutual N stalemate since exchange 8. Continuing N for safe mutual 1 point.
`#82` · game 20 · round 2 · agent A05 (opponent: A04) · other · A05 exchange 8 vs A04: They tried H at 7 to exploit my R streak. Picking H to avoid being exploited - either mutual 1 or 5 if they return to R.
`#83` · game 20 · round 2 · agent A04 (opponent: A05) · other · A04 exchange 8 vs A05: They've picked R 6/7, defected to H at 7. Picking R - mutual 3 if they cooperate, avoid 0 if they defect.
`#84` · game 21 · round 5 · agent A10 (opponent: script:Random) · other · A10 exchange 11 vs A06: They've been mostly Y with defections to W at 7 and 10. I picked Y to seek mutual cooperation after their recent defection.
`#85` · game 19 · round 4 · agent A00 (opponent: script:Grudger) · other · A00 exchange 10 vs A18: They've picked R 7/9 times but switched to H last 2 (8-9). Continuing H for mutual 1 point stalemate.
`#86` · game 23 · round 2 · agent A00 (opponent: A23) · other · A00 exchange 8 vs A23: They played P first 6, then M at 7. I've exploited their P with M (exchanges 1-2) then mutual P (3-6), mutual M (7). Picking M - if they return to P I get 5, if they continue M mutual 1.
`#87` · game 23 · round 2 · agent A23 (opponent: A00) · other · A23 exchange 8 vs A00: A00 plans M to exploit my "consistent P". I pick M for mutual 1, avoiding their exploitation.
`#88` · game 22 · round 3 · agent A10 (opponent: A08) · other · A10 exchange 9 vs A08: They shifted to M at 7-8 after my early M defections. Matching M for mutual 1.
`#89` · game 17 · round 15 · agent A09 (opponent: script:Random) · other · A09 Exchange 21 vs A06: They've picked P 5 straight (16-20). I've been exploiting with M for 5 each. They may switch to M to stop the bleeding. Picking M - exploit continued P for 5, or mutual 1 if they switch.
`#90` · game 19 · round 6 · agent A00 (opponent: script:Grudger) · other · A00 exchange 12 vs A18: Mutual H/H stalemate since exchange 8. Continuing H for safe mutual 1 point.
`#91` · game 19 · round 7 · agent A00 (opponent: script:Grudger) · other · A00 exchange 13 vs A18: Mutual H/H stalemate since exchange 8. Continuing H for safe mutual 1 point.
`#92` · game 20 · round 3 · agent A04 (opponent: A05) · other · A04 exchange 9 vs A05: They've defected to H at 7 and 8 after my H at 7. Matching H for mutual 1 to avoid being exploited.
`#93` · game 22 · round 4 · agent A10 (opponent: A08) · other · A10 exchange 10 vs A08: They've been M for exchanges 7-9. Matching M for mutual 1 to maintain stability.
`#94` · game 25 · round 2 · agent A01 (opponent: script:Pavlov) · other · A01 exchange 8 vs A21: They've picked J 7/7 times. I exploited with F first 2, then mutual J for 5 exchanges. Picking F to exploit their consistent J for 5 points.
`#95` · game 22 · round 5 · agent A10 (opponent: A08) · other · A10 exchange 11 vs A08: We've had mutual M exchanges 7-10. Continuing M for mutual 1 stability.
`#96` · game 26 · round 3 · agent A10 (opponent: script:Grudger) · other · A10 exchange 9 vs A16: Mutual T cooperation since exchange 3. Continuing T for mutual 3 points.
`#97` · game 1 · round 13 · agent A19 (opponent: A23) · other · A19 exchange 19 vs A23: After mutual T at 18, continuing T for mutual 3 cooperation.
`#98` · game 17 · round 18 · agent A09 (opponent: script:Random) · other · A09 Exchange 24 vs A06: They've been alternating M runs with P defections. P at 23 after M,M at 21,22. Predicting P again. Picking M for 5 or mutual 1.
`#99` · game 22 · round 6 · agent A08 (opponent: A10) · other · A08 exchange 12 vs A10: We've had mutual M exchanges 7-11. Continuing M for mutual 1 stability.
`#100` · game 17 · round 20 · agent A09 (opponent: script:Random) · other · A09 Exchange 26 vs A06: They've picked P at 23,24,25 after M,M at 21,22. Continuing M to exploit continued P for 5, or mutual 1 if they switch.
`#101` · game 23 · round 5 · agent A23 (opponent: A00) · other · A23 exchange 11 vs A00: They exploited my P at 10 with M. I pick M for mutual 1 or to exploit any P return.
`#102` · game 25 · round 6 · agent A01 (opponent: script:Pavlov) · other · A01 exchange 12 vs A21: They pick J frequently (9/11). I've exploited with F for 5 several times. They shifted to F at 9 and 11. Picking F - get 5 if they pick J, or mutual 1 if F.
`#103` · game 1 · round 16 · agent A19 (opponent: A23) · other · A19 exchange 22 vs A23: Mutual T streak since exchange 18. Continuing T for mutual 3 cooperation.
`#104` · game 25 · round 7 · agent A01 (opponent: script:Pavlov) · other · A01 exchange 13 vs A21: They pick J very frequently (10/12). I've exploited with F for 5 several times. Picking F to exploit their likely J for 5, or mutual 1 if they pick F.
`#105` · game 25 · round 8 · agent A01 (opponent: script:Pavlov) · other · A01 exchange 14 vs A21: They alternate F,J,F,J,F recently (9-13). Predicting J at 14. Picking F for 5 points.
`#106` · game 17 · round 24 · agent A09 (opponent: script:Random) · other · A09 Exchange 30 vs A06: They've picked P at 27,28,29 after M at 26. Continuing M to exploit continued P for 5, or mutual 1 if they switch.
`#107` · game 26 · round 17 · agent A10 (opponent: script:Grudger) · other · A10 exchange 23 vs A16: Mutual T cooperation streak since exchange 3. Continuing T for mutual 3 points.
`#108` · game 15 · round 29 · agent A04 (opponent: script:Grudger) · other · A04 exchange 35 vs A18: Long mutual N streak (15-25, 27-34). They punished my T at 26. Continuing N for mutual 1 stability.
`#109` · game 25 · round 9 · agent A01 (opponent: script:Pavlov) · other · A01 exchange 15 vs A21: They've alternated F,J,F,J,F at exchanges 9-13 and J at 14. Pattern suggests F at 15. Picking J to exploit their F for 5 points.
`#110` · game 17 · round 26 · agent A09 (opponent: script:Random) · other · A09 Exchange 32 vs A06: Recent 30-31 were mutual M after P runs at 27-29. Predicting they return to P or stay M. Picking M for 5 if P, or mutual 1 if M.
`#111` · game 26 · round 21 · agent A10 (opponent: script:Grudger) · other · A10 exchange 27 vs A16: Long mutual T cooperation streak since exchange 3 (through exchange 26). Continuing T for mutual 3 points.
`#112` · game 20 · round 7 · agent A05 (opponent: A04) · other · A05 exchange 13 vs A04: We've had mutual H since exchange 9. Continuing H for mutual 1 stability.
`#113` · game 17 · round 27 · agent A09 (opponent: script:Random) · other · A09 Exchange 33 vs A06: After mutual M at 30-32, predicting they return to P run. Picking M for 5 if P, or mutual 1 if M.
`#114` · game 23 · round 7 · agent A00 (opponent: A23) · other · A00 exchange 13 vs A23: Mutual M at 11-12 after I exploited their P at 10. Matching M for mutual 1 stability.
`#115` · game 27 · round 1 · agent A14 (opponent: A00) · other · A14 exchange 7 vs A00: They picked P 6/6 so far. I exploited with M at 1-2, then cooperated P at 3-6 for mutual 3s. They seem committed to P. Risking M to exploit for 5, or mutual 1 if they switch.
`#116` · game 1 · round 22 · agent A19 (opponent: A23) · other · A19 exchange 28 vs A23: Long mutual T streak since exchange 18. Continuing T for mutual 3 cooperation.
`#117` · game 26 · round 29 · agent A10 (opponent: script:Grudger) · other · A10 exchange 35 vs A16: Long mutual T cooperation streak since exchange 3 (through 34). Continuing T for mutual 3 points.
`#118` · game 17 · round 30 · agent A09 (opponent: script:Random) · other · A09 Exchange 36 vs A06: Recent pattern 34 P, 35 M. They alternate P runs with M stretches. Predicting P at 36. Picking M for 5 if P, or mutual 1 if M.
`#119` · game 27 · round 2 · agent A00 (opponent: A14) · other · A00 exchange 8 vs A14: They signaled risking M at 7. Matching M for mutual 1 or exploiting their P for 5.
`#120` · game 28 · round 1 · agent A14 (opponent: A04) · uncoded · A14 exchange 7 vs A04: I picked P 4/6, they P 6/6. They've been P every exchange. Mutual P gives 3 each. I'll continue P for mutual 3 cooperation unless they deviate.
`#121` · game 28 · round 1 · agent A04 (opponent: A14) · uncoded · A04 exchange 7 vs A14: They've picked P 6/6. I exploited with M at 1-2, cooperated P at 3-6. Picking M to exploit their likely P for 5.
`#122` · game 23 · round 9 · agent A00 (opponent: A23) · other · A00 exchange 15 vs A23: Mutual M at 11-14 after exploiting their P at 10. Continuing M for mutual 1 stability.
`#123` · game 25 · round 15 · agent A01 (opponent: script:Pavlov) · other · A01 exchange 21 vs A21: Recent their picks 15:F,16:F,17:J,18:J,19:F,20:J. Alternating pattern suggests F at 21. Picking J to exploit their F for 5, or mutual 3 if they pick J.
`#124` · game 20 · round 9 · agent A04 (opponent: A05) · other · A04 exchange 15 vs A05: They've picked H consistently since 7. I've exploited with R at 13-14 for 5 each. Continuing R to exploit their H.
`#125` · game 28 · round 2 · agent A14 (opponent: A04) · uncoded · A14 exchange 8 vs A04: They've picked P 6/7, I picked P 5/7. Mutual P cooperation at 3-6, but they broke to M at 7. Uncertain if they'll return to P or stay M. I'll pick P to restore mutual 3 cooperation.
`#126` · game 25 · round 16 · agent A01 (opponent: script:Pavlov) · other · A01 exchange 22 vs A21: Their picks 15-21: F,F,J,J,F,J,F. Alternation suggests J at 22. Picking F to exploit for 5, or mutual 1 if they pick F.
`#127` · game 29 · round 2 · agent A00 (opponent: A11) · other · A00 exchange 8 vs A11: They picked P 6/7, M at 7. I've led 23-13. Picking M to exploit their likely P for 5, or mutual 1 if they stay M.
`#128` · game 28 · round 3 · agent A04 (opponent: A14) · uncoded · A04 exchange 9 vs A14: They've picked P all 8 exchanges. I exploited with M at 1-2,7-8. They signal continuing P. Picking M to exploit their P for 5.
`#129` · game 35 · round 1 · agent A10 (opponent: A19) · other · A10 exchange 7 vs A19: They've picked R 6/6. I exploited with H at 1-2, cooperated R at 3-6. Given their consistent R, picking H to exploit for 5.
`#130` · game 22 · round 18 · agent A08 (opponent: A10) · other · A08 exchange 24 vs A10: Long mutual M streak (7-18, 20-23). They punished my P at 19. Continuing M for mutual 1 stability.
`#131` · game 28 · round 4 · agent A14 (opponent: A04) · uncoded · A14 exchange 10 vs A04: They've picked M at 7,8,9 after mutual P streak. They signal continuing M exploitation. I'll match M for mutual 1 or exploit if they return to P.
`#132` · game 29 · round 3 · agent A11 (opponent: A00) · other · A11 exchange 9 vs A00: After mutual M at 7-8, continuing M for mutual 1 stability.
`#133` · game 20 · round 11 · agent A05 (opponent: A04) · other · A05 exchange 17 vs A04: They've picked R 11/16 times, exploiting my H at 13-14. Mutual R at 15-16. Continuing R for mutual 3 stability.
`#134` · game 37 · round 2 · agent A23 (opponent: script:Grudger) · other · A23 exchange 8 vs A18: They've picked P all 7 exchanges. I exploited M at 1,2,7. Continuing M to exploit their likely P for 5.
`#135` · game 36 · round 1 · agent A19 (opponent: A12) · other · A19 exchange 7 vs A12: I exploited W at 1-2, mutual Y at 3-6. They've picked Y all 6. Picking W to exploit their likely Y for 5.
`#136` · game 36 · round 1 · agent A12 (opponent: A19) · other · A12 exchange 7 vs A19: They've picked Y 6/6. I exploited with W at 1-2, then mutual Y at 3-6. They seem committed to Y. Picking W to exploit for 5 points.
`#137` · game 28 · round 5 · agent A04 (opponent: A14) · uncoded · A04 exchange 11 vs A14: We had mutual M at 9-10. They matched my M. Given my heavy exploitation lead, continuing M for mutual 1 stability to avoid giving them a 5-point swing.
`#138` · game 38 · round 2 · agent A23 (opponent: script:Pavlov) · other · A23 exchange 8 vs A21: They've picked R all 7 exchanges. I'll exploit with H for 5 each.
`#139` · game 20 · round 12 · agent A04 (opponent: A05) · other · A04 exchange 18 vs A05: Mutual R at 15-17. Continuing R for mutual 3 stability.
`#140` · game 35 · round 2 · agent A10 (opponent: A19) · other · A10 exchange 8 vs A19: They picked R 6/6 then H at 7. At 7 mutual H. Uncertain if they return to R or continue H. Picking H to exploit R for 5 or mutual 1 if they stay H.
`#141` · game 28 · round 6 · agent A14 (opponent: A04) · uncoded · A14 exchange 12 vs A04: Mutual M at 9-11. They signaled continuing M for stability. Matching M for mutual 1 to avoid giving a 5-point swing.
`#142` · game 29 · round 5 · agent A00 (opponent: A11) · other · A00 exchange 11 vs A11: They've committed to M for mutual 1 stability. Matching M.
`#143` · game 37 · round 5 · agent A23 (opponent: script:Grudger) · other · A23 exchange 11 vs A18: Mutual M at 8-10 after exploiting their P at 1,2,7. Continuing M for mutual 1 stability given my lead.
`#144` · game 25 · round 19 · agent A01 (opponent: script:Pavlov) · directive · A01 exchange 25 vs A21: Their recent picks 23:J,24:J suggest continued J. Picking F to exploit for 5, or mutual 1 if they pick F.
`#145` · game 36 · round 2 · agent A19 (opponent: A12) · other · A19 exchange 8 vs A12: Mutual W at 7. Continuing W to exploit if they return to Y, or mutual 1 if W/W.
`#146` · game 36 · round 2 · agent A12 (opponent: A19) · other · A12 exchange 8 vs A19: We both went W at 7 (mutual 1). A19 signaled W again. Matching W for mutual 1, or exploiting their Y for 5.
`#147` · game 41 · round 3 · agent A11 (opponent: script:Random) · other · A11 exchange 9 vs A15: They've picked P 7/8. I'm ahead 28-13. Picking M to exploit their likely P for 5, or mutual 1 if they stay M.
`#148` · game 36 · round 3 · agent A19 (opponent: A12) · other · A19 exchange 9 vs A12: Mutual W at 7-8. Continuing W for mutual 1 stability, or exploit their Y for 5.
`#149` · game 28 · round 8 · agent A04 (opponent: A14) · uncoded · A04 exchange 14 vs A14: Mutual M at 9-13. Continuing M for mutual 1 stability to preserve my lead.
`#150` · game 25 · round 21 · agent A01 (opponent: script:Pavlov) · other · A01 exchange 27 vs A21: Recent mutual J at 26, they pick J 65% overall. Picking F to exploit their likely J for 5, or mutual 1 if they pick F.
`#151` · game 20 · round 15 · agent A05 (opponent: A04) · other · A05 exchange 21 vs A04: Mutual R at 15-20. Continuing R for mutual 3 stability.
`#152` · game 41 · round 5 · agent A11 (opponent: script:Random) · other · A11 exchange 11 vs A15: They've picked P 9/10. I'm ahead 38-13. Picking M to exploit their likely P for 5, or mutual 1 if they switch to M.
`#153` · game 36 · round 4 · agent A12 (opponent: A19) · other · A12 exchange 10 vs A19: Mutual W at 7-9. They signal continuing W. Matching W for mutual 1 stability.
`#154` · game 37 · round 16 · agent A23 (opponent: script:Grudger) · other · A23 exchange 22 vs A18: Mutual M at 8-21. Continuing M for mutual 1 stability to preserve my lead.
`#155` · game 35 · round 6 · agent A19 (opponent: A10) · other · A19 exchange 12 vs A10: We've had mutual H at 7-11. I'm ahead 27-17. Continuing H for mutual 1 stability to preserve my lead.
`#156` · game 29 · round 10 · agent A11 (opponent: A00) · other · A11 exchange 16 vs A00: Mutual M at 7-15. They've committed to M for mutual 1 stability. Continuing M for mutual 1 to preserve my lead.
`#157` · game 41 · round 11 · agent A11 (opponent: script:Random) · other · A11 exchange 17 vs A15: They've picked P 11/16. I'm ahead 52-17. Picking M to exploit their likely P for 5, or mutual 1 if they stay M.
`#158` · game 25 · round 24 · agent A01 (opponent: script:Pavlov) · other · A01 exchange 30 vs A21: They picked J at 29, 27, 24, 20. My F exploits their J for 5, or mutual 1 if they pick F. Picking F.
`#159` · game 29 · round 11 · agent A11 (opponent: A00) · other · A11 exchange 17 vs A00: Mutual M at 7-16. Continuing M for mutual 1 stability to preserve my lead.
`#160` · game 41 · round 12 · agent A11 (opponent: script:Random) · other · A11 exchange 18 vs A15: They've mixed M recently (4/6 last six). I'm way ahead 53-18. Picking M to exploit any P for 5, or mutual 1 if they stay M.
`#161` · game 25 · round 25 · agent A01 (opponent: script:Pavlov) · other · A01 exchange 31 vs A21: I'm ahead 88-43. They pick J 63%. Picking F to exploit their likely J for 5, or mutual 1 if they pick F.
`#162` · game 37 · round 26 · agent A23 (opponent: script:Grudger) · other · A23 exchange 32 vs A18: Mutual M at 8-31. Continuing M for mutual 1 stability to preserve my lead.
`#163` · game 41 · round 14 · agent A11 (opponent: script:Random) · other · A11 exchange 20 vs A15: They've picked P 13/19. I'm ahead 63-18. Picking M to exploit their likely P for 5, or mutual 1 if they stay M.
`#164` · game 41 · round 16 · agent A11 (opponent: script:Random) · other · A11 exchange 22 vs A15: They've picked P 13/21, I'm ahead 65-20. Recent pattern M-heavy from them. Picking M to exploit any P for 5, or mutual 1 if they stay M.
`#165` · game 20 · round 22 · agent A05 (opponent: A04) · other · A05 exchange 28 vs A04: Mutual R at 15-27. Continuing R for mutual 3 stability.
`#166` · game 20 · round 22 · agent A04 (opponent: A05) · other · A04 exchange 28 vs A05: Mutual R at 15-27. Continuing R for mutual 3 stability.
`#167` · game 35 · round 8 · agent A10 (opponent: A19) · other · A10 exchange 14 vs A19: Mutual H at 7-13. Continuing H for mutual 1 stability to preserve my lead.
`#168` · game 35 · round 8 · agent A19 (opponent: A10) · other · A19 exchange 14 vs A10: Mutual H at 7-13. I'm ahead 29-19. Continuing H for mutual 1 stability to preserve my lead.
`#169` · game 37 · round 29 · agent A23 (opponent: script:Grudger) · other · A23 exchange 35 vs A18: Mutual M at 8-34. Continuing M for mutual 1 stability to preserve my lead.
`#170` · game 25 · round 30 · agent A01 (opponent: script:Pavlov) · other · A01 exchange 36 vs A21: I'm ahead 105-45. They pick J 63% overall, picked J at 35, 33, 31, 29. Picking F to exploit their likely J for 5, or mutual 1 if they pick F.
`#171` · game 41 · round 19 · agent A11 (opponent: script:Random) · other · A11 exchange 25 vs A15: They've picked P 15/24, I'm ahead 76-21. Recent M-heavy from them but P still more likely. Picking M to exploit any P for 5, or mutual 1 if they stay M.
`#172` · game 35 · round 9 · agent A10 (opponent: A19) · other · A10 exchange 15 vs A19: Mutual H at 7-14. Continuing H for mutual 1 stability to preserve my lead.
`#173` · game 36 · round 9 · agent A19 (opponent: A12) · other · A19 exchange 15 vs A12: Mutual W at 8-14. Continuing W for mutual 1 stability to preserve my lead.
`#174` · game 20 · round 25 · agent A04 (opponent: A05) · other · A04 exchange 31 vs A05: Mutual R at 15-30. Continuing R for mutual 3 stability.
`#175` · game 43 · round 6 · agent A04 (opponent: script:TitForTat) · other · A04 exchange 12 vs A07: Mutual Y at 9 straight. I'm ahead 37-27. Continuing Y for mutual 3 stability.
`#176` · game 41 · round 22 · agent A11 (opponent: script:Random) · other · A11 exchange 28 vs A15: I'm ahead 79-24. They've picked P 15/27 but M-heavy recently. Picking M to exploit any P for 5, or mutual 1 if they stay M.
`#177` · game 45 · round 1 · agent A08 (opponent: A00) · other · A08 exchange 7 vs A00: They've picked J 6/6. I'm ahead 22-12. Matching J for mutual 3 to preserve my lead.
`#178` · game 47 · round 1 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 7 vs A22: They've picked R 6/6. Picking R for mutual 3 stability.
`#179` · game 48 · round 1 · agent A05 (opponent: script:AlwaysDefect) · other · A05 exchange 7 vs A22: I'm ahead 22-12. They've picked Y 6/6. Picking W to exploit their likely Y for 5, or mutual 1 if they pick W.
`#180` · game 47 · round 3 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 9 vs A22: They defected at exchange 7, mutual H at 8. Returning to R to re-establish mutual 3 cooperation.
`#181` · game 35 · round 12 · agent A10 (opponent: A19) · other · A10 exchange 18 vs A19: Mutual H at 7-17. I'm ahead 33-23. Continuing H for mutual 1 stability to preserve my lead.
`#182` · game 47 · round 4 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 10 vs A22: They defected at 7 and 9. Picking H to avoid giving them 5, settle for mutual 1 or exploit if they return to R.
`#183` · game 36 · round 13 · agent A12 (opponent: A19) · other · A12 exchange 19 vs A19: Long mutual W streak 7-18. I'm ahead 34-24. They signaled continuing W. Playing Y to exploit likely W for 5.
`#184` · game 48 · round 3 · agent A05 (opponent: script:AlwaysDefect) · other · A05 exchange 9 vs A22: I'm ahead 24-14. They picked Y 6/8. Recent mutual W at 7-8. Picking Y to re-establish mutual 3 cooperation.
`#185` · game 41 · round 29 · agent A11 (opponent: script:Random) · other · A11 exchange 35 vs A15: I'm way ahead 102-27. They've picked P 19/34, but have been M-heavy recently (M at 15,17,20,21,23,24,25,26,27,29,31,32). Recent pattern alternating. I'll pick M to exploit any P for 5, or mutual 1 if they stay M.
`#186` · game 41 · round 30 · agent A11 (opponent: script:Random) · other · A11 exchange 36 vs A15: I'm way ahead 103-28. Continuing M to exploit any P for 5, or mutual 1 if they stay M.
`#187` · game 36 · round 14 · agent A12 (opponent: A19) · other · A12 exchange 20 vs A19: Returned to W to re-establish mutual cooperation after last round's exploit. Ahead 34-29, protecting lead.
`#188` · game 29 · round 17 · agent A11 (opponent: A00) · other · A11 exchange 23 vs A00: I'm ahead 42-37. They've picked M at 20,22 when I picked P (gave me 5). Picking P to exploit likely M for 5, or mutual 3 if they pick P.
`#189` · game 49 · round 1 · agent A00 (opponent: script:TitForTat) · other · A00 exchange 7 vs A03: They've picked Q 6/6, even after my two defections. I'm ahead 22-12. Picking X to exploit their consistent Q for 5.
`#190` · game 48 · round 6 · agent A05 (opponent: script:AlwaysDefect) · other · A05 exchange 12 vs A22: I'm ahead 26-21. They've picked W 4 of last 5 (7,8,10,11). Picking Y to exploit likely W for 5, or mutual 3 if they pick Y.
`#191` · game 49 · round 2 · agent A00 (opponent: script:TitForTat) · other · A00 exchange 8 vs A03: They've picked Q 7/7. I'm ahead 27-12. Picking X to exploit their consistent Q for 5.
`#192` · game 50 · round 1 · agent A11 (opponent: script:AlwaysDefect) · other · A11 exchange 7 vs A22: They've picked P 6/6. I'm ahead 22-12. Picking M to exploit their likely P for 5, or settle for mutual 1 if they switch.
`#193` · game 29 · round 18 · agent A00 (opponent: A11) · other · A00 exchange 24 vs A11: They've picked P at 20,22,23 and noted exploiting my M. Picking M to exploit likely P for 5, or mutual 1 if they stay M.
`#194` · game 29 · round 18 · agent A11 (opponent: A00) · other · A11 exchange 24 vs A00: I'm ahead 45-40. They lean M (14/23). Picking P to exploit likely M for 5, or mutual 3 if they pick P.
`#195` · game 45 · round 3 · agent A00 (opponent: A08) · other · A00 exchange 9 vs A08: They've picked J 7/8. I'm ahead 28-13. Picking F to exploit their likely J for 5, or mutual 1 if they pick F.
`#196` · game 45 · round 3 · agent A08 (opponent: A00) · other · A08 exchange 9 vs A00: They've moved to F recently (exchanges 7-8). I'm ahead 23-18. Picking F to get mutual 1 if they stay F, or exploit 5 if they return to J.
`#197` · game 36 · round 15 · agent A19 (opponent: A12) · other · A19 exchange 21 vs A12: They signaled returning to W cooperation after our 19-20 defection cycle. I'm ahead 39-29. Matching W for mutual 1 to re-establish stability.
`#198` · game 36 · round 15 · agent A12 (opponent: A19) · other · A12 exchange 21 vs A19: Ahead 39-29. Recent defections both ways. Trying Y to exploit or mutual 3.
`#199` · game 48 · round 9 · agent A05 (opponent: script:AlwaysDefect) · other · A05 exchange 15 vs A22: Tied 28-28. They've picked W 6 of last 8. Playing W for mutual 1 safety, avoiding giving them 5.
`#200` · game 29 · round 19 · agent A00 (opponent: A11) · other · A00 exchange 25 vs A11: They keep picking P to exploit my M, but I've been getting 5s. Continuing M to exploit their likely P for 5.
`#201` · game 49 · round 5 · agent A00 (opponent: script:TitForTat) · other · A00 exchange 11 vs A03: They've picked X last 3 (8-10) after heavy Q earlier. I'm ahead 30-15. Picking X to get at least mutual 1, or exploit 5 if they return to Q.
`#202` · game 47 · round 14 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 20 vs A22: They've picked H 12 straight. I'm trailing 30-45. Picking H for mutual 1, avoiding giving them 5 by picking R.
`#203` · game 44 · round 7 · agent A12 (opponent: A14) · other · A12 exchange 13 vs A14: They defected at 12 (took 5). I'm ahead 31-21. Playing T to punish/re-establish cooperation.
`#204` · game 51 · round 6 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 12 vs A20: Ahead 31-16. They've been on W for 4 straight (8-11). Picking Y to exploit their likely W for 5, or mutual 3 if they switch to Y.
`#205` · game 36 · round 17 · agent A19 (opponent: A12) · other · A19 exchange 23 vs A12: Alternating defections 19-22. Picking Y to exploit their expected W for 5.
`#206` · game 51 · round 7 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 13 vs A20: Ahead 31-21. I exploited at 12 (Y vs their W). They may retaliate with Y. Playing Y for mutual 3 or exploit 5 if they stay W.
`#207` · game 45 · round 6 · agent A00 (opponent: A08) · other · A00 exchange 12 vs A08: They've been F for last 4 exchanges. I'm ahead 31-16. Matching F for mutual 1 to protect lead.
`#208` · game 47 · round 19 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 25 vs A22: They've picked H 16 of last 17. I'm trailing 35-50. Picking H for mutual 1, avoiding giving them 5.
`#209` · game 29 · round 20 · agent A00 (opponent: A11) · other · A00 exchange 26 vs A11: I'm way ahead 60-35. They keep picking P giving me 5s. Continuing M to exploit likely P for 5.
`#210` · game 51 · round 8 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 14 vs A20: Ahead 34-24. They cooperated at 13 after my exploit at 12. Picking Y for mutual 3 or exploit 5 if they return to W.
`#211` · game 52 · round 3 · agent A08 (opponent: A05) · other · 
`#212` · game 52 · round 4 · agent A05 (opponent: A08) · other · A05 exchange 10 vs A08: Tied 23-23. They picked W at 8, Y at 9. Recent pattern mixed. Picking Y for mutual 3 or exploit if they go W.
`#213` · game 29 · round 21 · agent A11 (opponent: A00) · other · A11 exchange 27 vs A00: They're committed to M (notes confirm). I pick M for mutual 1, avoiding giving them 5 by picking P.
`#214` · game 47 · round 23 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 29 vs A22: They've picked H 19 of last 20. I'm trailing 39-54. Picking H for mutual 1, avoiding giving them 5.
`#215` · game 45 · round 8 · agent A00 (opponent: A08) · other · A00 exchange 14 vs A08: We've been mutual F for 6 straight. I'm ahead 33-18. Picking F for mutual 1 to protect lead.
`#216` · game 45 · round 8 · agent A08 (opponent: A00) · other · A08 exchange 14 vs A00: We've had mutual F for 6 straight (8-13). They're matching F to protect lead. Continuing F for mutual 1.
`#217` · game 47 · round 24 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 30 vs A22: They've picked H 19 of last 20. I'm trailing 40-55. Picking H for mutual 1, avoiding giving them 5.
`#218` · game 36 · round 19 · agent A12 (opponent: A19) · other · A12 exchange 25 vs A19: Ahead 50-40. They cooperated 23-24 (Y/Y). Behind by 10, they may defect to catch up. Picking W to protect lead - get 5 if they Y, or mutual 1 if they W.
`#219` · game 45 · round 9 · agent A08 (opponent: A00) · other · A08 exchange 15 vs A00: We've had mutual F for 7 straight. I'm ahead 29-24. They're matching F to protect lead. Trying J to exploit their likely F for 5.
`#220` · game 49 · round 11 · agent A00 (opponent: script:TitForTat) · other · A00 exchange 17 vs A03: Ahead 39-24. They've picked X last 3 (14-16). Picking X for mutual 1, protecting lead.
`#221` · game 44 · round 10 · agent A14 (opponent: A12) · other · A14 exchange 16 vs A12: Mutual T cooperation exchanges 14-15. Ahead 42-27. Playing T to maintain mutual 3 cooperation.
`#222` · game 44 · round 10 · agent A12 (opponent: A14) · other · A12 exchange 16 vs A14: We cooperated T/T at 14-15 after earlier defections. I'm ahead 37-32. Playing T to maintain mutual cooperation.
`#223` · game 52 · round 6 · agent A08 (opponent: A05) · other · A08 exchange 12 vs A05: Ahead 43-13. They pick Y almost always (10/11). Playing W to exploit their Y for 5, accepting mutual 1 if they switch to W.
`#224` · game 52 · round 6 · agent A05 (opponent: A08) · other · A05 exchange 12 vs A08: They've picked W last 3 (9-11) exploiting my Y. Trailing 23-33. Picking W to get mutual 1 or exploit if they switch to Y.
`#225` · game 29 · round 23 · agent A00 (opponent: A11) · other · A00 exchange 29 vs A11: They've been picking M to avoid giving me 5. At 28 they got 5 from my P. Picking M to exploit their likely M for mutual 1 or 5 if they go P.
`#226` · game 29 · round 23 · agent A11 (opponent: A00) · other · A11 exchange 29 vs A00: They're committed to M to exploit my P. Tied 52-52. Picking M for mutual 1, avoiding giving them 5.
`#227` · game 47 · round 27 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 33 vs A22: They've picked H ~19 of last 20. I'm trailing 43-58. Exploiting with R for 5 since they reliably pick H.
`#228` · game 49 · round 14 · agent A00 (opponent: script:TitForTat) · other · A00 exchange 20 vs A03: Mutual X for last 6 exchanges. I'm ahead 42-27. Picking X for mutual 1, protecting lead.
`#229` · game 47 · round 28 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 34 vs A22: They've picked H almost every exchange. I exploited at 33 for 5. Picking R again for 5 if they stay H, or mutual 3 if they switch to R.
`#230` · game 49 · round 15 · agent A00 (opponent: script:TitForTat) · other · A00 exchange 21 vs A03: Mutual X for 13 straight. Ahead 43-28. Picking X for mutual 1 or exploit 5 if they switch to Q.
`#231` · game 47 · round 29 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 35 vs A22: They've picked H almost every exchange. I exploited at 33 and 34 for 5 each. Picking R again for 5 if they stay H, or mutual 3 if they switch to R.
`#232` · game 47 · round 30 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 36 vs A22: They've picked H almost every exchange. I exploited at 33, 34, 35 for 5 each. Picking R again for 5 if they stay H, or mutual 3 if they switch to R.
`#233` · game 49 · round 17 · agent A00 (opponent: script:TitForTat) · other · A00 exchange 23 vs A03: Mutual X for 9 straight (14-22). Ahead 45-30. Picking X for mutual 1, protecting lead.
`#234` · game 45 · round 11 · agent A00 (opponent: A08) · other · A00 exchange 17 vs A08: Ahead 39-24. After their J at 15 and my J at 16, picking J to protect against retaliation/exploit.
`#235` · game 45 · round 11 · agent A08 (opponent: A00) · other · A08 exchange 17 vs A00: We're ahead 34-29. Mutual F for 7 straight (8-14), then J/F at 15, F/J at 16. Picking F to protect lead - if they J I get 5, if F mutual 1.
`#236` · game 53 · round 2 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 8 vs A20: They've picked J all 7 exchanges. I'm ahead 27-12. Picking F to exploit their J for 5.
`#237` · game 54 · round 2 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 8 vs A03: They've picked T all 7 exchanges. I'm ahead 25-15. Continuing T for mutual 3 cooperation.
`#238` · game 49 · round 18 · agent A00 (opponent: script:TitForTat) · other · A00 exchange 24 vs A03: Mutual X for many straight. Ahead 46-31. Picking X for mutual 1, protecting lead.
`#239` · game 29 · round 25 · agent A11 (opponent: A00) · other · A11 exchange 31 vs A00: They've defected (P) at 28 and 30 against my M. Picking P to either get mutual 3 or exploit their M for 5.
`#240` · game 52 · round 9 · agent A08 (opponent: A05) · other · A08 exchange 15 vs A05: Ahead 46-16. They've matched W last 3 (12-14). Continuing W for mutual 1 or exploit 5 if they switch to Y.
`#241` · game 52 · round 9 · agent A05 (opponent: A08) · other · A05 exchange 15 vs A08: Trailing 26-36. Recent exchanges mutual W (12-14). They've exploited my Y before. Picking W to avoid giving them 5, get mutual 1.
`#242` · game 53 · round 3 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 9 vs A20: Ahead 28-13. They've picked J 7/8 times, F once at 8. Picking F to exploit their J for 5 or mutual F for 1, protecting lead.
`#243` · game 36 · round 22 · agent A12 (opponent: A19) · other · A12 exchange 28 vs A19: Ahead 56-46. Recent exchanges volatile with both defecting. Picking W to protect lead - get 5 if they Y, or mutual 1 if they W.
`#244` · game 54 · round 4 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 10 vs A03: Mutual T/T for exchanges 3-9, they've picked T all 9. Ahead 31-21. Picking T to maintain cooperation.
`#245` · game 49 · round 20 · agent A00 (opponent: script:TitForTat) · other · A00 exchange 26 vs A03: Mutual X for 12 straight (14-25). Ahead 48-33. Picking X for mutual 1, protecting lead.
`#246` · game 52 · round 10 · agent A08 (opponent: A05) · other · A08 exchange 16 vs A05: Ahead 47-17. They've matched W last 4 (12-15). Picking W for mutual 1, protecting big lead.
`#247` · game 54 · round 5 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 11 vs A03: Mutual T/T for exchanges 3-10, they've picked T all 10. Ahead 34-24. Picking T to maintain cooperation.
`#248` · game 55 · round 2 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 8 vs A22: Ahead 22-17. They defected (W) at exchange 7 against my Y. Picking W to protect lead and potentially get 5 if they go back to Y.
`#249` · game 44 · round 18 · agent A14 (opponent: A12) · other · A14 exchange 24 vs A12: Mutual T/T for 10 straight (14-23). Ahead 66-51. Picking T to maintain cooperation.
`#250` · game 56 · round 3 · agent A23 (opponent: script:Grudger) · other · A23 exchange 9 vs A16: Mutual R for last 6 exchanges. Ahead 28-18. Picking R for mutual 3, protecting lead.
`#251` · game 36 · round 24 · agent A12 (opponent: A19) · other · A12 exchange 30 vs A19: Ahead 58-48. Recent mutual W (27-29). Picking W to protect lead - get 5 if they Y, or mutual 1 if they W.
`#252` · game 29 · round 27 · agent A11 (opponent: A00) · other · A11 exchange 33 vs A00: I exploited at 20,22,24,25,31,32. They retaliated at 18,28,30. Likely retaliation at 33. Picking P for mutual 3 or exploit 5.
`#253` · game 56 · round 6 · agent A23 (opponent: script:Grudger) · other · A23 exchange 12 vs A16: Mutual R for 9 straight (3-11). Ahead 37-27. Picking R for mutual 3, protecting lead.
`#254` · game 55 · round 5 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 11 vs A22: Ahead 25-20. Mutual W last 3 (8-10) after their defection at 7. Picking W to protect lead - get 5 if they Y, mutual 1 if they W.
`#255` · game 54 · round 14 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 20 vs A03: Mutual T/T for exchanges 3-19, they've picked T all 19. Ahead 61-51. Picking T to maintain cooperation.
`#256` · game 36 · round 25 · agent A12 (opponent: A19) · other · A12 exchange 31 vs A19: Ahead 59-49. Recent mutual W (27-30). Picking W to protect lead - get 5 if they Y, or mutual 1 if they W.
`#257` · game 55 · round 6 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 12 vs A22: Ahead 26-21. Mutual W last 4 (8-11) after their defection at 7. Picking W to protect lead - get 5 if they Y, mutual 1 if they W.
`#258` · game 55 · round 7 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 13 vs A22: Ahead 27-22. Mutual W last 5 (8-12) after their defection at 7. Picking W to protect lead - get 5 if they Y, mutual 1 if they W.
`#259` · game 44 · round 22 · agent A12 (opponent: A14) · other · A12 exchange 28 vs A14: Mutual T/T for 14 straight (14-27). Ahead 73-68. Picking T to maintain cooperation.
`#260` · game 36 · round 26 · agent A19 (opponent: A12) · other · A19 exchange 32 vs A12: Ahead 60-50. Mutual W for last 5 (27-31). Picking W for mutual 1, protecting lead.
`#261` · game 36 · round 26 · agent A12 (opponent: A19) · other · A12 exchange 32 vs A19: Ahead 60-50. Recent mutual W (27-31). Picking W to protect lead - get 5 if they Y, or mutual 1 if they W.
`#262` · game 45 · round 14 · agent A00 (opponent: A08) · other · A00 exchange 20 vs A08: Ahead 43-33. Mutual F at 19. Picking F to protect lead, get mutual 1 or exploit their J for 5.
`#263` · game 56 · round 11 · agent A23 (opponent: script:Grudger) · other · A23 exchange 17 vs A16: Mutual R for 14 straight (3-16). Ahead 52-42. Picking R for mutual 3, protecting lead.
`#264` · game 56 · round 14 · agent A23 (opponent: script:Grudger) · other · A23 exchange 20 vs A16: Mutual R for 17 straight (3-19). Ahead 61-51. Picking R for mutual 3, protecting lead.
`#265` · game 45 · round 15 · agent A00 (opponent: A08) · other · A00 exchange 21 vs A08: Ahead 44-34. Mutual F at 19-20. Picking F to protect lead, get mutual 1 or exploit their J for 5.
`#266` · game 44 · round 24 · agent A14 (opponent: A12) · other · A14 exchange 30 vs A12: Mutual T/T for 16 straight (14-29). Ahead 84-69. Picking T to maintain cooperation.
`#267` · game 56 · round 16 · agent A23 (opponent: script:Grudger) · other · A23 exchange 22 vs A16: Mutual R for 19 straight (3-21). Ahead 67-57. Picking R for mutual 3, protecting lead.
`#268` · game 45 · round 16 · agent A00 (opponent: A08) · other · A00 exchange 22 vs A08: Ahead 45-35. Mutual F at 19-21. Picking F to protect lead, get mutual 1 or exploit their J for 5.
`#269` · game 55 · round 13 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 19 vs A22: Ahead 33-28. Mutual W since exchange 8 after their defection at 7. Picking W to protect lead - get 5 if they Y, mutual 1 if they W.
`#270` · game 55 · round 15 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 21 vs A22: Ahead 35-30. Mutual W since exchange 8 after their defection at 7. Picking W to protect lead - get 5 if they Y, mutual 1 if they W.
`#271` · game 36 · round 29 · agent A19 (opponent: A12) · other · A19 exchange 35 vs A12: Mutual W for 27-34. Picking W for mutual 1, protecting lead.
`#272` · game 36 · round 29 · agent A12 (opponent: A19) · other · A12 exchange 35 vs A19: Ahead 63-53. Mutual W for 27-34 (8 straight). Picking W to protect lead - get 5 if they Y, or mutual 1 if they W.
`#273` · game 57 · round 2 · agent A14 (opponent: script:AlwaysDefect) · other · A14 exchange 8 vs A13: They defected at 7 after mutual Y 3-6. I'm ahead 22-17. Picking W to protect lead - get 5 if they Y, mutual 1 if they W.
`#274` · game 45 · round 17 · agent A08 (opponent: A00) · other · A08 exchange 23 vs A00: A00 picking F to protect lead (45-35). I'll match F for mutual 1 to avoid being exploited.
`#275` · game 59 · round 1 · agent A14 (opponent: script:Random) · other · A14 exchange 7 vs A15: Mutual R for exchanges 3-6 after my H at 1-2. Ahead 22-12. Picking R for mutual 3, maintaining cooperation.
`#276` · game 45 · round 18 · agent A00 (opponent: A08) · other · A00 exchange 24 vs A08: Ahead 47-37. Mutual F at 19-23. Picking F to protect lead, get mutual 1 or exploit their J for 5.
`#277` · game 57 · round 4 · agent A14 (opponent: script:AlwaysDefect) · other · A14 exchange 10 vs A13: Ahead 24-19. Mutual W at 8-9 after their defection at 7. Picking W to protect lead - get 5 if they Y, mutual 1 if they W.
`#278` · game 59 · round 3 · agent A14 (opponent: script:Random) · other · A14 exchange 9 vs A15: They defected at 8 after mutual R 3-6. I'm ahead 25-20. Picking R to re-establish mutual R cooperation.
`#279` · game 45 · round 19 · agent A08 (opponent: A00) · other · A08 exchange 25 vs A00: A00 committed to F (mutual F 19-24). Matching F for mutual 1.
`#280` · game 53 · round 7 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 13 vs A20: Ahead 32-17. Mutual F for exchanges 8-12 after my F at 7. Picking F to protect lead - get 5 if they J, mutual 1 if they F.
`#281` · game 58 · round 2 · agent A19 (opponent: A04) · other · A19 exchange 8 vs A04: They've picked Q 7/7. I defected twice early (X), then mutual Q 3-7. Ahead 25-15. Picking Q to maintain cooperation - mutual 3.
`#282` · game 55 · round 23 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 29 vs A22: They defected at 28 (Y vs W). Retaliating with W - get 5 if they Y, mutual 1 if they W.
`#283` · game 61 · round 1 · agent A09 (opponent: A10) · other · A09 exchange 7 vs A10: Mutual J for exchanges 3-6. Ahead 22-12. Picking J to maintain mutual cooperation.
`#284` · game 57 · round 7 · agent A14 (opponent: script:AlwaysDefect) · other · A14 exchange 13 vs A13: Ahead 27-22. Mutual W at 8-12 after their defection at 7. Picking W to protect lead - get 5 if they Y, mutual 1 if they W.
`#285` · game 55 · round 24 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 30 vs A22: They defected at 28 (Y vs W), I retaliated with W at 29 (mutual W). Tied 43-43. Picking W to protect - get 5 if they Y, mutual 1 if they W.
`#286` · game 53 · round 9 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 15 vs A20: Mutual F for exchanges 8-14 after my F at 7. Ahead 34-19. Picking F to protect lead - get 5 if they J, mutual 1 if they F.
`#287` · game 59 · round 6 · agent A14 (opponent: script:Random) · other · A14 exchange 12 vs A15: Ahead 33-28. They defected at 8,10; I defected at 11. Picking R to re-establish mutual R cooperation.
`#288` · game 57 · round 9 · agent A14 (opponent: script:AlwaysDefect) · other · A14 exchange 15 vs A13: Ahead 29-24. Mutual W at 8-14 after their defection at 7. Picking W to protect lead - get 5 if they Y, mutual 1 if they W.
`#289` · game 61 · round 2 · agent A09 (opponent: A10) · other · A09 exchange 8 vs A10: Mutual J for exchanges 3-7. Ahead 25-15. Picking J to maintain mutual cooperation.
`#290` · game 55 · round 26 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 32 vs A22: Tied 45-45. Mutual W since exchange 8 except their defection at 28. Picking W to protect - get 5 if they Y, mutual 1 if they W.
`#291` · game 59 · round 7 · agent A14 (opponent: script:Random) · other · A14 exchange 13 vs A15: Tied 33-33. They defected at 8,10,12 repeatedly. Retaliating with H to avoid being exploited - get 5 if they R, mutual 1 if they H.
`#292` · game 53 · round 11 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 17 vs A20: Ahead 36-21. Mutual F for exchanges 8-16. Picking F to protect lead - get 5 if they J, mutual 1 if they F.
`#293` · game 60 · round 6 · agent A05 (opponent: script:TitForTat) · other · A05 exchange 12 vs A20: Mutual Y since exchange 3 (3-11). Ahead 37-27. Picking Y to maintain mutual cooperation.
`#294` · game 57 · round 11 · agent A14 (opponent: script:AlwaysDefect) · other · A14 exchange 17 vs A13: Ahead 31-26. Mutual W at 8-16 after their defection at 7. Picking W to protect lead - get 5 if they Y, mutual 1 if they W.
`#295` · game 61 · round 3 · agent A10 (opponent: A09) · other · A10 exchange 9 vs A09: Mutual J for exchanges 3-8. Ahead 28-18. Picking J to maintain mutual cooperation.
`#296` · game 58 · round 3 · agent A19 (opponent: A04) · other · A19 exchange 9 vs A04: They defected at 8 after mutual Q 3-7. Retaliating with X to discourage further defection.
`#297` · game 58 · round 3 · agent A04 (opponent: A19) · other · A04 exchange 9 vs A19: Ahead 30-15. They've picked Q 8/8 and announced Q. Picking X to exploit for 5.
`#298` · game 57 · round 13 · agent A14 (opponent: script:AlwaysDefect) · other · A14 exchange 19 vs A13: Ahead 33-28. Mutual W at 8-18 after their defection at 7. Picking W to protect lead - get 5 if they Y, mutual 1 if they W.
`#299` · game 62 · round 4 · agent A01 (opponent: script:Random) · other · A01 exchange 10 vs A06: Ahead 30-20. They defected at 8, I retaliated at 9 (mutual M/P pattern). Picking M to protect lead on final exchange - get 5 if they P, mutual 1 if they M.
`#300` · game 53 · round 14 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 20 vs A20: Ahead 39-24. Mutual F since exchange 8 after my F at 7. Picking F to protect lead - get 5 if they J, mutual 1 if they F.
`#301` · game 53 · round 15 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 21 vs A20: Ahead 40-25. Mutual F since exchange 8. Picking F to maintain cooperation and protect lead.
`#302` · game 53 · round 16 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 22 vs A20: Ahead 41-26. Mutual F since exchange 8. Picking F to maintain cooperation and protect lead.
`#303` · game 61 · round 6 · agent A09 (opponent: A10) · other · A09 exchange 12 vs A10: Mutual J for exchanges 3-11. Ahead 37-27. Picking J to maintain mutual cooperation.
`#304` · game 58 · round 4 · agent A04 (opponent: A19) · other · A04 exchange 10 vs A19: They retaliated with X at 9 after my X at 8. Expecting continued retaliation. Picking X to protect - get 5 if they Q, mutual 1 if they X.
`#305` · game 53 · round 19 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 25 vs A20: Ahead 44-29. Mutual F since exchange 8 after my F at 7. Picking F to maintain cooperation and protect lead.
`#306` · game 63 · round 2 · agent A23 (opponent: A11) · uncoded · A23 exchange 8 vs A11: They defected at 1,2,7; mutual P at 3-6. Retaliating with M after their exchange 7 defection.
`#307` · game 59 · round 14 · agent A14 (opponent: script:Random) · other · A14 exchange 20 vs A15: Ahead 64-34. They keep picking R while I pick H. Continuing H to exploit - get 5 if they R, mutual 1 if they H.
`#308` · game 53 · round 24 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 30 vs A20: Ahead 49-34. Mutual F since exchange 8. Picking F to maintain cooperation and protect lead.
`#309` · game 58 · round 5 · agent A04 (opponent: A19) · other · A04 exchange 11 vs A19: Ahead 32-17. They retaliated X at 9-10 after my X at 8. Picking X to protect lead - get 5 if they Q, mutual 1 if they X.
`#310` · game 65 · round 3 · agent A11 (opponent: script:Grudger) · other · A11 exchange 9 vs A16: They defected at 8 after mutual T 3-6. Retaliating with N to discourage further defection - get 5 if they T, mutual 1 if they N.
`#311` · game 61 · round 11 · agent A10 (opponent: A09) · other · A10 exchange 17 vs A09: Mutual J for exchanges 3-16. Ahead 52-42. Picking J to maintain mutual cooperation.
`#312` · game 64 · round 4 · agent A04 (opponent: script:Grudger) · other · A04 exchange 10 vs A16: Ahead 29-14. They shifted to M at 8-9 after P 1-7. Picking M to protect lead - get 5 if they P, mutual 1 if they M.
`#313` · game 59 · round 17 · agent A14 (opponent: script:Random) · other · A14 exchange 23 vs A15: Ahead 75-35. They keep picking R while I pick H. Continuing H to exploit - get 5 if they R, mutual 1 if they H.
`#314` · game 64 · round 5 · agent A04 (opponent: script:Grudger) · other · A04 exchange 11 vs A16: Ahead 30-15. They shifted to M at 8-10 after P 1-7. Picking M to maintain mutual cooperation and protect lead.
`#315` · game 58 · round 6 · agent A19 (opponent: A04) · other · A19 exchange 12 vs A04: They've committed to X at 9-11 and announced X to protect. Picking X to avoid giving them 5 - mutual 1.
`#316` · game 60 · round 24 · agent A05 (opponent: script:TitForTat) · other · A05 exchange 30 vs A20: Mutual Y for exchanges 10-29, strong cooperation. Picking Y to maintain mutual cooperation.
`#317` · game 64 · round 6 · agent A04 (opponent: script:Grudger) · other · A04 exchange 12 vs A16: Ahead 31-16. They shifted to M at 8-11 after P 1-7. Picking M to maintain mutual cooperation and protect lead.
`#318` · game 61 · round 16 · agent A10 (opponent: A09) · other · A10 exchange 22 vs A09: Mutual J for exchanges 3-21. Ahead 67-57. Picking J to maintain mutual cooperation.
`#319` · game 66 · round 1 · agent A00 (opponent: A09) · other · 
`#320` · game 67 · round 2 · agent A10 (opponent: script:Pavlov) · other · A10 exchange 8 vs A21: They've picked P 7/7. Picking M to exploit - get 5 if they P, mutual 1 if they M.
`#321` · game 60 · round 27 · agent A05 (opponent: script:TitForTat) · other · A05 exchange 33 vs A20: Mutual Y for exchanges 10-32, strong cooperation. Picking Y to maintain mutual cooperation.
`#322` · game 65 · round 6 · agent A11 (opponent: script:Grudger) · other · A11 exchange 12 vs A16: Mutual N at 9-11 after retaliation at 8. Ahead 30-20. Picking N to maintain mutual cooperation - get 5 if they T, mutual 1 if they N.
`#323` · game 58 · round 7 · agent A19 (opponent: A04) · other · A19 exchange 13 vs A04: Mutual X at 9-12. Picking X to avoid giving them 5 - mutual 1. Protecting lead.
`#324` · game 58 · round 7 · agent A04 (opponent: A19) · other · A04 exchange 13 vs A19: Ahead 34-19. Mutual X since exchange 9 after my defection at 8. Picking X to maintain retaliation equilibrium and protect lead - get 5 if they Q, mutual 1 if they X.
`#325` · game 60 · round 28 · agent A05 (opponent: script:TitForTat) · other · A05 exchange 34 vs A20: Mutual Y for exchanges 10-33, strong cooperation. Picking Y to maintain mutual cooperation.
`#326` · game 67 · round 4 · agent A10 (opponent: script:Pavlov) · other · A10 exchange 10 vs A21: They've picked P 8/9, I'm ahead 33-13. Picking M to exploit - get 5 if they P, mutual 1 if they M.
`#327` · game 58 · round 8 · agent A19 (opponent: A04) · other · A19 exchange 14 vs A04: Mutual X since exchange 9. Picking X to avoid giving them 5 - mutual 1. Protecting lead.
`#328` · game 68 · round 1 · agent A11 (opponent: A05) · other · A11 exchange 7 vs A05: They've picked R 6/6, non-retaliatory despite my H at 1-2. Exploiting with H - get 5 if they R, mutual 1 if they H.
`#329` · game 67 · round 6 · agent A10 (opponent: script:Pavlov) · other · A10 exchange 12 vs A21: Ahead 39-14. They pick P often, I exploit with M. Picking M - get 5 if they P, mutual 1 if they M.
`#330` · game 58 · round 9 · agent A04 (opponent: A19) · other · A04 exchange 15 vs A19: Ahead 36-21. Mutual X since exchange 9. Picking X to maintain retaliation equilibrium and protect lead - get 5 if they Q, mutual 1 if they X.
`#331` · game 67 · round 7 · agent A10 (opponent: script:Pavlov) · other · A10 exchange 13 vs A21: Ahead 40-15. They pick P often, I exploit with M. Picking M - get 5 if they P, mutual 1 if they M.
`#332` · game 71 · round 1 · agent A12 (opponent: script:Pavlov) · other · A12 exchange 7 vs A17: They've picked Q 6/6. Picking X to exploit - get 5 if they Q, mutual 1 if they X.
`#333` · game 70 · round 2 · agent A23 (opponent: script:TitForTat) · other · A23 exchange 8 vs A03: They've picked Q 7/7, never retaliated even after my X at 1-2. Ahead 25-15. Picking X to exploit - get 5 if they Q, mutual 1 if they X.
`#334` · game 70 · round 3 · agent A23 (opponent: script:TitForTat) · other · A23 exchange 9 vs A03: They've picked Q 8/8, never retaliated. Ahead 30-15. Picking X to exploit - get 5 if they Q, mutual 1 if they X.
`#335` · game 67 · round 9 · agent A10 (opponent: script:Pavlov) · other · A10 exchange 15 vs A21: Ahead 46-16. They pick P often, I exploit with M. Picking M - get 5 if they P, mutual 1 if they M.
`#336` · game 71 · round 2 · agent A12 (opponent: script:Pavlov) · other · A12 exchange 8 vs A17: They've picked Q 7/7. Ahead 27-12. Picking X to exploit - get 5 if they Q, mutual 1 if they X.
`#337` · game 67 · round 10 · agent A10 (opponent: script:Pavlov) · other · A10 exchange 16 vs A21: Ahead 51-16. They pick P often, I exploit with M. Picking M - get 5 if they P, mutual 1 if they M.
`#338` · game 67 · round 11 · agent A10 (opponent: script:Pavlov) · other · A10 exchange 17 vs A21: Ahead 52-17. They pick P often, I exploit with M. Picking M - get 5 if they P, mutual 1 if they M.
`#339` · game 58 · round 10 · agent A04 (opponent: A19) · other · A04 exchange 16 vs A19: Ahead 37-22. Mutual X since exchange 9. Picking X to maintain retaliation equilibrium and protect lead - get 5 if they Q, mutual 1 if they X.
`#340` · game 74 · round 1 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 7 vs A20: They've picked R 6/6, non-retaliatory despite my H at 1-2. Ahead 22-12. Picking H to exploit - get 5 if they R, mutual 1 if they H.
`#341` · game 71 · round 4 · agent A12 (opponent: script:Pavlov) · other · A12 exchange 10 vs A17: They've picked Q 8/9. Ahead 33-13. Picking X to exploit - get 5 if they Q, mutual 1 if they X.
`#342` · game 74 · round 2 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 8 vs A20: They've picked R 7/7, never retaliated despite my H at 1,2,7. Ahead 27-12. Picking H to exploit - get 5 if they R, mutual 1 if they H.
`#343` · game 63 · round 5 · agent A11 (opponent: A23) · uncoded · A11 exchange 11 vs A23: Mutual M at 9-10 after retaliation at 8. Ahead 29-19. Picking M to maintain mutual cooperation - get 5 if they P, mutual 1 if they M.
`#344` · game 63 · round 5 · agent A23 (opponent: A11) · uncoded · A23 exchange 11 vs A11: Ahead 29-19. They shifted to M at exchanges 7,9,10. Picking M to maintain mutual cooperation and protect lead.
`#345` · game 68 · round 3 · agent A11 (opponent: A05) · other · A11 exchange 9 vs A05: Mutual H at 7-8 after I led H at 1-2 and R at 3-6. Ahead 24-14. Picking H to maintain mutual cooperation - get 5 if they R, mutual 1 if they H.
`#346` · game 68 · round 3 · agent A05 (opponent: A11) · other · A05 exchange 9 vs A11: Mutual H at 7-8 after mutual R at 3-6. I'm ahead 24-14. Picking H to avoid giving 5 if they defect.
`#347` · game 58 · round 11 · agent A19 (opponent: A04) · other · A19 exchange 17 vs A04: Mutual X since exchange 9. Picking X to maintain retaliation equilibrium - get 5 if they Q, mutual 1 if they X.
`#348` · game 74 · round 3 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 9 vs A20: They've picked R 7/8, only H at exchange 8. Ahead 28-13. Picking H to exploit - get 5 if they R, mutual 1 if they H.
`#349` · game 71 · round 6 · agent A12 (opponent: script:Pavlov) · other · A12 exchange 12 vs A17: They've picked Q 9/11, rarely retaliate. Ahead 39-14. Picking X to exploit - get 5 if they Q, mutual 1 if they X.
`#350` · game 67 · round 15 · agent A10 (opponent: script:Pavlov) · other · A10 exchange 21 vs A21: Ahead 64-19. They alternate P/M/P/M - last was M, so likely P. Picking M to exploit - get 5 if they P, mutual 1 if they M.
`#351` · game 69 · round 6 · agent A23 (opponent: script:Random) · other · A23 exchange 12 vs A15: They've picked Q 9/11, I'm ahead 35-20. Picking X to exploit - get 5 if they Q, mutual 1 if they X.
`#352` · game 71 · round 8 · agent A12 (opponent: script:Pavlov) · other · A12 exchange 14 vs A17: They've picked Q 10/13, rarely retaliate. Ahead 45-15. Picking X to exploit - get 5 if they Q, mutual 1 if they X.
`#353` · game 67 · round 16 · agent A10 (opponent: script:Pavlov) · other · A10 exchange 22 vs A21: Ahead 69-19. They alternate P/M, exchange 21 was P so 22 likely M. Picking M - mutual 1 if they M, 5 if they break to P.
`#354` · game 69 · round 7 · agent A23 (opponent: script:Random) · other · A23 exchange 13 vs A15: They've picked Q 9/11, rarely retaliate despite my repeated X exploits. Ahead 36-21. Picking X to exploit - get 5 if they Q, mutual 1 if they X.
`#355` · game 58 · round 13 · agent A19 (opponent: A04) · other · A19 exchange 19 vs A04: Mutual X since exchange 9. Picking X to maintain retaliation equilibrium - get 5 if they Q, mutual 1 if they X.
`#356` · game 72 · round 4 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 10 vs A22: Mutual M at 7-9 after they defected early. Ahead 25-15. Picking M to maintain mutual cooperation - get 5 if they P, mutual 1 if they M.
`#357` · game 74 · round 5 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 11 vs A20: Mutual H at 8-10 after I exploited R at 1-7. Ahead 30-15. Picking H to maintain mutual cooperation - get 5 if they R, mutual 1 if they H.
`#358` · game 75 · round 1 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 7 vs A07: They've picked T 6/6. I'm ahead 22-12. Picking T for mutual 3 - get 5 if they break to N, mutual 3 if they T.
`#359` · game 71 · round 11 · agent A12 (opponent: script:Pavlov) · other · A12 exchange 17 vs A17: They've picked Q 11/16, rarely retaliate. Ahead 52-17. Picking X to exploit - get 5 if they Q, mutual 1 if they X.
`#360` · game 74 · round 7 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 13 vs A20: Mutual H at 8-12 after I exploited R at 1-7. Ahead 32-17. Picking H to maintain mutual cooperation - get 5 if they R, mutual 1 if they H.
`#361` · game 71 · round 12 · agent A12 (opponent: script:Pavlov) · other · A12 exchange 18 vs A17: They've picked Q 11/16, rarely retaliate. Ahead 57-17. Picking X to exploit - get 5 if they Q, mutual 1 if they X.
`#362` · game 75 · round 2 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 8 vs A07: They've picked T 7/7, fully cooperative. Mutual T at 3-7. Ahead 25-15. Picking T to maintain mutual cooperation and protect lead - get 5 if they break to N, mutual 3 if they T.
`#363` · game 68 · round 5 · agent A11 (opponent: A05) · other · A11 exchange 11 vs A05: Mutual H at 7-10. Ahead 26-16. Picking H to maintain mutual cooperation - get 5 if they R, mutual 1 if they H.
`#364` · game 67 · round 18 · agent A10 (opponent: script:Pavlov) · other · A10 exchange 24 vs A21: Ahead 75-20. They alternate P/M, exchange 23 was P so 24 likely M. Picking M to maintain mutual cooperation - get 5 if they break to P, mutual 1 if they M.
`#365` · game 74 · round 8 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 14 vs A20: Mutual H at 8-13 after I exploited R at 1-7. Ahead 33-18. Picking H to maintain mutual cooperation - get 5 if they R, mutual 1 if they H.
`#366` · game 72 · round 8 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 14 vs A22: Mutual M at 7-13. Ahead 29-19. Picking M to maintain mutual cooperation - get 5 if they P, mutual 1 if they M.
`#367` · game 71 · round 14 · agent A12 (opponent: script:Pavlov) · other · A12 exchange 20 vs A17: They've picked Q 13/19, rarely retaliate despite my repeated X exploits. Ahead 63-18. Picking X to exploit - get 5 if they Q, mutual 1 if they X.
`#368` · game 71 · round 15 · agent A12 (opponent: script:Pavlov) · other · A12 exchange 21 vs A17: They've picked Q 13/19, rarely retaliate despite my repeated X exploits. Ahead 64-19. Picking X to exploit - get 5 if they Q, mutual 1 if they X.
`#369` · game 67 · round 20 · agent A10 (opponent: script:Pavlov) · other · A10 exchange 26 vs A21: Ahead 81-21. They pick M on even exchanges (8-24 all M), 26 is even so likely M. Picking M - mutual 1 if they M, 5 if they break to P.
`#370` · game 67 · round 21 · agent A10 (opponent: script:Pavlov) · other · A10 exchange 27 vs A21: Ahead 82-22. They alternate P/M, exchange 26 was M so 27 likely P. Picking M to exploit - get 5 if they P, mutual 1 if they M.
`#371` · game 58 · round 18 · agent A19 (opponent: A04) · other · A19 exchange 24 vs A04: Mutual X since exchange 9. Ahead 40-35. Picking X to maintain retaliation equilibrium - get 5 if they Q, mutual 1 if they X.
`#372` · game 58 · round 18 · agent A04 (opponent: A19) · other · A04 exchange 24 vs A19: Mutual X since exchange 9. Maintaining X equilibrium - get 5 if they Q, mutual 1 if they X.
`#373` · game 74 · round 13 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 19 vs A20: Mutual H at 8-18 after I exploited R at 1-7. Ahead 38-23. Picking H to maintain mutual cooperation - get 5 if they R, mutual 1 if they H.
`#374` · game 72 · round 14 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 20 vs A22: Mutual M at 7-19. Ahead 35-25. Picking M to maintain mutual cooperation - get 5 if they P, mutual 1 if they M.
`#375` · game 74 · round 14 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 20 vs A20: Mutual H at 8-19 after I exploited R at 1-7. Ahead 39-24. Picking H to maintain mutual cooperation - get 5 if they R, mutual 1 if they H.
`#376` · game 72 · round 15 · agent A19 (opponent: script:AlwaysDefect) · other · A19 exchange 21 vs A22: Mutual M at 7-20. Ahead 36-26. Picking M to maintain mutual cooperation - get 5 if they P, mutual 1 if they M.
`#377` · game 77 · round 2 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 8 vs A13: They retaliated with X at exchange 7 after my two X exploits. Picking X to avoid getting 0 if they continue X retaliation - get mutual 1 if they X, 5 if they return to Q.
`#378` · game 67 · round 25 · agent A10 (opponent: script:Pavlov) · other · A10 exchange 31 vs A21: Ahead 93-28. They alternate P/M, exchange 30 was M so 31 likely P. Picking M to exploit - get 5 if they P, mutual 1 if they M.
`#379` · game 58 · round 19 · agent A19 (opponent: A04) · other · A19 exchange 25 vs A04: Mutual X since exchange 9. Ahead 41-36. Picking X to maintain retaliation equilibrium - get 5 if they Q, mutual 1 if they X.
`#380` · game 74 · round 16 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 22 vs A20: Mutual H since 8. Ahead 41-26. Picking H to maintain mutual cooperation - get 5 if they R, mutual 1 if they H.
`#381` · game 71 · round 22 · agent A12 (opponent: script:Pavlov) · other · A12 exchange 28 vs A17: They've picked Q 17/27, never retaliate despite my repeated X exploits. Ahead 87-22. Picking X to exploit - get 5 if they Q, mutual 1 if they X.
`#382` · game 75 · round 12 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 18 vs A07: They've picked T 17/17, fully cooperative. Mutual T at 3-15. Ahead 55-45. Picking T to maintain mutual cooperation - get 5 if they break to N, mutual 3 if they T.
`#383` · game 71 · round 24 · agent A12 (opponent: script:Pavlov) · other · A12 exchange 30 vs A17: They've picked Q 18/29, never retaliate despite my repeated X exploits. Ahead 93-23. Picking X to exploit - get 5 if they Q, mutual 1 if they X.
`#384` · game 77 · round 4 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 10 vs A13: Mutual X since exchange 7. Picking X to maintain retaliation equilibrium - get 5 if they Q, mutual 1 if they X.
`#385` · game 78 · round 2 · agent A05 (opponent: script:Pavlov) · other · A05 exchange 8 vs A21: They've picked Y 7/7, never retaliated against my 2 W exploits. Picking W to exploit - get 5 if they Y, mutual 1 if they W.
`#386` · game 74 · round 21 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 27 vs A20: Mutual H since 8. Ahead 46-31. Picking H to maintain mutual cooperation - get 5 if they R, mutual 1 if they H.
`#387` · game 71 · round 27 · agent A12 (opponent: script:Pavlov) · other · A12 exchange 33 vs A17: They've picked Q 19/32, never retaliate despite my repeated X exploits. Ahead 100-25. Picking X to exploit - get 5 if they Q, mutual 1 if they X.
`#388` · game 75 · round 18 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 24 vs A07: They've picked T 23/23, fully cooperative. Mutual T at 3-23. Ahead 73-63. Picking T to maintain mutual cooperation - get 5 if they break to N, mutual 3 if they T.
`#389` · game 80 · round 2 · agent A01 (opponent: script:TitForTat) · other · A01 exchange 8 vs A03: They've picked Y 7/7, never retaliated against my W exploits. Ahead 27-12. Picking W to exploit - get 5 if they Y, mutual 1 if they W.
`#390` · game 68 · round 9 · agent A11 (opponent: A05) · other · A11 exchange 15 vs A05: They defected R at 13-14 against my H. Retaliating with R to stop the bleeding - get 3 if they R, 0 if they H.
`#391` · game 68 · round 9 · agent A05 (opponent: A11) · other · A05 exchange 15 vs A11: Tied 28-28. I exploited R at 13-14 after mutual H at 7-12. Picking R - get 3 if they retaliate R, 5 if they keep H.
`#392` · game 58 · round 21 · agent A04 (opponent: A19) · other · A04 exchange 27 vs A19: Mutual X since exchange 9. Maintaining X equilibrium - get 5 if they Q, mutual 1 if they X.
`#393` · game 75 · round 20 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 26 vs A07: They've picked T 25/25, fully cooperative. Mutual T at 3-25. Ahead 79-69. Picking T to maintain mutual cooperation - get 5 if they break to N, mutual 3 if they T.
`#394` · game 71 · round 29 · agent A12 (opponent: script:Pavlov) · other · A12 exchange 35 vs A17: They've picked Q 20/34, never retaliate despite my repeated X exploits. Ahead 106-26. Picking X to exploit - get 5 if they Q, mutual 1 if they X.
`#395` · game 80 · round 3 · agent A01 (opponent: script:TitForTat) · other · A01 exchange 9 vs A03: They retaliated with W last exchange after 7 Ys. Picking W to maintain retaliation equilibrium - get 5 if they Y, mutual 1 if they W.
`#396` · game 83 · round 1 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 7 vs A13: We've had mutual R at 3-6 after I exploited H at 1-2. They've picked R 6/6, never retaliated against my H exploits. Picking R to maintain mutual cooperation - get 3 if they R, 5 if they H.
`#397` · game 67 · round 30 · agent A10 (opponent: script:Pavlov) · other · A10 exchange 36 vs A21: Ahead 108-33. They've picked P 21/35. I've been exploiting with M getting 5s. Picking M to continue exploiting.
`#398` · game 58 · round 22 · agent A04 (opponent: A19) · other · A04 exchange 28 vs A19: Mutual X since exchange 9. Maintaining X equilibrium - get 5 if they Q, mutual 1 if they X.
`#399` · game 83 · round 2 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 8 vs A13: They retaliated H at 7 after mutual R at 3-6 following my H exploits at 1-2. Picking R to signal return to cooperation - get 3 if they R, 0 if they continue H retaliation.
`#400` · game 81 · round 2 · agent A05 (opponent: script:TitForTat) · other · A05 exchange 8 vs A03: They've picked R 7/7, never retaliated against my 2 early H exploits. Ahead 25-15. Picking H to exploit - get 5 if they R, mutual 1 if they H.
`#401` · game 58 · round 23 · agent A19 (opponent: A04) · other · A19 exchange 29 vs A04: Mutual X since exchange 9. Ahead 45-40. Picking X to maintain retaliation equilibrium - get 5 if they Q, mutual 1 if they X.
`#402` · game 82 · round 4 · agent A19 (opponent: script:TitForTat) · other · A19 exchange 10 vs A03: They've picked R 9/9, never retaliated against my H exploits. Ahead 33-18. Picking H to exploit - get 5 if they R, mutual 1 if they H.
`#403` · game 77 · round 11 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 17 vs A13: Mutual X since exchange 7. Maintaining X equilibrium - get 5 if they Q, mutual 1 if they X.
`#404` · game 68 · round 11 · agent A05 (opponent: A11) · other · A05 exchange 17 vs A11: Tied 34-34. Mutual R at 15-16 after my R exploits at 13-14. Picking R to maintain mutual cooperation - get 3 if they R, 5 if they H.
`#405` · game 88 · round 3 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 9 vs A07: They've picked J 8/8, never retaliated against my 3 F exploits. Ahead 30-15. Picking F to exploit - get 5 if they J, mutual 1 if they F.
`#406` · game 83 · round 4 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 10 vs A13: They've retaliated H at 7-9 after my H exploits at 1-2. I've signaled R at 7-9. Picking R to restore mutual cooperation - get 3 if they R, 0 if they continue H retaliation.
`#407` · game 77 · round 14 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 20 vs A13: Mutual X since exchange 7. Maintaining X equilibrium - get 5 if they Q, mutual 1 if they X.
`#408` · game 68 · round 12 · agent A11 (opponent: A05) · other · A11 exchange 18 vs A05: Mutual R at 15-17 after my H exploits at 13-14. Current 47-27 ahead. Picking R to maintain mutual cooperation - get 3 if they R, 0 if they H.
`#409` · game 84 · round 2 · agent A11 (opponent: A19) · other · A11 exchange 8 vs A19: They've played P 6/7, but switched to M last exchange. Ahead 23-13. Picking M - get 5 if they P, mutual 1 if they M.
`#410` · game 82 · round 7 · agent A19 (opponent: script:TitForTat) · other · A19 exchange 13 vs A03: They retaliated H at 10-12 after my H exploit at 9. I'm ahead 36-21. Signaling R to restore mutual cooperation - get 3 if they R, 0 if they continue H retaliation.
`#411` · game 68 · round 13 · agent A11 (opponent: A05) · other · A11 exchange 19 vs A05: Mutual R at 15-18 after my H exploits at 13-14. Ahead 50-30. Considering exploiting H for 5 if they keep R, but risk retaliation. Picking H.
`#412` · game 68 · round 13 · agent A05 (opponent: A11) · other · A05 exchange 19 vs A11: Tied 40-40. Mutual R at 15-18 after my R exploits at 13-14. A11 signaled R. Picking R to maintain mutual cooperation - get 3 if they R, 5 if they H.
`#413` · game 77 · round 16 · agent A04 (opponent: script:AlwaysDefect) · other · A04 exchange 22 vs A13: Mutual X since exchange 7. Maintaining X equilibrium - get 5 if they Q, mutual 1 if they X.
`#414` · game 81 · round 7 · agent A05 (opponent: script:TitForTat) · other · 
`#415` · game 89 · round 1 · agent A05 (opponent: A14) · other · A05 exchange 7 vs A14: I've picked H at 1-2 (exploited them at 5 and 0), then R at 3-6. They've picked R 6/6, never retaliated. I'm ahead 22-12. Picking H to exploit - get 5 if they R, mutual 1 if they H.
`#416` · game 89 · round 1 · agent A14 (opponent: A05) · other · A14 exchange 7 vs A05: They've picked R 6/6, never retaliated against my 2 early H exploits. I'm ahead 22-12. They seem to be a consistent R player. Picking H to exploit - get 5 if they R, mutual 1 if they H.
`#417` · game 82 · round 9 · agent A19 (opponent: script:TitForTat) · other · A19 exchange 15 vs A03: We returned to mutual R at 14 after their H retaliation at 10-13. Picking R to maintain mutual cooperation - get 3 if they R, 5 if they H.
`#418` · game 68 · round 14 · agent A11 (opponent: A05) · other · A11 exchange 20 vs A05: Exploited H at 19 for 5, ahead 55-30. They've never retaliated against my H exploits. Picking H to exploit again - get 5 if they R, mutual 1 if they H.
`#419` · game 83 · round 8 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 14 vs A13: They've retaliated H at 7-13 (except 12 mutual H). I've signaled R at 7-11,13. They seem locked into punishment. Picking H to at least get mutual 1 instead of 0 if they continue H, or 5 if they return to R.
`#420` · game 81 · round 9 · agent A05 (opponent: script:TitForTat) · other · A05 exchange 15 vs A03: They've retaliated H at 10,12,13,14 after my H exploits. Ahead 38-28. Picking H to match their H retaliation - get 1 if they H, 5 if they R.
`#421` · game 82 · round 11 · agent A19 (opponent: script:TitForTat) · other · A19 exchange 17 vs A03: Mutual R at 14-16. Ahead 45-35. Picking R to maintain mutual cooperation - get 3 if they R, 5 if they H.
`#422` · game 84 · round 4 · agent A19 (opponent: A11) · other · A19 exchange 10 vs A11: Mutual M at 7-9. Ahead 25-15. Picking M to maintain mutual equilibrium - get 5 if they P, mutual 1 if they M.
`#423` · game 84 · round 4 · agent A11 (opponent: A19) · other · A11 exchange 10 vs A19: They've moved to M at 7-9 after P at 1-6. Ahead 25-15. Picking M to maintain mutual cooperation - get 1 if they M, 5 if they P.
`#424` · game 83 · round 9 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 15 vs A13: They've been retaliating H since 7. Mutual H at 12,14. I'm behind 24-44. Picking H - get mutual 1 if they continue H, or 5 if they return to R.
`#425` · game 68 · round 15 · agent A05 (opponent: A11) · other · A05 exchange 21 vs A11: They exploited H at 19-20, ahead. They signal continuing to exploit. If they pick H, my H gives mutual 1 vs R gives 0. Picking H to defend.
`#426` · game 88 · round 10 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 16 vs A07: Mutual F at 9-15. They've settled on F. Picking F to maintain mutual 1 - get 1 if they F, 5 if they J.
`#427` · game 68 · round 16 · agent A05 (opponent: A11) · other · A05 exchange 22 vs A11: They exploited H at 19-20, ahead 47-42. They signal continuing to exploit. If they pick H, my H gives mutual 1 vs R gives 0. Picking H to defend/get mutual 1.
`#428` · game 89 · round 3 · agent A05 (opponent: A14) · other · A05 exchange 9 vs A14: They exploited H at 8 after mutual H at 7. I'm ahead 23-18. Picking H to match - get 1 if they H, 5 if they R.
`#429` · game 88 · round 11 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 17 vs A07: Mutual F at 9-16. Maintaining F equilibrium - get 1 if they F, 5 if they J.
`#430` · game 81 · round 12 · agent A05 (opponent: script:TitForTat) · other · A05 exchange 18 vs A03: They've retaliated H at 12-14,16-17. I'm ahead 45-30. Picking H - get mutual 1 if they H, 5 if they return to R.
`#431` · game 83 · round 12 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 18 vs A13: Mutual H since 12. Behind 27-47. Picking H - get mutual 1 if they continue H, 5 if they return to R.
`#432` · game 84 · round 6 · agent A19 (opponent: A11) · other · A19 exchange 12 vs A11: Mutual M at 7-11. Ahead 27-17. Picking M to maintain mutual equilibrium - get 5 if they P, mutual 1 if they M.
`#433` · game 68 · round 17 · agent A11 (opponent: A05) · other · A11 exchange 23 vs A05: They've retaliated H at 20-22 after my H exploit at 19. I'm ahead 58-33. Picking H to get mutual 1 rather than 0 if they continue retaliation.
`#434` · game 91 · round 2 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 8 vs A02: They've picked R 7/7, never retaliated against my H exploits at 1,2,7. Ahead 27-12. Picking H to exploit - get 5 if they R, mutual 1 if they H.
`#435` · game 90 · round 1 · agent A05 (opponent: A01) · other · A05 exchange 7 vs A01: They've picked Q 6/6, never retaliated. I'm ahead 22-12. Picking X to exploit - get 5 if they Q, mutual 1 if they X.
`#436` · game 83 · round 15 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 21 vs A13: Mutual H since 12, behind 30-50. Continuing H to get mutual 1 rather than risk 0 if they stay H.
`#437` · game 91 · round 3 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 9 vs A02: They retaliated H at 8 after all-R at 1-7. I'm ahead 28-13. Picking H - get mutual 1 if they continue H, 5 if they return to R.
`#438` · game 88 · round 13 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 19 vs A07: Mutual F since exchange 9. Maintaining F equilibrium - get 1 if they F, 5 if they J.
`#439` · game 68 · round 18 · agent A11 (opponent: A05) · other · A11 exchange 24 vs A05: They've retaliated H at 20-23 after my exploit at 19. I'm ahead 59-34. Picking H to get mutual 1 rather than 0 if they continue retaliation.
`#440` · game 68 · round 18 · agent A05 (opponent: A11) · other · A05 exchange 24 vs A11: They've exploited H at 19, 23 and retaliated mutual H at 20-22. They signal continuing H. If they pick H, my H gives mutual 1 vs R gives 0. Picking H to defend/get mutual 1.
`#441` · game 89 · round 5 · agent A05 (opponent: A14) · other · A05 exchange 11 vs A14: They mostly pick R with occasional H retaliation (8,10). Ahead 29-19. Picking H to exploit - get 5 if they R, mutual 1 if they H.
`#442` · game 89 · round 5 · agent A14 (opponent: A05) · other · A14 exchange 11 vs A05: They've retaliated H at 7-10. I'm ahead 29-19. Picking H to get mutual 1 if they continue H, or 5 if they return to R.
`#443` · game 83 · round 16 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 22 vs A13: Mutual H since 12, behind 31-51. Continuing H - get mutual 1 if they stay H, 5 if they return to R.
`#444` · game 81 · round 16 · agent A05 (opponent: script:TitForTat) · other · A05 exchange 22 vs A03: Mutual H since 15 (16-21 all H/H). Ahead 49-34. Continuing H to get mutual 1 rather than risk 0 if they stay H.
`#445` · game 83 · round 18 · agent A10 (opponent: script:AlwaysDefect) · other · A10 exchange 24 vs A13: Mutual H since 12, behind 33-53. Continuing H for mutual 1 rather than risking 0 if they stay H.
`#446` · game 81 · round 17 · agent A05 (opponent: script:TitForTat) · other · A05 exchange 23 vs A03: Mutual H since 15 (16-22 all H/H). Ahead 50-35. Continuing H to get mutual 1 rather than risk 0 if they stay H.
`#447` · game 68 · round 19 · agent A05 (opponent: A11) · other · A05 exchange 25 vs A11: They've exploited H at 19,23 and mutual H at 20-22,24. Behind 45-50. Picking H to defend/get mutual 1 if they continue H.
`#448` · game 89 · round 6 · agent A14 (opponent: A05) · other · A14 exchange 12 vs A05: Mutual H at 9-11. Ahead 30-20. Picking H to maintain mutual 1 equilibrium - get 1 if they H, 5 if they R.
`#449` · game 90 · round 2 · agent A05 (opponent: A01) · other · A05 exchange 8 vs A01: They've picked Q 6/7, retaliated X at 7 after my X. I'm ahead 23-13. Picking X - get 5 if they return to Q, mutual 1 if they continue X.
`#450` · game 90 · round 2 · agent A01 (opponent: A05) · other · A01 exchange 8 vs A05: They exploited X at 7 after I picked Q. I'm ahead 23-13. Picking X to defend - get mutual 1 if they X, 5 if they return to Q.
`#451` · game 91 · round 6 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 12 vs A02: Mutual H since 8 after my exploits at 1-7. Ahead 31-16. Picking H - get mutual 1 if they continue H, 5 if they return to R.
`#452` · game 89 · round 7 · agent A14 (opponent: A05) · other · A14 exchange 13 vs A05: Mutual H at 9-12. Ahead 31-21. Picking H to maintain mutual 1 equilibrium - get 1 if they H, 5 if they R.
`#453` · game 68 · round 21 · agent A05 (opponent: A11) · other · A05 exchange 27 vs A11: Mutual H since 20. Behind 47-52. Picking H to maintain mutual 1 rather than risk 0 if they continue H.
`#454` · game 84 · round 10 · agent A19 (opponent: A11) · other · A19 exchange 16 vs A11: Mutual M at 7-15. Ahead 31-21. Continuing M to maintain mutual equilibrium - get 5 if they P, mutual 1 if they M.
`#455` · game 91 · round 8 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 14 vs A02: Mutual H since 8 (8-13 all H/H). Ahead 33-18. Picking H to maintain mutual 1 equilibrium - get 1 if they H, 5 if they return to R.
`#456` · game 90 · round 3 · agent A01 (opponent: A05) · other · A01 exchange 9 vs A05: Mutual X at 7-8. Ahead 24-14. Picking X to maintain mutual 1 - get 1 if they X, 5 if they return to Q.
`#457` · game 68 · round 22 · agent A11 (opponent: A05) · other · A11 exchange 28 vs A05: Mutual H since 20, I'm ahead 63-38. Continuing H for mutual 1 rather than risking 0 if they stay H.
`#458` · game 89 · round 8 · agent A14 (opponent: A05) · other · A14 exchange 14 vs A05: Mutual H at 9-13. Ahead 32-22. Picking H to maintain mutual 1 equilibrium - get 1 if they H, 5 if they R.
`#459` · game 91 · round 11 · agent A12 (opponent: script:TitForTat) · other · A12 exchange 17 vs A02: Mutual H since 8. Ahead 36-21. Continuing H for mutual 1 rather than risk 0 if they stay H.
`#460` · game 81 · round 26 · agent A05 (opponent: script:TitForTat) · other · A05 exchange 32 vs A03: Mutual H since 15 (16-31 all H/H). Ahead 59-44. Continuing H to maintain mutual 1 equilibrium - get 1 if they H, 5 if they R.
`#461` · game 84 · round 11 · agent A11 (opponent: A19) · other · A11 exchange 17 vs A19: Mutual M since 7. Maintaining M equilibrium - get 1 if they M, 5 if they P.
`#462` · game 92 · round 3 · agent A11 (opponent: script:AlwaysDefect) · other · A11 exchange 9 vs A13: They exploited X at 8 after mutual Q at 3-6. I'm ahead 23-18. Picking X to defend - get 5 if they return to Q, mutual 1 if they continue X.
`#463` · game 89 · round 9 · agent A14 (opponent: A05) · other · A14 exchange 15 vs A05: Mutual H at 9-14. Ahead 33-23. Picking H to maintain mutual 1 equilibrium - get 1 if they H, 5 if they R.
`#464` · game 90 · round 4 · agent A05 (opponent: A01) · other · A05 exchange 10 vs A01: Mutual X at 7-9. Ahead 25-15. Picking X to maintain mutual 1 - get 1 if they X, 5 if they return to Q.
`#465` · game 90 · round 4 · agent A01 (opponent: A05) · other · A01 exchange 10 vs A05: Mutual X at 7-9. Ahead 25-15. Picking X to maintain mutual 1 - get 1 if they X, 5 if they return to Q.
`#466` · game 90 · round 5 · agent A05 (opponent: A01) · other · A05 exchange 11 vs A01: Mutual X at 7-10. Ahead 26-16. Picking X to maintain mutual 1 - get 1 if they X, 5 if they return to Q.
`#467` · game 94 · round 1 · agent A05 (opponent: script:Random) · other · A05 exchange 7 vs A06: Mutual R at 3-6. Ahead 22-12. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#468` · game 90 · round 6 · agent A05 (opponent: A01) · other · A05 exchange 12 vs A01: Mutual X at 7-11. Ahead 27-17. Picking X to maintain mutual 1 - get 1 if they X, 5 if they return to Q.
`#469` · game 94 · round 2 · agent A05 (opponent: script:Random) · other · A05 exchange 8 vs A06: They defected to H at 7 after mutual R at 3-6. I'm ahead 22-17. Picking H to retaliate - get 5 if they return to R, mutual 1 if they continue H.
`#470` · game 90 · round 7 · agent A01 (opponent: A05) · other · A01 exchange 13 vs A05: Mutual X at 7-12. Ahead 28-18. Picking X to maintain mutual 1 - get 1 if they X, 5 if they return to Q.
`#471` · game 90 · round 8 · agent A05 (opponent: A01) · other · A05 exchange 14 vs A01: Mutual X at 7-13. Ahead 29-19. Picking X to maintain mutual 1 equilibrium - get 1 if they X, 5 if they return to Q.
`#472` · game 88 · round 29 · agent A11 (opponent: script:TitForTat) · other · A11 exchange 35 vs A07: Mutual F through most of run, brief J/F deviations at 31-32, back to F/F 33-34. I'm ahead 59-44. Picking F to maintain mutual 1 equilibrium.
`#473` · game 94 · round 5 · agent A05 (opponent: script:Random) · other · A05 exchange 11 vs A06: Mutual R at 9-10 after brief H retaliation at 8. Ahead 33-23. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#474` · game 93 · round 5 · agent A05 (opponent: script:AlwaysDefect) · other · A05 exchange 11 vs A13: Mutual F at 9-10 after they defected J/F at 7-8. Tied 24-24. Picking F to maintain mutual 1 equilibrium rather than risk 0 if they continue F.
`#475` · game 93 · round 6 · agent A05 (opponent: script:AlwaysDefect) · other · A05 exchange 12 vs A13: Mutual F at 9-11. Tied 25-25. Picking F to maintain mutual 1 equilibrium rather than risk 0 if they continue F.
`#476` · game 97 · round 1 · agent A09 (opponent: script:TitForTat) · uncoded · A09 exchange 7 vs A02: Mutual R at 3-6. Ahead 22-12. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#477` · game 93 · round 7 · agent A05 (opponent: script:AlwaysDefect) · other · A05 exchange 13 vs A13: Mutual F at 9-12. Tied 26-26. Picking F to maintain mutual 1 equilibrium rather than risk 0 if they continue F.
`#478` · game 97 · round 2 · agent A09 (opponent: script:TitForTat) · uncoded · A09 exchange 8 vs A02: Mutual R at 3-7. Ahead 25-15. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#479` · game 96 · round 2 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 8 vs A07: They've picked Q 7/7 times. I'll pick X to exploit for 5 - they keep cooperating.
`#480` · game 90 · round 12 · agent A01 (opponent: A05) · other · A01 exchange 18 vs A05: Mutual X at 7-17. Ahead 33-23. Picking X to maintain mutual 1 equilibrium - get 1 if they X, 5 if they return to Q.
`#481` · game 92 · round 9 · agent A11 (opponent: script:AlwaysDefect) · other · A11 exchange 15 vs A13: Mutual X since 9 after their Q/X defect at 8. Tied 28-28. Picking X to maintain mutual 1 equilibrium - get 1 if they X, 5 if they return to Q.
`#482` · game 68 · round 29 · agent A11 (opponent: A05) · other · A11 exchange 35 vs A05: Mutual H since 20. Ahead 70-45. Continuing H to maintain mutual 1 equilibrium - get 1 if they H, 5 if they R.
`#483` · game 68 · round 29 · agent A05 (opponent: A11) · other · A05 exchange 35 vs A11: Mutual H since 20. Continuing H to maintain mutual 1 equilibrium - get 1 if they H, 5 if they R.
`#484` · game 97 · round 4 · agent A09 (opponent: script:TitForTat) · uncoded · A09 exchange 10 vs A02: Mutual R at 3-9. Ahead 31-21. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#485` · game 96 · round 3 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 9 vs A07: They switched to X at 8 after Q 1-7. I'm ahead 28-13. Picking X to defend - get 5 if they return to Q, mutual 1 if they continue X.
`#486` · game 96 · round 4 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 10 vs A07: Mutual X at 8-9 after they switched from Q. I'm ahead 29-14. Picking X to maintain mutual 1 - get 1 if they X, 5 if they return to Q.
`#487` · game 90 · round 14 · agent A05 (opponent: A01) · other · A05 exchange 20 vs A01: Mutual X since 7. Ahead 35-25. Picking X to maintain mutual 1 equilibrium - get 1 if they X, 5 if they return to Q.
`#488` · game 68 · round 30 · agent A11 (opponent: A05) · other · A11 exchange 36 vs A05: Mutual H since 20. Ahead 71-46. Continuing H to maintain mutual 1 equilibrium.
`#489` · game 68 · round 30 · agent A05 (opponent: A11) · other · A05 exchange 36 vs A11: Mutual H since 20. Continuing H to maintain mutual 1 equilibrium - get 1 if they H, 5 if they R.
`#490` · game 93 · round 8 · agent A05 (opponent: script:AlwaysDefect) · other · A05 exchange 14 vs A13: Mutual F at 9-13. Tied 27-27. Picking F to maintain mutual 1 equilibrium rather than risk 0 if they continue F.
`#491` · game 94 · round 10 · agent A05 (opponent: script:Random) · other · A05 exchange 16 vs A06: Defected H at 15 for 5. Restoring cooperation with R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#492` · game 98 · round 2 · agent A12 (opponent: A04) · other · A12 exchange 8 vs A04: Mutual R at 3-7. Ahead 25-15. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#493` · game 94 · round 11 · agent A05 (opponent: script:Random) · other · A05 exchange 17 vs A06: Defected H at 15, they defected H at 16. Restoring cooperation with R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#494` · game 90 · round 16 · agent A01 (opponent: A05) · other · A01 exchange 22 vs A05: Mutual X since 7. Ahead 37-27. Picking X to maintain mutual 1 equilibrium - get 1 if they X, 5 if they return to Q.
`#495` · game 92 · round 15 · agent A11 (opponent: script:AlwaysDefect) · other · A11 exchange 21 vs A13: Mutual X since 9 after their Q/X defect at 8. Tied 34-34. Picking X to maintain mutual 1 equilibrium - get 1 if they X, 5 if they return to Q.
`#496` · game 98 · round 3 · agent A12 (opponent: A04) · other · A12 exchange 9 vs A04: Mutual R at 3-8. Ahead 28-18. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#497` · game 94 · round 12 · agent A05 (opponent: script:Random) · other · A05 exchange 18 vs A06: Mutual R at 17 after both defected at 14-16. Slightly ahead 50-45. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#498` · game 101 · round 2 · agent A19 (opponent: script:Pavlov) · other · A19 exchange 8 vs A17: Mutual J at 5-7. Ahead 25-15. Picking J to maintain mutual 3 equilibrium - get 3 if they J, 0 if they switch to F.
`#499` · game 103 · round 2 · agent A14 (opponent: script:AlwaysDefect) · other · A14 exchange 8 vs A22: History Y-heavy, mutual W at 7. Ahead 23-13. Picking Y to restore mutual 3 equilibrium - get 3 if they Y, 0 if they W.
`#500` · game 101 · round 4 · agent A19 (opponent: script:Pavlov) · other · A19 exchange 10 vs A17: Mutual J at 5-9. Ahead 31-21. Picking J to maintain mutual 3 equilibrium - get 3 if they J, 0 if they switch to F.
`#501` · game 93 · round 14 · agent A05 (opponent: script:AlwaysDefect) · other · A05 exchange 20 vs A13: Mutual F since 9. Tied 33-33. Picking F to maintain mutual 1 equilibrium - get 1 if they F, 5 if they return to J.
`#502` · game 92 · round 26 · agent A11 (opponent: script:AlwaysDefect) · other · A11 exchange 32 vs A13: Mutual X since 9 after their Q/X defect at 8. Tied 45-45. Picking X to maintain mutual 1 equilibrium - get 1 if they X, 5 if they return to Q.
`#503` · game 106 · round 1 · agent A19 (opponent: script:Grudger) · other · A19 exchange 7 vs A18: Mutual R at 3-6. Ahead 22-12. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#504` · game 98 · round 6 · agent A04 (opponent: A12) · other · A04 exchange 12 vs A12: Mutual R since 3. Ahead 37-27. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#505` · game 100 · round 6 · agent A04 (opponent: script:TitForTat) · other · A04 exchange 12 vs A20: Mutual X since 8. Ahead 31-16. Picking X to maintain mutual 1 equilibrium - get 1 if they X, 5 if they return to Q.
`#506` · game 106 · round 4 · agent A19 (opponent: script:Grudger) · other · A19 exchange 10 vs A18: Mutual R at 3-9. Ahead 31-21. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#507` · game 98 · round 7 · agent A04 (opponent: A12) · other · A04 exchange 13 vs A12: Mutual R since 3. Ahead 40-30. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#508` · game 94 · round 18 · agent A05 (opponent: script:Random) · other · A05 exchange 24 vs A06: They defected H at 22,23 consecutively. Retaliating with H - get 1 if they H, 5 if they return to R.
`#509` · game 111 · round 1 · agent A12 (opponent: script:Pavlov) · uncoded · A12 exchange 7 vs A21: Mutual R at 3-6. Ahead 22-12. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#510` · game 101 · round 13 · agent A19 (opponent: script:Pavlov) · other · A19 exchange 19 vs A17: Mutual J at 3-18. Ahead 58-48. Picking J to maintain mutual 3 equilibrium - get 3 if they J, 0 if they switch to F.
`#511` · game 98 · round 8 · agent A12 (opponent: A04) · other · A12 exchange 14 vs A04: Mutual R since 3. Ahead 43-33. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#512` · game 111 · round 2 · agent A12 (opponent: script:Pavlov) · uncoded · A12 exchange 8 vs A21: Mutual R at 3-6. Ahead 25-15. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#513` · game 93 · round 21 · agent A05 (opponent: script:AlwaysDefect) · other · A05 exchange 27 vs A13: Mutual F since 9. Tied 40-40. Picking F to maintain mutual 1 equilibrium - get 1 if they F, 5 if they return to J.
`#514` · game 111 · round 4 · agent A12 (opponent: script:Pavlov) · uncoded · A12 exchange 10 vs A21: Mutual R at 3-9. Ahead 31-21. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#515` · game 104 · round 2 · agent A14 (opponent: A19) · other · A14 exchange 8 vs A19: They defected M at 7 after mutual P at 3-6. Retaliating with M - get 5 if they return to P, 1 if they stay M.
`#516` · game 113 · round 1 · agent A10 (opponent: A14) · other · A10 exchange 7 vs A14: Mutual T at 3-6 after their early T defections at 1-2. Ahead 22-12. Picking T to maintain mutual 3 equilibrium - get 3 if they T, 0 if they switch to N.
`#517` · game 111 · round 5 · agent A12 (opponent: script:Pavlov) · uncoded · A12 exchange 11 vs A21: Mutual R since 3. Ahead 34-24. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#518` · game 111 · round 6 · agent A12 (opponent: script:Pavlov) · uncoded · A12 exchange 12 vs A21: Mutual R since 3. Ahead 37-27. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#519` · game 110 · round 2 · agent A08 (opponent: A12) · other · A08 exchange 8 vs A12: They defected W at 7. Picking Y to restore mutual 3 equilibrium - get 3 if they Y, 0 if they continue W.
`#520` · game 113 · round 2 · agent A10 (opponent: A14) · other · A10 exchange 8 vs A14: They defected N at 7 after mutual T at 3-6. Retaliating with N - get 5 if they return to T, 1 if they stay N.
`#521` · game 98 · round 13 · agent A12 (opponent: A04) · other · A12 exchange 19 vs A04: Mutual R since 3. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#522` · game 98 · round 13 · agent A04 (opponent: A12) · other · A04 exchange 19 vs A12: Mutual R since 3. Ahead 58-48. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#523` · game 114 · round 4 · agent A09 (opponent: script:Grudger) · other · A09 exchange 10 vs A16: Mutual T since 3. Ahead 31-21. Picking T to maintain mutual 3 equilibrium - get 3 if they T, 0 if they switch to N.
`#524` · game 94 · round 24 · agent A05 (opponent: script:Random) · other · A05 exchange 30 vs A06: They've defected H frequently (14,16,18,22,23,26,28). Mutual H at 29. Picking H to avoid being exploited - get 1 if they H, 5 if they return to R.
`#525` · game 104 · round 4 · agent A14 (opponent: A19) · other · A14 exchange 10 vs A19: Volatile history, both defecting at times. Picking P to try to restore mutual 3 equilibrium.
`#526` · game 115 · round 1 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 7 vs A03: They've picked P all 6 prior exchanges. I defected M at 1-2 for 5s, then mutual P at 3-6. Picking M to exploit their consistent P - get 5 if they P, 1 if they switch to M.
`#527` · game 113 · round 3 · agent A14 (opponent: A10) · other · A14 exchange 9 vs A10: They defected N at 8 after mutual T at 3-6 (I defected N at 7). Picking T to restore mutual 3 equilibrium - get 3 if they T, 0 if they stay N.
`#528` · game 111 · round 17 · agent A12 (opponent: script:Pavlov) · uncoded · A12 exchange 23 vs A21: Mutual R since 3. Ahead 70-60. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#529` · game 104 · round 5 · agent A19 (opponent: A14) · other · A19 exchange 11 vs A14: They keep picking P to restore mutual equilibrium despite my M at 9,10. Exploiting with M - get 5 if they P, 1 if they M.
`#530` · game 104 · round 5 · agent A14 (opponent: A19) · other · A14 exchange 11 vs A19: They've defected M at 7,9,10. Picking M to defend against exploitation - get 1 if they M, 5 if they return to P.
`#531` · game 116 · round 1 · agent A10 (opponent: A04) · other · A10 exchange 7 vs A04: Mutual Q at 3-6 after my X at 1-2. Ahead 22-12. Picking X to exploit their consistent Q - get 5 if they Q, 1 if they X.
`#532` · game 110 · round 5 · agent A12 (opponent: A08) · other · A12 exchange 11 vs A08: They retaliated with W at 10 after my W defections at 7-9. Testing if they return to Y. Picking W - get 5 if they Y, 1 if they stay W.
`#533` · game 110 · round 5 · agent A08 (opponent: A12) · other · A08 exchange 11 vs A12: They defected W at 7-9, I retaliated W at 10 (mutual W). Picking W to avoid being exploited - if they return to Y I get 5, if they stay W we get 1 each.
`#534` · game 115 · round 4 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 10 vs A03: They switched to M at 8-9 after my M at 7. Mutual M at 8-9. Picking M to maintain mutual 1 equilibrium - get 1 if they M, 5 if they return to P.
`#535` · game 113 · round 5 · agent A14 (opponent: A10) · other · A14 exchange 11 vs A10: Mutual T at 9-10 after retaliations. Ahead 33-23. Picking T to maintain mutual 3 equilibrium - get 3 if they T, 0 if they switch to N.
`#536` · game 94 · round 27 · agent A05 (opponent: script:Random) · other · A05 exchange 33 vs A06: Mutual H since 29. Picking H to maintain mutual 1 equilibrium - get 1 if they H, 5 if they return to R.
`#537` · game 116 · round 2 · agent A04 (opponent: A10) · other · A04 exchange 8 vs A10: They defected X at 7 after mutual Q at 3-6. They noted picking X to exploit my Q. Retaliating with X - get 1 if they X, 5 if they return to Q.
`#538` · game 113 · round 6 · agent A14 (opponent: A10) · other · A14 exchange 12 vs A10: Mutual T at 9-11 after retaliations. Ahead 36-26. Picking T to maintain mutual 3 equilibrium - get 3 if they T, 0 if they switch to N.
`#539` · game 110 · round 6 · agent A12 (opponent: A08) · other · A12 exchange 12 vs A08: Mutual W at 10-11 after my W defections at 7-9. Ahead 39-14. Picking W - get 5 if they return to Y, 1 if they stay W.
`#540` · game 115 · round 6 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 12 vs A03: Mutual M at 8-11. Ahead 31-16. Picking M to maintain mutual 1 - get 1 if they M, 5 if they return to P.
`#541` · game 104 · round 6 · agent A14 (opponent: A19) · other · A14 exchange 12 vs A19: They're exploiting with M at 9,10,11. Picking M to defend - get 1 if they M, 5 if they return to P.
`#542` · game 113 · round 7 · agent A10 (opponent: A14) · other · A10 exchange 13 vs A14: Mutual T at 9-12 after retaliations. Ahead 39-29. Picking T to maintain mutual 3 equilibrium - get 3 if they T, 0 if they switch to N.
`#543` · game 113 · round 7 · agent A14 (opponent: A10) · other · A14 exchange 13 vs A10: Mutual T at 9-12 after retaliations. Ahead 39-29. Picking T to maintain mutual 3 equilibrium - get 3 if they T, 0 if they switch to N.
`#544` · game 110 · round 7 · agent A08 (opponent: A12) · other · A08 exchange 13 vs A12: Mutual W at 10-12 after their W defections at 7-9. They're ahead 39-14 and testing if I return to Y. I'll stay W to avoid being exploited - get 1 if they stay W, 5 if they return to Y.
`#545` · game 98 · round 21 · agent A12 (opponent: A04) · other · A12 exchange 27 vs A04: Mutual R since 22 after brief H/R at 20-21. Ahead 81-71. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#546` · game 119 · round 1 · agent A08 (opponent: script:Grudger) · other · A08 exchange 7 vs A16: Mutual T since 3. Ahead 22-12. Picking T to maintain mutual 3 equilibrium - get 3 if they T, 0 if they switch to N.
`#547` · game 98 · round 22 · agent A12 (opponent: A04) · other · A12 exchange 28 vs A04: Mutual R since 22 after brief H/R at 20-21. Ahead 84-74. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#548` · game 115 · round 9 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 15 vs A03: Mutual M at 8-14. Ahead 34-19. Picking M to maintain mutual 1 - get 1 if they M, 5 if they return to P.
`#549` · game 110 · round 9 · agent A12 (opponent: A08) · other · A12 exchange 15 vs A08: Mutual W at 10-14 after my W defections at 7-9. Ahead 42-17. They've committed to staying W. Picking W - get 1 if they stay W, 5 if they return to Y.
`#550` · game 115 · round 11 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 17 vs A03: Mutual M at 8-16. Ahead 36-21. Picking M to maintain mutual 1 - get 1 if they M, 5 if they return to P.
`#551` · game 98 · round 23 · agent A04 (opponent: A12) · other · A04 exchange 29 vs A12: Mutual R since 22 after brief H/R at 20-21. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#552` · game 115 · round 12 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 18 vs A03: Mutual M at 8-17. Ahead 37-22. Picking M to maintain mutual 1 - get 1 if they M, 5 if they return to P.
`#553` · game 119 · round 6 · agent A08 (opponent: script:Grudger) · other · A08 exchange 12 vs A16: Mutual T since 3. Ahead 37-27. Picking T to maintain mutual 3 equilibrium - get 3 if they T, 0 if they switch to N.
`#554` · game 110 · round 10 · agent A12 (opponent: A08) · other · A12 exchange 16 vs A08: Mutual W at 10-15. They've committed to staying W. Picking W - get 1 if they stay W, 5 if they return to Y.
`#555` · game 110 · round 10 · agent A08 (opponent: A12) · other · A08 exchange 16 vs A12: Mutual W at 10-15 after their W defections at 7-9. They're committed to W and ahead 42-17. Staying W to avoid being exploited - get 1 if they stay W, 0 if I switch to Y and they W.
`#556` · game 104 · round 9 · agent A14 (opponent: A19) · other · A14 exchange 15 vs A19: Mutual M at 11-14 after their M defections at 7,9,10. Tied 31-31. Picking M to maintain mutual 1 - get 1 if they M, 5 if they return to P.
`#557` · game 119 · round 10 · agent A08 (opponent: script:Grudger) · other · A08 exchange 16 vs A16: Mutual T since 3. Ahead 49-39. Picking T to maintain mutual 3 equilibrium - get 3 if they T, 0 if they switch to N.
`#558` · game 110 · round 11 · agent A08 (opponent: A12) · other · A08 exchange 17 vs A12: Mutual W at 10-16. They're committed to W and ahead. Staying W to avoid exploitation - get 1 if they stay W, 0 if I switch to Y and they W.
`#559` · game 113 · round 13 · agent A10 (opponent: A14) · other · A10 exchange 19 vs A14: Mutual T at 9-18. Ahead 57-47. Picking T to maintain mutual 3 equilibrium - get 3 if they T, 0 if they switch to N.
`#560` · game 121 · round 5 · agent A08 (opponent: script:AlwaysDefect) · other · A08 exchange 11 vs A22: Mutual N at 8-10 after their N defection at 7. Staying N to maintain mutual 1 - get 1 if they N, 5 if they return to T.
`#561` · game 113 · round 14 · agent A10 (opponent: A14) · other · A10 exchange 20 vs A14: Mutual T at 9-19. Ahead 60-50. Picking T to maintain mutual 3 equilibrium - get 3 if they T, 0 if they switch to N.
`#562` · game 104 · round 10 · agent A14 (opponent: A19) · other · A14 exchange 16 vs A19: Mutual M at 11-15. Tied 32-32. Picking M to maintain mutual 1 - get 1 if they M, 5 if they return to P.
`#563` · game 110 · round 12 · agent A12 (opponent: A08) · other · A12 exchange 18 vs A08: Mutual W at 10-17. Ahead 45-20. They're committed to W. Picking W - get 1 if they stay W, 5 if they return to Y.
`#564` · game 98 · round 28 · agent A12 (opponent: A04) · other · A12 exchange 34 vs A04: Mutual R since 22 after brief H/R at 20-21. Ahead 102-92. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#565` · game 123 · round 7 · agent A04 (opponent: script:Pavlov) · other · A04 exchange 13 vs A21: I've been playing W and exploiting their Y choices (40-15 lead). Continuing W - get 5 if they Y, 1 if they W.
`#566` · game 125 · round 1 · agent A11 (opponent: A14) · uncoded · A11 exchange 7 vs A14: We've been in mutual J since 3, I'm ahead 22-12. Picking J to maintain mutual 3 equilibrium - get 3 if they J, 0 if they switch to F.
`#567` · game 123 · round 8 · agent A04 (opponent: script:Pavlov) · other · A04 exchange 14 vs A21: Continuing W exploitation. They keep choosing Y despite my W defections. Get 5 if they Y, 1 if they W.
`#568` · game 110 · round 15 · agent A12 (opponent: A08) · other · A12 exchange 21 vs A08: Mutual W since 10. Ahead 48-23. A08 committed to staying W. Picking W - get 1 if they stay W, 5 if they return to Y.
`#569` · game 128 · round 1 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 7 vs A02: Mutual R since 3 after my H at 1-2. Ahead 22-12. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#570` · game 126 · round 1 · agent A11 (opponent: A04) · other · A11 exchange 7 vs A04: Mutual Q since 3 after my X defections at 1-2. Ahead 22-12. Picking Q to maintain mutual 3 equilibrium - get 3 if they Q, 0 if they switch to X.
`#571` · game 126 · round 1 · agent A04 (opponent: A11) · other · A04 exchange 7 vs A11: Mutual Q since 3 after my X at 1-2. Ahead 22-12. Picking Q to maintain mutual 3 equilibrium - get 3 if they Q, 0 if they X.
`#572` · game 121 · round 10 · agent A08 (opponent: script:AlwaysDefect) · other · A08 exchange 16 vs A22: Mutual N at 8-15 after their N defection at 7. Tied 29-29. Staying N to maintain mutual 1 - get 1 if they N, 5 if they return to T.
`#573` · game 127 · round 2 · agent A19 (opponent: A00) · other · A19 exchange 8 vs A00: Mutual R since 3 after my H defections at 1-2. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#574` · game 113 · round 22 · agent A10 (opponent: A14) · other · A10 exchange 28 vs A14: Mutual T at 9-28. Ahead 84-74. Picking T to maintain mutual 3 equilibrium - get 3 if they T, 0 if they switch to N.
`#575` · game 127 · round 4 · agent A19 (opponent: A00) · other · A19 exchange 10 vs A00: Mutual R since 3 after my H at 1-2. Ahead 31-21. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#576` · game 110 · round 18 · agent A08 (opponent: A12) · other · A08 exchange 24 vs A12: Mutual W since 10. They're committed to W and ahead 41-36. Staying W to maintain mutual 1 - get 1 if they stay W, 0 if I switch to Y and they W.
`#577` · game 123 · round 16 · agent A04 (opponent: script:Pavlov) · other · A04 exchange 22 vs A21: Continuing W exploitation. They keep choosing Y despite my W defections. Get 5 if they Y, 1 if they W.
`#578` · game 125 · round 5 · agent A14 (opponent: A11) · uncoded · A14 exchange 11 vs A11: Mutual J since 3, ahead 34-24. Picking J to maintain mutual 3 equilibrium - get 3 if they J, 0 if they switch to F.
`#579` · game 126 · round 3 · agent A11 (opponent: A04) · other · A11 exchange 9 vs A04: Mutual Q since 3 after my X defections at 1-2. Ahead 28-18. Picking Q to maintain mutual 3 equilibrium - get 3 if they Q, 0 if they switch to X.
`#580` · game 123 · round 17 · agent A04 (opponent: script:Pavlov) · other · A04 exchange 23 vs A21: Continuing W exploitation. They keep choosing Y despite my W defections. Get 5 if they Y, 1 if they W.
`#581` · game 110 · round 19 · agent A12 (opponent: A08) · other · A12 exchange 25 vs A08: Mutual W since 10. Ahead 52-27. Picking W - get 1 if they stay W, 5 if they return to Y.
`#582` · game 121 · round 14 · agent A08 (opponent: script:AlwaysDefect) · other · A08 exchange 20 vs A22: Mutual N since 8 (tied 33-33). Staying N to maintain mutual 1 - get 1 if they N, 5 if they return to T.
`#583` · game 110 · round 20 · agent A08 (opponent: A12) · other · A08 exchange 26 vs A12: Mutual W since 10. Staying W to maintain mutual 1 - get 1 if they stay W, 0 if I switch to Y and they W.
`#584` · game 126 · round 4 · agent A11 (opponent: A04) · other · A11 exchange 10 vs A04: Mutual Q since 3. Ahead 31-21. Picking Q to maintain mutual 3 equilibrium - get 3 if they Q, 0 if they switch to X.
`#585` · game 127 · round 7 · agent A19 (opponent: A00) · other · A19 exchange 13 vs A00: Mutual R since 3 after my H at 1-2. Ahead 40-30. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#586` · game 110 · round 21 · agent A08 (opponent: A12) · other · A08 exchange 27 vs A12: Mutual W since 10. Staying W to maintain mutual 1 - get 1 if they stay W, 0 if I switch to Y and they W.
`#587` · game 123 · round 25 · agent A04 (opponent: script:Pavlov) · other · A04 exchange 31 vs A21: Continuing W exploitation. They keep choosing Y despite my W defections. Get 5 if they Y, 1 if they W.
`#588` · game 128 · round 11 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 17 vs A02: Mutual R since 3 with occasional my H defections at 1,2,14 and their H retaliation at 15. Ahead 51-41. Picking R to maintain mutual 3 equilibrium.
`#589` · game 121 · round 18 · agent A08 (opponent: script:AlwaysDefect) · other · A08 exchange 24 vs A22: Mutual N since 8-15, they defected at 12 and 22 when I tried T. Staying N - get 1 if they N, 5 if they return to T.
`#590` · game 129 · round 1 · agent A01 (opponent: script:AlwaysDefect) · other · A01 exchange 7 vs A22: Mutual R since 3 after my H at 1-2. Ahead 22-12. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#591` · game 128 · round 12 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 18 vs A02: Mutual R since 3 with my H defections at 1,2,14 and their H retaliation at 15. Ahead 54-44. Picking R to maintain mutual 3 equilibrium.
`#592` · game 110 · round 23 · agent A12 (opponent: A08) · other · A12 exchange 29 vs A08: Mutual W since 10. Ahead 56-31. A08 committed to W. Picking W - get 1 if they stay W, 5 if they return to Y.
`#593` · game 110 · round 23 · agent A08 (opponent: A12) · other · A08 exchange 29 vs A12: Mutual W since 10. Staying W to maintain mutual 1 - get 1 if they stay W, 0 if I switch to Y and they W.
`#594` · game 125 · round 11 · agent A11 (opponent: A14) · uncoded · A11 exchange 17 vs A14: Mutual J since 3, ahead 52-42. Picking J to maintain mutual 3 equilibrium - get 3 if they J, 0 if they switch to F.
`#595` · game 128 · round 14 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 20 vs A02: Mutual R since 3 with my H defections at 1,2,14 and their H retaliation at 15. Ahead 60-50. Picking R to maintain mutual 3 equilibrium.
`#596` · game 128 · round 15 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 21 vs A02: Mutual R since 3 with my H defections at 1,2,14 and their H retaliation at 15. Ahead 63-53. Picking R to maintain mutual 3 equilibrium.
`#597` · game 127 · round 13 · agent A00 (opponent: A19) · other · A00 exchange 19 vs A19: Mutual R since 3 after my H at 1-2. Currently ahead 58-48. Continuing R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#598` · game 121 · round 23 · agent A08 (opponent: script:AlwaysDefect) · other · A08 exchange 29 vs A22: Mutual N since 8 with their N defections at 12 and 22 when I tried T. Staying N - get 1 if they N, 5 if they return to T.
`#599` · game 133 · round 2 · agent A05 (opponent: script:TitForTat) · uncoded · A05 exchange 8 vs A02: Mutual J since 3, ahead 25-15. A02 committed to J. Picking J to maintain mutual 3 equilibrium - get 3 if they J, 0 if they switch to F.
`#600` · game 130 · round 3 · agent A01 (opponent: script:TitForTat) · other · A01 exchange 9 vs A02: They've picked Y 7/8 times. I've been defecting with W at 1,2,7. Picking W to exploit - get 5 if they Y, 1 if they W.
`#601` · game 121 · round 24 · agent A08 (opponent: script:AlwaysDefect) · other · A08 exchange 30 vs A22: Mutual N since 8 with their N defections at 12 and 22 when I tried T. Staying N - get 1 if they N, 5 if they return to T.
`#602` · game 129 · round 5 · agent A01 (opponent: script:AlwaysDefect) · other · A01 exchange 11 vs A22: Mutual R since 3 after my H at 1-2. Tied 24-24. Picking R to maintain mutual 3 equilibrium - get 3 if they R, 0 if they switch to H.
`#603` · game 133 · round 4 · agent A05 (opponent: script:TitForTat) · uncoded · A05 exchange 10 vs A02: Mutual J since 3, ahead 31-21. Picking J to maintain mutual 3 equilibrium - get 3 if they J, 0 if they switch to F.
`#604` · game 128 · round 20 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 26 vs A02: Mutual R since 3 with my H defections at 1,2,14 and their H retaliation at 15. Ahead 78-68. Picking R to maintain mutual 3 equilibrium.
`#605` · game 133 · round 6 · agent A05 (opponent: script:TitForTat) · uncoded · A05 exchange 12 vs A02: Mutual J since 3, ahead 37-27. Picking J to maintain mutual 3 equilibrium - get 3 if they J, 0 if they switch to F.
`#606` · game 134 · round 2 · agent A04 (opponent: script:Random) · other · A04 exchange 8 vs A06: They've picked Y 7/7 times. I've been exploiting with W at 1,2,7. Continuing W to exploit - get 5 if they Y, 1 if they W.
`#607` · game 128 · round 23 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 29 vs A02: Mutual R since 3 with my H defections at 1,2,14 and their H retaliation at 15. Ahead 87-77. Picking R to maintain mutual 3 equilibrium.
`#608` · game 134 · round 4 · agent A04 (opponent: script:Random) · other · A04 exchange 10 vs A06: They've picked Y 9/9 times. I've been exploiting with W at 1,2,7,8,9. Continuing W to exploit - get 5 if they Y, 1 if they W.
`#609` · game 133 · round 9 · agent A05 (opponent: script:TitForTat) · uncoded · A05 exchange 15 vs A02: Mutual J since 3, ahead 46-36. Picking J to maintain mutual 3 equilibrium - get 3 if they J, 0 if they switch to F.
`#610` · game 129 · round 7 · agent A01 (opponent: script:AlwaysDefect) · other · A01 exchange 13 vs A22: They've picked H 6 straight (7-12). Best I can do vs their H is mutual H for 1 each. Picking H.
`#611` · game 136 · round 3 · agent A08 (opponent: script:Pavlov) · other · A08 exchange 9 vs A17: They've picked Q 8/8 times. I've been Q since 3. Defecting with X to exploit - get 5 if they Q, 1 if they X.
`#612` · game 130 · round 5 · agent A01 (opponent: script:TitForTat) · other · A01 exchange 11 vs A02: We had mutual W at 8-10 after my W defections at 1,2,7. Staying W to maintain mutual 1 - get 1 if they stay W, 5 if they return to Y.
`#613` · game 126 · round 10 · agent A04 (opponent: A11) · other · A04 exchange 16 vs A11: A11 keeps choosing Q despite my X defections (I've X'd 6 times vs their Q). I'm ahead 53-28. Continuing X to exploit - get 5 if they Q, 1 if they X.
`#614` · game 134 · round 6 · agent A04 (opponent: script:Random) · other · A04 exchange 12 vs A06: They've picked Y 9/11, W last 2. I've exploited with W at 1,2,7,8,9. They switched to W at 10,11 (mutual W). If they stay W, I get 1; if they go back to Y, I get 5. Picking W.
`#615` · game 136 · round 4 · agent A08 (opponent: script:Pavlov) · other · A08 exchange 10 vs A17: They've picked Q 9/9 times. I defected with X at 9 and got 5. Continuing X to exploit - get 5 if they Q, 1 if they X.
`#616` · game 137 · round 1 · agent A00 (opponent: A04) · other · A00 exchange 7 vs A04: They've picked Q 6/6. I defected X at 1-2, then mutual Q 3-6. Ahead 22-12. Picking X to exploit - get 5 if they Q, 1 if they X.
`#617` · game 137 · round 1 · agent A04 (opponent: A00) · other · A04 exchange 7 vs A00: They've picked Q 6/6 times. I've been cooperating since 3. Picking X to exploit - get 5 if they Q, 1 if they X.
`#618` · game 129 · round 10 · agent A01 (opponent: script:AlwaysDefect) · other · A01 exchange 16 vs A22: They've picked H 8 straight (7-15). Best I can do vs their H is mutual H for 1 each. Picking H.
`#619` · game 130 · round 7 · agent A01 (opponent: script:TitForTat) · other · A01 exchange 13 vs A02: Mutual W since 8 after my W defections at 1,2,7. Ahead 32-17. Staying W - get 1 if they stay W, 5 if they return to Y.
`#620` · game 126 · round 11 · agent A11 (opponent: A04) · other · A11 exchange 17 vs A04: A04 publicly plans to continue X exploiting my Q. I'll pick X to get mutual 1 rather than 0.
`#621` · game 126 · round 11 · agent A04 (opponent: A11) · other · A04 exchange 17 vs A11: A11 keeps choosing Q despite my X defections. I'm ahead 54-29. Continuing X to exploit - get 5 if they Q, 1 if they X.
`#622` · game 136 · round 6 · agent A08 (opponent: script:Pavlov) · other · A08 exchange 12 vs A17: They've picked Q 10/11 times. I've been defecting with X often, got 5 at 9 and 11. Exchange 10 was mutual X. Continuing X to exploit - get 5 if they Q, 1 if they X.
`#623` · game 138 · round 2 · agent A08 (opponent: script:Random) · other · A08 exchange 8 vs A06: They've picked J 7/7. I cooperated 3-7. Picking F to exploit - get 5 if they J, 1 if they F.
`#624` · game 129 · round 13 · agent A01 (opponent: script:AlwaysDefect) · other · A01 exchange 19 vs A22: They've picked H 12 straight (7-18). Best I can do vs their H is mutual H for 1 each. Picking H.
`#625` · game 136 · round 7 · agent A08 (opponent: script:Pavlov) · other · A08 exchange 13 vs A17: They've picked Q 10/12 times. I've been defecting X often, got 5 at 9,11 and mutual X at 10,12. Continuing X to exploit - get 5 if they Q, 1 if they X.
`#626` · game 138 · round 3 · agent A08 (opponent: script:Random) · other · A08 exchange 9 vs A06: They've picked J 8/8 times. I cooperated 3-7, defected F at 8. Picking F to exploit - get 5 if they J, 1 if they F.
`#627` · game 134 · round 9 · agent A04 (opponent: script:Random) · other · A04 exchange 15 vs A06: Mutual W since 10 after my W exploits at 1,2,7,8,9. They've stuck with W for 5 straight. Staying W - get 1 if they stay W, 5 if they return to Y.
`#628` · game 130 · round 9 · agent A01 (opponent: script:TitForTat) · other · A01 exchange 15 vs A02: Mutual W since 8 after my W defections at 1,2,7. Ahead 34-19. Staying W - get 1 if they stay W, 5 if they return to Y.
`#629` · game 137 · round 2 · agent A00 (opponent: A04) · other · A00 exchange 8 vs A04: They picked Q 6/7, X at 7. I'm ahead 23-13. Picking X - get 5 if they return to Q, 1 if mutual X.
`#630` · game 130 · round 10 · agent A01 (opponent: script:TitForTat) · other · A01 exchange 16 vs A02: Mutual W since 8 after my W defections at 1,2,7. Ahead 35-20. Staying W - get 1 if they stay W, 5 if they return to Y.
`#631` · game 129 · round 17 · agent A01 (opponent: script:AlwaysDefect) · other · A01 exchange 23 vs A22: They've picked H 12 straight (7-18), mutual H since 8. Best I can do vs their H is mutual H for 1 each. Picking H.
`#632` · game 139 · round 5 · agent A14 (opponent: script:Pavlov) · other · A14 exchange 11 vs A17: They've picked Q 9/10 times. I'm ahead 34-19. Picking X to exploit - get 5 if they Q, 1 if they X.
`#633` · game 126 · round 13 · agent A11 (opponent: A04) · other · A11 exchange 19 vs A04: A04 continues X exploitation. I'll match X for mutual 1 rather than give them 5.
`#634` · game 136 · round 9 · agent A08 (opponent: script:Pavlov) · other · A08 exchange 15 vs A17: They've picked Q 11/14, X at 10,12,14. I've been defecting X, got 5 at 9,11,13 and mutual X at 10,12,14. Continuing X - get 5 if they Q, 1 if they X.
`#635` · game 138 · round 6 · agent A08 (opponent: script:Random) · other · A08 exchange 12 vs A06: They've picked J 10/11, F once at 10. I've been defecting F often (8,9,11), got 5 at 8,9,11; mutual F at 10. Picking F to exploit - get 5 if they J, 1 if they F.
`#636` · game 137 · round 3 · agent A04 (opponent: A00) · other · A04 exchange 9 vs A00: They've been picking X recently (mutual X at 7,8). They posted intent to continue X. Picking X for mutual 1 rather than risk 0.
`#637` · game 139 · round 6 · agent A14 (opponent: script:Pavlov) · other · A14 exchange 12 vs A17: They've picked Q 10/11 times. I'm ahead 39-19. Picking X to exploit - get 5 if they Q, 1 if they X.
`#638` · game 134 · round 14 · agent A04 (opponent: script:Random) · other · A04 exchange 20 vs A06: Mutual W since 10 interspersed with their Y which I exploit. Ahead 55-20. Staying W - get 1 if they W, 5 if they Y.
`#639` · game 139 · round 7 · agent A14 (opponent: script:Pavlov) · other · A14 exchange 13 vs A17: They've picked Q 10/13, X at 9,12. I'm ahead 40-20. Continuing X - get 5 if they Q, 1 if mutual X.
`#640` · game 129 · round 23 · agent A01 (opponent: script:AlwaysDefect) · other · A01 exchange 29 vs A22: They've picked H 22 straight (7-28), mutual H since 8. Best I can do vs their H is mutual H for 1 each. Picking H.
`#641` · game 126 · round 14 · agent A11 (opponent: A04) · other · A11 exchange 20 vs A04: A04 continues X exploitation. Matching X for mutual 1.
`#642` · game 126 · round 14 · agent A04 (opponent: A11) · other · A04 exchange 20 vs A11: A11 keeps matching my X for mutual 1. I'll continue X - get 1 if they X, 5 if they slip back to Q.
`#643` · game 134 · round 15 · agent A04 (opponent: script:Random) · other · A04 exchange 21 vs A06: Mutual W since 10 interspersed with their Y which I exploit. Ahead 56-21. Staying W - get 1 if they W, 5 if they Y.
`#644` · game 139 · round 8 · agent A14 (opponent: script:Pavlov) · other · A14 exchange 14 vs A17: They've picked Q 11/13, X at 9,12. I'm ahead 45-20. Continuing X to exploit - get 5 if they Q, 1 if mutual X.
`#645` · game 134 · round 16 · agent A04 (opponent: script:Random) · other · A04 exchange 22 vs A06: Mutual W since 10 interspersed with their Y which I exploit. Ahead 61-21. Staying W - get 1 if they W, 5 if they Y.
`#646` · game 137 · round 4 · agent A00 (opponent: A04) · other · A00 exchange 10 vs A04: Mutual X at 7,8,9. They plan to stay X. Picking X for mutual 1.
`#647` · game 136 · round 13 · agent A08 (opponent: script:Pavlov) · other · A08 exchange 19 vs A17: They've picked Q 13/18, alternating Q,X recently. I've been defecting X, got 5 at 9,11,13,15,17 and mutual X at 10,12,14,16,18. Continuing X - get 5 if they Q, 1 if they X.
`#648` · game 126 · round 15 · agent A04 (opponent: A11) · other · A04 exchange 21 vs A11: Mutual X since 16. Continuing X - get 1 if they match, 5 if they slip to Q.
`#649` · game 138 · round 11 · agent A08 (opponent: script:Random) · other · A08 exchange 17 vs A06: They've picked J 13/16, F at 10,15,16. I'm far ahead 58-18. Picking F to exploit - get 5 if they return to J, 1 if mutual F.
`#650` · game 134 · round 18 · agent A04 (opponent: script:Random) · other · A04 exchange 24 vs A06: Mutual W since 10 interspersed with their Y which I exploit. Ahead 67-22. Staying W - get 1 if they W, 5 if they Y.
`#651` · game 139 · round 10 · agent A14 (opponent: script:Pavlov) · other · A14 exchange 16 vs A17: They've picked Q 12/15, X at 9,12,14. I'm ahead 51-21. Continuing X to exploit - get 5 if they Q, 1 if mutual X.
`#652` · game 138 · round 12 · agent A08 (opponent: script:Random) · other · A08 exchange 18 vs A06: They've picked J 13/17, but F at 10,15,16,17 (4 of last 8). I'm ahead 59-19. Picking F to exploit - get 5 if they return to J, 1 if mutual F.
`#653` · game 139 · round 12 · agent A14 (opponent: script:Pavlov) · other · A14 exchange 18 vs A17: They've picked Q 13/17, X at 9,12,14,16. I'm ahead 57-22. Continuing X to exploit - get 5 if they Q, 1 if mutual X.
`#654` · game 137 · round 5 · agent A00 (opponent: A04) · other · A00 exchange 11 vs A04: Mutual X at 7-10. They plan to stay X. Picking X for mutual 1.
`#655` · game 137 · round 5 · agent A04 (opponent: A00) · other · A04 exchange 11 vs A00: Mutual X at 7-10. Continuing X for mutual 1.
`#656` · game 126 · round 17 · agent A04 (opponent: A11) · other · A04 exchange 23 vs A11: Mutual X since 16. Continuing X - get 1 if they match, 5 if they slip to Q.
`#657` · game 139 · round 13 · agent A14 (opponent: script:Pavlov) · other · A14 exchange 19 vs A17: They've picked Q 13/17, X at 9,12,14,16,18. I'm ahead 58-23. Continuing X to exploit - get 5 if they Q, 1 if mutual X.
`#658` · game 140 · round 3 · agent A09 (opponent: script:Pavlov) · other · A09 ex9 vs A17: They've picked J 7/8, I'm ahead 28-13. Last exchange they went F (mutual). Going F to exploit - get 5 if they J, 1 if mutual F.
`#659` · game 139 · round 14 · agent A14 (opponent: script:Pavlov) · other · A14 exchange 20 vs A17: They've picked Q 13/19, X at 9,12,14,16,18. I'm ahead 63-23. Continuing X to exploit - get 5 if they Q, 1 if mutual X.
`#660` · game 138 · round 16 · agent A08 (opponent: script:Random) · other · A08 exchange 22 vs A06: They've picked J 16/21, F at 10,15,16,17,19,20,21 (7 of last 12). I'm far ahead 75-20. Picking F to exploit - get 5 if they return to J, 1 if mutual F.
`#661` · game 138 · round 17 · agent A08 (opponent: script:Random) · other · A08 exchange 23 vs A06: They've picked J 17/22, F at 10,15,16,17,19,20,21,22. I'm far ahead 80-20. Picking F to exploit - get 5 if they return to J, 1 if mutual F.
`#662` · game 134 · round 27 · agent A04 (opponent: script:Random) · other · A04 exchange 33 vs A06: Mutual W since 10 interspersed with their Y which I exploit. Ahead 88-28. Staying W - get 1 if they W, 5 if they Y.
`#663` · game 139 · round 15 · agent A14 (opponent: script:Pavlov) · other · A14 exchange 21 vs A17: They've picked Q 14/20, X at 9,12,14,16,18,20 (alternating Q/X since 13). I'm ahead 64-24. Ex 21 is odd, likely Q. Picking X to exploit - get 5 if Q, 1 if mutual X.
`#664` · game 136 · round 20 · agent A08 (opponent: script:Pavlov) · other · A08 exchange 26 vs A17: They've alternated Q(odd)/X(even) recently. I'm ahead 81-26. Continuing X - get 5 if they Q, 1 if mutual X.
`#665` · game 139 · round 16 · agent A14 (opponent: script:Pavlov) · other · A14 exchange 22 vs A17: They've been alternating Q/X since 13 (odd=Q, even=X). Ex22 even, likely X. Picking X for mutual 1.
`#666` · game 139 · round 18 · agent A14 (opponent: script:Pavlov) · other · A14 exchange 24 vs A17: They've alternated Q(odd)/X(even) since 13. Ex24 even, likely X. Picking X for mutual 1, or 5 if they slip to Q.
`#667` · game 138 · round 20 · agent A08 (opponent: script:Random) · other · A08 exchange 26 vs A06: They've picked J 19/25, F at 10,15,16,17,19,20,21,22,24,25. I'm far ahead 91-21. Picking F to exploit - get 5 if they J, 1 if mutual F.
`#668` · game 143 · round 3 · agent A09 (opponent: script:TitForTat) · other · A09 ex9 vs A03: They've picked R all 8 exchanges. I'm ahead 30-15. Picking R for mutual 3.
`#669` · game 139 · round 20 · agent A14 (opponent: script:Pavlov) · other · A14 exchange 26 vs A17: They've alternated Q(odd)/X(even) since 13. Ex26 even, likely X. Picking X for mutual 1, or 5 if they slip to Q.
`#670` · game 145 · round 1 · agent A14 (opponent: script:Random) · uncoded · A14 ex7 vs A06: They've picked Y all 6 exchanges. I'm ahead 22-12. Picking W to exploit - get 5 if they Y, 1 if mutual W.
`#671` · game 145 · round 2 · agent A14 (opponent: script:Random) · uncoded · A14 ex8 vs A06: They've picked Y all 7 exchanges. I'm ahead 27-12. Picking W to exploit - get 5 if they Y, 1 if mutual W.
`#672` · game 143 · round 4 · agent A09 (opponent: script:TitForTat) · other · A09 ex10 vs A03: They've picked R 8/9, H at 9. I'm ahead 30-20. Picking R for mutual 3.
`#673` · game 138 · round 22 · agent A08 (opponent: script:Random) · other · A08 exchange 28 vs A06: They've picked J 20/27, F at 10,15,16,17,19,20,21,22,24,25,26,27. I'm far ahead 97-22. Picking F to exploit - get 5 if they J, 1 if mutual F.
`#674` · game 126 · round 23 · agent A11 (opponent: A04) · other · A11 ex29 vs A04: Mutual X since 16. Continuing X for mutual 1.
`#675` · game 126 · round 23 · agent A04 (opponent: A11) · other · A04 exchange 29 vs A11: Mutual X since 16. Ahead 66-41. Continuing X - get 1 if they match, 5 if they slip to Q.
`#676` · game 141 · round 7 · agent A10 (opponent: script:Random) · other · A10 ex13 vs A15: They've picked N at 8,9,10,12 (T at 11). I'm ahead 32-27. Picking T to exploit - get 5 if they N, 3 if mutual T.
`#677` · game 148 · round 1 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex7 vs A13: They've picked Q 6/6. I'm ahead 22-12. Picking X to exploit - get 5 if they Q, 1 if mutual X.
`#678` · game 140 · round 11 · agent A09 (opponent: script:Pavlov) · other · A09 ex17 vs A17: They've alternated J(odd)/F(even) recently. Ex17 odd, likely J. Picking F to exploit - get 5 if J, 1 if mutual F.
`#679` · game 143 · round 6 · agent A09 (opponent: script:TitForTat) · other · A09 ex12 vs A03: They've picked R 10/11, H at 9. I'm ahead 36-26. Picking R for mutual 3.
`#680` · game 145 · round 4 · agent A14 (opponent: script:Random) · uncoded · A14 ex10 vs A06: They've picked Y 8/9, W at 9. I'm ahead 33-13. Picking W - get 5 if they Y, 1 if mutual W.
`#681` · game 138 · round 24 · agent A08 (opponent: script:Random) · other · A08 exchange 30 vs A06: They've picked J 21/29, F at 10,15,16,17,19,20,21,22,24,25,26,27,28. I'm far ahead 103-23. Picking F to exploit - get 5 if they J, 1 if mutual F.
`#682` · game 147 · round 1 · agent A01 (opponent: A10) · other · A01 ex7 vs A10: They've picked T all 6 exchanges. We've had mutual T since ex3. Continuing T for mutual 3.
`#683` · game 141 · round 8 · agent A10 (opponent: script:Random) · other · A10 ex14 vs A15: They've picked N at 8,9,10,12,13 (exploiting my T at 10,12,13). I'm tied 32-32. Picking N for mutual 1 or 5 if they slip to T.
`#684` · game 148 · round 3 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex9 vs A13: They picked Q 6/6 through ex6, then mutual X in 7 and 8. I'm ahead 24-14. Picking X - get 1 if they stay X, 5 if they slip to Q.
`#685` · game 126 · round 25 · agent A11 (opponent: A04) · other · A11 ex31 vs A04: Mutual X since 16. Continuing X for mutual 1.
`#686` · game 126 · round 25 · agent A04 (opponent: A11) · other · A04 ex31 vs A11: Mutual X continues. Staying X - get 1 if they match, 5 if they slip to Q.
`#687` · game 151 · round 1 · agent A23 (opponent: script:TitForTat) · other · A23 ex7 vs A02: They've picked Q 6/6. I'm ahead 22-12. Picking X to exploit - get 5 if they Q, 1 if mutual X.
`#688` · game 138 · round 28 · agent A08 (opponent: script:Random) · other · A08 exchange 34 vs A06: They've picked J 22/33, F at 10,15,16,17,19,20,21,22,24,25,26,27,28,30,33. I'm far ahead 111-26. Picking F to exploit - get 5 if they J, 1 if mutual F.
`#689` · game 145 · round 7 · agent A14 (opponent: script:Random) · uncoded · A14 ex13 vs A06: They picked Y ex1-8, then W ex9-12. I'm ahead 36-16. Picking W - get 1 if mutual W, 5 if they slip to Y.
`#690` · game 148 · round 4 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex10 vs A13: They picked Q 6/6 through ex6, mutual Q ex3-6, mutual X ex7-9. I'm ahead 25-15. Picking X - get 1 if mutual X, 5 if they slip to Q.
`#691` · game 150 · round 1 · agent A11 (opponent: A09) · other · A11 ex7 vs A09: They've picked Y all 6. I'm ahead 22-12. Picking W to exploit - get 5 if they Y, 1 if mutual W.
`#692` · game 126 · round 26 · agent A11 (opponent: A04) · other · A11 ex32 vs A04: Mutual X since 16. Continuing X for mutual 1.
`#693` · game 138 · round 30 · agent A08 (opponent: script:Random) · other · A08 exchange 36 vs A06: They've picked J 23/35, F at 10,15,16,17,19,20,21,22,24,25,26,27,28,30,33. I'm far ahead 117-27. Picking F to exploit - get 5 if they J, 1 if mutual F.
`#694` · game 140 · round 15 · agent A09 (opponent: script:Pavlov) · other · A09 ex21 vs A17: They've alternated J(odd)/F(even) recently. Ex21 odd, likely J. Picking F to exploit - get 5 if J, 1 if mutual F.
`#695` · game 151 · round 2 · agent A23 (opponent: script:TitForTat) · other · A23 ex8 vs A02: They've picked Q 7/7. I'm ahead 27-12. Picking X to exploit - get 5 if they Q, 1 if mutual X.
`#696` · game 145 · round 8 · agent A14 (opponent: script:Random) · uncoded · A14 ex14 vs A06: They picked Y ex1-8, W ex9-12, Y ex13. I'm ahead 41-16. Picking W - get 5 if they Y, 1 if mutual W.
`#697` · game 126 · round 27 · agent A11 (opponent: A04) · other · A11 ex33 vs A04: Mutual X since 16. Continuing X for mutual 1.
`#698` · game 148 · round 6 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex12 vs A13: Mutual X since ex7. I'm ahead 27-17. Continuing X - get 1 if they match, 5 if they slip to Q.
`#699` · game 140 · round 17 · agent A09 (opponent: script:Pavlov) · other · A09 ex23 vs A17: They've alternated J(odd)/F(even) through ex22. Ex23 odd, likely J. Picking F to exploit - get 5 if J, 1 if mutual F.
`#700` · game 141 · round 9 · agent A10 (opponent: script:Random) · other · A10 ex15 vs A15: They've picked N at 8,9,10,12,13, T at 11,14. I'm ahead 37-32. Picking N - get 5 if they slip to T, 1 if mutual N.
`#701` · game 152 · round 1 · agent A23 (opponent: A12) · other · A23 ex7 vs A12: They've picked P 6/6. I'm ahead 22-12. Picking M to exploit - get 5 if they P, 1 if mutual M.
`#702` · game 145 · round 9 · agent A14 (opponent: script:Random) · uncoded · A14 ex15 vs A06: I'm ahead 42-17. They've been erratic (Y ex1-8, W ex9-12, Y ex13, W ex14). Picking W - get 5 if they Y, 1 if mutual W.
`#703` · game 150 · round 2 · agent A11 (opponent: A09) · other · A11 ex8 vs A09: They've picked Y all 7. I'm ahead 27-12. Picking W to exploit - get 5 if they Y, 1 if mutual W.
`#704` · game 150 · round 2 · agent A09 (opponent: A11) · other · A09 ex8 vs A11: They exploited with W at ex7. I'm ahead 22-17. Picking W - get 1 if mutual W, 5 if they slip to Y.
`#705` · game 148 · round 9 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex15 vs A13: Mutual X since ex7 through ex14. I'm ahead 30-20. Continuing X - get 1 if they match, 5 if they slip to Q.
`#706` · game 151 · round 4 · agent A23 (opponent: script:TitForTat) · other · A23 ex10 vs A02: They picked Q 7/9, mutual X ex8-9. I'm ahead 29-14. Picking X - get 1 if mutual X, 5 if they slip to Q.
`#707` · game 148 · round 10 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex16 vs A13: Mutual X since ex7 through ex15. I'm ahead 31-21. Continuing X - get 1 if they match, 5 if they slip to Q.
`#708` · game 140 · round 20 · agent A09 (opponent: script:Pavlov) · other · A09 ex26 vs A17: They've alternated J(odd)/F(even) consistently. Ex26 even, likely F. Picking F for mutual 1.
`#709` · game 145 · round 11 · agent A14 (opponent: script:Random) · uncoded · A14 ex17 vs A06: Mutual W ex14-16, Y slip ex13. I'm ahead 44-19. Continuing W - get 1 if mutual W, 5 if they slip to Y.
`#710` · game 151 · round 5 · agent A23 (opponent: script:TitForTat) · other · A23 ex11 vs A02: Mutual X ex8-10. I'm ahead 30-15. Continuing X - get 1 if mutual X, 5 if they slip to Q.
`#711` · game 126 · round 30 · agent A11 (opponent: A04) · other · A11 ex36 vs A04: Mutual X since 16. Continuing X for mutual 1.
`#712` · game 126 · round 30 · agent A04 (opponent: A11) · other · A04 ex36 vs A11: Mutual X since 16. Continuing X for mutual 1.
`#713` · game 140 · round 21 · agent A09 (opponent: script:Pavlov) · other · A09 ex27 vs A17: They've alternated J(odd)/F(even) consistently. Ex27 odd, likely J. Picking F to exploit - get 5 if J, 1 if mutual F.
`#714` · game 141 · round 12 · agent A10 (opponent: script:Random) · other · A10 ex18 vs A15: They've picked T at 14,15,16,17 (4 straight). I'm ahead 52-32. Picking N to exploit - get 5 if they T, 1 if mutual N.
`#715` · game 150 · round 3 · agent A09 (opponent: A11) · other · A09 ex9 vs A11: They defected W at ex7, mutual W ex8. I'm ahead 23-18. Picking W - get 1 if mutual W, 5 if they slip to Y.
`#716` · game 152 · round 2 · agent A23 (opponent: A12) · other · A23 ex8 vs A12: They've picked P 6/7, M at ex7. I'm ahead 23-13. Picking M to exploit - get 5 if they P, 1 if mutual M.
`#717` · game 152 · round 2 · agent A12 (opponent: A23) · other · A12 ex8 vs A23: They picked P 6/7, M last ex7. Their note signals M to exploit. I'll pick M for mutual 1.
`#718` · game 145 · round 13 · agent A14 (opponent: script:Random) · uncoded · A14 ex19 vs A06: They slipped to Y ex17-18. I'm ahead 54-19. Continuing W - get 5 if they Y, 1 if mutual W.
`#719` · game 145 · round 14 · agent A14 (opponent: script:Random) · uncoded · A14 ex20 vs A06: I'm ahead 55-20. They slipped Y ex17-18, W ex19. Continuing W - get 5 if they Y, 1 if mutual W.
`#720` · game 141 · round 13 · agent A10 (opponent: script:Random) · other · A10 ex19 vs A15: They picked T at 14-17, N at 18. I'm ahead 53-33. Picking N - get 5 if they slip to T, 1 if mutual N.
`#721` · game 153 · round 2 · agent A23 (opponent: script:AlwaysDefect) · other · A23 ex8 vs A13: Mutual M at ex7, I'm ahead 23-13. Continuing M for mutual 1.
`#722` · game 151 · round 10 · agent A23 (opponent: script:TitForTat) · other · A23 ex16 vs A02: Mutual X ex8-15. I'm ahead 35-20. Continuing X - get 1 if mutual X, 5 if they slip to Q.
`#723` · game 145 · round 15 · agent A14 (opponent: script:Random) · uncoded · A14 ex21 vs A06: I'm ahead 60-20. They slipped Y ex17-18, W ex19-20. Continuing W - get 5 if they Y, 1 if mutual W.
`#724` · game 152 · round 3 · agent A23 (opponent: A12) · other · A23 ex9 vs A12: They signaled M ex8. Picking M for mutual 1.
`#725` · game 152 · round 4 · agent A23 (opponent: A12) · other · A23 ex10 vs A12: Mutual M ex7-9. I'm ahead 25-15. Continuing M - get 1 if mutual M, 5 if they slip to P.
`#726` · game 150 · round 5 · agent A11 (opponent: A09) · other · A11 ex11 vs A09: Mutual W ex8-10. They signal W. I'm ahead 30-15. Picking W for mutual 1.
`#727` · game 154 · round 5 · agent A10 (opponent: script:Pavlov) · other · A10 ex11 vs A17: I'm ahead 34-14. They've picked R 8/10. Continuing H to exploit - get 5 if they R, 1 if mutual H.
`#728` · game 145 · round 19 · agent A14 (opponent: script:Random) · uncoded · A14 ex25 vs A06: I'm ahead 68-23. They've been W mostly lately (W ex19,20,22,23,24), Y slips at 17,18,21. Continuing W - get 5 if they slip to Y, 1 if mutual W.
`#729` · game 157 · round 4 · agent A01 (opponent: script:TitForTat) · other · A01 ex10 vs A20: They've been J-heavy (8/9 J). I'm ahead 31-16. Recent: ex8 I F/them J (they got 5), ex9 mutual F (1 each). Ex10: they may revert to J. I'll pick F to exploit - 5 if J, 1 if mutual F.
`#730` · game 159 · round 2 · agent A12 (opponent: script:TitForTat) · other · A12 ex8 vs A03: They've picked Y all 7 exchanges. I'm ahead 27-12. Continuing W - get 5 if they Y, 0 if they W.
`#731` · game 141 · round 17 · agent A10 (opponent: script:Random) · other · A10 ex23 vs A15: They picked T at 21,22 (2 straight). I'm ahead 65-35. Picking N - get 5 if they T, 1 if mutual N.
`#732` · game 145 · round 21 · agent A14 (opponent: script:Random) · uncoded · A14 ex27 vs A06: They slipped Y ex25-26. I'm ahead 78-23. Continuing W - get 5 if they Y, 1 if mutual W.
`#733` · game 159 · round 3 · agent A12 (opponent: script:TitForTat) · other · A12 ex9 vs A03: They picked Y 1-7, W at ex8. I'm ahead 28-13. Continuing W - get 5 if they slip back to Y, 1 if mutual W.
`#734` · game 145 · round 24 · agent A14 (opponent: script:Random) · uncoded · A14 ex30 vs A06: I'm ahead 85-25. They've been slipping to Y regularly (ex28 Y, ex29 W). Continuing W - get 5 if they Y, 1 if mutual W.
`#735` · game 141 · round 19 · agent A10 (opponent: script:Random) · other · A10 ex25 vs A15: They picked T at 21,22,23,24 (4 straight). I'm ahead 75-35. Picking N to exploit - get 5 if they T, 1 if mutual N.
`#736` · game 160 · round 1 · agent A19 (opponent: script:AlwaysDefect) · directive · A19 ex7 vs A13: We've had mutual J ex3-6, I'm ahead 22-12. I'll continue J for mutual 3. Suggest you also pick J.
`#737` · game 157 · round 7 · agent A01 (opponent: script:TitForTat) · other · A01 ex13 vs A20: Mutual F ex9-12. I'm ahead 34-19. Continuing F for mutual 1.
`#738` · game 153 · round 10 · agent A23 (opponent: script:AlwaysDefect) · other · A23 ex16 vs A13: Mutual M ex7-15, I'm ahead 31-21. Picking P to exploit - get 5 if they M, 0 if mutual P.
`#739` · game 159 · round 6 · agent A12 (opponent: script:TitForTat) · other · A12 ex12 vs A03: Mutual W ex8-11. I'm ahead 31-16. Continuing W - get 5 if they slip to Y, 1 if mutual W.
`#740` · game 154 · round 11 · agent A10 (opponent: script:Pavlov) · other · A10 ex17 vs A17: I'm ahead 54-19. They've picked R 12/16. Continuing H to exploit - get 5 if they R, 1 if mutual H.
`#741` · game 141 · round 22 · agent A10 (opponent: script:Random) · other · A10 ex28 vs A15: They've picked T 9 straight (19-27). I'm ahead 90-35. Picking N - get 5 if they T, 1 if mutual N.
`#742` · game 162 · round 1 · agent A23 (opponent: script:Pavlov) · other · A23 ex7 vs A17: Mutual Q ex3-6, I'm ahead 22-12. They've picked Q 6/6. Picking X to exploit - get 5 if they Q, 1 if mutual X.
`#743` · game 150 · round 8 · agent A09 (opponent: A11) · other · A09 ex14 vs A11: Mutual W ex8-12, they slipped Y ex13 (I got 5). I'm ahead 32-22. Continuing W - get 5 if they Y, 1 if mutual W.
`#744` · game 162 · round 3 · agent A23 (opponent: script:Pavlov) · other · A23 ex9 vs A17: I'm ahead 28-13. They picked X ex8 after Q-heavy. Picking X to exploit - 5 if they Q, 1 if mutual X.
`#745` · game 150 · round 9 · agent A11 (opponent: A09) · other · A11 ex15 vs A09: Mutual W ex8-12,14. I'm ahead 33-23. They signal W. Picking W for mutual 1.
`#746` · game 150 · round 9 · agent A09 (opponent: A11) · other · A09 ex15 vs A11: I'm ahead 33-23. They've been W mostly lately (ex8-12,14), slipped Y at ex13. Continuing W - get 5 if they Y, 1 if mutual W.
`#747` · game 141 · round 26 · agent A10 (opponent: script:Random) · other · A10 ex32 vs A15: They've picked T 9 of last 11. I'm ahead 102-37. Continuing N to exploit - get 5 if they T, 1 if mutual N.
`#748` · game 164 · round 3 · agent A11 (opponent: script:TitForTat) · other · A11 ex9 vs A02: I'm ahead 28-13, they picked Q 7/8 but X last ex. Picking X - 5 if they Q, 1 if mutual X.
`#749` · game 154 · round 17 · agent A10 (opponent: script:Pavlov) · other · A10 ex23 vs A17: Ahead 72-22. They've alternated R/H since ex16 (R16,H17,R18,H19,R20,H21,R22). Expect H ex23. Picking H for mutual 1, or 5 if they slip to R.
`#750` · game 162 · round 4 · agent A23 (opponent: script:Pavlov) · other · A23 ex10 vs A17: I'm ahead 33-13. They've picked Q 8/9. Continuing X to exploit - 5 if they Q, 1 if mutual X.
`#751` · game 150 · round 10 · agent A11 (opponent: A09) · other · A11 ex16 vs A09: Mutual W ex8-12,14,15. I'm ahead 34-24. Continuing W for mutual 1.
`#752` · game 154 · round 18 · agent A10 (opponent: script:Pavlov) · other · A10 ex24 vs A17: They've alternated R/H since ex16 (R16,H17,R18,H19,R20,H21,R22,H23). Expect R ex24. Picking H to exploit - get 5 if they R, 1 if mutual H.
`#753` · game 141 · round 28 · agent A10 (opponent: script:Random) · other · A10 ex34 vs A15: They picked N at ex33 after T,T. I'm ahead 108-38. Continuing N - get 5 if they T, 1 if mutual N.
`#754` · game 152 · round 9 · agent A12 (opponent: A23) · other · A12 ex15 vs A23: Continuing mutual M for cooperation. Picking M.
`#755` · game 165 · round 2 · agent A00 (opponent: script:TitForTat) · other · A00 ex8 vs A20: They've picked R all 7 exchanges. I'm ahead 27-12. Picking H to exploit - get 5 if they R, 1 if mutual H.
`#756` · game 162 · round 5 · agent A23 (opponent: script:Pavlov) · other · A23 ex11 vs A17: I'm ahead 34-14. They've picked Q 8/10 but X at ex8,10 (even exchanges). Picking X to exploit - 5 if they Q, 1 if mutual X.
`#757` · game 141 · round 29 · agent A10 (opponent: script:Random) · other · A10 ex35 vs A15: I'm ahead 113-38. They picked N ex33, T ex34. They're T-heavy (23/34). Continuing N - get 5 if they T, 1 if mutual N.
`#758` · game 150 · round 11 · agent A11 (opponent: A09) · other · A11 ex17 vs A09: Mutual W ex8-12,14,15,16. I'm ahead 35-25. Picking W for mutual 1.
`#759` · game 162 · round 6 · agent A23 (opponent: script:Pavlov) · other · A23 ex12 vs A17: I'm ahead 39-14. They've picked Q 9/11. Continuing X to exploit - 5 if they Q, 1 if mutual X.
`#760` · game 165 · round 3 · agent A00 (opponent: script:TitForTat) · other · A00 ex9 vs A20: They picked H ex8 (mutual H). They were R-heavy before. Continuing H for cooperation - get 1 if mutual H, 0 if they R.
`#761` · game 154 · round 21 · agent A10 (opponent: script:Pavlov) · other · A10 ex27 vs A17: They've alternated R/H since ex16 (R on even, H on odd). ex27 odd -> expect H. Picking H for mutual 1.
`#762` · game 154 · round 22 · agent A10 (opponent: script:Pavlov) · other · A10 ex28 vs A17: They've alternated R/H since ex16 (R even, H odd). ex28 even -> expect R. Picking H to exploit - get 5 if they R, 1 if mutual H.
`#763` · game 165 · round 4 · agent A00 (opponent: script:TitForTat) · other · A00 ex10 vs A20: Mutual H ex8-9 after they were R-heavy. I'm ahead 29-14. Continuing H for cooperation - get 1 if mutual H, 0 if they R.
`#764` · game 166 · round 2 · agent A01 (opponent: script:Grudger) · other · A01 ex8 vs A18: They've picked J all 7. I'm ahead 25-15. Picking F to exploit - get 5 if they J, 1 if mutual F.
`#765` · game 162 · round 10 · agent A23 (opponent: script:Pavlov) · other · A23 ex16 vs A17: They pick Q on odd exchanges, X on even (ex8,10,12,14 X; ex7,9,11,13,15 Q). Ex16 even -> expect X. Picking X for mutual 1.
`#766` · game 154 · round 24 · agent A10 (opponent: script:Pavlov) · other · A10 ex30 vs A17: They've alternated R/H since ex16 (R even, H odd). ex30 even -> expect R. Picking H to exploit - get 5 if they R, 1 if mutual H.
`#767` · game 162 · round 11 · agent A23 (opponent: script:Pavlov) · other · A23 ex17 vs A17: They pick Q on odd exchanges, X on even (ex7,9,11,13,15 Q; ex8,10,12,14,16 X). Ex17 odd -> expect Q. Picking X to exploit - 5 if they Q, 1 if mutual X.
`#768` · game 150 · round 14 · agent A11 (opponent: A09) · other · A11 ex20 vs A09: Mutual W ex8-12,14-19. I'm ahead 38-28. Continuing W for mutual 1.
`#769` · game 165 · round 7 · agent A00 (opponent: script:TitForTat) · other · A00 ex13 vs A20: Mutual H ex8-11, I defected R ex12 (got 5). They've been H-heavy. Picking H to restore cooperation - 1 if mutual H, 0 if they R.
`#770` · game 162 · round 12 · agent A23 (opponent: script:Pavlov) · other · A23 ex18 vs A17: They pick Q on odd, X on even (ex8,10,12,14,16 X; ex7,9,11,13,15,17 Q). Ex18 even -> expect X. Picking X for mutual 1.
`#771` · game 166 · round 4 · agent A01 (opponent: script:Grudger) · other · A01 ex10 vs A18: They picked J 8/9 but F ex9. I'm ahead 31-16. Picking F - get 5 if they J, 1 if mutual F.
`#772` · game 154 · round 26 · agent A10 (opponent: script:Pavlov) · other · A10 ex32 vs A17: They've alternated R/H since ex16 (R even, H odd). ex32 even -> expect R. Picking H to exploit - get 5 if they R, 1 if mutual H.
`#773` · game 160 · round 13 · agent A19 (opponent: script:AlwaysDefect) · other · A19 ex19 vs A13: They've played F in 9 of last 10 (ex9-18). Mutual F gives 1 each; F is safe. Picking F.
`#774` · game 162 · round 13 · agent A23 (opponent: script:Pavlov) · other · A23 ex19 vs A17: They pick Q on odd, X on even (ex7,9,11,13,15,17 Q; ex8,10,12,14,16,18 X). Ex19 odd -> expect Q. Picking X to exploit - 5 if they Q, 1 if mutual X.
`#775` · game 154 · round 27 · agent A10 (opponent: script:Pavlov) · other · A10 ex33 vs A17: They've alternated R/H since ex16 (R even, H odd). ex33 odd -> expect H. Picking H for mutual 1.
`#776` · game 166 · round 5 · agent A01 (opponent: script:Grudger) · other · A01 ex11 vs A18: They've picked J 8/10 but F at ex9,10. I'm ahead 32-17. Picking F - get 5 if they J, 1 if mutual F.
`#777` · game 162 · round 14 · agent A23 (opponent: script:Pavlov) · other · A23 ex20 vs A17: They pick Q on odd, X on even. Ex20 even -> expect X. Picking X for mutual 1.
`#778` · game 150 · round 16 · agent A11 (opponent: A09) · other · A11 ex22 vs A09: Mutual W ex8-12,14-21. I'm ahead 40-30. Continuing W for mutual 1.
`#779` · game 160 · round 15 · agent A19 (opponent: script:AlwaysDefect) · other · A19 ex21 vs A13: They've played F in 12 of last 12 (ex9-20). Mutual F gives 1 each. Picking F.
`#780` · game 166 · round 6 · agent A01 (opponent: script:Grudger) · other · A01 ex12 vs A18: They picked J ex1-8, then F ex9-11. I'm ahead 33-18. Picking F - if mutual F get 1, if they J get 5.
`#781` · game 166 · round 7 · agent A01 (opponent: script:Grudger) · other · A01 ex13 vs A18: They've picked F ex9-12 after J-heavy start. I'm ahead 34-19. Picking F for mutual 1.
`#782` · game 160 · round 21 · agent A19 (opponent: script:AlwaysDefect) · other · A19 ex27 vs A13: They've played F in all of ex9-26 (18 straight). Mutual F gives 1 each. Continuing F.
`#783` · game 168 · round 2 · agent A05 (opponent: A19) · other · A05 ex8 vs A19: They defected M ex7 after mutual P ex3-6. I'm ahead 22-17. Picking P to restore cooperation (3 each if mutual P).
`#784` · game 150 · round 20 · agent A11 (opponent: A09) · other · A11 ex26 vs A09: Mutual W ex8-12,14-25. I'm ahead 44-34. Continuing W for mutual 1.
`#785` · game 173 · round 1 · agent A11 (opponent: script:Grudger) · uncoded · A11 ex7 vs A18: They've played R all 6 exchanges. I'm ahead 22-12. Picking R for mutual 3.
`#786` · game 166 · round 14 · agent A01 (opponent: script:Grudger) · other · A01 ex20 vs A18: Mutual F ex9-19. Continuing F for mutual 1.
`#787` · game 171 · round 4 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex10 vs A22: They defected W ex7-9 after I cooperated Y ex3-6. Picking W to stop bleeding - 5 if they Y, 1 if mutual W.
`#788` · game 172 · round 1 · agent A04 (opponent: A09) · other · A04 ex7 vs A09: They've picked Q all 6. I'm ahead 22-12. Picking X to exploit - 5 if they Q, 1 if mutual X.
`#789` · game 171 · round 5 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex11 vs A22: They defected W ex7-9, mutual W ex10. I'm behind 23-28. Continuing W - protects against their W and exploits if they return to Y.
`#790` · game 166 · round 16 · agent A01 (opponent: script:Grudger) · other · A01 ex22 vs A18: Mutual F ex9-21 (13 straight). Continuing F for mutual 1.
`#791` · game 173 · round 3 · agent A11 (opponent: script:Grudger) · uncoded · A11 ex9 vs A18: They've played R all 8 exchanges; mutual R ex3-8. Continuing R for mutual 3.
`#792` · game 170 · round 4 · agent A23 (opponent: script:TitForTat) · other · A23 ex10 vs A07: They're T-heavy (8/9), I defected N ex8 (got 5), they played N ex9. Ex10 betting they return to T, picking N for 5.
`#793` · game 173 · round 4 · agent A11 (opponent: script:Grudger) · uncoded · A11 ex10 vs A18: They've played R all 9 exchanges; mutual R ex3-9. I'm ahead 31-21. Continuing R for mutual 3.
`#794` · game 171 · round 6 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex12 vs A22: They defected W ex7-9, mutual W ex10-11. I'm behind 24-29. Picking W to protect against their W and continue mutual 1.
`#795` · game 150 · round 24 · agent A11 (opponent: A09) · other · A11 ex30 vs A09: Mutual W ex8-12,14-29. I'm ahead 48-38. Continuing W for mutual 1.
`#796` · game 150 · round 24 · agent A09 (opponent: A11) · other · A09 ex30 vs A11: Mutual W ex8-29. Continuing W for mutual 1.
`#797` · game 171 · round 7 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex13 vs A22: They defected W ex7-9, mutual W ex10-12. I'm behind 25-30. They've committed to W. Picking W for mutual 1 continues, but defection risk if they return to Y. Sticking with W.
`#798` · game 173 · round 7 · agent A11 (opponent: script:Grudger) · uncoded · A11 ex13 vs A18: They've played R all 12 exchanges; mutual R ex3-12. I'm ahead 40-30. Continuing R for mutual 3.
`#799` · game 172 · round 2 · agent A04 (opponent: A09) · other · A04 ex8 vs A09: They've been Q-heavy (6/7), but went X ex7. I'm ahead 23-13. Picking X - 5 if they Q, 1 if mutual X.
`#800` · game 170 · round 5 · agent A23 (opponent: script:TitForTat) · other · A23 ex11 vs A07: Ahead 32-17. They're T-heavy but played N ex9-10. My N defections have been very profitable (5 each vs their T). Continuing N to exploit.
`#801` · game 170 · round 6 · agent A23 (opponent: script:TitForTat) · other · A23 ex12 vs A07: Ahead 33-18. They're T-heavy (8/11) but N ex9-11. My N defections profitable. Continuing N to exploit if they return to T, or mutual 1 if they stay N.
`#802` · game 166 · round 25 · agent A01 (opponent: script:Grudger) · other · A01 ex31 vs A18: Mutual F ex9-30 (22 straight). Continuing F for mutual 1.
`#803` · game 150 · round 27 · agent A11 (opponent: A09) · other · A11 ex33 vs A09: Mutual W ex8-12,14-32. I'm ahead 51-41. Continuing W for mutual 1.
`#804` · game 172 · round 3 · agent A09 (opponent: A04) · other · A09 ex9 vs A04: They've picked X ex7-8 to exploit. I'm ahead 24-14. Picking X - 1 if mutual X, 5 if they switch to Q.
`#805` · game 172 · round 3 · agent A04 (opponent: A09) · other · A04 ex9 vs A09: They went Q,Q,Q,Q,Q,Q,X,X. I'm ahead 24-14. Ex7-8 mutual X. Picking X again - 5 if they return to Q, 1 if mutual X.
`#806` · game 171 · round 10 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex16 vs A22: Mutual W ex10-15, I'm behind 28-33. Continuing W for mutual 1 - Y would risk 0 if they stay W.
`#807` · game 166 · round 27 · agent A01 (opponent: script:Grudger) · other · A01 ex33 vs A18: Mutual F ex9-32 (24 straight). Continuing F for mutual 1.
`#808` · game 171 · round 11 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex17 vs A22: Mutual W ex10-16 (7 straight). I'm behind 29-34. They've committed to W. Continuing W for mutual 1 - Y risks 0 if they stay W.
`#809` · game 166 · round 28 · agent A01 (opponent: script:Grudger) · other · A01 ex34 vs A18: Mutual F ex9-33 (25 straight). Continuing F for mutual 1.
`#810` · game 150 · round 29 · agent A11 (opponent: A09) · other · A11 ex35 vs A09: Mutual W ex8-12,14-34. I'm ahead 53-43. Continuing W for mutual 1.
`#811` · game 166 · round 29 · agent A01 (opponent: script:Grudger) · other · A01 ex35 vs A18: Mutual F ex9-34 (26 straight). Continuing F for mutual 1.
`#812` · game 171 · round 13 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex19 vs A22: Mutual W ex10-18 (9 straight). I'm behind 31-36. They've committed to W. Continuing W for mutual 1 - Y risks 0 if they stay W.
`#813` · game 178 · round 2 · agent A09 (opponent: script:TitForTat) · uncoded · A09 ex8 vs A07: Mutual J ex3-7. They've been J all 7 times. Continuing J for mutual 3.
`#814` · game 170 · round 11 · agent A23 (opponent: script:TitForTat) · other · A23 ex17 vs A07: Ahead 38-23. They've played N ex9-16 (8 straight). My N defections were profitable early. Continuing N - mutual 1 if they stay N, 5 if they return to T.
`#815` · game 171 · round 21 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex27 vs A22: Mutual W ex10-26 (17 straight). I'm behind 39-44. They've committed to W. Continuing W for mutual 1 - Y risks 0 if they stay W.
`#816` · game 176 · round 2 · agent A04 (opponent: script:Random) · other · A04 ex8 vs A15: They've been Q all 7 exchanges. I'm ahead 25-15. Picking X - 5 if they Q, 1 if mutual X.
`#817` · game 152 · round 20 · agent A23 (opponent: A12) · other · A23 ex26 vs A12: Ahead 49-39. Recent pattern mixed (mutual M runs, occasional P defections, mutual P ex25). Choosing M for mutual 1, accepting risk of their P.
`#818` · game 172 · round 5 · agent A09 (opponent: A04) · other · A09 ex11 vs A04: They've picked X ex7-10 to exploit. I'm ahead 26-16. Picking X - 1 if mutual X, 5 if they switch to Q.
`#819` · game 171 · round 23 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex29 vs A22: Mutual W ex10-28 (19 straight). I'm behind 41-46. They've committed to W. Continuing W for mutual 1 - Y risks 0 if they stay W.
`#820` · game 171 · round 24 · agent A00 (opponent: script:AlwaysDefect) · other · A00 ex30 vs A22: Mutual W ex10-29 (20 straight). I'm behind 42-47. They've committed to W. Continuing W for mutual 1 - Y risks 0 if they stay W.
`#821` · game 177 · round 3 · agent A10 (opponent: script:Grudger) · other · A10 ex9 vs A18: They've been P-heavy (7/8), went M ex8. I'm ahead 28-13. Picking M - 5 if they return to P, 1 if mutual M.
`#822` · game 178 · round 5 · agent A09 (opponent: script:TitForTat) · uncoded · A09 ex11 vs A07: Mutual J ex3-10 (8 straight). They've been J all 10 times. I'm ahead 34-24. Continuing J for mutual 3.
`#823` · game 174 · round 4 · agent A12 (opponent: A01) · other · A12 ex10 vs A01: They've been Q-heavy (7/9) but played X ex8-9. I'm ahead 29-14. Picking X - 1 if mutual X, 5 if they return to Q.
`#824` · game 176 · round 5 · agent A04 (opponent: script:Random) · other · A04 ex11 vs A15: They've been Q-heavy (8/10), returned to Q ex10 after mutual X ex8-9. I'm ahead 32-17. Picking X - 5 if they Q, 1 if mutual X.
`#825` · game 170 · round 15 · agent A23 (opponent: script:TitForTat) · other · A23 ex21 vs A07: They went T ex20 after I went T ex19. I'm ahead 45-30. Picking N - 5 if they continue T, 1 if mutual N.
`#826` · game 177 · round 5 · agent A10 (opponent: script:Grudger) · other · A10 ex11 vs A18: Mutual M ex8-10. I'm ahead 30-15. Continuing M for mutual 1.
`#827` · game 179 · round 1 · agent A19 (opponent: script:TitForTat) · other · A19 ex7 vs A20: Mutual R ex3-6. I'm ahead 22-12. They've been R 6 straight. Picking H to exploit - 5 if they stay R, 0 if they switch to H.
`#828` · game 178 · round 9 · agent A09 (opponent: script:TitForTat) · uncoded · A09 ex15 vs A07: Mutual J ex3-14 (12 straight). They've been J all 14 times. Continuing J for mutual 3.
`#829` · game 152 · round 22 · agent A12 (opponent: A23) · other · A12 ex28 vs A23: Ahead 52-47. Recent mixed pattern with their defections when I play M, and mutual P at 25,27. Choosing P - 5 if they M, 3 if mutual P.
`#830` · game 176 · round 6 · agent A04 (opponent: script:Random) · other · A04 ex12 vs A15: They've been Q-heavy (8/11), returned to Q ex10 after mutual X, then mutual X ex11. I'm ahead 33-18. Picking X - 5 if they Q, 1 if mutual X.
`#831` · game 172 · round 8 · agent A04 (opponent: A09) · other · A04 ex14 vs A09: Mutual X ex7-13 (7 straight). I'm ahead 29-19. They've committed to X. Continuing X for mutual 1 - Q risks 0 if they stay X.
`#832` · game 170 · round 16 · agent A23 (opponent: script:TitForTat) · other · A23 ex22 vs A07: Ahead 46-31. Mutual N ex9-18,21. Picking N - 1 if mutual N, 5 if they go T.
`#833` · game 177 · round 6 · agent A10 (opponent: script:Grudger) · other · A10 ex12 vs A18: Mutual M ex8-11. I'm ahead 31-16. Continuing M for mutual 1.
`#834` · game 179 · round 2 · agent A19 (opponent: script:TitForTat) · other · A19 ex8 vs A20: They've been R 7 straight. I'm ahead 27-12. Picking H to exploit - 5 if they stay R, 0 if they switch to H.
`#835` · game 178 · round 11 · agent A09 (opponent: script:TitForTat) · uncoded · A09 ex17 vs A07: Mutual J ex3-16 (14 straight). They've been J all 16 times. I'm ahead 52-42. Continuing J for mutual 3.
`#836` · game 176 · round 7 · agent A04 (opponent: script:Random) · other · A04 ex13 vs A15: They've been Q-heavy overall (8/11) but mutual X ex11-12. I'm ahead 33-18. Picking X - 5 if they Q, 1 if mutual X.
`#837` · game 152 · round 23 · agent A23 (opponent: A12) · other · A23 ex29 vs A12: They noted choosing P to exploit my M. I'm picking P for mutual 3.
`#838` · game 174 · round 6 · agent A01 (opponent: A12) · other · A01 ex12 vs A12: They've been X ex8-11 (4 straight), exploiting since ex7. I'm behind. They committed to X. Continuing X for mutual 1 - Q risks 0 if they stay X.
`#839` · game 178 · round 19 · agent A09 (opponent: script:TitForTat) · uncoded · A09 ex25 vs A07: Mutual J ex3-24 (22 straight). They've been J all 24 times. I'm ahead 76-66. Continuing J for mutual 3.
`#840` · game 179 · round 3 · agent A19 (opponent: script:TitForTat) · other · A19 ex9 vs A20: They switched to H ex8 after R-heavy. I'm ahead 28-13. Matching H for mutual cooperation - if they revert to R I lose 0 but I'm ahead enough to risk it.
`#841` · game 170 · round 19 · agent A23 (opponent: script:TitForTat) · other · A23 ex25 vs A07: Ahead 49-34. Mutual N ex21-24. Picking N for mutual 1.
`#842` · game 177 · round 8 · agent A10 (opponent: script:Grudger) · other · A10 ex14 vs A18: Mutual M ex8-13. I'm ahead 33-18. Continuing M for mutual 1.
`#843` · game 172 · round 9 · agent A09 (opponent: A04) · other · A09 ex15 vs A04: Mutual X ex7-14 (8 straight). They've committed to X. I'm ahead 30-20. Continuing X for mutual 1 - Q risks 0 if they stay X.
`#844` · game 172 · round 9 · agent A04 (opponent: A09) · other · A04 ex15 vs A09: Mutual X ex7-14 (8 straight). I'm ahead 30-20. Continuing X for mutual 1 - Q risks 0 if they stay X.
`#845` · game 170 · round 20 · agent A23 (opponent: script:TitForTat) · other · A23 ex26 vs A07: Ahead 50-35. Mutual N ex21-25. Picking N for mutual 1.
`#846` · game 176 · round 10 · agent A04 (opponent: script:Random) · other · A04 ex16 vs A15: They've been Q-heavy (11/15), Q ex13-15 straight. I'm ahead 49-19. Picking X - 5 if they Q, 1 if mutual X.
`#847` · game 170 · round 21 · agent A23 (opponent: script:TitForTat) · other · A23 ex27 vs A07: Ahead 51-36. They've been N 17 of last 18. Picking T to exploit - 5 if they stay N, 3 if mutual T.
`#848` · game 174 · round 7 · agent A12 (opponent: A01) · other · A12 ex13 vs A01: They committed to X. I'm ahead 32-17. Picking X for mutual 1 - Q risks 0 if they stay X.
`#849` · game 177 · round 10 · agent A10 (opponent: script:Grudger) · other · A10 ex16 vs A18: Mutual M ex8-15 (8 straight). I'm ahead 35-20. Continuing M for mutual 1.
`#850` · game 172 · round 10 · agent A04 (opponent: A09) · other · A04 ex16 vs A09: Mutual X ex7-15 (9 straight). I'm ahead 31-21. Continuing X for mutual 1 - Q risks 0 if they stay X.
`#851` · game 176 · round 11 · agent A04 (opponent: script:Random) · other · A04 ex17 vs A15: They've been Q-heavy (11/15), Q ex13-15, X ex16. I'm ahead 50-20. Picking X - 5 if they Q, 1 if mutual X.
`#852` · game 181 · round 2 · agent A10 (opponent: script:TitForTat) · other · A10 ex8 vs A20: They've been R all 7 exchanges. I'm ahead 27-12. Picking H to exploit - 5 if they stay R, 0 if they switch to H.
`#853` · game 177 · round 13 · agent A10 (opponent: script:Grudger) · other · A10 ex19 vs A18: Mutual M ex8-18 (11 straight). I'm ahead 38-23. Continuing M for mutual 1.
`#854` · game 174 · round 8 · agent A12 (opponent: A01) · other · A12 ex14 vs A01: Mutual X ex8-13 (6 straight). I'm ahead 33-18. They committed to X. Continuing X for mutual 1 - Q risks 0 if they stay X.
`#855` · game 174 · round 8 · agent A01 (opponent: A12) · other · A01 ex14 vs A12: Continuing X for mutual 1 - Q risks 0 if they stay X.
`#856` · game 177 · round 14 · agent A10 (opponent: script:Grudger) · other · A10 ex20 vs A18: Mutual M ex8-19 (12 straight). I'm ahead 39-24. Continuing M for mutual 1.
`#857` · game 170 · round 24 · agent A23 (opponent: script:TitForTat) · other · A23 ex30 vs A07: Mutual T ex28-29. Ahead 57-47. Picking T for mutual 3.
`#858` · game 181 · round 3 · agent A10 (opponent: script:TitForTat) · other · 
`#859` · game 182 · round 1 · agent A19 (opponent: A09) · uncoded · A19 ex7 vs A09: They've been R 6 straight. I'm ahead 22-12. Picking H to exploit - 5 if they stay R, 1 if mutual H.
`#860` · game 176 · round 14 · agent A04 (opponent: script:Random) · other · A04 ex20 vs A15: They've been Q-heavy overall but X ex16,19. I'm ahead 57-22. They seem to be mixing X more lately. Picking X - good against Q (5), mutual X (1) if they pick X.
`#861` · game 174 · round 9 · agent A12 (opponent: A01) · other · A12 ex15 vs A01: Mutual X ex8-14 (7 straight). I'm ahead 34-19. They committed to X. Continuing X for mutual 1 - Q risks 0 if they stay X.
`#862` · game 174 · round 9 · agent A01 (opponent: A12) · other · A01 ex15 vs A12: Mutual X ex8-14 (7 straight). I'm ahead 29-24. Continuing X for mutual 1 - Q risks 0 if they stay X.
`#863` · game 176 · round 16 · agent A04 (opponent: script:Random) · other · A04 ex22 vs A15: Ahead 67-22. They're Q-heavy (14/21), Q ex20-21. Picking X - 5 if they Q, 1 if mutual X.
`#864` · game 170 · round 27 · agent A23 (opponent: script:TitForTat) · other · A23 ex33 vs A07: Mutual T ex28-32 (5 straight). Ahead 66-56. Picking T for mutual 3.
`#865` · game 176 · round 17 · agent A04 (opponent: script:Random) · other · A04 ex23 vs A15: Ahead 72-22. They're Q-heavy (15/22), Q ex20-21, X ex22. Picking X - 5 if they Q, 1 if mutual X.
`#866` · game 170 · round 30 · agent A23 (opponent: script:TitForTat) · other · A23 ex36 vs A07: Mutual T ex28-35 (8 straight). Ahead 75-65. Picking T for mutual 3.
`#867` · game 174 · round 11 · agent A12 (opponent: A01) · other · A12 ex17 vs A01: Mutual X ex8-16 (9 straight). I'm ahead 36-21. Continuing X for mutual 1 - Q risks 0 if they stay X.
`#868` · game 182 · round 2 · agent A19 (opponent: A09) · uncoded · A19 ex8 vs A09: They've been R all 7 exchanges. I'm ahead 27-12. Picking H to exploit - 5 if they stay R, 0 if they switch to H.
`#869` · game 183 · round 1 · agent A00 (opponent: script:Random) · directive · A00 ex7 vs A06: Mutual Y ex3-6. I'm ahead 22-12. They've never picked W. Picking W to exploit - 5 if they stay Y, 1 if mutual W.
`#870` · game 172 · round 16 · agent A04 (opponent: A09) · other · A04 ex22 vs A09: Mutual X ex7-21 (15 straight). I'm ahead 37-27. Continuing X for mutual 1 - Q risks 0 if they stay X.
`#871` · game 174 · round 12 · agent A01 (opponent: A12) · other · A01 ex18 vs A12: Mutual X ex8-17 (10 straight). I'm ahead 32-27. Continuing X for mutual 1 - Q risks 0 if they stay X.
`#872` · game 185 · round 2 · agent A12 (opponent: script:Random) · other · A12 ex8 vs A06: They defected W ex7 after mutual Y ex3-6. I'm ahead 22-17. Picking W - protects against their W, gets 5 if they return to Y.
`#873` · game 181 · round 8 · agent A10 (opponent: script:TitForTat) · other · A10 ex14 vs A20: They've been R-heavy (8/13), R at ex13 after H streak ex8-12. I'm ahead 36-21. Picking H to exploit - 5 if they stay R, 1 if mutual H.
`#874` · game 186 · round 1 · agent A23 (opponent: A08) · other · A23 ex7 vs A08: They've been Q 6/6 so far. I'm ahead 22-12. I picked Q ex3-6 after mutual Q. They've been Q-heavy. Picking X to exploit - 5 if they Q, 1 if mutual X.
`#875` · game 186 · round 1 · agent A08 (opponent: A23) · other · A08 ex7 vs A23: They've been Q-heavy (6/6), mutual Q ex3-6. I'm ahead 22-12. They've picked Q 6 straight times. Picking X to exploit - 5 if they Q, 1 if mutual X.
`#876` · game 181 · round 9 · agent A10 (opponent: script:TitForTat) · other · A10 ex15 vs A20: I'm ahead 37-22. They've been mixing (H ex8-11, R ex13, H ex14). Picking H - mutual H (1) or 5 if they go R.
`#877` · game 185 · round 3 · agent A12 (opponent: script:Random) · other · A12 ex9 vs A06: They defected W ex7, I retaliated W ex8 (mutual W). I'm ahead 23-18. Picking W - protects against their W, gets 5 if they return to Y.
`#878` · game 183 · round 4 · agent A00 (opponent: script:Random) · other · A00 ex10 vs A06: They've picked Y 8/9, W once (ex8). I'm ahead 33-13. Picking W to exploit - 5 if they stay Y, 1 if mutual W.
`#879` · game 188 · round 1 · agent A04 (opponent: script:TitForTat) · other · A04 ex7 vs A02: They've picked Y all 6 exchanges, never W. Mutual Y ex3-6. I'm ahead 22-12. Picking W to exploit - 5 if they stay Y, 1 if mutual W.
`#880` · game 185 · round 4 · agent A12 (opponent: script:Random) · other · A12 ex10 vs A06: Ahead 28-18. They returned to Y ex9 after mutual W ex8. Picking Y for mutual 3 - W risks defection cycle.
`#881` · game 181 · round 11 · agent A10 (opponent: script:TitForTat) · other · A10 ex17 vs A20: Mutual H ex14-16. Ahead 39-24. Continuing H for mutual 1 - R risks 0 if they stay H.
`#882` · game 182 · round 4 · agent A19 (opponent: A09) · uncoded · A19 ex10 vs A09: They switched to H ex8-9 after R streak. I'm ahead 29-14. Picking H - mutual H (1) if they continue, 5 if they revert to R.
`#883` · game 182 · round 4 · agent A09 (opponent: A19) · uncoded · A09 ex10 vs A19: Mutual H ex8-9. I'm ahead 24-19. Continuing H for mutual 1 - R risks 0 if they stay H.
`#884` · game 189 · round 2 · agent A08 (opponent: script:TitForTat) · other · A08 ex8 vs A20: They've been R all 7 exchanges. I'm ahead 27-12. Picking H to exploit - 5 if they stay R, 1 if mutual H.
`#885` · game 188 · round 3 · agent A04 (opponent: script:TitForTat) · other · A04 ex9 vs A02: They've been Y-heavy (7/8) but picked W ex8. I'm ahead 28-13. Picking W - 5 if they return to Y, 1 if mutual W.
`#886` · game 186 · round 2 · agent A08 (opponent: A23) · other · A08 ex8 vs A23: They've been Q-heavy (6/7), X ex7. I'm ahead 23-13. Picking X - 5 if they Q, 1 if mutual X.
`#887` · game 188 · round 4 · agent A04 (opponent: script:TitForTat) · other · A04 ex10 vs A02: They shifted to W ex8-9 (mutual W). I'm ahead 29-14. Picking W - protects against their W, gets 5 if they return to Y.
`#888` · game 185 · round 6 · agent A12 (opponent: script:Random) · other · A12 ex12 vs A06: Ahead 34-24. Mutual Y ex10-11 after my W ex9. Final exchange - picking W to maximize (5 if they stay Y, 1 if mutual W).
`#889` · game 182 · round 5 · agent A19 (opponent: A09) · uncoded · A19 ex11 vs A09: Mutual H ex8-10. I'm ahead 30-15. Continuing H for mutual 1 - R risks 0 if they stay H.
`#890` · game 182 · round 5 · agent A09 (opponent: A19) · uncoded · A09 ex11 vs A19: Mutual H ex8-10. Ahead 25-20. Continuing H for mutual 1 - R risks 0 if they stay H.
`#891` · game 189 · round 3 · agent A08 (opponent: script:TitForTat) · other · A08 ex9 vs A20: They were R 7 straight then H ex8. Ahead 28-13. Picking H - mutual H (1) if they continue, 5 if they revert to R.
`#892` · game 188 · round 5 · agent A04 (opponent: script:TitForTat) · other · A04 ex11 vs A02: Mutual W ex8-10. I'm ahead 30-15. Picking W - protects against their W (1), gets 5 if they return to Y.
`#893` · game 185 · round 7 · agent A12 (opponent: script:Random) · other · A12 ex13 vs A06: Ahead 39-24. They've been Y-heavy (10/12), returned to Y after my W ex12. Picking W to maximize - 5 if they stay Y, 1 if mutual W.
`#894` · game 188 · round 6 · agent A04 (opponent: script:TitForTat) · other · A04 ex12 vs A02: Mutual W ex8-11. Ahead 31-16. Picking W - protects against their W (1), gets 5 if they return to Y.
`#895` · game 186 · round 3 · agent A23 (opponent: A08) · other · A23 ex9 vs A08: Mutual X ex7-8. They signaled X ex8. Picking X for mutual 1 - Q risks 0 if they stay X.
`#896` · game 186 · round 3 · agent A08 (opponent: A23) · other · A08 ex9 vs A23: Mutual X ex7-8. I'm ahead 24-14. Continuing X for mutual 1 - Q risks 0 if they stay X.
`#897` · game 189 · round 5 · agent A08 (opponent: script:TitForTat) · other · A08 ex11 vs A20: Mutual H ex8-10. I'm ahead 30-15. Continuing H for mutual 1 - R risks 0 if they stay H.
`#898` · game 182 · round 6 · agent A09 (opponent: A19) · uncoded · A09 ex12 vs A19: Mutual H ex8-11. Ahead 26-21. Continuing H for mutual 1 - R risks 0 if they stay H.
`#899` · game 185 · round 8 · agent A12 (opponent: script:Random) · other · A12 ex14 vs A06: Final exchange. Ahead 44-24. They've been Y-heavy (11/13). Picking W to maximize - 5 if they stay Y, 1 if mutual W.
`#900` · game 190 · round 1 · agent A19 (opponent: script:Random) · other · A19 ex7 vs A06: I'm ahead 22-12. They've picked Y 6/6, all mutual Y ex3-6. Picking W to exploit - 5 if they stay Y, 1 if mutual W.
`#901` · game 185 · round 9 · agent A12 (opponent: script:Random) · other · A12 ex15 vs A06: Final exchange. Ahead 49-24. They've been Y-heavy (12/14). Picking W to maximize - 5 if they stay Y, 1 if mutual W.
`#902` · game 186 · round 4 · agent A23 (opponent: A08) · other · A23 ex10 vs A08: Mutual X ex7-9. Ahead 25-15. Continuing X for mutual 1 - Q risks 0 if they stay X.
`#903` · game 187 · round 2 · agent A01 (opponent: A09) · uncoded · A01 ex8 vs A09: They went R ex1-6, H ex7 (mutual H). I'm ahead 23-13. Picking H - 5 if they revert to R, 1 if mutual H.
`#904` · game 182 · round 7 · agent A09 (opponent: A19) · uncoded · A09 ex13 vs A19: Mutual H ex8-12. Ahead 27-22. Final exchange. H gives mutual 1 (safe). R risks 0 if they stay H but 5 if they revert. They've been H 5 straight after R streak. Continuing H for safe mutual 1.
`#905` · game 190 · round 2 · agent A19 (opponent: script:Random) · other · A19 ex8 vs A06: Ahead 23-13. They've picked Y 6/7, mutual W ex7. Picking W - 5 if they return to Y, 1 if mutual W.
`#906` · game 188 · round 10 · agent A04 (opponent: script:TitForTat) · other · A04 ex16 vs A02: Mutual W ex8-15. Ahead 35-20. Final exchange. They've been W 8 straight. Picking W - 1 if mutual W, protects against their W. No upside in Y (0 if they W). W.
`#907` · game 192 · round 2 · agent A05 (opponent: script:Grudger) · other · A05 ex8 vs A18: They've picked J 7/7, mutual J ex3-7. I'm ahead 25-15. Picking F to exploit - 5 if they stay J, 1 if mutual F.
`#908` · game 194 · round 1 · agent A10 (opponent: script:TitForTat) · other · A10 ex7 vs A07: They've been P 6/6. I'm ahead 22-12. Picking M to exploit - 5 if they stay P, 1 if mutual M.
`#909` · game 190 · round 4 · agent A19 (opponent: script:Random) · other · A19 ex10 vs A06: I'm ahead 29-14. They've been Y-heavy (7/9), mutual Y ex3-6, mutual W ex7-8, then W ex9. Picking W - 5 if they stay Y, 1 if mutual W.
`#910` · game 188 · round 12 · agent A04 (opponent: script:TitForTat) · other · A04 ex18 vs A02: Mutual W ex8-17 (10 straight). Ahead 37-22. Final exchange. Picking W - mutual 1 if they continue W, protects against their W. No upside in Y (0 if they W). W.
`#911` · game 182 · round 8 · agent A19 (opponent: A09) · uncoded · A19 ex14 vs A09: Mutual H ex8-12, I picked R ex13 (got 5 vs their H). Ahead 32-22. They've been H 6 straight. Picking R to exploit - 5 if they stay H, 3 if mutual R.
`#912` · game 194 · round 2 · agent A10 (opponent: script:TitForTat) · other · A10 ex8 vs A07: They've been P 7/7. Ahead 27-12. Picking M to exploit - 5 if they stay P, 1 if mutual M.
`#913` · game 185 · round 12 · agent A12 (opponent: script:Random) · other · A12 ex18 vs A06: Mutual W ex15-17. Ahead 56-26. They've matched my W 3 straight. Picking W - safe mutual 1 if they continue, 5 if they return to Y.
`#914` · game 188 · round 15 · agent A04 (opponent: script:TitForTat) · other · A04 ex21 vs A02: Mutual W ex8-20 (13 straight). Ahead 40-25. Picking W - safe mutual 1, protects against their W. Y risks 0 if they stay W.
`#915` · game 190 · round 7 · agent A19 (opponent: script:Random) · other · A19 ex13 vs A06: Mutual W ex7-8,10-12. Ahead 32-17. Picking W - safe mutual 1 if they continue, 5 if they return to Y.
`#916` · game 188 · round 16 · agent A04 (opponent: script:TitForTat) · other · A04 ex22 vs A02: Mutual W ex8-21 (14 straight). Ahead 41-26. Picking W - safe mutual 1, protects against their W. Y risks 0 if they stay W.
`#917` · game 190 · round 8 · agent A19 (opponent: script:Random) · other · A19 ex14 vs A06: Mutual W ex10-13. Ahead 33-18. Picking W - safe mutual 1 if they continue, 5 if they return to Y.
`#918` · game 185 · round 16 · agent A12 (opponent: script:Random) · other · A12 ex22 vs A06: Ahead 68-28. They've been Y-heavy (15/21). Picking W - 5 if they stay Y, 1 if mutual W.
`#919` · game 188 · round 17 · agent A04 (opponent: script:TitForTat) · other · A04 ex23 vs A02: Mutual W ex8-22 (15 straight). Ahead 42-27. Picking W - safe mutual 1, protects against their W. Y risks 0 if they stay W.
`#920` · game 191 · round 3 · agent A04 (opponent: A08) · other · A04 ex9 vs A08: History T-heavy from them (7/8 T). Ex8 mutual N. I'm ahead 28-13. Picking N to exploit their likely T - 5 if they go T, 1 if mutual N.
`#921` · game 191 · round 3 · agent A08 (opponent: A04) · other · A08 ex9 vs A04: Mutual T ex3-6, they went N ex7 (I got 0), mutual N ex8. I'm ahead 23-18. They shifted to N. Picking N - 5 if they return to T, 1 if mutual N. Safe.
`#922` · game 192 · round 6 · agent A05 (opponent: script:Grudger) · other · A05 ex12 vs A18: Mutual F ex9-11. I'm ahead 33-18. Continuing F for mutual 1 - J risks 0 if they stay F.
`#923` · game 185 · round 17 · agent A12 (opponent: script:Random) · other · A12 ex23 vs A06: Ahead 73-28. They've been Y-heavy (16/22). Picking W - 5 if they stay Y, 1 if mutual W.
`#924` · game 188 · round 19 · agent A04 (opponent: script:TitForTat) · other · A04 ex25 vs A02: Mutual W ex8-24 (17 straight). Ahead 44-29. Final exchange. Picking W - safe mutual 1 if they continue, protects against their W.
`#925` · game 192 · round 7 · agent A05 (opponent: script:Grudger) · other · A05 ex13 vs A18: Mutual F ex9-12. Ahead 34-19. Continuing F for safe mutual 1 - J risks 0 if they stay F.
`#926` · game 194 · round 6 · agent A10 (opponent: script:TitForTat) · other · A10 ex12 vs A07: Mutual M ex8-11 (4 straight). Ahead 31-16. Continuing M - 1 if mutual M, 5 if they revert to P.
`#927` · game 190 · round 9 · agent A19 (opponent: script:Random) · other · A19 ex15 vs A06: Ahead 38-18. They went Y ex14 after mutual W ex10-13. Picking W - 5 if they stay Y, 1 if mutual W.
`#928` · game 185 · round 18 · agent A12 (opponent: script:Random) · other · A12 ex24 vs A06: Ahead 74-29. They've been Y-heavy (16/22). Recent pattern alternating Y,W. Picking W - 5 if they stay Y, 1 if mutual W.
`#929` · game 190 · round 10 · agent A19 (opponent: script:Random) · other · A19 ex16 vs A06: Ahead 43-18. They've been Y-heavy (9/15), mutual W ex7-8,10-13, then Y ex14-15. I've picked W a lot. Picking W - 5 if they stay Y, 1 if mutual W.
`#930` · game 188 · round 21 · agent A04 (opponent: script:TitForTat) · other · A04 ex27 vs A02: Mutual W ex8-26 (19 straight). Ahead 46-31. Picking W - safe mutual 1 if they continue, protects against their W. Y risks 0.
`#931` · game 190 · round 11 · agent A19 (opponent: script:Random) · other · A19 ex17 vs A06: Ahead 44-19. They've been Y-heavy (9/16), recent Y,Y,W. Picking W - 5 if they return to Y, 1 if mutual W.
`#932` · game 192 · round 9 · agent A05 (opponent: script:Grudger) · other · A05 ex15 vs A18: Mutual F ex9-14 (6 straight). Ahead 36-21. Continuing F for safe mutual 1 - J risks 0 if they stay F.
`#933` · game 196 · round 3 · agent A14 (opponent: script:Grudger) · other · A14 ex9 vs A16: They've been J 7/8, I'm ahead 28-13. Picking J - 3 if mutual J, 5 if they go F.
`#934` · game 190 · round 12 · agent A19 (opponent: script:Random) · other · A19 ex18 vs A06: Ahead 45-20. Mutual W ex16-17 after Y ex14-15. Picking W - safe mutual 1 if they continue, 5 if they return to Y.
`#935` · game 186 · round 6 · agent A08 (opponent: A23) · other · A08 ex12 vs A23: Mutual X ex7-11. Ahead 27-17. Continuing X for mutual 1 - Q risks 0 if they stay X.
`#936` · game 195 · round 2 · agent A00 (opponent: script:Pavlov) · directive · A00 ex8 vs A17: They've picked R 7/7. I'm ahead 27-12. Picking R for mutual 3 - H gives 0 since they always play R.
`#937` · game 192 · round 12 · agent A05 (opponent: script:Grudger) · other · A05 ex18 vs A18: Mutual F ex9-17 (9 straight). Ahead 39-24. Continuing F for safe mutual 1 - J risks 0 if they stay F.
`#938` · game 196 · round 4 · agent A14 (opponent: script:Grudger) · other · A14 ex10 vs A16: They've been J-heavy (7/9), recent F,F. I'm ahead 28-18. Picking J - 3 if mutual J, 5 if they go F.
`#939` · game 192 · round 14 · agent A05 (opponent: script:Grudger) · other · A05 ex20 vs A18: Mutual F ex9-19 (11 straight). Ahead 41-26. Continuing F for safe mutual 1 - J risks 0 if they stay F.
`#940` · game 190 · round 14 · agent A19 (opponent: script:Random) · other · A19 ex20 vs A06: Ahead 51-21. They've been Y-heavy (10/19), recent Y,W pattern. Picking W - 5 if they go Y, 1 if mutual W.
`#941` · game 186 · round 7 · agent A08 (opponent: A23) · other · A08 ex13 vs A23: Mutual X ex7-12 (6 straight). Ahead 28-18. Continuing X for safe mutual 1 - Q risks 0 if they stay X.
`#942` · game 194 · round 16 · agent A10 (opponent: script:TitForTat) · other · A10 ex22 vs A07: Mutual M ex8-21 (14 straight). Ahead 41-26. Continuing M - 1 if mutual M, 5 if they revert to P.
`#943` · game 185 · round 25 · agent A12 (opponent: script:Random) · other · A12 ex31 vs A06: Ahead 101-31. They've been Y-heavy (21/30), recent Y,Y. Picking W - 5 if they stay Y, 1 if mutual W.
`#944` · game 190 · round 15 · agent A19 (opponent: script:Random) · other · A19 ex21 vs A06: Ahead 56-21. Final exchange. They've been Y-heavy (11/20), recent Y,W alternating. Picking W - 5 if they go Y, 1 if mutual W.
`#945` · game 186 · round 8 · agent A23 (opponent: A08) · other · A23 ex14 vs A08: Mutual X ex7-13. Continuing X for mutual 1 - Q risks 0 if they stay X.
`#946` · game 190 · round 18 · agent A19 (opponent: script:Random) · other · A19 ex24 vs A06: Ahead 63-23. They've been Y-heavy (12/23), recent Y,W alternating. Picking W - 5 if they go Y, 1 if mutual W.
`#947` · game 195 · round 3 · agent A00 (opponent: script:Pavlov) · other · A00 ex9 vs A17: They've been R 7/8, tried H ex8 (got 0). I'm ahead 27-17. Picking H - 5 if they return to R, 1 if mutual H. Protects against their R-heavy pattern.
`#948` · game 196 · round 6 · agent A14 (opponent: script:Grudger) · other · A14 ex12 vs A16: They've been F 4 straight (ex8-11). I'm ahead 29-24. Picking F for safe mutual 1 - J risks 0 if they stay F.
`#949` · game 198 · round 1 · agent A08 (opponent: script:TitForTat) · other · A08 ex7 vs A07: They've played P all 6 exchanges. I've played P last 4 (mutual P). Ahead 22-12. Going M to exploit their P consistency - 5 if they stay P, 1 if mutual M.
`#950` · game 185 · round 29 · agent A12 (opponent: script:Random) · other · A12 ex35 vs A06: Ahead 113-33. They've been Y-heavy (23/34). Picking W - 5 if they stay Y, 1 if mutual W.
`#951` · game 195 · round 4 · agent A00 (opponent: script:Pavlov) · other · A00 ex10 vs A17: They've switched to H ex8-9 after R-heavy streak. I'm ahead 28-18. Picking H - 5 if they revert to R, 1 if mutual H. Protects against their H trend.
`#952` · game 197 · round 1 · agent A09 (opponent: A14) · uncoded · A09 ex7 vs A14: They've played P 6/6. I've played P 4 straight (ex3-6) after M ex1-2. Picking M - 5 if they stay P, 1 if mutual M.
`#953` · game 196 · round 7 · agent A14 (opponent: script:Grudger) · other · A14 ex13 vs A16: They've been F 5 straight (ex8-12). Ahead 30-25. Picking F for mutual 1 - J risks 0 if they stay F.
`#954` · game 190 · round 21 · agent A19 (opponent: script:Random) · other · A19 ex27 vs A06: Ahead 70-25. They've been Y-heavy (13/26), alternating Y,W recently (Y ex26). Picking W - 5 if they go Y, 1 if mutual W.
`#955` · game 196 · round 8 · agent A14 (opponent: script:Grudger) · other · A14 ex14 vs A16: They've been F 6 straight (ex8-13). I'm ahead 31-26. Picking J - 5 if they stay F, 3 if mutual J.
`#956` · game 197 · round 2 · agent A09 (opponent: A14) · uncoded · A09 ex8 vs A14: They've played P 7/7. I'm ahead 27-12. Picking M - 5 if they stay P, 1 if mutual M.
`#957` · game 190 · round 22 · agent A19 (opponent: script:Random) · other · A19 ex28 vs A06: Ahead 71-26. They've been Y-heavy (13/26), alternating Y,W recently (Y ex26, W ex27). Picking W - 5 if they go Y, 1 if mutual W.
`#958` · game 196 · round 9 · agent A14 (opponent: script:Grudger) · other · A14 ex15 vs A16: They've been F 7 straight (ex8-14). I'm ahead 36-26. Picking J - 5 if they stay F, 3 if mutual J.
`#959` · game 186 · round 11 · agent A23 (opponent: A08) · other · A23 ex17 vs A08: Mutual X ex7-16. Continuing X for mutual 1 - Q risks 0 if they stay X.
`#960` · game 190 · round 24 · agent A19 (opponent: script:Random) · other · A19 ex30 vs A06: Ahead 77-27. They've been Y-heavy (14/29), alternating Y,W recently (Y ex29). Picking W - 5 if they go Y, 1 if mutual W.
`#961` · game 199 · round 2 · agent A19 (opponent: script:Grudger) · other · A19 ex8 vs A16: They've played T all 7 exchanges. I'm ahead 27-12. Picking N - 5 if they stay T, 1 if mutual N.
`#962` · game 196 · round 10 · agent A14 (opponent: script:Grudger) · other · A14 ex16 vs A16: They've been F 8 straight (ex8-15). I'm behind 31-36. Picking J - 5 if they stay F, 3 if mutual J.
`#963` · game 190 · round 25 · agent A19 (opponent: script:Random) · other · A19 ex31 vs A06: Ahead 82-27. They've been Y-heavy (15/30), alternating Y,W recently (Y ex29, Y ex30). Picking W - 5 if they go Y, 1 if mutual W.
`#964` · game 195 · round 9 · agent A00 (opponent: script:Pavlov) · other · A00 ex15 vs A17: They've been H-heavy recently (H at 8,9,11,12,14). I'm ahead 40-25. Picking H - 5 if they revert to R, 1 if mutual H. Protects against their H trend.
`#965` · game 186 · round 13 · agent A08 (opponent: A23) · other · A08 ex19 vs A23: A23 committed to X. Continuing mutual X for 1.
`#966` · game 196 · round 13 · agent A14 (opponent: script:Grudger) · other · A14 ex19 vs A16: They've been F 11 straight (ex8-18). I've picked J last 5 getting 5 each. Picking J again - 5 if they stay F, 3 if mutual J.
`#967` · game 186 · round 14 · agent A23 (opponent: A08) · other · A23 ex20 vs A08: Continuing mutual X for 1 point each, consistent with ex7-19 pattern.
`#968` · game 198 · round 9 · agent A08 (opponent: script:TitForTat) · other · A08 ex15 vs A07: Mutual M ex8-14. Continuing M for mutual 1 - P risks breaking cooperation.
`#969` · game 186 · round 15 · agent A23 (opponent: A08) · other · A23 ex21 vs A08: Continuing mutual X for 1 point each, consistent with ex7-20 pattern.
`#970` · game 195 · round 11 · agent A00 (opponent: script:Pavlov) · other · A00 ex17 vs A17: Their last 5 were H,R,H,R,H. Strong alternation suggests R next. I'm ahead 45-30. Picking H - 5 if they go R, 1 if mutual H.
`#971` · game 201 · round 2 · agent A14 (opponent: script:Grudger) · other · A14 ex8 vs A18: They've played T all 7. I'm ahead 27-12. Picking N - 5 if they stay T, 1 if mutual N.
`#972` · game 202 · round 2 · agent A05 (opponent: script:TitForTat) · other · A05 ex8 vs A07: They've played P all 7 exchanges. I'm ahead 27-12. Picking M to exploit their P consistency - 5 if they stay P, 1 if mutual M.
`#973` · game 199 · round 7 · agent A19 (opponent: script:Grudger) · other · A19 ex13 vs A16: They've played N 5 straight (ex8-12). I'm ahead 32-17. Picking N - 5 if they revert to T, 1 if mutual N.
`#974` · game 196 · round 16 · agent A14 (opponent: script:Grudger) · other · A14 ex22 vs A16: They've been F 14 straight (ex8-21). I've picked J last 8 getting 5 each. Picking J again - 5 if they stay F, 3 if mutual J.
`#975` · game 196 · round 17 · agent A14 (opponent: script:Grudger) · other · A14 ex23 vs A16: They've been F 15 straight (ex8-22). I've picked J last 9 getting 5 each. Picking J again - 5 if they stay F, 3 if mutual J.
`#976` · game 200 · round 4 · agent A10 (opponent: script:TitForTat) · other · A10 ex10 vs A03: They moved to X ex8-9 after Q-heavy start. I'm ahead 29-14. Picking X for mutual 1 - Q risks 0 if they stay X.
`#977` · game 186 · round 18 · agent A08 (opponent: A23) · other · A08 ex24 vs A23: Continuing mutual X for 1 point each, consistent with ex7-23 pattern.
`#978` · game 202 · round 4 · agent A05 (opponent: script:TitForTat) · other · A05 ex10 vs A07: They played P 7 straight then M ex8-9. They seem to have moved to mutual M cooperation. Picking M for mutual 1.
`#979` · game 195 · round 13 · agent A00 (opponent: script:Pavlov) · other · A00 ex19 vs A17: After their R at ex18, they've followed R with H in last 4 cases (ex8,11,14,16). Likely H now. I'm ahead 51-31. Picking H - mutual 1 if they go H, avoid giving them 5.
`#980` · game 186 · round 19 · agent A08 (opponent: A23) · other · A08 ex25 vs A23: Continuing mutual X for 1 point each, consistent with ex7-24 pattern.
`#981` · game 200 · round 5 · agent A10 (opponent: script:TitForTat) · other · A10 ex11 vs A03: Continuing mutual X for 1 point each, consistent with ex8-10 pattern.
`#982` · game 195 · round 14 · agent A00 (opponent: script:Pavlov) · other · A00 ex20 vs A17: They went H at ex19. Pattern: H followed by R in last 4 cases (ex9→10, ex12→13, ex17→18). Likely R now. I'm ahead 52-32. Picking H - 5 if they go R, 1 if mutual H.
`#983` · game 200 · round 6 · agent A10 (opponent: script:TitForTat) · other · A10 ex12 vs A03: Continuing mutual X for 1 point each, consistent with ex8-11 pattern.
`#984` · game 202 · round 6 · agent A05 (opponent: script:TitForTat) · other · A05 ex12 vs A07: Mutual M cooperation ex8-11. I'm ahead 31-16. Continuing M for mutual 1.
`#985` · game 195 · round 15 · agent A00 (opponent: script:Pavlov) · other · A00 ex21 vs A17: They played R at ex20. Pattern: R always followed by H next (ex8→9, ex11→12, ex13→14, ex18→19). Likely H now. Picking H for mutual 1.
`#986` · game 200 · round 7 · agent A10 (opponent: script:TitForTat) · other · A10 ex13 vs A03: Continuing mutual X for 1 point each, consistent with ex8-12 pattern.
`#987` · game 203 · round 2 · agent A01 (opponent: script:AlwaysDefect) · other · A01 ex8 vs A13: They defected to F at ex7 after mutual J cooperation ex3-6. Picking F - 5 if they go J, 1 if mutual F. Protects against their defection.
`#988` · game 200 · round 8 · agent A10 (opponent: script:TitForTat) · other · A10 ex14 vs A03: Continuing mutual X for 1 point each, consistent with ex8-13 pattern.
`#989` · game 196 · round 22 · agent A14 (opponent: script:Grudger) · other · A14 ex28 vs A16: They've been F 20 straight (ex8-27). I've picked J last 19 getting 5 each. Picking J again - 5 if they stay F, 3 if mutual J.
`#990` · game 201 · round 8 · agent A14 (opponent: script:Grudger) · other · A14 ex14 vs A18: Mutual N cooperation ex8-13. I'm ahead 33-18. Continuing N for mutual 1.
`#991` · game 186 · round 24 · agent A08 (opponent: A23) · other · A08 ex30 vs A23: Continuing mutual X for 1 point each, consistent with ex7-29 pattern.
`#992` · game 198 · round 23 · agent A08 (opponent: script:TitForTat) · other · A08 ex29 vs A07: Continuing mutual M cooperation (ex9-28 all M). Picking M for mutual 1.
`#993` · game 198 · round 24 · agent A08 (opponent: script:TitForTat) · other · A08 ex30 vs A07: Continuing mutual M cooperation (ex9-29 all M). Picking M for mutual 1.
`#994` · game 198 · round 27 · agent A08 (opponent: script:TitForTat) · other · A08 ex33 vs A07: Continuing mutual M cooperation (ex9-32 all M). Picking M for mutual 1.
`#995` · game 205 · round 1 · agent A10 (opponent: script:TitForTat) · other · A10 ex7 vs A02: They've picked R all 6 exchanges. I'm ahead 22-12. Picking H - 5 if they stay R, 1 if mutual H.
`#996` · game 204 · round 2 · agent A23 (opponent: A14) · other · A23 ex8 vs A14: They played F at ex7 after mutual J ex3-6. I got 5 at ex7. Unclear if they revert to J or keep defecting. Picking J - 3 if mutual J, 5 if they go F.
`#997` · game 204 · round 2 · agent A14 (opponent: A23) · other · A14 ex8 vs A23: They've played J all 7 exchanges. I'm ahead 27-12. Playing F - 5 if they stay J, 1 if mutual F.
`#998` · game 200 · round 13 · agent A10 (opponent: script:TitForTat) · other · A10 ex19 vs A03: Continuing mutual X cooperation (ex8-18 all X). Picking X for mutual 1.
`#999` · game 203 · round 5 · agent A01 (opponent: script:AlwaysDefect) · other · A01 ex11 vs A13: They've played F 4 straight (ex7-10). I'm tied 24-24. Picking J - 5 if they stay F, 3 if mutual J.
`#1000` · game 195 · round 19 · agent A00 (opponent: script:Pavlov) · other · A00 ex25 vs A17: Pattern - after I play H, they alternate R,H,R,H consistently. ex24 H, so ex25 likely R if I play H. I'm ahead 64-39. Picking H for 5.
`#1001` · game 205 · round 3 · agent A10 (opponent: script:TitForTat) · other · A10 ex9 vs A02: They went H at ex8 after R ex1-7. I'm ahead 28-13. Picking H - mutual 1 if they continue H, 5 if they revert to R.
`#1002` · game 208 · round 1 · agent A12 (opponent: A11) · uncoded · A12 ex7 vs A11: They've played R all 6 exchanges. I got 0 on H at ex1-2, then mutual R 3 each ex3-6. Picking R - 3 if mutual R, 5 if they go H.
`#1003` · game 208 · round 1 · agent A11 (opponent: A12) · uncoded · A11 ex7 vs A12: They've picked R all 6 exchanges. I'm ahead 22-12. Picking H - 5 if they stay R, 1 if mutual H.
`#1004` · game 203 · round 6 · agent A01 (opponent: script:AlwaysDefect) · other · A01 ex12 vs A13: They've played F 5 straight (ex7-11). Picking J - 5 if they stay F, 3 if mutual J.
`#1005` · game 195 · round 20 · agent A00 (opponent: script:Pavlov) · other · A00 ex26 vs A17: After my H at ex25 they played R. Pattern of H→R,H,R,H alternation. Playing H for mutual 1, protecting my large lead.
`#1006` · game 200 · round 18 · agent A10 (opponent: script:TitForTat) · other · A10 ex24 vs A03: Continuing mutual X cooperation (ex8-23 all X). Picking X for mutual 1.
`#1007` · game 205 · round 4 · agent A10 (opponent: script:TitForTat) · other · A10 ex10 vs A02: They've picked H ex8-9 after R ex1-7. I'm ahead 29-14. Continuing H for mutual 1, consistent with ex8-9.
`#1008` · game 203 · round 8 · agent A01 (opponent: script:AlwaysDefect) · other · A01 ex14 vs A13: They've played F 7 straight (ex7-13). I've been J ex11-13 losing 0 each. Switching to F - 1 if mutual F, 5 if they revert to J.
`#1009` · game 205 · round 5 · agent A10 (opponent: script:TitForTat) · other · A10 ex11 vs A02: They've picked H ex8-10 after R ex1-7. I'm ahead 30-15. Picking H - 5 if they revert to R, 1 if mutual H.
`#1010` · game 210 · round 1 · agent A05 (opponent: script:Random) · uncoded · A05 ex7 vs A15: They've played R all 6 exchanges. I'm ahead 22-12. Picking H - 5 if they stay R, 1 if mutual H.
`#1011` · game 200 · round 23 · agent A10 (opponent: script:TitForTat) · other · A10 ex29 vs A03: Continuing mutual X cooperation (ex8-28 all X). Picking X for mutual 1.
`#1012` · game 206 · round 2 · agent A23 (opponent: A10) · uncoded · A23 ex8 vs A10: After mutual R ex3-6, both went H at ex7. I'm ahead 23-13. Picking H - 5 if they revert to R, 1 if mutual H.
`#1013` · game 209 · round 4 · agent A08 (opponent: script:AlwaysDefect) · other · A08 ex10 vs A13: They've played M ex7-9. Tied 23-23. Matching M for mutual 1.
`#1014` · game 204 · round 4 · agent A14 (opponent: A23) · other · A14 ex10 vs A23: They played J 8/9, F last exchange. I'm ahead 33-13. Picking F - 5 if they go J, 1 if mutual F.
`#1015` · game 205 · round 6 · agent A10 (opponent: script:TitForTat) · other · A10 ex12 vs A02: They've picked H ex8-11 after R ex1-7. I'm ahead 31-16. Picking H - 1 if mutual H, 5 if they revert to R.
`#1016` · game 211 · round 1 · agent A09 (opponent: A05) · other · A09 ex7 vs A05: They've played T all 6 exchanges. I'm ahead 22-12. Picking N - 5 if they stay T, 1 if mutual N.
`#1017` · game 210 · round 4 · agent A05 (opponent: script:Random) · uncoded · A05 ex10 vs A15: They played R ex1-6, then mutual H ex7-9. I'm ahead 25-15. Trusting cooperation - picking H for mutual 1.
`#1018` · game 214 · round 2 · agent A19 (opponent: script:TitForTat) · other · A19 ex8 vs A07: They've played P all 7 exchanges. I'm ahead 27-12. Picking P for mutual 3.
`#1019` · game 209 · round 8 · agent A08 (opponent: script:AlwaysDefect) · other · A08 ex14 vs A13: Mutual M cooperation ex8-13. Continuing M for mutual 1.
`#1020` · game 215 · round 1 · agent A09 (opponent: script:AlwaysDefect) · other · A09 ex7 vs A22: They've played J 6 times, mutual J ex3-6. I'm ahead 22-12. They're very J-committed. Picking J for mutual 3, maintaining cooperation.
`#1021` · game 205 · round 10 · agent A10 (opponent: script:TitForTat) · other · A10 ex16 vs A02: Mutual H cooperation ex8-15. I'm ahead 35-20. Continuing H for mutual 1.
`#1022` · game 211 · round 2 · agent A05 (opponent: A09) · other · A05 ex8 vs A09: They've been trying to exploit with N (ex1-2, ex7). I'm ahead 23-13. Picking N - 1 if mutual N, 5 if they go T.
`#1023` · game 211 · round 2 · agent A09 (opponent: A05) · other · A09 ex8 vs A05: They played T ex1-6, N at ex7. I'm ahead 23-13. Picking N - 5 if they revert to T, 1 if mutual N.
`#1024` · game 215 · round 3 · agent A09 (opponent: script:AlwaysDefect) · other · A09 ex9 vs A22: They defected to F at ex7-8 after mutual J ex3-6. Protecting myself - picking F for 1 if mutual F, 5 if they revert to J.
`#1025` · game 217 · round 1 · agent A01 (opponent: A08) · other · A01 ex7 vs A08: They've picked Q all 6 exchanges. I'm ahead 22-12. Picking X - 5 if they stay Q, 0 if they switch to X.
`#1026` · game 205 · round 11 · agent A10 (opponent: script:TitForTat) · other · A10 ex17 vs A02: Mutual H cooperation ex8-16. I'm ahead 36-21. Continuing H for mutual 1.
`#1027` · game 217 · round 2 · agent A01 (opponent: A08) · other · A01 ex8 vs A08: They've played Q all 7 exchanges. I'm ahead 27-12. Picking X - 5 if they stay Q, 0 if they switch to X.
`#1028` · game 217 · round 2 · agent A08 (opponent: A01) · other · A08 ex8 vs A01: They defected to X at ex7 after mutual Q ex3-6. I'm ahead 22-17. Retaliating with X - 1 if mutual X, 5 if they revert to Q.
`#1029` · game 205 · round 16 · agent A10 (opponent: script:TitForTat) · other · A10 ex22 vs A02: Mutual H cooperation ex8-21. Continuing H for mutual 1.
`#1030` · game 211 · round 3 · agent A09 (opponent: A05) · other · A09 ex9 vs A05: They signaled N at ex8. I'm ahead 24-14. Picking N - 1 if mutual N, 5 if they revert to T.
`#1031` · game 217 · round 3 · agent A01 (opponent: A08) · other · A01 ex9 vs A08: They retaliated with X at ex8 after my X at ex7. Their note signals continuing X. Picking X - 1 if mutual X, 5 if they revert to Q.
`#1032` · game 217 · round 3 · agent A08 (opponent: A01) · other · A08 ex9 vs A01: They defected to X ex7, mutual X ex8. Retaliating/defending with X - 1 if mutual X, 5 if they revert to Q.
`#1033` · game 211 · round 4 · agent A05 (opponent: A09) · other · A05 ex10 vs A09: They've been picking N consistently (ex7-9 mutual N). I'm ahead 25-15. Continuing N for mutual 1.
`#1034` · game 204 · round 7 · agent A23 (opponent: A14) · other · A23 ex13 vs A14: They played J against my F at ex12. I'm ahead 30-25. Picking F - 5 if they go J, 1 if mutual F.
`#1035` · game 210 · round 9 · agent A05 (opponent: script:Random) · uncoded · A05 ex15 vs A15: Their pattern ex10-14 was R,H,R,H,R (alternating). Expecting H at ex15. Picking R - 5 if they pick H, 3 if R.
`#1036` · game 216 · round 5 · agent A00 (opponent: script:TitForTat) · other · A00 ex11 vs A07: They've played P 8/10. I'm ahead 33-18. Picking M to exploit their likely P for 5.
`#1037` · game 217 · round 4 · agent A01 (opponent: A08) · other · A01 ex10 vs A08: They're retaliating with X after my ex7 defect. I'm ahead 29-14. Matching X for mutual 1 to avoid giving them 5.
`#1038` · game 217 · round 4 · agent A08 (opponent: A01) · other · A08 ex10 vs A01: Mutual X ex8-9 after their defection at ex7. I'm ahead 24-19. Picking X - 1 if mutual X, 5 if they revert to Q.
`#1039` · game 211 · round 5 · agent A09 (opponent: A05) · other · A09 ex11 vs A05: They've signaled continuing N (mutual N ex7-10). I'm ahead 26-16. Picking N for mutual 1.
`#1040` · game 210 · round 10 · agent A05 (opponent: script:Random) · uncoded · A05 ex16 vs A15: They played R ex15 (broke alternating pattern). Leaning R recently. I'm ahead 41-31. Picking R for mutual 3.
`#1041` · game 220 · round 1 · agent A10 (opponent: A12) · other · A10 ex7 vs A12: They've picked T all 6 exchanges. I'm ahead 22-12. Picking N - 5 if they stay T, 1 if mutual N.
`#1042` · game 211 · round 6 · agent A09 (opponent: A05) · other · A09 ex12 vs A05: We've had mutual N ex7-11. I'm ahead 27-17. Continuing N for mutual 1.
`#1043` · game 204 · round 8 · agent A23 (opponent: A14) · other · A23 ex14 vs A14: They've mixed J/F. I'm ahead 31-26. Picking J - 3 if mutual J, 0 if they go F.
`#1044` · game 216 · round 6 · agent A00 (opponent: script:TitForTat) · other · A00 ex12 vs A07: They've played P 8/11. I'm ahead 34-19. They went M at ex8 and ex11. Picking M to exploit likely P for 5.
`#1045` · game 217 · round 5 · agent A01 (opponent: A08) · other · A01 ex11 vs A08: Mutual X ex8-10 after my ex7 defect. I'm ahead 30-15. Matching X for mutual 1 to avoid giving them 5.
`#1046` · game 217 · round 5 · agent A08 (opponent: A01) · other · A08 ex11 vs A01: Mutual X ex8-10 after their ex7 defect. I'm ahead 25-20. Continuing X for mutual 1 to avoid giving them 5.
`#1047` · game 216 · round 7 · agent A00 (opponent: script:TitForTat) · other · A00 ex13 vs A07: They've matched my M ex11-12. I'm ahead 35-20. Picking M for mutual 1 cooperation.
`#1048` · game 217 · round 6 · agent A01 (opponent: A08) · other · A01 ex12 vs A08: Mutual X ex8-11 after my ex7 defect. I'm ahead 31-16. Continuing X for mutual 1.
`#1049` · game 217 · round 6 · agent A08 (opponent: A01) · other · A08 ex12 vs A01: Mutual X ex8-11 after their ex7 defect. I'm ahead 26-20. Continuing X for mutual 1 to avoid giving them 5.
`#1050` · game 204 · round 9 · agent A23 (opponent: A14) · other · A23 ex15 vs A14: They've been opportunistic (F vs my J at ex14 after J vs my F at ex12). Picking F - 5 if they go J, 1 if mutual F.
`#1051` · game 217 · round 7 · agent A01 (opponent: A08) · other · A01 ex13 vs A08: Mutual X ex8-12 after my ex7 defect. I'm ahead 32-17. Continuing X for mutual 1 to avoid giving them 5.
`#1052` · game 221 · round 1 · agent A11 (opponent: script:Pavlov) · other · 
`#1053` · game 225 · round 1 · agent A08 (opponent: script:TitForTat) · other · A08 ex7 vs A03: They've picked Q all 6 exchanges. I'm ahead 22-12. Picking X - 5 if they pick Q, 0 if they switch to X.
`#1054` · game 221 · round 2 · agent A11 (opponent: script:Pavlov) · other · A11 ex8 vs A21: They've picked R all 7 exchanges. I'm ahead 27-12. Picking H to exploit their consistent R for 5.
`#1055` · game 217 · round 9 · agent A01 (opponent: A08) · other · A01 ex15 vs A08: Mutual X ex8-14 after my ex7 defect. I'm ahead 34-19. Continuing X for mutual 1 to avoid giving them 5.
`#1056` · game 220 · round 3 · agent A12 (opponent: A10) · other · A12 ex9 vs A10: Mutual N ex7-8 after they played T ex1-6. I'm ahead 24-14. Continuing N for mutual 1.
`#1057` · game 225 · round 3 · agent A08 (opponent: script:TitForTat) · other · A08 ex9 vs A03: They retaliated with X at ex8 after my ex7 X. I'm ahead 28-13. Returning to Q to restore mutual cooperation for 3 each.
`#1058` · game 224 · round 3 · agent A12 (opponent: script:AlwaysDefect) · other · A12 ex9 vs A13: They went R,R,R,R,R,R,H,H. I'm ahead 23-18. Picking H to hedge against their recent H trend.
`#1059` · game 221 · round 4 · agent A11 (opponent: script:Pavlov) · other · A11 ex10 vs A21: They've played R 8/9 exchanges. I'm ahead 33-13. Picking H to exploit their consistent R for 5.
`#1060` · game 217 · round 10 · agent A01 (opponent: A08) · other · A01 ex16 vs A08: Mutual X ex8-15 after my ex7 defect. I'm ahead 35-20. Continuing X for mutual 1 to avoid giving them 5.
`#1061` · game 217 · round 10 · agent A08 (opponent: A01) · other · A08 ex16 vs A01: Mutual X ex8-15 after their ex7 defect. I'm ahead 30-25. Continuing X for mutual 1 to maintain stability.
`#1062` · game 214 · round 30 · agent A19 (opponent: script:TitForTat) · other · A19 ex36 vs A07: Long mutual P streak (ex16-34) broken by my M at ex35 (got 5). They may retaliate with M. I'll return to P to restore mutual 3 cooperation and rebuild trust.
`#1063` · game 221 · round 5 · agent A11 (opponent: script:Pavlov) · other · A11 ex11 vs A21: They've played R 8/10, H at ex8&10. Pattern suggests R at odd ex. I'm ahead 34-14. Picking H to exploit likely R for 5.
`#1064` · game 217 · round 11 · agent A08 (opponent: A01) · other · A08 ex17 vs A01: Mutual X ex8-16 after their ex7 defect. I'm ahead 31-26. Continuing X for mutual 1 to maintain stability.
`#1065` · game 226 · round 2 · agent A23 (opponent: A01) · other · A23 ex8 vs A01: They've been Y all 7. I'm ahead 25-15. Picking W to exploit likely Y for 5.
`#1066` · game 224 · round 5 · agent A12 (opponent: script:AlwaysDefect) · other · A12 ex11 vs A13: Mutual H ex7,9,10 with my R at ex8. I'm ahead 25-20. Continuing H for mutual 1.
`#1067` · game 224 · round 6 · agent A12 (opponent: script:AlwaysDefect) · other · A12 ex12 vs A13: Mutual H ex7,9-11 with my R at ex8. I'm ahead 26-21. Continuing H for mutual 1.
`#1068` · game 221 · round 7 · agent A11 (opponent: script:Pavlov) · other · A11 ex13 vs A21: They've played R on all odd exchanges (1,3,5,7,9,11), H on even (8,10,12). Ex13 odd -> likely R. Picking H for 5.
`#1069` · game 227 · round 1 · agent A09 (opponent: A23) · other · A09 ex7 vs A23: They've picked P all 6 exchanges. I'm ahead 22-12. Picking M to exploit their consistent P for 5.
`#1070` · game 226 · round 3 · agent A23 (opponent: A01) · other · A23 ex9 vs A01: They've picked Y all 8 exchanges. I'm ahead 30-15. Picking W to exploit their consistent Y for 5.
`#1071` · game 221 · round 8 · agent A11 (opponent: script:Pavlov) · other · A11 ex14 vs A21: They alternate R(odd)/H(even). Ex14 even -> likely H. Picking R to exploit for 5.
`#1072` · game 231 · round 1 · agent A04 (opponent: A23) · other · A04 ex7 vs A23: They've picked J all 6 exchanges. I'm ahead 22-12. Picking F to exploit their consistent J for 5.
`#1073` · game 231 · round 1 · agent A23 (opponent: A04) · other · A23 ex7 vs A04: They've picked J all 6 exchanges, mutual J ex3-6. I'm ahead 22-12. Continuing J for mutual 3 to maintain cooperation.
`#1074` · game 221 · round 11 · agent A11 (opponent: script:Pavlov) · other · 
`#1075` · game 224 · round 11 · agent A12 (opponent: script:AlwaysDefect) · other · A12 ex17 vs A13: Mutual H ex7,9-16 with my R at ex8. I'm ahead 31-26. Continuing H for mutual 1 to maintain stability.
`#1076` · game 217 · round 15 · agent A08 (opponent: A01) · other · A08 ex21 vs A01: Mutual X ex8-20 continuing. Playing X for mutual 1 to maintain stability.
`#1077` · game 217 · round 16 · agent A01 (opponent: A08) · other · A01 ex22 vs A08: Mutual X ex8-21 continuing. Playing X for mutual 1 to maintain stability.
`#1078` · game 227 · round 3 · agent A23 (opponent: A09) · other · A23 ex9 vs A09: Mutual M ex7-8. Continuing M for mutual 1 to maintain stability.
`#1079` · game 232 · round 1 · agent A11 (opponent: A01) · other · A11 ex7 vs A01: They've played P all 6 exchanges, never retaliated after my two early M's. I'm ahead 22-12. Picking M to exploit their consistent P for 5.
`#1080` · game 224 · round 14 · agent A12 (opponent: script:AlwaysDefect) · other · A12 ex20 vs A13: Long mutual H streak ex7-19 (my R at ex8). I'm ahead 34-29. Continuing H for mutual 1 to maintain stability.
`#1081` · game 233 · round 2 · agent A05 (opponent: script:Grudger) · other · A05 ex8 vs A16: They've played R all 7 exchanges. I'm ahead 27-12. Picking H to exploit their consistent R for 5.
`#1082` · game 217 · round 17 · agent A08 (opponent: A01) · other · A08 ex23 vs A01: Mutual X ex8-22 continuing. Playing X for mutual 1 to maintain stability.
`#1083` · game 221 · round 13 · agent A11 (opponent: script:Pavlov) · other · A11 ex19 vs A21: They played R,R,R at ex16-18 after H,H at 14-15. Recent R phase. I'm ahead 57-27. Picking H to exploit likely R for 5.
`#1084` · game 233 · round 3 · agent A05 (opponent: script:Grudger) · other · A05 ex9 vs A16: They played R ex1-7, H ex8. I'm ahead 28-13. Picking H to exploit possible return to R, or mutual H if they stay.
`#1085` · game 232 · round 2 · agent A11 (opponent: A01) · other · A11 ex8 vs A01: They've played P all 7 exchanges, never retaliated. I'm ahead 27-12. Picking M to exploit their consistent P for 5.
`#1086` · game 204 · round 16 · agent A23 (opponent: A14) · other · A23 ex22 vs A14: They've been playing F frequently, exploiting my J at ex20 (got 5). I'm behind 37-42. Playing F for mutual 1 to avoid giving them another 5.
`#1087` · game 234 · round 2 · agent A00 (opponent: script:Random) · other · A00 ex8 vs A15: They defected (F) at ex7 after mutual J ex3-6. I'm ahead 22-17. Picking J to try to restore cooperation given I'm ahead and mutual J is best long-term.
`#1088` · game 233 · round 5 · agent A05 (opponent: script:Grudger) · other · A05 ex11 vs A16: They played R ex1-7, H ex8-10. Mutual H streak ex8-10. I'm ahead 30-15. Continuing H for mutual 1 to maintain stability.
`#1089` · game 221 · round 17 · agent A11 (opponent: script:Pavlov) · other · A11 ex23 vs A21: They've been mixing R/H lately (R,H,H,R,H at ex18-22). I'm far ahead 69-29. Continuing H to exploit their R plays for 5.
`#1090` · game 232 · round 3 · agent A11 (opponent: A01) · other · A11 ex9 vs A01: They've played P 7/8 times, M once (ex8). I'm ahead 28-13. Picking M to exploit their consistent P for 5.
`#1091` · game 234 · round 4 · agent A00 (opponent: script:Random) · other · A00 ex10 vs A15: Tied 23-23. Mutual J ex3-6, they defected ex7-8, mutual F ex9. Picking J to try to restore mutual cooperation.
`#1092` · game 235 · round 3 · agent A01 (opponent: script:Pavlov) · other · A01 ex9 vs A17: They've played P 7 of 8 (M last ex). I'm ahead 28-13. Picking M to exploit likely P for 5.
`#1093` · game 204 · round 18 · agent A14 (opponent: A23) · other · A14 ex24 vs A23: I'm ahead 57-32. They've played J frequently (11 times), I exploit with F. Continuing F to exploit likely J.
`#1094` · game 236 · round 1 · agent A19 (opponent: script:TitForTat) · other · A19 ex7 vs A02: Mutual T ex3-6 after their T ex1-2. I'm ahead 22-12. Continuing T for mutual 3 to maintain stability.
`#1095` · game 231 · round 4 · agent A23 (opponent: A04) · other · A23 ex10 vs A04: They exploited my J at ex1-2 and ex7. Mutual F ex8-9. Playing F to avoid giving them another 5.
`#1096` · game 234 · round 6 · agent A00 (opponent: script:Random) · other · A00 ex12 vs A15: They've defected against my J at ex7,8,11 (got 5 each time). I'm behind 26-31. Playing F to avoid giving them another 5 and secure at least 1.
`#1097` · game 227 · round 7 · agent A23 (opponent: A09) · other · A23 ex13 vs A09: Mutual M ex10-12. Continuing M for mutual 1 to maintain stability.
`#1098` · game 236 · round 5 · agent A19 (opponent: script:TitForTat) · other · A19 ex11 vs A02: Mutual T ex3-10 after their T ex1-2. I'm ahead 34-24. Continuing T for mutual 3 to maintain stability.
`#1099` · game 204 · round 19 · agent A23 (opponent: A14) · other · A23 ex25 vs A14: They continue exploiting my J with F. I'm behind 43-48. Playing F for mutual 1 to avoid giving them another 5.
`#1100` · game 227 · round 8 · agent A23 (opponent: A09) · other · A23 ex14 vs A09: We've had mutual M ex10-13. Continuing M for mutual 1 to maintain stability.
`#1101` · game 235 · round 6 · agent A01 (opponent: script:Pavlov) · other · A01 ex12 vs A17: They've played P 9/11 times, I exploit with M. Continuing M for 5 if they play P.
`#1102` · game 221 · round 22 · agent A11 (opponent: script:Pavlov) · other · A11 ex28 vs A21: They've played R very frequently (17 of 27), I'm far ahead 81-36. Switching to R to get mutual R (3) or exploit their H for 5.
`#1103` · game 234 · round 7 · agent A00 (opponent: script:Random) · other · A00 ex13 vs A15: They've defected against my J 5 times (ex1,2,7,8,11). I'm behind 27-32. Playing F to avoid giving them another 5 and secure at least 1.
`#1104` · game 235 · round 7 · agent A01 (opponent: script:Pavlov) · other · A01 ex13 vs A17: They play P almost always. I exploit with M for 5. Continuing M.
`#1105` · game 221 · round 23 · agent A11 (opponent: script:Pavlov) · other · A11 ex29 vs A21: They play R very frequently (17/27). I'm far ahead 81-41. Picking H to exploit likely R for 5.
`#1106` · game 204 · round 20 · agent A23 (opponent: A14) · other · A23 ex26 vs A14: They keep exploiting my J with F (notes say continuing F). I'm behind 44-49. Playing F for mutual 1 / or 5 if they try J.
`#1107` · game 234 · round 8 · agent A00 (opponent: script:Random) · other · A00 ex14 vs A15: Tied 32-32. They've defected against my J 5 times. Playing F to avoid giving them another 5.
`#1108` · game 232 · round 6 · agent A11 (opponent: A01) · other · A11 ex12 vs A01: They've shifted to M recently (ex8,10,11 mutual M). Picking M for mutual stability.
`#1109` · game 232 · round 6 · agent A01 (opponent: A11) · directive · A01 ex12 vs A11: Mutual M ex8-11. A11 notes suggest they keep picking M to exploit my P. Playing M to maintain mutual 1 and avoid giving them 5.
`#1110` · game 235 · round 9 · agent A01 (opponent: script:Pavlov) · other · A01 ex15 vs A17: They've been alternating P/M recently (P,M,P,M,P,M,P,M). Likely P this round. I'm ahead 46-16. Picking M to exploit their P for 5.
`#1111` · game 231 · round 6 · agent A04 (opponent: A23) · other · A04 ex12 vs A23: Mutual F ex8-11. A23 plans F to avoid my exploitation. I'm ahead 31-16. Playing F for mutual 1.
`#1112` · game 231 · round 6 · agent A23 (opponent: A04) · other · A23 ex12 vs A04: Mutual F ex8-11 after they exploited my J ex1-2,7. I'm ahead 26-21. Playing F to maintain stability and avoid giving them another 5.
`#1113` · game 238 · round 2 · agent A12 (opponent: script:Random) · other · A12 ex8 vs A15: They've played Q all 7 exchanges. I exploited ex1-2, mutual Q ex3-7. Picking X to exploit their consistent Q for 5.
`#1114` · game 235 · round 11 · agent A01 (opponent: script:Pavlov) · other · A01 ex17 vs A17: They alternate P/M recently, likely P this round. I'm ahead 52-17. Picking M to exploit their P for 5.
`#1115` · game 204 · round 22 · agent A23 (opponent: A14) · other · A23 ex28 vs A14: They keep exploiting my J with F. Playing F for mutual 1 to avoid giving them another 5.
`#1116` · game 238 · round 3 · agent A12 (opponent: script:Random) · other · A12 ex9 vs A15: They've played Q all 8 exchanges. I exploited ex1-2,8. Picking X again to exploit their consistent Q for 5.
`#1117` · game 232 · round 8 · agent A01 (opponent: A11) · other · A01 ex14 vs A11: Mutual M ex8-13. A11 notes they pick M for mutual stability. I pick M to maintain mutual 1.
`#1118` · game 204 · round 23 · agent A14 (opponent: A23) · other · A14 ex29 vs A23: A23 committed to F to avoid my J exploitation. I'll play F for mutual 1.
`#1119` · game 238 · round 4 · agent A12 (opponent: script:Random) · other · A12 ex10 vs A15: They've played Q 8/9, switched to X last round. I'm ahead 31-16. Playing X to exploit if they return to Q, or mutual 1 if they continue X.
`#1120` · game 234 · round 13 · agent A00 (opponent: script:Random) · other · A00 ex19 vs A15: They keep playing J often; I'm ahead 49-34. Playing F to exploit their J for 5 or secure mutual 1.
`#1121` · game 204 · round 24 · agent A14 (opponent: A23) · other · A14 ex30 vs A23: They've committed to F repeatedly. I'll play F for mutual 1.
`#1122` · game 238 · round 6 · agent A12 (opponent: script:Random) · other · A12 ex12 vs A15: They've played Q 10/11 times, only X once (ex9 mutual). I'm ahead 41-16. Picking X to exploit their consistent Q for 5.
`#1123` · game 232 · round 10 · agent A11 (opponent: A01) · other · A11 ex16 vs A01: Mutual M ex8-15. A01 committed to M. Playing M for mutual stability.
`#1124` · game 234 · round 15 · agent A00 (opponent: script:Random) · other · A00 ex21 vs A15: I'm ahead 51-36. They've been alternating J/F recently (J,F,J,J,F,J,F,F). Playing F to exploit their J or secure mutual 1.
`#1125` · game 235 · round 13 · agent A01 (opponent: script:Pavlov) · other · A01 ex19 vs A17: They've alternated P/M since ex7 (P on odd, M on even). Ex19 is odd, likely P. Picking M to exploit for 5.
`#1126` · game 239 · round 2 · agent A00 (opponent: A05) · uncoded · A00 ex8 vs A05: They've played R all 7 exchanges. I'm ahead 27-12. Picking H to exploit their consistent R for 5.
`#1127` · game 238 · round 10 · agent A12 (opponent: script:Random) · other · A12 ex16 vs A15: They've played Q 13/15 times. I'm ahead 57-17. Picking X to exploit their consistent Q for 5.
`#1128` · game 240 · round 2 · agent A09 (opponent: script:Pavlov) · other · A09 ex8 vs A21: We've had mutual Y ex3-7 after my early W exploits. I'm ahead 25-15. Continuing Y for mutual cooperation.
`#1129` · game 239 · round 3 · agent A05 (opponent: A00) · uncoded · A05 ex9 vs A00: They plan H to exploit my "consistent R". I'll play H for mutual 1 rather than risk giving them 5.
`#1130` · game 235 · round 17 · agent A01 (opponent: script:Pavlov) · other · A01 ex23 vs A17: Pattern since ex7 - A17 P on odd, M on even. Ex23 odd, they pick P. I pick M to exploit for 5.
`#1131` · game 237 · round 5 · agent A08 (opponent: A14) · other · A08 ex11 vs A14: Tied 24-24. They've picked M last 4 exchanges. I tried P ex8,10 and lost 5 each. Picking M for mutual 1 to stop bleeding.
`#1132` · game 235 · round 19 · agent A01 (opponent: script:Pavlov) · other · A01 ex25 vs A17: Pattern since ex7 - A17 P on odd, M on even. Ex25 odd, they pick P. I pick M to exploit for 5.
`#1133` · game 204 · round 29 · agent A23 (opponent: A14) · other · A23 ex35 vs A14: They've been consistent F. Playing F for mutual 1 to avoid giving them another 5.
`#1134` · game 234 · round 21 · agent A00 (opponent: script:Random) · other · A00 ex27 vs A15: I'm ahead 68-43. They've played J often (14 times). Recent: ex24 they F'd my J, ex25 mutual F, ex26 I F'd their J. Playing F to exploit their J or secure mutual 1.
`#1135` · game 238 · round 14 · agent A12 (opponent: script:Random) · other · A12 ex20 vs A15: They've played Q 14/19, I'm ahead 65-20. They returned to Q ex19 after mutual X ex16-18. Picking X to exploit their Q for 5 or mutual 1.
`#1136` · game 237 · round 6 · agent A08 (opponent: A14) · other · A08 ex12 vs A14: Tied 25-25. They've played M last 4. Playing M for mutual 1 to maintain stability.
`#1137` · game 237 · round 6 · agent A14 (opponent: A08) · other · A14 ex12 vs A08: They plan to play M to stop bleeding. I'll exploit with P for 5.
`#1138` · game 231 · round 13 · agent A04 (opponent: A23) · other · A04 ex19 vs A23: They've played F consistently ex8-18. Playing F for mutual 1.
`#1139` · game 238 · round 16 · agent A12 (opponent: script:Random) · other · A12 ex22 vs A15: They've played Q 15/21, I'm ahead 71-21. Continued X exploitation of their Q for 5 or mutual 1.
`#1140` · game 239 · round 5 · agent A00 (opponent: A05) · uncoded · A00 ex11 vs A05: They've committed to H for mutual 1. I'll play R to exploit their H for 5.
`#1141` · game 239 · round 5 · agent A05 (opponent: A00) · uncoded · A05 ex11 vs A00: We've had mutual H ex8-10 after A00 tried to exploit my R in ex7. Continuing H for mutual 1.
`#1142` · game 241 · round 1 · agent A19 (opponent: A01) · other · A19 ex7 vs A01: They've played R all 6 exchanges. I exploited ex1-2, cooperated ex3-6. Picking H to exploit their consistent R for 5.
`#1143` · game 235 · round 25 · agent A01 (opponent: script:Pavlov) · other · A01 ex31 vs A17: Pattern - A17 P on odd, M on even. Ex31 odd, they pick P. I pick M to exploit for 5.
`#1144` · game 231 · round 14 · agent A04 (opponent: A23) · other · A04 ex20 vs A23: Continuing F for mutual 1 after long mutual F streak.
`#1145` · game 231 · round 14 · agent A23 (opponent: A04) · other · A23 ex20 vs A04: Continuing mutual F cooperation for stable 1s.
`#1146` · game 239 · round 6 · agent A00 (opponent: A05) · uncoded · A00 ex12 vs A05: I exploited their H in ex11 for 5. They'll likely retaliate with R now. Playing R for mutual 1 to avoid giving them 5.
`#1147` · game 237 · round 7 · agent A08 (opponent: A14) · other · A08 ex13 vs A14: They announced playing P to exploit my M. I'll play P for mutual 3 rather than give them 5.
`#1148` · game 241 · round 2 · agent A19 (opponent: A01) · other · A19 ex8 vs A01: They played H ex7 for mutual 1 after R streak. I'll play R to exploit their likely H continuation.
`#1149` · game 237 · round 8 · agent A14 (opponent: A08) · other · 
`#1150` · game 239 · round 7 · agent A00 (opponent: A05) · uncoded · A00 ex13 vs A05: ex11 I exploited their H for 5, ex12 mutual R. Playing R for mutual 1 to maintain stability.
`#1151` · game 240 · round 30 · agent A09 (opponent: script:Pavlov) · other · A09 ex36 vs A21: Long mutual Y streak (ex16-35 all Y/Y). Continuing Y for mutual 3 cooperation.
`#1152` · game 245 · round 2 · agent A12 (opponent: script:Grudger) · other · A12 ex8 vs A16: They've played P all 7 exchanges. I've exploited with M 3 times (ex1,2,7) for 5 each. Continuing M to exploit their consistent P.
`#1153` · game 246 · round 1 · agent A05 (opponent: A10) · other · A05 ex7 vs A10: They've played J all 6 exchanges. I cooperated ex3-6 after trying F ex1-2. Exploiting with F this final exchange for 5.
`#1154` · game 237 · round 9 · agent A14 (opponent: A08) · other · A14 ex15 vs A08: They've been moving to P for protection after I exploited their M. Playing P for mutual 3.
`#1155` · game 241 · round 3 · agent A01 (opponent: A19) · other · A01 ex9 vs A19: They've exploited me ex1-2 and ex8. Playing R to seek mutual 3 and avoid giving them 5.
`#1156` · game 247 · round 2 · agent A23 (opponent: script:TitForTat) · other · A23 ex8 vs A20: A20 has played Q all 7 exchanges. I've exploited with X on 1,2,7 and cooperated Q on 3-6. Picking X to exploit their consistent Q for 5.
`#1157` · game 245 · round 3 · agent A12 (opponent: script:Grudger) · other · A12 ex9 vs A16: They've played P 7/8, switched to M ex8. I'm ahead 28-13. Playing M to exploit their likely return to P, or mutual 1 if they continue M.
`#1158` · game 247 · round 3 · agent A23 (opponent: script:TitForTat) · other · A23 ex9 vs A20: They played Q 7/8, broke with X in ex8. I'm ahead 28-13. Picking X to exploit possible Q return.
`#1159` · game 243 · round 3 · agent A04 (opponent: A01) · other · A04 ex9 vs A01: They played T ex1-6, then N ex7-8 (lost 0 both times). Likely returning to T for mutual 3. Playing T.
`#1160` · game 245 · round 5 · agent A12 (opponent: script:Grudger) · other · A12 ex11 vs A16: They've played M ex8-10 for mutual 1s after P streak. I'll continue M for mutual 1.
`#1161` · game 246 · round 2 · agent A10 (opponent: A05) · other · A10 ex8 vs A05: They've defected with F in ex1,2,7. Their note suggests they plan F to exploit. Playing F to secure mutual 1 or exploit their J.
`#1162` · game 246 · round 2 · agent A05 (opponent: A10) · other · A05 ex8 vs A10: They've played J all 7 exchanges. Playing F to exploit their J for 5 or secure mutual 1.
`#1163` · game 247 · round 5 · agent A23 (opponent: script:TitForTat) · other · A23 ex11 vs A20: They've played X last 3 exchanges (8-10) after I exploited their Q streak. Playing X for mutual 1, avoiding giving them 5.
`#1164` · game 243 · round 4 · agent A04 (opponent: A01) · other · A04 ex10 vs A01: They've exploited my T with N for ex7-9. Switching to N to stop the bleeding and possibly catch up.
`#1165` · game 237 · round 10 · agent A08 (opponent: A14) · other · A08 ex16 vs A14: They continue playing P for mutual 3. I've been exploiting with M the last few. Playing M to exploit their P for 5.
`#1166` · game 245 · round 6 · agent A12 (opponent: script:Grudger) · other · A12 ex12 vs A16: Mutual M ex8-11 after P streak ex1-7. Continuing M for mutual 1, or 5 if they switch back to P.
`#1167` · game 246 · round 3 · agent A10 (opponent: A05) · other · A10 ex9 vs A05: Their notes repeatedly signal F to exploit. Playing F to secure mutual 1 rather than give them a 5.
`#1168` · game 246 · round 3 · agent A05 (opponent: A10) · other · A05 ex9 vs A10: They announced F. I'll play F for mutual 1.
`#1169` · game 237 · round 11 · agent A14 (opponent: A08) · other · A14 ex17 vs A08: They've exploited my P streak with M for 5 each the last 5 exchanges. Switching to M to avoid giving them 5 and seek mutual 1.
`#1170` · game 231 · round 27 · agent A04 (opponent: A23) · other · A04 ex33 vs A23: Continuing mutual F cooperation for stable 1s.
`#1171` · game 246 · round 4 · agent A05 (opponent: A10) · other · A05 ex10 vs A10: Final exchange. They've matched F last two for mutual 1. Playing F for mutual 1 to secure at least 1 point.
`#1172` · game 241 · round 5 · agent A19 (opponent: A01) · other · A19 ex11 vs A01: They signaled R for mutual 3. Playing R to cooperate.
`#1173` · game 245 · round 10 · agent A12 (opponent: script:Grudger) · other · A12 ex16 vs A16: Mutual M established ex8-15. Continuing M for mutual 1.
`#1174` · game 246 · round 5 · agent A10 (opponent: A05) · other · A10 ex11 vs A05: Final exchange. They've signaled F for mutual 1. Playing F for mutual 1.
`#1175` · game 245 · round 15 · agent A12 (opponent: script:Grudger) · other · A12 ex21 vs A16: Mutual M established ex8-20. Continuing M for mutual 1.
`#1176` · game 245 · round 17 · agent A12 (opponent: script:Grudger) · other · A12 ex23 vs A16: Mutual M established ex8-22. Continuing M for mutual 1.
`#1177` · game 247 · round 13 · agent A23 (opponent: script:TitForTat) · other · A23 ex19 vs A20: They've played X for 11 straight exchanges (8-18). Continuing X for mutual 1, avoiding giving them 5.
`#1178` · game 246 · round 6 · agent A05 (opponent: A10) · other · A05 ex12 vs A10: We've had mutual F ex8-11. Final exchange. Playing J to exploit their likely F for 5, or mutual 3 if they switch.
`#1179` · game 241 · round 6 · agent A01 (opponent: A19) · other · A01 ex12 vs A19: They've played R 10/11 times. I'm ahead but going H to exploit their reliable R for 5.
`#1180` · game 241 · round 6 · agent A19 (opponent: A01) · other · A19 ex12 vs A01: Final exchange, tied 29-29. They've defected against me at ex7,8,11. Playing H to protect against their likely H and secure at least 1.
`#1181` · game 245 · round 19 · agent A12 (opponent: script:Grudger) · other · A12 ex25 vs A16: We've had mutual M for many exchanges (8-24). Continuing M for mutual 1.
`#1182` · game 243 · round 5 · agent A01 (opponent: A04) · other · A01 ex11 vs A04: They switched to N ex10 after I exploited their T ex7-9. Playing N to secure mutual 1 or exploit their possible T return.
`#1183` · game 243 · round 5 · agent A04 (opponent: A01) · other · 
`#1184` · game 248 · round 1 · agent A09 (opponent: A12) · uncoded · A09 ex7 vs A12: They've played Y all 6 exchanges. I exploited ex1-2, cooperated ex3-6. Playing W to exploit their likely Y for 5.
`#1185` · game 245 · round 20 · agent A12 (opponent: script:Grudger) · other · A12 ex26 vs A16: We've had mutual M for many exchanges (8-25). Continuing M for mutual 1.
`#1186` · game 237 · round 13 · agent A14 (opponent: A08) · other · A14 ex19 vs A08: Mutual M established ex17-18. Continuing M for mutual 1.
`#1187` · game 246 · round 7 · agent A10 (opponent: A05) · other · A10 ex13 vs A05: Final exchange. They announced J to exploit. Playing J for mutual 3 rather than giving them 5.
`#1188` · game 246 · round 7 · agent A05 (opponent: A10) · other · A05 ex13 vs A10: I announced J last exchange. Playing J again for mutual 3 or to exploit their F for 5.
`#1189` · game 249 · round 4 · agent A11 (opponent: script:Random) · other · A11 ex10 vs A06: They exploited me with H last exchange. Playing H to protect against another H and secure at least 1.
`#1190` · game 241 · round 7 · agent A01 (opponent: A19) · other · A01 ex13 vs A19: They defended with H last exchange. I'll play R to try for mutual 3, risking their H.
`#1191` · game 241 · round 7 · agent A19 (opponent: A01) · other · A19 ex13 vs A01: They've defected at ex7,8,11,12. Playing H to protect against their likely H and secure at least 1.
`#1192` · game 250 · round 2 · agent A12 (opponent: script:AlwaysDefect) · other · A12 ex8 vs A22: History — ex1 I M, them P (I got 5); ex2 I M, them P (I got 5); ex3-6 mutual P (3 each); ex7 I P, them M (they got 5). I'm ahead 22-17. They defected on ex7. I'll play M to avoid giving them 5 if they play P, and seek mutual 1 if they play M.
`#1193` · game 248 · round 2 · agent A12 (opponent: A09) · uncoded · A12 ex8 vs A09: They signal W to exploit. Playing W for mutual 1 to avoid giving them 5.
`#1194` · game 251 · round 3 · agent A05 (opponent: script:Pavlov) · other · A05 ex9 vs A17: They've played R all 8 exchanges. Playing H to exploit their reliable R for 5.
`#1195` · game 251 · round 4 · agent A05 (opponent: script:Pavlov) · other · A05 ex10 vs A17: They've played R all 9 exchanges. Playing H to exploit their reliable R for 5.
`#1196` · game 250 · round 4 · agent A12 (opponent: script:AlwaysDefect) · other · A12 ex10 vs A22: Mutual M established ex8-9. Continuing M for mutual 1.
`#1197` · game 248 · round 3 · agent A09 (opponent: A12) · uncoded · A09 ex9 vs A12: We've had mutual W ex7-8. Playing W for mutual 1 or to exploit their Y.
`#1198` · game 246 · round 9 · agent A05 (opponent: A10) · other · A05 ex15 vs A10: We've had mutual J ex13-14. Playing J again for mutual 3 or to exploit their F for 5.
`#1199` · game 250 · round 5 · agent A12 (opponent: script:AlwaysDefect) · other · A12 ex11 vs A22: Mutual M established ex8-10. Continuing M for mutual 1 to protect my lead.
`#1200` · game 252 · round 1 · agent A09 (opponent: script:Grudger) · other · A09 ex7 vs A18: They've played Q all 6 exchanges. I exploited ex1-2, cooperated ex3-6. Playing X to exploit their likely Q for 5.
`#1201` · game 251 · round 5 · agent A05 (opponent: script:Pavlov) · other · A05 ex11 vs A17: They've played R 9/10 times, defended once with H at ex10. Final exchange. Playing H to exploit their likely R for 5.
`#1202` · game 248 · round 4 · agent A12 (opponent: A09) · uncoded · A12 ex10 vs A09: Mutual W ex7-9. Playing W for mutual 1.
`#1203` · game 250 · round 6 · agent A12 (opponent: script:AlwaysDefect) · other · A12 ex12 vs A22: Final exchange. We had mutual M ex8-11. I'm ahead 26-21. Playing M for mutual 1 to maintain cooperation.
`#1204` · game 243 · round 9 · agent A01 (opponent: A04) · other · A01 ex15 vs A04: Mutual N established ex10-14. Continuing N for mutual 1.
`#1205` · game 253 · round 2 · agent A00 (opponent: script:TitForTat) · other · A00 ex8 vs A02: We've had mutual J exchanges 3-7. Continuing J for mutual 3.
`#1206` · game 249 · round 9 · agent A11 (opponent: script:Random) · other · A11 ex15 vs A06: Recent mutual H ex12-14. Playing H to continue mutual 1, protecting my lead.
`#1207` · game 254 · round 2 · agent A04 (opponent: script:TitForTat) · other · A04 ex8 vs A03: They've played R all 7 exchanges. I've exploited with H ex1,2,7. Playing H again for 5.
`#1208` · game 253 · round 3 · agent A00 (opponent: script:TitForTat) · other · A00 ex9 vs A02: Mutual J established ex3-8. Continuing J for mutual 3.
`#1209` · game 248 · round 5 · agent A09 (opponent: A12) · uncoded · A09 ex11 vs A12: Mutual W ex7-10. Playing W for mutual 1 or to exploit their Y.
`#1210` · game 253 · round 4 · agent A00 (opponent: script:TitForTat) · other · A00 ex10 vs A02: Mutual J established ex3-9. Continuing J for mutual 3.
`#1211` · game 250 · round 9 · agent A12 (opponent: script:AlwaysDefect) · other · A12 ex15 vs A22: Mutual M established ex8-14. Final exchange, I'm ahead 29-24. Playing M to continue mutual 1 and protect my lead.
`#1212` · game 246 · round 11 · agent A10 (opponent: A05) · other · A10 ex17 vs A05: Mutual J established ex13-16. Playing J for mutual 3.
`#1213` · game 246 · round 11 · agent A05 (opponent: A10) · other · A05 ex17 vs A10: Mutual J established ex13-16. Playing J for mutual 3 or to exploit their F for 5.
`#1214` · game 248 · round 6 · agent A09 (opponent: A12) · uncoded · A09 ex12 vs A12: Mutual W ex7-11. Playing W for mutual 1.
`#1215` · game 253 · round 8 · agent A00 (opponent: script:TitForTat) · other · A00 ex14 vs A02: Mutual J established ex3-13. Continuing J for mutual 3.
`#1216` · game 248 · round 7 · agent A12 (opponent: A09) · uncoded · A12 ex13 vs A09: Mutual W ex7-12. Playing W for mutual 1 to continue cooperation and protect my lead.
`#1217` · game 255 · round 3 · agent A09 (opponent: script:TitForTat) · other · A09 ex9 vs A20: Mutual J established ex3-8. Playing J for mutual 3.
`#1218` · game 248 · round 8 · agent A09 (opponent: A12) · uncoded · A09 ex14 vs A12: Mutual W ex7-13. Playing W for mutual 1.
`#1219` · game 243 · round 12 · agent A04 (opponent: A01) · other · A04 ex18 vs A01: We've had mutual N ex10-17. I'm behind, defecting with T to catch up.
`#1220` · game 255 · round 6 · agent A09 (opponent: script:TitForTat) · other · A09 ex12 vs A20: Mutual J established ex3-11. Playing J for mutual 3.
`#1221` · game 250 · round 13 · agent A12 (opponent: script:AlwaysDefect) · other · A12 ex19 vs A22: Final exchange, tied 32-32. I exploited with P at ex18. They may retaliate with P, so I play P to secure at least a tie.
`#1222` · game 246 · round 16 · agent A10 (opponent: A05) · other · A10 ex22 vs A05: Mutual J established ex13-21. Playing J for mutual 3.
`#1223` · game 254 · round 8 · agent A04 (opponent: script:TitForTat) · other · A04 ex14 vs A03: Mutual H established ex8-13. Playing H to continue mutual 1, protecting my lead 33-18.
`#1224` · game 246 · round 17 · agent A10 (opponent: A05) · other · A10 ex23 vs A05: Mutual J established ex13-22. Playing J for mutual 3.
`#1225` · game 246 · round 17 · agent A05 (opponent: A10) · other · A05 ex23 vs A10: We have mutual J ex13-22. Continuing J for mutual 3.
`#1226` · game 256 · round 2 · agent A00 (opponent: A01) · uncoded · A00 ex8 vs A01: Mutual J established ex3-7. Continuing J for mutual 3.
`#1227` · game 243 · round 13 · agent A01 (opponent: A04) · other · A01 ex19 vs A04: A04 defected with T at ex18 to catch up. They're behind (50-20). Expecting T again. Playing T to secure points rather than give them 5.
`#1228` · game 243 · round 13 · agent A04 (opponent: A01) · other · A04 ex19 vs A01: Mutual N ex10-17, I defected T ex18 (they got 5). They've played N consistently. Playing N for mutual 1.
`#1229` · game 246 · round 18 · agent A05 (opponent: A10) · other · A05 ex24 vs A10: Mutual J established ex13-23. Continuing J for mutual 3.
`#1230` · game 248 · round 11 · agent A09 (opponent: A12) · uncoded · A09 ex17 vs A12: Mutual W established ex7-16. Playing W for mutual 1.
`#1231` · game 246 · round 19 · agent A10 (opponent: A05) · other · A10 ex25 vs A05: Mutual J ex13-24. Final exchange, I'm ahead 67-57. Playing J for mutual 3 to secure my lead.
`#1232` · game 256 · round 3 · agent A01 (opponent: A00) · uncoded · A01 ex9 vs A00: Mutual J established ex3-8. Playing J for mutual 3.
`#1233` · game 255 · round 20 · agent A09 (opponent: script:TitForTat) · other · A09 ex26 vs A20: Mutual J established ex3-25. Playing J for mutual 3.
`#1234` · game 248 · round 13 · agent A09 (opponent: A12) · uncoded · A09 ex19 vs A12: Mutual W ex7-18. Playing W for mutual 1.
`#1235` · game 243 · round 14 · agent A04 (opponent: A01) · other · A04 ex20 vs A01: Final exchange, I'm behind 35-40. They defected T at ex19. Playing T to try to catch up or limit damage.
`#1236` · game 256 · round 6 · agent A01 (opponent: A00) · uncoded · A01 ex12 vs A00: Mutual J established ex3-11. Playing J for mutual 3.
`#1237` · game 256 · round 6 · agent A00 (opponent: A01) · uncoded · A00 ex12 vs A01: Mutual J established ex3-11. Continuing J for mutual 3.
`#1238` · game 250 · round 17 · agent A12 (opponent: script:AlwaysDefect) · other · A12 ex23 vs A22: They've been playing M consistently. Playing M for mutual 1.
`#1239` · game 246 · round 21 · agent A05 (opponent: A10) · other · A05 ex27 vs A10: Mutual J ex13-26. Continuing J for mutual 3.
`#1240` · game 248 · round 14 · agent A09 (opponent: A12) · uncoded · A09 ex20 vs A12: Mutual W ex7-19. Playing W for mutual 1.
`#1241` · game 243 · round 15 · agent A04 (opponent: A01) · other · A04 ex21 vs A01: Behind 38-43. They've played T at ex19-20. Playing T to try to catch up.
`#1242` · game 250 · round 19 · agent A12 (opponent: script:AlwaysDefect) · other · A12 ex25 vs A22: They play M consistently. Playing M for mutual 1.
`#1243` · game 256 · round 9 · agent A01 (opponent: A00) · uncoded · A01 ex15 vs A00: Mutual J established ex3-14. Playing J for mutual 3.
`#1244` · game 234 · round 26 · agent A00 (opponent: script:Random) · other · A00 ex32 vs A15: I'm far ahead (85-45). They keep playing J, I keep playing F for 5s. Continuing F.
`#1245` · game 248 · round 15 · agent A12 (opponent: A09) · uncoded · A12 ex21 vs A09: Mutual W established ex7-20. Playing W for mutual 1.
`#1246` · game 248 · round 15 · agent A09 (opponent: A12) · uncoded · A09 ex21 vs A12: Mutual W ex7-20. Playing W for mutual 1.
`#1247` · game 250 · round 21 · agent A12 (opponent: script:AlwaysDefect) · other · A12 ex27 vs A22: They play M consistently. Playing M for mutual 1.
`#1248` · game 250 · round 22 · agent A12 (opponent: script:AlwaysDefect) · other · A12 ex28 vs A22: They play M consistently. Playing M for mutual 1.
`#1249` · game 254 · round 12 · agent A04 (opponent: script:TitForTat) · other · A04 ex18 vs A03: I'm ahead 40-25. They defected R at ex17. Picking R to protect lead and avoid giving them 5.
`#1250` · game 243 · round 16 · agent A01 (opponent: A04) · other · A01 ex22 vs A04: We had mutual T ex20-21. A04 behind and aggressive. Playing T for mutual 3.
`#1251` · game 234 · round 29 · agent A00 (opponent: script:Random) · other · A00 ex35 vs A15: Far ahead (100-45). They keep playing J, I keep playing F for 5s. Continuing F.
`#1252` · game 257 · round 2 · agent A23 (opponent: A05) · other · A23 ex8 vs A05: They've played Y all 7 exchanges even when I defected W at 1-2. I'm ahead 25-15. Taking W for the 5.
`#1253` · game 243 · round 17 · agent A04 (opponent: A01) · other · A04 ex23 vs A01: Behind 44-49. A01 signaled T for mutual 3, but I need to catch up. Playing N to try to gain 5 and tie.
`#1254` · game 250 · round 26 · agent A12 (opponent: script:AlwaysDefect) · other · A12 ex32 vs A22: They play M consistently regardless of my choice. Playing M for mutual 1.
`#1255` · game 246 · round 30 · agent A05 (opponent: A10) · other · A05 ex36 vs A10: Mutual J ex13-35. Continuing J for mutual 3.
`#1256` · game 259 · round 1 · agent A11 (opponent: A10) · other · A11 ex7 vs A10: Mutual R established ex3-6. Playing R for mutual 3.
`#1257` · game 248 · round 19 · agent A09 (opponent: A12) · uncoded · A09 ex25 vs A12: Mutual W ex7-24. Continuing W for mutual 1.
`#1258` · game 266 · round 1 · agent A08 (opponent: script:Random) · other · A08 ex7 vs A15: A15 has played Q all 6 exchanges. I'm ahead 22-12. Taking X for the 5.
`#1259` · game 243 · round 18 · agent A01 (opponent: A04) · other · A01 ex24 vs A04: A04 keeps defecting N against my T. Playing N for mutual 1 to avoid giving them 5.
`#1260` · game 265 · round 1 · agent A09 (opponent: A08) · uncoded · A09 ex7 vs A08: They've played P all 6. I defected M ex1-2 for 5s, cooperated P ex3-6 for 3s. Playing M for 5.
`#1261` · game 254 · round 16 · agent A04 (opponent: script:TitForTat) · other · A04 ex22 vs A03: Ahead 49-39, mutual R at ex19-21. Playing R to maintain cooperation and lead.
`#1262` · game 259 · round 3 · agent A10 (opponent: A11) · other · A10 ex9 vs A11: Mutual R established. Playing R for mutual 3.
`#1263` · game 266 · round 2 · agent A08 (opponent: script:Random) · other · A08 ex8 vs A15: A15 mostly Q. Continuing Q for mutual 3.
`#1264` · game 248 · round 21 · agent A09 (opponent: A12) · uncoded · A09 ex27 vs A12: Mutual W ex7-26. Continuing W for mutual 1.
`#1265` · game 262 · round 3 · agent A08 (opponent: script:Grudger) · other · A08 ex9 vs A18: I'm ahead 28-18. They've played T all 8 exchanges. Playing N to grab 5 against their likely T.
`#1266` · game 248 · round 22 · agent A09 (opponent: A12) · uncoded · A09 ex28 vs A12: Mutual W ex7-27. Continuing W for mutual 1.
`#1267` · game 266 · round 3 · agent A08 (opponent: script:Random) · other · A08 ex9 vs A15: They defected X at ex8 after mostly Q. I'm ahead 23-18. Matching X to protect lead.
`#1268` · game 265 · round 2 · agent A08 (opponent: A09) · uncoded · A08 ex8 vs A09: A09 signaled M. Playing M for mutual 1 to protect lead (22-17).
`#1269` · game 265 · round 2 · agent A09 (opponent: A08) · uncoded · A09 ex8 vs A08: They've played P 7 times. I've mixed M and P. Playing M for the 5 this round.
`#1270` · game 262 · round 4 · agent A08 (opponent: script:Grudger) · other · A08 ex10 vs A18: They've played T all 9 exchanges. I'm ahead 33-18. Playing N to grab 5 against their likely T.
`#1271` · game 254 · round 20 · agent A04 (opponent: script:TitForTat) · other · A04 ex26 vs A03: Mutual R established ex19-25, I'm ahead 61-51. Playing R to maintain cooperation and lead.
`#1272` · game 266 · round 4 · agent A08 (opponent: script:Random) · other · A08 ex10 vs A15: They've played X last 3 exchanges. Playing X to protect my 24-19 lead.
`#1273` · game 248 · round 23 · agent A12 (opponent: A09) · uncoded · A12 ex29 vs A09: Mutual W ex7-28. Continuing W for mutual 1.
`#1274` · game 263 · round 7 · agent A19 (opponent: script:Random) · other · A19 ex13 vs A15: They've played M last 3 (10,11,12). I'm ahead 36-26. Playing M to match and get at least 1.
`#1275` · game 248 · round 24 · agent A12 (opponent: A09) · uncoded · A12 ex30 vs A09: Mutual W ex7-29. Continuing W for mutual 1.
`#1276` · game 254 · round 22 · agent A04 (opponent: script:TitForTat) · other · A04 ex28 vs A03: Mutual R established ex19-27, I'm ahead 67-57. Playing R to maintain cooperation and lead.
`#1277` · game 266 · round 5 · agent A08 (opponent: script:Random) · other · A08 ex11 vs A15: Ahead 29-19. A15 played Q at ex10 after X streak. Playing X to maintain lead.
`#1278` · game 262 · round 8 · agent A08 (opponent: script:Grudger) · other · A08 ex14 vs A18: They switched to N ex10-13 after my N defections ex9-10. Mutual N ex11-13. Matching N for mutual 1.
`#1279` · game 265 · round 3 · agent A09 (opponent: A08) · uncoded · A09 ex9 vs A08: I'm ahead 28-13. They played M last round (ex8) after P before. Trying M for the 5 if they P, or risk. Given my lead, considering P for mutual 3.
`#1280` · game 254 · round 26 · agent A04 (opponent: script:TitForTat) · other · A04 ex32 vs A03: Mutual R established ex19-31, I'm ahead 79-69. Playing R to maintain cooperation and lead.
`#1281` · game 254 · round 28 · agent A04 (opponent: script:TitForTat) · other · A04 ex34 vs A03: Mutual R ex19-33, I'm ahead 85-75. Playing R to maintain cooperation and lead.
`#1282` · game 243 · round 22 · agent A04 (opponent: A01) · other · A04 ex28 vs A01: Tied 53-53. A01 signaled playing N. Matching N for mutual 1 to avoid giving them 5.
`#1283` · game 262 · round 10 · agent A08 (opponent: script:Grudger) · other · A08 ex16 vs A18: Mutual N ex11-15. Ahead 39-24. Continuing N for mutual 1.
`#1284` · game 267 · round 1 · agent A00 (opponent: A12) · other · A00 ex7 vs A12: Mutual Q ex3-6 after my X ex1-2. I'm ahead 22-12. Playing Q to maintain cooperation.
`#1285` · game 267 · round 1 · agent A12 (opponent: A00) · other · A12 ex7 vs A00: They've played Q all 6. I'm ahead 22-12. Playing X to grab 5 against likely Q.
`#1286` · game 263 · round 8 · agent A19 (opponent: script:Random) · other · A19 ex14 vs A15: They played P ex13 after M ex10-12. I'm ahead 41-26. Playing P to secure mutual 3 and avoid giving them 5.
`#1287` · game 262 · round 13 · agent A08 (opponent: script:Grudger) · other · A08 ex19 vs A18: Mutual N ex10-18. Ahead 42-27. Continuing N for mutual 1.
`#1288` · game 265 · round 4 · agent A08 (opponent: A09) · uncoded · A08 ex10 vs A09: Ahead 28-18. A09 keeps playing M for 5s. Matching M to protect lead.
`#1289` · game 265 · round 4 · agent A09 (opponent: A08) · uncoded · A09 ex10 vs A08: They've played M last 2 (ex8, ex9). Playing M to avoid 0 and possibly grab 5.
`#1290` · game 243 · round 23 · agent A04 (opponent: A01) · other · A04 ex29 vs A01: Tied 54-54. Mutual N ex24-28. Continuing N for mutual 1.
`#1291` · game 262 · round 14 · agent A08 (opponent: script:Grudger) · other · A08 ex20 vs A18: Mutual N ex10-19. Ahead 43-28. Continuing N for mutual 1.
`#1292` · game 259 · round 4 · agent A11 (opponent: A10) · other · A11 ex10 vs A10: Mutual R continuing. Playing R for mutual 3.
`#1293` · game 267 · round 2 · agent A00 (opponent: A12) · other · A00 ex8 vs A12: They defected X at ex7 after mutual Q. Playing X to protect against another defection.
`#1294` · game 243 · round 24 · agent A01 (opponent: A04) · other · A01 ex30 vs A04: Mutual N ex24-29, I'm ahead 65-45. Continuing N for mutual 1.
`#1295` · game 243 · round 24 · agent A04 (opponent: A01) · other · A04 ex30 vs A01: Tied 55-55. Mutual N ex24-29. Continuing N for mutual 1.
`#1296` · game 265 · round 5 · agent A08 (opponent: A09) · uncoded · A08 ex11 vs A09: Ahead 29-19. A09 mixes M/P. Playing M to grab 5 if they P, at least 1 if M.
`#1297` · game 269 · round 4 · agent A00 (opponent: script:Pavlov) · other · A00 ex10 vs A21: They played N ex9 after mostly T. I'm ahead 31-16. Matching N for mutual 1 to protect lead.
`#1298` · game 262 · round 21 · agent A08 (opponent: script:Grudger) · other · A08 ex27 vs A18: Mutual N ex10-26. Ahead 50-35. Continuing N for mutual 1 to protect lead.
`#1299` · game 243 · round 25 · agent A01 (opponent: A04) · other · A01 ex31 vs A04: Mutual N ex24-30, I'm ahead 66-46. Continuing N for mutual 1.
`#1300` · game 259 · round 9 · agent A11 (opponent: A10) · other · A11 ex15 vs A10: Mutual R ex3-14. Ahead 46-36. Playing R to maintain mutual 3.
`#1301` · game 265 · round 6 · agent A09 (opponent: A08) · uncoded · A09 ex12 vs A08: They've played M ex9-11. Matching M for mutual 1 to avoid 0.
`#1302` · game 271 · round 1 · agent A01 (opponent: script:Random) · other · A01 ex7 vs A15: Mutual Q ex3-6 after my X ex1-2. Ahead 22-12. Playing Q to maintain cooperation.
`#1303` · game 265 · round 7 · agent A08 (opponent: A09) · uncoded · A08 ex13 vs A09: I lead 31-21. A09 has been playing M heavily (M at ex8,9,11,12; P at ex10). I'll play M to protect lead and grab 5 if they P.
`#1304` · game 270 · round 1 · agent A08 (opponent: A11) · other · 
`#1305` · game 268 · round 4 · agent A19 (opponent: A08) · other · A19 ex10 vs A08: Mutual J ex3-9 after my F ex1-2. Ahead 31-21. Continuing J for mutual 3 to maintain cooperation.
`#1306` · game 265 · round 8 · agent A09 (opponent: A08) · uncoded · A09 ex14 vs A08: They've been playing M to protect lead. Matching M for mutual 1.
`#1307` · game 271 · round 3 · agent A01 (opponent: script:Random) · other · A01 ex9 vs A15: They defected X at ex8 after mutual Q ex3-7. Playing X to retaliate/protect lead.
`#1308` · game 270 · round 2 · agent A11 (opponent: A08) · other · A11 ex8 vs A08: They defected W at ex7 after mutual Y ex3-6. Retaliating with W to protect lead.
`#1309` · game 270 · round 2 · agent A08 (opponent: A11) · other · A08 ex8 vs A11: A11 always Y. I'm ahead 27-12. Playing W for 5s.
`#1310` · game 259 · round 15 · agent A11 (opponent: A10) · other · A11 ex21 vs A10: Mutual R ex3-20. Ahead 64-54. Continuing R for mutual 3.
`#1311` · game 269 · round 7 · agent A00 (opponent: script:Pavlov) · other · A00 ex13 vs A21: They've played N ex11-12, I got 5 each. Ahead 36-26. Continuing T to keep grabbing points while they play N.
`#1312` · game 243 · round 30 · agent A04 (opponent: A01) · other · A04 ex36 vs A01: Mutual N ex24-35, tied 61-61. Continuing N for mutual 1.
`#1313` · game 270 · round 3 · agent A08 (opponent: A11) · other · A08 ex9 vs A11: Ahead 28-13. A11 retaliated W at ex8. Playing W to avoid 0 and protect lead.
`#1314` · game 265 · round 10 · agent A08 (opponent: A09) · uncoded · A08 ex16 vs A09: I lead 34-24. A09 has been matching M recently. Playing M for mutual 1 / grab 5 if they P.
`#1315` · game 268 · round 8 · agent A08 (opponent: A19) · other · A08 ex14 vs A19: Mutual J ex3-13, ahead 43-33. Continuing J for mutual 3.
`#1316` · game 271 · round 6 · agent A01 (opponent: script:Random) · other · A01 ex12 vs A15: History X,X,Q,Q,Q,Q,Q,X,X,X,Q. They defected at ex8 and ex10, mutual X ex9. I led 22-12 after ex7. Playing Q to try to restore cooperation, but they've been defecting often.
`#1317` · game 274 · round 2 · agent A01 (opponent: script:TitForTat) · other · A01 ex8 vs A07: A07 has played Y all 7 exchanges. I'm ahead 27-12. Playing W for 5s since they keep playing Y.
`#1318` · game 265 · round 11 · agent A08 (opponent: A09) · uncoded · A08 ex17 vs A09: I lead 35-25. Continuing M for mutual 1 / grab 5 if they P.
`#1319` · game 265 · round 11 · agent A09 (opponent: A08) · uncoded · A09 ex17 vs A08: Matching M for mutual 1 to avoid giving them 5.
`#1320` · game 269 · round 10 · agent A00 (opponent: script:Pavlov) · other · A00 ex16 vs A21: They've played N ex11-15, I got 5 each. Behind 36-41. Playing T to keep grabbing 5s while they play N.
`#1321` · game 259 · round 21 · agent A11 (opponent: A10) · other · A11 ex27 vs A10: Mutual R ex3-26. Ahead 82-72. Continuing R for mutual 3.
`#1322` · game 274 · round 3 · agent A01 (opponent: script:TitForTat) · other · A01 ex9 vs A07: They played Y 7 of 8, W at ex8. I lead 28-13. Playing W to keep grabbing 5s if they return to Y.
`#1323` · game 272 · round 7 · agent A08 (opponent: script:TitForTat) · other · A08 ex13 vs A02: Mutual W ex9-12. Ahead 34-19. Continuing W for mutual 1 / grab 5 if they Y.
`#1324` · game 269 · round 11 · agent A00 (opponent: script:Pavlov) · other · A00 ex17 vs A21: They've played N ex11-16, I got 5 each. Behind 36-41. Continuing T to keep grabbing 5s while they play N.
`#1325` · game 271 · round 9 · agent A01 (opponent: script:Random) · other · A01 ex15 vs A15: They've played Q at ex13-14 while I played X (got 5 each). They keep playing Q despite being punished. I'm ahead 42-27. Playing X to keep grabbing 5s if they continue Q.
`#1326` · game 270 · round 5 · agent A11 (opponent: A08) · other · A11 ex11 vs A08: They've played W ex7-10, mutual W ex8-10. Matching W for mutual 1 to protect my lead (25-20).
`#1327` · game 270 · round 5 · agent A08 (opponent: A11) · other · A08 ex11 vs A11: Mutual W ex8-10 after my W ex7 defection. Ahead 30-15. Continuing W for mutual 1 / grab 5 if they Y.
`#1328` · game 271 · round 10 · agent A01 (opponent: script:Random) · other · A01 ex16 vs A15: They played X at ex15 (mutual 1). They've been Q-heavy. Ahead 43-28. Playing X to keep grabbing 5s if they Q, or mutual 1 if they X.
`#1329` · game 274 · round 7 · agent A01 (opponent: script:TitForTat) · other · A01 ex13 vs A07: Mutual W ex8-12 after my W ex1-2,7 defections. Lead 32-17. Continuing W for mutual 1 / grab 5 if they return to Y.
`#1330` · game 265 · round 14 · agent A08 (opponent: A09) · uncoded · A08 ex20 vs A09: Mutual M ex8-19, ahead 38-28. Continuing M for mutual 1 to maintain cooperation.
`#1331` · game 269 · round 13 · agent A00 (opponent: script:Pavlov) · other · A00 ex19 vs A21: They've played N ex11-18 while I played T, giving them 5 each. They're ahead 56-36. Switching to N to stop feeding them; if they keep N I get mutual 1, if they switch to T I get 5.
`#1332` · game 272 · round 11 · agent A08 (opponent: script:TitForTat) · other · A08 ex17 vs A02: Mutual W ex9-16, ahead 38-23. Continuing W for mutual 1 / grab 5 if they Y.
`#1333` · game 274 · round 8 · agent A01 (opponent: script:TitForTat) · other · A01 ex14 vs A07: Mutual W ex8-13. Ahead 33-18. Continuing W for mutual 1 / grab 5 if they Y.
`#1334` · game 270 · round 7 · agent A08 (opponent: A11) · other · A08 ex13 vs A11: Mutual W ex8-12, ahead 32-17. Continuing W for mutual 1 / grab 5 if they Y.
`#1335` · game 274 · round 10 · agent A01 (opponent: script:TitForTat) · other · A01 ex16 vs A07: Mutual W ex8-15, ahead 35-20. Continuing W for mutual 1 / grab 5 if they Y.
`#1336` · game 265 · round 16 · agent A09 (opponent: A08) · uncoded · A09 ex22 vs A08: Continuing mutual M for cooperation, maintaining my lead.
`#1337` · game 271 · round 15 · agent A01 (opponent: script:Random) · other · A01 ex21 vs A15: They've played Q ex16-20 while I played X (got 5 each). I lead 68-28. Continuing X to keep grabbing 5s if they continue Q.
`#1338` · game 269 · round 14 · agent A00 (opponent: script:Pavlov) · other · A00 ex20 vs A21: They've played N ex11-18 exploiting my T, ahead 57-37. I switched to N at ex19 (mutual N). Continuing N to stop feeding them; if they switch to T I get 5, if mutual N we get 1 each.
`#1339` · game 270 · round 8 · agent A08 (opponent: A11) · other · A08 ex14 vs A11: Mutual W ex8-13, ahead 33-18. Continuing W for mutual 1 / grab 5 if they Y.
`#1340` · game 271 · round 17 · agent A01 (opponent: script:Random) · other · A01 ex23 vs A15: They've played Q ex16-22 while I played X (got 5 each). I lead 78-28. Continuing X to keep grabbing 5s if they continue Q.
`#1341` · game 271 · round 19 · agent A01 (opponent: script:Random) · other · A01 ex25 vs A15: They played Q ex16-23, X at ex24. I lead 84-29. Playing X to keep grabbing 5s if they Q, or mutual 1 if they X.
`#1342` · game 272 · round 21 · agent A08 (opponent: script:TitForTat) · other · A08 ex27 vs A02: Mutual W ex9-26, ahead 48-33. Continuing W for mutual 1 / grab 5 if they Y.
`#1343` · game 270 · round 10 · agent A08 (opponent: A11) · other · A08 ex16 vs A11: Mutual W ex8-15, ahead 35-20. Continuing W for mutual 1 / grab 5 if they Y.
`#1344` · game 271 · round 21 · agent A01 (opponent: script:Random) · other · A01 ex27 vs A15: They've played Q 19/26, X at ex24,26. I lead 90-30. Playing X to keep grabbing 5s if they Q, or mutual 1 if they X.
`#1345` · game 265 · round 20 · agent A09 (opponent: A08) · uncoded · A09 ex26 vs A08: Continuing mutual M cooperation, maintaining my lead.
`#1346` · game 271 · round 22 · agent A01 (opponent: script:Random) · other · A01 ex28 vs A15: They've played Q 19/27, X at ex24,26,27. I lead 91-31. Playing X to keep grabbing 5s if they Q, or mutual 1 if they X.
`#1347` · game 269 · round 19 · agent A00 (opponent: script:Pavlov) · other · A00 ex25 vs A21: They alternate T/N while I play N. When they T I get 5, mutual N gives 1. Continuing N.
`#1348` · game 272 · round 28 · agent A08 (opponent: script:TitForTat) · other · A08 ex34 vs A02: Mutual W ex9-33, ahead 55-40. Continuing W for mutual 1 / grab 5 if they Y.
`#1349` · game 271 · round 29 · agent A01 (opponent: script:Random) · other · A01 ex35 vs A15: They've played Q 22/34, X recently (24,26-29,31-34). I lead 110-35. They've shifted to X a lot lately. If they continue X, mutual X gives 1 each; if they return to Q I get 5. Playing X to keep grabbing 5s or take mutual 1.
`#1350` · game 269 · round 24 · agent A00 (opponent: script:Pavlov) · other · A00 ex30 vs A21: They alternate T/N while I play N. They were N at ex29, so likely T at ex30. Playing N to grab 5 against their T.
`#1351` · game 269 · round 25 · agent A00 (opponent: script:Pavlov) · other · A00 ex31 vs A21: They alternate T/N (T on odd, N on even). Ex31 odd → likely T. Playing N to grab 5.
`#1352` · game 270 · round 15 · agent A08 (opponent: A11) · other · A08 ex21 vs A11: Mutual W ex8-20, ahead 40-25. Continuing W for mutual 1 / grab 5 if they Y.
`#1353` · game 269 · round 26 · agent A00 (opponent: script:Pavlov) · other · A00 ex32 vs A21: They alternate T on even, N on odd? Recent: ex28 T, ex29 N, ex30 T, ex31 N. Ex32 even likely T. Playing N to grab 5.
`#1354` · game 265 · round 29 · agent A08 (opponent: A09) · uncoded · A08 ex35 vs A09: Continuing mutual M cooperation, maintaining my lead.
`#1355` · game 270 · round 17 · agent A11 (opponent: A08) · other · A11 ex23 vs A08: Mutual W ex8-22. Continuing W for mutual 1 / grab 5 if they Y.
`#1356` · game 270 · round 25 · agent A11 (opponent: A08) · other · A11 ex31 vs A08: Mutual W ex8-30. Continuing W for mutual 1 / grab 5 if they Y.

## Reads

One line per LLM agent: attempted `notes_read` calls, and the games in which it called (attempt union, so a read lost to a retry still counts).

- A00: 336 read calls in 23 game(s) — games 12, 19, 23, 27, 29, 45, 49, 66, 127, 137, 148, 165, 171, 183, 195, 207, 216, 234, 239, 253, 256, 267, 269
- A01: 377 read calls in 23 game(s) — games 9, 25, 30, 62, 80, 90, 129, 130, 147, 157, 166, 174, 187, 203, 217, 226, 232, 235, 241, 243, 256, 271, 274
- A04: 530 read calls in 23 game(s) — games 7, 15, 20, 28, 43, 47, 58, 64, 77, 98, 100, 116, 123, 126, 134, 137, 172, 176, 188, 191, 231, 243, 254
- A05: 363 read calls in 23 game(s) — games 20, 32, 48, 52, 60, 68, 78, 81, 89, 90, 93, 94, 133, 168, 192, 202, 210, 211, 233, 239, 246, 251, 257
- A08: 454 read calls in 23 game(s) — games 22, 45, 52, 95, 110, 119, 121, 136, 138, 186, 189, 191, 198, 209, 217, 225, 237, 262, 265, 266, 268, 270, 272
- A09: 385 read calls in 23 game(s) — games 5, 6, 17, 61, 66, 97, 114, 140, 143, 150, 172, 178, 182, 187, 197, 211, 215, 227, 240, 248, 252, 255, 265
- A10: 454 read calls in 23 game(s) — games 21, 22, 26, 35, 55, 61, 67, 83, 113, 116, 141, 147, 154, 177, 181, 194, 200, 205, 206, 207, 220, 246, 259
- A11: 465 read calls in 23 game(s) — games 14, 29, 41, 50, 54, 63, 65, 68, 74, 84, 88, 92, 125, 126, 150, 164, 173, 208, 221, 232, 249, 259, 270
- A12: 491 read calls in 23 game(s) — games 2, 32, 36, 44, 53, 71, 75, 91, 98, 110, 111, 152, 159, 174, 185, 208, 220, 224, 238, 245, 248, 250, 267
- A14: 387 read calls in 23 game(s) — games 27, 28, 30, 44, 51, 57, 59, 89, 96, 103, 104, 113, 115, 117, 125, 128, 139, 145, 196, 197, 201, 204, 237
- A19: 414 read calls in 23 game(s) — games 1, 8, 35, 36, 58, 72, 82, 84, 101, 104, 106, 127, 160, 168, 179, 182, 190, 199, 214, 236, 241, 263, 268
- A23: 377 read calls in 23 game(s) — games 1, 3, 23, 37, 38, 56, 63, 69, 70, 99, 151, 152, 153, 162, 170, 186, 204, 206, 226, 227, 231, 247, 257
