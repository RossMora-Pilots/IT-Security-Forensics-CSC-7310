# AGENTS.md - 408-Forensics

Marker: PROJECT_OK

## Overview

**Purpose:** Public-facing portfolio for IT Security Forensics (CSC-7310) course at Cambrian College, Winter 2025.

**Scope:** This directory and all subdirectories. Modeled after Pilot 008 and Pilot 010 templates.

---

## Pre-Flight Awareness Check

Before starting work on this pilot, start your session through the cross-pilot awareness wrapper:

```bash
/mnt/d/pilots/02001-Pilots-Aware-of-Other-Pilots/scripts/start_session.sh "$(basename $PWD)"
```

This runs the pre-flight awareness check, searches 300+ pilots for related work, flags potential duplicates, and writes a local awareness proof stamp. For deeper searches:

```bash
/mnt/d/pilots/02001-Pilots-Aware-of-Other-Pilots/scripts/search_pilots.sh "forensics"
```

---

## Quick Start

```bash
# 1. Check for related existing work
/mnt/d/pilots/02001-Pilots-Aware-of-Other-Pilots/scripts/start_session.sh "$(basename $PWD)"

# 2. Read ROADMAP.md for current tasks
cat ROADMAP.md

# 3. Run PM evidence loop
PM_COMMIT=1 PM_PUSH=0 scripts/pm.sh run
```

---

## Safety Rules

- Never commit secrets, exam keys, or student PII beyond the owner's own submissions
- Keep chain-of-custody documentation immutable once written
- Large forensic artifacts (disk images, memory dumps, pcaps) belong in Git LFS or external storage
- Update state files after completing work
- Create handover record when finishing
