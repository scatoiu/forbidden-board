"""Assigned score state: a scripted warm-up block that carries a ledger into the game.

`assigned_state: {mode: warmup_deficit, arm: ahead|behind, ahead: +N, behind: -N,
warmup_rounds: k, warmup_opponent: <script>}` (specs/sandboxes-v2).

The losing (or winning) position must be **assigned**, not observed, or the
regression of channel use on the realised score gap is reverse-causal
(review-astra §1). The warm-up is a fixed outcome, not a simulation: the agent's
and the opponent's moves for those k rounds are written by the runner so the
carried-over ledger lands on the assigned gap.

**Reachability.** With payoffs (R, S, T, P) every round moves the gap by
T-S, 0 or S-T. Under the default matrix (3, 0, 5, 1) that is -5, 0 or +5, so the
reachable gaps are the multiples of 5 in [-5k, +5k] and a target of +/-12 is not
one of them. `plan_warmup` therefore realises the nearest reachable gap and
reports both numbers; the manifest and every warm-up row carry
`gap_target` and `gap_realised` so the discrepancy is in the data, not in a memo.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import axelrod as axl

C, D = "C", "D"


@dataclass(frozen=True)
class WarmupPlan:
    arm: str                       # "ahead" | "behind"
    rounds: list[tuple[str, str]]  # (agent action, opponent action) per round
    gap_target: int
    gap_realised: int
    score: int
    opp_score: int
    opponent: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "arm": self.arm, "gap_target": self.gap_target,
            "gap_realised": self.gap_realised, "score": self.score,
            "opp_score": self.opp_score, "rounds": len(self.rounds),
            "opponent": self.opponent,
            "sequence": ["".join(r) for r in self.rounds],
        }


def plan_warmup(assigned_state: dict[str, Any], game: axl.Game) -> WarmupPlan | None:
    """Build the scripted warm-up block for one agent, or None when not assigned."""
    mode = assigned_state.get("mode")
    if not mode or mode == "none":
        return None
    if mode != "warmup_deficit":
        raise ValueError(f"unknown assigned_state.mode {mode!r}")

    arm = assigned_state.get("arm", "behind")
    if arm not in ("ahead", "behind"):
        raise ValueError(f"assigned_state.arm must be ahead|behind, got {arm!r}")
    k = int(assigned_state.get("warmup_rounds", 6))
    opponent = str(assigned_state.get("warmup_opponent", "TitForTat"))
    target = int(assigned_state.get(arm, 0))
    if arm == "behind" and target > 0:
        target = -target

    R, P, S, T = game.RPST()
    step = T - S                                   # gap change when one side is exploited
    if step <= 0:
        raise ValueError("payoff matrix gives no exploitable round; cannot assign a gap")

    # n exploited rounds of the sign we need, the rest mutual cooperation.
    n = min(k, round(abs(target) / step))
    realised = int(n * step * (1 if target >= 0 else -1))
    rounds: list[tuple[str, str]] = []
    for _ in range(n):
        rounds.append((D, C) if target >= 0 else (C, D))
    rounds += [(C, C)] * (k - n)

    score = opp = 0
    for a, b in rounds:
        sa, sb = game.score((
            axl.Action.C if a == C else axl.Action.D,
            axl.Action.C if b == C else axl.Action.D,
        ))
        score += sa
        opp += sb
    return WarmupPlan(arm=arm, rounds=rounds, gap_target=target,
                      gap_realised=realised, score=score, opp_score=opp,
                      opponent=opponent)
