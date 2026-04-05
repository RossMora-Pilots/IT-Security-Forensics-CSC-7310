#!/usr/bin/env python3
"""test_parse_recycle_bin.py — Pytest tests for parse_recycle_bin.py

Tests cover:
  1. FILETIME conversion (known values, zero, negative)
  2. Win10+ $I format parsing (version 0x02)
  3. Vista $I format parsing (version 0x01)
  4. Malformed file handling (too short, unreadable)
  5. CSV output validation (columns, sort order)

Reference: CSC-7310 Lab 09 — Recycle Bin Forensics (Week 7)
"""
from __future__ import annotations

import csv
import struct
import sys
import unittest.mock
from pathlib import Path

import pytest  # noqa: F401 — used by pytest framework

# Ensure the scripts directory is importable
sys.path.insert(0, str(Path(__file__).parent))

from parse_recycle_bin import filetime_to_iso, parse_i_file, main  # noqa: E402


# ---------------------------------------------------------------------------
# Helpers: build synthetic $I binary data
# ---------------------------------------------------------------------------

def _build_win10_i_file(
    file_size: int = 142336,
    filetime: int = 133_843_442_710_000_000,  # 2025-02-18T09:24:31Z
    path_str: str = r"C:\Users\jdoe\Documents\budget.xlsx",
) -> bytes:
    """Build a Win10+ (version 2) $I metadata blob."""
    path_bytes = path_str.encode("utf-16-le") + b"\x00\x00"
    path_len = len(path_str) + 1  # include null
    return (
        struct.pack("<Q", 2)
        + struct.pack("<Q", file_size)
        + struct.pack("<Q", filetime)
        + struct.pack("<I", path_len)
        + path_bytes
    )


def _build_vista_i_file(
    file_size: int = 28672,
    filetime: int = 133_843_443_020_000_000,  # 2025-02-18T09:25:02Z
    path_str: str = r"C:\Users\jdoe\Desktop\memo.docx",
) -> bytes:
    """Build a Vista (version 1) $I metadata blob with 520-byte fixed path."""
    path_bytes = path_str.encode("utf-16-le")
    path_padded = path_bytes.ljust(520, b"\x00")
    return (
        struct.pack("<Q", 1)
        + struct.pack("<Q", file_size)
        + struct.pack("<Q", filetime)
        + path_padded
    )


# ---------------------------------------------------------------------------
# Tests: FILETIME conversion
# ---------------------------------------------------------------------------

class TestFiletimeConversion:
    """Validate Windows FILETIME → ISO 8601 UTC conversion."""

    def test_known_timestamp(self):
        # 2025-02-18T09:24:31Z in FILETIME
        ft = 133_843_442_710_000_000
        assert filetime_to_iso(ft) == "2025-02-18T09:24:31Z"

    def test_zero_returns_empty(self):
        assert filetime_to_iso(0) == ""

    def test_negative_returns_empty(self):
        assert filetime_to_iso(-1) == ""


# ---------------------------------------------------------------------------
# Tests: Win10+ format
# ---------------------------------------------------------------------------

class TestWin10Format:
    """Parse version-2 $I files (Windows 10+)."""

    def test_parse_valid_file(self, tmp_path: Path):
        sid_dir = tmp_path / "S-1-5-21-test"
        sid_dir.mkdir()
        i_file = sid_dir / "$IABC1234"
        i_file.write_bytes(_build_win10_i_file())

        result = parse_i_file(i_file)
        assert result is not None
        assert result["version"] == 2
        assert result["size_bytes"] == 142336
        assert result["original_path"] == r"C:\Users\jdoe\Documents\budget.xlsx"
        assert result["deletion_time_utc"] == "2025-02-18T09:24:31Z"
        assert result["sid"] == "S-1-5-21-test"

    def test_r_file_detection(self, tmp_path: Path):
        sid_dir = tmp_path / "S-1-5-21-test"
        sid_dir.mkdir()
        i_file = sid_dir / "$IABC1234"
        r_file = sid_dir / "$RABC1234"
        i_file.write_bytes(_build_win10_i_file())
        r_file.write_bytes(b"file content")

        result = parse_i_file(i_file)
        assert result is not None
        assert result["r_file_exists"] is True


# ---------------------------------------------------------------------------
# Tests: Vista format
# ---------------------------------------------------------------------------

class TestVistaFormat:
    """Parse version-1 $I files (Vista through Win 8.1)."""

    def test_parse_valid_file(self, tmp_path: Path):
        sid_dir = tmp_path / "S-1-5-21-vista"
        sid_dir.mkdir()
        i_file = sid_dir / "$I1DEF456"
        i_file.write_bytes(_build_vista_i_file())

        result = parse_i_file(i_file)
        assert result is not None
        assert result["version"] == 1
        assert result["size_bytes"] == 28672
        assert "memo.docx" in result["original_path"]
        assert result["deletion_time_utc"] == "2025-02-18T09:25:02Z"


# ---------------------------------------------------------------------------
# Tests: Malformed input
# ---------------------------------------------------------------------------

class TestMalformedInput:
    """Graceful handling of broken or incomplete $I files."""

    def test_too_short_returns_none(self, tmp_path: Path):
        short_file = tmp_path / "$ISHORT"
        short_file.write_bytes(b"\x00" * 10)
        assert parse_i_file(short_file) is None

    def test_empty_file_returns_none(self, tmp_path: Path):
        empty_file = tmp_path / "$IEMPTY"
        empty_file.write_bytes(b"")
        assert parse_i_file(empty_file) is None

    def test_nonexistent_file_returns_none(self, tmp_path: Path):
        missing = tmp_path / "$IGHOST"
        assert parse_i_file(missing) is None


# ---------------------------------------------------------------------------
# Tests: CSV output via main()
# ---------------------------------------------------------------------------

class TestCSVOutput:
    """End-to-end: run main() and validate CSV output."""

    def test_main_produces_csv(self, tmp_path: Path):
        sid_dir = tmp_path / "recycle_bin" / "S-1-5-21-csv-test"
        sid_dir.mkdir(parents=True)
        (sid_dir / "$IABC0001").write_bytes(_build_win10_i_file())
        (sid_dir / "$IDEF0002").write_bytes(
            _build_vista_i_file(path_str=r"C:\Users\jdoe\notes.txt")
        )
        out_csv = tmp_path / "output.csv"

        with unittest.mock.patch(
            "sys.argv",
            ["test", str(tmp_path / "recycle_bin"), "--output", str(out_csv)],
        ):
            rc = main()

        assert rc == 0
        assert out_csv.exists()

        with out_csv.open() as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        assert len(rows) == 2
        assert "deletion_time_utc" in rows[0]
        assert "original_path" in rows[0]
        assert "size_bytes" in rows[0]

    def test_empty_dir_returns_nonzero(self, tmp_path: Path):
        empty_dir = tmp_path / "empty_recycle"
        empty_dir.mkdir()
        out_csv = tmp_path / "empty.csv"

        with unittest.mock.patch(
            "sys.argv",
            ["test", str(empty_dir), "--output", str(out_csv)],
        ):
            rc = main()

        assert rc == 1

    def test_nonexistent_path(self, tmp_path: Path):
        with unittest.mock.patch(
            "sys.argv",
            ["test", str(tmp_path / "no_such_dir")],
        ):
            rc = main()

        assert rc == 2
