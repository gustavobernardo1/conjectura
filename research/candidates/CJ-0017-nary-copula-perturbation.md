# CJ-0017 — Mesiar's Problem 4.1: higher-dimensional copula perturbation C − ∏(x_i − C)

*Compiled 2026-11-27 by the problem-scout subagent (model claude-sonnet-5-5). Not audited. The hand calculation below is unchecked by any program.*

## Statement

Verbatim from the primary source (Fuzzy Sets and Systems 261 (2015), p. 114, read from page images):

> "Definition 4.1. Let n >= 2 be fixed. A function C: [0,1]^n -> [0,1] is called a (n-ary) copula whenever it is n-increasing and satisfies boundary conditions, i.e., (C1) for any x, y in [0,1]^n, x_1<=y_1, ..., x_n<=y_n it holds V_C([x,y]) = sum over eps in {-1,1}^n of ( C(z^(eps)) prod_{i=1}^n eps_i ) >= 0, where z^(eps)=(z_1^{eps_1},...,z_n^{eps_n}), z_i^{1}=y_i, z_i^{-1}=x_i, i=1,...,n; (C2) C(x)=0 whenever 0 in {x_1,...,x_n} and C(x)=x_i whenever x_j=1 for all j != i."
>
> "Problem 4.1 (Mesiar). Let C: [0,1]^n -> [0,1] be an n-ary copula. Define C_1: [0,1]^n -> [0,1] by C_1(x_1,...,x_n) = C(x_1,...,x_n) - prod_{i=1}^n (x_i - C(x_1,...,x_n)). (2) Is the function C_1 n-increasing, i.e., is it an n-copula? If in general not, characterize all n-copulas C such that C_1 is an n-copula, too."

Context quoted in the source: for n = 2 the construction $C_\lambda=C+\lambda(x-C)(y-C)$ is known (their reference [38]); "if, for a given n-copula C, C_1 given by (2) is n-copula, then also C_λ ... λ in [0,1], is an n-copula."

**Source.** R. Mesiar, A. Stupňanová, "Open problems from the 12th International Conference on Fuzzy Set Theory and Its Applications", Fuzzy Sets and Systems 261 (2015) 112–123, DOI 10.1016/j.fss.2014.07.012, Problem 4.1. URL: http://library.utia.cas.cz/separaty/2019/E/mesiar-0506948.pdf (fetched 2026-11-27).

**Statement checked against:** primary-source (page images).

## Definitions and hypotheses

- The product $\prod(x_i-C(x))$ runs over all $n$ coordinates. The boundary conditions of $C_1$ hold (if some $x_j=0$ the factor vanishes; if $x_j=1$ for all $j\ne i$ then $C=x_i$ and the $i$-th factor vanishes), so only $n$-increasingness is at stake. $C_1=C$ for $C=M$.
- n-increasing means non-negative $V$-volume of every box; for polynomial $C_1$ this is equivalent to non-negativity of the mixed derivative $\partial^n C_1/\partial x_1\cdots\partial x_n$ on $[0,1]^n$.

## Known partial results

- n = 2, $C_\lambda$, $\lambda\in[0,1]$, is a family of 2-copulas — Mesiar–Komorníková–Komorník, "Perturbation of bivariate copulas", Fuzzy Sets Syst. 268 (2015) (cited as [38] in the problem paper; the paper itself NOT fetched; a catalogue record at katalog.lib.cas.cz was returned by search).
- Scout's hand calculation (UNCHECKED): for $n=3$ and $C=\Pi$ the function $C_1$ is NOT 3-increasing. $C_1=x^2y^2z+xy^2z^2+x^2yz^2-x^2y^2z^2(x+y+z)+x^3y^3z^3$ and
  $\partial_{xyz}C_1 = 4(xy+yz+zx)-12xyz(x+y+z)+27x^2y^2z^2$.
  At $(x,y,z)=(0.95,0.95,0.5)$ this equals $7.41-12.996+5.498\approx-0.088<0$; at $(1,1,t)$ it is $4-16t+15t^2$, with minimum $\approx-0.267$ at $t=8/15$. Hence for $\Pi$, $n=3$ the first question of the problem has the answer "no", and $C_\lambda=C-\lambda\prod(x_i-C)$ has density $1+\lambda(d_1-1)$, where $d_1$ is the expression above, so $\Pi$ gives a critical value $\lambda^*\le 1/(1-\min d_1)\approx0.79$ (to be computed exactly).
- For $C=M$: $C_1=M$, a copula.

## Relevant literature

- Mesiar, Komorníková, Komorník, "Perturbation of bivariate copulas" (FSS 268, 2015) — not fetched.
- Mesiar et al., "Random noise and perturbation of copulas", Kybernetika 55(2) (2019) 422–434 — surfaced by search; per the search summary it treats binary copulas only; not fetched.
- OpenAlex cites-filter on the problem paper (W2036212222), 32 citing works listed 2026-11-27, including "The unwalked path between quasi-copulas and copulas: Stepping stones in higher dimensions" (2016) — in the 2010 list's citing set, not the 2015 one; no title in the 2015 citing set addresses n-ary perturbation.

## Open-status evidence

The problem was posed in 2015. No source found that answers it. The first yes/no question appears to be settled "no" by the hand computation above, so the open content is the second part: *characterize all n-copulas C for which C_1 (equivalently the whole segment C_λ, λ in [0,1]) is an n-copula.* Evidence that this is still open is weak (absence from 32 citing-work titles; no resolution found in one web search). A literature-auditor should check the full texts of the 2019 Kybernetika paper and later perturbation papers before this is relied on.

## Novelty search coverage and limitations

2026-11-27: OpenAlex title search; OpenAlex cites-filter (32 works); two web searches (one on n-ary perturbation). Not checked: full texts of the citing works, Google Scholar, MathSciNet/zbMATH, the book chapter literature on higher-dimensional copula constructions. Whether the "no" for $\Pi$, $n=3$ is already known is unknown.

## Computational approaches

Exact polynomial arithmetic. (1) Verify the $\Pi$, $n=3$ violation by computing an explicit rational box $V_{C_1}$ (a small box around $(0.95,0.95,0.5)$) with `Fraction`. (2) Compute exactly $\lambda^*(\Pi,3)=1/(1-\min d_1)$ by solving the critical-point equations of the cubic-in-each-variable polynomial $d_1$ over $[0,1]^3$ (Sturm/resultants or interval arithmetic with rational certificates). (3) Test families of 3-copulas: FGM, Clayton/Frank-type closed forms, M, W-like shuffles of M, checkerboard copulas with $k^3$ cells (density piecewise constant, but $C_1$ is not piecewise polynomial of low degree in a uniform way; use grid of boxes plus interval/Lipschitz bounds). (4) Test $n=4,5$ with $\Pi$ and decide whether $C_1$ fails for every $n\ge3$.

## Mathematical approaches

Characterization question: since $C_\lambda=C-\lambda\prod(x_i-C)$ is affine in $\lambda$ and equals $C$ at $\lambda=0$, the admissible set of $\lambda$ for a fixed $C$ is an interval $[0,\lambda^*(C)]$ (this uses that $n$-increasingness is a linear condition on the volumes). The problem becomes computing or bounding $\lambda^*(C)$ and characterizing $\lambda^*(C)\ge1$. For absolutely continuous $C$ with density $c$ this is a pointwise inequality involving $c$ and the first and second partial derivatives of $C$. Natural conjectures to test: $\lambda^*(C)<1$ for every $n\ge3$ and every $C$ with an interior density point where $c$ is small relative to products of partials; $\lambda^*(C)\ge1$ for $C=M$ and for $n$-copulas concentrated on a set where $x_i=C(x)$ for all but one coordinate.

## Formalization feasibility

Mathlib has no copulas. Stating $n$-increasingness needs a short definition via finite sums over `Finset`/`Fin n → Bool`. The $\Pi$, $n=3$ violation is a one-box rational computation, formalizable with `norm_num`.

## Prerequisites

Copulas and their volume characterization (Nelsen, An Introduction to Copulas); mixed derivatives; polynomial optimization over a cube.

## Unverified items

- The hand calculation of $\partial_{xyz}C_1$ for $\Pi$ (derived by the scout, not executed by any program).
- Whether the violation for $n=3$ is already published.
- Full texts of [38] and of the 2019 Kybernetika paper.
- Transcription of the statement is from page images.
