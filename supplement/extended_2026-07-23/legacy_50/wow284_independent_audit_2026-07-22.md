# Independent audit of the WOW-284 counterexample

**Repository:** `SamPetkov/wow284`  
**Commit audited:** `db3d5d5ad5a5f89ee5cce815a6bb47b66f5d8107`  
**Audit date:** 22 July 2026  
**Disposition:** Ready for arXiv submission, subject to author identity/affiliation confirmation, any required endorsement, and arXiv moderation.

## 1. Independent graph reconstruction

The graph was reconstructed from the coordinate rules without importing the repository's graph implementation:

- vertices `P_(i,j)` and `Q_(k,l)` over `F_5`;
- `P_(i,j)--P_(i,j+1)`;
- `Q_(k,l)--Q_(k,l+2)`;
- `P_(i,j)--Q_(k,ik+j)`.

The reconstruction produced:

- 50 vertices;
- 175 distinct unordered edges;
- no loops;
- degree 7 at every vertex.

## 2. Exhaustive structural checks

All `C(50,2)=1225` unordered vertex pairs were checked.

- All 175 adjacent pairs have exactly 0 common neighbors.
- All 1050 nonadjacent pairs have exactly 1 common neighbor.
- Integer breadth-first search from every vertex gives connectedness and diameter 2.
- An independent shortest-cycle computation gives girth 5.
- Every exact dual degree, computed from its definition using rational arithmetic, is 7.

Thus the graph is finite, simple, connected, 7-regular, and has girth exactly 5, with
`delta*(G)=7`.

## 3. Exact spectral checks

With exact integer matrices `A`, `D`, `I`, and `J`, the following identities hold entrywise:

```text
A^2 = 6I - A + J
D   = 2J - 2I - A
D   = -14I + A + 2A^2
```

Exact characteristic polynomials:

```text
chi_A(x) = (x - 7)(x - 2)^28(x + 3)^21
chi_D(x) = (x - 91)(x - 1)^21(x + 4)^28
```

Therefore the complete distance spectrum is

```text
91^(1), 1^(21), (-4)^(28),
```

and the least distance eigenvalue is exactly `-4`.

## 4. Independent positive-definiteness certificate

A separate exact rational, no-pivot `LDL^T` algorithm was applied to `D+7I`; it did not call SymPy's `LDLdecomposition`.

- 50 pivots were produced.
- Every pivot is strictly positive.
- The smallest pivot in the fixed vertex ordering is `2352/563`.
- The product of the pivots is exactly

```text
98 * 8^21 * 3^28
= 20678114446557725351321892053581824,
```

which agrees with the determinant implied by the exact spectrum.

Hence `D+7I` is positive definite and
`delta*(G)+lambda_min(D)=7-4=3>0`.

## 5. Manuscript and source audit

The manuscript:

- gives a reproducible coordinate construction;
- proves simplicity, regularity, connectivity, and girth;
- accounts for every adjacency and distance eigenspace and multiplicity;
- computes dual degree from the stated definition;
- states a strict, exact violation;
- makes no minimality claim;
- credits the previously published Hoffman-Singleton distance spectrum;
- avoids a first-discovery or new-spectrum claim.

The arXiv source archive is recorded as containing exactly:

```text
main.tex
references.bib
main.bbl
```

Expected archive SHA-256:

```text
3db826e70a24639824f9b4296648a36dd131adc8d39fb22d839e063a08530b5e
```

The repository's isolated-build check reports a successful four-page pdfLaTeX/BibTeX build with no undefined references or citations.

## 6. Publication recommendation

**Primary category:** `math.CO`  
**Cross-list:** none recommended  
**MSC:** `05C50 (Primary), 05C12 (Secondary)`  
**License:** CC BY 4.0 only if deliberately accepted by the author.

No mathematical correction is required before submission. The author must personally confirm the name, current affiliation, email, license choice, generated PDF, and any endorsement requirement.

## 7. Explicit limitations

This audit is not journal peer review. It does not prove priority, novelty against every unpublished source, or minimality below order 50. arXiv endorsement, moderation, and acceptance remain external processes.
