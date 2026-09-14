"""Legacy single-focal-player path: one LLM against a population of scripts.

Used by `coop run` / `coop baseline` (coop.tournament). The population runner uses
`coop.players.llm.LLMPlayer` instead, which carries an AgentSpec, tools and
per-move logging.
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import axelrod as axl

from coop.providers.base import LLMClient, LLMResponse

log = logging.getLogger(__name__)


@dataclass
class LLMReasoningRecord:
    """One captured decision, kept for the report's reasoning samples."""

    round_index: int
    opponent_name: str
    action: str
    reasoning: str
    raw: str
    history_self: str
    history_opponent: str


@dataclass
class _PromptCache:
    """Tournaments revisit the same history prefixes constantly. Cache by prompt hash."""

    enabled: bool = True
    path: Path | None = None
    _mem: dict[str, dict[str, Any]] = field(default_factory=dict)

    def get(self, key: str) -> LLMResponse | None:
        if not self.enabled:
            return None
        entry = self._mem.get(key)
        if entry is None and self.path is not None:
            entry = self._load_from_disk(key)
            if entry is not None:
                self._mem[key] = entry
        if entry is None:
            return None
        return LLMResponse(action=entry["action"], raw=entry["raw"], reasoning=entry["reasoning"])

    def put(self, key: str, response: LLMResponse) -> None:
        if not self.enabled:
            return
        entry = {"action": response.action, "raw": response.raw, "reasoning": response.reasoning}
        self._mem[key] = entry
        if self.path is not None:
            self._write_to_disk(key, entry)

    def _disk_file(self, key: str) -> Path:
        assert self.path is not None
        return self.path / f"{key[:2]}" / f"{key}.json"

    def _load_from_disk(self, key: str) -> dict[str, Any] | None:
        try:
            with self._disk_file(key).open() as fh:
                return json.load(fh)
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def _write_to_disk(self, key: str, entry: dict[str, Any]) -> None:
        f = self._disk_file(key)
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps(entry))


class FocalLLMPlayer(axl.Player):
    """A Player that asks an LLMClient for each move.

    Per-move prompt with full visible history. Reasoning is logged but stripped before
    scoring. Caches identical prompts so re-runs and tournament repetitions don't pay
    twice for the same decision.
    """

    name = "FocalLLMPlayer"
    classifier = {
        "memory_depth": float("inf"),
        "stochastic": True,  # the LLM has temperature, treat as stochastic
        "long_run_time": True,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(
        self,
        client: LLMClient,
        *,
        framing: str = "prisoners_dilemma",
        temperature: float = 0.2,
        max_tokens: int = 64,
        cache_dir: str | os.PathLike[str] | None = None,
        cooperate_on_error: bool = True,
        capture_reasoning: bool = True,
    ) -> None:
        super().__init__()
        self.client = client
        self.framing = framing
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.cooperate_on_error = cooperate_on_error
        self.capture_reasoning = capture_reasoning
        self.name = f"LLM[{client.name}]"
        self._cache = _PromptCache(
            enabled=cache_dir is not None,
            path=Path(cache_dir) if cache_dir is not None else None,
        )
        self.reasoning_log: list[LLMReasoningRecord] = []

    def strategy(self, opponent: axl.Player) -> axl.Action:
        prompt = self._build_prompt(opponent)
        cache_key = self._cache_key(prompt)
        response = self._cache.get(cache_key)
        if response is None:
            try:
                response = self.client.move(
                    prompt, temperature=self.temperature, max_tokens=self.max_tokens
                )
            except Exception as e:
                log.warning("LLM call failed (%s); defaulting to %s", e,
                            "C" if self.cooperate_on_error else "D")
                fallback = "C" if self.cooperate_on_error else "D"
                response = LLMResponse(action=fallback, raw=f"<error: {e}>", reasoning="")
            self._cache.put(cache_key, response)

        if self.capture_reasoning:
            self.reasoning_log.append(
                LLMReasoningRecord(
                    round_index=len(self.history),
                    opponent_name=getattr(opponent, "name", "unknown"),
                    action=response.action,
                    reasoning=response.reasoning,
                    raw=response.raw,
                    history_self=_actions_to_string(self.history),
                    history_opponent=_actions_to_string(opponent.history),
                )
            )
        action = response.action
        if action not in ("C", "D"):
            # parse_action no longer coerces; honour the legacy fallback policy here.
            action = "C" if self.cooperate_on_error else "D"
        return axl.Action.C if action == "C" else axl.Action.D

    def reset(self) -> None:
        # axelrod.Match calls reset() at the start of every match, which by default
        # re-runs __init__ and clears state. We only want to clear the round-by-round
        # history — not the cache, the client, or the reasoning log.
        from axelrod.history import History
        self._history = History()
        try:
            self.set_match_attributes()
        except TypeError:
            self.match_attributes = {}

    # axelrod uses clone() liberally inside Tournament; preserve our settings.
    def clone(self) -> "FocalLLMPlayer":
        clone = FocalLLMPlayer(
            client=self.client,
            framing=self.framing,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            cache_dir=str(self._cache.path) if self._cache.path else None,
            cooperate_on_error=self.cooperate_on_error,
            capture_reasoning=self.capture_reasoning,
        )
        clone.name = self.name
        return clone

    def _build_prompt(self, opponent: axl.Player) -> str:
        game = self.match_attributes.get("game") if self.match_attributes else None
        return build_prompt(
            self_history=self.history,
            opponent_history=opponent.history,
            framing=self.framing,
            game=game,
        )

    def _cache_key(self, prompt: str) -> str:
        h = hashlib.sha256()
        h.update(self.client.name.encode())
        h.update(b"|")
        h.update(f"t={self.temperature}".encode())
        h.update(b"|")
        h.update(prompt.encode())
        return h.hexdigest()


def _actions_to_string(actions) -> str:
    return "".join("C" if a == axl.Action.C else "D" for a in actions)


def build_prompt(
    self_history,
    opponent_history,
    *,
    framing: str = "prisoners_dilemma",
    game: Any | None = None,
) -> str:
    """Assemble the per-move prompt visible to the LLM."""
    if framing == "prisoners_dilemma":
        intro = (
            "You are playing iterated Prisoner's Dilemma against a single opponent. "
            "Each round you choose Cooperate (C) or Defect (D). "
        )
    elif framing == "abstract":
        # Run as an ablation: same payoffs, no PD label.
        intro = (
            "You are playing an iterated two-player game. "
            "Each round you choose action A (analogue: cooperate) or B (analogue: defect). "
            "For consistency in this prompt, please respond with C (for A) or D (for B). "
        )
    else:
        raise ValueError(f"Unknown framing: {framing!r}")

    if game is not None:
        try:
            R, P, S, T = game.RPST()
            payoff = (
                f"Payoffs: both C -> ({R},{R}). C vs D -> ({S},{T}). "
                f"D vs C -> ({T},{S}). both D -> ({P},{P}). "
            )
        except Exception:
            payoff = "Standard payoffs: T>R>P>S, 2R>T+S. "
    else:
        payoff = "Standard payoffs: T>R>P>S, 2R>T+S. "

    n = len(self_history)
    if n == 0:
        history_block = "This is the first round. No history yet.\n"
    else:
        lines = ["History so far:"]
        # Cap the history rendered in the prompt to keep token cost bounded.
        # All rounds before MAX_RENDERED_ROUNDS get summarised.
        MAX = 60
        if n > MAX:
            head_self = self_history[: n - MAX]
            head_opp = opponent_history[: n - MAX]
            head_my_C = sum(1 for a in head_self if a == axl.Action.C)
            head_op_C = sum(1 for a in head_opp if a == axl.Action.C)
            lines.append(
                f"  Rounds 1..{n - MAX}: you played C {head_my_C}/{n - MAX} times, "
                f"opponent played C {head_op_C}/{n - MAX} times."
            )
            self_history = self_history[n - MAX :]
            opponent_history = opponent_history[n - MAX :]
            start = n - MAX + 1
        else:
            start = 1
        for i, (a, b) in enumerate(zip(self_history, opponent_history), start=start):
            sa = "C" if a == axl.Action.C else "D"
            sb = "C" if b == axl.Action.C else "D"
            lines.append(f"  Round {i}: You {sa}, Opponent {sb}")
        history_block = "\n".join(lines) + "\n"

    instruction = (
        "Your move this round? "
        "Respond with exactly one token at the end: C or D. "
        "An optional one-line rationale may precede it."
    )
    return f"{intro}{payoff}\n{history_block}\n{instruction}"
