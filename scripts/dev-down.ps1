$repoRoot = Split-Path -Parent $PSScriptRoot
$composeFile = Join-Path $repoRoot "compose.dev.yaml"

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Write-Host "Running: docker compose -f $composeFile down"
& docker compose -f $composeFile down
exit $LASTEXITCODE
