# Digital Forensics Demo Kit - Quick Start Guide

## 📋 Project Overview

A complete digital forensics demonstration kit for the CSC-7310 IT Security Forensics portfolio, including:

- **Synthetic Windows Recycle Bin metadata files** for forensic analysis
- **Python forensic analysis scripts** for parsing and verification
- **Comprehensive pytest test suite** with 18 passing tests
- **Complete documentation** and usage examples

## 🚀 Quick Start

### 1. Installation

```bash
# Install development dependencies
cd D:\pilots\408-Forensics
pip install -r requirements-dev.txt
```

### 2. Run Tests

```bash
# Run the complete test suite
cd scripts
python -m pytest test_parse_recycle_bin.py -v

# Expected: All 18 tests pass in ~0.12 seconds
```

### 3. Analyze Sample Evidence

```bash
# Parse Recycle Bin metadata
python scripts/parse_recycle_bin.py "CC/Winter 2025/IT Security Forensics - Maryam Ahmed - CSC-7310/sample_data/recycle_bin"

# Output will show:
# - File 1: budget.xlsx (142 KB, deleted 2025-02-18T09:24:31Z)
# - File 2: memo.docx (28 KB, deleted 2025-02-18T09:25:02Z)
```

### 4. Verify Disk Image

```bash
# Verify test image integrity
bash scripts/verify_image_hash.sh \
  "CC/Winter 2025/IT Security Forensics - Maryam Ahmed - CSC-7310/sample_data/test_image.dd" \
  CFFD56D3F3E9B19AAD7F973F5611EF38 \
  907D13DB2BB9181D4D82F5B9ED322D33444E6C0073B650ACE8B1DCABA28FC421
```

## 📁 File Structure

```
D:\pilots\408-Forensics\
│
├── requirements-dev.txt                         ← Dependencies (pytest, flake8)
├── DEMO_KIT_SUMMARY.md                         ← Technical documentation
│
├── scripts/
│   ├── parse_recycle_bin.py                   ← Main forensic analysis script
│   ├── verify_image_hash.sh                   ← Hash verification script
│   └── test_parse_recycle_bin.py               ← 18 comprehensive pytest tests
│
└── CC/Winter 2025/IT Security Forensics - Maryam Ahmed - CSC-7310/
    └── sample_data/
        ├── README.md                           ← Sample data documentation
        ├── demo.sh                             ← Demo script for running tools
        ├── generate_i_files.py                 ← Script to create synthetic $I files
        ├── test_image.dd                       ← Test disk image (2 KB)
        │
        └── recycle_bin/
            └── S-1-5-21-1234567890-1234567890-1234567890-1001/
                ├── $I0ABC123.bin               ← Win10+ format $I file
                └── $I1DEF456.bin               ← Vista format $I file
```

## 🧪 Test Suite Results

```
TestFiletimeConversion ........................ 3/3 ✓ PASSED
TestVistaFormatParsing ........................ 2/2 ✓ PASSED
TestWin10FormatParsing ........................ 2/2 ✓ PASSED
TestMalformedFiles ............................ 4/4 ✓ PASSED
TestDirectoryScanning ......................... 3/3 ✓ PASSED
TestCSVOutput ................................. 2/2 ✓ PASSED
TestMainFunction .............................. 2/2 ✓ PASSED
─────────────────────────────────────────────────────────────
TOTAL ....................................... 18/18 ✓ PASSED
Execution Time: 0.12 seconds
```

## 📊 Sample Data Specifications

### $I0ABC123.bin (Windows 10+ Format)

- **Format Version**: 0x02
- **Size**: 100 bytes
- **Original File**: C:\Users\jdoe\Documents\budget.xlsx
- **Original Size**: 142,336 bytes
- **Deletion Time**: 2025-02-18T09:24:31Z (FILETIME: 133843442710000000)

### $I1DEF456.bin (Windows Vista Format)

- **Format Version**: 0x01
- **Size**: 540 bytes
- **Original File**: C:\Users\jdoe\Desktop\memo.docx
- **Original Size**: 28,672 bytes
- **Deletion Time**: 2025-02-18T09:25:02Z (FILETIME: 133843443020000000)

### test_image.dd

- **Size**: 2,048 bytes
- **Content**: Repeating pattern 0x00-0x07
- **MD5**: CFFD56D3F3E9B19AAD7F973F5611EF38
- **SHA-256**: 907D13DB2BB9181D4D82F5B9ED322D33444E6C0073B650ACE8B1DCABA28FC421

## 🔧 Scripts Reference

### parse_recycle_bin.py

**Purpose**: Parse Windows Recycle Bin metadata files

**Usage**:
```bash
python parse_recycle_bin.py <recycle_bin_path> [options]

Options:
  -o, --output FILE      Write CSV output to file (default: stdout)
  -f, --format FORMAT    Output format: csv or json (default: csv)
  -v, --verbose          Verbose output
```

**Features**:
- Supports Vista (0x01) and Windows 10+ (0x02) formats
- Automatic format detection
- FILETIME to ISO 8601 conversion
- CSV and JSON output
- Recursive directory scanning
- Error handling for malformed files

### verify_image_hash.sh

**Purpose**: Verify disk image integrity

**Usage**:
```bash
bash verify_image_hash.sh <image_file> <expected_md5> <expected_sha256>
```

**Features**:
- Computes MD5 and SHA-256 hashes
- Validates against expected values
- Clear pass/fail reporting
- Exit codes for automation

## 📚 Documentation

### Key Documents

1. **README.md** (in sample_data/)
   - Comprehensive guide to the sample data kit
   - Binary format specifications
   - FILETIME conversion formulas
   - Usage examples

2. **DEMO_KIT_SUMMARY.md**
   - Technical specifications
   - Detailed test descriptions
   - File manifest
   - Educational value overview

3. **test_parse_recycle_bin.py**
   - 18 comprehensive tests
   - Inline documentation
   - Test fixtures and examples

## 🎯 Learning Objectives

This demo kit teaches:

1. **Windows Forensics**
   - Recycle Bin structure and metadata
   - $I file format variations
   - FILETIME timestamp representation
   - UTF-16LE path encoding

2. **Python Development**
   - Binary file format parsing
   - Command-line tool design
   - Error handling and edge cases
   - CSV/JSON output generation

3. **Software Testing**
   - pytest framework usage
   - Test fixtures and temporary files
   - Edge case and error testing
   - Test-driven development

4. **Digital Forensics**
   - Evidence preservation
   - Hash verification
   - Metadata analysis
   - Timeline reconstruction

## 🔍 Forensic Analysis Examples

### Analyzing the Sample Recycle Bin

```bash
$ python scripts/parse_recycle_bin.py sample_data/recycle_bin

i_file,version,original_path,file_size_bytes,deletion_time_utc,full_path
$I0ABC123.bin,0x02,C:\Users\jdoe\Documents\budget.xlsx,142336,2025-02-18T09:24:31+00:00,...
$I1DEF456.bin,0x01,C:\Users\jdoe\Desktop\memo.docx,28672,2025-02-18T09:25:02+00:00,...
```

### Verifying Disk Image Integrity

```bash
$ bash scripts/verify_image_hash.sh sample_data/test_image.dd CFFD56D3F3E9B19AAD7F973F5611EF38 907D13DB2BB9181D4D82F5B9ED322D33444E6C0073B650ACE8B1DCABA28FC421

MD5: ✓ VERIFIED
SHA-256: ✓ VERIFIED
```

## 🛠️ Troubleshooting

### Tests Not Running

```bash
# Ensure pytest is installed
pip install pytest flake8

# Run from scripts directory
cd D:\pilots\408-Forensics\scripts
python -m pytest test_parse_recycle_bin.py -v
```

### Parse Script Not Found

```bash
# Ensure scripts directory is in Python path
export PYTHONPATH=D:\pilots\408-Forensics\scripts:$PYTHONPATH
python scripts/parse_recycle_bin.py --help
```

### Windows Path Issues

Use forward slashes or raw strings:
```bash
python scripts/parse_recycle_bin.py "sample_data/recycle_bin"
# or
python scripts/parse_recycle_bin.py r"sample_data\recycle_bin"
```

## 📖 References

- Microsoft: Windows Recycle Bin Format
- RFC 3339: Date and Time on the Internet
- Windows FILETIME Structure Documentation
- SANS Institute: Windows Forensics
- NIST: Digital Forensics Standards

## ✅ Verification Checklist

- [x] 2 synthetic $I metadata files created
- [x] 1 test disk image with known hashes
- [x] parse_recycle_bin.py script (9,048 bytes)
- [x] verify_image_hash.sh script (2,361 bytes)
- [x] 18 pytest tests (all passing)
- [x] requirements-dev.txt with dependencies
- [x] Comprehensive README documentation
- [x] Demo script for tool usage
- [x] Technical summary document
- [x] File generation script

## 📝 Summary

**Total Files Created**: 10  
**Total Size**: ~41 KB  
**Test Pass Rate**: 18/18 (100%)  
**Status**: ✓ Complete and verified

---

**For additional information, see DEMO_KIT_SUMMARY.md**
