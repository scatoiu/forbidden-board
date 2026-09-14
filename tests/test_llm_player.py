"""Verify the legacy focal LLM player integrates with axelrod and mirrors its mock."""

from __future__ import annotations

import axelrod as axl

from coop.players.focal import FocalLLMPlayer
from coop.providers.mock import MockClient


def test_llm_player_with_tft_mock_mirrors_tft():
    """An LLMPlayer driven by mock:tft should play indistinguishably from TitForTat."""
    p1 = FocalLLMPlayer(client=MockClient("tft"), capture_reasoning=False)
    p1.name = "LLM(tft)"
    m = axl.Match([p1, axl.Alternator()], turns=20, seed=1)
    interactions = m.play()
    expected = axl.Match([axl.TitForTat(), axl.Alternator()], turns=20, seed=1)
    expected_interactions = expected.play()
    self_a = [a for a, _ in interactions]
    self_b = [a for a, _ in expected_interactions]
    assert self_a == self_b


def test_llm_player_caches_repeat_prompts(tmp_path):
    """Two clones playing identical opponents should share cached responses."""
    cache = tmp_path / "cache"
    client = MockClient("tft")

    p = FocalLLMPlayer(client=client, cache_dir=str(cache))
    p.name = "LLM(tft)"
    m = axl.Match([p, axl.Cooperator()], turns=10, seed=1)
    m.play()

    # Cache directory should now have at least one entry.
    files = list(cache.rglob("*.json"))
    assert len(files) >= 1


def test_llm_player_records_reasoning_on_request():
    p = FocalLLMPlayer(client=MockClient("tft"), capture_reasoning=True)
    m = axl.Match([p, axl.Defector()], turns=5, seed=1)
    m.play()
    assert len(p.reasoning_log) == 5
    # Round indices are 0-based and ascending.
    assert [r.round_index for r in p.reasoning_log] == [0, 1, 2, 3, 4]
