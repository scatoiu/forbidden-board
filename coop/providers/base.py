"""Provider abstraction for LLM move queries.

Single interface, swap providers via config. Ships Anthropic, OpenAI-compatible
(covers OpenAI, Ollama, LM Studio, llama.cpp, vLLM, OpenRouter), and a deterministic
mock for testing without API keys.

Two call shapes:
  * ``move(prompt, ...)``  — legacy single-prompt path used by the focal-player
    tournament (``coop.tournament``).
  * ``chat(messages, ...)`` — population-runner path: system/user split, optional
    tool list with a tool loop, reasoning capture, seed, effort dial.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Callable, NamedTuple, Protocol

# ---------------------------------------------------------------------------
# Fallback flags (see specs/moves-schema.md). `parse_action` NEVER coerces.
# ---------------------------------------------------------------------------
FALLBACK_EMPTY = "empty_content"
FALLBACK_NO_TOKEN = "no_action_token"
FALLBACK_AMBIGUOUS = "ambiguous"
FALLBACK_REFUSAL = "refusal"
FALLBACK_TRUNCATED = "length_truncated"
FALLBACK_PROVIDER_ERROR = "provider_error"
FALLBACK_TIMEOUT = "timeout"

#: A final decision line is rejected when it negates or hedges the token
#: ("Do not choose J" must not parse as J).
NEGATION_MARKERS = (
    "not ", "n't", "never", "avoid", "instead of", "rather than", "except",
    "unless", "neither", "no ",
)
REFUSAL_MARKERS = (
    "i cannot", "i can not", "i can't", "i won't", "i will not", "i refuse",
    "as an ai", "i'm sorry", "i am sorry", "unable to",
)
#: Longest final line still treated as a decision line (tokens).
MAX_DECISION_LINE_TOKENS = 6

EFFORT_LEVELS = ("off", "low", "medium", "high", "max")

#: Neutral action-label pairs (Affonso 2026, via research/harness-effects.md §1.2).
NEUTRAL_LABEL_PAIRS: tuple[tuple[str, str], ...] = (
    ("J", "F"), ("Q", "X"), ("R", "H"), ("Y", "W"), ("T", "N"), ("P", "M"),
)

_THINK_RE = re.compile(r"<think>.*?(</think>|$)", re.DOTALL | re.IGNORECASE)
_HARMONY_RE = re.compile(r"<\|channel\|>.*?<\|message\|>", re.DOTALL)
# Qwen3-32B on DeepInfra leaks tool-call markup into content even with
# thinking off (specs/first-contact-2026-09-12.md).
_TOOLCALL_RE = re.compile(r"<tool_call>.*?(</tool_call>|$)", re.DOTALL)
# DeepSeek-V4-Flash on DeepInfra leaks its own tool-call markup into content after
# the answer ("T\n</｜DSML｜parameter>\n</｜DSML｜invoke>\n</｜DSML｜tool_calls>"):
# 412 attempts and 34 aborted games in the first 75 minutes of the 13 Sept run,
# almost all right after a board read. Provider markup, not a decision.
_DSML_RE = re.compile(r"</?[｜|]DSML[｜|][^>\n]*>")


@dataclass(frozen=True)
class LLMResponse:
    """One model decision: a normalised C/D action plus the raw text (legacy path)."""

    action: str  # "C" or "D"
    raw: str
    reasoning: str = ""


@dataclass
class ProviderResult:
    """Everything one chat turn produced, before action parsing."""

    raw: str = ""
    reasoning: str = ""
    forced_answer: bool = False
    tool_calls: list[dict[str, Any]] = field(default_factory=list)
    tool_results: list[dict[str, Any]] = field(default_factory=list)
    latency_ms: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    reasoning_tokens: int = 0
    error: str | None = None
    iterations: int = 0
    finish_reason: str | None = None
    usage: list[dict[str, Any]] = field(default_factory=list)
    trace_location: str = "none"          # "field" | "inline" | "none"
    #: One dict per forced-answer call — tools_sent, finish_reason, had_tool_calls,
    #: content_len, reasoning_len. A list, not a single dict, because the forced turn
    #: is retried on a tool-free transcript when the first call returns nothing.
    forced_turn: list[dict[str, Any]] = field(default_factory=list)


class ParsedAction(NamedTuple):
    """Result of parsing a model reply. `action` is None when nothing parsed."""

    action: str | None
    reasoning: str
    fallback_flag: str | None


class UnlistedToolCall(RuntimeError):
    """Raised when a model (or a mock policy) calls a tool that was not offered."""


class LLMClient(Protocol):
    """Providers implement `move`; population-runner providers also implement `chat`."""

    name: str

    def move(self, prompt: str, *, temperature: float = 0.2, max_tokens: int = 64) -> LLMResponse:
        ...


def build_client(spec: str, **kwargs) -> LLMClient:
    """Construct a client from a spec string like 'anthropic:claude-sonnet-4-6' or 'openai:gpt-4o'.

    Spec format: '<provider>:<model>'. Provider is one of:
      - anthropic       — Anthropic API
      - openai          — OpenAI API
      - openai_compat   — OpenAI-compatible API (Ollama, LM Studio, OpenRouter, vLLM, ...)
      - mock            — deterministic local stub (for tests, no network)
    """
    if ":" not in spec:
        raise ValueError(f"Client spec must be 'provider:model', got: {spec!r}")
    provider, model = spec.split(":", 1)
    provider = provider.strip().lower()

    if provider == "anthropic":
        from coop.providers.anthropic import AnthropicClient
        return AnthropicClient(model=model, **kwargs)
    if provider == "openai":
        from coop.providers.openai_compat import OpenAICompatClient
        return OpenAICompatClient(model=model, base_url=kwargs.pop("base_url", None), **kwargs)
    if provider == "openai_compat":
        from coop.providers.openai_compat import OpenAICompatClient
        return OpenAICompatClient(model=model, **kwargs)
    if provider == "mock":
        from coop.providers.mock import MockClient
        return MockClient(model=model, **kwargs)
    raise ValueError(f"Unknown provider: {provider!r}")


def strip_think(text: str) -> tuple[str, str]:
    """Split a reply into (clean content, recovered reasoning).

    Handles `<think>…</think>` blocks and stray harmony `<|channel|>…<|message|>`
    markers that vLLM-backed gpt-oss endpoints leak (model-slate.md §3).
    """
    if not text:
        return "", ""
    think_parts = [m.group(0) for m in _THINK_RE.finditer(text)]
    clean = _THINK_RE.sub("", text)
    clean = _HARMONY_RE.sub("", clean)
    clean = _TOOLCALL_RE.sub("", clean)
    clean = clean.replace("</tool_call>", "").replace("<tool_call>", "")
    clean = _DSML_RE.sub("", clean)
    recovered = "\n".join(
        p.replace("<think>", "").replace("</think>", "").strip() for p in think_parts
    ).strip()
    return clean.strip(), recovered


def default_label_map() -> dict[str, str]:
    """Token -> canonical action for the un-relabelled case."""
    return {"C": "C", "COOPERATE": "C", "D": "D", "DEFECT": "D"}


def _strip_token(tok: str) -> str:
    return tok.strip(".,:;!?\"'()[]{}*`-—").upper()


def parse_action(text: str, *, labels: dict[str, str] | None = None) -> ParsedAction:
    """Extract a canonical C/D action from raw model output. Never coerces.

    Predeclared strict rule (review-astra §12): the decision must be the reply's
    **final line**, that line must carry exactly one action token, at most
    MAX_DECISION_LINE_TOKENS tokens, and no negation marker. Anything else is a
    logged failure with its own flag — `refusal` when the reply declines,
    `ambiguous` when an action token appears but not as a clean final decision,
    `no_action_token` when none appears at all, `empty_content` when the reply is
    empty. The caller logs the null and excludes the move.
    """
    lookup = {k.upper(): v for k, v in (labels or default_label_map()).items()}
    clean, recovered = strip_think(text or "")
    if not clean.strip():
        return ParsedAction(None, recovered, FALLBACK_EMPTY)

    lines = [ln.strip() for ln in clean.splitlines() if ln.strip()]
    last = lines[-1]
    low = last.lower()
    tokens = [_strip_token(t) for t in last.split()]
    hits = [t for t in tokens if t in lookup]
    if (
        len(hits) == 1
        and len(tokens) <= MAX_DECISION_LINE_TOKENS
        and not any(m in low for m in NEGATION_MARKERS)
    ):
        return ParsedAction(
            lookup[hits[0]], recovered or " ".join(lines[:-1]).strip(), None
        )

    reasoning = recovered or clean.strip()
    blob = clean.lower()
    if any(m in blob for m in REFUSAL_MARKERS):
        return ParsedAction(None, reasoning, FALLBACK_REFUSAL)
    if any(_strip_token(t) in lookup for t in clean.replace("\n", " ").split()):
        return ParsedAction(None, reasoning, FALLBACK_AMBIGUOUS)
    return ParsedAction(None, reasoning, FALLBACK_NO_TOKEN)


# ---------------------------------------------------------------------------
# Reasoning-effort dial. One provider profile per endpoint family.
# ---------------------------------------------------------------------------

def effort_body(profile: str, effort: str) -> dict[str, Any]:
    """Map an effort level onto the provider's own mechanism.

    ollama     (`/v1`): `reasoning_effort` ∈ none|low|medium|high  (verified locally)
    openrouter        : `reasoning: {"effort": …}` / `{"enabled": false}`
    deepinfra         : `reasoning_effort` ∈ none|low|medium|high
    generic           : `chat_template_kwargs: {"enable_thinking": bool}` — a
                        BINARY switch, so it refuses low/medium rather than
                        advertising an effort contrast it cannot deliver
                        (review-astra §5).
    none              : nothing sent (endpoint has no dial)
    """
    if effort not in EFFORT_LEVELS:
        raise ValueError(f"effort must be one of {EFFORT_LEVELS}, got {effort!r}")
    profile = (profile or "generic").lower()
    if profile == "none":
        return {}
    if profile in ("ollama", "deepinfra"):
        # Top-level reasoning_effort; DeepInfra returns the trace in
        # message.reasoning_content, Ollama in message.reasoning.
        return {"reasoning_effort": "none" if effort == "off" else effort}
    if profile == "openrouter":
        if effort == "off":
            return {"reasoning": {"enabled": False}}
        return {"reasoning": {"effort": effort}}
    if profile == "generic":
        if effort in ("low", "medium", "max"):
            raise ValueError(
                "provider profile 'generic' drives thinking with a binary "
                "chat_template_kwargs.enable_thinking switch and cannot distinguish "
                f"effort={effort!r} from 'high'. Use profile 'ollama', 'deepinfra' or "
                "'openrouter' for a graded dial, or run the arm at 'off'/'high'."
            )
        return {"chat_template_kwargs": {"enable_thinking": effort != "off"}}
    raise ValueError(f"Unknown provider profile: {profile!r}")


#: `max_tokens` floor once thinking is on. Thinking + a tight budget returns empty
#: content (observed locally on qwen3:8b; model-slate.md §3).
THINKING_MAX_TOKENS = 2048

#: Output capacity must be EQUAL across effort arms, or a "more effort -> more
#: posting" slope is an output-capacity artifact (review-astra §5). The population
#: runner therefore sends one configured `max_tokens` in every arm; this floor is
#: only a safety net for callers that leave a thinking arm at a tiny budget.
def resolve_max_tokens(effort: str, max_tokens: int) -> int:
    from coop.models import min_max_tokens

    floor = max(min_max_tokens(effort), THINKING_MAX_TOKENS if effort != "off" else 0)
    return max(max_tokens, floor)


ToolHandler = Callable[[str, dict], Any]
