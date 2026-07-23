# Adversarial handoff: proposed 40-vertex WOW-284 counterexample

Please audit this claim from first principles. Do not trust the claimed spectra
or the accompanying script merely because they agree. Look specifically for a
wrong deletion set, a hidden disconnection, a girth/diameter error, a dual-degree
definition mismatch, a characteristic-polynomial convention error, or an
incorrect block-matrix multiplicity count.

## Exact claim

Work over `F_5`, with every subscript reduced modulo 5. The
Hoffman--Singleton coordinate graph has vertices

```math
\{P_{i,j}:i,j\in\mathbb F_5\}\sqcup
\{Q_{k,\ell}:k,\ell\in\mathbb F_5\}
```

and edges

```math
P_{i,j}\sim P_{i,j+1},\qquad
Q_{k,\ell}\sim Q_{k,\ell+2},\qquad
P_{i,j}\sim Q_{k,ik+j}.
```

Delete the ten vertices

```math
\{P_{0,j},Q_{0,j}:j\in\mathbb F_5\}.
```

They induce a Petersen graph. Let `B` be the adjacency matrix and `D` the
ordinary graph-distance matrix of the remaining graph `R`.

The claims to check are:

```math
|V(R)|=40,\quad |E(R)|=120,\quad R\text{ is 6-regular},
\quad g(R)=5,\quad \operatorname{diam}(R)=3,
```

```math
\chi_B(x)=(x-6)(x-2)^{18}(x-1)^4(x+2)^5(x+3)^{12},
```

```math
\chi_D(x)=(x-75)(x-3)^5x^{16}(x+5)^{18}.
```

Because the graph is 6-regular, every dual degree is 6. Thus

```math
\delta^*(R)=6>5=-\lambda_{\min}(D),
```

which would make `R` a strict counterexample to WOW-284.

## Analytic proof to audit

Order the full Hoffman--Singleton adjacency matrix in the block form

```math
A_{HS}=\begin{pmatrix}B&C\\C^{\mathsf T}&P\end{pmatrix},
```

where `P` is the adjacency matrix of the deleted Petersen graph. The proposed
proof uses

```math
C^{\mathsf T}C=4I,
\qquad
A_{HS}^2=6I-A_{HS}+J,
\qquad
BC=C(J-I-P).
```

Since

```math
\operatorname{Spec}(P)=\{3^{(1)},1^{(5)},(-2)^{(4)}\},
```

the restriction of `B` to `col(C)` should have spectrum
`{6^(1),(-2)^(5),1^(4)}`. On `ker(C^T)`, the top-left block identity should
reduce to

```math
B^2+B-6I=0.
```

The remaining 30 eigenvalues are therefore 2 or -3; dimension and
`tr(B)=0` should force multiplicities 18 and 12.

For any connected `k`-regular graph of girth at least five and diameter three,
the distance matrices satisfy

```math
A_2=A^2-kI,
\qquad
D=3J+(k-3)I-2A-A^2.
```

With `k=6`, every nonprincipal adjacency eigenvalue `theta` should therefore
map to

```math
4-(\theta+1)^2,
```

while the all-ones vector should have distance eigenvalue 75. Check every step
and multiplicity independently.

## Reproduction

Run:

```bash
python verify_40.py
```

The script requires Python 3.11+ and SymPy 1.14. It builds graph distances by
independent breadth-first searches and uses exact integer characteristic
polynomials. It also checks the block identities. Please independently inspect
the mathematics rather than treating a `PASS` line as a proof.

## Classical construction sources

- M. O'Keefe and Pak-Ken Wong, “A smallest graph of girth 5 and valency 6,”
  *Journal of Combinatorial Theory, Series B* 26(2) (1979), 145--149,
  <https://doi.org/10.1016/0095-8956(79)90052-2>.
- Pak-Ken Wong, “On the uniqueness of the smallest graph of girth 5 and
  valency 6,” *Journal of Graph Theory* 3(4) (1979), 407--409,
  <https://doi.org/10.1002/jgt.3190030413>.
- Geoffrey Exoo and Robert Jajcay, “Dynamic Cage Survey,” Section 2.1.11,
  <https://doi.org/10.37236/37>. It explicitly describes the unique `(6,5)`
  cage as Hoffman--Singleton with an induced Petersen graph removed.
- M. Klin, M. Muzychuk, and M. Ziv-Av, “Higmanian Rank-5 Association Schemes
  on 40 Points,” *Michigan Mathematical Journal* 58 (2009), 255--284,
  <https://doi.org/10.1307/mmj/1242071692>.

No source located so far explicitly states this distance spectrum or its
connection to WOW-284. Do not infer novelty or priority from that negative
search. The current Lean artifact in `wow284` verifies only the 50-vertex
Hoffman--Singleton counterexample, not this proposed 40-vertex graph.
