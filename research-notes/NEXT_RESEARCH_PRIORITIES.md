# Next research priorities after the deep literature audit

This document converts the literature audit into a sequence of research
projects with explicit promotion gates. It does not alter the submitted
manuscript.

## Priority 1: compare the degree-six window with spectral Moore bounds

### Question

For
\[
  k=6,\qquad \theta_{\mathrm{WOW}}=-1+\sqrt{10},
\]
what is the strongest published or directly derivable upper bound on
\[
  v(6,\theta_{\mathrm{WOW}})?
\]

The current project-side arguments leave the diameter-three range
\[
  40\le n\le51.
\]

### Required work

1. Evaluate the Cioabă--Koolen--Nozaki--Vermette linear-programming bound at
   \((k,\theta)=(6,-1+\sqrt{10})\).
2. Compare it with Koledin's girth-five degree bound and the project-side
   fourth-moment and distance-layer bounds.
3. Check whether equality or near-equality forces a Moore polygon,
   distance-regular graph, or another restricted intersection array.
4. Preserve the lower-tail condition
   \[
     \lambda_{\min}(A)>-1-\sqrt{10};
   \]
   a one-sided \(v(k,\theta)\) result is not sufficient.

### Promotion gate

Produce a symbolic or exact rational derivation of the best bound, with
theorem-number citations to the source used. Only then decide whether a
canonical graph census is necessary.

## Priority 2: canonical degree-six census if the LP bound leaves cases

### Class

Connected simple 6-regular graphs with:

- order in the surviving spectral-Moore range;
- girth at least five;
- diameter three;
- \(\lambda_2<-1+\sqrt{10}\);
- \(\lambda_{\min}>-1-\sqrt{10}\).

### Generation specification

The computation must record:

- GENREG/nauty version and source checksum;
- complete command line;
- canonical generation mode;
- counts at every filter stage;
- independent triangle/4-cycle audit;
- exact diameter audit;
- adjacency characteristic polynomial for every survivor;
- graph6 strings and SHA-256 values;
- all equality and near-boundary cases.

Floating point may prune only with a protective interval. Every retained or
rejected boundary graph must be reconstructed exactly.

### Promotion gate

A complete rerunnable log and independent exact verifier. No classification
claim from a partial order range.

## Priority 3: institutional priority clearance for punctured Moore spectra

### Claims to clear

- one-vertex puncture;
- adjacent-pair puncture;
- nonadjacent-pair puncture;
- exact least eigenvalue and multiplicity formulas;
- deletion-stability specialization.

### Required databases

- MathSciNet;
- zbMATH Open;
- Web of Science;
- ProQuest dissertations;
- books and proceedings on distance-regular graphs, graph perturbations,
  and Terwilliger algebras.

### Search distinctions

Do not conflate:

- adjacency spectrum after deletion;
- principal submatrices of the original distance matrix;
- recomputed distance matrices after deletion;
- local or second-subconstituent spectra;
- quantum-walk deleted-vertex constructions.

### Promotion gate

A source ledger with theorem numbers and explicit comparison. Without a
positive priority argument, retain “we derive” and “priority unresolved.”

## Priority 4: equality-boundary classification

### Boundary

For regular girth-five diameter-three graphs,
\[
  |\theta+1|=\sqrt{2k-2}
\]
for at least one nonprincipal adjacency eigenvalue.

### Subproblems

1. If \(2k-2\) is not a square, use algebraic conjugacy to constrain
   multiplicities of the two boundary roots.
2. If \(2k-2\) is a square, write \(k=2r^2+1\) and classify feasible integral
   spectra and trace moments.
3. Compare equality in the project quotient bound with equality in a spectral
   Moore LP bound.
4. Test known distance-regular and association-scheme families.
5. Use the exact degree-9 order-96 graph as a control, not as a classification
   theorem.

### Promotion gate

At least one exact theorem excluding a parameter range or classifying a
family, plus exact computational controls.

## Priority 5: quadratic-embedding restriction

### Question

Does WOW-284 hold for finite graph metrics of quadratic-embedding class?

### Caution

QEC is
\[
  \max_{\|x\|=1,\ x\perp\mathbf1}x^{\mathsf T}Dx,
\]
whereas WOW uses \(\lambda_{\min}(D)\). Negative type controls the wrong
extremal end for a direct implication.

### First computation

Build a canonical database of small connected \(C_3,C_4\)-free graphs for
which the QEC sign can be certified exactly. For each graph record:

- exact dual degree;
- exact least distance eigenvalue;
- exact QEC or a rigorous sign certificate;
- WOW score;
- whether the graph is transmission regular;
- whether QEC equals the second distance eigenvalue.

### Promotion gate

Either an explicit QE counterexample or a structural inequality linking QEC,
dual degree, and the least distance eigenvalue.

## Priority 6: prime-field family beyond diameter three

### Known result

The finite-field construction is established. The project-side Fourier
argument excludes diameter-three strict counterexamples for the stated prime
parameters.

### Open part

Higher-diameter members are not covered.

### Required work

1. Determine the diameter as a function of \((q,m)\), at least for fixed small
   \(m\) and varying prime \(q\).
2. Derive exact Fourier blocks for the distance matrix rather than only
   adjacency.
3. Check whether the distance matrix remains in a low-dimensional block
   algebra.
4. Seek exact asymptotic bounds on the least distance eigenvalue.

### Promotion gate

A theorem with all parameter hypotheses stated and exact controls for several
primes. Do not extrapolate the diameter-three obstruction.

## Priority 7: unconditional infinite family

### Necessary conditions

An infinite regular family must have unbounded degree. For each member:

- girth at least five;
- controlled diameter;
- upper adjacency tail below \(-1+\sqrt{2k-2}\);
- lower adjacency tail above \(-1-\sqrt{2k-2}\), in diameter three;
- exact or rigorously bounded distance spectrum.

### Candidate mechanisms

- association schemes with growing valency;
- nonbipartite quotients of generalized polygons;
- rank-three or low-rank permutation graphs;
- subconstituents with explicit intersection data;
- Cayley graphs with character-theoretic two-sided spectral bounds.

### Promotion gate

One explicit parameterized construction and a proof for every allowed
parameter. Conditional Moore-graph statements do not count as an
unconditional infinite family.

## Priority 8: irregular order 37 and below

This is lower priority than the regular and literature-driven projects.

### Structural pruning required first

Prove and implement:

- \(\delta^*>\operatorname{diam}(G)\);
- minimum-degree restrictions;
- radius-two growth bounds;
- leaf, bridge, and articulation obstructions;
- forbidden local degree patterns;
- exact interlacing obstructions from induced paths;
- safe canonical augmentation rules.

### Promotion gate

Canonical generation of every surviving degree sequence, with independently
checkable counts and exact spectral certificates. No minimality wording before
completion.

## Research governance

Every route must be classified as one of:

- analytically proved;
- exact-computationally proved;
- literature-established;
- priority unresolved;
- exploratory;
- blocked.

A claim moves toward a manuscript only when:

1. the proof or exact certificate is complete;
2. the source comparison is complete enough to control wording;
3. all hypotheses and exceptional cases are explicit;
4. independent checks agree;
5. CI is green;
6. `main.tex` changes occur in a separate PR after review.
