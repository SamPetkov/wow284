# Moore Graphs of Diameter Two and the Failure of WOW-284

**Samuil Petkov**<br>
Ecole normale superieure, Universite PSL, Paris, France<br>
19 July 2026

> Reading copy generated from `main.tex`. The TeX source is authoritative if
> this rendering differs in notation, citations, or layout.

# Introduction

Let $`G`$ be a finite simple connected graph on $`n\ge2`$ vertices. Its distance matrix is $`D(G)=(d_G(u,v))_{u,v\in V(G)}`$, where $`d_G`$ is graph distance. This matrix is real symmetric; order its real eigenvalues as
``` math
\partial_1(G)\ge \partial_2(G)\ge\cdots\ge\partial_n(G).
```
For a vertex $`v`$, its *dual degree* is the average degree of its neighbors,
``` math
d^*(v)=\frac{1}{d(v)}\sum_{u\in N(v)}d(u),
  \qquad
  \delta^*(G)=\min_{v\in V(G)}d^*(v).
```
Write $`g(G)`$ for the shortest-cycle length, with $`g(G)=\infty`$ for an acyclic graph; spectral superscripts indicate algebraic multiplicity.

Aouchiche and Hansen record the following Graffiti conjecture in their survey of distance spectra ([Aouchiche and Hansen 2014](#ref-AouchicheHansen2014), Conjecture 7.16, p. 370); they attribute it to Fajtlowicz’s 1998 *Written on the Wall* report ([Fajtlowicz 1998](#ref-Fajtlowicz1998)). For related historical context, see DeLaViña’s separate *Written on the Wall II* catalogue ([DeLaViña n.d.](#ref-DeLaVinaWOWII)).

<div id="conj:wow284" class="conjecture">

**Conjecture 1** (WOW-284). *If $`G`$ is connected, has $`n\ge3`$ vertices, and has girth $`g(G)\ge5`$, then
``` math
\delta^*(G)\le -\partial_n(G).
```*

</div>

In that 2014 survey, the authors reported that the conjecture remained open and noted equality for the Petersen graph ([Aouchiche and Hansen 2014](#ref-AouchicheHansen2014), Conjecture 7.16, p. 370). This equality is the degree-3 boundary case of a general Moore-graph calculation. The degree-7 Moore graph constructed by Hoffman and Singleton ([Hoffman and Singleton 1960](#ref-HoffmanSingleton1960)) lies beyond that boundary and gives a strict violation.

There is important prior spectral work. Howlader and Panigrahi determine a distance polynomial for minimal $`(k,5)`$-cages and explicitly list the distance spectra of the Petersen, Hoffman–Singleton, and hypothetical degree-57 Moore graphs ([Howlader and Panigrahi 2022](#ref-HowladerPanigrahi2022), Theorems 2.3 and 2.5(1)); the existence of the last graph remains open ([Smith and Montemanni 2026](#ref-SmithMontemanni2026)). Their $`k=7`$ calculation, together with regularity and the girth condition, already supplies every ingredient needed to disprove Conjecture <a href="#conj:wow284" data-reference-type="ref" data-reference="conj:wow284">1</a>. The present note records the sharp degree criterion, makes the WOW-284 connection explicit, and supplies a self-contained coordinate certificate. No claim is made that the distance spectra are new, that this observation has priority over every unpublished observation, or that 50 is the smallest possible order.

<span id="thm:moore-wow" label="thm:moore-wow"></span>

<div class="theoremA">

**Theorem A 1**. *Let $`G`$ be a Moore graph of diameter two and degree $`k\ge2`$. Then
``` math
|V(G)|=k^2+1,\qquad g(G)=5,\qquad \delta^*(G)=k,
 \qquad
 \partial_{k^2+1}(G)=-\frac{3+\sqrt{4k-3}}2.
```
Consequently $`G`$ satisfies the inequality in WOW-284 if and only if $`k\le3`$, with equality exactly when $`k=3`$.*

</div>

# The Moore-graph mechanism

A *Moore graph of diameter two and degree $`k`$* is a finite simple connected $`k`$-regular graph of diameter two attaining the Moore bound $`|V(G)|\le 1+k+k(k-1)=k^2+1`$. We include the short derivation needed for [Theorem A](#thm:moore-wow); no classification of Moore graphs is used.

Fix a vertex $`v`$. Its $`k`$ neighbors initiate $`k(k-1)`$ nonbacktracking walks of length two. Exactly $`k(k-1)`$ vertices lie outside $`\{v\}\cup N(v)`$, and diameter two makes every one of them the endpoint of at least one such walk. The endpoint map is therefore a surjection between finite sets of the same size, hence a bijection. Applying the same argument at each vertex shows that adjacent vertices have no common neighbor, whereas nonadjacent vertices have exactly one. Thus there are no triangles or 4-cycles. To exhibit a 5-cycle, take an edge $`uv`$, choose $`x\in N(u)\setminus\{v\}`$ and $`y\in N(v)\setminus\{u\}`$, and let $`z`$ be the unique common neighbor of the necessarily nonadjacent vertices $`x,y`$. The absence of triangles and 4-cycles makes these five vertices distinct, so $`uxzyvu`$ is a 5-cycle. Hence $`g(G)=5`$.

Let $`A`$, $`I`$, and $`J`$ denote the adjacency, identity, and all-ones matrices of order $`n=k^2+1`$. The common-neighbor counts give, entry by entry,
``` math
\begin{equation}
\label{eq:general-a-square}
 A^2=(k-1)I-A+J.
\end{equation}
```
Indeed, the diagonal entries are $`k`$, the entries indexed by edges are zero, and the remaining off-diagonal entries are one. Since $`A\mathbf 1=k\mathbf 1`$ and the graph is connected, the eigenvalue $`k`$ is simple. For example, for $`x\in\mathbb R^n`$,
``` math
x^{\mathsf T}(kI-A)x
   =\sum_{\{u,v\}\in E(G)}(x_u-x_v)^2,
```
so equality holds only for constant $`x`$. The real symmetric matrix $`A`$ preserves $`\mathbf 1^\perp`$, and <a href="#eq:general-a-square" data-reference-type="eqref" data-reference="eq:general-a-square">[eq:general-a-square]</a> restricts there to
``` math
A^2+A-(k-1)I=0.
```
Writing $`q=\sqrt{4k-3}`$, the two nonprincipal adjacency eigenvalues are
``` math
r=\frac{-1+q}{2},\qquad s=\frac{-1-q}{2}.
```
Their multiplicities, obtained from their sum $`k^2`$ and $`\operatorname{tr}A=0`$, are
``` math
\begin{equation}
\label{eq:general-multiplicities}
 m_r=\frac12\left(k^2+\frac{k(k-2)}q\right),\qquad
 m_s=\frac12\left(k^2-\frac{k(k-2)}q\right).
\end{equation}
```

Every nonedge joins vertices at distance two, so
``` math
\begin{equation}
\label{eq:general-distance}
 D=2J-2I-A.
\end{equation}
```
It follows that the full distance spectrum is
``` math
\begin{equation}
\label{eq:general-distance-spectrum}
 \operatorname{Spec}(D)=
 \left\{(2k^2-k)^{(1)},
 \left(\frac{q-3}{2}\right)^{(m_s)},
 \left(-\frac{q+3}{2}\right)^{(m_r)}\right\}.
\end{equation}
```
In particular, the last displayed eigenvalue is the least one. Regularity gives $`\delta^*(G)=k`$. Hence the conjectured inequality is
``` math
k\le\frac{3+\sqrt{4k-3}}2.
```
For $`k\ge2`$, comparison after moving 3 to the left is legitimate, and
``` math
(2k-3)^2-(4k-3)=4(k-1)(k-3).
```
Thus the inequality is strict for $`k=2`$, is an equality for $`k=3`$, and fails precisely for $`k>3`$. This proves [Theorem A](#thm:moore-wow).

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

After reindexing the $`Q`$-layers by $`k\mapsto-k`$, these are exactly Hafner’s affine-coordinate form of Robertson’s pentagon-and-pentagram construction ([Hafner 2003, sec. 2](#ref-Hafner2003) and Theorem 2.1). Thus $`G`$ is the Hoffman–Singleton graph; all properties needed here are proved directly.

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

Equations <a href="#eq:p-neighborhood" data-reference-type="eqref" data-reference="eq:p-neighborhood">[eq:p-neighborhood]</a>–<a href="#eq:q-neighborhood" data-reference-type="eqref" data-reference="eq:q-neighborhood">[eq:q-neighborhood]</a> list seven distinct neighbors at every vertex. For a $`P`$-vertex, the two same-layer neighbors are distinct because $`1\ne-1`$ in $`\mathbb F_5`$; the five cross neighbors are distinct because their first $`Q`$-coordinates are distinct; and the two types cannot overlap. The $`Q`$-case is identical with steps $`\pm2`$. There are 25 edges of type $`E_P`$, 25 of type $`E_Q`$, and 125 cross edges, hence 175 in total. Equivalently, the handshake identity gives $`50\cdot7/2=175`$. ◻

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

*Proof.* First consider two $`P`$-vertices $`P_{i,j}`$ and $`P_{i',j'}`$. If $`i=i'`$, their layer is a 5-cycle. Adjacent pairs have no common $`P`$-neighbor. If, for example, $`j'=j+2`$, the unique common $`P`$-neighbor is $`P_{i,j+1}`$; the case $`j'=j-2`$ is analogous. They cannot have a common $`Q`$-neighbor: for fixed $`i`$ and $`k`$, the equation $`Q_{k,\ell}\sim P_{i,j}`$ determines $`j=\ell-ik`$ uniquely. If $`i\ne i'`$, there is no common $`P`$-neighbor, and a common $`Q`$-neighbor must satisfy
``` math
ik+j=i'k+j'.
```
This has the unique solution
``` math
k=\frac{j'-j}{i-i'},\qquad \ell=ik+j,
```
because $`\mathbb F_5`$ is a field.

The argument for two $`Q`$-vertices is dual. If their first coordinates agree, they lie in the 5-cycle generated by steps $`\pm2`$. Adjacent pairs have no common $`Q`$-neighbor. For a nonadjacent pair, whose second coordinates differ by $`\pm1`$, direct intersection of the two sets of $`\pm2`$-neighbors gives exactly one common $`Q`$-neighbor; no common $`P`$-neighbor is possible. If $`k\ne k'`$, a common $`P_{i,j}`$ is determined uniquely by
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

# The explicit counterexample

The graph just constructed is 7-regular on $`50=7^2+1`$ vertices and has diameter two. It is therefore a Moore graph to which [Theorem A](#thm:moore-wow) applies. Substituting $`k=7`$ into <a href="#eq:general-distance-spectrum" data-reference-type="eqref" data-reference="eq:general-distance-spectrum">[eq:general-distance-spectrum]</a> gives
``` math
\begin{equation}
\label{eq:distance-spectrum}
 \operatorname{Spec}(D)=\{91^{(1)},1^{(21)},(-4)^{(28)}\},
\end{equation}
```
or equivalently
``` math
\det(tI-D)=(t-91)(t-1)^{21}(t+4)^{28}.
```
Every vertex and every one of its neighbors has degree 7, so
``` math
d^*(v)=\frac{1}{7}\sum_{u\in N(v)}7=7.
```
Consequently
``` math
g(G)=5,\qquad \delta^*(G)=7>4=-\partial_{50}(G),
 \qquad \delta^*(G)+\partial_{50}(G)=3.
```
This proves that the explicitly constructed Hoffman–Singleton graph is a strict counterexample to WOW-284.

Equivalently, $`D+\delta^*(G)I=D+7I`$ has eigenvalues $`98`$, $`8`$ with multiplicity 21, and $`3`$ with multiplicity 28. Thus it is positive definite, which is the matrix form of the strict inequality $`\delta^*(G)>-\partial_{50}(G)`$.

# Computational certificate

The proof above is entirely analytic. The accompanying Python code supplies a separate exact check from the coordinate rules. It performs the following steps:

1.  constructs the 175 unordered edges and checks all 50 degrees;

2.  checks the common-neighbor count for every unordered vertex pair;

3.  constructs all 2,500 distance entries by integer breadth-first search;

4.  computes the distance characteristic polynomial symbolically; and

5.  computes an exact rational $`L\Delta L^{\mathsf T}`$ decomposition of $`D+7I`$ and checks that all 50 pivots are positive.

The symbolic steps use SymPy ([<span class="nocase">Meurer et al.</span> 2017](#ref-MeurerEtAl2017)). The expected output is
``` math
(t-91)(t-1)^{21}(t+4)^{28}
```
together with 50 positive rational pivots. Here $`L`$ is unit lower triangular and therefore invertible. If $`M=D+7I=L\Delta L^{\mathsf T}`$, then for every nonzero $`y`$,
``` math
y^{\mathsf T}My=(L^{\mathsf T}y)^{\mathsf T}
 \Delta(L^{\mathsf T}y)>0,
```
so the pivot check proves positive definiteness. Because the distance matrix is built by BFS, the certificate does not use equation <a href="#eq:general-distance" data-reference-type="eqref" data-reference="eq:general-distance">[eq:general-distance]</a> or the spectral derivation above. Numerical agreement is not treated as a proof; all calculations in the certificate are exact.

# Formal verification

The explicit 50-vertex counterexample is fully formalized and verified in Lean 4.31 with Mathlib 4.31 ([Moura and Ullrich 2021](#ref-deMouraUllrich2021); [The mathlib Community 2020](#ref-Mathlib2020)). The development verifies the graph, 7-regularity, the exhaustive common-neighbor certificate, girth five, and the adjacency-square and distance-matrix identities. It supplies exact rational matrices $`S,S^{-1}`$, proves their two-sided inverse identities by denominator-cleared integer certificates, proves $`DS=S\operatorname{diag}(91,(-4)^{(28)},1^{(21)})`$, and checks the multiplicities. Thus the complete explicit proof, including its least distance eigenvalue, is kernel-checked. The scalar $`k\le3`$ threshold is formalized separately. Section <a href="#sec:moore" data-reference-type="ref" data-reference="sec:moore">1</a> remains a conventional proof; the formal verification claim here is deliberately limited to the explicit counterexample and the scalar threshold.

# Scope, provenance, and disclosures

The counterexample has order 50. No minimality claim is made, and no exhaustive search over smaller graphs is part of this note. The general distance-spectral input for minimal cages and all three classical degree cases are credited to Howlader and Panigrahi; the repository’s source ledger separately records the explicit WOW-284 connection and the limits of the targeted priority search.

OpenAI ChatGPT-5.6 Sol Pro assisted with adversarial proof checking and finding the exact graph construction. No AI system is an author. Samuil Petkov is the sole named author and assumes full responsibility for the mathematics, citations, attribution, and conclusions.

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

<div id="ref-Hafner2003" class="csl-entry">

Hafner, Paul R. 2003. “The Hoffman–Singleton Graph and Its Automorphisms.” *Journal of Algebraic Combinatorics* 18 (1): 7–12. <https://doi.org/10.1023/A:1025136524481>.

</div>

<div id="ref-HoffmanSingleton1960" class="csl-entry">

Hoffman, Alan J., and Robert R. Singleton. 1960. “On Moore Graphs with Diameters 2 and 3.” *IBM Journal of Research and Development* 4 (5): 497–504. <https://doi.org/10.1147/rd.45.0497>.

</div>

<div id="ref-HowladerPanigrahi2022" class="csl-entry">

Howlader, Aditi, and Pratima Panigrahi. 2022. “On the Distance Spectrum of Minimal Cages and Associated Distance Biregular Graphs.” *Linear Algebra and Its Applications* 636: 115–33. <https://doi.org/10.1016/j.laa.2021.11.014>.

</div>

<div id="ref-MeurerEtAl2017" class="csl-entry">

<span class="nocase">Meurer, Aaron et al.</span> 2017. “SymPy: Symbolic Computing in Python.” *PeerJ Computer Science* 3: e103. <https://doi.org/10.7717/peerj-cs.103>.

</div>

<div id="ref-deMouraUllrich2021" class="csl-entry">

Moura, Leonardo de, and Sebastian Ullrich. 2021. “The Lean 4 Theorem Prover and Programming Language.” *Automated Deduction—CADE 28*, Lecture notes in computer science, vol. 12699: 625–35. <https://doi.org/10.1007/978-3-030-79876-5_37>.

</div>

<div id="ref-SmithMontemanni2026" class="csl-entry">

Smith, Derek H., and Roberto Montemanni. 2026. “The Moore Graph of Diameter 2 and Degree 57 via Cyclic Derangements.” *Axioms* 15 (5): 332. <https://doi.org/10.3390/axioms15050332>.

</div>

<div id="ref-Mathlib2020" class="csl-entry">

The mathlib Community. 2020. “The Lean Mathematical Library.” *Proceedings of the 9th ACM SIGPLAN International Conference on Certified Programs and Proofs*, 367–81. <https://doi.org/10.1145/3372885.3373824>.

</div>

</div>
