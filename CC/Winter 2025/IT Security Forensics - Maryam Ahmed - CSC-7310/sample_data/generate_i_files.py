#!/usr/bin/env python3
"""
Generate synthetic Windows Recycle Bin $I metadata files for forensics testing.

Formats:
- Vista: version 0x01, max path 520 bytes
- Win10+: version 0x02, variable-length path with length field
"""
import struct
import os
from datetime import datetime, timezone

def windows_filetime_from_iso(iso_string):
    """Convert ISO 8601 datetime string to Windows FILETIME (100-nanosecond intervals since 1601-01-01)."""
    dt = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))
    # Windows epoch: January 1, 1601
    # Unix epoch: January 1, 1970
    # Difference: 116444736000000000 hundred-nanosecond intervals
    windows_epoch_diff = 116444736000000000
    unix_timestamp = dt.timestamp()
    filetime = int((unix_timestamp * 10000000) + windows_epoch_diff)
    return filetime

def create_vista_i_file(file_size, deletion_time_iso, original_path, output_path):
    """
    Create a Vista-format $I file (version 0x01).
    
    Structure:
    - Version (4 bytes LE): 0x01
    - File size (8 bytes LE)
    - Deletion time (8 bytes LE, FILETIME)
    - Original path (520 bytes, UTF-16LE null-padded)
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    filetime = windows_filetime_from_iso(deletion_time_iso)
    path_utf16 = original_path.encode('utf-16-le')
    
    # Pack the version and file size and time
    data = struct.pack('<I', 0x01)  # Version 0x01
    data += struct.pack('<Q', file_size)  # File size
    data += struct.pack('<Q', filetime)  # Deletion time
    
    # Add path padded to 520 bytes
    path_padded = path_utf16 + b'\x00' * (520 - len(path_utf16))
    data += path_padded[:520]
    
    with open(output_path, 'wb') as f:
        f.write(data)
    print(f"✓ Created Vista $I file: {output_path} ({len(data)} bytes)")
    return data

def create_win10_i_file(file_size, deletion_time_iso, original_path, output_path):
    """
    Create a Win10+ $I file (version 0x02).
    
    Structure:
    - Version (8 bytes LE): 0x02
    - File size (8 bytes LE)
    - Deletion time (8 bytes LE, FILETIME)
    - Path length (4 bytes LE): number of UTF-16 characters
    - Original path (variable length, UTF-16LE null-terminated)
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    filetime = windows_filetime_from_iso(deletion_time_iso)
    path_utf16 = original_path.encode('utf-16-le') + b'\x00\x00'  # null-terminate
    path_length = len(path_utf16) // 2  # Length in UTF-16 characters (including null terminator)
    
    # Pack header
    data = struct.pack('<Q', 0x02)  # Version 0x02 (8 bytes)
    data += struct.pack('<Q', file_size)  # File size
    data += struct.pack('<Q', filetime)  # Deletion time
    data += struct.pack('<I', path_length)  # Path length in UTF-16 chars
    data += path_utf16  # Variable-length path
    
    with open(output_path, 'wb') as f:
        f.write(data)
    print(f"✓ Created Win10+ $I file: {output_path} ({len(data)} bytes)")
    return data

def create_test_image():
    """Create a small test binary file for hash verification."""
    test_data = b'\x00\x01\x02\x03\x04\x05\x06\x07' * 256  # 2048 bytes of predictable data
    output_path = 'D:\\pilots\\408-Forensics\\CC\\Winter 2025\\IT Security Forensics - Maryam Ahmed - CSC-7310\\sample_data\\test_image.dd'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'wb') as f:
        f.write(test_data)
    print(f"✓ Created test image: {output_path}")
    return test_data

if __name__ == '__main__':
    base_path = 'D:\\pilots\\408-Forensics\\CC\\Winter 2025\\IT Security Forensics - Maryam Ahmed - CSC-7310\\sample_data'
    recycleBinPath = os.path.join(base_path, 'recycle_bin\\S-1-5-21-1234567890-1234567890-1234567890-1001')
    
    # Create Vista format $I file
    create_vista_i_file(
        file_size=28672,
        deletion_time_iso='2025-02-18T09:25:02Z',
        original_path='C:\\Users\\jdoe\\Desktop\\memo.docx',
        output_path=os.path.join(recycleBinPath, '$I1DEF456.bin')
    )
    
    # Create Win10+ format $I file
    create_win10_i_file(
        file_size=142336,
        deletion_time_iso='2025-02-18T09:24:31Z',
        original_path='C:\\Users\\jdoe\\Documents\\budget.xlsx',
        output_path=os.path.join(recycleBinPath, '$I0ABC123.bin')
    )
    
    # Create test image
    create_test_image()
    
    print("\n✓ All synthetic evidence files created successfully!")
