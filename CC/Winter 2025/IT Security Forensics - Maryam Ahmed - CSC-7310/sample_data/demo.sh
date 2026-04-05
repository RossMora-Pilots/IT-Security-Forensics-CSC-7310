#!/usr/bin/env bash
# demo.sh — Run forensic scripts against synthetic sample data
# This script demonstrates the usage of forensic analysis tools on test data

set -euo pipefail

# Get the script directory
SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)/scripts"
SAMPLE_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "========================================="
echo "  Digital Forensics Demo"
echo "========================================="
echo ""
echo "Sample Data Location: $SAMPLE_DIR"
echo "Scripts Location: $SCRIPT_DIR"
echo ""

# Check if scripts exist
if [ ! -d "$SCRIPT_DIR" ]; then
    echo "Error: Scripts directory not found at $SCRIPT_DIR"
    exit 1
fi

# Demo 1: Parse Recycle Bin
echo "========================================="
echo "Demo 1: Parse Recycle Bin Metadata"
echo "========================================="
if [ -f "$SCRIPT_DIR/parse_recycle_bin.py" ]; then
    echo "Running: python3 $SCRIPT_DIR/parse_recycle_bin.py $SAMPLE_DIR/recycle_bin"
    echo ""
    python3 "$SCRIPT_DIR/parse_recycle_bin.py" "$SAMPLE_DIR/recycle_bin" --output "$SAMPLE_DIR/output_deleted_files.csv" || true
    echo ""
    if [ -f "$SAMPLE_DIR/output_deleted_files.csv" ]; then
        echo "Output:"
        cat "$SAMPLE_DIR/output_deleted_files.csv"
        echo ""
    fi
else
    echo "Warning: parse_recycle_bin.py not found. Skipping demo."
fi

echo ""

# Demo 2: Verify Image Hash
echo "========================================="
echo "Demo 2: Verify Image Hash"
echo "========================================="
if [ -f "$SCRIPT_DIR/verify_image_hash.sh" ]; then
    echo "Computing hashes for test image..."
    EXPECTED_MD5=$(md5sum "$SAMPLE_DIR/test_image.dd" | awk '{print $1}')
    EXPECTED_SHA256=$(sha256sum "$SAMPLE_DIR/test_image.dd" | awk '{print $1}')
    echo "MD5: $EXPECTED_MD5"
    echo "SHA-256: $EXPECTED_SHA256"
    echo ""
    echo "Running: bash $SCRIPT_DIR/verify_image_hash.sh $SAMPLE_DIR/test_image.dd $EXPECTED_MD5 $EXPECTED_SHA256"
    bash "$SCRIPT_DIR/verify_image_hash.sh" "$SAMPLE_DIR/test_image.dd" "$EXPECTED_MD5" "$EXPECTED_SHA256" || true
    echo ""
else
    echo "Warning: verify_image_hash.sh not found. Skipping demo."
fi

echo ""
echo "========================================="
echo "✓ All demos completed"
echo "========================================="
