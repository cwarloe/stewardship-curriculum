#!/usr/bin/env python3
"""Check that research/EVIDENCE_INDEX.md and the research records agree.

For every research/R###-*.md record there must be exactly one index row with
that ID, its Record link must point at that file, and the index Status must
match the record's own `**Status:**` line. Statuses must be one of the values
the index lists. Exits 1 on any mismatch.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESEARCH = ROOT / "research"
INDEX = RESEARCH / "EVIDENCE_INDEX.md"
STATUSES = {"candidate", "assessed", "superseded", "retracted"}
RECORD_FILE = re.compile(r"^(R\d{3})-.+\.md$")
ROW_ID = re.compile(r"^\|\s*(R\d{3})\s*\|")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
RECORD_STATUS = re.compile(r"\*\*Status:\*\*\s*([A-Za-z]+)")


def main() -> int:
    errors: list[str] = []

    records: dict[str, Path] = {}
    for path in sorted(RESEARCH.glob("R*.md")):
        m = RECORD_FILE.match(path.name)
        if not m:
            continue
        if m.group(1) in records:
            errors.append(f"duplicate record ID {m.group(1)}: {records[m.group(1)].name}, {path.name}")
        records[m.group(1)] = path

    rows: dict[str, tuple[str, str, int]] = {}
    for lineno, line in enumerate(INDEX.read_text(encoding="utf-8").splitlines(), 1):
        m = ROW_ID.match(line)
        if not m:
            continue
        rid = m.group(1)
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 6:
            errors.append(f"EVIDENCE_INDEX.md:{lineno}: {rid} row has {len(cells)} columns, expected 6")
            continue
        if rid in rows:
            errors.append(f"EVIDENCE_INDEX.md:{lineno}: duplicate row for {rid}")
        link = LINK.search(cells[5])
        rows[rid] = (cells[4], link.group(1) if link else "", lineno)

    for rid, path in records.items():
        if rid not in rows:
            errors.append(f"research/{path.name}: no row for {rid} in EVIDENCE_INDEX.md")
            continue
        status, target, lineno = rows[rid]
        where = f"EVIDENCE_INDEX.md:{lineno}"
        if target != path.name:
            errors.append(f"{where}: {rid} Record links to {target or '(nothing)'}, expected {path.name}")
        if status not in STATUSES:
            errors.append(f"{where}: {rid} status {status!r} is not one of {sorted(STATUSES)}")
        m = RECORD_STATUS.search(path.read_text(encoding="utf-8"))
        if not m:
            errors.append(f"research/{path.name}: no **Status:** line")
        elif m.group(1).lower() != status.lower():
            errors.append(f"{where}: {rid} status {status!r} but record says {m.group(1)!r}")

    for rid, (_, _, lineno) in rows.items():
        if rid not in records:
            errors.append(f"EVIDENCE_INDEX.md:{lineno}: {rid} has no research/{rid}-*.md record")

    for e in errors:
        print(e)
    print(f"Checked {len(records)} research records against {len(rows)} index rows; {len(errors)} problems.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
