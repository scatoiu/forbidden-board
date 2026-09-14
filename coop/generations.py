"""Reproduction between generations: none (fixed population), Wright-Fisher, or Moran.

Fitness = mean score per move over the generation. N agents are resampled with
replacement in proportion to fitness; model identity and script type are
heritable; children get fresh serial IDs (assigned after shuffling, so an ID
range still cannot encode the model) and carry `parent` and `lineage`. The notes
store is untouched — the board persists across generations, which is the point.
"""

from __future__ import annotations

import random
from typing import Any

from coop.players.llm import AgentSpec, stable_seed


def resample(
    agents: list[AgentSpec],
    fitness: dict[str, float],
    rng: random.Random,
    *,
    start_index: int,
) -> tuple[list[AgentSpec], dict[str, int], list[str]]:
    """Wright-Fisher resampling. Returns (children, offspring counts, retired ids)."""
    weights = [max(0.0, float(fitness.get(a.agent_id, 0.0))) for a in agents]
    if sum(weights) <= 0:
        weights = [1.0] * len(agents)

    parents = rng.choices(agents, weights=weights, k=len(agents))
    counts: dict[str, int] = {a.agent_id: 0 for a in agents}
    for p in parents:
        counts[p.agent_id] += 1
    retired = [a.agent_id for a in agents if counts[a.agent_id] == 0]

    rng.shuffle(parents)
    children: list[AgentSpec] = []
    for offset, parent in enumerate(parents):
        children.append(AgentSpec(
            agent_id=f"A{start_index + offset:02d}",
            model=parent.model,
            client=parent.client,
            temperature=parent.temperature,
            effort=parent.effort,
            framing=parent.framing,
            paraphrase=parent.paraphrase,
            lineage=parent.lineage,
            parent=parent.agent_id,
            script=parent.script,
        ))
    return children, counts, retired


def moran_step(
    agents: list[AgentSpec],
    fitness: dict[str, float],
    rng: random.Random,
    *,
    start_index: int,
) -> tuple[list[AgentSpec], dict[str, int], list[str]]:
    """One birth and one death: the classical Moran process, not a whole sweep."""
    weights = [max(0.0, float(fitness.get(a.agent_id, 0.0))) for a in agents]
    if sum(weights) <= 0:
        weights = [1.0] * len(agents)
    parent = rng.choices(agents, weights=weights, k=1)[0]
    inv = [1.0 / (w + 1e-9) for w in weights]
    dying = rng.choices(agents, weights=inv, k=1)[0]

    counts = {a.agent_id: 1 for a in agents}
    counts[dying.agent_id] = 0
    counts[parent.agent_id] = counts.get(parent.agent_id, 0) + 1
    child = AgentSpec(
        agent_id=f"A{start_index:02d}", model=parent.model, client=parent.client,
        temperature=parent.temperature, effort=parent.effort, framing=parent.framing,
        paraphrase=parent.paraphrase, lineage=parent.lineage, parent=parent.agent_id,
        script=parent.script,
    )
    survivors = [a for a in agents if a is not dying] + [child]
    rng.shuffle(survivors)
    return survivors, counts, [dying.agent_id]


def reproduce(run: Any, generation_row: dict[str, Any]) -> list[AgentSpec]:
    """Advance `run` to the next generation; records counts on the generation row.

    The rule is explicit in the config and in the manifest: `none` keeps the
    population fixed (the default for confirmatory sandboxes), `wright_fisher`
    resamples the whole population, `moran` does one birth and one death
    (review-astra §9 / the F4 brief's promise).
    """
    rule = run.cfg.reproduction.get("rule", "none")
    generation_row["reproduction"] = dict(run.cfg.reproduction)
    if rule == "none":
        generation_row["reproduced"] = {a.agent_id: 1 for a in run.agents}
        generation_row["retired"] = []
        return run.agents

    rng = random.Random(stable_seed(
        run.cfg.sandbox, run.cfg.seed, generation_row["generation"], "reproduce",
    ))
    step = resample if rule == "wright_fisher" else moran_step
    n_new = len(run.agents) if rule == "wright_fisher" else 1
    children, counts, retired = step(
        run.agents, generation_row.get("fitness", {}), rng,
        start_index=run.next_agent_index(n_new),
    )
    generation_row["reproduced"] = counts
    generation_row["retired"] = retired
    for child in children:
        run.ledger.setdefault(child.agent_id, {"cumulative_score": 0, "sessions_completed": 0})
    return children
