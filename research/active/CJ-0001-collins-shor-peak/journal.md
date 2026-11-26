# CJ-0001 — journal

Append-only. One entry per session. Current truth is in `STATE.md`.

## Session 1 — 2026-11-26

- **Agent / model:** Claude, model `claude-fable-5-2`, in Claude Code. No human
  mathematical input during the session; the session was started by the project
  director's initialization request.
- **Role(s):** Research Director, Literature Auditor (statement only),
  Computational Experimenter, Mathematical Researcher.
- **Repository revision at start:** none (the session created the repository).
- **Objective (exact):** (1) fix the exact statement of the Collins–Shor
  conjecture from a primary source; (2) reproduce the published exhaustive
  verification for trees of order at most 20 with exact arithmetic and an
  independent check; (3) extend it beyond order 20; (4) look for structure that
  suggests a provable intermediate statement, and try to break whatever is found.
- **Approach:** exact integer characteristic polynomials of distance matrices
  over all trees of each order; comparison of every tree with the star and the
  path; exact formulas for structured families at large orders.
- **Falsification test:** any tree with a maximizing index outside
  `[⌊n/2⌋, ⌈n − n/√5⌉]`; and, for each sharper hypothesis, sampled and structured
  trees beyond the exhaustive range.
- **Stopping conditions:** stop the exhaustive search at order 23; stop the
  session once the state is recorded with a concrete next objective.
- **Budget:** 30 minutes of computation; one session.

### What was done

All computations use exact integer or rational arithmetic. Commands are run from
the repository root with `uv run python`.

1. Statement: downloaded the TeX source of arXiv:1507.02341 and read
   Conjecture 1.2 and its context. One web search for later work.
2. `tests/test_cj0001_distpoly.py`: 87 tests pass — tree counts against OEIS
   A000055 (orders 1–12), pairwise non-isomorphism by an independent canonical
   form (orders 2–10), agreement of the main computation with an independent
   Laplacian-based method on every tree of order 3–9, Graham–Pollak and the
   formula for `d_{n−2}` on every tree of order 3–11, the star's peak for orders
   3–40, the `d_1` formula, and the order-20 refutation by both methods.
3. `exhaustive.py --min-order 3 --max-order 20 --workers 7`: 1,346,022 trees,
   0 violations, 0 guard failures, counts match (90 s).
4. `exhaustive.py --min-order 21 --max-order 23 --workers 7`: 22,596,335 trees,
   0 violations, 0 guard failures, counts match (2,014 s).
5. `ratio_extremality.py exhaustive` for orders 4–17 and 18–20: Hypothesis A(ii)
   holds on all 1,346,021 trees; Hypothesis A(i) holds through order 19 and
   fails for 10 trees of order 20 (109 s in total).
6. `ratio_extremality.py sampled --orders 24 30 40 60 90 --samples 400 --seed
   20261126`: 10,000 trees; 0 violations of A(ii) and of the conjecture; 108
   violations of A(i), all in the caterpillar and preferential-attachment
   models (109 s).
7. `near_star_families.py`: double stars against the star for even orders
   6–40; balanced caterpillars at orders 10³ to 10⁶ through the quotient-matrix
   formula (111 s).

### Findings

See `STATE.md` for the precise statements and evidence levels: E1–E4 (exhaustive
verification through order 23), R1 and L1–L3 (short proofs, unreviewed),
Hypothesis A(ii) (open, supported), Hypothesis A(i) (refuted at order 20 by the
double star `S(9,9)`), Questions Q1 and Q2.

### What failed

- Hypothesis A(i): refuted (recorded in `STATE.md`).
- A first version of `near_star_families.py` used full binomial coefficients and
  did not finish at order 10⁶ within ten minutes; it was stopped and rewritten
  with exact binomial ratios. No result of the first version was used.
- The 30-minute computation budget was exceeded: about 41 minutes of recorded
  computation, because the order-23 run (23 minutes) was allowed to finish.
- Not done: reading Collins (1989) and Graham–Lovász (1978); any independent
  review; any formalization.

### Telemetry

| Item | Value |
| --- | --- |
| Model | `claude-fable-5-2` |
| Computation wall-clock | about 2,430 s recorded by the scripts (7 worker processes for the exhaustive runs; Intel Core i7-7700, 16 GB RAM, Windows 10) |
| Token usage | unavailable (not reported to the agent for the main session) |
| Research iterations | 1 session |
| Proof attempts | 4 short lemmas written (R1, L1, L2, L3); none reviewed |
| Counterexamples found | 0 to the conjecture; 1 family refuting Hypothesis A(i) |
| Formalization attempts | 0 |
| Successful verifications | 87 tests; 2 exhaustive runs; cross-check by an independent method |
| Cost estimate and assumptions | unavailable |

### Outcome and next step

Durable contributions: reproducible exhaustive verification through order 23;
a refuted natural hypothesis with an explicit counterexample; an open sharper
hypothesis for the upper bound; a concrete provable-looking objective (O1 in
`STATE.md`: the lower bound for double stars), to be preceded by a literature
audit of Collins (1989) and arXiv:2206.07561.
