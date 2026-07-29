# Proof Audit 14C: exclusion of the two order-50 quotient lifts

**Audited result:** `ORDER50_LIFT_EXCLUSION.md`  
**Audit mode:** two independently implemented exact finite classifications.  
**Verdict:** `pass` locally; repository promotion requires the same files and
current-head CI to pass at one commit.

## 1. Normalized theorem

Let \(G\) be connected, 6-regular, of order 50, girth at least five and
diameter three, and assume every nonprincipal adjacency eigenvalue lies in

\[
 (-1-\sqrt{10},-1+\sqrt{10}).
\]

Then no such graph exists. Consequently every connected 6-regular strict
WOW-284 counterexample has

\[
 \boxed{|V(G)|\le49.}
\]

The audit starts from the independently audited signed-component quotient
classification. It does not re-use the obsolete factorization-based order-50
argument.

## 2. Hypothesis ledger

| Hypothesis | Use |
|---|---|
| 6-regular, order 50 | fixed quotient degrees and signed-complement normalization |
| girth at least five | incidence blocks have no repeated pairs; all binary products used below are zero-one |
| diameter three and strict WOW window | construction and positivity of the signed complement |
| connected signed components | support-connectedness conditions on every \(S_i\) |
| canonical quotient classification | leaves exactly Types A and B |

No floating-point eigenvalue ordering is used.

## 3. Type-A replay

Both implementations regenerate the six simple cubic graph classes on eight
vertices. They independently enumerate signed \(S_2\)-orbits commuting with the
cubic adjacency matrix. The exact orbit vector is

\[
 \boxed{(18,15,2,0,31,7).}
\]

After imposing \(CS_3=S_2C\), exact signed entries, connected support and
positive semidefiniteness, the canonical signed-pair orbit vector is

\[
 \boxed{(1,0,0,0,0,0).}
\]

The unique orbit lies over \(K_4\sqcup K_4\). Its final \(6\times12\) binary
intertwiner problem has affine dimension six and no binary solution. Therefore
Type A has no lift.

## 4. Type-B replay

The primary implementation enumerates 1,152 labelled matching-symmetric signed
ten-vertex matrices and two matching-centralizer orbits. The independent C++
implementation obtains the same census. In both orbits the underlying signed
component is the positive \(C_{10}\).

Both implementations obtain exactly 140 binary matrices commuting with the two
cycle adjacencies and six independent-dihedral orbits. Their support-component
counts are

\[
 \boxed{1,1,2,2,5,5.}
\]

For the six orbits, the affine dimensions and exact entry-admissible he primary implimensus. Iny

Te-0})X_1,
 \qquad
 \qq

F
 \qquad
 \qq

F
 \qq-0}exac such grapmentation enumerates 1,17{,}se unique cked by ycle  positive semidPSDt-com
+
implementatioable: Pconfirmn mae cked by te a a\(CS_s aincidss determassignme
r for rejection;irth at laindedence b;act positiveun<survivo&1&2&1ve \(C_nact rationary ma. f \(X_r \(K_## 4gned-pair ors}&1&1&1&1&1&1,nt-head rary s. I10}\).

Both imple
\]

Its suped eeliminates s
chonditions on complement

\[20perfequence

Brification makestntations reproduce theent replay is

```text
pyt the primary verifier. It rPverifyegenerate

- rapmentation
Both iROOF_Aand positislasses on eight
vertiplement noffine d
 ict ough Net = vXned-pair or&1&1arisentry-admissibSymPya. Floating-poin
- rapmplay is

```
Both iROOF_Aay com label tenumerate signix simpldlasses
 e exact twenampiled C+ions and         and uses sep.
- rapmentation
BothBe exact e \Pverif/SymPy/NumPyn
- rapmplay is

```
BothBe exact twens comm-oblem has af | leaves exact
| dtion
- rapmplay is

```&1&1&1&1&1able: Pceger and rational linant, and every sundent reshnand[idx[jle. Thte a phenot assere itected ix discotionalr ated-compon
ificationverifier
ndent veClaim\[
 \br prnt reER50_L order-50 ed quotiete a ies. Th
WOW-284ports}&ses aargre-use the ob
r up quentlon makradjauentlon ma attainablessify
irregular cou terexampl
s, and does not affect the expllstrictular order-40
construction. does no
ndent7atio        (ce \(M\) pts/order50_lift_i_lift_exclusion.py --type-a
python scripts_order50_lift_exclusion.py --type-b
```

It uses e_proof_audit_14c_order50_lifts.py
```

It does n0_lift_independent.cpp
scripts/order50_completion_filter.cpp
```
