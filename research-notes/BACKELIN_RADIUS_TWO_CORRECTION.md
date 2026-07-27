# Backelin correction for the radius-two dual-degree identity

**Audit status:** literature-established elementary identity.
**Effect on the prior v1 manuscript package:** none; this note controls the completed v2 wording.

For a graph with no triangle or 4-cycle, the project uses

\[
  d^*(v)=\frac{|B_2(v)|-1}{d(v)}.
\]

This follows by writing

\[
  |B_2(v)|
  =1+d(v)+\sum_{u\in N(v)}(d(u)-1)
  =1+\sum_{u\in N(v)}d(u).
\]

A direct published precedent is Jörgen Backelin,
*Sizes of the Extremal Girth 5 Graphs of Orders from 40 to 49*,
arXiv:1511.08128. Backelin defines

\[
  \deg^2(v)=\sum_{w\in N(v)}\deg(w)
\]

as the second degree and proves in Lemma 2.1 that, for girth at least five,

\[
  |B(v;2)|=\deg^2(v)+1.
\]

Dividing by \(d(v)\) gives the project's dual-degree identity exactly.

## Required wording

Use:

> By Backelin's radius-two identity, the dual degree is the second degree
> normalized by the ordinary degree:
> \(d^*(v)=(|B_2(v)|-1)/d(v)\).

Do not describe this identity as newly introduced or source-unlocated.

## Source

J. Backelin, *Sizes of the Extremal Girth 5 Graphs of Orders from 40 to 49*,
arXiv:1511.08128 (2015), Lemma 2.1.
