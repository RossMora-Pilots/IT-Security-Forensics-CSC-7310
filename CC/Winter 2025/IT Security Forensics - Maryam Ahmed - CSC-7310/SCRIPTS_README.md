# Scripts — Usage and Notes

Forensic automation scripts for this course. Student-authored scripts live in [`scripts/`](scripts/); reference / external scripts live in [`scripts-extra/`](scripts-extra/).

**Safety:** Review scripts before running. Always run against a **working copy** of a forensic image, never the original evidence.

---

## Student-Created Scripts (`scripts/`)

### [`verify_image_hash.sh`](scripts/verify_image_hash.sh)

**Purpose:** Verify the MD5 and SHA-256 of a forensic image against an expected value (from the acquisition log).

**Usage:**

```bash
./scripts/verify_image_hash.sh <path-to-image.E01> <expected-md5> <expected-sha256>
```

**Example:**

```bash
./scripts/verify_image_hash.sh evidence/case001.E01 \
    d41d8cd98f00b204e9800998ecf8427e \
    e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

**Exit codes:** `0` = both hashes match, `1` = hash mismatch (evidence compromised), `2` = tool error.

**When to use:** Immediately after image acquisition, and before **every** analysis session against the working copy.

---

### [`extract_registry_hives.sh`](scripts/extract_registry_hives.sh)

**Purpose:** Extract common Windows registry hives from a mounted forensic image to a working directory for offline analysis.

**Usage:**

```bash
./scripts/extract_registry_hives.sh <mount-point> <output-dir>
```

**Extracts:**

- `<mount>/Windows/System32/config/SAM`
- `<mount>/Windows/System32/config/SYSTEM`
- `<mount>/Windows/System32/config/SOFTWARE`
- `<mount>/Windows/System32/config/SECURITY`
- `<mount>/Users/*/NTUSER.DAT`
- `<mount>/Users/*/AppData/Local/Microsoft/Windows/UsrClass.dat`

**Output:** Per-hive files + a manifest with SHA-256 of each hive for chain-of-custody.

**When to use:** As the first step of Windows Registry analysis ([Lab 04](assignments/README.md#lab-04--windows-registry-forensics-week-9)).

---

### [`parse_recycle_bin.py`](scripts/parse_recycle_bin.py)

**Purpose:** Parse Windows `$Recycle.Bin\<SID>\$I*` metadata files to produce a CSV of deleted files with original paths, deletion timestamps, and sizes.

**Usage:**

```bash
python3 ./scripts/parse_recycle_bin.py <path-to-recycle-bin-dir> --output deleted_files.csv
```

**Output columns:** `deleted_time_utc, original_path, size_bytes, user_sid, i_file, r_file_exists`

**When to use:** [Lab 09](assignments/README.md#lab-09--recycle-bin-forensics-week-7) and Final Project phase 3 (file-system + deleted-file analysis).

---

### [`event_log_timeline.ps1`](scripts/event_log_timeline.ps1)

**Purpose:** Extract selected event IDs from a Windows `.evtx` file and produce a timeline CSV for correlation with other artifact sources.

**Usage (PowerShell):**

```powershell
.\scripts\event_log_timeline.ps1 -EvtxPath 'C:\evidence\Security.evtx' `
    -EventIds 4624,4625,4672,4688,4720,1102 `
    -OutputCsv '.\timeline_security.csv'
```

**Output columns:** `timestamp_utc, event_id, user, source_ip, logon_type, description`

**When to use:** [Lab 17](assignments/README.md#lab-17--log-capturing-and-interpretation-week-12), Final Project phase 5 (event log analysis).

---

## External / Reference Scripts (`scripts-extra/`)

Reference scripts from forensic open-source community. Not authored by the student; reviewed and used for learning.

### RBCmd.exe (Eric Zimmerman)

**Source:** https://ericzimmerman.github.io/

**Purpose:** Parse `$I` files from Windows `$Recycle.Bin`.

**Usage:**

```bash
RBCmd.exe -d "C:\evidence\mounted\$Recycle.Bin" --csv recycle_bin_output.csv
```

### RECmd.exe (Eric Zimmerman)

**Source:** https://ericzimmerman.github.io/

**Purpose:** Registry browsing and batch-plugin execution.

**Usage:**

```bash
RECmd.exe -d "C:\evidence\hives" --bn "BatchExamples\Kroll_Batch.reb" --csv registry_output.csv
```

### RegRipper (Harlan Carvey)

**Source:** https://github.com/keydet89/RegRipper3.0

**Purpose:** Plugin-based registry analysis — over 300 plugins for specific artifacts.

---

## Validation / Linting

Scripts in `scripts/` pass [ShellCheck](https://www.shellcheck.net/) validation via the [Portfolio CI workflow](../../../.github/workflows/portfolio-ci.yml).

Run locally:

```bash
shellcheck scripts/*.sh
```

For PowerShell scripts:

```powershell
Invoke-ScriptAnalyzer -Path .\scripts\
```

---

## Prerequisites

| Tool | Purpose | Install |
|---|---|---|
| `md5sum`, `sha256sum` | Hash verification | Built into Linux/macOS/WSL |
| `CertUtil` | Windows-native hash utility | Built into Windows |
| Python 3.10+ | Custom parsers | https://www.python.org/ |
| PowerShell 7+ | Event log scripts | https://github.com/PowerShell/PowerShell |
| Eric Zimmerman tools | Reference parsers | https://ericzimmerman.github.io/ |

---

## Related

- **[Lab Index](assignments/README.md)** — which labs exercise which scripts
- **[Final Project](FINAL_PROJECT_FORENSIC_INVESTIGATION.md)** — scripts used in the integrated investigation
