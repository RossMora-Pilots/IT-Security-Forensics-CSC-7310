#!/usr/bin/env bash
# verify_image_hash.sh — Verify MD5 and SHA-256 of a forensic image
#
# Usage: ./verify_image_hash.sh <image-path> <expected-md5> <expected-sha256>
#
# Exit codes:
#   0 = both hashes match (evidence integrity verified)
#   1 = hash mismatch (evidence may be compromised)
#   2 = tool error / invalid input
#
# Reference: CSC-7310 Lab 01 — Creating a Forensic Image (Week 4)

set -euo pipefail

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <image-path> <expected-md5> <expected-sha256>" >&2
    exit 2
fi

IMAGE="$1"
EXPECTED_MD5="$2"
EXPECTED_SHA256="$3"

if [ ! -f "$IMAGE" ]; then
    echo "ERROR: Image file not found: $IMAGE" >&2
    exit 2
fi

echo "Verifying: $IMAGE"
echo "File size: $(stat -c%s "$IMAGE" 2>/dev/null || stat -f%z "$IMAGE") bytes"
echo

echo "Computing MD5..."
ACTUAL_MD5=$(md5sum "$IMAGE" | awk '{print $1}')
echo "  Expected: $EXPECTED_MD5"
echo "  Actual:   $ACTUAL_MD5"

echo "Computing SHA-256..."
ACTUAL_SHA256=$(sha256sum "$IMAGE" | awk '{print $1}')
echo "  Expected: $EXPECTED_SHA256"
echo "  Actual:   $ACTUAL_SHA256"

echo

if [ "$ACTUAL_MD5" = "$EXPECTED_MD5" ] && [ "$ACTUAL_SHA256" = "$EXPECTED_SHA256" ]; then
    echo "VERIFIED: Both hashes match. Evidence integrity preserved."
    exit 0
else
    echo "FAILURE: Hash mismatch detected. Evidence may be compromised." >&2
    echo "Do not proceed with analysis until the discrepancy is resolved." >&2
    exit 1
fi
