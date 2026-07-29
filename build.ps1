$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$python = if (Test-Path -LiteralPath (Join-Path $root '.venv\Scripts\python.exe')) {
    Join-Path $root '.venv\Scripts\python.exe'
} else {
    'python'
}
& $python (Join-Path $root 'scripts\verify_exact.py') --output (Join-Path $root 'results\verification.json')
& $python (Join-Path $root 'scripts\export_graph_data.py') --output-dir (Join-Path $root 'results')
& $python (Join-Path $root 'scripts\verify_optimal_slack_gram_unification.py')
& $python (Join-Path $root 'scripts\verify_integral_optimal_slack_collapse.py')
& $python (Join-Path $root 'scripts\verify_optimal_slack_excess_matrix.py')
& $python (Join-Path $root 'scripts\verify_two_gram_hierarchies.py')
& $python (Join-Path $root 'scripts\verify_three_to_one_excess_bound.py')
& $python (Join-Path $root 'scripts\verify_three_to_one_equality_rigidity.py')
& $python (Join-Path $root 'scripts\verify_proof_audit_14_three_to_one.py')
& $python (Join-Path $root 'scripts\verify_signed_complement_bridge.py')
& $python (Join-Path $root 'scripts\verify_order50_minus_two_multiplicity.py')
& $python (Join-Path $root 'scripts\verify_order50_signed_complement_disconnected.py')
& $python (Join-Path $root 'scripts\verify_component_indicator_noninvariance.py')
& $python (Join-Path $root 'scripts\sync_manuscript_artifacts.py')
& $python -m pytest -q $root
& $python (Join-Path $root 'scripts\validate_repository.py')
