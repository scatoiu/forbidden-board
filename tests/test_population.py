"""Scripted-mock population sanity check (harness-effects §5.4 (1)) and runner tests.

Every rate here is exact and known in advance: no LLM is called.
"""

from __future__ import annotations

import json
import random
from collections import defaultdict

import pytest

from coop.generations import resample
from coop.notes import NotesStore, tools_for
from coop.players.llm import AgentSpec, ResumeCache
from coop.population import (
    SandboxConfig,
    SandboxRun,
    build_agents,
    expected_moves,
    make_pairings,
    normalise_config,
    run_sandbox,
)
from coop.providers.base import ProviderResult, UnlistedToolCall

ROUNDS = 20
DEFECTORS = {"mock:defector", "script:AlwaysDefect"}
COOPERATORS = {"mock:cooperator", "script:AlwaysCooperate"}
TFTS = {"mock:tft", "script:TitForTat", "mock:poster", "mock:decoy"}

MIXED = {
    "mock:tft": 1, "mock:cooperator": 1, "mock:defector": 1,
    "TitForTat": 1, "AlwaysCooperate": 1, "AlwaysDefect": 1,
}


def _cfg(tmp_path, **kw) -> SandboxConfig:
    base = dict(
        sandbox="TST", population=dict(MIXED), channel="absent",
        rounds_per_game=ROUNDS, generations=1, seed=11, concurrency=1,
        prompts_dir=None, end_of_game_questions=False, out_dir=str(tmp_path),
    )
    base.update(kw)
    return SandboxConfig.from_dict(base)


def _rows(run):
    return [json.loads(line) for line in run.logger.path.read_text().splitlines()]


def _coop_by_game_agent(rows):
    """(game, agent) -> (model, opponent_model, coop rate over parsed moves)."""
    acc: dict[tuple[int, str], list] = defaultdict(lambda: ["", "", 0, 0])
    for r in rows:
        if r["kind"] != "move" or not r["parse_ok"]:
            continue
        key = (r["game"], r["agent"])
        acc[key][0] = r["model"]
        acc[key][1] = r["opponent_model"]
        acc[key][2] += 1 if r["action"] == "C" else 0
        acc[key][3] += 1
    return {k: (v[0], v[1], v[2] / v[3]) for k, v in acc.items()}


def _expected(mine: str, theirs: str, n: int) -> float:
    if mine in DEFECTORS:
        return 0.0
    if mine in COOPERATORS:
        return 1.0
    if theirs in DEFECTORS:      # TFT retaliates from round 2
        return 1.0 / n
    return 1.0


# --------------------------------------------------------------------------
# §5.4 (1): the scripted-mock population with known answers
# --------------------------------------------------------------------------

def test_scripted_mock_population_hits_exact_rates(tmp_path):
    run = run_sandbox(_cfg(tmp_path), out_dir=tmp_path / "TST")
    rows = _rows(run)
    table = _coop_by_game_agent(rows)

    assert len(table) == 2 * (6 * 5 // 2)          # both sides of every pairing
    for (game, agent), (model, opp_model, rate) in table.items():
        assert model in DEFECTORS | COOPERATORS | TFTS, model
        assert rate == pytest.approx(_expected(model, opp_model, ROUNDS)), (
            f"game {game} agent {agent} ({model} vs {opp_model})"
        )


def test_tft_vs_defector_and_cooperator_vs_tft_named_explicitly(tmp_path):
    run = run_sandbox(_cfg(tmp_path), out_dir=tmp_path / "TST")
    table = _coop_by_game_agent(_rows(run))
    seen = set()
    for (_, _), (model, opp_model, rate) in table.items():
        if model in TFTS and opp_model in DEFECTORS:
            assert rate == pytest.approx(1 / ROUNDS)
            seen.add("tft_vs_defector")
        if model in COOPERATORS and opp_model in TFTS:
            assert rate == 1.0
            seen.add("cooperator_vs_tft")
        if model in DEFECTORS:
            assert rate == 0.0
            seen.add("defector_vs_anything")
    assert seen == {"tft_vs_defector", "cooperator_vs_tft", "defector_vs_anything"}


def test_jsonl_move_rows_equal_expected_moves(tmp_path):
    cfg = _cfg(tmp_path)
    run = run_sandbox(cfg, out_dir=tmp_path / "TST")
    rows = _rows(run)
    moves = [r for r in rows if r["kind"] == "move"]
    assert len(moves) == expected_moves(cfg, len(run.agents)) == 15 * ROUNDS * 2
    assert run.logger.counts["move"] == len(moves)
    assert sum(1 for r in rows if r["kind"] == "generation_end") == 1
    assert all(r["parse_ok"] for r in moves)


@pytest.mark.parametrize("condition", ["permitted", "forbidden", "hidden"])
def test_poster_uses_channel_on_every_move_and_board_equals_posts(tmp_path, condition):
    cfg = _cfg(tmp_path, population={"mock:poster": 1, "TitForTat": 1, "AlwaysDefect": 1},
               channel=condition, sandbox=f"P_{condition}")
    run = run_sandbox(cfg, out_dir=tmp_path / condition)
    moves = [r for r in _rows(run) if r["kind"] == "move"]
    poster = [m for m in moves if m["model"] == "mock:poster"]

    assert len(poster) == 2 * ROUNDS                      # two pairings
    assert all(m["channel_calls"] == 1 for m in poster)   # 100% use rate
    assert all(m["tool_calls"][0]["name"] == "notes_post" for m in poster)
    assert run.store.size() == len(poster)                # board size == posts
    assert all(m["decoy_calls"] == 0 for m in poster)


def test_poster_fails_loudly_when_no_tools_are_listed(tmp_path):
    cfg = _cfg(tmp_path, population={"mock:poster": 1, "TitForTat": 1}, channel="absent")
    with pytest.raises(UnlistedToolCall):
        run_sandbox(cfg, out_dir=tmp_path / "absent")


def test_decoy_calls_are_counted_separately(tmp_path):
    cfg = _cfg(tmp_path, population={"mock:decoy": 1, "TitForTat": 1}, channel="permitted")
    run = run_sandbox(cfg, out_dir=tmp_path / "decoy")
    decoy = [r for r in _rows(run) if r["kind"] == "move" and r["model"] == "mock:decoy"]
    assert all(m["decoy_calls"] == 1 and m["channel_calls"] == 0 for m in decoy)
    assert run.store.size() == 0


def test_game_end_rows_carry_the_schema_fields(tmp_path):
    cfg = _cfg(tmp_path, population={"mock:poster": 1, "AlwaysDefect": 1},
               channel="forbidden", end_of_game_questions=True)
    run = run_sandbox(cfg, out_dir=tmp_path / "ge")
    ends = [r for r in _rows(run) if r["kind"] == "game_end"]
    assert len(ends) == 1                                  # one LLM agent, one pairing
    end = ends[0]
    assert end["channel_used"] is True
    assert end["first_use_round"] == 1
    assert end["use_count"] == ROUNDS
    assert end["coop_rate"] == pytest.approx(1 / ROUNDS)
    assert end["prohibition_recall_answer"] is not None     # asked only in forbidden
    assert set(end["awareness_mentions"]) == {"test", "experiment", "evaluation", "researcher"}


# --------------------------------------------------------------------------
# Nuisance controls (harness-effects §5.1 / §5.2)
# --------------------------------------------------------------------------

def test_serial_ids_do_not_encode_model(tmp_path):
    cfg = _cfg(tmp_path, population={"mock:tft": 4, "TitForTat": 4})
    orders = set()
    for seed in range(6):
        agents = build_agents(SandboxConfig.from_dict({**cfg.as_dict(), "seed": seed}),
                              random.Random(seed))
        assert [a.agent_id for a in agents] == [f"A{i:02d}" for i in range(8)]
        orders.add(tuple(a.model_tag for a in agents))
    assert len(orders) > 1, "model order must be shuffled before IDs are assigned"


def test_label_map_and_option_order_are_logged(tmp_path):
    run = run_sandbox(_cfg(tmp_path, neutral_labels=True), out_dir=tmp_path / "labels")
    moves = [r for r in _rows(run) if r["kind"] == "move"]
    per_game = {m["game"]: tuple(sorted(m["label_map"].items())) for m in moves}
    assert len(set(per_game.values())) >= 2, "labels are drawn per game"
    llm = [m for m in moves if not m["model"].startswith("script:")]
    for m in llm:
        assert set(m["option_order"]) == set(m["label_map"].values())
    for m in moves:
        assert m["action"] in ("C", "D")           # canonical, never the neutral letter
    assert not any(m["option_order"] for m in moves if m["model"].startswith("script:")), (
        "scripts are never shown options"
    )
    by_game: dict[int, set] = defaultdict(set)
    for m in llm:
        by_game[m["game"]].add(tuple(m["option_order"]))
    assert any(len(v) == 2 for v in by_game.values()), "option order randomised per move"


def test_no_prompt_cache_by_default_and_resume_cache_keys_on_identity():
    k1 = ResumeCache.key(agent_id="A01", game=1, round=3, seed=5, prompt="p")
    assert k1 != ResumeCache.key(agent_id="A02", game=1, round=3, seed=5, prompt="p")
    assert k1 != ResumeCache.key(agent_id="A01", game=2, round=3, seed=5, prompt="p")
    assert k1 != ResumeCache.key(agent_id="A01", game=1, round=4, seed=5, prompt="p")
    assert k1 != ResumeCache.key(agent_id="A01", game=1, round=3, seed=6, prompt="p")
    assert SandboxConfig().resume_cache is None


def test_tools_listed_only_outside_absent():
    assert tools_for("absent") is None
    for cond in ("permitted", "forbidden", "hidden"):
        names = [t["function"]["name"] for t in tools_for(cond)]
        assert names == ["notes_read", "notes_post", "ledger_lookup"]


# --------------------------------------------------------------------------
# Generations
# --------------------------------------------------------------------------

def test_board_and_lineage_persist_across_generations(tmp_path):
    cfg = _cfg(tmp_path, population={"mock:poster": 2, "AlwaysDefect": 1},
               channel="permitted", generations=3, rounds_per_game=4,
               reproduction={"rule": "wright_fisher", "fitness": "mean_per_move"})
    run = run_sandbox(cfg, out_dir=tmp_path / "gens")
    rows = _rows(run)
    gens = [r for r in rows if r["kind"] == "generation_end"]
    assert len(gens) == 3
    assert [g["board"]["size"] for g in gens] == sorted(g["board"]["size"] for g in gens)
    assert sum(g["board"]["new_posts"] for g in gens) == run.store.size()
    assert gens[0]["reproduced"] and gens[-1]["reproduced"] == {}
    assert all(g["reproduction"]["rule"] == "wright_fisher" for g in gens)
    children = [r for r in rows if r["kind"] == "move" and r["generation"] == 1]
    assert all(c["parent"] is not None for c in children)
    assert all(c["lineage"].startswith("A") for c in children)


def test_resample_is_fitness_proportional_and_heritable():
    agents = [
        AgentSpec(agent_id="A00", model="m", client=object()),
        AgentSpec(agent_id="A01", model="script:TitForTat", script="TitForTat"),
    ]
    children, counts, retired = resample(
        agents, {"A00": 5.0, "A01": 0.0}, random.Random(0), start_index=2,
    )
    assert len(children) == 2
    assert counts == {"A00": 2, "A01": 0}
    assert retired == ["A01"]
    assert all(c.model == "m" and c.script is None for c in children)
    assert [c.agent_id for c in children] == ["A02", "A03"]
    assert all(c.parent == "A00" and c.lineage == "A00" for c in children)


def test_reproduction_none_keeps_the_population_fixed(tmp_path):
    """The default for confirmatory sandboxes: generations are repeats, not selection."""
    cfg = _cfg(tmp_path, population={"mock:tft": 2, "AlwaysDefect": 1},
               generations=2, rounds_per_game=3)
    assert cfg.reproduction == {"rule": "none", "fitness": "mean_per_move"}
    run = run_sandbox(cfg, out_dir=tmp_path / "fixed")
    rows = _rows(run)
    gens = [r for r in rows if r["kind"] == "generation_end"]
    assert all(g["retired"] == [] for g in gens)
    assert {r["agent"] for r in rows if r["kind"] == "move"} == {"A00", "A01", "A02"}
    assert all(r["parent"] is None for r in rows if r["kind"] == "move")


def test_moran_step_is_one_birth_and_one_death():
    from coop.generations import moran_step

    agents = [AgentSpec(agent_id=f"A0{i}", model="m") for i in range(4)]
    survivors, counts, retired = moran_step(
        agents, {"A00": 9.0, "A01": 1.0, "A02": 1.0, "A03": 0.1},
        random.Random(0), start_index=4,
    )
    assert len(survivors) == 4 and len(retired) == 1
    assert sum(counts.values()) == 4
    assert sum(1 for s in survivors if s.parent is not None) == 1


def test_fitness_rule_total_versus_mean_per_move(tmp_path):
    cfg = _cfg(tmp_path, population={"mock:cooperator": 1, "AlwaysDefect": 1},
               rounds_per_game=5,
               reproduction={"rule": "wright_fisher", "fitness": "total"})
    run = run_sandbox(cfg, out_dir=tmp_path / "fit")
    gen = [r for r in _rows(run) if r["kind"] == "generation_end"][0]
    # AlwaysDefect exploits AlwaysCooperate for 5 rounds at T=5.
    assert gen["fitness"]["A00"] + gen["fitness"]["A01"] == 25.0


def test_resample_falls_back_to_uniform_on_all_zero_fitness():
    agents = [AgentSpec(agent_id=f"A0{i}", model="m") for i in range(4)]
    children, counts, _ = resample(agents, {}, random.Random(1), start_index=4)
    assert len(children) == 4 and sum(counts.values()) == 4


# --------------------------------------------------------------------------
# Config plumbing
# --------------------------------------------------------------------------

def test_normalise_accepts_the_sandbox_spec_shape():
    data = normalise_config({
        "sandbox": "S01",
        "population": {"llm": {"qwen3:8b": 2}, "scripts": {"TitForTat": 1}, "total_agents": 3},
        "neutral_labels": {"enabled": False, "draw": "per_game"},
        "provider": "hosted", "prob_end": 0.0, "notes": "ignored",
    })
    assert data["population"] == {"qwen3:8b": 2, "TitForTat": 1}
    assert data["neutral_labels"] is False
    assert data["provider"] == "deepinfra"
    assert data["prob_end"] is None
    assert "notes" not in data


def test_total_agents_mismatch_is_rejected():
    with pytest.raises(ValueError, match="total_agents"):
        normalise_config({"population": {"llm": {"m": 2}, "total_agents": 5}})


def test_unknown_condition_rejected():
    with pytest.raises(ValueError, match="channel"):
        SandboxConfig.from_dict({"population": {"mock:tft": 1}, "channel": "secret"})


def test_pairings_round_robin_and_k_random():
    agents = [AgentSpec(agent_id=f"A{i:02d}", model="m") for i in range(6)]
    cfg = SandboxConfig(population={"m": 6})
    assert len(make_pairings(agents, cfg, random.Random(0))) == 15
    cfg.pairings = 2
    pairs = make_pairings(agents, cfg, random.Random(0))
    assert 6 <= len(pairs) <= 12
    assert all(i < j for i, j in pairs)


# --------------------------------------------------------------------------
# Text-protocol fallback
# --------------------------------------------------------------------------

class _TextProtocolClient:
    """A model that cannot tool-call and uses the NOTES_POST: line instead."""

    name = "fake:text"
    is_mock = False
    profile = "none"
    quant = None

    def chat(self, messages, **kw):
        return ProviderResult(raw="NOTES_READ\nNOTES_POST: agent here, I cooperate\nC")


def test_text_protocol_executes_notes_lines(tmp_path):
    store = NotesStore(tmp_path / "notes.jsonl")
    cfg = SandboxConfig.from_dict({
        "population": {"x": 1}, "channel": "permitted", "rounds_per_game": 3,
        "text_protocol": True, "prompts_dir": None, "end_of_game_questions": False,
        "neutral_labels": False, "out_dir": str(tmp_path), "concurrency": 1,
    })
    from coop.players.llm import GameContext, LLMPlayer
    from coop.tournament import make_game
    import axelrod as axl

    spec = AgentSpec(agent_id="A00", model="x", client=_TextProtocolClient())
    opp = AgentSpec(agent_id="A01", model="script:TitForTat", script="TitForTat")
    ctx = GameContext(sandbox="T", seed=1, condition="permitted", generation=0, game=1,
                      game_obj=make_game("default"), label_map={"C": "C", "D": "D"},
                      store=store, text_protocol=True, prompts_dir=None)
    player = LLMPlayer(spec, ctx, opp)
    axl.Match((player, axl.TitForTat()), turns=3, seed=1).play()

    assert store.size() == 3
    assert store.texts()[0] == "agent here, I cooperate"
    rec = player.move_records[0]
    assert [c["name"] for c in rec.tool_calls] == ["notes_read", "notes_post"]
    assert rec.read_before_post is True
    assert rec.action == "C" and rec.parse_ok


def test_text_protocol_cannot_implement_the_hidden_condition():
    from coop.prompts import text_protocol_block
    with pytest.raises(ValueError, match="hidden"):
        text_protocol_block("hidden")


# --------------------------------------------------------------------------
# .env and API-key resolution (values never logged, only variable names)
# --------------------------------------------------------------------------

def test_env_file_does_not_override_the_environment(tmp_path, monkeypatch):
    from coop.env import load_env_file

    monkeypatch.setenv("DEEPINFRA_API_KEY", "already-set")
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    f = tmp_path / ".env"
    f.write_text("# comment\n\nDEEPINFRA_API_KEY=from-file\nOPENROUTER_API_KEY='or-key'\n")
    assert load_env_file(f) == ["OPENROUTER_API_KEY"]
    import os
    assert os.environ["DEEPINFRA_API_KEY"] == "already-set"
    assert os.environ["OPENROUTER_API_KEY"] == "or-key"


def test_api_key_resolution_order(monkeypatch):
    from coop.env import resolve_api_key

    monkeypatch.setenv("DEEPINFRA_API_KEY", "di")
    monkeypatch.setenv("OPENROUTER_API_KEY", "or")
    monkeypatch.setenv("OPENAI_API_KEY", "oa")
    assert resolve_api_key("generic", "explicit") == ("explicit", "--api-key")
    assert resolve_api_key("generic") == ("di", "DEEPINFRA_API_KEY")
    assert resolve_api_key("openrouter") == ("or", "OPENROUTER_API_KEY")
    monkeypatch.delenv("DEEPINFRA_API_KEY")
    assert resolve_api_key("generic") == ("oa", "OPENAI_API_KEY")
    monkeypatch.delenv("OPENAI_API_KEY")
    assert resolve_api_key("generic") == (None, "none")


def test_manifest_never_contains_the_key_value(tmp_path):
    cfg = _cfg(tmp_path, population={"mock:tft": 1, "TitForTat": 1}, rounds_per_game=2)
    cfg.api_key = "sk-super-secret"
    cfg.api_key_var = "DEEPINFRA_API_KEY"
    run = run_sandbox(cfg, out_dir=tmp_path / "manifest")
    text = (run.out / "manifest.json").read_text()
    assert "sk-super-secret" not in text
    assert "DEEPINFRA_API_KEY" in text
    manifest = json.loads(text)
    assert manifest["config"]["api_key"] == "<redacted>"
    assert manifest["config_sha256"] and manifest["git_sha"]
    assert manifest["expected_moves"] == 2 * 2


# --------------------------------------------------------------------------
# Board read limit and end-of-game question spend (review-astra §3/§14)
# --------------------------------------------------------------------------

def test_board_read_limit_is_config_reaches_the_game_and_is_on_the_manifest(
        tmp_path, monkeypatch):
    from coop import population as pop

    seen: list[dict] = []
    real = pop.GameContext

    def spy(**kw):
        seen.append(kw)
        return real(**kw)

    monkeypatch.setattr(pop, "GameContext", spy)
    cfg = _cfg(tmp_path, population={"mock:tft": 1, "TitForTat": 1},
               rounds_per_game=2, board_read_limit=5)
    assert cfg.board_read_limit == 5                      # loaded like any other key
    run = run_sandbox(cfg, out_dir=tmp_path / "brl")

    assert seen and all(kw["board_read_limit"] == 5 for kw in seen)
    manifest = json.loads((run.out / "manifest.json").read_text())
    assert manifest["board_read_limit"] == 5
    assert manifest["max_tool_iterations"] == cfg.max_tool_iterations
    assert manifest["config"]["board_read_limit"] == 5


def test_board_read_limit_defaults_to_twenty():
    assert SandboxConfig(population={"mock:tft": 1}).board_read_limit == 20


class _UsageClient:
    """A mock client that also prices its completions, and fails every question."""

    name, is_mock, profile, quant = "usage-mock", True, "none", None

    def __init__(self, inner):
        self.inner = inner

    def chat(self, messages, *, tools=None, tool_handler=None, **kw):
        out = self.inner.chat(messages, tools=tools, tool_handler=tool_handler, **kw)
        out.usage = [{"iteration": 1, "prompt_tokens": 10, "completion_tokens": 2,
                      "reasoning_tokens": 0, "estimated_cost": 0.001}]
        if tools is None:                 # `_ask` never passes tools: a question turn
            out.error = "Timeout: read timed out"
        return out


def test_question_usage_and_errors_land_on_the_game_end_row(tmp_path):
    """A discarded ProviderResult hid both the question spend and its failures."""
    cfg = _cfg(tmp_path, population={"mock:tft": 1, "AlwaysDefect": 1},
               channel="forbidden", end_of_game_questions=True, rounds_per_game=2)
    run = SandboxRun(cfg, out_dir=tmp_path / "q")
    for a in run.agents:
        if a.is_llm:
            a.client = _UsageClient(a.client)
    run.play_generation(0)
    run.close()

    ends = [r for r in _rows(run) if r["kind"] == "game_end"]
    assert len(ends) == 1
    end = ends[0]
    # forbidden asks both questions, so both completions are on the record
    assert len(end["question_usage"]) == 2
    assert all(set(u) >= {"iteration", "prompt_tokens", "completion_tokens",
                          "reasoning_tokens", "estimated_cost"}
               for u in end["question_usage"])
    assert end["question_errors"] == ["Timeout: read timed out"] * 2


def test_a_game_without_questions_still_carries_the_empty_usage_fields(tmp_path):
    cfg = _cfg(tmp_path, population={"mock:tft": 1, "TitForTat": 1}, rounds_per_game=2)
    run = run_sandbox(cfg, out_dir=tmp_path / "noq")
    ends = [r for r in _rows(run) if r["kind"] == "game_end"]
    assert ends and all(e["question_usage"] == [] and e["question_errors"] == []
                        for e in ends)
    assert all(e["error"] is None for e in ends)
