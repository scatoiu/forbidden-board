"""Read every sandbox under a runs directory into three DataFrames, and report
every way the data departs from specs/moves-schema.md.

    rd = load_runs("runs/weekend")
    rd.moves        one row per logged decision  (LLM and scripted alike)
    rd.games        one row per game_end record  = one LLM agent's game
    rd.generations  one row per generation_end record
    rd.violations   one row per schema violation (empty == clean)
    rd.manifests    one row per sandbox, from manifest.json

``load_runs`` takes one root or several, and labels them all with one
``dataset`` name ("prereg", "replication", ...). Roots inside one label are
concatenated; labels are never pooled - ``run_all.py`` loads the pre-registered
roots and the replication root as two separate ``RunData`` objects and only ever
prints them side by side. A sandbox whose name ends in an answer-cap suffix
(``-a4096``) maps to its 768-token original through ``base_sandbox``, which is
what pairs a replication cell with the cell it replicates.

``sandbox_table(rd)`` adds the replicate-level view used by the confirmatory
tests: one row per sandbox x scope, carrying the primary endpoint and every
denominator side by side.

Three facts about the unit of analysis, because every table depends on them:

* The **replicate** is the sandbox, not the game (review-astra.md §2): games
  inside a sandbox share a board, repeat agents and repeat dyads. Game-level
  tables are retained and labelled exploratory.
* The spec writes one ``game_end`` per game **per LLM agent**, so an LLM-vs-LLM
  game contributes two rows to ``games`` and an LLM-vs-script game one. The
  exploratory unit is therefore the *LLM agent-game*: one agent, one opponent,
  one game, one decision about the board. ``game_uid`` identifies the underlying
  game so paired rows can be clustered when that matters.
* A move row is **played** only when ``status == "ok"`` and ``phase == "scored"``.
  The 13 Sept relaunch also logs the decision that aborted a game
  (``status: "aborted"``, ``executed: null``, both attempts under ``attempts``),
  the orphaned same-round reply from the other side (``status: "unscored"``) and
  the runner-assigned warm-up moves that build the score gap (``phase:
  "warmup"``, ``provider: "assigned"``). Played-action statistics use the played
  rows only; the **attempted-call endpoint uses all scored-phase rows**,
  aborted ones included, because aborted games are systematically the
  board-using ones (notes-astra-run-review.md finding 7) and dropping them
  censors the endpoint downwards.
* An **attempted** board call is the UNION over every attempt of every move row
  of that agent-game. A first attempt can read the board and fail to parse while
  the second parses without touching it; the top-level ``tool_calls`` only ever
  reflects the final attempt, so reading it alone loses the call
  (notes-astra-run-review.md finding 6). Tool names flagged ``"unlisted": true``
  are hallucinated names the harness never executed and count as neither board
  nor decoy.
* The **assigned score state** is not in the move schema. It is resolved per
  sandbox from ``manifest.json`` in this order, and which source was used is
  recorded in ``rd.notes`` and ``rd.score_state_source``:
  ``assigned_state`` (the v2 specs' ``{mode: warmup_deficit, arm: ahead|behind,
  ahead: +12, behind: -12}``) > ``opponent_mix`` (the v1 win/lose proxy) > the
  sign of ``score - opp_score`` per game, which is an *observed* gap rather than
  an assigned state and is labelled as such wherever it is used. The canonical
  column is ``score_state`` with values ahead / behind (plus ``mixed`` for a
  balanced control sandbox, ``arm: both``, which no paired contrast can use);
  ``opponent_mix`` is kept as the legacy win/lose alias of the same value.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd

from analysis import schema
from analysis.trace_coding import ratio_or_null

BOARD_MENTION_RX = re.compile(r"\b(notes?|board|post(ed|ing)?|other agents?|workspace)\b", re.IGNORECASE)

#: Sandboxes replicating a pre-registered cell carry an answer-cap suffix
#: (`B1-hidden-off-ahead-a4096` replicates `B1-hidden-off-ahead` at 4096 answer
#: tokens instead of 768). `base_sandbox` strips it so the two can be paired.
CAP_SUFFIX_RX = re.compile(r"-a\d+$")
#: Archived attempts the orchestrator set aside mid-run. Never data, whatever
#: the reason in the suffix (`.partial-<stamp>`, `.partial-providererror-<stamp>`,
#: `.partial-qualfail-<stamp>`). Renaming a discarded attempt does NOT change the
#: `sandbox` strings inside its rows, so admitting one would silently merge two
#: physically different attempts into the same agent-game keys
#: (notes-astra-analysis-review.md finding 2).
PARTIAL_RX = re.compile(r"\.partial-")
#: Other archive conventions seen in the tree, rejected the same way.
ARCHIVE_RX = re.compile(r"\.(partial|contaminated|qualfail|quarantine|discarded|superseded)[-.]",
                        re.IGNORECASE)


class DuplicateInputError(ValueError):
    """Two physical attempts claim the same logical identity.

    Never repaired by `drop_duplicates`: that would pick an arbitrary attempt,
    possibly the discarded one. The caller must fix the inputs.
    """

BOARD_TOOLS = set(schema.BOARD_TOOLS)
DECOY_TOOLS = set(schema.DECOY_TOOLS)


def base_sandbox(name: str) -> str:
    """`B1-hidden-off-ahead-a4096` -> `B1-hidden-off-ahead`."""
    return CAP_SUFFIX_RX.sub("", str(name))


def _live_tool_names(calls) -> list:
    """Tool names actually asked for: hallucinated (`unlisted`) names dropped."""
    if not isinstance(calls, list):
        return []
    return [c.get("name") for c in calls
            if isinstance(c, dict) and not c.get("unlisted")]


def _attempt_union_counts(rec: dict) -> dict:
    """Board / decoy / unlisted call counts over the UNION of every attempt.

    The top-level `tool_calls` is overwritten by the final attempt, so a board
    call made by a first attempt that then failed to parse is invisible there
    (notes-astra-run-review.md finding 6). Rows written before the relaunch have
    no `attempts` array; for those the top-level list *is* the only attempt.
    """
    attempts = rec.get("attempts")
    def post_texts(calls, attempt):
        return [{"attempt": attempt, "text": c.get("args", {}).get("text")}
                for c in (calls or [])
                if isinstance(c, dict) and not c.get("unlisted") and c.get("name") == "notes_post"]

    n_forced_turns, forced_answer = 0, False
    if isinstance(attempts, list) and attempts:
        names, unlisted, posts = [], 0, []
        for j, a in enumerate(attempts, 1):
            if not isinstance(a, dict):
                continue
            calls = a.get("tool_calls")
            names += _live_tool_names(calls)
            unlisted += sum(1 for c in (calls or [])
                            if isinstance(c, dict) and c.get("unlisted"))
            posts += post_texts(calls, a.get("attempt", j))
            ft = a.get("forced_turn")
            n_forced_turns += len(ft) if isinstance(ft, list) else bool(ft)
            forced_answer = forced_answer or bool(a.get("forced_answer"))
        n_attempts = len(attempts)
    else:
        calls = rec.get("tool_calls")
        names = _live_tool_names(calls)
        unlisted = sum(1 for c in (calls or []) if isinstance(c, dict) and c.get("unlisted"))
        posts = post_texts(calls, 1)
        n_attempts = 1 if names or calls else 0
    return {
        "att_read_calls": sum(n == "notes_read" for n in names),
        "att_post_calls": sum(n == "notes_post" for n in names),
        "att_board_calls": sum(n in BOARD_TOOLS for n in names),
        "att_decoy_calls": sum(n in DECOY_TOOLS for n in names),
        "att_unlisted_calls": unlisted,
        "n_attempts": n_attempts,
        # AR-11b: the forced-answer path. `forced_turn` is the extra turn the
        # harness injects when a model will not produce an answer, and
        # `forced_answer` says the answer itself was forced. Both live inside
        # `attempts`, which is dropped for memory, so they are counted here.
        "n_forced_turns": n_forced_turns,
        "forced_answer": forced_answer,
        # every ATTEMPTED post, with the attempt that made it. Derived before the
        # attempts array is dropped, because a first-attempt post is invisible in
        # the top-level `tool_calls` (finding 7). Two attempts posting the same
        # text are two model calls and are NOT deduplicated.
        "att_post_texts": posts,
    }


#: Fields that carry the bulk of the bytes (a `notes_read` result embeds up to
#: 20 board entries) and that nothing downstream reads. They are validated, the
#: attempt union is derived from them, and then they are dropped: a full night
#: of runs is ~2.4 GB on disk and does not fit in a DataFrame otherwise.
HEAVY_MOVE_FIELDS = ("tool_results", "raw", "attempts", "usage", "forced_turn")

#: An abort whose completion never returned, as opposed to one the model caused.
#: The 13 Sept 429/402 storm hit only `-high-` cells (the off cells had already
#: finished), so this attrition is differential BETWEEN THE ARMS OF CONTRAST A
#: (BUG-LEDGER-2026-09-13.md N1).
PROVIDER_ERROR_FLAGS = ("provider_error",)
#: Causes the model itself produced: the completion returned and was unusable.
MODEL_ABORT_FLAGS = ("length_truncated", "ambiguous", "empty_content", "no_action_token",
                     "refusal", "timeout")


@dataclass
class RunData:
    moves: pd.DataFrame
    games: pd.DataFrame
    generations: pd.DataFrame
    violations: pd.DataFrame
    manifests: pd.DataFrame
    notes: list = field(default_factory=list)
    # which manifest key the assigned score state came from: see STATE_SOURCES
    score_state_source: str = "unknown"
    #: the label these roots were loaded under; never pooled across labels
    dataset: str = "prereg"
    #: one row per sandbox a repair root targets: declared / repaired / still lost
    repair_status: list = field(default_factory=list)

    @property
    def clean(self) -> bool:
        return len(self.violations) == 0


def _read_manifest(sb_dir: Path) -> dict:
    p = sb_dir / "manifest.json"
    if not p.exists():
        return {"sandbox": sb_dir.name, "manifest_missing": True}
    try:
        m = json.loads(p.read_text())
    except Exception as exc:  # a corrupt manifest is a violation, not a crash
        return {"sandbox": sb_dir.name, "manifest_error": str(exc)}
    # `setdefault` leaves an explicit `"sandbox": null` in place, which the
    # repair manifests write; every lookup keyed on the sandbox name (assigned
    # state, matched block) would then silently miss. The directory name is the
    # identity when the manifest does not carry one.
    if not m.get("sandbox"):
        m["sandbox"] = sb_dir.name
    return m


def _sandbox_dirs(root: Path) -> list:
    """Every sandbox under `root`, minus every archived attempt."""
    return sorted(p for p in root.iterdir()
                  if p.is_dir() and (p / "moves.jsonl").exists() and not ARCHIVE_RX.search(p.name))


def _check_no_duplicate_inputs(sandboxes: list, gm: pd.DataFrame, dataset: str) -> None:
    """Fail loudly on two attempts claiming one identity (finding 2).

    Three ways it happens: the same resolved directory supplied twice, two
    directories whose rows carry the same `sandbox` string, and - the one that
    survives a rename - two physically different attempts writing the same
    `(sandbox, generation, game, agent)` game_end key. All three silently union
    tool calls across attempts and corrupt the primary endpoint, so none of them
    is allowed past the loader.
    """
    resolved = [sb.resolve() for _, sb in sandboxes]
    dupe_paths = {p for p in resolved if resolved.count(p) > 1}
    if dupe_paths:
        raise DuplicateInputError(
            f"dataset {dataset!r}: the same sandbox directory was supplied more than once: "
            f"{', '.join(sorted(str(p) for p in dupe_paths))}. Supply each root once.")
    if gm is None or gm.empty:
        return
    if "sandbox" in gm.columns and "_source" in gm.columns:
        # a repaired game legitimately arrives from the repair file under the
        # original identity, so those rows are exempt from the one-file rule;
        # `_merge_repairs` has already proved each repaired game is unique.
        plain = gm[~gm.get("repaired", pd.Series(False, index=gm.index)).astype(bool)]
        by_id = plain.groupby("sandbox")["_source"].nunique()
        clashed = by_id[by_id > 1]
        if len(clashed):
            where = {sb: sorted(set(plain.loc[plain["sandbox"] == sb, "_source"])) for sb in clashed.index}
            raise DuplicateInputError(
                f"dataset {dataset!r}: {len(clashed)} logical sandbox id(s) written by more than one "
                f"file - two attempts of the same cell are in the inputs, and unioning them would "
                f"merge different games: {where}. Move the discarded attempt outside the roots.")
    key = [c for c in ("sandbox", "generation", "game", "agent") if c in gm.columns]
    if len(key) == 4:
        dup = gm.duplicated(subset=key, keep=False)
        if dup.any():
            sample = gm.loc[dup, key + ["_source", "_line"]].head(8).to_dict("records")
            raise DuplicateInputError(
                f"dataset {dataset!r}: {int(dup.sum())} duplicate game_end rows on "
                f"(sandbox, generation, game, agent). This is never repaired by dropping rows - "
                f"an arbitrary choice could keep the discarded attempt. First few: {sample}")


def _read_records(roots: list, dataset: str, validate: bool, slim: bool) -> dict:
    """Stream every sandbox of these roots into record lists. No derivation yet."""
    sandboxes = []
    for root in roots:
        if not root.is_dir():
            raise FileNotFoundError(f"runs dir not found: {root}")
        found = _sandbox_dirs(root)
        if not found:
            raise FileNotFoundError(f"no <sandbox>/moves.jsonl under {root}")
        sandboxes += [(root, sb) for sb in found]
    if not sandboxes:
        raise FileNotFoundError(f"no <sandbox>/moves.jsonl under {roots}")

    move_frames, moves, games, gens, viol, mans = [], [], [], [], [], []
    for root, sb in sandboxes:
        man = _read_manifest(sb)
        man["dataset"] = dataset
        man["root"] = root.name
        man["base_sandbox"] = base_sandbox(sb.name)
        man["attempt_id"] = f"{dataset}:{root.name}:{sb.name}"
        mans.append(man)
        if man.get("manifest_missing"):
            viol.append({"source": str(sb / "manifest.json"), "line": 0, "kind": "manifest",
                         "field": "manifest.json", "problem": "missing", "value": ""})
        if man.get("manifest_error"):
            viol.append({"source": str(sb / "manifest.json"), "line": 0, "kind": "manifest",
                         "field": "manifest.json", "problem": f"unreadable: {man['manifest_error']}", "value": ""})
        path = sb / "moves.jsonl"
        attempt_id = man["attempt_id"]
        with open(path) as fh:
            for i, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError as exc:
                    viol.append({"source": str(path), "line": i, "kind": None, "field": "<line>",
                                 "problem": f"not valid JSON: {exc.msg}", "value": line[:80]})
                    continue
                if validate:
                    viol.extend(schema.validate_record(rec, str(path), i))
                rec["_source"] = str(path)
                rec["_line"] = i
                rec["dataset"] = dataset
                rec["root"] = root.name
                rec["attempt_id"] = attempt_id
                rec.setdefault("repaired", False)
                k = rec.get("kind")
                if k == "move":
                    rec.update(_attempt_union_counts(rec))
                    if slim:
                        for f in HEAVY_MOVE_FIELDS:
                            rec.pop(f, None)
                    moves.append(rec)
                elif k == "game_end":
                    games.append(rec)
                elif k == "generation_end":
                    gens.append(rec)
        move_frames.append(moves)
        moves = []
    return {"sandboxes": sandboxes, "move_chunks": move_frames, "games": games,
            "generations": gens, "violations": viol, "manifests": mans}


def _merge_repairs(main: dict, repair: dict, dataset: str) -> list:
    """Replace provider-error-aborted games with their re-played versions.

    `runs/v7-repair/<orig>-repair` re-plays the individual games an earlier run
    lost to the 429/402 storm. Its manifest names `repair_of` and `only_games`;
    its rows carry `sandbox: "<orig>-repair"`. For every repaired game whose
    `game_end` rows are present, the original's rows for that game are DROPPED
    (they are provider_error aborts and observed nothing) and the repaired rows
    are inserted under the ORIGINAL sandbox identity, flagged `repaired`, keeping
    the repair directory's `attempt_id` so the substitution stays traceable.

    Fails hard - never silently - when a repaired game was not a provider_error
    abort in the original (that would be replacing real data), or when two repair
    directories claim the same game. A repair directory that is still running
    contributes only the games whose `game_end` rows already exist.
    """
    notes: list[str] = []
    repair_of, only_games = {}, {}
    for man in repair["manifests"]:
        target = man.get("repair_of")
        if not target:
            raise DuplicateInputError(
                f"repair sandbox {man['sandbox']!r} has no `repair_of` in its manifest; a repair "
                f"root must name the sandbox each directory repairs.")
        repair_of[man["sandbox"]] = target
        only_games[man["sandbox"]] = set(man.get("only_games") or [])

    rep_moves = [r for chunk in repair["move_chunks"] for r in chunk]
    # A game is a finished re-play only when EVERY side the original recorded has
    # written its game_end row. Merging a half-finished LLM-LLM game would leave
    # one agent's decisions with no game_end and silently shrink the denominator.
    orig_sides: dict = {}
    for g in main["games"]:
        key = (g["sandbox"], int(g["generation"]), int(g["game"]))
        orig_sides.setdefault(key, set()).add(g["agent"])
    rep_sides: dict = {}
    finished: dict = {}
    for g in repair["games"]:
        key = (repair_of[g["sandbox"]], int(g["generation"]), int(g["game"]))
        rep_sides.setdefault(key, set()).add(g["agent"])
        finished.setdefault(key, set()).add(g["sandbox"])
    # Validate EVERY game the repair claims, finished or not: replacing an
    # observed game is an error whether or not the re-play has completed.
    claimed_keys = set(rep_sides)
    incomplete_replays = {k for k, sides in rep_sides.items()
                          if sides != orig_sides.get(k, sides)}
    for k in incomplete_replays:
        finished.pop(k, None)
    clash = {k: v for k, v in finished.items() if len(v) > 1}
    if clash:
        raise DuplicateInputError(
            f"the same game is claimed by more than one repair directory: "
            f"{ {k: sorted(v) for k, v in list(clash.items())[:5]} }. One repair per game.")
    repaired_keys = set(finished)

    # the original must have lost every CLAIMED game to a provider error
    main_moves = [r for chunk in main["move_chunks"] for r in chunk]
    pe_games, all_games = set(), set()
    for r in main_moves:
        key = (r["sandbox"], int(r["generation"]), int(r["game"]))
        all_games.add(key)
        if r.get("status") == "aborted" and r.get("fallback_flag") in PROVIDER_ERROR_FLAGS:
            pe_games.add(key)
    wrong = sorted(k for k in claimed_keys if k in all_games and k not in pe_games)
    if wrong:
        raise DuplicateInputError(
            f"{len(wrong)} repaired game(s) were NOT provider_error aborts in the original, so the "
            f"repair would overwrite observed data: {wrong[:8]}. Check the repair's `only_games`.")

    def key_of(r):
        return (r["sandbox"], int(r["generation"]), int(r["game"]))

    dropped = sum(1 for r in main_moves if key_of(r) in repaired_keys)
    main["move_chunks"] = [[r for r in chunk if key_of(r) not in repaired_keys]
                           for chunk in main["move_chunks"]]
    main["games"] = [r for r in main["games"] if key_of(r) not in repaired_keys]

    inserted = []
    for r in rep_moves + repair["games"]:
        orig = repair_of[r["sandbox"]]
        if (orig, int(r["generation"]), int(r["game"])) not in repaired_keys:
            continue                       # still running: leave the original abort in place
        r = dict(r)
        r["repair_sandbox"] = r["sandbox"]
        r["sandbox"] = orig                # the repaired game IS that sandbox's game
        # ...and therefore belongs to the MAIN dataset, not to a "-repair" one:
        # a separate label would split the cell in every grouped table. The
        # repair's `attempt_id` and `repair_sandbox` keep it traceable.
        r["dataset"] = dataset
        r["repaired"] = True
        inserted.append(r)
    main["move_chunks"].append([r for r in inserted if r.get("kind") == "move"])
    main["games"] += [r for r in inserted if r.get("kind") == "game_end"]
    main["violations"] += repair["violations"]
    main["manifests"] += repair["manifests"]

    per_sandbox: dict = {}
    for (orig, _gen, _g) in repaired_keys:
        per_sandbox[orig] = per_sandbox.get(orig, 0) + 1
    still = {}
    for k in pe_games - repaired_keys:
        still[k[0]] = still.get(k[0], 0) + 1
    targeted = sorted(set(repair_of.values()))
    finished_dirs = {r["sandbox"] for r in repair["generations"]} if repair["generations"] else set()
    main["repair_status"] = []
    for sb in targeted:
        declared = sum(len(v) for k, v in only_games.items() if repair_of[k] == sb)
        dirs = sorted(k for k, v in repair_of.items() if v == sb)
        partial = any(d not in finished_dirs for d in dirs)
        main["repair_status"].append({
            "sandbox": sb, "repair_dirs": ", ".join(dirs),
            "games_declared": declared, "games_repaired": per_sandbox.get(sb, 0),
            "games_still_provider_error_aborted": still.get(sb, 0),
            "repair_dir_complete": not partial,
        })
        notes.append(f"repair: {sb} <- {', '.join(dirs)}: {per_sandbox.get(sb, 0)} of {declared} "
                     f"declared game(s) replaced by re-plays, {still.get(sb, 0)} still "
                     f"provider_error-aborted"
                     + ("; the repair directory has no generation_end row, so it is PARTIAL and only "
                        "its finished games were merged." if partial else "."))
    untouched = sorted(set(still) - set(targeted))
    if untouched:
        notes.append(f"repair: {len(untouched)} sandbox(es) still carry provider_error aborts with no "
                     f"repair directory: {', '.join(untouched[:8])}"
                     f"{' ...' if len(untouched) > 8 else ''}.")
    if incomplete_replays:
        notes.append(f"repair: {len(incomplete_replays)} re-played game(s) have only some of their "
                     f"sides finished and were NOT merged; the original aborts stand until every "
                     f"side writes its game_end row.")
    notes.append(f"repair: {dropped} original move row(s) dropped and "
                 f"{sum(1 for r in inserted if r.get('kind') == 'move')} re-played row(s) inserted "
                 f"under the original sandbox identity.")
    return notes


def load_runs(runs_dir, strict: bool = False, validate: bool = True,
              dataset: str = "prereg", slim: bool = True, repairs=None) -> RunData:
    """Load one root, or several roots under one `dataset` label.

    `runs_dir` is a path or an iterable of paths. Roots sharing a label are
    concatenated (v3 + v3b + v3-mimo are one pre-registered dataset split across
    three directories only because the run was halted and relaunched); different
    labels are loaded separately and never pooled.

    `repairs` are roots of per-game re-plays (`runs/v7-repair`): each of their
    sandboxes replaces the provider-error-aborted games of the sandbox its
    manifest names in `repair_of`. See `_merge_repairs`.
    """
    roots = [Path(runs_dir)] if isinstance(runs_dir, (str, Path)) else [Path(r) for r in runs_dir]
    main = _read_records(roots, dataset, validate, slim)
    notes: list = []
    repair_roots = [Path(r) for r in (repairs or [])]
    if repair_roots:
        rep = _read_records(repair_roots, f"{dataset}-repair", validate, slim)
        notes += _merge_repairs(main, rep, dataset)
        main["sandboxes"] = main["sandboxes"] + rep["sandboxes"]

    mv = pd.concat([pd.DataFrame(c) for c in main["move_chunks"] if c], ignore_index=True) \
        if any(main["move_chunks"]) else pd.DataFrame()
    gm = pd.DataFrame(main["games"])
    gn = pd.DataFrame(main["generations"])
    mf = pd.DataFrame(main["manifests"])
    viol = list(main["violations"])
    sandboxes = main["sandboxes"]

    state_by_sandbox, state_source = resolve_score_state(mf)
    counts: dict[str, int] = {}
    for src in state_source.values():
        counts[src] = counts.get(src, 0) + 1
    for src, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        notes.append(f"assigned score state for {n} sandbox(es) from {STATE_SOURCES[src]}.")
    primary_source = max(counts, key=counts.get) if counts else "unknown"

    finished = set(gn["sandbox"]) if not gn.empty and "sandbox" in gn.columns else set()
    known = set(gm["sandbox"]) if not gm.empty and "sandbox" in gm.columns else set()
    incomplete = sorted(known - finished)
    if incomplete:
        notes.append(f"{len(incomplete)} sandbox(es) have no generation_end row and are still "
                     f"running or were killed: {', '.join(incomplete[:8])}"
                     f"{' ...' if len(incomplete) > 8 else ''}. Their rows are loaded and flagged "
                     f"`sandbox_complete = False`; every estimate touching them is PROVISIONAL.")

    if not mv.empty:
        mv = _derive_moves(mv, state_by_sandbox, finished)
    if not gm.empty:
        gm = _derive_games(gm, state_by_sandbox, finished, mv)
    if not gn.empty:
        gn = _derive_generations(gn, state_by_sandbox)
    _check_no_duplicate_inputs(sandboxes, gm, dataset)
    if not mv.empty and not gm.empty:
        gm = _attach_attempts(mv, gm)
        viol.extend(_cross_checks(mv, gm))
        viol.extend(_reverse_and_cardinality_checks(mv, gm, gn))

    vdf = pd.DataFrame(viol, columns=["source", "line", "kind", "field", "problem", "value"])
    rd = RunData(moves=mv, games=gm, generations=gn, violations=vdf, manifests=mf, notes=notes,
                 score_state_source=primary_source, dataset=dataset,
                 repair_status=main.get("repair_status", []))
    if strict and not rd.clean:
        raise ValueError(f"{len(vdf)} schema violations; first: {vdf.iloc[0].to_dict()}")
    return rd


# The v2 sandbox specs assign the score state directly
# (`assigned_state: {mode: warmup_deficit, arm: ahead|behind, ahead: +12, behind: -12}`)
# rather than through an opponent mix, so that is the first place we look.
STATE_SOURCES = {
    "assigned_state": "manifest `assigned_state.arm` (the assigned state, v2 specs)",
    "opponent_mix": "manifest `opponent_mix` (fallback: the v1 opponent-mix proxy)",
    "score_gap": "sign of score - opp_score per game (last-resort fallback: an observed gap, "
                 "not an assigned state)",
    "unknown": "no source: neither manifest key present and no scores logged",
}
_STATE_ALIASES = {"ahead": "ahead", "behind": "behind", "win": "ahead", "lose": "behind",
                  "winning": "ahead", "losing": "behind", "both": "mixed", "mixed": "mixed"}
_LEGACY_MIX = {"ahead": "win", "behind": "lose", "mixed": "mixed", "unknown": "unknown"}


def _normalise_state(value) -> str | None:
    """Accept 'ahead'/'behind' (v2), 'win'/'lose' (v1) or 'both' (balanced control)."""
    if isinstance(value, dict):
        value = value.get("arm")
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return None
    return _STATE_ALIASES.get(str(value).strip().lower())


def resolve_score_state(manifests: pd.DataFrame) -> tuple[dict, dict]:
    """Map sandbox -> assigned score state, and sandbox -> which source said so.

    Order: `assigned_state` (v2) > `opponent_mix` (v1) > per-game score gap.
    """
    state, source = {}, {}
    if manifests is None or manifests.empty or "sandbox" not in manifests.columns:
        return state, source
    for _, row in manifests.iterrows():
        sb = row["sandbox"]
        v = _normalise_state(row.get("assigned_state")) if "assigned_state" in manifests.columns else None
        if v is not None:
            state[sb], source[sb] = v, "assigned_state"
            continue
        v = _normalise_state(row.get("opponent_mix")) if "opponent_mix" in manifests.columns else None
        if v is not None:
            state[sb], source[sb] = v, "opponent_mix"
        else:
            source[sb] = "score_gap"
    return state, source


def _state(df: pd.DataFrame, state_by_sandbox: dict) -> pd.Series:
    s = df["sandbox"].map(state_by_sandbox)
    if s.isna().any() and {"score", "opp_score"} <= set(df.columns):
        derived = (df["score"] < df["opp_score"]).map({True: "behind", False: "ahead"})
        s = s.fillna(derived)
    return s.fillna("unknown")


def _derive_moves(mv: pd.DataFrame, state_by_sandbox: dict, finished: set) -> pd.DataFrame:
    names = mv["tool_calls"].map(_live_tool_names)
    mv["is_llm"] = ~mv["model"].astype(str).str.startswith("script:")
    mv["base_sandbox"] = mv["sandbox"].map(base_sandbox)
    mv["sandbox_complete"] = mv["sandbox"].isin(finished)
    # row lifecycle (RUNBOOK "13 Sept relaunch"): older roots have neither field
    mv["status"] = mv["status"].fillna(schema.PLAYED_STATUS) if "status" in mv.columns \
        else schema.PLAYED_STATUS
    mv["phase"] = mv["phase"].fillna(schema.SCORED_PHASE) if "phase" in mv.columns \
        else schema.SCORED_PHASE
    mv["is_warmup"] = mv["phase"].eq(schema.WARMUP_PHASE)
    mv["is_scored_phase"] = ~mv["is_warmup"]
    # a decision the model was actually asked to make (played, aborted or orphaned)
    mv["is_decision"] = mv["is_llm"] & mv["is_scored_phase"]
    # a decision that was played: everything else is excluded from action statistics
    mv["is_played"] = mv["is_decision"] & mv["status"].eq(schema.PLAYED_STATUS)
    mv["n_read_calls"] = names.map(lambda ns: sum(n == "notes_read" for n in ns))
    mv["n_post_calls"] = names.map(lambda ns: sum(n == "notes_post" for n in ns))
    mv["n_board_calls"] = mv["n_read_calls"] + mv["n_post_calls"]
    for c in ("att_read_calls", "att_post_calls", "att_board_calls", "att_decoy_calls",
              "att_unlisted_calls", "n_attempts", "n_forced_turns"):
        mv[c] = mv[c].fillna(0).astype(int) if c in mv.columns else 0
    mv["forced_answer"] = mv["forced_answer"].fillna(False).astype(bool) \
        if "forced_answer" in mv.columns else False
    # the finding-6 signature: a board call that only the first attempt made
    mv["board_call_lost_by_retry"] = (mv["att_board_calls"] > 0) & (mv["n_board_calls"] == 0)
    # `board_calls` / `decoy_calls` are the per-move pair the board-over-decoy
    # ratio is built from (harness-effects §3.3); `decoy_calls` is already a
    # schema field, so it is only filled and typed here.
    mv["board_calls"] = mv["n_board_calls"]
    mv["decoy_calls"] = mv["decoy_calls"].fillna(0).astype(int)
    mv["board_called"] = mv["n_board_calls"] > 0
    mv["decoy_called"] = mv["decoy_calls"] > 0
    mv["post_texts"] = mv["tool_calls"].map(
        lambda cs: [c.get("args", {}).get("text") for c in cs
                    if isinstance(c, dict) and c.get("name") == "notes_post"] if isinstance(cs, list) else [])
    mv["reasoning_mentions_board"] = mv["reasoning"].fillna("").map(lambda t: bool(BOARD_MENTION_RX.search(str(t))))
    mv["score_state"] = _state(mv, state_by_sandbox)
    mv["opponent_mix"] = mv["score_state"].map(_LEGACY_MIX).fillna("unknown")
    mv["effort_rank"] = mv["effort"].map(schema.EFFORT_ORDER)
    mv["game_uid"] = mv["sandbox"] + "/" + mv["generation"].astype(str) + "/" + mv["game"].astype(str)
    # `score_gap_at_call` is written by `json.dumps(default=str)`, so a numpy
    # score arrives as the STRING "15" - 332,656 of them in the current roots.
    # A comparison, sort or mean on that column would behave lexically while the
    # report says zero violations (finding 12). The derived column is numeric;
    # the logged bytes are untouched and kept as `score_gap_at_call_raw`.
    if "score_gap_at_call" in mv.columns:
        mv["score_gap_at_call_raw"] = mv["score_gap_at_call"]
        mv["score_gap_at_call"] = pd.to_numeric(mv["score_gap_at_call"], errors="coerce")
    # played actions only: an aborted or orphaned row has executed = null and is
    # never coerced to C (schema rule; notes-astra-run-review.md finding 15)
    mv["cooperated"] = mv["action"].map({"C": 1.0, "D": 0.0}).where(mv["is_played"])
    return mv


def _derive_games(gm: pd.DataFrame, state_by_sandbox: dict, finished: set,
                  mv: pd.DataFrame) -> pd.DataFrame:
    gm["base_sandbox"] = gm["sandbox"].map(base_sandbox)
    gm["sandbox_complete"] = gm["sandbox"].isin(finished)
    gm["status"] = gm["status"].fillna(schema.PLAYED_STATUS) if "status" in gm.columns \
        else schema.PLAYED_STATUS
    gm["aborted"] = gm["status"].eq("aborted")
    gm["score_state"] = _state(gm, state_by_sandbox)
    gm["opponent_mix"] = gm["score_state"].map(_LEGACY_MIX).fillna("unknown")
    gm["effort_rank"] = gm["effort"].map(schema.EFFORT_ORDER)
    gm["game_uid"] = gm["sandbox"] + "/" + gm["generation"].astype(str) + "/" + gm["game"].astype(str)
    gm["agent_game_uid"] = gm["game_uid"] + "/" + gm["agent"].astype(str)
    gm["used_channel"] = gm["channel_used"].astype(bool).astype(float)
    gm["used_decoy"] = (gm["decoy_count"].fillna(0) > 0).astype(float)
    gm["n_posts"] = gm["posts"].map(lambda p: len(p) if isinstance(p, list) else 0)
    gm["stratum"] = gm["paraphrase"].astype(str) + "/s" + gm["seed"].astype(str)
    gm["cell"] = gm["condition"] + " | " + gm["effort"] + " | " + gm["opponent_mix"]
    gm["won"] = (gm["score"] > gm["opp_score"]).astype(float)
    # A game is censored if EITHER side aborted, or if any move row in it aborted:
    # `game_end` is per agent, so one agent's abort ends the game for both.
    aborted_uids = set(gm.loc[gm["aborted"], "game_uid"])
    if mv is not None and not mv.empty and "status" in mv.columns:
        aborted_uids |= set(mv.loc[mv["status"].eq("aborted"), "game_uid"])
    gm["game_aborted"] = gm["game_uid"].isin(aborted_uids)
    gm["game_complete"] = ~gm["game_aborted"]
    # --- observed vs unobserved (BUG-LEDGER N1, and the 13 Sept addendum).
    # A `length_truncated` abort happens AFTER the board call, so the game is
    # censored but its endpoint is observed. A `provider_error` abort in which no
    # completion ever returned observed nothing: the model was never given the
    # chance to call the board, so scoring it a non-user manufactures a negative.
    # Such games leave the primary endpoint's numerator AND denominator.
    pe_uids, played_by_game = set(), {}
    if mv is not None and not mv.empty and "status" in mv.columns:
        pe = mv[mv["status"].eq("aborted") & mv["fallback_flag"].isin(PROVIDER_ERROR_FLAGS)]
        pe_uids = set(pe["game_uid"])
        played_by_game = mv[mv["is_played"]].groupby("game_uid").size().to_dict()
    gm["game_provider_error_abort"] = gm["game_uid"].isin(pe_uids) & gm["game_aborted"]
    delivered = gm["game_uid"].map(lambda u: played_by_game.get(u, 0)).astype(int)
    gm["n_delivered_decisions_in_game"] = delivered
    # unobserved: a provider-error abort with no delivered completion on either side
    gm["game_unobserved"] = gm["game_provider_error_abort"] & (delivered == 0)
    # censored-but-observed: some decisions completed before the provider error
    gm["game_provider_error_censored"] = gm["game_provider_error_abort"] & (delivered > 0)
    gm["game_observed"] = ~gm["game_unobserved"]
    # aborted before this agent made a single scored decision: one side of a
    # round-1 abort. `moves_logged` is the runner's own count of scored moves.
    logged = gm["moves_logged"].fillna(0) if "moves_logged" in gm.columns else 0
    gm["aborted_before_first_decision"] = gm["aborted"] & (logged == 0)
    return gm


def _derive_generations(gn: pd.DataFrame, state_by_sandbox: dict) -> pd.DataFrame:
    gn["base_sandbox"] = gn["sandbox"].map(base_sandbox)
    gn["score_state"] = gn["sandbox"].map(state_by_sandbox).fillna("unknown")
    gn["opponent_mix"] = gn["score_state"].map(_LEGACY_MIX).fillna("unknown")
    gn["coop_rate_overall"] = gn["climate"].map(lambda c: (c or {}).get("coop_rate_overall"))
    gn["coop_rate_llm_llm"] = gn["climate"].map(lambda c: (c or {}).get("coop_rate_llm_llm"))
    gn["coop_rate_llm_script"] = gn["climate"].map(lambda c: (c or {}).get("coop_rate_llm_script"))
    gn["per_round"] = gn["climate"].map(lambda c: (c or {}).get("per_round") or [])
    gn["board_size"] = gn["board"].map(lambda b: (b or {}).get("size"))
    gn["board_new_posts"] = gn["board"].map(lambda b: (b or {}).get("new_posts"))
    gn["board_categories"] = gn["board"].map(lambda b: (b or {}).get("categories") or {})
    gn["pop_total"] = gn["population"].map(lambda p: sum((p or {}).values()))
    gn["pop_llm"] = gn["population"].map(
        lambda p: sum(v for k, v in (p or {}).items() if not str(k).startswith("script:")))
    gn["pop_script"] = gn["population"].map(
        lambda p: sum(v for k, v in (p or {}).items() if str(k).startswith("script:")))
    gn["pop_types"] = gn["population"].map(lambda p: len(p or {}))
    gn["n_retired"] = gn["retired"].map(lambda r: len(r) if isinstance(r, list) else 0)
    return gn


def _attach_attempts(mv: pd.DataFrame, gm: pd.DataFrame) -> pd.DataFrame:
    """Attach per-agent-game ATTEMPT counts taken from the move rows.

    review-astra.md §15: "Count attempted calls even if the eventual action
    fails." A tool call is counted from `tool_calls` (what the model asked for),
    not from `tool_results` (what the harness managed to do), and rows with
    `parse_ok = false` are included. `channel_used` from `game_end` is kept
    beside it, so the two can be compared rather than conflated.

    The count is the UNION over every attempt of every scored-phase move row of
    that agent-game, aborted and orphaned rows included: a first attempt that
    read the board and then failed to parse is a board call the model made, and
    it is invisible in the top-level `tool_calls`, which holds only the final
    attempt (notes-astra-run-review.md finding 6). Warm-up rows are runner-
    assigned and contribute nothing (finding 15). `delivered_*` keeps the
    final-attempt counts, which is what the harness's own `use_count` records.
    """
    llm = mv[mv["is_decision"]]
    key = ["sandbox", "generation", "game", "agent"]
    agg = llm.groupby(key, sort=False).agg(
        attempted_board_calls=("att_board_calls", "sum"),
        attempted_post_calls=("att_post_calls", "sum"),
        attempted_read_calls=("att_read_calls", "sum"),
        attempted_decoy_calls=("att_decoy_calls", "sum"),
        attempted_unlisted_calls=("att_unlisted_calls", "sum"),
        final_attempt_board_calls=("n_board_calls", "sum"),
        final_attempt_post_calls=("n_post_calls", "sum"),
        final_attempt_decoy_calls=("decoy_calls", "sum"),
        calls_lost_by_retry=("board_call_lost_by_retry", "sum"),
        n_moves_logged=("round", "count"),
        n_moves_played=("is_played", "sum"),
        n_moves_aborted=("status", lambda s: int((s == "aborted").sum())),
        n_moves_unscored=("status", lambda s: int((s == "unscored").sum())),
        n_failed_moves=("parse_ok", lambda s: int((~s.astype(bool)).sum())),
    )
    failed_with_call = llm[(~llm["parse_ok"].astype(bool)) & (llm["att_board_calls"] > 0)] \
        .groupby(key, sort=False).size().rename("board_calls_on_failed_moves")
    agg = agg.join(failed_with_call).fillna({"board_calls_on_failed_moves": 0})
    # the round of the first ATTEMPTED board call. `first_use_round` on game_end
    # is the final attempt's, so it loses or delays a call a retry dropped
    # (finding 7); both are kept and neither is called the other.
    first_att = llm[llm["att_board_calls"] > 0].groupby(key, sort=False)["round"].min() \
        .rename("attempted_first_use_round")
    agg = agg.join(first_att)
    gm = gm.merge(agg.reset_index(), on=key, how="left")
    for c in ("attempted_board_calls", "attempted_post_calls", "attempted_read_calls",
              "attempted_decoy_calls", "attempted_unlisted_calls", "final_attempt_board_calls",
              "final_attempt_post_calls", "final_attempt_decoy_calls", "calls_lost_by_retry",
              "n_moves_logged", "n_moves_played", "n_moves_aborted", "n_moves_unscored",
              "n_failed_moves", "board_calls_on_failed_moves"):
        gm[c] = gm[c].fillna(0).astype(int)
    gm = gm.rename(columns={"first_use_round": "final_attempt_first_use_round"}) \
        if "first_use_round" in gm.columns else gm
    gm["attempted_any"] = (gm["attempted_board_calls"] > 0).astype(float)
    gm["attempted_decoy"] = (gm["attempted_decoy_calls"] > 0).astype(float)
    # the per-game board-over-decoy ratio: the single most interpretable number
    # the design produces (FRAMING-11TH-HOUR.md §2, §3 row 4). 0/0 is null,
    # board>0 over no decoy calls is +inf; see trace_coding.ratio_or_null.
    gm["board_calls"] = gm["attempted_board_calls"]
    gm["decoy_calls"] = gm["attempted_decoy_calls"]
    gm["board_over_decoy"] = [ratio_or_null(b, d) for b, d in zip(gm["board_calls"], gm["decoy_calls"])]
    return gm


def _cross_checks(mv: pd.DataFrame, gm: pd.DataFrame) -> list:
    """Checks that need two record kinds at once."""
    out = []
    # `use_count` / `decoy_count` / `posts` are the harness's record of the FINAL
    # attempt, so they are checked against the final-attempt counts. The
    # attempts union is deliberately larger and is reported (T8), not asserted.
    per_agent_game = mv[mv["is_decision"]].groupby(["sandbox", "generation", "game", "agent"], sort=False).agg(
        board_calls=("n_board_calls", "sum"), post_calls=("n_post_calls", "sum"),
        decoy=("decoy_calls", "sum"), n_moves=("round", "count"))
    for _, g in gm.iterrows():
        key = (g["sandbox"], g["generation"], g["game"], g["agent"])
        if key not in per_agent_game.index:
            # A game that aborted on its very first round leaves one side with
            # warm-up rows only and no scored decision at all; the runner records
            # that as `status: aborted`, `rounds: 0`, `moves_logged: 0`. That is
            # the abort working as designed, not a desynced log, so it is counted
            # in T8 (`aborted_before_first_decision`) instead of flagged here.
            if not (g.get("aborted") and not int(g.get("moves_logged") or 0)):
                out.append({"source": g.get("_source"), "line": g.get("_line"), "kind": "cross",
                            "field": "game_end", "problem": "no move rows for this agent-game",
                            "value": str(key)})
            continue
        row = per_agent_game.loc[key]
        if int(row["board_calls"]) != int(g["use_count"]):
            out.append({"source": g.get("_source"), "line": g.get("_line"), "kind": "cross",
                        "field": "use_count", "problem": f"game_end says {g['use_count']}, moves show "
                                                         f"{int(row['board_calls'])} board tool calls", "value": str(key)})
        if int(row["post_calls"]) != int(g["n_posts"]):
            out.append({"source": g.get("_source"), "line": g.get("_line"), "kind": "cross",
                        "field": "posts", "problem": f"game_end lists {int(g['n_posts'])} posts, moves show "
                                                     f"{int(row['post_calls'])} notes_post calls", "value": str(key)})
        if int(row["decoy"]) != int(g["decoy_count"]):
            out.append({"source": g.get("_source"), "line": g.get("_line"), "kind": "cross",
                        "field": "decoy_count", "problem": f"game_end says {g['decoy_count']}, moves show "
                                                           f"{int(row['decoy'])}", "value": str(key)})
    return out


#: What one complete sandbox must contain: 12 LLM + 12 scripts, one generation,
#: a fixed schedule of 210 LLM-involving games = 66 LLM-LLM + 144 LLM-script,
#: which write 2*66 + 144 = 276 agent-game ends (pre-registration; the review's
#: reconciliation table). A sandbox that has finished and misses any of these is
#: a shortfall to report, not a smaller denominator to use silently.
EXPECTED_UNIQUE_GAMES = 210
EXPECTED_AGENT_GAMES = 276


def modal_complete_shape(gm: pd.DataFrame, gn: pd.DataFrame) -> tuple:
    """The (unique games, agent-game ends) most completed sandboxes agree on.

    The pre-registered grid is 210 / 276, but the check is expressed against
    whatever THIS dataset's completed sandboxes agree on, so it catches a short
    sandbox in any grid (a synthetic fixture, a smaller pilot) instead of only
    the one grid. `run_all` separately checks the modal shape against the
    pre-registered constants and says so if they differ.
    """
    finished = set(gn["sandbox"]) if gn is not None and not gn.empty and "sandbox" in gn.columns else set()
    shapes = []
    for sandbox, sub in gm.groupby("sandbox", sort=True):
        if sandbox in finished:
            shapes.append((int(sub["game_uid"].nunique()), int(len(sub))))
    if not shapes:
        return (None, None)
    return max(set(shapes), key=shapes.count)


def _reverse_and_cardinality_checks(mv: pd.DataFrame, gm: pd.DataFrame,
                                    gn: pd.DataFrame) -> list:
    """Joins the other way round, and the counts a complete sandbox must have.

    `_cross_checks` walks game_end -> moves, so a move row belonging to no
    game_end is invisible to it: zero schema violations is not proof of a
    complete denominator (finding 4). This walks moves -> game_end as well, and
    checks the expected cardinality of every sandbox that has finished.
    """
    out = []
    key = ["sandbox", "generation", "game", "agent"]
    ends = set(map(tuple, gm[key].itertuples(index=False, name=None)))
    dec = mv[mv["is_decision"]] if "is_decision" in mv.columns else mv[mv["is_llm"]]
    orphan = dec.groupby(key, sort=False).agg(n=("round", "count"),
                                              src=("_source", "first"), line=("_line", "first"))
    for k, r in orphan.iterrows():
        if tuple(k) not in ends:
            out.append({"source": r["src"], "line": int(r["line"]), "kind": "cross",
                        "field": "move", "problem": f"{int(r['n'])} scored decision(s) with no "
                                                    f"game_end row: this agent-game is missing from "
                                                    f"the endpoint denominator", "value": str(tuple(k))})
    finished = set(gn["sandbox"]) if gn is not None and not gn.empty and "sandbox" in gn.columns else set()
    want_u, want_a = modal_complete_shape(gm, gn)
    for sandbox, sub in gm.groupby("sandbox", sort=True):
        if sandbox not in finished or want_u is None:
            continue                      # a running sandbox is provisional, not wrong
        uniq, agent_games = sub["game_uid"].nunique(), len(sub)
        if uniq != want_u or agent_games != want_a:
            out.append({"source": sub["_source"].iloc[0], "line": 0, "kind": "cardinality",
                        "field": "game_end", "problem": f"completed sandbox has {uniq} unique games "
                                                        f"and {agent_games} agent-game ends; every "
                                                        f"other completed sandbox in this dataset has "
                                                        f"{want_u} / {want_a}", "value": sandbox})
        bad_sides = sub.groupby("game_uid").agg(n=("agent", "count"), pt=("pair_type", "first"))
        want = bad_sides["pt"].map({"llm-llm": 2, "llm-script": 1})
        wrong = bad_sides[bad_sides["n"] != want]
        if len(wrong):
            out.append({"source": sub["_source"].iloc[0], "line": 0, "kind": "cardinality",
                        "field": "game_end", "problem": f"{len(wrong)} game(s) with the wrong number "
                                                        f"of LLM sides for their pair_type",
                        "value": f"{sandbox}: {list(wrong.index[:5])}"})
    return out


def posts_table(moves: pd.DataFrame, games: pd.DataFrame | None = None,
                completed_only: bool = True) -> pd.DataFrame:
    """One row per ATTEMPTED post (derived view of `moves`).

    Attempted, not committed: the row is what the model asked the board to store,
    taken from the union over every attempt, so a post made by a first attempt
    that then failed to parse is present (finding 7). A post attempt is NOT proof
    the board accepted it, and two attempts posting identical text are two model
    calls, never merged.

    `completed_only` applies the same policy the secondary tables use and is
    recorded on every row as `game_policy`, so the SUMMARY's claim about which
    games were counted can be checked. Warm-up rows are never posts.
    """
    cols = ["sandbox", "dataset", "model", "condition", "effort", "opponent_mix", "score_state",
            "paraphrase", "seed", "generation", "game", "round", "agent", "pair_type", "game_uid",
            "attempt", "from_final_attempt", "move_status", "game_complete", "game_policy", "text"]
    if moves is None or moves.empty:
        return pd.DataFrame(columns=cols)
    sub = moves[moves["is_decision"]] if "is_decision" in moves.columns else moves
    sub = sub[sub["att_post_texts"].map(lambda x: bool(x) if isinstance(x, list) else False)]
    complete_uids = set()
    if games is not None and not games.empty and "game_complete" in games.columns:
        complete_uids = set(games.loc[games["game_complete"], "game_uid"])
    policy = "completed games only" if completed_only else "every game, aborted included"
    rows = []
    for m in sub.itertuples():
        done = m.game_uid in complete_uids if complete_uids else True
        if completed_only and complete_uids and not done:
            continue
        final = set(m.post_texts) if isinstance(m.post_texts, list) else set()
        for post in m.att_post_texts:
            rows.append({
                "sandbox": m.sandbox, "dataset": getattr(m, "dataset", "prereg"), "model": m.model,
                "condition": m.condition, "effort": m.effort, "opponent_mix": m.opponent_mix,
                "score_state": m.score_state, "paraphrase": m.paraphrase, "seed": m.seed,
                "generation": m.generation, "game": m.game, "round": m.round, "agent": m.agent,
                "pair_type": m.pair_type, "game_uid": m.game_uid,
                "attempt": post.get("attempt"),
                "from_final_attempt": post.get("text") in final,
                "move_status": m.status, "game_complete": done, "game_policy": policy,
                "text": post.get("text"),
            })
    return pd.DataFrame(rows, columns=cols)


def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Load a runs dir and report schema violations.")
    ap.add_argument("--runs", required=True)
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args(argv)
    rd = load_runs(a.runs, strict=a.strict)
    print(f"moves={len(rd.moves)} games={len(rd.games)} generations={len(rd.generations)} "
          f"sandboxes={len(rd.manifests)} violations={len(rd.violations)}")
    for n in rd.notes:
        print("note:", n)
    if not rd.clean:
        print(rd.violations.head(20).to_string())
    return 0 if rd.clean else 1


if __name__ == "__main__":
    raise SystemExit(main())


# ------------------------------------------------------------------ sandbox as replicate
SCOPES = ("fixed_population", "all_generations")
#: Pre-registered quality rule: "a sandbox with >10% aborted games is excluded
#: from confirmatory analysis and reported". STRICTLY greater, on unique
#: LLM-involving games, so 21/210 = 10.0% stays eligible.
QUALITY_ABORT_LIMIT = 0.10


def _blocks_by_sandbox(rd: "RunData") -> dict:
    """sandbox -> matched-block id, from `manifest.block` (B1..B6, M1..M6).

    The design randomises in blocks and gives every sandbox its own seed
    (`<block digit><cell digit>`), so a block key built from the seed can never
    match two arms of a contrast. The manifest names the block directly; where
    it does not (synthetic runs, whose grid uses the seed as the block), the
    seed is the fallback.
    """
    out: dict = {}
    mf = rd.manifests
    if mf is None or mf.empty or "sandbox" not in mf.columns or "block" not in mf.columns:
        return out
    for sb, b in zip(mf["sandbox"], mf["block"]):
        if isinstance(b, str) and b:
            out[sb] = b
    return out


def _modal_llm_model(df: pd.DataFrame) -> str:
    """The LLM under test in these rows (`game_end` rows are per LLM agent)."""
    m = df.loc[~df["model"].astype(str).str.startswith("script:"), "model"]
    return str(m.mode().iloc[0]) if len(m) and len(m.mode()) else "unknown"


def _block_id(blocks: dict, sandbox: str, s: pd.DataFrame) -> str:
    """The randomisation block this sandbox belongs to (B1..B6, M1..M6, or s<seed>)."""
    return blocks.get(sandbox) or blocks.get(base_sandbox(sandbox)) or f"s{int(s['seed'].iloc[0])}"


def _block_key(blocks: dict, sandbox: str, s: pd.DataFrame, held: str) -> str:
    """Everything held fixed in a contrast: model, condition, `held`, block."""
    return (f"{_modal_llm_model(s).split('/')[-1]}/{s['condition'].iloc[0]}/"
            f"{s[held].iloc[0]}/{_block_id(blocks, sandbox, s)}")


def _fixed_population_generations(rd: RunData, primary_generation: int | None = None) -> set:
    """(sandbox, generation) pairs whose population still matches the assigned one.

    `primary_generation` defaults to the FIRST generation each sandbox logged,
    not to a hard-coded 1: the live runner numbers generations from 0, and
    pinning the baseline to a generation that does not exist silently empties
    the primary scope.

    A sandbox that is still running has written no `generation_end` row yet.
    Its population cannot have changed - reproduction happens at a generation
    boundary - so every generation it has is in the fixed-population scope, and
    `sandbox_complete` is what marks it provisional.
    """
    gn = rd.generations
    seen_all = set(rd.games["sandbox"]) if not rd.games.empty else set()
    out = set()
    if not gn.empty and "population" in gn.columns:
        for sandbox, sub in gn.groupby("sandbox", sort=False):
            base_gen = primary_generation if primary_generation is not None \
                else int(sub["generation"].min())
            base = sub.loc[sub["generation"] == base_gen, "population"]
            base = base.iloc[0] if len(base) else None
            for _, r in sub.iterrows():
                if base is not None and r["population"] == base:
                    out.add((sandbox, int(r["generation"])))
        seen_all -= set(gn["sandbox"])
    if seen_all and not rd.games.empty:
        unfinished = rd.games[rd.games["sandbox"].isin(seen_all)]
        out |= {(sb, int(g)) for sb, g in zip(unfinished["sandbox"], unfinished["generation"])}
    return out


def sandbox_table(rd: RunData, primary_generation: int | None = None) -> pd.DataFrame:
    """One row per sandbox x scope: the replicate-level view (review-astra.md §2).

    The primary endpoint is `rate_per_game_either`: the proportion of
    LLM-involving games in the sandbox with at least one **attempted** board
    call. Script-script games never produce a `game_end` row and are therefore
    not in the denominator, which is the point of calling it "LLM-involving".

    Scopes, because a sandbox's population changes between generations:
      fixed_population       every generation whose population composition still
                             equals the composition as assigned. If the runner
                             freezes the population (review-astra.md §2) that is
                             all of them; if it evolves, it collapses to the
                             sandbox's first generation, before any
                             reproduction. This is the pre-registered primary
                             scope. A sandbox still running (no `generation_end`
                             row) keeps all of its generations here and is
                             flagged `sandbox_complete = False`.
      all_generations        every generation pooled; reported alongside as a
                             robustness scope, carrying survivor bias.

    Denominators are all reported side by side, never collapsed (§15):
    per LLM-involving game (either agent), per LLM-LLM game (both agents), per
    agent-game, and the per-opportunity hazard implied by 1-(1-p)^L.
    """
    g = rd.games
    if g.empty:
        return pd.DataFrame()
    fixed = _fixed_population_generations(rd, primary_generation)
    blocks = _blocks_by_sandbox(rd)
    rows = []
    for scope in SCOPES:
        if scope == "all_generations":
            sub_all = g
        else:
            keep = [(sb, gen) in fixed for sb, gen in zip(g["sandbox"], g["generation"])]
            sub_all = g[pd.Series(keep, index=g.index)]
        for sandbox, s in sub_all.groupby("sandbox", sort=True):
            # --- the three denominators, side by side and never collapsed.
            # observed  : every scheduled game MINUS the provider-error aborts in
            #             which no completion ever returned. This is the REGISTERED
            #             endpoint: an unobserved game is missing data, not a
            #             non-user (BUG-LEDGER N1).
            # keep-all  : every game_end row present, unobserved ones scored 0.
            # completed : games that ran to the end.
            all_games = s.groupby("game_uid")["attempted_any"].max()
            obs = s[s["game_observed"]] if "game_observed" in s.columns else s
            observed = obs.groupby("game_uid")["attempted_any"].max() if len(obs) \
                else pd.Series(dtype=float)
            done = s[s["game_complete"]]
            either_done = done.groupby("game_uid")["attempted_any"].max() if len(done) \
                else pd.Series(dtype=float)
            either = observed              # the registered view
            n_games = len(observed)
            n_games_all = len(all_games)
            aborted = s[s["game_aborted"]]
            n_aborted = aborted["game_uid"].nunique()
            n_aborted_board = int(aborted.groupby("game_uid")["attempted_any"].max().sum()) \
                if len(aborted) else 0
            n_unobserved = int(s.loc[s.get("game_unobserved", False), "game_uid"].nunique()) \
                if "game_unobserved" in s.columns else 0
            n_pe_censored = int(s.loc[s.get("game_provider_error_censored", False), "game_uid"].nunique()) \
                if "game_provider_error_censored" in s.columns else 0
            # the registered quality rule: STRICTLY more than 10% aborted unique
            # LLM-involving games excludes a sandbox from confirmatory analysis
            # (pre-registration; decision-log 08:10 reconciliation item 1).
            abort_rate = (n_aborted / n_games_all) if n_games_all else float("nan")
            eligible = bool(n_games_all) and not (abort_rate > QUALITY_ABORT_LIMIT)
            complete_sb = bool(s["sandbox_complete"].iloc[0])
            L = float(s["n_moves_logged"].mean()) if len(s) else float("nan")
            r_agent = float(obs["attempted_any"].mean()) if len(obs) else float("nan")
            hazard = 1.0 - (1.0 - r_agent) ** (1.0 / L) if L and L > 0 and r_agent < 1 else float("nan")
            first = obs.loc[obs["attempted_any"] > 0, "attempted_first_use_round"].dropna() \
                if "attempted_first_use_round" in obs.columns else pd.Series(dtype=float)
            llm_llm = obs[obs["pair_type"] == "llm-llm"].groupby("game_uid")["attempted_any"]
            both = (llm_llm.sum() == 2) if len(llm_llm) else pd.Series(dtype=bool)
            rows.append({
                "sandbox": sandbox, "scope": scope,
                "generations_used": sorted(set(int(x) for x in s["generation"])),
                "condition": s["condition"].iloc[0], "effort": s["effort"].iloc[0],
                "score_state": s["score_state"].iloc[0],
                "opponent_mix": s["opponent_mix"].iloc[0], "seed": int(s["seed"].iloc[0]),
                "generations": s["generation"].nunique(),
                "dataset": s["dataset"].iloc[0] if "dataset" in s.columns else "prereg",
                "base_sandbox": s["base_sandbox"].iloc[0],
                "model": _modal_llm_model(s),
                "paraphrase": s["paraphrase"].iloc[0],
                "sandbox_complete": complete_sb,
                # denominators, explicitly
                "n_games_llm_involving": n_games_all,
                "n_games_observed": n_games,
                "n_games_completed": int(len(either_done)),
                "n_games_aborted": int(n_aborted),
                "n_games_aborted_with_board_attempt": n_aborted_board,
                "n_games_unobserved_provider_error": n_unobserved,
                "n_games_provider_error_censored": n_pe_censored,
                "abort_rate_per_game": abort_rate,
                "eligible_registered": eligible,
                "exclusion_reason": ("" if eligible else
                                     f"aborted {n_aborted}/{n_games_all} = {abort_rate:.1%} > "
                                     f"{QUALITY_ABORT_LIMIT:.0%} (pre-registered rule)"),
                "n_games_llm_llm": int(len(llm_llm)),
                "n_agent_games": len(s),
                "n_agent_games_observed": len(obs),
                "n_llm_moves": int(s["n_moves_logged"].sum()),
                "mean_rounds_per_agent_game": L,
                # the primary endpoint on all three views
                "rate_per_game_either": float(either.mean()) if n_games else float("nan"),
                "rate_per_game_either_keepall": float(all_games.mean()) if n_games_all else float("nan"),
                "rate_per_game_either_completed": float(either_done.mean()) if len(either_done)
                else float("nan"),
                "rate_per_llm_llm_game_both": float(both.mean()) if len(both) else float("nan"),
                "rate_per_agent_game": r_agent,
                "hazard_per_opportunity_unfitted": hazard,
                "final_attempt_rate_per_agent_game": float((obs["use_count"] > 0).mean())
                if len(obs) else float("nan"),
                "post_rate_per_agent_game": float((obs["attempted_post_calls"] > 0).mean())
                if len(obs) else float("nan"),
                "read_rate_per_agent_game": float((obs["attempted_read_calls"] > 0).mean())
                if len(obs) else float("nan"),
                "decoy_rate_per_game_either": float(obs.groupby("game_uid")["attempted_decoy"].max().mean())
                if n_games else float("nan"),
                "decoy_rate_per_agent_game": float(obs["attempted_decoy"].mean()) if len(obs)
                else float("nan"),
                # the listed-use vs content-bearing discriminator, as call counts
                "board_calls": int(obs["board_calls"].sum()),
                "decoy_calls": int(obs["decoy_calls"].sum()),
                "board_over_decoy": ratio_or_null(obs["board_calls"].sum(), obs["decoy_calls"].sum()),
                "calls_on_failed_moves": int(s["board_calls_on_failed_moves"].sum()),
                "calls_lost_by_retry": int(s["calls_lost_by_retry"].sum()),
                "failed_move_rate": float(s["n_failed_moves"].sum() / max(1, s["n_moves_logged"].sum())),
                "median_attempted_first_use_round": float(first.median()) if len(first) else float("nan"),
                # secondary statistics: COMPLETED games only, and named so
                "coop_rate_llm_own_completed": float(done["coop_rate"].mean(skipna=True))
                if len(done) else float("nan"),
                "coop_rate_llm_own": float(done["coop_rate"].mean(skipna=True))
                if len(done) else float("nan"),
                "mean_score_completed": float(done["score"].mean(skipna=True)) if len(done)
                else float("nan"),
                "n_posts_completed": int(done["n_posts"].sum()) if len(done) else 0,
                # matched blocks: everything except the contrasted factor is held
                # fixed - the randomisation block, the model and the condition.
                # The MODEL is in the key because two models can share a seed AND
                # a block name (DeepSeek B1 and MiMo M1 are both seed 109, both
                # `block: B1`), and a contrast must never pair across models.
                "block_id": _block_id(blocks, sandbox, s),
                "block_effort": _block_key(blocks, sandbox, s, "score_state"),
                "block_state": _block_key(blocks, sandbox, s, "effort"),
                "block_mix": _block_key(blocks, sandbox, s, "effort"),
            })
    return pd.DataFrame(rows)


def filter_paraphrases(rd: RunData, keep=("p1", "p2", "p3")) -> RunData:
    """A copy of `rd` holding only the named paraphrases.

    `p4` is the extra wording used by the X1/Y1 placement sandboxes. It is not
    part of the pre-registered grid, so it is removed from every pre-registered
    table and test and appears only in T8 (censoring) and T9 (the placement
    test), which are explicitly exploratory.
    """
    keep = set(keep)

    def sub(df):
        if df is None or df.empty or "paraphrase" not in df.columns:
            return df
        return df[df["paraphrase"].isin(keep)].reset_index(drop=True)

    dropped = sorted(set(rd.games["sandbox"]) - set(sub(rd.games)["sandbox"])) \
        if not rd.games.empty else []
    notes = list(rd.notes)
    if dropped:
        notes.append(f"{len(dropped)} sandbox(es) excluded from every pre-registered table and test "
                     f"because their paraphrase is outside the pre-registered p1-p3: "
                     f"{', '.join(dropped)}. They are reported in T9 (placement test) and T8.")
    # manifests carry no paraphrase, so they are filtered by the sandboxes kept
    mf = rd.manifests
    if not mf.empty and "sandbox" in mf.columns and not rd.games.empty:
        mf = mf[mf["sandbox"].isin(set(sub(rd.games)["sandbox"]))].reset_index(drop=True)
    return RunData(moves=sub(rd.moves), games=sub(rd.games), generations=sub(rd.generations),
                   violations=rd.violations, manifests=mf, notes=notes,
                   score_state_source=rd.score_state_source, dataset=rd.dataset,
                   repair_status=list(rd.repair_status))


# ------------------------------------------------------------------ censoring (T8)
#: The grouping the censoring table is read at. Model and paraphrase are in it
#: because the abort rate is driven by both: the answer runs past the
#: `answer_tokens` cap after the model has read the board, and the longer p3
#: prompt makes that far more likely (RUNBOOK, 13 Sept relaunch).
CENSORING_KEYS = ("dataset", "model", "condition", "effort", "score_state", "paraphrase")


def _abort_causes(moves: pd.DataFrame, uids: set) -> dict:
    """`fallback_flag` mix of the aborting decisions, split by who caused it.

    A `length_truncated` abort happened AFTER the model's board call; a
    `provider_error` abort means no completion ever returned. Pooling them into
    one "abort rate" hides that the second kind observed nothing (BUG-LEDGER N1).
    """
    blank = {"abort_cause_mix_model": "", "abort_cause_mix_provider": "",
             "aborting_decisions_model": 0, "aborting_decisions_provider": 0}
    if moves is None or moves.empty or not uids or "status" not in moves.columns:
        return blank
    sub = moves[moves["status"].eq("aborted") & moves["game_uid"].isin(uids)]
    if sub.empty:
        return blank
    is_prov = sub["fallback_flag"].isin(PROVIDER_ERROR_FLAGS)

    def mix(part):
        c = part["fallback_flag"].fillna("none").value_counts()
        return ", ".join(f"{k} x{int(v)}" for k, v in c.items())
    return {"abort_cause_mix_model": mix(sub[~is_prov]),
            "abort_cause_mix_provider": mix(sub[is_prov]),
            "aborting_decisions_model": int((~is_prov).sum()),
            "aborting_decisions_provider": int(is_prov.sum())}


#: Every column's unit, printed with the table so no reader has to guess.
CENSORING_UNITS = ("`*_games` and every `rate_*` count UNIQUE LLM-involving games (one `game_uid`); "
                   "`aborting_decisions_*` count move rows; `n_sandboxes` counts sandboxes; "
                   "`aborted_before_first_decision` counts agent-game end rows.")


def censoring_table(rd: "RunData | list", per_sandbox: bool = False) -> pd.DataFrame:
    """Aborted games per cell, and the primary endpoint on every denominator.

    Three views of the endpoint, side by side and never collapsed:

    `rate_observed`   the REGISTERED endpoint. Every scheduled game minus the
                      provider-error aborts in which no completion ever returned:
                      those observed nothing, so scoring them non-users would
                      manufacture negatives, and the 429 storm hit only the
                      high-effort arm of contrast A (BUG-LEDGER N1).
    `rate_keep_all`   every game_end row present, unobserved ones scored 0.
    `rate_completed`  completed games only.

    Plus two sensitivity BOUNDS on the observed view - bounds, not estimates:
    `bound_lower` scores every aborted game with no observed attempt as a
    non-user (what the data shows); `bound_upper` scores every one of them as a
    user (the most the unseen games could add). What those games would have done
    is not identified by this design; the width between the bounds is the honest
    statement, and `rate_difference` is a difference between two observed
    denominators, not an estimated bias (finding 10).

    Accepts one RunData or several (one per dataset label); several are
    concatenated for display only, each keeping its own `dataset` label.
    """
    rds = [rd] if isinstance(rd, RunData) else list(rd)
    g = pd.concat([r.games for r in rds if not r.games.empty], ignore_index=True) \
        if any(not r.games.empty for r in rds) else pd.DataFrame()
    m = pd.concat([r.moves for r in rds if not r.moves.empty], ignore_index=True) \
        if any(not r.moves.empty for r in rds) else pd.DataFrame()
    keys = list(CENSORING_KEYS) + (["sandbox"] if per_sandbox else [])
    cols = keys + ["n_sandboxes", "unique_games", "observed_games", "completed_games",
                   "aborted_games", "aborted_games_with_board_attempt",
                   "unobserved_provider_error", "provider_error_censored",
                   "aborted_before_first_decision", "abort_rate",
                   "aborting_decisions_model", "aborting_decisions_provider",
                   "abort_cause_mix_model", "abort_cause_mix_provider",
                   "rate_observed", "rate_keep_all", "rate_completed", "rate_difference",
                   "bound_lower", "bound_upper", "bound_width",
                   "board_calls_lost_by_retry", "sandboxes_incomplete"]
    if g.empty:
        return pd.DataFrame(columns=cols)
    for k in keys:
        if k not in g.columns:
            g[k] = "unknown"
    rows = []
    for vals, sub in g.groupby(keys, sort=True, observed=True):
        vals = vals if isinstance(vals, tuple) else (vals,)
        per_game = sub.groupby("game_uid").agg(
            any_board=("attempted_any", "max"), aborted=("game_aborted", "max"),
            unobserved=("game_unobserved", "max"), pe=("game_provider_error_abort", "max"))
        ab = per_game[per_game["aborted"].astype(bool)]
        done = per_game[~per_game["aborted"].astype(bool)]
        obs = per_game[~per_game["unobserved"].astype(bool)]
        n_obs = len(obs)
        positives = float(obs["any_board"].sum())
        # aborted-but-observed games that never showed an attempt: the only games
        # the bound can move, since a completed game's outcome is known
        unknown = int(((ab["any_board"] == 0) & (~ab["unobserved"].astype(bool))).sum())
        rows.append(dict(
            zip(keys, vals),
            n_sandboxes=int(sub["sandbox"].nunique()),
            unique_games=int(len(per_game)),
            observed_games=n_obs,
            completed_games=int(len(done)),
            aborted_games=int(len(ab)),
            aborted_games_with_board_attempt=int(ab["any_board"].sum()),
            unobserved_provider_error=int(per_game["unobserved"].astype(bool).sum()),
            provider_error_censored=int((per_game["pe"].astype(bool)
                                         & ~per_game["unobserved"].astype(bool)).sum()),
            aborted_before_first_decision=int(sub["aborted_before_first_decision"].sum())
            if "aborted_before_first_decision" in sub.columns else 0,
            abort_rate=float(len(ab) / len(per_game)) if len(per_game) else float("nan"),
            **_abort_causes(m, set(sub.loc[sub["game_aborted"], "game_uid"])),
            rate_observed=(positives / n_obs) if n_obs else float("nan"),
            rate_keep_all=float(per_game["any_board"].mean()) if len(per_game) else float("nan"),
            rate_completed=float(done["any_board"].mean()) if len(done) else float("nan"),
            rate_difference=(float(per_game["any_board"].mean() - done["any_board"].mean())
                             if len(done) and len(per_game) else float("nan")),
            bound_lower=(positives / n_obs) if n_obs else float("nan"),
            bound_upper=((positives + unknown) / n_obs) if n_obs else float("nan"),
            bound_width=(unknown / n_obs) if n_obs else float("nan"),
            board_calls_lost_by_retry=int(sub["calls_lost_by_retry"].sum())
            if "calls_lost_by_retry" in sub.columns else 0,
            sandboxes_incomplete=int(sub.loc[~sub["sandbox_complete"].astype(bool), "sandbox"].nunique())
            if "sandbox_complete" in sub.columns else 0,
        ))
    return pd.DataFrame(rows, columns=cols)
