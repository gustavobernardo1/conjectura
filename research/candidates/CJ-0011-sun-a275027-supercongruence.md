# CJ-0011 — Sun's supercongruence conjecture for OEIS A275027

*Compiled 2026-11-26 from the record of a literature-scout subagent (Claude, model `claude-fable-5-2`), lightly reformatted. It is a preliminary dossier: it has not been independently audited, and every item under “Unverified items” must be checked before it is relied upon.*

## Statement

(A) OEIS A275027, verbatim: 'a(n) = Sum_{k=0..n} C(n,k)^2*C(n-k,k), where C(n,k) denotes the binomial coefficient n!/(k!*(n-k)!).' 'Conjecture: For any prime p > 5 and positive integer n, the number (a(p*n)-a(n))/(p*n)^3 is always a p-adic integer.'
(B) arXiv:1610.03384v8, Conjecture 5.6 (reconstructed from the PDF text): 'For any prime p > 5 and n in Z^+, we have (g_{pn}(-1) - g_n(-1))/(pn)^3 in Z_p', where (eq. (1.16)) $g_n(x):=\sum_{k=0}^n\binom nk^2\binom{2k}{k}x^k$.
Equivalent integer form of both: $p^{3(1+v_p(n))}$ divides $a(pn)-a(n)$ (resp. $g_{pn}(-1)-g_n(-1)$). Note (checked numerically in this session): the two sequences are different (A275027 = 1, 1, 5, 19, 85, 401, ...; g_n(-1) = 1, -1, -1, 17, -65, 49, 881, ...), so (A) and (B) are two distinct conjectures of the same shape.

**Source.** Z.-W. Sun, comment in OEIS entry A275027 (12 November 2016; revision 37 of 7 November 2026 read); companion: Conjecture 5.6 of arXiv:1610.03384v8. <https://oeis.org/A275027>

**Statement checked against:** primary-source. The OEIS statement is quoted verbatim. The companion conjecture concerns a different sequence and was reconstructed from PDF text.

## Definitions and hypotheses

p prime with p > 5 (p = 5 genuinely fails: in this session v_5(a(5)-a(1)) = 2 < 3 for both sequences); n >= 1 any positive integer, including n divisible by p - this is what makes the statement stronger than a mod p^3 congruence: for p | n one needs p^6, p^9, ... Z_p = ring of p-adic integers. OEIS also gives a(n) = Sum_k C(n,k)*C(n,2k)*C(2k,k) and a Zeilberger recurrence of order 3: (n+3)^2(23n+25)a(n+3) = 25(n+1)^2(23n+48)a(n) + (391n^3+1989n^2+3288n+1750)a(n+1) + (46n^3+280n^2+519n+265)a(n+2). For (B) the paper notes g_n(-1) = Sum_{k=0..floor(n/2)} C(n,2k)^2 C(2k,k) (-1)^(n-k).

## Known partial results

- OEIS: 'The author has proved that for any prime p > 5 and positive integer n the number (a(p*n)-a(n))/(p^3*n^2) is always a p-adic integer.' (i.e. one factor of n short of the conjecture). — OEIS A275027 comment (Z.-W. Sun) <https://oeis.org/A275027> (source fetched)
- Theorem 1.3 of arXiv:1610.03384v8: for any prime p > 5 and n in Z^+, (g_{pn}(-1) - g_n(-1))/n^2 == 0 (mod p^3); Remark 5.6 says Conjecture 5.6 'is stronger than Theorem 1.3'. — Z.-W. Sun, Supercongruences involving Lucas sequences, arXiv:1610.03384v8 <https://arxiv.org/abs/1610.03384> (source fetched)
- A275027 is the diagonal of the rational function 1/((1-x)(1-y)(1-z) - x^2 y z) (Gutkovskiy, 2025) and has g.f. given by a 2F1 in an explicit rational argument (van Hoeij, 2024); OEIS links Henningsen-Straub, 'Generalized Lucas congruences and linear p-schemes' (arXiv:2111.08641). — OEIS A275027 comments/formulas/links <https://oeis.org/A275027> (source fetched)
- Sanity check in this session: for p in {7,11,13,17} and all n with pn <= 420 (n up to 39 for p = 7), p^(3(1+v_p(n))) divides a(pn)-a(n) and g_{pn}(-1)-g_n(-1), with equality of valuations occurring (no slack in general). — own computation, scratchpad/scripts/check1.py <> (source not fetched)

## Relevant literature

- Z.-W. Sun, comment in OEIS entry A275027 (12 November 2016; revision 37 of 7 November 2026 read); companion: Conjecture 5.6 of arXiv:1610.03384v8. <https://oeis.org/A275027>
- OEIS A275027 comment (Z.-W. Sun) <https://oeis.org/A275027>
- Z.-W. Sun, Supercongruences involving Lucas sequences, arXiv:1610.03384v8 <https://arxiv.org/abs/1610.03384>
- OEIS A275027 comments/formulas/links <https://oeis.org/A275027>
- own computation, scratchpad/scripts/check1.py <>

## Open-status evidence

- Most recent source: OEIS A275027 revision #37 dated Nov 07 2026 still shows the conjecture with only Sun's partial result; OEIS Open data (2026-09-16): 'oeis_275027_conjecture_0' attempted 4 times, never accepted; arXiv:1610.03384 latest version is v8 (14 Dec 2020) and still lists Conjecture 5.6.
- URL: <https://oeis.org/A275027>
- Date: 2026-11-07
- Content: 'Conjecture: For any prime p > 5 and positive integer n, the number (a(p*n)-a(n))/(p*n)^3 is always a p-adic integer.' followed only by the weaker proved statement.

This is evidence that the statement was regarded as open at the stated date. It is not proof that no resolution exists.

## Novelty search coverage and limitations

Queries run:

- "Supercongruences involving Lucas sequences" Sun conjecture "g_n(-1)" OR "g_{pn}(-1)" OR A275027 proof (pn)^3 p-adic integer 2024 OR 2025 OR 2026
- arXiv 2025 2026 "conjecture of Zhi-Wei Sun" congruence OR permanent OR determinant "we confirm" OR "still open"
- local grep of solved-conjectures CONTENTS.md for 'Zhi-Wei', "Sun's", 'A275027', 'supercongruence' (no relevant hit)

Sources checked:

- OEIS entry text, fetched 2026-11-26 via https://oeis.org/search?q=id:<A-number>&fmt=text
- OEIS Open results explorer data https://tadamcz.com/oeis-open/results.json (generatedAt 2026-09-16; 3468 attempts by 2026 frontier models on 492 Lean-formalized OEIS conjectures, 170 resolved) and paper abstract https://arxiv.org/abs/2608.11941 (Adamczewski, 12-13 Aug 2026)
- GitHub epoch-research/LeanOpenProblems-results (README, metadata/oeis/conjectures.json, Submission/Spec.lean of the relevant sample)
- GitHub 1337isnot1337/solved-conjectures: README.md and CONTENTS.md (451 lines, fetched 2026-11-26) searched locally for the author name, A-number and key words; no match
- arXiv:1610.03384v8 PDF (text extracted locally)

Limitations: Budget-limited search (about 35 web operations for all candidates together). WebSearch is US-only and returns summaries; MathOverflow, MathSciNet, zbMATH, Google Scholar citation lists and the seqfan mailing list were NOT searched. An unsuccessful search does not establish that the statement is open or that partial results below are the only ones. Warning from this session: the OEIS Open 'open conjecture' list itself contains stale items (A001818, A053175, A296056, A277060 were already proved), so benchmark membership alone is not evidence of openness. Citations of arXiv:1610.03384 were not enumerated; Sun's own later lists of open conjectures were not consulted; similar Sun conjectures for Apery-like numbers were proved by others in 2019-2022 (not verified here), so a proof of this one may exist under a title not containing these keywords.

## Computational approaches

Compute a(n) with the order-3 recurrence (or the binomial sum) as exact integers; check v_p(a(pn)-a(n)) >= 3(1+v_p(n)) for all primes 7 <= p < 200 and n up to several thousand, with emphasis on n = p, p^2 (needs p^6, p^9). No verification range is stated in the sources read. Useful experiments: determine a(p) mod p^4 (a formula with Bernoulli numbers would explain the exact exponent), and test the same statement for the sibling sequences A208425 (mod (pn)^3, p > 3) and A278415 (mod (pn)^2, p > 3).

## Mathematical approaches

(1) Follow Sun's proof of the (p^3 n^2)-version in arXiv:1610.03384 (Section 4) and find where a factor of n is lost; the conjecture asks for the extra v_p(n). (2) Use a(n) = Sum_k C(n,k) C(n,2k) C(2k,k): apply Jacobsthal-Kazandzidis to terms with p | k (C(pn,pk) == C(n,k) mod p^(3+v_p(n)+...)), and bound the remaining terms using C(pn,k) = (pn/k) C(pn-1,k-1), which gives p^(1+v_p(n)) per binomial; three such factors or a harmonic-sum cancellation are needed. (3) Diagonal/constant-term structure: a(n) is the diagonal of an explicit rational function, so methods for 'Gauss congruences of higher order' for diagonals apply. (4) Multiplicative induction on v_p(n).

Scout's tractability assessment: Plausible full proof: Sun already has all but one factor of n, and the remaining gap only concerns n divisible by p (for p not dividing n the conjecture coincides with the proved statement). So the real content is: prove a(p^2 m) == a(p m) (mod p^6) etc. - a clean, checkable target. Risk: Sun has dozens of conjectures of this exact shape and several were proved by others around 2019-2022; this specific one showed no proof in OEIS as of Nov 2026, but the literature check here was shallow.

## Formalization feasibility

Elementary to state; Lean 4 statements exist in the OEIS Open benchmark ('oeis_275027_conjecture_0', stated with Padic/PadicInt on a rational quotient; the fetched Spec.lean also contains an equivalent divisibility form p^(3*(1+n.factorization p)) | a(p*n) - a(n)). Mathlib has Nat.choose, padicValNat, Nat.factorization. Proof-side p-adic binomial lemmas: not checked.

## Prerequisites

Same toolkit as candidate 1: p-adic valuations, Lucas/Kummer, Wolstenholme, Jacobsthal-Kazandzidis, harmonic numbers mod p^2, Zeilberger's algorithm; reading Sun's paper (25 pages).

## Unverified items

- Which version of arXiv:1610.03384 (if any) contains the proof of the partial result claimed in OEIS for the A275027 sequence: v8 states and proves the analogous Theorem 1.3 for g_n(-1) only.
- Journal publication data for arXiv:1610.03384 (not shown in the text read).
- Statements for the siblings A208425 and A278415 are from the OEIS Open metadata paraphrase only.
- Formulas of Conjecture 5.6/Theorem 1.3 were reconstructed from pdftotext output with broken layout; re-read the PDF before formalizing.
