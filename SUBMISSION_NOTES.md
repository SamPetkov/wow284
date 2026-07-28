# arXiv metadata

**Release:** This manuscript corresponds to GitHub release `v2.2.0`.

**Title:** Counterexamples, Spectral Obstructions, and Deletion Stability for WOW-284

**Author:** Samuil Petkov

**Primary category:** `math.CO`

**Cross-list:** `math.SP`

**MSC class:** `05C50; 05C12; 05C35; 05E30`

**Comments:** 20 pages. Corresponds to GitHub release `v2.2.0`.

**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

**Current public research release:** `v2.2.0`

**Current package:** Identified by `MANIFEST.txt` and `SHA256SUMS`.

**Keywords:** distance spectrum; dual degree; Moore graph

**Abstract (copy and paste as TeX):**

> WOW-284 asserts that the minimum dual degree of every connected graph of
> order at least three and girth at least five does not exceed the negative of
> its least distance eigenvalue. We give exact counterexamples of orders
> $38,39,40,42$, and $50$, beginning with the Hoffman--Singleton graph, and
> develop a structural theory of the failure. For a regular graph of girth at
> least five and diameter three, the counterexample score is
> $\delta^*(G)+\lambda_{\min}(D(G))
> =2k-2-\max_{\theta\ne k}(\theta+1)^2$, where $\theta$ ranges over the
> nonprincipal adjacency eigenvalues. Every regular strict counterexample has
> degree at least six and diameter at most four, and every diameter-four
> counterexample has degree at least ten. We determine the exact optimum, and
> the unique optimizer up to scale, of the standard one-variable
> nonbacktracking linear-programming bound. Localizing its extremal polynomial
> at an edge yields a five-cycle certificate which excludes degree-six order
> $51$, and hence every degree-six regular strict counterexample has order at
> most $50$. We further derive complete distance spectra for one- and
> two-vertex punctures of Moore graphs, prove a general deletion-stability
> inequality, and give a metric normal form for arbitrary punctures of size at
> most $k-1$. In particular, every deletion of at most five vertices from the
> Hoffman--Singleton graph remains a strict counterexample, while one explicit
> six-vertex deletion does not. Equality cases, finite-field obstructions,
> matching-deletion controls, and exact local constraints on a hypothetical
> degree-six order-$50$ example are also obtained. All theorem-level
> computations use exact arithmetic, with independent Python certificates
> cited inline. Lean 4.31 kernel-checks the complete graph-level proof for the
> $50$-vertex counterexample, finite spectral certificates for the
> constructions of orders $38,39,40,42$, and, as a separate analytic theorem,
> the exact one-variable LP optimum and coefficient-level optimizer rigidity
> for every integer $k\ge4$.

**Leave blank:** Report number, journal reference, external DOI, and ACM class.

The `math.SP` cross-list is defensible because the paper studies distance and
adjacency spectra, but it is optional; `math.CO` is the essential primary
category.
