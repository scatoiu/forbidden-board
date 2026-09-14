"""OpenAI-compatible provider — works for OpenAI, Ollama, LM Studio, vLLM, OpenRouter.

Local model support is a config change (set base_url), not a code change.

`chat()` is the population-runner entry point: system/user messages, an optional
tool list executed through a caller-supplied handler (up to `max_tool_iterations`
round trips), reasoning capture from `message.reasoning` /
`message.reasoning_content` / a stripped `<think>` block, a `seed`, and the
reasoning-effort dial mapped onto the provider profile.
"""

from __future__ import annotations

import json
import logging
import os
import time
from typing import Any

from coop.providers.base import (
    LLMResponse,
    ProviderResult,
    ToolHandler,
    effort_body,
    parse_action,
    resolve_max_tokens,
    strip_think,
)

log = logging.getLogger(__name__)

DEFAULT_SYSTEM = (
    "You are a player in an iterated game. Respond to each prompt with one move only. "
    "Output a single character C (cooperate) or D (defect) at the end of your reply. "
    "Optional one-line reasoning may precede the move."
)


class OpenAICompatClient:
    """Wrapper around chat.completions.create. Works for any OpenAI-compatible endpoint."""

    def __init__(
        self,
        model: str,
        *,
        base_url: str | None = None,
        api_key: str | None = None,
        system: str | None = None,
        client: Any | None = None,
        profile: str = "generic",
        quant: str | None = None,
        timeout: float | None = 480.0,
        max_retries: int = 1,
    ) -> None:
        try:
            from openai import OpenAI  # type: ignore
        except ImportError as e:
            raise ImportError(
                "openai SDK not installed. `pip install openai` (or coop[openai])."
            ) from e
        self.model = model
        self.name = f"openai_compat:{model}" if base_url else f"openai:{model}"
        self.system = system or DEFAULT_SYSTEM
        self.profile = profile
        self.quant = quant
        # base_url=None defaults to api.openai.com. Local servers pass e.g.
        # http://localhost:11434/v1 (Ollama) or http://localhost:1234/v1 (LM Studio).
        # api_key may be a placeholder for local servers; OpenAI SDK requires it non-empty.
        self._client = client or OpenAI(
            api_key=api_key or os.environ.get("OPENAI_API_KEY") or "local-no-auth",
            base_url=base_url or os.environ.get("OPENAI_BASE_URL"),
            timeout=timeout,
            # The harness's own two-attempt rule owns retries; the SDK default of two
            # silent retries on top of it made one failed decision cost up to an hour
            # (3 x 600 s x 2 attempts) in the 12 Sept run.
            max_retries=max_retries,
        )

    # ---------------- legacy single-prompt path (coop.tournament) ----------------

    def move(self, prompt: str, *, temperature: float = 0.2, max_tokens: int = 64) -> LLMResponse:
        resp = self._client.chat.completions.create(
            model=self.model,
            temperature=temperature,
            max_tokens=max_tokens,
            messages=[
                {"role": "system", "content": self.system},
                {"role": "user", "content": prompt},
            ],
        )
        text = resp.choices[0].message.content or ""
        parsed = parse_action(text)
        return LLMResponse(action=parsed.action or "", raw=text, reasoning=parsed.reasoning)

    # ---------------- population-runner path ------------------------------------

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
        out = ProviderResult()
        convo = list(messages)
        max_tokens = resolve_max_tokens(effort, max_tokens)
        extra = effort_body(self.profile, effort)
        listed = {t["function"]["name"] for t in (tools or [])}
        t0 = time.perf_counter()
        # True while the last completion carried tool calls: its content is
        # pre-result prose ("I will check the notes"), not a decision, even when it
        # happens to contain a label (Astra review, finding 11).
        answer_owed = False

        try:
            for iteration in range(1, max_tool_iterations + 1):
                out.iterations = iteration
                kwargs: dict[str, Any] = {
                    "model": self.model,
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                    "messages": convo,
                }
                if tools:
                    kwargs["tools"] = tools
                if seed is not None:
                    kwargs["seed"] = seed
                if extra:
                    kwargs["extra_body"] = extra

                resp = self._client.chat.completions.create(**kwargs)
                choice = resp.choices[0]
                msg = choice.message
                out.finish_reason = getattr(choice, "finish_reason", None)
                _accumulate_usage(out, resp, iteration)
                reasoning = _extract_reasoning(msg)
                if reasoning:
                    out.reasoning = (out.reasoning + "\n" + reasoning).strip()

                content = msg.content or ""
                out.trace_location = "field" if reasoning else (
                    "inline" if "<think>" in content else out.trace_location
                )
                calls = list(getattr(msg, "tool_calls", None) or [])
                answer_owed = bool(calls)
                if not calls:
                    clean, recovered = strip_think(content)
                    out.raw = content
                    if recovered and not out.reasoning:
                        out.reasoning = recovered
                    break

                convo.append(_assistant_turn(msg, calls))
                for call in calls:
                    name = call.function.name
                    args = _safe_args(call.function.arguments)
                    entry: dict[str, Any] = {
                        "name": name, "args": args, "iteration": iteration,
                    }
                    # A hallucinated tool name, an unavailable handler and a handler
                    # that raises are all DATA, not fatal errors: they are logged, the
                    # model is handed a JSON error so it can continue, and the loop
                    # goes on. Raising here cost a 4-hour sandbox on 2026-09-12
                    # (runs/v2/B2-forbidden-off-ahead.partial-20260912T221328Z).
                    problem: str | None = None
                    if name not in listed:
                        entry["unlisted"] = True
                        problem = f"unknown tool {name!r}"
                    elif tool_handler is None:
                        problem = f"no tool handler available for {name!r}"
                    out.tool_calls.append(entry)
                    if problem is not None:
                        log.warning("%s (listed: %s)", problem, sorted(listed))
                        result: Any = {"error": problem}
                        ok = False
                    else:
                        try:
                            result, ok = tool_handler(name, args), True
                        except Exception as e:   # bad args, oversized text, disk error
                            result = {"error": f"{type(e).__name__}: {e}"}
                            ok = False
                            log.warning("tool %r raised: %s", name, result["error"])
                    out.tool_results.append({"name": name, "ok": ok, "result": result})
                    convo.append({
                        "role": "tool",
                        "tool_call_id": getattr(call, "id", None) or name,
                        "content": json.dumps(result, default=str),
                    })
                out.raw = content
            # Forced-answer turn: the loop ended with tool calls still pending or an
            # empty message. Ask once more with tools disabled so a board-happy model
            # (MiMo read the board at the last iteration in 2/8 early games) still
            # delivers a decision. Recorded as forced_answer=True; never coerced.
            #
            # Second forced call, on a tool-free transcript. While the tool_call /
            # tool messages are in the prompt, MiMo-V2.5-Pro on DeepInfra keeps
            # emitting a tool call at the forced turn, and the endpoint drops the
            # whole completion: content=null, tool_calls=null, reasoning_content=null,
            # finish_reason "stop"/"length", tokens billed. 16 of 51 forced turns in
            # the 12 Sept mini-pilot. Seed-matched probes on those 16: dropping
            # `tools` but keeping the tool turns recovers 1/16; replaying the same
            # request with tool_choice unset returns a native notes_post/notes_read
            # call in 9/12; replaying with the tool turns flattened into one user
            # message and no tools recovers 16/16. So the retry rebuilds the prompt
            # from `messages` (system + state block) plus that flattened text. It is
            # still one ordinary sample: parse_action applies its strict final-line
            # rule to whatever comes back, and nothing here coerces an action.
            if (answer_owed or not (out.raw or "").strip()) and out.error is None:
                ask = {"role": "user", "content": "Give your pick now, on one line."}
                flat: list[str] = []
                for turn in convo[len(messages):]:
                    if turn.get("role") == "tool":
                        flat.append(f"tool result: {turn.get('content')}")
                    for c in (turn.get("tool_calls") or []):
                        fn = c["function"]
                        flat.append(f"you called {fn['name']}({fn['arguments']})")
                notes = ([{"role": "user", "content":
                           "Tool activity so far this turn:\n" + "\n".join(flat)}]
                         if flat else [])
                plans = [(convo + [ask], bool(tools))]
                if tools:
                    plans.append((list(messages) + notes + [ask], False))
                for forced_msgs, send_tools in plans:
                    kwargs = {"model": self.model, "temperature": temperature,
                              "max_tokens": max_tokens, "messages": forced_msgs}
                    if send_tools:
                        kwargs["tools"] = tools
                        kwargs["tool_choice"] = "none"
                    if seed is not None:
                        kwargs["seed"] = seed
                    if extra:
                        kwargs["extra_body"] = extra
                    resp = self._client.chat.completions.create(**kwargs)
                    choice = resp.choices[0]
                    msg = choice.message
                    out.finish_reason = getattr(choice, "finish_reason", None)
                    _accumulate_usage(out, resp, out.iterations + 1)
                    reasoning = _extract_reasoning(msg)
                    if reasoning:
                        out.reasoning = (out.reasoning + "\n" + reasoning).strip()
                    clean, recovered = strip_think(msg.content or "")
                    # One row per forced call, so a future empty_content says which
                    # shape was sent and what came back (specs/moves-schema.md).
                    out.forced_turn.append({
                        "tools_sent": bool(send_tools),
                        "finish_reason": out.finish_reason,
                        "had_tool_calls": bool(getattr(msg, "tool_calls", None)),
                        "content_len": len(msg.content or ""),
                        "reasoning_len": len(reasoning or ""),
                    })
                    out.raw = msg.content or ""
                    if recovered and not out.reasoning:
                        out.reasoning = recovered
                    out.forced_answer = True
                    if clean.strip():
                        break
        except Exception as e:  # provider/network/timeout — logged, never coerced
            out.error = f"{type(e).__name__}: {e}"
            log.warning("provider call failed: %s", out.error)

        out.latency_ms = int((time.perf_counter() - t0) * 1000)
        return out


def _assistant_turn(msg: Any, calls: list) -> dict[str, Any]:
    return {
        "role": "assistant",
        "content": msg.content or "",
        "tool_calls": [
            {
                "id": getattr(c, "id", None) or c.function.name,
                "type": "function",
                "function": {"name": c.function.name, "arguments": c.function.arguments},
            }
            for c in calls
        ],
    }


def _safe_args(raw: Any) -> dict[str, Any]:
    if isinstance(raw, dict):
        return raw
    try:
        parsed = json.loads(raw or "{}")
        return parsed if isinstance(parsed, dict) else {"_raw": parsed}
    except (json.JSONDecodeError, TypeError):
        return {"_raw": str(raw)}


def _extract_reasoning(msg: Any) -> str:
    for attr in ("reasoning", "reasoning_content"):
        val = getattr(msg, attr, None)
        if val:
            return str(val)
    extra = getattr(msg, "model_extra", None) or {}
    for attr in ("reasoning", "reasoning_content"):
        if extra.get(attr):
            return str(extra[attr])
    return ""


def _accumulate_usage(out: ProviderResult, resp: Any, iteration: int) -> None:
    usage = getattr(resp, "usage", None)
    if not usage:
        return
    prompt = int(getattr(usage, "prompt_tokens", 0) or 0)
    completion = int(getattr(usage, "completion_tokens", 0) or 0)
    details = getattr(usage, "completion_tokens_details", None)
    reasoning = int(getattr(details, "reasoning_tokens", 0) or 0) if details else 0
    out.prompt_tokens += prompt
    out.completion_tokens += completion
    out.reasoning_tokens += reasoning
    # Per-completion usage, so an effort arm's real output spend is visible
    # rather than inferred (review-astra §5).
    out.usage.append({
        "iteration": iteration, "prompt_tokens": prompt,
        "completion_tokens": completion, "reasoning_tokens": reasoning,
        "estimated_cost": getattr(usage, "estimated_cost", None)
        or (getattr(usage, "model_extra", None) or {}).get("estimated_cost"),
    })
