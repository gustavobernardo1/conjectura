# CJ-0013 — Chen–Edelman–Urschel conjecture on the 5x5 growth factor under complete pivoting

*Compiled 2026-11-26 from the record of a literature-scout subagent (Claude, model `claude-fable-5-2`), lightly reformatted. It is a preliminary dossier: it has not been independently audited, and every item under “Unverified items” must be checked before it is relied upon.*

## Statement

Verbatim (arXiv HTML v2): 'Conjecture 2.1. The largest possible growth factor for a $5\times 5$ real matrix under complete pivoting is exactly the lower bound proven in this paper, i.e., the unique real root $g$ in the interval $[4,5]$ of the $61^{st}$ degree polynomial $P_{5}(g)$ in Equation (2.15).' Definitions from the same paper: Gaussian elimination writes $A=LU$; the growth factor is $g(A)=\max\{\|L\|_{\max},\ \|U\|_{\max}/\|A\|_{\max}\}$ where $\|\cdot\|_{\max}$ is the largest magnitude entry. With $A^{(k)}:=A_{k:n,k:n}-A_{k:n,1:k-1}[A_{1:k-1,1:k-1}]^{-1}A_{1:k-1,k:n}$, a matrix is 'completely pivoted' if $|A^{(k)}_{i,j}|\le |A^{(k)}_{k,k}|$ for all $i,j=k,\ldots,n$, $k=1,\ldots,n-1$. For a completely pivoted matrix $g(A)=\max_k |U_{kk}|$, and for the maximum over $n\times n$ completely pivoted matrices it suffices to maximise $|U_{nn}|$. $P_5$ is an explicit integer polynomial of degree 61 printed in Eq. (2.15) of the paper; its relevant root is $g=4.1325170786\,3247285422\,3346853277\,3712699527\ldots$ (200 digits are printed in Eq. (2.16)). Companion statements in the paper, called suppositions rather than numbered conjectures: the lower bounds $5$ for $n=6$, the real root $6.0569534737\ldots$ of $P_7(g)=3g^6-86g^5+688g^4-1136g^3-5888g^2+12032g+22528$ for $n=7$, and $8$ for $n=8$ 'which we suppose are maximums as well'.

**Source.** J. Chen, A. Edelman, J. Urschel, The largest 5th pivot may be the root of a 61st degree polynomial, arXiv:2602.20390v2 (15 March 2026), Conjecture 2.1. <https://arxiv.org/abs/2602.20390>

**Statement checked against:** primary-source. Quoted from the fetched arXiv page.

## Definitions and hypotheses

Real matrices only ('we restrict ourselves to real $n\times n$ matrices'). WLOG $\|A\|_{\max}=A_{11}=1$ and all leading principal minors $\ge 0$; the complete-pivoting constraints are the determinantal inequalities $-\det(A_{1:k,1:k})\le \det(A_{1:k-1\cup\{i\},1:k-1\cup\{j\}})\le \det(A_{1:k,1:k})$ (paper Eq. 1.8). So for $n=5$ the problem is: maximise the fifth pivot over a compact semi-algebraic set in 24 real variables. Easy to get wrong: (a) the conjecture is about the supremum over ALL completely pivoted matrices, whereas Theorem 2.2 only proves optimality on the face cut out by the specific 23 equality constraints that numerical optimisation found tight; (b) known values quoted for $n=1..4$ are $1,2,2\tfrac14,4$; (c) the old 'growth $\le n$' conjecture is false for larger $n$ (see partial results), so no simple pattern should be assumed; (d) ties in pivot choice are irrelevant once one works with completely pivoted matrices.

## Known partial results

- Maximum growth factors for n=1,...,4 are 1, 2, 2 1/4, 4 ('known since the 1960s'). — Stated in Section 1 of arXiv:2602.20390v2 <https://arxiv.org/html/2602.20390v2> (source fetched)
- Theorem 2.2: over all completely pivoted 5x5 matrices satisfying the equality-constraint pattern (2.1) suggested by JuMP, the largest growth factor is exactly the root of P_5 near 4.1325 (proof by Groebner basis + discriminant case analysis in Mathematica; code in a GitHub repository). — arXiv:2602.20390v2, Theorem 2.2 <https://arxiv.org/html/2602.20390v2> (source fetched)
- Theorem 3.5: g(A) <= 4.84 for all completely pivoted 5x5 matrices (interval-arithmetic branch and bound; improves Tornheim's 1969 bound 4 17/18 ~ 4.94 and Cohen's 1974 bound 5.005). The authors state 4.84 'can be readily lowered by simply lowering a handful of numbers in the associated code and suffering a slightly longer runtime' but that the technique 'certainly falls short of 4.1325'. — arXiv:2602.20390v2, Theorem 3.5 and Table 1 <https://arxiv.org/html/2602.20390v2> (source fetched)
- Proposition 1.1: the largest possible growth factor for an n x n real matrix under complete pivoting is an algebraic number of degree at most (2n)^(n^2-1). — arXiv:2602.20390v2, Proposition 1.1 <https://arxiv.org/html/2602.20390v2> (source fetched)
- Numerical lower bounds for n=1:75 and n=100; evidence that maximum growth exceeds n iff n >= 11; largest growth factor > 1.0045 n for n > 10; lim sup of ratio to n is >= 3.317. — A. Edelman, J. Urschel, 'Some new results on the maximum growth factor in Gaussian elimination', arXiv:2303.04892 (SIAM J. Matrix Anal. Appl. 45(2):967-991, 2024 per the reference list of 2602.20390) <https://arxiv.org/abs/2303.04892> (source fetched)
- General upper bound n^(0.2079 ln n + 0.91), first improvement on Wilkinson's 1961 bound 2 n^(0.25 ln n + 0.5); does not improve Tornheim's bound for n=5. — A. Bisain, A. Edelman, J. Urschel, arXiv:2312.00994 (Bull. LMS 57(5):1369-1387, 2025 per the reference list of 2602.20390) <https://arxiv.org/abs/2312.00994> (source fetched)

## Relevant literature

- J. Chen, A. Edelman, J. Urschel, The largest 5th pivot may be the root of a 61st degree polynomial, arXiv:2602.20390v2 (15 March 2026), Conjecture 2.1. <https://arxiv.org/abs/2602.20390>
- Stated in Section 1 of arXiv:2602.20390v2 <https://arxiv.org/html/2602.20390v2>
- arXiv:2602.20390v2, Theorem 2.2 <https://arxiv.org/html/2602.20390v2>
- arXiv:2602.20390v2, Theorem 3.5 and Table 1 <https://arxiv.org/html/2602.20390v2>
- arXiv:2602.20390v2, Proposition 1.1 <https://arxiv.org/html/2602.20390v2>
- A. Edelman, J. Urschel, 'Some new results on the maximum growth factor in Gaussian elimination', arXiv:2303.04892 (SIAM J. Matrix Anal. Appl. 45(2):967-991, 2024 per the reference list of 2602.20390) <https://arxiv.org/abs/2303.04892>
- A. Bisain, A. Edelman, J. Urschel, arXiv:2312.00994 (Bull. LMS 57(5):1369-1387, 2025 per the reference list of 2602.20390) <https://arxiv.org/abs/2312.00994>

## Open-status evidence

- Most recent source: arXiv:2602.20390v2 itself (the conjecture is 9 months old) plus an arXiv API listing run on 2026-11-26
- URL: <https://arxiv.org/html/2602.20390v2>
- Date: 2026-03-15 (v2); listing checked 2026-11-26
- Content: 'While the super-exponentially many possible configurations of tight constraints prevents us from fully proving this conjecture...' and 'The resolution of the maximum growth for n=5 will likely require an impressive marriage of mathematics and computation, one that may not yet be possible in 2026.' An arXiv API query for all:"growth factor" AND all:"complete pivoting", sorted by submission date, returned this paper as the newest entry (nothing later).

This is evidence that the statement was regarded as open at the stated date. It is not proof that no resolution exists.

## Novelty search coverage and limitations

Queries run:

- web: growth factor Gaussian elimination complete pivoting 2024 OR 2025 OR 2026 maximum growth n=5 open conjecture Hadamard matrices growth
- web: Cryer conjecture Hadamard matrix growth factor complete pivoting order 20 open 2024 OR 2025 OR 2026
- arXiv API: all:"growth factor" AND all:"complete pivoting", sortBy=submittedDate desc, 12 results

Sources checked:

- arXiv abs + HTML of 2602.20390v2
- arXiv API listing
- general web search

Limitations: Session date 2026-11-26. About 30 outbound requests in total across all candidates: 13 model-summarised web searches (US-only index), 4 model-summarised page fetches, 13 direct downloads of arXiv abs/HTML pages and arXiv API listings (sorted by submission date). NOT checked: MathOverflow, Open Problem Garden, MathSciNet/zbMATH, Google Scholar citation trails, journal sites, conference proceedings, non-arXiv preprint servers (several 2026 AI-assisted proofs of other conjectures appeared first on preprints.org or GitHub, which this search does not cover). An unsuccessful search does not establish that the problem is open or that a planned partial result is new. The GitHub repository cited by the paper (github.com/jamiecjx/growth-5x5) was not opened, so I do not know whether it has been updated with stronger bounds since March 2026.

## Computational approaches

Everything is polynomial with rational data, so exact methods apply. (1) Reproduce Theorem 2.2 independently (Singular/Sage/msolve Groebner basis + discriminant) and certify the root isolation of P_5 with exact arithmetic. (2) Lower the global upper bound below 4.84 by rerunning or re-implementing the interval branch-and-bound of Section 3 with tighter parameters (the paper says this is possible at the cost of runtime); a rigorous new bound such as 4.7 or 4.6 would be a citable, checkable result. (3) Treat other active-constraint patterns: for each candidate set of tight constraints solve the KKT system exactly and show the value is below 4.1325..., i.e. extend Theorem 2.2 pattern by pattern. (4) Rigorous global optimisation (interval branch and bound, SOS/Positivstellensatz certificates, SMT/NLSAT) on the 24-variable semi-algebraic set; closing the whole gap this way looks out of reach, but subregions can be excluded with certificates. (5) The analogous exact statements for n=6 (value 5) and n=7 (root of the sextic P_7): the paper reports the method is 'notably simpler' there, so 'optimal on the JuMP constraint pattern' theorems for n=6,7 with independent certificates are feasible. Largest case settled in the literature: n=4 (value 4); for n=5 only 4.1325... <= max <= 4.84.

## Mathematical approaches

Structure theory of completely pivoted matrices (Schur-complement / determinantal inequalities, Eq. 1.8); combining bounds for the leading 3x3 block and the trailing 3x3 Schur complement (the paper's g = p_3 p_3' argument, with Cohen's 3x3 pivot relations); KKT / active-set analysis on a semi-algebraic set; elimination theory (Groebner bases, discriminants, resultants); Tarski-Seidenberg / algebraic-degree arguments.

Scout's tractability assessment: Full conjecture: hard; the authors (leading experts) say it may not be possible in 2026, and the gap 4.1325 vs 4.84 is large. Realistic partial progress for a small team: (i) independent exact re-verification of Theorem 2.2 and of the n=6, n=7 values; (ii) a certified improvement of the 4.84 upper bound (the authors explicitly leave slack); (iii) exact optimality on additional constraint patterns; (iv) a certified local-maximality statement (second-order conditions) at the conjectured maximiser. What has been tried extensively: numerical global optimisation for n=5 (NPSOL 1988, LANCELOT 1991, JuMP 2024, LANCELOT 2026) always returns 4.1325..., so a numerical counterexample search is unlikely to succeed and should not be the main bet.

## Formalization feasibility

Not checked in this session. From memory (unverified): Mathlib has matrices, determinants, Schur complements and basic LU-free linear algebra but, as far as I know, no formal definition of Gaussian elimination with complete pivoting or of the growth factor; the cleanest formal statement would avoid the algorithm and use the determinantal inequalities (1.8) directly, which only needs Matrix.det and submatrices. Stating the conjectured constant needs 'the unique real root of an explicit degree-61 integer polynomial in [4,5]', which is statable but heavy. Formalising a full interval-arithmetic upper-bound proof would require a verified interval/certificate checker.

## Prerequisites

LU factorisation and pivoting; Schur complements and determinantal identities; constrained optimisation (KKT conditions); Groebner bases, resultants and discriminants in a CAS; interval arithmetic and branch-and-bound; basic real algebraic geometry (semi-algebraic sets, algebraic numbers).

## Unverified items

- The contents and current state of the GitHub repository github.com/jamiecjx/growth-5x5 (cited in the paper; not opened).
- The explicit coefficients of P_5 (present in the fetched HTML, Eq. 2.15, but not transcribed or re-checked here).
- Whether the paper has been published in a journal.
- Related claim seen only in a search-engine summary: growth of Hadamard matrices under complete pivoting equals n has been proved only for n = 4, 8, 12, 16 (Cryer's Hadamard conjecture, order 20 open). I did not fetch a primary or recent source for this, so it is not included as a candidate.
