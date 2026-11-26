# CJ-0012 — Kellner's conjectures on denominators of Bernoulli polynomials

*Compiled 2026-11-26 from the record of a literature-scout subagent (Claude, model `claude-fable-5-2`), lightly reformatted. It is a preliminary dossier: it has not been independently audited, and every item under “Unverified items” must be checked before it is relied upon.*

## Statement

Notation: s_p(n) = sum of the base-p digits of n; rad = radical. Let $D_n^+ := \prod_{p>\sqrt n,\ s_p(n)\ge p} p$ (p prime, n >= 1).
Conjecture 2(i) (Kellner 2017, as restated in 2023): 'We have D_n^+ > 1, respectively, omega(D_n^+) > 0 for n > 192.'
Conjecture 1: with S := {1, 2, 4, 6, 10, 12, 28, 30, 36, 60} and $\bar S := \{n\ge 1 : B_n'(x)\in\mathbb Z[x]\}$ (B_n(x) the Bernoulli polynomials): '(i) The set \bar S is finite. (ii) We have \bar S = S.' Part (i) is now a theorem; part (ii) is open.
Conjecture 11: with $\bar R := \{n\ge 1 : \mathrm{denom}(B_n(x)-B_n) = \mathrm{rad}(n+1)\}$ and R := {3, 5, 8, 9, 11, 27, 29, 35, 59}: 'We have \bar R = R.' (This is the form recorded in OEIS A195441: 'It is conjectured that S = {3, 5, 8, 9, 11, 27, 29, 35, 59} is the full set of all such solutions' of a(n-1) = rad(n+1).)
Logical relations proved in the paper: Conjecture 2(i) implies Conjecture 1(ii) (Theorem 3); Conjecture 11 restricted to odd n implies Conjecture 1 (Theorem 12).

**Source.** B. C. Kellner, On the finiteness of Bernoulli polynomials whose derivative has only integral coefficients, J. Integer Seq. 27 (2024), Article 24.2.8, arXiv:2310.01325v2, Conjectures 1(ii), 2(i) and 11; Conjecture 2 originates in B. C. Kellner, J. Number Theory 179 (2017) 126-141. <https://arxiv.org/abs/2310.01325>

**Statement checked against:** primary-source. Quoted from the fetched arXiv version of the 2024 paper.

## Definitions and hypotheses

In D_n^+ the product runs over primes p > sqrt(n) (the square-root sign is lost in the text extraction I used but is confirmed by my computation: with p > sqrt(n) the set {n : D_n^+ = 1} for n <= 20000 is exactly {1,2,4,6,10,11,12,15,16,28,29,30,35,36,58,59,60,69,70,78,79,80,174,190,191,192}, matching the bound 192). denom(B_n(x)-B_n) = OEIS A195441(n-1) = product of all primes p with s_p(n) >= p (Kellner-Sondow; in A195441's indexing: primes p <= (n+2)/(2+(n mod 2)) with s_p(n+1) >= p). B_n'(x) = n B_{n-1}(x). The three denominators denom(B_n), denom(B_n(x)-B_n), denom(B_n(x)) carry different typographic decorations of 'D_n' in the paper; the decorations are lost in my text extraction - re-read the PDF before formalizing. Elementary reformulation derived in this session (verified by program for n <= 6000, not taken from the paper): D_n^+ > 1 iff there are a prime p > sqrt(n) and integers k >= 2, 1 <= j <= k-1 with n + j = k*p; i.e. some integer m in (n, n+sqrt(n)) has a prime factor p > sqrt(n) whose cofactor m/p exceeds m - n.

## Known partial results

- Finiteness: Conjecture 2(ii) (omega(D_n^+) ~ kappa*sqrt(n)/log n) was proved with kappa = 2 for n > n_0 by Bordelles, Luca, Moree, Shparlinski (Mathematika 64 (2018), 519-541, Cor. 1.6), hence \bar S and \bar R are finite (Corollary 4, Theorem 10). 'Unfortunately, their methods do not lead to an explicit or computable bound n_0.' — Kellner, arXiv:2310.01325v2, Corollary 4 and surrounding text <https://arxiv.org/abs/2310.01325> (source fetched)
- Theorem 5: (i) if n in \bar S then n+1 is prime; (ii) if \bar S != S and n in \bar S \ S, then n > 10^7. Theorem 9: B_n'(x) in Z[x] iff denom(B_{n-1}(x)-B_{n-1}) = rad(n). Theorem 10: if n in \bar R then n+1 is composite; \bar R is finite. — Kellner, arXiv:2310.01325v2 <https://arxiv.org/abs/2310.01325> (source fetched)
- OEIS A195441 (revision of Nov 09 2026) formulas by Kellner: a(n-1) = lcm(a(n), rad(n+1)) for odd n >= 3; if n+1 is composite then rad(n+1) divides a(n-1). — OEIS A195441 <https://oeis.org/A195441> (source fetched)
- Reproduced in this session: \bar S restricted to [1, 20000] = S; \bar R restricted to [1, 5000] = R; D_n^+ > 1 for 192 < n <= 20000. — own computation, scratchpad/scripts/check2.py and check6.py <> (source not fetched)

## Relevant literature

- B. C. Kellner, On the finiteness of Bernoulli polynomials whose derivative has only integral coefficients, J. Integer Seq. 27 (2024), Article 24.2.8, arXiv:2310.01325v2, Conjectures 1(ii), 2(i) and 11; Conjecture 2 originates in B. C. Kellner, J. Number Theory 179 (2017) 126-141. <https://arxiv.org/abs/2310.01325>
- Kellner, arXiv:2310.01325v2, Corollary 4 and surrounding text <https://arxiv.org/abs/2310.01325>
- Kellner, arXiv:2310.01325v2 <https://arxiv.org/abs/2310.01325>
- OEIS A195441 <https://oeis.org/A195441>
- own computation, scratchpad/scripts/check2.py and check6.py <>

## Open-status evidence

- Most recent source: Kellner, J. Integer Seq. 27 (2024) / arXiv:2310.01325v2 (29 Feb 2024); OEIS A195441 revision of Nov 09 2026 still says 'It is conjectured that S = {3, 5, 8, 9, 11, 27, 29, 35, 59} is the full set'; OEIS Open data (2026-09-16): 'oeis_a195441_conjecture_set_of_solutions' attempted 4 times, never accepted.
- URL: <https://arxiv.org/abs/2310.01325>
- Date: 2024-02-29 (paper); 2026-11-09 (OEIS revision)
- Content: 'However, it is still an open task to establish Conjectures 1(ii) and 2(i).'

This is evidence that the statement was regarded as open at the stated date. It is not proof that no resolution exists.

## Novelty search coverage and limitations

Queries run:

- Kellner conjecture "derivative" Bernoulli polynomials integral coefficients A094960 finite {1,2,4,6,10,12,28,30,36,60} proof 2025 OR 2026 explicit bound
- local grep of solved-conjectures CONTENTS.md for 'Kellner', 'Bernoulli', 'A195441' (no hit)

Sources checked:

- OEIS entry text, fetched 2026-11-26 via https://oeis.org/search?q=id:<A-number>&fmt=text
- OEIS Open results explorer data https://tadamcz.com/oeis-open/results.json (generatedAt 2026-09-16; 3468 attempts by 2026 frontier models on 492 Lean-formalized OEIS conjectures, 170 resolved) and paper abstract https://arxiv.org/abs/2608.11941 (Adamczewski, 12-13 Aug 2026)
- GitHub epoch-research/LeanOpenProblems-results (README, metadata/oeis/conjectures.json, Submission/Spec.lean of the relevant sample)
- GitHub 1337isnot1337/solved-conjectures: README.md and CONTENTS.md (451 lines, fetched 2026-11-26) searched locally for the author name, A-number and key words; no match
- arXiv:2310.01325v2 PDF (full text extracted locally)
- OEIS A195441 (rev. Nov 09 2026)

Limitations: Budget-limited search (about 35 web operations for all candidates together). WebSearch is US-only and returns summaries; MathOverflow, MathSciNet, zbMATH, Google Scholar citation lists and the seqfan mailing list were NOT searched. An unsuccessful search does not establish that the statement is open or that partial results below are the only ones. Warning from this session: the OEIS Open 'open conjecture' list itself contains stale items (A001818, A053175, A296056, A277060 were already proved), so benchmark membership alone is not evidence of openness. The 2017 J. Number Theory paper and the Bordelles-Luca-Moree-Shparlinski paper were not read; OEIS A094960 was seen only through a search-result summary.

## Computational approaches

Everything is exactly computable from digit sums. Literature range: Theorem 5(ii) gives 10^7 for \bar S; a search-result summary of OEIS A094960 says 'no other terms below 10^9' (not fetched directly). Feasible on a desktop: (a) for \bar S only n with n+1 prime need testing, and a single small prime p not dividing n with s_p(n-1) >= p kills n - a sieve-like test reaching 10^12-10^13 looks realistic; (b) for D_n^+ > 1 use the reformulation: n is 'good' as soon as n+1 is composite with largest prime factor > sqrt(n) (j = 1), so only n with n+1 prime or sqrt(n)-smooth need the j >= 2 checks - a segmented largest-prime-factor sieve to 10^11-10^12 is feasible; (c) record the minimal j needed as a function of n to see how much room an explicit analytic bound would have.

## Mathematical approaches

(1) Make the Bordelles-Luca-Moree-Shparlinski argument explicit to get a computable n_0 (exponential sums over primes of fractional parts {n/p}); probably yields an astronomically large n_0, so it must be combined with (2). (2) Elementary route via the reformulation: show that for every n > 192 some n + j (j small) equals k*p with p prime > sqrt(n) and k > j; e.g. handle n by the factorisation type of n+1, n+2, n+3, ... and use explicit results on primes in short intervals / explicit Dusart-type bounds for large n. (3) For Conjecture 1(ii) alone the condition is much stronger (every prime p not dividing n must have s_p(n-1) < p, including small p), so one can exploit small primes: n even with n+1 prime, s_3(n-1) <= 2 unless 3 | n, s_5(n-1) <= 4 unless 5 | n, ... - a covering/density argument plus Baker-type bounds for simultaneous small digit sums might give an explicit proof. (4) Partial theorems: \bar S is contained in an explicit sparse set; conditional proofs under explicit prime-gap hypotheses.

Scout's tractability assessment: A full proof is NOT a realistic newcomer goal: finiteness is known only ineffectively, and the comment in one AI submission fetched from the benchmark says the statement was checked to 3*10^6 and names a 'Baker-level obstruction' (linear forms in logarithms) as the reason no proof was produced. Realistic and publishable progress: extending verification by several orders of magnitude with a certified sieve, the elementary reformulation above with proofs for large classes of n (e.g. all n with n+1 composite having a prime factor > sqrt(n)), and possibly an explicit proof of the weaker Conjecture 1(ii) if the small-prime digit constraints can be made effective. Not tried to death: essentially one author plus one analytic paper.

## Formalization feasibility

Mathlib has Polynomial.bernoulli, bernoulli numbers, Nat.digits, Nat.Prime; 'radical' is available in FormalConjectures/Mathlib. A Lean 4 statement of the A195441 form exists in the OEIS Open benchmark ('oeis_a195441_conjecture_set_of_solutions', fetched; it defines A195441 via Polynomial.bernoulli and the lcm of coefficient denominators). The Kellner-Sondow product formula (denominator = product of primes with s_p(n) >= p) would have to be formalized first to make the statement computable; not known to be in Mathlib (not checked).

## Prerequisites

Bernoulli numbers and polynomials, von Staudt-Clausen theorem, base-p expansions and Legendre's formula, the Kellner-Sondow papers (Amer. Math. Monthly 2017), basic sieve programming, explicit prime-number estimates (Dusart-type) for the analytic part.

## Unverified items

- Exact wording and numbering of the conjectures in the 2017 J. Number Theory paper (only the 2023/2024 restatement was read).
- Conjecture 2(ii) formula: the square root in 'kappa*sqrt(n)/log n' is reconstructed (the extraction shows 'n / log n').
- The claim 'no other terms below 10^9' and the related A094960 comment about 'the sum of the last two base-p digits of k' come from a web-search summary of OEIS A094960, not from a fetched page.
- Typographic identification of the three 'D_n' symbols in the paper.
