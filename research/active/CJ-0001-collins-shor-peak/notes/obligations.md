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

## Text moved from `STATE.md` in session 11 (verbatim except for the targets of relative links)

Obligations 1 to 8 as they read in `STATE.md` at the end of session 10 (the director's decision of session 11
defers human consultation until there is a mature manuscript; see `STATE.md`, Decisions):

1. **Literature.** T1 to T3 must cite the published formulas; L3 and S1 must
   cite Collins 1993, Cor. 7; S3 must cite Bapat–Kirkland–Neumann 2005,
   Thm 2.4. **Session 8:** MD-0013 items (ii) (bound) and (iv) must cite
   Richman–Shokrieh–Wu, arXiv:2411.11488 (Thms A, 2.4, 4.4, 4.6) — the
   auditor's bridging step is unreviewed, and that paper was read by text
   extraction only; S13(d) has a shorter proof by a definite pencil (auditor's
   remark, unreviewed); Lemma G1 is classical; `Φ(T, ν)` is the principal
   Laplacian matching polynomial of arXiv:2410.14112. Still unread: the
   sources listed in the dossier's two audit sections; no search of
   MathSciNet, zbMATH, Google Scholar. No search for MD-0015.
2. **T1, T2, T3: one revision of the three notes**, then one recheck. A human
   reader, or a different vendor's model, before any promotion.
3. **Revisions owed after reviews** (each followed by a recheck):
   `skeleton-identity.md`, `skeleton-locality.md`, `vertex-principle.md`,
   `gamma-components.md` (three defects of wording), two trivial defects in
   `gamma-reduction.md`, `rooted-calculus.md` (seven defects of wording
   listed by its review: degrees in the proof of S21 when all weights are 0;
   "strictly larger" for Γ_w argued only for `d ≥ 2`; Remark 2 ignores parts
   of zero weight; two sentences after S21; the result files were produced
   on a dirty tree at `9069d88`; (★) and S20(d) checked by an unstored
   script), the result file's provenance and
   test coverage of `skeleton_structure.py`. A human reader, or a model of
   another vendor, before any promotion. The two classical formulas
   (Graham–Pollak, Graham–Lovász inverse) have not been compared with the
   printed papers.
4. **E2** (orders 21 to 23): independent recomputation, about 34 minutes,
   needs the director's approval of the budget. MD-0001 stays `partial-result`.
5. Comparison of the code with Table II of Graham–Lovász (cheap, not done).
6. The audit's identifications of L1 and L3 as known, and the two specialised
   statements of R1 about `M`, are unreviewed.
7. **Formalization.** Done: see Status. Owed: an independent
   comparison of all the registered Lean statements with the written ones;
   the bridge from multi-affine polynomials to the exchange inequality (L4
   as written); the inductive cone against explicit non-negative sums, and a
   non-membership example. Next: Proposition S4 (binomial inequalities for
   the generators of `C_d`), then Lemma F.
8. `spine3.py` and `results/spine3.json` still say "spine length 3" in their
   description strings (the result file is evidence and is not edited).

Decisions of sessions 1 to 8, as they read in `STATE.md` at the end of session 10:

- 2026-11-26. CJ-0001 selected first. Strong reading of ties.
- 2026-11-26 (director). MD-0006 to MD-0008 stay candidate theorems until
  their validity and originality are adequately assessed; an AI review is not
  that assessment. Every description of T2 states `a, b, c ≥ 1`.
  Formalization accompanies the investigation. The session budget of 60
  minutes is binding, review and verification included.
- 2026-11-26 (director, session 5). Priority: a general mechanism, not
  further fixed-spine theorems.
- 2026-11-26 (sessions 3 to 7). Reviews by a model other than the author's.
  A note is left byte-identical to the revision that was reviewed; its
  defects are corrected in one revision that is then rechecked; new results
  go in a new note. Γ⁺, Γ_c and (E) are not registered as conjectures of
  their own.
- 2026-11-26 (director, sessions 7 and 8). The classifications of MD-0011 to
  MD-0014 are approved as they stand. Verified commits may be pushed to
  `research` only.
- 2026-11-26 (session 8). (Λ) is stated inside MD-0015 and not registered as
  a conjecture of its own, like Γ_c and (E). MD-0013 is not split: its items
  (ii) (bound) and (iv) are recorded as implied by Richman–Shokrieh–Wu in its
  novelty search; splitting it is a decision for the director.

## Text moved from `STATE.md` in session 13 (verbatim except for the targets of relative links)

Moved on 2026-11-27 to keep `STATE.md` compact; the summaries left in `STATE.md` point here.

## Decisions

- Sessions 1 to 8 (verbatim in [`notes/obligations.md`](obligations.md),
  last section). Still in force: strong reading of ties; T1 to T3 stay
  candidate theorems (director); every description of T2 states
  `a, b, c ≥ 1`; formalization accompanies the investigation; reviews by a
  model other than the author's; a note is left byte-identical to the
  revision that was reviewed, its defects go into one revision that is then
  rechecked, new results go in a new note; Γ⁺, Γ_c, (E), (Λ) are not
  registered as conjectures of their own; MD-0013 is not split.
- 2026-11-26 (director, session 9). The AI investigator allocates effort by
  its own judgment; earlier directions are revisable. MD-0013 keeps its
  identifier and review; its items are classified as known or potentially
  original in the record. The current classifications are approved; verified
  commits may be pushed to `research` only.
- 2026-11-26 (session 9). Direction changed: the lower half is attacked for
  the whole tree (Wiener form, leaf recursion), not through Γ, L4 and
  "skeleton plus one star". O8 ((Λ)) is deferred, not abandoned: (Λ) still
  implies (Γ_c¹). (SM) is registered as a conjecture of its own (MD-0017)
  because it implies the lower half for every tree; (Γ_c¹) is not.
- 2026-11-26 (director, session 10). MD-0016 is to receive independent
  validation and an originality assessment before promotion; CJ-0001 keeps
  its status until the validation requirements are met; the director's
  preliminary reading with GPT-6.2 (no apparent gap) is not a proof audit.
  Verified commits may be pushed to `research` only.
- 2026-11-26 (session 10). `wiener-form.md` had its one revision (`a3e5179`)
  and is left byte-identical to it; the five defects found by the audit of
  that revision go into one further revision. (SM⁺) is recorded under
  MD-0017, not registered. S28 to S31 are one record (MD-0018).
- 2026-11-26 (director, session 11). Session budget 120 minutes, with
  checkpoints (harness commit `759d93f`); this replaces the 60 minutes of the
  decision above. For the current phase the project relies on independent AI
  reviews, adversarial verification, exact computation and Lean; **human
  specialist consultation is deferred until there is a mature manuscript**
  (this replaces "a human reader, or a different vendor's model, before any
  promotion" as the next step of obligations 2, 3 and 9; the requirement of
  section 4 of `AGENTS.md` for promotion is unchanged). Verified commits may
  be pushed to `research` for research contributions.
- 2026-11-26 (session 11). T5, T6 and S36 are one record (MD-0019); MD-0017
  keeps its identifier and its statement (the conjecture (SM)), now with a
  candidate proof. The lower half is treated as a candidate proof to be
  consolidated into one self-contained manuscript before promotion.
- Earlier decisions (budget overrun of session 1, widening of O1, deferral of
  the rerun of orders 21 to 23, the notes of sessions 5 and 6) are in the
  journal.


9. **T4 (MD-0016), before any promotion.** Done: two AI reviews (same
   vendor), no gap; a first literature audit; Lean for Lemma A and `K_d`.
   Owed: (a) one revision of `wiener-form.md` for the audit's defects D1 to
   D5 (S26 and the tools list still cite Lemma F; `W = Σ_e n_e(n − n_e)`
   uncited; L1 at `n = 2`; the `C`-clause of S24; "strong induction"), then
   a recheck, then drop the dependency on MD-0012; (b) **a human reader or a
   model of another vendor** — the director's GPT-6.2 reading is not a
   recorded audit; (c) literature: Collins 1989 and Collins's thesis were
   **read in session 11** (neither contains S25 or T4; the thesis has a leaf
   formula, Theorem 4, to be cited for S23 and S29, and a formula for two
   graphs joined at a vertex, Theorem 7, to be cited for S19(d); S23(d) is
   Collins 1989, Theorem 1). Still unread: Graham–Lovász pp. 72–88, Merris
   1990, Moon 1995; MathSciNet, zbMATH, Google Scholar not searched; the
   auditor's two bridging steps (S24, identity (1)) are unreviewed; (d) a
   result package. `leaf-telescoping.md` (S23, S27) is **unreviewed**.
10. **Session 10.** `even-order.md` (S28 to S31, MD-0018) is **unreviewed**
   and has no literature search. The Lean statements of `WienerCone.lean`
   were compared with the note by the formalizing agent and the author only.
11. **Session 11: T5, T6, S36 (MD-0019), before any promotion.** Done: two
   independent AI reviews of `lower-bound.md` at `74d65b0`, both **no gap
   found** — `claude-opus-5-5` (every step by hand, S23(a) to (c) included;
   its own code on all 205,002 trees of order 3 to 18 and on extreme
   families) and `claude-fable-5-2` in a fresh context (the author's model,
   so independent by context only; a machine re-derivation from the
   definitions on 7,813 rooted trees of order ≤ 12, 18,048 pairs, weighted
   trees, all trees of order ≤ 18); the stored computation `lower_bound.py`
   (1,040,693 checks, 0 failures); Collins (1986, 1989) read. Owed:
   (a) **one revision of `lower-bound.md`**, then a recheck, for the defects
   the two reports list (none is a gap): the section "Exact checks" cites a
   script that did not exist at the reviewed revision and gives "778 pairs"
   where the described set has 1,064, and "1,064 pairs" for S36 of which 486
   are outside its hypothesis; the proof of S32 is by reference to that of
   S24 and should be written out; Remark 1 of S36 asserts `E ≡ 0 (mod x²)`
   without argument; notation used twice (`E` is not the `E` of S17 and S20;
   `a`, `a_v`, `a_i`; `Q`, `Q¹`; `X`, `X_{il}`; `n` for a weight in "S19(a)
   with `n = 0`"); in `leaf-telescoping.md`, S23(a) uses L1 at `n = 2` while
   `lemmas.md` states it for `n ≥ 3` (true at `n = 2`; a citation defect).
   The note is left byte-identical to `74d65b0` until that revision.
   **Session 13: (a) done** — revision 1 at `e16cb62` (S32 written out, L1
   at `n = 2`, Remark 1 marked unproved, exact checks at the stored run,
   notation list), rechecked by `claude-sonnet-5-5`: no gap; five defects of
   bookkeeping remain (the unreviewed status of S23(a) to (c) not listed as
   left, the wording of Remark 1, one notation item, part E not listed; the
   README, corrected).
   (b) **One self-contained manuscript of the lower half**, from the
   Graham–Lovász inverse to T6(c) (L1, Lemma K, S24, S19 with zero weights,
   S23, S33 to S35, T5, T6), then a complete audit of that one document; a
   model of another vendor when one is available (human consultation is
   deferred by the director's decision of session 11). S19 was re-derived by
   neither reviewer of this session (they relied on the review of `59c47f7`
   and on exact checks). (c) Literature: see the audit of session 11 in the
   dossier, and the limits it states. (d) A result package. (e) The Lean
   statements of `LowerBoundCone.lean`, if registered, were compared with
   the note by the formalizing agent and the author only.

12. **Session 12: T7, T8 (MD-0020).** Done: one AI review of
   `path-maximality.md` at `8b03309` (`claude-opus-5-5`, the author's model;
   no gap); the stored computation `tree_shift.py` (`results/tree-shift.json`,
   0 failures). Owed: one revision of the note for the review's defects D1 to
   D8 (the cited code for `Δ_k = c_k` is the wrong scratch script — the check
   is now part A of `tree_shift.py`; notation `a_j`, `ρ_k`, `C(t)`, `Q`, `T_0`;
   a self-contradictory sentence in the equality remark; the star's unique
   peak cited to S23(d) instead of Collins 1989; two negative claims stated
   beyond their support; the path bound attributed to Collins's theorem
   rather than to its informal last step; the header's dependency list), then
   a recheck; a reviewer of another model when one is available; a
   literature search aimed at distance-matrix versions of Csikvári's
   results; it depends on MD-0019 and MD-0015, which are candidates.


(From the section "Remaining obstacles")

- **Upper half (session 13).** No mathematical obstacle is known: T9 is a
  candidate proof for every tree; what remains is validation (obligation 13).
  The text below is the obstacle as it stood before session 13.
- **Upper half, before session 13.** Reduced to (PM) (MD-0021), with no proof mechanism: the
  cone order controls only `μ ≤ n/2`, and ratio dominance fails at the
  relevant index. What a proof must show is a sign: with `p = p_max(T_k)`,
  `λ_{p+1}(ℓ_{T′_k}) = λ_{p+1}(ℓ_{T_k}) − λ_{p+1}(ℓ_{T_k} − ℓ_{T′_k}) < 0`, where
  the second term is given by S37. A(ii) is unproved beyond `k = 0`.

(From the section "Next step")

The items below are as left by session 12 (the part on (PM) is no longer on
the route to the conjecture).

**Owed first.** (a) Obligation 11: the one revision of
`notes/lower-bound.md` for the defects listed there, and its recheck; then
`manuscripts/CJ-0001-lower-bound/`, one self-contained proof of T6(c) from the
Graham–Lovász inverse (L1, Lemma K, S24, S19 for zero weights, S23, S33 to
S35, T5, T6) for a complete audit. (b) Obligation 12: the one revision of
`notes/path-maximality.md` for the defects D1 to D8 of its review, and its
recheck.

**Objective O11 (the upper half) through (PM) (MD-0021).** First action
(exploration, cheap, exact): for the shifts of order ≤ 14 where ratio
dominance fails at `p = p_max(T_k)`, split `λ_{p+1}(ℓ_{T_k} − ℓ_{T′_k})` into the
four terms of S37 and see which one is negative and how it compares with
`λ_{p+1}(ℓ_{T_k})`; look for an inequality between `λ_{p+1}` of the terms
`a_{k−1}(H_AE_B + E_AH_B)` and `λ_{p+1}(ℓ_{T_k})` that a proof could use. Keep
testing (PM) on families before building on it (spiders with legs of mixed
lengths and caterpillars near the star at orders ≥ 200).

Upper cone, floating-point LP of session 11 (exploratory, not a
certificate): for every tree of order 5 to 14 the part of `ℓ_T` of degree
`≤ n − 2` is a non-negative combination of `x^e(1+x)^i` with `2e + i ≤ 2M + 1`
(on which `λ_{M+1} ≤ 0`), with no margin for two near-stars at order 14.

Also open and cheap: obligations 5 and 8; the rerun of orders 21 to 23
(obligation 4) needs the director's approval of its budget.

## Text moved from `STATE.md` in session 15 (verbatim except for the targets of relative links)

### The paragraph on (PX-peak) and (PM), as of session 14

**(PX-peak) and (PM) — open (MD-0021, session 12); no longer needed for
the upper half since session 13 (T9 proves the bound directly).** T9 gives
(PX-peak) for every `n` with fractional part of `n − n/√5` below `2/5`: then
the path peaks at `⌊n − n/√5⌋` (S48(a)) and `p_max(T) ≤ ⌈n − n/√5 − 2/5⌉ =
⌊n − n/√5⌋`. Open for the other `n`. (PX-peak):
`p_max(T) ≤ p_max(P_n)` for every tree. (PM): for every generalized shift,
`p_max(T′_k) ≤ p_max(T_k)`. Proved: (PM) ⇒ (PX-peak) (S39 and induction on
the leaves); (PX-peak) and `p_max(P_n) ≤ ⌈n − n/√5⌉` ⇒ the upper half. The
path bound is the informal last step of Collins's Theorem 3; exact for
`n ≤ 2000` (the path's maximizing index is unique and equals
`⌈n − n/√5⌉` for 393 values of `n`, `⌊n − n/√5⌋` for 1,605). Evidence for
(PM), exact (`results/tree-shift.json`, part E): every shift of every tree of
order 5 to 15; 10,812 shifts of families of orders 20 to 150; 4,000 random
shifts of random trees of orders 30 to 100; no violation; smallest relative
margin about 0.0014 (order 120). Scratch, not stored: double brooms shifted
to brooms up to order 300, no violation, margin about `c/n`, `c` between 0.3
and 0.7. Ratio dominance `d_{j+1}(T′)/d_j(T′) ≤ d_{j+1}(T)/d_j(T)` fails even
at `j = p_max(T_k)` (2,292 of 95,248 shifts of orders 4 to 14, the smallest
`S(2,2) → S_6`; the reviewer of `8b03309`), so (PM) needs another mechanism.

(Session 15: its sentence "Open for the other `n`" and the claim in "Next step" that those `n` need a sharper mode-mean inequality were too strong; see the review of revision 2 of the manuscript, finding 2, and `STATE.md`.)

### Open obligations 9 to 14, as of session 14

9. **T4 (MD-0016):** one revision of `wiener-form.md` for the audit's defects
   D1 to D5 and a recheck; a reader of another vendor; literature still
   unread (Graham–Lovász pp. 72–88, Moon 1995); a result package.
   `leaf-telescoping.md` (S23, S27) has had no review of its own.
10. **Session 10:** `even-order.md` (MD-0018) unreviewed, no literature
   search; `WienerCone.lean` compared by its author only.
11. **Session 11: T5, T6, S36 (MD-0019).** Two AI reviews of `74d65b0`, no
   gap; stored computation `lower_bound.py`, 0 failures. (a) **Done in
   session 13:** revision 1 at `e16cb62`, rechecked (`claude-sonnet-5-5`, no
   gap; five defects of bookkeeping left: the unreviewed status of S23(a) to
   (c), the wording of Remark 1, one notation item, part E not listed).
   (b) **Owed: one self-contained manuscript** (L1, Lemma K, S24, S19 with
   zero weights, S23, S33 to S35, T5, T6), audited as one document by a
   model of another vendor when available; S19 was re-derived by neither
   reviewer of session 11. (c) Literature (audit of session 11). (d) A result
   package. (e) `LowerBoundCone.lean` compared by its author only.
12. **Session 12: T7, T8 (MD-0020).** One review of `8b03309`, no gap; one
   revision for its defects D1 to D8 and a recheck owed; a reviewer of
   another model; literature on distance versions of Csikvári's results.

13. **Session 13: T9, T10 (MD-0022, MD-0023), before any promotion.** Done
   in session 13: the note `notes/upper-bound.md` at `53421a6`; two
   independent AI reviews of that revision, no gap (`claude-opus-5-5` by
   context, `claude-sonnet-5-5` a different model); revision 1 at `2037b18`
   for their defects (wording, notation, citation, provenance); a literature
   audit (dossier, section of session 13); the stored computation
   `upper_bound.py` (`results/upper-bound.json`, run at `917d657` on a clean
   checkout, 0 failures); the recheck of revision 1 (`claude-sonnet-5-5`,
   no gap; four defects of bookkeeping: the citation limits not listed as
   left open, the README (corrected), `d_k` from `lemmas.md` not under
   Tools, the name of the provenance block); a first review of
   `notes/path-peak.md` at `2037b18` (MD-0024; `claude-sonnet-5-5`, no gap;
   four defects of wording: the ceiling criterion written for `n ≥ 6` only,
   an outdated sentence about `upper-bound.md`, the reliance on Collins's
   formula beyond `n ≤ 30`, a redundant condition); Lean for Lemma S41
   (`UpperBoundPeak.lean`; statement compared by the formalizing agent and
   the author only). Owed: those defects in one later revision of each note
   (no recheck of a recheck is planned); the auditor's derivation of T10 from
   Andriantiana–Misanantenaina–Wagner (two classical steps unchecked);
   Darroch (1964) not read in the original (read through Pitman 1997 by the
   auditor and a reviewer); a reviewer of another vendor when one is
   available; one manuscript of the whole conjecture; a result package;
   Lean beyond Lemma S41. **Draft manuscript of the upper half**
   (`manuscripts/CJ-0001-upper-bound/main.tex`, session 13, by a
   publication-agent subagent; compiles with MiKTeX pdfLaTeX, 18 pages;
   **unreviewed**): it supplies three small steps missing from the note —
   a proof of Corollary 3 (`p_max(T) < n + 1 − tr(I+L_T)^{−1}`, via the
   largest mode of `q` and S41), `K ≥ 2` in the proof of T9 (needed for
   `k ≥ 0` in S41), the case `Y = {v}` of S43 — and some citation details
   from memory (titles of Darroch 1964 and Pitman 1997, Graham–Pollak 1971,
   textbooks) that must be checked before any use. Next: an audit of the
   draft as one document, then extend it to the whole conjecture.
   (Superseded in session 14 by the manuscript of obligation 14.)

14. **Session 14: the manuscript of the whole conjecture**
   (`manuscripts/CJ-0001-collins-shor/main.tex`, first commit `8df6bea`;
   review packet `README.md`, `REVIEW-PROMPT.md` there). New in it and not
   reviewed before: Lemma 5.1 ((★) for root weights only) and the derivation
   of the raise and plant rules from it, replacing S15 and S16; the leaf
   recursion S23(b) derived from the plant rule; the presentation with the
   cones `K_d` only. Checked by `manuscript_check.py` (exact, independent of
   the notes' code; `results/manuscript-check.json`). Reviews of the whole
   document at `8df6bea`: `claude-opus-5-5` and `claude-sonnet-5-5` (fresh
   contexts), both no gap found within stated scope
   (`reviews/2026-11-27-*-manuscript.md`); their defects corrected in
   revision 2 (`87c3c8c`), which also adds Lemma 7.5 (the shape of the
   star's sequence), so that neither bound uses the log-concavity theorem of
   arXiv:1507.02341 or Collins's Theorem 1; recheck of revision 2: journal
   of session 14. The count "1,346,023 trees of order 3 to 20" in
   `notes/leaf-telescoping.md` is a slip for 1,346,022 (orders 2 to 20 give
   1,346,023); left in the note, corrected in the manuscript. Owed: a review
   by a model of another vendor (use `REVIEW-PROMPT.md`); human reading
   (deferred by the director); a result package; the literature items of
   obligations 9, 11(c), 13.

### Sections "Conjectures and hypotheses", "Failed approaches" and "Counterexamples and observations", as of session 14 (without the (PX-peak) paragraph, which is above)

## Conjectures and hypotheses of this investigation

**Statement (SM), star minimality (MD-0017, session 9) — candidate proof
since session 11 (Theorem T6(b), MD-0019).** For every tree of order
`n ≥ 3`: `ℓ_T − ℓ_{S_n} ∈ C_{n−1}`. Exact for all 1,346,023 trees of order 3
to 20 (equality only for the star). It implies the lower bound `⌊n/2⌋` for
**every** tree, and it follows from **(Γ_c¹)**: `R(B, e_c) ∈ C_{j+1}` for
every rooted tree, which is Theorem T5. **(SM⁺)** (session 10): `Ω_T ∈ C_{n−1}`
for every tree; it follows from T5(i) and the formula of S30 (unreviewed).
**(CM)** (session 11): the same cone order is respected by the contraction
of any non-pendant edge (S36). Still open, and no longer needed for the
lower half: Γ_c for general weights, (E), (Λ), Conjecture Γ.

**Three kinds of extremality** (session 12; `path-maximality.md`, last
sections). (1) *Coefficientwise*: `d_k(S_n) ≤ d_k(T) ≤ d_k(P_n)` — T6(b) and
T8, candidate proofs. (2) *Increments below the middle*: the same order for
`d_μ − d_{μ−1}`, `μ ≤ ⌊n/2⌋`; the cone reaches no further. (3) *Peak
location*: the star is peak-minimal (every tree has `p_min ≥ ⌊n/2⌋ = p_max(S_n)`;
this is T6(c), the lower half); whether the path is peak-maximal is open,
and (1) does not imply it (termwise domination does not order maximizing
indices).

**Conjecture Γ (MD-0010) and Hypothesis V (MD-0009) — open; no longer on
the route to the lower half.** Γ: for every tree `S` and every `A ⊆ V(S)`,
`|A| ≥ 2`, the polynomial `r_A` is in the half-gamma cone `C_{s−|A|+1}`.
Proved for `A = V`, for `A` with independent complement or complement of at
most two vertices, and (exactly) for the 47 trees with 2 to 8 vertices; all
roots of `r_A` are real. Chain `Γ ⇐ Γ⁺ ⇐ Γ_c ⇐ (E) ⇐ (Λ)`; (E″), (S) false.
V: non-negative mixed partials of `D_n` for caterpillars. Full text as of
session 10: [`notes/gamma-chain.md`](gamma-chain.md), last section.

**Hypothesis A(ii) — open (MD-0005).** For every tree `T` of order `n` and
every `0 ≤ k ≤ min(p_n, n−3)`, `p_n` the largest maximizing index of the path:
`ρ_k(T) ≤ ρ_k(P_n)`. Exact for all trees of order 4 to 20 and 10,000 sampled
trees of orders 24 to 90; proved for `k = 0` (L2). With Collins's theorem on
paths it would give the upper half. The path does not maximize `ρ_k` at every
index.

**Questions Q1, Q2 — open.** Q1: for balanced caterpillars with fixed spine
length `s`, `n(1 − q) → 6/(2s+3)` (observed at `n = 10³ … 10⁶`). Q2: is
`q(T) < 1` for every tree of even order (the lower half)? The smallest margins
found are on balanced caterpillars whose spine grows slowly with `n`
(`1 − q ≈ 1.3 × 10⁻⁶` at `n = 10⁵`, spine 33); `results/near-star-families.json`.

## Failed approaches and refuted hypotheses

Full text of each: [`notes/dead-ends.md`](dead-ends.md).

- **Hypothesis A(i) — refuted (MD-0004).** `ρ_k(T) ≥ ρ_k(S_n)` for
  `k ≤ ⌊n/2⌋ − 1` holds for all trees of order 4 to 19 and fails at order 20
  (`S(9,9)`: `q = 10255/10791 > 94/99`). Do not retry star-comparison at
  `k = ⌊n/2⌋ − 1`.
- **Inequality (3) of `wiener-form.md` — refuted as a route (S31, session
  10).** Dropping the pairs at distance ≥ 2 from the Wiener form loses the
  even case: negative at `n = 100` on spiders with legs of length 2. The
  cone statement `4(W − 3n)Θ_T − 16n(1+x)^{n−2} − Σ_e (n − 2n_e)² Π_e ∈ C_{n−2}`
  (which would imply (3) > 0) holds for all trees of order 7 to 15 and fails
  on the same spiders from about `n = 30` (scratch, not stored). **Test
  even-order statements on spiders with many legs of length 2 at `n ≥ 100`.**
- **Roots of `r_A`** (session 7): real-rootedness does not give the cone
  (`1 + 5x/2 + x²/2`); pairing roots cannot work for long paths.
- **Darroch's theorem** on the mode (session 7): the index needed is the upper
  central one, where a bound on the mean decides nothing.
- **Termwise absorption in S17** (session 7): `E*` alone leaves the cone.
- **(E″) and (S)** (proposed in session 7, **refuted in session 8**, S21):
  `F = E − xR(T′, ν+e_u)` is not in `C_{j′+2}` for stars with many heavy
  leaves, so a proof of (E) cannot discard `R(T′, ν+e_u)`; the slope
  statement (S) fails already at 5 vertices. The session-7 range (`j ≤ 5`,
  weights ≤ 2) contained no failure: **test auxiliary cone statements on
  stars with heavy leaves (weights ≥ 4) before building on them.**

## Counterexamples and observations

- No counterexample to the Collins–Shor conjecture was found.
- For odd `n` the lower-bound margin is wide; for even `n` it tends to 0.
- For `10 ≤ n ≤ 19` the star minimizes `ρ_k` exactly for `k ≤ ⌊n/2⌋ − 1`.
- The relative margin `1 − d_{m−1}/d_m` behaves like a constant over `n` in
  every family examined (double stars: about `1/n` for even and `3/n` for odd
  order; `K(a,b,c)`: `≈ 0.0024` at order 302). Not proved.
- In every case computed, the tree "skeleton plus one star" with the smallest
  `d_m − d_{m−1}` has the star at a vertex of large degree or central
  position; no rule was extracted.
- `Ω` has non-negative coefficients in all 4,395 rooted weighted trees
  computed (not proved; it would follow from Γ_c).


### The section "Dependency map", as of session 14 (the T10 line already as updated in session 15)


```
Collins–Shor, lower half  (⇔ d_{m−1} < d_m, m = ⌊n/2⌋, by R1 [Lean])
  ODD ORDER, every tree:  T4  ⇐ S25 (Wiener form) ⇐ L1, S24 ⇐ Lemma F   [candidate proof, session 9 (MD-0016)]
  EVERY ORDER, every tree: T6(c)                                          [candidate proof, session 11 (MD-0019)]
    ⇐ (SM): ℓ_T − ℓ_{S_n} ∈ C_{n−1}   (T6(b); also from S36)              [candidate proof]
    ⇐ S23(c) (telescoped leaf recursion) + T6(a) ⇐ T5(i): Ω ∈ K_a          [S23(a)–(c): see obligation 11]
    ⇐ T5: (Γ_c¹), by induction on rooted trees                            [candidate proof]
        ⇐ S19 (plant, merge rules) [AI-reviewed, MD-0015], S33 to S35, Lemma K, Lemma S24
    ⇐ the star: d_{m−1}(S_n) < d_m(S_n)                                   [KNOWN: Collins 1989, Theorem 1]
    ⇐ R1 [Lean], Lemma A(a) [Lean on the cone], log-concavity [Theorem 2.1 of the source]
  routes that are not needed any more: S30(d) and (SM⁺) (now consequences of T5); Γ_c, (E), (Λ) [OPEN];
    inequality (3) of wiener-form.md                                     [FALSE in general: S31]
  the route of sessions 4 to 8 (S1, L4, S4, Property Γ, "skeleton plus one star"; leafy trees only):
    superseded for the lower half; verbatim in notes/gamma-chain.md, last section.
  special cases with complete candidate proofs, both halves, peak exactly m:
    diameter 3: T1;  caterpillars of diameter 4: T2, T3, P_5;  stars: Collins 1989, Theorem 1

Collins–Shor, upper half
  EVERY TREE: T9 [candidate proof, session 13 (MD-0022)]
    ⇐ S41 (peak of d ≤ mode of q) ⇐ S40 (ℓ_T = 4(α − x)q) ⇐ Graham–Lovász, Weyl, Newton
    ⇐ Darroch's rule [KNOWN, 1964] applied to q
    ⇐ S42: μ_q ≤ n − tr(I+L)^{−1} [interlacing; KNOWN in substance: Merris 1990]
    ⇐ T10: tr(I+L_T)^{−1} ≥ tr(I+L_{P_n})^{−1} [KNOWN: AMW 2020, Thm 4.4, via the subdivision (MD-0023)]
        independent proof: S45 (MD-0025) ⇐ S43 (gluing), S43′, S44 (cosh forms; convexity of x/(φ^{2x}+1) on [3, ∞))
    ⇐ S46: tr(I+L_{P_n})^{−1} > n/√5 + 2/5   [proof by Fourier series]
  routes no longer needed:
  ⇐ (PX-peak) + p_max(P_n) ≤ ⌈n − n/√5⌉               [(PX-peak) OPEN (MD-0021); path bound exact for n ≤ 2000]
      ⇐ (PM) + Lemma S39                             [(PM) OPEN; S39 candidate proof (MD-0020)]
  coefficientwise path maximality T8                 [candidate proof; does NOT locate the peak]
  ⇐ Hypothesis A(ii) at k = p_n                      [OPEN; k = 0 proved (L2)]
  ⇐ Collins 1989, Theorem 3: d_{n−k}(P_n) = C(n+k−1, 2k−1)(k−1)n/k; peak of P_n at ⌊n − n/√5⌋ or ⌈n − n/√5⌉
                                                     [read in session 11; the last step of its proof is informal]
  no mechanism from the skeleton expansion           [Property Γ says nothing about it]
```

