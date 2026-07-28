#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

import apply_final_arxiv_line_review as base

ROOT = Path(__file__).resolve().parents[1]
OLD = "v2.2.1"
NEW = "v2.2.2"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise AssertionError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def bump(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if OLD in text:
        text = text.replace(OLD, NEW)
    elif NEW in text:
        return
    elif path.name == "CITATION.cff" and "version: 2.2.1" in text:
        text = text.replace("version: 2.2.1", "version: 2.2.2", 1)
    elif path.name == "CITATION.cff" and "version: 2.2.2" in text:
        return
    else:
        raise AssertionError(f"no current release marker in {path}")
    path.write_text(text, encoding="utf-8", newline="\n")


def clarity(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    replacements = [
        (
            "Let \\(G\\) be a finite simple connected graph.  Write \\(d(v)\\) for the degree\n"
            "of \\(v\\), \\(N(v)\\) for its open neighbourhood, and\n",
            "Let \\(G\\) be a finite simple connected graph.  Write \\(d(v)\\) for the degree\n"
            "of \\(v\\), \\(N(v)\\) for its open neighbourhood, and, for\n"
            "\\(S\\subseteq V(G)\\), let \\(G-S\\) denote the subgraph induced by\n"
            "\\(V(G)\\setminus S\\).  Define\n",
            "G-S definition",
        ),
        (
            "The graph \\(R\\) is the classical \\((6,5)\\)-cage of O'Keefe and Wong\n"
            "\\cite{OKeefeWong1979,Wong1979}.  The Moore block identity gives\n",
            "The graph \\(R\\) is the classical \\((6,5)\\)-cage of O'Keefe and Wong\n"
            "\\cite{OKeefeWong1979,Wong1979}; its realization as a Petersen deletion of\n"
            "the Hoffman--Singleton graph also appears in \\cite{KlinMuzychukZivAv2009}.\n"
            "The Moore block identity gives\n",
            "R attribution",
        ),
        (
            "The second-subconstituent calculation gives\n"
            "\\[\n"
            " \\Spec D(X_{42})=\\{81^{(1)},4^{(6)},0^{(14)},(-5)^{(21)}\\}.\n"
            "\\]\n",
            "The second-subconstituent calculation gives\n"
            "\\[\n"
            " \\Spec D(X_{42})=\\{81^{(1)},4^{(6)},0^{(14)},(-5)^{(21)}\\}.\n"
            "\\]\n"
            "The classical second-subconstituent identification and adjacency spectrum are\n"
            "recorded in \\cite{vanDamHaemers2003}.\n",
            "X42 attribution",
        ),
        (
            "so \\(f_*\\) is admissible and \\(f_*(k)=B_k\\).\n",
            "On \\(I_k\\), the factor \\((x+1)^2-(2k-2)\\) is nonpositive, while\n"
            "\\((x+2)^2\\ge0\\); hence \\(f_*\\) is admissible and \\(f_*(k)=B_k\\).\n",
            "LP primal sign",
        ),
        (
            "all positive for \\(k\\ge4\\).  For \\(i\\ge10\\), put \\(r=k-1\\ge3\\).  The support\n"
            "lies in \\([-2\\sqrt r,2\\sqrt r]\\), because\n"
            "\\(1+\\sqrt{2r}\\le2\\sqrt r\\), and the Chebyshev representation gives\n"
            "\\[\n"
            " \\frac{|\\mu(F_i)|}{F_i(k)}\n"
            " \\le \\frac{2i+1}{3}\\,3^{3-i/2}<1.\n"
            "\\]\n",
            "all positive for \\(k\\ge4\\); for the nontrivial residual factors this follows\n"
            "after writing \\(k=m+4\\), when all coefficients are nonnegative and the\n"
            "constant terms are positive.  For \\(i\\ge10\\), put \\(r=k-1\\ge3\\).\n"
            "The support lies in \\([-2\\sqrt r,2\\sqrt r]\\), because\n"
            "\\(1+\\sqrt{2r}\\le2\\sqrt r\\).  For \\(|z|\\le1\\), the recurrence gives\n"
            "\\[\n"
            " F_i(2\\sqrt r\\,z)\n"
            " =r^{i/2}U_i(z)-r^{(i-2)/2}U_{i-2}(z),\n"
            "\\]\n"
            "where \\(U_j\\) is the Chebyshev polynomial of the second kind.  Using\n"
            "\\(|U_j(z)|\\le j+1\\) yields\n"
            "\\[\n"
            " \\frac{|\\mu(F_i)|}{F_i(k)}\n"
            " \\le \\frac{2i+1}{3}\\,3^{3-i/2}.\n"
            "\\]\n"
            "At \\(i=10\\) the right-hand side is \\(7/9\\), and it decreases thereafter\n"
            "because \\(3(2i+1)^2-(2i+3)^2=8i^2-6>0\\).  Thus it is strictly less\n"
            "than one for every \\(i\\ge10\\).\n",
            "LP tail derivation",
        ),
        (
            "Since \\(f\\le0\\) on the support of \\(\\mu\\), weak duality gives\n"
            "\\[\n"
            " 0\\ge\\int f\\,d\\mu\\ge B_kf_0-f(k).\n"
            "\\]\n",
            "Expanding in the nonbacktracking basis gives\n"
            "\\[\n"
            " \\int f\\,d\\mu\n"
            " =B_kf_0-f(k)+\\sum_{i\\ge5}f_i a_i\n"
            " \\ge B_kf_0-f(k).\n"
            "\\]\n"
            "Since \\(f\\le0\\) on the support of \\(\\mu\\), the left-hand side is at\n"
            "most zero, which proves weak duality.\n",
            "LP weak duality expansion",
        ),
        (
            "For one deleted vertex, put \\(A=N(v)\\), \\(B=\\Gamma_2(v)\\), let \\(C\\) be\n",
            "The displayed dual-degree formulas are the cases \\(s=1\\) and \\(s=2\\) of\n"
            "Theorem~\\ref{thm:small-puncture}; its proof below is independent of the\n"
            "spectral decompositions.  For one deleted vertex, put \\(A=N(v)\\),\n"
            "\\(B=\\Gamma_2(v)\\), let \\(C\\) be\n",
            "puncture dual degrees",
        ),
        (
            "For strictness, the distance-increase matrix is the adjacency matrix of two\n"
            "copies of \\(K_k\\) meeting in \\(w\\), and hence has least eigenvalue\n",
            "The value \\(\\delta^*(H)=k-2/k\\) is again the \\(s=2\\) case of\n"
            "Theorem~\\ref{thm:small-puncture}.  For strictness, the distance-increase\n"
            "matrix is the adjacency matrix of two copies of \\(K_k\\) meeting in \\(w\\),\n"
            "and hence has least eigenvalue\n",
            "nonadjacent dual degree",
        ),
        (
            "Since the parent Moore graph has score\n"
            "\\(k-(3+\\Delta)/2\\) and \\(a-b=2/k\\),\n",
            "Since the parent Moore graph has score\n"
            "\\(k-(3+\\Delta)/2\\) and deletion lowers the minimum dual degree by\n"
            "\\(2/k\\),\n",
            "nonadjacent loss wording",
        ),
        (
            "written derivations are also supplied.  No theorem-level sign or eigenvalue\n"
            "ordering uses floating-point arithmetic.\n",
            "written derivations are also supplied.  No theorem-level sign or eigenvalue\n"
            "ordering uses floating-point arithmetic.  The exact symbolic and graph\n"
            "computations use SymPy and NetworkX \\cite{MeurerEtAl2017,HagbergSchultSwart2008}.\n",
            "software citations",
        ),
    ]
    for old, new, label in replacements:
        text = replace_once(text, old, new, f"{path}: {label}")
    path.write_text(text, encoding="utf-8", newline="\n")


def update_ledger() -> None:
    path = ROOT / "SOURCE_LEDGER.md"
    text = path.read_text(encoding="utf-8")
    old = "This research-only control is not currently part of the manuscript."
    new = "The equality computation is included in the manuscript with this source boundary made explicit."
    if old in text:
        text = text.replace(old, new, 1)
    elif new not in text:
        raise AssertionError("Jorgensen ledger state")
    old = (
        "The Lean files presently prove\n"
        "only the associated scalar inequalities, not the generic graph-to-spectrum\n"
        "theorems. “Punctured Moore graph” is package terminology and must be defined\n"
        "when used."
    )
    new = (
        "The one-variable LP optimum and optimizer rigidity are formalized in Lean as a\n"
        "graph-independent analytic theorem. The generic punctured-Moore spectra and\n"
        "graph-to-spectrum bridges remain conventional analytic proofs. “Punctured\n"
        "Moore graph” is package terminology and is defined when used."
    )
    if old in text:
        text = text.replace(old, new, 1)
    elif new not in text:
        raise AssertionError("formalization ledger state")
    path.write_text(text, encoding="utf-8", newline="\n")


def update_claim_registry() -> None:
    path = ROOT / "research-notes" / "CLAIM_REGISTRY.md"
    text = path.read_text(encoding="utf-8")
    old = "| This is the first observation of the counterexample. | Targeted search found no explicit prior connection, but cannot prove priority. | Not claimed. |"
    addition = "| The all-degree one-variable LP optimum and optimizer rigidity are formalized in Lean. | `lean/Wow284/LPCeiling.lean`, `lean/Wow284LPAudit.lean`, and the pinned public build. | Proved as a graph-independent analytic theorem; the graph trace bridge is not part of this Lean claim. |"
    if addition in text:
        return
    if old not in text:
        raise AssertionError("claim registry priority row")
    text = text.replace(old, old + "\n" + addition, 1)
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    marker_old = r"\newcommand{\RepoTag}{v2.2.1}"
    marker_new = r"\newcommand{\RepoTag}{v2.2.2}"
    current = (ROOT / "main.tex").read_text(encoding="utf-8")
    if marker_old in current:
        base.revise_tex(ROOT / "main.tex")
        base.revise_tex(ROOT / "v22" / "main.tex")
    elif marker_new not in current:
        raise AssertionError("unknown TeX release state")

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
        bump(ROOT / relative)

    update_ledger()
    base.write_release_notes()

    current = (ROOT / "main.tex").read_text(encoding="utf-8")
    if r"For \(|z|\le1\), the recurrence gives" not in current:
        clarity(ROOT / "main.tex")
        clarity(ROOT / "v22" / "main.tex")
    update_claim_registry()
    print("final arXiv line-review driver: PASS")


if __name__ == "__main__":
    main()
