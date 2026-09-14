import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Close-out: verify every moves.jsonl on disk against the freeze inventory (bytes, lines, sha256)."""
import csv, hashlib, sys
from pathlib import Path
T = Path(_REPO+'')
inv = T/'reports/FREEZE-20260913T144509Z-inventory.tsv'
rows = list(csv.DictReader(open(inv), delimiter='\t'))
cols = rows[0].keys()
pathcol = next(c for c in cols if 'path' in c.lower() or 'file' in c.lower())
shacol = next(c for c in cols if 'sha' in c.lower())
ok = bad = missing = 0
for r in rows:
    p = T / r[pathcol]
    if not p.exists():
        missing += 1; print('MISSING', r[pathcol]); continue
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    if h.hexdigest() == r[shacol]:
        ok += 1
    else:
        bad += 1; print('MISMATCH', r[pathcol])
print(f'inventory rows {len(rows)}: ok {ok}, mismatch {bad}, missing {missing}')
