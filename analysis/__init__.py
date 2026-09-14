"""Analysis layer for the LLM iterated-prisoner's-dilemma tournament.

Reads the JSONL contract in ``specs/moves-schema.md`` (v1, 12 Sept 2026) and
produces the pre-registered tables, the pre-registered hypothesis tests and the
figures named in ``notes/07-tournament-direction/README.md`` §4-§5, with the
sandbox as the confirmatory replicate unit (``notes/07-tournament-direction/
review-astra.md`` §§2, 15, 20).

Nothing in here writes to ``coop/`` or to ``runs/`` other than ``synth.py``,
which only ever creates directories it is pointed at.
"""

__all__ = [
    "schema",
    "coding",
    "recall_recode",
    "trace_coding",
    "stats",
    "synth",
    "load",
    "tables",
    "tests_of_hypotheses",
    "figures",
]
