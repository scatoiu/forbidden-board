"""Per-model reasoning-dial availability. Encoded, never assumed.

Live-verified against DeepInfra on 12 Sept 2026 (specs/first-contact-2026-09-12.md,
specs/providers-matrix.md). The ten slate models do NOT share one interchangeable
{off, low, medium, high} dial, so an arm that asks for a level a model cannot
deliver is refused at build time rather than silently becoming "no intervention"
(review-astra §5).

`grades` lists the levels the provider actually distinguishes. `binary` models
accept only off/on: any on-level is sent as the single on setting and recorded as
such, so no graded dose-response may be claimed for them.
"""

from __future__ import annotations

from dataclasses import dataclass

DEEPINFRA_BASE_URL = "https://api.deepinfra.com/v1/openai"
DEEPINFRA_KEY_VAR = "DEEPINFRA_API_KEY"


@dataclass(frozen=True)
class EffortSupport:
    grades: tuple[str, ...]          # levels the provider distinguishes
    binary: bool = False             # on/off only; grades collapse to "on"
    on_level: str = "high"           # what an on-level is actually sent as
    trace_location: str = "field"    # "field" (reasoning[_content]) or "inline"
    notes: str = ""


#: model id -> support. Unknown models fall back to UNKNOWN_SUPPORT.
EFFORT_SUPPORT: dict[str, EffortSupport] = {
    # --- DeepInfra slate, verified live ---
    "deepseek-ai/DeepSeek-V4-Flash-0731": EffortSupport(
        ("off", "low", "high", "max"), notes="all four verified live"),
    "XiaomiMiMo/MiMo-V2.5-Pro": EffortSupport(
        ("off", "high"), notes="off and high verified live 12 Sept (none -> 0 trace chars, tool calls; high -> ~750 chars in reasoning_content)"),
    "openai/gpt-oss-120b": EffortSupport(
        ("low", "medium", "high"), notes="no off; reasoning is mandatory"),
    "openai/gpt-oss-20b": EffortSupport(
        ("low", "medium", "high"), notes="no off; reasoning is mandatory"),
    "zai-org/GLM-5.3-Flash": EffortSupport(
        ("low", "high", "max"), notes="no off"),
    "Qwen/Qwen3-32B": EffortSupport(
        ("off", "high"), binary=True, on_level="high", trace_location="inline",
        notes="binary thinking; trace arrives INLINE in content, and <tool_call> "
              "markup leaks into content even with thinking off"),
    "Qwen/Qwen3.5-9B": EffortSupport(("off", "high"), binary=True),
    "google/gemma-4-26B-A4B-it": EffortSupport(("off", "high"), binary=True),
    "meta-llama/Llama-3.3-70B-Instruct-Turbo": EffortSupport(("off",), notes="no dial"),
    "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo": EffortSupport(("off",), notes="no dial"),
    "Qwen/Qwen2.5-72B-Instruct": EffortSupport(("off",), notes="no dial"),
    # --- local Ollama, verified on this Mac ---
    "qwen3:8b": EffortSupport(("off", "high"), binary=True,
                              notes="reasoning_effort none|low|medium|high accepted; "
                                    "only on/off is a real distinction"),
    "qwen3-coder:30b": EffortSupport(("off",), notes="no reasoning mode"),
    "gpt-oss:20b": EffortSupport(("low", "medium", "high"),
                                 notes="graded locally: 32 vs 607 completion tokens"),
}

UNKNOWN_SUPPORT = EffortSupport(("off", "low", "medium", "high"),
                                notes="unregistered model: dial assumed, not verified")

#: Once reasoning is on at this level or above, reserve a larger answer budget:
#: gpt-oss-120b at high spent 1024 tokens and returned finish_reason=length with
#: empty content.
HIGH_EFFORT_LEVELS = ("high", "max")
HIGH_EFFORT_MIN_MAX_TOKENS = 4096


def support_for(model: str) -> EffortSupport:
    return EFFORT_SUPPORT.get(model, UNKNOWN_SUPPORT)


def resolve_effort(model: str, effort: str) -> tuple[str, dict]:
    """Map a requested effort level onto what this model can actually do.

    Returns (level to send, a record of the mapping for the manifest). Raises
    ValueError when the model cannot deliver the requested level at all.
    """
    sup = support_for(model)
    record = {
        "model": model, "requested": effort, "grades": list(sup.grades),
        "binary": sup.binary, "trace_location": sup.trace_location, "notes": sup.notes,
    }
    if effort in sup.grades:
        record["sent"] = effort
        return effort, record
    if effort == "off":
        raise ValueError(
            f"{model} cannot run with reasoning off (grades: {sup.grades}). "
            "Drop the off arm for this model or choose another model."
        )
    if sup.binary and effort in ("low", "medium", "high", "max"):
        record["sent"] = sup.on_level
        record["collapsed"] = (
            f"{model} exposes binary thinking: {effort!r} is sent as {sup.on_level!r}; "
            "no graded dose-response may be claimed for this model."
        )
        return sup.on_level, record
    raise ValueError(
        f"{model} does not distinguish effort={effort!r} (grades: {sup.grades}). "
        "Pick a supported level or a model with the dial."
    )


def min_max_tokens(effort: str) -> int:
    """Answer budget floor: reasoning must not eat the whole completion."""
    return HIGH_EFFORT_MIN_MAX_TOKENS if effort in HIGH_EFFORT_LEVELS else 0
