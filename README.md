# 408-Forensics — IT Security Forensics (CSC-7310) Portfolio

[![CI](https://github.com/RossMora-Pilots/IT-Security-Forensics-CSC-7310/actions/workflows/ci.yml/badge.svg)](https://github.com/RossMora-Pilots/IT-Security-Forensics-CSC-7310/actions/workflows/ci.yml)
[![Portfolio CI](https://github.com/RossMora-Pilots/IT-Security-Forensics-CSC-7310/actions/workflows/portfolio-ci.yml/badge.svg)](https://github.com/RossMora-Pilots/IT-Security-Forensics-CSC-7310/actions/workflows/portfolio-ci.yml)
[![Markdown Lint](https://github.com/RossMora-Pilots/IT-Security-Forensics-CSC-7310/actions/workflows/markdownlint.yml/badge.svg)](https://github.com/RossMora-Pilots/IT-Security-Forensics-CSC-7310/actions/workflows/markdownlint.yml)
[![Gitleaks](https://github.com/RossMora-Pilots/IT-Security-Forensics-CSC-7310/actions/workflows/gitleaks.yml/badge.svg)](https://github.com/RossMora-Pilots/IT-Security-Forensics-CSC-7310/actions/workflows/gitleaks.yml)
[![PM Evidence](https://github.com/RossMora-Pilots/IT-Security-Forensics-CSC-7310/actions/workflows/pm-evidence.yml/badge.svg)](https://github.com/RossMora-Pilots/IT-Security-Forensics-CSC-7310/actions/workflows/pm-evidence.yml)

> Public portfolio of digital forensics coursework from the **Postgraduate Cybersecurity Certificate** at **Cambrian College, Sudbury, Ontario**. Winter 2025. Instructor: **Dr. Maryam Ahmed**.

---

## 🚀 Quick Start for Hiring Managers

**If you have 5 minutes:**

- Read: [Key Achievements](#key-achievements) (below)
- Scan: [Course README](CC/Winter%202025/IT%20Security%20Forensics%20-%20Maryam%20Ahmed%20-%20CSC-7310/README.md) for the headline topics

**If you have 15 minutes:**

- Review: [Final Project — Forensic Investigation](CC/Winter%202025/IT%20Security%20Forensics%20-%20Maryam%20Ahmed%20-%20CSC-7310/FINAL_PROJECT_FORENSIC_INVESTIGATION.md)
- Browse: [Weekly Learning Path](CC/Winter%202025/IT%20Security%20Forensics%20-%20Maryam%20Ahmed%20-%20CSC-7310/WEEKLY_SUMMARY.md) (Weeks 1–12)

**If you have 30 minutes:**

- Deep-dive: [Lab Index](CC/Winter%202025/IT%20Security%20Forensics%20-%20Maryam%20Ahmed%20-%20CSC-7310/assignments/README.md) — 7 lab write-ups with methodology, findings, and tool outputs
- Read: [Learning Reflection](CC/Winter%202025/IT%20Security%20Forensics%20-%20Maryam%20Ahmed%20-%20CSC-7310/LEARNING_REFLECTION.md) — how the course maps to DFIR/SOC analyst roles

---

## Key Achievements

| Metric | Value |
|---|---|
| Labs completed | **7 / 7** (NDG Forensics v2) |
| Major investigation | **1** (Windows forensic case — Project 1) |
| Forensic tools used | FTK Imager 4.7.3, Autopsy, Magnet AXIOM |
| Scripts authored | **4** (Python, Bash, PowerShell) |
| Evidence screenshots | **48** indexed and captioned |

**Investigation lifecycle covered end-to-end:** Legal authority → Chain of custody → Forensic imaging → File system analysis → Artifact extraction → Timeline reconstruction → Expert report.

For the detailed skills matrix, tools list, and lab-by-lab breakdown, see the **[Course README](CC/Winter%202025/IT%20Security%20Forensics%20-%20Maryam%20Ahmed%20-%20CSC-7310/README.md)**.

---

## Repository Navigation

```text
408-Forensics/
├── CC/
│   └── Winter 2025/
│       └── IT Security Forensics - Maryam Ahmed - CSC-7310/
│           ├── README.md                              ← Course portfolio (start here)
│           ├── FINAL_PROJECT_FORENSIC_INVESTIGATION.md ← Major project write-up
│           ├── WEEKLY_SUMMARY.md                      ← All 12 weeks, topic-by-topic
│           ├── EVIDENCE_INDEX.md                      ← Screenshot catalog w/ captions
│           ├── SCRIPTS_README.md                      ← Automation scripts & usage
│           ├── LEARNING_REFLECTION.md                 ← Course → career mapping
│           ├── assignments/                           ← 7 labs × (NDG PDF + submission DOCX)
│           ├── scripts/                               ← student-authored forensic helpers
│           ├── scripts-extra/                         ← reference / external scripts
│           ├── screenshots/                           ← lab evidence captures
│           ├── transcripts/                           ← 8 lecture transcripts
│           └── project/                               ← Project 1 rubric + planning docs
├── .github/workflows/                                  ← CI, gitleaks, lint, portfolio-ci, pm-evidence
├── docs/                                               ← Generated sessions index, reference docs
├── portfolio/config.json                               ← Metrics, skills, references
├── scripts/                                            ← pm.sh, roadmap parser, portfolio generators
├── artifacts/                                          ← Generated roadmap.json, state.json
├── AGENTS.md, CONTRIBUTING.md, ROADMAP.md              ← Project management scaffolding
```

---

## Course Context

| Field | Value |
|---|---|
| **Institution** | Cambrian College of Applied Arts and Technology, Sudbury, Ontario |
| **Program** | Postgraduate Cybersecurity Certificate |
| **Course Code** | CSC-7310-11823-202501-002 |
| **Course Title** | IT Security Forensics |
| **Term** | Winter 2025 (January 9 – March 31, 2025) |
| **Instructor** | Dr. Maryam Ahmed |
| **Delivery** | Synchronous online lectures + NDG virtual labs |
| **Credential** | Ontario College Graduate Certificate (Level 8) |

This course is one of **11 courses** in the program. Related course portfolios in this series:

- `400-Fundamentals-of-IT` — Robert Comtois (CSC-7300)
- `401-CSEC-Infrastructure` — Dr. Maryam Ahmed (CSC-7302)
- `402-Business-Continuity` — Kevin Bryanton (CSC-7304)
- `403-Policies-Compliance` — Janice Cordeiro (CSC-7305)
- `404-Communications-Cybersecurity` — Shawn McLaren (CSC-7313)
- `405-Mobile-Wireless-Security` — Mohamed Jbeili (CSC-7306)
- `406-SysOps-Cloud-Security` — Aditya Palshikar (CSC-7308)
- `407-Tool-Development` — Travis Czech (CSC-7309)
- **`408-Forensics` — Dr. Maryam Ahmed (CSC-7310) ← this repo**
- `409-Ethical-Hacking` — Jeff Caldwell (CSC-7311)
- `410-Malware-Analysis` — Travis Czech (CSC-7312)

---

## Naming Conventions

- **Course folder:** `CC/<Term>/<Course Name - Instructor - Code>`
- **Screenshots:** `wkNN_<topic>_<index>.png` (e.g., `wk02_chain_of_custody_1.png`) or `ScreenshotN_<ShortDesc>.png`
- **Scripts:** student-authored in `scripts/`; external/reference in `scripts-extra/`
- **Assignments:** `Lab-NN-<Topic>-<NDG-Instructions|Submission>.<ext>`
- **Transcripts:** `week-NN-YYYY-MM-DD-transcript.txt`

---

## Privacy & Ethics Notes

- This portfolio contains the **author's own coursework** (Ross Moravec, A00322717).
- No classmate work or instructor proprietary materials beyond the publicly-distributed NDG lab instruction PDFs.
- Student ID is kept visible **only** in rubric/submission filenames for evidence authenticity; not sensitive per Cambrian College's public portfolio guidance.
- No real victim data, actual case files, or confidential investigation artifacts are included — labs use NDG-provided synthetic evidence only.
- Commits are scanned with [gitleaks](.gitleaks.toml) on every push to `main`.

---

## License & Attribution

- **Original writing, scripts, and analysis:** © 2025 Ross Moravec. Licensed for review, learning, and portfolio evaluation. Not for commercial redistribution without permission.
- **NDG Forensics v2 lab instruction PDFs:** Copyright Network Development Group (NDG) — included under Cambrian College academic license. Not redistributed under open-source terms.
- **Course content (lectures, transcripts):** Presented under fair-use for educational portfolio demonstration. Instructor credited throughout.

---

## Contact

- **Author:** Ross Moravec
- **Program:** Postgraduate Cybersecurity Certificate, Cambrian College (graduating 2025)
- **Focus areas:** DFIR, SOC analysis, infrastructure security, forensic automation
- **GitHub:** [@RossMora](https://github.com/RossMora)
- **LinkedIn:** [linkedin.com/in/ross-moravec](https://linkedin.com/in/ross-moravec)
