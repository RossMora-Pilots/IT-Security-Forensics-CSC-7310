# Contributing & PM Conventions (408-Forensics)

- Roadmap-first: Edit `ROADMAP.md` (Now/Next/Later, Milestones, Runbook)
- Evidence: `scripts/pm.sh run` → `artifacts/roadmap.json`, `docs/sessions.md`, `artifacts/state.json`
- Issues (optional): `scripts/pm.sh sync` (requires `gh` + `GH_TOKEN`)
- Labels: `roadmap`, `lane:now|next|later|unspecified`, `pilot:408-forensics`
- Secrets: never commit. Fetch via providers; scripts avoid echo; temp files use umask 077.
- Commit template: `.gitmessage.txt` + `.githooks/prepare-commit-msg` (run `git config core.hooksPath .githooks`)
- Forensic data: anonymize sample data; route disk images, memory dumps, pcaps through Git LFS.
