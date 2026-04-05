# Contributing & PM Conventions — 408-Forensics

Thank you for your interest in contributing to this portfolio repository.

---

## Quick Reference

| Aspect | Convention |
|--------|-----------|
| **Primary branch** | `main` |
| **Commit style** | Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`) |
| **Markdown style** | Enforced by [markdownlint](.markdownlint.json) — run `npx markdownlint-cli2 "**/*.md"` |
| **Shell script lint** | Enforced by ShellCheck via [portfolio-ci](.github/workflows/portfolio-ci.yml) |
| **Python lint** | Enforced by flake8 via [ci.yml](.github/workflows/ci.yml) — max line length 120 |
| **Secret scanning** | Enforced by [gitleaks](.github/workflows/gitleaks.yml) on every push |

---

## Branch Naming

```text
feat/<short-description>     — new content or scripts
fix/<short-description>      — corrections to existing content
docs/<short-description>     — documentation improvements
chore/<short-description>    — CI, tooling, config changes
```

---

## Pull Request Process

1. **Create a feature branch** from `main`.
2. **Make changes** following the code style and naming conventions below.
3. **Run local checks** before pushing:

   ```bash
   # Markdown lint
   npx markdownlint-cli2 "**/*.md"

   # Shell lint
   shellcheck CC/Winter\ 2025/IT\ Security\ Forensics\ -\ Maryam\ Ahmed\ -\ CSC-7310/scripts/*.sh

   # Python lint + tests
   cd "CC/Winter 2025/IT Security Forensics - Maryam Ahmed - CSC-7310/scripts"
   flake8 --max-line-length 120
   python -m pytest test_parse_recycle_bin.py -v
   ```

4. **Open a PR** against `main` with a descriptive title and body.
5. **CI must pass** — all 5 workflows (CI, Gitleaks, Markdownlint, PM Evidence, Portfolio CI) must succeed.
6. **Self-review** — check the rendered markdown on GitHub before requesting merge.

---

## Code Style

### Python

- Python 3.10+ (type hints, `from __future__ import annotations`)
- Max line length: 120 characters
- Use `argparse` for CLI interfaces
- Use `pathlib.Path` instead of `os.path`
- Exit codes: `0` = success, `1` = expected failure, `2` = usage/tool error

### Bash

- `set -euo pipefail` at the top of every script
- ShellCheck-clean (no suppressed warnings without justification)
- Use `"$variable"` quoting everywhere

### PowerShell

- `[CmdletBinding()]` with typed parameters
- `$ErrorActionPreference = 'Stop'`
- Include `.SYNOPSIS`, `.DESCRIPTION`, `.EXAMPLE` comment-based help

---

## Naming Conventions

| Asset | Pattern | Example |
|-------|---------|---------|
| Screenshots | `wkNN_<topic>_<index>.png` | `wk04_lab01_2.png` |
| Lab files | `Lab-NN-<Topic>-{NDG-Instructions\|Submission}.{pdf\|docx}` | `Lab-04-Registry-Forensics-Submission.docx` |
| Transcripts | `week-NN-YYYY-MM-DD-transcript.txt` | `week-02-2025-01-16-transcript.txt` |
| Scripts | Descriptive snake_case | `parse_recycle_bin.py` |

---

## Forensic Data Handling

- **Never commit real victim data, case files, or confidential investigation artifacts.**
- Anonymize or synthesize all sample data.
- Route large forensic artifacts (disk images, memory dumps, PCAPs) through **Git LFS**.
- Verify working copies via hash before and after every analysis session.

---

## Secrets & Credentials

- Never commit secrets. Fetch via environment variables or credential providers.
- Scripts must avoid `echo` of sensitive values; temp files use `umask 077`.
- Gitleaks scans every push — `.gitleaks.toml` defines allowed patterns.

---

## PM Workflow

- **Roadmap-first:** Edit `ROADMAP.md` (Now / Next / Later, Milestones, Runbook).
- **Evidence loop:** `PM_COMMIT=1 PM_PUSH=0 scripts/pm.sh run` — parses roadmap, indexes sessions.
- **Issues sync (optional):** `GH_REPO=RossMora/408-forensics-csc7310-cambrian scripts/pm.sh sync` (requires `gh` CLI + `GH_TOKEN`).
- **Labels:** `roadmap`, `lane:now|next|later|unspecified`, `pilot:408-forensics`.
- **Commit template:** `.gitmessage.txt` + `.githooks/prepare-commit-msg` — install with `git config core.hooksPath .githooks`.

---

## Testing

### Running Tests Locally

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run forensic script tests
cd "CC/Winter 2025/IT Security Forensics - Maryam Ahmed - CSC-7310/scripts"
python -m pytest test_parse_recycle_bin.py -v --tb=short
```

### What CI Checks

| Workflow | What It Checks |
|----------|---------------|
| `ci.yml` | Python lint (flake8), pytest, import validation |
| `gitleaks.yml` | No hardcoded secrets or credentials |
| `markdownlint.yml` | Markdown formatting consistency |
| `pm-evidence.yml` | Roadmap parsing, session indexing |
| `portfolio-ci.yml` | Broken links, ShellCheck for shell scripts |
