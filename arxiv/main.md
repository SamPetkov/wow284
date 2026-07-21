# The Hoffman-Singleton Graph Refutes WOW-284

**Samuil Petkov**<br>
Ecole normale superieure, Universite PSL, Paris, France<br>
19 July 2026

> Reading copy generated from `main.tex`. The TeX source is authoritative if
> this rendering differs in notation, citations, or layout.

# Introduction

Let $`G`$ be a finite simple connected graph. Write $`D(G)`$ for its distance matrix and order its distance eigenvalues as
``` math
\partial_1(G)\ge \partial_2(G)\ge\cdots\ge\partial_n(G).
```
For a vertex $`v`$, its *dual degree* is the average degree of its neighbors,
``` math
d^*(v)=\frac{1}{d(v)}\sum_{u\in N(v)}d(u),
  \qquad
  \delta^*(G)=\min_{v\in V(G)}d^*(v).
```
Aouchiche and Hansen record the following Graffiti conjecture in their survey of distance spectra ([Aouchiche and Hansen 2014](#ref-AouchicheHansen2014), Conjecture 7.16); they attribute it to Fajtlowicz’s 1998 *Written on the Wall* report ([Fajtlowicz 1998](#ref-Fajtlowicz1998)). The associated public catalogue is DeLaViña’s *Written on the Wall II* site ([DeLaViña n.d.](#ref-DeLaVinaWOWII)).

<div id="conj:wow284" class="conjecture">

**Conjecture 1** (WOW-284). *If $`G`$ is connected, has $`n\ge3`$ vertices, and has girth $`g(G)\ge5`$, then
``` math
\delta^*(G)\le -\partial_n(G).
```*

</div>

The same survey states that the conjecture was open there and notes equality for the Petersen graph. The degree-7 Moore graph constructed by Hoffman and Singleton ([Hoffman and Singleton 1960](#ref-HoffmanSingleton1960)) gives a strict violation.

There is an important prior spectral calculation. Howlader and Panigrahi explicitly give the distance spectrum $`\{91,(-4)^{(28)},1^{(21)}\}`$ of the Hoffman–Singleton graph ([Howlader and Panigrahi 2022](#ref-HowladerPanigrahi2022), Theorem 2.5(1b)). Combining that calculation with 7-regularity already disproves Conjecture <a href="#conj:wow284" data-reference-type="ref" data-reference="conj:wow284">1</a>. The present note records this connection and supplies a self-contained coordinate certificate, so neither the graph identification nor the earlier spectral formula is needed as a premise. No claim is made that the spectrum is new, that this observation has priority over every unpublished observation, or that 50 is the smallest possible order.

<div class="theoremA">

**Theorem A 1**. *There is a simple connected graph $`G`$ on 50 vertices such that
``` math
g(G)=5,\qquad \delta^*(G)=7,\qquad \partial_{50}(G)=-4.
```
In particular, $`G`$ violates WOW-284 by the strict gap $`\delta^*(G)+\partial_{50}(G)=3`$.*

</div>

# Coordinate construction

All subscripts in this section lie in the field $`\mathbb F_5=\mathbb Z/5\mathbb Z`$. Introduce vertices
``` math
V(G)=\{P_{i,j}:i,j\in\mathbb F_5\}\mathbin{\dot\cup}
      \{Q_{k,\ell}:k,\ell\in\mathbb F_5\}.
```
Thus $`|V(G)|=50`$. The edges are the following unordered pairs:
``` math
\begin{align*}
 E_P&=\bigl\{\{P_{i,j},P_{i,j+1}\}:i,j\in\mathbb F_5\bigr\},\\
 E_Q&=\bigl\{\{Q_{k,\ell},Q_{k,\ell+2}\}:k,\ell\in\mathbb F_5\bigr\},\\
 E_X&=\bigl\{\{P_{i,j},Q_{k,ik+j}\}:i,j,k\in\mathbb F_5\bigr\}.
\end{align*}
```
Set $`E(G)=E_P\cup E_Q\cup E_X`$. For a fixed numerical labeling, with representatives in $`\{0,1,2,3,4\}`$, use
``` math
P_{i,j}\longleftrightarrow 5i+j,
 \qquad
 Q_{k,\ell}\longleftrightarrow 25+5k+\ell.
```

The complete neighborhood formulas are
``` math
\begin{align}
 N(P_{i,j})
 &=\{P_{i,j-1},P_{i,j+1}\}
   \cup\{Q_{k,ik+j}:k\in\mathbb F_5\},\label{eq:p-neighborhood}\\
 N(Q_{k,\ell})
 &=\{Q_{k,\ell-2},Q_{k,\ell+2}\}
   \cup\{P_{i,\ell-ik}:i\in\mathbb F_5\}.
   \label{eq:q-neighborhood}
\end{align}
```

<div id="lem:simple-regular" class="lemma">

**Lemma 2**. *The construction defines a simple 7-regular graph with 175 edges.*

</div>

<div class="proof">

*Proof.* Every listed edge has distinct endpoints. Within each of the five fixed $`P`$-layers, addition by $`1`$ gives a 5-cycle; within each fixed $`Q`$-layer, addition by $`2`$ gives a 5-cycle. The cross edges have one endpoint of each type. The set notation removes any possibility of parallel edges.

Equations <a href="#eq:p-neighborhood" data-reference-type="eqref" data-reference="eq:p-neighborhood">[eq:p-neighborhood]</a>–<a href="#eq:q-neighborhood" data-reference-type="eqref" data-reference="eq:q-neighborhood">[eq:q-neighborhood]</a> list seven distinct neighbors at every vertex. There are 25 edges of type $`E_P`$, 25 of type $`E_Q`$, and 125 cross edges, hence 175 in total. Equivalently, the handshake identity gives $`50\cdot7/2=175`$. ◻

</div>

# The common-neighbor certificate

<div id="prop:common-neighbors" class="proposition">

**Proposition 3**. *For any two distinct vertices $`x,y`$,
``` math
|N(x)\cap N(y)|=
 \begin{cases}
 0,&x\sim y,\\
 1,&x\not\sim y.
 \end{cases}
```*

</div>

<div class="proof">

*Proof.* First consider two $`P`$-vertices $`P_{i,j}`$ and $`P_{i',j'}`$. If $`i=i'`$, their layer is a 5-cycle. Adjacent pairs have no common $`P`$-neighbor, while nonadjacent pairs have exactly one. They cannot have a common $`Q`$-neighbor: for fixed $`i`$ and $`k`$, the equation $`Q_{k,\ell}\sim P_{i,j}`$ determines $`j=\ell-ik`$ uniquely. If $`i\ne i'`$, there is no common $`P`$-neighbor, and a common $`Q`$-neighbor must satisfy
``` math
ik+j=i'k+j'.
```
This has the unique solution
``` math
k=\frac{j'-j}{i-i'},\qquad \ell=ik+j,
```
because $`\mathbb F_5`$ is a field.

The argument for two $`Q`$-vertices is dual. If their first coordinates agree, they lie in the 5-cycle generated by steps $`\pm2`$. Adjacent pairs have no common $`Q`$-neighbor and nonadjacent pairs have exactly one; no common $`P`$-neighbor is possible. If $`k\ne k'`$, a common $`P_{i,j}`$ is determined uniquely by
``` math
\ell=ik+j,\qquad \ell'=ik'+j,
```
namely
``` math
i=\frac{\ell-\ell'}{k-k'},\qquad j=\ell-ik.
```

It remains to compare $`P_{i,j}`$ with $`Q_{k,\ell}`$. Put
``` math
r=\ell-(ik+j)\in\mathbb F_5.
```
The pair is adjacent precisely when $`r=0`$. A common $`P`$-vertex must be $`P_{i,j+s}`$ with $`s\in\{\pm1\}`$, and it is adjacent to $`Q_{k,\ell}`$ precisely when $`r=s`$. Hence there is exactly one common $`P`$-neighbor if $`r\in\{\pm1\}`$, and none otherwise. A common $`Q`$-vertex must be $`Q_{k,\ell+t}`$ with $`t\in\{\pm2\}`$, and it is adjacent to $`P_{i,j}`$ precisely when $`t=-r`$. Hence there is exactly one common $`Q`$-neighbor if $`r\in\{\pm2\}`$, and none otherwise. Finally,
``` math
\mathbb F_5=\{0\}\mathbin{\dot\cup}\{\pm1\}
          \mathbin{\dot\cup}\{\pm2\},
```
which proves every cross case and completes the certificate. ◻

</div>

<div id="cor:geometry" class="corollary">

**Corollary 4**. *The graph is connected, has diameter two, and has girth five.*

</div>

<div class="proof">

*Proof.* Every pair of distinct vertices is adjacent or has a common neighbor, so the graph is connected and has diameter at most two. It is not complete, since it is 7-regular on 50 vertices, so its diameter is exactly two.

A triangle would give an adjacent pair a common neighbor. In a 4-cycle, two opposite vertices would have the other two cycle vertices as distinct common neighbors. Both possibilities contradict Proposition <a href="#prop:common-neighbors" data-reference-type="ref" data-reference="prop:common-neighbors">3</a>. Thus $`g(G)\ge5`$. On the other hand, for every fixed $`i`$,
``` math
P_{i,0}P_{i,1}P_{i,2}P_{i,3}P_{i,4}P_{i,0}
```
is a 5-cycle, so $`g(G)=5`$. ◻

</div>

# Exact spectral calculation

Let $`A`$ be the adjacency matrix, let $`I`$ be the $`50\times50`$ identity matrix, and let $`J`$ be the all-ones matrix. Proposition <a href="#prop:common-neighbors" data-reference-type="ref" data-reference="prop:common-neighbors">3</a> gives, entry by entry,
``` math
\begin{equation}
\label{eq:a-square}
 A^2=6I-A+J.
\end{equation}
```
Indeed, the diagonal entries on both sides are 7, the entries indexed by edges are 0, and all other off-diagonal entries are 1.

Since the graph is connected and 7-regular, $`A\mathbf 1=7\mathbf 1`$, with this eigenvalue simple. On $`\mathbf 1^\perp`$, equation <a href="#eq:a-square" data-reference-type="eqref" data-reference="eq:a-square">[eq:a-square]</a> becomes
``` math
A^2+A-6I=0.
```
Thus the other adjacency eigenvalues are $`2`$ and $`-3`$. If their multiplicities are $`m_2`$ and $`m_{-3}`$, then
``` math
m_2+m_{-3}=49,
 \qquad
 7+2m_2-3m_{-3}=\operatorname{tr}A=0.
```
Consequently
``` math
\begin{equation}
\label{eq:adjacency-spectrum}
 \operatorname{Spec}(A)=\{7^{(1)},2^{(28)},(-3)^{(21)}\}.
\end{equation}
```

By Corollary <a href="#cor:geometry" data-reference-type="ref" data-reference="cor:geometry">4</a>, two distinct vertices are at distance one on edges and distance two on nonedges. Therefore
``` math
\begin{equation}
\label{eq:distance-matrix}
 D=A+2(J-I-A)=2J-2I-A.
\end{equation}
```
On $`\mathbf 1`$, the distance matrix has eigenvalue
``` math
2\cdot50-2-7=91.
```
If $`x\in\mathbf 1^\perp`$ and $`Ax=\theta x`$, then
``` math
Dx=(-2I-A)x=(-2-\theta)x.
```
Using <a href="#eq:adjacency-spectrum" data-reference-type="eqref" data-reference="eq:adjacency-spectrum">[eq:adjacency-spectrum]</a>, we obtain
``` math
\begin{equation}
\label{eq:distance-spectrum}
 \operatorname{Spec}(D)=\{91^{(1)},1^{(21)},(-4)^{(28)}\},
\end{equation}
```
or equivalently
``` math
\det(xI-D)=(x-91)(x-1)^{21}(x+4)^{28}.
```

<div class="proof">

*Proof of Theorem A.* Corollary <a href="#cor:geometry" data-reference-type="ref" data-reference="cor:geometry">4</a> gives connectedness and $`g(G)=5`$. By Lemma <a href="#lem:simple-regular" data-reference-type="ref" data-reference="lem:simple-regular">2</a>, every vertex and every one of its neighbors has degree 7, so
``` math
d^*(v)=\frac{1}{7}\sum_{u\in N(v)}7=7
```
for every $`v`$, and hence $`\delta^*(G)=7`$. Equation <a href="#eq:distance-spectrum" data-reference-type="eqref" data-reference="eq:distance-spectrum">[eq:distance-spectrum]</a> gives $`\partial_{50}(G)=-4`$. Thus
``` math
\delta^*(G)=7>4=-\partial_{50}(G),
 \qquad
 \delta^*(G)+\partial_{50}(G)=3>0.
```
This is a strict counterexample to WOW-284. ◻

</div>

As a further exact certificate, the eigenvalues of $`D+7I`$ are $`98`$, $`8`$ with multiplicity 21, and $`3`$ with multiplicity 28. Thus $`D+7I`$ is positive definite.

# Computational certificate

The proof above is entirely analytic. The accompanying Python code supplies a separate exact check from the coordinate rules. It performs the following steps:

1.  constructs the 175 unordered edges and checks all 50 degrees;

2.  checks the common-neighbor count for every unordered vertex pair;

3.  constructs all 2,500 distance entries by integer breadth-first search;

4.  computes the distance characteristic polynomial symbolically; and

5.  computes an exact rational $`LDL^{\mathsf T}`$ decomposition of $`D+7I`$ and checks that all 50 pivots are positive.

The symbolic steps use SymPy ([Meurer et al. 2017](#ref-MeurerEtAl2017)). The expected output is
``` math
(x-91)(x-1)^{21}(x+4)^{28}
```
together with 50 positive rational pivots. Because the distance matrix is built by BFS, this check does not use equation <a href="#eq:distance-matrix" data-reference-type="eqref" data-reference="eq:distance-matrix">[eq:distance-matrix]</a> or the spectral derivation above. Numerical agreement is not treated as a proof; all calculations in the certificate are exact.

# Scope, provenance, and disclosures

The counterexample has order 50. No minimality claim is made, and no exhaustive search over smaller graphs is part of this note. The repository’s source ledger distinguishes the published distance spectrum from the explicit WOW-284 connection and records the limits of the targeted priority search.

The graph construction and counterexample claim were supplied by the author. OpenAI Codex assisted with adversarial proof checking, source discovery, editorial restructuring, LaTeX preparation, and reproducibility code. No AI system is an author. Samuil Petkov is the sole named author and assumes full responsibility for the mathematics, citations, attribution, and conclusions.

The author received no funding for this work and declares no competing interests. The manuscript source, exact verification code, machine-readable certificates, and build instructions are available in the public repository [`github.com/SamPetkov/wow284`](https://github.com/SamPetkov/wow284).

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-AouchicheHansen2014" class="csl-entry">

Aouchiche, Mustapha, and Pierre Hansen. 2014. “Distance Spectra of Graphs: A Survey.” *Linear Algebra and Its Applications* 458: 301–86. <https://doi.org/10.1016/j.laa.2014.06.010>.

</div>

<div id="ref-DeLaVinaWOWII" class="csl-entry">

DeLaViña, Ermelinda. n.d. *Written on the Wall II*. Online conjecture catalogue. <http://cms.dt.uh.edu/faculty/delavinae/research/wowII/list.htm>.

</div>

<div id="ref-Fajtlowicz1998" class="csl-entry">

Fajtlowicz, Siemion. 1998. *Written on the Wall: Conjectures Derived on the Basis of the Program Galatea Gabriella Graffiti*. Technical report. University of Houston.

</div>

<div id="ref-HoffmanSingleton1960" class="csl-entry">

Hoffman, Alan J., and Robert R. Singleton. 1960. “On Moore Graphs with Diameters 2 and 3.” *IBM Journal of Research and Development* 4 (5): 497–504. <https://doi.org/10.1147/rd.45.0497>.

</div>

<div id="ref-HowladerPanigrahi2022" class="csl-entry">

Howlader, Aditi, and Pratima Panigrahi. 2022. “On the Distance Spectrum of Minimal Cages and Associated Distance Biregular Graphs.” *Linear Algebra and Its Applications* 636: 115–33. <https://doi.org/10.1016/j.laa.2021.11.014>.

</div>

<div id="ref-MeurerEtAl2017" class="csl-entry">

Meurer, Aaron, Christopher P. Smith, Mateusz Paprocki, et al. 2017. “SymPy: Symbolic Computing in Python.” *PeerJ Computer Science* 3: e103. <https://doi.org/10.7717/peerj-cs.103>.

</div>

</div>
