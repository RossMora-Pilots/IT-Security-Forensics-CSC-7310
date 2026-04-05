# External / Reference Scripts

External tools referenced in labs and the final project. Not authored by the student. Included here for documentation and reproducibility.

## Eric Zimmerman's Tools

**Source:** https://ericzimmerman.github.io/ · **License:** MIT

| Tool | Purpose | Used In |
|---|---|---|
| RBCmd.exe | Parse $Recycle.Bin $I files | Lab 09, Final Project |
| RECmd.exe | Registry batch processing | Lab 04, Final Project |
| Registry Explorer | Interactive registry viewing | Lab 04, Final Project |
| MFTECmd.exe | NTFS MFT parsing | Final Project |
| EvtxECmd.exe | .evtx event log parser | Lab 17, Final Project |

## RegRipper 3.0

**Source:** https://github.com/keydet89/RegRipper3.0 · **Author:** Harlan Carvey

Plugin-based registry analysis. 300+ plugins covering most Windows artifacts.

**Usage:**
```bash
perl rip.pl -r NTUSER.DAT -f ntuser > ntuser_output.txt
```

## Autopsy (The Sleuth Kit)

**Source:** https://www.autopsy.com/ · **License:** Apache 2.0

GUI forensic analysis platform. Free alternative to EnCase/X-Ways.

Used conceptually via NDG virtual labs.

## Safety Notes

- **Always run against a working copy** of a forensic image, never the original evidence.
- Verify the working copy's hash matches the original before each session.
- Document every tool invocation with its version, parameters, and output in the examiner's notebook.
- Open-source forensic tools do not have the same legal admissibility pedigree as commercial tools in some jurisdictions — document thoroughly.

## Installation

These tools are **not** bundled in this repository. Download directly from the source links above and install in a dedicated forensic workstation environment (air-gapped or isolated VM recommended).
