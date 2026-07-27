# WOW-284: reader-first prose revision

## Scope

This document is a concrete exposition pass for the WOW-284 manuscript and its
selective Version 2 extension.  It is not a new mathematical claim.  The goals
are to make the elementary disproof visible immediately, separate conceptual
arguments from finite certificates, and prevent the post-v1 research stack from
turning the paper into a theorem ledger.

The proposed prose follows three rules.

1. **State the shortest disproof first.**  A reader should see within one page
   that a degree-seven Moore graph has minimum dual degree \(7\) and least
   distance eigenvalue \(-4\).
2. **Separate mechanism from certification.**  The Moore calculation and the
   diameter-three operator identity belong in the main narrative.  Long
   characteristic polynomials, orbit tables, and rational pivot ledgers belong
   in appendices or the repository.
3. **Promote only audited extensions.**  The post-v1 synthesis remains a source
   ledger.  A Version 2 manuscript should contain only results whose theorem
   statement, hypotheses, proof, exact verifier, and literature boundary have
   passed their dedicated gates.

## The paper in one paragraph

WOW-284 predicts that every connected graph of order at least three and girth
at least five satisfies

\[
  \delta^*(G)\le -\lambda_{\min}(D(G)).
\]

The conjecture fails already for the Hoffman--Singleton graph.  More generally,
if \(G\) is a degree-\(k\) Moore graph of diameter two, then

\[
  \delta^*(G)=k,
  \qquad
  \lambda_{\min}(D(G))=-\frac{3+\sqrt{4k-3}}2.
\]

Hence the conjectured inequality holds exactly for \(k\le3\), with equality at
\(k=3\), and fails for every realizable \(k>3\).  The degree-seven
Hoffman--Singleton graph therefore gives the explicit strict gap
\(7-4=3\).  The rest of the paper explains this mechanism self-containedly,
extracts smaller induced counterexamples, and records the broader
adjacency-spectral criterion for regular diameter-three graphs.

## Recommended title and abstract logic

The existing title is appropriate.  The abstract should be ordered as follows:

1. state the conjecture;
2. give the Hoffman--Singleton disproof and the Moore threshold;
3. state the diameter-three operator identity;
4. list the smaller exact examples;
5. state the exact-computation and Lean scope.

This ordering is preferable to leading with the full list of graph orders.  The
mathematical reason the conjecture fails is more important than the inventory
of examples.

A copy-ready abstract and introduction are provided in
`V2_READER_FIRST_FRONT_MATTER.tex`.

## Main-text architecture

### 1. Conjecture and immediate disproof

Define \(D(G)\), \(\lambda_{\min}(D(G))\), and \(\delta^*(G)\), state WOW-284,
and then state the Moore-graph theorem.  The reader should know the verdict
before any coordinate construction appears.

The introduction should say explicitly:

> The disproof is short.  The work of the paper is to isolate the general
> spectral mechanism, give self-contained exact certificates, and determine how
> far the mechanism survives under natural deletions and diameter constraints.

### 2. Moore-graph mechanism

Keep the current derivation, but compress the narrative around the three
load-bearing identities:

\[
  A^2=(k-1)I-A+J,
  \qquad
  D=2J-2I-A,
\]

and

\[
  \lambda_{\min}(D)=-\frac{3+\sqrt{4k-3}}2.
\]

The multiplicity formulas are useful, but they should not interrupt the main
threshold calculation.  They may be stated after the least-eigenvalue formula
or moved to a short remark.

### 3. Explicit coordinate certificate

Present the coordinate graph as a reproducibility certificate rather than as
the conceptual origin of the proof.  Open the section with:

> The preceding theorem already disproves WOW-284 once the
> Hoffman--Singleton graph is invoked.  We now give a labelled coordinate model
> so that every structural and spectral assertion can be checked directly.

The common-neighbour case split should remain self-contained, but its role must
be described once and not repeatedly: it proves simplicity, regularity,
diameter two, and girth five in one certificate.

### 4. Smaller induced counterexamples

Group the examples by mechanism rather than order.

- **Petersen deletion:** the 40-vertex regular example and its invariant-space
  decomposition.
- **Small punctures of the 40-vertex graph:** the 39- and 38-vertex examples.
- **Second subconstituent:** the 42-vertex regular example.

The main text should state exact dual degrees and least-eigenvalue information,
while full characteristic-polynomial factorizations and LDL data should be
sent to an appendix or the repository.

### 5. Diameter-three spectral mechanism

Move the identity

\[
  D=3J+(k-3)I-2A-A^2
\]

forward.  It is the second conceptual theorem of the paper and should appear
before long finite-certificate details whenever the section order is revised.
The reader-facing interpretation is

\[
  \Phi(G)=2k-2-\max_{\theta\ne k}(\theta+1)^2.
\]

Thus regular diameter-three failure is controlled by how tightly the
nonprincipal adjacency spectrum is concentrated around \(-1\).

### 6. Selective Version 2 extensions

A coherent Version 2 should contain at most the following theorem chain.

1. regular strict counterexamples have degree at least six;
2. regular strict counterexamples have diameter at most four;
3. the diameter-four regime begins only at degree ten;
4. the standard one-point nonbacktracking LP hierarchy has an exact ceiling;
5. every degree-six regular strict counterexample has order at most fifty;
6. small Moore punctures admit a common normal form, with an exact
   Hoffman--Singleton deletion-robustness radius.

Each theorem should begin with one sentence explaining its role.  For example:

> The Moore and diameter-three constructions show how failure occurs.  The next
> theorem shows where a regular counterexample cannot occur.

Do not insert the full order-50 feasibility system, the 120 matching-deletion
classification, orbit tables, or long characteristic polynomials into the
main narrative.  They are valuable exact artifacts, but they are not part of
the shortest mathematical story.

## Recurrent prose corrections

### Prefer statements to announcements

Replace sentences of the form

> We now proceed to prove the following exact result.

with the result or its mathematical motivation directly.

### Use one name for each quantity

Use `least distance eigenvalue` in prose and
\(\lambda_{\min}(D(G))\) in formulas.  Avoid alternating among
`∂_n`, `lambda_D`, and `least root` inside one proof unless the notation is
being translated explicitly.

Use `WOW score`

\[
  \Phi(G)=\delta^*(G)+\lambda_{\min}(D(G))
\]

only after it has been defined, and then use it consistently.

### Distinguish proof from certificate

Use the following vocabulary throughout.

- **proof:** the mathematical reduction showing why a claim follows;
- **exact certificate:** finite data whose stated identity or sign is checked;
- **verifier:** the program reconstructing and checking the certificate;
- **formalisation:** the Lean theorem and its precise imported-axiom scope.

This prevents an executable calculation from being described as though it were
itself the conceptual proof.

### Compress claim boundaries

One compact paragraph in the introduction and one final limitations paragraph
are sufficient.  Do not repeat the same nonclaims after every construction.
Point-of-use qualifications remain appropriate where a result is computational
or where literature priority is unresolved.

## Appendix policy

Move or retain outside the main narrative:

- full characteristic polynomials not used in a displayed theorem;
- complete Sturm chains and LDL pivot ledgers;
- automorphism generators and deletion-orbit tables;
- the 266 surviving order-50 coarse profiles;
- implementation details of generated Lean matrix shards;
- fail-closed CI and provenance mechanics.

The main paper should explain what each artifact certifies and point to its
stable repository path.

## Proposed opening transitions

Before the Moore section:

> The counterexample is a consequence of a general calculation for Moore
> graphs.  We derive it without using the classification of Moore graphs.

Before the coordinate section:

> The spectral calculation above is conceptual.  The following coordinate model
> supplies a fully labelled certificate for the degree-seven instance.

Before the 40-vertex section:

> The same ambient graph contains smaller counterexamples.  The first is
> regular and retains enough symmetry for a short invariant-subspace proof.

Before the diameter-three section:

> The preceding examples share a common operator identity.  In diameter three,
> the distance matrix is a quadratic polynomial in the adjacency matrix, so the
> conjecture becomes an exact shifted-spectrum condition.

Before the Version 2 obstruction section:

> We now turn from constructions to restrictions: how small can the degree and
> diameter of a regular strict counterexample be?

## Editorial acceptance test

A reader who knows basic spectral graph theory should be able to answer the
following after the first two pages.

1. What is WOW-284?
2. Which graph disproves it?
3. Why is its minimum dual degree \(7\)?
4. Why is its least distance eigenvalue \(-4\)?
5. What is the general Moore threshold?
6. What is the diameter-three spectral criterion?

If any answer requires consulting a computational appendix, the main
exposition is still too indirect.
