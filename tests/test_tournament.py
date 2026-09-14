"""End-to-end tournament smoke tests."""

from __future__ import annotations

from pathlib import Path

from coop.players.classical import make_player
from coop.players.focal import FocalLLMPlayer
from coop.populations import get_population
from coop.providers.mock import MockClient
from coop.report import write_report
from coop.tournament import (
    PAYOFF_MATRICES,
    focal_behavioural_profile,
    focal_score_table,
    play_tournament,
)


def test_smoke_tournament_with_mock_tft(tmp_path):
    def factory():
        return FocalLLMPlayer(client=MockClient("tft"), capture_reasoning=False)

    run = play_tournament(
        focal_factory=factory,
        focal_name="MockTFT",
        population_names=["smoke"],
        population_lookup=get_population,
        matrices=["default"],
        noise_levels=[0.0, 0.05],
        turns=40,
        prob_end=0.0,
        repetitions=2,
        seed=1,
        only_focal_pairings=True,
    )
    assert len(run.matches) > 0
    df = run.to_frame()
    # Two noise levels × one matrix × one population × 5 opponents × 2 reps = 20 focal pairings,
    # plus 2 self-play (one per noise) — actual count depends on whether we include self-play.
    # Just check we have records on both noise levels and the focal player participated.
    assert set(df["noise"].unique()) == {0.0, 0.05}
    assert df["is_focal_a"].sum() + df["is_focal_b"].sum() > 0


def test_focal_score_table_and_profile_run_through(tmp_path):
    def factory():
        return FocalLLMPlayer(client=MockClient("tft"), capture_reasoning=False)

    run = play_tournament(
        focal_factory=factory,
        focal_name="MockTFT",
        population_names=["smoke"],
        population_lookup=get_population,
        matrices=["default"],
        noise_levels=[0.0],
        turns=50,
        prob_end=0.0,
        repetitions=1,
        seed=1,
        only_focal_pairings=True,
    )
    score = focal_score_table(run)
    assert not score.empty
    assert "score_per_turn" in score.columns

    profile = focal_behavioural_profile(run, by=("population",))
    assert not profile.empty
    assert {"vengefulness", "reactiveness", "past_focus"}.issubset(profile.columns)


def test_report_renders_markdown_and_pngs(tmp_path):
    def factory():
        return FocalLLMPlayer(client=MockClient("tft"), capture_reasoning=True)

    run = play_tournament(
        focal_factory=factory,
        focal_name="MockTFT",
        population_names=["smoke"],
        population_lookup=get_population,
        matrices=["default"],
        noise_levels=[0.0],
        turns=40,
        prob_end=0.0,
        repetitions=1,
        seed=1,
        only_focal_pairings=True,
    )
    paths = write_report(run, out_dir=tmp_path)
    assert paths.markdown.exists()
    assert paths.radar_png.exists()
    assert paths.drift_png.exists()
    md = paths.markdown.read_text()
    assert "Cooperation tournament report" in md
    assert "Behavioural fingerprint" in md
    assert "Drift map" not in md  # we removed that title; just heatmap is rendered


def test_payoff_matrices_satisfy_pd_constraint():
    """Strict-PD matrices keep the canonical ordering; the experimental matrices
    deliberately bend it (high_temptation/brutal_world break 2R>T+S, cheap_forgiveness
    breaks P>S to make a snowdrift-style game, punishing_defection sends P negative)."""
    strict_pd = ["default", "high_temptation", "low_temptation", "stag_hunt", "brutal_world"]
    for name in strict_pd:
        R, S, T, P = PAYOFF_MATRICES[name]
        assert T > R > P > S, f"{name}: T>R>P>S violated"
    for name in ["default", "low_temptation", "stag_hunt"]:
        R, S, T, P = PAYOFF_MATRICES[name]
        assert 2 * R > T + S, f"{name} should satisfy 2R>T+S"
    # Snowdrift-style orderings (S > P): being suckered beats mutual defection.
    for name in ["cheap_forgiveness", "punishing_defection"]:
        R, S, T, P = PAYOFF_MATRICES[name]
        assert T > R > S > P, f"{name}: T>R>S>P violated"
