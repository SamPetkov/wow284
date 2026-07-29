$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$python = if (Test-Path -LiteralPath (Join-Path $root '.venv\Scripts\python.exe')) {
    Join-Path $root '.venv\Scripts\python.exe'
} else {
    'python'
}

function Invoke-CheckedPython {
    param([Parameter(ValueFromRemainingArguments = $true)][string[]]$Arguments)
    & $python @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Python command failed with exit code ${LASTEXITCODE}: $($Arguments -join ' ')"
    }
}

Invoke-CheckedPython (Join-Path $root 'scripts\verify_exact.py') --output (Join-Path $root 'results\verification.json')
Invoke-CheckedPython (Join-Path $root 'scripts\export_graph_data.py') --output-dir (Join-Path $root 'results')
Invoke-CheckedPython (Join-Path $root 'scripts\verify_optimal_slack_gram_unification.py')
Invoke-CheckedPython (Join-Path $root 'scripts\verify_integral_optimal_slack_collapse.py')
Invoke-CheckedPython (Join-Path $root 'scripts\verify_optimal_slack_excess_matrix.py')
Invoke-CheckedPython (Join-Path $root 'scripts\verify_two_gram_hierarchies.py')
Invoke-CheckedPython (Join-Path $root 'scripts\verify_three_to_one_excess_bound.py')
Invoke-CheckedPython (Join-Path $root 'scripts\verify_three_to_one_equality_rigidity.py')
Invoke-CheckedPython (Join-Path $root 'scripts\verify_proof_audit_14_three_to_one.py')
Invoke-CheckedPython (Join-Path $root 'scripts\verify_signed_complement_bridge.py')
Invoke-CheckedPython (Join-Path $root 'scripts\verify_order50_minus_two_multiplicity.py')
Invoke-CheckedPython (Join-Path $root 'scripts\verify_order50_signed_complement_disconnected.py')
Invoke-CheckedPython (Join-Path $root 'scripts\verify_component_indicator_noninvariance.py')
Invoke-CheckedPython (Join-Path $root 'scripts\sync_manuscript_artifacts.py')
Invoke-CheckedPython -m pytest -q $root
Invoke-CheckedPython (Join-Path $root 'scripts\validate_repository.py')
