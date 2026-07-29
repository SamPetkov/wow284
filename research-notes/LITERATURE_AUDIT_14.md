# Literature audit for Proof Audit 14

**Scope:** optimal-slack matrix, integral excess matrix, three-to-one order
bound, signed-complement bridge, and the external least-eigenvalue-minus-two
classification.  
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

## 2. External classification theorem

The only substantial external theorem used in the three-to-one proof is the
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

## 3. Targeted searches for the project-derived statements

Targeted searches were run for combinations of the following terms:

- `optimal slack matrix` and regular graph;
- `integral excess matrix` and spectral graph;
- shifted adjacency window centred at `-1`;
- nonbacktracking LP plus integrality improvement;
- regular graph order bound from an integral polynomial matrix;
- signed complement with smallest eigenvalue at least `-2`;
- three-to-one excess inequality;
- root-system Gram reformulation of a girth-five spectral bound.

The searches returned literature on:

- the standard Nozaki linear-programming method;
- spectral-excess and distance-regularity criteria;
- ordinary excess and defect matrices for degree--diameter problems;
- signed graphs and root-system representations with smallest eigenvalue at
  least `-2`;
- line-graph and generalized-line-graph classifications.

No accessible source located in this audit stated the project-specific matrix

```
-g_k(A)+(C_k/n)J,
```

its integralized excess matrix

```
g_k(A)-(6k+13)J+I,
```

or the resulting inequality

```
n <= floor(3(k+2)^2(k^2+3)/(18k+41))
```

in the WOW-284 setting.

This absence supports conservative wording such as `we derive` or
`project-derived`. It does **not** support `first`, `new`, `previously unknown`,
or an absolute priority claim.

## 4. Claim boundaries for the manuscript

The following distinctions should be preserved.

1. **Established:** nonbacktracking-polynomial LP framework, spectral-excess
   philosophy, least-eigenvalue-minus-two classification, line-graph root
   arithmetic.
2. **Specialized here:** the two-sided shifted WOW interval and exact optimizer
   inside the Nozaki-type cone.
3. **Project-derived:** the optimal-slack matrix interpretation, integral excess
   matrix, strict integral collapse, three-to-one order bound, signed-complement
   bridge, and order-50 rank consequence.
4. **Computer-assisted but exact:** finite divisor tables, exceptional parameter
   checks, and current low-degree numerical windows.
5. **Not claimed:** minimum counterexample order, classification of all
   counterexamples, existence of an infinite family, or priority over
   unpublished observations.

## 5. Promotion recommendation

The general optimal-slack and three-to-one theorems are suitable for manuscript
promotion only after:

- the dedicated and independent exact audits pass at the same commit;
- every invocation of the least-eigenvalue-minus-two classification includes
  connectedness and the order-28 boundary;
- the manuscript cites the book or the recent paper above at the point of use;
- novelty language follows the conservative claim boundaries in Section 4.
