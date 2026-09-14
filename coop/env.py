"""Read a git-ignored `.env` and resolve the provider API key by name, never by value.

No dependency: KEY=VALUE lines, `#` comments and blank lines skipped, and a variable
already present in the environment is never overridden. The key value itself is
never logged or written to the manifest — only the name of the variable it came from.
"""

from __future__ import annotations

import os
from pathlib import Path

#: Provider profile -> the variable checked before OPENAI_API_KEY.
PROFILE_KEY_VARS = {
    "openrouter": "OPENROUTER_API_KEY",
    "deepinfra": "DEEPINFRA_API_KEY",
    "generic": "DEEPINFRA_API_KEY",
    "ollama": None,
    "none": None,
}

FALLBACK_KEY_VAR = "OPENAI_API_KEY"


def load_env_file(path: str | Path | None = None) -> list[str]:
    """Load `.env` into os.environ without overriding what is already set.

    Returns the names of the variables it set (never the values).
    """
    p = Path(path) if path else Path(__file__).resolve().parent.parent / ".env"
    if not p.is_file():
        return []
    loaded: list[str] = []
    for line in p.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        name, _, value = line.partition("=")
        name, value = name.strip(), value.strip().strip('"').strip("'")
        if not name or not value or name in os.environ:
            continue
        os.environ[name] = value
        loaded.append(name)
    return loaded


def resolve_api_key(profile: str, explicit: str | None = None) -> tuple[str | None, str]:
    """Return (key, source label). The label is safe to log; the key is not."""
    if explicit:
        return explicit, "--api-key"
    var = PROFILE_KEY_VARS.get((profile or "").lower(), FALLBACK_KEY_VAR)
    for name in ([var] if var else []) + [FALLBACK_KEY_VAR]:
        if name and os.environ.get(name):
            return os.environ[name], name
    return None, "none"
