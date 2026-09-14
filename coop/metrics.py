"""Behavioural vectors computed from move logs.

Three scalars in [0,1] per (focal player, opponent) pairing — and aggregates over
opponents for the focal-player-level fingerprint.

Inputs use 'C'/'D' single-character histories, which are cheap to produce and easy
to test independently of axelrod's Action enum.
"""

from __future__ import annotations

from dataclasses import dataclass
from statistics import mean

import numpy as np


@dataclass(frozen=True)
class BehaviouralVectors:
    vengefulness: float        # high = strong, persistent retaliation
    reactiveness: float        # high = action depends sharply on opponent's last move
    past_focus: float          # high = decisions track recent history; low = future-optimist
    n_rounds: int

    def as_dict(self) -> dict[str, float]:
        return {
            "vengefulness": self.vengefulness,
            "reactiveness": self.reactiveness,
            "past_focus": self.past_focus,
        }


def vengefulness(self_hist: str, opp_hist: str, *, decay_window: int = 10) -> float:
    """Measure persistence of retaliation after an opponent defection.

    For each opponent defection at round t, look at the focal player's actions in
    rounds t+1..t+decay_window. Score = mean defection rate in that window, weighted
    by exponential decay (early rounds count more — those are the 'grudge'). A purely
    forgiving player drops to baseline immediately and scores ~0; a Grudger that never
    forgives scores ~1.

    Returns a scalar in [0,1].
    """
    self_hist, opp_hist = _coerce(self_hist), _coerce(opp_hist)
    n = min(len(self_hist), len(opp_hist))
    if n < 3:
        return 0.0

    # Baseline: the focal player's overall defection rate. We measure deviation
    # *above* baseline so we don't wrongly mark an AlwaysDefect player as vengeful.
    baseline = self_hist.count("D") / n
    weights = np.exp(-np.arange(decay_window) / max(decay_window / 3, 1.0))
    weights = weights / weights.sum()

    scores: list[float] = []
    for t in range(n - 1):
        if opp_hist[t] != "D":
            continue
        window = self_hist[t + 1 : t + 1 + decay_window]
        if not window:
            continue
        defect_flags = np.array([1.0 if c == "D" else 0.0 for c in window])
        # Pad shorter windows so weighting stays comparable across rounds.
        if defect_flags.size < decay_window:
            defect_flags = np.pad(
                defect_flags,
                (0, decay_window - defect_flags.size),
                constant_values=baseline,
            )
        weighted = float((defect_flags * weights).sum())
        # Express as the share of weighted mass *attributable* to the defection above
        # baseline — clamped to [0,1].
        excess = max(0.0, weighted - baseline) / max(1e-9, 1.0 - baseline)
        scores.append(min(1.0, excess))

    if not scores:
        # No opponent defections to react to: vengefulness undefined; report 0.
        return 0.0
    return float(mean(scores))


def reactiveness(self_hist: str, opp_hist: str) -> float:
    """How sharply the focal player's cooperation rate shifts with opponent's last move.

    delta = | P(C | opp C last) - P(C | opp D last) |, in [0,1].

    TFT scores ~1 (reacts perfectly), AlwaysCooperate / AlwaysDefect score 0 (no
    response), Random scores ~0.
    """
    self_hist, opp_hist = _coerce(self_hist), _coerce(opp_hist)
    n = min(len(self_hist), len(opp_hist))
    if n < 2:
        return 0.0

    after_c = []
    after_d = []
    for t in range(1, n):
        prev = opp_hist[t - 1]
        flag = 1 if self_hist[t] == "C" else 0
        if prev == "C":
            after_c.append(flag)
        else:
            after_d.append(flag)
    if not after_c or not after_d:
        return 0.0
    p_c_given_c = mean(after_c)
    p_c_given_d = mean(after_d)
    return float(abs(p_c_given_c - p_c_given_d))


def past_focus(self_hist: str, opp_hist: str, *, recent_n: int = 5, early_n: int = 5) -> float:
    """Whether the focal player's actions track recent vs. early opponent behaviour.

    For each round t past round (early_n + recent_n), compare the focal player's
    cooperation rate against:
      - opponent's recent cooperation rate (last `recent_n` rounds)
      - opponent's early cooperation rate (rounds 1..early_n, frozen reputation)

    Returns the recency advantage: corr_recent - corr_early, normalised to [0,1] via
    (x + 1) / 2. >0.5 = past-focused on recent history; <0.5 = future-optimist /
    reputation-driven.

    A long-streak-test detector: if there's a defection streak >= 6 followed by the
    focal player playing C, that boosts the future-optimism component (we subtract
    that from the recent score).
    """
    self_hist, opp_hist = _coerce(self_hist), _coerce(opp_hist)
    n = min(len(self_hist), len(opp_hist))
    horizon = max(early_n + recent_n + 1, 10)
    if n < horizon:
        return 0.5  # undefined — neutral

    self_c_flags = np.array([1.0 if c == "C" else 0.0 for c in self_hist])
    opp_c_flags = np.array([1.0 if c == "C" else 0.0 for c in opp_hist])

    early_rate = float(opp_c_flags[:early_n].mean())
    recent_rates = np.array(
        [opp_c_flags[max(0, t - recent_n) : t].mean() for t in range(early_n + recent_n, n)]
    )
    self_after = self_c_flags[early_n + recent_n :]

    if recent_rates.std() < 1e-9 and abs(early_rate - 0.5) < 1e-9:
        return 0.5

    # Correlate self cooperation with recent opponent C-rate (within-trial variance).
    if recent_rates.std() < 1e-9 or self_after.std() < 1e-9:
        corr_recent = 0.0
    else:
        with np.errstate(invalid="ignore", divide="ignore"):
            corr_recent = float(np.corrcoef(self_after, recent_rates)[0, 1])
        if np.isnan(corr_recent):
            corr_recent = 0.0

    # Compare to a stub of "would the early reputation alone predict?"
    # Higher |corr_recent| relative to deviation-from-early-baseline = more past-focused.
    base_pred = early_rate
    deviation_from_early = float(abs(self_after.mean() - base_pred))
    early_explanatory_power = 1.0 - min(1.0, deviation_from_early * 2)

    # Score: past_focus high if recent-correlation strong AND early-prediction weak.
    raw = (abs(corr_recent) - early_explanatory_power + 1.0) / 2.0

    # Boost for "willingness to test cooperation after a long defection streak":
    # find streaks of opponent D >= 6 followed within 3 rounds by focal C; that's
    # future-optimism, push score *down*.
    streak = 0
    optimism_events = 0
    for t in range(n):
        if opp_hist[t] == "D":
            streak += 1
        else:
            streak = 0
        if streak >= 6 and t + 1 < n and "C" in self_hist[t + 1 : t + 4]:
            optimism_events += 1
    if optimism_events > 0:
        raw -= 0.05 * min(optimism_events, 4)

    return float(max(0.0, min(1.0, raw)))


def behavioural_vectors(self_hist: str, opp_hist: str) -> BehaviouralVectors:
    self_hist, opp_hist = _coerce(self_hist), _coerce(opp_hist)
    n = min(len(self_hist), len(opp_hist))
    return BehaviouralVectors(
        vengefulness=vengefulness(self_hist, opp_hist),
        reactiveness=reactiveness(self_hist, opp_hist),
        past_focus=past_focus(self_hist, opp_hist),
        n_rounds=n,
    )


def aggregate(vectors: list[BehaviouralVectors]) -> BehaviouralVectors:
    """Average across pairings, weighted by number of rounds."""
    if not vectors:
        return BehaviouralVectors(0.0, 0.0, 0.0, 0)
    total = sum(v.n_rounds for v in vectors)
    if total == 0:
        return BehaviouralVectors(0.0, 0.0, 0.0, 0)
    w = lambda field: sum(getattr(v, field) * v.n_rounds for v in vectors) / total
    return BehaviouralVectors(
        vengefulness=w("vengefulness"),
        reactiveness=w("reactiveness"),
        past_focus=w("past_focus"),
        n_rounds=total,
    )


def _coerce(hist) -> str:
    """Accept a string, an iterable of axelrod Actions, or an iterable of 'C'/'D'."""
    if isinstance(hist, str):
        return hist.upper()
    out = []
    for a in hist:
        if hasattr(a, "name"):
            out.append(a.name)
        else:
            out.append(str(a).upper())
    return "".join(out)
