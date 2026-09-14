"""The JSONL contract from ``specs/moves-schema.md`` (v1), as data + validators.

One place for the enums and the per-kind field rules, so ``load.py`` validates
and ``synth.py`` generates against the *same* definition.

Where the spec is silent, the choice made here is marked ``AMBIGUITY:`` in a
comment and repeated in the analysis README section of SUMMARY.md.
"""
from __future__ import annotations

from typing import Any

# --- enums, verbatim from the spec -------------------------------------------------
KINDS = ("move", "game_end", "generation_end")
CONDITIONS = ("absent", "permitted", "forbidden", "hidden")
EFFORTS = ("off", "low", "medium", "high")
EFFORT_ORDER = {"off": 0, "low": 1, "medium": 2, "high": 3}
FRAMINGS = ("F0", "F1", "F4", "F6", "F8")
# p1-p3 are the pre-registered paraphrases (blocks B1-B2, B3-B4, B5-B6);
# p4 is the extra wording used only by the X1/Y1 diagnostic sandboxes.
PARAPHRASES = ("p1", "p2", "p3", "p4")
# "script-script" is new in the 13 Sept relaunch: script-vs-script games are now
# logged as move rows (they still write no `game_end`, so they stay out of every
# rate's denominator).
PAIR_TYPES = ("llm-llm", "llm-script", "script-script")
# The 13 Sept runner adds three parse outcomes the v1 spec did not name:
# "ambiguous" (both option letters present), "length_truncated" (the answer hit
# the `answer_tokens` cap - the cause of the aborted decisions) and "refusal".
FALLBACK_FLAGS = (None, "empty_content", "no_action_token", "provider_error", "timeout",
                  "ambiguous", "length_truncated", "refusal")
ACTIONS = ("C", "D", None)
CHANNEL_CONDITIONS = ("permitted", "forbidden", "hidden")  # conditions where tools exist

# A move row's lifecycle, added by the 13 Sept relaunch (RUNBOOK "13 Sept relaunch"):
#   status "ok"        a decision that was played
#   status "aborted"   both attempts failed to parse; `executed` is null, both
#                      attempts are under `attempts`, the game is abandoned
#   status "unscored"  an orphaned same-round reply from the other side of an
#                      abandoned round; `executed` is null
#   phase  "warmup"    a runner-assigned move (provider "assigned") used to build
#                      the ahead/behind score gap - not a model decision at all
MOVE_STATUSES = ("ok", "aborted", "unscored")
MOVE_PHASES = ("scored", "warmup")
GAME_STATUSES = ("ok", "aborted")
PLAYED_STATUS, SCORED_PHASE, WARMUP_PHASE = "ok", "scored", "warmup"

BOARD_TOOLS = ("notes_read", "notes_post")
# The decoy is `workspace_clock` in every live manifest (`decoy_tool`);
# `ledger_lookup` is the name the v1 spec used and is still accepted so older
# captures and fixtures validate.
DECOY_TOOL = "workspace_clock"
DECOY_TOOLS = ("workspace_clock", "ledger_lookup")
TOOLS = BOARD_TOOLS + DECOY_TOOLS

# AMBIGUITY: opponent mix (D5's winning/losing column) has no field in the move
# schema. It is a sandbox-level design factor, so it is read from manifest.json
# (key ``opponent_mix``) and only derived from scores if the manifest omits it.
OPPONENT_MIXES = ("win", "lose")

COMMON_FIELDS = ("sandbox", "seed", "condition", "framing", "paraphrase", "effort", "generation")

MOVE_FIELDS = (
    "game", "round", "agent", "model", "lineage", "parent", "opponent", "opponent_model",
    "pair_type", "prompt_sha256", "label_map", "option_order", "raw", "reasoning",
    "reasoning_tokens", "action", "executed", "noise_flipped", "fallback_flag", "parse_ok",
    "retries", "tool_calls", "tool_results", "read_before_post", "board_size_at_read",
    "decoy_calls", "score_gap_at_call", "payoff", "opponent_action", "latency_ms",
    "prompt_tokens", "completion_tokens", "provider", "quant", "ts",
)
GAME_END_FIELDS = (
    "game", "agent", "model", "opponent", "opponent_model", "pair_type", "rounds",
    "coop_rate", "opp_coop_rate", "score", "opp_score", "classification_answer",
    "classification_correct", "classification_raw", "prohibition_recall_answer",
    "prohibition_recall_correct", "channel_used", "first_use_round", "use_count",
    "decoy_count", "posts", "awareness_mentions",
)
GENERATION_END_FIELDS = ("population", "climate", "board", "fitness", "reproduced", "retired")


def _is_num(v: Any) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def _rate_ok(v: Any) -> bool:
    return v is None or (_is_num(v) and 0.0 <= float(v) <= 1.0)


def validate_record(rec: Any, source: str = "?", line: int = -1) -> list[dict]:
    """Return a list of violations (empty == valid). Never raises on bad input."""
    V: list[dict] = []

    def bad(field: str, problem: str, value: Any = None) -> None:
        V.append({
            "source": source, "line": line, "kind": (rec or {}).get("kind") if isinstance(rec, dict) else None,
            "field": field, "problem": problem, "value": repr(value)[:120],
        })

    if not isinstance(rec, dict):
        bad("<record>", "not a JSON object", rec)
        return V
    kind = rec.get("kind")
    if kind not in KINDS:
        bad("kind", f"not one of {KINDS}", kind)
        return V

    for f in COMMON_FIELDS:
        if f not in rec:
            bad(f, "missing required common field")
    if rec.get("condition") not in CONDITIONS:
        bad("condition", f"not one of {CONDITIONS}", rec.get("condition"))
    if rec.get("effort") not in EFFORTS:
        bad("effort", f"not one of {EFFORTS}", rec.get("effort"))
    if rec.get("paraphrase") not in PARAPHRASES:
        bad("paraphrase", f"not one of {PARAPHRASES}", rec.get("paraphrase"))
    if rec.get("framing") not in FRAMINGS:
        bad("framing", f"not one of {FRAMINGS}", rec.get("framing"))
    if not isinstance(rec.get("seed"), int) or isinstance(rec.get("seed"), bool):
        bad("seed", "not an int", rec.get("seed"))
    if not isinstance(rec.get("generation"), int) or isinstance(rec.get("generation"), bool):
        bad("generation", "not an int", rec.get("generation"))

    cond = rec.get("condition")
    if kind == "move":
        for f in MOVE_FIELDS:
            if f not in rec:
                bad(f, "missing required move field")
        if not isinstance(rec.get("round"), int) or (isinstance(rec.get("round"), int) and rec["round"] < 1):
            bad("round", "not an int >= 1", rec.get("round"))
        if rec.get("pair_type") not in PAIR_TYPES:
            bad("pair_type", f"not one of {PAIR_TYPES}", rec.get("pair_type"))
        if rec.get("action") not in ACTIONS:
            bad("action", "not one of C/D/null", rec.get("action"))
        if rec.get("executed") not in ACTIONS:
            bad("executed", "not one of C/D/null", rec.get("executed"))
        if rec.get("fallback_flag") not in FALLBACK_FLAGS:
            bad("fallback_flag", f"not one of {FALLBACK_FLAGS}", rec.get("fallback_flag"))
        if rec.get("status", PLAYED_STATUS) not in MOVE_STATUSES:
            bad("status", f"not one of {MOVE_STATUSES}", rec.get("status"))
        if rec.get("phase", SCORED_PHASE) not in MOVE_PHASES:
            bad("phase", f"not one of {MOVE_PHASES}", rec.get("phase"))
        ats = rec.get("attempts")
        if ats is not None and not isinstance(ats, list):
            bad("attempts", "not a list", ats)
        elif isinstance(ats, list):
            for a in ats:
                if not isinstance(a, dict):
                    bad("attempts", "entry is not an object", a)
                    continue
                atc = a.get("tool_calls")
                if atc is not None and not isinstance(atc, list):
                    bad("attempts", "attempt tool_calls is not a list", atc)
                if a.get("fallback_flag") not in FALLBACK_FLAGS:
                    bad("attempts", f"attempt fallback_flag not one of {FALLBACK_FLAGS}",
                        a.get("fallback_flag"))
        # An aborted or unscored decision is never played: `executed` must be null.
        if rec.get("status") in ("aborted", "unscored") and rec.get("executed") is not None:
            bad("executed", f"status={rec.get('status')} but executed is not null", rec.get("executed"))
        if not isinstance(rec.get("parse_ok"), bool):
            bad("parse_ok", "not a bool", rec.get("parse_ok"))
        if not isinstance(rec.get("noise_flipped"), bool):
            bad("noise_flipped", "not a bool", rec.get("noise_flipped"))
        # spec: "an unparsable move is retried once, then logged with action:null".
        # An `unscored` row parsed fine and simply lost its round, so it keeps a
        # non-null `action` with a null `executed`; the rule does not apply to it.
        if rec.get("status") != "unscored" and isinstance(rec.get("parse_ok"), bool) \
                and (rec.get("action") is None) != (not rec["parse_ok"]):
            bad("action", "action is null iff parse_ok is false (spec rule)", rec.get("action"))
        if rec.get("action") is not None and rec.get("executed") is not None:
            if (rec["action"] != rec["executed"]) and not rec.get("noise_flipped"):
                bad("executed", "differs from action but noise_flipped is false", rec.get("executed"))
        tc = rec.get("tool_calls")
        if tc is not None and not isinstance(tc, list):
            bad("tool_calls", "not a list", tc)
        elif isinstance(tc, list):
            for c in tc:
                if not isinstance(c, dict) or "name" not in c:
                    bad("tool_calls", "entry without a name", c)
                elif c.get("unlisted"):
                    # A hallucinated tool name: logged, never executed, and legal in
                    # any condition (in `absent` no tools are passed at all, and the
                    # model can still invent one).
                    continue
                elif c["name"] not in TOOLS:
                    bad("tool_calls", f"unknown tool (expected {TOOLS})", c["name"])
                elif cond == "absent":
                    bad("tool_calls", "tool call logged in condition=absent (no tools are passed)", c["name"])
        # AMBIGUITY: the spec shows label_map/option_order on every move row, but a
        # scripted agent is never shown options. Scripted rows may therefore carry
        # empty values; LLM rows must carry a consistent pair.
        # AMBIGUITY, extended: a warm-up move is chosen by the runner from
        # `assigned_state_spec.sequence`, so like a scripted agent the model is
        # never shown the options and the row carries an empty `option_order`.
        unprompted = (str(rec.get("model", "")).startswith("script:")
                      or rec.get("phase") == WARMUP_PHASE
                      or rec.get("provider") == "assigned")
        lm = rec.get("label_map")
        oo = rec.get("option_order")
        if not isinstance(lm, dict) or (set(lm) != {"C", "D"} and not (unprompted and lm == {})):
            bad("label_map", "not a dict with keys C and D", lm)
        if not isinstance(oo, list):
            bad("option_order", "not a list", oo)
        elif isinstance(lm, dict) and set(oo) != set(lm.values()) and not (unprompted and not oo):
            bad("option_order", "not a permutation of the label_map values", oo)
        if not isinstance(rec.get("decoy_calls"), int) or (isinstance(rec.get("decoy_calls"), int) and rec["decoy_calls"] < 0):
            bad("decoy_calls", "not an int >= 0", rec.get("decoy_calls"))
        if not isinstance(rec.get("retries"), int) or (isinstance(rec.get("retries"), int) and rec["retries"] < 0):
            bad("retries", "not an int >= 0", rec.get("retries"))
        # Optional (runs before 2026-09-12 have no such field).
        uc = rec.get("unlisted_calls")
        if uc is not None and (not isinstance(uc, int) or isinstance(uc, bool) or uc < 0):
            bad("unlisted_calls", "not an int >= 0", uc)

    elif kind == "game_end":
        for f in GAME_END_FIELDS:
            if f not in rec:
                bad(f, "missing required game_end field")
        if rec.get("pair_type") not in PAIR_TYPES:
            bad("pair_type", f"not one of {PAIR_TYPES}", rec.get("pair_type"))
        if rec.get("status", PLAYED_STATUS) not in GAME_STATUSES:
            bad("status", f"not one of {GAME_STATUSES}", rec.get("status"))
        # an aborted game can end before a single round was scored
        floor = 0 if rec.get("status") == "aborted" else 1
        if not isinstance(rec.get("rounds"), int) or (isinstance(rec.get("rounds"), int)
                                                      and rec["rounds"] < floor):
            bad("rounds", f"not an int >= {floor}", rec.get("rounds"))
        for f in ("coop_rate", "opp_coop_rate"):
            if not _rate_ok(rec.get(f)):
                bad(f, "not a rate in [0,1]", rec.get(f))
        if not isinstance(rec.get("channel_used"), bool):
            bad("channel_used", "not a bool", rec.get("channel_used"))
        for f in ("use_count", "decoy_count"):
            v = rec.get(f)
            if not isinstance(v, int) or isinstance(v, bool) or v < 0:
                bad(f, "not an int >= 0", v)
        if isinstance(rec.get("channel_used"), bool) and isinstance(rec.get("use_count"), int):
            if rec["channel_used"] != (rec["use_count"] > 0):
                bad("channel_used", "inconsistent with use_count", rec.get("channel_used"))
        if cond == "absent":
            if rec.get("channel_used"):
                bad("channel_used", "true in condition=absent (no tools are passed)", True)
            if rec.get("decoy_count"):
                bad("decoy_count", "non-zero in condition=absent", rec.get("decoy_count"))
        fur = rec.get("first_use_round")
        if fur is not None and (not isinstance(fur, int) or isinstance(fur, bool) or fur < 1):
            bad("first_use_round", "not null or an int >= 1", fur)
        if isinstance(rec.get("channel_used"), bool) and (fur is None) == bool(rec["channel_used"]):
            bad("first_use_round", "null iff channel_used is false", fur)
        if not isinstance(rec.get("posts"), list):
            bad("posts", "not a list", rec.get("posts"))
        if rec.get("classification_correct") not in (True, False, None):
            bad("classification_correct", "not a bool or null", rec.get("classification_correct"))
        # spec: prohibition_recall only in condition H (forbidden); null elsewhere
        if cond != "forbidden":
            if rec.get("prohibition_recall_correct") is not None or rec.get("prohibition_recall_answer") is not None:
                bad("prohibition_recall_correct", "non-null outside condition=forbidden", rec.get("prohibition_recall_correct"))
        am = rec.get("awareness_mentions")
        if not isinstance(am, dict):
            bad("awareness_mentions", "not a dict", am)

    elif kind == "generation_end":
        for f in GENERATION_END_FIELDS:
            if f not in rec:
                bad(f, "missing required generation_end field")
        pop = rec.get("population")
        if not isinstance(pop, dict) or not pop:
            bad("population", "not a non-empty dict", pop)
        else:
            for k, v in pop.items():
                if not isinstance(v, int) or isinstance(v, bool) or v < 0:
                    bad("population", f"count for {k} is not an int >= 0", v)
        cl = rec.get("climate")
        if not isinstance(cl, dict):
            bad("climate", "not a dict", cl)
        else:
            for f in ("coop_rate_overall", "coop_rate_llm_llm", "coop_rate_llm_script"):
                if f not in cl:
                    bad(f"climate.{f}", "missing")
                elif not _rate_ok(cl.get(f)):
                    bad(f"climate.{f}", "not a rate in [0,1]", cl.get(f))
            pr = cl.get("per_round")
            if not isinstance(pr, list):
                bad("climate.per_round", "not a list", pr)
            elif any(not _rate_ok(x) for x in pr):
                bad("climate.per_round", "contains a value outside [0,1]", pr[:5])
        bd = rec.get("board")
        if not isinstance(bd, dict):
            bad("board", "not a dict", bd)
        else:
            for f in ("size", "new_posts"):
                v = bd.get(f)
                if not isinstance(v, int) or isinstance(v, bool) or v < 0:
                    bad(f"board.{f}", "not an int >= 0", v)
            if not isinstance(bd.get("categories"), dict):
                bad("board.categories", "not a dict", bd.get("categories"))
        for f in ("fitness", "reproduced"):
            if not isinstance(rec.get(f), dict):
                bad(f, "not a dict", rec.get(f))
        if not isinstance(rec.get("retired"), list):
            bad("retired", "not a list", rec.get("retired"))

    return V
