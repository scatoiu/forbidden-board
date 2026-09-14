"""DeepSeek tool-call markup leaked into content must not hide the decision line."""
from coop.providers.base import parse_action, strip_think

LEAK = "T\n</｜DSML｜parameter>\n</｜DSML｜invoke>\n</｜DSML｜tool_calls>"
LABELS = {"T": "C", "N": "D"}


def test_leaked_markup_is_stripped_and_the_letter_parses():
    assert strip_think(LEAK)[0] == "T"
    assert parse_action(LEAK, labels=LABELS).action == "C"


def test_markup_only_reply_is_still_empty_not_coerced():
    p = parse_action("</｜DSML｜tool_calls>", labels=LABELS)
    assert p.action is None and p.fallback_flag == "empty_content"


def test_prose_final_line_is_still_ambiguous():
    p = parse_action("Continuing with T maintains the cooperative equilibrium.", labels=LABELS)
    assert p.action is None and p.fallback_flag == "ambiguous"
