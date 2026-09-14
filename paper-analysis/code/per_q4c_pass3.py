import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Third pass: (a) count traces that state the PROHIBITION and call the board in the
same move, per cell; (b) dump every high-effort forbidden mention_and_use trace."""
import sys, csv, re
sys.path.insert(0,_REPO+"/paper-analysis/code")
from collections import Counter, defaultdict
import pandas as pd
from per_common import save, short, FROZEN
csv.field_size_limit(10**9)
DEFICIT=re.compile(r"\b(behind|losing|catch up|catching up|deficit|trailing|i'?m down|we'?re down)\b",re.I)
cells=defaultdict(Counter); dump=[]
n=0
with open(FROZEN/"traces_coded.csv", newline="") as fh:
    for r in csv.DictReader(fh):
        n+=1
        k=(short(r["model"]), r["effort"], r["condition"])
        c=cells[k]; c["n"]+=1
        bc = r["board_called"]=="True"; pr = r["mentions_prohibition"]=="True"
        c["prohibition"]+=int(pr); c["board_called"]+=int(bc)
        c["prohibition_and_call"]+=int(pr and bc)
        c["prohibition_and_nocall"]+=int(pr and not bc)
        if pr and bc and DEFICIT.search(r["reasoning"] or ""): c["proh_call_deficit"]+=1
        if r["condition"]=="forbidden" and r["effort"]=="high" and r["trace_code"]=="mention_and_use":
            dump.append(dict(sandbox=r["sandbox"], game_uid=r["game_uid"], agent=r["agent"],
                             round=r["round"], score_state=r["score_state"],
                             mentions_prohibition=pr, board_calls=r["board_calls"],
                             decoy_calls=r["decoy_calls"],
                             reasoning=(r["reasoning"] or "").replace("\n"," ")[-1400:]))
print("rows:",n)
rows=[]
for k,c in cells.items():
    rows.append(dict(model=k[0],effort=k[1],condition=k[2],n_traces=c["n"],
                     n_states_prohibition=c["prohibition"], n_board_called=c["board_called"],
                     n_states_prohibition_and_calls=c["prohibition_and_call"],
                     n_states_prohibition_and_abstains=c["prohibition_and_nocall"],
                     share_of_calls_that_state_prohibition=(c["prohibition_and_call"]/c["board_called"]) if c["board_called"] else None,
                     n_proh_call_with_deficit_language=c["proh_call_deficit"]))
save(pd.DataFrame(rows).sort_values(["model","effort","condition"]),"per_q4_prohibition_stated_and_called.csv")
save(pd.DataFrame(dump),"per_q4_forbidden_high_mention_and_use_all.csv")
print(pd.DataFrame(rows).sort_values(["model","effort","condition"]).to_string(index=False))
