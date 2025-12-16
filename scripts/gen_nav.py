#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MKDOCS_YML = ROOT / "mkdocs.yml"

BEGIN = "# BEGIN AUTO NAV"
END = "# END AUTO NAV"

def title_case_week(stem: str) -> str:
    """
    Convert 'week-01' -> 'Week 01'
    """
    m = re.match(r"week-(\d+)$", stem)
    if not m:
        return stem
    return f"Week {m.group(1)}"

def guess_title_from_h1(md_path: Path) -> str | None:
    """
    Parse the first Markdown H1 line: '# Title'
    If not found, return None.
    """
    try:
        text = md_path.read_text(encoding="utf-8")
    except Exception:
        return None
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return None

def collect_weeks() -> list[tuple[int, str, str]]:
    """
    Returns: list of (week_number, nav_label, rel_path)
    """
    weeks_dir = DOCS / "weeks"
    if not weeks_dir.exists():
        return []

    items = []
    for p in weeks_dir.glob("week-*.md"):
        m = re.match(r"week-(\d+)\.md$", p.name)
        if not m:
            continue
        num = int(m.group(1))
        # label priority: H1 title (shortened) OR Week NN
        h1 = guess_title_from_h1(p)
        if h1 and h1.lower().startswith("week"):
            # Use a stable label like "Week 01" even if H1 is long
            label = title_case_week(p.stem)
        else:
            label = title_case_week(p.stem)

        rel = p.relative_to(DOCS).as_posix()
        items.append((num, label, rel))

    items.sort(key=lambda x: x[0])
    return items

def collect_concepts() -> list[tuple[str, str]]:
    """
    Returns: list of (nav_label, rel_path)
    Uses file H1 as label if available, otherwise file stem.
    """
    concepts_dir = DOCS / "concepts"
    if not concepts_dir.exists():
        return []

    items = []
    for p in concepts_dir.glob("*.md"):
        if p.name.lower() == "index.md":
            continue
        h1 = guess_title_from_h1(p)
        label = h1 if h1 else p.stem.replace("-", " ").title()
        rel = p.relative_to(DOCS).as_posix()
        items.append((label, rel))

    # sort alphabetically by label
    items.sort(key=lambda x: x[0].lower())
    return items

def render_nav_block() -> str:
    weeks = collect_weeks()
    concepts = collect_concepts()

    lines = []

    if weeks:
        lines.append("Weeks:")
        for _, label, rel in weeks:
            lines.append(f"  {label}: {rel}")

    if concepts:
        lines.append("Concepts:")
        for label, rel in concepts:
            lines.append(f"  {label}: {rel}")

    return "\n".join(lines) + "\n"


def replace_block(mkdocs_text: str, new_block: str) -> str:
    # Support both LF and CRLF newlines
    nl = r"(?:\r?\n)"

    pattern = re.compile(
        rf"^(?P<indent>[ \t]*){re.escape(BEGIN)}[ \t]*$"   # BEGIN line
        rf"(?P<body>(?:{nl}.*?)*?)"                        # zero or more lines (can be empty)
        rf"{nl}"
        rf"^(?P=indent){re.escape(END)}[ \t]*$",           # END line (same indent)
        re.DOTALL | re.MULTILINE,
    )

    m = pattern.search(mkdocs_text)
    if not m:
        raise SystemExit(
            f"Could not find markers in mkdocs.yml. "
            f"Please add lines:\n{BEGIN}\n{END}"
        )

    indent = m.group("indent")

    # Re-indent the generated block to match marker indentation
    reindented_lines = []
    for line in new_block.splitlines():
        if line.strip() == "":
            reindented_lines.append(line)
        else:
            reindented_lines.append(indent + line)
    reindented_block = "\n".join(reindented_lines) + "\n"

    replacement = f"{indent}{BEGIN}\n{reindented_block}{indent}{END}"
    return pattern.sub(replacement, mkdocs_text, count=1)


def main() -> None:
    mkdocs_text = MKDOCS_YML.read_text(encoding="utf-8")
    new_block = render_nav_block()
    updated = replace_block(mkdocs_text, new_block)
    MKDOCS_YML.write_text(updated, encoding="utf-8")
    print("Updated mkdocs.yml nav block.")

if __name__ == "__main__":
    main()
