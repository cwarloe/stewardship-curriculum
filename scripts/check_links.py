#!/usr/bin/env python3
"""Check that local Markdown links and #anchors in this repo resolve.

External links (http, https, mailto) are not fetched. Anchors are matched
against GitHub-style heading slugs in the target file. Exits 1 on any
broken link.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
EXTERNAL = ("http://", "https://", "mailto:")


def strip_code(text: str) -> list[str]:
    """Return lines with fenced blocks blanked and inline code removed."""
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else re.sub(r"`[^`]*`", "", line))
    return out


def slug(heading: str) -> str:
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)  # link text only
    text = re.sub(r"[*_`]", "", text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors(path: Path, cache: dict[Path, set[str]]) -> set[str]:
    if path not in cache:
        seen: dict[str, int] = {}
        found = set()
        for line in strip_code(path.read_text(encoding="utf-8")):
            m = HEADING.match(line)
            if not m:
                continue
            base = slug(m.group(2))
            n = seen.get(base, 0)
            found.add(base if n == 0 else f"{base}-{n}")
            seen[base] = n + 1
        cache[path] = found
    return cache[path]


def main() -> int:
    cache: dict[Path, set[str]] = {}
    errors: list[str] = []
    files = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
    count = 0
    for md in files:
        for lineno, line in enumerate(strip_code(md.read_text(encoding="utf-8")), 1):
            for target in LINK.findall(line):
                if target.startswith(EXTERNAL):
                    continue
                count += 1
                path_part, _, frag = target.partition("#")
                dest = md if not path_part else (md.parent / unquote(path_part)).resolve()
                where = f"{md.relative_to(ROOT)}:{lineno}"
                if not dest.exists():
                    errors.append(f"{where}: missing file {target}")
                elif frag and dest.suffix == ".md" and unquote(frag).lower() not in anchors(dest, cache):
                    errors.append(f"{where}: missing anchor {target}")
    for e in errors:
        print(e)
    print(f"Checked {count} local links in {len(files)} Markdown files; {len(errors)} broken.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
