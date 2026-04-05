#!/usr/bin/env bash
# sync_roadmap.sh — Sync ROADMAP.md checklist items to GitHub Issues
#
# Usage: sync_roadmap.sh <roadmap-path> <owner/repo>
# Requires: gh (GitHub CLI), GH_TOKEN in environment

set -euo pipefail

ROADMAP="${1:-ROADMAP.md}"
REPO="${2:-}"

if [ -z "$REPO" ]; then
    echo "Usage: $0 <roadmap-path> <owner/repo>" >&2
    exit 2
fi

if ! command -v gh >/dev/null 2>&1; then
    echo "gh (GitHub CLI) not found on PATH" >&2
    exit 2
fi

if [ -z "${GH_TOKEN:-}" ]; then
    echo "GH_TOKEN not set" >&2
    exit 2
fi

echo "[sync_roadmap] Repo: $REPO"
echo "[sync_roadmap] Roadmap: $ROADMAP"
echo "[sync_roadmap] (Stub) Would sync checklist items → GitHub Issues with labels: roadmap, lane:*, pilot:408-forensics"
# Future: parse ROADMAP.md, create/update issues with matching labels
