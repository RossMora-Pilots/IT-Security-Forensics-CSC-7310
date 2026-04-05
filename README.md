# 408-Forensics — IT Security Forensics (CSC-7310) Portfolio

[![CI](https://github.com/<owner>/<repo>/actions/workflows/ci.yml/badge.svg)](https://github.com/<owner>/<repo>/actions/workflows/ci.yml)
[![Portfolio CI](https://github.com/<owner>/<repo>/actions/workflows/portfolio-ci.yml/badge.svg)](https://github.com/<owner>/<repo>/actions/workflows/portfolio-ci.yml)
[![Markdown Lint](https://github.com/<owner>/<repo>/actions/workflows/markdownlint.yml/badge.svg)](https://github.com/<owner>/<repo>/actions/workflows/markdownlint.yml)
[![Gitleaks](https://github.com/<owner>/<repo>/actions/workflows/gitleaks.yml/badge.svg)](https://github.com/<owner>/<repo>/actions/workflows/gitleaks.yml)
[![PM Evidence](https://github.com/<owner>/<repo>/actions/workflows/pm-evidence.yml/badge.svg)](https://github.com/<owner>/<repo>/actions/workflows/pm-evidence.yml)

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

**Quantified Results (Winter 2025, CSC-7310):**

| Metric | Value |
|---|---|
| Weeks of instruction completed | 11 of 12 (Week 3 cancelled) |
| NDG Forensics labs completed | **7 of 7** (100%) |
| Major investigations delivered | **1** (Project 1 — Windows forensic case) |
| Lectures attended & transcribed | 8 (approximately 16 hours of instruction) |
| Student submission size archived | 68 MB across 8 deliverables |
| Forensic tools hands-on | FTK Imager, Magnet AXIOM, NDG virtual labs |

**Investigation Lifecycle Covered End-to-End:**

Legal authority (4th Amendment / Section 8) → Chain of custody → Forensic imaging (bit-for-bit, hash-verified) → File system analysis (FAT, NTFS, ext3/4) → Artifact extraction (registry, recycle bin, email, mobile) → Timeline reconstruction (logs, event correlation) → Expert report.

---

## Skills Demonstrated

**Digital Forensics & Incident Response (DFIR):**

- Chain-of-custody documentation and evidence handling under ACLD/ASCLD lab-certification standards
- Forensic image acquisition with FTK Imager (bit-stream, write-blocked, hash-verified MD5/SHA-256)
- File system forensics across FAT16/32, NTFS, ext3/ext4 (MFT, $I30, slack space, unallocated)
- Windows Registry forensics (SAM, SYSTEM, SOFTWARE, NTUSER.DAT hives; ShellBags, UserAssist, RunMRU)
- Recycle Bin forensics ($Recycle.Bin, $I/$R files, deleted file recovery)
- Steganography detection and extraction (LSB, EOF injection, header analysis)
- Email header analysis (SMTP, POP3, IMAP, MAPI; sender spoofing, message tracking)
- Mobile device forensics (iOS/Android acquisition, app data extraction, SQLite artifacts)
- Network forensics and PCAP analysis (TCP/UDP reconstruction, protocol artifacts)
- Log analysis and timeline reconstruction (Windows Event Logs, Syslog, Apache access logs)
- Expert report writing (fact-finding → correlation → legally-defensible conclusions)

**Legal & Professional:**

- U.S. 4th Amendment / Canadian Charter Section 8 search-and-seizure framework
- ASCLD-Lab / ISO 17025 lab certification requirements
- Professional conduct expectations for forensic practitioners
- Civil vs. criminal vs. administrative case typing

**Tools Hands-On:**

- **Exterro FTK Imager 4.7.3** — forensic image acquisition, verification, logical export
- **Magnet AXIOM** — multi-platform artifact carving and timeline analysis
- **NDG Online Cybersecurity Labs** — NISGTC Forensics v2 curriculum
- **Autopsy / Sleuth Kit** (conceptual, via NDG labs)
- **Volatility** (memory forensics, conceptual)
- **Wireshark** (PCAP analysis, conceptual + Week 11 deep-dive)

---

## Repository Navigation

```
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
- **GitHub:** @RossMora
