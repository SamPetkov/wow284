# Proof Audit 09: the Jørgensen order-96 equality control

**Audited results:** `JORGENSEN96_PROVENANCE.md` and the finite example in
`EQUALITY_BOUNDARY.md`.
**Verdict:** `pass_after_correction`.
**Claim boundary:** the graph construction and public adjacency list are due to
Leif K. Jørgensen. The distance spectrum and WOW-284 equality statement are
project-side exact computations.

## 1. Normalized theorem

Let \(G\) be the graph specified by the 96-row adjacency list on Jørgensen's
public girth-five page. Then \(G\) is connected, simple, 9-regular, of order 96,
girth five, and diameter three. Its exact adjacency characteristic polynomial is

\[
\begin{aligned}
\chi_A(x)={}&(x-9)(x-3)^7(x-1)^7(x+5)\\
&\cdot(x^2-8)^{16}(x^2+2x-6)^8\\
&\cdot(x^4+2x^3-17x^2-18x+74)^8.
\end{aligned}
\]

Its least distance eigenvalue is

\[
 \lambda_{\min}(D)=-9
\]

with multiplicity eight. Since the graph is 9-regular,

\[
 \delta^*=9,
 \qquad
 \Phi=0.
\]

Thus the graph is an exact equality control, not a strict counterexample.

## 2. Corrections found

No graph, characteristic polynomial, eigenvalue, or multiplicity changes. Three
claims are narrowed or made unambiguous.

1. The source snapshot, normalized adjacency list, and graph6 file are three
   independently parsed **representations of one source adjacency list**. They
   are not three source-independent attestations of the graph's historical
   origin.
2. SHA-256 values in `PROVENANCE.json` certify integrity of the committed local
   files. Because the stored source snapshot is normalized page-visible text,
   not raw downloaded HTML, the hashes do not authenticate the remote page.
3. The original least-root test used `count_roots(-oo,-9)=1`, whose endpoint
   convention is not self-explanatory. The audit instead proves directly that
   every nonprincipal adjacency root lies in `[-5,3]`, with boundary roots
   exactly `-5` and `3`.

The current public page was reopened on 27 July 2026. Its title and all 96
visible adjacency rows agree with the committed source snapshot. This external
recheck is recorded as an audit observation, not as a network-dependent CI
step.

## 3. Provenance ledger

The following statements have different evidentiary status and must not be
conflated.

| Statement | Evidence |
| --- | --- |
| Jørgensen constructed a family containing a 9-regular order-96 girth-five graph | the 2005 paper and the author's graph index |
| the displayed 96-row list is publicly supplied by Jørgensen | the author's order-96 page |
| the committed source snapshot reproduces that page-visible list | external row-by-row recheck plus local parser |
| the normalized list and graph6 file encode the same labelled graph | independent local parsers |
| local files have not changed unnoticed | byte counts and SHA-256 values in `PROVENANCE.json` |
| the distance polynomial and WOW equality hold | project-side exact matrix and spectral calculations |

The paper is:

L. K. Jørgensen, *Girth 5 Graphs from Relative Difference Sets*,
*Discrete Mathematics* **293** (2005), 177--184,
DOI `10.1016/j.disc.2004.08.029`.

The public page is

`https://people.math.aau.dk/~leif/research/girth5/96.html`.

## 4. Independent reconstruction

The audit uses three representation paths.

1. A strict row parser extracts rows `0,...,95` from the stored source-page
   snapshot and rejects missing rows, repeated rows, repeated neighbors, loops,
   and out-of-range labels.
2. A separately written canonical-row parser reads `adjacency.txt`.
3. A handwritten graph6 decoder reads `jorgensen96.graph6`; it does not use
   NetworkX's graph6 decoder.

The resulting labelled adjacency structures agree exactly. This proves
representation consistency. Historical attribution still comes from the
external page and paper, not from agreement among files generated from that
page.

## 5. Structural checks

The graph has 96 vertices, degree nine at every vertex, and therefore 432
edges. Symmetry and absence of loops are checked entry by entry. Breadth-first
search proves connectedness and diameter three. An exact shortest-cycle search
gives girth five.

Let \(A,I,J\) be the adjacency, identity, and all-ones matrices. Girth at least
five and diameter three give

\[
 D=3J+6I-2A-A^2.
\]

The row sum is

\[
 3\cdot96+6-2\cdot9-9^2=195.
\]

Thus 195 is the principal distance eigenvalue.

## 6. Exact least-eigenvalue proof from the adjacency spectrum

On \(\mathbf1^\perp\),

\[
 D+9I=16I-(A+I)^2.
\]

It is therefore enough to prove that every nonprincipal adjacency eigenvalue
lies in

\[
 [-5,3].
\]

The linear and quadratic factors are immediate:

- \(3,1,-5\in[-5,3]\);
- the roots of \(x^2-8\) are \(\pm\sqrt8\), and \(\sqrt8<3\);
- the roots of \(x^2+2x-6\) are \(-1\pm\sqrt7\), and \(\sqrt7<4\).

For

\[
 q(x)=x^4+2x^3-17x^2-18x+74,
\]

we have

\[
 q(-5)=114,
 \qquad
 q(3)=2.
\]

An exact Sturm sequence has no roots in \(( -\infty,-5]\) or in
\([3,\infty)\), and four roots in \((-5,3)\). Hence all roots of the quartic lie
strictly inside the interval.

It follows that \(D+9I\succeq0\). Equality occurs exactly for adjacency
eigenvalues \(3\) and \(-5\). Their multiplicities are seven and one,
respectively. Consequently

\[
 \lambda_{\min}(D)=-9
\]

with multiplicity eight.

The principal shifted eigenvalue is

\[
 195+9=204>0,
\]

so no principal-eigenspace exception is hidden in the argument.

## 7. Redundant direct distance certificate

The directly computed distance characteristic polynomial is

\[
\begin{aligned}
\chi_D(x)={}&x^{16}(x-195)(x-3)^7(x+9)^8\\
&\cdot(x^2+4x-28)^{16}\\
&\cdot(x^4+10x^3+5x^2-72x-96)^8.
\end{aligned}
\]

After dividing by \((x+9)^8\), the remaining polynomial is nonzero at \(-9\),
and an exact Sturm count gives no root below \(-9\). This independently confirms
the least root and its multiplicity without relying on ambiguous interval
endpoint conventions.

## 8. Independent Python verification

Run

```text
python scripts/verify_jorgensen96_provenance.py
python scripts/verify_jorgensen_96.py
python scripts/verify_proof_audit_09_jorgensen96.py
```

The third script does not import either existing verifier. It checks:

- all local hashes and byte counts;
- three representation parsers, including a handwritten graph6 decoder;
- all graph hypotheses;
- the distance-polynomial identity and transmission;
- the complete adjacency and distance characteristic polynomials;
- exact Sturm localization of the quartic adjacency factor;
- the boundary eigenspaces and multiplicity eight;
- an independent direct-distance least-root certificate;
- \(\delta^*=9\) and score zero.

No floating-point arithmetic or numerical eigensolver is used.

## 9. Claim boundary

This audit establishes the graph and spectral equality calculation. It does not
claim that the order-96 graph is unique, extremal for WOW-284, or new. The graph
construction and adjacency data are attributed to Jørgensen; only the exact
WOW-284 analysis is a project computation.
