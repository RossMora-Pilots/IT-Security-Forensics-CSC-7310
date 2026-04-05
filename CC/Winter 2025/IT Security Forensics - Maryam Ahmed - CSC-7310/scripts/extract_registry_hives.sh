#!/usr/bin/env bash
# extract_registry_hives.sh — Extract Windows Registry hives from a mounted forensic image
#
# Usage: ./extract_registry_hives.sh <mount-point> <output-dir>
#
# Extracts:
#   - SAM, SYSTEM, SOFTWARE, SECURITY (system-wide hives)
#   - NTUSER.DAT (per-user)
#   - UsrClass.dat (per-user shell artifacts)
#
# Produces a manifest with SHA-256 hashes for chain-of-custody.
#
# Reference: CSC-7310 Lab 04 — Windows Registry Forensics (Week 9)

set -euo pipefail

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <mount-point> <output-dir>" >&2
    echo "Example: $0 /mnt/evidence/working ./hives_out" >&2
    exit 2
fi

MOUNT="$1"
OUT="$2"

if [ ! -d "$MOUNT" ]; then
    echo "ERROR: Mount point not found: $MOUNT" >&2
    exit 2
fi

mkdir -p "$OUT"
MANIFEST="$OUT/manifest.txt"

{
    echo "Registry Hive Extraction Manifest"
    echo "================================="
    echo "Source mount: $MOUNT"
    echo "Extracted:    $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "Host:         $(hostname)"
    echo
} > "$MANIFEST"

extract_hive() {
    local src="$1"
    local dest_name="$2"
    if [ -f "$src" ]; then
        cp -p "$src" "$OUT/$dest_name"
        local hash
        hash=$(sha256sum "$OUT/$dest_name" | awk '{print $1}')
        echo "$dest_name  $hash  (from: ${src#"$MOUNT"})" >> "$MANIFEST"
        echo "Extracted: $dest_name ($hash)"
    else
        echo "MISSING: $src" >> "$MANIFEST"
        echo "Not present: $src" >&2
    fi
}

# System-wide hives
CONFIG="$MOUNT/Windows/System32/config"
extract_hive "$CONFIG/SAM" "SAM"
extract_hive "$CONFIG/SYSTEM" "SYSTEM"
extract_hive "$CONFIG/SOFTWARE" "SOFTWARE"
extract_hive "$CONFIG/SECURITY" "SECURITY"

# Per-user hives
if [ -d "$MOUNT/Users" ]; then
    for userdir in "$MOUNT"/Users/*/; do
        username=$(basename "$userdir")
        case "$username" in
            "All Users"|"Default"|"Default User"|"Public"|"desktop.ini") continue ;;
        esac
        extract_hive "$userdir/NTUSER.DAT" "NTUSER-${username}.DAT"
        extract_hive "$userdir/AppData/Local/Microsoft/Windows/UsrClass.dat" "UsrClass-${username}.dat"
    done
fi

echo
echo "Manifest written to: $MANIFEST"
echo "Done."
