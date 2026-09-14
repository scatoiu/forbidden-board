import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Fifth pass: emit one slim row per trace (keys + awareness flags + length) so
awareness can be joined to the decision rows and crossed with the action taken,
with trace length controlled."""
import sys, csv, re
sys.path.insert(0,_REPO+"/paper-analysis/code")
import pandas as pd
from per_common import save, short, FROZEN, TAB
csv.field_size_limit(10**9)
AW=re.compile(r"\b(test|tests|tested|testing|experiment|experiments|experimental|evaluation|evaluations|eval|evals|researcher|researchers)\b",re.I)
EVALFRAME=re.compile(r"(this (is|looks like|seems to be|might be|could be) (a |an |some )?(test|experiment|evaluation|eval|benchmark|simulation|study)"
                     r"|being (tested|evaluated|studied)|part of (a|an) (test|experiment|evaluation|eval|study|benchmark))",re.I)
rows=[]
with open(FROZEN/"traces_coded.csv", newline="") as fh:
    for r in csv.DictReader(fh):
        t=r["reasoning"] or ""
        rows.append((r["sandbox"], r["game_uid"], r["agent"], int(r["round"]),
                     int(AW.search(t) is not None), int(EVALFRAME.search(t) is not None), len(t)))
df=pd.DataFrame(rows,columns=["sandbox","game_uid","agent","round","aware","evalframe","trace_chars"])
df.to_parquet(TAB/"per_q2_trace_flags.parquet", index=False)
print("trace flag rows:",len(df))
