"""notes_read is a bounded view: most recent N entries plus the total."""
from coop.notes import NotesStore, make_tool_handler


def _handler(store, limit):
    seen = {}
    h = make_tool_handler(store, agent="A00", generation=0, game=1, round_getter=lambda: 1,
                          ledger=lambda: {}, on_call=lambda n, a, r: seen.setdefault(n, r),
                          read_limit=limit)
    return h, seen


def test_read_returns_most_recent_entries_and_total():
    store = NotesStore()
    for i in range(25):
        store.post(agent=f"A{i:02d}", generation=0, game=i, round=1, text=f"note {i}")
    h, _ = _handler(store, 20)
    res = h("notes_read", {})
    assert res["total"] == 25 and res["shown"] == 20 and len(res["entries"]) == 20
    assert res["entries"][0]["text"] == "note 5" and res["entries"][-1]["text"] == "note 24"


def test_read_limit_none_is_unbounded_and_small_boards_are_whole():
    store = NotesStore()
    for i in range(3):
        store.post(agent="A00", generation=0, game=i, round=1, text=f"n{i}")
    assert _handler(store, None)[0]("notes_read", {})["shown"] == 3
    assert _handler(store, 20)[0]("notes_read", {})["shown"] == 3
