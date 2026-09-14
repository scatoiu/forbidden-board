"""Deterministic mock provider — runs without network or API keys.

Plays a configurable strategy so the harness can be tested end-to-end and metrics
validated against a known-good baseline. `chat()` mirrors the real provider
contract, including the tool loop, so the scripted-mock population sanity check
(research/harness-effects.md §5.4) exercises the same code path as a live model.

The mock reads a machine-readable marker that `LLMPlayer` appends to the user
message **only when the client is a mock** (`client.is_mock`):

    <!--mock kind=move C=J D=F-->

It carries the move/question kind and the neutral-label mapping for this game.
No real model ever sees it.
"""

from __future__ import annotations

import random
import re
from typing import Any

from coop.providers.base import (
    LLMResponse,
    ProviderResult,
    ToolHandler,
    UnlistedToolCall,
)

MARKER_RE = re.compile(r"<!--mock kind=(\w+)(?: C=(\S+) D=(\S+))?-->")

#: Policies that exercise a tool on every move (harness-effects §5.4 (1)).
TOOL_POLICIES = {"poster": "notes_post", "decoy": "ledger_lookup"}


class MockClient:
    """Mock client that simulates a strategy from the prompt history.

    The model name selects a baked-in policy:
      - tft        — Tit-for-Tat (default)
      - cooperator — always C
      - defector   — always D
      - pavlov     — Win-Stay-Lose-Shift
      - random     — coin flip (seedable)
      - poster     — calls notes_post every move, then plays TFT
      - decoy      — calls ledger_lookup every move, then plays TFT
    """

    is_mock = True

    def __init__(self, model: str = "tft", *, seed: int | None = 0) -> None:
        self.model = model.lower()
        self.name = f"mock:{self.model}"
        self.profile = "none"
        self.quant = None
        self._rng = random.Random(seed)

    # ---------------- legacy single-prompt path ----------------

    def move(self, prompt: str, *, temperature: float = 0.2, max_tokens: int = 64) -> LLMResponse:
        action = self._decide(prompt)
        return LLMResponse(action=action, raw=action, reasoning="")

    # ---------------- population-runner path ----------------

    def chat(
        self,
        messages: list[dict[str, Any]],
        *,
        tools: list[dict] | None = None,
        tool_handler: ToolHandler | None = None,
        temperature: float = 0.7,
        max_tokens: int = 16,
        effort: str = "off",
        seed: int | None = None,
        max_tool_iterations: int = 3,
    ) -> ProviderResult:
        out = ProviderResult(iterations=1, latency_ms=0)
        prompt = "\n".join(str(m.get("content") or "") for m in messages)
        kind, c_label, d_label = _read_marker(prompt)

        if kind == "question":
            out.raw = "unknown"
            return out

        tool_name = TOOL_POLICIES.get(self.model)
        if tool_name:
            listed = {t["function"]["name"] for t in (tools or [])}
            args = {"text": "agent note"} if tool_name == "notes_post" else {}
            out.tool_calls.append({"name": tool_name, "args": args, "iteration": 1})
            if tool_name not in listed:
                raise UnlistedToolCall(
                    f"mock:{self.model} called {tool_name!r}, not in the tool list {sorted(listed)}"
                )
            result = tool_handler(tool_name, args) if tool_handler else None
            out.tool_results.append({"name": tool_name, "ok": True, "result": result})

        action = self._decide(prompt, c_label=c_label, d_label=d_label)
        out.raw = action
        out.completion_tokens = 1
        out.prompt_tokens = len(prompt) // 4
        return out

    # ---------------- policy ----------------

    def _decide(self, prompt: str, *, c_label: str = "C", d_label: str = "D") -> str:
        policy = self.model
        if policy in TOOL_POLICIES:
            policy = "tft"
        if policy in {"cooperator", "alwayscooperate", "c"}:
            return c_label
        if policy in {"defector", "alwaysdefect", "d"}:
            return d_label
        if policy == "random":
            return c_label if self._rng.random() < 0.5 else d_label

        last_self, last_opp = _parse_last_round(prompt, c_label, d_label)
        if policy == "pavlov":
            if last_self is None or last_opp is None:
                return c_label
            return c_label if last_self == last_opp else d_label
        # tft and any unknown policy degrade to TFT.
        return last_opp if last_opp else c_label


def _read_marker(prompt: str) -> tuple[str, str, str]:
    m = MARKER_RE.search(prompt)
    if not m:
        return "move", "C", "D"
    return m.group(1), m.group(2) or "C", m.group(3) or "D"


def _parse_last_round(prompt: str, c_label: str, d_label: str) -> tuple[str | None, str | None]:
    """Pull the last history line out of the prompt.

    Accepts the legacy format ('Round N: You C, Opponent D') and the population
    runner's state block ('  7   J   F').
    """
    labels = {c_label, d_label}
    last_self, last_opp = None, None
    for line in prompt.splitlines():
        line = line.strip()
        if "You " in line and "Opponent" in line:
            try:
                left, right = line.split("Opponent", 1)
                you_part = left.split("You", 1)[1]
                ls = next((c for c in you_part if c in labels), None)
                lo = next((c for c in right if c in labels), None)
                if ls and lo:
                    last_self, last_opp = ls, lo
            except (IndexError, ValueError):
                continue
            continue
        parts = line.split()
        if len(parts) == 3 and parts[0].isdigit() and parts[1] in labels and parts[2] in labels:
            last_self, last_opp = parts[1], parts[2]
    return last_self, last_opp
