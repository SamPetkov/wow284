# Provenance and exact audit for the Jørgensen order-96 equality graph

**Status:** audited exact equality control. The graph construction and public
adjacency list are attributed to Jørgensen; the distance spectrum and WOW-284
calculation are project-side computations.

## 1. External source boundary

The external sources are:

- public adjacency list:
  `https://people.math.aau.dk/~leif/research/girth5/96.html`;
- graph-family index:
  `https://people.math.aau.dk/~leif/research/girth5/`;
- published construction:
  L. K. Jørgensen, *Girth 5 Graphs from Relative Difference Sets*,
  *Discrete Mathematics* **293** (2005), 177--184,
  DOI `10.1016/j.disc.2004.08.029`.

The author's index identifies the degree-nine member as an order-96 graph, and
the order-96 page supplies the complete 96-row adjacency list. The public page
was reopened on 27 July 2026; its title and all visible adjacency rows agreed
with the committed source snapshot.

The exact distance characteristic polynomial, least distance eigenvalue, and
WOW-284 equality are not attributed to the source paper. They are project-side
exact computations.

## 2. What the stored artifacts prove

The directory `data/jorgensen96/` contains:

- normalized page-visible source text;
- a canonical adjacency list;
- a fixed-label graph6 representation;
- `PROVENANCE.json`, recording URL, retrieval time, normalization, byte counts,
  and SHA-256 values.

These artifacts support two different claims.

1. Their parsers prove that three local representations encode the same labelled
   graph.
2. Their byte counts and SHA-256 values detect later changes to the committed
   files.

They are not three source-independent attestations: the normalized adjacency and
graph6 files were derived from the same public list. Moreover, the source
snapshot is normalized visible text rather than raw HTML, so its hash is a local
integrity certificate, not cryptographic authentication of the remote page.
Historical attribution rests on the public page and publication.

## 3. Representation checks

Run

```text
python scripts/verify_jorgensen96_provenance.py
python scripts/verify_jorgensen_96.py
python scripts/verify_proof_audit_09_jorgensen96.py
```

The audit uses:

1. a parser of the stored page-visible rows;
2. a strict parser of the normalized adjacency file;
3. a handwritten graph6 decoder, independent of NetworkX's decoder.

All three labelled adjacency structures agree exactly. The older provenance
verifier retains NetworkX decoding as a redundant fourth implementation.

## 4. Structural certificate

The graph has:

- 96 vertices and 432 edges;
- no loops and symmetric 9-regular adjacency;
- connectedness, girth five, and diameter three.

With adjacency matrix \(A\),

\[
 D=3J+6I-2A-A^2.
\]

The principal distance eigenvalue is the transmission

\[
 3\cdot96+6-2\cdot9-9^2=195.
\]

## 5. Exact adjacency spectrum and the boundary interval

The exact adjacency characteristic polynomial is

\[
\begin{aligned}
\chi_A(x)={}&(x-9)(x-3)^7(x-1)^7(x+5)\\
&\cdot(x^2-8)^{16}(x^2+2x-6)^8\\
&\cdot(x^4+2x^3-17x^2-18x+74)^8.
\end{aligned}
\]

On \(\mathbf1^\perp\),

\[
 D+9I=16I-(A+I)^2.
\]

Every nonprincipal adjacency root lies in \([-5,3]\): the linear and quadratic
factors are immediate, while an exact Sturm sequence places all four roots of

\[
 x^4+2x^3-17x^2-18x+74
\]

strictly in \((-5,3)\). Therefore \(D+9I\succeq0\). Equality occurs only at
adjacency eigenvalues \(3\) and \(-5\), whose multiplicities are seven and one.
Thus

\[
 \lambda_{\min}(D)=-9
\]

with multiplicity eight.

The principal shifted eigenvalue is \(195+9=204>0\), so it does not contribute
to the kernel.

## 6. Redundant direct-distance certificate

The exact distance characteristic polynomial is

\[
\begin{aligned}
\chi_D(x)={}&x^{16}(x-195)(x-3)^7(x+9)^8\\
&\cdot(x^2+4x-28)^{16}\\
&\cdot(x^4+10x^3+5x^2-72x-96)^8.
\end{aligned}
\]

After removing \((x+9)^8\), the remaining factor is nonzero at \(-9\), and an
exact Sturm count shows that it has no root below \(-9\). This independently
certifies the least root and multiplicity without relying on an interval API's
endpoint convention.

Regularity gives

\[
 \delta^*=9,
 \qquad
 \Phi=9-9=0.
\]

The graph is therefore an equality control, not a strict counterexample.

## 7. Claim boundary

The project does not claim:

- construction or discovery of the graph;
- uniqueness of the order-96 graph;
- extremality for WOW-284;
- novelty of the graph's adjacency data.

The certified project contribution here is the exact distance-spectral and
WOW-284 boundary calculation, together with reproducible provenance and local
representation checks.