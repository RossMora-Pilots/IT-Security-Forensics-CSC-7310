# Evidence & Screenshots Index

This document catalogs all **52 screenshot artifacts** captured during lab work, extracted from the original DOCX submissions. Each entry links to the image file and provides a forensic caption describing the tool, artifact, and investigative significance.

**Naming convention:** `wkNN_labLL_N.png` — week number, lab number, image sequence.

**Source:** All screenshots were extracted from submission DOCX files in [`assignments/`](assignments/).

---

## Week 2 — Chain of Custody (Lab 21) · 2 screenshots

Source: [Lab-21-Chain-of-Custody-Submission.docx](assignments/Lab-21-Chain-of-Custody-Submission.docx)

| # | File | Caption |
|---|------|---------|
| 1 | ![thumb](screenshots/wk02_lab21_1.png) | **Evidence Intake Form** — Completed chain-of-custody form in Foxit Reader documenting a fraud case intake: Det. John Brown as requesting officer, Ross Moravec as lab personnel, Hitachi 500 GB HDD as evidence item with serial number and hash values. |
| 2 | ![thumb](screenshots/wk02_lab21_2.png) | **Custody Transfer Log** — Continuation of the chain-of-custody form showing transfer entries, storage location, and signature blocks for each evidence handoff. |

---

## Week 4 — Creating a Forensic Image (Lab 01) · 3 screenshots

Source: [Lab-01-Creating-Forensic-Image-Submission.docx](assignments/Lab-01-Creating-Forensic-Image-Submission.docx)

| # | File | Caption |
|---|------|---------|
| 1 | ![thumb](screenshots/wk04_lab01_1.png) | **FTK Imager E01 Creation** — FTK Imager 4.3.0.18 "Create Image" dialog with case metadata: case number, evidence number, examiner name, and E01 output path configured for forensic acquisition. |
| 2 | ![thumb](screenshots/wk04_lab01_2.png) | **Drive Geometry & Source Selection** — FTK Imager showing source drive geometry (sector count, total size, partition layout) prior to acquisition. |
| 3 | ![thumb](screenshots/wk04_lab01_3.png) | **Hash Verification — Acquisition Complete** — FTK Imager post-acquisition verification showing matching MD5 and SHA-1 hashes between source drive and E01 image, confirming forensic integrity. |

---

## Week 6 — Steganography (Lab 10) · 4 screenshots

Source: [Lab-10-Steganography-Submission.docx](assignments/Lab-10-Steganography-Submission.docx)

| # | File | Caption |
|---|------|---------|
| 1 | ![thumb](screenshots/wk06_lab10_1.png) | **Hidden Message Revealed in Hex** — HxD hex editor showing PlanC.jpg with hidden plaintext message "THIS IS MY SECRET MESSAGE. THEY WON'T EVER FIND THIS." appended after the JPEG end-of-file marker, viewed alongside IrfanView rendering the carrier image. |
| 2 | ![thumb](screenshots/wk06_lab10_2.png) | **Hex Analysis of Second Carrier File** — HxD hex editor examination of another suspect file, inspecting byte patterns for steganographic indicators. |
| 3 | ![thumb](screenshots/wk06_lab10_3.png) | **Steganographic Payload Extraction** — Extraction of hidden data from carrier file using forensic steganography tools, demonstrating recovery of concealed content. |
| 4 | ![thumb](screenshots/wk06_lab10_4.png) | **Carrier File Comparison** — Additional hex/steganographic analysis comparing file structure and identifying embedded payload boundaries. |

---

## Week 7 — Recycle Bin Forensics (Lab 09) · 7 screenshots

Source: [Lab-09-Recycle-Bin-Forensics-Submission.docx](assignments/Lab-09-Recycle-Bin-Forensics-Submission.docx)

| # | File | Caption |
|---|------|---------|
| 1 | ![thumb](screenshots/wk07_lab09_1.png) | **Autopsy New Case Setup** — Autopsy 4.13.0 "New Case" dialog creating case NDG009 with examiner Ross Moravec, establishing the forensic workspace. |
| 2 | ![thumb](screenshots/wk07_lab09_2.png) | **Evidence Tree — Forensic Image Loaded** — Autopsy file system tree displaying Lab9-1.E01 with vol2 containing NTFS/exFAT partitions ready for analysis. |
| 3 | ![thumb](screenshots/wk07_lab09_3.png) | **$Recycle.Bin Contents** — Autopsy browsing `$Recycle.Bin` SID directory showing 8 results including Dc1–Dc4.exe files with 2004-era timestamps, indicating pre-Vista recycle bin artifacts. |
| 4 | ![thumb](screenshots/wk07_lab09_4.png) | **RECYCLER + rifiuti Parsing** — Autopsy showing RECYCLER SID folder contents (Dc1–Dc4.exe, desktop.ini, INFO2) alongside a terminal running `rifiuti` to parse the pre-Vista INFO2 metadata file into human-readable deletion records. |
| 5 | ![thumb](screenshots/wk07_lab09_5.png) | **Deleted File Metadata Analysis** — Autopsy file content/metadata view examining recovered Recycle Bin artifacts and their associated metadata fields. |
| 6 | ![thumb](screenshots/wk07_lab09_6.png) | **Recycle Bin Artifact Correlation** — Further analysis of Recycle Bin artifacts correlating deletion timestamps with file metadata. |
| 7 | ![thumb](screenshots/wk07_lab09_7.png) | **Analysis Summary** — Final results view consolidating Recycle Bin forensic findings from the investigation. |

---

## Week 9 — Windows Registry Forensics (Lab 04) · 17 screenshots

Source: [Lab-04-Registry-Forensics-Submission.docx](assignments/Lab-04-Registry-Forensics-Submission.docx)

| # | File | Caption |
|---|------|---------|
| 1 | ![thumb](screenshots/wk09_lab04_1.png) | **FTK Imager NTFS Evidence Browse** — FTK Imager displaying the NTFS file system structure of the forensic image with registry hive files visible for extraction. |
| 2 | ![thumb](screenshots/wk09_lab04_2.png) | **Registry Hive Extraction** — Extracting Windows registry hive files (SAM, SYSTEM, SOFTWARE) from the forensic image for offline analysis. |
| 3 | ![thumb](screenshots/wk09_lab04_3.png) | **NTFS Boot Sector Hex View** — Hex dump of the NTFS boot sector showing volume serial number, bytes per sector, and cluster size parameters. |
| 4 | ![thumb](screenshots/wk09_lab04_4.png) | **SYSTEM Hive Analysis** — Registry examination of the SYSTEM hive revealing hardware configuration and mounted device information. |
| 5 | ![thumb](screenshots/wk09_lab04_5.png) | **USBSTOR Key Examination** — USBSTOR registry subkey showing connected USB device history with vendor IDs, product IDs, and serial numbers. |
| 6 | ![thumb](screenshots/wk09_lab04_6.png) | **SOFTWARE Hive — Installed Applications** — Registry analysis of SOFTWARE hive showing installed program entries and version information. |
| 7 | ![thumb](screenshots/wk09_lab04_7.png) | **NTUSER.DAT — User Activity Artifacts** — Per-user registry hive showing UserAssist, RecentDocs, and other user activity tracking keys. |
| 8 | ![thumb](screenshots/wk09_lab04_8.png) | **UserAssist Decoded Entries** — UserAssist registry entries (ROT-13 decoded) revealing GUI application launch history with execution counts and timestamps. |
| 9 | ![thumb](screenshots/wk09_lab04_9.png) | **ShellBags — Folder Browsing History** — ShellBags analysis showing folders the user navigated to, including deleted folders that no longer exist on disk. |
| 10 | ![thumb](screenshots/wk09_lab04_10.png) | **RecentDocs Artifact View** — RecentDocs registry key showing recently opened documents organized by file extension. |
| 11 | ![thumb](screenshots/wk09_lab04_11.png) | **NetworkList — Wi-Fi SSID History** — NetworkList registry entries revealing Wi-Fi networks the machine connected to with first/last connection timestamps. |
| 12 | ![thumb](screenshots/wk09_lab04_12.png) | **RunMRU — Command History** — RunMRU (Win+R) registry key showing commands typed by the user in the Run dialog. |
| 13 | ![thumb](screenshots/wk09_lab04_13.png) | **MD5 Hash Verification** — Hash computation output showing MD5 values for forensic integrity verification of extracted evidence. |
| 14 | ![thumb](screenshots/wk09_lab04_14.png) | **SHA-1 Hash Verification** — SHA-1 hash values computed alongside MD5 for dual-algorithm integrity confirmation. |
| 15 | ![thumb](screenshots/wk09_lab04_15.png) | **Registry Timeline Correlation** — Correlating registry artifact timestamps across multiple hives to build a user activity timeline. |
| 16 | ![thumb](screenshots/wk09_lab04_16.png) | **Evidence Export Summary** — Summary of extracted registry artifacts exported for inclusion in the forensic report. |
| 17 | ![thumb](screenshots/wk09_lab04_17.png) | **Final Hash Comparison** — Post-analysis hash verification confirming the forensic image was not modified during examination. |

---

## Week 10 — Mobile Forensics (Lab 16) · 9 screenshots

Source: [Lab-16-Mobile-Forensics-Submission.docx](assignments/Lab-16-Mobile-Forensics-Submission.docx)

| # | File | Caption |
|---|------|---------|
| 1 | ![thumb](screenshots/wk10_lab16_1.png) | **Android App Data in Autopsy** — Autopsy 4.13.0 browsing `com.android.providers.settings/databases` on an Android device image, showing application data stores for forensic extraction. |
| 2 | ![thumb](screenshots/wk10_lab16_2.png) | **Device Configuration Database** — Autopsy displaying Android system settings databases containing device configuration and user preference artifacts. |
| 3 | ![thumb](screenshots/wk10_lab16_3.png) | **Google Mobile Services Shared Preferences** — Autopsy examining `com.google.android.gms/shared_prefs` with Checkin.xml containing device identifiers, Google account info, and GMS registration data. |
| 4 | ![thumb](screenshots/wk10_lab16_4.png) | **SMS/MMS Database Examination** — Forensic analysis of Android messaging databases (mmssms.db) revealing sent/received message content and timestamps. |
| 5 | ![thumb](screenshots/wk10_lab16_5.png) | **Call Log Reconstruction** — Parsed call history database showing incoming, outgoing, and missed calls with duration and contact information. |
| 6 | ![thumb](screenshots/wk10_lab16_6.png) | **Browser History Artifacts** — Mobile browser history extracted from Chrome/WebView databases showing URLs visited with timestamps. |
| 7 | ![thumb](screenshots/wk10_lab16_7.png) | **Contacts Database Analysis** — Examination of the contacts provider database revealing stored contact names, phone numbers, and email addresses. |
| 8 | ![thumb](screenshots/wk10_lab16_8.png) | **Application Installation Records** — Package manager data showing installed applications, install dates, and permissions granted. |
| 9 | ![thumb](screenshots/wk10_lab16_9.png) | **Device Artifact Summary** — Consolidated view of extracted mobile forensic artifacts organized by data category. |

---

## Week 12 — Log Capturing & Interpretation (Lab 17) · 4 screenshots

Source: [Lab-17-Log-Capturing-Submission.docx](assignments/Lab-17-Log-Capturing-Submission.docx)

| # | File | Caption |
|---|------|---------|
| 1 | ![thumb](screenshots/wk12_lab17_1.png) | **Windows Event Log Directory in Autopsy** — Autopsy 4.15.0 browsing `winevt/Logs/` showing 122 event log files (Application.evtx, Security.evtx, System.evtx, etc.) ready for forensic analysis. |
| 2 | ![thumb](screenshots/wk12_lab17_2.png) | **Security Event Log Parsing** — Forensic examination of Security.evtx entries including logon events (4624), failed logons (4625), and privilege use (4672). |
| 3 | ![thumb](screenshots/wk12_lab17_3.png) | **System Event Log Analysis** — Examination of System.evtx for service installations (7045), driver loads, and log-clearing events (104) as anti-forensics indicators. |
| 4 | ![thumb](screenshots/wk12_lab17_4.png) | **Event Log Timeline Reconstruction** — Correlating events across multiple log sources to build a unified incident timeline with timestamped entries. |

---

## Final Project Evidence · 2 screenshots

Source: Project planning and solution documents in [`project/`](project/)

| # | File | Caption |
|---|------|---------|
| 1 | ![thumb](screenshots/project_plan_1.png) | **Investigation Plan — Phase Overview** — Project planning document outlining the forensic investigation methodology, phases, and deliverables. |
| 2 | ![thumb](screenshots/project_plan_2.png) | **Investigation Plan — Tool & Timeline Matrix** — Continuation of the project plan detailing tool selection, timeline milestones, and evidence handling procedures. |

> **Note:** The project solution DOCX files (101 MB combined) contain detailed analysis inline. See the PDF conversions in [`project/pdf/`](project/pdf/) for browser-viewable versions, or the [Final Project write-up](FINAL_PROJECT_FORENSIC_INVESTIGATION.md) for the synthesized investigation report.

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total screenshots | **48** |
| Lab evidence screenshots | **46** |
| Project planning screenshots | **2** |
| Labs with evidence | **7 / 7** |
| Most-documented lab | Lab 04 — Registry Forensics (**17** screenshots) |

---

## Related

- **[Lab Index](assignments/README.md)** — each lab section embeds key screenshots from this collection
- **[Final Project](FINAL_PROJECT_FORENSIC_INVESTIGATION.md)** — integrates project planning screenshots
- **[Weekly Summary](WEEKLY_SUMMARY.md)** — topic context for each week's evidence
