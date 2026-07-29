# Proof Audit 14B: canonical order-50 signed-component quotients

**Audited result:** `ORDER50_COMPONENT_QUOTIENT_CLASSIFICATION.md`  
**Audit mode:** two exact enumerations with different search orders and
implementations, followed by a separate algebraic review of every surviving
quotient.  
**Verdict:** `pass` for the quotient classification; no verdict on existence or
nonexistence of graphs realizing the two surviving quotients.

## 1. Corrected theorem boundary

The earlier unconditional order-50 exclusion is not retained.  Its component
argument used an incorrect cubic factor of \(g_6(x)+4\).  The correct statement
proved and audited here is:

> If a connected 6-regular order-50 strict WOW candidate exists, then its signed
> complement has exactly four connected components.  Up to relabelling, the
> adjacency quotient of the original graph is one of two explicit matrices.

The current degree-six order bound therefore remains

\[
 n\le50,
\]

not \(n\le49\).

## 2. Algebraic primary reduction

With

\[
 g_6(x)+4=(x+4)(x^3+2x^2-5x-8),
\]

let \(a\) be the multiplicity of the linear factor and \(b\) the number of
cubic blocks on the nonprincipal component-indicator space.  Dimension and
trace give

\[
 c=1+a+3b,
 \qquad
 \operatorname{tr}Q=6-4a-2b\ge0.
\]

The audit independently obtains

\[
 (a,b,c)\in
 \{(1,0,2),(0,1,4),(1,1,5),(0,2,7),(0,3,10)\}.
\]

No other component count is compatible with nonnegative internal quotient
degrees.

## 3. Exact search spaces

Every branch enforces:

- nonnegative integral entries;
- row sum six;
- detailed balance with positive cell sizes summing to fifty;
- simple internal-degree and handshake constraints;
- the Moore radius-two bound in every internal cell;
- the biregular four-cycle obstruction on every cross block;
- the quotient radius-two inequalities;
- the exact polynomial identity on the component-indicator space;
- connectedness of the quotient.

The primary verifier uses Python for the \(2\)-, \(4\)- and \(5\)-cell cases and
optimized C++ backends for the \(7\)- and \(10\)-cell cases.  The independent
verifier re-enumerates the \(7\)-cell case with a generic Python pair search and
the \(10\)-cell case with a separate Python row-first search.

The independent counts are

\[
egin{array}{c|cc}
 c&\text{branch nodes}&\text{complete row-sum leaves}\\
\hline
 7&14\,179\,432&3\,260\\
 10&3\,130\,846&0.
\end{array}
\]

Both searches return zero quotients.

## 4. Small cases

After the elementary internal-cell filters, the canonical counts are

\[
egin{array}{c|ccc}
 c&2&4&5\\
\hline
 \text{canonical quotients}&1&3&0.
\end{array}
\]

The two-cell quotient is the cubic-free \(20+30\) design branch, already
excluded by the valid incidence argument.  Of the three four-cell quotients,
one contains a signed component of size two and is impossible because a
zero-diagonal signed \(2\times2\) matrix cannot have row sum two.

The two surviving quotients are

\[
 Q_A=
 egin{pmatrix}
 2&0&0&4\\
 0&0&3&3\\
 0&2&0&4\\
 1&1&2&2
 \end{pmatrix},
 \qquad
 (n_i)=(6,8,12,24),
\]

and

\[
 Q_B=
 egin{pmatrix}
 1&0&3&2\\
 0&1&1&4\\
 3&1&0&2\\
 1&2&1&2
 \end{pmatrix},
 \qquad
 (n_i)=(10,10,10,20).
\]

The independent audit verifies directly that both matrices:

- have row sum six;
- satisfy detailed balance;
- have characteristic polynomial
  \((x-6)(x^3+2x^2-5x-8)\);
- satisfy the exact cubic matrix identity;
- satisfy every radius-two inequality.

## 5. Local uniqueness

A separate exhaustive signed-graph enumeration considers connected symmetric
\(6\times6\) matrices with zero diagonal, entries in
\(\{-1,0,1\}\), row sum two, and \(S+2I\succeq0\).  Exact principal minors and
isomorphism reduction leave one class:

\[
 oxed{	ext{the positive cycle }C_6.}
\]

Thus the six-vertex signed component in \(Q_A\) is unique up to relabelling.

## 6. Claim boundary

The audit proves a uniqueness/classification statement at the quotient level.
It does not show that either quotient lifts to a graph, nor does it show that a
lift is unique.  Further progress must use block-level incidence identities or
canonical generation inside \(Q_A\) and \(Q_B\).

The exact scripts are

```text
scripts/verify_order50_component_quotients.py
scripts/verify_proof_audit_14b_component_quotients.py
scripts/order50_component_quotients_c7.cpp
scripts/order50_component_quotients_c10.cpp
```
