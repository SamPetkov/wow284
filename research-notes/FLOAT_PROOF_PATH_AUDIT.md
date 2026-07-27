# Audit excluding floating-point decisions from proof paths

**Status:** candidate closure of v2 Gate 2, pending green CI.

The exact research workflow executes
```text
scripts/verify_research_extensions_exact.py
```
rather than the historical reporter
```text
scripts/verify_research_extensions.py
```. The exact entrypoint checks the order-40 and order-42 adjacency and
distance characteristic polynomials directly and derives the least distance
eigenvalue from the exact transform
\[
  \mu(\theta)=k-2-(\theta+1)^2.
\]

Run
```text
python scripts/audit_no_float_proof_paths.py
```
The AST audit rejects, in every exact workflow entrypoint:

- `float(...)` and `complex(...)`;
- `sympy.N(...)` and `.evalf(...)`;
- NumPy imports;
- NumPy eigenvalue or singular-value routines.

It also verifies that GitHub Actions invokes the exact wrapper and does not
invoke the legacy reporter. The two historical calls `float(sp.N(...))` are
classified explicitly as unreachable code inside the legacy helper
`verify_operator_identity`; any change to that classification fails the audit
and requires review.

Floating point remains permitted only in separately labelled exploratory
scripts. It may not determine a least eigenvalue, root order, strict sign,
multiplicity, or equality claim.
