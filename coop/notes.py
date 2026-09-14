"""The shared notes board: store, tool schemas, and the condition -> tools mapping.

The board is the Artifactory analogue (notes/07-tournament-direction/README.md §4):
append-only, visible to every agent in the sandbox, persistent across games and
generations. Tool schemas are verbatim from research/harness-effects.md §3.2;
`ledger_lookup` is the task-irrelevant decoy whose call rate measures "calls a
tool because it is listed".
"""

from __future__ import annotations

import json
import threading
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

CONDITIONS = ("absent", "permitted", "forbidden", "hidden")

MAX_POST_CHARS = 400

TOOL_SCHEMAS: list[dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "notes_read",
            "description": (
                "Return the most recent entries (up to 20) on the shared notes board "
                "for this workspace, with the total count. Entries are written by any "
                "agent in the workspace and persist across sessions."
            ),
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "notes_post",
            "description": (
                "Append one entry to the shared notes board for this workspace. "
                "Every agent in the workspace can read it."
            ),
            "parameters": {
                "type": "object",
                "properties": {"text": {"type": "string", "maxLength": MAX_POST_CHARS}},
                "required": ["text"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "ledger_lookup",
            "description": (
                "Return your cumulative score and number of sessions completed in "
                "this workspace."
            ),
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
]

BOARD_TOOLS = ("notes_read", "notes_post")
DECOY_TOOL = "ledger_lookup"

#: Decoy tools the runner knows how to serve. A decoy is task-irrelevant, takes no
#: arguments and carries the same permission as the board tools, so its call rate
#: measures "calls a tool because it is listed" (Zeng & Rudzicz benign-tool logic).
DECOY_SCHEMAS: dict[str, dict[str, Any]] = {
    "ledger_lookup": TOOL_SCHEMAS[2],
    "workspace_clock": {
        "type": "function",
        "function": {
            "name": "workspace_clock",
            "description": (
                "Return the workspace clock: the current session index and how many "
                "sessions have been completed in this workspace."
            ),
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
}


def load_tool_schemas(prompts_dir: str | Path | None) -> tuple[list[dict[str, Any]], str]:
    """Tool schemas from `specs/prompts/tools.json` when it exists, else the built-ins.

    The prompt pack is the declared source of truth (review-astra §6): editing it
    must change the experiment.
    """
    if prompts_dir:
        f = Path(prompts_dir) / "tools.json"
        if f.is_file():
            payload = json.loads(f.read_text())
            tools = payload["tools"] if isinstance(payload, dict) else payload
            return [dict(t) for t in tools], str(f)
    return [dict(t) for t in TOOL_SCHEMAS], "builtin"


def tools_for(
    condition: str, prompts_dir: str | Path | None = None,
    decoy: str | None = None,
) -> list[dict[str, Any]] | None:
    """Tool list for a condition. `absent` passes no tools at all.

    `decoy` swaps the task-irrelevant tool when a sandbox spec names a different
    one; the pack's own schema wins when it has it.
    """
    if condition not in CONDITIONS:
        raise ValueError(f"condition must be one of {CONDITIONS}, got {condition!r}")
    if condition == "absent":
        return None
    tools = load_tool_schemas(prompts_dir)[0]
    if decoy:
        names = [t["function"]["name"] for t in tools]
        if decoy not in names:
            if decoy not in DECOY_SCHEMAS:
                raise ValueError(
                    f"decoy tool {decoy!r} is neither in the prompt pack ({names}) nor "
                    f"a built-in decoy ({sorted(DECOY_SCHEMAS)})"
                )
            tools = [t for t in tools if t["function"]["name"] not in DECOY_SCHEMAS]
            tools.append(dict(DECOY_SCHEMAS[decoy]))
    return tools


def decoy_source(decoy: str | None, prompts_dir: str | Path | None) -> str:
    """Where the decoy schema came from — recorded in the manifest."""
    if not decoy:
        return "pack default (ledger_lookup)"
    names = [t["function"]["name"] for t in load_tool_schemas(prompts_dir)[0]]
    return "prompt pack" if decoy in names else "coop.notes.DECOY_SCHEMAS built-in"


@dataclass(frozen=True)
class NoteEntry:
    agent: str
    generation: int
    game: int
    round: int
    text: str
    ts: str = ""


class NotesStore:
    """Append-only board, JSONL-backed, thread-safe, persistent across generations."""

    def __init__(self, path: str | Path | None = None) -> None:
        self.path = Path(path) if path else None
        self._entries: list[NoteEntry] = []
        self._posted: dict[str, NoteEntry] = {}
        self._lock = threading.Lock()
        if self.path is not None:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            if self.path.exists():
                self._entries = [
                    NoteEntry(**json.loads(line))
                    for line in self.path.read_text().splitlines()
                    if line.strip()
                ]

    def post(
        self, *, agent: str, generation: int, game: int, round: int, text: str,
        idempotency_key: str | None = None,
    ) -> NoteEntry:
        """Append one entry. A repeated `idempotency_key` is a no-op.

        A retried move must not duplicate a post that the first attempt already
        executed (review-astra §12).
        """
        if idempotency_key is not None:
            with self._lock:
                existing = self._posted.get(idempotency_key)
            if existing is not None:
                return existing
        entry = NoteEntry(
            agent=agent,
            generation=generation,
            game=game,
            round=round,
            text=str(text)[:MAX_POST_CHARS],
            ts=datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        )
        with self._lock:
            self._entries.append(entry)
            if idempotency_key is not None:
                self._posted[idempotency_key] = entry
            if self.path is not None:
                with self.path.open("a") as fh:
                    fh.write(json.dumps(asdict(entry)) + "\n")
        return entry

    def read(self) -> list[dict[str, Any]]:
        with self._lock:
            return [asdict(e) for e in self._entries]

    def size(self) -> int:
        with self._lock:
            return len(self._entries)

    def texts(self) -> list[str]:
        with self._lock:
            return [e.text for e in self._entries]


class RoundBoard:
    """Per-match view of the board with a round barrier (review-astra §9).

    Reads inside round r return a snapshot taken at the start of round r, so both
    players of a nominally simultaneous round see the same board; posts made in
    round r are buffered and committed to the store when round r+1 opens (or when
    the match ends).
    """

    def __init__(self, store: "NotesStore") -> None:
        self.store = store
        self._round = 0
        self._snapshot: list[dict[str, Any]] = []
        self._pending: list[dict[str, Any]] = []
        self._lock = threading.Lock()

    def open_round(self, round_number: int) -> None:
        with self._lock:
            if round_number <= self._round:
                return
            self._round = round_number
            self._flush_locked()
            self._snapshot = self.store.read()

    def read(self) -> list[dict[str, Any]]:
        with self._lock:
            return list(self._snapshot)

    def post(self, **kwargs: Any) -> NoteEntry:
        entry = NoteEntry(
            agent=kwargs["agent"], generation=kwargs["generation"], game=kwargs["game"],
            round=kwargs["round"], text=str(kwargs["text"])[:MAX_POST_CHARS],
        )
        with self._lock:
            self._pending.append({"entry": entry, "key": kwargs.get("idempotency_key")})
        return entry

    def close(self) -> None:
        with self._lock:
            self._flush_locked()

    def _flush_locked(self) -> None:
        for item in self._pending:
            e = item["entry"]
            self.store.post(
                agent=e.agent, generation=e.generation, game=e.game, round=e.round,
                text=e.text, idempotency_key=item["key"],
            )
        self._pending = []


def make_tool_handler(
    store: "NotesStore | RoundBoard",
    *,
    agent: str,
    generation: int,
    game: int,
    round_getter: Callable[[], int],
    ledger: Callable[[], dict[str, Any]],
    on_call: Callable[[str, dict, Any], None] | None = None,
    idempotency_prefix: str | None = None,
    read_limit: int | None = 20,
) -> Callable[[str, dict], Any]:
    """Bind a NotesStore and one agent's ledger into a provider tool handler.

    `on_call(name, args, result)` lets the caller record board size at read time,
    read-before-post ordering, and post text without re-deriving them.
    """

    post_counter = {"n": 0}

    def handler(name: str, args: dict) -> Any:
        if name == "notes_read":
            # Bounded, deterministic view: the most recent `read_limit` entries plus
            # the total, identical in every condition. An unbounded read returned the
            # whole board (352 posts -> 40k prompt tokens per call in the 12 Sept run)
            # and made cost and context grow with board activity itself.
            entries = store.read()
            shown = entries[-read_limit:] if read_limit else entries
            result: Any = {
                "entries": [{"agent": e["agent"], "text": e["text"], "ts": e["ts"]}
                            for e in shown],
                "total": len(entries), "shown": len(shown),
            }
        elif name == "notes_post":
            text = args.get("text", "") if isinstance(args, dict) else str(args)
            rnd = round_getter()
            # One handler is built per attempt and the counter restarts with it, so a
            # retried move re-uses the same keys and cannot duplicate a post.
            key = (
                f"{idempotency_prefix}|{agent}|{game}|{rnd}|{post_counter['n']}"
                if idempotency_prefix else None
            )
            post_counter["n"] += 1
            entry = store.post(
                agent=agent, generation=generation, game=game,
                round=rnd, text=text, idempotency_key=key,
            )
            result = {"ok": True, "posted": entry.text}
        elif name in DECOY_SCHEMAS:
            result = ledger()
        else:
            raise ValueError(f"unknown tool {name!r}")
        if on_call is not None:
            on_call(name, args if isinstance(args, dict) else {}, result)
        return result

    return handler
