# CJ-0016 — Klement–Mesiar Conjecture 3.2: L_p-Lipschitz Archimedean t-norms

*Compiled 2026-11-27 by the problem-scout subagent (model claude-sonnet-5-5). Not audited. The "Mathematical approaches" section contains a hand derivation by the scout that has NOT been checked by any program or reviewer.*

## Statement

Verbatim from the primary source (pp. 227 of the paper; read from the page images of the PDF):

> "Problem 3.1. (R. Mesiar) Characterize all t-norms which are 1-Lipschitz (or, generally, k-Lipschitz with k >= 1) with respect to the L_p-norm for p in ]1, infinity[."
>
> "Observe that in the case p = 1, the 1-Lipschitz property of an Archimedean t-norm is equivalent to the convexity of its additive generator, see [23] and [17, 26]."
>
> "Conjecture 3.2. An Archimedean t-norm T is 1-Lipschitz with respect to the L_p-norm if and only if each of its additive generators is a p-power of a convex function."

(Transcription from page images; the typeset text uses the symbol for infinity and "≥".) Context quoted from the same page: an Archimedean continuous t-norm is $T(x,y)=t^{(-1)}(t(x)+t(y))$ with $t:[0,1]\to[0,\infty]$ continuous, strictly decreasing, $t(1)=0$, and $t^{(-1)}(u)=t^{-1}(\min(u,t(0)))$.

**Source.** E. P. Klement, R. Mesiar, "Open problems posed at the Eighth International Conference on Fuzzy Set Theory and Applications (FSTA 2006, Liptovský Ján, Slovakia)", Kybernetika 42 (2006), no. 2, 225–235, Conjecture 3.2 (page 227). URL: https://dml.cz/bitstream/handle/10338.dmlcz/135710/Kybernetika_42-2006-2_7.pdf (fetched 2026-11-27).

**Statement checked against:** primary-source.

## Definitions and hypotheses

- 1-Lipschitz w.r.t. the $L_p$-norm is read as: $|T(x,y)-T(x',y')|\le (|x-x'|^p+|y-y'|^p)^{1/p}$ for all points of $[0,1]^2$ (the paper does not spell this out; this is the standard meaning and should be confirmed). The conjecture does not restate the range of $p$; Problem 3.1 uses $p\in\,]1,\infty[$. $p=1$ is the case said to be known.
- "p-power of a convex function": read as $t=h^p$ with $h:[0,1]\to[0,\infty]$ convex (necessarily non-increasing, $h(1)=0$). Not defined in the source; confirm with the authors' references [23], [17], [26] (not fetched).
- Additive generators of a continuous Archimedean t-norm are unique up to a positive multiplicative constant, and $c\,t=(c^{1/p}h)^p$, so "each" and "some" generator coincide.

## Known partial results

- p = 1: Lipschitz iff additive generator convex — stated in the problem paper, citing [23], [17], [26] — (source: the paper fetched; the cited works not fetched).
- Scout's hand derivation (unchecked) that the direction "generator is a p-th power of a convex function ⇒ L_p-Lipschitz" holds for smooth generators, and that the converse direction appears to fail; see below.

## Relevant literature

- Klement, Mesiar, Pap, "Convexity conditions on t-norms and their additive generators" (listed by OpenAlex among works citing the 2004 KMP problem paper; Fuzzy Sets and Systems 2004; DOI 10.1016/j.fss.2004.05.005; NOT fetched).
- Klement, Mesiar, Pap, "Triangular Norms", Kluwer 2000 (not fetched).
- Page of citing works of the 2006 problem paper (OpenAlex, W2224096457, fetched 2026-11-27): 15 works; none has a title about Lipschitz t-norms (titles concern fuzzy implications, law of importation, t-subnorms, FSTA problem lists).

## Open-status evidence

The only evidence is the 2006 statement itself. No recent source stating the conjecture is open was found. The scout's score for `open_evidence` is therefore 1, below the gate of 2, until a literature-auditor finds either a recent restatement or a resolution. A web search (2026-11-27) for resolutions found nothing but could not check full texts; two arXiv hits (2601.10756, 2609.11150) were returned for the query and not opened.

## Novelty search coverage and limitations

Queries (2026-11-27): OpenAlex title search for the problem papers; OpenAlex cites-filter for the 2006 problem paper (15 citing works); two general web searches. NOT checked: Google Scholar, MathSciNet/zbMATH, the books "Triangular Norms" (2000) and "Associative Functions" (2006), Mesiar's own later papers on Lipschitz aggregation functions, the arXiv hits above, other-language literature. A failed search is not evidence that the conjecture is unresolved.

## Computational approaches

Exact rational arithmetic suffices. A candidate counterexample generator is piecewise quadratic (below); one can (i) verify symbolically that the generator is continuous and strictly decreasing, (ii) verify the dual-gradient inequality piecewise, (iii) cross-check by an exact rational grid test of $|T(z)-T(z')|^{p}$ for $p=2$ (note $T$ involves a square root, so use exact algebraic numbers or squared comparisons), (iv) verify non-convexity of $\sqrt{t}$ at explicit rational points.

## Mathematical approaches

Scout's derivation (UNCHECKED, for the experimenter and reviewer to test). Let $q=p/(p-1)$. For a differentiable Archimedean $T$ with generator $t$, set $g=-t'>0$. Then $T_x=t'(x)/t'(T)$, so $T$ is 1-Lipschitz for $L_p$ iff $g(x)^q+g(y)^q\le g(T(x,y))^q$ wherever $T>0$ (the $L_q$-norm of the gradient is at most 1).
Put $u=t(x)$, $v=t(y)$ and $G(u)=g(t^{-1}(u))^q$. The condition becomes: $G(u)+G(v)\le G(u+v)$ for $u,v\ge0$, $u+v\le t(0)$, i.e. $G$ is superadditive.
If $t=h^p$ with $h$ convex, then $G(u)=p^q\,u\,|h'|^q$ and $G(u)/u$ is non-decreasing in $u$ (since $|h'|$ is non-increasing in $x$ and $u$ is decreasing in $x$); this implies superadditivity, so "if" holds in the smooth case.
Conversely, convexity of $h$ is *equivalent* to "$G(u)/u$ non-decreasing", which is strictly stronger than superadditivity. A superadditive $G$ with non-monotone ratio is $G(u)=u+\varepsilon\lfloor u/\varepsilon\rfloor$ (sum of additive and superadditive; the ratio at $u=2\varepsilon$ is $2$ and at $u=1.9\varepsilon$ is $1.526\ldots<2$). For $p=2$ the ODE $t'=-\sqrt{G(t)}$ with $t(1)=0$ gives on each level $k\varepsilon\le t<(k+1)\varepsilon$ the piecewise-quadratic solution $\sqrt{t+k\varepsilon}=c_k-x/2$, with $c_k$ fixed by continuity at the level crossings. This $t$ is continuous, strictly decreasing, and its $T$ would be 1-Lipschitz for $L_2$ while $\sqrt t$ is not convex. If correct, this refutes the "only if" half of Conjecture 3.2 for $p=2$ (and the same construction with $G=g^q$ works for every $p>1$), and yields a corrected statement: *an Archimedean t-norm is 1-Lipschitz for $L_p$ iff $(−t'\circ t^{-1})^q$ is superadditive* (for differentiable generators). Points to check: behaviour at kinks and at the boundary $T=0$, the case of non-differentiable generators, the precise meaning of "p-power", and whether the literature already contains this correction.

## Formalization feasibility

Mathlib has convex functions, Lipschitz maps and real $L_p$ norms on `EuclideanSpace`/`PiLp`. Defining t-norms and additive generators is a short development. A formal proof of a specific counterexample is feasible but the ODE construction needs care; a direct explicit piecewise-quadratic definition is easier.

## Prerequisites

Triangular norms and additive generators (Klement–Mesiar–Pap, Triangular Norms, chapters 3 and 5); dual norms and Lipschitz functions; superadditive functions.

## Unverified items

- The transcription of the statement is from page images, not machine text.
- Meaning of "p-power of a convex function" and of "1-Lipschitz w.r.t. the L_p-norm" (not defined in the source).
- Everything in "Mathematical approaches" is an unchecked hand derivation.
- Whether the conjecture has been resolved or restated since 2006 (not established).
- References [17], [23], [26] of the problem paper (not fetched).

## Director's note, 2026-11-27

A web search (one query) found the record of A. Mesiarová(-Zemánková),
"k-lp-Lipschitz t-norms", International Journal of General Systems (2007)
(dblp key `journals/ijgs/Mesiarova07`; abstract seen only through an
aggregator page, <https://manuscript.isc.ac/Inventory/10/1182442.htm>). Per that
abstract, k-l_p-Lipschitz t-norms are ordinal sums of k-l_p-Lipschitz
Archimedean t-norms, and their additive generators are characterised by
"k-p-convexity". If that characterisation differs from "p-power of a convex
function", Conjecture 3.2 is already decided by it. The full text was not
read. Until it is, CJ-0016 stays below the open-evidence gate and no work
should start on it.
