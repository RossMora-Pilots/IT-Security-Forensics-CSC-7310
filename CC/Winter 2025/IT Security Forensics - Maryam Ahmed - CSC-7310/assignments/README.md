# Lab Index — IT Security Forensics (CSC-7310)

Seven NDG Forensics v2 labs completed over Winter 2025. Each lab pairs:

- **NDG Instructions** (PDF) — the lab curriculum from Network Development Group
- **Submission** (DOCX + PDF) — the student's completed lab write-up with screenshots, answers, and analysis

| # | Lab | Week | Topic | Lab PDF | Submission |
|---|---|---|---|---|---|
| 1 | Lab 21 | Week 2 | Chain of Custody | [PDF](Lab-21-Chain-of-Custody-NDG-Instructions.pdf) | [DOCX](Lab-21-Chain-of-Custody-Submission.docx) · [PDF](pdf/Lab-21-Chain-of-Custody-Submission.pdf) |
| 2 | Lab 01 | Week 4 | Creating a Forensic Image | [PDF](Lab-01-Creating-Forensic-Image-NDG-Instructions.pdf) | [DOCX](Lab-01-Creating-Forensic-Image-Submission.docx) · [PDF](pdf/Lab-01-Creating-Forensic-Image-Submission.pdf) |
| 3 | Lab 10 | Week 6 | Steganography | [PDF](Lab-10-Steganography-NDG-Instructions.pdf) | [DOCX](Lab-10-Steganography-Submission.docx) · [PDF](pdf/Lab-10-Steganography-Submission.pdf) |
| 4 | Lab 09 | Week 7 | Recycle Bin Forensics | [PDF](Lab-09-Recycle-Bin-Forensics-NDG-Instructions.pdf) | [DOCX](Lab-09-Recycle-Bin-Forensics-Submission.docx) · [PDF](pdf/Lab-09-Recycle-Bin-Forensics-Submission.pdf) |
| 5 | Lab 04 | Week 9 | Windows Registry Forensics | [PDF](Lab-04-Registry-Forensics-NDG-Instructions.pdf) | [DOCX](Lab-04-Registry-Forensics-Submission.docx) · [PDF](pdf/Lab-04-Registry-Forensics-Submission.pdf) |
| 6 | Lab 16 | Week 10 | Mobile Forensics | [PDF](Lab-16-Mobile-Forensics-NDG-Instructions.pdf) | [DOCX](Lab-16-Mobile-Forensics-Submission.docx) · [PDF](pdf/Lab-16-Mobile-Forensics-Submission.pdf) |
| 7 | Lab 17 | Week 12 | Log Capturing & Interpretation | [PDF](Lab-17-Log-Capturing-NDG-Instructions.pdf) | [DOCX](Lab-17-Log-Capturing-Submission.docx) · [PDF](pdf/Lab-17-Log-Capturing-Submission.pdf) |

> **Viewing submissions:** PDF versions are provided for direct viewing on GitHub. Original DOCX files (with full formatting and embedded images) are retained via Git LFS.

---

## Lab 21 — Chain of Custody (Week 2)

**Objective:** Demonstrate the complete lifecycle of evidence custody from first response through courtroom admissibility. Document every transfer, every access, every handoff in accordance with ASCLD-Lab standards.

```mermaid
flowchart LR
    A[First Response<br/>Scene Arrival] --> B[Evidence Seizure<br/>Tag · Serial · Photo]
    B --> C[Packaging<br/>Tamper-Evident Bag]
    C --> D[Transport<br/>Signed Transfer Log]
    D --> E[Lab Intake<br/>Locker + Access Log]
    E --> F[Analyst Handoff<br/>Custody Form Signed]
    F --> G[Return / Court<br/>Sealed for Production]
```

**Key Evidence:**

![Evidence Intake Form — fraud case intake documenting Hitachi 500 GB HDD with hash values, Det. John Brown requesting, Ross Moravec as lab personnel](../screenshots/wk02_lab21_1.png)

**Methodology:**

1. Simulated intake of a seized workstation from a company policy violation.
2. Completed chain-of-custody form (evidence tag, serial, hash values, seal number, intake officer).
3. Documented every subsequent handoff (analyst receipt, locker storage, return-to-requester).
4. Sealed evidence and verified tamper-evident packaging.

**Key Findings / Outputs:**

- A fully-populated chain-of-custody document with signatures at every transfer.
- Evidence item: Hitachi 500 GB HDD, serial-numbered and hash-tagged, requested by Det. John Brown; received by lab personnel (Ross Moravec).
- Evidence-bag seal verification log with tamper-evident seal numbers recorded at each transfer.
- Understanding that a **broken custody chain = inadmissible evidence** regardless of technical merit of the forensic work.

**Applicable Standards:** ASCLD-Lab / ISO 17025 lab certification; NIST SP 800-86 §4 (Evidence Collection); ACPO Good Practice Guide §3 (Principles of Digital Evidence).

**Tools:** Pen-and-paper forms (simulated), evidence tags, tamper-evident bags, locker with access log.

**Lessons Learned:**

- Custody is as much a legal/procedural discipline as a technical one.
- Every person touching evidence must be documented — including the analyst who does the imaging.
- Lab certification (ASCLD-Lab, ISO 17025) exists to enforce these procedures uniformly across practitioners.

**What I Would Do Differently:** In a real engagement, I would implement a digital chain-of-custody system (barcode + database) in addition to paper forms — paper is legally required but digital enables searchability and audit trails. I would also add photographic documentation of evidence seals at each transfer point.

**Connects to:** Week 1 (legal authority — search warrants must specify scope), Project 1 (case intake + custody).

---

## Lab 01 — Creating a Forensic Image (Week 4)

**Objective:** Acquire a bit-for-bit forensic image from a target drive using FTK Imager, verify integrity via hashing, and preserve the original evidence unaltered.

```mermaid
flowchart LR
    A[Source Drive<br/>Write-Blocked] --> B[FTK Imager<br/>Create Disk Image]
    B --> C[E01 Output<br/>Compressed + Metadata]
    C --> D[Hash Compute<br/>MD5 + SHA-1]
    D --> E{Hashes<br/>Match?}
    E -- Yes --> F[✅ Verified Image<br/>Ready for Analysis]
    E -- No --> G[❌ Abort<br/>Investigate + Retry]
```

**Key Evidence:**

![FTK Imager 4.3.0.18 — E01 forensic image creation dialog with case metadata configured](../screenshots/wk04_lab01_1.png)

![Post-acquisition hash verification — MD5 and SHA-1 match confirms forensic integrity](../screenshots/wk04_lab01_3.png)

**Methodology:**

1. Attach source drive to a write-blocker (hardware or software).
2. Launch FTK Imager 4.7.3 → *Create Disk Image* → Physical Drive.
3. Select output format: **E01** (EnCase) with compression, or **dd** raw.
4. Configure case metadata (case number, evidence tag, examiner, notes).
5. Execute acquisition; FTK computes MD5 + SHA-1 during read.
6. Verify the post-image hash matches the pre-image read hash.

**Key Findings / Outputs:**

- Created verified E01 forensic image: `C Drive.E01` — output confirmed via FTK Imager Image Report.
- FTK Imager acquisition log documenting start time, duration, and hash verification.
- Post-acquisition hash match confirmed evidence integrity (MD5 + SHA-1 matched between pre-image read and post-image verification).

**Applicable Standards:** NIST SP 800-86 §4.3 (Acquiring the Data); ISO/IEC 27037 §7.4 (Digital Evidence Acquisition).

**Tools:** Exterro FTK Imager 4.7.3, write-blocker (simulated via NDG virtual lab), Windows forensic workstation.

**Lessons Learned:**

- E01 format embeds metadata + segmented archive + hash inline — preferred over raw `dd` for forensic contexts requiring self-contained evidence packages.
- Always acquire to a **forensically sterile** destination (wiped and verified).
- A mismatch between pre-image and post-image hash = abort, investigate, retry.

**What I Would Do Differently:** I would add SHA-256 alongside MD5/SHA-1 for future-proofing — MD5 is cryptographically broken (collision attacks) and some jurisdictions no longer accept it as sole verification. I would also document drive geometry (sector size, total sectors) in the acquisition log for completeness.

**Connects to:** Week 5 (triage and on-scene acquisition), Project 1 (case evidence preservation).

---

## Lab 10 — Steganography (Week 6)

**Objective:** Detect and extract hidden payloads concealed within carrier files (images, audio, documents) using LSB-substitution, header-appending, and metadata-embedding techniques.

```mermaid
flowchart LR
    A[Suspect File<br/>Size Anomaly?] --> B[Hex Inspection<br/>Header · Footer · Chunks]
    B --> C[Steg Tool<br/>StegHide / OpenStego]
    C --> D{Payload<br/>Found?}
    D -- Yes --> E[Extract Payload<br/>Document Contents]
    D -- No --> F[Hash Compare<br/>vs. Known-Clean]
    F --> G[Report<br/>Detection Method + Findings]
    E --> G
```

**Key Evidence:**

![HxD hex editor reveals hidden plaintext "THIS IS MY SECRET MESSAGE" appended after JPEG EOF marker in PlanC.jpg, with IrfanView showing the carrier image](../screenshots/wk06_lab10_1.png)

**Methodology:**

1. Examine suspected carrier files for size anomalies (file larger than expected for dimensions/format).
2. Use hex editor to inspect file headers, footers, and embedded chunks.
3. Use steganography tools (StegHide, OpenStego, or NDG-provided utility) to extract payloads.
4. Compare carrier file hashes against known-clean originals where available.
5. Document extracted payload and method of detection.

**Key Findings / Outputs:**

- Identified hidden content via Alternative Data Streams (ADS): `secret.txt` embedded as `Legitimate_program.exe:secret.txt` using the NTFS ADS colon syntax.
- Detection method: `dir /r` command reveals ADS attached to files — without this command, the hidden stream is invisible to standard directory listings.
- Hidden file creation technique: `Type legitimate_program.exe > Legitimate_program.exe:secret.txt` — demonstrates how trivially data can be concealed in NTFS.
- Produced analysis report showing detection method, extraction tool, and payload contents.

**Applicable Standards:** NIST SP 800-86 §5 (Examining and Analyzing Data); SWGDE Best Practices for Data Acquisition.

**Tools:** Hex editor (HxD / xxd), StegHide / OpenStego, file-type identification (`file` command, PE/JPEG header inspection), `dir /r` for ADS detection.

**Lessons Learned:**

- Steganography is **easy to miss** without suspicion — size anomaly is often the first (only) clue.
- NTFS Alternative Data Streams are a common hiding technique — always run `dir /r` or use Streams.exe (Sysinternals) on NTFS evidence.
- Modern forensic suites (AXIOM, Autopsy) include steganography detection modules but are not infallible.
- Passphrase recovery is often required — check for plaintext passphrase artifacts elsewhere in the case.

**What I Would Do Differently:** I would automate ADS scanning across the entire evidence drive using `streams.exe -s` (Sysinternals) or a PowerShell one-liner (`Get-ChildItem -Recurse | Get-Item -Stream *`). Manual `dir /r` is fine for targeted directories but doesn't scale to a full disk image.

**Connects to:** Week 7 (email forensics — attachments as steg carriers), Project 1 (hidden evidence artifacts).

---

## Lab 09 — Recycle Bin Forensics (Week 7)

**Objective:** Recover deleted files from the Windows Recycle Bin (`$Recycle.Bin`), parse `$I` and `$R` metadata files, and reconstruct the deletion timeline.

```mermaid
flowchart LR
    A[Forensic Image<br/>Read-Only Mount] --> B["Navigate<br/>$Recycle.Bin\\&lt;SID&gt;"]
    B --> C["Parse $I Files<br/>Path · Timestamp · Size"]
    B --> D["Export $R Files<br/>Actual Content"]
    C --> E[Deletion Timeline<br/>Per-User Activity]
    D --> E
    E --> F[Correlate<br/>with Logon Sessions]
```

**Key Evidence:**

![Autopsy browsing RECYCLER SID folder with Dc1–Dc4.exe and INFO2 file; terminal running rifiuti to parse pre-Vista Recycle Bin metadata](../screenshots/wk07_lab09_4.png)

**Methodology:**

1. Mount the forensic image read-only.
2. Navigate to `C:\$Recycle.Bin\<SID>\` for each user account (SID from registry).
3. Enumerate `$I*` files (metadata: original path, deletion timestamp, file size).
4. Enumerate `$R*` files (the actual file content — still recoverable until emptied).
5. Parse `$I` files with forensic parser (e.g., `RBCmd.exe` by Eric Zimmerman).
6. Export recovered files and verify content.

**Key Findings / Outputs:**

- Identified two user SIDs with Recycle Bin activity:
  - `S-1-5-21-2000478354-688789844-1708537768-1003`
  - `S-1-5-21-1843218942-199276559-4149176266-1001`
- Extracted INFO2 file (pre-Vista format) and parsed with Rifiuti to recover deletion metadata.
- Extracted 5 `$I` files from SID folder `S-1-5-21-1843218942-...-1001` — each containing original path, deletion timestamp, and file size.
- Found deleted executables (`Dc1.exe`–`Dc4.exe`) in the RECYCLER folder — potential evidence of anti-forensics or malware cleanup.
- Reconstructed user's deletion activity timeline correlating SIDs with user accounts.

**Applicable Standards:** NIST SP 800-86 §5.2 (File Recovery); ISO/IEC 27037 §7.5 (Evidence Preservation).

**Tools:** FTK Imager (logical file export), Autopsy (case management), Rifiuti (INFO2 parser), RBCmd.exe, Windows SID resolution (`wmic useraccount get name,sid`).

**Lessons Learned:**

- Recycle Bin is a gold mine — users often assume delete = gone.
- `$I` format changed between Windows Vista and Windows 10+; parsers must support both.
- Empty Recycle Bin ≠ gone — file content may still be in unallocated clusters (see Week 9 registry + MFT).

**What I Would Do Differently:** I would cross-reference the deletion timestamps against Windows Event Log logon sessions (Event ID 4624/4634) to prove which user was logged in when each file was deleted. I would also check the `$MFT` for the original file creation timestamps to build a complete file lifecycle (created → modified → deleted).

**Connects to:** Week 9 (Registry — UserAssist shows what files user opened), Project 1 (timeline reconstruction).

---

## Lab 04 — Windows Registry Forensics (Week 9)

**Objective:** Extract and interpret forensic artifacts from Windows Registry hives to establish user activity, installed software, network history, and USB device connection history.

```mermaid
flowchart TD
    A[Forensic Image] --> B[Extract Hives<br/>SAM · SYSTEM · SOFTWARE · NTUSER.DAT]
    B --> C[ShellBags<br/>Folder Browsing]
    B --> D[UserAssist<br/>App Launches]
    B --> E[USBSTOR<br/>USB Device History]
    B --> F[NetworkList<br/>Wi-Fi SSIDs]
    B --> G[RecentDocs<br/>Opened Files]
    C --> H[User Activity Timeline]
    D --> H
    E --> H
    F --> H
    G --> H
```

**Key Evidence:**

![FTK Imager browsing NTFS file system structure with registry hive files visible for extraction](../screenshots/wk09_lab04_1.png)

![UserAssist registry entries (ROT-13 decoded) revealing GUI application launch history with execution counts](../screenshots/wk09_lab04_8.png)

**Methodology:**

1. Extract registry hives from forensic image:
   - `%SystemRoot%\System32\config\SAM` (local accounts)
   - `%SystemRoot%\System32\config\SYSTEM` (devices, services, USB)
   - `%SystemRoot%\System32\config\SOFTWARE` (installed programs, run keys)
   - `C:\Users\<user>\NTUSER.DAT` (per-user activity)
   - `C:\Users\<user>\AppData\Local\Microsoft\Windows\UsrClass.dat` (shell activity)
2. Load hives in Registry Explorer / RegRipper.
3. Extract artifacts:
   - **ShellBags** (folders the user browsed)
   - **UserAssist** (GUI apps the user launched, with run counts and timestamps)
   - **RunMRU** (Win+R command history)
   - **RecentDocs** (recently-opened documents by extension)
   - **USBSTOR** (USB devices ever connected, serials, connection times)
   - **NetworkList** (Wi-Fi SSIDs connected to, timestamps)
4. Correlate findings into user-activity timeline.

**Key Findings / Outputs:**

- Extracted registry hives from forensic image: NTUSER.DAT from `Documents and Settings\IEUser\`, UsrClass.dat from `Documents and Settings\IEUser\Local Settings\Application Data\Microsoft\Windows\`, and system hives (SAM, SYSTEM, SOFTWARE, SECURITY) from `C:\Windows\System32\config\`.
- **RecentDocs:** Found `---README---.txt` at `C:\Documents and Settings\IEUser\Desktop\---README---.txt` — evidence of user accessing a suspicious file.
- **TypedURLs:** Recovered browser URL history with LastWrite timestamps from NTUSER.DAT, revealing web activity patterns.
- **USBSTOR:** Extracted USB device connection history — vendor IDs, product IDs, serial numbers, and first/last connection timestamps.
- **WinNT_CV:** Recovered OS installation date, build number, and registered owner from SOFTWARE hive.
- Registry analysis performed with **RegRipper v2.8** for automated artifact extraction.

**Applicable Standards:** NIST SP 800-86 §5.3 (Windows Artifact Analysis); SWGDE Best Practices for Windows Forensics.

**Tools:** FTK Imager (hive extraction), Registry Explorer (Eric Zimmerman), RegRipper v2.8, RECmd.

**Lessons Learned:**

- Registry is the **second most important forensic source** after the MFT — it persists across reboots and records user intent.
- UserAssist keys are ROT-13 encoded (historical obfuscation, trivially reversed).
- USB history is definitive for answering "did this device ever connect to this machine?"
- Per-user hives (`NTUSER.DAT`) must be extracted from each user's profile separately.

**What I Would Do Differently:** I would automate the full hive extraction and parsing pipeline using the `extract_registry_hives.sh` script from this portfolio, piped into RegRipper batch mode. This would produce a comprehensive HTML report in minutes rather than the manual hive-by-hive approach. I would also check for deleted registry keys using Registry Explorer's "recovered" view.

**Connects to:** Week 7 (recycle bin deletion events tied to user SID), Week 12 (log analysis correlates registry activity with event logs).

---

## Lab 16 — Mobile Forensics (Week 10)

**Objective:** Perform forensic acquisition and analysis of a mobile device (iOS or Android), extract app data, and reconstruct user activity.

```mermaid
flowchart LR
    A[Device ID<br/>iOS / Android] --> B{Acquisition<br/>Method}
    B -- Logical --> C[iTunes / ADB<br/>Backup]
    B -- File System --> D[Jailbreak / Root<br/>Full FS]
    B -- Physical --> E[Chip-Off / JTAG<br/>Bit-Stream]
    C --> F[Parse Artifacts<br/>SMS · Calls · Browser · Apps]
    D --> F
    E --> F
    F --> G[SQLite + WAL<br/>Recover Deleted]
    G --> H[Activity Narrative]
```

**Key Evidence:**

![Autopsy 4.13.0 browsing Android app data — com.android.providers.settings databases for forensic extraction](../screenshots/wk10_lab16_1.png)

![Google Mobile Services shared_prefs — Checkin.xml containing device identifiers and GMS registration data](../screenshots/wk10_lab16_3.png)

**Methodology:**

1. Identify device platform (iOS version / Android version).
2. Select acquisition method:
   - **Logical** (iTunes/ADB backup) — fastest, limited to user-visible data
   - **File system** (jailbreak/root required) — full filesystem access
   - **Physical** (chip-off, JTAG) — bit-stream of flash (destructive, specialized)
3. Extract backup / filesystem dump.
4. Parse common artifacts:
   - SMS/MMS databases (SQLite)
   - Call logs
   - Contacts
   - Browser history (Safari / Chrome)
   - App data (WhatsApp, Signal, Telegram)
   - Location history (GPS breadcrumbs in photos, Maps cache)
5. Correlate artifacts into user-activity narrative.

**Key Findings / Outputs:**

- Analyzed Android data partition (`vol15`) using Autopsy forensic suite.
- **Settings database:** Extracted device configuration from `data/com.android.providers.settings/databases/settings.db` — device identifiers, security settings.
- **Device identifiers:** Found IMEI, Google account registration data in `com.google.android.gms > shared_prefs > checkin.xml`.
- **Email artifacts:** Recovered complete email database `mailstore.cfttmobile1@gmail.com.db` containing emails with timestamps, senders, recipients, and attachments.
- **GPS/Location history:** Extracted navigation data from `da_destination_history` table — GPS coordinates, street addresses, and navigation timestamps establishing physical movement patterns.
- **Device hardware:** Recovered device model, manufacturer, serial number from `wpa_supplicant.conf`; SIM card data (ICCID, phone number, SIM operator) from `SimCard.dat`.

**Applicable Standards:** NIST SP 800-101 Rev. 1 (Guidelines on Mobile Device Forensics); SWGDE Best Practices for Mobile Phone Forensics.

**Tools:** Autopsy 4.13.0 (artifact extraction including call logs, messages, installed programs); conceptual coverage of Cellebrite UFED, Magnet AXIOM Mobile.

**Lessons Learned:**

- Mobile acquisition is **legally fraught** — often requires separate warrant from computer search.
- SQLite WAL files hold **uncommitted deletes** — check WAL before treating delete as permanent.
- iOS is more challenging than Android for non-jailbroken devices (encryption + sandboxing).
- App-layer artifacts (WhatsApp, Signal) are often more useful than OS-level artifacts.

**What I Would Do Differently:** I would prioritize extracting the SQLite WAL (Write-Ahead Log) files alongside the main databases — they often contain recently deleted records. I would also use `sqlitebrowser` to examine all databases for deleted rows (free-list pages) rather than relying solely on Autopsy's built-in parsers.

**Connects to:** Project 1 (mobile device as evidence source), Week 4 (acquisition verification).

---

## Lab 17 — Log Capturing and Interpretation (Week 12)

**Objective:** Collect, parse, and correlate logs from multiple sources (Windows Event Logs, syslog, application logs) to reconstruct an incident timeline suitable for an expert report.

```mermaid
flowchart TD
    A[Security.evtx<br/>Logon · Object Access] --> D[Normalize<br/>Timestamp + Format]
    B[System.evtx<br/>Services · Drivers] --> D
    C[Application Logs<br/>Web · Firewall · Syslog] --> D
    D --> E[Unified Timeline<br/>CSV / JSON]
    E --> F[Anomaly Detection<br/>Brute Force · Lateral Movement]
    F --> G[Incident Narrative<br/>Event Citations + Timestamps]
```

**Key Evidence:**

![Autopsy 4.15.0 browsing winevt/Logs directory — 122 event log files including Application.evtx, Security.evtx, System.evtx](../screenshots/wk12_lab17_1.png)

**Methodology:**

1. Collect Windows Event Logs (`%SystemRoot%\System32\winevt\Logs\*.evtx`):
   - **Security.evtx** (logon/logoff, object access)
   - **System.evtx** (services, drivers)
   - **Application.evtx** (app crashes, installs)
2. Collect syslog from Unix/Linux hosts (`/var/log/auth.log`, `/var/log/syslog`).
3. Collect application logs (web server access logs, firewall logs).
4. Parse into unified timeline (CSV / JSON).
5. Identify anomalies — impossible travel, failed logins, privilege escalations, unusual processes.
6. Write incident narrative with cited log events and timestamps.

**Key Findings / Outputs:**

- Located Windows Event Logs in `Windows\System32\winevt\Logs\` — 122 `.evtx` files identified via Autopsy 4.15.0, including the three primary logs: `Application.evtx`, `System.evtx`, `Security.evtx`.
- Parsed Security.evtx for logon events (Event ID 4624) — correlated logon timestamps with user activity from other evidence sources.
- Examined USN Journal (`$UsnJrnl`) components: `$J` (main journal recording file create/delete/rename operations) and `$Max` (maximum journal size configuration).
- Built unified timeline CSV with timestamped events from multiple log sources, enabling cross-source correlation.
- Identified attack indicators through anomaly detection: brute-force logon attempts, privilege escalation patterns, and unusual process creation.

**Applicable Standards:** NIST SP 800-92 (Guide to Computer Security Log Management); NIST SP 800-86 §5.4 (Log Analysis); ISO/IEC 27037 §7.6.

**Tools:** Autopsy 4.15.0 (evidence browsing), Windows Event Viewer, `wevtutil`, EvtxECmd.exe (Eric Zimmerman), grep/awk/sed, Python parsers.

**Lessons Learned:**

- **Timestamps are lies** until you've verified timezone, NTP sync, and clock drift across hosts.
- Event log IDs are the universal language — memorize the top 20 (4624, 4625, 4672, 4688, 4720, etc.).
- Log correlation across hosts is where incident response lives — single-host logs rarely tell the full story.
- Attackers clear logs — **log-clearing events** (1102 in Security, 104 in System) are themselves high-value indicators.

**What I Would Do Differently:** I would use the `event_log_timeline.ps1` script from this portfolio to automate extraction into CSV, then feed the unified timeline into a SIEM-style visualization (even a simple Excel pivot table). I would also check for gaps in the event log sequence numbers — missing sequence numbers indicate log tampering or rotation.

**Connects to:** Week 9 (registry activity correlates with Event Log entries), Week 11 (network log correlation with PCAP).

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
