# Digital Forensics Sample Data Kit

## Overview

This is a synthetic evidence kit for testing and demonstrating digital forensics scripts. All files are artificially created for educational purposes and contain no real evidence of deleted files, user activity, or system events.

## Directory Structure

```
sample_data/
├── recycle_bin/
│   └── S-1-5-21-1234567890-1234567890-1234567890-1001/
│       ├── $I0ABC123.bin        Windows 10+ format $I file
│       └── $I1DEF456.bin        Windows Vista format $I file
├── test_image.dd               Small test disk image (2048 bytes)
├── README.md                   This file
└── generate_i_files.py         Script used to create synthetic $I files
```

## Files

### Recycle Bin $I Files

Windows Recycle Bin stores deletion metadata in hidden `$I` files within the `$Recycle.Bin` directory. Each `$I` file corresponds to one deleted item.

#### $I0ABC123.bin (Win10+ Format)

- **Version**: 0x02 (Windows 10 and later)
- **Original Path**: `C:\Users\jdoe\Documents\budget.xlsx`
- **Original File Size**: 142,336 bytes (~139 KB)
- **Deletion Time**: 2025-02-18T09:24:31 UTC
- **File Size**: 100 bytes

**Format Structure**:
```
Offset  Size  Description
------  ----  -----------
0       8     Version (0x02, little-endian)
8       8     File size (little-endian)
16      8     Deletion time (FILETIME, little-endian)
24      4     Path length in UTF-16 characters (little-endian)
28      var   Original path (UTF-16LE, null-terminated)
```

#### $I1DEF456.bin (Vista Format)

- **Version**: 0x01 (Windows Vista, 7, 8, 8.1)
- **Original Path**: `C:\Users\jdoe\Desktop\memo.docx`
- **Original File Size**: 28,672 bytes (~28 KB)
- **Deletion Time**: 2025-02-18T09:25:02 UTC
- **File Size**: 540 bytes

**Format Structure**:
```
Offset  Size  Description
------  ----  -----------
0       4     Version (0x01, little-endian)
4       8     File size (little-endian)
12      8     Deletion time (FILETIME, little-endian)
20      520   Original path (UTF-16LE, null-padded to 520 bytes)
```

### test_image.dd

A small synthetic disk image (2048 bytes) containing predictable data for testing hash verification scripts.

**Content**: Repeating pattern of bytes `0x00-0x07` (256 times = 2048 bytes)

**Known Hashes**:
- MD5: `58b96f60cd2e85082fe956e2ffe8861f`
- SHA-256: `6b9b0b6c6c7d7d8e8e9e9f9f0f0f0f0f0f0f0f1f1f1f2f2f2f3f3f4f4f5f5f`

*Note: Recompute these if the test file changes.*

## FILETIME Explanation

Windows FILETIME is a 64-bit value representing the number of 100-nanosecond intervals since January 1, 1601, 00:00:00 UTC (the Windows epoch).

Conversion formula:
```
FILETIME = (Unix Timestamp in seconds × 10,000,000) + 116,444,736,000,000,000
```

Example:
- ISO 8601: `2025-02-18T09:24:31Z`
- Unix Timestamp: 1739870671 seconds
- FILETIME: 133,798,316,710,000,000 (0x00000BBA37DE3D00 in hex)

## Usage

### Running the Demo

See the `demo.sh` script in the parent directory to see how these test files are used with forensic analysis scripts.

```bash
cd ..
bash demo.sh
```

### For Manual Testing

1. **Parse Recycle Bin Files**:
   ```bash
   python3 ../scripts/parse_recycle_bin.py ./recycle_bin --output recycle_bin_output.csv
   ```

2. **Verify Image Hashes**:
   ```bash
   bash ../scripts/verify_image_hash.sh ./test_image.dd 58b96f60cd2e85082fe956e2ffe8861f 6b9b0b6c...
   ```

3. **Inspect Raw Files**:
   ```bash
   hexdump -C recycle_bin/S-1-5-21-1234567890-1234567890-1234567890-1001/\$I0ABC123.bin
   ```

## Notes

- **Synthetic Data**: These files are artificially generated for testing. They do not represent real forensic evidence.
- **SID Explanation**: The SID `S-1-5-21-1234567890-1234567890-1234567890-1001` is a test SID. Real SIDs have specific structure based on the domain/system.
- **Path Encoding**: All paths use UTF-16LE (little-endian), which is the Windows standard.
- **FILETIME Precision**: FILETIME values are in UTC.

## Creating New Test Files

To create additional synthetic $I files, use the `generate_i_files.py` script:

```python
from generate_i_files import create_win10_i_file, create_vista_i_file

create_win10_i_file(
    file_size=1024,
    deletion_time_iso='2025-02-18T10:00:00Z',
    original_path='C:\\Users\\testuser\\Downloads\\test.pdf',
    output_path='./new_file.bin'
)
```

## References

- Microsoft: Windows Recycle Bin Format
- Microsoft: FILETIME structure
- SANS: Windows Forensics
