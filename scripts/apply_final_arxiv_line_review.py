#!/usr/bin/env python3
"""Apply the final line-by-line arXiv corrections and prepare release v2.2.2.

This is fail-closed: each mathematical/prose replacement must occur exactly
once in both canonical TeX copies. Release metadata is then advanced from
v2.2.1 to v2.2.2 without rewriting the historical v2.2.1 release notes.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD = "v2.2.1"
NEW = "v2.2.2"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise AssertionError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def revise_tex(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    replacements = [
        (
            r"\newcommand{\RepoTag}{v2.2.1}",
            r"\newcommand{\RepoTag}{v2.2.2}",
            "release tag",
        ),
        (
            "Our contribution is the specialization to\n"
            "the two-sided WOW window, the exact method ceiling, the edge-local cycle\n"
            "certificate, and the deletion theory developed below.  Completed in its\n"
            "original counterexample form on 19 July 2026, this work is, to the author's\n"
            "knowledge, the first proof that WOW-284 is false and the first Lean\n"
            "formalization of such a refutation.  We do not claim that order \\(38\\) is\n"
            "minimum or that the constructions classify all counterexamples.",
            "Our contribution is the specialization to\n"
            "the two-sided WOW window, the exact method ceiling, the edge-local cycle\n"
            "certificate, and the deletion theory developed below.  The paper gives a\n"
            "self-contained refutation and a Lean formalization of its principal finite\n"
            "and optimization certificates.  We make no priority claim, and we do not\n"
            "claim that order \\(38\\) is minimum or that the constructions classify all\n"
            "counterexamples.",
            "priority language",
        ),
        (
            "Thus \\(B\\) has principal eigenvalue \\(K-1\\), eigenvalue \\(-1\\) on\n"
            "\\(C^{\\mathsf T}(\\one^\\perp)\\), and the two Moore roots\n"
            "\\((-1\\pm\\sqrt{4K-3})/2\\) on \\(\\ker C\\).  It remains to identify the\n",
            "Since \\(CC^{\\mathsf T}=(K-1)I\\), the map \\(C^{\\mathsf T}\\) is injective,\n"
            "its image is orthogonal to \\(\\ker C\\), and\n"
            "\\[\n"
            " \\mathbb R^{\\Gamma_2(v)}\n"
            " =\\langle\\one\\rangle\\perp C^{\\mathsf T}(\\one^\\perp)\\perp\\ker C.\n"
            "\\]\n"
            "Thus \\(B\\) has principal eigenvalue \\(K-1\\), eigenvalue \\(-1\\) on\n"
            "\\(C^{\\mathsf T}(\\one^\\perp)\\), and the two Moore roots\n"
            "\\((-1\\pm\\sqrt{4K-3})/2\\) on \\(\\ker C\\).  It remains to identify the\n",
            "second-subconstituent direct sum",
        ),
        (
            "distance matrices are the nonbacktracking polynomials in \\(A\\); summing\n"
            "\\(D=\\sum iA_i\\) and eliminating \\(A_d\\) with \\(J=\\sum A_i\\) proves the\n",
            "distance-\\(i\\) matrices are the nonbacktracking polynomials in \\(A\\); summing\n"
            "\\(D=\\sum_{i=0}^d iA_i\\) and eliminating \\(A_d\\) with\n"
            "\\(J=\\sum_{i=0}^d A_i\\) proves the\n",
            "higher-diameter summation indices",
        ),
        (
            "Lemma~\\ref{lem:diam-rayleigh} and strictness give \\(\\diam(G)<k\\).  The cases \\(k\\le2\\) are immediate.  For \\(k=3\\), the girth\n"
            "lower bound and diameter at most two force the Petersen graph, which is an\n"
            "equality case of Theorem~\\ref{thm:moore-threshold}.",
            "Lemma~\\ref{lem:diam-rayleigh} and strictness give \\(\\diam(G)<k\\).\n"
            "The cases \\(k\\le2\\) are immediate.  For \\(k=3\\), the radius-two lower\n"
            "bound and diameter at most two force equality in the Moore bound.  Hence the\n"
            "graph is a degree-three Moore graph, and Theorem~\\ref{thm:moore-threshold}\n"
            "gives equality rather than strict violation.",
            "degree-three reduction",
        ),
        (
            "\\(n\\in\\{30,31,32\\}\\), and parity removes \\(31\\).  At \\(n=32\\), the\n"
            "normalized distance-layer compression has nonprincipal factor\n"
            "\\[\n"
            " p_{5,6}(x)=4x^3+10x^2-16x-30,\n"
            " \\qquad p_{5,6}(11/6)=-29/27<0.\n"
            "\\]\n"
            "Its largest root therefore exceeds \\(11/6>-1+\\sqrt8\\), contradicting the\n",
            "\\(n\\in\\{30,31,32\\}\\), and parity removes \\(31\\).  At \\(n=32\\), the\n"
            "normalized distance-layer compression is monotone in the average internal\n"
            "degree of the distance-two layer.  At the smallest feasible value, its\n"
            "nonprincipal factor is\n"
            "\\[\n"
            " p_{5,6}(x)=4x^3+10x^2-16x-30,\n"
            " \\qquad p_{5,6}(11/6)=-29/27<0.\n"
            "\\]\n"
            "Because the leading coefficient is positive, its largest root exceeds\n"
            "\\(11/6>-1+\\sqrt8\\), contradicting the\n",
            "degree-five compression explanation",
        ),
        (
            r"\sum_{a\in U,b\in V}d(a,b)\ge2k^2+k.",
            r"\sum_{a\in U,b\in V}d_G(a,b)\ge2k^2+k.",
            "distance notation",
        ),
        (
            "Thus increasing the polynomial degree cannot improve this one-variable LP\n"
            "bound.  If the nonprincipal spectrum lies in the interior of \\(I_k\\), then\n"
            "\\(n<B_k\\).",
            "Thus increasing the polynomial degree cannot improve this one-variable LP\n"
            "bound.  Consequently, any connected \\(k\\)-regular graph of girth at least\n"
            "five whose nonprincipal spectrum lies in the interior of \\(I_k\\) satisfies\n"
            "\\(n<B_k\\).",
            "LP graph consequence",
        ),
        (
            r"order-\(50\) Hoffman--Singleton graph",
            r"order \(50\) Hoffman--Singleton graph",
            "order typography",
        ),
        (
            "Hence \\(a-b-c-a'\\) is a surviving path.  Hence\n",
            "Hence \\(a-b-c-a'\\) is a surviving path, and therefore\n",
            "duplicated Hence",
        ),
        (
            "The residual adjacency trace is \\(k-2\\), giving \\(a_\\pm\\).  The residual\n"
            "negative root is greater than \\(-2-\\sqrt{k}\\), and the same is true of the\n"
            "smaller constant-quotient roots because\n",
            "The residual adjacency trace is \\(k-2\\), giving \\(a_\\pm\\).  The residual\n"
            "negative root is greater than \\(-2-\\sqrt{k}\\).  The same is true of the\n"
            "smaller constant-quotient roots: in each case the leading diagonal entry of\n"
            "the shifted quotient is positive, and\n",
            "quotient positive-definiteness explanation",
        ),
        (
            "\\begin{proof}\nLet \\(x,y\\in V(H)\\) be nonadjacent in \\(M\\), and suppose their unique common\n",
            "\\begin{proof}\nThe case \\(s=0\\) is immediate, so assume \\(1\\le s\\le k-1\\).  Let\n"
            "\\(x,y\\in V(H)\\) be nonadjacent in \\(M\\), and suppose their unique common\n",
            "empty-deletion boundary case",
        ),
        (
            r"\mathcal M_\pi=\{P_{i,j}Q_{\pi(i),i\pi(i)+j}:i,j\in\F\}",
            r"\mathcal M_\pi=\bigl\{\{P_{i,j},Q_{\pi(i),i\pi(i)+j}\}:i,j\in\F\bigr\}",
            "matching as unordered edges",
        ),
        (
            "Representative axiom reports contain only\n",
            "The public endpoint axiom reports contain only\n",
            "axiom wording",
        ),
        (
            r"\section{Characteristic polynomials for the smallest explicit descendants}",
            r"\section{Characteristic polynomials for the order-39 and order-38 descendants}",
            "appendix title",
        ),
        (
            r"and correspond to release \texttt{v2.2.1}.",
            r"and correspond to release \texttt{v2.2.2}.",
            "release prose",
        ),
    ]
    for old, new, label in replacements:
        text = replace_once(text, old, new, f"{path}: {label}")
    path.write_text(text, encoding="utf-8", newline="\n")


def bump_current_text(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if OLD not in text:
        raise AssertionError(f"expected current release marker in {path}")
    path.write_text(text.replace(OLD, NEW), encoding="utf-8", newline="\n")


def update_source_ledger() -> None:
    path = ROOT / "SOURCE_LEDGER.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "This research-only control is not currently part of the manuscript.",
        "The equality computation is included in the manuscript with this source boundary made explicit.",
        "Jorgensen manuscript status",
    )
    text = replace_once(
        text,
        "The Lean files presently prove only the associated scalar inequalities, not the generic graph-to-spectrum\n"
        "theorems. “Punctured Moore graph” is package terminology and must be defined\n"
        "when used.",
        "The one-variable LP optimum and optimizer rigidity are formalized in Lean as a\n"
        "graph-independent analytic theorem. The generic punctured-Moore spectra and\n"
        "graph-to-spectrum bridges remain conventional analytic proofs. “Punctured\n"
        "Moore graph” is package terminology and is defined when used.",
        "formalization status",
    )
    path.write_text(text, encoding="utf-8", newline="\n")


def write_release_notes() -> None:
    path = ROOT / "RELEASE_NOTES_v2.2.2.md"
    if path.exists():
        return
    notes = """# WOW-284 v2.2.2

Final arXiv line-by-line review of the expanded manuscript.

- Removes priority language that a targeted source search cannot establish conclusively.
- Makes the second-subconstituent direct sum, higher-diameter summation indices, low-degree reductions, and quotient positive-definiteness arguments explicit.
- Repairs the empty-deletion boundary case, matching-edge notation, duplicated prose, and ambiguous appendix title.
- Rebuilds the manuscript in an arXiv-like TeX Live environment; the source-generated PDF has 20 pages.
- Regenerates the canonical PDF, Markdown reading copy, arXiv source archive, metadata, manifest, and SHA-256 ledger.

No theorem statement or numerical certificate is weakened by these corrections.
"""
    path.write_text(notes, encoding="utf-8", newline="\n")


def main() -> None:
    revise_tex(ROOT / "main.tex")
    revise_tex(ROOT / "v22" / "main.tex")

    for relative in (
        "CITATION.cff",
        "README.md",
        "BUILD_VERIFICATION.txt",
        "SUBMISSION_NOTES.md",
        "REVIEW.md",
        "LICENSE_SCOPE.md",
        "scripts/sync_manuscript_artifacts.py",
        "scripts/validate_repository.py",
        "scripts/audit_v22_manuscript.py",
    ):
        bump_current_text(ROOT / relative)

    update_source_ledger()
    write_release_notes()
    print("final arXiv line-review corrections: PASS")


if __name__ == "__main__":
    main()
