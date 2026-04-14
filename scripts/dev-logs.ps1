Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$composeFile = Join-Path $repoRoot "compose.dev.yaml"

Write-Host "Running: docker compose -f $composeFile logs -f"
& docker compose -f $composeFile logs -f
exit $LASTEXITCODE
