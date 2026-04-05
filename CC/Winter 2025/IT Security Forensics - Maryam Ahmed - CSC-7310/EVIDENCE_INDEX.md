# Evidence & Screenshots Index

This document catalogs screenshot evidence captured during lab work, grouped by week and topic. Each entry includes the filename and a short caption describing what the screenshot demonstrates.

**Naming convention:**

- Week/topic pattern: `wkNN_<topic>_<index>.png` (e.g., `wk02_chain_of_custody_1.png`)
- Generic pattern: `ScreenshotN_<short-desc>.png` (e.g., `Screenshot1_FTKImager.png`)

**Status:** Screenshots from original lab submissions are embedded in the `assignments/*Submission.docx` files. This index will be populated as screenshots are extracted to the `screenshots/` folder and captioned.

---

## Week 2 — Chain of Custody

*Screenshots to be extracted from [Lab-21-Chain-of-Custody-Submission.docx](assignments/Lab-21-Chain-of-Custody-Submission.docx)*

Expected captures:
- Chain-of-custody form completed
- Evidence bag sealed with tag
- Locker access log entry
- Transfer-to-analyst signature block

---

## Week 4 — Creating a Forensic Image

*Screenshots to be extracted from [Lab-01-Creating-Forensic-Image-Submission.docx](assignments/Lab-01-Creating-Forensic-Image-Submission.docx)*

Expected captures:
- FTK Imager main interface
- "Create Disk Image" dialog with source selected
- Acquisition in progress (progress bar with elapsed time)
- Hash verification dialog — pre- and post-image MD5/SHA-1 matching
- Completed E01 file in destination directory with metadata

---

## Week 6 — Steganography

*Screenshots to be extracted from [Lab-10-Steganography-Submission.docx](assignments/Lab-10-Steganography-Submission.docx)*

Expected captures:
- Hex editor showing carrier-file header and suspicious trailing bytes
- StegHide / OpenStego extraction session
- Recovered payload file contents
- Carrier-file size comparison (expected vs. actual)

---

## Week 7 — Recycle Bin Forensics

*Screenshots to be extracted from [Lab-09-Recycle-Bin-Forensics-Submission.docx](assignments/Lab-09-Recycle-Bin-Forensics-Submission.docx)*

Expected captures:
- `$Recycle.Bin\<SID>\` directory listing
- `$I*` metadata file structure (hex view)
- RBCmd.exe output showing parsed deletion metadata
- Recovered `$R*` file contents
- Timeline table of deletions with user SIDs

---

## Week 9 — Windows Registry Forensics

*Screenshots to be extracted from [Lab-04-Registry-Forensics-Submission.docx](assignments/Lab-04-Registry-Forensics-Submission.docx)*

Expected captures:
- Registry Explorer loading SYSTEM hive
- USBSTOR subkey with USB device serial numbers
- UserAssist decoded entries (ROT-13 decoded)
- ShellBags browser output
- RecentDocs artifact view
- NetworkList Wi-Fi SSID history

---

## Week 10 — Mobile Forensics

*Screenshots to be extracted from [Lab-16-Mobile-Forensics-Submission.docx](assignments/Lab-16-Mobile-Forensics-Submission.docx)*

Expected captures:
- Mobile acquisition tool interface
- SMS database (SQLite) parsed view
- Call log reconstruction
- Browser history from mobile device
- Recovered deleted messages from WAL

---

## Week 12 — Log Capturing & Interpretation

*Screenshots to be extracted from [Lab-17-Log-Capturing-Submission.docx](assignments/Lab-17-Log-Capturing-Submission.docx)*

Expected captures:
- Windows Event Viewer showing Security.evtx
- Event ID 4624 (logon) details pane
- Log Parser query and results
- Unified timeline spreadsheet
- Log-clearing event (1102) detection

---

## Final Project Evidence

See [FINAL_PROJECT_FORENSIC_INVESTIGATION.md](FINAL_PROJECT_FORENSIC_INVESTIGATION.md).

Expected captures (when extracted):
- Case intake / chain-of-custody form
- FTK Imager image-verification log
- Registry Explorer findings
- Timeline spreadsheet (cross-artifact)
- Final report cover page and table of contents

---

## How to Contribute Screenshots

When populating this index:

1. Extract screenshots from submission DOCX files using a DOCX-to-images tool.
2. Save to `screenshots/` using the naming convention above.
3. Add an entry to this index under the correct week with a 1-line caption.
4. Optionally link the screenshot from the corresponding lab section in [assignments/README.md](assignments/README.md).

---

## Related

- **[Lab Index](assignments/README.md)** — each lab links back here for its evidence
- **[Weekly Summary](WEEKLY_SUMMARY.md)** — topic context for each week's screenshots
