#!/usr/bin/env python3
"""parse_roadmap.py — ROADMAP.md → artifacts/roadmap.json

Parses a Markdown roadmap with H2 section headings and checklist items:

    ## Now
    - [x] Completed task
    - [ ] Pending task

    ## Next
    - [ ] Next task

Produces JSON with per-section items and aggregate summary.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


HEADING_RE = re.compile(r"^##\s+(.+?)\s*$")
ITEM_RE = re.compile(r"^\s*-\s+\[([ xX])\]\s+(.+?)\s*$")


def parse(text: str) -> dict:
    sections: list[dict] = []
    current: dict | None = None
    total = done = 0

    for lineno, raw in enumerate(text.splitlines(), start=1):
        m = HEADING_RE.match(raw)
        if m:
            current = {"name": m.group(1), "items": []}
            sections.append(current)
            continue
        m = ITEM_RE.match(raw)
        if m and current is not None:
            is_done = m.group(1).lower() == "x"
            current["items"].append({
                "text": m.group(2),
                "done": is_done,
                "line": lineno,
            })
            total += 1
            if is_done:
                done += 1

    return {
        "sections": sections,
        "summary": {
            "total": total,
            "done": done,
            "pending": total - done,
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Parse ROADMAP.md to JSON.")
    ap.add_argument("roadmap", type=Path, help="Path to ROADMAP.md")
    ap.add_argument("--out", type=Path, default=Path("artifacts/roadmap.json"),
                    help="Output JSON path")
    args = ap.parse_args()

    if not args.roadmap.is_file():
        print(f"Not a file: {args.roadmap}", file=sys.stderr)
        return 1

    text = args.roadmap.read_text(encoding="utf-8")
    data = parse(text)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(data, indent=2), encoding="utf-8")

    s = data["summary"]
    print(f"Parsed {s['total']} items ({s['done']} done, {s['pending']} pending) "
          f"across {len(data['sections'])} section(s) -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
