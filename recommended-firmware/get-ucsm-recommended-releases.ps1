<#
.SYNOPSIS
    Gets recommended releases for UCS Manager from software.cisco.com

.DESCRIPTION
    This script authenticates anonymously to software.cisco.com and retrieves
    the recommended software releases for UCS Manager.

.PARAMETER MdfId
    The product MDF ID (default: 283612660 for UCS Manager)

.PARAMETER SoftwareId
    The software type ID (default: 283655658 for UCS Manager Software)

.EXAMPLE
    .\get-releases.ps1
    Gets recommended releases for UCS Manager

.EXAMPLE
    .\get-releases.ps1 -MdfId 283612660 -SoftwareId 283655658
    Gets recommended releases with specific IDs
#>

param(
    [Parameter()]
    [string]$MdfId = "283612660",
    
    [Parameter()]
    [string]$SoftwareId = "283655658"
)

# Set TLS to 1.2 or higher
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

function Get-CiscoAnonymousSession {
    <#
    .SYNOPSIS
        Gets an anonymous session token from Cisco Software Download
    .DESCRIPTION
        Makes an initial request to the download page which sets the swsession cookie
        containing a JWT token for anonymous access.
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$MdfId,
        
        [Parameter(Mandatory)]
        [string]$SoftwareId
    )
    
    Write-Verbose "Obtaining anonymous session token..."
    
    # URL to get the session cookie - visiting the download page triggers cookie creation
    $downloadPageUrl = "https://software.cisco.com/download/home/$MdfId/type/$SoftwareId"
    
    try {
        # Create a session variable to capture cookies
        $session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
        
        # Make the initial request to get the session cookie
        $headers = @{
            "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            "Accept" = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            "Accept-Language" = "en-US,en;q=0.9"
        }
        
        $response = Invoke-WebRequest -Uri $downloadPageUrl -Method Get -Headers $headers -WebSession $session -ErrorAction Stop
        
        # Extract the swsession cookie
        $swsessionCookie = $session.Cookies.GetCookies($downloadPageUrl) | Where-Object { $_.Name -eq "swsession" }
        
        if (-not $swsessionCookie) {
            throw "swsession cookie not found in response"
        }
        
        Write-Verbose "Successfully obtained session token"
        return @{
            Token = $swsessionCookie.Value
            Session = $session
        }
    }
    catch {
        Write-Error "Failed to obtain session token: $_"
        throw
    }
}

function Get-CiscoSoftwareReleases {
    <#
    .SYNOPSIS
        Gets software releases for a Cisco product
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [Microsoft.PowerShell.Commands.WebRequestSession]$WebSession,
        
        [Parameter(Mandatory)]
        [string]$MdfId,
        
        [Parameter(Mandatory)]
        [string]$SoftwareId
    )
    
    Write-Verbose "Retrieving releases for MDF ID: $MdfId, Software ID: $SoftwareId"
    
    # Generate timestamp (similar to HAR file)
    $timestamp = "L$(Get-Date -Format 'ddHHmmssfffyyyyMMddHHmmss')"
    
    # Build the API URL
    $releasesUrl = "https://software.cisco.com/services/catalog/v1/releases?mdfid=$MdfId&softwareId=$SoftwareId&ts=$timestamp"
    
    # Create headers
    $headers = @{
        "Accept" = "application/json, text/plain, */*"
        "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        "Referer" = "https://software.cisco.com/download/home/$MdfId/type/$SoftwareId"
    }
    
    try {
        # Request the releases using the session which contains the cookies
        $response = Invoke-RestMethod -Uri $releasesUrl -Method Get -Headers $headers -WebSession $WebSession -ErrorAction Stop
        
        Write-Verbose "Successfully retrieved releases"
        return $response
    }
    catch {
        Write-Error "Failed to retrieve releases: $_"
        throw
    }
}

function Format-ReleaseOutput {
    <#
    .SYNOPSIS
        Formats release information for output
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [object]$ReleasesData
    )
    
    Write-Host "`n========================================" -ForegroundColor Cyan
    Write-Host "UCS Manager Software Releases" -ForegroundColor Cyan
    Write-Host "========================================`n" -ForegroundColor Cyan
    
    # Display Suggested/Recommended Releases
    if ($ReleasesData.suggestedRelease) {
        Write-Host "RECOMMENDED RELEASES:" -ForegroundColor Green
        Write-Host "--------------------" -ForegroundColor Green
        foreach ($release in $ReleasesData.suggestedRelease) {
            Write-Host "  Version: $($release.releaseVersion)" -ForegroundColor Yellow
            Write-Host "    Release Track: $($release.bucket1)"
            Write-Host "    Status: $($release.releaseIndicator)"
            Write-Host ""
        }
    }
    
    # Display Latest Releases
    if ($ReleasesData.latestRelease) {
        Write-Host "`nLATEST RELEASES (per major version):" -ForegroundColor Green
        Write-Host "-----------------------------------" -ForegroundColor Green
        foreach ($release in $ReleasesData.latestRelease) {
            Write-Host "  Version: $($release.releaseVersion)" -ForegroundColor Yellow
            Write-Host "    Status: $($release.releaseIndicator)"
            Write-Host ""
        }
    }
    
    # Display Deferred Releases
    if ($ReleasesData.deferredRelease -and $ReleasesData.deferredRelease.Count -gt 0) {
        Write-Host "`nDEFERRED RELEASES: $($ReleasesData.deferredRelease.Count) versions" -ForegroundColor Red
    }
    
    Write-Host "`nTotal Available Releases: $($ReleasesData.allRelease.Count)" -ForegroundColor Cyan
    Write-Host "========================================`n" -ForegroundColor Cyan
}

# Main script execution
try {
    Write-Host "Cisco UCS Manager Release Information" -ForegroundColor Cyan
    Write-Host "======================================`n" -ForegroundColor Cyan
    
    # Step 1: Get anonymous session
    Write-Host "Step 1: Establishing anonymous session..." -ForegroundColor Yellow
    $sessionData = Get-CiscoAnonymousSession -MdfId $MdfId -SoftwareId $SoftwareId
    Write-Host "  ✓ Session established" -ForegroundColor Green
    
    # Step 2: Get releases
    Write-Host "`nStep 2: Retrieving release information..." -ForegroundColor Yellow
    $releases = Get-CiscoSoftwareReleases -WebSession $sessionData.Session -MdfId $MdfId -SoftwareId $SoftwareId
    Write-Host "  ✓ Release information retrieved" -ForegroundColor Green
    
    # Step 3: Display results
    Format-ReleaseOutput -ReleasesData $releases
    
    # Optionally export to JSON
    $exportPath = Join-Path $PSScriptRoot "ucs-releases-$(Get-Date -Format 'yyyyMMdd-HHmmss').json"
    $releases | ConvertTo-Json -Depth 10 | Out-File -FilePath $exportPath -Encoding UTF8
    Write-Host "Full data exported to: $exportPath" -ForegroundColor Gray
    
}
catch {
    Write-Error "Script execution failed: $_"
    exit 1
}
