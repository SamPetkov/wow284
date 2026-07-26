# Reader-first guide to the WOW-284 programme

**Purpose.** This document is an expository map for the submitted v1 paper and the
post-v1 research stack. It does not certify a theorem, change a proof status, or
promote any draft result into `main.tex`. The controlling status ledger remains
`V2_COMPLETE_MATHEMATICAL_SYNTHESIS.md`, together with the individual proof notes
and proof-audit registry.

The main editorial principle is simple:

> Keep the disproof visible in five lines, then add structure in layers. Do not
> make the reader traverse the computational and audit infrastructure before
> seeing why WOW-284 is false.

---

## 1. The result in thirty seconds

For a degree-`k` Moore graph of diameter two,

```text
A^2 = (k - 1)I - A + J,
D   = 2J - 2I - A,
delta* = k.
```

On the orthogonal complement of the all-ones vector, the nonprincipal adjacency
eigenvalues satisfy

```text
theta^2 + theta - (k - 1) = 0.
```

Hence

```text
lambda_min(D) = -(3 + sqrt(4k - 3))/2,
Phi(G)         = k - (3 + sqrt(4k - 3))/2.
```

Therefore a realizable Moore graph is a strict WOW-284 counterexample exactly
when `k > 3`. The Hoffman--Singleton graph has `k = 7`, so

```text
delta* = 7,
lambda_min(D) = -4,
Phi = 3.
```

That is the conceptual disproof. Every later theorem should be presented as an
answer to one of three subsequent questions:

1. **How small can a counterexample be?**
2. **What structural conditions force or forbid a counterexample?**
3. **How stable is the Hoffman--Singleton mechanism under deletion?**

---

## 2. Three reading paths

### Path A: understand the disproof

Read only:

1. the statement of WOW-284;
2. the Moore identity and distance-matrix identity;
3. the Hoffman--Singleton substitution `k = 7`;
4. one explicit coordinate certificate, if a self-contained construction is
   desired.

This path should require no puncture theory, linear programming, orbit
enumeration, or characteristic-polynomial ledger.

### Path B: understand the organising spectral mechanism

After Path A, read:

1. the regular diameter-three identity
   ```text
   D = 3J + (k - 3)I - 2A - A^2;
   ```
2. the shifted-window criterion
   ```text
   |theta + 1| < sqrt(2k - 2)
   ```
   for every nonprincipal adjacency eigenvalue;
3. the degree obstruction `k >= 6`;
4. the diameter trichotomy:
   - diameter two: Moore;
   - diameter three: shifted spectral window;
   - diameter four: degree at least ten;
   - diameter at least five: impossible for a regular strict counterexample.

This is the shortest route to the paper's larger mathematical message: failure
of WOW-284 is controlled by low-dimensional distance algebras and a narrow
adjacency-spectral window.

### Path C: review the complete post-v1 programme

Continue with:

1. the exact limitation of the standard one-point nonbacktracking LP method;
2. the audited degree-six order bound `n <= 50`;
3. the exact order-50 local feasibility system;
4. Moore-puncture normal forms and deletion-stability inequalities;
5. the exact Hoffman--Singleton robustness radius five;
6. finite negative controls, orbit classifications, and low-degree windows;
7. the remaining proof-audit and literature-priority queue.

Path C is a research-program reading path, not the intended order of a concise
journal manuscript.

---

## 3. The theorem spine

A readable v2 should expose the following dependency chain before any detailed
calculation.

```text
WOW-284 definition
  |
  +-- Moore distance identity
  |     -> Hoffman--Singleton counterexample
  |     -> exact Moore threshold k > 3
  |
  +-- regular diameter-three identity
        -> shifted adjacency-spectrum criterion
        |
        +-- low-degree exclusion: k >= 6
        |
        +-- one-point LP ceiling
        |     -> degree-six candidate window
        |     -> local edge certificate
        |           -> audited n <= 50
        |
        +-- endpoint-neighbourhood Rayleigh bounds
        |     -> regular diameter <= 4
        |     -> diameter-four degree >= 10
        |
        +-- Moore deletion algebra
              -> puncture normal forms
              -> exact Hoffman--Singleton radius five
```

The finite examples of orders `38, 39, 40, 42, 50` support the first two branches
but should not interrupt this spine.

---

## 4. Recommended v2 main-text hierarchy

### Theorem A: explicit disproof and Moore threshold

State the general Moore calculation first and specialize immediately to the
Hoffman--Singleton graph. Keep the proof self-contained but short. The coordinate
construction may follow as a certificate rather than as the conceptual entry
point.

### Theorem B: diameter-three shifted-spectrum criterion

State the operator identity and its exact spectral consequence. This theorem is
the bridge from a single counterexample to a structural theory.

### Theorem C: degree and diameter localization

Combine the reader-facing conclusions:

```text
regular strict counterexample
  -> degree at least 6
  -> diameter at most 4
  -> if diameter 4, degree at least 10.
```

The proof may be split into two propositions, but the statement should be read as
one localization theorem.

### Theorem D: exact ceiling of the standard one-point LP method

Explain first what the theorem says methodologically: increasing the polynomial
degree inside the same LP hierarchy cannot improve the fourth-moment ceiling.
Only then present the primal-dual certificate.

### Theorem E: every degree-six regular strict counterexample has order at most 50

The proof must include the diameter-three reduction before invoking the shifted
spectral window. The dedicated audit found and repaired precisely this scope
issue; the published exposition should make the reduction impossible to miss.

### Theorem F: small Moore punctures and Hoffman--Singleton robustness

Present the analytic normal form before the orbit computation. The finite
classification should be described as the exact specialization of the normal
form, not as a disconnected computer search.

---

## 5. What belongs outside the main narrative

The following material is mathematically useful but should be moved to appendices,
a companion note, or the repository unless it is needed for a stated theorem:

- full characteristic-polynomial factorizations;
- complete `LDL^T` pivot ledgers;
- every automorphism-orbit representative;
- the 266 surviving coarse order-50 profiles;
- the 120 matching-deletion negative controls;
- generator and graph6 data;
- Lean implementation details beyond the exact public theorem scope;
- historical failed approaches and rejected shortcuts;
- literature-query transcripts.

The main text should cite exact artifacts at the point where they discharge a
finite claim. It should not reproduce the artifact inventory as prose.

---

## 6. A one-page notation policy

Use one notation consistently throughout the v2 manuscript.

```text
A(G)                 adjacency matrix
D(G)                 ordinary distance matrix
lambda_D(G)          least eigenvalue of D(G)
d*(v)                dual degree at v
delta*(G)            minimum dual degree
Phi(G)               delta*(G) + lambda_D(G)
k                     regular degree
n                     order
A_i                   distance-i matrix
theta                 nonprincipal adjacency eigenvalue
mu(theta)             corresponding distance eigenvalue
```

Recommended conventions:

1. Write `lambda_D(G)` in expository prose and reserve indexed distance
   eigenvalues for statements that need the full ordered spectrum.
2. Define `Phi` once and use it to state strictness, but expand it in every main
   theorem so the reader does not have to remember the sign convention.
3. Use `k` for degree throughout. Use a different symbol for a Moore-graph
   ambient degree only when two graphs occur simultaneously.
4. Distinguish ordinary graph deletion `G - S` from a deleted incidence matrix
   or block by typography, not by context alone.
5. State whether a spectrum is adjacency or distance every time a new graph is
   introduced.

---

## 7. Proof-status language

Every theorem or proposition promoted from the research stack should carry one
of the following internal labels until final submission:

- **v1:** already in the submitted manuscript;
- **proved/exact:** analytic proof and exact certificate present;
- **audited:** independent one-proof audit completed;
- **finite classification:** exhaustive only inside a precisely named family;
- **conditional:** depends on an explicit unproved or unaudited input;
- **priority unresolved:** correctness supported, novelty not cleared.

These labels need not appear verbatim in the final paper, but the manuscript
must not erase their distinctions. In particular:

- exact computation is not the same as an independent proof audit;
- a classification of a defined deletion family is not a global classification;
- failure to locate prior literature is not a priority theorem.

---

## 8. Current hard boundaries

The integrated stack does **not** establish any of the following:

1. order `38` is globally minimal;
2. no degree-six order-50 counterexample exists;
3. every six-vertex deletion of the Hoffman--Singleton graph fails;
4. a regular diameter-four counterexample exists;
5. every regular diameter-four graph satisfies WOW-284;
6. an unconditional infinite family of strict counterexamples exists;
7. priority for the puncture spectra, LP certificate, diameter bounds, or
   robustness theorem;
8. that exact computation or Lean replaces independent mathematical review.

These nonclaims should appear once, near the end of the introduction or in a
single scope paragraph, rather than being repeated defensively in every section.

---

## 9. Section-level readability checklist

Before a theorem enters `main.tex`, verify that its section answers the following
questions in this order:

1. **What problem does this theorem solve?**
2. **What is the one-sentence mechanism?**
3. **Which earlier theorem does it depend on?**
4. **Which finite or analytic step is genuinely new?**
5. **Where is the exact certificate?**
6. **What does the theorem not claim?**

For a computational theorem, also state:

- the exact finite family being exhausted;
- why the orbit list is exhaustive;
- which arithmetic is exact;
- how the spectral sign is certified;
- whether an independent implementation exists.

---

## 10. Recommended introduction flow

A concise introduction should proceed as follows.

1. State WOW-284 and define `Phi`.
2. Give the Hoffman--Singleton values immediately.
3. State the Moore threshold in one displayed theorem.
4. Explain that the distance spectra themselves are established literature and
   that the contribution is the explicit WOW connection, exact certificates,
   smaller examples, and structural theory.
5. State the diameter-three identity and describe the shifted window.
6. Summarize the degree/diameter localization, degree-six bound, and puncture
   robustness in one paragraph.
7. Give one compact attribution and claim-boundary paragraph.
8. End with a section roadmap.

Do not begin with the coordinate construction, the formalization, or the list of
all finite examples. Those are evidence after the mechanism, not the mechanism.

---

## 11. Suggested review order for the current stack

A reviewer trying to decide what can enter v2 should proceed in this order:

1. v1 Moore and diameter-three proofs;
2. dedicated audit of the degree-six `n <= 50` theorem;
3. all-degree LP ceiling;
4. degree-at-least-six theorem;
5. endpoint-neighbourhood diameter theorem;
6. diameter-four obstruction;
7. one-vertex and adjacent/nonadjacent Moore punctures;
8. small-puncture normal form;
9. Hoffman--Singleton robustness-radius classification;
10. literature-priority clearance for the selected theorem package.

Only after those reviews should the canonical manuscript be rewritten. A green
exact workflow is a merge gate for certificates, not a substitute for this
mathematical order.

---

## 12. Editorial decision

The strongest readable v2 is not the longest one. It should present a coherent
structural paper with six principal theorems and place the remaining exact data
in appendices or companion artifacts. The research repository may remain
comprehensive; the paper should remain selective.