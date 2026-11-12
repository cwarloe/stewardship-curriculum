#!/usr/bin/env python3
"""Check that web pages take every color and font from docs/tokens.css.

Flags, in any .html, .css or .js file outside docs/tokens.css: hex colors, rgb()/rgba()/hsl()/hsla(),
colors inside data-URI images (%23abc), and font families written out instead of var(--font-...).
A line that really needs a literal says why with a comment containing "theme-ok: <reason>".
See docs/THEMING.md. Exits 1 on any finding.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = {"docs/tokens.css"}
SKIP_DIRS = {".git", "node_modules"}

HEX = re.compile(r"(?<=[:\s,('\"=])#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})(?=[;}\s,)!'\"]|$)")
FUNC = re.compile(r"\b(?:rgba?|hsla?)\(\s*[\d.]")
URI = re.compile(r"%23[0-9a-fA-F]{3,8}\b")
FONT = re.compile(r"\bfont(?:-family)?\s*:\s*([^;}{]*)")
FAMILY = re.compile(r"\"[^\"]+\"|'[^']+'|\b(?:serif|sans-serif|monospace|cursive|system-ui|Arial|Helvetica|Georgia|Verdana|Times)\b")
# Plain color words count too (white, black, ...), but only as a property value.
NAMED = re.compile(r"\b(?:color|background(?:-color)?|border(?:-[a-z]+)?|fill|stroke)\s*:\s*[^;}]*\b(white|black|red|blue|green|gray|grey)\b")


def hits(line: str) -> list[str]:
    found = HEX.findall(line) + FUNC.findall(line) + URI.findall(line) + NAMED.findall(line)
    for m in FONT.finditer(line):
        if "var(--" not in m.group(1) and FAMILY.search(m.group(1)):
            found.append("font: " + m.group(1).strip()[:40])
    return found


def main() -> int:
    findings = []
    for p in sorted(ROOT.rglob("*")):
        if p.suffix not in (".html", ".css", ".js") or not p.is_file() or SKIP_DIRS & set(p.parts):
            continue
        rel = p.relative_to(ROOT).as_posix()
        if rel in TOKENS:
            continue
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if "theme-ok:" in line or "@font-face" in line:
                continue
            h = hits(line)
            if h:
                findings.append(f"{rel}:{i}  {', '.join(dict.fromkeys(h))}")
    for f in findings:
        print(f)
    if findings:
        print(f"\n{len(findings)} line(s) use raw colors or fonts. Use a token from docs/tokens.css (docs/THEMING.md).")
        return 1
    print("Theme check: every page uses docs/tokens.css.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
