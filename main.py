from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import yaml


def _parse_added_date(s: Any) -> datetime:
    """Parse YYYY-MM-DD; if missing/invalid, push to bottom."""
    if not s:
        return datetime.min
    try:
        return datetime.strptime(str(s), "%Y-%m-%d")
    except Exception:
        return datetime.min


def _load_watchlist(env) -> List[Dict[str, Any]]:
    """
    Load docs/_data/watchlist.yml.

    Supports two YAML formats:
      1) dict with "items": { items: [...] }
      2) plain list: [ ... ]

    Cached on env to avoid re-reading on every render.
    """
    cache_key = "_watchlist_cache_items"
    if hasattr(env, cache_key):
        return getattr(env, cache_key)

    project_root = Path(__file__).resolve().parent
    data_path = project_root / "docs" / "_data" / "watchlist.yml"
    if not data_path.exists():
        setattr(env, cache_key, [])
        return []

    with data_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    # Accept either {"items": [...]} or just [...]
    if isinstance(data, dict):
        items = data.get("items", []) or []
    elif isinstance(data, list):
        items = data
    else:
        items = []

    # Normalize: keep only dict entries
    items = [x for x in items if isinstance(x, dict)]

    # Sort by added date (newest first)
    items_sorted = sorted(items, key=lambda x: _parse_added_date(x.get("added")), reverse=True)

    setattr(env, cache_key, items_sorted)
    return items_sorted


def define_env(env):
    @env.macro
    def watchlist_latest(n: int = 5) -> List[Dict[str, Any]]:
        items = _load_watchlist(env)
        return items[: max(0, int(n))]

    @env.macro
    def watchlist_by_type(t: str) -> List[Dict[str, Any]]:
        items = _load_watchlist(env)
        t = (t or "").strip().lower()
        return [x for x in items if str(x.get("type", "")).strip().lower() == t]
