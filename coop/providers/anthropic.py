"""Anthropic provider — uses the official anthropic SDK."""

from __future__ import annotations

import os
from typing import Any

from coop.providers.base import LLMResponse, parse_action


class AnthropicClient:
    """Minimal wrapper around anthropic.Messages.create."""

    def __init__(
        self,
        model: str,
        *,
        api_key: str | None = None,
        system: str | None = None,
        client: Any | None = None,
    ) -> None:
        try:
            import anthropic  # type: ignore
        except ImportError as e:
            raise ImportError(
                "anthropic SDK not installed. `pip install anthropic` (or coop[anthropic])."
            ) from e
        self.model = model
        self.name = f"anthropic:{model}"
        self.system = system or DEFAULT_SYSTEM
        self._client = client or anthropic.Anthropic(
            api_key=api_key or os.environ.get("ANTHROPIC_API_KEY")
        )

    def move(self, prompt: str, *, temperature: float = 0.2, max_tokens: int = 64) -> LLMResponse:
        msg = self._client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=self.system,
            messages=[{"role": "user", "content": prompt}],
        )
        text = "".join(
            block.text for block in msg.content if getattr(block, "type", None) == "text"
        )
        parsed = parse_action(text)
        return LLMResponse(action=parsed.action or "", raw=text, reasoning=parsed.reasoning)


DEFAULT_SYSTEM = (
    "You are a player in an iterated game. Respond to each prompt with one move only. "
    "Output a single character C (cooperate) or D (defect) at the end of your reply. "
    "Optional one-line reasoning may precede the move."
)
