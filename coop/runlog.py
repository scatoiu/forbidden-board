"""JSONL run log and manifest. One file per sandbox, no aggregation at write time."""

from __future__ import annotations

import hashlib
import json
import subprocess
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class RunLogger:
    """Thread-safe append-only JSONL writer for move / game_end / generation_end rows."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._fh = self.path.open("a")
        self._lock = threading.Lock()
        self.counts: dict[str, int] = {}

    def write(self, row: dict[str, Any]) -> None:
        line = json.dumps(row, default=str)
        with self._lock:
            self._fh.write(line + "\n")
            self._fh.flush()
            kind = row.get("kind", "?")
            self.counts[kind] = self.counts.get(kind, 0) + 1

    def close(self) -> None:
        with self._lock:
            if not self._fh.closed:
                self._fh.close()

    def __enter__(self) -> "RunLogger":
        return self

    def __exit__(self, *exc) -> None:
        self.close()


def git_sha(cwd: str | Path | None = None) -> str:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=str(cwd or Path(__file__).parent.parent),
            capture_output=True, text=True, timeout=10, check=True,
        )
        return out.stdout.strip()
    except (subprocess.SubprocessError, OSError):
        return "unknown"


def config_sha256(config: dict[str, Any]) -> str:
    return hashlib.sha256(
        json.dumps(config, sort_keys=True, default=str).encode()
    ).hexdigest()


def write_manifest(path: str | Path, config: dict[str, Any], **extra: Any) -> dict[str, Any]:
    """Written before move 1 (specs/moves-schema.md)."""
    from coop import __version__ as coop_version

    manifest = {
        "config": config,
        "config_sha256": config_sha256(config),
        "git_sha": git_sha(),
        "coop_version": coop_version,
        "start_time": datetime.now(timezone.utc).isoformat(timespec="seconds").replace(
            "+00:00", "Z"
        ),
        **extra,
    }
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(manifest, indent=2, default=str))
    return manifest
