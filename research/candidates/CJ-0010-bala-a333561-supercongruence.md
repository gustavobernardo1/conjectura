# CJ-0010 — Bala's supercongruence conjecture for OEIS A333561

*Compiled 2026-11-26 from the record of a literature-scout subagent (Claude, model `claude-fable-5-2`), lightly reformatted. It is a preliminary dossier: it has not been independently audited, and every item under “Unverified items” must be checked before it is relied upon.*

## Statement

OEIS A333561, verbatim: 'a(n) = Sum_{j = 0..2*n} binomial(n+j-1,j)*2^j.' ... 'We conjecture that this sequence satisfies the supercongruences a(n*p^k) == a(n*p^(k-1)) ( mod p^(3*k) ) for prime p >= 5 and positive integers n and k. Some examples are given below.'
In LaTeX: with $a(n)=\sum_{j=0}^{2n}\binom{n+j-1}{j}2^j$ ($a(0)=1$; 1, 7, 129, 2815, 65537, 1579007, ...), for every prime $p\ge 5$ and all integers $n,k\ge 1$: $a(np^k)\equiv a(np^{k-1}) \pmod{p^{3k}}$.
Sibling (OEIS A333565, verbatim): 'O.g.f.: (1 + 4*x)/((1 + x)*sqrt(1 - 8*x)).' ... 'We conjecture that this sequence satisfies the stronger congruences a(n*p^k) == a(n*p^(k-1)) ( mod p^(3*k) ) for prime p >= 3 and positive integers n and k. The particular case when n = k = 1 follows from the corresponding result for A333564.'
Further unproved claims in the A333561 entry (easier side targets): 'Conjectural o.g.f.: 1/(1 + x) + 8*x*f'(4*x)/(2*f(4*x) - 1), where f(x) = 1 + x + 3*x^2 + 12*x^3 + 55*x^4 + ... is the o.g.f. of A001764.' and 'exp( Sum_{n >= 1} a(n)*x^n/n ) = 1 + 7*x + 89*x^2 + 1447*x^3 + ... appears to be the o.g.f. of A062747.'

**Source.** P. Bala, comment in OEIS entry A333561 (entry created 27 March 2020; revision 33 of 29 October 2026 read). <https://oeis.org/A333561>

**Statement checked against:** primary-source. Quoted verbatim from the OEIS entry.

## Definitions and hypotheses

p prime, p >= 5 (A333561) resp. p >= 3 (A333565); n >= 1 and k >= 1 integers; modulus is p^(3k), not p^3. binomial(n+j-1,j) with n >= 1 (a(0)=1 by convention; index 0 is not used by the conjecture since n >= 1). Equivalent expressions stated in the same OEIS entry (Bala, 2022 and Aug 15 2026; Luschny 2022): a(n) = Sum_{k=0..2n} binomial(3n,2n-k)*binomial(n+k-1,k) = [x^(2n)] ((1+x)^3/(1-x))^n = Sum_{k=0..2n} (-2)^k*binomial(3n,k) = binomial(3n,2n)*hypergeom([-2n,n],[n+1],-1). For A333565: a(n) = 2^n*binomial(2n,n) + 3*Sum_{k=0..n-1} (-1)^(n+k+1)*2^k*binomial(2k,k) = 2*A119259(n) - (-1)^n, where A119259(n) = Sum_{j=0..n} binomial(n+j-1,j)*2^j. Easy to get wrong: (1) p = 2, 3 are excluded for A333561 and p = 2 for A333565 (in this session p = 2 visibly fails for A333565, e.g. v_2(a(2)-a(1)) = 1 < 3); (2) the family A333560 (columns r: Sum_{j=0..r*n}) has one conjecture per column - A333561 is column 2, A333562 column 3.

## Known partial results

- For A333565 the weaker Gauss congruences a(n*p^k) == a(n*p^(k-1)) (mod p^k) hold for all primes p, because exp(Sum a(n)x^n/n) has integer coefficients (Stanley, EC2, Ex. 5.2(a)); the entry also lists 'a(p) == 7 (mod p^3) for all prime p >= 3' and says the case n = k = 1 follows from the corresponding result for A333564. — OEIS A333565 comments/formulas (P. Bala, Apr 11 2020) <https://oeis.org/A333565> (source fetched)
- Closed forms, algebraic equation for the o.g.f. ((108x^3+212x^2+100x-4)A^3 - (216x^2+208x-8)A^2 + (48x^2+155x-5)A + 8x^2-40x+1 = 0) and a second-order P-recurrence (Kotesovec) for A333561; examples a(11)-a(1) == 0 (mod 11^3), a(21)-a(3) == 0 (mod 7^3) [actually divisible by 7^5], a(25)-a(5) == 0 (mod 5^6). — OEIS A333561 formulas and examples <https://oeis.org/A333561> (source fetched)
- A different Bala supercongruence conjecture (A277060: a(p-1) == 1 mod p^4, a(p^2-1) == 1 mod p^5) was recorded as proved in OEIS on Sep 21 2026 (A. R. Epstein, 'Proof of a conjecture in A277060'), showing that this class is attackable and that OEIS editors are recording such proofs. — OEIS A277060 comments <https://oeis.org/A277060> (source fetched)
- Sanity check run in this session (exact integer arithmetic, Python): no violation for A333561 with p in {5,7,11,13} and for A333565 with p in {3,5,7,11,13}, all n <= 6, k <= 3 with n*p^k <= 900; the exponent 3k is attained exactly in several cases (so it cannot be raised in general). — own computation, scratchpad/scripts/check1.py <> (source not fetched)

## Relevant literature

- P. Bala, comment in OEIS entry A333561 (entry created 27 March 2020; revision 33 of 29 October 2026 read). <https://oeis.org/A333561>
- OEIS A333565 comments/formulas (P. Bala, Apr 11 2020) <https://oeis.org/A333565>
- OEIS A333561 formulas and examples <https://oeis.org/A333561>
- OEIS A277060 comments <https://oeis.org/A277060>
- own computation, scratchpad/scripts/check1.py <>

## Open-status evidence

- Most recent source: OEIS A333561, revision #33 dated Oct 29 2026: the conjecture is still displayed with no proof or reference, although P. Bala added new formulas dated Aug 15 2026. OEIS Open results (data generated 2026-09-16): conjecture id 'oeis_333561_conjecture' had 4 attempts (Claude Opus 4.8, GPT-5.5, Gemini 3.5 Flash, Gemini 3.1 Pro at $50 each), none accepted; same for A333562 and A333565.
- URL: <https://oeis.org/A333561>
- Date: 2026-10-29 (OEIS revision); 2026-09-16 (benchmark data)
- Content: 'We conjecture that this sequence satisfies the supercongruences a(n*p^k) == a(n*p^(k-1)) ( mod p^(3*k) ) for prime p >= 5 and positive integers n and k.' (still present, no 'proved' note)

This is evidence that the statement was regarded as open at the stated date. It is not proof that no resolution exists.

## Novelty search coverage and limitations

Queries run:

- supercongruence a(n p^k) ≡ a(n p^(k-1)) (mod p^(3k)) Peter Bala conjecture OEIS proof 2025 OR 2026 "[x^n]" OR "Taylor polynomial" OR A333561 OR A333565
- arXiv API: abs:supercongruence AND (abs:OEIS OR abs:Bala OR abs:Gauss), sorted by date (1 irrelevant hit)
- local grep of solved-conjectures CONTENTS.md for 'Bala', 'supercongruence', 'A333561', 'A333565' (no hit)

Sources checked:

- OEIS entry text, fetched 2026-11-26 via https://oeis.org/search?q=id:<A-number>&fmt=text
- OEIS Open results explorer data https://tadamcz.com/oeis-open/results.json (generatedAt 2026-09-16; 3468 attempts by 2026 frontier models on 492 Lean-formalized OEIS conjectures, 170 resolved) and paper abstract https://arxiv.org/abs/2608.11941 (Adamczewski, 12-13 Aug 2026)
- GitHub epoch-research/LeanOpenProblems-results (README, metadata/oeis/conjectures.json, Submission/Spec.lean of the relevant sample)
- GitHub 1337isnot1337/solved-conjectures: README.md and CONTENTS.md (451 lines, fetched 2026-11-26) searched locally for the author name, A-number and key words; no match
- OEIS A333565 (revision #19, Oct 06 2021)
- OEIS A277060

Limitations: Budget-limited search (about 35 web operations for all candidates together). WebSearch is US-only and returns summaries; MathOverflow, MathSciNet, zbMATH, Google Scholar citation lists and the seqfan mailing list were NOT searched. An unsuccessful search does not establish that the statement is open or that partial results below are the only ones. Warning from this session: the OEIS Open 'open conjecture' list itself contains stale items (A001818, A053175, A296056, A277060 were already proved), so benchmark membership alone is not evidence of openness. General theorems on supercongruences for coefficients [x^{rn}]G(x)^n or for constant terms of powers of Laurent polynomials may already imply this conjecture; that literature was not searched systematically.

## Computational approaches

Exact: a(N) via the binomial sum, via Sum_{k<=2N} (-2)^k C(3N,k), or via the order-2 P-recurrence modulo p^(3k+c); compute v_p(a(n p^k) - a(n p^(k-1))) for all p < 100, k <= 3, n up to 10^3-10^4 on a desktop. Largest cases displayed in the literature found: the three OEIS examples (N = 11, 21, 25). Also test the whole A333560 array (columns r = 1..6) and record the exact valuation excess to guess the sharp statement; test the conjectural o.g.f. to several hundred terms and then prove it from the stated algebraic equation (routine elimination / Lagrange inversion).

## Mathematical approaches

(1) Write a(n) = [x^(2n)]((1+x)^3/(1-x))^n = constant term of Lambda^n with Lambda = (1+x)^3/(x^2(1-x)); Gauss congruences mod p^k then follow from integrality of exp(Sum a(n)x^n/n) and the task is the two extra powers of p. (2) Termwise approach used for Apery-like sequences: split Sum_{k} (-2)^k C(3n p^k, k) (or the double-binomial form) into indices divisible by p and the rest; apply Jacobsthal-Kazandzidis/Ljunggren congruences C(pa,pb) == C(a,b) (mod p^3) to the first part and show the second part vanishes mod p^(3k) using Wolstenholme-type harmonic sum congruences and a symmetry pairing. (3) For A333565 start from the explicit algebraic g.f. (1+4x)/((1+x)sqrt(1-8x)) and the formula 2^n C(2n,n) + 3*Sum(...): the case n = k = 1 needs the Fermat-quotient cancellation between 2^p and the partial sum, which already shows the mechanism. (4) Induction on k via a Dwork-type congruence a(np^k)/a(np^(k-1)) once k = 1 is done for all n. (5) Prove first the case k = 1, n arbitrary (mod p^3), then k arbitrary. The conjectural o.g.f. and the A062747 identity are plausible warm-up theorems.

Scout's tractability assessment: Best 'full proof plausible' candidate of this list: fully explicit, three equivalent closed forms, the technique family (supercongruences a(mp) == a(m) mod p^3 for Apery-like numbers) is well developed, and the smallest case n = k = 1 should be a one-page exercise. Realistic outcome for a small team: proof of k = 1 for all n, probably the full statement for A333565 (column 1, simplest), and the side conjectures (o.g.f., A062747). Honest caveats: four frontier-model attempts at $50 each failed in Aug 2026 (so it is not a one-shot exercise); nobody appears to have published on it, so 'tried to death' does not apply, but a general theorem in the literature might already cover it - check before investing.

## Formalization feasibility

Statement is elementary in Lean 4/Mathlib: Finset.sum, Nat.choose, Nat.Prime, Nat.ModEq. A Lean 4 statement already exists (theorem 'oeis_333561_conjecture' in the OEIS Open / FormalConjectures-style Spec.lean, fetched from epoch-research/LeanOpenProblems-results; it uses the equivalent definition Sum_{k<=2n} C(3n,2n-k) C(n+k-1,k)). A proof would need p-adic binomial congruences (Jacobsthal/Ljunggren, Wolstenholme harmonic sums); whether current Mathlib has these was not checked.

## Prerequisites

p-adic valuation, Lucas and Kummer theorems, Wolstenholme/Ljunggren/Jacobsthal binomial congruences, Fermat quotients, generating functions and Lagrange inversion, Gauss (Dold) congruences, creative telescoping (Zeilberger) for recurrences.

## Unverified items

- The date on which Bala added the supercongruence comment (the OEIS line is unsigned); 2020-03-27 is the entry creation date and the OEIS Open metadata date.
- Exact statements for the siblings A333562, A333095, A333096, A003161, A003162, A212334, A079727 are known here only through the OEIS Open metadata paraphrases (their OEIS pages were not fetched).
- Whether an existing general theorem (e.g. on supercongruences for constant terms / diagonal coefficients) already implies the conjecture.
- Stanley EC2 Ex. 5.2(a) reference is quoted from the OEIS entry, not checked in the book.
