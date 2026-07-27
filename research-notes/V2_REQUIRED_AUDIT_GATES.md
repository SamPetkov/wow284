# Required audit gates before any v2 manuscript revision

These four items are mandatory. None is optional prose polish. A v2 branch may
be opened only after every gate has a complete artifact, an independent check,
and green CI.

## Gate 1: provenance-check the Jørgensen order-96 equality control

### Required claim boundary

The order-96, 9-regular, girth-five graph is a known construction of Leif K.
Jørgensen. The project's WOW equality and distance-spectrum statements are
exact computations on that graph; they are not attributed to Jørgensen unless
his paper states them.

### Required artifacts

1. Store a local UTF-8 adjacency list copied from the constructor's public
   page:
   `https://people.math.aau.dk/~leif/research/girth5/96.html`.
2. Record:
   - source URL;
   - retrieval date;
   - SHA-256 of the downloaded source text;
   - normalization procedure, if whitespace or line endings change;
   - the corresponding paper DOI `10.1016/j.disc.2004.08.029`.
3. Verify exactly:
   - rows 0 through 95 appear once;
   - no loop or parallel edge;
   - symmetric adjacency;
   - 96 vertices, 432 edges, and degree 9;
   - connectedness, girth 5, and diameter 3;
   - `D = 3J + 6I - 2A - A^2`;
   - exact adjacency and distance characteristic polynomials;
   - the least distance eigenvalue is exactly `-9`;
   - `delta*=9`, hence equality in WOW-284.
4. Add a second parser or graph6 reconstruction that does not reuse the first
   parser's control flow.

### Promotion gate

Both reconstructions yield byte-identical normalized adjacency matrices and
all exact checks pass. The manuscript must distinguish the published graph
construction from the project-side distance-spectrum computation.

## Gate 2: remove floating-point eigenvalue ordering from every asserted proof

### Rule

Floating point may rank exploratory candidates only. It may not decide:

- which algebraic eigenvalue is least;
- the sign of a WOW score;
- a strict spectral-window inequality;
- root multiplicity;
- equality versus strictness.

### Required replacements

For each asserted graph or symbolic family use at least one of:

- exact characteristic-polynomial factorization plus algebraic comparison;
- Sturm root counts with endpoint nonvanishing;
- rational interval isolation;
- exact shifted positive definiteness;
- exact quotient/interlacing argument;
- symbolic monotonicity and exact endpoint checks.

### Required audit

Search the extension branch for:

```text
float(
np.linalg.eigvalsh
numpy.linalg.eig
sp.N(
key=lambda z: float
```

Each occurrence must be classified as:

- exploratory only;
- formatting only;
- prohibited in a proof path.

Add a CI check that fails if a proof verifier uses a floating-point conversion
to select or order eigenvalues.

### Promotion gate

Every theorem-level spectral ordering is exact, and the audit log lists all
remaining floating-point calls with an exploratory-only justification.

## Gate 3: complete the degree-six `c >= 15` argument

### Setting

For a connected 6-regular graph of girth at least five and diameter three,
write

\[
  n=37+c.
\]

The regular WOW criterion requires every nonprincipal adjacency eigenvalue to
lie in

\[
  (-1-\sqrt{10},-1+\sqrt{10}).
\]

### Required proof

1. Define the normalized distance-layer compression and its feasible parameter
   range.
2. Prove the compression is a positive-semidefinite rank-one perturbation of
   the extremal compression at the minimum feasible parameter.
3. Derive the exact nonprincipal factor
   \[
     \frac{p_{6,c}(x)}5,
   \]
   making clear that `p_{6,c}` is a positive scalar multiple, not necessarily
   the monic characteristic polynomial.
4. Verify at `c=15`:
   \[
     p_{6,15}(x)=5(x+2)(x^2+2x-9),
   \]
   so the largest quotient root is exactly
   \[
     -1+\sqrt{10}.
   \]
5. Prove monotonicity for all `c >= 15`, or give an exact direct evaluation
   showing the largest quotient root is at least the boundary.
6. Apply interlacing and preserve strictness: equality at `c=15` already
   excludes a strict WOW counterexample.
7. Conclude
   \[
     c\le14,\qquad n\le51.
   \]

### Required checks

- symbolic determinant identity;
- symbolic factorization at `c=15`;
- exact monotonicity or sign certificate for all `c>=15`;
- independent numerical sampling for diagnostics only, never as proof.

### Promotion gate

The written proof covers every integer `c>=15` without an unstated continuity,
monotonicity, or eigenvalue-ordering assumption.

## Gate 4: supply the direct-sum and multiplicity proof for the nonadjacent puncture

### Setting

Let `M` be a diameter-two Moore graph of degree `k`, and delete two
nonadjacent vertices. Their unique common neighbor determines the natural
five-cell partition.

### Required proof structure

1. Define every cell and prove its size.
2. Prove the partition is equitable for the recomputed distance matrix.
3. Identify the quotient space and its five-dimensional distance quotient.
4. Construct every nonconstant invariant module explicitly:
   - the symmetric matched-neighborhood module;
   - the antisymmetric matched-neighborhood module;
   - the common-neighbor incidence module;
   - the residual Moore kernel.
5. Prove pairwise orthogonality or direct-sum independence.
6. Prove invariance of each module under the distance matrix.
7. Derive the characteristic polynomial on each module.
8. Derive all multiplicities symbolically.
9. Check the dimension sum equals `k^2-1` exactly.
10. Specialize to `k=7` and recover the stored exact characteristic
    polynomial coefficient-for-coefficient.

### Required claim boundary

The deletion-stability theorem may certify strictness before the full spectrum
is known. A complete spectrum theorem, however, cannot be promoted from a
formal factor product alone; the invariant direct-sum and multiplicity
accounting must be written and independently checked.

### Promotion gate

A reader can reconstruct every eigenspace and multiplicity without trusting a
computer factorization. The symbolic verifier confirms all module
polynomials, multiplicities, and the `k=7` specialization.

## Final v2 gate

After all four items pass:

1. run the exact extension CI;
2. obtain an independent mathematical review of the four proofs;
3. rerun the literature audit;
4. open a separate manuscript PR;
5. modify `main.tex` only in that later PR;
6. rebuild and inspect the arXiv package independently.

Until then, PRs may contain research notes, data, and verifiers, but no v2
manuscript claim is considered approved.
