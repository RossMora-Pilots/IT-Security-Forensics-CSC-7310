# Lab Index — IT Security Forensics (CSC-7310)

Seven NDG Forensics v2 labs completed over Winter 2025. Each lab pairs:

- **NDG Instructions** (PDF) — the lab curriculum from Network Development Group
- **Submission** (DOCX + PDF) — the student's completed lab write-up with screenshots, answers, and analysis

| # | Lab | Week | Topic | Full Report | Lab PDF | Submission |
|---|---|---|---|---|---|---|
| 1 | Lab 21 | Week 2 | Chain of Custody | [📄 Read](lab-21-chain-of-custody.md) | [PDF](Lab-21-Chain-of-Custody-NDG-Instructions.pdf) | [DOCX](Lab-21-Chain-of-Custody-Submission.docx) · [PDF](pdf/Lab-21-Chain-of-Custody-Submission.pdf) |
| 2 | Lab 01 | Week 4 | Creating a Forensic Image | [📄 Read](lab-01-forensic-imaging.md) | [PDF](Lab-01-Creating-Forensic-Image-NDG-Instructions.pdf) | [DOCX](Lab-01-Creating-Forensic-Image-Submission.docx) · [PDF](pdf/Lab-01-Creating-Forensic-Image-Submission.pdf) |
| 3 | Lab 10 | Week 6 | Steganography | [📄 Read](lab-10-steganography.md) | [PDF](Lab-10-Steganography-NDG-Instructions.pdf) | [DOCX](Lab-10-Steganography-Submission.docx) · [PDF](pdf/Lab-10-Steganography-Submission.pdf) |
| 4 | Lab 09 | Week 7 | Recycle Bin Forensics | [📄 Read](lab-09-recycle-bin.md) | [PDF](Lab-09-Recycle-Bin-Forensics-NDG-Instructions.pdf) | [DOCX](Lab-09-Recycle-Bin-Forensics-Submission.docx) · [PDF](pdf/Lab-09-Recycle-Bin-Forensics-Submission.pdf) |
| 5 | Lab 04 | Week 9 | Windows Registry Forensics | [📄 Read](lab-04-registry-forensics.md) | [PDF](Lab-04-Registry-Forensics-NDG-Instructions.pdf) | [DOCX](Lab-04-Registry-Forensics-Submission.docx) · [PDF](pdf/Lab-04-Registry-Forensics-Submission.pdf) |
| 6 | Lab 16 | Week 10 | Mobile Forensics | [📄 Read](lab-16-mobile-forensics.md) | [PDF](Lab-16-Mobile-Forensics-NDG-Instructions.pdf) | [DOCX](Lab-16-Mobile-Forensics-Submission.docx) · [PDF](pdf/Lab-16-Mobile-Forensics-Submission.pdf) |
| 7 | Lab 17 | Week 12 | Log Capturing & Interpretation | [📄 Read](lab-17-log-analysis.md) | [PDF](Lab-17-Log-Capturing-NDG-Instructions.pdf) | [DOCX](Lab-17-Log-Capturing-Submission.docx) · [PDF](pdf/Lab-17-Log-Capturing-Submission.pdf) |

> **Viewing submissions:** PDF versions are provided for direct viewing on GitHub. Original DOCX files (with full formatting and embedded images) are retained via Git LFS.

---

## Lab 21 — Chain of Custody (Week 2)

Evidence lifecycle from first response through courtroom admissibility. Documented every transfer and handoff per ASCLD-Lab standards. Key artifact: fully-populated custody form for a Hitachi 500 GB HDD with hash-tagged seal verification.

**[→ Read full lab report](lab-21-chain-of-custody.md)**

---

## Lab 01 — Creating a Forensic Image (Week 4)

Bit-for-bit acquisition using FTK Imager with E01 output and dual-hash (MD5 + SHA-1) verification. Demonstrated write-blocking, case-metadata embedding, and post-acquisition integrity confirmation.

**[→ Read full lab report](lab-01-forensic-imaging.md)**

---

## Lab 10 — Steganography (Week 6)

Detected hidden payloads via hex inspection (HxD), NTFS Alternate Data Streams (`dir /r`), and EOF-marker analysis. Recovered plaintext "THIS IS MY SECRET MESSAGE" from a JPEG carrier and extracted ADS-hidden files.

**[→ Read full lab report](lab-10-steganography.md)**

---

## Lab 09 — Recycle Bin Forensics (Week 7)

Parsed `$I`/`$R` metadata from `$Recycle.Bin`, identified two user SIDs with deletion activity, recovered pre-Vista INFO2 records via Rifiuti, and reconstructed per-user deletion timelines.

**[→ Read full lab report](lab-09-recycle-bin.md)**

---

## Lab 04 — Windows Registry Forensics (Week 9)

Deep-dive into 5 registry hives (SAM, SYSTEM, SOFTWARE, NTUSER.DAT, UsrClass.dat). Extracted ShellBags, UserAssist (ROT-13 decoded), USBSTOR device history, RecentDocs, and TypedURLs. 17 evidence screenshots — the most thoroughly documented lab.

**[→ Read full lab report](lab-04-registry-forensics.md)**

---

## Lab 16 — Mobile Forensics (Week 10)

Android forensic acquisition via Autopsy: extracted settings databases, Google account identifiers (IMEI, GMS), email databases, GPS/navigation history, and SIM card data. Covered logical, file-system, and physical acquisition methods.

**[→ Read full lab report](lab-16-mobile-forensics.md)**

---

## Lab 17 — Log Capturing and Interpretation (Week 12)

Collected and correlated 122 `.evtx` files across Security, System, and Application logs. Parsed logon events (4624), failed logons (4625), privilege use (4672), and USN Journal entries into a unified incident timeline.

**[→ Read full lab report](lab-17-log-analysis.md)**

---

## Cross-Lab Skill Matrix

| Skill | Lab 21 | Lab 01 | Lab 10 | Lab 09 | Lab 04 | Lab 16 | Lab 17 |
|---|---|---|---|---|---|---|---|
| Chain of custody | ✅ |  |  |  |  |  |  |
| Hash verification |  | ✅ | ✅ | ✅ | ✅ | ✅ |  |
| Legal framework | ✅ | ✅ |  |  |  | ✅ |  |
| Forensic imaging |  | ✅ |  |  |  | ✅ |  |
| File carving |  |  | ✅ | ✅ |  |  |  |
| Artifact extraction |  |  | ✅ | ✅ | ✅ | ✅ |  |
| Timeline reconstruction |  |  |  | ✅ | ✅ | ✅ | ✅ |
| Expert reporting | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

All 7 labs culminate in **expert reporting** — because no forensic work matters if you can't defend it in writing.

---

## Related Portfolio Docs

- **[Weekly Summary](../WEEKLY_SUMMARY.md)** — lecture-level topic coverage
- **[Final Project](../FINAL_PROJECT_FORENSIC_INVESTIGATION.md)** — integrates skills from all 7 labs
- **[Learning Reflection](../LEARNING_REFLECTION.md)** — course → career role mapping
