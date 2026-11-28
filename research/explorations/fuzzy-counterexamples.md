# Counterexample-driven discovery in fuzzy mathematics

Exploration notes of the campaign started on 2026-11-27 at the director's
request (pause of CJ-0001, new mission: disprove published open conjectures
in fuzzy mathematics by explicit, independently verifiable counterexamples).
When a target becomes an investigation, its record moves to
`research/active/<id>-<slug>/` and this note points there.

## Session 1 — 2026-11-27

- **Entry status:** completed (closed 00:18 on 2026-11-28, about 68 minutes
  after the start; the remaining budget was not needed).
- **Agent / model:** `claude-opus-5-5` (Research Director, Claude Code);
  scouts: three `problem-scout` subagents (Sonnet, per their frontmatter).
  Human participant: the director set the mission and the budget.
- **Mode:** exploration (scouting and selection), switching to focused work on
  the selected target(s).
- **Role(s):** research director, computational experimenter, mathematical
  researcher; scouting delegated.
- **Repository revision at start:** `809cd1d` (branch `research`).
- **Objective:** (1) register 10–20 well-grounded candidate problems in fuzzy
  mathematics (t-norms and relatives, implications, interval-valued and
  type-2 sets, aggregation and fuzzy measures, fuzzy numbers, pairwise
  comparison / AHP); (2) select the most refutable ones and attack them with
  exact search. Exact objectives of the focused part are written below before
  that part starts.
- **Falsification test / stopping conditions:** per target, written before the
  focused work starts.
- **Budget:** 120 minutes from 23:10 (clock reading `date`, local time) to
  01:10; working part ends about 00:50, the rest is reserved for
  verification, documentation and persistence. Scouting: three subagents,
  each capped at about 30 web operations and 25 minutes. Computation: at most
  30 minutes of wall-clock time in total, desktop only, no single run above
  10 minutes. Tokens: unavailable unless reported.

### Checkpoints

- **+20 min (23:30, clock):** Scouting: five `problem-scout` subagents
  (three planned, two added after a low first yield). Yield: few precise
  yes/no problems; most published open problems in the field ask for
  characterisations. Catalogued (status `candidate` unless stated):
  CJ-0016 (Klement–Mesiar 2006, Conjecture 3.2, L_p-Lipschitz t-norms; open
  evidence below the gate), CJ-0017 (Mesiar 2015, n-ary perturbation of
  copulas; transcription suspect, precision below the gate), CJ-0023,
  CJ-0024 (Baczyński–Jayaram problems on the Weber implication), CJ-0025,
  CJ-0026 (Problems 9.3(i), 9.4(iii) of Baczyński–Jayaram 2010, read by the
  director), CJ-0037 (left-continuous t-norms on finite lattices; scout E's
  duplicate CJ-0043 merged into it), CJ-0038 (amalgamation for cancellative
  semilinear residuated lattices). Rejected and resolved problems are listed
  in the scouts' reports, summarised below.
  Focused work on CJ-0024/CJ-0023: explicit families T_c, T'_c (1 < c < 2),
  written proof in
  `research/active/CJ-0024-sn-r-nonborder-intersection/notes/weber-uniqueness.md`
  (candidate, not reviewed); exact grid check
  `experiments/CJ-0024-sn-r-nonborder-intersection/check_examples.py` passed
  (19048 grid pairs, 5 values of c). Running: literature audit, adversarial
  review, Lean formalization (all subagents, background). Next: CJ-0026 with
  the same construction while those run. Commit: this checkpoint.
- **+30 min (23:40, clock):** Literature audit of CJ-0024/CJ-0023 done (no
  answer found within its coverage; 2015 handbook chapter not accessible).
  New: Theorem C (`notes/rescaled-tnorms.md`): every left-continuous t-norm
  with strong natural negation, rescaled into [0,a] with a above the fixed
  point and closed by the drastic boundary, gives an (S,N)- and QL-residual
  outside the left-continuous class; a below the fixed point gives I_WB.
  Exact grid check `check_theorem_c.py`: 30 configurations passed
  (candidate, not reviewed). Registered MD-0027, MD-0028 (Theorems A, B,
  candidate counterexamples) and MD-0029 (Theorem C, candidate proof).
  CJ-0016: a 2007 characterisation by Mesiarová(-Zemánková) probably decides
  it (abstract only). Running: review of the first note, review of Theorem C,
  Lean formalization of Theorem A. Computation used: about 4 minutes.
- **+42 min (23:52, clock):** Review 1 of the CJ-0024 note (Opus, fresh
  context): theorems hold, gaps G1–G5 in side claims; revision 2 written
  (revision 1 kept); recheck of revision 2 by claude-sonnet-5-5 (Fable was
  refused: monthly spend limit): no gap found within stated scope. Found
  while answering G3: the printed Theorem 6.5 of the 2008 survey misses a
  hypothesis (its own Remark 6.4(i) contradicts it) — an erratum, not a
  result. Manuscript draft `manuscripts/CJ-0024-weber-uniqueness/main.tex`
  (4 pages, compiles). CJ-0025/CJ-0026: observations only (STATE.md).
  Running: Lean (Theorems A, B), review of Theorem C.
- **Correction (23:50, clock):** the time "23:52" in the previous checkpoint
  was written without reading the clock; that checkpoint was written at about
  23:47. Since then: MD-0027's registry statement corrected to the strong
  reading of Problem 4.5(ii) and the recheck bound to MD-0027/MD-0028
  (`a956225`); campaign 2 recorded in `research/scouting-log.md`.
- **+55 min (00:05, clock):** Theorem C review: no gap found (same model as
  the author; independent checks with three further base t-norms). Second
  target CJ-0017 (Mesiar 2015, Problem 4.1), started about 23:52: for the
  product copula, C − ∏(x_i − C) is not an n-copula for n = 3 (exact box,
  volume −23/5⁹, two independent methods), for every even n ≥ 4 (corner
  density 1 − (−1)ⁿ·D_n, D_n derangements; proof written) and for n = 5, 7
  (exact); the 3-dimensional family Π − λ∏(x_i − Π) is a copula iff
  −1/3 ≤ λ ≤ 15/19 (hand proof). Literature audit: no answer found, but
  Fernández-Sánchez–Úbeda-Flores (FSS 354, 2019) — closed access, may contain
  these results — not read; and the literal first question is already
  answered at n = 2 by W (auditor's observation). Registered MD-0030
  (candidate counterexample), MD-0031 (candidate proof); CJ-0017
  `partial-result`. Running: Lean (CJ-0024), review of the CJ-0017 note.
  Computation used so far: about 13 minutes (z3 run 4 min).
- **Correction:** the previous checkpoint was written at 00:02 (clock), not
  00:05; elapsed time +53 min.

### What was done

- Scouting (five `problem-scout` subagents) and catalogue registration of
  eight candidates; campaign record in `research/scouting-log.md`
  (Campaign 2), with the problems found resolved or rejected.
- **CJ-0024 / CJ-0023** (Baczyński–Jayaram 2013, Problems 4.2 and 4.5(ii);
  2008 monograph Problem 4.8.1; 2010 Problem 9.4(ii)): primary sources read
  (2013 chapter, 2010 paper, 2008 survey, EUSFLAT 2011); explicit families
  (Theorems A, B) and a general construction (Theorem C) found and proved;
  exact rational grid checks (`check_examples.py`: 5 values of c, 19,048
  pairs; `check_theorem_c.py`: 30 configurations); literature audit; review of
  revision 1 (Opus: gaps G1–G5 in side claims), revision 2, recheck (Sonnet:
  no gap found), review of Theorem C (Opus: no gap found); Lean
  formalization of Theorems A and B (25 theorems, `verify_lean.py` passed);
  manuscript draft `manuscripts/CJ-0024-weber-uniqueness/main.tex` (4 pages).
- **CJ-0017** (Mesiar 2015, Problem 4.1): exact computations
  (`experiments/CJ-0017-nary-copula-perturbation/`), note with
  Propositions 1–4, literature audit, review (Sonnet: no gap found).
- CJ-0025, CJ-0026 (Problems 9.3(i), 9.4(iii) of 2010): analysis only, notes
  in the dossiers and in the CJ-0024 STATE.md.

### Findings

- MD-0027, MD-0028 (candidate counterexamples; one review with gaps, then a
  recheck by a different model with no gap; Lean: theorem items formalized,
  statement comparison not independent): for 1 < c < 2 the t-norms T_c
  (shifted Łukasiewicz) and T'_c (threshold nilpotent minimum), closed by the
  drastic boundary, are non-border-continuous and have residuals that are
  (S,N)- and QL-implications, violate (OP), and differ from I_WB. This
  answers Problem 4.2(i) of the 2013 chapter (yes), refutes the equality of
  Problem 4.8.1 of the 2008 monograph, and answers the first question of
  Problem 4.5(ii) negatively under the strong reading (the literal reading
  is already answered in the sources by the Fodor implication).
- MD-0029 (candidate proof; one review, same model, no gap): Theorem C, the
  general rescaling construction for every left-continuous t-norm with
  strong natural negation; the Weber implication is its degenerate case.
- MD-0030 (candidate counterexample; one review by a different model, no
  gap): for C = Π, C − ∏(x_i − C) is not an n-copula for n = 3 (exact box,
  volume −23/5⁹), n = 5, 7, and every even n ≥ 4 (corner density
  1 − (−1)ⁿD_n, D_n derangements); n = 9 computed afterwards (not in the
  reviewed note).
- MD-0031 (candidate proof; same review): Π − λ∏(x_i − Π) is a 3-copula iff
  −1/3 ≤ λ ≤ 15/19.
- Observation (not a result): Theorem 6.5 of the 2008 survey, as printed,
  lacks a hypothesis (left-continuity of T); its own Remark 6.4(i) shows it.
- Novelty of all of the above: `preliminary-search-completed` only. The 2015
  handbook chapter (Baczyński, Jayaram, Massanet, Torrens) and the 2008
  monograph (CJ-0024), and Fernández-Sánchez–Úbeda-Flores, FSS 354 (2019)
  (CJ-0017), were not accessible and may contain these results.

### What failed

- Scouting yield: eight candidates, short of the 10–20 aimed at; most open
  problems found ask for characterisations.
- Fable model unavailable (monthly spend limit); the recheck ran on Sonnet.
- z3 could not decide the bound min d_3 ≥ −4/15 in 120 s per query (4 min
  spent); the bound was proved by hand instead.
- CJ-0025 / CJ-0026: no counterexample found; the local analysis suggests
  Problem 9.4(iii) may have a positive answer.
- Director's errors, corrected in the record: a wrong objection to the
  CJ-0017 transcription (margin conditions); two journal times written before
  reading the clock; registry evidence committed once in invalid form
  (fixed in `a956225`); an in-progress Lean file swept into checkpoint
  commits `e23d59c`, `88d33c6` (completed and verified in `f5de051`).

- **Lean, end of session:** `verify_lean.py` rerun on commit `f5de051`:
  passed, receipt `verification/receipts/20261128T031635Z-f5de051aad-dirty-passed.json`
  (marked dirty because non-Lean records were edited during the run; the Lean
  sources are those of `f5de051`; `tests/test_lean_scan.py` passes against
  it). Independent comparison of the 25 Lean statements with the note
  (claude-sonnet-5-5, `reviews/2026-11-28-lean-statement-review.md`):
  statements match within stated scope, with qualifications F1–F4.

### Telemetry

| Item | Value |
| --- | --- |
| Model | `claude-opus-5-5` (director); subagents: `problem-scout` ×5 (Sonnet); `literature-auditor` ×2 (Opus); `adversarial-reviewer` ×5 (Opus ×2, Sonnet ×3; one Fable attempt refused by the spend limit); `formalization-agent` ×1 (Opus) |
| Subagent tokens (reported by the environment) | scouts 131,897 / 78,525 / 71,015 / 76,474 / 93,238; auditors 146,286 / 87,326; reviewers 178,694 (rev. 1), 145,546 (Theorem C), 69,094 (recheck), 48,471 (CJ-0017), 83,569 (Lean statements); formalization 168,529; Fable attempt unavailable |
| Main-session token usage | unavailable |
| Computation wall-clock | research computations about 11 min (grid checks 0.8 + 2.75 min, copula scripts about 3 min, z3 4 min); verification runs about 24 min (two `verify_lean.py` runs of about 11 min each, pytest about 1.5 min). Together about 35 min, above the 30-minute computation line of the budget because the verification runs were counted in it; recorded, not hidden. |
| Research iterations | 2 targets attacked (CJ-0024/CJ-0023, CJ-0017); 2 analysed without result (CJ-0025, CJ-0026) |
| Proof attempts | Theorems A, B, C; Propositions 1–4 (CJ-0017) |
| Counterexamples found | families I_c, J_c (and Theorem C); Π-perturbation boxes/points for n = 3, 5, 7, 9 and even n ≥ 4 |
| Formalization attempts | 1 (Theorems A, B: 25 theorems, passed) |
| Successful verifications | exact grid checks (2 scripts), independent checks by four reviewers, `verify_lean.py` ×2 passed, pytest non-Lean suite passed |
| Cost estimate and assumptions | unavailable |

### Outcome and next step

Completed. Two published open problems of Baczyński and Jayaram (2013,
Problems 4.2(i) and, under its strong reading, 4.5(ii); 2008 Problem 4.8.1)
have candidate answers by explicit counterexamples, with written proofs, exact
checks, AI reviews by two models, a literature audit and a Lean formalization
of the theorem items; a general construction (Theorem C) is reviewed once.
For Mesiar's 2015 Problem 4.1 the product copula is shown not to admit the
higher-dimensional extension (n = 3, 5, 7, 9, all even n ≥ 4), with the exact
parameter range for n = 3. Nothing is promoted: novelty rests on searches that
could not reach the 2015 handbook chapter, the 2008 monograph and the 2019
Fernández-Sánchez–Úbeda-Flores paper, and no human has read the proofs.

Next steps, in order: (1) the director decides on `external_review`
(`ai-reviewed` is now permitted for CJ-0024/CJ-0023 and CJ-0017 by skill
`review-claim`, step 5); (2) obtain and read the three inaccessible sources
(see the STATE.md files); (3) if they do not contain the results, assemble the
CJ-0024 result package from `manuscripts/CJ-0024-weber-uniqueness/main.tex`
after a whole-manuscript review; (4) mathematics: CJ-0026 (a proof that
(I_QL ∩ I_T) \ I_{S,N} = ∅ may be within reach), odd n ≥ 11 for CJ-0017.
