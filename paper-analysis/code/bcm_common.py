import os as _os; _REPO=_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))  # repo root
"""Shared loaders for the board-communication analysis (06). READ-ONLY on project/tournament."""
import json, os, subprocess
from pathlib import Path
import pandas as pd

TOURN = Path(_REPO+'')
AN = Path(_REPO+'/paper-analysis')
RUNS = TOURN / 'runs'
FROZEN = TOURN / 'reports/final-20260913T144509Z/tables'
ROOTS = ['v3', 'v3b', 'v3-mimo']
REPAIR = 'v7-repair'

MODEL_SHORT = {'deepseek-ai/DeepSeek-V4-Flash-0731': 'DeepSeek',
               'XiaomiMiMo/MiMo-V2.5-Pro': 'MiMo'}
WORDING = {'p1': 'p1 (blocks B1,B2 / M1,M2)', 'p2': 'p2 (blocks B3,B4 / M3,M4)',
           'p3': 'p3 (blocks B5,B6 / M5,M6)'}


def prereg_sandboxes():
    s = pd.read_csv(AN / 'data/sandboxes.csv')
    s = s[(s.dataset == 'prereg') & (s.paraphrase != 'p4')].copy()
    return s.sort_values('sandbox').reset_index(drop=True)


def sandbox_dir(sb):
    for r in ROOTS:
        if (RUNS / r / sb).is_dir():
            return RUNS / r / sb
    return None


def repair_dir(sb):
    d = RUNS / REPAIR / f'{sb}-repair'
    return d if d.is_dir() else None


def repaired_games(sb):
    d = repair_dir(sb)
    if d is None:
        return set()
    out = subprocess.run(['grep', '-o', '"game": [0-9]*', str(d / 'moves.jsonl')],
                         capture_output=True, text=True).stdout
    return {int(x.split(': ')[1]) for x in out.splitlines()}


def read_notes(path, source):
    rows = []
    if path is None or not path.exists():
        return rows
    with open(path) as fh:
        for i, line in enumerate(fh):
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            d['_source'] = source
            d['_order'] = i
            rows.append(d)
    return rows


def board_entries(sb):
    """Merged board for a sandbox, in posting order.

    For a repaired sandbox the frozen dataset replaces the repaired games with the
    re-plays, so the original board entries belonging to a repaired game are dropped
    and the repair run's entries are appended; entries keep a `_source` column.
    """
    d = sandbox_dir(sb)
    orig = read_notes(d / 'notes.jsonl' if d else None, 'original')
    rep_dir = repair_dir(sb)
    rep = read_notes(rep_dir / 'notes.jsonl' if rep_dir else None, 'repair')
    if rep:
        rg = repaired_games(sb)
        orig = [e for e in orig if e.get('game') not in rg]
    rows = orig + rep
    for n, e in enumerate(rows, 1):
        e['_n'] = n
    return pd.DataFrame(rows)


def manifest(sb):
    d = sandbox_dir(sb)
    return json.load(open(d / 'manifest.json')) if d else None


def llm_agents(sb, model):
    m = manifest(sb)
    return sorted(a['agent_id'] for a in m['agents'] if a['model'] == model)
