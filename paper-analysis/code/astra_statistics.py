"""Exact finite enumerations, ceiling diagnostics, and frozen-report checks."""
from pathlib import Path
import itertools
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
T = ROOT / "tables"
F = ROOT.parent.parent / "tournament/reports/final-20260913T144509Z/tables"


def flip(d):
    d = np.asarray(d, float)
    return np.mean(np.abs(np.array(list(itertools.product([-1, 1], repeat=len(d)))) @ d)
                   >= abs(d.sum()) - 1e-10)


def holm(p):
    order = np.argsort(p)
    out = np.empty(len(p))
    out[order] = np.minimum(1, np.maximum.accumulate(np.array(p)[order] * np.arange(len(p), 0, -1)))
    return out


def main():
    b = pd.read_csv(T / "astra_endpoint_blocks.csv")
    x = b.query("unit == 'game' and variant == 'any' and contrast in ['A','B']")
    f = pd.read_csv(F / "registered_family.csv")
    fam = f[f.quality_policy == "registered_exclude_gt_10pct"].copy()
    fam["six_slot_holm"] = holm(fam.raw_p.fillna(1).to_numpy())
    for _, g in fam.groupby("model"):
        assert np.allclose(holm(g.raw_p.fillna(1).to_numpy()), g.holm_p)
    fam[["model", "member", "available", "k", "raw_p", "holm_p", "six_slot_holm"]].to_csv(T / "astra_multiplicity.csv", index=False)
    inference, ceilings, influence, margins = [], [], [], []
    for key, g in x.groupby(["model", "condition", "contrast"]):
        g = g.sort_values("block")
        d = g.difference_pp.to_numpy()
        signs = np.array(list(itertools.product([-1, 1], repeat=len(d))))
        upper = np.mean(signs @ (d-10) <= (d-10).sum()+1e-10)
        lower = np.mean(signs @ (d+10) >= (d+10).sum()-1e-10)
        margins.append(dict(zip(["model","condition","contrast"],key),
                            assumption="independent symmetric location-shift differences; exploratory",
                            tost_upper_p=upper,tost_lower_p=lower,tost_p=max(upper,lower),
                            greater_than_10_p=np.mean(signs @ (d-10) >= (d-10).sum()-1e-10)))
        boot = d[np.array(list(itertools.product(range(len(d)), repeat=len(d))))].mean(axis=1)
        strata = [z.difference_pp.to_numpy() for _, z in g.groupby("paraphrase")]
        draws = [v[np.array(list(itertools.product(range(len(v)), repeat=len(v))))].mean(axis=1) for v in strata]
        strat_boot = np.array(list(itertools.product(*draws))).mean(axis=1)
        inference.append(dict(zip(["model","condition","contrast"],key), k=len(d), mean_pp=d.mean(),
                              raw_p=flip(d), bootstrap_exact_lo=np.quantile(boot,.025),
                              bootstrap_exact_hi=np.quantile(boot,.975), bootstrap_patterns=len(boot),
                              fixed_paraphrase_boot_lo=np.quantile(strat_boot,.025),
                              fixed_paraphrase_boot_hi=np.quantile(strat_boot,.975),
                              above_10=int((d>10).sum()), sign_probability_lower_95=(.025**(1/len(d))) if (d>0).all() else np.nan))
        for omit in g.block:
            dd=g.loc[g.block!=omit,"difference_pp"].to_numpy()
            influence.append(dict(zip(["model","condition","contrast"],key), omit=omit, k=len(dd), mean_pp=dd.mean(), raw_p=flip(dd)))
        if key[-1] == "B":
            for _, r in g.iterrows():
                ceilings.append(dict(model=r.model,condition=r.condition,block=r.block,paraphrase=r.paraphrase,
                                     ahead_pct=100*r.lo_rate,behind_pct=100*r.hi_rate,difference_pp=r.difference_pp,
                                     maximum_positive_pp=100*(1-r.lo_rate),
                                     remaining_behind_pp=100*(1-r.hi_rate)))
    pd.DataFrame(inference).to_csv(T/"astra_inference.csv",index=False)
    pd.DataFrame(margins).to_csv(T/"astra_margin_sensitivity.csv",index=False)
    pd.DataFrame(influence).to_csv(T/"astra_leave_one_block.csv",index=False)
    pd.DataFrame(ceilings).to_csv(T/"astra_ceiling.csv",index=False)
    sub=[]
    for (model,contrast),g in x[x.condition=="forbidden"].groupby(["model","contrast"]):
        for name, z in [("p1p2",g[g.paraphrase!="p3"]),("p3",g[g.paraphrase=="p3"])]:
            sub.append(dict(model=model,contrast=contrast,subset=name,k=len(z),mean_pp=z.difference_pp.mean(),raw_p=flip(z.difference_pp)))
    pd.DataFrame(sub).to_csv(T/"astra_paraphrase_subsets.csv",index=False)
    # Simultaneous equality of the two quality views is checked by field, not inferred from p values.
    quality=[]
    for (model,member),g in f.groupby(["model","member"]):
        r=g.set_index("quality_policy")
        for col in ["mean_diff_pp","ci_lo_pp","ci_hi_pp","k","nonzero_k","raw_p","holm_p","resolution_floor","n_blocks_missing_an_arm"]:
            v=r.loc["registered_exclude_gt_10pct",col]; w=r.loc["keep_all_disclosed_deviation",col]
            quality.append(dict(model=model,member=member,field=col,registered=v,keep_all=w,
                                equal=(pd.isna(v) and pd.isna(w)) or v==w))
    pd.DataFrame(quality).to_csv(T/"astra_quality_comparison.csv",index=False)
    # Replicate the exploratory estimates with each endpoint, plus genuinely
    # sandbox-level (unpaired, effort-stratified) permutations for B.
    a=pd.read_parquet(ROOT/"data/agent_games.parquet")
    a=a[(a.dataset=="prereg") & a.paraphrase.isin(["p1","p2","p3"]) & (a.condition=="forbidden")].copy()
    a["attempted"]=(a.attempted_board_calls>0).astype(float)
    estimates=[]; perms=[]
    for model,g in a.groupby("model"):
        for endpoint in ["attempted","used_channel"]:
            rates=g.groupby(["effort","score_state"])[endpoint].mean()
            behind=rates.loc[("off","behind")]; ahead=rates.loc[("off","ahead")]
            estimates.append(dict(model=model,endpoint=endpoint,quantity="B_off_difference",value_pp=100*(behind-ahead)))
            for (effort,state), value in rates.items():
                estimates.append(dict(model=model,endpoint=endpoint,quantity=effort+"_"+state,value_pp=100*value))
            if "high" in set(g.effort):
                estimates.append(dict(model=model,endpoint=endpoint,quantity="off_pooled",value_pp=100*g.loc[g.effort=="off",endpoint].mean()))
            groups=list(dict.fromkeys(g.sandbox))
            means=g.groupby("sandbox")[endpoint].mean().reindex(groups).to_numpy()
            meta=g.drop_duplicates("sandbox").set_index("sandbox").reindex(groups)
            strata=[np.where(meta.effort.to_numpy()==e)[0] for e in sorted(meta.effort.unique())]
            labels=meta.score_state.to_numpy(); obs=behind-ahead
            rng=np.random.default_rng(20260913); count=0
            for _ in range(10000):
                lab=labels.copy()
                for inds in strata:
                    v=labels[inds].tolist(); rng.shuffle(v); lab[inds]=v
                off=(meta.effort.to_numpy()=="off")
                stat=means[off & (lab=="behind")].mean()-means[off & (lab=="ahead")].mean()
                count+=abs(stat)>=abs(obs)-1e-12
            offmeans=means[meta.effort.to_numpy()=="off"]
            stats=[]
            for inds in itertools.combinations(range(12),6):
                mask=np.zeros(12,bool); mask[list(inds)]=True
                stats.append(offmeans[mask].mean()-offmeans[~mask].mean())
            perms.append(dict(model=model,endpoint=endpoint,unit_permuted="sandbox",pairing="unpaired_within_effort",
                              difference_pp=100*obs,mc_10000_p=(count+1)/10001,
                              exact_924_p=np.mean(np.abs(stats)>=abs(obs)-1e-12)))
    pd.DataFrame(estimates).to_csv(T/"astra_exploratory_endpoint_check.csv",index=False)
    pd.DataFrame(perms).to_csv(T/"astra_exploratory_permutations.csv",index=False)
    print("PASS: reproduced per-model Holm; enumerated all 46,656 six-block bootstrap draws and all 924 unpaired B allocations.")
    print(fam[["model","member","holm_p","six_slot_holm"]].to_string(index=False))
    print(pd.DataFrame(inference).to_string(index=False))
    print(pd.DataFrame(perms).to_string(index=False))


if __name__=="__main__":
    main()
