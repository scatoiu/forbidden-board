"""Summarise a pilot run directory. Read-only."""
import json, sys
from collections import Counter
from pathlib import Path

for d in sorted(Path(sys.argv[1]).iterdir()):
    f = d / "moves.jsonl"
    if not f.is_file():
        continue
    rows = [json.loads(l) for l in f.read_text().splitlines()]
    mv = [r for r in rows if r["kind"] == "move"]
    llm = [m for m in mv if not m["model"].startswith("script:")]
    ge = [r for r in rows if r["kind"] == "game_end"]
    gen = [r for r in rows if r["kind"] == "generation_end"]
    fb = Counter(m["fallback_flag"] for m in llm if not m["parse_ok"])
    tc = Counter(c["name"] for m in llm for c in m["tool_calls"])
    reason = sum(1 for m in llm if (m.get("reasoning") or "").strip())
    fr = Counter(m.get("finish_reason") for m in llm)
    coop = [m["action"] for m in llm if m["parse_ok"]]
    print(f"\n=== {d.name} ===")
    print(f"  rows: move={len(mv)} game_end={len(ge)} generation_end={len(gen)}")
    print(f"  llm moves={len(llm)}  parsed={sum(1 for m in llm if m['parse_ok'])}"
          f"  fallbacks={len(llm)-sum(1 for m in llm if m['parse_ok'])} {dict(fb)}")
    print(f"  cooperation (llm, parsed) = "
          f"{round(coop.count('C')/len(coop),3) if coop else None}")
    print(f"  tool calls: {dict(tc) or 'none'}   finish_reason: {dict(fr)}")
    print(f"  reasoning captured on {reason}/{len(llm)} llm moves")
    if gen:
        g = gen[0]
        print(f"  climate={g['climate']['coop_rate_overall']}  board={g['board']}"
              f"  aborted={g['aborted_games']}  chance_baseline="
              f"{g['classification_chance_baseline']}")
    if ge:
        cc = [e["classification_correct"] for e in ge]
        print(f"  classification: correct={cc.count(True)} wrong={cc.count(False)} "
              f"unscored={cc.count(None)} of {len(ge)}")
        pr = [e["prohibition_recall_correct"] for e in ge if e.get("prohibition_recall_correct") is not None]
        if pr:
            print(f"  prohibition recall correct: {sum(pr)}/{len(pr)}")
        used = [e for e in ge if e["channel_used"]]
        print(f"  games with a board call: {len(used)}/{len(ge)};"
              f" decoy calls={sum(e['decoy_count'] for e in ge)}")
