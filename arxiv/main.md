# Exact Counterexamples and Spectral Mechanisms for WOW-284

**Samuil Petkov**<br>
Department of Physics, École normale supérieure, Université PSL, Paris, France<br>
<samuil.petkov@phys.ens.psl.eu><br>
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

Aouchiche and Hansen record the following Graffiti conjecture in their survey of distance spectra ([Aouchiche and Hansen 2014](#ref-AouchicheHansen2014), Conjecture 7.16, p. 370); they attribute it to Fajtlowicz’s 1998 *Written on the Wall* report ([Fajtlowicz 1998](#ref-Fajtlowicz1998)).

<div id="conj:wow284" class="conjecture">

**Conjecture 1** (WOW-284). *If $`G`$ is connected, has $`n\ge3`$ vertices, and has girth $`g(G)\ge5`$, then
``` math
\delta^*(G)\le -\partial_n(G).
```*

</div>

For such a graph, write
``` math
\Phi(G):=\delta^*(G)+\partial_{|V(G)|}(G).
```
Thus $`G`$ is a strict counterexample precisely when $`\Phi(G)>0`$.

In that 2014 survey, the authors reported that the conjecture remained open and noted equality for the Petersen graph ([Aouchiche and Hansen 2014](#ref-AouchicheHansen2014), Conjecture 7.16, p. 370). This equality is the degree-3 boundary case of a general Moore-graph calculation. The degree-7 Moore graph constructed by Hoffman and Singleton ([Hoffman and Singleton 1960](#ref-HoffmanSingleton1960)) lies beyond that boundary and gives a strict violation.

There is important prior spectral work. Howlader and Panigrahi determine a distance polynomial for minimal $`(k,5)`$-cages and explicitly list the distance spectra of the Petersen, Hoffman–Singleton, and hypothetical degree-57 Moore graphs ([Howlader and Panigrahi 2022](#ref-HowladerPanigrahi2022), Theorems 2.3 and 2.5(1)); the existence of the last graph remains open ([Smith and Montemanni 2026](#ref-SmithMontemanni2026)). Their $`k=7`$ calculation, together with regularity and the girth condition, already supplies every ingredient needed to disprove Conjecture <a href="#conj:wow284" data-reference-type="ref" data-reference="conj:wow284">1</a>. The present note records the sharp degree criterion, makes the WOW-284 connection explicit, and supplies a self-contained coordinate certificate. It also extracts the 40-vertex $`(6,5)`$-cage from the same coordinates and gives its distance spectrum directly. No claim is made that the distance spectra are new, that this observation has priority over every unpublished observation, or that the 38-vertex example has minimum possible order among all counterexamples.

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

# The 50-vertex coordinate counterexample

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

# A 40-vertex induced counterexample

The same coordinates contain a smaller regular counterexample. Delete
``` math
\mathcal P=\{P_{0,j},Q_{0,j}:j\in\mathbb F_5\}
```
and let $`R=G-\mathcal P`$ be the induced graph on the remaining 40 vertices. The deleted graph consists of the $`P_{0,\bullet}`$ pentagon, the $`Q_{0,\bullet}`$ pentagram, and the matching $`P_{0,j}Q_{0,j}`$; hence it is a Petersen graph. This construction is the classical 40-vertex $`(6,5)`$-cage of O’Keefe and Wong ([O’Keefe and Wong 1979](#ref-OKeefeWong1979)). Its uniqueness was proved by Wong ([Wong 1979](#ref-Wong1979)), and its realization as a Petersen deletion from the Hoffman–Singleton graph is recorded explicitly by Klin, Muzychuk, and Ziv-Av ([Klin et al. 2009, sec. 3.6](#ref-KlinMuzychukZivAv2009)).

<div id="thm:forty" class="theorem">

**Theorem 5**. *The graph $`R`$ is connected and 6-regular, has girth five and diameter three, and has distance spectrum
``` math
\operatorname{Spec}(D(R))=\{75^{(1)},3^{(5)},0^{(16)},(-5)^{(18)}\}.
```
Consequently
``` math
\delta^*(R)=6>5=-\partial_{40}(R),
 \qquad \delta^*(R)+\partial_{40}(R)=1,
```
so $`R`$ is a strict counterexample to WOW-284.*

</div>

<div class="proof">

*Proof.* Every retained vertex has exactly one neighbor in $`\mathcal P`$: $`P_{i,j}`$, with $`i\ne0`$, is adjacent there only to $`Q_{0,j}`$, while $`Q_{k,\ell}`$, with $`k\ne0`$, is adjacent there only to $`P_{0,\ell}`$. Thus $`R`$ is 6-regular. It inherits the absence of triangles and 4-cycles from $`G`$, and each retained $`P`$-layer is a 5-cycle, so $`g(R)=5`$.

Fix $`v\in V(R)`$. Girth five makes the distance-zero, distance-one, and distance-two layers from $`v`$ have respectively $`1`$, $`6`$, and $`6\cdot5=30`$ vertices. Three vertices remain. Each has no neighbor in $`L_0(v)\cup L_1(v)`$ and has at most two neighbors among the three remaining vertices; 6-regularity therefore gives it a neighbor in the distance-two layer. Hence all three lie at distance three from $`v`$. This proves connectedness and diameter three.

It remains to compute the spectrum. Order the vertices of $`G`$ with those of $`R`$ first, and write its adjacency matrix in blocks as
``` math
A_G=\begin{pmatrix}B&C\\ C^{\mathsf T}&P\end{pmatrix},
```
where $`B=A(R)`$, $`P=A(G[\mathcal P])`$, and $`C`$ is $`40\times10`$. Every row of $`C`$ has sum one and every column has sum four. Moreover, distinct vertices of $`\mathcal P`$ have no common retained neighbor: adjacent pairs have no common neighbor in $`G`$, while the unique common neighbor of a nonadjacent pair already lies in the induced Petersen graph. Therefore
``` math
\begin{equation}
\label{eq:c-block}
 C\mathbf1_{10}=\mathbf1_{40},\qquad C^{\mathsf T}C=4I_{10}.
\end{equation}
```
In particular, $`C`$ has rank ten.

Equation <a href="#eq:general-a-square" data-reference-type="eqref" data-reference="eq:general-a-square">[eq:general-a-square]</a> with $`k=7`$ gives $`A_G^2=6I-A_G+J`$. Its top-right block is
``` math
BC+CP=-C+J_{40,10}.
```
Here $`J_{a,b}`$ denotes the $`a\times b`$ all-ones matrix. Since $`J_{40,10}=CJ_{10}`$ by <a href="#eq:c-block" data-reference-type="eqref" data-reference="eq:c-block">[eq:c-block]</a>,
``` math
\begin{equation}
\label{eq:bc-intertwining}
 BC=C(J_{10}-I_{10}-P).
\end{equation}
```
The Petersen adjacency spectrum, obtained from the $`k=3`$ case of Section <a href="#sec:moore" data-reference-type="ref" data-reference="sec:moore">1</a>, is $`\{3^{(1)},1^{(5)},(-2)^{(4)}\}`$. Because $`C`$ is injective, equation <a href="#eq:bc-intertwining" data-reference-type="eqref" data-reference="eq:bc-intertwining">[eq:bc-intertwining]</a> gives
``` math
\operatorname{Spec}\bigl(B|_{\operatorname{col}C}\bigr)
 =\{6^{(1)},(-2)^{(5)},1^{(4)}\}.
```

The top-left block of the same identity is
``` math
B^2+CC^{\mathsf T}=6I_{40}-B+J_{40}.
```
Since $`B`$ is symmetric, $`\ker C^{\mathsf T}=(\operatorname{col}C)^\perp`$ is $`B`$-invariant. If $`x\in\ker C^{\mathsf T}`$, then $`\mathbf1_{40}^{\mathsf T}x=(C\mathbf1_{10})^{\mathsf T}x=0`$, so $`(B^2+B-6I)x=0`$. Thus the remaining 30 adjacency eigenvalues are $`2`$ or $`-3`$. If their multiplicities are $`a,b`$, then $`a+b=30`$; the displayed ten-dimensional spectrum has trace zero, and $`\operatorname{tr}B=0`$, so $`2a-3b=0`$. Hence $`a=18`$, $`b=12`$, and
``` math
\begin{equation}
\label{eq:forty-adjacency-spectrum}
 \operatorname{Spec}(B)=\{6^{(1)},2^{(18)},1^{(4)},(-2)^{(5)},(-3)^{(12)}\}.
\end{equation}
```

Let $`A_i`$ be the distance-$`i`$ matrix of $`R`$. Girth five and 6-regularity give $`A_2=B^2-6I`$, while diameter three gives $`J=I+B+A_2+A_3`$. Consequently
``` math
\begin{equation}
\label{eq:forty-distance-identity}
 D(R)=B+2A_2+3A_3=3J+3I-2B-B^2.
\end{equation}
```
On $`\mathbf1_{40}`$, the eigenvalue is $`3\cdot40+3-2\cdot6-6^2=75`$. A nonprincipal adjacency eigenvalue $`\theta`$ maps to
``` math
3-2\theta-\theta^2=4-(\theta+1)^2.
```
Applying this to <a href="#eq:forty-adjacency-spectrum" data-reference-type="eqref" data-reference="eq:forty-adjacency-spectrum">[eq:forty-adjacency-spectrum]</a> gives the claimed distance spectrum. Finally, regularity gives $`\delta^*(R)=6`$, completing the proof. ◻

</div>

# Smaller induced counterexamples

The 40-vertex graph contains strict counterexamples of orders 39 and 38. All claims in this section are reproduced exactly by the accompanying programs; floating-point eigenvalues are not used.

## Deleting the endpoints of an edge

Delete the adjacent vertices
``` math
a=P_{1,0},\qquad b=P_{1,1}
```
from $`R`$, and call the resulting graph $`H`$. A canonical graph6 string, complete adjacency lists, and an edge list are provided in `data/graphs/`.

<div id="thm:thirty-eight" class="theorem">

**Theorem 6**. *The graph $`H`$ is connected, has 38 vertices, 109 edges, girth five, diameter three, and degree multiset $`6^{(28)},5^{(10)}`$. Moreover,
``` math
\delta^*(H)=\frac{17}{3},
 \qquad
 \partial_{38}(H)=-3-\sqrt7.
```
Consequently
``` math
\delta^*(H)+\partial_{38}(H)=\frac83-\sqrt7>0,
```
so $`H`$ is a strict counterexample to WOW-284.*

</div>

<div class="proof">

*Proof.* Induced deletion preserves simplicity and cannot create a triangle or a 4-cycle. A distinct $`P`$-layer remains a 5-cycle. Exact breadth-first search from every vertex gives connectedness and diameter three.

Put
``` math
X=N_R(a)\setminus\{b\},\qquad
 Y=N_R(b)\setminus\{a\}.
```
The girth condition implies that $`X`$ and $`Y`$ are disjoint and that no vertex of $`X\cup Y`$ has a remaining neighbor in $`X\cup Y`$. These ten vertices therefore have degree five and all their remaining neighbors have degree six; every other vertex has degree six. A degree-six vertex has at most one neighbor in $`X`$ and at most one in $`Y`$, since two in either set would create a 4-cycle. If it has $`t\in\{0,1,2\}`$ neighbors in $`X\cup Y`$, then
``` math
d^*(v)=\frac{5t+6(6-t)}6=6-\frac{t}{6}.
```
There are $`10\cdot5=50`$ incidences from $`X\cup Y`$ to the 28 degree-six vertices, so some degree-six vertex has $`t=2`$. Hence $`\delta^*(H)=17/3`$.

The exact distance characteristic polynomial is displayed in Appendix <a href="#app:polynomials" data-reference-type="ref" data-reference="app:polynomials">13</a>. It contains $`(x^2+6x+2)^2`$, whose roots are $`-3\pm\sqrt7`$. An exact Sturm count shows that the full polynomial has exactly one distinct root below $`-28/5`$. Since
``` math
-3-\sqrt7<-\frac{28}{5},
```
this is the least distance eigenvalue. Independently, an exact rational $`LDL^{\mathsf T}`$ decomposition of $`3D(H)+17I`$ has 38 positive pivots. Finally $`8/3>\sqrt7`$, because $`64>63`$, proving strictness. ◻

</div>

## Orders 39 and 42

For any $`v\in V(R)`$, deleting $`v`$ leaves six vertices of degree five and 33 of degree six. A degree-six vertex meets at most one degree-five vertex, by the absence of 4-cycles, and at least one such incidence exists. Thus
``` math
\delta^*=\frac{5+5\cdot6}{6}=\frac{35}{6}.
```
Exact rational factorization gives $`6D+35I\succ0`$, so every distance eigenvalue is strictly greater than $`-35/6`$. This gives a 39-vertex strict counterexample. The exhaustive verification below checks connectivity for each of the 40 choices of $`v`$; as induced subgraphs, they retain girth at least five.

For another regular example, fix a vertex in the Hoffman–Singleton graph and retain its 42 vertices at distance two. The induced graph is 6-regular and has
``` math
\operatorname{Spec}(A)=\{6^{(1)},2^{(21)},(-1)^{(6)},(-3)^{(14)}\},
```
``` math
\operatorname{Spec}(D)=\{81^{(1)},4^{(6)},0^{(14)},(-5)^{(21)}\}.
```
Hence $`\delta^*=6>5=-\partial_{42}`$. The parameterized construction behind this classical second subconstituent is proved in Section <a href="#sec:subconstituent" data-reference-type="ref" data-reference="sec:subconstituent">8</a>; its adjacency spectrum is also tabulated by van Dam and Haemers ([Dam and Haemers 2003](#ref-vanDamHaemers2003), Table 3).

## Exact labelled descendant families

<div id="prop:descendants" class="proposition">

**Proposition 7**. *For every vertex $`v`$ of $`R`$, the graph $`R-v`$ is connected, has girth at least five, has $`\delta^*=35/6`$ and the same exact distance characteristic polynomial $`P_{39}`$ displayed in Appendix <a href="#app:polynomials" data-reference-type="ref" data-reference="app:polynomials">13</a>. Every one of these 40 labelled graphs is a strict counterexample.*

*For every edge $`uv`$ of $`R`$, the graph $`R-\{u,v\}`$ is connected, has girth at least five, has $`\delta^*=17/3`$, the same exact distance characteristic polynomial $`P_{38}`$, and least distance eigenvalue $`-3-\sqrt7`$. Every one of these 120 labelled graphs is a strict counterexample.*

</div>

<div class="proof">

*Proof.* The script `scripts/verify_descendant_families.py` enumerates all 40 vertices and all 120 edges. For every induced graph, breadth-first search from every vertex checks connectivity and reconstructs the integer distance matrix. Induced deletion cannot create a cycle of length below five. The script then computes every dual degree as a rational number and the characteristic polynomial $`\det(xI-D)`$ over $`\mathbb Z`$. Exact equality with $`P_{39}`$ or $`P_{38}`$, followed by an exact Sturm count for each common polynomial, proves the assertions. No graph-isomorphism or transitivity assumption is used. ◻

</div>

<div class="remark">

*Remark 8*. A numerical screen of all $`\binom{40}{3}=9880`$ three-vertex deletions found no graph with $`\Phi>0`$; its best value was approximately $`-0.306979936667`$. This is exploratory evidence only, not an exact elimination of order 37 and not a minimality proof.

</div>

# A diameter-three spectral criterion

<div id="thm:diam3" class="theorem">

**Theorem 9**. *Let $`G`$ be a connected $`k`$-regular graph on $`n`$ vertices, of girth at least five and diameter three. Then
``` math
\begin{equation}
\label{eq:diam3-polynomial}
 D=3J+(k-3)I-2A-A^2.
\end{equation}
```
The principal distance eigenvalue is $`3n-k^2-k-3`$, and every nonprincipal adjacency eigenvalue $`\theta`$ gives the distance eigenvalue
``` math
\mu(\theta)=k-2-(\theta+1)^2.
```
Consequently $`G`$ is a strict counterexample to WOW-284 precisely when
``` math
\max_{\theta\ne k}|\theta+1|<\sqrt{2k-2}.
```*

</div>

<div class="proof">

*Proof.* The absence of triangles and 4-cycles means that two vertices at distance two have exactly one common neighbor. Hence the distance-two matrix is $`A_2=A^2-kI`$. Since the diameter is three, $`A_3=J-I-A-A_2`$. Substitution into $`D=A+2A_2+3A_3`$ proves <a href="#eq:diam3-polynomial" data-reference-type="eqref" data-reference="eq:diam3-polynomial">[eq:diam3-polynomial]</a>. The asserted eigenvalues follow by applying the identity to $`\mathbf 1`$ and to $`\mathbf 1^\perp`$. The matrix $`D`$ is nonnegative and irreducible (indeed, every off-diagonal entry is positive), and its row sums are constant by the displayed identity. Perron–Frobenius therefore makes the principal eigenvalue its largest eigenvalue, so the least distance eigenvalue occurs among the nonprincipal images. Finally regularity gives $`\delta^*=k`$, so strict failure is equivalent to $`k>\max_{\theta\ne k}((\theta+1)^2-k+2)`$, which is the displayed criterion. ◻

</div>

<div class="corollary">

**Corollary 10** (Bipartite obstruction). *A connected $`k`$-regular bipartite graph of diameter three and girth at least five is not a strict counterexample for $`k\ge3`$.*

</div>

<div class="proof">

*Proof.* The nonprincipal adjacency eigenvalue $`-k`$ maps to
``` math
\mu(-k)=k-2-(k-1)^2.
```
Its negative is at least $`k`$ for $`k\ge3`$, with equality only at $`k=3`$. ◻

</div>

For comparison, exact negative controls follow directly from Theorem <a href="#thm:diam3" data-reference-type="ref" data-reference="thm:diam3">9</a>. The Odd graph $`O_4=KG(7,3)`$ has adjacency spectrum
``` math
\{4^{(1)},2^{(14)},(-1)^{(14)},(-3)^{(6)}\},
```
so $`\delta^*=4`$ and $`\partial_n=-7`$. The Heawood graph has adjacency spectrum
``` math
\{3^{(1)},(\sqrt2)^{(6)},(-\sqrt2)^{(6)},(-3)^{(1)}\},
```
so $`\delta^*=3`$ and $`\partial_n=-2-2\sqrt2`$.

# Moore second subconstituents

<div id="thm:second-sub" class="theorem">

**Theorem 11**. *Let $`M`$ be a degree-$`K`$ Moore graph of diameter two, where $`K\ge3`$, and fix a vertex $`v`$. Let $`X`$ be the graph induced by the vertices at distance two from $`v`$. Then
``` math
|V(X)|=K(K-1),\qquad X\text{ is }(K-1)\text{-regular},
```
$`X`$ has girth at least five and diameter three, and
``` math
\partial_{K(K-1)}(X)=-\frac{5+\sqrt{4K-3}}2.
```
Consequently
``` math
\delta^*(X)+\partial_{K(K-1)}(X)
 =K-1-\frac{5+\sqrt{4K-3}}2,
```
which is positive exactly for integers $`K\ge6`$.*

</div>

<div class="proof">

*Proof.* Relative to $`\{v\}\sqcup N(v)\sqcup V(X)`$, write
``` math
A(M)=
 \begin{pmatrix}
 0&\mathbf 1^{\mathsf T}&0\\
 \mathbf 1&0&C\\
 0&C^{\mathsf T}&B
 \end{pmatrix}.
```
Each vertex of $`X`$ has one neighbor in $`N(v)`$ and $`K-1`$ in $`X`$, so $`B`$ is $`(K-1)`$-regular. Distinct rows of $`C`$ have disjoint support and row sum $`K-1`$, hence $`CC^{\mathsf T}=(K-1)I`$. The middle-right block of the Moore identity gives $`CB=J-C`$. Thus $`B`$ has eigenvalue $`-1`$ on the $`(K-1)`$-dimensional image of $`C^{\mathsf T}`$ orthogonal to $`\mathbf 1`$. On $`\ker C`$, the bottom-right block gives
``` math
B^2+B-(K-1)I=0,
```
whose roots are
``` math
r=\frac{-1+\sqrt{4K-3}}2,
 \qquad
 s=\frac{-1-\sqrt{4K-3}}2.
```
The kernel has dimension $`K(K-2)>0`$. If the multiplicities of $`r,s`$ there are $`m_r,m_s`$, then the trace of $`B`$ gives $`m_rr+m_ss=0`$, because the principal eigenvalue $`K-1`$ cancels the $`(K-1)`$ copies of $`-1`$. Since $`r>0>s`$, both multiplicities are positive.

We record the diameter argument explicitly. Around any $`x\in X`$, girth at least five gives $`1`$, $`K-1`$, and $`(K-1)(K-2)`$ distinct vertices in the first three distance layers of $`X`$. The remaining $`K-2`$ vertices are exactly the other vertices of $`X`$ sharing the unique neighbor of $`x`$ in $`N(v)`$. They have no path of length at most two to $`x`$, since such a path would create a triangle or 4-cycle in $`M`$. Every neighbor of any such remaining vertex $`z`$ is nonadjacent to $`x`$, since an edge to $`x`$ would complete the 4-cycle through their shared neighbor in $`N(v)`$. If $`w\in N_X(z)`$, the unique ambient common neighbor of $`x`$ and $`w`$ cannot lie in $`N(v)`$: it would have to be the unique such neighbor of $`x`$, and would then form a triangle with $`w,z`$. It therefore lies in $`X`$, giving a path of length three from $`x`$ to $`z`$. Hence all remaining vertices are at distance three. This proves connectivity and diameter three.

Apply Theorem <a href="#thm:diam3" data-reference-type="ref" data-reference="thm:diam3">9</a> with $`k=K-1`$. The eigenvalue $`-1`$ maps to $`K-3`$, while $`r`$ and $`s`$ map respectively to
``` math
-\frac{5+\sqrt{4K-3}}2
 \quad\text{and}\quad
 -\frac{5-\sqrt{4K-3}}2.
```
Thus the first of these is the least distance eigenvalue. The final integer inequality is strict exactly for $`K\ge6`$. ◻

</div>

For $`K=7`$, this gives the explicit 42-vertex graph above. A degree-57 Moore graph, if it exists, would give a 56-regular example on 3192 vertices. Its existence remains open ([Smith and Montemanni 2026](#ref-SmithMontemanni2026)); the theorem is therefore a parameterized construction, not an unconditional infinite family.

# An equitable-deletion framework

<div id="prop:equitable-delete" class="proposition">

**Proposition 12**. *Let $`M`$ be a degree-$`K`$ Moore graph of diameter two. Partition its vertices as $`V(M)=R\sqcup S`$, write
``` math
A(M)=\begin{pmatrix}B&C\\C^{\mathsf T}&P\end{pmatrix},
```
and suppose $`M[S]`$ is $`r`$-regular while every vertex of $`R`$ has exactly $`t>0`$ neighbors in $`S`$. Then $`M[R]`$ is $`(K-t)`$-regular. If $`Py=\eta y`$ and $`y\perp\mathbf 1`$, then
``` math
BCy=-(1+\eta)Cy,
 \qquad
 \lVert Cy\rVert^2=(K-1-\eta-\eta^2)\lVert y\rVert^2.
```
Moreover, on $`\ker C^{\mathsf T}`$,
``` math
B^2+B-(K-1)I=0.
```
Whenever $`M[R]`$ has diameter three, these adjacency data feed directly into Theorem <a href="#thm:diam3" data-reference-type="ref" data-reference="thm:diam3">9</a>.*

</div>

<div class="proof">

*Proof.* The upper-right and lower-right blocks of the Moore identity are
``` math
BC+CP=-C+J,
 \qquad
 C^{\mathsf T}C+P^2=(K-1)I-P+J.
```
Apply them to an eigenvector orthogonal to $`\mathbf 1`$. Finally $`C\mathbf 1=t\mathbf 1`$, with $`t>0`$, implies $`\ker C^{\mathsf T}\subseteq\mathbf 1^\perp`$; the upper-left block gives the last equation. ◻

</div>

For the 40-vertex graph, $`K=7`$, $`S`$ is the induced Petersen graph, $`r=3`$, and $`t=1`$. If, more generally, $`S\subsetneq V(M)`$ is itself a degree-$`r`$ Moore graph and every outside vertex has exactly one neighbor in $`S`$, cross-edge counting gives
``` math
(r^2+1)(K-r)=K^2-r^2.
```
Because the outside set is nonempty, $`K>r`$, so cancellation yields $`K=r^2-r+1`$. The coordinate deletions displayed above realize the steps $`C_5\subset`$ Petersen $`\subset`$ Hoffman–Singleton, corresponding to $`(r,K)=(2,3)`$ and $`(3,7)`$, but do not yield an infinite chain.

# Further exact and exploratory checks

For $`i\in\mathbb F_5`$, put $`\mathcal L_i=\{P_{i,j},Q_{i,j}:j\in\mathbb F_5\}`$, and let $`R_m`$ be the graph obtained from $`G`$ by deleting $`\mathcal L_0,\ldots,\mathcal L_{m-1}`$ (with $`R_0=G`$). These balanced coordinate-layer deletions give the following exact representatives:
``` math
\begin{array}{c@{\qquad}c@{\qquad}c@{\qquad}c@{\qquad}c}
\toprule
m&|V|&\text{degree}&\partial_n&\delta^*+\partial_n\\
\midrule
0&50&7&-4&3\\
1&40&6&-5&1\\
2&30&5&-6&-1\\
3&20&4&-7&-3\\
4&10&3&-3&0\\
\bottomrule
\end{array}
```
Thus this natural chain stops producing strict counterexamples after the 40-vertex member. The preceding analytic theorems cover the Moore and regular diameter-three mechanisms, Moore second subconstituents, and the equitable deletion framework. The exact computations check the listed finite examples, all singleton and edge-endpoint deletions of $`R`$, the balanced layer chain, $`O_4`$, and the Heawood graph.

No unconditional infinite family is established. Fixed-degree, diameter-three graphs have bounded order by the Moore bound, so an infinite family within this framework would require unbounded degree. Covers, subdivisions, coronas, and general vertex replacements are not asserted to preserve the strict inequality; the present arguments establish no such preservation theorem.

# Computational certificate

The accompanying Python programs supply several exact checks with deliberately separated dependencies. The original 50-vertex certificate:

1.  constructs the 175 unordered edges and checks all 50 degrees;

2.  checks the common-neighbor count for every unordered vertex pair;

3.  constructs all 2,500 distance entries by integer breadth-first search;

4.  computes the distance characteristic polynomial symbolically; and

5.  computes an exact rational $`L\Delta L^{\mathsf T}`$ decomposition of $`D+7I`$ and checks that all 50 pivots are positive.

Its expected characteristic polynomial is
``` math
(t-91)(t-1)^{21}(t+4)^{28}
```
and all 50 rational pivots are positive. Since $`L`$ is unit lower triangular, for every nonzero $`y`$,
``` math
y^{\mathsf T}My=(L^{\mathsf T}y)^{\mathsf T}
 \Delta(L^{\mathsf T}y)>0,
```
so this proves positive definiteness of $`M=D+7I`$.

A second exact script constructs $`R`$ by the stated deletion and independently checks its 40 degrees, all BFS distances, girth, the block identities <a href="#eq:c-block" data-reference-type="eqref" data-reference="eq:c-block">[eq:c-block]</a>–<a href="#eq:bc-intertwining" data-reference-type="eqref" data-reference="eq:bc-intertwining">[eq:bc-intertwining]</a>, and the characteristic polynomials
``` math
\det(tI-B)=(t-6)(t-2)^{18}(t-1)^4(t+2)^5(t+3)^{12},
```
``` math
\det(tI-D(R))=(t-75)(t-3)^5t^{16}(t+5)^{18}.
```

The extended verifier reconstructs the 42-, 40-, 39-, and 38-vertex graphs from the field-coordinate rules and checks all structural, dual-degree, characteristic-polynomial, Sturm, and rational $`LDL^{\mathsf T}`$ assertions used above. A separate 38-vertex audit starts from the stored graph6 representation, reconstructs graph distances by integer breadth-first search through NetworkX ([Hagberg et al. 2008](#ref-HagbergSchultSwart2008)), and uses a handwritten `Fraction`-based decomposition. This is independent of the coordinate representation and of SymPy’s matrix factorization, although it is not an independently sourced graph.

Finally, `scripts/verify_descendant_families.py` exhausts the 40 labelled single-vertex and 120 labelled edge-endpoint deletions. SymPy supplies exact integer characteristic polynomials $`\det(tI-D)`$ and Sturm counts of their square-free parts ([<span class="nocase">Meurer et al.</span> 2017](#ref-MeurerEtAl2017)). The recorded output is `supplement/extended_2026-07-23/logs/descendant_family_output.txt`; the enclosing `SHA256SUMS` authenticates it and every other archived certificate in that supplement. The cross-platform command

    python scripts/verify_extended.py

runs every extended exact certificate and checks regenerated graph files byte-for-byte. No floating-point eigenvalue evidence is used for any theorem. The optional numerical three-vertex screen is isolated in `explore_generalizations.py` and is labelled exploratory wherever reported.

# Formal verification

The explicit 50-vertex counterexample is fully formalized and verified in Lean 4.31 with Mathlib 4.31 ([Moura and Ullrich 2021](#ref-deMouraUllrich2021); [The mathlib Community 2020](#ref-Mathlib2020)). The development verifies the graph, 7-regularity, the exhaustive common-neighbor certificate, girth five, and the adjacency-square and distance-matrix identities. It supplies exact rational matrices $`S,S^{-1}`$, proves their two-sided inverse identities by denominator-cleared integer certificates, proves $`DS=S\operatorname{diag}(91,(-4)^{(28)},1^{(21)})`$, and checks the multiplicities. Thus the complete explicit 50-vertex proof, including its least distance eigenvalue, is kernel-checked. The scalar $`k\le3`$ threshold is formalized separately.

Lean 4.31 also kernel-checks finite spectral certificates for the explicit 38-, 39-, 40-, and 42-vertex constructions. For orders 38, 39, and 42, the public endpoints certify the exact minimum dual-degree data, positive definiteness of a shifted finite matrix, and the resulting strict inequality for every nonzero real eigenpair. For order 40, the endpoint certifies a two-sided invertible exact diagonalization, its diagonal-entry multiplicities, and that $`-5`$ is an attained minimum diagonal entry, together with dual degree six and gap one.

The scope of these non-50 results is deliberately finite and spectral: their public endpoints do not bundle every structural hypothesis, and the semantic finite matrices are not identified with Mathlib’s `SimpleGraph.dist` in a single theorem. They are therefore described here as kernel-checked finite spectral certificates, rather than as a full standard-library formalization of every graph-theoretic phrase in the manuscript. Section <a href="#sec:moore" data-reference-type="ref" data-reference="sec:moore">1</a>, the descendant-family results, and the extended criteria remain conventional proofs supported by exact computation.

# Scope, provenance, and disclosures

The note gives counterexamples of orders 38, 39, 40, 42, and 50. No claim is made that 38 is the minimum possible order among WOW-284 counterexamples, and no exhaustive search over all smaller graphs is part of this note. Calling the 40-vertex graph the $`(6,5)`$-cage refers to its classical minimum-order property among 6-regular girth-five graphs, not to minimum order for the WOW problem. The distance-spectral input for Moore graphs is credited to Howlader and Panigrahi; the classical 40-vertex cage and 42-vertex second subconstituent are separately credited above. The repository source ledger records the explicit WOW-284 connection and the limits of the targeted priority search.

OpenAI ChatGPT-5.6 Sol Pro assisted with adversarial proof checking, proof exploration, and Lean formalization. No AI system is an author. Samuil Petkov is the sole named author and assumes full responsibility for the mathematics, citations, attribution, and conclusions.

The author received no funding for this work and declares no competing interests. The manuscript source, exact verification code, machine-readable certificates, and build instructions are available in the public repository [`github.com/SamPetkov/wow284`](https://github.com/SamPetkov/wow284).

# Exact distance characteristic polynomials

For every labelled single-vertex deletion considered in Proposition <a href="#prop:descendants" data-reference-type="ref" data-reference="prop:descendants">7</a>,
``` math
\begin{align*}
P_{39}(x)={}&x^9(x+5)^{12}(x^2+6x+3)\\
&\cdot(x^3+3x^2-15x-7)^2(x^3+3x^2-15x-3)^2\\
&\cdot(x^4-78x^3+303x^2-70x-450).
\end{align*}
```
For every labelled edge-endpoint deletion considered there,
``` math
\begin{align*}
P_{38}(x)={}&x^4(x-2)(x+5)^8(x^2+6x+2)^2\\
&\cdot(x^3+3x^2-15x-3)\\
&\cdot(x^4+5x^3-7x^2-23x-6)\\
&\cdot(x^5+9x^4+7x^3-77x^2-54x-4)\\
&\cdot(x^9-67x^8-404x^7+1772x^6+7205x^5\\
&\hspace{2.2em}-18489x^4-17018x^3+20288x^2+16824x+1680).
\end{align*}
```

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-AouchicheHansen2014" class="csl-entry">

Aouchiche, Mustapha, and Pierre Hansen. 2014. “Distance Spectra of Graphs: A Survey.” *Linear Algebra and Its Applications* 458: 301–86. <https://doi.org/10.1016/j.laa.2014.06.010>.

</div>

<div id="ref-vanDamHaemers2003" class="csl-entry">

Dam, Edwin R. van, and Willem H. Haemers. 2003. “Which Graphs Are Determined by Their Spectrum?” *Linear Algebra and Its Applications* 373: 241–72. <https://doi.org/10.1016/S0024-3795(03)00483-X>.

</div>

<div id="ref-Fajtlowicz1998" class="csl-entry">

Fajtlowicz, Siemion. 1998. *Written on the Wall: Conjectures Derived on the Basis of the Program Galatea Gabriella Graffiti*. Technical report. University of Houston.

</div>

<div id="ref-Hafner2003" class="csl-entry">

Hafner, Paul R. 2003. “The Hoffman–Singleton Graph and Its Automorphisms.” *Journal of Algebraic Combinatorics* 18 (1): 7–12. <https://doi.org/10.1023/A:1025136524481>.

</div>

<div id="ref-HagbergSchultSwart2008" class="csl-entry">

Hagberg, Aric A., Daniel A. Schult, and Pieter J. Swart. 2008. “Exploring Network Structure, Dynamics, and Function Using NetworkX.” *Proceedings of the 7th Python in Science Conference*, 11–15. <https://doi.org/10.25080/TCWV9851>.

</div>

<div id="ref-HoffmanSingleton1960" class="csl-entry">

Hoffman, Alan J., and Robert R. Singleton. 1960. “On Moore Graphs with Diameters 2 and 3.” *IBM Journal of Research and Development* 4 (5): 497–504. <https://doi.org/10.1147/rd.45.0497>.

</div>

<div id="ref-HowladerPanigrahi2022" class="csl-entry">

Howlader, Aditi, and Pratima Panigrahi. 2022. “On the Distance Spectrum of Minimal Cages and Associated Distance Biregular Graphs.” *Linear Algebra and Its Applications* 636: 115–33. <https://doi.org/10.1016/j.laa.2021.11.014>.

</div>

<div id="ref-KlinMuzychukZivAv2009" class="csl-entry">

Klin, Mikhail, Mikhail Muzychuk, and Matan Ziv-Av. 2009. “Higmanian Rank-5 Association Schemes on 40 Points.” *Michigan Mathematical Journal* 58 (1): 255–84. <https://doi.org/10.1307/mmj/1242071692>.

</div>

<div id="ref-MeurerEtAl2017" class="csl-entry">

<span class="nocase">Meurer, Aaron et al.</span> 2017. “SymPy: Symbolic Computing in Python.” *PeerJ Computer Science* 3: e103. <https://doi.org/10.7717/peerj-cs.103>.

</div>

<div id="ref-deMouraUllrich2021" class="csl-entry">

Moura, Leonardo de, and Sebastian Ullrich. 2021. “The Lean 4 Theorem Prover and Programming Language.” *Automated Deduction—CADE 28*, Lecture notes in computer science, vol. 12699: 625–35. <https://doi.org/10.1007/978-3-030-79876-5_37>.

</div>

<div id="ref-OKeefeWong1979" class="csl-entry">

O’Keefe, M., and Pak-Ken Wong. 1979. “A Smallest Graph of Girth 5 and Valency 6.” *Journal of Combinatorial Theory, Series B* 26 (2): 145–49. <https://doi.org/10.1016/0095-8956(79)90052-2>.

</div>

<div id="ref-SmithMontemanni2026" class="csl-entry">

Smith, Derek H., and Roberto Montemanni. 2026. “The Moore Graph of Diameter 2 and Degree 57 via Cyclic Derangements.” *Axioms* 15 (5): 332. <https://doi.org/10.3390/axioms15050332>.

</div>

<div id="ref-Mathlib2020" class="csl-entry">

The mathlib Community. 2020. “The Lean Mathematical Library.” *Proceedings of the 9th ACM SIGPLAN International Conference on Certified Programs and Proofs*, 367–81. <https://doi.org/10.1145/3372885.3373824>.

</div>

<div id="ref-Wong1979" class="csl-entry">

Wong, Pak-Ken. 1979. “On the Uniqueness of the Smallest Graph of Girth 5 and Valency 6.” *Journal of Graph Theory* 3 (4): 407–9. <https://doi.org/10.1002/jgt.3190030413>.

</div>

</div>
