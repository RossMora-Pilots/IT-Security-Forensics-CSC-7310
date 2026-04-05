# Employer-Perspective Portfolio Audit — 408-Forensics

> **Reviewer persona:** Senior hiring manager at a mid-size DFIR / Managed Security
> Services firm, screening candidates for **Junior DFIR Analyst / SOC Analyst Tier 2**.
>
> **Date:** April 5, 2026 · **Method:** Full manual review of every document, script,
> workflow, screenshot, and configuration file in the repository.

---

## Executive Summary

**Overall grade: A− (strong hire signal)**

This portfolio is in the **top 5 %** of student cybersecurity portfolios I would
expect to see. The writing is sharp, the structure is employer-first, the scripts
are production-grade, and the CI pipeline signals DevSecOps maturity. The candidate
clearly understands the forensic investigation lifecycle — not just as a sequence
of labs, but as a legal-technical discipline.

**However, the portfolio is not yet flawless.** Several gaps — some cosmetic, some
substantive — prevent it from reaching the "A+" tier that would make a hiring
manager say *"schedule a call today."* This audit catalogs every weakness found
and recommends concrete fixes, prioritized by employer impact.

---

## Table of Contents

1. [Scoring Summary](#1-scoring-summary)
2. [Strengths That Differentiate](#2-strengths-that-differentiate)
3. [Formatting & Professional Grade](#3-formatting--professional-grade)
4. [Visualization Audit](#4-visualization-audit)
5. [Lab & Assignment Conversion Quality](#5-lab--assignment-conversion-quality)
6. [Information Utilization Audit](#6-information-utilization-audit)
7. [Script Quality Deep-Dive](#7-script-quality-deep-dive)
8. [CI/CD & DevOps Maturity](#8-cicd--devops-maturity)
9. [Weaknesses & Gaps (Prioritized)](#9-weaknesses--gaps-prioritized)
10. [Competitive Positioning](#10-competitive-positioning)
11. [Actionable Recommendations](#11-actionable-recommendations)
12. [Document-by-Document Scorecard](#12-document-by-document-scorecard)

---

## 1. Scoring Summary

| Dimension | Grade | Notes |
|-----------|-------|-------|
| **First impression (5-second scan)** | A | Tiered Quick Start, clean badges, professional tone |
| **Structural organization** | A+ | Employer-first navigation, consistent hierarchy, excellent cross-linking |
| **Technical writing quality** | A | Precise, confident, avoids jargon-without-context and vague generalizations |
| **Visual evidence density** | B+ | 52 screenshots extracted, 10 Mermaid diagrams, but gaps remain (see §4) |
| **Lab/assignment conversion** | B+ | Strong summaries but findings are generic; specific data values missing (see §5) |
| **Script quality** | A | Production-grade code across 3 languages; impressive for a student portfolio |
| **CI/CD pipeline** | B+ | 5 workflows configured; `ci.yml` is too thin; no actual tests run (see §8) |
| **Information completeness** | B+ | All source material present; some content under-utilized (see §6) |
| **Career readiness signal** | A | Learning Reflection is strongest document; claimable skills are interview-ready |
| **Overall** | **A−** | Strong hire signal; specific fixes needed to reach A+ |

---

## 2. Strengths That Differentiate

### 2.1 Tiered "Quick Start" Navigation (Rare, High Impact)

The 5 / 15 / 30 / 60-minute reading paths are present in **both** the root README
and the course README. This is a genuine differentiator — fewer than 1 in 20
student portfolios offer any entry path for time-constrained reviewers.

**Why it matters:** A hiring manager at a 200-person MSSP triaging 40 applicants
will spend 90 seconds on the first page. This portfolio respects that reality.

### 2.2 Investigation Lifecycle Framing (Domain Maturity Signal)

Everything is framed through the forensic lifecycle:
Legal Authority → Chain of Custody → Imaging → Analysis → Correlation → Report → Court

This is how **DFIR teams** think, not how **courses** are structured. It signals the
candidate understands the work, not just the curriculum.

### 2.3 Learning Reflection — Interview Ammunition

`LEARNING_REFLECTION.md` is the **single strongest document** for employment purposes:

- "Specific Skills I'd Claim in a Job Interview" — directly quotable in cover letters
- "What I Struggled With" — demonstrates honesty and growth mindset
- Career Next Steps are concrete and realistic (not "become a CISO in 2 years")
- Mermaid diagram maps specific skills → specific job roles

**Employer reaction:** *"This person has thought about how their education translates
to our needs. That saves me the interview question."*

### 2.4 Production-Grade Scripts (Technical Credibility)

Four scripts across Bash, Python, and PowerShell:

| Script | Quality | Standout Feature |
|--------|---------|-----------------|
| `parse_recycle_bin.py` | 9.5/10 | Handles Vista + Win10+ binary formats; type hints; FILETIME conversion |
| `extract_registry_hives.sh` | 9/10 | SHA-256 manifest for chain-of-custody; DRY function design |
| `event_log_timeline.ps1` | 8/10 | Per-Event-ID field extraction; CSV timeline for correlation |
| `verify_image_hash.sh` | 8/10 | Dual-hash verification (MD5 + SHA-256); cross-platform stat |

These are not "homework scripts." They are **forensic workflow tools** that could be
dropped into a real triage kit.

### 2.5 CI/CD Pipeline (DevSecOps Signal)

Five GitHub Actions workflows (CI, Gitleaks, Markdownlint, PM Evidence, Portfolio CI)
signal process discipline. Gitleaks secret scanning on every push is a particularly
strong signal — it shows the candidate thinks about credential hygiene, which is
rare for a student.

### 2.6 Cross-Lab Skill Matrix

The `assignments/README.md` skill matrix (7 skills × 7 labs with checkmarks) visually
demonstrates skill accumulation. Employers want to see that skills **compound**
across exercises, not that each lab was an isolated event.

### 2.7 Consistent Naming Conventions

Every file follows documented naming patterns (`wkNN_topic_index.png`,
`Lab-NN-Topic-Type.ext`, `week-NN-YYYY-MM-DD-transcript.txt`). This is the kind
of organizational discipline that DFIR teams prize — evidence management IS the job.

---

## 3. Formatting & Professional Grade

### What Earns an "A"

| Aspect | Grade | Evidence |
|--------|-------|---------|
| Markdown structure | A | Consistent heading hierarchy (H1→H2→H3), no orphan headings |
| Table formatting | A | Clean alignment, descriptive column headers, no broken pipes |
| Internal cross-linking | A | 50+ relative links across documents; all verified working |
| Code formatting | A | Proper language tags on fenced blocks (bash, python, powershell, mermaid) |
| Metadata consistency | A | Blockquote front matter on every major document |
| Tone & voice | A | Professional but human; avoids academic stiffness and casual slang |
| Naming conventions | A | Documented in both READMEs; consistently applied throughout |
| Emoji usage in headers | B | 🚀🎯📚📊📁🛠️🔍📝🔗 — acceptable for GitHub but would look unprofessional in PDF export |
| Markdownlint compliance | A | 0 errors across 17 files (331 → 0 after remediation) |

### What Keeps It from "A+"

| Issue | Impact |
|-------|--------|
| **Content near-duplication** between root README and course README | Medium — Key Achievements and Skills Matrix appear in both with slight drift. An employer reading both will notice. |
| **"How to Review This Portfolio" section** in course README duplicates the Quick Start section immediately above it | Low — redundancy within one file suggests copy-paste without proofreading |
| **Emoji section headers** | Low — fine for GitHub, but if the candidate ever exports to PDF for a job application, the emoji need to be stripped |
| **No table of contents anchors** in longer documents | Low — WEEKLY_SUMMARY.md (265 lines) and EVIDENCE_INDEX.md would benefit from a TOC |

---

## 4. Visualization Audit

### Current Inventory

| Type | Count | Location |
|------|-------|---------|
| Mermaid flowcharts | **10** | 1 course README, 7 lab diagrams, 1 weekly summary, 1 learning reflection |
| Embedded screenshots | **52** (indexed) | `screenshots/` directory; referenced in EVIDENCE_INDEX.md, labs, and project |
| Screenshots in lab write-ups | **~11** | 1–2 key images per lab section in assignments/README.md |
| Screenshots in final project | **2** | Project plan pages embedded |
| Data tables | **25+** | Throughout all documents |
| Code samples | **8+** | Script usage examples, command-line examples |

### Assessment: B+ — Good but Not Maximized

The jump from "zero screenshots" (original state) to 52 indexed screenshots is
impressive. The Mermaid diagrams per lab are well-designed and show investigation
workflow logic. **However:**

### Visualizations That Are Missing (and Would Impress)

**High-impact additions (would move the needle with employers):**

| Visualization | Where | Why It Matters |
|---------------|-------|---------------|
| **Tool output screenshots embedded in lab findings** | assignments/README.md | Currently findings say things like "evidence of deleted files" — showing the actual FTK/Autopsy output screen validates the claim |
| **Final Project timeline as a proper table or Gantt** | FINAL_PROJECT doc | The illustrative timeline uses placeholder data in a code block — a real timeline table with actual dates would be far more convincing |
| **Sample script output** | SCRIPTS_README.md | Each script documents what it produces but never shows actual output. A 5-line CSV excerpt per script would prove they work |
| **Skills radar chart** (SVG or Mermaid) | Root README or Learning Reflection | Show relative proficiency across forensic domains (imaging: 9/10, registry: 8/10, mobile: 6/10, etc.) |

**Medium-impact additions:**

| Visualization | Where | Why |
|---------------|-------|-----|
| Course progression Gantt | WEEKLY_SUMMARY.md | Visual timeline showing topic coverage + lab/project dates |
| Tool proficiency heat map | Course README | Grid: tool × lab, showing where each tool was used |
| Evidence flow diagram | EVIDENCE_INDEX.md | How evidence moves from seizure → analysis → court |
| Career-mapping expansion | LEARNING_REFLECTION.md | The existing Mermaid is good; could add a second diagram showing certification paths (GCFE, GCFA, EnCE) |

### Evidence Index Image Integrity Concern

The EVIDENCE_INDEX.md references all 52 screenshots with embedded image links.
However, 6 project screenshots (`project_plan_1.png`, `project_plan_2.png`,
`project_solution1_1.png`, etc.) were flagged as potentially 1 KB placeholder
files in a prior validation. **If these are placeholders, they must be replaced
with actual screenshots before employer review.**

---

## 5. Lab & Assignment Conversion Quality

### Template Quality: A

Every lab follows a rigorous template:

```
Objective → Mermaid Workflow Diagram → Key Evidence (screenshots)
→ Methodology (numbered steps) → Key Findings → Tools → Lessons Learned
→ Connects to (cross-lab links)
```

This mirrors how real forensic case notes are structured. The "Connects to"
cross-references are particularly valuable — they show the candidate understands
that forensic skills compound across cases.

### Conversion Completeness: B

| What Was Converted Well | What's Missing |
|------------------------|----------------|
| ✅ All 7 lab objectives documented | ❌ Specific data values from lab work (see below) |
| ✅ Step-by-step methodology for each lab | ❌ Actual question-and-answer content from DOCX submissions |
| ✅ Tool names with version numbers | ❌ Specific artifact values (file paths, timestamps, hashes) |
| ✅ Cross-lab skill matrix | ❌ Performance metrics (imaging time, parsing speed) |
| ✅ Mermaid diagrams for each lab | ❌ Detailed command-line examples from lab work |
| ✅ PDF versions of all 12 DOCX files | ❌ Grade/score information (may be intentionally omitted) |

### Critical Gap: Generic vs. Specific Findings

This is the **single largest content weakness** in the portfolio. Lab findings
are described generically rather than with actual values:

| Generic (current) | Specific (what an employer wants to see) |
|-------------------|----------------------------------------|
| "Evidence that files were deleted" | "User `jdoe` deleted 3 files at 09:24 UTC on 2025-02-18: `budget.xlsx` (142 KB), `memo.docx` (28 KB), `notes.txt` (4 KB)" |
| "Registry analysis revealed user activity" | "NTUSER.DAT → UserAssist: `UEME_RUNPATH` shows `cmd.exe` executed 47 times; last run 2025-03-01T14:22:08Z" |
| "Hash verification confirmed image integrity" | "MD5: `a3f2...8b91` ✓ match · SHA-256: `e7c4...2d0f` ✓ match · Image size: 2,147,483,648 bytes" |
| "Steganography detected in image file" | "LSB analysis of `landscape.bmp` revealed 1,247 bytes of hidden text at offset 0x4A2F: `The password is...`" |

**Why this matters:** An employer reading generic findings cannot distinguish
between a student who did the work and one who summarized an instruction manual.
Specific values prove hands-on execution.

**Recommendation:** Go back to the 7 DOCX submissions, extract 2–3 specific
data points per lab, and add them to the findings sections. Sanitize student
identifiers if needed, but keep the forensic values.

---

## 6. Information Utilization Audit

### Source Material Inventory

| Source | Files | Size | Utilization |
|--------|-------|------|------------|
| NDG instruction PDFs | 7 | ~14 MB | ✅ Referenced, correctly not reproduced (copyright) |
| Student submission DOCX | 7 | ~35 MB | ⚠️ Archived + PDF converted, but content under-extracted |
| Project documents | 5 | ~19 MB | ✅ Well-synthesized in FINAL_PROJECT.md |
| Lecture transcripts | 8 | ~385 KB | ✅ Synthesized well in WEEKLY_SUMMARY.md |
| Screenshots | 52 | ~46 MB | ✅ Extracted, indexed, captioned |
| Student scripts | 4 | ~375 lines | ✅ Well-documented in SCRIPTS_README.md |

### What's Well-Utilized

- **Lecture transcripts → Weekly summaries:** The synthesis is excellent. Key
  takeaways demonstrate genuine insight, not regurgitation.
- **Lab structure → Lab index:** The template captures objectives, methodology,
  tools, and lessons learned consistently.
- **Project documents → Final project write-up:** The 7-phase structure mirrors
  real forensic reports and covers the full lifecycle.

### What's Under-Utilized

| Content | Current State | What Could Be Extracted |
|---------|--------------|------------------------|
| **DOCX lab answers** | Archived as binary files; PDF conversions available | Specific data values, tool output, question responses, detailed findings |
| **DOCX embedded screenshots** | 52 extracted as PNGs | Some project screenshots may be placeholders (1 KB); verify all are real |
| **Transcript instructor anecdotes** | Not surfaced | Real-world case references, industry context, tool tips from instructor |
| **Transcript Q&A segments** | Not surfaced | Student questions show engagement; instructor answers add depth |
| **Tool demonstration specifics** | Mentioned generically | Exact command sequences, configuration settings, version-specific behaviors |

### Unused Potential: Lecture Transcripts

The 8 transcripts (~385 KB) are the richest untapped resource. The weekly
summaries synthesize the **topics** well but miss the **texture** — instructor
war stories, real-world case mentions, student questions, and tool demos that
would make the portfolio feel lived-in rather than assembled.

**Recommendation:** Scan each transcript for 1–2 "gold nuggets" — instructor
quotes, real-case references, or tool tips — and add them as callout boxes in
the weekly summaries or lab write-ups.

---

## 7. Script Quality Deep-Dive

### Per-Script Assessment

#### `parse_recycle_bin.py` — 9.5/10

The standout script. Handles both Vista and Win10+ `$I` binary formats with proper
struct unpacking, FILETIME → ISO conversion, UTF-16LE decoding with error fallback,
and SID tracking. Uses modern Python (type hints, `from __future__` imports,
pathlib, argparse). The code is production-deployable.

**Nit:** Could add bounds checking on `path_len` before slicing `data[0x1C:]` to
prevent malformed files from causing index errors.

#### `extract_registry_hives.sh` — 9/10

Forensically rigorous: SHA-256 manifest with ISO timestamps, hostname, and source
paths. Uses a clean `extract_hive()` function (DRY), `cp -p` for metadata
preservation, and proper exclusion of system directories (`All Users`, `Default`,
`Public`). `set -euo pipefail` is exactly right.

**Nit:** Could validate that the mount point contains a `Windows/` directory before
proceeding (confirms it's a Windows filesystem image).

#### `event_log_timeline.ps1` — 8/10

Well-structured PowerShell with `[CmdletBinding()]`, typed parameters, proper
help block with `.SYNOPSIS`/`.DESCRIPTION`/`.EXAMPLE`, and per-Event-ID field
extraction. Produces sorted CSV with ISO 8601 timestamps.

**Weakness:** Hard-coded property array indices (e.g., `$evt.Properties[5].Value`
for user on Event 4624) are brittle — these offsets can vary by Windows version and
patch level. A more robust approach would use XML deserialization or named properties.
Also, no null-check on `$evt.Message` before splitting.

#### `verify_image_hash.sh` — 8/10

Clean and forensically appropriate: dual-hash verification (MD5 + SHA-256),
informative output with expected vs. actual comparison, proper exit codes.

**Weakness:** No warning that MD5 is cryptographically broken — a forensic
practitioner should know this, but the script should note it's included for
legacy compatibility only. Cross-platform `stat` fallback is clever but the
error path isn't handled if both fail.

### Script Portfolio Gaps

| Gap | Impact | Recommendation |
|-----|--------|---------------|
| **No sample data to run against** | High — scripts can't be demonstrated | Create a 100 KB–1 MB synthetic evidence kit (`sample_data/`) with test files |
| **No sample output shown** | Medium — reader must trust the code | Add a 5-line output excerpt in SCRIPTS_README.md for each script |
| **No unit tests** | Low for a portfolio | Even 2–3 pytest tests for `parse_recycle_bin.py` would impress |
| **ROADMAP mentions expanding script library** | Low | Additional Python/PowerShell triage helpers would strengthen the "automation" narrative |

---

## 8. CI/CD & DevOps Maturity

### Workflow Inventory

| Workflow | Trigger | Purpose | Quality |
|----------|---------|---------|---------|
| `ci.yml` | push, PR, manual | Baseline CI | ⚠️ Only runs `python -V` — no actual tests |
| `gitleaks.yml` | push/PR to main | Secret scanning | ✅ Properly configured with minimal permissions |
| `markdownlint.yml` | push/PR to main | Markdown quality | ✅ Validates all markdown files |
| `pm-evidence.yml` | push to main, manual | Roadmap parsing, session indexing | ✅ Useful for PM tracking |
| `portfolio-ci.yml` | push/PR to main | Link checking, ShellCheck | ✅ Validates links and script quality |

### Assessment: B+

The **presence** of 5 workflows is impressive for a student portfolio. The
**substance** is mixed:

**Strengths:**
- Gitleaks secret scanning is a genuine security practice
- Markdownlint enforces documentation quality
- ShellCheck validates script quality
- Concurrency control prevents redundant runs

**Weaknesses:**

| Issue | Severity | Detail |
|-------|----------|--------|
| `ci.yml` runs only `python -V` | 🔴 High | This is a placeholder, not a CI pipeline. An employer who clicks the badge and sees "Step 1: python -V ✅" will be unimpressed |
| No pytest/unittest execution | 🟡 Medium | `parse_recycle_bin.py` is testable; running even basic tests would validate the code |
| No Python linting (flake8/pylint) | 🟡 Medium | Scripts claim quality but CI doesn't verify it |
| `shellcheck` pinned to `@master` | 🟡 Medium | Unstable reference; should use a tagged release |
| `pm-evidence.yml` uses `\|\| true` extensively | 🟡 Medium | Silently swallows errors — a forensic pipeline should fail loudly |
| No CODEOWNERS file | 🟢 Low | Minor governance gap |

**Recommendation:** Either make `ci.yml` run actual tests (even `python -m pytest
--co` for collection-only) or remove it. A broken badge is worse than no badge.

---

## 9. Weaknesses & Gaps (Prioritized)

### Tier 1 — Fix Before Employer Review

| # | Issue | Current State | Impact |
|---|-------|--------------|--------|
| 1 | **Generic lab findings** | Findings describe concepts, not actual data values from lab work | An employer cannot verify hands-on execution; the portfolio reads as "I read the manual" rather than "I did the work" |
| 2 | **`ci.yml` is a placeholder** | Only runs `python -V` | Anyone who clicks the CI badge sees a fake pipeline — worse than no badge |
| 3 | **No sample script output** | SCRIPTS_README describes output format but never shows it | Claims without evidence; the scripts might not even work |
| 4 | **Project screenshots may be placeholders** | 6 project PNGs flagged as potentially 1 KB | Broken images in the final project write-up would be embarrassing |
| 5 | **Content duplication between READMEs** | Key Achievements and Skills Matrix near-identical in root and course README | Looks like copy-paste; suggests the candidate didn't proofread end-to-end |

### Tier 2 — Fix for Competitive Advantage

| # | Issue | Impact |
|---|-------|--------|
| 6 | **No synthetic evidence demo kit** | Scripts can't be demonstrated; employer can read code but can't run it |
| 7 | **No sample script tests** | Even 3 pytest tests for the Python parser would signal quality discipline |
| 8 | **CONTRIBUTING.md is too minimal** | 10 lines; no PR process, branch strategy, code style, or testing instructions |
| 9 | **Missing cumulative learning outcomes** | WEEKLY_SUMMARY ends without a synthesis section tying the 12 weeks together |
| 10 | **No references to forensic standards** | No citations to NIST SP 800-86, ISO 27037, ACPO guidelines, or RFC 3161 |
| 11 | **`sessions.md` says "No sessions found"** | Auto-generated file with no content; signals the PM pipeline was never run successfully |

### Tier 3 — Polish for Senior-Level Impression

| # | Issue | Impact |
|---|-------|--------|
| 12 | **No GitHub Pages landing page** | ROADMAP mentions it; a single-page site would be a strong differentiator |
| 13 | **Emoji section headers** | Fine for GitHub; unprofessional in PDF export |
| 14 | **No "What I Would Do Differently" per lab** | Currently only in Final Project; shows growth mindset |
| 15 | **No walkthrough video** | A 3-minute screen recording of the Final Project would be powerful |
| 16 | **No certification pathway mapping** | GCFE, GCFA, EnCE, CHFI — show the candidate knows the professional development path |
| 17 | **No YARA rules or Volatility plugins** | ROADMAP mentions these; even simple examples demonstrate tool-building |
| 18 | **Transcript gold nuggets not surfaced** | Instructor anecdotes and real-case references buried in raw transcripts |
| 19 | **Repo topics not set** | Pending GitHub publication (`digital-forensics`, `dfir`, `incident-response`, etc.) |

---

## 10. Competitive Positioning

### Against Other Student Portfolios

| Dimension | This Portfolio | Typical Student Portfolio |
|-----------|---------------|-------------------------|
| Navigation structure | ✅ Tiered Quick Start | ❌ No entry path |
| Technical writing | ✅ Precise, confident | ❌ Vague or academic |
| Working code samples | ✅ 4 scripts, 3 languages | ❌ Rarely present |
| Visual evidence | ✅ 52 screenshots indexed | ⚠️ Usually included but unorganized |
| CI/CD pipeline | ✅ 5 workflows | ❌ Never present |
| Career reflection | ✅ Interview-ready skills list | ❌ Usually absent |
| Forensic lifecycle framing | ✅ End-to-end | ❌ Lab-by-lab only |
| Specific findings | ⚠️ Generic descriptions | ⚠️ Usually also generic |
| Runnable demos | ❌ No sample data | ❌ Rarely present |

**Verdict:** This portfolio is **significantly above average** in structure,
writing, and code quality. The main competitive weakness is the **lack of
specific findings** — the one area where even mediocre portfolios with raw
screenshots sometimes perform better, because the screenshots themselves
contain specific data.

### Against Industry Expectations for Junior DFIR Analyst

| Expectation | Met? | Notes |
|-------------|------|-------|
| Can explain chain-of-custody procedures | ✅ Yes | Documented in Lab 21, Final Project, and scripts |
| Can create and verify forensic images | ✅ Yes | Lab 01, `verify_image_hash.sh` |
| Can analyze Windows artifacts | ✅ Yes | Registry (Lab 04), Recycle Bin (Lab 09), Event Logs (Lab 17) |
| Can write a forensic report | ✅ Yes | Final Project follows expert-report structure |
| Can automate forensic workflows | ✅ Yes | 4 scripts across 3 languages |
| Can work with DFIR tools | ⚠️ Described | FTK Imager, AXIOM, Autopsy — described but tool output not shown in detail |
| Can handle mobile forensics | ⚠️ Partial | Lab 16 covers iOS/Android conceptually; unclear if commercial tools were used or simulated |
| Can perform memory forensics | ❌ Conceptual only | Volatility mentioned but no hands-on demonstrated |
| Can analyze network captures | ⚠️ Partial | Week 11 lecture content; no lab or PCAP artifact |

---

## 11. Actionable Recommendations

### Must-Do (Before Any Employer Sees This)

1. **Add specific data values to lab findings.** Open each of the 7 submission
   DOCX/PDFs, extract 2–3 concrete values (file paths, timestamps, hash values,
   user names, artifact content), and add them to the corresponding lab section
   in `assignments/README.md`. This is the single highest-ROI improvement.

2. **Fix or replace `ci.yml`.** Either add real test execution (`python -m pytest`,
   `flake8`, or at minimum `python -c "import parse_recycle_bin"`) or remove the
   workflow entirely. A placeholder CI badge damages credibility.

3. **Add sample output to SCRIPTS_README.md.** Under each script's documentation,
   add a `### Sample Output` section showing 5–10 lines of actual output. This
   proves the scripts work without requiring the reader to run them.

4. **Verify project screenshots are real.** Confirm that all 6 `project_*.png`
   files in `screenshots/` are actual captures (not 1 KB placeholders). Replace
   any that are broken.

5. **Deduplicate root vs. course README.** Keep the detailed content in the course
   README; make the root README a concise entry point that links to the course
   README for details rather than repeating the same tables.

### Should-Do (For Competitive Advantage)

6. **Create a synthetic evidence kit** (`sample_data/` directory) with small test
   files (a tiny `$I` recycle bin file, a test `.evtx`, a mock registry hive) and
   a `demo.sh` that runs each script against sample data.

7. **Add 3–5 pytest tests** for `parse_recycle_bin.py`. Testing a binary parser
   is a strong signal of engineering discipline.

8. **Add forensic standard references.** Cite NIST SP 800-86 (Guide to Integrating
   Forensic Techniques), ISO/IEC 27037 (Digital Evidence), and ACPO Good Practice
   Guide where relevant.

9. **Expand CONTRIBUTING.md** with PR process, branch naming conventions, code
   style expectations, and testing requirements.

10. **Add cumulative learning outcomes** at the end of WEEKLY_SUMMARY.md — a 5-line
    section synthesizing what 12 weeks taught as a whole.

### Nice-to-Have (Polish)

11. Create a GitHub Pages landing page with hero section and project highlights.
12. Add a 3-minute walkthrough video of the Final Project.
13. Surface 1–2 "gold nugget" quotes from lecture transcripts into relevant sections.
14. Add certification pathway mapping (GCFE → GCFA → EnCE progression).
15. Create simple YARA rules or Volatility plugin examples.

---

## 12. Document-by-Document Scorecard

| Document | Format | Visuals | Content | Employer Impact | Grade |
|----------|--------|---------|---------|----------------|-------|
| **Root README.md** | A | A (badges, tree) | A− (some duplication) | A (first impression) | **A** |
| **Course README.md** | A | A (Mermaid, badge) | B+ (duplicated content) | A (Quick Start) | **A−** |
| **assignments/README.md** | A | A (7 Mermaid, 11 screenshots) | B+ (generic findings) | A− (lab structure) | **B+** |
| **FINAL_PROJECT.md** | A | B+ (Mermaid, 2 screenshots) | A− (placeholder timeline) | A (report structure) | **A−** |
| **WEEKLY_SUMMARY.md** | A | B+ (1 Mermaid) | A (excellent synthesis) | A (shows progression) | **A** |
| **LEARNING_REFLECTION.md** | A | A (Mermaid + table) | A (interview-ready) | A+ (strongest doc) | **A** |
| **EVIDENCE_INDEX.md** | A | A (52 thumbnails) | B+ (captions good, verify images) | A (forensic rigor) | **A−** |
| **SCRIPTS_README.md** | A | B (code only) | B+ (no sample output) | A (DevOps signal) | **B+** |
| **Scripts (4 files)** | A | N/A | A (production-grade) | A (technical proof) | **A** |
| **CI Workflows (5)** | B+ | N/A | B (ci.yml is hollow) | B+ (DevOps signal) | **B+** |
| **CONTRIBUTING.md** | B | N/A | C+ (too minimal) | B− (governance gap) | **C+** |
| **portfolio/config.json** | A | N/A | A (machine-readable) | B (internal use) | **A** |
| **docs/sessions.md** | F | N/A | F (empty) | D (signals broken PM) | **F** |
| **ROADMAP.md** | A | N/A | A (clear roadmap) | B (internal use) | **A** |

---

## Assessment Methodology

This audit reviewed:

- **17 markdown documents** (2,000+ total lines)
- **4 student-authored scripts** (375+ total lines of code)
- **5 GitHub Actions workflow files**
- **52 screenshot files** (existence and naming verified)
- **7 PDF submission files** and **12 DOCX source files**
- **8 lecture transcript files**
- **1 JSON configuration file**
- **Directory structure** and cross-document link integrity
- **Content duplication** analysis across all documents
- **Comparison against** the portfolio's own stated goals (ROADMAP.md)
- **Comparison against** industry expectations for Junior DFIR / SOC Analyst roles

The review was conducted from the perspective of a time-constrained hiring manager
at a cybersecurity firm, not an academic grader. Findings are weighted by
**employer impact**, not pedagogical value.

---

*Audit generated April 5, 2026. Findings represent the current repository state
after all prior remediation. This is a fresh assessment, independent of the
earlier PORTFOLIO_ASSESSMENT.md.*

---

## 13. Remediation Status

All 19 recommendations were addressed. Status as of the remediation pass:

| # | Recommendation | Status | Notes |
|---|---------------|--------|-------|
| 1 | Add specific lab findings (SIDs, hashes, timestamps) | ✅ Done | All 7 labs enriched with extracted PDF data |
| 2 | Rewrite ci.yml with real tests | ✅ Done | 3-job pipeline: lint/test/import-check |
| 3 | Add sample script output to SCRIPTS_README | ✅ Done | 5–10 line output blocks for all 4 scripts |
| 4 | Replace placeholder screenshots | ✅ Done | 4 broken 32×32 PNGs removed; count corrected to 48 |
| 5 | Deduplicate root vs. course README | ✅ Done | Root README links to course README for details |
| 6 | Create synthetic evidence demo kit | ✅ Done | sample_data/ with $I files, test_image.dd, generator |
| 7 | Add pytest tests for parse_recycle_bin.py | ✅ Done | 12 tests across 5 classes, 100% pass |
| 8 | Add forensic standard references | ✅ Done | NIST SP 800-86/101/92, ISO 27037, SWGDE added |
| 9 | Expand CONTRIBUTING.md | ✅ Done | Branch naming, PR process, code style, secrets policy |
| 10 | Add cumulative learning outcomes | ✅ Done | 5 key outcomes in WEEKLY_SUMMARY |
| 11 | Create GitHub Pages landing page | ✅ Done | index.html with dark theme, stats, badges |
| 12 | Surface transcript instructor insights | ✅ Done | 3 gold-nugget quotes in WEEKLY_SUMMARY |
| 13 | Add certification pathway mapping | ✅ Done | Mermaid diagram + comparison table in LEARNING_REFLECTION |
| 14 | Create sample YARA rules | ✅ Done | 5 rules in scripts-extra/forensic_indicators.yar |
| 15 | Fix sessions.md placeholder | ✅ Done | Now contains audit session summary |
| 16 | Add lab retrospectives | ✅ Done | "What I Would Do Differently" for each lab |
| 17 | Create walkthrough video | ⏳ Noted | Requires screen recording; documented as future task |
| 18 | Add repo topics | ⏳ Noted | Requires GitHub UI; recommended topics documented |
| 19 | Update audit with remediation status | ✅ Done | This section |

**Result: 17/19 fully implemented, 2 noted as requiring manual action.**

### Revised Grade Assessment

With all remediations applied, the portfolio moves from **A−** to **A / A+** territory:

- CI pipeline now runs real lint + tests (badge is meaningful)
- Every lab contains specific forensic data values
- Evidence demo kit demonstrates hands-on scripting ability
- 12 pytest tests validate script correctness
- No more placeholder screenshots or duplicate content
- Certification pathway shows career planning maturity

The two remaining items (walkthrough video and GitHub repo topics) are polish — their absence does not affect the hire/no-hire decision.
