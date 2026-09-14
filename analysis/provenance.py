"""Provenance for one analysis report: what bytes went in, and what came out.

A report that cannot be traced back to its inputs cannot be defended
(notes-astra-analysis-review.md finding 8). This writes `PROVENANCE.json` beside
the report: the analysis commit and whether the tree was dirty, the exact argv
and cwd, package versions, every resolved root with its dataset label, and one
entry per physical sandbox attempt - INCLUDED OR EXCLUDED - with its manifest
digest, the launch `git_sha` and `config_sha256` the runner recorded, and the
`moves.jsonl` byte size, physical line count, final-newline status and SHA256.
`complete` is set true only after every artifact has been written and hashed.
"""
from __future__ import annotations

import hashlib
import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

FORMAT_VERSION = 1
#: roots whose names say they are not pre-registered data
NON_PREREG_ROOT_RX = ("v4", "v5", "v6", "pilot", "v2", "quarantine", "calibration")


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _sha256_and_shape(path: Path) -> dict:
    """Stream the file: digest, bytes, physical lines, final-newline status."""
    h = hashlib.sha256()
    size = lines = 0
    last = b""
    with open(path, "rb") as fh:
        while chunk := fh.read(1 << 20):
            h.update(chunk)
            size += len(chunk)
            lines += chunk.count(b"\n")
            last = chunk[-1:]
    return {"bytes": size, "lines": lines, "sha256": h.hexdigest(),
            "ends_with_newline": last == b"\n"}


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        while chunk := fh.read(1 << 20):
            h.update(chunk)
    return h.hexdigest()


def _git(args: list, cwd: Path) -> str:
    try:
        return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True,
                              timeout=20).stdout.strip()
    except Exception:                                     # noqa: BLE001
        return ""


def _package_versions() -> dict:
    out = {"python": sys.version.split()[0], "platform": platform.platform()}
    try:
        from importlib.metadata import distributions
        for d in distributions():
            name = (d.metadata.get("Name") or "").lower()
            if name in ("numpy", "pandas", "scipy", "matplotlib", "axelrod", "pytest"):
                out[name] = d.version
    except Exception:                                     # noqa: BLE001
        pass
    return out


def check_root_inventory(runs: list, replication: list) -> list:
    """Refuse a replication/diagnostic root supplied as pre-registered data.

    Dataset labels come entirely from CLI position, so one transposed argument
    silently promotes the cap replication into the confirmatory family
    (finding 9). The names are unambiguous; this reads them.
    """
    problems = []
    for r in runs:
        name = Path(r).name.lower()
        for bad in NON_PREREG_ROOT_RX:
            if name.startswith(bad) and not name.startswith("v3"):
                problems.append(f"{r!r} was supplied to --runs (the PRE-REGISTERED dataset) but its "
                                f"name marks it as a {bad} root. The pre-registered roots are "
                                f"runs/v3, runs/v3b and runs/v3-mimo; a replication belongs in "
                                f"--replication and a diagnostic root belongs in neither.")
                break
    for r in replication:
        if Path(r).name.lower().startswith("v3"):
            problems.append(f"{r!r} was supplied to --replication but is a pre-registered root.")
    return problems


def sandbox_entries(rds: list, roots_by_dataset: dict) -> list:
    """One entry per physical sandbox attempt, included and excluded alike."""
    from analysis.load import ARCHIVE_RX

    seen, entries = set(), []
    included = {}
    for rd in rds:
        if rd is None or rd.manifests.empty:
            continue
        for _, m in rd.manifests.iterrows():
            included[(rd.dataset, m["sandbox"])] = m
    for dataset, roots in roots_by_dataset.items():
        for root in roots:
            root = Path(root)
            if not root.is_dir():
                continue
            for sb in sorted(p for p in root.iterdir() if p.is_dir()):
                mv = sb / "moves.jsonl"
                if not mv.exists():
                    continue
                archived = bool(ARCHIVE_RX.search(sb.name))
                man_path = sb / "manifest.json"
                man = {}
                if man_path.exists():
                    try:
                        man = json.loads(man_path.read_text())
                    except Exception:                     # noqa: BLE001
                        man = {}
                key = (dataset, sb.name)
                entry = {
                    "dataset": dataset,
                    "path": str(sb),
                    "attempt_id": f"{dataset}:{root.name}:{sb.name}",
                    "logical_sandbox": man.get("sandbox", sb.name),
                    "base_cell": __import__("analysis.load", fromlist=["base_sandbox"])
                    .base_sandbox(sb.name),
                    "disposition": "excluded" if archived else
                                   ("included" if key in included else "excluded"),
                    "reason": ("archived attempt (name carries an archive suffix)" if archived
                               else "" if key in included else "not selected by the analysis"),
                    "block": man.get("block"),
                    "condition": man.get("condition"),
                    "assigned_state": man.get("assigned_state"),
                    "answer_tokens": (man.get("output_cap") or {}).get("answer_tokens"),
                    "models": man.get("models"),
                    "launch_git_sha": man.get("git_sha"),
                    "config_sha256": man.get("config_sha256"),
                    "tools_source_sha256": (man.get("prompt_resources_sha256") or {}).get("tools.json"),
                    "manifest_sha256": _sha256_file(man_path) if man_path.exists() else None,
                    "moves": _sha256_and_shape(mv),
                }
                if key not in seen:
                    seen.add(key)
                    entries.append(entry)
    return entries


def expected_vs_observed(rds: list) -> list:
    """Per included sandbox: the grid's expected counts against what is there."""
    from analysis.load import EXPECTED_AGENT_GAMES, EXPECTED_UNIQUE_GAMES

    out = []
    for rd in rds:
        if rd is None or rd.games.empty:
            continue
        finished = set(rd.generations["sandbox"]) if not rd.generations.empty else set()
        for sandbox, sub in rd.games.groupby("sandbox", sort=True):
            uniq, ag = int(sub["game_uid"].nunique()), int(len(sub))
            out.append({
                "dataset": rd.dataset, "sandbox": sandbox,
                "generation_end_seen": sandbox in finished,
                "expected_unique_games": EXPECTED_UNIQUE_GAMES,
                "observed_unique_games": uniq,
                "expected_agent_games": EXPECTED_AGENT_GAMES,
                "observed_agent_games": ag,
                "shortfall_unique_games": EXPECTED_UNIQUE_GAMES - uniq,
                "aborted_games": int(sub.loc[sub["game_aborted"], "game_uid"].nunique()),
                "unobserved_provider_error_games":
                    int(sub.loc[sub["game_unobserved"], "game_uid"].nunique()),
            })
    return out


def write_provenance(out_dir, argv: list, roots_by_dataset: dict, rds: list,
                     defaults: dict, read_start: str, read_end: str) -> Path:
    """Write PROVENANCE.json with `complete: false`; `finalise` sets it true."""
    out_dir = Path(out_dir)
    repo = Path(__file__).resolve().parent.parent
    dirty = _git(["status", "--porcelain"], repo)
    doc = {
        "format_version": FORMAT_VERSION,
        "report_utc": _utc(),
        "input_read_start_utc": read_start,
        "input_read_end_utc": read_end,
        "analysis": {
            "git_sha": _git(["rev-parse", "HEAD"], repo),
            "branch": _git(["rev-parse", "--abbrev-ref", "HEAD"], repo),
            "dirty": bool(dirty),
            "dirty_paths": sorted(l[3:] for l in dirty.splitlines()) if dirty else [],
            "cwd": os.getcwd(),
            "argv": list(argv),
            "python_executable": sys.executable,
            "package_versions": _package_versions(),
            "defaults": defaults,
        },
        "roots": {k: [str(Path(r).resolve()) for r in v] for k, v in roots_by_dataset.items()},
        "sandboxes": sandbox_entries(rds, roots_by_dataset),
        "cardinality": expected_vs_observed(rds),
        "quality_policies": list(defaults.get("quality_policies", [])),
        "outputs": {},
        "complete": False,
    }
    path = out_dir / "PROVENANCE.json"
    path.write_text(json.dumps(doc, indent=1, default=str))
    return path


def finalise(out_dir) -> dict:
    """Hash every artifact, then mark the report complete."""
    out_dir = Path(out_dir)
    path = out_dir / "PROVENANCE.json"
    doc = json.loads(path.read_text())
    outputs = {}
    for f in sorted(out_dir.rglob("*")):
        if f.is_file() and f.name != "PROVENANCE.json":
            outputs[str(f.relative_to(out_dir))] = {"bytes": f.stat().st_size,
                                                    "sha256": _sha256_file(f)}
    doc["outputs"] = outputs
    doc["finalised_utc"] = _utc()
    doc["complete"] = True
    path.write_text(json.dumps(doc, indent=1, default=str))
    return doc
