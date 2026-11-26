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
