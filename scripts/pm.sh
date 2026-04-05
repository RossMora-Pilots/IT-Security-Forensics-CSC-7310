#!/usr/bin/env bash
# pm.sh — PM loop orchestrator for 408-Forensics
#
# Parses ROADMAP.md → artifacts/roadmap.json, optionally syncs to GitHub Issues,
# builds sessions index, and auto-commits artifacts.
#
# Commands:
#   run    — parse + sync + index + commit
#   parse  — ROADMAP.md → artifacts/roadmap.json
#   sync   — Push roadmap updates to GitHub Issues (requires GH_REPO + GH_TOKEN)
#   index  — Generate docs/sessions.md
#   all    — parse + sync + index + commit (with push if PM_PUSH=1)
#
# Environment variables:
#   PM_COMMIT   — Auto-commit artifacts (default: 1)
#   PM_PUSH     — Auto-push commits (default: 0)
#   GH_REPO     — GitHub repo slug (e.g., RossMora/408-forensics)
#   GH_TOKEN    — GitHub token (for Issues sync)

set -euo pipefail
umask 077

PM_COMMIT="${PM_COMMIT:-1}"
PM_PUSH="${PM_PUSH:-0}"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

mkdir -p artifacts docs

parse() {
    echo "[pm.sh] Parsing ROADMAP.md..."
    python3 scripts/roadmap/parse_roadmap.py ROADMAP.md --out artifacts/roadmap.json
    echo "[pm.sh] Wrote artifacts/roadmap.json"
}

sync_safe() {
    if [ -z "${GH_REPO:-}" ] || [ -z "${GH_TOKEN:-}" ]; then
        echo "[pm.sh] Skipping Issues sync (GH_REPO or GH_TOKEN not set)"
        return 0
    fi
    echo "[pm.sh] Syncing roadmap to GitHub Issues: $GH_REPO..."
    scripts/roadmap/sync_roadmap.sh ROADMAP.md "$GH_REPO" || {
        echo "[pm.sh] Sync failed (non-fatal)" >&2
    }
}

index_sessions() {
    echo "[pm.sh] Building sessions index..."
    python3 scripts/sessions/index_sessions.py --root . --out docs/sessions.md
    echo "[pm.sh] Wrote docs/sessions.md"
}

git_commit() {
    if [ "$PM_COMMIT" != "1" ]; then
        echo "[pm.sh] Auto-commit disabled (PM_COMMIT=0)"
        return 0
    fi
    if ! git diff --quiet HEAD -- artifacts/roadmap.json docs/sessions.md 2>/dev/null; then
        git add artifacts/roadmap.json docs/sessions.md 2>/dev/null || true
        git commit -m "chore(pm): refresh roadmap + sessions index

Why
- Evidence capture for PM loop

What
- artifacts/roadmap.json regenerated from ROADMAP.md
- docs/sessions.md regenerated from sessions/

Co-Authored-By: pm.sh <noreply@408-forensics>" || true
        if [ "$PM_PUSH" = "1" ]; then
            git push || true
        fi
    else
        echo "[pm.sh] No changes to commit"
    fi
}

case "${1:-run}" in
    run|all)
        parse
        sync_safe
        index_sessions
        git_commit
        ;;
    parse)
        parse
        ;;
    sync)
        sync_safe
        ;;
    index)
        index_sessions
        ;;
    *)
        echo "Usage: $0 {run|parse|sync|index|all}" >&2
        exit 2
        ;;
esac
