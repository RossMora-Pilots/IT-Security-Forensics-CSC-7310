<#
.SYNOPSIS
    Extract selected events from a Windows .evtx file and produce a timeline CSV.

.DESCRIPTION
    Queries a Windows Event Log file for specified Event IDs and writes a
    flat CSV for cross-source timeline correlation.

    Reference: CSC-7310 Lab 17 — Log Capturing and Interpretation (Week 12)

.PARAMETER EvtxPath
    Path to the .evtx file (e.g., C:\evidence\Security.evtx).

.PARAMETER EventIds
    One or more Event IDs to extract.
    Common Security.evtx IDs:
        4624 = Logon (successful)
        4625 = Logon (failed)
        4634 = Logoff
        4672 = Special privileges assigned (admin logon)
        4688 = Process creation
        4720 = User account created
        1102 = Security log cleared (anti-forensics indicator)

.PARAMETER OutputCsv
    Path to the output CSV file.

.EXAMPLE
    .\event_log_timeline.ps1 -EvtxPath 'C:\evidence\Security.evtx' `
        -EventIds 4624,4625,4672,4688,4720,1102 `
        -OutputCsv '.\timeline_security.csv'
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)]
    [string]$EvtxPath,

    [Parameter(Mandatory=$true)]
    [int[]]$EventIds,

    [Parameter(Mandatory=$true)]
    [string]$OutputCsv
)

$ErrorActionPreference = 'Stop'

if (-not (Test-Path -LiteralPath $EvtxPath)) {
    Write-Error "EVTX file not found: $EvtxPath"
    exit 2
}

Write-Host "Reading $EvtxPath for event IDs: $($EventIds -join ', ')"

try {
    $events = Get-WinEvent -FilterHashtable @{
        Path = $EvtxPath
        Id   = $EventIds
    } -ErrorAction Stop
} catch {
    Write-Warning "No matching events found or file could not be read: $_"
    exit 1
}

Write-Host "Found $($events.Count) event(s). Building timeline..."

$timeline = foreach ($evt in $events) {
    # Extract user info — varies per event ID
    $user = $null
    $sourceIp = $null
    $logonType = $null

    if ($evt.Properties.Count -gt 0) {
        # Security.evtx 4624/4625 standard property positions
        switch ($evt.Id) {
            4624 {
                $user      = $evt.Properties[5].Value
                $logonType = $evt.Properties[8].Value
                $sourceIp  = $evt.Properties[18].Value
            }
            4625 {
                $user      = $evt.Properties[5].Value
                $logonType = $evt.Properties[10].Value
                $sourceIp  = $evt.Properties[19].Value
            }
            4634 { $user = $evt.Properties[1].Value }
            4672 { $user = $evt.Properties[1].Value }
            4688 { $user = $evt.Properties[1].Value }
            4720 { $user = $evt.Properties[0].Value }
        }
    }

    [PSCustomObject]@{
        timestamp_utc = $evt.TimeCreated.ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')
        event_id      = $evt.Id
        provider      = $evt.ProviderName
        user          = $user
        source_ip     = $sourceIp
        logon_type    = $logonType
        description   = ($evt.Message -split "`n")[0]
    }
}

$timeline | Sort-Object timestamp_utc | Export-Csv -Path $OutputCsv -NoTypeInformation -Encoding UTF8

Write-Host "Timeline written: $OutputCsv ($($timeline.Count) rows)"
exit 0
