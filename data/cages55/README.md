# Fixed records of the four `(5,5)`-cages

These four graph6 files support the exact low-degree regular obstruction in
`scripts/verify_regular_low_degree.py`.

## Source identification

Meringer proved that exactly four 5-regular graphs of girth five attain the
minimum order 30:

- M. Meringer, “Fast Generation of Regular Graphs and Construction of Cages,”
  *Journal of Graph Theory* **30** (1999), 137–146,
  DOI: <https://doi.org/10.1002/(SICI)1097-0118(199902)30:2%3C137::AID-JGT7%3E3.0.CO;2-G>.

The names and public fixed-label adjacency prefixes are identified through
House of Graphs:

| Local file | House of Graphs ID | Public name |
| --- | ---: | --- |
| `foster.graph6` | [48173](https://houseofgraphs.org/graphs/48173) | Foster cage |
| `meringer.graph6` | [1227](https://houseofgraphs.org/graphs/1227) | Meringer graph |
| `robertson_wegner.graph6` | [1290](https://houseofgraphs.org/graphs/1290) | Robertson–Wegner graph |
| `wong.graph6` | [1433](https://houseofgraphs.org/graphs/1433) | Wong graph |

For the database itself, cite:

- K. Coolsaet, S. D'hondt, and J. Goedgebeur, “House of Graphs 2.0: A
  Database of Interesting Graphs and More,” *Discrete Applied Mathematics*
  **325** (2023), 97–107.

## Reconstruction and independent checks

The files are fixed-label reconstructions, not claims of byte-for-byte export
from the House of Graphs download button. The reconstruction fixed the first
ten public adjacency rows shown on each House page and solved the remaining
0–1 incidence constraints subject to:

- 30 vertices;
- degree five at every vertex;
- no triangle;
- no 4-cycle.

The committed verifier then checks independently that every record has:

- 75 edges, connectedness, girth five, and diameter three;
- the displayed first ten House of Graphs adjacency rows;
- the complete exact adjacency characteristic polynomial;
- the complete exact distance characteristic polynomial;
- the expected automorphism-group order;
- pairwise nonisomorphism from the other three records.

The automorphism-group orders are respectively 30, 96, 20, and 120. Together
with Meringer's exhaustive count of four `(5,5)`-cages, these four nonisomorphic
records exhaust the degree-five cage case used by the proof.

## Reproducibility

Run from the repository root:

```text
python scripts/verify_regular_low_degree.py
```

The verifier uses NetworkX 3.6.1 for graph6 decoding and exact graph
isomorphism enumeration, and SymPy 1.14.0 for integer characteristic
polynomials. No floating-point eigenvalue is used for a theorem.
