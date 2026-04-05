#!/usr/bin/env python3
"""Sample YARA rules for forensic artifact classification.

These rules demonstrate pattern-matching for common forensic indicators.
They are educational examples written for the CSC-7310 portfolio —
not production-grade detections.

Usage:
    yara -r forensic_indicators.yar <target-directory>

Reference: CSC-7310 — IT Security Forensics, Cambrian College
"""

# ------------------------------------------------------------------
# Rule 1: Detect NTFS Alternate Data Streams indicators
# ------------------------------------------------------------------
rule ADS_Hidden_Content
{
    meta:
        description = "Detects references to NTFS Alternate Data Streams — common data-hiding technique"
        author      = "Ross Moravec"
        course      = "CSC-7310 Lab 10 — Steganography"
        severity    = "medium"
        reference   = "https://attack.mitre.org/techniques/T1564/004/"

    strings:
        $ads_colon    = /[A-Za-z0-9_\-\.]+:[A-Za-z0-9_\-\.]+/ ascii wide
        $zone_id      = "Zone.Identifier" ascii wide nocase
        $ads_command   = "type " ascii nocase
        $streams_tool = "streams.exe" ascii nocase

    condition:
        2 of them
}

# ------------------------------------------------------------------
# Rule 2: Detect Windows Event Log anti-forensics (log clearing)
# ------------------------------------------------------------------
rule EventLog_Clearing_Indicator
{
    meta:
        description = "Detects commands or artifacts associated with Windows Event Log clearing"
        author      = "Ross Moravec"
        course      = "CSC-7310 Lab 17 — Log Capturing and Interpretation"
        severity    = "high"
        reference   = "https://attack.mitre.org/techniques/T1070/001/"

    strings:
        $wevtutil_cl  = "wevtutil cl" ascii nocase
        $wevtutil_el  = "wevtutil el" ascii nocase
        $clear_evtlog = "Clear-EventLog" ascii nocase
        $event_1102   = "EventID\":1102" ascii
        $event_104    = "EventID\":104" ascii
        $powershell_clear = "Remove-EventLog" ascii nocase

    condition:
        any of them
}

# ------------------------------------------------------------------
# Rule 3: Detect Recycle Bin metadata files
# ------------------------------------------------------------------
rule RecycleBin_I_File
{
    meta:
        description = "Matches Windows $Recycle.Bin $I metadata file structure (Vista+ and Win10+ formats)"
        author      = "Ross Moravec"
        course      = "CSC-7310 Lab 09 — Recycle Bin Forensics"
        severity    = "informational"

    strings:
        $version_v1 = { 01 00 00 00 00 00 00 00 }
        $version_v2 = { 02 00 00 00 00 00 00 00 }

    condition:
        ($version_v1 at 0 or $version_v2 at 0) and filesize < 1MB
}

# ------------------------------------------------------------------
# Rule 4: Detect forensic tool artifacts (indicates prior analysis)
# ------------------------------------------------------------------
rule Forensic_Tool_Artifacts
{
    meta:
        description = "Detects artifacts left by common forensic tools — useful for detecting prior examination"
        author      = "Ross Moravec"
        course      = "CSC-7310 — General forensic awareness"
        severity    = "low"

    strings:
        $ftk_imager   = "FTK Imager" ascii wide nocase
        $autopsy      = "org.sleuthkit.autopsy" ascii wide
        $axiom        = "Magnet AXIOM" ascii wide nocase
        $encase       = "EnCase Forensic" ascii wide nocase
        $regripper    = "RegRipper" ascii wide nocase
        $volatility   = "Volatility Foundation" ascii wide nocase

    condition:
        2 of them
}

# ------------------------------------------------------------------
# Rule 5: Detect USB device connection artifacts in registry exports
# ------------------------------------------------------------------
rule USB_Device_History
{
    meta:
        description = "Detects USBSTOR registry key patterns indicating USB device connection history"
        author      = "Ross Moravec"
        course      = "CSC-7310 Lab 04 — Windows Registry Forensics"
        severity    = "medium"
        reference   = "https://attack.mitre.org/techniques/T1052/001/"

    strings:
        $usbstor     = "USBSTOR" ascii wide nocase
        $disk_vendor  = "Disk&Ven_" ascii wide nocase
        $disk_prod    = "&Prod_" ascii wide nocase
        $device_desc  = "DeviceDesc" ascii wide nocase
        $friendly     = "FriendlyName" ascii wide nocase

    condition:
        $usbstor and 2 of ($disk_vendor, $disk_prod, $device_desc, $friendly)
}
