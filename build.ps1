$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$python = if (Test-Path -LiteralPath (Join-Path $root '.venv\Scripts\python.exe')) {
    Join-Path $root '.venv\Scripts\python.exe'
} else {
    'python'
}
& $python (Join-Path $root 'scripts\verify_exact.py') --output (Join-Path $root 'results\verification.json')
& $python (Join-Path $root 'scripts\export_graph_data.py') --output-dir (Join-Path $root 'results')
& $python (Join-Path $root 'scripts\sync_manuscript_artifacts.py')
& $python -m pytest -q $root
& $python (Join-Path $root 'scripts\validate_repository.py')
