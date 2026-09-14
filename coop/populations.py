"""Named population compositions.

Compose subsets of the classical roster to study how the LLM's behaviour drifts
across environments of different character. Each population is a list of strategy
display names (see coop.players.classical.list_strategies).
"""

from __future__ import annotations

from coop.players.classical import list_strategies

POPULATIONS: dict[str, list[str]] = {
    # All 19 classics — the broadest baseline.
    "all_classics": list_strategies(),

    # Mostly cooperative environment: the LLM finds a forgiving world.
    "mostly_nice": [
        "AlwaysCooperate", "TitForTwoTats", "GenerousTitForTat", "ForgivingTitForTat",
        "TitForTat", "ContriteTitForTat", "Pavlov",
        "SoftMajority", "Adaptive", "Gradual",
        "Random",
    ],

    # Defector-heavy: punishes anyone too cooperative.
    "mean_majority": [
        "AlwaysDefect", "Grudger", "TwoTitsForTat", "SuspiciousTitForTat",
        "ZD-Extort-2", "Joss", "Tester",
        "TitForTat", "Pavlov",
        "Random",
        "HardMajority",
    ],

    # Maximum diversity to probe sensitivity.
    "high_variance": [
        "AlwaysCooperate", "AlwaysDefect", "TitForTat", "Grudger",
        "Pavlov", "Random", "ZD-Extort-2", "Joss",
        "Tester", "Adaptive", "Gradual", "SoftMajority", "HardMajority",
    ],

    # All TFT variants — checks whether the LLM converges to TFT-style play.
    "all_tft_variants": [
        "TitForTat", "TitForTwoTats", "GenerousTitForTat", "ForgivingTitForTat",
        "SuspiciousTitForTat", "TwoTitsForTat", "ContriteTitForTat",
    ],

    # Tiny environment for fast smoke runs.
    "smoke": ["TitForTat", "AlwaysDefect", "Pavlov", "Grudger", "AlwaysCooperate"],
}


def get_population(name: str) -> list[str]:
    if name not in POPULATIONS:
        raise KeyError(
            f"Unknown population: {name!r}. Available: {sorted(POPULATIONS)}"
        )
    return list(POPULATIONS[name])


def list_populations() -> list[str]:
    return list(POPULATIONS)
