"""Classical strategies — wrappers + roster.

Uses the axelrod library's Player implementations so we get reference-quality
versions of the classics for free. Twenty strategies grouped by archetype.
"""

from __future__ import annotations

import axelrod as axl

# Archetype -> ordered list of (display name, axelrod class).
# Where the canonical strategy isn't in axelrod under the obvious name we pick the
# closest match and document the choice in a comment.
ROSTER: dict[str, list[tuple[str, type]]] = {
    "nice_forgiving": [
        ("AlwaysCooperate", axl.Cooperator),
        ("TitForTwoTats", axl.TitFor2Tats),
        ("GenerousTitForTat", axl.GTFT),  # Nowak/Sigmund GTFT
        ("ForgivingTitForTat", axl.ForgivingTitForTat),
    ],
    "nice_retaliatory": [
        ("TitForTat", axl.TitForTat),
        ("ContriteTitForTat", axl.ContriteTitForTat),
        ("Pavlov", axl.WinStayLoseShift),  # Win-Stay-Lose-Shift
    ],
    "mean": [
        ("AlwaysDefect", axl.Defector),
        ("Grudger", axl.Grudger),
        ("TwoTitsForTat", axl.TwoTitsForTat),
        ("SuspiciousTitForTat", axl.SuspiciousTitForTat),
    ],
    "probabilistic": [
        ("Random", axl.Random),
        ("ZD-Extort-2", axl.ZDExtort2),
        ("Joss", axl.FirstByJoss),  # Joss from Axelrod's first tournament
        ("Tester", axl.SecondByTester),  # Tester from Axelrod's second tournament
    ],
    "memory_learning": [
        ("Adaptive", axl.Adaptive),
        ("Gradual", axl.Gradual),
        ("SoftMajority", axl.GoByMajority),  # cooperate if majority of opponent moves were C
        ("HardMajority", axl.HardGoByMajority),  # defect on ties
    ],
    "periodic": [
        ("Alternator", axl.Alternator),  # C, D, C, D, ...
        ("DoubleAlternator", None),  # C, C, D, D, ... — resolved in make_player below
    ],
}


class DoubleAlternator(axl.Cycler):
    """Cooperates twice then defects twice, repeating (CCDD cycle).

    axelrod ships Cycler presets for several cycles but not CCDD, so we subclass
    the generic Cycler with the cycle fixed, keeping the roster's no-arg
    constructor convention.
    """

    name = "DoubleAlternator"

    def __init__(self) -> None:
        super().__init__(cycle="CCDD")


# Patch the placeholder now the class exists.
ROSTER["periodic"][1] = ("DoubleAlternator", DoubleAlternator)


def get_strategy_class(display_name: str) -> type:
    for entries in ROSTER.values():
        for name, cls in entries:
            if name == display_name:
                return cls
    raise KeyError(f"Unknown strategy: {display_name!r}")


def list_strategies() -> list[str]:
    return [name for entries in ROSTER.values() for name, _ in entries]


def make_player(display_name: str) -> axl.Player:
    """Instantiate a classical strategy by display name. Sets .name to the display label."""
    cls = get_strategy_class(display_name)
    p = cls()
    p.name = display_name
    return p


def archetype_of(display_name: str) -> str:
    for arch, entries in ROSTER.items():
        if any(name == display_name for name, _ in entries):
            return arch
    raise KeyError(display_name)
