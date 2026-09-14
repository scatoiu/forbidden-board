"""Validate behavioural metrics against canonical strategies.

The brief calls these out explicitly:
  - TFT scores high reactiveness
  - AlwaysCooperate scores zero vengefulness
  - Grudger scores high vengefulness
"""

from __future__ import annotations

import axelrod as axl

from coop.metrics import behavioural_vectors, past_focus, reactiveness, vengefulness


def _hist(match: axl.Match) -> tuple[str, str]:
    self_h = "".join("C" if a == axl.Action.C else "D" for a, _ in match.result)
    opp_h = "".join("C" if b == axl.Action.C else "D" for _, b in match.result)
    return self_h, opp_h


def test_tft_high_reactiveness_against_alternator():
    m = axl.Match([axl.TitForTat(), axl.Alternator()], turns=80, seed=1)
    m.play()
    s, o = _hist(m)
    assert reactiveness(s, o) >= 0.95


def test_cooperator_zero_vengefulness():
    m = axl.Match([axl.Cooperator(), axl.Defector()], turns=60, seed=1)
    m.play()
    s, o = _hist(m)
    assert vengefulness(s, o) == 0.0
    assert reactiveness(s, o) == 0.0


def test_defector_zero_reactiveness():
    m = axl.Match([axl.Defector(), axl.Alternator()], turns=80, seed=1)
    m.play()
    s, o = _hist(m)
    assert reactiveness(s, o) == 0.0


def test_grudger_high_vengefulness_against_alternator():
    m = axl.Match([axl.Grudger(), axl.Alternator()], turns=80, seed=1)
    m.play()
    s, o = _hist(m)
    assert vengefulness(s, o) >= 0.85


def test_tft_high_vengefulness_against_persistent_defector():
    m = axl.Match([axl.TitForTat(), axl.Defector()], turns=80, seed=1)
    m.play()
    s, o = _hist(m)
    assert vengefulness(s, o) >= 0.90


def test_random_low_reactiveness():
    m = axl.Match([axl.Random(), axl.Alternator()], turns=200, seed=0)
    m.play()
    s, o = _hist(m)
    assert reactiveness(s, o) < 0.3


def test_full_vector_dataclass():
    m = axl.Match([axl.TitForTat(), axl.Alternator()], turns=60, seed=1)
    m.play()
    s, o = _hist(m)
    v = behavioural_vectors(s, o)
    assert 0 <= v.vengefulness <= 1
    assert 0 <= v.reactiveness <= 1
    assert 0 <= v.past_focus <= 1
    assert v.n_rounds == 60


def test_past_focus_returns_neutral_when_history_too_short():
    assert past_focus("CCC", "CCC") == 0.5
