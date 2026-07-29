# arXiv metadata

**Release:** This manuscript corresponds to GitHub release `v2.3.0`.

**Title:** Counterexamples, Spectral Obstructions, and Deletion Stability for WOW-284

**Author:** Samuil Petkov

**Primary category:** `math.CO`

**Cross-list:** `math.SP`

**MSC class:** `05C50; 05C12; 05C35; 05E30`

**Comments:** 28 pages. Corresponds to GitHub release `v2.3.0`.

**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

**Current public research release:** `v2.3.0`

**Current package:** Identified by `MANIFEST.txt` and `SHA256SUMS`.

**Keywords:** distance spectrum; dual degree; Moore graph

**Abstract (copy and paste as TeX):**

> WOW-284 asserts that the minimum dual degree of every connected graph of
> order at least three and girth at least five does not exceed the negative of
> its least distance eigenvalue. We refute it with exact counterexamples of
> orders $38,39,40,42$, and $50$, and develop a structural theory of the
> failure. For a connected $k$-regular graph of girth at least five and
> diameter three, we prove
> $\delta^*(G)+\lambda_{\min}(D(G))
> =2k-2-\max_{\theta\ne k}(\theta+1)^2$.
> Consequently every regular strict counterexample has degree at least six and
> diameter at most four, while diameter four forces degree at least ten. We
> solve the associated one-variable nonbacktracking linear program exactly,
> including optimizer rigidity. The optimizer yields a positive-semidefinite
> slack matrix whose integral excess gives the stronger universal bound
> $n\le\left\lfloor
> 3(k+2)^2(k^2+3)/(18k+41)
> \right\rfloor$; this follows from a three-to-one quantization theorem for the
> integral excess. The slack matrix's principal minors also recover local
> cycle constraints. In particular, degree-six counterexamples have order at
> most $50$, and at the remaining boundary the associated signed complement
> is necessarily disconnected. We determine the distance spectra of one- and
> two-vertex punctures of Moore graphs and establish a uniform
> deletion-stability bound: every deletion of at most five vertices from the
> Hoffman--Singleton graph remains a strict counterexample, whereas an
> explicit six-vertex deletion does not. All
> theorem-level computations use exact arithmetic. Lean 4.31 kernel-checks the
> full $50$-vertex proof, finite
> spectral certificates at orders $38,39,40,42$, and the analytic LP optimum
> and rigidity for every integer $k\ge4$.

**Leave blank:** Report number, journal reference, external DOI, and ACM class.

The `math.SP` cross-list is defensible because the paper studies distance and
adjacency spectra, but it is optional; `math.CO` is the essential primary
category.
