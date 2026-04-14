param(
    [switch]$Detached,
    [switch]$NoBuild,
    [switch]$Logs
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$composeFile = Join-Path $repoRoot "compose.dev.yaml"

$args = @("compose", "-f", $composeFile, "up")

if ($Detached) {
    $args += "-d"
}

if (-not $NoBuild) {
    $args += "--build"
}

Write-Host "Running: docker $($args -join ' ')"
& docker @args

if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

if ($Logs -and $Detached) {
    & docker compose -f $composeFile logs -f
    exit $LASTEXITCODE
}
