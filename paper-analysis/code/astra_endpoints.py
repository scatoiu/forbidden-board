"""Independent endpoint audit. Reads compact data; writes only astra CSVs."""
from pathlib import Path
import itertools
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "tables"
FROZEN = ROOT.parent.parent / "tournament/reports/final-20260913T144509Z/tables"


def signflip(d):
    d = np.asarray(d, float)
    signs = np.array(list(itertools.product([-1, 1], repeat=len(d))))
    return np.mean(np.abs(signs @ d) >= abs(d.sum()) - 1e-10)


def main():
    a = pd.read_parquet(ROOT / "data/agent_games.parquet")
    d = pd.read_parquet(ROOT / "data/decisions.parquet")
    s = pd.read_csv(ROOT / "data/sandboxes.csv")
    keep = lambda x: x.paraphrase.isin(["p1", "p2", "p3"])
    a, d, s = a[keep(a)].copy(), d[keep(d)].copy(), s[keep(s)].copy()
    assert not a.agent_game_uid.duplicated().any()
    assert len(a[a.dataset == "prereg"]) == 19044
    assert len(d[d.dataset == "prereg"]) == 357433
    assert d.loc[d.dataset == "prereg", "is_played"].sum() == 356352
    # Independent reconciliation of decision counts against agent-game totals.
    sums = d.groupby("agent_game_uid")[["att_board_calls", "att_post_calls", "att_read_calls"]].sum()
    aa = a.set_index("agent_game_uid")
    for dc, ac in zip(sums.columns, ["attempted_board_calls", "attempted_post_calls", "attempted_read_calls"]):
        assert np.array_equal(sums[dc].reindex(aa.index, fill_value=0), aa[ac])
    for out, col in [("any", "attempted_board_calls"), ("post", "attempted_post_calls"),
                     ("read", "attempted_read_calls"), ("decoy", "attempted_decoy_calls")]:
        a[out] = a[col] > 0
    a["final"] = a.agent_game_uid.map(d.groupby("agent_game_uid").board_calls.sum()).fillna(0) > 0
    a["reported_final"] = a.used_channel > 0
    first = d[d["round"] == 1].groupby("agent_game_uid").att_board_calls.sum()
    a["round1"] = a.agent_game_uid.map(first).fillna(0) > 0
    variants = ["any", "read", "post", "final", "reported_final", "decoy", "round1"]
    assert (a["any"] >= a["final"]).all()
    meta = ["dataset", "sandbox", "model", "block", "paraphrase", "effort", "score_state", "condition", "seed"]
    games = a.groupby(meta + ["game_uid"], sort=False).agg(
        **{v: (v, "max") for v in variants},
        observed=("game_observed", "max"), aborted=("game_aborted", "max"),
        unobserved=("game_unobserved", "max"), provider_abort=("game_provider_error_abort", "max"),
        game=("game", "first"), pair_type=("pair_type", "first")).reset_index()
    cells = []
    for unit, frame, obs in [("game", games, "observed"), ("agent_game", a, "game_observed")]:
        for key, g in frame.groupby(meta):
            for variant in variants:
                cells.append(dict(zip(meta, key), unit=unit, variant=variant,
                                  numerator=int(g.loc[g[obs], variant].sum()), denominator=int(g[obs].sum()),
                                  rate=g.loc[g[obs], variant].mean()))
    cells = pd.DataFrame(cells)
    cells.to_csv(TABLES / "astra_endpoint_cells.csv", index=False)
    refs = s[s.dataset == "prereg"].set_index("sandbox").frozen_rate_per_game_either
    baseline = cells.query("dataset == 'prereg' and unit == 'game' and variant == 'any'").set_index("sandbox").rate
    assert np.allclose(baseline, refs.reindex(baseline.index), atol=1e-12)
    contrasts = []
    for (model, condition, unit, variant), g in cells.groupby(["model", "condition", "unit", "variant"]):
        specs = [("B", "prereg", "off", "behind", "prereg", "off", "ahead"),
                 ("A", "prereg", "high", "behind", "prereg", "off", "behind"),
                 ("low_off", "low_arm", "low", "behind", "prereg", "off", "behind"),
                 ("high_low", "prereg", "high", "behind", "low_arm", "low", "behind"),
                 ("deficit", "deficit_d30", "off", "behind", "prereg", "off", "behind")]
        for name, ds1, e1, st1, ds0, e0, st0 in specs:
            hi = g[(g.dataset == ds1) & (g.effort == e1) & (g.score_state == st1)]
            lo = g[(g.dataset == ds0) & (g.effort == e0) & (g.score_state == st0)]
            for _, row in hi.merge(lo, on="block", suffixes=("_hi", "_lo")).iterrows():
                contrasts.append(dict(model=model, condition=condition, unit=unit, variant=variant,
                                      contrast=name, block=row.block, paraphrase=row.paraphrase_hi,
                                      hi_sandbox=row.sandbox_hi, lo_sandbox=row.sandbox_lo,
                                      hi_seed=row.seed_hi, lo_seed=row.seed_lo,
                                      hi_rate=row.rate_hi, lo_rate=row.rate_lo,
                                      difference_pp=100 * (row.rate_hi - row.rate_lo)))
    contrasts = pd.DataFrame(contrasts)
    contrasts.to_csv(TABLES / "astra_endpoint_blocks.csv", index=False)
    summaries = []
    for key, g in contrasts.groupby(["model", "condition", "unit", "variant", "contrast"]):
        dif = g.difference_pp.to_numpy()
        summaries.append(dict(zip(["model", "condition", "unit", "variant", "contrast"], key),
                              k=len(g), mean_pp=dif.mean(), positive=int((dif > 1e-10).sum()),
                              negative=int((dif < -1e-10).sum()), raw_p=signflip(dif),
                              min_pp=dif.min(), max_pp=dif.max()))
    summary = pd.DataFrame(summaries)
    summary.to_csv(TABLES / "astra_endpoint_summary.csv", index=False)
    f = pd.read_csv(FROZEN / "registered_family.csv")
    for _, r in f[f.available].iterrows():
        c = contrasts[(contrasts.model.str.endswith(r.model)) & (contrasts.condition == r.condition)
                      & (contrasts.unit == "game") & (contrasts.variant == "any")
                      & (contrasts.contrast == r.member.split("_")[0])]
        if r.quality_policy == "registered_exclude_gt_10pct":
            eligible = s.set_index("sandbox").frozen_eligible_registered
            c = c[c.hi_sandbox.map(eligible).eq(True) & c.lo_sandbox.map(eligible).eq(True)]
        assert len(c) == r.k
        assert np.isclose(c.difference_pp.mean(), r.mean_diff_pp)
        assert np.isclose(signflip(c.difference_pp), r.raw_p)
    gap = []
    for key, g in a[a.dataset == "prereg"].groupby(["model", "condition", "effort", "score_state"]):
        gap.append(dict(zip(["model", "condition", "effort", "score_state"], key), n=len(g),
                        attempted_pct=100*g["any"].mean(), final_pct=100*g["final"].mean(),
                        reported_final_pct=100*g.reported_final.mean(),
                        union_only=int((g["any"] & ~g["final"]).sum()),
                        final_vs_reported=int((g["final"] != g.reported_final).sum())))
    pd.DataFrame(gap).to_csv(TABLES / "astra_attempt_gap.csv", index=False)
    quality = []
    for key, g in games.groupby(meta):
        n, used = len(g), int(g["any"].sum())
        unknown = g.unobserved | (g.aborted & ~g["any"])
        quality.append(dict(zip(meta,key), n=n, used=used, aborted=int(g.aborted.sum()),
                            unobserved=int(g.unobserved.sum()), provider_abort=int(g.provider_abort.sum()),
                            observed_rate=g.loc[g.observed,"any"].mean(), all_rate=used/n,
                            completed_rate=g.loc[~g.aborted,"any"].mean(),
                            lower_rate=used/n, upper_rate=(used+int(unknown.sum()))/n))
    pd.DataFrame(quality).to_csv(TABLES / "astra_attrition_cells.csv", index=False)
    # Decision-level denominators and reasoning summaries are descriptive only.
    desc = []
    for key, g in d.groupby(meta):
        q = g.reasoning_tokens.quantile([.25,.5,.75]).to_numpy()
        desc.append(dict(zip(meta,key), n_decisions=len(g), n_played=int(g.is_played.sum()),
                         board_decision_rate=(g.att_board_calls>0).mean(), decoy_decision_rate=(g.att_decoy_calls>0).mean(),
                         reasoning_q25=q[0], reasoning_median=q[1], reasoning_q75=q[2]))
    pd.DataFrame(desc).to_csv(TABLES / "astra_decision_cells.csv", index=False)
    print("PASS: frozen counts, all sandbox primary rates, all 8 available quality-family rows, and decision-to-agent endpoint totals.")
    print(summary.query("condition == 'forbidden' and contrast in ['A','B','low_off','high_low','deficit']").to_string(index=False))


if __name__ == "__main__":
    main()
