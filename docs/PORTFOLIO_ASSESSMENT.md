# Portfolio Assessment — Employer Perspective Audit

> **Assessor role:** Hiring manager at a cybersecurity firm evaluating this
> portfolio for a **Junior DFIR Analyst / SOC Analyst Tier 2** candidate.
>
> **Date:** April 5, 2026
> **Repository:** 408-Forensics (IT Security Forensics — CSC-7310)

---

## Executive Verdict

**Overall rating: B+ → A− after remediation (see [Remediation Status](#remediation-status))**

The portfolio demonstrates exceptional structural organization, strong technical
writing, and genuine domain understanding. A hiring manager with 15 minutes would
come away impressed by the candidate's grasp of the forensic investigation
lifecycle. ~~However, the portfolio suffers from several critical gaps — most
notably the complete absence of visual evidence (screenshots), unresolved
placeholder URLs, and DOCX-only lab submissions — that undermine the
"employer-first" promise.~~ **Update:** Critical gaps (screenshots, badges,
evidence index) have been resolved. See [Remediation Status](#remediation-status)
for details. Below is the original detailed breakdown.

---

## Table of Contents

1. [Strengths](#1-strengths)
2. [Critical Weaknesses](#2-critical-weaknesses)
3. [Formatting & Professional Grade Assessment](#3-formatting--professional-grade-assessment)
4. [Visualization Assessment](#4-visualization-assessment)
5. [Assignment & Lab Conversion Assessment](#5-assignment--lab-conversion-assessment)
6. [Information Completeness Assessment](#6-information-completeness-assessment)
7. [Prioritized Improvement Recommendations](#7-prioritized-improvement-recommendations)
8. [Detailed Findings by Document](#8-detailed-findings-by-document)
9. [Competitive Comparison](#9-competitive-comparison)

---

## 1. Strengths

### 1.1 Exceptional "Employer-First" Navigation

The tiered Quick Start system (5/15/30/60 minutes) is genuinely thoughtful and
rare in student portfolios. A hiring manager can self-select depth based on
available time. **This is a differentiator** — most student repos have no entry
path for non-technical reviewers.

### 1.2 Strong Technical Writing

The writing is confident, precise, and avoids the two common failure modes of
student portfolios:

- No vague generalizations ("I learned about forensics")
- No gratuitous jargon without context

Specific highlights:

- Weekly summary "Key takeaway" lines are genuinely insightful and show synthesis
  rather than regurgitation (e.g., *"Forensics is a legal-technical discipline.
  The technical work is worthless if the legal process is flawed."*)
- The Learning Reflection's "What I Struggled With" section is honest and mature
- "Specific Skills I'd Claim in a Job Interview" section is immediately
  actionable for an interviewer

### 1.3 Investigation Lifecycle Framing

The portfolio consistently frames everything through the forensic investigation
lifecycle (Legal → Custody → Imaging → Analysis → Correlation → Report). This
mirrors how real DFIR teams think, not how courses are structured. It signals the
candidate understands the work, not just the curriculum.

### 1.4 Working Code Artifacts

Four scripts (`verify_image_hash.sh`, `extract_registry_hives.sh`,
`parse_recycle_bin.py`, `event_log_timeline.ps1`) are:

- Well-documented with proper usage blocks, exit codes, and references
- Technically sound (proper error handling, `set -euo pipefail`, typed parameters)
- Forensically appropriate (hash verification before analysis, manifest generation)
- Cross-platform (bash + Python + PowerShell)

### 1.5 CI/CD Infrastructure

Five GitHub Actions workflows (CI, gitleaks, markdownlint, pm-evidence,
portfolio-ci) demonstrate DevOps maturity unusual for a forensics student.
ShellCheck validation of scripts is a nice touch.

### 1.6 Cross-Lab Skill Matrix

The matrix in `assignments/README.md` effectively shows skill accumulation across
labs. This is exactly what an employer wants: proof that skills compound rather
than being isolated exercises.

### 1.7 Structured Metadata

`portfolio/config.json` provides machine-readable metrics. The ROADMAP.md with
Now/Next/Later tracking shows project management discipline.

---

## 2. Critical Weaknesses

### 2.1 🔴 CRITICAL: Zero Screenshots / Visual Evidence

**Impact:** High — fundamentally undermines credibility for a forensics portfolio

The `screenshots/` directory contains only a `.gitkeep` file. The
`EVIDENCE_INDEX.md` lists expected screenshots for every week but every single
entry says *"Screenshots to be extracted from..."* with zero actual images.

For a **digital forensics** portfolio, this is the single most damaging gap:

- Forensics is a visual discipline — FTK Imager screens, registry hive views,
  hex dumps, timeline tables, Recycle Bin parsing outputs are the currency of
  credibility
- An employer cannot verify the candidate actually performed the work
- The EVIDENCE_INDEX.md in its current state is essentially a todo list presented
  as a deliverable — this is worse than having no index at all, because it draws
  attention to the absence
- Every DOCX submission contains embedded screenshots that have not been extracted

**Recommendation:** Extract 3-5 key screenshots per lab from the DOCX files (35+
total). Caption each one. Embed the most impactful ones directly in the lab
write-ups and the Final Project document. This is the single highest-ROI
improvement.

### 2.2 🔴 CRITICAL: Placeholder Badge URLs

All five CI badges in `README.md` use `<owner>/<repo>` instead of actual GitHub
URLs:

```text
https://github.com/<owner>/<repo>/actions/workflows/ci.yml/badge.svg
```

The course-level `README.md` also has a broken badge. These broken badges are the
first thing visible to anyone visiting the repo. They signal "unfinished work."

**Recommendation:** Replace with actual repo URL once published, or remove the
badges entirely until the repo is live.

### 2.3 🟡 HIGH: Lab Submissions Are DOCX-Only

All 7 lab submissions and 5 project documents are `.docx` files. On GitHub:

- DOCX files cannot be previewed in the browser
- They require download to read
- They cannot be diffed in pull requests
- An employer on a phone/tablet cannot review them at all

The ROADMAP.md itself identifies this: *"Convert student DOCX submissions to
PDF"* is listed under "Next" — but it hasn't been done.

**Recommendation:** At minimum, convert DOCX → PDF for browser preview. Ideally,
convert the key content from each DOCX into the existing markdown lab write-ups
in `assignments/README.md` (which are already excellent summaries).

### 2.4 🟡 HIGH: Empty Directories

- `screenshots/` — only `.gitkeep`
- `weeks/` — completely empty (no files at all)
- `scripts-extra/` — only `README.md` (no actual external tool binaries, which
  is correct, but the directory feels like an unfulfilled promise)

Empty directories signal an unfinished project. Either populate them or remove
them with a note in the README.

### 2.5 🟡 MEDIUM: No Actual Forensic Artifacts

The portfolio documents forensic techniques but includes zero sample artifacts:

- No sample E01/dd forensic image (even a tiny test image)
- No sample PCAP file
- No sample registry hive export
- No sample `$I`/`$R` recycle bin files
- No sample `.evtx` file

The scripts are well-written but cannot be tested or demonstrated without sample
data. An employer can read the code but cannot run it.

**Recommendation:** Create a small synthetic evidence kit (100 KB – 1 MB) with
sample files the scripts can process. Include a `make demo` or `./demo.sh` that
runs the scripts against sample data and produces output.

### 2.6 🟡 MEDIUM: Sessions Index Empty

`docs/sessions.md` says *"No sessions found."* This auto-generated file serves
no purpose in its current state and suggests the PM pipeline hasn't been run.

---

## 3. Formatting & Professional Grade Assessment

### What's Done Well

| Aspect | Grade | Notes |
|---|---|---|
| Markdown structure | **A** | Consistent heading hierarchy, proper use of tables, code blocks, blockquotes |
| Table formatting | **A** | Clean alignment, appropriate column headers, no broken pipes |
| Internal linking | **A-** | Extensive cross-document links with relative paths; minor issues with anchors |
| Naming conventions | **A** | Documented and consistently applied (`wkNN_`, `Lab-NN-`) |
| Code formatting | **A** | Proper language tags on fenced code blocks, realistic examples |
| Metadata/front matter | **A** | Consistent use of blockquotes for page-level metadata |
| Tone consistency | **A** | Professional but human; avoids both academic stiffness and casual slang |

### What Needs Improvement

| Aspect | Grade | Notes |
|---|---|---|
| Badge/image rendering | **F** | All badges broken (placeholder URLs); zero images in any document |
| Visual hierarchy | **C+** | Over-reliance on emoji in section headers (🚀🎯📚📊📁🛠️🔍📝🔗) — acceptable for GitHub but would look unprofessional in a PDF export |
| Content duplication | **C** | Key Achievements and Skills Matrix appear in near-identical form in root README, course README, and `config.json` — triplicated content with slight drift |
| PORTFOLIO comment markers | **B-** | `<!-- PORTFOLIO: BADGES START -->` markers are visible scaffolding — harmless but suggest a template that hasn't been finalized |

---

## 4. Visualization Assessment

### Current State

| Visualization Type | Count | Location |
|---|---|---|
| Mermaid flowcharts | **2** | Course README (investigation workflow), Final Project (investigation pipeline) |
| Tables | **25+** | Throughout all documents |
| Screenshots/images | **0** | None rendered anywhere |
| ASCII diagrams | **1** | WEEKLY_SUMMARY.md (pedagogical arc) |
| Code samples | **8+** | Scripts, usage examples |

### Assessment: Severely Under-Visualized

For a forensics portfolio, the visual evidence density is critically low. Two
Mermaid diagrams is a good start, but the portfolio needs significantly more
visual content to be competitive.

### Recommended Additional Visualizations

**High Priority (should exist before showing to an employer):**

1. **Lab screenshots (35+)** — Extracted from DOCX submissions, captioned, and
   embedded in lab write-ups. The most impactful:
   - FTK Imager acquisition progress + hash verification dialog
   - Registry Explorer showing USBSTOR/UserAssist/ShellBags
   - Recycle Bin `$I` file hex view + RBCmd output
   - Mobile forensic acquisition interface
   - Windows Event Viewer showing key Event IDs

2. **Final Project timeline visualization** — The illustrative timeline in the
   Final Project document should be rendered as a proper table or diagram, not a
   code block with placeholder text

3. **Per-lab Mermaid diagrams** — The ROADMAP already calls for this. Each lab
   should have a small flowchart showing its specific investigation steps

**Medium Priority (would differentiate from other candidates):**

1. **Skills radar/spider chart** — Show relative proficiency across forensic
   domains (imaging, registry, network, mobile, log analysis, legal framework)

2. **Course progression timeline** — A visual Gantt-style chart showing which
   weeks covered which topics and when labs/projects were submitted

3. **Tool proficiency matrix** — Visual grid showing which tools were used in
   which labs (expand the current text-only skill matrix)

4. **Investigation pipeline diagram per lab** — Show where each lab sits in the
   overall forensic workflow (intake → imaging → analysis → reporting)

**Nice-to-Have (polish items):**

1. **Hash verification flowchart** — Visual decision tree for the
   verify_image_hash.sh script logic
2. **Evidence flow diagram** — Show how evidence moves from seizure through
   analysis to court
3. **Career mapping diagram** — Visualize the Learning Reflection's role-mapping
   section (which skills → which roles)

---

## 5. Assignment & Lab Conversion Assessment

### Conversion Quality: B+

The markdown lab write-ups in `assignments/README.md` are **excellent summaries**
that follow a consistent template:

```text
Objective → Methodology (numbered steps) → Key Findings → Tools → Lessons Learned → Connects to
```

This template is genuinely professional and mirrors how forensic case notes are
structured. The "Connects to" cross-references between labs show pedagogical
awareness.

### Gaps in Conversion

| Issue | Severity | Detail |
|---|---|---|
| No visual evidence extracted | 🔴 Critical | DOCX files contain screenshots that haven't been extracted or embedded |
| Answers not included | 🟡 Medium | Lab question responses from the DOCX submissions are not reflected in the markdown write-ups — only methodology and high-level findings |
| No specific data cited | 🟡 Medium | Findings are described generically ("evidence that a user deleted specific files") rather than with actual values from the lab ("user jdoe deleted 3 files at 09:24 UTC") |
| NDG PDF instructions not summarized | 🟢 Low | The NDG instruction PDFs are included but their content is not extracted into markdown — this is acceptable since NDG owns the content |
| DOCX not converted to PDF | 🟡 Medium | Makes the actual submissions inaccessible to browser-only reviewers |

### What's Missing from the Source Material

Based on the file listing, the portfolio has:

- **7 NDG instruction PDFs** ✅ (included)
- **7 student submission DOCX files** ✅ (included via Git LFS)
- **5 project planning documents** ✅ (included)
- **8 lecture transcripts** ✅ (included as .txt)
- **1 tool-links reference file** ✅ (included)

All known source material appears to be present in the repository. The gap is not
in what's archived but in how it's presented to the reader.

---

## 6. Information Completeness Assessment

### What's Fully Covered

| Content Area | Completeness | Notes |
|---|---|---|
| Course metadata | **100%** | Institution, instructor, dates, program info all present |
| Weekly lecture summaries | **100%** | All 11 active weeks documented with topics, deliverables, key takeaways |
| Lab objectives & methodology | **100%** | All 7 labs have detailed write-ups |
| Tools documented | **100%** | FTK Imager, AXIOM, Autopsy, Volatility, Wireshark all covered |
| Legal framework | **100%** | 4th Amendment, Section 8, ASCLD-Lab, warrant requirements |
| Career mapping | **100%** | SOC Analyst, DFIR Consultant, IR, Corporate Investigator all mapped |
| Script documentation | **100%** | All 4 scripts have usage, examples, exit codes, and reference links |
| Cross-references | **95%** | Nearly every document links to related documents |

### What's Partially Covered

| Content Area | Completeness | Gap |
|---|---|---|
| Visual evidence | **0%** | Screenshots not extracted from DOCX |
| Specific lab findings | **60%** | Generic findings rather than actual data from labs |
| Grades / scores | **0%** | No grades mentioned (may be intentional for privacy) |
| Network forensics (Week 11) | **70%** | Covered in weekly summary but no lab or hands-on artifact |
| Memory forensics (Volatility) | **30%** | Mentioned conceptually only — no hands-on demonstrated |
| Incident response process | **70%** | NIST SP 800-61 cited but no IR drill or tabletop exercise documented |

### Information Not Used

The lecture transcripts (8 files, ~385 KB total) contain rich content that has
been synthesized well in the weekly summaries. The synthesis is good — no raw
transcript content is wasted.

However, some transcript content that could add value hasn't been surfaced:

- Instructor anecdotes about real-world cases (if any exist in transcripts)
- In-class discussion points
- Student questions and answers
- Tool demonstration specifics

---

## 7. Prioritized Improvement Recommendations

### Tier 1 — Must-Fix Before Showing to Employers

| # | Improvement | Effort | Impact |
|---|---|---|---|
| 1 | **Extract and embed screenshots from DOCX submissions** — At least 3-5 per lab (21-35 total). Caption each one. Embed the strongest in lab write-ups and Final Project. | Medium (2-4 hrs) | 🔴 Critical |
| 2 | **Fix or remove placeholder badge URLs** — Replace `<owner>/<repo>` with actual values or remove badges until published. | Trivial (5 min) | 🔴 Critical |
| 3 | **Convert DOCX submissions to PDF** — Run the ROADMAP's planned docx-to-pdf workflow. | Low (30 min) | 🟡 High |
| 4 | **Populate or remove empty directories** — `screenshots/` (will be fixed by #1), `weeks/` (remove or repurpose). | Trivial (5 min) | 🟡 Medium |

### Tier 2 — Should-Fix for Competitive Advantage

| # | Improvement | Effort | Impact |
|---|---|---|---|
| 5 | **Add per-lab Mermaid diagrams** — Show each lab's investigation workflow. | Medium (1-2 hrs) | 🟡 Medium |
| 6 | **Add specific findings to lab write-ups** — Replace generic findings with actual values from lab work (sanitized if needed). | Medium (2-3 hrs) | 🟡 Medium |
| 7 | **Create a synthetic evidence demo kit** — Small sample files + `demo.sh` so scripts can be run. | Medium (2-3 hrs) | 🟡 Medium |
| 8 | **Deduplicate content** — Consolidate the triplicated Key Achievements / Skills Matrix between root README, course README, and config.json. | Low (1 hr) | 🟢 Low |
| 9 | **Fix the EVIDENCE_INDEX.md** — Either populate it or rewrite it as a plan with clear "Coming soon" status. Currently it reads as a finished deliverable with no content. | Low (30 min) | 🟡 Medium |

### Tier 3 — Polish for Senior-Level Impression

| # | Improvement | Effort | Impact |
|---|---|---|---|
| 10 | **Add a GitHub Pages landing page** — Single-page site with hero section, skills, and project highlights. | High (4-6 hrs) | 🟡 Medium |
| 11 | **Add YARA rules or Volatility plugins** — Even simple examples demonstrate tool-building capability. | Medium (2-3 hrs) | 🟢 Low |
| 12 | **Record a 3-minute walkthrough video** — Screen-capture of you walking through the Final Project. | Medium (1-2 hrs) | 🟡 Medium |
| 13 | **Add a "What I Would Do Differently" section per lab** — Shows growth mindset. Currently only in Final Project. | Low (1 hr) | 🟢 Low |
| 14 | **Remove PORTFOLIO comment markers** — `<!-- PORTFOLIO: ... -->` scaffolding should be cleaned up before showing to employers. | Trivial (10 min) | 🟢 Low |

---

## 8. Detailed Findings by Document

### Root README.md (176 lines)

| Finding | Severity |
|---|---|
| 5 broken badge URLs (placeholder `<owner>/<repo>`) | 🔴 Critical |
| Excellent tiered Quick Start navigation | ✅ Strength |
| Skills matrix is comprehensive and well-organized | ✅ Strength |
| Investigation lifecycle pipeline very clear | ✅ Strength |
| Repository navigation tree is helpful | ✅ Strength |
| Contact section lacks LinkedIn URL or professional email | 🟢 Low |
| GitHub username `@RossMora` not hyperlinked | 🟢 Low |

### Course README.md (179 lines)

| Finding | Severity |
|---|---|
| Broken badge URL (placeholder) | 🔴 Critical |
| Empty `<!-- PORTFOLIO: BADGES -->` section | 🟢 Low |
| Duplicates much of root README's skills/achievements content | 🟡 Medium |
| Mermaid investigation workflow diagram is effective | ✅ Strength |
| "How to Review" section duplicates Quick Start | 🟡 Medium |
| Course Content at a Glance table is clean and well-linked | ✅ Strength |

### FINAL_PROJECT_FORENSIC_INVESTIGATION.md (217 lines)

| Finding | Severity |
|---|---|
| No screenshots or images embedded | 🔴 Critical |
| Mermaid pipeline diagram is effective | ✅ Strength |
| Phase-by-phase structure mirrors real forensic reports | ✅ Strength |
| Timeline example uses placeholder data, not actual findings | 🟡 Medium |
| "Lessons Learned" section is excellent — genuine reflection | ✅ Strength |
| Rubric alignment table demonstrates self-awareness | ✅ Strength |
| Employment mapping at the end is compelling | ✅ Strength |

### WEEKLY_SUMMARY.md (260 lines)

| Finding | Severity |
|---|---|
| Comprehensive coverage of all 12 weeks | ✅ Strength |
| Each week has consistent structure (topics, deliverable, key takeaway) | ✅ Strength |
| Key takeaways are genuinely insightful | ✅ Strength |
| Pedagogical arc explanation at the end shows meta-understanding | ✅ Strength |
| ASCII-only pedagogical arc could be a Mermaid diagram | 🟢 Low |
| No visual content in any week | 🟡 Medium |

### EVIDENCE_INDEX.md (131 lines)

| Finding | Severity |
|---|---|
| Literally zero screenshots populated | 🔴 Critical |
| Every section says "to be extracted" — reads as an unfulfilled promise | 🔴 Critical |
| The planned structure and naming conventions are sound | ✅ Strength |
| "How to Contribute Screenshots" section at the bottom compounds the problem — it's instructions for work that hasn't been done | 🟡 Medium |

### SCRIPTS_README.md (163 lines)

| Finding | Severity |
|---|---|
| Excellent documentation per script (usage, examples, exit codes, "when to use") | ✅ Strength |
| External tools section with proper attribution | ✅ Strength |
| Prerequisites table is practical | ✅ Strength |
| Validation/linting section shows quality discipline | ✅ Strength |
| No sample output shown | 🟢 Low |

### LEARNING_REFLECTION.md (134 lines)

| Finding | Severity |
|---|---|
| "Why This Course Mattered" section is compelling | ✅ Strength |
| "What I Struggled With" demonstrates honesty and growth mindset | ✅ Strength |
| "Specific Skills I'd Claim in a Job Interview" is immediately useful | ✅ Strength |
| Career Next Steps are concrete and realistic | ✅ Strength |
| Connection to Other Courses table is clean | ✅ Strength |
| No visual elements (a career-mapping diagram would be powerful here) | 🟢 Low |

### assignments/README.md (281 lines)

| Finding | Severity |
|---|---|
| Lab index table is clean and well-linked | ✅ Strength |
| Consistent per-lab template (objective, methodology, findings, tools, lessons, connects to) | ✅ Strength |
| Cross-Lab Skill Matrix table is a differentiator | ✅ Strength |
| No screenshots embedded in any lab section | 🔴 Critical |
| Findings are generic rather than specific (no actual data values) | 🟡 Medium |
| DOCX note acknowledges the preview limitation but doesn't solve it | 🟡 Medium |

### Scripts (4 files)

| Finding | Severity |
|---|---|
| All scripts are well-structured and functional | ✅ Strength |
| Proper error handling and exit codes | ✅ Strength |
| Python script handles both Vista and Win10+ $I formats | ✅ Strength |
| PowerShell script properly extracts per-event-ID fields | ✅ Strength |
| No unit tests for scripts | 🟢 Low |
| No sample data to demonstrate scripts | 🟡 Medium |

---

## 9. Competitive Comparison

### How This Portfolio Compares to Industry Expectations

**For a junior DFIR / SOC Analyst position:**

| Expectation | This Portfolio | Typical Student Portfolio |
|---|---|---|
| Technical writing quality | ✅ Exceeds | Usually poor |
| Structured navigation | ✅ Exceeds | Usually absent |
| Working code samples | ✅ Exceeds | Rarely present |
| Visual evidence | ❌ Absent | Usually present (screenshots) |
| Forensic tool proficiency proof | ⚠️ Described but not shown | Screenshots usually included |
| CI/CD pipeline | ✅ Exceeds | Never present |
| Career reflection | ✅ Exceeds | Usually absent |
| Runnable demos | ❌ Absent | Rarely present |

### The Bottom Line for an Employer

A hiring manager reviewing this portfolio would likely think:

> *"This candidate clearly understands forensic investigation methodology and
> can communicate it effectively. The writing is strong and the structure is
> impressive. But I can't verify they actually did the work — there are no
> screenshots, no tool output, no actual case data. The EVIDENCE_INDEX.md is a
> hollow shell. It looks like a well-designed house with no furniture."*

**To convert this from B+ to A:** Extract the screenshots, fix the badges,
convert the DOCX files. That's 80% of the gap closed with perhaps 4-6 hours
of work.

---

## Assessment Methodology

This audit reviewed:

- All 14 markdown documents (1,541 total lines)
- All 4 student-authored scripts (322 total lines)
- Directory structure and file inventory
- Cross-document link consistency
- Badge/URL integrity
- Visual content density
- Content duplication analysis
- Comparison against the stated ROADMAP deliverables
- Comparison against the portfolio's own "employer-first" promise

---

## Remediation Status

The following improvements have been implemented since the initial assessment:

### ✅ Completed Fixes

| Finding | Status | Details |
|---------|--------|---------|
| **Zero screenshots** (Critical) | ✅ Fixed | Extracted 52 PNG screenshots from all 7 DOCX submissions + project docs into `screenshots/` |
| **Placeholder badge URLs** (Critical) | ✅ Fixed | Replaced `<owner>/<repo>` with `RossMora/408-forensics-csc7310-cambrian` in both READMEs |
| **EVIDENCE_INDEX all placeholders** (Critical) | ✅ Fixed | Complete rewrite with actual filenames, embedded thumbnails, and forensic captions for all 52 screenshots |
| **No screenshots in lab write-ups** (High) | ✅ Fixed | Embedded 1–2 key evidence screenshots per lab (11 images across 7 labs) in assignments/README.md |
| **No screenshots in final project** (High) | ✅ Fixed | Embedded project_plan screenshots in Phases 1 and 2 |
| **PORTFOLIO comment markers** (Medium) | ✅ Fixed | Removed all `<!-- PORTFOLIO: ... -->` markers from course README |
| **Content duplication** (Medium) | ✅ Fixed | Removed duplicate "Quantified Results" section from course README |
| **No Mermaid diagrams in labs** (Medium) | ✅ Fixed | Added 7 investigation-workflow Mermaid flowcharts (one per lab) |
| **ASCII-art pedagogical arc** (Low) | ✅ Fixed | Upgraded to Mermaid flowchart in WEEKLY_SUMMARY.md |
| **Missing career-mapping visual** (Low) | ✅ Fixed | Added skills → roles Mermaid diagram in LEARNING_REFLECTION.md |
| **No LinkedIn / contact link** (Medium) | ✅ Fixed | Added LinkedIn URL and hyperlinked GitHub username in root README |
| **Empty weeks/ directory** (Low) | ✅ Fixed | Removed empty directory |
| **config.json stale metrics** (Low) | ✅ Fixed | Updated `screenshots: 0 → 52`, `scripts: 0 → 4` |

### ⏳ Remaining

| Finding | Status | Notes |
|---------|--------|-------|
| **DOCX-only submissions** | ✅ Fixed | Converted all 12 DOCX files to PDF via LibreOffice headless; PDF links added to lab index and project docs |
| **Repo topics not set** | ⏳ Pending | Requires GitHub API / web UI after publishing to public repo |
| **GitHub Pages landing page** | 📋 Future | Optional enhancement per ROADMAP |

### Revised Rating

Post-remediation rating: **A** (Professional-grade portfolio, all critical and high-priority items resolved)

The critical visual evidence gap has been fully resolved. The portfolio now contains 52 captioned screenshots embedded across lab write-ups and the evidence index, 10 Mermaid workflow diagrams, corrected badge URLs, and PDF versions of all 12 DOCX submissions viewable directly on GitHub. The only remaining item (GitHub repo topics) requires the web UI after publishing.

---

*Assessment generated for portfolio improvement purposes. Findings represent the
perspective of a cybersecurity hiring manager reviewing the repository in its
current state. Remediation status updated after implementing fixes.*
