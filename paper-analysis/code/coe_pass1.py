import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Chain-of-evidence pass 1: independent streaming recomputation from RAW LOGS.

Reads runs/<root>/<sandbox>/moves.jsonl line by line, keeps only the fields the
endpoint needs, applies the repair merge at the aggregate level, and writes one
row per LLM agent-game plus a JSON of global counts. No use of analysis/*.
"""
from __future__ import annotations
import json, os, re, sys, csv
from collections import defaultdict

TOURN = _REPO+""
OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/coe"
os.makedirs(OUT, exist_ok=True)

ARCHIVE_RX = re.compile(r"\.(partial|contaminated|qualfail|quarantine|discarded|superseded)[-.]", re.I)
BOARD_TOOLS = {"notes_read", "notes_post"}
DECOY_TOOLS = {"workspace_clock", "ledger_lookup"}
PROVIDER_ERROR = {"provider_error"}

ROOTS = {                      # label -> list of root dirs
    "prereg":      ["runs/v3", "runs/v3b", "runs/v3-mimo"],
    "repair":      ["runs/v7-repair"],
    "replication": ["runs/v4-a4096"],
    "low_arm":     ["runs/v6-low"],
    "deficit_d30": ["runs/v5-d30"],
}


def live_names(calls):
    if not isinstance(calls, list):
        return []
    return [c.get("name") for c in calls if isinstance(c, dict) and not c.get("unlisted")]


def attempt_union(rec):
    """board/decoy/read/post counts over the UNION of every attempt."""
    attempts = rec.get("attempts")
    if isinstance(attempts, list) and attempts:
        names = []
        for a in attempts:
            if isinstance(a, dict):
                names += live_names(a.get("tool_calls"))
    else:
        names = live_names(rec.get("tool_calls"))
    b = sum(n in BOARD_TOOLS for n in names)
    return (b,
            sum(n in DECOY_TOOLS for n in names),
            sum(n == "notes_read" for n in names),
            sum(n == "notes_post" for n in names))


def new_ag():
    return dict(att_board=0, att_decoy=0, att_read=0, att_post=0,
                fin_board=0, fin_decoy=0, n_logged=0, n_played=0, n_aborted=0,
                n_coop=0, n_act=0, first_att_round=None, reasoning_tokens=0,
                n_unparsed=0, n_board_lost_by_retry=0)


def main():
    ag = {}                               # (label, sandbox, gen, game, agent) -> dict
    gmeta = defaultdict(lambda: dict(aborted_move=False, pe=False, played=0,
                                     move_rows=0, warmup_rows=0, scored=0, played_rows=0,
                                     game_end_rows=0))
    gends = []                            # game_end rows (dicts)
    manifests = {}                        # (label, sandbox) -> manifest
    gen_end_dirs = set()                  # (label, sandbox) with a generation_end row
    counts = defaultdict(int)

    for label, roots in ROOTS.items():
        for root in roots:
            rd = os.path.join(TOURN, root)
            if not os.path.isdir(rd):
                continue
            for sb in sorted(os.listdir(rd)):
                sd = os.path.join(rd, sb)
                if not os.path.isdir(sd) or ARCHIVE_RX.search(sb):
                    continue
                mf = os.path.join(sd, "manifest.json")
                mj = os.path.join(sd, "moves.jsonl")
                if not os.path.exists(mj):
                    continue
                man = json.load(open(mf)) if os.path.exists(mf) else {}
                man["_root"] = root
                manifests[(label, sb)] = man
                with open(mj) as f:
                    for line in f:
                        if not line.strip():
                            continue
                        r = json.loads(line)
                        k = r.get("kind")
                        sbx = r["sandbox"]
                        if k == "move":
                            counts[label + ":move_rows"] += 1
                            gen, gm = int(r["generation"]), int(r["game"])
                            is_llm = not str(r.get("model", "")).startswith("script:")
                            phase = r.get("phase") or "scored"
                            status = r.get("status") or "ok"
                            gkey = (label, sbx, gen, gm)
                            gmeta[gkey]["move_rows"] += 1
                            if status == "aborted":
                                gmeta[gkey]["aborted_move"] = True
                                if r.get("fallback_flag") in PROVIDER_ERROR:
                                    gmeta[gkey]["pe"] = True
                            if phase == "warmup":
                                counts[label + ":warmup_rows"] += 1
                                gmeta[gkey]["warmup_rows"] += 1
                                continue
                            if not is_llm:
                                continue
                            counts[label + ":scored_decisions"] += 1
                            gmeta[gkey]["scored"] += 1
                            if status == "ok":
                                counts[label + ":played"] += 1
                                gmeta[gkey]["played"] += 1
                                gmeta[gkey]["played_rows"] += 1
                            key = (label, sbx, gen, gm, r["agent"])
                            a = ag.get(key)
                            if a is None:
                                a = ag[key] = new_ag()
                            b, d, rdc, pc = attempt_union(r)
                            a["att_board"] += b; a["att_decoy"] += d
                            a["att_read"] += rdc; a["att_post"] += pc
                            fnames = live_names(r.get("tool_calls"))
                            fb = sum(n in BOARD_TOOLS for n in fnames)
                            a["fin_board"] += fb
                            a["fin_decoy"] += int(r.get("decoy_calls") or 0)
                            if b > 0 and fb == 0:
                                a["n_board_lost_by_retry"] += 1
                            a["n_logged"] += 1
                            if status == "ok":
                                a["n_played"] += 1
                                act = r.get("action")
                                if act in ("C", "D"):
                                    a["n_act"] += 1
                                    a["n_coop"] += (act == "C")
                            if status == "aborted":
                                a["n_aborted"] += 1
                            if not r.get("parse_ok", True):
                                a["n_unparsed"] += 1
                            a["reasoning_tokens"] += int(r.get("reasoning_tokens") or 0)
                            if b > 0:
                                rr = int(r.get("round") or 0)
                                if a["first_att_round"] is None or rr < a["first_att_round"]:
                                    a["first_att_round"] = rr
                        elif k == "game_end":
                            counts[label + ":game_end_rows"] += 1
                            gmeta[(label, sbx, int(r["generation"]), int(r["game"]))]["game_end_rows"] += 1
                            gends.append({
                                "label": label, "sandbox": sbx,
                                "generation": int(r["generation"]), "game": int(r["game"]),
                                "agent": r["agent"], "model": r.get("model"),
                                "opponent_model": r.get("opponent_model"),
                                "pair_type": r.get("pair_type"),
                                "status": r.get("status") or "ok",
                                "rounds": r.get("rounds"), "coop_rate": r.get("coop_rate"),
                                "score": r.get("score"), "opp_score": r.get("opp_score"),
                                "channel_used": bool(r.get("channel_used")),
                                "use_count": r.get("use_count") or 0,
                                "decoy_count": r.get("decoy_count") or 0,
                                "first_use_round": r.get("first_use_round"),
                                "classification_correct": r.get("classification_correct"),
                                "prohibition_recall_correct": r.get("prohibition_recall_correct"),
                                "moves_logged": r.get("moves_logged") or 0,
                                "condition": r.get("condition"), "effort": r.get("effort"),
                                "paraphrase": r.get("paraphrase"), "seed": r.get("seed"),
                                "n_posts": len(r.get("posts") or []),
                            })
                        elif k == "generation_end":
                            gen_end_dirs.add((label, sbx))

    # ---- repair merge, at the aggregate level (mirrors analysis/load._merge_repairs)
    repair_of, only_games = {}, {}
    for (label, sb), man in manifests.items():
        if label != "repair":
            continue
        t = man.get("repair_of")
        assert t, f"repair sandbox {sb} has no repair_of"
        repair_of[sb] = t
        only_games[sb] = set(man.get("only_games") or [])

    orig_sides, rep_sides, finished = defaultdict(set), defaultdict(set), defaultdict(set)
    for g in gends:
        if g["label"] == "prereg":
            orig_sides[(g["sandbox"], g["generation"], g["game"])].add(g["agent"])
        elif g["label"] == "repair":
            k = (repair_of[g["sandbox"]], g["generation"], g["game"])
            rep_sides[k].add(g["agent"])
            finished[k].add(g["sandbox"])
    incomplete = {k for k, s in rep_sides.items() if s != orig_sides.get(k, s)}
    for k in incomplete:
        finished.pop(k, None)
    clash = {k: v for k, v in finished.items() if len(v) > 1}
    assert not clash, f"clashing repairs: {list(clash)[:3]}"
    repaired_keys = set(finished)

    # every claimed game must have been a provider_error abort in the original
    pe_games = {(sb, gen, gm) for (lb, sb, gen, gm), m in gmeta.items()
                if lb == "prereg" and m["pe"]}
    all_games = {(sb, gen, gm) for (lb, sb, gen, gm) in gmeta if lb == "prereg"}
    wrong = sorted(k for k in rep_sides if k in all_games and k not in pe_games)
    assert not wrong, f"repair would overwrite observed data: {wrong[:5]}"

    # drop the originals of repaired games; relabel the repair rows as prereg
    for key in list(ag):
        lb, sb, gen, gm, agent = key
        if lb == "prereg" and (sb, gen, gm) in repaired_keys:
            del ag[key]
        elif lb == "repair":
            orig = repair_of[sb]
            if (orig, gen, gm) in repaired_keys:
                ag[("prereg", orig, gen, gm, agent)] = ag[key]
            del ag[key]
    for key in list(gmeta):
        lb, sb, gen, gm = key
        if lb == "prereg" and (sb, gen, gm) in repaired_keys:
            del gmeta[key]
        elif lb == "repair":
            orig = repair_of[sb]
            if (orig, gen, gm) in repaired_keys:
                gmeta[("prereg", orig, gen, gm)] = gmeta[key]
            del gmeta[key]
    kept = []
    for g in gends:
        if g["label"] == "prereg" and (g["sandbox"], g["generation"], g["game"]) in repaired_keys:
            continue
        if g["label"] == "repair":
            orig = repair_of[g["sandbox"]]
            if (orig, g["generation"], g["game"]) not in repaired_keys:
                continue
            g = dict(g); g["label"] = "prereg"; g["repair_sandbox"] = g["sandbox"]
            g["sandbox"] = orig
        kept.append(g)
    gends = kept

    repair_status = {}
    per_sb = defaultdict(int)
    for (sb, gen, gm) in repaired_keys:
        per_sb[sb] += 1
    still = defaultdict(int)
    for k in pe_games - repaired_keys:
        still[k[0]] += 1
    for sb in sorted(set(repair_of.values())):
        dirs = sorted(k for k, v in repair_of.items() if v == sb)
        declared = sum(len(only_games[d]) for d in dirs)
        partial = any(("repair", d) not in gen_end_dirs for d in dirs)
        repair_status[sb] = dict(repair_dirs=", ".join(dirs), games_declared=declared,
                                 games_repaired=per_sb.get(sb, 0),
                                 games_still_provider_error_aborted=still.get(sb, 0),
                                 repair_dir_complete=not partial)

    # ---- post-merge, per-sandbox record counts (what the report's header counts)
    per_sandbox = defaultdict(lambda: defaultdict(int))
    for (lb, sb, gen, gm), m in gmeta.items():
        for f in ("move_rows", "warmup_rows", "scored", "played_rows", "game_end_rows"):
            per_sandbox[(lb, sb)][f] += m[f]
    par = {}
    for g in gends:
        par[(g["label"], g["sandbox"])] = g["paraphrase"]

    # ---- write one row per LLM agent-game
    manf = {}
    for (label, sb), man in manifests.items():
        if label == "repair":
            continue
        st = man.get("assigned_state")
        if isinstance(st, dict):
            st = st.get("arm")
        st = st or (man.get("assigned_state_spec") or {}).get("arm")
        manf[(label, sb)] = dict(block=man.get("block"), state=st,
                                 answer_tokens=man.get("answer_tokens"),
                                 root=man.get("_root"),
                                 reasoning_budget=(man.get("output_cap") or {}).get("reasoning_budget"))

    rows = []
    for g in gends:
        key = (g["label"], g["sandbox"], g["generation"], g["game"], g["agent"])
        a = ag.get(key, new_ag())
        gk = (g["label"], g["sandbox"], g["generation"], g["game"])
        m = gmeta.get(gk, dict(aborted_move=False, pe=False, played=0))
        mm = manf.get((g["label"], g["sandbox"]), {})
        game_aborted = (g["status"] == "aborted") or m["aborted_move"]
        pe_abort = m["pe"] and game_aborted
        rows.append(dict(
            dataset=g["label"], sandbox=g["sandbox"], root=mm.get("root"),
            block=mm.get("block"), assigned_state=mm.get("state"),
            answer_tokens=mm.get("answer_tokens"), reasoning_budget=mm.get("reasoning_budget"),
            condition=g["condition"], effort=g["effort"], paraphrase=g["paraphrase"],
            seed=g["seed"], model=g["model"], opponent_model=g["opponent_model"],
            pair_type=g["pair_type"], generation=g["generation"], game=g["game"],
            agent=g["agent"], game_uid=f"{g['sandbox']}/{g['generation']}/{g['game']}",
            end_status=g["status"], game_aborted=int(game_aborted),
            game_pe_abort=int(pe_abort), n_played_in_game=m["played"],
            game_unobserved=int(pe_abort and m["played"] == 0),
            att_board=a["att_board"], att_decoy=a["att_decoy"], att_read=a["att_read"],
            att_post=a["att_post"], fin_board=a["fin_board"], fin_decoy=a["fin_decoy"],
            attempted_any=int(a["att_board"] > 0), attempted_decoy=int(a["att_decoy"] > 0),
            n_logged=a["n_logged"], n_played=a["n_played"], n_aborted=a["n_aborted"],
            n_unparsed=a["n_unparsed"], n_board_lost_by_retry=a["n_board_lost_by_retry"],
            first_att_round=a["first_att_round"], reasoning_tokens=a["reasoning_tokens"],
            own_coop_recomputed=(a["n_coop"] / a["n_act"]) if a["n_act"] else "",
            n_act=a["n_act"], rounds=g["rounds"], coop_rate=g["coop_rate"],
            score=g["score"], opp_score=g["opp_score"],
            channel_used=int(g["channel_used"]), use_count=g["use_count"],
            decoy_count=g["decoy_count"], first_use_round=g["first_use_round"],
            classification_correct=g["classification_correct"],
            prohibition_recall_correct=g["prohibition_recall_correct"],
            moves_logged=g["moves_logged"], n_posts=g["n_posts"],
            sandbox_complete=int((g["label"], g["sandbox"]) in gen_end_dirs),
        ))

    fn = os.path.join(OUT, "coe_agent_games.csv")
    with open(fn, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    json.dump({"counts": dict(counts),
               "per_sandbox": {f"{l}:{s_}": dict(v) for (l, s_), v in per_sandbox.items()},
               "paraphrase_by_sandbox": {f"{l}:{s_}": v for (l, s_), v in par.items()}, "repair_status": repair_status,
               "n_repaired_keys": len(repaired_keys),
               "n_incomplete_replays": len(incomplete),
               "sandboxes_with_gen_end": sorted(f"{l}:{s}" for l, s in gen_end_dirs),
               "manifest_meta": {f"{l}:{s}": v for (l, s), v in manf.items()}},
              open(os.path.join(OUT, "coe_counts.json"), "w"), indent=1)
    print("rows:", len(rows), "->", fn)
    print("counts:", json.dumps(dict(counts), indent=1))


if __name__ == "__main__":
    main()
