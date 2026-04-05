#!/usr/bin/env python3
"""index_sessions.py — Build docs/sessions.md from sessions/*.md files.

Lists every session file with its size and SHA-256 hash for integrity.
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description="Build sessions index.")
    ap.add_argument("--root", type=Path, default=Path("."), help="Repository root")
    ap.add_argument("--out", type=Path, default=Path("docs/sessions.md"))
    args = ap.parse_args()

    sessions_dir = args.root / "sessions"
    md = ["# Sessions Index", ""]

    if not sessions_dir.is_dir():
        md.append("_No sessions directory found._")
    else:
        files = sorted(sessions_dir.rglob("*.md"))
        if not files:
            md.append("_No sessions found._")
        else:
            md.append("| File | Size (bytes) | SHA-256 |")
            md.append("|---|---|---|")
            for f in files:
                rel = f.relative_to(args.root).as_posix()
                size = f.stat().st_size
                digest = sha256_of(f)
                md.append(f"| `{rel}` | {size} | `{digest}` |")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
