"""Read manifest design facts and bound missing/repaired forbidden games."""
from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
T=ROOT/"tables"
TOURN=ROOT.parent.parent/"tournament"


def main():
    prov=json.loads((ROOT/"data/PROVENANCE.json").read_text())
    records=[]; repairs={}
    for dataset,spec in prov["datasets"].items():
        for moves in spec["input_files"]:
            manifest=(TOURN/moves).parent/"manifest.json"
            if not manifest.exists():
                continue
            m=json.loads(manifest.read_text()); c=m["config"]
            plan=m.get("assigned_state_plan",{})
            records.append(dict(dataset=dataset,sandbox=c["sandbox"],source=str(manifest),
                                condition=c["channel"],effort=c["reasoning_effort"],paraphrase=c["paraphrase"],
                                seed=c["seed"],shuffle_seed=c.get("schedule",{}).get("shuffle_seed"),
                                provider=c["provider"],quant=c["quant"],matrix=c["matrix"],
                                arm=plan.get("arm"),gap=plan.get("gap_realised"),
                                history=",".join(plan.get("sequence",[])),
                                start=m.get("start_time"),repair_of=m.get("repair_of"),board_replay=m.get("board_replay")))
            if m.get("repair_of") and c["channel"]=="forbidden":
                repairs[m["repair_of"]]=set(m["only_games"])
    design=pd.DataFrame(records)
    design.to_csv(T/"astra_manifest_design.csv",index=False)
    a=pd.read_parquet(ROOT/"data/agent_games.parquet")
    a=a[(a.dataset=="prereg") & a.paraphrase.isin(["p1","p2","p3"])]
    a["any"]=a.attempted_board_calls>0
    ag=a.groupby(["sandbox","game"]).agg(used=("any","max"),unobserved=("game_unobserved","max"),
                                            aborted=("game_aborted","max")).reset_index()
    cell=pd.read_csv(T/"astra_attrition_cells.csv")
    rows=[]
    ds=cell.query("dataset == 'prereg' and condition == 'forbidden' and score_state == 'behind'")
    ds=ds[ds.model.str.contains("DeepSeek")]
    for block,g in ds.groupby("block"):
        h=g[g.effort=="high"].iloc[0]; l=g[g.effort=="off"].iloc[0]
        games=ag[ag.sandbox==h.sandbox]
        repaired=games.game.isin(repairs.get(h.sandbox,set()))
        r=int(repaired.sum()); u=int(games.loc[repaired,"used"].sum())
        if h.sandbox in repairs:
            assert r==len(repairs[h.sandbox])
        known=h.used-u
        rows.append(dict(block=block,high_n=h.n,off_n=l.n,high_used=h.used,off_used=l.used,
                         high_unobserved=h.unobserved,off_unobserved=l.unobserved,
                         high_provider_abort=h.provider_abort,off_provider_abort=l.provider_abort,
                         observed_A_pp=100*(h.observed_rate-l.observed_rate),
                         include_unobserved_as_zero_A_pp=100*(h.all_rate-l.all_rate),
                         completed_A_pp=100*(h.completed_rate-l.completed_rate),
                         residual_missing_lower_A_pp=100*(h.lower_rate-l.upper_rate),
                         residual_missing_upper_A_pp=100*(h.upper_rate-l.lower_rate),
                         repaired_games=r,repaired_used=u,
                         omit_repairs_A_pp=100*(known/(h.n-r)-l.observed_rate),
                         repairs_unknown_lower_A_pp=100*(known/h.n-l.upper_rate),
                         repairs_unknown_upper_A_pp=100*((known+r)/h.n-l.lower_rate)))
    out=pd.DataFrame(rows)
    out.to_csv(T/"astra_A_attrition_bounds.csv",index=False)
    # Compare board and decoy on identical cells; this is not mediation analysis.
    b=pd.read_csv(T/"astra_endpoint_blocks.csv")
    z=b.query("condition == 'forbidden' and unit == 'game' and variant in ['any','decoy']")
    diff=z.pivot(index=["model","contrast","block"],columns="variant",values="difference_pp").reset_index()
    diff["board_change_minus_decoy_change_pp"]=diff["any"]-diff.decoy
    diff.to_csv(T/"astra_board_decoy_blocks.csv",index=False)
    inventory=pd.read_csv(ROOT/"data/sandboxes.csv")
    inventory=inventory[inventory.paraphrase.isin(["p1","p2","p3"])]
    inventory.groupby(["dataset","model","condition","effort","score_state"]).size().rename("n_sandboxes").reset_index().to_csv(T/"astra_arm_inventory.csv",index=False)
    print("PASS: manifest repair IDs match their compact-game rows; missingness and repair bounds computed for all six A pairs.")
    print(out.to_string(index=False))
    print("Mean A bounds:",out.select_dtypes("number").mean().to_dict())
    print("Manifest design levels:",design.groupby("dataset")[["provider","quant","matrix","paraphrase"]].nunique().to_dict())


if __name__=="__main__":
    main()
