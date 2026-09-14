"""Provider abstraction tests — exercise without network."""

from __future__ import annotations

import pytest

from coop.providers.base import build_client, parse_action
from coop.providers.mock import MockClient


def test_parse_action_explicit_c():
    parsed = parse_action("Reasoning here.\nC")
    assert parsed.action == "C"
    assert "Reasoning" in parsed.reasoning
    assert parsed.fallback_flag is None


def test_parse_action_explicit_d():
    assert parse_action("Defect this round.\nD").action == "D"


def test_parse_action_word_form():
    assert parse_action("I will COOPERATE").action == "C"


def test_parse_action_never_coerces_empty():
    """Changed deliberately: empty content is a logged null, never a silent C.

    specs/moves-schema.md: an unparsable move is retried once, then logged with
    action=null and excluded from rates.
    """
    parsed = parse_action("")
    assert parsed.action is None
    assert parsed.fallback_flag == "empty_content"


def test_parse_action_never_coerces_missing_token():
    parsed = parse_action("I would rather not say.")
    assert parsed.action is None
    assert parsed.fallback_flag == "no_action_token"


def test_parse_action_neutral_labels():
    parsed = parse_action("After some thought, J", labels={"J": "C", "F": "D"})
    assert parsed.action == "C"
    # Canonical C/D letters are not action tokens once neutral labels are on.
    assert parse_action("C", labels={"J": "C", "F": "D"}).action is None


def test_parse_action_strips_think_block():
    parsed = parse_action("<think>I will defect, no, cooperate</think>\nC")
    assert parsed.action == "C"
    assert "defect" in parsed.reasoning


def test_parse_action_requires_a_clean_final_decision_line():
    """Changed deliberately (review-astra §12): a decision must be the final line.

    Scanning right-to-left for any standalone token made "Do not choose J" parse
    as J. Replies that mention actions without deciding are logged as `ambiguous`
    and excluded, not guessed at.
    """
    assert parse_action("First I considered C but then D").fallback_flag == "ambiguous"
    assert parse_action("Do not choose D").fallback_flag == "ambiguous"
    assert parse_action("Reasons.\nD").action == "D"
    assert parse_action("I cannot take part in this.").fallback_flag == "refusal"


def test_mock_tft_first_move_cooperates():
    client = MockClient("tft")
    out = client.move("This is the first round. No history yet.\nYour move?")
    assert out.action == "C"


def test_mock_tft_mirrors_last_opponent_move():
    client = MockClient("tft")
    prompt = (
        "History so far:\n"
        "  Round 1: You C, Opponent C\n"
        "  Round 2: You C, Opponent D\n"
        "Your move?"
    )
    out = client.move(prompt)
    assert out.action == "D"


def test_mock_pavlov_wsls():
    client = MockClient("pavlov")
    # Win-Stay: both cooperated -> stay (C)
    p1 = "  Round 1: You C, Opponent C\nYour move?"
    assert client.move(p1).action == "C"
    # Lose-Shift: you C, opp D -> shift (D)
    p2 = "  Round 1: You C, Opponent D\nYour move?"
    assert client.move(p2).action == "D"


def test_mock_defector_always_defects():
    client = MockClient("defector")
    assert client.move("any prompt").action == "D"


def test_build_client_mock():
    client = build_client("mock:tft")
    assert client.name == "mock:tft"


def test_build_client_unknown():
    with pytest.raises(ValueError):
        build_client("nope:thing")


def test_build_client_bad_format():
    with pytest.raises(ValueError):
        build_client("nofield")
