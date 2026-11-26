# CJ-0001 — open obligations in detail

Moved here from `STATE.md` on 2026-11-26 (session 5), when that file was
compacted. The text below is the section as it stood at `ef98710`, unchanged;
`STATE.md` carries the current short list and says which items have moved (one relative link was adjusted to the new location)
since. Numbers are those used in the journal and in the registry.

## Obligations as recorded up to session 4

1. **Literature.** The audit of session 2 is in the dossier. Still unread:
   Collins (1989) and her 1986 thesis (publisher and repositories refused
   automated access; everything said about them is second-hand); Graham–Lovász
   pp. 68–79 and 87–88; do Nascimento, Del-Vecchio and de Freitas (2019), "The
   distance matrix of caterpillar", which bears on L3 and possibly on T1; the
   journal versions; MathSciNet, zbMATH, Google Scholar and MathOverflow were
   not searched. For MD-0004 and MD-0005 only one query was made.
2. **Review of T1.** AI review of `5e5ef14` (same model family, fresh context):
   no gap found within stated scope; eight minor discrepancies of
   presentation. No mathematician has read it. Before T1 is promoted it needs
   a human reader or a review by a different model, and the reading of
   Collins (1989). The defects (a) to (g) listed by the review were corrected
   in `notes/double-stars.md` on 2026-11-26 (its *Revision history* says
   what changed); no statement, formula or step of the proof was changed. The
   review was made on the earlier text. A recheck of that revision (`1c38662`)
   by `claude-opus-5-5`,
   [`reviews/2026-11-26-claude-opus-5-5-recheck-T1-T2.md`](../reviews/2026-11-26-claude-opus-5-5-recheck-T1-T2.md),
   found no change to the mathematics and that the first verdict still
   applies; the loose sentences it found were corrected in a second revision,
   which no one but the author has checked.
3. **Review of the audit's identifications.** That L1 is a rewriting of
   Graham–Lovász (10)–(12), and that L3 is a special case of Hogben–Reinhart
   Theorem 3.3, are the auditor's own short computations, unreviewed. They only
   lower what the project claims.
4. **Independent recomputation of E2.** Orders 21–23 were computed by one
   implementation with internal guards (E3); the independent method was run on
   all trees only up to order 9. `results/exhaustive-21-23.json` was produced
   before the first commit and carries no provenance block; rerunning it at a
   committed revision takes about 34 minutes and needs the director's approval
   of the budget. MD-0001 stays `partial-result` until then.
5. **A published data set to compare with.** Table II of Graham–Lovász (1978,
   pp. 85–86) lists the normalized coefficients of all trees on at most eight
   vertices. The project's code has not been compared with it.
6. R1 was restated after the review of `e34acfc`. Its general form was since
   reconstructed in both directions by the review of T1 (`5e5ef14`), and the
   direction used by T2 by the review of T2; the two specialised statements
   of R1 about `M` have not been re-reviewed, and the header of
   `notes/lemmas.md` still says "has not been re-reviewed" (the file is left
   unchanged because two reviews pin its hash).
7. **Formalization.** Only the general form of R1 is formalized (session 4).
   Its statement was compared with the written one by the formalizing agent
   and by the session's author; an independent comparison is owed before the
   formal status is relied on. Next targets, in order of usefulness: Lemma L4
   (independent of trees); the polynomial inequalities of Step 3 of T2 and T3.
8. **Review of T2.** AI review of `74cb5bb` by `claude-opus-5-5`: no gap found
   within stated scope. No mathematician has read it, and no literature
   auditor searched for this statement (do Nascimento, Del-Vecchio and de
   Freitas 2019 on caterpillars is the first thing to read). The review
   listed eight defects of record and presentation. D1 and D2 (no registry
   record and no result file at the reviewed revision) were met by `1ef55b8`.
   D3 to D7 were corrected in `notes/spine3.md` on 2026-11-26 (its *Revision
   history* says what changed); no statement, formula or step of the proof
   was changed, and the review was made on the earlier text. D8 concerns the
   brief given to the reviewer, which misquoted the title of
   arXiv:1507.02341. The commit subject of `74cb5bb` says "every spine-3
   caterpillar", which is broader than T2 (`a, b, c ≥ 1`); the history is not
   rewritten. The recheck of `1c38662` named under obligation 2 found no
   change to the mathematics of T2 and that the first verdict still applies;
   it found three wrong sentences in the revision, corrected in a second
   revision that no one but the author has checked. Still open from it:
   `spine3.py` and `results/spine3.json` keep the words "spine length 3" in
   their description strings (the result file is evidence and is not
   edited).

9. **Review of T3.** AI review of `d2eb9ac` by `claude-opus-5-5`: no gap found
   within stated scope. No mathematician has read it; no literature auditor
   searched for the statement. `notes/diameter4-caterpillars.md` is unchanged
   since the review. Defects it listed, to be corrected in one revision that
   then needs a recheck: (E3) the notes call "Lemma C1" the determinant
   identity, which is a step inside its proof, and call the identities of
   Lemma C2 "between polynomials in `m, a, c`" although `c_0`, `e_0` and the
   `d_k` are not polynomials in `m`; (E4) the description of the caterpillars
   of diameter 4 in the corollary is asserted without argument and
   "caterpillar" is not defined in the notes; (E5) Step 3(ii) writes `R` for
   `R(m, n−3)`; (E6) no script or test re-derives Lemma C2 at `b = 0` (the
   reviewer did). E1 and E2 (no registry record and no result file at the
   reviewed revision) are met by the commit that follows the review.
10. **The exploration is unreviewed.** Lemma L4, the `s = 3` identities of
    `notes/vertex-principle.md` and the extension of L3 to empty leaf classes
    for general `s` (a sketch) have been checked by no one but their author.
    Nothing that depends on them may be promoted.

## The obligations as they read in `STATE.md` at the end of session 7

Moved here verbatim in session 8, when `STATE.md` was compacted. Item 9 was
met in session 8 (regression test `tests/test_cj0001_component_form.py`;
`STATE.md` compacted). The current short list is in `STATE.md`.

1. **Literature.** Session 5 found the closed formulas of T1 and T3, and the
   balanced case of T2, in print (see Sources); T1 to T3 must cite them, and
   Lemma D1 is to be recorded as known. Session 6 read Collins 1993 in the
   author's manuscript (no peak statement, no subset expansion; only the
   balanced double star, with a formula that fails as printed there — see the
   dossier) and thesis pages 14 to 38 (nothing on the peak). L3 and S1 must
   cite Collins 1993, Corollary 7. Still unread: the Discrete Appl. Math. 2019
   paper (the publisher refused automated access; a person can probably open
   it: DOI `10.1016/j.dam.2018.10.018`), the published version of Collins
   1993, Collins 1989, thesis pages 1–3, 6–11, 50–77, Graham–Lovász
   pp. 68–79; no search of MathSciNet, zbMATH, Google Scholar. Session 7: a
   first audit for MD-0011 and MD-0012 found no identical statement and
   three sources to cite — Bapat–Kirkland–Neumann 2005, Thm 2.4 (**the
   determinant behind S3 is in print**: `det(D + xJ)` for weighted trees) and
   Thm 2.1; Richman–Shokrieh–Wu, arXiv:2411.11488, Thms A and 4.4 (principal
   minors of `D` through a Laplacian minor on the complement). Unread and
   most likely to contain Lemma F: matching polynomials of forests, Laplacian
   coefficients of trees (Mohar 2007, Zhou–Gutman, arXiv:2410.14112),
   Chebotarev–Shamis. **No search at all for MD-0013 and MD-0014.**
2. **T1, T2, T3: one revision of the three notes** (citations of the published
   formulas; defects E3 to E5 of the review of T3; the last wording changes of
   T1 and T2, which no one but the author has checked), followed by one
   recheck. A human reader, or a different vendor's model, before any
   promotion.
3. **Reviews of sessions 5 and 6.** S1 to S4 (`1bb2bbe`), S6 to S10 with
   Lemma C (`1805bca`), Lemma F, F′ and S11 (`5622d19`; one paragraph of the note had a gap, repaired and rechecked at `7acd425`): AI reviews, no gap found; reports under
   `reviews/`. Owed: (a) one revision of `notes/skeleton-identity.md` for the
   four defects of its review (the degree bound of `r_A` needs its one-line
   cofactor argument; `γ_A` at `x = 0`; `M_A` used for two matrices; `p_∅`),
   and one of `notes/skeleton-locality.md` (the count 1,011 should be 1,010
   for S9 as stated; "Property Γ" used for one subset; the remark "has to use
   the tree"; a redundant proviso), each followed by a recheck
   (`notes/gamma-reduction.md` was already revised and rechecked; two trivial
   defects of wording remain in it); (b) L4, S5 and
   the Γ computation were reviewed in session 7 (no gap); their defects are
   owed one revision: `vertex-principle.md` (L3′ is superseded by S1; "V(s)
   not proved for any s ≥ 4" is stale), `skeleton-identity.md` (S1 was checked
   with zero leaf numbers only for `s ≤ 5`; "orders up to 100" has no
   committed evidence; "at least two non-leaf vertices"; stale review status),
   the result file's provenance, test coverage (`s ≤ 5` only); (b′) S12 to
   S18 were reviewed at `b0a4dbe` (no gap); `notes/gamma-components.md` is
   left byte-identical to that revision and is owed one revision for three
   defects of wording ("two elementary facts" lists three; statement (E)
   must say "there is a leaf `w`" and quantify `ν`; the opening paragraph
   calls a sufficient condition a reduction and a family of polynomials "one
   polynomial") and for the observation (E″) below, then a recheck; (c) a human reader, or a model of another vendor,
   before any promotion; (d) the two classical formulas (Graham–Pollak,
   Graham–Lovász inverse) have not been compared with the printed papers.
4. **E2** (orders 21 to 23): independent recomputation, about 34 minutes,
   needs the director's approval of the budget. MD-0001 stays `partial-result`.
5. Comparison of the code with Table II of Graham–Lovász (cheap, not done).
6. The audit's identifications of L1 and L3 as known, and the two specialised
   statements of R1 about `M`, are unreviewed.
7. **Formalization.** In Lean: the general form of R1 and the one-dimensional
   core of L4. An independent comparison of the Lean statements with the
   written ones is owed. Next: L4 in `s` variables; Proposition S4 (binomial
   inequalities only).
8. `spine3.py` and `results/spine3.json` still say "spine length 3" in their
   description strings (the result file is evidence and is not edited).
9. This file is above its target of 400 lines since session 7: compact it
   (the dead ends and the details of O7 belong in a note), and add a
   regression test for `component_form.py` (none exists).

## Deferred objective O8 (text of the section "Next step" of STATE.md as left by session 8, moved here in session 9; verbatim except for the target of one link)

**Objective O8.** Prove statement (Λ) of
[`notes/rooted-calculus.md`](rooted-calculus.md), or find a
counterexample. Start from the recursion over the branches at `u`
(`rooted-calculus.md`, "Where the difficulty is"):

`Λ(T, ν, u) = x[R(T, ν) + (1−x)Φ − 2xG + ((1+2x)² + 2x(1+ν_u))Ψ] + x Σ_c Λ(T_c, ν, c) P_c`.

1. The first bracket `Λ⁰ := R(T, ν) + (1−x)Φ − 2xG + ((1+2x)² + 2x(1+ν_u))Ψ`
   was tested in a scratch run of session 8 (not stored): `xΛ⁰ ∈ C_{j+2}`
   failed in 8 of the 4,395 rooted weighted trees with `j ≤ 5`, weights 0 to
   2, and in 7 of 18,009 rooted stars with at most 5 leaves and weights up to
   8 — **in every failing case `ν = 0`** (smallest: the path on 2 vertices,
   `xΛ⁰ = x + 3x²`). So on that range (Λ) splits into two statements:
   **(Λ⁰)** `xΛ⁰ ∈ C_{j+2}` for every rooted weighted tree with `ν ≠ 0`, which
   contains no `Λ` and no `Ω`; and (Λ) for trees with zero weights, a family
   with no parameters besides the rooted tree. First action: add the check
   of (Λ⁰) next to `B3` in `cone_checks` of `rooted_state.py`, store the
   run, and test it on stars, brooms, spiders and double stars with weights
   up to 50.
2. Then expand `Λ⁰` with the merge rule S19(d) for `R` over the branches at
   `u`: the cross terms are `−2G_cG_{c′}` between two branches. Look for the
   inequality between `G_c` and `(R_c, Ω_c, Φ_c)` of one branch that absorbs
   them (on stars: `G^ = 2nx²`, `Ω^ = n(1+5x+4x²) + n²x` for a leaf of weight
   `n`; the cross term `8n n′x⁴` must come from the terms `n²x`).
3. Search wider for a counterexample to (Λ) before investing in a proof:
   weights up to 50 on stars, brooms, spiders and double stars with up to 12
   vertices (minutes of exact computation).

Cheap exact computations that remain: Γ_c for `j = 8`; the trees "skeleton
plus one star" as polynomials in `m`.

Owed first by default: obligations 1 to 3.

## Sources read (the list of the section "Sources" of STATE.md as of session 8, moved here verbatim in session 9)

- G. Aalipour et al., arXiv:1507.02341 — read in full (TeX source; twice by reviewers).
- R. L. Graham, L. Lovász, Adv. Math. 29 (1978) 60–88 — pp. 60–67, 80–86 read.
- L. Hogben, C. Reinhart, arXiv:2103.00647 — pp. 5–12 read.
- A. Abiad et al., arXiv:2206.07561; R. Jana et al., arXiv:2407.03309 — read in full.
- J. Xue, R. Liu, H. Jia, Filomat 30:6 (2016) 1559–1565 — read in full: Lemma 2.3.
- J. S. do Nascimento, D.Sc. thesis, COPPE/UFRJ 2018 — pp. vi–ix, 4–5, 12–49, 78–79 read: Props. 3.2.1, 3.2.6, 3.2.9; Section 3.1.
- J. S. do Nascimento, R. R. Del-Vecchio, M. A. A. de Freitas, Discrete Appl. Math. 266 (2019) 141–152 — not read (DOI `10.1016/j.dam.2018.10.018`).
- K. L. Collins, Discrete Math. 122 (1993) 103–112 — read in full in the author's manuscript (supplied by the director, kept outside the repository); the published version not seen.
- K. L. Collins, Discrete Appl. Math. 25 (1989) 27–35 — not accessible; second-hand only.
- R. Bapat, S. J. Kirkland, M. Neumann, Linear Algebra Appl. 401 (2005) 193–209 — read in full by the auditor: Thm 2.1, Thm 2.4.
- H. Richman, F. Shokrieh, C. Wu, arXiv:2411.11488v2 — read by text extraction, proofs not read (sessions 7 and 8): Thms A, 2.4, 4.4, 4.6, D.
- R. Merris, J. Graph Theory 14 (1990) 365–369 — read in full by the auditor.
- Wan, Wang, Wang (surnames as given by the auditor), arXiv:2410.14112 — read by text extraction (session 8): eq. (1.4), Thms 1.2, 3.1.
- K. Castillo, I. Zaballa, arXiv:2103.13739 — pp. 1–2 read by the auditor (session 8): Thm 2.1.
- Full list with access notes: the dossier.
