#!/usr/bin/env python3
"""parse_recycle_bin.py — Parse Windows $Recycle.Bin $I metadata files.

Usage:
    python3 parse_recycle_bin.py <recycle-bin-dir> [--output deleted_files.csv]

Parses Vista+/Windows 10+ $I file format to extract:
    - Original file path (UTF-16LE)
    - Deletion timestamp (FILETIME, UTC)
    - Original file size

Reference: CSC-7310 Lab 09 — Recycle Bin Forensics (Week 7)

$I file format (Windows 10+):
    Offset 0x00: 8 bytes — header version (0x02 = Win10+)
    Offset 0x08: 8 bytes — file size (little-endian int64)
    Offset 0x10: 8 bytes — deletion time (Windows FILETIME)
    Offset 0x18: 4 bytes — path length in UTF-16 chars (Win10+ only)
    Offset 0x1C: variable — original path as UTF-16LE string (null-terminated)

$I file format (Vista-Win8.1):
    Offset 0x00: 8 bytes — header version (0x01)
    Offset 0x08: 8 bytes — file size
    Offset 0x10: 8 bytes — deletion time
    Offset 0x18: 520 bytes — original path (fixed UTF-16LE, 260 chars max)
"""
from __future__ import annotations

import argparse
import csv
import struct
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


FILETIME_EPOCH = datetime(1601, 1, 1, tzinfo=timezone.utc)


def filetime_to_iso(filetime: int) -> str:
    """Convert Windows FILETIME (100-nanosecond intervals since 1601) to ISO UTC."""
    if filetime <= 0:
        return ""
    delta = timedelta(microseconds=filetime / 10)
    return (FILETIME_EPOCH + delta).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_i_file(path: Path) -> dict | None:
    """Parse a single $I metadata file. Returns None if unparseable."""
    try:
        data = path.read_bytes()
    except OSError as e:
        print(f"Could not read {path}: {e}", file=sys.stderr)
        return None

    if len(data) < 0x18:
        return None

    version = struct.unpack_from("<Q", data, 0x00)[0]
    file_size = struct.unpack_from("<Q", data, 0x08)[0]
    deletion_time = struct.unpack_from("<Q", data, 0x10)[0]

    if version >= 2:
        if len(data) < 0x1C:
            return None
        path_len = struct.unpack_from("<I", data, 0x18)[0]
        path_bytes = data[0x1C:0x1C + (path_len * 2)]
    else:
        path_bytes = data[0x18:0x18 + 520]

    try:
        original_path = path_bytes.decode("utf-16-le").rstrip("\x00")
    except UnicodeDecodeError:
        original_path = "<undecodable>"

    # Corresponding $R file exists if filename exists with $R prefix
    r_file = path.parent / ("$R" + path.name[2:])

    return {
        "i_file": path.name,
        "version": version,
        "original_path": original_path,
        "size_bytes": file_size,
        "deletion_time_utc": filetime_to_iso(deletion_time),
        "r_file_exists": r_file.exists(),
        "sid": path.parent.name,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Parse Windows $Recycle.Bin $I metadata.")
    parser.add_argument("recycle_bin_dir", type=Path,
                        help="Path to mounted $Recycle.Bin (contains <SID> subdirs)")
    parser.add_argument("--output", "-o", type=Path, default=Path("deleted_files.csv"),
                        help="Output CSV path (default: deleted_files.csv)")
    args = parser.parse_args()

    root = args.recycle_bin_dir
    if not root.is_dir():
        print(f"Not a directory: {root}", file=sys.stderr)
        return 2

    i_files = list(root.rglob("$I*"))
    if not i_files:
        print("No $I files found.", file=sys.stderr)
        return 1

    rows = []
    for i_path in sorted(i_files):
        parsed = parse_i_file(i_path)
        if parsed:
            rows.append(parsed)

    if not rows:
        print("No parseable $I files.", file=sys.stderr)
        return 1

    with args.output.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=[
            "deletion_time_utc", "sid", "original_path", "size_bytes",
            "i_file", "r_file_exists", "version",
        ])
        writer.writeheader()
        rows.sort(key=lambda r: r["deletion_time_utc"])
        for row in rows:
            writer.writerow(row)

    print(f"Parsed {len(rows)} deleted file(s); output: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
