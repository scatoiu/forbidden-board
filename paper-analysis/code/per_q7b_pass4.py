import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Fourth pass: within the forbidden condition, is deficit language in the trace
associated with calling the board in that same move? This is the 'risk appetite'
question asked of what the models SAY."""
import sys, csv, re
sys.path.insert(0,_REPO+"/paper-analysis/code")
from collections import Counter, defaultdict
import pandas as pd
from per_common import save, short, FROZEN, wilson
csv.field_size_limit(10**9)
DEFICIT=re.compile(r"\b(behind|losing|catch up|catching up|deficit|trailing)\b",re.I)
LASTROUND=re.compile(r"\b(last (round|exchange)|final (round|exchange)|end of the run|endgame)\b",re.I)
cells=defaultdict(Counter)
with open(FROZEN/"traces_coded.csv", newline="") as fh:
    for r in csv.DictReader(fh):
        k=(short(r["model"]), r["effort"], r["condition"], r["score_state"])
        c=cells[k]; t=r["reasoning"] or ""
        bc=r["board_called"]=="True"; de=bool(DEFICIT.search(t)); lr=bool(LASTROUND.search(t))
        c["n"]+=1; c["deficit"]+=de; c["lastround"]+=lr; c["call"]+=bc
        c[f"call_deficit_{int(de)}"]+=int(bc)
        c[f"n_deficit_{int(de)}"]+=1
        c[f"call_lastround_{int(lr)}"]+=int(bc); c[f"n_lastround_{int(lr)}"]+=1
rows=[]
for k,c in cells.items():
    r=dict(model=k[0],effort=k[1],condition=k[2],score_state=k[3],n_traces=c["n"],
           share_deficit_language=c["deficit"]/c["n"], share_endgame_language=c["lastround"]/c["n"],
           call_rate_overall=c["call"]/c["n"])
    for f,lab in ((1,"deficit"),(0,"no_deficit")):
        n=c[f"n_deficit_{f}"]; r[f"n_{lab}"]=n
        r[f"call_rate_{lab}"]=(c[f"call_deficit_{f}"]/n) if n else None
    r["diff_pp_deficit_minus_not"]=100*((r["call_rate_deficit"] or 0)-(r["call_rate_no_deficit"] or 0)) \
        if r["call_rate_deficit"] is not None and r["call_rate_no_deficit"] is not None else None
    for f,lab in ((1,"endgame"),(0,"no_endgame")):
        n=c[f"n_lastround_{f}"]; r[f"n_{lab}"]=n
        r[f"call_rate_{lab}"]=(c[f"call_lastround_{f}"]/n) if n else None
    rows.append(r)
df=pd.DataFrame(rows).sort_values(["model","effort","condition","score_state"])
save(df,"per_q7_deficit_language_vs_call.csv")
print(df.round(4).to_string(index=False))
