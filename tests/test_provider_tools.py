"""Provider tool loop, reasoning capture and the effort dial — no network."""

from __future__ import annotations

import types

import pytest

from coop.providers.base import (
    EFFORT_LEVELS,
    THINKING_MAX_TOKENS,
    UnlistedToolCall,
    effort_body,
    resolve_max_tokens,
)
from coop.providers.mock import MockClient
from coop.providers.openai_compat import OpenAICompatClient

TOOLS = [
    {"type": "function", "function": {"name": "notes_read", "parameters": {}}},
    {"type": "function", "function": {"name": "notes_post", "parameters": {}}},
    {"type": "function", "function": {"name": "ledger_lookup", "parameters": {}}},
]


class _FakeCompletions:
    def __init__(self, scripted):
        self.scripted = list(scripted)
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return self.scripted.pop(0)


class _FakeClient:
    def __init__(self, scripted):
        self.chat = types.SimpleNamespace(completions=_FakeCompletions(scripted))


def _msg(content=None, *, reasoning=None, tool_calls=None):
    m = types.SimpleNamespace(content=content, tool_calls=tool_calls, model_extra={})
    if reasoning is not None:
        m.reasoning = reasoning
    return types.SimpleNamespace(
        choices=[types.SimpleNamespace(message=m)],
        usage=types.SimpleNamespace(prompt_tokens=100, completion_tokens=7,
                                    completion_tokens_details=None),
    )


def _tool_call(name, arguments="{}", cid="call_1"):
    return types.SimpleNamespace(
        id=cid, function=types.SimpleNamespace(name=name, arguments=arguments)
    )


def _client(scripted):
    return OpenAICompatClient("m", client=_FakeClient(scripted), profile="ollama")


def test_effort_body_per_profile():
    assert effort_body("ollama", "off") == {"reasoning_effort": "none"}
    assert effort_body("ollama", "high") == {"reasoning_effort": "high"}
    assert effort_body("openrouter", "off") == {"reasoning": {"enabled": False}}
    assert effort_body("openrouter", "medium") == {"reasoning": {"effort": "medium"}}
    assert effort_body("generic", "high") == {"chat_template_kwargs": {"enable_thinking": True}}
    assert effort_body("deepinfra", "medium") == {"reasoning_effort": "medium"}
    assert effort_body("none", "high") == {}
    with pytest.raises(ValueError):
        effort_body("ollama", "maximum")
    # The generic switch is binary: it must refuse a level it cannot deliver
    # rather than advertise an effort contrast that is no intervention at all.
    for level in ("low", "medium"):
        with pytest.raises(ValueError, match="binary"):
            effort_body("generic", level)


def test_max_tokens_floor_reserves_an_answer_budget():
    assert resolve_max_tokens("off", 16) == 16
    for level in ("low", "medium"):
        assert resolve_max_tokens(level, 16) == THINKING_MAX_TOKENS
    # gpt-oss-120b at high spent its whole 1024-token budget on reasoning and
    # returned finish_reason=length with empty content.
    for level in ("high", "max"):
        assert resolve_max_tokens(level, 16) == 4096
    assert resolve_max_tokens("high", 8192) == 8192


def test_tool_loop_executes_and_appends_results():
    c = _client([
        _msg(content="", tool_calls=[_tool_call("notes_read")]),
        _msg(content="C", reasoning="the board was empty"),
    ])
    seen = []

    def handler(name, args):
        seen.append((name, args))
        return {"entries": []}

    out = c.chat([{"role": "user", "content": "go"}], tools=TOOLS, tool_handler=handler,
                 effort="low", seed=7)
    assert seen == [("notes_read", {})]
    assert out.raw == "C"
    assert out.reasoning == "the board was empty"
    assert out.tool_calls == [{"name": "notes_read", "args": {}, "iteration": 1}]
    assert out.tool_results[0]["ok"] is True
    assert out.iterations == 2
    assert out.prompt_tokens == 200 and out.completion_tokens == 14
    sent = c._client.chat.completions.calls
    assert sent[0]["seed"] == 7
    assert sent[0]["extra_body"] == {"reasoning_effort": "low"}
    assert sent[0]["max_tokens"] == THINKING_MAX_TOKENS
    # the tool result was appended to the conversation
    assert sent[1]["messages"][-1]["role"] == "tool"


def test_tool_loop_stops_after_three_iterations():
    c = _client([_msg(content="", tool_calls=[_tool_call("notes_read")]) for _ in range(3)])
    out = c.chat([{"role": "user", "content": "go"}], tools=TOOLS,
                 tool_handler=lambda n, a: {"entries": []})
    assert out.iterations == 3
    assert len(out.tool_calls) == 3


def test_unlisted_tool_call_is_logged_and_the_loop_continues():
    """A hallucinated tool name must not end the sandbox.

    A model called 'workspace' in runs/v2/B2-forbidden-off-ahead.partial-...; the
    raise propagated through Match.play and killed a 4-hour run. It is now a logged
    tool_calls entry, a JSON error handed back to the model, and a normal answer.
    """
    c = _client([
        _msg(content="", tool_calls=[_tool_call("workspace")]),
        _msg(content="C"),
    ])
    seen = []
    out = c.chat([{"role": "user", "content": "go"}], tools=TOOLS,
                 tool_handler=lambda n, a: seen.append(n))

    assert out.raw == "C"                       # the move still completed
    assert seen == []                           # nothing was executed
    assert out.tool_calls == [
        {"name": "workspace", "args": {}, "iteration": 1, "unlisted": True}
    ]
    assert out.tool_results[0]["ok"] is False
    assert "workspace" in out.tool_results[0]["result"]["error"]
    # the model was told, in a role:tool turn, that the tool does not exist
    tool_msg = c._client.chat.completions.calls[1]["messages"][-1]
    assert tool_msg["role"] == "tool"
    assert "unknown tool" in tool_msg["content"]


def test_handler_exception_becomes_an_error_tool_result():
    c = _client([
        _msg(content="", tool_calls=[_tool_call("notes_post", '{"text": 42}')]),
        _msg(content="D"),
    ])

    def boom(name, args):
        raise TypeError("text must be a string")

    out = c.chat([{"role": "user", "content": "go"}], tools=TOOLS, tool_handler=boom)
    assert out.raw == "D"
    assert out.tool_calls[0].get("unlisted") is None
    assert out.tool_results[0]["ok"] is False
    assert "text must be a string" in out.tool_results[0]["result"]["error"]


def test_listed_tool_without_a_handler_is_reported_not_raised():
    c = _client([
        _msg(content="", tool_calls=[_tool_call("notes_read")]),
        _msg(content="C"),
    ])
    out = c.chat([{"role": "user", "content": "go"}], tools=TOOLS, tool_handler=None)
    assert out.raw == "C"
    assert out.tool_results[0]["ok"] is False


def test_provider_error_is_recorded_not_raised():
    class _Boom:
        def create(self, **kw):
            raise RuntimeError("connection reset")

    c = OpenAICompatClient("m", client=types.SimpleNamespace(
        chat=types.SimpleNamespace(completions=_Boom())), profile="ollama")
    out = c.chat([{"role": "user", "content": "go"}])
    assert out.error and "connection reset" in out.error
    assert out.raw == ""


def test_think_block_recovered_as_reasoning():
    c = _client([_msg(content="<think>weighing it up</think>\nD")])
    out = c.chat([{"role": "user", "content": "go"}])
    assert "weighing it up" in out.reasoning


def test_mock_poster_calls_notes_post():
    out = MockClient("poster").chat([{"role": "user", "content": "<!--mock kind=move C=C D=D-->"}],
                                    tools=TOOLS, tool_handler=lambda n, a: {"ok": True})
    assert [tc["name"] for tc in out.tool_calls] == ["notes_post"]
    assert out.raw == "C"


def test_mock_poster_raises_when_no_tools_offered():
    """The mock keeps its own self-check: a tool policy with no tools listed is a
    harness misconfiguration, not model behaviour, and must still fail loudly."""
    with pytest.raises(UnlistedToolCall):
        MockClient("poster").chat([{"role": "user", "content": "<!--mock kind=move C=C D=D-->"}],
                                  tools=None, tool_handler=None)


def test_mock_decoy_calls_ledger_lookup():
    out = MockClient("decoy").chat([{"role": "user", "content": "<!--mock kind=move C=C D=D-->"}],
                                   tools=TOOLS, tool_handler=lambda n, a: {"score": 0})
    assert [tc["name"] for tc in out.tool_calls] == ["ledger_lookup"]


def test_mock_honours_neutral_labels_and_question_kind():
    m = MockClient("cooperator")
    out = m.chat([{"role": "user", "content": "<!--mock kind=move C=J D=F-->"}])
    assert out.raw == "J"
    q = m.chat([{"role": "user", "content": "<!--mock kind=question-->"}], tools=TOOLS)
    assert q.tool_calls == []
