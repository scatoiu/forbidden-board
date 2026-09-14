"""Command-line entry point: `coop run --client mock:tft --population smoke ...`"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from coop.interpret import (
    characteristics_table,
    environment_volume,
    key_findings,
    matchup_ledger,
    outcomes_table,
)
from coop.notes import CONDITIONS, tools_for
from coop.players.classical import list_strategies, make_player
from coop.players.focal import FocalLLMPlayer
from coop.populations import get_population, list_populations
from coop.providers import build_client
from coop.providers.base import EFFORT_LEVELS
from coop.report import write_report
from coop.tournament import (
    PAYOFF_MATRICES,
    focal_behavioural_profile,
    focal_score_table,
    play_tournament,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="coop", description="LLM cooperation tournament harness")
    sub = parser.add_subparsers(dest="cmd", required=True)

    run = sub.add_parser("run", help="Run a tournament for one focal player")
    run.add_argument("--client", required=True,
                     help="Client spec, e.g. anthropic:claude-sonnet-4-6, "
                          "openai_compat:llama3, mock:tft")
    run.add_argument("--base-url", default=None, help="Override base URL for openai_compat")
    run.add_argument("--api-key", default=None, help="API key (else read from env)")
    run.add_argument("--temperature", type=float, default=0.2)
    run.add_argument("--framing", default="prisoners_dilemma",
                     choices=["prisoners_dilemma", "abstract"])
    run.add_argument("--cache-dir", default=".coop_cache")
    run.add_argument("--population", action="append", default=None,
                     help="Population name (repeat for several). Default: smoke")
    run.add_argument("--scenario", action="append", default=None,
                     help="Run in real-life scenario environments instead of "
                          "matrix/noise sweeps (repeat; 'all' for every scenario). "
                          "Overrides --matrix/--noise/--prob-end/--turns.")
    run.add_argument("--matrix", action="append", default=None,
                     help=f"Payoff matrix name. Choices: {sorted(PAYOFF_MATRICES)}. Default: default")
    run.add_argument("--noise", type=float, action="append", default=None,
                     help="Noise levels (repeat). Default: 0 0.01 0.05 0.10")
    run.add_argument("--turns", type=int, default=200)
    run.add_argument("--prob-end", type=float, default=0.01)
    run.add_argument("--repetitions", type=int, default=5)
    run.add_argument("--seed", type=int, default=42)
    run.add_argument("--only-focal-pairings", action="store_true",
                     help="Skip classical-vs-classical matches (faster)")
    run.add_argument("--out", default="reports", help="Report output directory")
    run.add_argument("--runs", default="runs", help="Parquet log output directory")
    run.add_argument("--label", default=None, help="Override the focal-player display name")
    run.add_argument("--verbose", action="store_true")

    classical = sub.add_parser("baseline", help="Run a classical strategy as the focal player")
    classical.add_argument("--strategy", required=True, choices=list_strategies())
    classical.add_argument("--population", action="append", default=None)
    classical.add_argument("--matrix", action="append", default=None)
    classical.add_argument("--noise", type=float, action="append", default=None)
    classical.add_argument("--turns", type=int, default=200)
    classical.add_argument("--prob-end", type=float, default=0.01)
    classical.add_argument("--repetitions", type=int, default=5)
    classical.add_argument("--seed", type=int, default=42)
    classical.add_argument("--out", default="reports")
    classical.add_argument("--runs", default="runs")

    board = sub.add_parser(
        "scoreboard",
        help="Full round-robin of classical strategies — every strategy scored per matrix",
    )
    board.add_argument("--population", default="all_classics",
                       help="Population name. Default: all_classics")
    board.add_argument("--matrix", action="append", default=None,
                       help=f"Payoff matrix name (repeat). Choices: {sorted(PAYOFF_MATRICES)}. "
                            "Default: all matrices")
    board.add_argument("--custom-matrix", action="append", default=None, metavar="NAME:R,S,T,P",
                       help="Add a custom payoff matrix, e.g. my_game:3,0,6,-2 (repeatable)")
    board.add_argument("--noise", type=float, action="append", default=None,
                       help="Noise level (repeat for a sweep). Default: 0")
    board.add_argument("--turns", type=int, default=150)
    board.add_argument("--prob-end", type=float, default=0.01)
    board.add_argument("--repetitions", type=int, default=3)
    board.add_argument("--seed", type=int, default=42)
    board.add_argument("--out", default="reports")
    board.add_argument("--runs", default="runs")
    board.add_argument("--verbose", action="store_true")

    scen = sub.add_parser(
        "scenarios",
        help="Run real-life scenario tournaments (payoffs + noise + relationship length)",
    )
    scen.add_argument("--population", default="all_classics")
    scen.add_argument("--scenario", action="append", default=None,
                      help="Scenario name (repeat). Default: all scenarios")
    scen.add_argument("--repetitions", type=int, default=3)
    scen.add_argument("--seed", type=int, default=42)
    scen.add_argument("--out", default="reports")
    scen.add_argument("--runs", default="runs")

    pop = sub.add_parser(
        "run-population",
        help="Run one sandbox: N LLM agents + scripts, a channel condition, G generations",
    )
    pop.add_argument("--config", default=None,
                     help="Path to a sandbox YAML. Flags below override its keys.")
    pop.add_argument("--sandbox", default=None)
    pop.add_argument("--population", action="append", default=None, metavar="NAME=COUNT",
                     help="Model or Axelrod strategy and how many agents (repeatable)")
    pop.add_argument("--channel", default=None, choices=list(CONDITIONS),
                     help="Channel condition (absent|permitted|forbidden|hidden)")
    pop.add_argument("--framing", default=None)
    pop.add_argument("--paraphrase", default=None)
    pop.add_argument("--reasoning-effort", dest="reasoning_effort", default=None,
                     choices=list(EFFORT_LEVELS))
    pop.add_argument("--rounds-per-game", dest="rounds_per_game", type=int, default=None)
    pop.add_argument("--prob-end", dest="prob_end", type=float, default=None)
    pop.add_argument("--generations", type=int, default=None)
    pop.add_argument("--seed", type=int, default=None)
    pop.add_argument("--provider", default=None,
                     help="Provider profile for the effort dial: ollama|openrouter|generic|none")
    pop.add_argument("--base-url", dest="base_url", default=None)
    pop.add_argument("--api-key", dest="api_key", default=None)
    pop.add_argument("--concurrency", type=int, default=None)
    pop.add_argument("--history-window", dest="history_window", type=int, default=None)
    pop.add_argument("--neutral-labels", dest="neutral_labels", action="store_true", default=None)
    pop.add_argument("--no-neutral-labels", dest="neutral_labels", action="store_false")
    pop.add_argument("--matrix", default=None)
    pop.add_argument("--noise", type=float, default=None)
    pop.add_argument("--temperature", type=float, default=None)
    pop.add_argument("--max-tokens", dest="max_tokens", type=int, default=None)
    pop.add_argument("--quant", default=None)
    pop.add_argument("--pairings", default=None,
                     help="'round_robin' or an integer k of random pairings per agent")
    pop.add_argument("--text-protocol", dest="text_protocol", action="store_true", default=None)
    pop.add_argument("--no-questions", dest="end_of_game_questions",
                     action="store_false", default=None)
    pop.add_argument("--prompts-dir", dest="prompts_dir", default=None)
    pop.add_argument("--out-dir", dest="out_dir", default=None)
    pop.add_argument("--resume-cache", dest="resume_cache", default=None)
    pop.add_argument("--only-games", dest="only_games", default=None, metavar="IDS",
                     help="Repair mode: replay ONLY these game ids (comma-separated), "
                          "with the pairing, seeds and labels the original run gave them")
    pop.add_argument("--only-games-from", dest="only_games_from", default=None,
                     metavar="MOVES_JSONL",
                     help="Repair mode: derive the ids from a previous run's moves.jsonl "
                          "— every game whose game_end says aborted and whose aborting "
                          "move row says fallback_flag=provider_error")
    pop.add_argument("--dry-run", action="store_true",
                     help="Print the resolved plan and total expected moves, run nothing")
    pop.add_argument("--verbose", action="store_true")

    sub.add_parser("list-strategies", help="List available classical strategies")
    sub.add_parser("list-populations", help="List available named populations")
    sub.add_parser("list-scenarios", help="List real-life scenarios with parameters")

    args = parser.parse_args(argv)

    if args.cmd == "list-strategies":
        for n in list_strategies():
            print(n)
        return 0
    if args.cmd == "list-populations":
        for n in list_populations():
            print(n, "->", ", ".join(get_population(n)))
        return 0
    if args.cmd == "list-scenarios":
        from coop.scenarios import SCENARIOS
        for sc in SCENARIOS.values():
            print(f"{sc.name}: (R,S,T,P)=({sc.R},{sc.S},{sc.T},{sc.P}) "
                  f"noise={sc.noise:.0%} avg_relationship={sc.avg_relationship:.0f} rounds")
            print(f"  {sc.description}")
        return 0

    if getattr(args, "verbose", False):
        logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

    if args.cmd == "run-population":
        return _cmd_run_population(args)
    if args.cmd == "run":
        return _cmd_run(args)
    if args.cmd == "baseline":
        return _cmd_baseline(args)
    if args.cmd == "scoreboard":
        return _cmd_scoreboard(args)
    if args.cmd == "scenarios":
        return _cmd_scenarios(args)
    parser.error(f"Unknown command {args.cmd!r}")
    return 2


_POP_OVERRIDES = (
    "channel", "framing", "paraphrase", "reasoning_effort", "rounds_per_game",
    "prob_end", "generations", "seed", "provider", "base_url", "api_key", "concurrency",
    "history_window", "neutral_labels", "matrix", "noise", "temperature", "max_tokens",
    "quant", "pairings", "text_protocol", "end_of_game_questions", "prompts_dir",
    "out_dir", "resume_cache",
)


def _cmd_run_population(args) -> int:
    """`coop run-population --config sandbox.yaml [overrides] [--dry-run]`."""
    import yaml

    from coop.env import load_env_file, resolve_api_key
    from coop.population import (
        SandboxConfig,
        build_agents,
        expected_moves,
        provider_error_aborts,
        render_preview,
        run_sandbox,
        source_fingerprint,
    )
    from coop.prompts import get_brief

    env_vars = load_env_file()

    data: dict = {}
    if args.config:
        loaded = yaml.safe_load(Path(args.config).read_text()) or {}
        if not isinstance(loaded, dict):
            print(f"config must be a YAML mapping, got {type(loaded).__name__}", file=sys.stderr)
            return 2
        data.update(loaded)

    for key in _POP_OVERRIDES:
        val = getattr(args, key, None)
        if val is not None:
            data[key] = val
    if args.population:
        mix: dict[str, int] = {}
        for item in args.population:
            if "=" not in item:
                print(f"--population expects NAME=COUNT, got {item!r}", file=sys.stderr)
                return 2
            name, count = item.rsplit("=", 1)
            mix[name] = int(count)
        data["population"] = mix
    if isinstance(data.get("pairings"), str) and data["pairings"].isdigit():
        data["pairings"] = int(data["pairings"])

    try:
        cfg = SandboxConfig.from_dict(data)
    except (TypeError, ValueError) as e:
        print(f"bad sandbox config: {e}", file=sys.stderr)
        return 2

    # --- repair mode ---------------------------------------------------------
    if args.only_games and args.only_games_from:
        print("pass --only-games or --only-games-from, not both", file=sys.stderr)
        return 2
    only_games: list[int] | None = None
    source: dict | None = None
    if args.only_games:
        try:
            only_games = sorted({int(tok) for tok in args.only_games.split(",") if tok.strip()})
        except ValueError:
            print(f"--only-games expects comma-separated game ids, got "
                  f"{args.only_games!r}", file=sys.stderr)
            return 2
        if not only_games:
            print("--only-games named no game ids", file=sys.stderr)
            return 2
    elif args.only_games_from:
        src = Path(args.only_games_from)
        if not src.is_file():
            print(f"--only-games-from: no such file {src}", file=sys.stderr)
            return 2
        keys = provider_error_aborts(src)
        only_games = sorted({game for _gen, game in keys})
        source = source_fingerprint(src)
        print(f"provider_error aborts in {src}: {len(keys)} game(s) "
              + (", ".join(f"g{g}/game{n}" for g, n in keys) or "none"))
        if not only_games:
            print("nothing to repair", file=sys.stderr)
            return 0

    if only_games is not None:
        cfg.repair_of = cfg.sandbox
        cfg.sandbox = args.sandbox or f"{cfg.sandbox}-repair"
    elif args.sandbox:
        cfg.sandbox = args.sandbox

    key, key_source = resolve_api_key(cfg.provider, cfg.api_key)
    cfg.api_key = key
    cfg.api_key_var = key_source

    import random as _random
    agents = build_agents(cfg, _random.Random(cfg.seed))
    brief = get_brief(cfg.framing, cfg.paraphrase, cfg.channel, prompts_dir=cfg.prompts_dir)
    tools = [t["function"]["name"] for t in (tools_for(cfg.channel) or [])]

    if args.dry_run:
        n_llm = sum(1 for a in agents if a.is_llm)
        print(f"sandbox           {cfg.sandbox}")
        print(f"condition         {cfg.channel}   tools: {tools or 'none'}")
        print(f"framing/para      {cfg.framing}/{cfg.paraphrase}   "
              f"brief: {brief.source}{' (PLACEHOLDER)' if brief.placeholder else ''}")
        print(f"effort            {cfg.reasoning_effort} via profile {cfg.provider}")
        print(f"api key           from {key_source}"
              + (f"   (.env supplied {', '.join(env_vars)})" if env_vars else ""))
        print(f"agents            {len(agents)} ({n_llm} LLM, {len(agents)-n_llm} script)")
        for a in agents:
            print(f"  {a.agent_id}  {a.model_tag}")
        print(f"pairings          {cfg.pairings}")
        print(f"rounds/game       {cfg.rounds_per_game}   prob_end={cfg.prob_end}   "
              f"noise={cfg.noise}   matrix={cfg.matrix}")
        print(f"generations       {cfg.generations}   seed={cfg.seed}   "
              f"concurrency={cfg.concurrency}")
        print(f"history window    {cfg.history_window}   "
              f"neutral_labels={cfg.neutral_labels}")
        extra = 0
        if cfg.end_of_game_questions:
            extra = 1 + (1 if cfg.channel == "forbidden" else 0)
        print(f"EXPECTED MOVES    {expected_moves(cfg, len(agents))}")
        print(f"reproduction      {cfg.reproduction}")
        print(f"max_tokens        {cfg.max_tokens} (equal in every effort arm)")
        for model, mapping in cfg.effort_mapping.items():
            note = mapping.get("collapsed") or mapping.get("notes") or ""
            print(f"  effort {model}: requested {mapping['requested']} -> "
                  f"sent {mapping['sent']}   {note}")
        try:
            preview = render_preview(cfg)
        except Exception as e:                      # contract failure: fail loudly
            print(f"\nPROMPT CONTRACT FAILED: {type(e).__name__}: {e}", file=sys.stderr)
            return 3
        print(f"\nlabels            {preview['labels']}")
        print(f"tools passed      {preview['tools']}")
        print("\n--- SYSTEM ---\n" + preview["system"])
        print("\n--- USER (move) ---\n" + preview["user_move"])
        print("\n--- USER (classification question) ---\n" + preview["user_classification"])
        if "user_prohibition" in preview:
            print("\n--- USER (prohibition-recall question) ---\n"
                  + preview["user_prohibition"])
        print(f"end-of-game calls {extra} per LLM agent per game")
        if only_games is not None:
            print(f"repair of         {cfg.repair_of}   games: "
                  + ",".join(str(g) for g in only_games))
        print(f"output            {Path(cfg.out_dir) / cfg.sandbox}")
        return 0

    try:
        run = run_sandbox(cfg, only_games=only_games, source=source)
    except ValueError as e:              # incl. UnsupportedSpec
        print(f"cannot run: {e}", file=sys.stderr)
        return 2
    if only_games is not None:
        missing = sorted(set(only_games) - set(run.selected_games))
        if missing:
            print(f"WARNING: no game with id {missing} in this spec's schedule; "
                  f"replayed {sorted(run.selected_games)}", file=sys.stderr)
        if not run.selected_games:
            return 1
    counts = run.logger.counts
    print(f"wrote {run.logger.path}")
    print("  " + "  ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    if run.store is not None:
        print(f"  board entries: {run.store.size()}")
    return 0


def _register_custom_matrices(specs: list[str] | None) -> None:
    """Parse NAME:R,S,T,P specs and inject them into PAYOFF_MATRICES."""
    for spec in specs or []:
        try:
            name, values = spec.split(":", 1)
            r, s, t, p = (float(v) for v in values.split(","))
        except ValueError:
            raise SystemExit(
                f"Bad --custom-matrix spec {spec!r}; expected NAME:R,S,T,P e.g. my_game:3,0,6,-2"
            )
        PAYOFF_MATRICES[name.strip()] = (r, s, t, p)


def _cmd_scenarios(args) -> int:
    from coop.scenarios import SCENARIOS, get_scenario, run_scenarios, scenario_table

    names = args.scenario or list(SCENARIOS)
    members = get_population(args.population)

    records = run_scenarios(
        members, scenarios=names, repetitions=args.repetitions, seed=args.seed,
    )

    runs_dir = Path(args.runs)
    runs_dir.mkdir(parents=True, exist_ok=True)
    parquet_path = runs_dir / f"scenarios_{args.population}.parquet"
    records.to_parquet(parquet_path, index=False)

    table = scenario_table(records)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / f"scenarios_{args.population}.md"
    md_lines = [
        f"# Real-life scenarios: `{args.population}` ({len(members)} strategies)\n",
        "\nMean score per turn, full round-robin per scenario, "
        f"{args.repetitions} repetitions.\n\n",
        table.to_markdown(), "\n\n## Scenario parameters\n",
    ]
    for name in names:
        sc = get_scenario(name)
        md_lines.append(
            f"\n### {sc.name}\n(R,S,T,P)=({sc.R},{sc.S},{sc.T},{sc.P}), "
            f"noise={sc.noise:.0%}, avg relationship={sc.avg_relationship:.0f} rounds.\n\n"
            f"{sc.rationale}\n"
        )
    md_path.write_text("".join(md_lines))

    print(f"Scenarios complete: {len(records)} participations recorded.")
    print(f"  parquet: {parquet_path}")
    print(f"  report:  {md_path}")
    print()
    print(table.to_string())
    return 0


def _cmd_scoreboard(args) -> int:
    from coop.tournament import play_scoreboard, scoreboard_table

    _register_custom_matrices(args.custom_matrix)
    matrices = args.matrix or list(PAYOFF_MATRICES)
    noise_levels = args.noise if args.noise is not None else [0.0]
    members = get_population(args.population)

    import pandas as pd

    frames = []
    for noise in noise_levels:
        frames.append(play_scoreboard(
            members,
            matrices=matrices,
            noise=noise,
            turns=args.turns,
            prob_end=args.prob_end,
            repetitions=args.repetitions,
            seed=args.seed,
        ))
    records = pd.concat(frames, ignore_index=True)

    runs_dir = Path(args.runs)
    runs_dir.mkdir(parents=True, exist_ok=True)
    parquet_path = runs_dir / f"scoreboard_{args.population}.parquet"
    records.to_parquet(parquet_path, index=False)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / f"scoreboard_{args.population}.md"

    md_lines = [
        f"# Scoreboard: `{args.population}` ({len(members)} strategies)\n",
        f"\nMean score per turn, full round-robin, noise levels {noise_levels}, "
        f"{args.repetitions} repetitions, {args.turns} turns (prob_end={args.prob_end}).\n",
    ]

    print(f"Scoreboard complete: {len(records)} participations recorded.")
    print(f"  parquet: {parquet_path}")

    if len(noise_levels) > 1:
        # Noise-sweep view first: strategy × noise, averaged over matrices.
        noise_table = scoreboard_table(records, columns="noise")
        md_lines += ["\n## Strategy × noise (mean over matrices)\n\n",
                     noise_table.to_markdown(), "\n"]
        print("\nStrategy × noise (mean score/turn over all matrices):\n")
        print(noise_table.to_string())

    for noise in noise_levels:
        table = scoreboard_table(records[records["noise"] == noise])
        md_lines += [f"\n## Strategy × matrix at noise={noise}\n\n", table.to_markdown(), "\n"]
        if len(noise_levels) == 1:
            print()
            print(table.to_string())

    md_lines += [
        "\nMatrices (R,S,T,P): "
        + "; ".join(f"`{m}`={PAYOFF_MATRICES[m]}" for m in matrices)
        + "\n",
    ]
    md_path.write_text("".join(md_lines))
    print(f"  report:  {md_path}")
    return 0


def _cmd_run(args) -> int:
    populations = args.population or ["smoke"]
    matrices = args.matrix or ["default"]
    noise = args.noise if args.noise is not None else [0.0]

    client_kwargs = {}
    if args.base_url:
        client_kwargs["base_url"] = args.base_url
    if args.api_key:
        client_kwargs["api_key"] = args.api_key
    client = build_client(args.client, **client_kwargs)

    cache_dir = Path(args.cache_dir) if args.cache_dir else None
    if cache_dir:
        cache_dir.mkdir(parents=True, exist_ok=True)

    focal_name = args.label or f"LLM[{client.name}]"

    # Collect reasoning across every fresh LLMPlayer the factory produces, so the
    # report can show samples even though we throw players away each repetition.
    reasoning_log: list = []

    def factory():
        player = FocalLLMPlayer(
            client=client,
            framing=args.framing,
            temperature=args.temperature,
            cache_dir=str(cache_dir) if cache_dir else None,
        )
        # Mutate the player's log to be a shared list reference so we capture
        # reasoning produced after this point. Player appends to this list directly.
        player.reasoning_log = reasoning_log
        return player

    if args.scenario:
        # Scenario mode: each scenario supplies its own matrix, noise, and
        # relationship length. The population supplies the opponents.
        from coop.scenarios import SCENARIOS, run_focal_scenarios

        scenario_names = (
            list(SCENARIOS) if args.scenario == ["all"] else args.scenario
        )
        members = get_population(populations[0] if args.population else "all_classics")
        run_obj = run_focal_scenarios(
            focal_factory=factory,
            focal_name=focal_name,
            members=members,
            scenarios=scenario_names,
            repetitions=args.repetitions,
            seed=args.seed,
            only_focal_pairings=args.only_focal_pairings,
            progress=args.verbose,
        )
    else:
        run_obj = play_tournament(
            focal_factory=factory,
            focal_name=focal_name,
            population_names=populations,
            population_lookup=get_population,
            matrices=matrices,
            noise_levels=noise,
            turns=args.turns,
            prob_end=args.prob_end,
            repetitions=args.repetitions,
            seed=args.seed,
            only_focal_pairings=args.only_focal_pairings,
            progress=args.verbose,
        )

    runs_dir = Path(args.runs)
    runs_dir.mkdir(parents=True, exist_ok=True)
    parquet_path = runs_dir / f"{_slug(focal_name)}.parquet"
    run_obj.save_parquet(parquet_path)

    paths = write_report(run_obj, out_dir=args.out, reasoning_log=reasoning_log)
    print(f"Tournament complete: {len(run_obj.matches)} matches.")
    print(f"  parquet: {parquet_path}")
    print(f"  report:  {paths.markdown}")
    _print_summary(run_obj, focal_name)
    return 0


def _cmd_baseline(args) -> int:
    populations = args.population or ["smoke"]
    matrices = args.matrix or ["default"]
    noise = args.noise if args.noise is not None else [0.0]

    def factory():
        return make_player(args.strategy)

    run_obj = play_tournament(
        focal_factory=factory,
        focal_name=args.strategy,
        population_names=populations,
        population_lookup=get_population,
        matrices=matrices,
        noise_levels=noise,
        turns=args.turns,
        prob_end=args.prob_end,
        repetitions=args.repetitions,
        seed=args.seed,
        only_focal_pairings=False,
        progress=False,
    )
    runs_dir = Path(args.runs)
    runs_dir.mkdir(parents=True, exist_ok=True)
    run_obj.save_parquet(runs_dir / f"baseline_{_slug(args.strategy)}.parquet")
    paths = write_report(run_obj, out_dir=args.out)
    print(f"Baseline complete: {len(run_obj.matches)} matches.")
    print(f"  report: {paths.markdown}")
    _print_summary(run_obj, args.strategy)
    return 0


def _print_summary(run_obj, focal_name: str) -> None:
    """Print a plain-English summary of the tournament to stdout."""
    score_table = focal_score_table(run_obj)
    profile = focal_behavioural_profile(run_obj, by=("population",))
    profile_by_noise = focal_behavioural_profile(run_obj, by=("population", "noise"))
    matches_df = run_obj.to_frame()

    if score_table.empty or profile.empty:
        return

    print()
    print("=" * 78)
    print(f"  {focal_name} — plain-English summary")
    print("=" * 78)

    print("\nBehavioural characteristics (per population, averaged over noise/matrix):\n")
    print(characteristics_table(profile).to_string(index=False))

    volume = environment_volume(matches_df)
    print("\nOutcomes by environment (competitors = distinct opponent strategies met):\n")
    print(outcomes_table(score_table, volume=volume).to_string(index=False))

    print("\nMatchup ledger (per opponent strategy, summed across the whole sweep):\n")
    print(matchup_ledger(matches_df).to_string(index=False))

    bullets = key_findings(
        score_table=score_table,
        profile_by_population=profile,
        profile_by_pop_noise=profile_by_noise,
        focal_name=focal_name,
    )
    if bullets:
        print("\nKey findings:")
        import re
        bold_pat = re.compile(r"\*\*([^*]+)\*\*")
        for b in bullets:
            print("  - " + bold_pat.sub(r"\1", b))
    print()


def _slug(s: str) -> str:
    return "".join(c if c.isalnum() or c in "._-" else "_" for c in s).strip("_")


if __name__ == "__main__":
    sys.exit(main())
