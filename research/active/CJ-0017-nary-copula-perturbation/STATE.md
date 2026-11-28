# CJ-0017 — Mesiar's Problem 4.1 (n-ary perturbation C − ∏(x_i − C)) — investigation state

Last updated: 2026-11-28 (session 1, about 00:05).

## Exact statement

Mesiar, Stupňanová, Fuzzy Sets Syst. 261 (2015) 112–123, Problem 4.1, p. 114
(verbatim in `research/candidates/CJ-0017-nary-copula-perturbation.md`): for an
n-copula C, C_1 = C − ∏_{i=1}^n (x_i − C). "Is the function C_1 n-increasing,
i.e., is it an n-copula? If in general not, characterize all n-copulas C such
that C_1 is an n-copula, too."

## Definitions and conventions

n-copula as in Definition 4.1 of the source (n-increasing plus boundary
conditions). C_1 always satisfies the boundary conditions.

## Status

Catalogue: mathematical `partial-result`; formal `not-started`; novelty
`unknown`; external review `not-reviewed`.

## Established results

| ID | Statement | Level | Evidence |
| --- | --- | --- | --- |
| O1 | Literal first question: no, already at n = 2 (C = W gives C_1 = −xy for x + y < 1). | trivial; observation of the literature auditor | audit file |
| P1 | C = Π, n = 3: V_{C_1}([3/5,4/5]×[4/5,1]²) = −23/5⁹. | exact computation, two independent methods | note §3; `box_search.py`, `independent_check.py` |
| P2 | C = Π: d_n(1,…,1) = 1 − (−1)ⁿ·D_n (derangements); not an n-copula for even n ≥ 4. | candidate proof; exact check n ≤ 8 | note §3; `edge_density.py` |
| P3 | C = Π, n = 5, 7: negative density at explicit rational points. | exact computation | `edge_density.py` |
| P4 | C = Π, n = 3: D_λ = Π − λ∏(x_i − Π) is a 3-copula iff −1/3 ≤ λ ≤ 15/19. | candidate proof (case analysis); floating grid agrees | note §3 |

## Failed approaches and refuted hypotheses

- z3 (nlsat) could not decide min d_3 ≥ −4/15 within 120 s per query.
- Director's error, corrected: the session first thought the transcription
  violated the margin conditions for n ≥ 3; it does not (only univariate
  margins are required).

## Counterexamples and observations

C = M: C_1 = M. For n = 2, C = Π gives FGM(−1).

## Dependency map

P4 ← min/max of d_3 (hand proof); P1–P3 independent of each other.

## Decisions

2026-11-27/28 (session 1): worked on as a second target of the fuzzy campaign.

## Open obligations

1. Review of `notes/product-copula.md` revision 1 (running; `reviews/`).
2. **Read Fernández-Sánchez, Úbeda-Flores, Fuzzy Sets Syst. 354 (2019)
   116–122** (doi:10.1016/j.fss.2018.06.013, closed access): it may already
   contain P1–P4. Also the leads listed in the audit file.
3. Odd n ≥ 9 for Π; λ-range for n ≥ 4.

## Remaining obstacles

The characterisation of all C with C_1 an n-copula.

## Next step

Obtain and read the 2019 Fernández-Sánchez–Úbeda-Flores paper (obligation 2)
before any further work; if it does not contain P2, prove the odd case.

## Sources

- <http://library.utia.cas.cz/separaty/2019/E/mesiar-0506948.pdf>
