# Counterexample-driven discovery in fuzzy mathematics

Exploration notes of the campaign started on 2026-11-27 at the director's
request (pause of CJ-0001, new mission: disprove published open conjectures
in fuzzy mathematics by explicit, independently verifiable counterexamples).
When a target becomes an investigation, its record moves to
`research/active/<id>-<slug>/` and this note points there.

## Session 1 — 2026-11-27

- **Entry status:** in progress.
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
