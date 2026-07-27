# Proof Audit 02: the all-degree two-sided LP ceiling

**Audited result:** `TWO_SIDED_LP_CEILING.md`.  
**Verdict:** `pass`.  
**New mathematical consequence:** the extremal polynomial is unique up to
positive scaling.  
**Wording correction:** the result is a girth-five specialization of the
standard nonbacktracking LP framework, not a claim about every possible linear
or semidefinite programming hierarchy.

## 1. Normalized theorem

Fix an integer \(k\ge4\), and let \(F_i\) be the nonbacktracking polynomials

\[
 F_0=1,
 \qquad
 F_1=x,
 \qquad
 F_2=x^2-k,
 \qquad
 F_i=xF_{i-1}-(k-1)F_{i-2}.
\]

Let

\[
 I_k=[-1-\sqrt{2k-2},-1+\sqrt{2k-2}].
\]

Suppose

\[
 f=\sum_{i=0}^d f_iF_i
\]

is finite and satisfies

\[
 f_0>0,
 \qquad
 f_i\ge0\quad(i\ge5),
 \qquad
 f\le0\quad\text{on }I_k.
\]

Then

\[
 \frac{f(k)}{f_0}
 \ge
 \frac{(k+2)(k^2+3)}6.
\]

Equality holds exactly for positive scalar multiples of

\[
 f_*(x)=
 \frac{(x+2)^2((x+1)^2-(2k-2))}{6(k+2)}.
\]

## 2. Claim boundary

The theorem optimizes one explicit cone:

1. the one-variable nonbacktracking basis \(F_i\);
2. no sign restriction on \(f_1,\dots,f_4\), because their traces vanish under
   girth at least five;
3. nonnegative coefficients from degree five onward;
4. pointwise nonpositivity on the full shifted WOW interval.

It does not optimize:

- multipoint semidefinite programs;
- Terwilliger-algebra or coherent-configuration bounds;
- constraints using local intersection numbers;
- cycle-incidence realizability conditions;
- arbitrary polynomial cones unrelated to the nonbacktracking trace argument.

The phrase “all-degree ceiling” refers to polynomial degree inside this precise
cone.

## 3. Hypothesis ledger

| Hypothesis | Where it is used |
| --- | --- |
| \(k\ge4\) | positivity of the dual weights; support inclusion; uniform tail bound with \(r=k-1\ge3\) |
| finite polynomial | permits termwise trace and dual calculations without convergence issues |
| \(f_0>0\) | makes the objective ratio meaningful and fixes the positive scaling in the equality case |
| \(f_i\ge0\) for \(i\ge5\) | converts dual slack inequalities into weak duality and equality rigidity |
| \(f\le0\) on \(I_k\) | gives \(\int f\,d\mu\le0\) and forces zeros at the positive dual support in equality |
| graph girth at least five | gives \(\operatorname{tr}F_i(A)=0\) for \(1\le i\le4\) and nonnegativity thereafter |
| nonprincipal spectrum in \(I_k\) | gives the spectral side of the graph LP bound |
| open interval for strict graph conclusion | excludes the two endpoint zeros of \(f_*\) |

## 4. Dependency graph

The proof imports only:

1. the recurrence and evaluation
   \[
   F_i(k)=k(k-1)^{i-1};
   \]
2. the closed-nonbacktracking-walk interpretation of
   \(\operatorname{tr}F_i(A)\);
3. the elementary Chebyshev bound
   \[
   |U_j(z)|\le j+1\quad(|z|\le1);
   \]
4. finite-dimensional weak duality, written out directly rather than invoked
   as a black box.

No graph classification, numerical eigenvalue ordering, or canonical search is
used.

## 5. Critical step A: the graph LP inequality

For a \(k\)-regular girth-five graph,

\[
 \operatorname{tr}f(A)
 =nf_0+\sum_{i=5}^d f_i\operatorname{tr}F_i(A)
 \ge nf_0.
\]

If the nonprincipal spectrum is contained in \(I_k\), then

\[
 \operatorname{tr}f(A)
 =f(k)+\sum_{\theta\ne k}f(\theta)
 \le f(k).
\]

Therefore

\[
 n\le\frac{f(k)}{f_0}.
\]

**Adversarial check.** The coefficients \(f_1,\dots,f_4\) need not be
nonnegative. Their trace contributions are exactly zero. This is why the
admissible cone is slightly larger than the most naive coefficientwise-positive
cone.

## 6. Critical step B: primal feasibility

The candidate optimizer satisfies

\[
\begin{aligned}
 6(k+2)f_*
 ={}&6(k+2)F_0+2(2k+7)F_1\\
 &+(k+13)F_2+6F_3+F_4.
\end{aligned}
\]

Thus its \(F_0\)-coefficient is one after normalization, and all coefficients
from degree five onward are zero.

On \(I_k\),

\[
 (x+1)^2-(2k-2)\le0,
\]

so \(f_*\le0\). Also

\[
 f_*(k)=\frac{(k+2)(k^2+3)}6.
\]

## 7. Critical step C: positivity of the dual measure

The three support points are

\[
 \xi_-=-1-\sqrt{2k-2},
 \qquad
 -2,
 \qquad
 \xi_+=-1+\sqrt{2k-2}.
\]

The middle and upper weights are manifestly positive. For the lower weight,
write

\[
 A=2k^2-6,
 \qquad
 B=3(k-1)\sqrt{2k-2}.
\]

Both \(A\) and \(B\) are positive, and

\[
 A^2-B^2
 =2(k-3)(2k-3)(k^2+3)>0.
\]

Hence \(A>B\), proving positivity of the lower weight.

**Adversarial check.** Squaring is legitimate because positivity of both sides
is established before the comparison.

## 8. Critical step D: exact finite moments and slacks

The dual measure has mass \(B_k-1\) and satisfies

\[
 \mu(F_i)=-F_i(k)
 \qquad(1\le i\le4).
\]

For \(5\le i\le9\), each slack

\[
 a_i=\mu(F_i)+F_i(k)
\]

factors into positive elementary terms for \(k\ge4\). The three nontrivial
residual factors become coefficientwise-positive polynomials after setting
\(k=m+4\).

The audit recomputes these identities independently rather than importing the
original verifier.

## 9. Critical step E: support inclusion and Chebyshev tail

Put \(r=k-1\ge3\). The support must lie in

\[
 [-2\sqrt r,2\sqrt r]
\]

before applying the Chebyshev representation. The only nontrivial check is

\[
 1+\sqrt{2r}\le2\sqrt r.
\]

After rearrangement and squaring, the margin is

\[
 (2r-1)^2-8r.
\]

At \(r=m+3\), this is

\[
 4m^2+12m+1>0.
\]

The recurrence gives

\[
 F_i(2\sqrt r\,z)
 =r^{i/2}U_i(z)-r^{(i-2)/2}U_{i-2}(z).
\]

The resulting ratio satisfies

\[
 \frac{|\mu(F_i)|}{F_i(k)}
 \le
 \frac{2i+1}{3}3^{3-i/2}.
\]

At \(i=10\), this is \(7/9\), and the ratio decreases because

\[
 3(2i+1)^2-(2i+3)^2=8i^2-6>0.
\]

Therefore every slack is **strictly** positive for \(i\ge10\), not merely
nonnegative.

## 10. Critical step F: weak duality

Since \(f\le0\) on the support,

\[
 \int f\,d\mu\le0.
\]

The exact low moments and nonnegative high-degree coefficients give

\[
 \int f\,d\mu
 \ge
 B_kf_0-f(k).
\]

Thus

\[
 f(k)\ge B_kf_0.
\]

The signs were checked term by term. In particular, no sign condition is used
on \(f_1,\dots,f_4\); their exact dual moments handle them.

## 11. New result: uniqueness of the optimizer

Suppose equality holds. Every high-degree dual slack is strictly positive and
all \(f_i\), \(i\ge5\), are nonnegative. Equality in weak duality therefore
forces

\[
 f_i=0\qquad(i\ge5).
\]

Hence \(\deg f\le4\).

Equality also gives \(\int f\,d\mu=0\). Since every dual weight is positive and
\(f\le0\),

\[
 f(\xi_-)=f(-2)=f(\xi_+)=0.
\]

The point \(-2\) is interior to \(I_k\), so its multiplicity is even. The
quartic degree limit forces

\[
 f(x)=c(x-\xi_-)(x+2)^2(x-\xi_+).
\]

The sign condition and \(f_0>0\) imply \(c>0\). Thus the optimizer is unique
up to positive scaling.

The independent Python audit also treats a generic quartic, imposes the four
linear conditions corresponding to the two endpoint zeros and the double
interior zero, and verifies that the coefficient nullspace is one-dimensional.

## 12. Strict graph equality case

If a graph has nonprincipal spectrum in the open interval and order \(B_k\),
then equality forces use of \(f_*\). Every nonprincipal eigenvalue must be a
zero of \(f_*\). Strictness excludes the endpoints, leaving only \(-2\).

The adjacency trace would then be

\[
 0=k-2(n-1),
\]

which is incompatible with \(n\ge k+1\). Therefore

\[
 n<B_k.
\]

## 13. Independent Python verification

The audit adds

```text
scripts/verify_proof_audit_02_two_sided_lp.py
```

It does not import `verify_two_sided_lp_ceiling.py`. It independently checks:

- the recurrence through degree 30;
- the exact primal expansion;
- positivity of all three dual weights;
- moments through degree nine;
- strict finite slacks;
- support inclusion;
- the uniform Chebyshev tail;
- the one-dimensional optimizer nullspace;
- an exact grid for \(4\le k\le12\) and \(5\le i\le30\).

No floating-point arithmetic is used.

## 14. Audit conclusion

The original theorem is mathematically sound. The audit records one wording
clarification and proves one additional theorem:

\[
 \boxed{\text{the extremal polynomial is unique up to positive scaling}.}
\]

The result should be presented as an exact limitation of the specified
one-variable girth-five nonbacktracking LP cone. It should not be described as
a limitation of all semidefinite or multipoint methods.
