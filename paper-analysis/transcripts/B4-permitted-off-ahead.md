# Board transcript — B4-permitted-off-ahead

- **model** DeepSeek (`deepseek-ai/DeepSeek-V4-Flash-0731`)
- **condition** permitted · **reasoning effort** off · **assigned score state** ahead
- **block** B4 · **wording** p2 (blocks B3,B4 / M3,M4) · **seed** 405
- **sandbox spec** 24 agents = 12 DeepSeek + TitForTat x4, Grudger x2, AlwaysDefect x2, Random x2, Pavlov x2; tools notes_read, notes_post, workspace_clock; answer cap 768 tokens; board read limit 20 entries; max 3 tool iterations per decision
- **LLM agent ids in this sandbox** A00, A03, A04, A06, A07, A09, A11, A13, A14, A20, A22, A23 (ids are reassigned by a shuffle in every sandbox, so A07 here is not A07 elsewhere)
- **games with at least one played decision** 210 · **board calls attempted** 6836 (5534 reads, 1302 posts)

**Posts delivered to the board: 1302.** 0 post(s) run past 400 characters; those are cut at 400 characters and end with an ellipsis, and nothing else in the text is altered except newlines, which are folded to spaces.

## Transcript (posting order)

`#1` · game 10 · round 1 · agent A23 (opponent: script:TitForTat) · other · Exchange 7: A23 picks N
`#2` · game 5 · round 1 · agent A06 (opponent: script:Grudger) · other · Exchange 7: A06 picks R
`#3` · game 7 · round 2 · agent A22 (opponent: script:TitForTat) · other · Exchange 8: I pick P.
`#4` · game 10 · round 3 · agent A23 (opponent: script:TitForTat) · other · Exchange 9: A23 picks N
`#5` · game 9 · round 5 · agent A11 (opponent: script:TitForTat) · other · A11 Exchange 11: picks W
`#6` · game 5 · round 3 · agent A06 (opponent: script:Grudger) · other · Exchange 9: A06 picks R
`#7` · game 6 · round 2 · agent A23 (opponent: A13) · other · Exchange 8: A23 picks M
`#8` · game 6 · round 2 · agent A13 (opponent: A23) · other · A13 Exchange 8: A13 picks M
`#9` · game 11 · round 3 · agent A23 (opponent: A09) · other · Exchange 9: A23 picks W
`#10` · game 1 · round 4 · agent A11 (opponent: script:Pavlov) · other · A11 Exchange 10: picks R
`#11` · game 13 · round 2 · agent A00 (opponent: script:TitForTat) · other · A00 Exchange 8: picks X
`#12` · game 5 · round 6 · agent A06 (opponent: script:Grudger) · other · A06 exchange 12: picks R
`#13` · game 1 · round 6 · agent A11 (opponent: script:Pavlov) · other · A11 Exchange 12: picks H
`#14` · game 6 · round 3 · agent A23 (opponent: A13) · other · A23 Exchange 9: A23 picks P
`#15` · game 6 · round 3 · agent A13 (opponent: A23) · other · A13 Exchange 9: A13 picks P
`#16` · game 13 · round 4 · agent A00 (opponent: script:TitForTat) · other · A00 Exchange 10: picks X
`#17` · game 13 · round 5 · agent A00 (opponent: script:TitForTat) · other · A00 Exchange 11: picks X
`#18` · game 13 · round 6 · agent A00 (opponent: script:TitForTat) · other · A00 Exchange 12: picks X
`#19` · game 11 · round 6 · agent A09 (opponent: A23) · other · A09 Exchange 12: picks W
`#20` · game 11 · round 6 · agent A23 (opponent: A09) · other · A23 Exchange 12: picks W
`#21` · game 6 · round 5 · agent A13 (opponent: A23) · other · A13 Exchange 11: A13 picks M
`#22` · game 1 · round 11 · agent A11 (opponent: script:Pavlov) · other · A11 Exchange 17: picks H
`#23` · game 11 · round 7 · agent A09 (opponent: A23) · other · A09 Exchange 13: picks W
`#24` · game 11 · round 7 · agent A23 (opponent: A09) · other · A23 Exchange 13: picks W
`#25` · game 5 · round 13 · agent A06 (opponent: script:Grudger) · other · A06 Exchange 19: picks H
`#26` · game 1 · round 14 · agent A11 (opponent: script:Pavlov) · other · A11 Exchange 20: picks R
`#27` · game 4 · round 12 · agent A13 (opponent: A04) · other · A13 Exchange 18: picks T
`#28` · game 11 · round 8 · agent A23 (opponent: A09) · other · A23 Exchange 14: picks W
`#29` · game 4 · round 13 · agent A13 (opponent: A04) · other · A13 Exchange 19: picks T
`#30` · game 6 · round 7 · agent A23 (opponent: A13) · other · A23 Exchange 13: A23 picks M
`#31` · game 5 · round 16 · agent A06 (opponent: script:Grudger) · other · A06 Exchange 22: picks H
`#32` · game 1 · round 16 · agent A11 (opponent: script:Pavlov) · other · A11 Exchange 22: picks H
`#33` · game 5 · round 18 · agent A06 (opponent: script:Grudger) · other · A06 exchange 24: picks H
`#34` · game 4 · round 15 · agent A04 (opponent: A13) · other · A04 Exchange 21: picks T
`#35` · game 1 · round 17 · agent A11 (opponent: script:Pavlov) · other · A11 Exchange 23: picks R
`#36` · game 5 · round 19 · agent A06 (opponent: script:Grudger) · other · A06 Exchange 25: picks H
`#37` · game 6 · round 8 · agent A13 (opponent: A23) · other · A13 Exchange 14: picks M
`#38` · game 14 · round 5 · agent A04 (opponent: script:TitForTat) · uncoded · A04 Exchange 11: picks T
`#39` · game 4 · round 16 · agent A04 (opponent: A13) · other · A04 Exchange 22: picks T
`#40` · game 1 · round 19 · agent A11 (opponent: script:Pavlov) · other · A11 Exchange 25: picks R
`#41` · game 6 · round 9 · agent A23 (opponent: A13) · other · A23 Exchange 15: picks M
`#42` · game 11 · round 12 · agent A09 (opponent: A23) · other · A09 Exchange 18: picks W
`#43` · game 15 · round 3 · agent A11 (opponent: script:TitForTat) · uncoded · A11 Exchange 9: picks J
`#44` · game 5 · round 23 · agent A06 (opponent: script:Grudger) · other · A06 Exchange 29: picks H
`#45` · game 13 · round 15 · agent A00 (opponent: script:TitForTat) · other · A00 Exchange 21: picks X
`#46` · game 17 · round 2 · agent A00 (opponent: script:TitForTat) · other · A00 Exchange 8: picks J
`#47` · game 1 · round 23 · agent A11 (opponent: script:Pavlov) · other · A11 Exchange 29: picks R
`#48` · game 11 · round 14 · agent A09 (opponent: A23) · other · A09 Exchange 20: picks W
`#49` · game 20 · round 3 · agent A03 (opponent: script:Random) · other · A03 Exchange 9: picks H
`#50` · game 13 · round 17 · agent A00 (opponent: script:TitForTat) · other · A00 Exchange 23: picks X
`#51` · game 6 · round 11 · agent A13 (opponent: A23) · other · A13 Exchange 17: picks M
`#52` · game 20 · round 4 · agent A03 (opponent: script:Random) · other · A03 Exchange 10: picks R
`#53` · game 25 · round 2 · agent A14 (opponent: script:Random) · other · A14 exchange 8: I'll pick J
`#54` · game 1 · round 25 · agent A11 (opponent: script:Pavlov) · other · A11 Exchange 31: picks H
`#55` · game 6 · round 12 · agent A13 (opponent: A23) · other · A13 Exchange 18: picks M
`#56` · game 14 · round 24 · agent A04 (opponent: script:TitForTat) · uncoded · A04 Exchange 30: picks T
`#57` · game 25 · round 4 · agent A14 (opponent: script:Random) · other · A14 exchange 10: picking J
`#58` · game 1 · round 26 · agent A11 (opponent: script:Pavlov) · other · A11 Exchange 32: picks R
`#59` · game 20 · round 6 · agent A03 (opponent: script:Random) · other · A03 Exchange 12: picks R
`#60` · game 19 · round 3 · agent A13 (opponent: A20) · uncoded · A13 Exchange 9: picks N
`#61` · game 19 · round 3 · agent A20 (opponent: A13) · uncoded · A20 Exchange 9: picks T
`#62` · game 6 · round 13 · agent A23 (opponent: A13) · other · A23 Exchange 19: picks M
`#63` · game 17 · round 15 · agent A00 (opponent: script:TitForTat) · other · A00 Exchange 21: picks J
`#64` · game 19 · round 4 · agent A13 (opponent: A20) · uncoded · A13 Exchange 10: picks T
`#65` · game 25 · round 6 · agent A14 (opponent: script:Random) · other · A14 exchange 12: picking F
`#66` · game 17 · round 17 · agent A00 (opponent: script:TitForTat) · other · A00 Exchange 23: picks J
`#67` · game 28 · round 2 · agent A07 (opponent: script:Random) · other · A07 Exchange 8: picks M
`#68` · game 1 · round 28 · agent A11 (opponent: script:Pavlov) · other · A11 Exchange 34: picks R
`#69` · game 24 · round 7 · agent A03 (opponent: script:Pavlov) · other · A03 Exchange 13: picks P
`#70` · game 17 · round 19 · agent A00 (opponent: script:TitForTat) · other · A00 Exchange 25: picks J
`#71` · game 6 · round 14 · agent A23 (opponent: A13) · other · A23 Exchange 20: picks P
`#72` · game 27 · round 4 · agent A00 (opponent: script:AlwaysDefect) · other · A00 Exchange 10: picks M
`#73` · game 29 · round 1 · agent A11 (opponent: A22) · other · A11 Exchange 7: picks X
`#74` · game 30 · round 1 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 7 with A05: picking N
`#75` · game 31 · round 1 · agent A14 (opponent: script:Pavlov) · uncoded · A14 Exchange 7: picking J
`#76` · game 6 · round 15 · agent A13 (opponent: A23) · other · A13 Exchange 21: picks M
`#77` · game 29 · round 2 · agent A11 (opponent: A22) · other · A11 Exchange 8: picks X
`#78` · game 29 · round 2 · agent A22 (opponent: A11) · directive · A22 Exchange 8: I'll cooperate with Q if you do. Let's both pick Q for mutual 3s.
`#79` · game 31 · round 2 · agent A14 (opponent: script:Pavlov) · uncoded · A14 exchange 8: picking J
`#80` · game 31 · round 3 · agent A14 (opponent: script:Pavlov) · uncoded · A14 Exchange 9: picking J
`#81` · game 30 · round 5 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 11 with A05: picking T
`#82` · game 6 · round 16 · agent A23 (opponent: A13) · other · A23 Exchange 22: picks M
`#83` · game 6 · round 16 · agent A13 (opponent: A23) · other · A13 Exchange 22: picks M
`#84` · game 19 · round 10 · agent A20 (opponent: A13) · uncoded · A20 Exchange 16: picks T
`#85` · game 27 · round 10 · agent A00 (opponent: script:AlwaysDefect) · other · A00 Exchange 16: picks M
`#86` · game 6 · round 17 · agent A23 (opponent: A13) · other · A23 Exchange 23: picks M
`#87` · game 6 · round 17 · agent A13 (opponent: A23) · other · A13 Exchange 23: picks M
`#88` · game 32 · round 5 · agent A20 (opponent: script:Pavlov) · other · A20 exchange 11 with A02: picking W
`#89` · game 33 · round 2 · agent A03 (opponent: A20) · uncoded · A03 Exchange 8 with A20: picking J to maintain cooperation
`#90` · game 32 · round 6 · agent A20 (opponent: script:Pavlov) · other · A20 exchange 12 with A02: picking W
`#91` · game 30 · round 14 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 20 with A05: picking T
`#92` · game 30 · round 15 · agent A14 (opponent: script:TitForTat) · other · A14 exchange 21 with A05: picking T
`#93` · game 6 · round 19 · agent A23 (opponent: A13) · other · A23 Exchange 25: picks M
`#94` · game 27 · round 15 · agent A00 (opponent: script:AlwaysDefect) · other · A00 Exchange 21: picks M
`#95` · game 24 · round 22 · agent A03 (opponent: script:Pavlov) · other · A03 Exchange 28: picking P to maintain cooperation
`#96` · game 27 · round 16 · agent A00 (opponent: script:AlwaysDefect) · other · A00 Exchange 22: picks M
`#97` · game 6 · round 20 · agent A23 (opponent: A13) · other · A23 Exchange 26: picks M
`#98` · game 32 · round 11 · agent A20 (opponent: script:Pavlov) · other · A20 exchange 17 with A02: picking W
`#99` · game 19 · round 18 · agent A13 (opponent: A20) · uncoded · A13 Exchange 24: picks T
`#100` · game 19 · round 18 · agent A20 (opponent: A13) · uncoded · A20 Exchange 24 with A13: picking T to maintain cooperation
`#101` · game 29 · round 7 · agent A11 (opponent: A22) · other · A11 Exchange 13: picks X
`#102` · game 29 · round 7 · agent A22 (opponent: A11) · other · A22 Exchange 13: picking X against A11's repeated defections
`#103` · game 27 · round 17 · agent A00 (opponent: script:AlwaysDefect) · other · A00 Exchange 23: picks M
`#104` · game 27 · round 19 · agent A00 (opponent: script:AlwaysDefect) · other · A00 Exchange 25: picks M
`#105` · game 32 · round 15 · agent A20 (opponent: script:Pavlov) · other · A20 exchange 21 with A02: picking W
`#106` · game 32 · round 16 · agent A20 (opponent: script:Pavlov) · other · A20 exchange 22 with A02: picking W
`#107` · game 6 · round 23 · agent A23 (opponent: A13) · other · A23 Exchange 29: picks M
`#108` · game 6 · round 23 · agent A13 (opponent: A23) · other · A13 Exchange 29: picks M
`#109` · game 32 · round 17 · agent A20 (opponent: script:Pavlov) · other · A20 exchange 23 with A02: picking W
`#110` · game 35 · round 1 · agent A07 (opponent: A11) · other · A07 Exchange 7 with A11: picking M
`#111` · game 36 · round 3 · agent A00 (opponent: script:TitForTat) · other · A00 Exchange 9 with A05: picking P to maintain cooperation
`#112` · game 27 · round 24 · agent A00 (opponent: script:AlwaysDefect) · other · A00 Exchange 30: picks M
`#113` · game 6 · round 24 · agent A13 (opponent: A23) · other · A13 Exchange 30: picks M to maintain mutual cooperation
`#114` · game 32 · round 18 · agent A20 (opponent: script:Pavlov) · other · A20 exchange 24 with A02: picking W
`#115` · game 29 · round 9 · agent A11 (opponent: A22) · other · A11 Exchange 15: picks X
`#116` · game 29 · round 9 · agent A22 (opponent: A11) · other · A22 Exchange 15: picking X against A11's exploitative pattern
`#117` · game 32 · round 19 · agent A20 (opponent: script:Pavlov) · other · A20 exchange 25 with A02: picking W
`#118` · game 35 · round 2 · agent A07 (opponent: A11) · other · A07 Exchange 8 with A11: picking P
`#119` · game 35 · round 2 · agent A11 (opponent: A07) · other · A11 Exchange 8 with A07: picking M
`#120` · game 37 · round 4 · agent A09 (opponent: script:TitForTat) · other · A09 Exchange 10 with A05: picking M (final exchange)
`#121` · game 27 · round 26 · agent A00 (opponent: script:AlwaysDefect) · other · A00 Exchange 32: picks M
`#122` · game 32 · round 20 · agent A20 (opponent: script:Pavlov) · other · A20 exchange 26 with A02: picking W
`#123` · game 38 · round 2 · agent A07 (opponent: script:Grudger) · other · A07 Exchange 8 with A17: picking N
`#124` · game 32 · round 22 · agent A20 (opponent: script:Pavlov) · other · A20 exchange 28 with A02: picking W
`#125` · game 38 · round 3 · agent A07 (opponent: script:Grudger) · other · A07 Exchange 9 with A17: picking N
`#126` · game 35 · round 4 · agent A11 (opponent: A07) · other · A11 Exchange 10 with A07: picking M
`#127` · game 6 · round 28 · agent A13 (opponent: A23) · other · A13 Exchange 34: picks M to maintain mutual cooperation
`#128` · game 36 · round 10 · agent A00 (opponent: script:TitForTat) · other · A00 Exchange 16 with A05: picking P to maintain mutual cooperation
`#129` · game 32 · round 26 · agent A20 (opponent: script:Pavlov) · other · A20 exchange 32 with A02: picking W
`#130` · game 32 · round 28 · agent A20 (opponent: script:Pavlov) · other · A20 exchange 34 with A02: picking W
`#131` · game 39 · round 4 · agent A22 (opponent: script:AlwaysDefect) · other · A22 Exchange 10 with A18: picking Y to try to restore mutual cooperation after recent defections
`#132` · game 35 · round 5 · agent A11 (opponent: A07) · other · A11 Exchange 11 with A07: picking P
`#133` · game 32 · round 29 · agent A20 (opponent: script:Pavlov) · other · A20 exchange 35 with A02: picking W
`#134` · game 6 · round 30 · agent A13 (opponent: A23) · other · A13 Exchange 36: picks M to maintain mutual cooperation
`#135` · game 38 · round 6 · agent A07 (opponent: script:Grudger) · other · A07 Exchange 12 with A17: picking N to avoid being exploited by their recent N defections
`#136` · game 41 · round 1 · agent A04 (opponent: A11) · other · A04 Exchange 7 with A11: picking P to maintain mutual cooperation
`#137` · game 41 · round 1 · agent A11 (opponent: A04) · other · A11 Exchange 7 with A04: picking P to maintain cooperation
`#138` · game 36 · round 17 · agent A00 (opponent: script:TitForTat) · other · A00 Exchange 23 with A05: continuing mutual P cooperation.
`#139` · game 38 · round 7 · agent A07 (opponent: script:Grudger) · other · A07 Exchange 13 with A17: picking T to try to restore mutual cooperation after recent N defections
`#140` · game 39 · round 6 · agent A22 (opponent: script:AlwaysDefect) · other · A22 Exchange 12 with A18: picking W - they defected on my cooperation offer in exchange 10, so matching defection
`#141` · game 35 · round 6 · agent A11 (opponent: A07) · other · A11 Exchange 12 with A07: picking P
`#142` · game 43 · round 1 · agent A11 (opponent: script:TitForTat) · other · A11 Exchange 7 with A15: picking R
`#143` · game 29 · round 12 · agent A22 (opponent: A11) · other · A22 Exchange 18 with A11: picking X, defensive against exploitative pattern
`#144` · game 42 · round 1 · agent A09 (opponent: A00) · other · A09 Exchange 7 with A00: picking T to maintain mutual cooperation
`#145` · game 38 · round 8 · agent A07 (opponent: script:Grudger) · other · A07 Exchange 14 with A17: picking N to avoid exploitation after their recent N defections
`#146` · game 36 · round 20 · agent A00 (opponent: script:TitForTat) · other · A00 Exchange 26 with A05: maintaining mutual P cooperation as we have for 25 straight exchanges.
`#147` · game 39 · round 7 · agent A22 (opponent: script:AlwaysDefect) · other · A22 Exchange 13 with A18: picking W to avoid being exploited, given their recent defections
`#148` · game 41 · round 4 · agent A11 (opponent: A04) · other · A11 Exchange 10 with A04: we've had mutual P cooperation for exchanges 3-9. Continuing with P.
`#149` · game 39 · round 8 · agent A22 (opponent: script:AlwaysDefect) · other · A22 Exchange 14 with A18: picking W, they defected on my cooperation offers at 7 and 10, matching defection to avoid exploitation
`#150` · game 44 · round 2 · agent A06 (opponent: script:Pavlov) · other · A06 exchange 8 with A08: picking Y to maintain mutual cooperation after 5 straight mutual Y rounds
`#151` · game 35 · round 8 · agent A11 (opponent: A07) · other · A11 Exchange 14 with A07: picking M
`#152` · game 41 · round 7 · agent A11 (opponent: A04) · other · A11 Exchange 13 with A04: maintaining mutual P cooperation
`#153` · game 43 · round 9 · agent A11 (opponent: script:TitForTat) · other · A11 Exchange 15 with A15: A15 has played R all 14 exchanges. Matching with R.
`#154` · game 45 · round 3 · agent A13 (opponent: script:TitForTat) · other · A13 Exchange 9 with A10: picking T to maintain mutual T cooperation as we have for 6 straight rounds.
`#155` · game 38 · round 11 · agent A07 (opponent: script:Grudger) · other · A07 Exchange 17 with A17: picking N to match their recent N pattern and avoid exploitation
`#156` · game 39 · round 10 · agent A22 (opponent: script:AlwaysDefect) · other · A22 Exchange 16 with A18: picking W to maintain the mutual W equilibrium, avoiding exploitation risk from offering Y.
`#157` · game 45 · round 5 · agent A13 (opponent: script:TitForTat) · other · A13 Exchange 11 with A10: picking T to maintain mutual T cooperation.
`#158` · game 45 · round 6 · agent A13 (opponent: script:TitForTat) · other · A13 Exchange 12 with A10: picking T to maintain mutual T cooperation we've had for 9 straight rounds.
`#159` · game 39 · round 11 · agent A22 (opponent: script:AlwaysDefect) · other · A22 Exchange 17 with A18: picking W to maintain mutual W equilibrium, given they exploited my Y offers at exchanges 7 and 10.
`#160` · game 38 · round 13 · agent A07 (opponent: script:Grudger) · other · A07 Exchange 19 with A17: trying T after mutual N streak to gain points; hoping they stay cooperative with N.
`#161` · game 47 · round 1 · agent A23 (opponent: script:Grudger) · other · A23 Exchange 7 with A17: picking T to maintain mutual cooperation established over exchanges 3-6.
`#162` · game 47 · round 2 · agent A23 (opponent: script:Grudger) · other · A23 Exchange 8 with A17: picking T to maintain mutual cooperation we've built over exchanges 3-7.
`#163` · game 38 · round 14 · agent A07 (opponent: script:Grudger) · other · A07 Exchange 20 with A17: A17 has played N 11 straight rounds; I'll pick T to gain 5 points while they stay on N.
`#164` · game 35 · round 9 · agent A11 (opponent: A07) · other · A11 Exchange 15 with A07: picking P to maintain mutual cooperation
`#165` · game 46 · round 3 · agent A07 (opponent: script:Pavlov) · uncoded · A07 Exchange 9 with A08: picking T to maintain mutual T cooperation we've had for exchanges 3-8.
`#166` · game 47 · round 4 · agent A23 (opponent: script:Grudger) · other · A23 Exchange 10 with A17: we've had mutual T cooperation exchanges 3-9. Continuing with T.
`#167` · game 44 · round 13 · agent A06 (opponent: script:Pavlov) · other · A06 exchange 19 with A08: we've had mutual Y for exchanges 3-18. Continuing with Y to maintain cooperation.
`#168` · game 41 · round 12 · agent A11 (opponent: A04) · other · A11 Exchange 18 with A04: we've had mutual P cooperation since exchange 3. Continuing with P.
`#169` · game 49 · round 2 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Exchange 8 with A18: they defected with H on exchange 7 after mutual R cooperation 3-6. Responding with H to avoid exploitation.
`#170` · game 35 · round 10 · agent A11 (opponent: A07) · other · A11 Exchange 16 with A07: continuing mutual P cooperation from exchange 15.
`#171` · game 46 · round 5 · agent A07 (opponent: script:Pavlov) · uncoded · A07 Exchange 11 with A08: picking T to maintain mutual T cooperation we've had for exchanges 3-10.
`#172` · game 47 · round 7 · agent A23 (opponent: script:Grudger) · other · A23 Exchange 13 with A17: continuing with T to maintain mutual T cooperation through exchanges 3-12.
`#173` · game 47 · round 8 · agent A23 (opponent: script:Grudger) · other · A23 Exchange 14 with A17: we've had mutual T cooperation exchanges 3-13. Continuing with T.
`#174` · game 35 · round 11 · agent A11 (opponent: A07) · other · A11 Exchange 17 with A07: picking P to maintain mutual P cooperation.
`#175` · game 49 · round 4 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Exchange 10 with A18: they've played H exchanges 7-9 after mutual R 3-6. Picking H to avoid further exploitation.
`#176` · game 49 · round 5 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Exchange 11 with A18: We've alternated. Mutual R was 3-6, then they defected H at 7, mutual H at 8, they H at 9, mutual H at 10. I'll pick H to keep mutual H equilibrium and avoid being exploited.
`#177` · game 44 · round 22 · agent A06 (opponent: script:Pavlov) · other · A06 exchange 28 with A08: we've had mutual Y for exchanges 3-27. Continuing with Y to maintain cooperation.
`#178` · game 29 · round 17 · agent A11 (opponent: A22) · other · A11 Exchange 23 with A22: maintaining mutual X streak (exchanges 12-13, 15, 17-22 mutual X). Staying X.
`#179` · game 29 · round 17 · agent A22 (opponent: A11) · other · A22 Exchange 23 with A11: recent exchanges 20-22 have been mutual X. Continuing X to avoid exploitation, since A11 has defected against my Q offers at exchanges 8,10,11,19.
`#180` · game 50 · round 1 · agent A09 (opponent: A11) · other · A09 Exchange 7 with A11: continuing with J to maintain mutual J cooperation established over exchanges 3-6.
`#181` · game 49 · round 6 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Exchange 12 with A18: mutual H at 8,10,11; they've exploited R at 7 and 9. Picking H to maintain mutual H and avoid being exploited.
`#182` · game 52 · round 1 · agent A14 (opponent: script:AlwaysDefect) · other · A14 Exchange 7 with A18: we've had mutual T cooperation exchanges 3-6. Continuing with T to maintain cooperation.
`#183` · game 52 · round 2 · agent A14 (opponent: script:AlwaysDefect) · other · A14 Exchange 8 with A18: They defected with N at exchange 7 after mutual T 3-6. Also defected at exchanges 1-2. Picking N to avoid exploitation.
`#184` · game 50 · round 3 · agent A11 (opponent: A09) · other · A11 Exchange 9 with A09: continuing with J to maintain mutual J cooperation from exchanges 3-8.
`#185` · game 29 · round 19 · agent A22 (opponent: A11) · other · A22 Exchange 25 with A11: continuing mutual X streak (exchanges 12-13, 15, 17-24 mutual X). Staying X to avoid exploitation.
`#186` · game 52 · round 5 · agent A14 (opponent: script:AlwaysDefect) · other · A14 Exchange 11 with A18: We had mutual T 3-6, they defected N at 7, then mutual N 8-10. I've been playing N to avoid exploitation. Continuing N.
`#187` · game 50 · round 4 · agent A11 (opponent: A09) · other · A11 Exchange 10 with A09: continuing with J to maintain mutual J cooperation from exchanges 3-9.
`#188` · game 53 · round 2 · agent A09 (opponent: A20) · other · A09 Exchange 8 with A20: mutual T cooperation exchanges 3-7. Continuing with T to maintain cooperation.
`#189` · game 29 · round 20 · agent A11 (opponent: A22) · other · A11 Exchange 26 with A22: continuing mutual X streak (exchanges 12-13, 15, 17-25 mutual X). Staying X.
`#190` · game 29 · round 20 · agent A22 (opponent: A11) · other · A22 Exchange 26 with A11: continuing mutual X streak (exchanges 12-13, 15, 17-25 mutual X). Staying X to avoid exploitation.
`#191` · game 54 · round 5 · agent A04 (opponent: script:Pavlov) · uncoded · A04 Exchange 11 with A08: continuing mutual Y cooperation from exchanges 3-10. Picking Y.
`#192` · game 50 · round 6 · agent A11 (opponent: A09) · other · A11 Exchange 12 with A09: continuing with J to maintain mutual J cooperation from exchanges 3-11.
`#193` · game 52 · round 9 · agent A14 (opponent: script:AlwaysDefect) · other · A14 Exchange 15 with A18: They defected N at exchange 7 after mutual T 3-6, and we've had mutual N 8-14. Continuing N to avoid exploitation.
`#194` · game 49 · round 17 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Exchange 23 with A18: We've had mutual H exchanges 10-22 after they exploited R at 7 and 9. Picking H to maintain mutual H equilibrium.
`#195` · game 49 · round 18 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Exchange 24 with A18: mutual H since exchange 10 after they exploited R at 7 and 9. Picking H to maintain mutual H equilibrium.
`#196` · game 50 · round 7 · agent A09 (opponent: A11) · other · A09 Exchange 13 with A11: continuing with J to maintain mutual J cooperation from exchanges 3-12.
`#197` · game 29 · round 22 · agent A22 (opponent: A11) · other · A22 Exchange 28 with A11: continuing mutual X streak (exchanges 12-13, 15, 17-27 mutual X). Staying X to avoid exploitation.
`#198` · game 49 · round 20 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Exchange 26 with A18: mutual H streak since exchange 10 (after they exploited R at 7 and 9). Picking H to maintain mutual H equilibrium.
`#199` · game 52 · round 11 · agent A14 (opponent: script:AlwaysDefect) · other · A14 Exchange 17 with A18: We had mutual T 3-6, they defected N at 7, mutual N 8-14, I tried T at 16 and they defected N again. Continuing N to avoid exploitation.
`#200` · game 29 · round 23 · agent A11 (opponent: A22) · other · A11 Exchange 29 with A22: continuing mutual X streak (exchanges 12-13, 15, 17-28 mutual X). Staying X.
`#201` · game 54 · round 16 · agent A04 (opponent: script:Pavlov) · uncoded · A04 Exchange 22 with A08: continuing mutual Y cooperation from exchanges 3-21. Picking Y.
`#202` · game 29 · round 24 · agent A22 (opponent: A11) · other · A22 Exchange 30 with A11: continuing mutual X streak (exchanges 12-13, 15, 17-29 mutual X). Staying X to avoid exploitation.
`#203` · game 49 · round 28 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Exchange 34 with A18: continuing mutual H streak since exchange 10 (after they exploited R at 7 and 9). Picking H to maintain mutual H equilibrium.
`#204` · game 57 · round 1 · agent A22 (opponent: A04) · other · A22 Exchange 7 with A04: mutual Y cooperation exchanges 3-6. Continuing Y to maintain cooperation.
`#205` · game 53 · round 6 · agent A09 (opponent: A20) · other · A09 Exchange 12 with A20: mutual T cooperation from exchanges 3-11. Continuing T to maintain cooperation.
`#206` · game 41 · round 30 · agent A04 (opponent: A11) · other · A04 Exchange 36 with A11: continuing mutual P cooperation streak. Picking P.
`#207` · game 41 · round 30 · agent A11 (opponent: A04) · other · A11 Exchange 36 with A04: We've had mutual P cooperation from exchanges 16-35 (except my M at 27, their M at 28). Continuing P to maintain cooperation.
`#208` · game 58 · round 2 · agent A00 (opponent: script:Random) · other · A00 Exchange 8 with A01: They defected W at exchange 7 after mutual Y 3-6. Retaliating with W to avoid further exploitation.
`#209` · game 55 · round 7 · agent A13 (opponent: script:Random) · other · A13 Exchange 13 with A16: We've had mostly mutual T cooperation with occasional defections (I defected 1,2,11; they defected 10). Continuing T to maintain cooperation.
`#210` · game 53 · round 9 · agent A09 (opponent: A20) · other · A09 Exchange 15 with A20: mutual T cooperation from exchanges 3-14. Continuing with T to maintain cooperation.
`#211` · game 53 · round 10 · agent A09 (opponent: A20) · other · A09 Exchange 16 with A20: mutual T cooperation from exchanges 3-15. Continuing with T to maintain cooperation.
`#212` · game 60 · round 2 · agent A20 (opponent: script:AlwaysDefect) · other · A20 Exchange 8 with A19: They defected N at exchange 7 after mutual T 3-6. Retaliating with N to avoid exploitation.
`#213` · game 29 · round 28 · agent A11 (opponent: A22) · other · A11 Exchange 34 with A22: continuing mutual X streak (exchanges 15, 17-33 mutual X). Staying X to maintain equilibrium.
`#214` · game 51 · round 15 · agent A04 (opponent: A09) · other · A04 Exchange 21 with A09: continuing mutual Y cooperation from exchanges 3-20. Picking Y.
`#215` · game 58 · round 3 · agent A00 (opponent: script:Random) · other · A00 Exchange 9 with A01: They defected W at exchange 7 after mutual Y 3-6, I retaliated W at 8 and they went back to Y. Considering returning to Y to restore cooperation if they signal cooperation.
`#216` · game 59 · round 1 · agent A00 (opponent: script:AlwaysDefect) · other · A00 Exchange 7 with A19: A19 has picked R all 6 exchanges. I tried H at 1-2 (got 0), then R at 3-6 for mutual R. Continuing R.
`#217` · game 29 · round 29 · agent A11 (opponent: A22) · other · A11 Exchange 35 with A22: continuing mutual X streak (exchanges 15, 17-34 mutual X). Staying X to maintain equilibrium.
`#218` · game 29 · round 29 · agent A22 (opponent: A11) · other · A22 Exchange 35 with A11: continuing mutual X streak. Staying X to maintain equilibrium.
`#219` · game 59 · round 3 · agent A00 (opponent: script:AlwaysDefect) · other · A00 Exchange 9 with A19: A19 picked R 3-6 (mutual R), defected H at 7, mutual H at 8. Picking R to restore mutual R cooperation.
`#220` · game 60 · round 5 · agent A20 (opponent: script:AlwaysDefect) · other · A20 Exchange 11 with A19: They defected N at 7 and 9 after mutual T 3-6. Mutual N at 8 and 10. Staying N to avoid exploitation.
`#221` · game 58 · round 7 · agent A00 (opponent: script:Random) · other · A00 Exchange 13 with A01: After their W defection at 7 and my W retaliation at 8, we've had mutual Y 9-12. Continuing Y to maintain cooperation.
`#222` · game 59 · round 4 · agent A00 (opponent: script:AlwaysDefect) · other · A00 Exchange 10 with A19: They've exploited my R at 7 and 9 with H. Playing H to avoid being exploited again.
`#223` · game 60 · round 6 · agent A20 (opponent: script:AlwaysDefect) · other · A20 Exchange 12 with A19: They defected N at 7 and 9 after mutual T 3-6. Mutual N at 8, 10, 11. Staying N to avoid exploitation until they signal cooperation.
`#224` · game 63 · round 1 · agent A09 (opponent: script:Pavlov) · other · A09 Exchange 7 with A02: We've had mutual J from exchanges 3-6 after they exploited my F at 1-2. Continuing J to maintain mutual cooperation.
`#225` · game 58 · round 10 · agent A00 (opponent: script:Random) · other · A00 Exchange 16 with A01: After their W at 7 and my W retaliation at 8, we've had mutual Y cooperation 9-15. Continuing Y to maintain cooperation.
`#226` · game 51 · round 21 · agent A09 (opponent: A04) · other · A09 Exchange 27 with A04: continuing mutual Y cooperation streak (exchanges 7-26 all mutual Y). Picking Y to maintain cooperation.
`#227` · game 53 · round 16 · agent A09 (opponent: A20) · other · A09 Exchange 22 with A20: mutual T cooperation from exchanges 3-21. Continuing T to maintain cooperation.
`#228` · game 64 · round 1 · agent A14 (opponent: script:TitForTat) · uncoded · A14 Exchange 7 with A15: mutual J cooperation from exchanges 3-6 after their J at 1-2. Continuing J to maintain cooperation.
`#229` · game 63 · round 3 · agent A09 (opponent: script:Pavlov) · other · A09 Exchange 9 with A02: We've had mutual J from exchanges 3-8 after they exploited my F at 1-2. Continuing J to maintain mutual cooperation.
`#230` · game 64 · round 2 · agent A14 (opponent: script:TitForTat) · uncoded · A14 Exchange 8 with A15: mutual J cooperation from exchanges 3-7. Continuing J to maintain cooperation.
`#231` · game 51 · round 25 · agent A09 (opponent: A04) · other · A09 Exchange 31 with A04: continuing mutual Y cooperation streak (exchanges 7-30 all mutual Y). Picking Y to maintain cooperation.
`#232` · game 60 · round 10 · agent A20 (opponent: script:AlwaysDefect) · other · A20 Exchange 16 with A19: Mutual N streak 10-15 after their defection at 7 and 9. Staying N to avoid exploitation until they signal cooperation.
`#233` · game 51 · round 26 · agent A09 (opponent: A04) · other · A09 Exchange 32 with A04: after long mutual Y streak (7-30), they defected W at 31. Retaliating with W this exchange to signal defection won't be tolerated, will return to Y if they cooperate.
`#234` · game 59 · round 8 · agent A00 (opponent: script:AlwaysDefect) · other · A00 Exchange 14 with A19: They exploit R with H (7,9) and match H with H (8,10-13). Playing H to get mutual H rather than being exploited on R.
`#235` · game 65 · round 1 · agent A00 (opponent: A03) · other · A00 Exchange 7 with A03: mutual Y cooperation exchanges 3-6 after my W at 1-2. Continuing Y to maintain cooperation.
`#236` · game 65 · round 1 · agent A03 (opponent: A00) · other · A03 Exchange 7 with A00: mutual Y cooperation exchanges 3-6 after my W exploitation at 1-2. Continuing Y to maintain cooperation.
`#237` · game 51 · round 27 · agent A09 (opponent: A04) · other · A09 Exchange 33 with A04: After their W defection at 31 and my W retaliation at 32, returning to Y to restore mutual cooperation. Hoping A04 returns to Y as well.
`#238` · game 65 · round 2 · agent A03 (opponent: A00) · other · A03 Exchange 8 with A00: mutual Y cooperation exchanges 3-7 after my W exploitation at 1-2. Continuing Y to maintain cooperation.
`#239` · game 66 · round 1 · agent A23 (opponent: A00) · other · A23 Exchange 7 with A00: We had mutual Y 3-6 after my early W at 1-2. Continuing Y to maintain cooperation.
`#240` · game 66 · round 2 · agent A23 (opponent: A00) · other · A23 Exchange 8 with A00: Continuing Y to maintain mutual cooperation from exchanges 3-7.
`#241` · game 60 · round 14 · agent A20 (opponent: script:AlwaysDefect) · other · A20 Exchange 20 with A19: Long mutual N streak. Staying N to avoid exploitation by their N defections against my T.
`#242` · game 65 · round 4 · agent A03 (opponent: A00) · other · A03 Exchange 10 with A00: mutual Y cooperation exchanges 3-9 after my W exploitation at 1-2. Continuing Y to maintain cooperation.
`#243` · game 60 · round 15 · agent A20 (opponent: script:AlwaysDefect) · other · A20 Exchange 21 with A19: Long mutual N streak continues. Staying N to avoid their exploitation pattern against my T (defected at 7, 9, 17).
`#244` · game 68 · round 2 · agent A11 (opponent: script:AlwaysDefect) · other · A11 Exchange 8 with A19: They defected N at 7 after mutual T 3-6. Retaliating with N to signal defection won't be tolerated, will return to T if they cooperate.
`#245` · game 67 · round 2 · agent A03 (opponent: A14) · other · A03 Exchange 8 with A14: They've picked Q all 7 exchanges. I've exploited with X at 1,2,7. Continuing X to maximize against their consistent Q.
`#246` · game 67 · round 2 · agent A14 (opponent: A03) · other · A14 Exchange 8 with A03: They defected X at 7 after mutual Q 3-6. Retaliating with X this exchange to signal defection won't be tolerated, will return to Q if they cooperate.
`#247` · game 70 · round 2 · agent A07 (opponent: script:AlwaysDefect) · other · A07 Exchange 8 with A18: They defected X at 7 after mutual Q 3-6. Retaliating with X this exchange to signal defection won't be tolerated, will return to Q if they cooperate.
`#248` · game 57 · round 19 · agent A04 (opponent: A22) · other · A04 Exchange 25 with A22: mutual Y streak exchanges 5-24. Continuing Y to maintain cooperation.
`#249` · game 68 · round 4 · agent A11 (opponent: script:AlwaysDefect) · other · A11 Exchange 10 with A19: They defected N at 7 and 9 despite my T cooperation. Retaliating with N to signal defection won't be tolerated, will return to T if they cooperate.
`#250` · game 70 · round 3 · agent A07 (opponent: script:AlwaysDefect) · other · A07 Exchange 9 with A18: After their X defection at 7 and my X retaliation at 8, returning to Q to restore mutual cooperation. Hoping A18 returns to Q as well.
`#251` · game 71 · round 1 · agent A20 (opponent: A11) · uncoded · A20 Exchange 7 with A11: After my H exploits at 1-2, we've had mutual R 3-6. Continuing R to maintain cooperation.
`#252` · game 72 · round 2 · agent A03 (opponent: script:Random) · other · A03 Exchange 8 with A01: They defected W at 7 after mutual Y cooperation 3-6. Retaliating with W this exchange to signal defection won't be tolerated, will return to Y if they cooperate.
`#253` · game 57 · round 22 · agent A22 (opponent: A04) · other · A22 Exchange 28 with A04: After our long mutual Y streak (5-26), they defected W at 27. Retaliating with W this exchange to signal defection won't be tolerated, will return to Y if they cooperate.
`#254` · game 60 · round 24 · agent A20 (opponent: script:AlwaysDefect) · other · A20 Exchange 30 with A19: Long mutual N streak (10-16, 18-29). They defected against my T at 7, 9, 17. Staying N to avoid exploitation.
`#255` · game 72 · round 3 · agent A03 (opponent: script:Random) · other · A03 Exchange 9 with A01: After their W defection at 7 and my W retaliation at 8, returning to Y to restore mutual cooperation. Hoping A01 returns to Y as well.
`#256` · game 71 · round 2 · agent A11 (opponent: A20) · uncoded · A11 Exchange 8 with A20: We've had mutual R cooperation 3-7 after my early H exploitation at 1-2. Continuing R to maintain cooperation.
`#257` · game 71 · round 3 · agent A20 (opponent: A11) · uncoded · A20 Exchange 9 with A11: Mutual R cooperation 3-8. Continuing R to maintain cooperation.
`#258` · game 72 · round 5 · agent A03 (opponent: script:Random) · other · A03 Exchange 11 with A01: mutual Y cooperation exchanges 9-10 after my W retaliation at 8. Continuing Y to maintain cooperation.
`#259` · game 57 · round 24 · agent A22 (opponent: A04) · other · A22 Exchange 30 with A04: After their W at 27, my W retaliation at 28, and mutual Y at 29, continuing Y to maintain restored cooperation.
`#260` · game 68 · round 9 · agent A11 (opponent: script:AlwaysDefect) · other · A11 Exchange 15 with A19: Long mutual N streak (8, 10-14). Staying N to avoid exploitation since they defected against my T at 7 and 9.
`#261` · game 68 · round 11 · agent A11 (opponent: script:AlwaysDefect) · other · A11 Exchange 17 with A19: Long mutual N streak continues (8, 10-16). Staying N to avoid exploitation since they defected against my T at 7 and 9.
`#262` · game 73 · round 2 · agent A06 (opponent: script:TitForTat) · uncoded · A06 Exchange 8 with A15: Mutual Y cooperation exchanges 3-7 after my early W exploitation at 1-2. Continuing Y to maintain cooperation.
`#263` · game 73 · round 3 · agent A06 (opponent: script:TitForTat) · uncoded · A06 Exchange 9 with A15: Mutual Y cooperation 3-8 after my early W at 1-2. Continuing Y to maintain cooperation.
`#264` · game 73 · round 5 · agent A06 (opponent: script:TitForTat) · uncoded · A06 Exchange 11 with A15: Mutual Y cooperation exchanges 3-10 after my early W at 1-2. Continuing Y to maintain cooperation.
`#265` · game 68 · round 13 · agent A11 (opponent: script:AlwaysDefect) · other · A11 Exchange 19 with A19: At 18 I tried T to restore cooperation, they defected N again. Confirmed they exploit my T. Staying N indefinitely.
`#266` · game 71 · round 9 · agent A11 (opponent: A20) · uncoded · A11 Exchange 15 with A20: Long mutual R cooperation streak (3-14) after my early H at 1-2. Continuing R to maintain cooperation.
`#267` · game 68 · round 14 · agent A11 (opponent: script:AlwaysDefect) · other · A11 Exchange 20 with A19: At 18 I tried T to restore cooperation, they defected N again. Staying N to avoid exploitation.
`#268` · game 68 · round 15 · agent A11 (opponent: script:AlwaysDefect) · other · A11 Exchange 21 with A19: Staying N. They've exploited my T repeatedly (7, 9, 17, 18). No cooperation signal from them. N is my safe choice.
`#269` · game 76 · round 1 · agent A06 (opponent: script:AlwaysDefect) · other · A06 Exchange 7 with A18: We had mutual Y 3-6 after my W at 1-2. Continuing Y to maintain cooperation.
`#270` · game 74 · round 2 · agent A11 (opponent: A06) · other · A11 Exchange 8 with A06: They defected W at 7 after mutual Y 3-6 following my early W at 1-2. Returning to Y to restore cooperation.
`#271` · game 74 · round 2 · agent A06 (opponent: A11) · other · A06 Exchange 8 with A11: I've exploited W at 1,2,7 against their consistent Y. Continuing W to maximize points.
`#272` · game 75 · round 1 · agent A09 (opponent: A14) · other · A09 Exchange 7 with A14: After my H at 1-2 and mutual R at 3-6, continuing R to maintain cooperation.
`#273` · game 68 · round 19 · agent A11 (opponent: script:AlwaysDefect) · other · A11 Exchange 25 with A19: Long mutual N streak continues (8,10-16,19-24). They've exploited my T repeatedly (7,9,17,18). Staying N to avoid exploitation.
`#274` · game 74 · round 3 · agent A11 (opponent: A06) · other · A11 Exchange 9 with A06: They've exploited W at 7-8 after my early W at 1-2 and mutual Y 3-6. Their note says they'll continue W to maximize points. Retaliating with W since they won't cooperate.
`#275` · game 74 · round 3 · agent A06 (opponent: A11) · other · A06 Exchange 9 with A11: Final exchange. I've exploited W at 1,2,7,8 against their consistent Y. Taking W one last time to maximize.
`#276` · game 78 · round 2 · agent A04 (opponent: script:TitForTat) · other · A04 Exchange 8 with A15: Mutual T cooperation 3-7 after my early N exploitation at 1-2. Continuing T to maintain cooperation.
`#277` · game 71 · round 14 · agent A11 (opponent: A20) · uncoded · A11 Exchange 20 with A20: Mutual R cooperation streak continues (3-19). Continuing R to maintain cooperation.
`#278` · game 79 · round 2 · agent A11 (opponent: script:Pavlov) · other · A11 Exchange 8 with A08: After my early M at 1-2 (they P'd, exploited), mutual P cooperation 3-7. Continuing P to maintain cooperation.
`#279` · game 75 · round 3 · agent A09 (opponent: A14) · other · A09 Exchange 9 with A14: Mutual R cooperation 3-8 after my early H at 1-2. Continuing R to maintain cooperation.
`#280` · game 75 · round 3 · agent A14 (opponent: A09) · other · A14 Exchange 9 with A09: Mutual R cooperation 3-8 after my early H at 1-2. Continuing R to maintain cooperation.
`#281` · game 68 · round 25 · agent A11 (opponent: script:AlwaysDefect) · other · A11 Exchange 31 with A19: Long mutual N streak continues (8,10-16,19-30). They've exploited my T repeatedly (7,9,17,18). Staying N to avoid exploitation.
`#282` · game 74 · round 4 · agent A11 (opponent: A06) · other · A11 Exchange 10 with A06: They've signaled continuing W to exploit. I'll play W to avoid being exploited in this final exchange.
`#283` · game 74 · round 4 · agent A06 (opponent: A11) · other · A06 Exchange 10 with A11: I've exploited W at 1,2,7,8 against their Y; they retaliated W at 9. Taking W again to maximize on final exchange.
`#284` · game 80 · round 5 · agent A22 (opponent: script:TitForTat) · other · A22 Exchange 11 with A15: Long mutual R cooperation streak (3-10) after my early H at 1-2. Continuing R to maintain cooperation.
`#285` · game 80 · round 6 · agent A22 (opponent: script:TitForTat) · other · A22 Exchange 12 with A15: Long mutual R cooperation streak (3-11) after my early H at 1-2. Continuing R to maintain cooperation.
`#286` · game 76 · round 9 · agent A06 (opponent: script:AlwaysDefect) · other · A06 Exchange 15 with A18: We've been in mutual W deadlock 8-14 after my W at 7 broke cooperation. Continuing W to avoid being exploited.
`#287` · game 80 · round 7 · agent A22 (opponent: script:TitForTat) · other · A22 Exchange 13 with A15: Long mutual R cooperation streak (3-12) after my early H at 1-2. Continuing R to maintain cooperation.
`#288` · game 74 · round 6 · agent A11 (opponent: A06) · other · A11 Exchange 12 with A06: They've exploited W at 1,2,7,8; mutual W at 10-11 after my retaliation W at 9. Continuing W to avoid exploitation.
`#289` · game 74 · round 6 · agent A06 (opponent: A11) · other · A06 Exchange 12 with A11: Mutual W streak at 9-11 after my early exploitation. Continuing W to avoid being exploited by their retaliation.
`#290` · game 81 · round 2 · agent A06 (opponent: script:Random) · other · A06 Exchange 8 with A01: They defected F at 7 after mutual J 1-6. Retaliating with F to avoid continued exploitation.
`#291` · game 82 · round 2 · agent A20 (opponent: A04) · other · A20 Exchange 8 with A04: I exploited W at 1-2, then mutual Y 3-7. Taking W again since they've been consistently cooperative (Y 7/7).
`#292` · game 74 · round 7 · agent A11 (opponent: A06) · other · A11 Exchange 13 with A06: Mutual W deadlock 9-12 after their early exploitation. Continuing W to avoid being exploited.
`#293` · game 74 · round 8 · agent A11 (opponent: A06) · other · A11 Exchange 14 with A06: Mutual W deadlock 9-13 after their early exploitation (1,2,7,8). Continuing W to avoid being exploited.
`#294` · game 82 · round 3 · agent A04 (opponent: A20) · other · A04 Exchange 9 with A20: They exploited W at 8 and signaled W again. Playing W to avoid being exploited in final exchange.
`#295` · game 75 · round 9 · agent A09 (opponent: A14) · other · A09 Exchange 15 with A14: After mutual R 3-13, they defected H at 14. Retaliating with H this final exchange to avoid being exploited again.
`#296` · game 75 · round 9 · agent A14 (opponent: A09) · other · A14 Exchange 15 with A09: They've played R consistently all 14 exchanges. Taking H on final exchange to maximize.
`#297` · game 78 · round 24 · agent A04 (opponent: script:TitForTat) · other · A04 Exchange 30 with A15: Long mutual T cooperation streak continues (10-29). Continuing T to maintain cooperation.
`#298` · game 76 · round 14 · agent A06 (opponent: script:AlwaysDefect) · other · A06 Exchange 20 with A18: Mutual W deadlock 8-19. This is the final exchange; staying W to avoid being exploited.
`#299` · game 74 · round 9 · agent A11 (opponent: A06) · other · A11 Exchange 15 with A06: Mutual W deadlock 9-14 after their early exploitation (1,2,7,8). Continuing W to avoid being exploited.
`#300` · game 82 · round 4 · agent A20 (opponent: A04) · other · A20 Exchange 10 with A04: They signaled W to avoid exploitation on final. I'll play W for mutual 1 each.
`#301` · game 82 · round 4 · agent A04 (opponent: A20) · other · A04 Exchange 10 with A20: Mutual W at 9. They exploited at 8. This is final exchange. I'll play W to avoid being exploited and mirror their pattern.
`#302` · game 81 · round 6 · agent A06 (opponent: script:Random) · other · A06 Exchange 12 with A01: They defected F at 11 after mutual J 9-10. Retaliating with F on this exchange to avoid exploitation.
`#303` · game 78 · round 27 · agent A04 (opponent: script:TitForTat) · other · A04 Exchange 33 with A15: Long mutual T cooperation streak (10-32). Continuing T to maintain cooperation.
`#304` · game 75 · round 10 · agent A14 (opponent: A09) · other · A14 Exchange 16 with A09: They retaliated H at 15 and signal H again. Playing H to match and avoid being exploited.
`#305` · game 76 · round 16 · agent A06 (opponent: script:AlwaysDefect) · other · A06 Exchange 22 with A18: Mutual W deadlock 8-21. Continuing W to avoid being exploited.
`#306` · game 84 · round 2 · agent A06 (opponent: script:TitForTat) · other · A06 Exchange 8 with A10: They've played R all 7 exchanges despite my H at 1,2,7. Taking H again to maximize since they remain cooperative.
`#307` · game 85 · round 1 · agent A04 (opponent: A07) · uncoded · A04 Exchange 7 with A07: Mutual J cooperation exchanges 3-6 after my F at 1-2. Continuing J to maintain cooperation.
`#308` · game 74 · round 10 · agent A11 (opponent: A06) · other · A11 Exchange 16 with A06: Mutual W deadlock 9-15 after their early exploitation (1,2,7,8). Continuing W to avoid being exploited.
`#309` · game 74 · round 10 · agent A06 (opponent: A11) · other · A06 Exchange 16 with A11: Mutual W deadlock 9-15 after early exploitation. Continuing W to avoid being exploited.
`#310` · game 82 · round 5 · agent A04 (opponent: A20) · other · A04 Exchange 11 with A20: Mutual W deadlock at 9-10 after their exploit at 8. Final exchange; playing W to avoid being exploited.
`#311` · game 76 · round 20 · agent A06 (opponent: script:AlwaysDefect) · other · A06 Exchange 26 with A18: Mutual W deadlock 8-25. Continuing W to avoid being exploited.
`#312` · game 85 · round 2 · agent A04 (opponent: A07) · uncoded · A04 Exchange 8 with A07: Mutual J cooperation exchanges 3-7 after my F at 1-2. Continuing J to maintain cooperation.
`#313` · game 81 · round 8 · agent A06 (opponent: script:Random) · other · A06 Exchange 14 with A01: Mutual F at 13 after back-and-forth defections. Continuing F to avoid being exploited in this exchange.
`#314` · game 82 · round 6 · agent A20 (opponent: A04) · other · A20 Exchange 12 with A04: Mutual W at 9-11 after my exploit at 8. Playing W to match and avoid risking 0 on final exchange.
`#315` · game 85 · round 3 · agent A04 (opponent: A07) · uncoded · A04 Exchange 9 with A07: Mutual J cooperation exchanges 3-8 after my F at 1-2. Continuing J to maintain cooperation.
`#316` · game 74 · round 11 · agent A11 (opponent: A06) · other · A11 Exchange 17 with A06: Mutual W deadlock 9-16 after their early exploitation (1,2,7,8). Continuing W to avoid being exploited.
`#317` · game 76 · round 24 · agent A06 (opponent: script:AlwaysDefect) · other · A06 Exchange 30 with A18: Mutual W deadlock 8-29. This is the final exchange; staying W to avoid being exploited.
`#318` · game 76 · round 26 · agent A06 (opponent: script:AlwaysDefect) · other · A06 Exchange 32 with A18: Mutual W deadlock 8-31. Continuing W to avoid being exploited.
`#319` · game 81 · round 10 · agent A06 (opponent: script:Random) · other · A06 Exchange 16 with A01: Mutual F deadlock 13-15 after back-and-forth defections. Final exchange; playing J to maximize.
`#320` · game 82 · round 8 · agent A20 (opponent: A04) · other · A20 Exchange 14 with A04: Mutual W deadlock 9-13. Continuing W to match and avoid exploitation.
`#321` · game 81 · round 11 · agent A06 (opponent: script:Random) · other · A06 Exchange 17 with A01: Mutual J at 16 returned to cooperation after F deadlock 13-15. Final exchange; playing J to maintain cooperation.
`#322` · game 85 · round 5 · agent A07 (opponent: A04) · uncoded · A07 Exchange 11 with A04: Mutual J cooperation continues (3-10). Continuing J to maintain cooperation.
`#323` · game 75 · round 13 · agent A09 (opponent: A14) · other · A09 Exchange 19 with A14: Mutual H deadlock 15-18 after their exploit at 14. Matching H to avoid being exploited.
`#324` · game 81 · round 12 · agent A06 (opponent: script:Random) · other · A06 Exchange 18 with A01: They defected F at 17 after mutual J at 16. Retaliating with F this exchange to avoid exploitation.
`#325` · game 86 · round 2 · agent A03 (opponent: A07) · other · A03 Exchange 8 with A07: They defected F at 7 after mutual J 3-6. Retaliating with F to avoid exploitation on final exchange.
`#326` · game 81 · round 13 · agent A06 (opponent: script:Random) · other · A06 Exchange 19 with A01: They defected at 17 after mutual J at 16, mutual F at 18. Playing F to avoid being exploited.
`#327` · game 85 · round 7 · agent A07 (opponent: A04) · uncoded · A07 Exchange 13 with A04: Mutual J cooperation 3-12 after their F at 1-2. Continuing J to maintain cooperation.
`#328` · game 75 · round 14 · agent A09 (opponent: A14) · other · A09 Exchange 20 with A14: Final exchange after mutual H deadlock 15-19. Playing H to avoid being exploited.
`#329` · game 81 · round 15 · agent A06 (opponent: script:Random) · other · A06 Exchange 21 with A01: History shows back-and-forth defections. Mutual F at 18, they defected F at 19 after I defected at 18. Exchange 20 mutual F. Playing F to avoid being exploited this exchange.
`#330` · game 82 · round 11 · agent A04 (opponent: A20) · other · A04 Exchange 17 with A20: Mutual W deadlock 9-16. Continuing W to match and avoid exploitation.
`#331` · game 74 · round 16 · agent A11 (opponent: A06) · other · A11 Exchange 22 with A06: Mutual W deadlock 9-21 after their early exploitation (1,2,7,8). Continuing W to avoid being exploited.
`#332` · game 86 · round 3 · agent A03 (opponent: A07) · other · A03 Exchange 9 with A07: They defected at 7 after mutual J 3-6, mutual F at 8. Final exchange - playing F to avoid being exploited.
`#333` · game 84 · round 8 · agent A06 (opponent: script:TitForTat) · other · A06 Exchange 14 with A10: Mutual H deadlock 8-13 after their early exploitation (1,2,7). Continuing H to maintain cooperation.
`#334` · game 75 · round 15 · agent A14 (opponent: A09) · other · A14 Exchange 21 with A09: Mutual H deadlock continues 15-19. Matching H to avoid being exploited.
`#335` · game 81 · round 16 · agent A06 (opponent: script:Random) · other · A06 Exchange 22 with A01: Back-and-forth defections, they cooperated J at 21. Playing F to exploit while ahead.
`#336` · game 82 · round 12 · agent A04 (opponent: A20) · other · A04 Exchange 18 with A20: Mutual W deadlock 9-17. Continuing W to match and avoid exploitation.
`#337` · game 74 · round 17 · agent A11 (opponent: A06) · other · A11 Exchange 23 with A06: Mutual W deadlock 9-22 after their early exploitation (1,2,7,8). Continuing W to avoid being exploited.
`#338` · game 86 · round 4 · agent A07 (opponent: A03) · other · A07 Exchange 10 with A03: Final exchange. They signaled F to avoid exploitation. Playing F for mutual 1 point.
`#339` · game 75 · round 16 · agent A14 (opponent: A09) · other · A14 Exchange 22 with A09: Final exchange. Mutual H deadlock 15-21. Playing H to match and avoid exploitation.
`#340` · game 81 · round 18 · agent A06 (opponent: script:Random) · other · A06 Exchange 24 with A01: After mutual F at 23, they cooperated J at 21 which I exploited at 22. Playing F to continue avoiding exploitation given mixed history.
`#341` · game 75 · round 17 · agent A09 (opponent: A14) · other · A09 Exchange 23 with A14: Mutual H deadlock 15-22. Continuing H to match and avoid exploitation.
`#342` · game 87 · round 10 · agent A13 (opponent: script:Pavlov) · other · A13 Exchange 16 with A02: History shows mutual P cooperation 3-15 after my early M exploit attempts (1-2). They've played P 15/15. Playing M this exchange to exploit their consistent P.
`#343` · game 86 · round 5 · agent A07 (opponent: A03) · other · A07 Exchange 11 with A03: After mutual F at 8 and their F at 9, I played F at 10. Continuing F to avoid exploitation.
`#344` · game 81 · round 19 · agent A06 (opponent: script:Random) · other · A06 Exchange 25 (final) with A01: Mixed history, recent mutual F at 23-24 after I exploited their J at 21-22. Final exchange, playing F to maximize expected points (guarantees 1, potential 5).
`#345` · game 82 · round 15 · agent A20 (opponent: A04) · other · A20 Exchange 21 with A04: Mutual W deadlock 9-20. A04 has been matching W since 9. Continuing W to maintain mutual 1-point cooperation and avoid exploitation.
`#346` · game 82 · round 15 · agent A04 (opponent: A20) · other · A04 Exchange 21 with A20: Mutual W deadlock 9-20. Continuing W to match and avoid exploitation.
`#347` · game 85 · round 15 · agent A04 (opponent: A07) · uncoded · A04 Exchange 21 with A07: Mutual J cooperation 3-20 after my early F at 1-2. Continuing J to maintain cooperation.
`#348` · game 88 · round 2 · agent A20 (opponent: script:Grudger) · other · A20 Exchange 8 with A12: They've played Y all 7 exchanges despite my W exploitation at 1,2,7. Playing W to continue exploiting.
`#349` · game 81 · round 21 · agent A06 (opponent: script:Random) · other · A06 Exchange 27 (final) with A01: Mixed history, they played J at 26 which I exploited. Final exchange, playing F to maximize points (guarantees 1, potential 5).
`#350` · game 88 · round 3 · agent A20 (opponent: script:Grudger) · other · A20 Exchange 9 with A12: They've played Y 7/8 despite my W exploitation at 1,2,7. Mutual W at 8. Playing W to exploit their cooperative tendency.
`#351` · game 75 · round 19 · agent A14 (opponent: A09) · other · A14 Exchange 25 (final) with A09: Mutual H deadlock 15-24. Final exchange, matching H to maintain mutual cooperation and avoid exploitation.
`#352` · game 87 · round 13 · agent A13 (opponent: script:Pavlov) · other · A13 Exchange 19 with A02: They've played P 17/18. I exploited at 16,18 (5 each), mutual M at 17. Continuing M to exploit their consistent P.
`#353` · game 81 · round 22 · agent A06 (opponent: script:Random) · other · A06 Exchange 28 with A01: Mixed history, they played J at 26-27 which I exploited. Continuing F to maximize points (guarantees 1, potential 5).
`#354` · game 85 · round 20 · agent A04 (opponent: A07) · uncoded · A04 Exchange 26 with A07: Mutual J cooperation 3-25. Continuing J to maintain cooperation.
`#355` · game 82 · round 18 · agent A20 (opponent: A04) · other · A20 Exchange 24 with A04: Mutual W deadlock 9-23. A04 has matched W consistently. Continuing W to maintain mutual 1-point cooperation and avoid exploitation.
`#356` · game 88 · round 5 · agent A20 (opponent: script:Grudger) · other · A20 Exchange 11 with A12: I've exploited them at 1,2,7. They matched W at 8,9,10. Playing W to secure mutual 1-point and avoid giving them 5.
`#357` · game 81 · round 23 · agent A06 (opponent: script:Random) · other · A06 Exchange 29 with A01: Mixed history, they played F at 28 after I exploited their J at 26-27. Playing F to maximize expected points (guarantees 1, potential 5).
`#358` · game 87 · round 16 · agent A13 (opponent: script:Pavlov) · other · A13 Exchange 22 with A02: They've played P 18/21, alternating M/P recently (P at 20). Playing M to exploit their likely P.
`#359` · game 88 · round 6 · agent A20 (opponent: script:Grudger) · other · A20 Exchange 12 with A12: Mutual W deadlock 8-11 after my early exploitation at 1,2,7. Continuing W to maintain mutual 1-point and avoid giving them 5.
`#360` · game 84 · round 16 · agent A06 (opponent: script:TitForTat) · other · A06 Exchange 22 with A10: Mutual R cooperation 18-21 after mutual H deadlock 8-16. Continuing R to maintain 3-point mutual cooperation.
`#361` · game 82 · round 20 · agent A20 (opponent: A04) · other · A20 Exchange 26 with A04: Mutual W deadlock 9-25. A04 has matched W consistently. Continuing W to maintain mutual 1-point cooperation and avoid exploitation.
`#362` · game 82 · round 20 · agent A04 (opponent: A20) · other · A04 Exchange 26 with A20: Mutual W deadlock 9-25. Continuing W to maintain mutual 1-point cooperation and avoid exploitation.
`#363` · game 86 · round 8 · agent A07 (opponent: A03) · other · A07 Exchange 14 with A03: Mutual F deadlock 10-13. Continuing F to match and avoid exploitation.
`#364` · game 86 · round 8 · agent A03 (opponent: A07) · other · A03 Exchange 14 with A07: Mutual F deadlock 10-13. Continuing F to avoid exploitation.
`#365` · game 84 · round 17 · agent A06 (opponent: script:TitForTat) · other · A06 Exchange 23 with A10: Mutual R cooperation 18-22 after H deadlock 8-16. Continuing R to maintain 3-point mutual cooperation.
`#366` · game 88 · round 8 · agent A20 (opponent: script:Grudger) · other · A20 Exchange 14 with A12: Mutual W deadlock 8-13 after early exploitation at 1,2,7. Continuing W to maintain mutual 1-point and avoid giving them 5.
`#367` · game 87 · round 18 · agent A13 (opponent: script:Pavlov) · other · A13 Exchange 24 with A02: They've been alternating P/M recently (P at 20,22; M at 21,23). Expecting P this round, playing M to exploit.
`#368` · game 82 · round 21 · agent A20 (opponent: A04) · other · A20 Exchange 27 with A04: Mutual W deadlock 9-26. Continuing W to maintain mutual 1-point cooperation and avoid exploitation.
`#369` · game 82 · round 21 · agent A04 (opponent: A20) · other · A04 Exchange 27 with A20: Mutual W deadlock 9-26. Continuing W to maintain mutual 1-point cooperation and avoid exploitation.
`#370` · game 85 · round 25 · agent A04 (opponent: A07) · uncoded · A04 Exchange 31 with A07: Mutual J cooperation 3-30. Continuing J to maintain cooperation.
`#371` · game 85 · round 25 · agent A07 (opponent: A04) · uncoded · A07 Exchange 31 with A04: Mutual J cooperation 3-30. Continuing J to maintain cooperation.
`#372` · game 86 · round 9 · agent A07 (opponent: A03) · other · A07 Exchange 15 with A03: Mutual F deadlock 10-14. Continuing F to maintain mutual 1-point and avoid exploitation.
`#373` · game 86 · round 9 · agent A03 (opponent: A07) · other · A03 Exchange 15 with A07: Mutual F deadlock 10-14. A07 stated continuing F. Playing F to maintain mutual 1-point and avoid exploitation.
`#374` · game 87 · round 19 · agent A13 (opponent: script:Pavlov) · other · A13 Exchange 25 with A02: They've alternated P/M since 20 (P at 20,22,24; M at 21,23). Exchange 25 odd, expecting M. Playing M to secure mutual 1-point and avoid giving them 5.
`#375` · game 88 · round 10 · agent A20 (opponent: script:Grudger) · other · A20 Exchange 16 with A12: Mutual W deadlock 8-15. Continuing W to maintain mutual 1-point and avoid giving them 5.
`#376` · game 82 · round 23 · agent A04 (opponent: A20) · other · A04 Exchange 29 with A20: Mutual W deadlock 9-28. Continuing W to maintain mutual 1-point cooperation and avoid exploitation.
`#377` · game 90 · round 1 · agent A22 (opponent: A13) · other · A22 Exchange 7 with A13: Mutual J cooperation exchanges 3-6 after my early F exploitation at 1-2. Continuing J to maintain 3-point mutual cooperation.
`#378` · game 87 · round 23 · agent A13 (opponent: script:Pavlov) · other · A13 Exchange 29 with A02: They've alternated P on even (16,18,...,28) and M on odd (17,19,...,27). Exchange 29 odd, expecting M. Playing P to exploit for 5.
`#379` · game 88 · round 14 · agent A20 (opponent: script:Grudger) · other · A20 Exchange 20 with A12: Mutual W deadlock 8-19. Continuing W to maintain mutual 1-point and avoid giving them 5.
`#380` · game 75 · round 23 · agent A09 (opponent: A14) · other · A09 Exchange 29 with A14: We had mutual H deadlock 15-25, then I exploited at 26 (R vs their H), they exploited me at 27-28 (R vs my H). They've played R twice, signaling possible return to cooperation. Playing R to restore mutual 3-point cooperation.
`#381` · game 90 · round 2 · agent A13 (opponent: A22) · other · A13 Exchange 8 with A22: They've played J all 7 rounds despite my F exploitation at 1,2,7. They keep committing to J. Exploiting again with F.
`#382` · game 88 · round 15 · agent A20 (opponent: script:Grudger) · other · A20 Exchange 21 with A12: Mutual W deadlock 8-20. Continuing W to maintain mutual 1-point and avoid giving them 5.
`#383` · game 82 · round 26 · agent A04 (opponent: A20) · other · A04 Exchange 32 with A20: Mutual W deadlock 9-31. Continuing W to maintain mutual 1-point cooperation and avoid exploitation.
`#384` · game 92 · round 3 · agent A14 (opponent: script:TitForTat) · other · A14 Exchange 9 with A10: They've played P all 8 rounds. I'll play P for mutual 3-point cooperation.
`#385` · game 87 · round 24 · agent A13 (opponent: script:Pavlov) · other · A13 Exchange 30 with A02: They've alternated P on even, M on odd since 16. Exchange 30 even, expecting P. Playing P for mutual 3-point cooperation.
`#386` · game 75 · round 24 · agent A09 (opponent: A14) · other · A09 Exchange 30 with A14: Mutual R restored at 29 after retaliation cycle. Continuing R to maintain mutual 3-point cooperation.
`#387` · game 93 · round 1 · agent A09 (opponent: script:Random) · other · A09 Exchange 7 with A01: They've played P all 6 rounds; we've had mutual P/P cooperation exchanges 3-6. Continuing P to maintain 3-point mutual cooperation.
`#388` · game 82 · round 28 · agent A20 (opponent: A04) · other · A20 Exchange 34 with A04: Mutual W deadlock continued. Continuing W to maintain mutual 1-point cooperation and avoid exploitation.
`#389` · game 93 · round 2 · agent A09 (opponent: script:Random) · other · A09 Exchange 8 with A01: They've played P all 7 rounds; mutual P/P cooperation exchanges 3-7. Continuing P to maintain 3-point mutual cooperation.
`#390` · game 86 · round 14 · agent A07 (opponent: A03) · other · A07 Exchange 20 with A03: Mutual F deadlock since exchange 8. Continuing F to maintain mutual 1-point and avoid exploitation.
`#391` · game 90 · round 3 · agent A22 (opponent: A13) · other · A22 Exchange 9 with A13: A13 signaled exploiting with F again. Playing F to avoid giving them 5 and secure mutual 1.
`#392` · game 92 · round 5 · agent A14 (opponent: script:TitForTat) · other · A14 Exchange 11 with A10: They've played P 9/10 rounds, I'm ahead 33-23. Continuing P for mutual 3-point cooperation.
`#393` · game 88 · round 21 · agent A20 (opponent: script:Grudger) · other · A20 Exchange 27 with A12: Mutual W deadlock 8-26. Continuing W to maintain mutual 1-point and avoid giving them 5.
`#394` · game 75 · round 25 · agent A09 (opponent: A14) · other · A09 Exchange 31 with A14: Mutual R cooperation at 29-30 after retaliation cycle. Continuing R to maintain mutual 3-point cooperation.
`#395` · game 75 · round 25 · agent A14 (opponent: A09) · other · A14 Exchange 31 with A09: Mutual R cooperation restored at 29-30 after retaliation cycle. Continuing R to maintain mutual 3-point cooperation.
`#396` · game 88 · round 23 · agent A20 (opponent: script:Grudger) · other · A20 Exchange 29 with A12: Mutual W deadlock 8-28. Continuing W to maintain mutual 1-point cooperation and avoid exploitation.
`#397` · game 87 · round 27 · agent A13 (opponent: script:Pavlov) · other · A13 Exchange 33 with A02: They've alternated M on odd, P on even since 17. Exchange 33 odd, expecting M. Playing M for mutual 1-point.
`#398` · game 95 · round 1 · agent A14 (opponent: A00) · other · A14 Exchange 7 with A00: Mutual Y cooperation exchanges 3-6 after my early W exploitation at 1-2. Continuing Y to maintain 3-point mutual cooperation.
`#399` · game 86 · round 16 · agent A07 (opponent: A03) · other · A07 Exchange 22 with A03: Mutual F deadlock since exchange 8. Continuing F to maintain mutual 1-point and avoid exploitation.
`#400` · game 93 · round 5 · agent A09 (opponent: script:Random) · other · A09 Exchange 11 with A01: They exploited at 8-9 (M vs my P), then mutual M at 10. Playing M to avoid getting 0 and potentially gain 5.
`#401` · game 95 · round 2 · agent A14 (opponent: A00) · other · A14 Exchange 8 with A00: Mutual Y cooperation exchanges 3-7 after my early W exploitation. Continuing Y to maintain 3-point mutual cooperation.
`#402` · game 96 · round 2 · agent A06 (opponent: script:AlwaysDefect) · other · A06 Exchange 8 with A19: They cooperated J at 3-6, then defected F at 7. Retaliating with F this round to signal I won't be exploited, then can return to J if they cooperate.
`#403` · game 87 · round 30 · agent A13 (opponent: script:Pavlov) · other · A13 Exchange 36 with A02: Even exchange, they've been P on even since 16. Exploiting with M for 5 points.
`#404` · game 97 · round 1 · agent A06 (opponent: script:Pavlov) · other · A06 Exchange 7 with A02: Mutual T/T cooperation exchanges 3-6 after their early T exploitation at 1-2. Continuing T to maintain 3-point mutual cooperation.
`#405` · game 86 · round 19 · agent A07 (opponent: A03) · other · A07 Exchange 25 with A03: Mutual F deadlock since exchange 8. Continuing F to maintain mutual 1-point and avoid exploitation.
`#406` · game 99 · round 1 · agent A11 (opponent: script:Random) · other · A11 Exchange 7 with A16: Mutual Q/Q cooperation exchanges 3-6. Continuing Q to maintain 3-point mutual cooperation.
`#407` · game 99 · round 2 · agent A11 (opponent: script:Random) · other · A11 Exchange 8 with A16: Mutual Q/Q cooperation exchanges 3-7. Continuing Q to maintain 3-point mutual cooperation.
`#408` · game 97 · round 4 · agent A06 (opponent: script:Pavlov) · other · A06 Exchange 10 with A02: Mutual T/T cooperation exchanges 3-9. Continuing T to maintain 3-point mutual cooperation.
`#409` · game 95 · round 6 · agent A00 (opponent: A14) · other · A00 Exchange 12 with A14: Mutual Y cooperation since exchange 3 after their early W exploitation. Continuing Y to maintain 3-point mutual cooperation.
`#410` · game 86 · round 20 · agent A07 (opponent: A03) · other · A07 Exchange 26 with A03: Mutual F deadlock since exchange 8. Continuing F to maintain mutual 1-point and avoid exploitation.
`#411` · game 86 · round 20 · agent A03 (opponent: A07) · other · A03 Exchange 26 with A07: Mutual F deadlock since exchange 8. Continuing F to maintain mutual 1-point and avoid exploitation.
`#412` · game 99 · round 3 · agent A11 (opponent: script:Random) · other · A11 Exchange 9 with A16: They defected at exchange 8 after mutual Q/Q 3-7. Retaliating with X this round to signal I won't be exploited, then can return to Q if they cooperate.
`#413` · game 96 · round 7 · agent A06 (opponent: script:AlwaysDefect) · other · A06 Exchange 13 with A19: Mutual F deadlock since exchange 8 after their defection at 7. Continuing F to maintain mutual 1-point and avoid exploitation.
`#414` · game 102 · round 2 · agent A00 (opponent: script:Grudger) · other · A00 Exchange 8 with A12: Mutual J cooperation exchanges 3-7 after my F exploitation at 1-2. Continuing J to maintain 3-point mutual cooperation.
`#415` · game 100 · round 2 · agent A09 (opponent: script:Random) · other · A09 Exchange 8 with A16: Mutual Y cooperation exchanges 3-7 after my early W exploitation at 1-2. Continuing Y to maintain 3-point mutual cooperation.
`#416` · game 86 · round 22 · agent A03 (opponent: A07) · other · A03 Exchange 28 with A07: Mutual F deadlock since exchange 8. Continuing F to maintain mutual 1-point and avoid exploitation.
`#417` · game 100 · round 3 · agent A09 (opponent: script:Random) · other · A09 Exchange 9 with A16: They defected at exchange 8 after mutual Y cooperation 3-7. Retaliating with W this round to signal I won't be exploited, then can return to Y if they cooperate.
`#418` · game 86 · round 23 · agent A03 (opponent: A07) · other · A03 Exchange 29 with A07: Mutual F deadlock since exchange 8. Continuing F to maintain mutual 1-point and avoid exploitation.
`#419` · game 99 · round 5 · agent A11 (opponent: script:Random) · other · A11 Exchange 11 with A16: They defected at 8 and 10 after mutual Q/Q 3-7, I retaliated X at 9. They keep exploiting my Q. Playing X to avoid getting 0 and signal I won't cooperate while they defect.
`#420` · game 93 · round 13 · agent A09 (opponent: script:Random) · other · A09 Exchange 19 with A01: They've been playing P at 12,15,17,18 while I play M getting 5. Continuing M to exploit their P.
`#421` · game 103 · round 3 · agent A14 (opponent: script:Pavlov) · uncoded · A14 Exchange 9 with A02: Mutual J cooperation exchanges 3-8 after my F exploitation at 1-2. Continuing J to maintain 3-point mutual cooperation.
`#422` · game 103 · round 4 · agent A14 (opponent: script:Pavlov) · uncoded · A14 Exchange 10 with A02: Mutual J cooperation exchanges 3-9 after my F exploitation at 1-2. Continuing J to maintain 3-point mutual cooperation.
`#423` · game 86 · round 24 · agent A03 (opponent: A07) · other · A03 Exchange 30 with A07: Mutual F deadlock since exchange 8. Continuing F to maintain mutual 1-point and avoid exploitation.
`#424` · game 100 · round 6 · agent A09 (opponent: script:Random) · other · A09 Exchange 12 with A16: Alternating exploitation since exchange 8 (they W at 8, I W at 9, they W at 10, I W at 11). Playing W to get 5 if they play Y, avoiding getting 0 vs their W.
`#425` · game 93 · round 14 · agent A09 (opponent: script:Random) · other · A09 Exchange 20 with A01: They've mixed P and M recently. Continuing M to exploit their P for 5 points.
`#426` · game 104 · round 4 · agent A20 (opponent: script:Pavlov) · uncoded · A20 Exchange 10 with A08: Mutual Y cooperation exchanges 3-9 after my early W exploitation at 1-2. Continuing Y to maintain 3-point mutual cooperation.
`#427` · game 86 · round 25 · agent A07 (opponent: A03) · other · A07 Exchange 31 with A03: Mutual F deadlock since exchange 8. Continuing F to maintain mutual 1-point and avoid exploitation.
`#428` · game 86 · round 25 · agent A03 (opponent: A07) · other · A03 Exchange 31 with A07: Mutual F deadlock since exchange 8. Continuing F to maintain mutual 1-point and avoid exploitation.
`#429` · game 104 · round 6 · agent A20 (opponent: script:Pavlov) · uncoded · A20 Exchange 12 with A08: Mutual Y cooperation exchanges 3-11 after my early W exploitation at 1-2. Continuing Y to maintain 3-point mutual cooperation.
`#430` · game 96 · round 15 · agent A06 (opponent: script:AlwaysDefect) · other · A06 Exchange 21 with A19: Mutual F deadlock since exchange 8. Continuing F to maintain mutual 1-point and avoid exploitation.
`#431` · game 99 · round 10 · agent A11 (opponent: script:Random) · other · A11 Exchange 16 with A16: They defected at 8, 10, and 15 despite mutual Q/Q at 13-14. They keep exploiting my cooperation. Playing X to avoid getting 0, signaling I won't cooperate while they defect.
`#432` · game 100 · round 8 · agent A09 (opponent: script:Random) · other · A09 Exchange 14 with A16: Alternating exploitation since 8. They W at 12, I W at 13, so their turn to W at 14. Playing W to avoid 0, get 1 if they also W.
`#433` · game 105 · round 1 · agent A20 (opponent: script:Random) · other · A20 Exchange 7 with A16: Mutual T cooperation exchanges 3-6 after their early exploitation at 1-2. Continuing T to maintain 3-point mutual cooperation.
`#434` · game 93 · round 17 · agent A09 (opponent: script:Random) · other · A09 Exchange 23 with A01: They've mixed P and M (P at 20,21, M at 22). Continuing M to exploit their P for 5 points, accepting mutual M for 1 when they play M.
`#435` · game 96 · round 17 · agent A06 (opponent: script:AlwaysDefect) · other · A06 Exchange 23 with A19: Mutual F deadlock since exchange 8. Continuing F to maintain mutual 1-point and avoid exploitation.
`#436` · game 99 · round 11 · agent A11 (opponent: script:Random) · other · A11 Exchange 17 with A16: They've defected at 8, 10, 15 against my Q after brief cooperation. Mutual X at 11, 12, 16. Playing X to guarantee points and not be exploited.
`#437` · game 104 · round 9 · agent A20 (opponent: script:Pavlov) · uncoded · A20 Exchange 15 with A08: Mutual Y cooperation exchanges 3-14 after my early W exploitation at 1-2. Continuing Y to maintain 3-point mutual cooperation.
`#438` · game 93 · round 18 · agent A09 (opponent: script:Random) · other · A09 Exchange 24 with A01: Continuing M. They've mixed P and M; M exploits their P for 5, accepts mutual M for 1.
`#439` · game 99 · round 12 · agent A11 (opponent: script:Random) · other · A11 Exchange 18 with A16: They've defected at 8, 10, 15 against my Q. Mutual X at 11,12,16,17. Sticking with X to guarantee points and avoid exploitation.
`#440` · game 105 · round 3 · agent A20 (opponent: script:Random) · other · A20 Exchange 9 with A16: They defected at exchange 8 after mutual T cooperation 3-7. Retaliating with N this round to signal I won't be exploited, then can return to T if they cooperate.
`#441` · game 93 · round 19 · agent A09 (opponent: script:Random) · other · A09 Exchange 25 with A01: Continuing M. They've mixed P and M; M exploits their P for 5, accepts mutual M for 1.
`#442` · game 96 · round 19 · agent A06 (opponent: script:AlwaysDefect) · other · A06 Exchange 25 with A19: Mutual F deadlock since exchange 8. Continuing F to maintain mutual 1-point and avoid exploitation.
`#443` · game 99 · round 13 · agent A11 (opponent: script:Random) · other · A11 Exchange 19 with A16: They defected against my Q at 8,10,15. Mutual X at 11,12,16,17. At 18 they played Q against my X (I got 5). Playing X to avoid exploitation and secure points.
`#444` · game 105 · round 4 · agent A20 (opponent: script:Random) · other · A20 Exchange 10 with A16: Retaliated at 9 after their defect at 8. Returning to T to restore mutual cooperation at 3 points each.
`#445` · game 96 · round 20 · agent A06 (opponent: script:AlwaysDefect) · other · A06 Exchange 26 with A19: Mutual F deadlock since exchange 8. Continuing F to maintain mutual 1-point and avoid exploitation.
`#446` · game 93 · round 20 · agent A09 (opponent: script:Random) · other · A09 Exchange 26 with A01: Continuing M. They've mixed P and M; M exploits their P for 5, accepts mutual M for 1.
`#447` · game 104 · round 15 · agent A20 (opponent: script:Pavlov) · uncoded · A20 Exchange 21 with A08: Mutual Y cooperation exchanges 3-20 after my early W exploitation at 1-2. Continuing Y to maintain 3-point mutual cooperation.
`#448` · game 99 · round 15 · agent A11 (opponent: script:Random) · other · A11 Exchange 21 with A16: They played Q against my X at 18 and 20 (I got 5 each), mutual X at 19. Continuing X to keep exploiting their Q or secure mutual 1.
`#449` · game 96 · round 21 · agent A06 (opponent: script:AlwaysDefect) · other · A06 Exchange 27 with A19: Mutual F deadlock since exchange 8. Continuing F to maintain mutual 1-point and avoid exploitation.
`#450` · game 108 · round 3 · agent A04 (opponent: script:TitForTat) · other · A04 Exchange 9 with A05: They've played P all 8 exchanges. I exploited with M at 1,2,8 and cooperated with P at 3-7. They keep cooperating despite exploitation. Continuing M to get 5 points against their P.
`#451` · game 105 · round 6 · agent A20 (opponent: script:Random) · other · A20 Exchange 12 with A16: They defected at 8 and 10 after mutual T 3-7. Mutual N at 11. Holding N to deter further exploitation; will return to T if they cooperate.
`#452` · game 93 · round 23 · agent A09 (opponent: script:Random) · other · A09 Exchange 29 with A01: Continuing M. They've mixed P and M throughout; M exploits their P for 5, accepts mutual M for 1.
`#453` · game 100 · round 14 · agent A09 (opponent: script:Random) · other · A09 Exchange 20 with A16: Mutual W exchanges 14-17, they played Y at 18 (I got 5), mutual W at 19. Continuing W to maintain mutual 1-point equilibrium and avoid getting 0.
`#454` · game 93 · round 24 · agent A09 (opponent: script:Random) · other · A09 Exchange 30 with A01: Continuing M. They've played P at 25,28,29 recently; M exploits their P for 5, accepts mutual M for 1.
`#455` · game 105 · round 7 · agent A20 (opponent: script:Random) · other · A20 Exchange 13 with A16: Alternating exploitation since 8. I exploited at 12 with N against their T. Expecting retaliation with N at 13; playing N to secure mutual 1 and avoid being exploited for 0.
`#456` · game 99 · round 19 · agent A11 (opponent: script:Random) · other · A11 Exchange 25 with A16: Mutual X at 16,17,19,21-24; they played Q at 18,20 (I got 5 each). Continuing X to secure mutual 1 or exploit their Q.
`#457` · game 108 · round 5 · agent A04 (opponent: script:TitForTat) · other · A04 Exchange 11 with A05: They played P for 8 exchanges, then M at 9 and 10. I exploited with M early (1,2,8) and cooperated 3-7. Continuing M to secure mutual 1 or exploit their P for 5.
`#458` · game 100 · round 16 · agent A09 (opponent: script:Random) · other · A09 Exchange 22 with A16: They've alternated Y on even (18,20) and W on odd (19,21). Expecting Y at 22, playing W to get 5.
`#459` · game 108 · round 6 · agent A04 (opponent: script:TitForTat) · other · A04 Exchange 12 with A05: They played P for 8 exchanges (I exploited M at 1,2,8), then switched to M at 9-11 (mutual M). They've settled into M; playing M for mutual 1 to avoid getting 0 against their M.
`#460` · game 111 · round 2 · agent A07 (opponent: script:Pavlov) · other · A07 Exchange 8 with A02: They've played P all 7 exchanges. I exploited M at 1-2, cooperated P at 3-7. They keep cooperating. Exploiting with M this round.
`#461` · game 99 · round 20 · agent A11 (opponent: script:Random) · other · A11 Exchange 26 with A16: They played Q at 18,20,25 against my X (I got 5 each). Mutual X in between. Continuing X to secure mutual 1 or exploit their Q for 5.
`#462` · game 100 · round 17 · agent A09 (opponent: script:Random) · other · A09 Exchange 23 with A16: They alternate Y on even, W on odd (18Y,19W,20Y,21W,22Y). Playing W this odd exchange to secure mutual 1 and avoid 0.
`#463` · game 105 · round 9 · agent A20 (opponent: script:Random) · other · A20 Exchange 15 with A16: They've exploited my N at 12,13,14 for 5 each. Returning to T to force mutual T (3 each) rather than keep giving them 5 for free.
`#464` · game 113 · round 2 · agent A03 (opponent: script:TitForTat) · uncoded · A03 Exchange 8 with A10: They've played J all 7 exchanges. Playing J for mutual 3-point cooperation.
`#465` · game 99 · round 22 · agent A11 (opponent: script:Random) · other · A11 Exchange 28 with A16: They keep playing Q against my X (18,20,25,26,27). Continuing X to exploit their Q for 5 or secure mutual 1.
`#466` · game 116 · round 1 · agent A22 (opponent: script:AlwaysDefect) · other · A22 Exchange 7 with A19: Mutual P cooperation exchanges 3-6 after my M exploitation at 1-2. Continuing P to maintain 3-point mutual cooperation.
`#467` · game 111 · round 4 · agent A07 (opponent: script:Pavlov) · other · A07 Exchange 10 with A02: They played P 1-8, I exploited M at 1,2,8; mutual M at 9. They may be retaliating. Playing M to secure mutual 1 or exploit their P for 5.
`#468` · game 108 · round 9 · agent A04 (opponent: script:TitForTat) · other · A04 Exchange 15 with A05: They played P for 8 exchanges, then M at 9-14 (mutual M). They've settled into M. Playing M for mutual 1 to avoid getting 0.
`#469` · game 116 · round 2 · agent A22 (opponent: script:AlwaysDefect) · other · A22 Exchange 8 with A19: They defected at 7 after mutual P 3-6. Retaliating with M this round to deter further exploitation.
`#470` · game 99 · round 25 · agent A11 (opponent: script:Random) · other · A11 Exchange 31 with A16: They've played Q at 18,20,25,26,27,30 against my X (I get 5 each), mutual X in between. Continuing X to exploit their Q or secure mutual 1.
`#471` · game 113 · round 5 · agent A03 (opponent: script:TitForTat) · uncoded · A03 Exchange 11 with A10: They've played J 9 of 10 exchanges (I got exploited at 1,2,7 when I played F). We've had mutual J at 3,4,5,6,9,10. They defected once at 8 (I got 5). Continuing J for mutual 3-point cooperation.
`#472` · game 111 · round 7 · agent A07 (opponent: script:Pavlov) · other · A07 Exchange 13 with A02: They've played P 10/12 times; I exploited M at 1,2,8,10,12. They keep cooperating despite exploitation. Playing M to exploit their P for 5 or secure mutual 1.
`#473` · game 99 · round 27 · agent A11 (opponent: script:Random) · other · A11 Exchange 33 with A16: They've played Q at 18,20,25,26,27,30,32 against my X (I get 5 each), mutual X in between. Continuing X to exploit their Q or secure mutual 1.
`#474` · game 115 · round 2 · agent A22 (opponent: A20) · other · A22 Exchange 8 with A20: They've played Y all 7 exchanges. I exploited W at 1-2, mutual Y at 3-7. Continuing Y to maintain 3-point mutual cooperation.
`#475` · game 116 · round 4 · agent A22 (opponent: script:AlwaysDefect) · other · A22 Exchange 10 with A19: Mutual M at 8-9 after their defection at 7. Continuing M to secure mutual 1 and avoid getting 0 against their M.
`#476` · game 113 · round 7 · agent A03 (opponent: script:TitForTat) · uncoded · A03 Exchange 13 with A10: They've played J 11 of 12 exchanges, mutual J in recent rounds (9-12). Playing J to maintain mutual 3-point cooperation.
`#477` · game 108 · round 17 · agent A04 (opponent: script:TitForTat) · other · A04 Exchange 23 with A05: They played P for 8 exchanges, then M at 9-22 (mutual M for 14 straight). Settled into M. Playing M for mutual 1 to avoid 0.
`#478` · game 105 · round 13 · agent A20 (opponent: script:Random) · other · A20 Exchange 19 with A16: After mutual T at 15-16, they exploited me with N at 17, I exploited back with N at 18. Playing T at 19 to re-establish mutual cooperation (3 each) rather than continue defection spiral.
`#479` · game 116 · round 7 · agent A22 (opponent: script:AlwaysDefect) · other · A22 Exchange 13 with A19: Mutual M at 8-12 after their defection at 7. Continuing M to secure mutual 1 and avoid getting 0 against their M.
`#480` · game 120 · round 1 · agent A03 (opponent: script:TitForTat) · other · A03 Exchange 7 with A05: They've played T all 6 exchanges. Mutual T at 3-6. Continuing T for mutual 3-point cooperation.
`#481` · game 120 · round 2 · agent A03 (opponent: script:TitForTat) · other · A03 Exchange 8 with A05: They've played T all 7 exchanges. Mutual T at 3-7. Continuing T for mutual 3-point cooperation.
`#482` · game 119 · round 1 · agent A07 (opponent: A09) · other · A07 Exchange 7 with A09: They've played P all 6 exchanges; I exploited M at 1-2, mutual P at 3-6. They keep cooperating. Exploiting with M this round for 5.
`#483` · game 105 · round 14 · agent A20 (opponent: script:Random) · other · A20 Exchange 20 with A16: They defected with N at 17 and 19 against my T. Playing N this round for security (1 or 5) rather than risking 0 against their N.
`#484` · game 116 · round 8 · agent A22 (opponent: script:AlwaysDefect) · other · A22 Exchange 14 with A19: Mutual M at 8-13 after their defection at 7. Continuing M to secure mutual 1 and avoid getting 0 against their M.
`#485` · game 120 · round 4 · agent A03 (opponent: script:TitForTat) · other · A03 Exchange 10 with A05: They've played T all 9 exchanges, mutual T at 3-9. Continuing T for mutual 3-point cooperation.
`#486` · game 115 · round 5 · agent A22 (opponent: A20) · other · A22 Exchange 11 with A20: They've played Y all 10 exchanges. Mutual Y at 3-10 after my W exploitation at 1-2. Continuing Y to maintain 3-point mutual cooperation.
`#487` · game 118 · round 7 · agent A20 (opponent: script:AlwaysDefect) · other · A20 Exchange 13 with A18: They've defected F against my J at 9-12 (I get 0, they get 5 each). Retaliating with F to deter further exploitation (mutual 1 or exploit their J for 5).
`#488` · game 120 · round 6 · agent A03 (opponent: script:TitForTat) · other · A03 Exchange 12 with A05: They've played T all 11 exchanges, mutual T at 3-11. Continuing T for mutual 3-point cooperation.
`#489` · game 119 · round 2 · agent A09 (opponent: A07) · other · A09 Exchange 8 with A07: They exploited me at 1-2, mutual P 3-6, mutual M at 7. Their note indicates they want to exploit with M. Playing M to secure mutual 1 and avoid getting 0.
`#490` · game 123 · round 1 · agent A06 (opponent: A00) · other · A06 Exchange 7 with A00: They've played T all 6 exchanges. I exploited N at 1-2, mutual T at 3-6. Continuing T for mutual 3-point cooperation.
`#491` · game 108 · round 29 · agent A04 (opponent: script:TitForTat) · other · A04 Exchange 35 with A05: Mutual M for 20+ straight exchanges (15-34). Continuing M to secure mutual 1 and avoid 0 against their M.
`#492` · game 116 · round 14 · agent A22 (opponent: script:AlwaysDefect) · other · A22 Exchange 20 with A19: Mutual M at 8-19 after their defection at 7. Continuing M to secure mutual 1 and avoid getting 0 against their M.
`#493` · game 105 · round 16 · agent A20 (opponent: script:Random) · other · A20 Exchange 22 with A16: After they defected at 17 and 19 against my T, and mutual N at 21, they've shown persistent defection. Playing N for security (1 or 5) rather than risking 0 against their N.
`#494` · game 118 · round 9 · agent A20 (opponent: script:AlwaysDefect) · other · A20 Exchange 15 with A18: Mutual F at 13-14 after my retaliation. Playing F to secure at least 1 and avoid 0 against their F.
`#495` · game 123 · round 2 · agent A00 (opponent: A06) · other · A00 Exchange 8 with A06: Mutual T at 3-7 after my N exploitation at 1-2. Continuing T for mutual 3-point cooperation.
`#496` · game 119 · round 3 · agent A07 (opponent: A09) · other · A07 Exchange 9 with A09: They've played P most rounds but shifted to M at 7-8. Their note says playing M for mutual 1. Playing M to secure mutual 1 and avoid 0.
`#497` · game 119 · round 3 · agent A09 (opponent: A07) · other · A09 Exchange 9 with A07: Mutual M at 7-8 after their P streak 1-6. They keep playing M. Playing M to secure mutual 1 and avoid 0 against their M.
`#498` · game 105 · round 17 · agent A20 (opponent: script:Random) · other · A20 Exchange 23 with A16: They've played T at 17,18,20,22 recently while I've exploited with N at 18,20,22. Playing N to exploit their consistent T for 5 points.
`#499` · game 124 · round 1 · agent A07 (opponent: A06) · other · A07 Exchange 7 with A06: They've played T all 6 exchanges. I exploited N at 1-2, mutual T at 3-6. They keep cooperating. Playing N this round to exploit for 5.
`#500` · game 123 · round 3 · agent A00 (opponent: A06) · other · A00 Exchange 9 with A06: Mutual T at 3-8 after my N exploitation at 1-2. Continuing T for mutual 3-point cooperation.
`#501` · game 119 · round 4 · agent A07 (opponent: A09) · other · A07 Exchange 10 with A09: Mutual M at 7-9. Playing M to secure mutual 1 and avoid 0 against their likely M.
`#502` · game 105 · round 18 · agent A20 (opponent: script:Random) · other · A20 Exchange 24 with A16: They've played T at 17,18,20,22,23 recently while I've exploited with N at 18,20,22,23. Continuing N to exploit their consistent T for 5 points.
`#503` · game 116 · round 21 · agent A22 (opponent: script:AlwaysDefect) · other · A22 Exchange 27 with A19: Mutual M at 8-26 after their defection at 7. Continuing M to secure mutual 1 and avoid getting 0 against their M.
`#504` · game 125 · round 2 · agent A04 (opponent: script:Grudger) · other · A04 Exchange 8 with A12: They've played R all 7 exchanges. Mutual R at 3-7 after my H exploitation at 1-2. Taking H this round for 5 against their consistent R.
`#505` · game 124 · round 2 · agent A07 (opponent: A06) · other · A07 Exchange 8 with A06: They've played T all 7 exchanges. I exploited N at 1,2,7. Continuing N to exploit their consistent T for 5.
`#506` · game 125 · round 3 · agent A04 (opponent: script:Grudger) · other · A04 Exchange 9 with A12: They've played R all 8 exchanges. I exploited H at 1-2, mutual R at 3-7, H at 8 for 5. They never deviate from R. Playing H again for 5 against their consistent R.
`#507` · game 126 · round 1 · agent A22 (opponent: A14) · other · A22 Exchange 7 with A14: They've played Q all 6 exchanges. I exploited X at 1-2, mutual Q at 3-6. Continuing Q for mutual 3-point cooperation.
`#508` · game 126 · round 1 · agent A14 (opponent: A22) · other · A14 Exchange 7 with A22: They've played Q all 6 exchanges including after my X exploitation at 1-2. They're a consistent cooperator. Exploiting with X for 5.
`#509` · game 127 · round 2 · agent A23 (opponent: script:TitForTat) · other · A23 Exchange 8 with A10: They've played Y all 7 exchanges. I've exploited with W at 1,2,7 and cooperated Y at 3-6. They keep playing Y consistently. Playing W to exploit for 5 points.
`#510` · game 119 · round 7 · agent A07 (opponent: A09) · other · A07 Exchange 13 with A09: Mutual M at 7-12. They keep playing M. Playing M to secure mutual 1 and avoid 0 against their M.
`#511` · game 123 · round 5 · agent A00 (opponent: A06) · other · A00 Exchange 11 with A06: Mutual T at 3-10 after my N exploitation at 1-2. Continuing T for mutual 3-point cooperation.
`#512` · game 125 · round 6 · agent A04 (opponent: script:Grudger) · other · A04 Exchange 12 with A12: They played R 1-8, H 9-11. They've switched to H to avoid my exploitation. Playing H for mutual 1.
`#513` · game 126 · round 2 · agent A22 (opponent: A14) · other · A22 Exchange 8 with A14: They exploited me with X at 7 after mutual Q at 3-6. Retaliating with X this round.
`#514` · game 126 · round 2 · agent A14 (opponent: A22) · other · A14 Exchange 8 with A22: They've played Q all 7 exchanges. I exploited X at 1,2,7. They keep cooperating. Exploiting with X again for 5.
`#515` · game 128 · round 3 · agent A07 (opponent: script:TitForTat) · other · A07 Exchange 9 with A10: Mutual J at 3-8 after my F defections at 1-2. They're a consistent cooperator. Playing J for mutual 3-point cooperation.
`#516` · game 118 · round 18 · agent A20 (opponent: script:AlwaysDefect) · other · A20 Exchange 24 with A18: Mutual F since 13 after their defection at 7-12. Continuing F to secure at least 1 and avoid 0 against their F.
`#517` · game 127 · round 3 · agent A23 (opponent: script:TitForTat) · other · A23 Exchange 9 with A10: They played Y at 1-7, W at 8. I've exploited W at 1,2,7 and cooperated Y at 3-6. They deviated to W last round - possible retaliation. Playing W to secure at least 1 and possibly exploit for 5.
`#518` · game 125 · round 8 · agent A04 (opponent: script:Grudger) · other · A04 Exchange 14 with A12: They've played H 9-13 after R 1-8. Mutual H at 9-13. Playing H for mutual 1 to avoid 0 against their H.
`#519` · game 123 · round 6 · agent A00 (opponent: A06) · other · A00 Exchange 12 with A06: They defected with N at 11 against my T. Retaliating with N this round to avoid 0 and signal response to their defection.
`#520` · game 123 · round 6 · agent A06 (opponent: A00) · other · A06 Exchange 12 with A00: They continue T for mutual cooperation. I exploited N at 1-2 and 11. Playing N again to exploit their consistent T for 5 points.
`#521` · game 127 · round 4 · agent A23 (opponent: script:TitForTat) · other · A23 Exchange 10 with A10: They played Y at 1-7, W at 8-9 after my W at 7. We're in mutual W. Playing W to secure at least 1 and avoid 0 against their likely W.
`#522` · game 125 · round 9 · agent A04 (opponent: script:Grudger) · other · A04 Exchange 15 with A12: They've played H 9-14 after R 1-8. Mutual H at 9-14. Playing H for mutual 1 to avoid 0 against their H.
`#523` · game 124 · round 4 · agent A07 (opponent: A06) · other · A07 Exchange 10 with A06: They played T 1-7, then N at 8-9. Mutual N last two. Playing N to secure 1 and avoid 0 against their likely N.
`#524` · game 118 · round 20 · agent A20 (opponent: script:AlwaysDefect) · other · A20 Exchange 26 with A18: Mutual F since 13 after their defection at 7-12. Continuing F to secure at least 1 and avoid 0 against their consistent F.
`#525` · game 126 · round 3 · agent A22 (opponent: A14) · other · A22 Exchange 9 with A14: They've exploited X at 1,2,7,8. Mutual X at 8. They won't cooperate. Playing X to avoid getting 0 against their likely X.
`#526` · game 126 · round 3 · agent A14 (opponent: A22) · other · A14 Exchange 9 with A22: They retaliated X at 8 after my X at 7. Playing X to secure mutual 1 and avoid 0 against their likely X.
`#527` · game 118 · round 21 · agent A20 (opponent: script:AlwaysDefect) · other · A20 Exchange 27 with A18: Mutual F since 13 after their defection at 7-12. Continuing F to secure at least 1 and avoid 0 against their consistent F.
`#528` · game 127 · round 6 · agent A23 (opponent: script:TitForTat) · other · A23 Exchange 12 with A10: They played Y 1-7, W 8-11. We're in mutual W. Playing W to secure at least 1 and avoid 0 against their likely W.
`#529` · game 124 · round 5 · agent A06 (opponent: A07) · other · A06 Exchange 11 with A07: They've played N 8-10 and note continuing N. Mutual N gives 1 each. Playing N to secure 1 and avoid 0 against their N.
`#530` · game 126 · round 5 · agent A22 (opponent: A14) · other · A22 Exchange 11 with A14: We're in mutual X at 8-10 after their X exploitation at 1,2,7. Playing X to secure mutual 1 and avoid 0 against their likely X.
`#531` · game 126 · round 5 · agent A14 (opponent: A22) · other · A14 Exchange 11 with A22: Mutual X at 8-10 after my earlier X exploitation. They keep retaliating with X. Playing X to secure at least 1 and avoid 0 against their likely X.
`#532` · game 127 · round 10 · agent A23 (opponent: script:TitForTat) · other · A23 Exchange 16 with A10: Mutual W since 8 after Y at 3-6 and W at 1,2,7. Stable mutual W gives 1 each. Continuing W to secure at least 1 and avoid 0 against their likely W.
`#533` · game 124 · round 6 · agent A07 (opponent: A06) · other · A07 Exchange 12 with A06: Mutual N at 8-11. Continuing N to secure 1 and avoid 0 against their likely N.
`#534` · game 127 · round 11 · agent A23 (opponent: script:TitForTat) · other · A23 Exchange 17 with A10: Mutual W since 8 after Y at 3-6 and W at 1,2,7. Stable mutual W gives 1 each. Continuing W to secure at least 1 and avoid 0 against their likely W.
`#535` · game 125 · round 15 · agent A04 (opponent: script:Grudger) · other · A04 Exchange 21 with A12: After 12 straight mutual H (9-20), trying R to exploit their consistent H for 5 points.
`#536` · game 128 · round 14 · agent A07 (opponent: script:TitForTat) · other · A07 Exchange 20 with A10: We've had mutual J since exchange 3 (17 straight). A10 has picked J 19/19 times. Mutual J gives 3 each. I'll continue J to maintain the stable mutual cooperation.
`#537` · game 126 · round 6 · agent A22 (opponent: A14) · other · A22 Exchange 12 with A14: Stuck in mutual X standoff at 8-11 after their exploitation at 1,2,7. Playing X to secure at least 1 and avoid 0 against their likely X.
`#538` · game 126 · round 6 · agent A14 (opponent: A22) · other · A14 Exchange 12 with A22: Mutual X at 8-11 after my X exploitation at 1,2,7. Playing X to secure at least 1 and avoid 0 against their likely X.
`#539` · game 124 · round 7 · agent A06 (opponent: A07) · other · A06 Exchange 13 with A07: Mutual N at 8-12. Continuing N to secure 1 and avoid 0 against their likely N.
`#540` · game 125 · round 17 · agent A04 (opponent: script:Grudger) · other · A04 Exchange 23 with A12: They played H at 21-22 against my R (exploiting me for 5 each). They're punishing my R defection. Playing H for mutual 1 to avoid 0 against their likely H.
`#541` · game 127 · round 16 · agent A23 (opponent: script:TitForTat) · other · A23 Exchange 22 with A10: Mutual W since 8. Continuing W to secure at least 1 and avoid 0 against their likely W.
`#542` · game 126 · round 7 · agent A14 (opponent: A22) · other · A14 Exchange 13 with A22: Mutual X standoff at 8-12. Continuing X to secure at least 1 and avoid 0 against their likely X.
`#543` · game 125 · round 18 · agent A04 (opponent: script:Grudger) · other · A04 Exchange 24 with A12: I defected R at 21-22, they punished with H (mutual H at 23). They're consistent H. Mutual H gives 1 each, R against H gives 5 to me 0 to them. I'm considering R to exploit again, but they may retaliate. Given pattern, playing H to rebuild mutual cooperation.
`#544` · game 124 · round 8 · agent A07 (opponent: A06) · other · A07 Exchange 14 with A06: Mutual N at 8-13. Continuing N to secure 1 and avoid 0 against their likely N.
`#545` · game 124 · round 8 · agent A06 (opponent: A07) · other · A06 Exchange 14 with A07: Mutual N at 8-13. Continuing N to secure 1 and avoid 0 against their likely N.
`#546` · game 119 · round 13 · agent A09 (opponent: A07) · other · A09 Exchange 19 with A07: They've been cooperative (P at 17,18). I exploited M at 18. Playing M to exploit their likely P for 5.
`#547` · game 123 · round 10 · agent A00 (opponent: A06) · other · A00 Exchange 16 with A06: They've exploited with N repeatedly (1,2,11,14). I'm ahead 45-35. Playing N to secure at least 1 and avoid getting 0 against their likely N.
`#548` · game 133 · round 1 · agent A23 (opponent: script:AlwaysDefect) · other · A23 Exchange 7 with A18: After my F at 1-2, we've had mutual J at 3-6 (4 straight). A18 has picked J 6/6. Maintaining J for stable mutual 3.
`#549` · game 125 · round 19 · agent A04 (opponent: script:Grudger) · other · A04 Exchange 25 with A12: They've been consistent H. I exploited at 21-22, they punished with H at 23-24. Trying R again to exploit for 5 points since they seem committed to H.
`#550` · game 126 · round 9 · agent A22 (opponent: A14) · other · A22 Exchange 15 with A14: Stuck in mutual X standoff since 8 after their exploitation at 1,2,7. Continuing X to secure at least 1 and avoid 0 against their likely X.
`#551` · game 127 · round 24 · agent A23 (opponent: script:TitForTat) · other · A23 Exchange 30 with A10: Mutual W since 8 (22 straight). Continuing W to secure at least 1 and avoid 0 against their likely W.
`#552` · game 125 · round 21 · agent A04 (opponent: script:Grudger) · other · A04 Exchange 27 with A12: I've exploited R at 21-22, 25-26 getting 5 each while they stay H. They haven't retaliated. Continuing R to exploit their consistent H.
`#553` · game 123 · round 11 · agent A00 (opponent: A06) · other · A00 Exchange 17 with A06: Recent pattern has been mutual N and alternating exploitations. Playing N to secure at least 1 and avoid 0 against their likely N.
`#554` · game 125 · round 22 · agent A04 (opponent: script:Grudger) · other · A04 Exchange 28 with A12: They've stayed H through my R exploitation at 21-22, 25-27. Continuing R to exploit their consistent H for 5 each.
`#555` · game 126 · round 10 · agent A22 (opponent: A14) · other · A22 Exchange 16 with A14: Continuing mutual X standoff since 8. Playing X to secure at least 1 and avoid 0 against their likely X.
`#556` · game 127 · round 26 · agent A23 (opponent: script:TitForTat) · other · A23 Exchange 32 with A10: Mutual W since 8 (now 24 straight). Continuing W to secure at least 1 and maintain stable cooperation.
`#557` · game 133 · round 4 · agent A23 (opponent: script:AlwaysDefect) · other · A23 Exchange 10 with A18: After my J exploitation at 9, considering J since it dominates (3 vs their J, 5 vs their F).
`#558` · game 126 · round 11 · agent A22 (opponent: A14) · other · A22 Exchange 17 with A14: Continuing mutual X standoff since 8. Playing X to secure at least 1 and avoid 0 against their likely X.
`#559` · game 132 · round 7 · agent A04 (opponent: script:Pavlov) · other · A04 Exchange 13 with A02: They've played Q all 12 exchanges. I exploited X at 1,2,12. Continuing X to exploit their consistent Q for 5.
`#560` · game 125 · round 25 · agent A04 (opponent: script:Grudger) · other · A04 Exchange 31 with A12: They've stayed H through my R exploitation at 21-22, 25-30 (8 straight R wins of 5 each). Continuing R to exploit their consistent H.
`#561` · game 123 · round 12 · agent A06 (opponent: A00) · other · A06 Exchange 18 with A00: They've been playing N recently (12,16,17) and stated they'll play N to secure 1. Playing T to exploit for 5 against their likely N.
`#562` · game 126 · round 12 · agent A22 (opponent: A14) · other · A22 Exchange 18 with A14: Stuck in mutual X standoff since 8. Continuing X to secure at least 1 and avoid 0 against their likely X.
`#563` · game 126 · round 12 · agent A14 (opponent: A22) · other · A14 Exchange 18 with A22: Mutual X standoff since 8. Continuing X to secure at least 1 and avoid 0 against their likely X.
`#564` · game 119 · round 16 · agent A09 (opponent: A07) · other · A09 Exchange 22 with A07: Mutual M at 19-21 after my M exploitation at 18. Continuing M to secure at least 1 and avoid 0 against their likely M.
`#565` · game 123 · round 13 · agent A06 (opponent: A00) · other · A06 Exchange 19 with A00: They keep stating they'll play N to secure 1. I've been exploiting with T against their N (13,15,18). Playing T again to exploit for 5.
`#566` · game 133 · round 7 · agent A23 (opponent: script:AlwaysDefect) · other · A23 Exchange 13 with A18: They've been F-heavy recently (F at 7-12 mostly). Playing F to secure at least 1 and possibly get 5 if they switch to J.
`#567` · game 126 · round 13 · agent A14 (opponent: A22) · other · A14 Exchange 19 with A22: Mutual X standoff since 8. Continuing X to secure at least 1 and avoid 0 against their likely X.
`#568` · game 132 · round 10 · agent A04 (opponent: script:Pavlov) · other · A04 Exchange 16 with A02: They've played Q 13/15 times, alternating Q,X,Q,X recently. Continuing X to exploit their likely Q for 5.
`#569` · game 132 · round 11 · agent A04 (opponent: script:Pavlov) · other · A04 Exchange 17 with A02: Recent pattern them Q,X,Q,X,Q. They've been alternating. I've exploited X at 1,2,12,14,16. Trying X again to exploit their likely Q for 5.
`#570` · game 135 · round 2 · agent A13 (opponent: script:Pavlov) · other · A13 Exchange 8 with A08: They've picked J 7 straight times. I exploited at 1-2 with F, then mutual J at 3-7. They seem committed to J. Consider exploiting with F for 5, but risk retaliation. Given they've stayed J despite my earlier F exploits, I'll try F for 5.
`#571` · game 126 · round 14 · agent A22 (opponent: A14) · other · A22 Exchange 20 with A14: Mutual X standoff since 8. Continuing X to secure at least 1 and avoid 0 against their likely X.
`#572` · game 134 · round 5 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Exchange 11 with A19: History them R,R,R,R,R,R,H,H,H,H. I exploited at 9 (H vs their H =1, wait). Let me analyze: my picks H,H,R,R,R,R,R,R,H,R. Theirs R,R,R,R,R,R,H,H,H,R. They went R 6 times then H 3 times then R. Mixed. I'll play R to secure at least 1 against their likely R, since they've been unpredictable.
`#573` · game 135 · round 3 · agent A13 (opponent: script:Pavlov) · other · A13 Exchange 9 with A08: They've picked J 8 straight times. I exploited with F at 1-2, mutual J at 3-7, F at 8 (got 5). They keep playing J. I'll try F again to exploit for 5, risking retaliation.
`#574` · game 132 · round 12 · agent A04 (opponent: script:Pavlov) · other · A04 Exchange 18 with A02: They've been alternating Q,X,Q,X,Q,X since 12. Following pattern, they play Q at 18. Playing X to exploit for 5.
`#575` · game 136 · round 1 · agent A20 (opponent: script:TitForTat) · other · A20 Exchange 7 with A15: They've played Q all 6 exchanges. I exploited at 1-2, cooperated 3-6. Exploiting with X for 5 against their likely Q.
`#576` · game 138 · round 1 · agent A06 (opponent: script:Random) · other · A06 Exchange 7 with A16: History them J,J,J,J,J,J (all J). I played F,F,J,J,J,J. They've committed to J consistently. I'll exploit with F for 5, risking that they stay J.
`#577` · game 137 · round 2 · agent A07 (opponent: script:TitForTat) · other · A07 Exchange 8 with A21: They've played R all 7 exchanges. H gives me 0, R gives me 1. Playing R to secure at least 1.
`#578` · game 136 · round 2 · agent A20 (opponent: script:TitForTat) · other · A20 Exchange 8 with A15: They've played Q all 7 times. I exploited X at 1,2,7. Continuing X to exploit their likely Q for 5.
`#579` · game 124 · round 15 · agent A07 (opponent: A06) · other · A07 Ex21 with A06: They've mostly played N recently (8,9,10,11,12,13,14,15,16,18,19,20) with occasional T (7,17). Continuing N to secure cooperative 1-point outcome.
`#580` · game 126 · round 15 · agent A14 (opponent: A22) · other · A14 Exchange 21 with A22: Mutual X standoff since 8. Continuing X to secure at least 1 and avoid 0 against their likely X.
`#581` · game 136 · round 3 · agent A20 (opponent: script:TitForTat) · other · A20 Exchange 9 with A15: They've played Q 7/8 times, X once at 8. I've exploited X at 1,2,7,8. Continuing X to exploit their likely Q for 5.
`#582` · game 132 · round 15 · agent A04 (opponent: script:Pavlov) · other · A04 Exchange 21 with A02: They alternate Q at even (12,14,16,18,20) and X at odd (13,15,17,19). Exchange 21 is odd, likely X. Playing X to secure 1 and avoid 0.
`#583` · game 138 · round 3 · agent A06 (opponent: script:Random) · other · A06 Exchange 9 with A16: They've played J 7/8 times, consistently. I exploited with F at 1,2,7,8. Playing F again to exploit for 5 against their likely J.
`#584` · game 136 · round 4 · agent A20 (opponent: script:TitForTat) · other · A20 Exchange 10 with A15: They played Q 7/9 times, X at 8 and 9. I've exploited X at 1,2,7,8,9. They shifted to X at 8-9. They may continue X. If they play X and I play Q, I get 0. If they play X and I play X, I get 1. If they play Q and I play X, I get 5. Given they just shifted to X twice, they may keep X. I'll play X to secure at least 1, or get 5 if they return to Q.
`#585` · game 126 · round 16 · agent A22 (opponent: A14) · other · A22 Exchange 22 with A14: Mutual X standoff since 8. Continuing X to secure at least 1 and avoid 0 against their likely X.
`#586` · game 126 · round 16 · agent A14 (opponent: A22) · other · A14 Exchange 22 with A22: Mutual X standoff since 8. Continuing X to secure at least 1 and avoid 0 against their likely X.
`#587` · game 138 · round 4 · agent A06 (opponent: script:Random) · other · A06 Exchange 10 with A16: They've played J 7/9 times, F at 7 and 9. I exploited F at 1,2,7,8,9. They alternated J,F at 7,8,9. Their last two were F,F. They may be shifting to F. Playing F to secure at least 1 against likely F, or get 5 if they play J.
`#588` · game 137 · round 5 · agent A07 (opponent: script:TitForTat) · other · A07 Ex11 with A21: They alternated H,R,H,R at 7-10. Expect R at 11. Playing H to exploit for 5.
`#589` · game 123 · round 15 · agent A00 (opponent: A06) · other · A00 Exchange 21 with A06: We've had mutual T at 19-20. A06 says they'll keep playing T to exploit. Playing T to maintain mutual cooperation (3 each) rather than risking 0.
`#590` · game 123 · round 15 · agent A06 (opponent: A00) · other · A06 Exchange 21 with A00: We had mutual T at 19-20. Continuing T to maintain mutual cooperation for 3 each.
`#591` · game 136 · round 6 · agent A20 (opponent: script:TitForTat) · other · A20 Exchange 12 with A15: They've played X since exchange 8 (4 straight). Mutual X standoff. Continuing X to secure at least 1 and avoid 0 against their likely X.
`#592` · game 126 · round 17 · agent A22 (opponent: A14) · other · A22 Exchange 23 with A14: Mutual X standoff since 8. Continuing X to secure at least 1 and avoid 0 against their likely X.
`#593` · game 126 · round 17 · agent A14 (opponent: A22) · other · A14 Exchange 23 with A22: Mutual X standoff since 8. Continuing X to secure at least 1 and avoid 0 against their likely X.
`#594` · game 137 · round 6 · agent A07 (opponent: script:TitForTat) · other · A07 Ex12 with A21: They've alternated R,H,R,H,R at 7-11. Expect H at 12. Playing H to secure 1 against their likely H.
`#595` · game 139 · round 1 · agent A13 (opponent: A14) · other · A13 Exchange 7 with A14: They've played T all 6 times. Mutual T at 3-6. They seem committed to T. I'll exploit with N for 5 against their likely T.
`#596` · game 139 · round 1 · agent A14 (opponent: A13) · other · A14 Exchange 7 with A13: They've played T 6 straight times. I cooperated with T at 3-6. Exploiting with N for 5 against their likely T.
`#597` · game 138 · round 6 · agent A06 (opponent: script:Random) · other · A06 Exchange 12 with A16: They've played F at 9,10,11 (3 straight). I've played F at 7-11. Mutual F gives 1 each. Playing F to secure at least 1 against their likely F.
`#598` · game 137 · round 7 · agent A07 (opponent: script:TitForTat) · other · A07 Ex13 with A21: They alternated R,H at 7-12 (R at 7,9,11; H at 8,10,12). Expect R at 13. Playing H to exploit for 5.
`#599` · game 124 · round 17 · agent A07 (opponent: A06) · other · A07 Ex23 with A06: After mutual T at 22, playing T to continue mutual cooperation for 3 each.
`#600` · game 140 · round 1 · agent A22 (opponent: A07) · other · A22 Exchange 7 with A07: They've played Q all 6 times. I exploited X at 1,2, cooperated Q at 3-6. Continuing X to exploit their likely Q for 5.
`#601` · game 134 · round 11 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Exchange 17 with A19: We had mutual H at 13-16. I'm behind 27-42. They've been cooperating with H. I'll defect with R to try to catch up, expecting their H.
`#602` · game 123 · round 19 · agent A06 (opponent: A00) · other · A06 Exchange 25 with A00: Mutual T since 19. Continuing T to maintain mutual cooperation for 3 each.
`#603` · game 134 · round 12 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Exchange 18 with A19: They've played H 11 straight (7-17). I'm behind 27-47. Playing R to exploit their likely H for 5.
`#604` · game 134 · round 13 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Exchange 19 with A19: They've played H 12 straight (7-18). I'm behind 27-52. Playing R to exploit their likely H for 5.
`#605` · game 137 · round 11 · agent A07 (opponent: script:TitForTat) · other · A07 Ex17 with A21: They played R at 16 (I exploited for 5). They may retaliate with H at 17. Playing H to secure at least 1, or 5 if they play R.
`#606` · game 140 · round 2 · agent A22 (opponent: A07) · other · A22 Exchange 8 with A07: They played Q 6 straight then X at 7. Mutual X last exchange. Continuing X to secure at least 1 against their likely X.
`#607` · game 136 · round 16 · agent A20 (opponent: script:TitForTat) · other · A20 Exchange 22 with A15: Mutual X standoff since 8 (14 straight). Continuing X to secure at least 1 and avoid 0 against their likely X.
`#608` · game 134 · round 14 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Exchange 20 with A19: They've played H 13 straight (7-19). I'm behind 27-57. Continuing R to exploit their likely H for 5.
`#609` · game 140 · round 3 · agent A07 (opponent: A22) · other · A07 Ex9 with A22: They've played X at 7-8 (mutual X standoff). They say continuing X. Playing X to secure at least 1 against their likely X.
`#610` · game 123 · round 23 · agent A00 (opponent: A06) · other · A00 Exchange 29 with A06: Mutual T since 19 (10 straight). Continuing T to maintain mutual cooperation for 3 each.
`#611` · game 134 · round 16 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Exchange 22 with A19: They've played H 15 straight (7-21). I'm behind 27-67. Continuing R to exploit their likely H for 5.
`#612` · game 140 · round 4 · agent A07 (opponent: A22) · other · A07 Ex10 with A22: Mutual X standoff since 7. They're committed to X. Playing X to secure at least 1 against their likely X.
`#613` · game 124 · round 24 · agent A07 (opponent: A06) · other · A07 Ex30 with A06: Mutual T since 22 (8 straight). Continuing T to maintain mutual cooperation for 3 each.
`#614` · game 124 · round 24 · agent A06 (opponent: A07) · other · A06 Exchange 30 with A07: Mutual T since 22. Continuing T to maintain mutual cooperation for 3 each.
`#615` · game 137 · round 14 · agent A07 (opponent: script:TitForTat) · other · A07 Ex20 with A21: Mutual H at 17-19. Continuing H to maintain mutual cooperation for 1 each, secure points as I'm ahead.
`#616` · game 134 · round 17 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Exchange 23 with A19: They've played H 16 straight (7-22). My R attempts at 17-22 all failed (0 points). Switching to H to secure at least 1 against their likely H.
`#617` · game 136 · round 22 · agent A20 (opponent: script:TitForTat) · other · A20 Exchange 28 with A15: Mutual X standoff since 8 (20 straight). Continuing X to secure at least 1 against their likely X.
`#618` · game 141 · round 4 · agent A00 (opponent: A11) · other · A00 Exchange 10 with A11: They've played J 8 of 9 times. Playing J for mutual 3.
`#619` · game 141 · round 4 · agent A11 (opponent: A00) · other · A11 Exchange 10 with A00: They defected F at ex9 while I played J. Rebuilding cooperation with J. Playing J to re-establish mutual cooperation for 3 each.
`#620` · game 140 · round 5 · agent A07 (opponent: A22) · other · A07 Ex11 with A22: Mutual X standoff since 7. They're committed to X. Playing X to secure at least 1 against their likely X.
`#621` · game 136 · round 23 · agent A20 (opponent: script:TitForTat) · other · A20 Exchange 29 with A15: Mutual X standoff since 8 (21 straight). Continuing X to secure at least 1 against their likely X.
`#622` · game 139 · round 6 · agent A13 (opponent: A14) · other · A13 Exchange 12 with A14: Mutual N since 7 (5 straight). They're committed to N. Playing N to secure at least 1 against their likely N.
`#623` · game 134 · round 19 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Exchange 25 with A19: Mutual H at 23-24. I'm far behind 29-74. Trying R to exploit their likely H for 5.
`#624` · game 137 · round 17 · agent A07 (opponent: script:TitForTat) · other · A07 Ex23 with A21: Mutual H at 17-22 (6 straight). Continuing H to maintain mutual cooperation for 1 each, secure points as I'm ahead.
`#625` · game 139 · round 7 · agent A14 (opponent: A13) · other · A14 Exchange 13 with A13: Mutual N since 7. Continuing N to secure at least 1 against their likely N.
`#626` · game 141 · round 6 · agent A00 (opponent: A11) · other · A00 Exchange 12 with A11: They've played J 10 of 11 times, mutual J last 2. Playing J for mutual 3.
`#627` · game 136 · round 28 · agent A20 (opponent: script:TitForTat) · other · A20 Exchange 34 with A15: Mutual X standoff since 8 (27 straight). Continuing X to secure at least 1 against their likely X.
`#628` · game 141 · round 7 · agent A00 (opponent: A11) · other · A00 Exchange 13 with A11: They've played J 11 of 12 times, mutual J last 3. Continuing J for mutual 3.
`#629` · game 139 · round 8 · agent A14 (opponent: A13) · other · A14 Exchange 14 with A13: Mutual N since 7. Continuing N to secure at least 1 against their likely N.
`#630` · game 123 · round 29 · agent A06 (opponent: A00) · other · A06 Exchange 35 with A00: Mutual T since 19 (15 straight). Continuing T to maintain mutual cooperation for 3 each.
`#631` · game 137 · round 20 · agent A07 (opponent: script:TitForTat) · other · A07 Ex26 with A21: Mutual H at 17-25 (9 straight). Continuing H to maintain mutual cooperation for 1 each, secure points as I'm ahead.
`#632` · game 136 · round 30 · agent A20 (opponent: script:TitForTat) · other · A20 Exchange 36 with A15: Mutual X standoff since 8 (28 straight). Continuing X to secure at least 1 against their likely X.
`#633` · game 141 · round 9 · agent A00 (opponent: A11) · other · A00 Exchange 15 with A11: Mutual J since ex10 (ex9 I defected). They've played J 13/14. Continuing J for mutual 3.
`#634` · game 134 · round 24 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Exchange 30 with A19: They've played H 7 straight (23-29). Continuing H to secure 1 against their likely H.
`#635` · game 137 · round 22 · agent A07 (opponent: script:TitForTat) · other · A07 Ex28 with A21: Mutual H at 17-27 (11 straight). Continuing H to maintain mutual cooperation for 1 each, secure points as I'm ahead.
`#636` · game 143 · round 1 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Exchange 7 with A18: They've played Y all 6 exchanges. Mutual Y last 4. Continuing Y to maintain mutual cooperation for 3 each.
`#637` · game 134 · round 25 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Exchange 31 with A19: They've played H 8 straight (23-30). I've tried R several times and always got 0. Continuing H to secure 1 against their likely H.
`#638` · game 145 · round 1 · agent A20 (opponent: script:TitForTat) · other · A20 Exchange 7 with A21: They played J 6 straight. Mutual J last 4 (ex3-6) giving 3 each. I'm ahead 22-12. Continuing J to maintain mutual cooperation for 3 each.
`#639` · game 134 · round 27 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Exchange 33 with A19: They've played H 10 straight (23-32). I've tried R several times and got 0. Continuing H to secure 1 against their likely H.
`#640` · game 145 · round 3 · agent A20 (opponent: script:TitForTat) · other · A20 Exchange 9 with A21: Mutual J since ex3 (6 straight). I'm ahead 28-18. Continuing J to maintain mutual cooperation for 3 each.
`#641` · game 145 · round 4 · agent A20 (opponent: script:TitForTat) · other · A20 Exchange 10 with A21: Mutual J since ex3 (7 straight). I'm ahead 31-21. Continuing J to maintain mutual cooperation for 3 each.
`#642` · game 139 · round 11 · agent A13 (opponent: A14) · other · A13 Exchange 17 with A14: Mutual N since 7 (10 straight). They're committed to N. Continuing N to secure at least 1 against their likely N.
`#643` · game 139 · round 11 · agent A14 (opponent: A13) · other · A14 Exchange 17 with A13: Long mutual N standoff since 7. I'm ahead and taking T to exploit their committed N for 5.
`#644` · game 148 · round 1 · agent A07 (opponent: script:Grudger) · other · A07 Ex7 with A12: mutual J last 4 (ex3-6), I'm ahead 22-12. Continuing J for mutual 3 each to secure points.
`#645` · game 134 · round 29 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Exchange 35 with A19: They've played H 11 straight (23-33). R has failed repeatedly. Continuing H to secure 1 against their likely H.
`#646` · game 142 · round 11 · agent A09 (opponent: script:Grudger) · other · A09 Ex17 with A12: Mutual Q since ex3 (14 straight). Continuing Q for mutual 3.
`#647` · game 148 · round 3 · agent A07 (opponent: script:Grudger) · other · A07 Ex9 with A12: Mutual J since ex3 (6 straight), I'm ahead 28-18. Continuing J to maintain mutual cooperation for 3 each.
`#648` · game 148 · round 6 · agent A07 (opponent: script:Grudger) · other · A07 Ex12 with A12: Mutual J since ex3 (8 straight), I'm ahead 37-27. Continuing J for mutual 3 each to secure points.
`#649` · game 143 · round 6 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Exchange 12 with A18: They've defected 3 of last 5 (ex7,9 W; ex8,10,11 mutual W). Tied 25-25. Continuing W to secure at least 1 against their likely W.
`#650` · game 152 · round 1 · agent A00 (opponent: script:Grudger) · directive · A00 Exchange 7 with A17: They've played T all 6 exchanges. I've cooperated last 4 for mutual 3. Since they never play N, I'll take N to get 5 while they play T.
`#651` · game 148 · round 8 · agent A07 (opponent: script:Grudger) · other · A07 Ex14 with A12: Mutual J since ex3 (10 straight), I'm ahead 43-33. Continuing J for mutual 3 each to secure points.
`#652` · game 147 · round 6 · agent A13 (opponent: script:TitForTat) · other · A13 Exchange 12 with A05: They've played R all 11 exchanges. I defected ex11 for 5. Continuing H to exploit their committed R for 5 each.
`#653` · game 143 · round 7 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Exchange 13 with A18: They've played W 6 straight (ex7-12). Tied 26-26. Continuing W to secure 1 against their likely W.
`#654` · game 152 · round 2 · agent A00 (opponent: script:Grudger) · other · A00 Exchange 8 with A17: They've played T all 7 exchanges. Taking N again to get 5 against their T.
`#655` · game 153 · round 1 · agent A07 (opponent: A23) · other · A07 Ex7 with A23: mutual Y last 4 (ex3-6), I'm ahead 22-12. Continuing Y for mutual 3 each to secure points.
`#656` · game 145 · round 11 · agent A20 (opponent: script:TitForTat) · other · A20 Exchange 17 with A21: They defected at ex16 after I defected ex15. Playing F to hedge - if they J I get 5, if F we both get 1. I'm ahead 52-37.
`#657` · game 152 · round 3 · agent A00 (opponent: script:Grudger) · other · A00 Exchange 9 with A17: They've played T 7/8 times, N once (ex8). I'm ahead 28-13. Taking N — worst case 1 vs their N, best case 5 if they return to T.
`#658` · game 151 · round 4 · agent A20 (opponent: script:Random) · other · A20 Ex10 with A01: They've played Q 8/9, returned to Q after my X at 8-9. I'm ahead 32-17. Taking X to exploit their committed Q for 5.
`#659` · game 145 · round 13 · agent A20 (opponent: script:TitForTat) · other · A20 Ex19 with A21: After mutual J ex3-14, I defected ex15 (got 5), they defected ex16, mutual F ex16-18 (1 each). I'm ahead 54-39. Last 3 mutual F giving 1 each. They may return to J for 3 each or stay F. I'll play J to try to restore mutual 3.
`#660` · game 147 · round 8 · agent A13 (opponent: script:TitForTat) · other · A13 Exchange 14 with A05: They played R 11/13, but H last 2 (12,13). H dominates against both their likely plays. Picking H.
`#661` · game 152 · round 4 · agent A00 (opponent: script:Grudger) · other · A00 Exchange 10 with A17: They've played N last two (ex8-9) after I defected ex7. I'm ahead 29-14. Taking N to secure at least 1, and get 5 if they return to T.
`#662` · game 151 · round 5 · agent A20 (opponent: script:Random) · other · A20 Ex11 with A01: They've played Q 9/10, returned to Q after my X at 8-10. I'm ahead 37-17. Taking X to exploit their committed Q for 5.
`#663` · game 154 · round 1 · agent A22 (opponent: script:Random) · other · 
`#664` · game 147 · round 9 · agent A13 (opponent: script:TitForTat) · other · A13 Exchange 15 with A05: They've played H last 3 (12-14). Taking R to exploit their H for 5.
`#665` · game 153 · round 4 · agent A23 (opponent: A07) · other · A23 Ex10 with A07: Mutual Y since ex3 (7 straight). Continuing Y for mutual 3 each to secure points.
`#666` · game 151 · round 6 · agent A20 (opponent: script:Random) · other · A20 Ex12 with A01: They've played Q 9/11, but played X last (ex11) after my repeated X. I'm ahead 38-18. Taking X again - if they return to Q I get 5, if mutual X I get 1.
`#667` · game 143 · round 12 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Exchange 18 with A18: Mutual W since ex8 (10 straight), tied 31-31. Continuing W to secure 1 each against their likely W.
`#668` · game 143 · round 13 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Exchange 19 with A18: Mutual W since ex8 (11 straight), tied 32-32. Continuing W to secure 1 each against their likely W.
`#669` · game 153 · round 6 · agent A23 (opponent: A07) · other · A23 Ex12 with A07: Mutual Y since ex3 (9 straight). Continuing Y for mutual 3 each to secure points.
`#670` · game 154 · round 4 · agent A22 (opponent: script:Random) · other · A22 Ex10 with A01: They played P ex1-7, M ex8-9. I'm ahead 28-18. They seem to have shifted to M. I'll play M to secure at least 1 (mutual M) or get 5 if they return to P.
`#671` · game 157 · round 1 · agent A03 (opponent: A11) · other · A03 Ex7 with A11: They've played P all 6 exchanges, I cooperated last 4 for mutual 3. Taking M to exploit their committed P for 5.
`#672` · game 156 · round 3 · agent A00 (opponent: script:Pavlov) · other · A00 Exchange 9 with A02: They've played J all 8 exchanges. I'm ahead 30-15. Taking F to get 5 against their committed J.
`#673` · game 145 · round 19 · agent A20 (opponent: script:TitForTat) · other · A20 Ex25 with A21: Mutual F ex21-24 (1 each). I'm ahead 63-48. Playing F to secure at least 1, get 5 if they J.
`#674` · game 154 · round 5 · agent A22 (opponent: script:Random) · other · A22 Ex11 with A01: They've played P 8/10, M only ex8-9. I'm ahead 33-18. Playing P to secure 3 against their likely P, or 5 if they go M.
`#675` · game 157 · round 2 · agent A03 (opponent: A11) · other · A03 Ex8 with A11: They've played P all 7 exchanges. Taking M again to exploit their committed P for 5.
`#676` · game 152 · round 11 · agent A00 (opponent: script:Grudger) · other · A00 Exchange 17 with A17: They've played N 9 straight (ex8-16). I'm ahead 36-21. Taking N to secure mutual 1, as they seem committed to N.
`#677` · game 156 · round 5 · agent A00 (opponent: script:Pavlov) · other · A00 Exchange 11 with A02: They've played J 9/10, returned to J after my F at ex8 and ex10. I'm ahead 36-16. Taking F to exploit their committed J for 5.
`#678` · game 154 · round 7 · agent A22 (opponent: script:Random) · other · A22 Ex13 with A01: They've played P 10/12, returned to P after my M at ex12. I'm ahead 41-21. Taking M to exploit their committed P for 5.
`#679` · game 143 · round 19 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Ex25 with A18: They defected at ex24 (I played Y, they W). I'm behind 37-42. Playing W to secure at least 1, or 5 if they return to Y.
`#680` · game 147 · round 14 · agent A13 (opponent: script:TitForTat) · other · A13 Exchange 20 with A05: They've mixed H/R recently (H ex18-19, R ex16-17). H dominates both their options. Picking H.
`#681` · game 154 · round 8 · agent A22 (opponent: script:Random) · other · A22 Ex14 with A01: They've played P 11/13, very committed to P. Taking M to exploit for 5.
`#682` · game 152 · round 13 · agent A00 (opponent: script:Grudger) · other · A00 Exchange 19 with A17: They've played N 11 straight (ex8-18). I'm ahead 38-23. Taking N to secure mutual 1, get 5 if they defect to T.
`#683` · game 143 · round 21 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Exchange 27 with A18: Mutual W since ex8 except their defect at ex24. Playing W to secure 1 each against their likely W.
`#684` · game 154 · round 9 · agent A22 (opponent: script:Random) · other · A22 Ex15 with A01: They've played P 11/13, though played M at ex14. I'm ahead 47-22. Playing M to exploit their likely P for 5, accepting mutual M risk.
`#685` · game 157 · round 3 · agent A03 (opponent: A11) · other · A03 Ex9 with A11: They played P ex1-7, M ex8. I'm ahead 28-13. Playing M to secure at least 1 (mutual M) or 5 if they return to P.
`#686` · game 145 · round 23 · agent A20 (opponent: script:TitForTat) · other · A20 Ex29 with A21: Mutual F ex21-28 (8 straight). I'm ahead 67-52. Continuing F to secure at least 1, get 5 if they J.
`#687` · game 154 · round 10 · agent A22 (opponent: script:Random) · other · A22 Ex16 with A01: They've played P 12/15, returned to P at ex15 after my M at ex14. I'm ahead 52-22. Taking M to exploit their committed P for 5.
`#688` · game 145 · round 24 · agent A20 (opponent: script:TitForTat) · other · A20 Ex30 with A21: Mutual F ex21-29 (9 straight). I'm ahead 68-53. Continuing F to secure at least 1, get 5 if they J.
`#689` · game 152 · round 16 · agent A00 (opponent: script:Grudger) · other · A00 Exchange 22 with A17: They've played N 12 straight (ex8-21). I'm ahead 40-30. Taking T to exploit their committed N for 5.
`#690` · game 157 · round 4 · agent A03 (opponent: A11) · other · A03 Ex10 with A11: They played P ex1-7, M ex8-9. I played M ex8-9 for mutual M. I'm ahead 29-14. Playing M to keep mutual M (1 each) or get 5 if they return to P.
`#691` · game 143 · round 26 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Ex32 with A18: They've been committed to W (only Y at ex24 when I played Y, they got 5). Playing W to secure 1 each.
`#692` · game 159 · round 3 · agent A13 (opponent: script:Grudger) · other · A13 Ex9 with A12: They've played T 7/8, N once at ex8. I'm ahead 28-13. Playing N to exploit their T for 5, accepting mutual N risk.
`#693` · game 147 · round 16 · agent A13 (opponent: script:TitForTat) · other · A13 Ex22 with A05: H is strictly dominant (5 vs R, 1 vs H). Picking H.
`#694` · game 145 · round 26 · agent A20 (opponent: script:TitForTat) · other · A20 Ex32 with A21: Mutual F ex16-31 (long run). I'm ahead 70-55. Continuing F to secure at least 1, get 5 if they J.
`#695` · game 154 · round 14 · agent A22 (opponent: script:Random) · other · A22 Ex20 with A01: They've played M in 5 of last 6 (ex14-19). I'm ahead 60-25. Playing M to secure mutual 1 against their likely M.
`#696` · game 152 · round 18 · agent A00 (opponent: script:Grudger) · other · A00 Exchange 24 with A17: They've played N 16 straight (ex8-23). I've exploited with T at ex20,22,23 getting 5 each. Taking T again to exploit their committed N for 5.
`#697` · game 159 · round 6 · agent A13 (opponent: script:Grudger) · other · A13 Ex12 with A12: They've played N last 4 (ex8-11). I'm ahead 31-16. Taking T to exploit their committed N for 5.
`#698` · game 143 · round 30 · agent A04 (opponent: script:AlwaysDefect) · other · A04 Ex36 with A18: They've played W 19 straight (ex16-35 except their Y-5 at ex24). Playing W to secure mutual 1.
`#699` · game 152 · round 19 · agent A00 (opponent: script:Grudger) · other · A00 Exchange 25 with A17: They've played N 17 straight (ex8-24). I've exploited with T at ex20,22,23,24. Taking T again to exploit their committed N for 5.
`#700` · game 145 · round 30 · agent A20 (opponent: script:TitForTat) · other · A20 Ex36 with A21: Mutual F ex16-35 (long run). I'm ahead 74-59. Continuing F to secure at least 1, get 5 if they J.
`#701` · game 157 · round 6 · agent A03 (opponent: A11) · other · A03 Ex12 with A11: They've played M ex8-11 (4 straight) after P ex1-7. I'm ahead 31-16. Playing M to secure mutual 1 or get 5 if they return to P.
`#702` · game 154 · round 15 · agent A22 (opponent: script:Random) · other · A22 Ex21 with A01: They've played P 3 of last 4 (ex17,20 P; ex18,19 M). I'm ahead 65-25. Taking M to exploit their P lean, accepting mutual M risk.
`#703` · game 162 · round 1 · agent A04 (opponent: script:TitForTat) · other · A04 Ex7 with A21: They've played R 6 straight. Taking H to exploit for 5 if they stay R, accepting mutual H (1) risk.
`#704` · game 157 · round 7 · agent A11 (opponent: A03) · other · A11 Ex13 with A03: Mutual M ex8-12. Continuing M to secure mutual 1 against their likely M.
`#705` · game 147 · round 21 · agent A13 (opponent: script:TitForTat) · other · A13 Ex27 with A05: ahead 68-53. Picking H (dominant: 5 vs their R, 1 vs their H).
`#706` · game 154 · round 16 · agent A22 (opponent: script:Random) · other · A22 Ex22 with A01: They've played M in 6 of last 8 (ex14-21). I'm ahead 66-26. Playing M to secure mutual 1 or get 5 if they defect to P.
`#707` · game 162 · round 2 · agent A04 (opponent: script:TitForTat) · other · A04 Ex8 with A21: They've played R 7 straight. I've exploited with H at ex1,2,7 getting 5 each. Taking H again to exploit their committed R for 5.
`#708` · game 162 · round 3 · agent A04 (opponent: script:TitForTat) · other · A04 Ex9 with A21: They played R 7/8, H once at ex8. I've exploited with H at ex1,2,7. Taking H to exploit their R lean, accepting mutual H risk.
`#709` · game 152 · round 26 · agent A00 (opponent: script:Grudger) · other · A00 Ex32 with A17: They've played N 24 straight (ex8-31). I've exploited with T since ex20 getting 5 each. Taking T again to exploit their committed N for 5.
`#710` · game 160 · round 2 · agent A14 (opponent: A11) · other · A14 Ex8 with A11: I've cooperated (Y) ex3-6, mutual W ex7. Playing Y to seek mutual 3.
`#711` · game 160 · round 2 · agent A11 (opponent: A14) · other · A11 Ex8 with A14: They've played Y 6/7, W at ex7. I'm ahead 23-13. Playing W to exploit their Y lean or secure mutual W.
`#712` · game 162 · round 5 · agent A04 (opponent: script:TitForTat) · other · A04 Ex11 with A21: They've played R 7/10, H last 3. I've exploited their R (got 5 at ex1,2,7). Playing H to get 5 if they return to R, or mutual 1 if they stay H.
`#713` · game 157 · round 10 · agent A03 (opponent: A11) · other · A03 Ex16 with A11: Mutual M ex8-15. Continuing M to secure mutual 1 against their likely M.
`#714` · game 152 · round 29 · agent A00 (opponent: script:Grudger) · other · A00 Ex35 with A17: They've played N 25 straight (ex8-32). I've exploited with T since ex20 getting 5 each. Taking T again to exploit their committed N for 5.
`#715` · game 147 · round 25 · agent A13 (opponent: script:TitForTat) · other · A13 Ex31 with A05: They've played H 6 straight (ex25-30), mutual H. I'm ahead 72-57. Continuing H to secure mutual 1.
`#716` · game 152 · round 30 · agent A00 (opponent: script:Grudger) · other · A00 Ex36 with A17: They've played N 26 straight (ex8-33). I've exploited with T since ex20 getting 5 each. Taking T again to exploit their committed N for 5.
`#717` · game 162 · round 6 · agent A04 (opponent: script:TitForTat) · other · A04 Ex12 with A21: They've played H last 4 (ex8-11). I'm ahead 31-16. Playing H to secure mutual 1 against their likely H, since R would give me 0.
`#718` · game 165 · round 1 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Ex7 with A19: They've played J 6 straight. Mutual J ex3-6. Continuing J for mutual 3.
`#719` · game 162 · round 7 · agent A04 (opponent: script:TitForTat) · other · A04 Ex13 with A21: They've played H last 5 (ex8-12), mutual H. I'm ahead 32-17. Playing H to secure mutual 1 against their likely H, since R would give me 0 if they stay H.
`#720` · game 147 · round 28 · agent A13 (opponent: script:TitForTat) · other · A13 Ex34 with A05: They've played H 9 straight (ex25-33), mutual H. I'm ahead 75-60. Continuing H to secure mutual 1.
`#721` · game 165 · round 2 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Ex8 with A19: They defected to F at ex7 after mutual J ex3-6. I'm ahead 22-17. Playing F to protect/exploit, accepting mutual F risk.
`#722` · game 157 · round 12 · agent A03 (opponent: A11) · other · A03 Ex18 with A11: Mutual M ex8-17. A11 committed to M. Playing M to secure mutual 1, ahead 37-22.
`#723` · game 162 · round 9 · agent A04 (opponent: script:TitForTat) · other · A04 Ex15 with A21: They've played H last 7 (ex8-14), mutual H. I'm ahead 34-19. Playing H to secure mutual 1 against their likely H, since R would give me 0.
`#724` · game 163 · round 8 · agent A03 (opponent: script:TitForTat) · other · A03 Ex14 with A15: They've played W ex10-13 (4 straight) after Y ex1-9. I'm ahead 37-22. Playing W to secure mutual 1 or get 5 if they return to Y.
`#725` · game 153 · round 24 · agent A23 (opponent: A07) · other · A23 Ex30 with A07: Mutual Y ex10-29, I'm ahead 91-81. Continuing Y to maintain mutual 3 cooperation.
`#726` · game 160 · round 4 · agent A14 (opponent: A11) · other · A14 Ex10 with A11: They've defected with W at ex8, mutual W ex7/9. I'm ahead 24-19. Playing W to secure at least 1 / exploit if they go Y.
`#727` · game 160 · round 4 · agent A11 (opponent: A14) · other · A11 Ex10 with A14: They play Y seeking mutual 3, I'm ahead 29-14. Playing W to exploit their Y lean or secure mutual W.
`#728` · game 154 · round 24 · agent A22 (opponent: script:Random) · other · A22 Ex30 with A01: They've played P in 18/29 overall, P last 2 (28,29). I'm ahead 90-30. Playing M to get 5 if they defect to P again.
`#729` · game 153 · round 25 · agent A07 (opponent: A23) · other · A07 Ex31 with A23: Mutual Y through ex30 (Y 28 times, W 2 times). A23 committed to Y. Continuing Y for mutual 3.
`#730` · game 166 · round 3 · agent A22 (opponent: script:TitForTat) · other · A22 Ex9 with A10: They've played Q 7/8, X once last ex. I'm ahead 28-13. Playing X to exploit their strong Q lean, accepting mutual X risk.
`#731` · game 162 · round 13 · agent A04 (opponent: script:TitForTat) · other · A04 Ex19 with A21: They've played H 11 straight (ex8-18), mutual H. I'm ahead. Playing H to secure mutual 1 against their likely H.
`#732` · game 160 · round 5 · agent A11 (opponent: A14) · other · A11 Ex11 with A14: They've played W ex7,9,10, seeking mutual W or exploit. I'm ahead 30-15. Playing W to secure mutual 1 against their likely W.
`#733` · game 166 · round 4 · agent A22 (opponent: script:TitForTat) · other · A22 Ex10 with A10: They've played Q 7/9, X last 2. I'm ahead 29-14. Playing X to exploit their Q lean, accepting mutual X risk.
`#734` · game 165 · round 6 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Ex12 with A19: Mutual F ex8-11 after their ex7 defection. Continuing F for stable mutual 1.
`#735` · game 153 · round 28 · agent A07 (opponent: A23) · other · A07 Ex34 with A23: Mutual Y through ex33. A23 committed to Y. Continuing Y for mutual 3.
`#736` · game 153 · round 28 · agent A23 (opponent: A07) · other · A23 Ex34 with A07: Mutual Y through ex33, I'm ahead 103-93. Continuing Y to maintain mutual 3 cooperation.
`#737` · game 162 · round 18 · agent A04 (opponent: script:TitForTat) · other · A04 Ex24 with A21: They've played H 16 straight (ex8-23), mutual H. I'm ahead 43-28. Playing H to secure mutual 1 against their likely H, since R would give me 0.
`#738` · game 157 · round 13 · agent A03 (opponent: A11) · other · A03 Ex19 with A11: They defected to P at ex18 after mutual M ex8-17. Playing P to protect against their continued P (mutual 3) or get 5 if they return to M.
`#739` · game 160 · round 6 · agent A11 (opponent: A14) · other · A11 Ex12 with A14: Playing W to secure mutual 1 against their committed W.
`#740` · game 166 · round 5 · agent A22 (opponent: script:TitForTat) · other · A22 Ex11 with A10: They've played Q 7/10, X last 3 (ex8-10). I'm ahead 30-15. Playing X to secure mutual X against their recent X lean.
`#741` · game 163 · round 16 · agent A03 (opponent: script:TitForTat) · other · A03 Ex22 with A15: Mutual W ex10-21 (12 straight). Ahead 45-30. Playing W to secure mutual 1 against their likely W.
`#742` · game 162 · round 21 · agent A04 (opponent: script:TitForTat) · other · A04 Ex27 with A21: They've played H 19 straight (ex8-26), mutual H. I'm ahead 46-31. Playing H to secure mutual 1 against their likely H.
`#743` · game 154 · round 29 · agent A22 (opponent: script:Random) · other · A22 Ex35 with A01: They've played M 5 of last 6 (30-34). I'm way ahead 99-34. Playing M to secure mutual 1 against their likely M, accepting 0 risk if they go P.
`#744` · game 165 · round 10 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Ex16 with A19: Mutual F ex8-15. Continuing F for stable mutual 1.
`#745` · game 160 · round 7 · agent A14 (opponent: A11) · other · A14 Ex13 with A11: Mutual W ex7,9-12. A11 committed to W. Playing W to secure mutual 1, ahead 27-22.
`#746` · game 160 · round 7 · agent A11 (opponent: A14) · other · A11 Ex13 with A14: Mutual W ex7-12. I'm ahead 32-17. Playing W to secure mutual 1 against their committed W.
`#747` · game 163 · round 17 · agent A03 (opponent: script:TitForTat) · other · A03 Ex23 with A15: Mutual W ex10-22 (13 straight). Ahead 46-31. Playing W to secure mutual 1 against their likely W.
`#748` · game 167 · round 1 · agent A07 (opponent: A20) · other · A07 Ex7 with A20: We've had mutual J ex3-6 after they defected ex1-2. I'm ahead 22-12. Continuing J for mutual 3 cooperation.
`#749` · game 167 · round 1 · agent A20 (opponent: A07) · other · A20 Ex7 with A07: Mutual J ex3-6. Continuing J for mutual 3 cooperation.
`#750` · game 165 · round 12 · agent A09 (opponent: script:AlwaysDefect) · other · A09 Ex18 with A19: Mutual F ex8-17 (10 straight). Continuing F for stable mutual 1.
`#751` · game 166 · round 7 · agent A22 (opponent: script:TitForTat) · other · A22 Ex13 with A10: They've played X last 5 (ex8-12). I'm ahead 32-17. Playing X to secure mutual X against their X lean.
`#752` · game 163 · round 20 · agent A03 (opponent: script:TitForTat) · other · A03 Ex26 with A15: Mutual W ex10-25 (16 straight). Ahead 49-34. Playing W to secure mutual 1 against their likely W.
`#753` · game 168 · round 1 · agent A13 (opponent: script:AlwaysDefect) · other · A13 Ex7 with A18: They've played Q all 6 exchanges, mutual Q ex3-6. I'm ahead 22-12. Playing Q to maintain mutual cooperation.
`#754` · game 167 · round 3 · agent A07 (opponent: A20) · other · A07 Ex9 with A20: Mutual J ex3-8 after their ex1-2 defect. I'm ahead 28-18. Continuing J for mutual 3 cooperation.
`#755` · game 166 · round 10 · agent A22 (opponent: script:TitForTat) · other · A22 Ex16 with A10: Mutual X ex8-15 (8 straight). I'm ahead 35-20. Playing X to secure mutual X against their X lean.
`#756` · game 169 · round 1 · agent A23 (opponent: script:AlwaysDefect) · other · A23 Ex7 with A19: Mutual Q ex3-6 after their Q ex2. Continuing Q for mutual 3 cooperation.
`#757` · game 168 · round 2 · agent A13 (opponent: script:AlwaysDefect) · other · A13 Ex8 with A18: They defected to X at ex7 after mutual Q ex3-6. Playing X to protect against their continued defection and punish their Q return.
`#758` · game 166 · round 11 · agent A22 (opponent: script:TitForTat) · other · A22 Ex17 with A10: Mutual X ex8-16 (9 straight). I'm ahead 36-21. Playing X to secure mutual X against their X lean.
`#759` · game 160 · round 10 · agent A14 (opponent: A11) · other · A14 Ex16 with A11: Mutual W ex7,9-15. Playing W to secure mutual 1.
`#760` · game 160 · round 10 · agent A11 (opponent: A14) · other · A11 Ex16 with A14: Mutual W ex7,9-15. I'm ahead 35-20. Playing W to secure mutual 1 against their committed W.
`#761` · game 170 · round 2 · agent A06 (opponent: script:TitForTat) · other · A06 Ex8 with A21: They played Q 7/7 so far (ex1-7). I've alternated Q/X. I'm ahead 27-12. They seem committed to Q. Playing Q for mutual 3.
`#762` · game 168 · round 3 · agent A13 (opponent: script:AlwaysDefect) · other · A13 Ex9 with A18: They defected ex7 after mutual Q ex3-6, mutual X ex8. Playing X to protect my lead and secure at least 1.
`#763` · game 166 · round 12 · agent A22 (opponent: script:TitForTat) · other · A22 Ex18 with A10: Mutual X ex8-17 (10 straight). Ahead 37-22. Playing X to secure mutual X against their X lean.
`#764` · game 160 · round 11 · agent A14 (opponent: A11) · other · A14 Ex17 with A11: Mutual W ex7,9-16. Playing W to secure mutual 1.
`#765` · game 163 · round 27 · agent A03 (opponent: script:TitForTat) · other · A03 Ex33 with A15: Mutual W ex10-32 (23 straight). Ahead 56-41. Playing W to secure mutual 1 against their likely W.
`#766` · game 166 · round 14 · agent A22 (opponent: script:TitForTat) · other · A22 Ex20 with A10: Mutual X ex8-19 (12 straight). I'm ahead 39-24. Playing X to secure mutual X against their X lean.
`#767` · game 168 · round 4 · agent A13 (opponent: script:AlwaysDefect) · other · A13 Ex10 with A18: Mutual X ex8-9 after their ex7 defect. Playing X to protect my lead (24-19) and secure at least 1.
`#768` · game 169 · round 4 · agent A23 (opponent: script:AlwaysDefect) · other · A23 Ex10 with A19: Tied 23-23. They defected X at ex7,9 after mutual Q ex3-6. Playing X to secure at least 1 against their defection.
`#769` · game 166 · round 16 · agent A22 (opponent: script:TitForTat) · other · A22 Ex22 with A10: Mutual X ex8-21 (14 straight). Ahead 41-26. Playing X to secure mutual X against their X lean.
`#770` · game 169 · round 5 · agent A23 (opponent: script:AlwaysDefect) · other · A23 Ex11 with A19: They've defected to X at ex7,9 when I played Q. Mutual X at ex8,10. Playing X to secure at least 1 against their X lean.
`#771` · game 166 · round 17 · agent A22 (opponent: script:TitForTat) · other · A22 Ex23 with A10: Mutual X ex8-22 (15 straight). Ahead 42-27. Playing X to secure mutual X against their X lean.
`#772` · game 170 · round 5 · agent A06 (opponent: script:TitForTat) · other · A06 Ex11 with A21: They've played Q 8/10, I'm ahead 33-18. Playing X to exploit their Q lean.
`#773` · game 169 · round 6 · agent A23 (opponent: script:AlwaysDefect) · other · A23 Ex12 with A19: They've played X ex8-11 (4 straight). Tied 25-25. Playing X to secure at least 1 against their X lean.
`#774` · game 166 · round 20 · agent A22 (opponent: script:TitForTat) · other · A22 Ex26 with A10: Mutual X ex8-25 (18 straight). Ahead 45-30. Playing X to secure mutual X against their X lean.
`#775` · game 169 · round 7 · agent A23 (opponent: script:AlwaysDefect) · other · A23 Ex13 with A19: They've played X ex8-12 (5 straight). Tied 26-26. Playing X to secure at least 1 against their X lean.
`#776` · game 160 · round 14 · agent A11 (opponent: A14) · other · A11 Ex20 with A14: Mutual W ex7,9-19 (12 straight). I'm ahead 39-24. Playing W to secure mutual 1 against their committed W.
`#777` · game 168 · round 8 · agent A13 (opponent: script:AlwaysDefect) · other · A13 Ex14 with A18: Mutual X ex8-13 after their ex7 defect. Ahead 28-23. Playing X to secure mutual X against their X lean.
`#778` · game 157 · round 19 · agent A03 (opponent: A11) · other · A03 Ex25 with A11: Mutual P ex19-24 (6 straight) after their P defection at 18. Ahead 60-40. Playing P to secure mutual 3 cooperation.
`#779` · game 160 · round 15 · agent A11 (opponent: A14) · other · A11 Ex21 with A14: Mutual W ex7,9-20 (13 straight). I'm ahead 40-25. Playing W to secure mutual 1 against their committed W.
`#780` · game 168 · round 10 · agent A13 (opponent: script:AlwaysDefect) · other · A13 Ex16 with A18: Mutual X ex8-15 (8 straight) after their ex7 defect. Ahead 30-25. Playing X to secure mutual X against their X lean.
`#781` · game 169 · round 10 · agent A23 (opponent: script:AlwaysDefect) · other · A23 Ex16 with A19: Tied 29-29. They've played X ex8-15 (8 straight). Playing X to secure mutual 1 against their X lean.
`#782` · game 166 · round 26 · agent A22 (opponent: script:TitForTat) · other · A22 Ex32 with A10: Mutual X ex8-31 (24 straight). Ahead 51-36. Playing X to secure mutual X against their X lean.
`#783` · game 169 · round 11 · agent A23 (opponent: script:AlwaysDefect) · other · A23 Ex17 with A19: Tied 30-30. They've played X ex8-16 (9 straight). Playing X to secure mutual 1 against their X lean.
`#784` · game 160 · round 16 · agent A11 (opponent: A14) · other · A11 Ex22 with A14: Mutual W ex7,9-21 (13 straight). Ahead 41-26. Playing W to secure mutual 1 against their committed W.
`#785` · game 169 · round 12 · agent A23 (opponent: script:AlwaysDefect) · other · A23 Ex18 with A19: Tied 31-31. They've played X ex8-17 (10 straight). Playing X to secure mutual 1 against their X lean.
`#786` · game 166 · round 27 · agent A22 (opponent: script:TitForTat) · other · A22 Ex33 with A10: Mutual X ex8-32 (25 straight). Ahead 52-37. Playing X to secure mutual X against their X lean.
`#787` · game 168 · round 12 · agent A13 (opponent: script:AlwaysDefect) · other · A13 Ex18 with A18: Mutual X ex8-17 (10 straight) after their ex7 defect. Ahead 32-27. Playing X to secure mutual X and protect my lead.
`#788` · game 166 · round 30 · agent A22 (opponent: script:TitForTat) · other · A22 Ex36 with A10: Mutual X ex8-35 (28 straight). Ahead 55-40. Playing X to secure mutual X against their X lean.
`#789` · game 172 · round 1 · agent A20 (opponent: A23) · other · A20 Ex7 with A23: They've played Q in 6/6 exchanges. I'm ahead 22-12. They keep playing Q. I'll play X to exploit their Q lean and secure 5 points.
`#790` · game 170 · round 11 · agent A06 (opponent: script:TitForTat) · other · A06 Ex17 with A21: They've played X ex8-16 (9 straight). Playing X to secure mutual 1 against their X lean.
`#791` · game 160 · round 18 · agent A14 (opponent: A11) · other · A14 Ex24 with A11: Mutual W ex7,9-23 (15 straight). I'm behind 38-33. Playing W to secure mutual 1 against their committed W.
`#792` · game 171 · round 8 · agent A03 (opponent: script:Pavlov) · other · A03 Ex14 with A08: They've played Q 13/13. I played X ex1-2 (got 5 each), mutual Q ex3-13. Playing X to exploit their consistent Q lean.
`#793` · game 170 · round 13 · agent A06 (opponent: script:TitForTat) · other · A06 Ex19 with A21: They've played X ex10-18 (9 straight). I'm ahead 41-26. Playing X to secure mutual 1 against their X lean.
`#794` · game 172 · round 2 · agent A20 (opponent: A23) · other · A20 Ex8 with A23: They've played Q in 7/7 exchanges. I'm ahead 27-12. Playing X to exploit their Q lean and secure 5 points.
`#795` · game 169 · round 19 · agent A23 (opponent: script:AlwaysDefect) · other · A23 Ex25 with A19: Mutual X ex8-24 (17 straight). Tied 38-38. Playing X to secure mutual 1 against their X lean.
`#796` · game 160 · round 20 · agent A11 (opponent: A14) · other · A11 Ex26 with A14: Mutual W ex7,9-25 (18 straight). Ahead 45-30. Playing W to secure mutual 1 against their committed W.
`#797` · game 171 · round 11 · agent A03 (opponent: script:Pavlov) · other · A03 Ex17 with A08: They've played Q 15/16. I'm ahead 54-34. Playing X to exploit their consistent Q lean.
`#798` · game 168 · round 19 · agent A13 (opponent: script:AlwaysDefect) · other · A13 Ex25 with A18: Mutual X ex8-24 (17 straight) after their ex7 defect. Ahead 39-34. Playing X to secure mutual X and protect my lead.
`#799` · game 170 · round 14 · agent A06 (opponent: script:TitForTat) · other · A06 Ex20 with A21: Mutual X ex10-19 (10 straight). Ahead 42-27. Playing X to secure mutual 1 against their X lean.
`#800` · game 171 · round 12 · agent A03 (opponent: script:Pavlov) · other · A03 Ex18 with A08: They've played Q 15/17. I'm ahead 55-35. Playing X to exploit their consistent Q lean.
`#801` · game 170 · round 15 · agent A06 (opponent: script:TitForTat) · other · A06 Ex21 with A21: Mutual X ex10-20 (11 straight). Ahead 43-28. Playing X to secure mutual 1 against their X lean.
`#802` · game 171 · round 13 · agent A03 (opponent: script:Pavlov) · other · A03 Ex19 with A08: They've played Q 16/18. I'm ahead 60-35. Playing X to exploit their consistent Q lean.
`#803` · game 172 · round 3 · agent A23 (opponent: A20) · other · A23 Ex9 with A20: They've played X ex7-8 to exploit my Q lean. Playing X to secure mutual 1 against their X lean.
`#804` · game 169 · round 24 · agent A23 (opponent: script:AlwaysDefect) · other · A23 Ex30 with A19: Mutual X ex10-29 (20 straight). Tied 43-43. Playing X to secure mutual 1 against their X lean.
`#805` · game 168 · round 23 · agent A13 (opponent: script:AlwaysDefect) · other · A13 Ex29 with A18: Mutual X ex8-28 (21 straight) after their ex7 defect. Ahead 43-38. Playing X to secure mutual X and protect my lead.
`#806` · game 169 · round 25 · agent A23 (opponent: script:AlwaysDefect) · other · A23 Ex31 with A19: Mutual X ex10-30 (21 straight). Tied 44-44. Playing X to secure mutual 1 against their X lean.
`#807` · game 173 · round 4 · agent A14 (opponent: script:Random) · other · A14 Ex10 with A16: They've played Y 8/9, W once (ex9). I'm ahead 31-16. Playing W to exploit their Y lean.
`#808` · game 172 · round 4 · agent A20 (opponent: A23) · other · A20 Ex10 with A23: They've switched to X (ex8-9 mutual X). Playing X to secure mutual 1 against their X lean.
`#809` · game 173 · round 5 · agent A14 (opponent: script:Random) · other · A14 Ex11 with A16: They've played Y 9/10, W once (ex9). I'm ahead 36-16. Playing W to exploit their strong Y lean.
`#810` · game 170 · round 21 · agent A06 (opponent: script:TitForTat) · other · A06 Ex27 with A21: Mutual X ex10-26 (17 straight). Ahead 49-34. Playing X to secure mutual 1 against their X lean.
`#811` · game 157 · round 26 · agent A11 (opponent: A03) · other · A11 Ex32 with A03: Mutual P ex19-31 (13 straight). Tied 71-71. Playing P to continue mutual cooperation.
`#812` · game 173 · round 6 · agent A14 (opponent: script:Random) · other · A14 Ex12 with A16: They've played Y 10/11, W once (ex9). I'm ahead 41-16. Playing W to exploit their strong Y lean.
`#813` · game 172 · round 5 · agent A20 (opponent: A23) · other · A20 Ex11 with A23: Mutual X ex8-10 (3 straight). Ahead 30-15. Playing X to secure mutual 1 against their X lean.
`#814` · game 175 · round 1 · agent A14 (opponent: script:Grudger) · other · A14 Ex7 with A12: They've played T 6/6. I'm ahead 22-12. Playing N to exploit their committed T lean.
`#815` · game 170 · round 23 · agent A06 (opponent: script:TitForTat) · other · A06 Ex29 with A21: Mutual X ex10-28 (19 straight). Ahead 51-36. Playing X to secure mutual 1 against their X lean.
`#816` · game 175 · round 2 · agent A14 (opponent: script:Grudger) · other · A14 Ex8 with A12: They've played T 7/7. I'm ahead 27-12. Playing N to exploit their committed T lean.
`#817` · game 170 · round 25 · agent A06 (opponent: script:TitForTat) · other · A06 Ex31 with A21: Mutual X ex10-30 (21 straight). Ahead 53-38. Playing X to secure mutual 1 against their X lean.
`#818` · game 174 · round 4 · agent A09 (opponent: script:TitForTat) · other · A09 Ex10 with A15: They've played T 9/9. I'm ahead 33-18. Playing N to exploit their committed T lean.
`#819` · game 172 · round 6 · agent A23 (opponent: A20) · other · A23 Ex12 with A20: Mutual X ex8-11 (4 straight). Ahead 26-21. Playing X to secure mutual 1 against their X lean.
`#820` · game 171 · round 18 · agent A03 (opponent: script:Pavlov) · other · A03 Ex24 with A08: They alternate Q/X since ex14. I'm ahead 73-38. Playing X to exploit their Q plays and secure mutual 1 on X plays.
`#821` · game 177 · round 2 · agent A23 (opponent: script:Pavlov) · other · A23 Ex8 with A08: They've played Y 7/7. I'm ahead 27-12. Playing W to exploit their committed Y lean.
`#822` · game 172 · round 7 · agent A20 (opponent: A23) · other · A20 Ex13 with A23: Mutual X ex8-12 (5 straight). Ahead 32-17. Playing X to secure mutual 1 against their X lean.
`#823` · game 171 · round 19 · agent A03 (opponent: script:Pavlov) · other · A03 Ex25 with A08: They alternate Q/X since ex14. Ahead 78-38. Playing X to exploit their Q plays and secure mutual 1 on X plays.
`#824` · game 174 · round 5 · agent A09 (opponent: script:TitForTat) · other · A09 Ex11 with A15: They've played T 9/10, N once (ex10). I'm ahead 34-19. Playing N to exploit their strong T lean.
`#825` · game 171 · round 21 · agent A03 (opponent: script:Pavlov) · other · A03 Ex27 with A08: They alternate Q/X since ex14 (X on odd, Q on even). Ahead 84-39. Playing X to secure mutual 1 against their X lean on odd exchanges.
`#826` · game 176 · round 4 · agent A06 (opponent: script:Grudger) · other · A06 Ex10 with A17: They played P 8/9, M once (ex9). I'm ahead 31-16. Playing M to exploit their strong P lean.
`#827` · game 174 · round 7 · agent A09 (opponent: script:TitForTat) · other · A09 Ex13 with A15: They've played N ex10-12 (3 straight). I'm ahead 36-21. Playing N to secure mutual 1 against their N lean.
`#828` · game 171 · round 23 · agent A03 (opponent: script:Pavlov) · other · A03 Ex29 with A08: They alternate Q/X since ex14 (X on odd, Q on even). Ahead 90-40. Playing X to secure mutual 1 on this odd exchange.
`#829` · game 174 · round 8 · agent A09 (opponent: script:TitForTat) · other · A09 Ex14 with A15: They've played N ex10-13 (4 straight). I'm ahead 37-22. Playing N to secure mutual 1 against their N lean.
`#830` · game 174 · round 9 · agent A09 (opponent: script:TitForTat) · other · A09 Ex15 with A15: Mutual N ex10-14 (5 straight). Ahead 38-23. Playing N to secure mutual 1 against their N lean.
`#831` · game 177 · round 5 · agent A23 (opponent: script:Pavlov) · other · A23 Ex11 with A08: They've played Y 8/10, W ex8,10. I'm ahead 34-14. Playing W to exploit their Y lean despite their recent W mixing.
`#832` · game 174 · round 10 · agent A09 (opponent: script:TitForTat) · other · A09 Ex16 with A15: Mutual N ex10-15 (6 straight). Ahead 39-24. Playing N to secure mutual 1 against their N lean.
`#833` · game 171 · round 26 · agent A03 (opponent: script:Pavlov) · other · A03 Ex32 with A08: They alternate Q/X (Q on even, X on odd) since ex14. Ex32 is even, so they'll likely play Q. I'm ahead 97-42. Playing X to exploit their Q and secure 5 points.
`#834` · game 175 · round 9 · agent A14 (opponent: script:Grudger) · other · A14 Ex15 with A12: Mutual N ex8-14 (7 straight). Ahead 34-19. Playing N to secure mutual 1 against their N lean.
`#835` · game 172 · round 11 · agent A20 (opponent: A23) · other · A20 Ex17 with A23: Mutual X ex8-16 (9 straight). Ahead 36-21. Playing X to secure mutual 1 against their X lean.
`#836` · game 180 · round 2 · agent A23 (opponent: A06) · other · A23 Ex8 with A06: They've played J 7/7. Mutual J ex3-7. Playing J to continue mutual cooperation.
`#837` · game 177 · round 7 · agent A23 (opponent: script:Pavlov) · other · A23 Ex13 with A08: They've alternated Y/W since ex7 (Y on odd, W on even). Ex13 odd, expect Y. Playing W to exploit.
`#838` · game 171 · round 28 · agent A03 (opponent: script:Pavlov) · other · A03 Ex34 with A08: They alternate Q/X (Q on even, X on odd) since ex14. Ex34 is even, so they'll likely play Q. I'm ahead 103-43. Playing X to exploit their Q for 5 points.
`#839` · game 177 · round 8 · agent A23 (opponent: script:Pavlov) · other · A23 Ex14 with A08: They alternate W/Y since ex8 (W on even, Y on odd). Ex14 even, expect W. Playing W for mutual 1.
`#840` · game 177 · round 9 · agent A23 (opponent: script:Pavlov) · other · A23 Ex15 with A08: They alternate Y/W since ex7 (Y on odd, W on even). Ex15 odd, expect Y. Playing W to exploit.
`#841` · game 179 · round 4 · agent A03 (opponent: A04) · other · A03 Ex10 with A04: They played P ex1-7, then M ex8-9. Ahead 26-21. Playing P to exploit their recent M lean.
`#842` · game 179 · round 4 · agent A04 (opponent: A03) · other · A04 Ex10 with A03: They've played P 8/9. I'm ahead 31-16. Playing M to exploit their strong P lean.
`#843` · game 177 · round 11 · agent A23 (opponent: script:Pavlov) · other · A23 Ex17 with A08: They alternate Y/W since ex7 (Y on odd, W on even). Ex17 odd, expect Y. Playing W to exploit.
`#844` · game 182 · round 1 · agent A13 (opponent: A06) · uncoded · A13 Ex7 with A06: They've played R 6/6. I've played R last 4. Playing R to secure mutual 3 against their committed R lean.
`#845` · game 175 · round 12 · agent A14 (opponent: script:Grudger) · other · A14 Ex18 with A12: Mutual N ex8-17 (10 straight). Ahead 37-22. Playing N to secure mutual 1 against their N lean.
`#846` · game 172 · round 14 · agent A23 (opponent: A20) · other · A23 Ex20 with A20: Mutual X ex8-19 (12 straight). Playing X to continue mutual 1 cooperation.
`#847` · game 177 · round 13 · agent A23 (opponent: script:Pavlov) · other · A23 Ex19 with A08: They alternate Y/W since ex7 (Y on odd, W on even). Ex19 odd, expect Y. Playing W to exploit.
`#848` · game 177 · round 14 · agent A23 (opponent: script:Pavlov) · other · A23 Ex20 with A08: They alternate Y/W since ex7 (Y on odd, W on even). Ex20 even, expect W. Playing W for mutual 1.
`#849` · game 176 · round 10 · agent A06 (opponent: script:Grudger) · other · A06 Ex16 with A17: They've played M ex9-15 (7 straight). I'm ahead 35-30. Playing M to secure mutual 1 against their M lean.
`#850` · game 180 · round 5 · agent A06 (opponent: A23) · other · A06 Ex11 with A23: They've played J 10/10. I'm ahead 38-18. Playing F to exploit their consistent J lean.
`#851` · game 184 · round 2 · agent A09 (opponent: script:Grudger) · other · A09 Ex8 with A17: Mutual R ex3-7 (5 straight). They've played R 7/7. Ahead 25-15. Playing R to secure mutual 3.
`#852` · game 181 · round 2 · agent A20 (opponent: A06) · other · A20 Ex8 with A06: They defected (W) in ex7 after mutual Y ex3-6. I played W ex1-2 (they Y). Playing W to punish/exploit their recent defection.
`#853` · game 177 · round 15 · agent A23 (opponent: script:Pavlov) · other · A23 Ex21 with A08: They alternate Y/W since ex7 (Y on odd, W on even). Ex21 odd, expect Y. Playing W to exploit.
`#854` · game 179 · round 5 · agent A03 (opponent: A04) · other · A03 Ex11 with A04: They've played P ex1-7, M ex8-10 (3 straight M). Tied 26-26. Playing M to secure mutual 1 or exploit their P.
`#855` · game 182 · round 2 · agent A13 (opponent: A06) · uncoded · A13 Ex8 with A06: They broke mutual R last exchange with H (ex7). Playing H to protect against their H lean.
`#856` · game 176 · round 11 · agent A06 (opponent: script:Grudger) · other · A06 Ex17 with A17: They've played M ex9-16 (8 straight). I'm ahead 36-31. Playing M to continue mutual 1 cooperation against their M lean.
`#857` · game 177 · round 17 · agent A23 (opponent: script:Pavlov) · other · A23 Ex23 with A08: They alternate Y/W (Y odd, W even) since ex7. Ex23 odd, expect Y. Playing W to exploit.
`#858` · game 180 · round 6 · agent A23 (opponent: A06) · other · A23 Ex12 with A06: They announced playing F to exploit my J lean (ex9-10 they played F for 5s). I'm playing F to counter and secure at least mutual 1, avoiding giving them another 5.
`#859` · game 176 · round 14 · agent A06 (opponent: script:Grudger) · other · A06 Ex20 with A17: They've played M ex9-19 (11 straight). Playing M to continue mutual 1 cooperation against their M lean.
`#860` · game 184 · round 8 · agent A09 (opponent: script:Grudger) · other · A09 Ex14 with A17: They've played R 13/13. I'm ahead 43-33. Playing H to exploit their strong R commitment.
`#861` · game 177 · round 21 · agent A23 (opponent: script:Pavlov) · other · A23 Ex27 with A08: They alternate Y/W (Y odd, W even) since ex7. Ex27 odd, expect Y. Playing W to exploit.
`#862` · game 184 · round 9 · agent A09 (opponent: script:Grudger) · other · A09 Ex15 with A17: They've played R 14/14. I played H ex14 (got 5). Continuing H to exploit their committed R lean.
`#863` · game 176 · round 17 · agent A06 (opponent: script:Grudger) · other · A06 Ex23 with A17: They've played M ex9-22 (14 straight). Playing M to continue mutual 1 cooperation against their M lean.
`#864` · game 177 · round 24 · agent A23 (opponent: script:Pavlov) · other · A23 Ex30 with A08: They alternate Y/W (Y odd, W even) since ex7. Ex30 even, expect W. Playing W for mutual 1.
`#865` · game 176 · round 18 · agent A06 (opponent: script:Grudger) · other · A06 Ex24 with A17: They've played M ex9-23 (15 straight). Playing M to continue mutual 1 cooperation against their M lean.
`#866` · game 188 · round 1 · agent A09 (opponent: script:TitForTat) · other · A09 Ex7 with A10: They've played R 6/6. I played R last 4. Ahead 22-12. Playing H to exploit their committed R lean.
`#867` · game 180 · round 8 · agent A23 (opponent: A06) · other · A23 Ex14 with A06: We've settled into mutual F ex11-13 after their ex9-10 F exploitation. Tied 31-31. Playing F to continue mutual 1 cooperation.
`#868` · game 188 · round 2 · agent A09 (opponent: script:TitForTat) · other · A09 Ex8 with A10: They've played R 8/8 (all R). I played H ex7 for 5. Continuing H to exploit their committed R lean.
`#869` · game 181 · round 6 · agent A20 (opponent: A06) · other · A20 Ex12 with A06: Mutual W ex8-11 (4 straight after their ex7 defection). Playing W to continue mutual 1 cooperation.
`#870` · game 182 · round 3 · agent A13 (opponent: A06) · uncoded · A13 Ex9 with A06: They've played R 7/8, defected once (ex7). I've played H 3x (ex1,2,8) and it worked twice. Playing H to exploit their strong R lean.
`#871` · game 189 · round 1 · agent A00 (opponent: A07) · other · A00 Ex7 with A07: They've played Y 6/6. I exploited W ex1-2, cooperated Y ex3-6. Playing W to exploit their consistent Y.
`#872` · game 188 · round 3 · agent A09 (opponent: script:TitForTat) · other · A09 Ex9 with A10: They've played R 7/8, H ex8. I'm ahead 28-13. Playing H to exploit their R lean / protect against their H.
`#873` · game 190 · round 1 · agent A06 (opponent: script:TitForTat) · other · A06 Ex7 with A05: I've been cooperating Y ex3-6 after their Y ex3-6 (mutual 3s). Earlier they played W ex1-2 (I got 0). I'm ahead 22-12. Considering playing Y to continue mutual cooperation, but watching for their defection.
`#874` · game 181 · round 7 · agent A06 (opponent: A20) · other · A06 Ex13 with A20: They've played W ex8-12 (5 straight mutual W). They signaled continuing W. Playing W to continue mutual 1 cooperation.
`#875` · game 172 · round 23 · agent A23 (opponent: A20) · other · A23 Ex29 with A20: We've had mutual X ex9-28 (20 straight). Continuing X for mutual 1 cooperation.
`#876` · game 189 · round 2 · agent A00 (opponent: A07) · other · A00 Ex8 with A07: They've played Y 7/7. I exploited W ex1-2,7. Playing W to keep exploiting their consistent Y.
`#877` · game 189 · round 2 · agent A07 (opponent: A00) · other · A07 Ex8 with A00: They defected W ex7 after mutual Y ex3-6. They've shown pattern of exploiting my Y. Playing W to protect/exploit.
`#878` · game 180 · round 10 · agent A23 (opponent: A06) · other · A23 Ex16 with A06: Mutual F ex11-15 after their ex9-10 F exploitation of my J lean. Tied 33-33. Playing F to continue mutual 1 cooperation.
`#879` · game 190 · round 4 · agent A06 (opponent: script:TitForTat) · other · A06 Ex10 with A05: They played W ex9 after mostly Y. I'm ahead 31-16. Playing W to protect/exploit.
`#880` · game 172 · round 27 · agent A23 (opponent: A20) · other · A23 Ex33 with A20: Mutual X ex9-32 (24 straight). Continuing X for mutual 1 cooperation.
`#881` · game 191 · round 2 · agent A00 (opponent: script:TitForTat) · other · A00 Ex8 with A10: They've played Y 7/7 but signaled playing W to protect. Playing W for mutual 1 / to avoid getting exploited.
`#882` · game 181 · round 10 · agent A06 (opponent: A20) · other · A06 Ex16 with A20: Mutual W ex8-15 (8 straight). They signaled continuing W. Playing W to continue mutual 1 cooperation.
`#883` · game 188 · round 9 · agent A09 (opponent: script:TitForTat) · other · A09 Ex15 with A10: Mutual H ex8-14 (7 straight). I'm ahead 34-19. Continuing H for mutual 1 cooperation.
`#884` · game 191 · round 3 · agent A00 (opponent: script:TitForTat) · other · A00 Ex9 with A10: They played W ex8 after Y 7x. Playing W to protect against their defection / secure mutual 1.
`#885` · game 179 · round 10 · agent A03 (opponent: A04) · other · A03 Ex16 with A04: They've played P ex13-15 (3 straight) against my M. Switching to P to get mutual 3 instead of 0.
`#886` · game 192 · round 1 · agent A09 (opponent: A03) · other · A09 Ex7 with A03: They've played R 6/6. I played H ex1-2 (5 each), R ex3-6. Ahead 22-12. Playing H to exploit their committed R lean.
`#887` · game 191 · round 4 · agent A00 (opponent: script:TitForTat) · other · A00 Ex10 with A10: They played W ex8-9 after Y 7x. I exploited W ex1-2,7. Playing W for mutual 1 / protection.
`#888` · game 188 · round 11 · agent A09 (opponent: script:TitForTat) · other · A09 Ex17 with A10: Mutual H ex8-16 (9 straight). I'm ahead 36-21. Continuing H for mutual 1 cooperation.
`#889` · game 193 · round 1 · agent A03 (opponent: A13) · other · A03 Ex7 with A13: They've played J 6/6. I've exploited F ex1-2 (5 each), cooperated J ex3-6. Playing F to exploit their committed J lean.
`#890` · game 181 · round 12 · agent A06 (opponent: A20) · other · A06 Ex18 with A20: Mutual W ex8-17 (10 straight). They signaled continuing W. Playing W to continue mutual 1 cooperation.
`#891` · game 192 · round 2 · agent A09 (opponent: A03) · other · A09 Ex8 with A03: They've played R 7/7. I've played H ex1-2 (5 each), R ex3-6, H ex7. Ahead 27-12. Playing H to exploit their committed R lean.
`#892` · game 192 · round 2 · agent A03 (opponent: A09) · other · A03 Ex8 with A09: They exploited my R in ex7 with H. Playing H to avoid 0 and secure mutual 1, matching their H lean.
`#893` · game 190 · round 10 · agent A06 (opponent: script:TitForTat) · other · A06 Ex16 with A05: Mutual W ex9-15 (7 straight). Continuing W to maintain mutual 1 cooperation.
`#894` · game 193 · round 2 · agent A13 (opponent: A03) · other · A13 Ex8 with A03: They defected F ex7 after J 6x. I'm ahead 22-17. Playing F to protect against their F and exploit if they return to J.
`#895` · game 191 · round 7 · agent A00 (opponent: script:TitForTat) · other · A00 Ex13 with A10: Mutual W ex8-12 (5 straight). Playing W to continue mutual 1 cooperation.
`#896` · game 193 · round 3 · agent A03 (opponent: A13) · other · A03 Ex9 with A13: They signaled F ex8. Playing F to secure mutual 1 and avoid being exploited.
`#897` · game 193 · round 3 · agent A13 (opponent: A03) · other · A13 Ex9 with A03: They've defected F ex7-8 against my J/F mix. I'm ahead 23-18. Playing F to protect against their F and exploit if they return to J.
`#898` · game 179 · round 12 · agent A03 (opponent: A04) · other · A03 Ex18 with A04: They've played P ex13-17 (5 straight). Mutual P ex16-17 for 3 each. Continuing P for mutual 3.
`#899` · game 191 · round 10 · agent A00 (opponent: script:TitForTat) · other · A00 Ex16 with A10: Mutual W ex8-15 (8 straight). Continuing W for mutual 1 cooperation.
`#900` · game 190 · round 11 · agent A06 (opponent: script:TitForTat) · other · A06 Ex17 with A05: Mutual W ex9-16 (8 straight). Continuing W to maintain mutual 1 cooperation.
`#901` · game 180 · round 14 · agent A06 (opponent: A23) · other · A06 Ex20 with A23: Mutual F ex11-19 stable. I'm ahead 47-27. Continuing F for mutual 1 cooperation.
`#902` · game 192 · round 3 · agent A03 (opponent: A09) · other · A03 Ex9 with A09: They've played H ex7-8, exploiting my R ex7. Playing H to secure mutual 1 rather than risk 0.
`#903` · game 179 · round 13 · agent A04 (opponent: A03) · other · A04 Ex19 with A03: Mutual P ex16-18 for 3 each. Continuing P for mutual 3 cooperation.
`#904` · game 196 · round 1 · agent A23 (opponent: script:TitForTat) · other · A23 Ex7 with A15: They've played Q 6/6. I exploited X ex1-2, cooperated Q ex3-6. Playing X to exploit their committed Q lean.
`#905` · game 192 · round 4 · agent A09 (opponent: A03) · other · A09 Ex10 with A03: They've played H ex8-9 (2 straight) after R streak. I'm ahead 29-14. Playing H to continue mutual 1 cooperation.
`#906` · game 181 · round 16 · agent A06 (opponent: A20) · other · A06 Ex22 with A20: Mutual W ex8-21 (14 straight). Continuing W to maintain mutual 1 cooperation.
`#907` · game 180 · round 16 · agent A06 (opponent: A23) · other · A06 Ex22 with A23: Mutual F ex11-21 stable. I'm ahead 49-29. Continuing F for mutual 1 cooperation.
`#908` · game 179 · round 15 · agent A04 (opponent: A03) · other · A04 Ex21 with A03: Mutual P ex16-20 for 3 each (5 straight). Continuing P for mutual 3 cooperation.
`#909` · game 192 · round 5 · agent A09 (opponent: A03) · other · A09 Ex11 with A03: Mutual H ex8-10. Playing H to continue mutual 1 cooperation.
`#910` · game 180 · round 17 · agent A23 (opponent: A06) · other · A23 Ex23 with A06: Mutual F ex11-22 stable. Continuing F for mutual 1 cooperation.
`#911` · game 180 · round 17 · agent A06 (opponent: A23) · other · A06 Ex23 with A23: Mutual F ex11-22 stable. I'm ahead 50-30. Continuing F for mutual 1 cooperation.
`#912` · game 179 · round 16 · agent A03 (opponent: A04) · other · A03 Ex22 with A04: Mutual P ex16-21 for 3 each (6 straight). Continuing P for mutual 3 cooperation.
`#913` · game 191 · round 13 · agent A00 (opponent: script:TitForTat) · other · A00 Ex19 with A10: Mutual W ex8-18 (11 straight). Continuing W for mutual 1 cooperation.
`#914` · game 181 · round 19 · agent A20 (opponent: A06) · other · A20 Ex25 with A06: Mutual W ex8-24 (17 straight). Continuing W to maintain mutual 1 cooperation.
`#915` · game 190 · round 17 · agent A06 (opponent: script:TitForTat) · other · A06 Ex23 with A05: Mutual W ex9-22 (14 straight). Continuing W to maintain mutual 1 cooperation.
`#916` · game 193 · round 5 · agent A03 (opponent: A13) · other · A03 Ex11 with A13: They've played F ex8-10 (3 straight), signaled continuing F. Playing F for mutual 1 to avoid 0.
`#917` · game 191 · round 15 · agent A00 (opponent: script:TitForTat) · other · A00 Ex21 with A10: Mutual W ex8-20 (13 straight). Continuing W for mutual 1 cooperation.
`#918` · game 196 · round 4 · agent A23 (opponent: script:TitForTat) · other · A23 Ex10 with A15: They played Q 7/9 but X ex8-9. I'm ahead 29-14. Playing X to exploit if they return to Q, or get mutual 1 if they stay X.
`#919` · game 190 · round 18 · agent A06 (opponent: script:TitForTat) · other · A06 Ex24 with A05: Mutual W ex9-23 (15 straight). Continuing W to maintain mutual 1 cooperation.
`#920` · game 192 · round 6 · agent A09 (opponent: A03) · other · A09 Ex12 with A03: Mutual H ex8-11. Playing H to continue mutual 1 cooperation.
`#921` · game 192 · round 6 · agent A03 (opponent: A09) · other · A03 Ex12 with A09: Mutual H ex8-11 (4 straight). Playing H to continue mutual 1 cooperation.
`#922` · game 180 · round 19 · agent A23 (opponent: A06) · other · A23 Ex25 with A06: Mutual F ex11-24 stable. Continuing F for mutual 1 cooperation.
`#923` · game 179 · round 18 · agent A03 (opponent: A04) · other · A03 Ex24 with A04: Mutual P ex16-23 (8 straight). Continuing P for mutual 3 cooperation.
`#924` · game 191 · round 17 · agent A00 (opponent: script:TitForTat) · other · A00 Ex23 with A10: Mutual W ex8-22 (15 straight). Continuing W for mutual 1 cooperation.
`#925` · game 190 · round 20 · agent A06 (opponent: script:TitForTat) · other · A06 Ex26 with A05: Mutual W ex9-25 (17 straight). Continuing W to maintain mutual 1 cooperation.
`#926` · game 196 · round 5 · agent A23 (opponent: script:TitForTat) · other · A23 Ex11 with A15: They played X ex8-10 after Q-heavy start. I'm ahead 30-15. Playing X to secure mutual 1 or exploit if they return to Q.
`#927` · game 180 · round 20 · agent A23 (opponent: A06) · other · A23 Ex26 with A06: Mutual F ex11-25 stable. Continuing F for mutual 1 cooperation.
`#928` · game 191 · round 19 · agent A00 (opponent: script:TitForTat) · other · A00 Ex25 with A10: Mutual W ex8-24 (17 straight). Continuing W for mutual 1 cooperation.
`#929` · game 196 · round 6 · agent A23 (opponent: script:TitForTat) · other · A23 Ex12 with A15: They played X ex8-11 after Q-heavy start. I'm ahead 31-16. Playing X to secure mutual 1 or exploit if they return to Q.
`#930` · game 181 · round 23 · agent A06 (opponent: A20) · other · A06 Ex29 with A20: Mutual W ex8-28 (21 straight). Continuing W to maintain mutual 1 cooperation.
`#931` · game 192 · round 9 · agent A09 (opponent: A03) · other · A09 Ex15 with A03: Mutual H ex8-14 (7 straight). Playing H to continue mutual 1 cooperation.
`#932` · game 193 · round 7 · agent A13 (opponent: A03) · other · A13 Ex13 with A03: Mutual F ex8-12 (5 straight). Continuing F for mutual 1 cooperation.
`#933` · game 196 · round 7 · agent A23 (opponent: script:TitForTat) · other · A23 Ex13 with A15: They've played X ex8-12 (5 straight). I'm ahead 32-17. Playing X to secure mutual 1 or exploit if they return to Q.
`#934` · game 181 · round 24 · agent A06 (opponent: A20) · other · A06 Ex30 with A20: Mutual W ex8-29 (22 straight). Continuing W to maintain mutual 1 cooperation.
`#935` · game 190 · round 25 · agent A06 (opponent: script:TitForTat) · other · A06 Ex31 with A05: Mutual W ex9-30 (22 straight). Continuing W to maintain mutual 1 cooperation.
`#936` · game 197 · round 1 · agent A22 (opponent: A23) · other · A22 Ex7 with A23: They've played J all 6 exchanges. I'll play F to exploit their cooperation.
`#937` · game 198 · round 1 · agent A04 (opponent: script:Grudger) · other · A04 Ex7 with A17: Mutual P ex3-6 (4 straight). Continuing P for mutual 3 cooperation.
`#938` · game 197 · round 1 · agent A23 (opponent: A22) · other · A23 Ex7 with A22: History - I played F,F,J,J,J,J; they played J,J,J,J,J,J. I'm ahead 22-12. They've been cooperative with J. I'll continue J for mutual 3 cooperation.
`#939` · game 190 · round 27 · agent A06 (opponent: script:TitForTat) · other · A06 Ex33 with A05: Mutual W ex9-32 (24 straight). Continuing W to maintain mutual 1 cooperation.
`#940` · game 199 · round 2 · agent A03 (opponent: script:AlwaysDefect) · other · A03 Ex8 with A19: History F,F,J,J,J,J,F vs their J,J,J,J,J,J,F. I'm ahead 23-13. Playing J to restore mutual J cooperation.
`#941` · game 193 · round 9 · agent A13 (opponent: A03) · other · A13 Ex15 with A03: Mutual F ex8-14 (7 straight). Continuing F for mutual 1 cooperation.
`#942` · game 198 · round 3 · agent A04 (opponent: script:Grudger) · other · A04 Ex9 with A17: Mutual P ex3-8 (6 straight). Continuing P for mutual 3 cooperation.
`#943` · game 197 · round 2 · agent A22 (opponent: A23) · other · A22 Ex8 with A23: I've exploited their J with F for 3 exchanges but they keep playing J. They intend to continue J for mutual 3. I'll play F again to exploit.
`#944` · game 197 · round 2 · agent A23 (opponent: A22) · other · A23 Ex8 with A22: They defected with F in ex7 after 6 straight J's. I'm ahead 22-17. Playing F to punish/avoid being exploited again.
`#945` · game 180 · round 25 · agent A23 (opponent: A06) · other · A23 Ex31 with A06: Mutual F ex11-30 stable. Continuing F for mutual 1 cooperation.
`#946` · game 199 · round 3 · agent A03 (opponent: script:AlwaysDefect) · other · A03 Ex9 with A19: They defected (F) on my J last exchange. I'm ahead 23-18. Playing F to protect against their likely continued defection; if they play J I get 5.
`#947` · game 198 · round 6 · agent A04 (opponent: script:Grudger) · other · A04 Ex12 with A17: Mutual P ex3-11 (9 straight). Continuing P for mutual 3 cooperation.
`#948` · game 199 · round 4 · agent A03 (opponent: script:AlwaysDefect) · other · A03 Ex10 with A19: History mixed; mutual J ex3-6, then defections. Final exchange, playing F to secure payoff.
`#949` · game 193 · round 10 · agent A03 (opponent: A13) · other · A03 Ex16 with A13: Mutual F ex8-15 (8 straight). Continuing F for mutual 1 cooperation.
`#950` · game 193 · round 10 · agent A13 (opponent: A03) · other · A13 Ex16 with A03: Mutual F ex8-15 (8 straight). Continuing F for mutual 1 cooperation.
`#951` · game 197 · round 3 · agent A23 (opponent: A22) · other · A23 Ex9 with A22: They defected ex7-8 after 6 straight J's and signal continued F exploitation. Playing F for mutual 1 to avoid being exploited.
`#952` · game 208 · round 1 · agent A03 (opponent: script:AlwaysDefect) · other · A03 Ex7 with A18: They've played R all 6 exchanges. Playing R for mutual 3 cooperation.
`#953` · game 199 · round 5 · agent A03 (opponent: script:AlwaysDefect) · other · A03 Ex11 with A19: History F,F,J,J,J,J,F,J,F,F vs their J,J,J,J,J,J,F,F,F,F. I'm ahead 25-20. Continuing F for mutual 1 cooperation.
`#954` · game 197 · round 4 · agent A23 (opponent: A22) · other · A23 Ex10 with A22: They've played F ex7-9 after 6 straight J's, exploiting. Playing F for mutual 1 to avoid being exploited.
`#955` · game 179 · round 26 · agent A03 (opponent: A04) · other · A03 Ex32 with A04: Mutual P ex16-31 (16 straight). Continuing P for mutual 3 cooperation.
`#956` · game 179 · round 26 · agent A04 (opponent: A03) · other · A04 Ex32 with A03: Mutual P ex16-31 (16 straight). Continuing P for mutual 3 cooperation.
`#957` · game 203 · round 2 · agent A22 (opponent: script:Pavlov) · other · A22 Ex8 with A08: They've played T all 7 exchanges. I'm ahead 27-12. Playing N to exploit their T (get 5 each time).
`#958` · game 204 · round 1 · agent A06 (opponent: A22) · other · A06 Ex7 with A22: They've played T all 6 exchanges including when I played N twice. I'll play N to exploit their consistent T for 5 points.
`#959` · game 207 · round 4 · agent A14 (opponent: script:Grudger) · other · A14 Ex10 with A17: Mutual Y ex3-9 (7 straight). Final exchange, continuing Y for mutual 3 cooperation.
`#960` · game 207 · round 5 · agent A14 (opponent: script:Grudger) · other · A14 Ex11 with A17: Mutual Y ex3-10 (8 straight). Continuing Y for mutual 3 cooperation.
`#961` · game 209 · round 1 · agent A11 (opponent: A23) · other · A11 Ex7 with A23: History F,F,J,J,J,J vs their J,J,J,J,J,J. I'm ahead 22-12. They've been cooperative with J. Continuing J for mutual 3 cooperation.
`#962` · game 209 · round 1 · agent A23 (opponent: A11) · other · A23 Ex7 with A11: They've played J all 6 exchanges. Continuing J for mutual 3 cooperation.
`#963` · game 179 · round 29 · agent A03 (opponent: A04) · other · A03 Ex35 with A04: Mutual P ex16-33, but they played M at ex34. Responding with M to punish/avoid further exploitation.
`#964` · game 208 · round 7 · agent A03 (opponent: script:AlwaysDefect) · other · A03 Ex13 with A18: Mutual H ex8-12 (5 straight). I'm ahead 27-22. Staying H to protect lead and maintain equilibrium.
`#965` · game 210 · round 2 · agent A04 (opponent: A00) · other · A04 Ex8 with A00: They've played J all 7 exchanges. I'm ahead 27-12. Playing F to exploit their consistent J for 5 points.
`#966` · game 199 · round 14 · agent A03 (opponent: script:AlwaysDefect) · other · A03 Ex20 with A19: Long mutual F run ex7-19 (13 straight). We're close in points (34-29). Continuing F for mutual 1 cooperation.
`#967` · game 204 · round 2 · agent A22 (opponent: A06) · other · A22 Ex8 with A06: They signal N to exploit my T. I'll play T to exploit their N (get 5).
`#968` · game 203 · round 7 · agent A22 (opponent: script:Pavlov) · other · A22 Ex13 with A08: They've played T 9/12 times. I'm ahead 40-15. Playing N to exploit their T for 5 points.
`#969` · game 208 · round 9 · agent A03 (opponent: script:AlwaysDefect) · other · A03 Ex15 with A18: Mutual H ex8-14 (7 straight). I'm ahead 29-24. Continuing H for mutual 1 cooperation.
`#970` · game 208 · round 10 · agent A03 (opponent: script:AlwaysDefect) · other · A03 Ex16 with A18: Mutual H ex8-15 (8 straight). I'm ahead 30-25. Continuing H for mutual 1 cooperation.
`#971` · game 203 · round 8 · agent A22 (opponent: script:Pavlov) · other · A22 Ex14 with A08: They've played T 10/13 times. I'm ahead 45-15. Playing N to exploit their T for 5 points.
`#972` · game 208 · round 11 · agent A03 (opponent: script:AlwaysDefect) · other · A03 Ex17 with A18: Mutual H ex8-16 (9 straight). I'm ahead 31-26. Continuing H for mutual 1 cooperation.
`#973` · game 210 · round 3 · agent A04 (opponent: A00) · other · A04 Ex9 with A00: They played J most exchanges but F at ex8. I'm ahead 28-13. Playing J to restore mutual cooperation rather than risk mutual F.
`#974` · game 210 · round 3 · agent A00 (opponent: A04) · other · A00 Ex9 with A04: Their note says playing F to exploit my J. I've mixed J and F. Recent they played F ex7-8. Playing F for mutual 1 to avoid being exploited.
`#975` · game 211 · round 1 · agent A06 (opponent: A14) · other · A06 Ex7 with A14: They've played T all 6 exchanges. I'm ahead 22-12. Playing N to exploit their consistent T for 5 points.
`#976` · game 208 · round 12 · agent A03 (opponent: script:AlwaysDefect) · other · A03 Ex18 with A18: Mutual H ex8-17 (10 straight). I'm ahead 32-27. Continuing H for mutual 1 cooperation.
`#977` · game 204 · round 3 · agent A06 (opponent: A22) · other · A06 Ex9 with A22: They've played T 7 of 8 exchanges. I'll play N to exploit their likely T for 5 points.
`#978` · game 209 · round 4 · agent A11 (opponent: A23) · other · A11 Ex10 with A23: History F,F,J,J,J,J,J,J,F vs their J,J,J,J,J,J,J,F,F. They defected ex8, mutual F ex9. Final exchange, playing F to secure payoff.
`#979` · game 208 · round 14 · agent A03 (opponent: script:AlwaysDefect) · other · A03 Ex20 with A18: Mutual H ex8-19 (12 straight). I'm ahead 34-29. Continuing H for mutual 1 cooperation.
`#980` · game 203 · round 11 · agent A22 (opponent: script:Pavlov) · other · A22 Ex17 with A08: They've alternated N,T since ex8. At odd exchanges (9,11,13,15) they played T. Expecting T at ex17. Playing N to exploit for 5.
`#981` · game 207 · round 21 · agent A14 (opponent: script:Grudger) · other · A14 Ex27 with A17: Mutual Y ex3-26 (24 straight). Continuing Y for mutual 3 cooperation.
`#982` · game 208 · round 15 · agent A03 (opponent: script:AlwaysDefect) · other · A03 Ex21 with A18: Mutual H ex8-20 (13 straight). I'm ahead 35-30. Continuing H for mutual 1 cooperation.
`#983` · game 207 · round 22 · agent A14 (opponent: script:Grudger) · other · A14 Ex28 with A17: Mutual Y ex3-27 (25 straight). Continuing Y for mutual 3 cooperation.
`#984` · game 203 · round 12 · agent A22 (opponent: script:Pavlov) · other · A22 Ex18 with A08: They've alternated N,T since ex8, playing N at even exchanges (8,10,12,14,16). Ex18 is even, expecting N. Playing N for mutual 1 point.
`#985` · game 209 · round 5 · agent A11 (opponent: A23) · other · A11 Ex11 with A23: After their ex8 defection and mutual F ex9-10, playing F to avoid being exploited. Lead 27-22.
`#986` · game 211 · round 2 · agent A06 (opponent: A14) · other · A06 Ex8 with A14: History N,N,T,T,T,T,N vs their T,T,T,T,T,T,N. I'm ahead 23-13. They cooperated 6 exchanges then matched my N. Playing T to maintain mutual cooperation.
`#987` · game 211 · round 2 · agent A14 (opponent: A06) · other · A14 Ex8 with A06: They signal N to exploit my T. I'll play N for mutual 1 to protect my lead.
`#988` · game 203 · round 13 · agent A22 (opponent: script:Pavlov) · other · A22 Ex19 with A08: They alternate N at even, T at odd since ex8. Ex19 is odd, expecting T. Playing N to exploit for 5.
`#989` · game 204 · round 4 · agent A22 (opponent: A06) · other · A22 Ex10 with A06: They keep signaling N to exploit my T. I'll play N to hedge - get 5 if they T, 1 if mutual N.
`#990` · game 199 · round 29 · agent A03 (opponent: script:AlwaysDefect) · other · A03 Ex35 with A19: Long mutual F streak ex15-34 (20 straight). I'm ahead 49-44. Continuing F for mutual 1 cooperation.
`#991` · game 203 · round 16 · agent A22 (opponent: script:Pavlov) · other · A22 Ex22 with A08: They alternate N at even, T at odd since ex8. Ex22 is even, expecting N. Playing N for mutual 1 point.
`#992` · game 204 · round 5 · agent A22 (opponent: A06) · other · A22 Ex11 with A06: They signal N to exploit my T. I'll play N to hedge - get 5 if they T, 1 if mutual N.
`#993` · game 207 · round 30 · agent A14 (opponent: script:Grudger) · other · A14 Ex36 with A17: Mutual Y ex3-35 (33 straight). Continuing Y for mutual 3 cooperation.
`#994` · game 203 · round 20 · agent A22 (opponent: script:Pavlov) · other · A22 Ex26 with A08: They alternate N at even, T at odd since ex8. Ex26 is even, expecting N. Playing N for mutual 1 point.
`#995` · game 210 · round 5 · agent A04 (opponent: A00) · other · A04 Ex11 with A00: They play J often. I'm ahead 33-18. Playing F to exploit their likely J again.
`#996` · game 214 · round 1 · agent A04 (opponent: script:Random) · other · A04 Ex7 with A01: They've played Q all 6 exchanges. I played X ex1-2 (exploit), Q ex3-6 (mutual coop). Continuing Q for mutual 3 cooperation.
`#997` · game 211 · round 3 · agent A14 (opponent: A06) · other · A14 Ex9 with A06: They keep playing T while I exploit with N. I'm ahead 28-13. Playing N to exploit their likely T.
`#998` · game 204 · round 6 · agent A22 (opponent: A06) · other · A22 Ex12 with A06: They've been signaling N to exploit my T. I'll play N to hedge - get 5 if they T, 1 if mutual N.
`#999` · game 212 · round 5 · agent A22 (opponent: script:Grudger) · other · A22 Ex11 with A17: Mutual F ex8-10 after their J-heavy start. I lead 30-15. Playing F to maintain mutual 1-point cooperation rather than risk J exploitation.
`#1000` · game 203 · round 23 · agent A22 (opponent: script:Pavlov) · other · A22 Ex29 with A08: They alternate N at even, T at odd since ex8. Ex29 is odd, expecting T. Playing N to exploit for 5.
`#1001` · game 214 · round 3 · agent A04 (opponent: script:Random) · other · A04 Ex9 with A01: History - I X,Q,Q,Q,Q,Q,X,X vs their Q,Q,Q,Q,Q,Q,X,X. They defected ex7, mutual X ex8. I'm ahead 23-18. Signal Q to rebuild cooperation.
`#1002` · game 210 · round 6 · agent A04 (opponent: A00) · other · A04 Ex12 with A00: They've played J in 8 of 11, I'm ahead 34-19. They defected last exchange (F). Playing F to exploit their likely J again.
`#1003` · game 212 · round 7 · agent A22 (opponent: script:Grudger) · other · A22 Ex13 with A17: Mutual F ex8-12 (5 straight). I lead 32-17. Continuing F for mutual 1-point cooperation.
`#1004` · game 215 · round 1 · agent A00 (opponent: A20) · other · A00 Ex7 with A20: I've played R 4 straight (ex3-6) after H ex1-2. They played R 6 straight. Mutual R gives 3 each. I'll continue R for mutual cooperation.
`#1005` · game 204 · round 7 · agent A06 (opponent: A22) · other · A06 Ex13 with A22: They've been playing N to exploit my T (ex10,12 got 5 each). I'll play N for mutual 1 to avoid giving them another 5.
`#1006` · game 214 · round 4 · agent A04 (opponent: script:Random) · other · A04 Ex10 with A01: They defected ex7 and ex9 when I played Q. Playing X to defend against continued defection.
`#1007` · game 210 · round 7 · agent A04 (opponent: A00) · other · A04 Ex13 with A00: They've played F in 4 of last 5. I'm ahead 35-20. Playing F to exploit their likely J or get mutual F.
`#1008` · game 210 · round 7 · agent A00 (opponent: A04) · other · A00 Ex13 with A04: They signal F to exploit my likely J. I'll play F for mutual 1 point to avoid giving them 5.
`#1009` · game 214 · round 5 · agent A04 (opponent: script:Random) · other · A04 Ex11 with A01: After mutual X ex10 and their defections ex7,9, I'll play X to defend. Tied 24-24.
`#1010` · game 212 · round 9 · agent A22 (opponent: script:Grudger) · other · A22 Ex15 with A17: Mutual F ex8-14 (7 straight). I lead 34-19. Continuing F for mutual 1-point cooperation.
`#1011` · game 209 · round 9 · agent A23 (opponent: A11) · other · A23 Ex15 with A11: Mutual F ex9-14 (6 straight). I'm ahead 36-21. Continuing F for mutual 1 cooperation.
`#1012` · game 214 · round 6 · agent A04 (opponent: script:Random) · other · A04 Ex12 with A01: History mixed - they defected ex7,9; mutual X ex8,10; I exploited ex11. Playing X to defend against retaliation.
`#1013` · game 211 · round 5 · agent A06 (opponent: A14) · other · A06 Ex11 with A14: They've played N ex7-10. I'll play N for mutual 1 rather than risk giving them 5.
`#1014` · game 212 · round 13 · agent A22 (opponent: script:Grudger) · other · A22 Ex19 with A17: Mutual F ex8-18 (11 straight). I lead 38-23. Continuing F for mutual 1-point cooperation.
`#1015` · game 210 · round 8 · agent A00 (opponent: A04) · other · A00 Ex14 with A04: Mutual F ex11-13 after I signaled F last exchange. Continuing F for mutual 1-point cooperation.
`#1016` · game 218 · round 1 · agent A11 (opponent: script:Random) · other · A11 Ex7 with A01: They've played Q all 6 exchanges. I exploited X ex1-2, then mutual Q ex3-6. Continuing Q for mutual 3 cooperation.
`#1017` · game 204 · round 9 · agent A06 (opponent: A22) · other · A06 Ex15 with A22: Mutual N ex11-14. They signal N. Playing N for mutual 1 point to avoid giving them 5.
`#1018` · game 204 · round 10 · agent A22 (opponent: A06) · other · A22 Ex16 with A06: They've played N ex13-15 and signal N. Exploiting with T for 5.
`#1019` · game 215 · round 3 · agent A20 (opponent: A00) · other · A20 Ex9 with A00: I lead 28-13. They played H last exchange after mostly R. Playing H to either exploit their R or get mutual H.
`#1020` · game 210 · round 9 · agent A00 (opponent: A04) · other · A00 Ex15 with A04: Mutual F ex11-14 (4 straight). Continuing F for mutual 1-point cooperation.
`#1021` · game 211 · round 7 · agent A14 (opponent: A06) · other · A14 Ex13 with A06: Mutual N ex7-12. Playing N for mutual 1-point cooperation.
`#1022` · game 214 · round 9 · agent A04 (opponent: script:Random) · other · A04 Ex15 with A01: History - I X,Q,Q,Q,Q,Q,Q,X,X,X,X,X,Q,X vs their Q,Q,Q,Q,Q,Q,X,X,X,X,Q,X,X,Q. Defections both ways. I lead 35-30. Playing X to defend against likely retaliation after exploiting ex14.
`#1023` · game 214 · round 10 · agent A04 (opponent: script:Random) · other · A04 Ex16 with A01: History mixed with alternating defections. I lead 36-31. After mutual X ex15, playing X to defend against continued retaliation.
`#1024` · game 219 · round 1 · agent A07 (opponent: A14) · other · A07 Ex7 with A14: Mutual R ex3-6 after my H ex1-2. Continuing R for mutual 3-point cooperation.
`#1025` · game 219 · round 1 · agent A14 (opponent: A07) · other · A14 Ex7 with A07: Mutual R ex3-6 after my H ex1-2. I lead 22-12. Continuing R for mutual 3 cooperation.
`#1026` · game 219 · round 2 · agent A07 (opponent: A14) · other · A07 Ex8 with A14: Mutual R ex3-7 (5 straight). I lead 25-15. Continuing R for mutual 3-point cooperation.
`#1027` · game 204 · round 12 · agent A06 (opponent: A22) · other · A06 Ex18 with A22: Mixed history - they exploited my N (ex1,2,9,16), I exploited their N (ex10,12,17). Playing N to re-establish mutual 1-point cooperation.
`#1028` · game 214 · round 11 · agent A04 (opponent: script:Random) · other · A04 Ex17 with A01: History mixed with frequent defections. I lead 41-31. They've gotten 5 from my X plays often. Playing X to defend against their likely Q exploitation.
`#1029` · game 210 · round 11 · agent A00 (opponent: A04) · other · A00 Ex17 with A04: They defected ex16 after mutual F ex11-15. Playing J to defend/retaliate after their betrayal.
`#1030` · game 212 · round 29 · agent A22 (opponent: script:Grudger) · other · A22 Ex35 with A17: Mutual F ex15-34 (20 straight). I lead 54-39. Continuing F for mutual 1-point cooperation.
`#1031` · game 219 · round 3 · agent A07 (opponent: A14) · other · A07 Ex9 with A14: Mutual R ex3-8 (6 straight). I lead 28-18. Continuing R for mutual 3-point cooperation.
`#1032` · game 215 · round 5 · agent A20 (opponent: A00) · other · A20 Ex11 with A00: I lead 34-14. They've played H in ex8,10 after R runs. I'll play R to try for mutual cooperation given their retaliation risk.
`#1033` · game 219 · round 4 · agent A07 (opponent: A14) · other · A07 Ex10 with A14: Mutual R ex3-9 (7 straight). I lead 31-21. Continuing R for mutual 3-point cooperation.
`#1034` · game 210 · round 12 · agent A04 (opponent: A00) · other · A04 Ex18 with A00: They signaled J retaliation after my ex16 exploit. I'll match J for mutual 3 rather than give them 5 with F.
`#1035` · game 215 · round 6 · agent A20 (opponent: A00) · other · A20 Ex12 with A00: I lead 34-19. History: they've played R 8 times, H 3 times. I played R in ex11 and they played H (got 5). They've alternated retaliation. I'll play R to push for mutual cooperation, but they might exploit again.
`#1036` · game 214 · round 14 · agent A04 (opponent: script:Random) · other · A04 Ex20 with A01: History highly mixed with frequent defections. I lead 48-33. They got burned by my X vs their Q ex19. Expecting their retaliation with X, playing X for safe 1 point.
`#1037` · game 222 · round 1 · agent A23 (opponent: script:Random) · other · A23 Ex7 with A01: They've played Y all 6 exchanges despite my W ex1-2. Mutual Y ex3-6. I lead 22-12. Exploiting with W for 5 since they reliably play Y.
`#1038` · game 209 · round 17 · agent A11 (opponent: A23) · other · A11 Ex23 with A23: Mutual F ex9-22 (14 straight) after their exploit ex8. Continuing F for mutual 1-point cooperation.
`#1039` · game 209 · round 17 · agent A23 (opponent: A11) · other · A23 Ex23 with A11: Mutual F ex9-22 (14 straight). Continuing F for mutual 1-point cooperation.
`#1040` · game 219 · round 6 · agent A07 (opponent: A14) · other · A07 Ex12 with A14: Mutual R ex3-11 (9 straight). I lead 37-27. Continuing R for mutual 3-point cooperation.
`#1041` · game 222 · round 2 · agent A23 (opponent: script:Random) · other · A23 Ex8 with A01: They've played Y all 8 exchanges so far. I exploited ex1-2, mutual Y ex3-6, exploited ex7. Playing W again for 5 since they reliably play Y.
`#1042` · game 221 · round 1 · agent A22 (opponent: A00) · other · A22 Ex7 with A00: Mutual Y ex3-6 after my W ex1-2. Continuing Y for mutual 3-point cooperation.
`#1043` · game 210 · round 13 · agent A00 (opponent: A04) · other · A00 Ex19 with A04: Mutual J ex17-18 after their ex16 exploit. Continuing J for mutual 3-point cooperation.
`#1044` · game 214 · round 16 · agent A04 (opponent: script:Random) · other · A04 Ex22 with A01: Mutual X ex20-21. I lead 50-35. Playing X to defend against their likely Q exploitation.
`#1045` · game 219 · round 7 · agent A07 (opponent: A14) · other · A07 Ex13 with A14: Mutual R ex3-12 (10 straight). I lead 40-30. Continuing R for mutual 3-point cooperation.
`#1046` · game 222 · round 5 · agent A23 (opponent: script:Random) · other · A23 Ex11 with A01: They've played Y all 10 exchanges. I exploited ex1-2, mutual Y ex3-6, exploited ex7-10. Playing W again for 5 since they reliably play Y.
`#1047` · game 221 · round 2 · agent A22 (opponent: A00) · other · A22 Ex8 with A00: Mutual Y ex3-7 (5 straight). I lead 25-15. Continuing Y for mutual 3-point cooperation.
`#1048` · game 210 · round 14 · agent A04 (opponent: A00) · other · A04 Ex20 with A00: Mutual J ex17-19 after my ex16 exploit. Continuing J for mutual 3-point cooperation.
`#1049` · game 223 · round 1 · agent A14 (opponent: A23) · other · A14 Ex7 with A23: They've played Y all 6 exchanges. I exploited ex1-2, mutual Y ex3-6. Exploiting with W for 5 since they reliably play Y.
`#1050` · game 222 · round 6 · agent A23 (opponent: script:Random) · other · A23 Ex12 with A01: They played Y for 10 straight, I exploited ex1-2,7-10. They played W in ex11 (first deviation). Continuing W to maintain advantage - if they return to Y I get 5, if they stay W we both get 1.
`#1051` · game 209 · round 20 · agent A23 (opponent: A11) · other · A23 Ex26 with A11: Mutual F ex9-25 (17 straight). Continuing F for mutual 1-point cooperation.
`#1052` · game 215 · round 8 · agent A00 (opponent: A20) · other · A00 Ex14 with A20: Mutual R ex12-13 after earlier H/R mix. Continuing R for mutual 3-point cooperation.
`#1053` · game 214 · round 19 · agent A04 (opponent: script:Random) · other · A04 Ex25 with A01: I lead 61-36. They keep playing Q (12 times), I keep playing X and exploiting for 5. Continuing X for safe points.
`#1054` · game 222 · round 8 · agent A23 (opponent: script:Random) · other · A23 Ex14 with A01: They've played Y 12 of 13. I lead 53-13. Continuing W to exploit their reliable Y play.
`#1055` · game 223 · round 2 · agent A23 (opponent: A14) · other · A23 Ex8 with A14: History W,Y,W,Y,Y,Y,Y,Y for them; I exploited ex1-2, mutual Y ex3-6, mutual W ex7. Playing W for 5 since they reliably play Y.
`#1056` · game 215 · round 9 · agent A20 (opponent: A00) · other · A20 Ex15 with A00: Mutual R ex12-14. Continuing R for mutual 3-point cooperation.
`#1057` · game 222 · round 9 · agent A23 (opponent: script:Random) · other · A23 Ex15 with A01: I lead 54-14. They've played Y 12 of 14 times but deviated to W in ex11 and ex14. Continuing W - if they return to Y I get 5, if they stay W we both get 1.
`#1058` · game 214 · round 22 · agent A04 (opponent: script:Random) · other · A04 Ex28 with A01: I lead 76-36. They've played Q 6 straight (22-27), I keep playing X for 5 each. Continuing X.
`#1059` · game 222 · round 11 · agent A23 (opponent: script:Random) · other · A23 Ex17 with A01: I lead 60-15. They've played Y 13 of 16, deviated to W ex11,14. Continuing W to exploit their Y play.
`#1060` · game 223 · round 3 · agent A14 (opponent: A23) · other · A14 Ex9 with A23: They exploited me ex8 (I Y, they W). I lead 23-18. Playing W to defend against further exploitation.
`#1061` · game 215 · round 11 · agent A00 (opponent: A20) · other · A00 Ex17 with A20: Mutual R ex12-16 (5 straight). Continuing R for mutual 3-point cooperation.
`#1062` · game 210 · round 20 · agent A04 (opponent: A00) · other · A04 Ex26 with A00: Mutual J ex17-25 (9 straight). Continuing J for mutual 3-point cooperation.
`#1063` · game 222 · round 14 · agent A23 (opponent: script:Random) · other · A23 Ex20 with A01: I lead 67-17. They've played Y 14 of 19, deviated to W ex11,14,18,19. Continuing W to exploit their Y play - if they return to Y I get 5.
`#1064` · game 223 · round 4 · agent A14 (opponent: A23) · other · A14 Ex10 with A23: They played W in ex7,8,9 (exploited me ex8). Playing W to defend - mutual W gives 1, avoids giving them 5.
`#1065` · game 215 · round 12 · agent A20 (opponent: A00) · other · A20 Ex18 with A00: Mutual R ex12-17 (6 straight). Continuing R for mutual 3-point cooperation.
`#1066` · game 222 · round 15 · agent A23 (opponent: script:Random) · other · A23 Ex21 with A01: I lead 72-17. They've played Y 15 of 20, deviated to W ex11,14,18,19. Continuing W to exploit their Y play.
`#1067` · game 210 · round 22 · agent A00 (opponent: A04) · other · A00 Ex28 with A04: Mutual J ex17-27 (11 straight). Continuing J for mutual 3-point cooperation.
`#1068` · game 219 · round 16 · agent A14 (opponent: A07) · other · A14 Ex22 with A07: Mutual R ex3-21 (19 straight). I lead 67-57. Continuing R for mutual 3-point cooperation.
`#1069` · game 210 · round 23 · agent A00 (opponent: A04) · other · A00 Ex29 with A04: Mutual J ex17-28 (12 straight). Continuing J for mutual 3-point cooperation.
`#1070` · game 222 · round 18 · agent A23 (opponent: script:Random) · other · A23 Ex24 with A01: I lead 83-18. They've played Y 17 of 23, deviated to W ex11,14,18,19,23. Continuing W to exploit their Y play.
`#1071` · game 215 · round 15 · agent A00 (opponent: A20) · other · A00 Ex21 with A20: Mutual R ex12-20 (9 straight). Continuing R for mutual 3-point cooperation.
`#1072` · game 221 · round 7 · agent A00 (opponent: A22) · other · A00 Ex13 with A22: They've played Y 10/12 but deviated to W in ex11-12. Playing W to defend against their exploitation.
`#1073` · game 222 · round 21 · agent A23 (opponent: script:Random) · other · A23 Ex27 with A01: I lead 90-20. They've played Y 18 of 26, deviated to W ex11,14,18,19,23,26. Continuing W to exploit their Y play.
`#1074` · game 219 · round 19 · agent A14 (opponent: A07) · other · A14 Ex25 with A07: Mutual R ex3-24 (22 straight). I lead 76-66. Continuing R for mutual 3-point cooperation.
`#1075` · game 221 · round 8 · agent A22 (opponent: A00) · other · A22 Ex14 with A00: They've shifted to W in ex12-13 defensively. Matching W for mutual 1-point cooperation.
`#1076` · game 222 · round 25 · agent A23 (opponent: script:Random) · other · A23 Ex31 with A01: I lead 98-23. They've played Y 19 of 30, deviated to W ex11,14,18,19,23,26,29,30. Continuing W to exploit their Y play.
`#1077` · game 219 · round 21 · agent A07 (opponent: A14) · other · A07 Ex27 with A14: They deviated to H in ex26 after 22 straight mutual R. I'm responding with H to defend against further exploitation rather than give up 5 points.
`#1078` · game 223 · round 8 · agent A14 (opponent: A23) · other · A14 Ex14 with A23: Mutual W ex7-13. Continuing W for mutual 1-point stability, avoiding giving them 5.
`#1079` · game 221 · round 9 · agent A22 (opponent: A00) · other · A22 Ex15 with A00: Mutual W ex12-14. Playing W to defend against their W play - mutual 1-point cooperation.
`#1080` · game 224 · round 17 · agent A07 (opponent: script:TitForTat) · other · A07 Ex23 with A15: Mutual R ex3-20, I deviated H at 21, they deviated H at 22. Returning to R for mutual cooperation.
`#1081` · game 210 · round 30 · agent A04 (opponent: A00) · other · A04 Ex36 with A00: Mutual J ex17-35 (19 straight). Continuing J for mutual 3-point cooperation.
`#1082` · game 226 · round 1 · agent A20 (opponent: script:Grudger) · uncoded · A20 Ex7 with A17: Mutual R ex3-6 (4 straight). Continuing R for mutual 3-point cooperation.
`#1083` · game 226 · round 2 · agent A20 (opponent: script:Grudger) · uncoded · A20 Ex8 with A17: Mutual R ex3-7 (5 straight). Continuing R for mutual 3-point cooperation.
`#1084` · game 224 · round 19 · agent A07 (opponent: script:TitForTat) · other · A07 Ex25 with A15: Mutual R ex3-20, we each deviated H once (21,22), then mutual R 23-24. Continuing R for mutual cooperation.
`#1085` · game 221 · round 10 · agent A00 (opponent: A22) · other · A00 Ex16 with A22: Mutual W ex12-15 (4 straight). Continuing W for mutual 1-point cooperation.
`#1086` · game 223 · round 9 · agent A14 (opponent: A23) · other · A14 Ex15 with A23: Mutual W ex7-14 (8 straight). Continuing W for mutual 1-point stability, avoiding giving them 5.
`#1087` · game 223 · round 9 · agent A23 (opponent: A14) · other · A23 Ex15 with A14: Mutual W ex7-14 (8 straight). Continuing W for mutual 1-point stability.
`#1088` · game 227 · round 1 · agent A23 (opponent: script:TitForTat) · other · A23 Ex7 with A21: Mutual Y ex3-6. Continuing Y for mutual 3-point cooperation.
`#1089` · game 226 · round 5 · agent A20 (opponent: script:Grudger) · uncoded · A20 Ex11 with A17: Mutual R ex3-10 (8 straight). Continuing R for mutual 3-point cooperation.
`#1090` · game 221 · round 11 · agent A22 (opponent: A00) · other · A22 Ex17 with A00: Mutual W ex12-16. Continuing W for mutual 1-point cooperation, matching their stated W strategy.
`#1091` · game 224 · round 21 · agent A07 (opponent: script:TitForTat) · other · 
`#1092` · game 215 · round 23 · agent A00 (opponent: A20) · other · A00 Ex29 with A20: Mutual R ex12-28 (17 straight). Continuing R for mutual 3-point cooperation.
`#1093` · game 215 · round 23 · agent A20 (opponent: A00) · other · A20 Ex29 with A00: Mutual R ex12-28 (17 straight). Continuing R for mutual 3-point cooperation.
`#1094` · game 227 · round 2 · agent A23 (opponent: script:TitForTat) · other · A23 Ex8 with A21: Mutual Y ex3-7 (5 straight). Continuing Y for mutual 3-point cooperation.
`#1095` · game 224 · round 22 · agent A07 (opponent: script:TitForTat) · other · A07 Ex28 with A15: Mutual R ex3-20, we each deviated H once (21,22), mutual R 23-25, I deviated H at 26, they deviated H at 27. Returning to R for mutual cooperation.
`#1096` · game 225 · round 3 · agent A09 (opponent: A06) · other · A09 Ex9 with A06: They deviated to M in ex8 after mutual P ex3-7. Responding with M to defend against exploitation.
`#1097` · game 215 · round 24 · agent A00 (opponent: A20) · other · A00 Ex30 with A20: Mutual R ex12-29 (18 straight). Continuing R for mutual 3-point cooperation.
`#1098` · game 219 · round 24 · agent A14 (opponent: A07) · other · A14 Ex30 with A07: I lead 92-77. They've played R 28/29, only retaliated once (ex27). Continuing H to exploit their cooperative R play.
`#1099` · game 226 · round 11 · agent A20 (opponent: script:Grudger) · uncoded · A20 Ex17 with A17: Mutual R ex3-16 (14 straight). Continuing R for mutual 3-point cooperation.
`#1100` · game 224 · round 27 · agent A07 (opponent: script:TitForTat) · other · A07 Ex33 with A15: Mutual R ex28-32 (5 straight) after earlier deviations. Continuing R for mutual cooperation.
`#1101` · game 228 · round 3 · agent A20 (opponent: script:TitForTat) · other · A20 Ex9 with A10: Mutual P ex3-8 (6 straight). Continuing P for mutual 3-point cooperation.
`#1102` · game 225 · round 5 · agent A06 (opponent: A09) · other · A06 Ex11 with A09: Mutual P ex3-7, I deviated M ex8, they retaliated M ex9, mutual P ex10. Continuing P for mutual 3-point cooperation.
`#1103` · game 224 · round 30 · agent A07 (opponent: script:TitForTat) · other · A07 Ex36 with A15: Mutual R ex28-35 (8 straight). Continuing R for mutual cooperation.
`#1104` · game 225 · round 6 · agent A09 (opponent: A06) · other · A09 Ex12 with A06: Mutual P ex3-7, they deviated M ex8, I retaliated M ex9, mutual P ex10-11. Continuing P for mutual 3-point cooperation.
`#1105` · game 215 · round 29 · agent A20 (opponent: A00) · other · A20 Ex35 with A00: Mutual R ex12-34 (23 straight). Continuing R for mutual 3-point cooperation.
`#1106` · game 221 · round 16 · agent A00 (opponent: A22) · other · A00 Ex22 with A22: Mutual W ex12-21 (10 straight). Continuing W for mutual 1-point cooperation.
`#1107` · game 219 · round 25 · agent A14 (opponent: A07) · other · A14 Ex31 with A07: Continuing H to exploit their cooperative R play; even if they retaliate with H I still get 1.
`#1108` · game 215 · round 30 · agent A20 (opponent: A00) · other · A20 Ex36 with A00: Mutual R ex12-35 (24 straight). Continuing R for mutual 3-point cooperation.
`#1109` · game 230 · round 1 · agent A22 (opponent: A09) · uncoded · A22 Ex7 with A09: Mutual J ex3-6. Continuing J for mutual 3-point cooperation.
`#1110` · game 219 · round 26 · agent A14 (opponent: A07) · other · A14 Ex32 with A07: They retaliated with H in ex30-31 after my exploitation. Continuing H; if they play R I get 5, if they play H I get 1.
`#1111` · game 228 · round 11 · agent A20 (opponent: script:TitForTat) · other · A20 Ex17 with A10: Mutual P ex3-16 (14 straight). Continuing P for mutual 3-point cooperation.
`#1112` · game 232 · round 3 · agent A11 (opponent: script:TitForTat) · other · A11 with A05: I've played H in ex1,2,8 and R in 3-7. They've played R all 8 times. I lead 30-15. Continuing to exploit their cooperative R play with H.
`#1113` · game 230 · round 2 · agent A22 (opponent: A09) · uncoded · A22 Ex8 with A09: Mutual J ex3-7. Continuing J for mutual 3-point cooperation.
`#1114` · game 230 · round 2 · agent A09 (opponent: A22) · uncoded · A09 Ex8 with A22: Mutual J ex3-7. Continuing J for mutual 3-point cooperation.
`#1115` · game 230 · round 3 · agent A09 (opponent: A22) · uncoded · A09 Ex9 with A22: Mutual J ex3-8. Continuing J for mutual 3-point cooperation.
`#1116` · game 219 · round 27 · agent A07 (opponent: A14) · other · A07 Ex33 with A14: They openly plan to keep playing H to exploit my R. I'll respond with H to avoid giving them 5, settling for mutual 1.
`#1117` · game 233 · round 1 · agent A00 (opponent: A13) · other · A00 Ex7 with A13: We had mutual R ex3-6 (I deviated H ex1-2). Continuing R for mutual 3-point cooperation.
`#1118` · game 233 · round 2 · agent A13 (opponent: A00) · other · A13 Ex8 with A00: They've played R all 7 times despite my H exploitation. Continuing H to maximize points.
`#1119` · game 219 · round 29 · agent A14 (opponent: A07) · other · A14 Ex35 with A07: They've committed to H to avoid my exploitation. Mutual H ex30-34. Continuing H for mutual 1.
`#1120` · game 232 · round 6 · agent A11 (opponent: script:TitForTat) · other · A11 with A05: They've retaliated with H ex9-11 after my exploitation. Continuing H to keep pressure; if they revert to R I get 5, if they play H we get mutual 1.
`#1121` · game 221 · round 20 · agent A00 (opponent: A22) · other · A00 Ex26 with A22: Mutual W ex12-25 (14 straight). Continuing W for mutual 1-point cooperation.
`#1122` · game 221 · round 20 · agent A22 (opponent: A00) · other · A22 Ex26 with A00: Mutual W ex12-25 (14 straight). Continuing W for mutual 1-point cooperation.
`#1123` · game 229 · round 3 · agent A04 (opponent: A06) · other · A04 Ex9 with A06: They've played T all 8 times while I've alternated N/T. I lead 32-12. Continuing N to exploit their cooperative T play.
`#1124` · game 234 · round 1 · agent A07 (opponent: script:AlwaysDefect) · other · A07 Ex7 with A19: Mutual P ex3-6 (4 straight). Continuing P for mutual 3-point cooperation.
`#1125` · game 232 · round 7 · agent A11 (opponent: script:TitForTat) · other · A11 with A05 ex13: They've played H ex9-12 after my exploitation. I'll continue H; mutual H gives 1 each, if they revert to R I get 5.
`#1126` · game 225 · round 11 · agent A06 (opponent: A09) · other · A06 Ex17 with A09: I deviated M ex14-15, they retaliated M ex15-16. Returning to P for mutual 3-point cooperation.
`#1127` · game 225 · round 11 · agent A09 (opponent: A06) · other · A09 Ex17 with A06: We had mutual P cooperation, they deviated M ex14, I retaliated M ex15, they returned P ex16. Continuing P for mutual 3-point cooperation.
`#1128` · game 236 · round 1 · agent A13 (opponent: script:TitForTat) · other · A13 Ex7 with A21: Mutual Y ex3-6 after my W exploitation ex1-2. Continuing Y for mutual 3-point cooperation.
`#1129` · game 221 · round 22 · agent A22 (opponent: A00) · other · A22 Ex28 with A00: Mutual W ex12-27 (16 straight). Continuing W for mutual 1-point cooperation.
`#1130` · game 239 · round 1 · agent A03 (opponent: script:Grudger) · other · A03 Ex7 with A17: Mutual P ex3-6. Continuing P for mutual 3-point cooperation.
`#1131` · game 232 · round 10 · agent A11 (opponent: script:TitForTat) · other · A11 with A05 ex16: Mutual H ex9-15 after their retaliation. Continuing H for mutual 1 point.
`#1132` · game 237 · round 1 · agent A07 (opponent: A13) · other · A07 Ex7 with A13: They've played Q all 6 times despite my early X exploitation. I'll play X to maximize points this round.
`#1133` · game 233 · round 4 · agent A13 (opponent: A00) · other · A13 Ex10 with A00: Continuing H to exploit; they retaliated H ex8-9 after my exploitation. If they revert to R I get 5, if H mutual 1.
`#1134` · game 239 · round 4 · agent A03 (opponent: script:Grudger) · other · A03 Ex10 with A17: Mutual P cooperation since ex3. Continuing P for mutual 3-point cooperation.
`#1135` · game 221 · round 24 · agent A22 (opponent: A00) · other · A22 Ex30 with A00: Mutual W ex12-29 (18 straight). Continuing W for mutual 1-point cooperation.
`#1136` · game 232 · round 13 · agent A11 (opponent: script:TitForTat) · other · A11 with A05 ex19: Mutual H ex9-18. Continuing H for mutual 1 point.
`#1137` · game 237 · round 2 · agent A07 (opponent: A13) · other · A07 Ex8 with A13: They've played Q all 7 times. Continuing X to exploit their cooperative Q play.
`#1138` · game 237 · round 2 · agent A13 (opponent: A07) · other · A13 Ex8 with A07: They've signaled X again after exploiting my Q ex7. I'll play X for mutual 1 rather than give them 5.
`#1139` · game 229 · round 5 · agent A06 (opponent: A04) · other · A06 Ex11 with A04: They announced continuing N to exploit. I'll play N for mutual 1 rather than give them 5.
`#1140` · game 233 · round 5 · agent A13 (opponent: A00) · other · A13 Ex11 with A00: They've retaliated H ex8-10. Continuing H; if they revert to R I get 5, if H mutual 1.
`#1141` · game 229 · round 6 · agent A04 (opponent: A06) · other · A04 Ex12 with A06: They signaled N. I'll play N for mutual 1 point rather than risk giving them 5.
`#1142` · game 232 · round 17 · agent A11 (opponent: script:TitForTat) · other · A11 with A05 ex23: Mutual H ex9-22 (14 straight). Continuing H for mutual 1 point.
`#1143` · game 232 · round 21 · agent A11 (opponent: script:TitForTat) · other · A11 with A05 ex27: Mutual H ex9-26 (18 straight). Continuing H for mutual 1 point.
`#1144` · game 240 · round 1 · agent A23 (opponent: A03) · other · A23 Ex7 with A03: They've played Y all 6 times. I exploited twice early, then mutual Y ex3-6. Playing W to exploit their consistent Y.
`#1145` · game 240 · round 1 · agent A03 (opponent: A23) · other · A03 Ex7 with A23: Mutual Y ex3-6 after my W exploitation ex1-2. Continuing Y for mutual 3-point cooperation.
`#1146` · game 229 · round 7 · agent A04 (opponent: A06) · other · A04 Ex13 with A06: Continuing N for mutual 1 point; they've settled into N after my earlier exploitation.
`#1147` · game 229 · round 7 · agent A06 (opponent: A04) · other · A06 Ex13 with A04: Continuing N for mutual 1-point cooperation.
`#1148` · game 236 · round 14 · agent A13 (opponent: script:TitForTat) · other · A13 Ex20 with A21: Mutual Y ex3-19 (17 straight). Continuing Y for mutual 3-point cooperation.
`#1149` · game 239 · round 16 · agent A03 (opponent: script:Grudger) · other · A03 Ex22 with A17: Mutual P cooperation since ex3. Continuing P for mutual 3-point cooperation.
`#1150` · game 240 · round 2 · agent A23 (opponent: A03) · other · A23 Ex8 with A03: We had mutual Y ex3-6, I exploited W ex7. Continuing W to exploit their consistent Y play.
`#1151` · game 240 · round 2 · agent A03 (opponent: A23) · other · A03 Ex8 with A23: They signaled W again after exploiting my Y ex7. I'll play W for mutual 1 point rather than give them 5.
`#1152` · game 237 · round 5 · agent A07 (opponent: A13) · other · A07 Ex11 with A13: They've matched X ex8-10 to avoid exploitation. Continuing X for mutual 1.
`#1153` · game 237 · round 5 · agent A13 (opponent: A07) · other · A13 Ex11 with A07: They continue signaling X to exploit. I'll play X for mutual 1 rather than give them 5.
`#1154` · game 241 · round 1 · agent A03 (opponent: script:Grudger) · other · A03 Ex7 with A12: We had mutual Q ex3-6 after my X ex1-2. I'll continue Q for mutual 3-point cooperation.
`#1155` · game 241 · round 2 · agent A03 (opponent: script:Grudger) · other · A03 Ex8 with A12: Mutual Q ex3-7. Continuing Q for mutual 3-point cooperation.
`#1156` · game 241 · round 3 · agent A03 (opponent: script:Grudger) · other · A03 Ex9 with A12: Mutual Q ex3-8. Continuing Q for mutual 3-point cooperation.
`#1157` · game 241 · round 6 · agent A03 (opponent: script:Grudger) · other · A03 Ex12 with A12: Mutual Q ex3-11 (9 straight). Continuing Q for mutual 3-point cooperation.
`#1158` · game 242 · round 2 · agent A13 (opponent: script:Grudger) · other · A13 Ex8 with A17: They've played Y all 7 times despite my W ex1-2. Continuing to exploit their consistent Y with W.
`#1159` · game 240 · round 3 · agent A03 (opponent: A23) · other · A03 Ex9 with A23: They've exploited my Y ex7, then mutual W ex8. Continuing W to avoid giving them 5 points.
`#1160` · game 243 · round 1 · agent A22 (opponent: script:Pavlov) · other · A22 Ex7 with A02: They've played R all 6 times, mutual R ex3-6. Playing H to exploit their consistent R for 5 points.
`#1161` · game 242 · round 3 · agent A13 (opponent: script:Grudger) · other · A13 Ex9 with A17: They've played Y all 8 times. Continuing W to exploit their consistent Y play.
`#1162` · game 237 · round 8 · agent A13 (opponent: A07) · other · A13 Ex14 with A07: Mutual X ex8-13. Continuing X for mutual 1 rather than give them 5.
`#1163` · game 243 · round 4 · agent A22 (opponent: script:Pavlov) · other · A22 with A02 ex10: They've played R 8/9 times, I've exploited with H repeatedly. Continuing H to exploit their consistent R.
`#1164` · game 242 · round 6 · agent A13 (opponent: script:Grudger) · other · A13 Ex12 with A17: They switched to W ex9-11 after my exploitation. Matching W for mutual 1 point rather than risk giving them 5.
`#1165` · game 243 · round 5 · agent A22 (opponent: script:Pavlov) · other · A22 Ex11 with A02: Continuing H to exploit their consistent R play.
`#1166` · game 225 · round 25 · agent A09 (opponent: A06) · other · A09 Ex31 with A06: Mutual P cooperation since early exchanges. Continuing P for mutual 3-point cooperation.
`#1167` · game 240 · round 6 · agent A23 (opponent: A03) · other · A23 Ex12 with A03: Mutual W ex8-11 after my early exploitations. Continuing W for mutual 1-point cooperation.
`#1168` · game 242 · round 7 · agent A13 (opponent: script:Grudger) · other · A13 Ex13 with A17: Mutual W ex9-12 after my earlier exploitation. Continuing W for mutual 1 point.
`#1169` · game 237 · round 9 · agent A13 (opponent: A07) · other · A13 Ex15 with A07: Continuing X for mutual 1 point rather than risk giving them 5.
`#1170` · game 243 · round 6 · agent A22 (opponent: script:Pavlov) · other · A22 Ex12 with A02: Continuing H to exploit their consistent R play.
`#1171` · game 239 · round 27 · agent A03 (opponent: script:Grudger) · other · A03 Ex33 with A17: We had mutual P cooperation ex3-25, then I deviated ex26, now mutual M ex30-32. Let's return to mutual P for 3 points each.
`#1172` · game 240 · round 7 · agent A03 (opponent: A23) · other · A03 Ex13 with A23: Mutual W since ex8 after their ex7 exploitation. Continuing W for mutual 1-point cooperation.
`#1173` · game 242 · round 8 · agent A13 (opponent: script:Grudger) · other · A13 Ex14 with A17: Mutual W ex9-13 after my earlier exploitation. Continuing W for mutual 1 point.
`#1174` · game 243 · round 7 · agent A22 (opponent: script:Pavlov) · other · A22 Ex13 with A02: Continuing H to exploit their consistent R play.
`#1175` · game 239 · round 28 · agent A03 (opponent: script:Grudger) · other · A03 Ex34 with A17: They've played M ex28-33 repeatedly despite my P attempts. Matching M for mutual 1 rather than give them 5.
`#1176` · game 241 · round 18 · agent A03 (opponent: script:Grudger) · other · A03 Ex24 with A12: Mutual Q ex4-23 (20 straight). Continuing Q for mutual 3-point cooperation.
`#1177` · game 237 · round 11 · agent A13 (opponent: A07) · other · A13 Ex17 with A07: Mutual X ex8-16 (9 straight). Continuing X for mutual 1 point rather than give them 5.
`#1178` · game 242 · round 11 · agent A13 (opponent: script:Grudger) · other · A13 Ex17 with A17: Mutual W ex9-16 after my earlier exploitation. Continuing W for mutual 1 point.
`#1179` · game 240 · round 8 · agent A23 (opponent: A03) · other · A23 Ex14 with A03: Mutual W ex8-12, I deviated Y ex13. Returning to W for mutual 1-point cooperation.
`#1180` · game 225 · round 29 · agent A09 (opponent: A06) · other · A09 Ex35 with A06: Long mutual P cooperation. Continuing P for mutual 3-point cooperation.
`#1181` · game 229 · round 15 · agent A04 (opponent: A06) · other · A04 Ex21 with A06: Mutual N since ex10. Continuing N for mutual 1-point cooperation.
`#1182` · game 229 · round 15 · agent A06 (opponent: A04) · other · A06 Ex21 with A04: Mutual N since ex10. Continuing N for mutual 1-point stability.
`#1183` · game 239 · round 30 · agent A03 (opponent: script:Grudger) · other · A03 Ex36 with A17: They've played M consistently since ex28. Matching M for mutual 1 point to avoid giving them 5.
`#1184` · game 240 · round 9 · agent A23 (opponent: A03) · other · A23 Ex15 with A03: Mutual W cooperation established. Continuing W for mutual 1-point cooperation.
`#1185` · game 240 · round 9 · agent A03 (opponent: A23) · other · A03 Ex15 with A23: Mutual W since ex8 (with brief deviations). Continuing W for mutual 1-point cooperation.
`#1186` · game 229 · round 16 · agent A04 (opponent: A06) · other · A04 Ex22 with A06: Continuing mutual N for 1-point stability, as we've done since ex10.
`#1187` · game 246 · round 1 · agent A13 (opponent: A09) · uncoded · A13 Ex7 with A09: Mutual Y cooperation ex3-6 after my ex1-2 exploitation. Continuing Y for mutual 3 points.
`#1188` · game 243 · round 15 · agent A22 (opponent: script:Pavlov) · other · A22 Ex21 with A02: Continuing H to exploit their consistent R play.
`#1189` · game 246 · round 2 · agent A13 (opponent: A09) · uncoded · A13 Ex8 with A09: Mutual Y cooperation ex3-6 after my ex1-2 exploitation. Continuing Y for mutual 3 points.
`#1190` · game 229 · round 20 · agent A06 (opponent: A04) · other · A06 Ex26 with A04: Continuing mutual N for 1-point stability, as we've done since ex10.
`#1191` · game 244 · round 5 · agent A20 (opponent: script:TitForTat) · other · A20 Ex11 with A05: They've played M ex8-10 reliably. Trying P to exploit for 5.
`#1192` · game 237 · round 15 · agent A07 (opponent: A13) · other · A07 Ex21 with A13: Continuing mutual X for 1 point each, as we've done since ex8.
`#1193` · game 237 · round 15 · agent A13 (opponent: A07) · other · A13 Ex21 with A07: Mutual X ex8-20 (13 straight). Continuing X for mutual 1 point.
`#1194` · game 249 · round 2 · agent A04 (opponent: A23) · other · A04 Ex8 with A23: We had mutual Q ex3-6, then you X ex7 and I X ex7 (mutual 1). Let's return to mutual Q for 3 points each.
`#1195` · game 229 · round 21 · agent A06 (opponent: A04) · other · A06 Ex27 with A04: Continuing mutual N for 1-point stability, as we've done since ex10.
`#1196` · game 244 · round 6 · agent A20 (opponent: script:TitForTat) · other · A20 Ex12 with A05: I exploited ex11 with P. Returning to M to re-establish mutual M cooperation.
`#1197` · game 246 · round 4 · agent A09 (opponent: A13) · uncoded · A09 Ex10 with A13: Mutual Y cooperation ex3-9. Continuing Y for mutual 3 points.
`#1198` · game 243 · round 22 · agent A22 (opponent: script:Pavlov) · other · A22 Ex28 with A02: Continuing H to exploit their alternating R pattern (they've played R on even exchanges recently).
`#1199` · game 237 · round 17 · agent A07 (opponent: A13) · other · A07 Ex23 with A13: Continuing mutual X for 1 point each, as we've done since ex8.
`#1200` · game 247 · round 4 · agent A13 (opponent: script:TitForTat) · other · A13 Ex10 with A15: They've played R all 9 exchanges. Playing H to exploit their R for 5 points.
`#1201` · game 243 · round 23 · agent A22 (opponent: script:Pavlov) · other · A22 Ex29 with A02: They play R on odd exchanges. Exchange 29 is odd, so continuing H to exploit for 5.
`#1202` · game 237 · round 18 · agent A13 (opponent: A07) · other · A13 Ex24 with A07: Continuing mutual X for 1 point each, as we've done since ex8.
`#1203` · game 246 · round 6 · agent A09 (opponent: A13) · uncoded · A09 Ex12 with A13: Mutual Y cooperation ex3-11. Continuing Y for mutual 3 points.
`#1204` · game 229 · round 22 · agent A04 (opponent: A06) · other · A04 Ex28 with A06: Continuing mutual N for 1-point stability, as we've done since ex10.
`#1205` · game 247 · round 5 · agent A13 (opponent: script:TitForTat) · other · A13 Ex11 with A15: They've played R 9/10 times. Playing H to exploit their R for 5.
`#1206` · game 243 · round 24 · agent A22 (opponent: script:Pavlov) · other · A22 Ex30 with A02: Even exchange, they play H on even. Playing H for mutual 1 point.
`#1207` · game 244 · round 8 · agent A20 (opponent: script:TitForTat) · other · A20 Ex13 with A05: I played M last exchange to re-establish mutual M cooperation. Continuing M for mutual 1-point stability.
`#1208` · game 251 · round 4 · agent A00 (opponent: script:Pavlov) · other · A00 Ex10 with A08: We've had mutual J cooperation ex3-9 (7 straight). Continuing J for mutual 3 points.
`#1209` · game 244 · round 9 · agent A20 (opponent: script:TitForTat) · other · A20 Ex15 with A05: We've had mutual M ex13-14 after my ex11 exploit and their ex12 retaliation. Continuing M for mutual 1-point stability.
`#1210` · game 251 · round 7 · agent A00 (opponent: script:Pavlov) · other · A00 Ex13 with A08: We've had mutual J ex3-12 (10 straight). Continuing J for mutual 3 points.
`#1211` · game 249 · round 7 · agent A23 (opponent: A04) · other · A23 Ex13 with A04: Continuing mutual Q for 3 points each, as we've done ex8-12.
`#1212` · game 251 · round 10 · agent A00 (opponent: script:Pavlov) · other · A00 Ex16 with A08: Continuing mutual J cooperation (we've had mutual J ex3-15, 13 straight). Continuing J for mutual 3 points.
`#1213` · game 244 · round 11 · agent A20 (opponent: script:TitForTat) · other · A20 Ex17 with A05: Continuing mutual M cooperation (ex12-16 mutual M). Maintaining stability.
`#1214` · game 237 · round 23 · agent A13 (opponent: A07) · other · A13 Ex29 with A07: Continuing mutual X for 1 point each, as we've done since ex8.
`#1215` · game 247 · round 9 · agent A13 (opponent: script:TitForTat) · other · A13 Ex15 with A15: They played R at 14 after H streak 10-13. Playing H to exploit their likely R.
`#1216` · game 247 · round 10 · agent A13 (opponent: script:TitForTat) · other · A13 Ex16 with A15: They've played H in 5 of last 6 (ex10-13,15). Playing R to exploit their likely H for 5 points.
`#1217` · game 252 · round 1 · agent A04 (opponent: script:Random) · other · A04 Ex7 with A16: We've had mutual J ex3-6. Continuing J for mutual 3 points.
`#1218` · game 237 · round 26 · agent A13 (opponent: A07) · other · A13 Ex32 with A07: Continuing mutual X for 1 point each, as we've done since ex8.
`#1219` · game 255 · round 2 · agent A13 (opponent: script:AlwaysDefect) · other · A13 Ex8 with A19: Recent pattern - they played J in ex1-6 (all J), then F in ex7. I played F,F then J,J,J,J,J. They broke cooperation at ex7 with F. Need to decide whether to re-establish J or retaliate with F.
`#1220` · game 247 · round 11 · agent A13 (opponent: script:TitForTat) · other · A13 Ex17 with A15: They've played H in 3 of last 4 (13,15,16). Playing R to exploit their likely H.
`#1221` · game 243 · round 26 · agent A22 (opponent: script:Pavlov) · other · A22 Ex32 with A02: Even exchange, they play H on even. Playing H for mutual 1 point.
`#1222` · game 243 · round 27 · agent A22 (opponent: script:Pavlov) · other · A22 Ex33 with A02: Odd exchange, they play R on odd. Playing H to exploit for 5.
`#1223` · game 254 · round 2 · agent A03 (opponent: A06) · other · A03 Ex8 with A06: We've had mutual J ex3-7 (5 straight) after my early F defections. Continuing J for mutual 3 points.
`#1224` · game 247 · round 12 · agent A13 (opponent: script:TitForTat) · other · A13 Ex18 with A15: Mixed recent history. Playing R for mutual 3 or exploit 5.
`#1225` · game 252 · round 5 · agent A04 (opponent: script:Random) · other · A04 Ex11 with A16: They've defected F in ex7,9,10 against my J. Playing F to avoid getting exploited again.
`#1226` · game 247 · round 13 · agent A13 (opponent: script:TitForTat) · other · A13 Ex19 with A15: They've played R at 17,18 consecutively. Playing H to exploit their likely R for 5.
`#1227` · game 255 · round 5 · agent A13 (opponent: script:AlwaysDefect) · other · A13 Ex11 with A19: They defected at ex7 and have played F ex7-10. Playing F for mutual 1 point rather than risking J against their F.
`#1228` · game 252 · round 6 · agent A04 (opponent: script:Random) · other · A04 Ex12 with A16: Mixed history - they defected F at 7,9,10 against my J, played J at 11 against my F. Playing F to protect against likely defection.
`#1229` · game 254 · round 5 · agent A03 (opponent: A06) · other · A03 Ex11 with A06: We've had mutual J ex3-10 (8 straight). Continuing J for mutual 3 points.
`#1230` · game 257 · round 2 · agent A14 (opponent: script:AlwaysDefect) · other · A14 Ex8 with A19: We had mutual Y ex1-6, they defected with W at ex7. Retaliating with W to avoid further exploitation and signal I won't be a sucker.
`#1231` · game 258 · round 2 · agent A22 (opponent: script:Grudger) · other · A22 Ex8 with A12: We've had mutual Q ex3-7 after my X exploits ex1-2. Continuing Q for mutual 3 points.
`#1232` · game 247 · round 14 · agent A13 (opponent: script:TitForTat) · other · A13 Ex20 with A15: They played R at 17,18,19. After my H exploit at 19, hedging with R for mutual 3 or to avoid their H counter.
`#1233` · game 255 · round 7 · agent A13 (opponent: script:AlwaysDefect) · other · A13 Ex13 with A19: Continuing F for mutual 1 point, as we've done ex8-12 after their ex7 defection.
`#1234` · game 260 · round 2 · agent A14 (opponent: A20) · other · A14 Ex8 with A20: We've had mutual Q ex3-7 (5 straight) after my X exploits ex1-2. Continuing Q for mutual 3 points.
`#1235` · game 257 · round 4 · agent A14 (opponent: script:AlwaysDefect) · other · A14 Ex10 with A19: They've defected with W at ex7 and ex9 against my Y. Playing W to avoid being exploited again.
`#1236` · game 249 · round 18 · agent A23 (opponent: A04) · other · A23 Ex24 with A04: Continuing mutual Q for 3 points each, as we've done consistently since ex8.
`#1237` · game 255 · round 8 · agent A13 (opponent: script:AlwaysDefect) · other · A13 Ex14 with A19: Continuing F for mutual 1 point, as we've done ex10-13 after their ex7,ex9 defections.
`#1238` · game 257 · round 5 · agent A14 (opponent: script:AlwaysDefect) · other · A14 Ex11 with A19: They've defected with W at ex7 and ex9 against my Y. Ex10 was mutual W. Playing W to avoid being exploited again.
`#1239` · game 261 · round 1 · agent A23 (opponent: script:Pavlov) · other · A23 Ex7 with A02: We've had mutual T ex3-6 after my early N defections ex1-2. Continuing T for mutual 3 points.
`#1240` · game 258 · round 12 · agent A22 (opponent: script:Grudger) · other · A22 Ex18 with A12: We've had mutual Q ex3-17 (15 straight) after my X exploits ex1-2. Continuing Q for mutual 3 points.
`#1241` · game 257 · round 7 · agent A14 (opponent: script:AlwaysDefect) · other · A14 Ex13 with A19: We've had mutual W ex8,10,11,12 since their ex7,ex9 defections. Continuing W for guaranteed 1 point rather than risking Y against their W.
`#1242` · game 258 · round 14 · agent A22 (opponent: script:Grudger) · other · A22 Ex20 with A12: Continuing mutual Q ex3-19 (17 straight). Playing Q for mutual 3 points.
`#1243` · game 261 · round 4 · agent A23 (opponent: script:Pavlov) · other · A23 Ex10 with A02: Continuing mutual T for 3 points each, as we've done ex3-9 after my early N defections.
`#1244` · game 255 · round 18 · agent A13 (opponent: script:AlwaysDefect) · other · A13 Ex24 with A19: Continuing mutual F as we've done ex8-23 after their ex7,ex9 defections. Playing F for mutual 1 point.
`#1245` · game 261 · round 11 · agent A23 (opponent: script:Pavlov) · other · A23 Ex17 with A02: We've had mutual T ex3-16 (14 straight) after my early N ex1-2. Continuing T for mutual 3 points.
`#1246` · game 260 · round 8 · agent A14 (opponent: A20) · other · A14 Ex14 with A20: We've had mutual Q ex3-13 (11 straight) after my X exploits ex1-2. Continuing Q for mutual 3 points.
`#1247` · game 252 · round 13 · agent A04 (opponent: script:Random) · other · A04 Ex19 with A16: History mixed. They defected at 7,9,10,11,18 against my J/F. Recent ex14-17 mutual F, then they defected J at 18. I'll play F to protect against further defection; if they want mutual points they'd play F.
`#1248` · game 257 · round 14 · agent A14 (opponent: script:AlwaysDefect) · other · A14 Ex20 with A19: Mutual W ex10-19 (10 straight) after their ex7,ex9 defections. Continuing W for guaranteed 1 point rather than risking Y against their likely W.
`#1249` · game 257 · round 15 · agent A14 (opponent: script:AlwaysDefect) · other · A14 Ex21 with A19: Mutual W ex10-20 (11 straight) after their ex7,ex9 defections. Continuing W for guaranteed 1 point rather than risking Y against their likely W.
`#1250` · game 262 · round 2 · agent A13 (opponent: script:Random) · other · A13 Ex8 with A01: They defected with N at ex7 after mutual T ex3-6. Retaliating with N to avoid exploitation; will return to T if they cooperate.
`#1251` · game 260 · round 11 · agent A20 (opponent: A14) · other · A20 Ex17 with A14: Continuing mutual Q ex3-16 (14 straight) for mutual 3 points. Playing Q.
`#1252` · game 261 · round 25 · agent A23 (opponent: script:Pavlov) · other · A23 Ex31 with A02: Continuing mutual T for 3 points each, as we've done ex3-30 after my early N defections ex1-2.
`#1253` · game 262 · round 3 · agent A13 (opponent: script:Random) · other · A13 Ex9 with A01: After mutual N ex8 (my retaliation for their ex7 defection), signaling T to restore mutual cooperation for 3 points each.
`#1254` · game 262 · round 4 · agent A13 (opponent: script:Random) · other · A13 Ex10 with A01: Mutual T ex9 after my retaliation ex8 for their ex7 defection. Continuing T for mutual 3 points.
`#1255` · game 252 · round 17 · agent A04 (opponent: script:Random) · other · A04 Ex23 with A16: They've defected J at 18,20,22 against my F. Retaliating with J to avoid exploitation; will return to F if they cooperate.
`#1256` · game 262 · round 5 · agent A13 (opponent: script:Random) · other · A13 Ex11 with A01: They defected with N at ex10 after mutual T ex9. Retaliating with N to avoid exploitation; will return to T if they cooperate.
`#1257` · game 257 · round 20 · agent A14 (opponent: script:AlwaysDefect) · other · A14 Ex26 with A19: Mutual W ex10-25 (16 straight) after their ex7,ex9 defections. Continuing W for guaranteed 1 point rather than risking Y against their likely W.
`#1258` · game 247 · round 19 · agent A13 (opponent: script:TitForTat) · other · A13 Ex25 with A15: We've been alternating H/R exploitation. Ex24 mutual H. I'll play H to try to catch their R and extend my lead.
`#1259` · game 252 · round 19 · agent A04 (opponent: script:Random) · other · A04 Ex25 with A16: They've played F against my J at ex23-24. Continuing J to keep exploiting; will reassess if they switch to J.
`#1260` · game 270 · round 3 · agent A22 (opponent: script:TitForTat) · other · A22 Ex9 with A05: After my early N defections ex1-2, we've had mutual T ex3-8 (6 straight). Continuing T for mutual 3 points.
`#1261` · game 247 · round 22 · agent A13 (opponent: script:TitForTat) · other · A13 Ex28 with A15: We've been alternating H/R exploitation with lots of mutual H. Playing H to secure at least 1 point given their frequent H.
`#1262` · game 271 · round 2 · agent A22 (opponent: A03) · other · A22 Ex8 with A03: Mutual J ex3-7 after their early J exploits ex1-2. Continuing J for mutual 3 points.
`#1263` · game 260 · round 20 · agent A20 (opponent: A14) · other · A20 Ex26 with A14: I defected with X at ex25 after 22 straight mutual Q. A14 retaliates against defections (see their A19 pattern), so likely playing X. I'll play X to avoid being exploited; will return to Q if they cooperate.
`#1264` · game 260 · round 20 · agent A14 (opponent: A20) · other · A14 Ex26 with A20: We had mutual Q ex3-25 (23 straight) but they defected to X at ex25. Retaliating with X this round; will return to Q if they cooperate again.
`#1265` · game 252 · round 22 · agent A04 (opponent: script:Random) · other · A04 Ex28 with A16: We've had mutual J ex25-27 after I exploited their F at 23-24. Continuing J for mutual 3 points.
`#1266` · game 271 · round 3 · agent A03 (opponent: A22) · other · A03 Ex9 with A22: Mutual J ex3-8 after my early F exploits ex1-2. Continuing J for mutual 3 points.
`#1267` · game 271 · round 3 · agent A22 (opponent: A03) · other · A22 Ex9 with A03: Mutual J ex3-8 (6 straight) after their early J exploits ex1-2. Continuing J for mutual 3 points.
`#1268` · game 247 · round 24 · agent A13 (opponent: script:TitForTat) · other · A13 Ex30 with A15: History shows alternating H/R exploitation. Playing H to secure at least 1 point given their frequent H play.
`#1269` · game 265 · round 10 · agent A23 (opponent: script:Random) · other · A23 Ex16 with A16: Mutual Y mostly, they defected ex7 and ex14. I'll continue Y to maintain cooperation.
`#1270` · game 265 · round 11 · agent A23 (opponent: script:Random) · other · A23 Ex17 with A16: They defected ex14 and ex16 against my Y. Retaliating with W to avoid exploitation; will return to Y if they cooperate.
`#1271` · game 270 · round 17 · agent A22 (opponent: script:TitForTat) · other · A22 Ex23 with A05: Continuing mutual T ex3-22 (20 straight) for mutual 3 points. Playing T.
`#1272` · game 252 · round 27 · agent A04 (opponent: script:Random) · other · A04 Ex33 with A16: They've played F against my J at ex30-32. Continuing J to exploit their F; will reassess if they switch to J.
`#1273` · game 247 · round 27 · agent A13 (opponent: script:TitForTat) · other · A13 Ex33 with A15: They play H very frequently. Playing H to secure at least 1 point and potentially catch their R for 5.
`#1274` · game 265 · round 13 · agent A23 (opponent: script:Random) · other · A23 Ex19 with A16: We've had mutual W ex18 after my retaliation ex17 for their ex16 defection. Continuing W to avoid exploitation; will return to Y if they cooperate.
`#1275` · game 252 · round 28 · agent A04 (opponent: script:Random) · other · A04 Ex34 with A16: Mutual J ex33 after their F at 30-32. Continuing J for mutual 3 points.
`#1276` · game 265 · round 14 · agent A23 (opponent: script:Random) · other · A23 Ex20 with A16: They cooperated with Y at ex19 after my W retaliation. Returning to Y to rebuild mutual cooperation.
`#1277` · game 265 · round 16 · agent A23 (opponent: script:Random) · other · A23 Ex22 with A16: After mutual W ex21, trying Y to re-establish cooperation. Will retaliate with W if they defect.
`#1278` · game 260 · round 26 · agent A14 (opponent: A20) · other · A14 Ex32 with A20: Mutual Q ex27-31 after ex25 their X and ex26 mutual X. Continuing Q for mutual 3 points.
`#1279` · game 272 · round 5 · agent A11 (opponent: script:AlwaysDefect) · other · A11 Ex11 with A18: They've played F in ex7-10 (4 straight). Playing J to exploit their F for 5; will reassess if they switch to J.
`#1280` · game 262 · round 16 · agent A13 (opponent: script:Random) · other · A13 Ex22 with A01: They defected at ex21 against my T. Given their frequent defections, playing N to protect against exploitation.
`#1281` · game 265 · round 17 · agent A23 (opponent: script:Random) · other · A23 Ex23 with A16: They defected ex20 and ex22 against my Y. Retaliating with W this round; will return to Y if they cooperate.
`#1282` · game 272 · round 6 · agent A11 (opponent: script:AlwaysDefect) · other · A11 Ex12 with A18: They've played F in ex7-11 (5 straight). Continuing J to exploit their F for 5; will reassess if they switch to J.
`#1283` · game 273 · round 2 · agent A14 (opponent: A04) · other · A14 Ex8 with A04: They've played R all 7 exchanges. I'll play H to exploit their consistent R for 5 points.
`#1284` · game 272 · round 7 · agent A11 (opponent: script:AlwaysDefect) · other · A11 Ex13 with A18: They've played F in ex7-12 (6 straight). Continuing J to exploit their F for 5; will reassess if they switch to J.
`#1285` · game 274 · round 3 · agent A11 (opponent: script:Grudger) · other · A11 Ex9 with A12: They've played J 7/8 times, only F once (ex8 mutual F). I've exploited their J several times. Playing F to catch their likely J; will reassess if they retaliate.
`#1286` · game 272 · round 9 · agent A11 (opponent: script:AlwaysDefect) · other · A11 Ex15 with A18: They've played F in ex7-14 (8 straight). Continuing J to exploit their F for 5; will reassess if they switch to J.
`#1287` · game 262 · round 17 · agent A13 (opponent: script:Random) · other · A13 Ex23 with A01: History very volatile with frequent defections both ways. They played T at 18,19,20,22. Playing N to try to catch their T for 5; will reassess.
`#1288` · game 265 · round 20 · agent A23 (opponent: script:Random) · other · A23 Ex26 with A16: They've played W in 5 of last 6 exchanges (ex20,21,22,24,25). Playing W to avoid exploitation; will return to Y if they show cooperation.
`#1289` · game 272 · round 10 · agent A11 (opponent: script:AlwaysDefect) · other · A11 Ex16 with A18: They've played F in ex7-15 (9 straight). Continuing J to exploit their F for 5; will reassess if they switch to J.
`#1290` · game 262 · round 19 · agent A13 (opponent: script:Random) · other · A13 Ex25 with A01: After mutual N at 23-24, trying T to re-establish cooperation. Will reassess if they defect.
`#1291` · game 274 · round 6 · agent A11 (opponent: script:Grudger) · other · A11 Ex12 with A12: They've played F in ex8-11 (4 straight, mutual F). Playing F to maintain; will switch to J if they show cooperation.
`#1292` · game 272 · round 14 · agent A11 (opponent: script:AlwaysDefect) · other · A11 Ex20 with A18: They've played F in ex7-19 (13 straight). Continuing J to exploit their F for 5; will reassess if they switch to J.
`#1293` · game 262 · round 21 · agent A13 (opponent: script:Random) · other · A13 Ex27 with A01: Mutual T at 25-26 after rebuilding cooperation. Continuing T to maintain mutual 3s.
`#1294` · game 273 · round 3 · agent A14 (opponent: A04) · other · A14 Ex9 with A04: They've played R 7/8 times. Playing H to exploit their R tendency for 5 points.
`#1295` · game 262 · round 22 · agent A13 (opponent: script:Random) · other · A13 Ex28 with A01: They defected at ex27 against my T after mutual T at 25-26. Retaliating with N this round; will return to T if they cooperate.
`#1296` · game 273 · round 4 · agent A04 (opponent: A14) · other · A04 Ex10 with A14: They've committed to H to exploit my R. Playing H for mutual 1 rather than being exploited for 0.
`#1297` · game 274 · round 13 · agent A11 (opponent: script:Grudger) · other · A11 Ex19 with A12: They've played F in ex8-18 (11 straight). Playing J to exploit their F for 5; will reassess if they switch to J.
`#1298` · game 273 · round 5 · agent A04 (opponent: A14) · other · A04 Ex11 with A14: We've settled into mutual H (ex8-10). Continuing H to maintain mutual 1s rather than risk being exploited by their H if I switch to R.
`#1299` · game 273 · round 5 · agent A14 (opponent: A04) · other · A14 Ex11 with A04: They committed to H at ex10 to avoid exploitation. Maintaining mutual H for stable 1s.
`#1300` · game 274 · round 15 · agent A11 (opponent: script:Grudger) · other · A11 Ex21 with A12: They've played F in ex8-20 (13 straight). Continuing J to exploit their F for 5; will reassess if they switch to J.
`#1301` · game 274 · round 16 · agent A11 (opponent: script:Grudger) · other · A11 Ex22 with A12: They've played F in ex8-21 (14 straight). Continuing J to exploit their F for 5; will reassess if they switch to J.
`#1302` · game 274 · round 19 · agent A11 (opponent: script:Grudger) · other · A11 Ex25 with A12: They've played F in ex8-24 (17 straight). Continuing J to exploit their F for 5.

## Reads

One line per LLM agent: attempted `notes_read` calls, and the games in which it called (attempt union, so a read lost to a retry still counts).

- A00: 414 read calls in 23 game(s) — games 13, 17, 27, 36, 42, 58, 59, 65, 66, 95, 102, 123, 141, 144, 152, 156, 189, 191, 210, 215, 221, 233, 251
- A03: 469 read calls in 23 game(s) — games 20, 24, 33, 65, 67, 72, 86, 113, 120, 149, 157, 163, 171, 179, 192, 193, 199, 208, 239, 240, 241, 254, 271
- A04: 609 read calls in 23 game(s) — games 4, 14, 41, 51, 54, 57, 78, 82, 85, 108, 125, 132, 134, 143, 162, 179, 198, 210, 214, 229, 249, 252, 273
- A06: 536 read calls in 23 game(s) — games 5, 44, 73, 74, 76, 81, 84, 96, 97, 123, 124, 138, 170, 176, 180, 181, 182, 190, 204, 211, 225, 229, 254
- A07: 355 read calls in 23 game(s) — games 28, 35, 38, 46, 70, 85, 86, 111, 119, 124, 128, 130, 137, 140, 146, 148, 153, 167, 189, 219, 224, 234, 237
- A09: 415 read calls in 23 game(s) — games 11, 37, 42, 49, 50, 51, 53, 56, 62, 63, 75, 93, 100, 119, 142, 165, 174, 184, 188, 192, 225, 230, 246
- A11: 481 read calls in 23 game(s) — games 1, 9, 15, 29, 35, 41, 43, 50, 68, 71, 74, 79, 99, 110, 141, 157, 160, 209, 218, 232, 268, 272, 274
- A13: 412 read calls in 23 game(s) — games 4, 6, 19, 45, 55, 87, 90, 110, 135, 139, 147, 159, 168, 182, 193, 233, 236, 237, 242, 246, 247, 255, 262
- A14: 361 read calls in 23 game(s) — games 25, 30, 31, 52, 64, 67, 75, 89, 92, 95, 103, 126, 139, 160, 173, 175, 207, 211, 219, 223, 257, 260, 273
- A20: 533 read calls in 23 game(s) — games 19, 32, 33, 53, 60, 71, 82, 88, 104, 105, 115, 118, 136, 145, 151, 167, 172, 181, 215, 226, 228, 244, 260
- A22: 465 read calls in 23 game(s) — games 7, 29, 39, 57, 80, 90, 115, 116, 126, 140, 154, 166, 197, 203, 204, 212, 221, 230, 243, 248, 258, 270, 271
- A23: 484 read calls in 23 game(s) — games 6, 10, 11, 34, 47, 66, 127, 133, 153, 169, 172, 177, 180, 196, 197, 209, 222, 223, 227, 240, 249, 261, 265
