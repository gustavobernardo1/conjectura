# CJ-0024 manuscript — revision 2: supplementary documentation

Revision 2 (`main.tex`, `main.pdf` in this directory, 6 pages) is an
**editorial** revision of revision 1 (`../main.tex`, committed in `1b4309e`,
SHA-256 prefix `28fc83f1a9e14495`; its local build `../main.pdf`, 4 pages,
prefix `ceb9a5ccd1410e05`). Revision 1 is kept unchanged at its original path,
which the investigation's `STATE.md` and reviews refer to. PDFs under
`manuscripts/` are build products and are not committed (`.gitignore`); each
revision is rebuilt from its `main.tex`.

Prepared 2026-11-28 by Claude (`claude-opus-5-5`) at the request of the project
director, as an editorial task, not a research session. No scientific status in
`research/catalogue.json` or `research/discoveries.json` was changed.

## Review status of this revision

- **Revision 2 has not been reviewed.** Revision 1 had not been reviewed as a
  whole either (`STATE.md`, open obligation 5). The AI reviews listed below
  concern the project notes from which both revisions are drawn.
- No human has checked the mathematics.

## What changed (editorial only)

- New title, running head, abstract (one closing sentence on the open
  characterization parts), MSC 2020 codes (03B52, 03E72), keywords, PDF
  metadata (`\hypersetup`).
- Structure: Introduction (problems, reading remark, overview of results) is
  separated from Preliminaries; the Łukasiewicz family is stated early as
  Proposition 3.1 with its proof deferred to Section 6; Lemmas (Section 4),
  Theorem (Section 5), explicit families and answers (Section 6), Conclusion
  (Section 7), Verification/AI use/originality (unnumbered).
- Definitions, standard operations and all piecewise functions are displayed
  and numbered (`cases`); the facts F1–F5 of the proof of the theorem are an
  enumerated list.
- Notation: standard operations `T_M, S_M, T_L, S_L, T_nM, S_nM, T_D, N_D2`
  are defined explicitly (revision 1 used `T_L`, `T_nM`, `S_M`, `T_D`, `N_D2`
  without definitions). The arguments of `S*_c` are renamed from `(a,b)` to
  `(p,q)` to avoid a clash with the rescaling bound `a`.
- Bibliography: DOIs and page ranges added; the 2015 handbook chapter, cited in
  the originality statement of revision 1 only by description, is now a
  numbered reference.
- Repository paths and administrative detail are moved here.

## Correspondence of numbered items

| Revision 1 | Revision 2 | Change |
| --- | --- | --- |
| Problem A, Problem B, Remark 1 (reading) | Problem A, Problem B, Remark 1.1 | layout only |
| definitions in §1 prose | Definitions 2.1, 2.2, (2.1)–(2.9) | displayed; standard operations defined |
| Lemma 2 (drastic boundary) | Lemma 4.1 | displayed formulas; proof unchanged |
| Lemma 3 (left-continuity) | Lemma 4.2 | "an implication" → "a fuzzy implication" |
| Theorem 4 (general construction) | Theorem 5.1 | displayed (5.1)–(5.5); proof steps unchanged |
| — | Proposition 3.1 | restatement of Corollary A together with the properties stated in revision 1's paragraph after Corollary B (`I_c(c−1,0)=1`, `I_c ≠ I_WB`, distinct `c` distinct) |
| Corollary 5 (A) | Corollary 6.1 | displayed |
| Corollary 6 (B) | Corollary 6.2 | displayed (6.1)–(6.3) |
| paragraph after Corollary 6 | proof of Proposition 3.1 / Corollaries 6.1–6.2 | see below |
| Corollary 7 (answers) | Corollary 6.3 | unchanged |
| Remark 8 (Theorem 6.5 of the 2008 survey) | Remark 6.4 | unchanged |
| "Status, evidence and disclosure" | Section 7 + "Verification, AI use and originality" | expanded, see below |

**Additions that are not pure layout** (each is a direct check of revision 1's
statements, not a new result; they should be read by the next reviewer of the
manuscript):

1. The proof paragraph of Section 6 names the operations to which Theorem 5.1
   specializes: with `ψ(x)=x/c`, `N_0(v)=1−v`, `e=1/2`, `a=1/c`, the operations
   (5.1)–(5.3) become `T_c`, `N_c`, `S_L` (for `T_0=T_L`) and `T'_c`, `N_c`,
   `S*_c` (for `T_0=T_nM`), and `ψ^{-1}(N_0(a)) = c−1`. Revision 1 stated
   only "Taking ψ(x)=x/c … in Theorem C".
2. `J_c(c−1,0)=1` and `J_c ≠ I_WB` are written explicitly; revision 1 wrote
   "In each family I_c(c−1,0)=1, I_c ≠ I_WB", using `I_c` generically. The
   note proves both (`notes/weber-uniqueness.md`, Theorem B, items 4 and 5).
3. The conclusion separates the answered existence questions from the open
   characterization questions and states that Theorem 5.1 is not claimed to
   produce every element of the intersections.
4. The introduction's first paragraph is new narrative; its only factual
   claims are that the intersections are studied for left-continuous t-norms in
   [1, 3] and not characterized otherwise per [4] (both as recorded in the
   literature audit).

## Evidence (repository paths)

| Kind | Location | Status |
| --- | --- | --- |
| Source notes | `research/active/CJ-0024-sn-r-nonborder-intersection/notes/weber-uniqueness.md` (revision 2; revision 1 in `notes/versions/weber-uniqueness-r1.md`), `notes/rescaled-tnorms.md` (Theorem C) | candidate proofs |
| AI review, families, r1 | `reviews/2026-11-27-review-1.md` (Opus) | gaps G1–G5 in side claims |
| AI recheck, families, r2 | `reviews/2026-11-27-recheck-r2.md` (claude-sonnet-5-5) | no gap within stated scope |
| AI review, Theorem C | `reviews/2026-11-27-review-theorem-c.md` (fresh context, same model as author) | no gap within stated scope; review by a different model still owed |
| AI review, Lean statements | `reviews/2026-11-28-lean-statement-review.md` (claude-sonnet-5-5) | statements match within scope; qualifications F1–F4 |
| Lean formalization | `formalization/Conjectura/Research/WeberUniqueness.lean` (25 registered theorems; commit `f5de051`, co-authored by Claude Opus 5.5) | formal status `partial` |
| Lean receipts | `verification/receipts/20261128T030452Z-232840d982-dirty-passed.json`, `20261128T031635Z-f5de051aad-dirty-passed.json` | passed, **on a dirty working tree** |
| Exact computations | `experiments/CJ-0024-sn-r-nonborder-intersection/check_examples.py`, `check_theorem_c.py` | exact rational grid checks passed (finite evidence) |
| Literature audit | `research/candidates/CJ-0024-sn-r-nonborder-intersection-audit.md` | 2015 chapter and 2008 monograph not read |

Review paths are relative to `research/active/CJ-0024-sn-r-nonborder-intersection/`.

The manuscript's sentence "found no `sorry`, and audited their axioms to
`propext`, `Classical.choice` and `Quot.sound`" rests on the receipts above
and on `STATE.md` (open obligation 3); the Lean build was not rerun for this
editorial revision.

## Bibliographic fields not verified in the repository

DOIs of [1], [3], [4], [5], [6] and the page ranges of [1], [3], [4], [6] are
as recorded in the literature audit. The following were added from general
bibliographic knowledge and were not re-checked against a source in this
task: the editors of the 2013 volume [4]; the book title of [5] ("Springer
Handbook of Computational Intelligence"); the series and publisher details of
[2] and [7]; the place of publication "Berlin, Heidelberg". Check them before
any submission.

## Build

```
cd manuscripts/CJ-0024-weber-uniqueness/revision-2
latexmk -pdf -interaction=nonstopmode main.tex
```

Built on 2026-11-28 with MiKTeX `pdflatex` via `latexmk`: 6 pages, no
warnings, no overfull boxes. Every page was rendered (`pdftoppm`, 70 dpi) and
inspected visually.
