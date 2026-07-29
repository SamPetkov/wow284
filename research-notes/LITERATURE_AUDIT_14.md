# Literature audit for Proof Audit 14

**Scope:** optimal-slack matrix, integral excess matrix, three-to-one order
bound, signed-complement bridge, the degree-six order-50 component-design
exclusion, and the external least-eigenvalue-minus-two classifications.  
**Status:** targeted audit of accessible published and preprint literature. It is
not an absolute priority proof and does not cover private communications,
non-indexed manuscripts, or results stated in substantially different language.

## 1. Established frameworks used by the project

### Nonbacktracking linear programming

Hiroshi Nozaki's linear-programming framework for regular graphs supplies the
standard nonbacktracking-polynomial cone and trace method used in the manuscript:

- H. Nozaki, *Linear Programming Bounds for Regular Graphs*, Graphs and
  Combinatorics 31 (2015), 1973--1984,
  DOI `10.1007/s00373-015-1613-7`.

The exact two-sided WOW-window optimum and optimizer rigidity in this project
are a specialization and optimization of that established framework. The paper
must not describe the one-variable LP method itself as new.

### Distance-polynomial and spectral-excess methods

The surrounding distance-polynomial and spectral-excess literature establishes
that distance matrices or distance relations can often be expressed through
adjacency polynomials in highly regular settings. Relevant sources already
cited in the manuscript include Fiol's quotient-polynomial framework and the
minimal-cage calculations of Howlader and Panigrahi.

The term `excess matrix` also has an established meaning in the degree--diameter
and spectral-excess literature. Accordingly, the project should define its
`integral excess matrix` explicitly and avoid implying that every excess-matrix
construction is new. The claim is narrower: the particular matrix obtained by
integralizing the optimal two-sided WOW slack appears to be project-derived.

## 2. External classification theorems

### 2.1 Ordinary regular graphs with least eigenvalue at least -2

The substantial external theorem used in the three-to-one proof is the
classification of connected regular graphs with smallest adjacency eigenvalue
at least `-2`.

A standard source is:

- D. Cvetkovi\'c, P. Rowlinson and S. Simi\'c,
  *Spectral Generalizations of Line Graphs: On Graphs with Least Eigenvalue
  -2*, Cambridge University Press, 2004,
  DOI `10.1017/CBO9780511751759`.

The convenient regular corollary is:

> A connected regular graph with smallest eigenvalue at least `-2` is a line
> graph, a cocktail-party graph, or an exceptional graph represented in the
> `E_8` root system; regular exceptional graphs have order at most 28.

A recent paper states the same trichotomy in the precise form used here:

- J. H. Koolen, J. Yu, Y.-Y. Liang, S. M. C. Choi and G. Markowsky,
  *Non-bipartite distance-regular graphs with smallest eigenvalue at least
  -m*, European Journal of Combinatorics 126 (2025), Article 104118,
  DOI `10.1016/j.ejc.2024.104118`.

The project uses this theorem only after proving that the auxiliary graph is
connected and has order greater than 28, or componentwise after proving that
each component has order greater than 28. Those hypotheses must remain explicit
at every invocation.

### 2.2 Connected signed graphs with least eigenvalue at least -2

The order-50 component-design proof uses the signed root-system theorem of
Cameron, Goethals, Seidel and Shult.  A directly accessible modern source is:

- G. Greaves, J. H. Koolen, A. Munemasa, Y. Sano and T. Taniguchi,
  *Edge-signed graphs with smallest eigenvalue greater than -2*, Journal of
  Combinatorial Theory, Series B 110 (2015), 90--111,
  DOI `10.1016/j.jctb.2014.07.006`.

Theorem 2 in that paper records the classical statement used here:

> Every connected edge-signed graph with smallest eigenvalue at least `-2` is
> represented by a subset of a root system of type `D_n` or `E_8`.

The same source observes that a representation is integral exactly in the
`D_n` case.  In the project, the signed complement has Gram matrix `S+2I` of
rank at least 30.  Since an `E_8` representation has rank at most eight, only the
`D_n` alternative remains.  The subsequent coordinate-level, parity, equitable
partition and incidence-matrix arguments are project-derived; they are not part
of the external theorem.

The project does **not** invoke the stronger classification in the title of the
Greaves--Koolen--Munemasa--Sano--Taniguchi paper, which assumes smallest
eigenvalue strictly greater than `-2`.  It uses only the non-strict root-system
representation theorem stated in its preliminaries.  This distinction must be
preserved in the manuscript.

## 3. Targeted searches for the project-derived statements

Targeted searches were run for combinations of the following terms:

- `optimal slack matrix` and regular graph;
- `integral excess matrix` and spectral graph;
- shifted adjacency window centred at `-1`;
- nonbacktracking LP plus integrality improvement;
- regular graph order bound from an integral polynomial matrix;
- signed complement with smallest eigenvalue at least `-2`;
- three-to-one excess inequality;
- root-system Gram reformulation of a girth-five spectral bound;
- regular signed row sum two and least eigenvalue `-2`;
- component design with parameters `20`, `30`, row degree six and column degree
  four;
- an order-50 exclusion from a signed root representation.

The searches returned literature on:

- the standard Nozaki linear-programming method;
- spectral-excess and distance-regularity criteria;
- ordinary excess and defect matrices for degree--diameter problems;
- signed graphs and root-system representations with smallest eigenvalue at
  least `-2`;
- signed line graphs and star complements at eigenvalue `-2`;
- line-graph and generalized-line-graph classifications;
- large enumerations of `2-(10,4,4)` designs, but no statement matching the
  component-design contradiction derived here.

No accessible source located in this audit stated the project-specific matrix

```
-g_k(A)+(C_k/n)J,
```

its integralized excess matrix

```
g_k(A)-(6k+13)J+I,
```

the resulting inequality

```
n <= floor(3(k+2)^2(k^2+3)/(18k+41)),
```

or the degree-six order-50 exclusion through the signed-complement component
partition and incidence block identity.

This absence supports conservative wording such as `we derive` or
`project-derived`. It does **not** support `first`, `new`, `previously unknown`,
or an absolute priority claim.

## 4. Claim boundaries for the manuscript

The following distinctions should be preserved.

1. **Established:** nonbacktracking-polynomial LP framework, spectral-excess
   philosophy, ordinary and signed least-eigenvalue-minus-two root-system
   classifications, line-graph root arithmetic.
2. **Specialized here:** the two-sided shifted WOW interval and exact optimizer
   inside the Nozaki-type cone.
3. **Project-derived:** the optimal-slack matrix interpretation, integral excess
   matrix, strict integral collapse, three-to-one order bound, signed-complement
   bridge, component-design reduction, and degree-six order-50 exclusion.
4. **Computer-assisted but exact:** finite divisor tables, exceptional parameter
   checks, recurrence expansions, characteristic-polynomial checks and current
   low-degree numerical windows.
5. **Not claimed:** minimum counterexample order, classification of all
   counterexamples, existence of an infinite family, or priority over
   unpublished observations.

## 5. Promotion recommendation

The general optimal-slack, three-to-one and order-50 exclusion theorems are
suitable for manuscript promotion only after:

- the dedicated and independent exact audits pass at the same commit;
- every invocation of an ordinary or signed least-eigenvalue-minus-two theorem
  states connectedness, the strict/non-strict eigenvalue hypothesis, and any
  order or rank threshold;
- the manuscript cites the relevant source at the point of use;
- the component-design proof is checked independently from the signed-root
  disconnection proof through the final block trace identity;
- novelty language follows the conservative claim boundaries in Section 4.
