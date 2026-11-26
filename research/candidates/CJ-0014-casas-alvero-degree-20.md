# CJ-0014 — Casas-Alvero conjecture (smallest open degree 20)

*Compiled 2026-11-26 from the record of a literature-scout subagent (Claude, model `claude-fable-5-2`), lightly reformatted. It is a preliminary dossier: it has not been independently audited, and every item under “Unverified items” must be checked before it is relied upon.*

## Statement

Verbatim from arXiv:2608.14726v1: 'Conjecture 1.1 (Casas-Alvero). Let $K$ be a field of characteristic $0$. Then there is no $\mathrm{CA}$-polynomial over $K$; equivalently, if $f\in K[x]$ is monic of degree $d$ and $\gcd(f,f^{(i)})\neq 1$ for $i=1,\dots,d-1$, then $f=(x-\alpha)^{d}$ for some $\alpha\in K$.' Definition there: for $f(x)=x^{d}+a_{1}x^{d-1}+\cdots+a_{d}\in K[x]$, '$f$ is a Casas-Alvero polynomial (or CA-polynomial) if for every $i\in\{1,\dots,d-1\}$ the polynomial $f$ has a non-constant common factor with its $i$-th Hasse derivative $H_{i}(f)$, and $f$ is not the $d$-th power of a linear polynomial. In characteristic zero $H_{i}(f)=f^{(i)}/i!$'. Target small case: $\mathrm{CA}_{20,0}$, i.e. the statement for $d=20$ ('The smallest degree for which the conjecture is open is $d=20$').

**Source.** E. Casas-Alvero, Higher order polar germs, J. Algebra 240 (2001) 326-337; statement quoted from M. F. Marashdeh, arXiv:2608.14726v1 (12 August 2026), Conjecture 1.1. <https://arxiv.org/abs/2608.14726>

**Statement checked against:** secondary-source. Quoted from a 2026 restatement; the 2001 paper was not accessed.

## Definitions and hypotheses

Characteristic 0 is essential: the conjecture is FALSE in positive characteristic (a prime $p$ is 'bad' for $d$ if $\mathrm{CA}_{d,p}$ fails; e.g. $\mathcal{B}(3)=\{2\}$, $\mathcal{B}(4)=\{3,5,7\}$). In characteristic $p$ one must use Hasse derivatives, not ordinary derivatives. The gcd may be taken over the algebraic closure, so the condition is 'for every $i$ there is a root of $f$ that is also a root of $f^{(i)}$' (the shared root may differ with $i$). All $d-1$ conditions are needed: Draisma and de Jong showed that omitting any single one produces nontrivial solutions. WLOG a root is translated to 0 and the polynomial scaled; the solution set is a closed subscheme of a weighted projective space over $\mathbb{Z}$. Trivial for $d\le 2$.

## Known partial results

- Transfer (T): if CA_{d,p} holds for one prime p then CA_{d,0} holds. Descent (D): if p^e exactly divides d and CA_{d/p^e,p} holds then CA_{d,p} holds; in particular CA_{p^k,p} holds. Hence the conjecture holds for d = p^k and d = 2p^k. — H.-C. Graf von Bothmer, O. Labs, J. Schicho, C. van de Woestijne, J. Algebra 316 (2007) 224-230, as summarised in arXiv:2608.14726v1 <https://arxiv.org/html/2608.14726v1> (source fetched)
- Known degrees (per the 2026 summary): d = p^k, 2p^k; 3p^k with p != 2; 4p^k with p not in {3,5,7}; 5p^k with p not in B(5) = {2,3,7,11,131,193,599,3541,8009}; 6p^k and 7p^k with p not in B(6), B(7) (|B(6)| = 53, |B(7)| = 366); d = 12 by direct computation; d <= 7 by direct elimination. Bad prime sets are determined only for d <= 7. — arXiv:2608.14726v1 Section 1, citing Castryck-Laterveer-Ounaies (Math. Comp. 83 (2014) 3017-3037), Chellali-Salinier (2012), Draisma-de Jong (2011), Diaz-Toca and Gonzalez-Vega (2006) <https://arxiv.org/html/2608.14726v1> (source fetched)
- Constraints on a counterexample: no root of multiplicity >= d-2; at least two distinct roots in the interior of the convex hull of the roots; at least five distinct roots; at least three recycled roots. — Castryck, Laterveer, Ounaies (2014), as summarised in arXiv:2608.14726v1 <https://arxiv.org/html/2608.14726v1> (source fetched)
- In degree 20 there are no counterexamples with three recycled roots; finiteness of counterexamples in normal form for degrees p^r+p^s and p^r+2p^s. — C. Massri, 'The Casas-Alvero conjecture for three recycled roots in degree 20', arXiv:1806.09561v6 (abstract read via arXiv API) <https://arxiv.org/abs/1806.09561> (source fetched)
- Explicit description of, and an upper bound on, the set of bad primes in a given degree n (assuming the conjecture in degree n); criterion: if p divides binom(d,m)-1 for some 1 <= m <= d-1 then p is bad for d. — D. Schaub, M. Spivakovsky, arXiv:2411.13967 and Res. Math. Sci. 11 (2024) Paper No. 31 (abstract read via arXiv API; criterion as quoted in arXiv:2608.14726v1) <https://arxiv.org/abs/2411.13967> (source fetched)
- Descent-set obstruction (Aug 2026 preprint): after centring, when one nonzero root realises all surviving conditions the obstruction is MacMahon's descent-set count; every prime dividing such a count but none of the accompanying integers z_i is bad (e.g. 691 is bad for d=11; 19 and 2659 for d=10); two-element supports settled in every characteristic, so a counterexample has at least four terms in centred normal form. — M. F. Marashdeh, arXiv:2608.14726v1 (unrefereed preprint) <https://arxiv.org/abs/2608.14726> (source fetched)
- Claimed general proof downgraded: arXiv:2501.09272 was submitted 16 Jan 2025 (title then reported as 'Proof of the Casas-Alvero conjecture'); its current version v3, last revised 10 Nov 2026, is titled 'A conditional proof of the Casas-Alvero conjecture' and proves the conjecture only 'under a uniform local Lojasiewicz type hypothesis'. — S. Ghosh, arXiv:2501.09272v3 <https://arxiv.org/abs/2501.09272> (source fetched)

## Relevant literature

- E. Casas-Alvero, Higher order polar germs, J. Algebra 240 (2001) 326-337; statement quoted from M. F. Marashdeh, arXiv:2608.14726v1 (12 August 2026), Conjecture 1.1. <https://arxiv.org/abs/2608.14726>
- H.-C. Graf von Bothmer, O. Labs, J. Schicho, C. van de Woestijne, J. Algebra 316 (2007) 224-230, as summarised in arXiv:2608.14726v1 <https://arxiv.org/html/2608.14726v1>
- arXiv:2608.14726v1 Section 1, citing Castryck-Laterveer-Ounaies (Math. Comp. 83 (2014) 3017-3037), Chellali-Salinier (2012), Draisma-de Jong (2011), Diaz-Toca and Gonzalez-Vega (2006) <https://arxiv.org/html/2608.14726v1>
- Castryck, Laterveer, Ounaies (2014), as summarised in arXiv:2608.14726v1 <https://arxiv.org/html/2608.14726v1>
- C. Massri, 'The Casas-Alvero conjecture for three recycled roots in degree 20', arXiv:1806.09561v6 (abstract read via arXiv API) <https://arxiv.org/abs/1806.09561>
- D. Schaub, M. Spivakovsky, arXiv:2411.13967 and Res. Math. Sci. 11 (2024) Paper No. 31 (abstract read via arXiv API; criterion as quoted in arXiv:2608.14726v1) <https://arxiv.org/abs/2411.13967>
- M. F. Marashdeh, arXiv:2608.14726v1 (unrefereed preprint) <https://arxiv.org/abs/2608.14726>
- S. Ghosh, arXiv:2501.09272v3 <https://arxiv.org/abs/2501.09272>

## Open-status evidence

- Most recent source: arXiv:2501.09272v3 (revised 10 Nov 2026, now explicitly conditional) and arXiv:2608.14726v1 (12 Aug 2026)
- URL: <https://arxiv.org/abs/2501.09272>
- Date: 2026-11-10 and 2026-08-12
- Content: arXiv:2608.14726v1: 'The smallest degree for which the conjecture is open is d=20.' and 'A proof of Conjecture 1.1 in full generality is announced in a preprint of S. Ghosh [10] ... as that work has not been independently verified, the conjecture is treated here as open.' The Ghosh preprint itself was retitled 'A conditional proof ...' in its 10 Nov 2026 revision. A date-sorted arXiv API listing for "Casas-Alvero" shows nothing newer than these two items.

This is evidence that the statement was regarded as open at the stated date. It is not proof that no resolution exists.

## Novelty search coverage and limitations

Queries run:

- web: Casas-Alvero conjecture 2025 OR 2026 proof OR counterexample degree 12 OR 20 open status
- web: "Casas-Alvero conjecture" Ghosh proof 2501.09272 gap OR error OR withdrawn OR "still open" 2025 2026
- arXiv API: all:"Casas-Alvero", sortBy=submittedDate desc, 12 results

Sources checked:

- arXiv abs page of 2501.09272 (v3)
- arXiv HTML of 2608.14726v1
- arXiv API listing
- general web search (Wikipedia page surfaced, not opened)

Limitations: Session date 2026-11-26. About 30 outbound requests in total across all candidates: 13 model-summarised web searches (US-only index), 4 model-summarised page fetches, 13 direct downloads of arXiv abs/HTML pages and arXiv API listings (sorted by submission date). NOT checked: MathOverflow, Open Problem Garden, MathSciNet/zbMATH, Google Scholar citation trails, journal sites, conference proceedings, non-arXiv preprint servers (several 2026 AI-assisted proofs of other conjectures appeared first on preprints.org or GitHub, which this search does not cover). An unsuccessful search does not establish that the problem is open or that a planned partial result is new. I did not read the body of Ghosh's v3, so I cannot say how strong or checkable the remaining Lojasiewicz-type hypothesis is; if that hypothesis is proved the whole conjecture falls and degree-20 work becomes moot. Section 8 of arXiv:2608.14726 ('questions left open') was not read in detail.

## Computational approaches

The problem for fixed $d$ is a zero-dimensionality/emptiness question for an explicit system: the resultants $R_i=\mathrm{Res}(f,H_i(f))$, $i=1..d-1$, in the coefficients. Exact tools: Groebner bases over $\mathbb{F}_p$ (Singular, msolve, Magma) to prove $\mathrm{CA}_{d,p}$ for ONE prime $p$, which by Transfer gives characteristic 0. For $d=20$ the cheap route is blocked: $20=4\cdot 5$ needs $5\notin\mathcal{B}(4)$ but $5$ is bad for 4; $20=5\cdot 2^2$ needs $2\notin\mathcal{B}(5)$ but 2 is bad for 5; so one needs a direct computation as was done for $d=12$ (Castryck-Laterveer-Ounaies), organised by 'scenarios' (which root is recycled for which derivative) and pruned by the known constraints. Sub-cases are independently certifiable: Massri eliminated three recycled roots in degree 20; the next cases are four or more recycled roots, or fixed supports of the centred normal form (Marashdeh's stratification gives unit lower triangular systems and explicit integer obstructions). Also computable: bad-prime sets $\mathcal{B}(8)$, $\mathcal{B}(9)$, ... (known only for $d\le 7$), which would settle further degrees $8p^k$, $9p^k$ etc. Largest case settled by direct computation in the literature: $d=12$.

## Mathematical approaches

Arithmetic geometry of the Casas-Alvero scheme over Spec Z (properness, transfer between characteristics); resultant/elimination theory; combinatorics of scenarios and recycled roots; Gauss-Lucas type convex-hull constraints on roots; descent sets / alternating permutations (Marashdeh); Koszul homology and Lojasiewicz-type estimates (Ghosh, conditional).

Scout's tractability assessment: Good newcomer target in the sense that sub-cases are elementary to state and certify. Honest view: the full conjecture and even full degree 20 have resisted specialists for 15+ years (degree 12 needed a substantial Groebner computation plus theory in 2012; nothing new has been settled by direct computation since). Realistic partial results: (a) degree 20 with four recycled roots, or with prescribed small support in centred normal form; (b) determining the bad-prime set B(8) (settling degrees 8p^k for good p, e.g. 24 = 8*3 if 3 is good for 8); (c) new elementary constraints on counterexamples (number of distinct roots, multiplicities); (d) Lean proofs for small degrees. Risk: Ghosh's conditional proof might be completed, which would make degree-specific work obsolete.

## Formalization feasibility

Not checked in this session. From memory (unverified): the statement is easy in Lean 4 Mathlib: Polynomial, Polynomial.derivative / iterated derivative (and Polynomial.hasseDeriv), IsCoprime or gcd over a field, CharZero. I recall the conjecture being included in public collections of formal conjecture statements, but did not verify this. Proofs for fixed d by modular Groebner bases would need certificate checking (ideal-membership certificates are checkable by ring/linear_combination but are enormous for d = 12 or 20). Small degrees (d <= 5 or 6) are plausible Lean targets.

## Prerequisites

Polynomial rings, gcd, resultants and discriminants; finite fields and Hasse derivatives; Groebner bases and elimination; basic scheme language only for reading the transfer argument (it can be used as a black box); permutation statistics (descent sets) for the 2026 approach.

## Unverified items

- Original statement and page numbers in Casas-Alvero (2001): taken from a reference list, paper not fetched.
- The claim that Ghosh's v1/v2 was titled 'Proof of the Casas-Alvero conjecture' comes from a search summary and from the reference list of arXiv:2608.14726; I only fetched the current v3 abs page.
- Whether 3 is a good prime for degree 8 (my example in the tractability comment is hypothetical; B(8) is not determined in the literature I read).
- My statement that 2 is bad for 5 and 5 is bad for 4 is read off the bad-prime sets quoted in arXiv:2608.14726; the inference that the transfer+descent route is therefore blocked for d = 20 is mine, although consistent with the paper's remark that d = 20 is the smallest open degree.
- Presence of the conjecture in any formal-conjectures repository (memory only).
