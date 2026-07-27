# Literature audit for the edge-local order-50 obstruction

**Audit date:** 24 July 2026  
**Claim status:** exact project theorem; priority unresolved  
**Manuscript status:** not yet proposed for `main.tex`

## Claim audited

For a regular diameter-three strict WOW-284 counterexample, a centered
polynomial in the adjacency matrix gives upper and lower bounds on the number
\(\sigma_e\) of 5-cycles through an edge. At degree six, these bounds exclude
order 51 and leave the exact candidate range

\[
  40\le n\le50.
\]

## Closest located literature

### Radius-two and extremal girth-five counting

Backelin defines the second degree

\[
  \deg^2(v)=\sum_{u\in N(v)}\deg(u)
\]

and proves \(|B(v;2)|=\deg^2(v)+1\) for girth at least five. This is the
published source for the radius-two ball count used in the combinatorial half
of the edge argument.

- J. Backelin, *Sizes of the Extremal Girth 5 Graphs of Orders from 40 to 49*,
  arXiv:1511.08128, Lemma 2.1.

### Edge-girth-regular and girth-regular graphs

The number of shortest cycles through an edge is a standard parameter in the
edge-girth-regular literature. Relevant sources define
\(egr(v,k,g,\lambda)\) graphs, derive lower bounds, and generate fixed-parameter
classes.

- G. Araujo-Pardo, C. Balbuena, M. Conder, and G. Pineda-Villavicencio,
  *Edge-girth-regular graphs*, European Journal of Combinatorics 72 (2018),
  70--82, DOI `10.1016/j.ejc.2018.04.006`.
- I. Porupsánszki, *On edge-girth-regular graphs: lower bounds and new
  families*, arXiv:2305.17014.
- J. Goedgebeur and J. Jooken, *Exhaustive Generation of Edge-Girth-Regular
  Graphs*, arXiv:2401.08271.
- L. Droogendijk, *Nonexistence of Certain Edge-Girth-Regular Graphs*,
  arXiv:2403.20049.

These papers are close because they study the same local count \(\sigma_e\).
They do not, in the sources inspected, state the centered WOW-window Gram
matrix

\[
  -f_k(A)+\frac{f_k(k)}nJ\succeq0
\]

or the resulting order-51 divisibility contradiction.

### Linear-programming and spectral-Moore methods

The polynomial

\[
  f_k(x)=(x+2)^2\bigl(x^2+2x-(2k-3)\bigr)
\]

comes from the standard nonbacktracking/linear-programming framework for
regular graphs with restricted nonprincipal adjacency spectrum.

- H. Nozaki, *Linear Programming Bounds for Regular Graphs*, Graphs and
  Combinatorics 31 (2015), 1973--1984, DOI `10.1007/s00373-015-1613-7`,
  arXiv:1407.4562.
- S. M. Cioabă, J. H. Koolen, H. Nozaki, and J. R. Vermette,
  *Maximizing the Order of a Regular Graph of Given Valency and Second
  Eigenvalue*, SIAM Journal on Discrete Mathematics 30 (2016), 1509--1525,
  DOI `10.1137/15M1030935`, arXiv:1503.06286.

The framework is established. The edge-principal-minor specialization should
be presented as a project derivation, not as a new LP theory.

## Search outcome

Queries included:

```text
"number of 5-cycles through an edge" spectrum girth 5
"edge-girth-regular" spectral bound 5-cycles
"5-cycles through each edge" 6-regular
centered polynomial adjacency edge cycle count girth five
```

No direct indexed source was located for the exact inequalities

\[
  2k-2\le\sigma_e
  \le\frac{2(k+2)^2(k^2+3)}n-10k-26
\]

under the strict WOW adjacency window, or for the order-51 exclusion.

This search result does **not** establish novelty.

## Permitted wording

Use:

> Applying a centered nonbacktracking polynomial to the two endpoints of an
> edge gives an exact local 5-cycle bound. Combined with Backelin's radius-two
> count, this excludes order 51.

Do not use:

- first;
- new edge-girth theorem;
- previously unknown;
- complete degree-six classification.

A final priority claim would require institutional MathSciNet and zbMATH
searches and a cited-by review of the edge-girth-regular papers.
