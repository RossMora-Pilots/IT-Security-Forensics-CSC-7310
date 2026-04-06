# ROADMAP — IT Security Forensics Portfolio (Pilot 408)

This pilot tracks the end-to-end creation of a public, employer-facing GitHub portfolio for the **IT Security Forensics (CSC-7310)** course in the **Postgraduate Cybersecurity Certificate** program at **Cambrian College, Sudbury, Ontario**, Winter 2025, taught by **Dr. Maryam Ahmed**. The portfolio includes 7 lab submissions, a major investigation project, 12 weekly lecture summaries, runnable scripts, and a structured repository mirroring the pilot-008/010 conventions.

## Now

- [x] Repository scaffolding (AGENTS.md, CONTRIBUTING.md, .gitattributes, .gitignore, .gitleaks.toml)
- [x] Root README with program overview, skills matrix, course navigation
- [x] Course folder structure under `CC/Winter 2025/IT Security Forensics - Maryam Ahmed - CSC-7310`
- [x] Course README with employer-first Quick Start, Key Achievements, Skills, Navigation
- [x] Weekly summaries (Weeks 1, 2, 4-12 — Week 3 had no class)
- [x] Assignments: 7 labs indexed with objectives, methodology, findings, tools, evidence
- [x] Final Project write-up with scope, rubric alignment, deliverables
- [x] Evidence Index with screenshot conventions and captions
- [x] Scripts README with usage examples for forensic automation scripts
- [x] GitHub Actions: ci, gitleaks, markdownlint, pm-evidence, portfolio-ci (link-check + shellcheck)
- [x] Portfolio config.json with metrics (grade, labs completed, hours invested)
- [x] Architecture diagrams (Mermaid) for investigation workflow
- [x] Learning reflection document tying course content to employment goals
- [ ] Publish to public GitHub repository `RossMora/408-forensics-csc7310-cambrian`

## Next

- [x] Populate `screenshots/` with annotated lab evidence (48 verified captures from DOCX submissions)
- [x] Add Mermaid diagrams for each lab's investigation workflow
- [x] Convert student DOCX submissions to PDF (LibreOffice headless conversion)
- [x] Expand forensic script library (Python + PowerShell triage helpers)
- [ ] Add repo topics: `digital-forensics`, `dfir`, `incident-response`, `cambrian-college` *(requires GitHub UI)*
- [x] Add Issue/PR templates and contribution notes (CONTRIBUTING.md expanded)

## Later

- [x] GitHub Pages portfolio landing page (`index.html`)
- [ ] Integrate with program-level portfolio index (403 policies, 404 comm, 405 mobile, 406 cloud, 407 tooldev, 409 ethical, 410 malware)
- [x] Add sample forensic artifacts (synthetic $I files, test disk image in `sample_data/`)
- [x] Add YARA rules referenced in labs (`scripts-extra/forensic_indicators.yar`)
- [ ] Record 3–5 min walkthrough video *(requires screen recording)*
- [ ] Add Volatility plugins and custom Autopsy modules

## Completed — Employer Audit Cycle 2 Remediation (April 5–6, 2026)

- [x] Employer-perspective audit (19 findings across 3 tiers) → `docs/EMPLOYER_REVIEW_AUDIT.md`
- [x] Added specific forensic data values to all 7 lab write-ups
- [x] Rewrote CI pipeline from placeholder to 3-job lint/test/import-check
- [x] Added sample output blocks to SCRIPTS_README for all 4 scripts
- [x] Removed 4 placeholder screenshots; verified 48 real screenshots
- [x] Deduplicated root vs. course README content
- [x] Created synthetic evidence demo kit with pytest tests (12 tests, 100% pass)
- [x] Added forensic standard references (NIST SP 800-86, ISO 27037, SWGDE)
- [x] Expanded CONTRIBUTING.md to 139-line contributor guide
- [x] Added cumulative learning outcomes and instructor insights to WEEKLY_SUMMARY
- [x] Added certification pathway Mermaid diagram to LEARNING_REFLECTION
- [x] Created 5 sample YARA rules for forensic artifact classification
- [x] Fixed sessions.md placeholder
- [x] Added lab retrospectives ("What I Would Do Differently") for all 7 labs

## Completed — Employer Audit Cycle 3 Remediation (April 6, 2026)

- [x] Third employer-perspective audit (8 new + 5 carry-forward findings) → `docs/EMPLOYER_PERSPECTIVE_AUDIT_2026-04-06.md`
- [x] Fixed EVIDENCE_INDEX screenshot count 52→48
- [x] Replaced empty-file hashes with real test_image.dd hashes in SCRIPTS_README
- [x] Replaced retired CCFP certification with CFCE (IACIS) in LEARNING_REFLECTION
- [x] Added professional bio + contact section to course README
- [x] Added "What I'm Looking For" (target role + availability) to course README
- [x] Added concrete investigation findings to Final Project (4 tables + conclusion)
- [x] Added scripts-to-investigation pipeline Mermaid diagram to SCRIPTS_README
- [x] Improved 6 generic EVIDENCE_INDEX captions with specific tool/artifact details
- [x] Added Gantt timeline + pie chart to EVIDENCE_INDEX
- [x] Added chain-of-custody sequence diagram to Final Project
- [x] Upgraded index.html from text arrows to interactive CSS pipeline
- [x] Split 470-line assignments/README into 7 per-lab files + compact summary index
- [x] Surfaced 7 instructor insights from lecture transcripts (was 3)
- [x] Added skill-progression flowchart + cumulative table to WEEKLY_SUMMARY
- [x] Consolidated duplicate Quick Start / How to Review sections in course README
- [x] Fixed index.html diagram count 10→17

## Milestones (Definition of Done)

- [x] Public repo live and accessible; root README provides clear program overview
- [x] Course README renders cleanly with working image links and table of contents
- [x] Scripts present as files, embedded in README with Usage blocks, runnable with prechecks
- [x] No secrets or personal data beyond the owner's own student submissions
- [x] Portfolio registry updated; docs/Portfolio.md shows Pilot 408
- [x] All 10 labs (Weeks 1-12) and 1 project documented with outcomes

## Runbook

- PM loop: `scripts/pm.sh run` (parses ROADMAP → `artifacts/roadmap.json`, updates `docs/sessions.md`)
- Optional Issues sync: `GH_REPO=RossMora/408-forensics-csc7310-cambrian scripts/pm.sh sync`
- Auto-commit enabled by default; set `PM_COMMIT=0` to disable, `PM_PUSH=1` to push
- Portfolio phases: `scripts/portfolio/run.sh {immediate|short|followup|polish|enhance}`
