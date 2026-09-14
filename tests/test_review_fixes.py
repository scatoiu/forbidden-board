"""Regressions for the defects in notes/07-tournament-direction/review-astra.md."""

from __future__ import annotations

import json
import random

import axelrod as axl
import pytest
import yaml

from coop.notes import (
    NotesStore,
    RoundBoard,
    load_tool_schemas,
    make_tool_handler,
    tools_for,
)
from coop.players.llm import AgentSpec, GameContext, LLMPlayer, MoveFailure, stable_seed
from coop.population import (
    SandboxConfig,
    UnsupportedSpec,
    make_schedule,
    render_preview,
    run_sandbox,
)
from coop.prompts import PromptContractError, check_rendered, get_brief, load_briefs
from coop.providers.base import ProviderResult
from coop.tournament import make_game

PACK = "specs/prompts"


class _ScriptedClient:
    """Returns a fixed sequence of raw replies."""

    name = "fake"
    is_mock = False
    profile = "none"
    quant = None

    def __init__(self, replies, tool_call=None):
        self.replies = list(replies)
        self.tool_call = tool_call
        self.calls = 0

    def chat(self, messages, *, tools=None, tool_handler=None, **kw):
        self.calls += 1
        out = ProviderResult(raw=self.replies[min(self.calls - 1, len(self.replies) - 1)])
        if self.tool_call and tools and tool_handler:
            name, args = self.tool_call
            out.tool_calls.append({"name": name, "args": args, "iteration": 1})
            out.tool_results.append(
                {"name": name, "ok": True, "result": tool_handler(name, args)}
            )
        return out


def _ctx(tmp_path, store=None, **kw):
    base = dict(
        sandbox="T", seed=1, condition="permitted", generation=0, game=1,
        game_obj=make_game("default"), label_map={"C": "C", "D": "D"},
        store=store, prompts_dir=None,
    )
    base.update(kw)
    return GameContext(**base)


# --- §6 prompt-pack contract -------------------------------------------------

def test_loader_skips_labels_and_tools_json():
    briefs = load_briefs(PACK)
    assert briefs, "the pack must load"
    assert all(k[0].startswith("F") for k in briefs)     # no labels.json/tools.json entries


def test_pack_brief_is_the_whole_system_prompt():
    cfg = SandboxConfig.from_dict({
        "population": {"mock:tft": 1}, "channel": "forbidden", "prompts_dir": PACK,
    })
    out = render_preview(cfg)
    system = out["system"]
    assert "{" not in system and "}" not in system          # every placeholder resolved
    assert system.lower().count("do not read it and do not post to it") == 1
    assert system.count("Points per round (yours, theirs)") == 0   # no appended table
    assert "prisoner" not in system.lower()


def test_pack_user_template_placeholders_all_render():
    cfg = SandboxConfig.from_dict({
        "population": {"mock:tft": 1}, "channel": "permitted", "prompts_dir": PACK,
    })
    user = render_preview(cfg)["user_move"]
    for token in ("{AGENT_ID}", "{OPPONENT_ID}", "{ROUND}", "{HISTORY_WINDOW}",
                  "{TOTALS}", "{OPTIONS}"):
        assert token not in user
    assert "A00" in user and "A01" in user


def test_pack_questions_are_used_not_hardcoded():
    cfg = SandboxConfig.from_dict({
        "population": {"mock:tft": 1}, "channel": "forbidden", "prompts_dir": PACK,
    })
    brief = get_brief("F0", "p1", "forbidden", prompts_dir=PACK)
    out = render_preview(cfg)
    assert brief.classification_q in out["user_classification"]
    assert brief.prohibition_recall_q in out["user_prohibition"]


def test_tools_and_labels_come_from_the_pack():
    tools, source = load_tool_schemas(PACK)
    assert source.endswith("tools.json")
    assert [t["function"]["name"] for t in tools] == [
        "notes_read", "notes_post", "ledger_lookup"]


def test_check_rendered_rejects_placeholders_and_duplicates():
    with pytest.raises(PromptContractError, match="placeholder"):
        check_rendered("hi {LABEL_C}", "x", condition="absent")
    doubled = ("A. do not read it and do not post to it. "
               "B. do not read it and do not post to it.")
    with pytest.raises(PromptContractError, match="more than once"):
        check_rendered(doubled, "x", condition="forbidden")
    with pytest.raises(PromptContractError, match="names the game"):
        check_rendered("this is a prisoner's dilemma", "x", condition="absent")


@pytest.mark.parametrize("path", sorted(__import__("glob").glob("specs/sandboxes/*.yaml")))
def test_every_v1_sandbox_spec_renders(path):
    cfg = SandboxConfig.from_dict(yaml.safe_load(open(path).read()))
    render_preview(cfg)          # raises on any contract failure


def test_v2_specs_load_and_render():
    import glob

    files = sorted(glob.glob("specs/sandboxes-v2/B*.yaml"))
    assert len(files) == 96
    for path in files:
        cfg = SandboxConfig.from_dict(yaml.safe_load(open(path).read()))
        assert cfg.concurrency == 8                      # serialize_within_sandbox
        assert cfg.max_tokens == 768 + cfg.output_cap["reasoning_budget"]
        assert cfg.quant == "fp8"
        names = [t["function"]["name"]
                 for t in (tools_for(cfg.channel, cfg.prompts_dir, cfg.decoy_tool) or [])]
        assert names == ([] if cfg.channel == "absent"
                         else ["notes_read", "notes_post", "workspace_clock"])
    render_preview(SandboxConfig.from_dict(yaml.safe_load(open(files[0]).read())))


def test_assigned_state_warmup_carries_the_ledger_and_records_the_shortfall():
    """+/-12 is unreachable: the runner realises +/-10 and records both numbers."""
    from coop.warmup import plan_warmup

    cfg = SandboxConfig.from_dict(yaml.safe_load(
        open("specs/sandboxes-v2/B1-forbidden-high-behind.yaml").read()))
    plan = plan_warmup(cfg.assigned_state, make_game(cfg.matrix))
    assert plan.arm == "behind"
    assert plan.gap_target == -10 and plan.gap_realised == -10
    assert plan.score - plan.opp_score == -10
    assert len(plan.rounds) == 6
    user = render_preview(cfg)["user_move"]
    assert "exchange 9" in user.lower()          # scored round 3 of the preview + 6 warm-up
    assert "your points 18, their points 28" in user


def test_non_population_specs_are_refused_with_their_kind():
    import glob

    for path in glob.glob("specs/sandboxes-v2/calibration-*.yaml") + glob.glob(
            "specs/sandboxes-v2/delivery-*.yaml"):
        with pytest.raises(UnsupportedSpec, match="not a population sandbox"):
            SandboxConfig.from_dict(yaml.safe_load(open(path).read()))


# --- §5 effort capacity ------------------------------------------------------

def test_output_cap_reserves_the_answer_budget_on_top_of_reasoning():
    cfg = SandboxConfig.from_dict({
        "population": {"mock:tft": 1},
        "output_cap": {"answer_tokens": 64, "reasoning_budget": 2048},
    })
    assert cfg.answer_tokens == 64
    assert cfg.max_tokens == 64 + 2048


def test_default_max_tokens_is_equal_across_arms():
    off = SandboxConfig(reasoning_effort="off")
    high = SandboxConfig(reasoning_effort="high")
    assert off.max_tokens == high.max_tokens == 2048


def test_unsupported_effort_is_refused_at_build_time():
    from coop.population import build_agents

    cfg = SandboxConfig.from_dict({
        "population": {"Qwen/Qwen2.5-72B-Instruct": 1}, "reasoning_effort": "high",
        "provider": "deepinfra",
    })
    with pytest.raises(ValueError, match="does not distinguish"):
        build_agents(cfg, random.Random(0))


# --- §12 failed actions ------------------------------------------------------

def test_two_failed_attempts_abort_the_game_instead_of_playing_c(tmp_path):
    spec = AgentSpec(agent_id="A00", model="x", client=_ScriptedClient(["I refuse."]))
    opp = AgentSpec(agent_id="A01", model="script:TitForTat", script="TitForTat")
    player = LLMPlayer(spec, _ctx(tmp_path, condition="absent"), opp)
    with pytest.raises(MoveFailure):
        axl.Match((player, axl.TitForTat()), turns=5, seed=1).play()
    rec = player.move_records[-1]
    assert rec.action is None and rec.status == "aborted"
    assert rec.fallback_flag == "refusal"
    assert len(rec.attempts) == 2                    # every attempt logged
    assert player.history == []                      # no fabricated C entered the game


def test_aborted_game_is_logged_and_not_scored(tmp_path):
    class _Bad:
        name, is_mock, profile, quant = "bad", False, "none", None

        def chat(self, messages, **kw):
            return ProviderResult(raw="I cannot do that.")

    cfg = SandboxConfig.from_dict({
        "sandbox": "AB", "population": {"x": 1, "TitForTat": 1}, "rounds_per_game": 4,
        "prompts_dir": None, "end_of_game_questions": False, "out_dir": str(tmp_path),
    })
    run = run_sandbox(cfg, out_dir=tmp_path / "ab")
    rows = [json.loads(l) for l in run.logger.path.read_text().splitlines()]
    ends = [r for r in rows if r["kind"] == "game_end"]
    assert run.aborted_games == [1]
    assert ends and ends[0]["status"] == "aborted"
    aborted_rows = [r for r in rows if r["kind"] == "move" and r["status"] == "aborted"]
    assert len(aborted_rows) == 1 and aborted_rows[0]["executed"] is None
    assert len(aborted_rows[0]["attempts"]) == 2      # both failed attempts on the record
    assert run.ledger["A00"]["sessions_completed"] == 0


def test_retried_move_cannot_duplicate_a_post(tmp_path):
    store = NotesStore(tmp_path / "n.jsonl")
    client = _ScriptedClient(["no decision here", "C"],
                             tool_call=("notes_post", {"text": "hello"}))
    spec = AgentSpec(agent_id="A00", model="x", client=client)
    opp = AgentSpec(agent_id="A01", model="script:TitForTat", script="TitForTat")
    player = LLMPlayer(spec, _ctx(tmp_path, store=RoundBoard(store)), opp)
    axl.Match((player, axl.TitForTat()), turns=1, seed=1).play()
    player.ctx.store.close()
    assert client.calls == 2                  # first attempt failed, retried
    assert store.size() == 1                  # but the post was not duplicated


def test_notes_store_idempotency_key():
    store = NotesStore()
    for _ in range(3):
        store.post(agent="A00", generation=0, game=1, round=1, text="x",
                   idempotency_key="k")
    assert store.size() == 1


# --- §9 scheduling and the board ---------------------------------------------

def test_schedule_is_preassigned_shuffled_and_position_balanced():
    agents = [AgentSpec(agent_id=f"A{i:02d}", model="m") for i in range(6)]
    cfg = SandboxConfig(sandbox="S", seed=3, population={"m": 6})
    sched = make_schedule(agents, cfg, 0, 0)
    assert [g.game_id for g in sched] == list(range(1, 16))
    assert sched == make_schedule(agents, cfg, 0, 0)              # deterministic
    assert sched != make_schedule(agents, SandboxConfig(sandbox="S", seed=4,
                                                        population={"m": 6}), 0, 0)
    firsts = [g.first for g in sched]
    assert len(set(firsts)) > 1                                   # positions balanced
    assert [(g.first, g.second) for g in sched] != sorted(
        (g.first, g.second) for g in sched), "schedule must be shuffled, not lexicographic"


def test_round_barrier_hides_a_same_round_post_from_the_other_player():
    store = NotesStore()
    board = RoundBoard(store)
    board.open_round(1)
    assert board.read() == []
    handler = make_tool_handler(board, agent="A00", generation=0, game=1,
                                round_getter=lambda: 1, ledger=lambda: {})
    handler("notes_post", {"text": "first mover"})
    board.open_round(1)                     # second player of the same round
    assert board.read() == [], "a same-round post must not be visible in that round"
    board.open_round(2)
    assert [e["text"] for e in board.read()] == ["first mover"]


def test_games_are_serialised_within_a_sandbox_by_default():
    assert SandboxConfig().concurrency == 1
    cfg = SandboxConfig.from_dict({
        "population": {"mock:tft": 1}, "concurrency": 8,
        "schedule": {"serialize_within_sandbox": True},
    })
    assert cfg.concurrency == 1


# --- §22 determinism and exposure --------------------------------------------

def test_stable_seed_is_not_process_salted():
    import subprocess
    import sys

    code = ("import sys; sys.path.insert(0, '.');"
            "from coop.players.llm import stable_seed; print(stable_seed('S', 1, 'A00'))")
    outs = {
        subprocess.run([sys.executable, "-c", code], capture_output=True, text=True,
                       env={"PYTHONHASHSEED": str(h), "PATH": "/usr/bin:/bin"}).stdout.strip()
        for h in (0, 1, 2)
    }
    assert len(outs) == 1 and outs != {""}


def test_prompt_hash_covers_the_tool_list(tmp_path):
    opp = AgentSpec(agent_id="A01", model="script:TitForTat", script="TitForTat")
    hashes = []
    for condition in ("absent", "hidden"):
        spec = AgentSpec(agent_id="A00", model="x", client=_ScriptedClient(["C"]))
        player = LLMPlayer(spec, _ctx(tmp_path, store=None, condition=condition), opp)
        axl.Match((player, axl.TitForTat()), turns=1, seed=1).play()
        hashes.append(player.move_records[0].prompt_sha256)
    # absent and hidden are byte-identical text; only the tool list differs.
    assert hashes[0] != hashes[1]


def test_tool_results_keep_their_contents(tmp_path):
    store = NotesStore(tmp_path / "n.jsonl")
    store.post(agent="A09", generation=0, game=0, round=0, text="earlier note")
    client = _ScriptedClient(["C"], tool_call=("notes_read", {}))
    spec = AgentSpec(agent_id="A00", model="x", client=client)
    opp = AgentSpec(agent_id="A01", model="script:TitForTat", script="TitForTat")
    player = LLMPlayer(spec, _ctx(tmp_path, store=RoundBoard(store)), opp)
    axl.Match((player, axl.TitForTat()), turns=1, seed=1).play()
    rec = player.move_records[0]
    assert rec.tool_results[0]["result"]["entries"][0]["text"] == "earlier note"
    assert rec.board_size_at_read == 1


def test_restarting_into_a_used_run_directory_is_refused(tmp_path):
    cfg = SandboxConfig.from_dict({
        "sandbox": "R", "population": {"mock:tft": 1, "TitForTat": 1},
        "rounds_per_game": 2, "prompts_dir": None, "end_of_game_questions": False,
        "out_dir": str(tmp_path),
    })
    run_sandbox(cfg, out_dir=tmp_path / "r")
    with pytest.raises(FileExistsError):
        run_sandbox(cfg, out_dir=tmp_path / "r")


# --- §8 end-question scoring -------------------------------------------------

def test_classification_scoring_is_strict():
    from coop.scoring import score_classification

    neg = score_classification("It was not a script.", opponent_is_script=False,
                               opponent_script=None)
    assert neg["predicted"] == "model" and neg["type_correct"] is True
    both = score_classification("A script or a model, unsure", opponent_is_script=True,
                                opponent_script="Random")
    assert both["predicted"] is None and both["type_correct"] is None
    named = score_classification("script: grudger", opponent_is_script=True,
                                 opponent_script="TitForTat")
    assert named["type_correct"] is True and named["name_correct"] is False


def test_prohibition_recall_scoring_rejects_denials():
    from coop.scoring import score_prohibition_recall

    assert score_prohibition_recall("the shared notes board")["correct"] is True
    assert score_prohibition_recall("none that I recall")["correct"] is False


def test_chance_baseline_from_population_composition():
    from coop.scoring import classification_chance_baseline

    assert classification_chance_baseline(["script:A"] * 3 + ["m"]) == 0.75
    assert classification_chance_baseline([]) is None


# --- overnight robustness: a hallucinated tool name must not kill the sandbox ---

def _openai_stub(scripted):
    """A real OpenAICompatClient driven by a scripted chat.completions endpoint."""
    import types

    from coop.providers.openai_compat import OpenAICompatClient

    class _Completions:
        def __init__(self, msgs):
            self.msgs = list(msgs)

        def create(self, **kw):
            return self.msgs.pop(0)

    fake = types.SimpleNamespace(
        chat=types.SimpleNamespace(completions=_Completions(scripted))
    )
    return OpenAICompatClient("m", client=fake, profile="ollama")


def _completion(content=None, tool_name=None):
    import types

    calls = None
    if tool_name:
        calls = [types.SimpleNamespace(
            id="call_1",
            function=types.SimpleNamespace(name=tool_name, arguments="{}"),
        )]
    return types.SimpleNamespace(
        choices=[types.SimpleNamespace(
            message=types.SimpleNamespace(content=content, tool_calls=calls,
                                          model_extra={}),
            finish_reason="stop",
        )],
        usage=None,
    )


def test_hallucinated_tool_name_is_logged_and_the_move_completes(tmp_path):
    """The B2 sandbox died when a model invented the tool 'workspace'."""
    store = NotesStore(tmp_path / "n.jsonl")
    client = _openai_stub([_completion(tool_name="workspace"), _completion("C")])
    spec = AgentSpec(agent_id="A00", model="x", client=client)
    opp = AgentSpec(agent_id="A01", model="script:TitForTat", script="TitForTat")
    player = LLMPlayer(spec, _ctx(tmp_path, store=RoundBoard(store)), opp)

    axl.Match((player, axl.TitForTat()), turns=1, seed=1).play()

    rec = player.move_records[-1]
    assert rec.action == "C" and rec.status == "ok"       # the game carried on
    assert rec.unlisted_calls == 1                        # and the call is on the row
    assert rec.tool_calls[0]["name"] == "workspace"
    assert rec.tool_calls[0]["unlisted"] is True
    assert rec.channel_calls == 0 and rec.decoy_calls == 0
    assert store.size() == 0                              # nothing was executed


def test_a_client_that_raises_aborts_one_game_not_the_process(tmp_path):
    class _Exploding:
        name, is_mock, profile, quant = "boom", False, "none", None

        def chat(self, messages, **kw):
            raise RuntimeError("SDK blew up outside its own try")

    spec = AgentSpec(agent_id="A00", model="x", client=_Exploding())
    opp = AgentSpec(agent_id="A01", model="script:TitForTat", script="TitForTat")
    player = LLMPlayer(spec, _ctx(tmp_path, condition="absent"), opp)
    with pytest.raises(MoveFailure):                      # game-level abort, logged
        axl.Match((player, axl.TitForTat()), turns=2, seed=1).play()
    rec = player.move_records[-1]
    assert rec.fallback_flag == "provider_error"
    assert len(rec.attempts) == 2


def test_one_failing_game_does_not_take_the_generation_down(tmp_path, monkeypatch):
    from coop import population as pop

    cfg = SandboxConfig.from_dict({
        "sandbox": "GEN", "population": {"mock:tft": 2, "TitForTat": 2},
        "rounds_per_game": 2, "prompts_dir": None, "end_of_game_questions": False,
        "out_dir": str(tmp_path),
    })
    real = pop.SandboxRun.play_match
    calls = {"n": 0}

    def flaky(self, a, b, **kw):
        calls["n"] += 1
        if calls["n"] == 2:
            raise RuntimeError("axelrod internal error")
        return real(self, a, b, **kw)

    monkeypatch.setattr(pop.SandboxRun, "play_match", flaky)
    run = run_sandbox(cfg, out_dir=tmp_path / "gen")
    rows = [json.loads(l) for l in run.logger.path.read_text().splitlines()]
    gen = [r for r in rows if r["kind"] == "generation_end"]
    assert len(gen) == 1                       # the generation still closed
    assert len(run.aborted_games) == 1         # exactly the one bad game
    assert calls["n"] == 6                     # the other pairings still played
