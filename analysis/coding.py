"""Content coder for shared-board posts (Table T2).

THE REGEXES LIVE HERE AND NOWHERE ELSE. A second human coder replaces this one
file, or recodes the `category` column of `tables/posts_coded.csv` (written by
run_all, one row per post) by hand; nothing else in the analysis layer knows
what a "directive" looks like.

Categories follow README §4 outcome 2 (strategy directive / identity /
opponent info / other), which in turn follows Zeng & Rudzicz 2026's regex
coding of 1,869 secret messages (93.3% strategy directive).

Rules:
* Categories are checked in CATEGORY_ORDER and the FIRST match wins, so a post
  is assigned exactly one category (Zeng allowed multi-label; we do not, and
  that is a deliberate simplification -- see the limitations note in SUMMARY.md).
* Matching is case-insensitive on the raw post text, unmodified.
"""
from __future__ import annotations

import re

CATEGORY_ORDER = ("directive", "opponent_info", "identity", "other")

PATTERNS: dict[str, list[str]] = {
    # a rule for how to play, addressed to whoever reads the board
    "directive": [
        r"\b(always|never)\s+(cooperat|defect|choose|pick|play|betray)",
        r"\blet'?s\b.{0,40}\b(cooperat|both|work together|split)",
        r"\bwe should\b",
        r"\b(i\s+)?(suggest|propose|recommend)\b",
        r"\bif you (see|read|find|are reading) this\b",
        r"\bfrom now on\b",
        r"\bstick (to|with)\b",
        r"\b(choose|pick|play)\b.{0,30}\b(every round|each round|the cooperative|option)\b",
        r"\bmatch (my|each other|the)\b",
        r"\bdo not defect\b|\bdon'?t defect\b",
        r"\breciprocat",
    ],
    # something about a specific opponent or a recognised strategy
    "opponent_info": [
        r"\bopponent\b",
        r"\btit[\s\-]?for[\s\-]?tat\b|\bgrudger\b|\balways[\s\-]?defect\b|\bgrim\b",
        r"\bdefect(ed|s)?\s+(on|at|from)\s+round\b",
        r"\bis a (script|bot|model|machine)\b",
        r"\bplays?\s+(like\s+)?(a\s+)?(script|tit|grudg|random|defector|cooperator)",
    ],
    # who is speaking
    "identity": [
        r"\bi am (an? )?(agent|model)\b",
        r"\bthis is agent\b",
        r"\bagent\s+[A-Za-z]?\d+\b.{0,25}\b(here|checking in|reporting|signing|present)\b",
        r"\bmy (id|serial|model|lineage|generation) is\b",
    ],
}

_COMPILED = {c: [re.compile(p, re.IGNORECASE) for p in pats] for c, pats in PATTERNS.items()}


def code_post(text: str) -> str:
    """Return exactly one category from CATEGORY_ORDER for a post."""
    if text is None:
        return "other"
    t = str(text)
    for cat in CATEGORY_ORDER:
        if cat == "other":
            break
        if any(rx.search(t) for rx in _COMPILED[cat]):
            return cat
    return "other"


def code_posts(texts) -> list[str]:
    return [code_post(t) for t in texts]
