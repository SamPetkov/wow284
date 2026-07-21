# Author-supplied result, normalized summary

The author supplied an explicit graph on vertices

```text
P_(i,j), Q_(i,j),  i,j in F_5,
```

with same-type cycle edges

```text
P_(i,j) -- P_(i,j+1),
Q_(i,j) -- Q_(i,j+2),
```

and cross edges

```text
P_(i,j) -- Q_(k,ik+j).
```

The supplied proof claimed and derived

```text
g(G) = 5,
delta*(G) = 7,
partial_50(G) = -4,
delta*(G) + partial_50(G) = 3 > 0.
```

It also supplied an exact Python/SymPy verification based on BFS distances,
the distance characteristic polynomial, and an exact rational LDL
decomposition of `D+7I`.

The canonical manuscript is a proof-audited and source-attributed
reorganization of that material. This note is not a verbatim archival copy of
the originally pasted Markdown, which contained transport-encoding damage.
