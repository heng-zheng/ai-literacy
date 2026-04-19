#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "_data" / "watchlist.yml"
OUT_DIR = ROOT / "docs" / "_generated"


def parse_added_date(value: Any) -> datetime:
    if not value:
        return datetime.min
    try:
        return datetime.strptime(str(value), "%Y-%m-%d")
    except ValueError:
        return datetime.min


def load_items() -> list[dict[str, Any]]:
    data = yaml.safe_load(DATA.read_text(encoding="utf-8")) or {}
    if isinstance(data, dict):
        items = data.get("items", []) or []
    elif isinstance(data, list):
        items = data
    else:
        items = []

    normalized = [item for item in items if isinstance(item, dict)]
    return sorted(normalized, key=lambda item: parse_added_date(item.get("added")), reverse=True)


def cap(value: Any, fallback: str = "item") -> str:
    return str(value or fallback).capitalize()


def render_index(items: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    for item in items[:5]:
        title = item.get("title") or "Untitled"
        url = item.get("url") or ""
        lines.append(f'- **[{title}]({url})** · {cap(item.get("type"))}')
    return "\n".join(lines) + "\n"


def render_latest(items: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    for index, item in enumerate(items[:12]):
        title = item.get("title") or "Untitled"
        url = item.get("url") or ""
        lines.append(f"### [{title}]({url})")
        lines.append("")

        meta = f"Added {item.get('added') or '????-??-??'}"
        if item.get("type"):
            meta += f" · {cap(item.get('type'))}"
        if item.get("published"):
            meta += f" · Published {item.get('published')}"
        if item.get("source"):
            meta += f" · {item.get('source')}"

        lines.append("<small>")
        lines.append(meta)
        lines.append("</small>")
        lines.append("")

        if item.get("why"):
            lines.append(str(item.get("why")))
            lines.append("")

        if index != min(len(items), 12) - 1:
            lines.append("---")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_by_category(items: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    types = sorted({str(item.get("type", "")).strip().lower() for item in items if item.get("type")})

    for item_type in types:
        lines.append(f"### {cap(item_type)}")
        lines.append("")

        for item in items:
            if str(item.get("type", "")).strip().lower() != item_type:
                continue

            title = item.get("title") or "Untitled"
            url = item.get("url") or ""
            entry = f"- **[{title}]({url})**"
            if item.get("source"):
                entry += f" · {item.get('source')}"
            if item.get("published"):
                entry += f" · {item.get('published')}"
            if item.get("why"):
                entry += f"  \n  <small>{item.get('why')}</small>"
            lines.append(entry)

        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    items = load_items()

    (OUT_DIR / "watchlist-index.md").write_text(render_index(items), encoding="utf-8")
    (OUT_DIR / "watchlist-latest.md").write_text(render_latest(items), encoding="utf-8")
    (OUT_DIR / "watchlist-by-category.md").write_text(render_by_category(items), encoding="utf-8")

    print(f"Rendered watchlist includes from {len(items)} items.")


if __name__ == "__main__":
    main()
