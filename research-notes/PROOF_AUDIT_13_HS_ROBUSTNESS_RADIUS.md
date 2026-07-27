# Proof Audit 13: Hoffman--Singleton deletion robustness radius

**Audited result:** Theorem 6 of `DIAMETER_PUNCTURE_EXTENSIONS.md`.

**Verdict:** `pass_after_provenance_and_certificate_expansion`.

The theorem is correct. The audit separates provenance of the finite symmetry data from direct verification of its action, independently exhausts the deletion-set orbits, and replaces the original sign check by a handwritten rational \(LDL^{\mathsf T}\) implementation. The robustness radius remains exactly five.

## Audited theorem

Let \(M\) be the Hoffman--Singleton graph. For every \(S\subseteq V(M)\) with \(|S|\le5\), the induced graph \(M-S\) is a strict counterexample to WOW-284. There exists a six-vertex set whose deletion is not strict. Hence the largest integer \(r\) such that every deletion of at most \(r\) vertices preserves strict violation is

\[
\boxed{r=5.}
\]

## Dependencies

The audited small-puncture theorem gives, for \(s=|S|\le6\),

\[
\delta^*(M-S)=\frac{49-s}{7},
\]

and reconstructs the punctured distance matrix entry by entry. The remaining task is a finite global spectral certificate for every labelled deletion set of size at most five.

## Verified symmetry data

The independent verifier embeds the standard two permutations on 50 symbols used for the Hoffman--Singleton automorphism group. It does not assume they are automorphisms. It reconstructs a 175-edge orbit in the standard labelling, verifies a fixed relabelling to the manuscript's coordinate graph, conjugates the permutations, and checks every edge image. It also computes the generated permutation-group order as \(252000\).

The full-group identification is not needed for correctness: the verified subgroup orbits already partition all labelled deletion sets, and the verifier checks complete coverage.

## Orbit exhaustion

The exact orbit counts are

\[
\begin{array}{c|rrrrrr}
s&0&1&2&3&4&5\\
\hline
\#\text{orbits}&1&1&2&4&11&33.
\end{array}
\]

A combinadic rank assigns every labelled \(s\)-subset a unique position. Every unseen subset is expanded to its complete orbit, every orbit member is marked, and the verifier checks

\[
\sum_{\mathcal O}|\mathcal O|=\binom{50}{s}
\]

and that every rank was visited.

## Positive-definiteness certificates

For every orbit representative \(S\), \(s\le5\), the verifier reconstructs \(M-S\), checks connectedness by integer breadth-first search, computes the minimum dual degree from its definition, and checks the exact small-puncture distance formula. It then constructs

\[
7D(M-S)+(49-s)I=L\Delta L^{\mathsf T}
\]

using exact fractions, verifies the reconstruction, and checks that every pivot of \(\Delta\) is positive. Thus every labelled deletion set of size at most five remains strict.

## Six-vertex sharpness witness

Delete

\[
S=\{P_{2,4},P_{3,1},P_{3,4},Q_{2,1},Q_{3,4},Q_{4,4}\}.
\]

The resulting graph has

\[
\delta^*(M-S)=\frac{43}{7}.
\]

The exact decomposition of \(7D(M-S)+43I\) has no zero pivot and exactly one negative pivot. By Sylvester's law of inertia, the shifted matrix has a negative eigenvalue. This proves that the universal radius is at most five. It does not claim that every six-vertex deletion fails.

## Independent exact verification

Run

```text
python scripts/verify_proof_audit_13_hs_robustness.py
```

The script does not import the original robustness verifier. It checks the graph, all symmetry maps, group order, orbit exhaustion, all 52 representatives including the empty deletion, BFS distances, exact dual degree, the distance normal form, handwritten fraction \(LDL^{\mathsf T}\) reconstruction, and the six-vertex failure. No floating-point arithmetic or numerical eigensolver is used.

## Claim boundary

This is a complete finite determination of the universal deletion radius for the Hoffman--Singleton graph. It does not classify all six-vertex deletions by score and does not assert an analogous radius for every Moore graph.