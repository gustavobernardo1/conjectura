# CJ-0037 — Existence of left-continuous t-norms on a given (finite) bounded lattice

*Compiled 2026-11-27 by the problem-scout subagent (model claude-sonnet-5-5). Not audited. Statement quotations were returned by a model-summarised fetch of the arXiv HTML page and must be re-read verbatim from the paper before use.*

## Statement

The problem is posed in He and Wang, "Left-continuous pseudo-t-norms on modular lattices", arXiv:2506.07567v1 (submitted 9 June 2025; published as Fuzzy Sets and Systems, DOI 10.1016/j.fss.2026.109847 per OpenAlex). Section 1 poses two problems (as reported by the fetch):

1. "for an arbitrarily given complete lattice, the question of whether a left-continuous t-norm exists on it remains open"
2. "what are the specific structural characterizations of the lattice in which left-continuous t-norms" (sentence truncated by the fetch; exact wording not captured).

A second paper by the same authors (arXiv:2601.07146v1, 12 January 2026) repeats: "However, the structure of left-continuous t-norms on complete lattices remains an open problem."

**Source.** arXiv:2506.07567v1, https://arxiv.org/html/2506.07567v1, Section 1 (no statement number).

**Statement checked against:** primary-source (arXiv HTML, but through a summarising fetch; verbatim wording to be re-checked).

### The yes/no form proposed for the project (a DIFFERENT, finite statement)

The published problem is a "characterize" problem and cannot be refuted as stated. For a finite bounded lattice L the existence question is a finite decision problem. Candidate yes/no questions that a computation can settle by one explicit object:

- (Q-a) Is the necessary condition "L is 1-distributive" (their Proposition 4.3) also sufficient for a finite *modular* lattice to admit a left-continuous t-norm? The paper gives S_{7,2}: 1-distributive, no left-continuous pseudo-t-norm (Example 4.1, as reported), so sufficiency fails for general finite 1-distributive lattices; whether it holds for modular ones is not stated in the fetched text.
- (Q-b) For the smallest finite lattice that admits a left-continuous pseudo-t-norm but no left-continuous t-norm (their Example 5.1 shows one exists), is the class of finite lattices admitting a t-norm equal to a recognisable class (e.g. lattices of order ideals / finite quantale-frames)? This would be a new conjecture, to be formulated from data, and must be recorded as a new statement.

## Definitions and hypotheses

(As reported from the paper.)

- t-norm on a bounded lattice L: T:L^2 -> L with T(1,a)=a, monotone, commutative, associative.
- pseudo-t-norm: T(1,a)=a and T(0,a)=0, monotone; the paper also assumes commutativity.
- left-continuous: T(a, join S) = join over s in S of T(a,s) for every a and every non-empty S subset of L. On a finite lattice this is join preservation in each argument for non-empty joins.
- 1-distributive: defined in the paper; definition not captured.
- Easy fact (my inference, not from the paper): a finite lattice with a left-continuous t-norm is an integral commutative residuated lattice, hence T(a,b) <= a meet b. M_3 admits none: a*(b join c) = a*1 = a but a*b, a*c <= a meet b = 0.

## Known partial results

- Prop. 4.3: existence of a join-distributive pseudo-t-norm implies L is 1-distributive. Theorem 4.1: for complete atomistic lattices with top, equivalent: 1-distributive; isomorphic to 2^A; continuous t-norm; left-continuous t-norm; left-continuous pseudo-t-norm. Lemma 4.1: a finite modular lattice with such a pseudo-t-norm has no 1-sublattice M_3, M_{3,2}, M_{3,4}. (fetched, summarised)
- He, Wang, "Triangular norms on finite lattices", arXiv:2412.04944 (6 Dec 2024), Fuzzy Sets Syst. 522 (2026) 109609: t-norms on non-Boolean atomistic lattices are not left-continuous; T_M is the only left-continuous t-norm on an atomistic Boolean lattice. (abstract fetched)
- OpenAlex lists "General and left-continuous operators on lattice-based sums" (Fuzzy Sets Syst., 2025, DOI 10.1016/j.fss.2025.109706); not fetched.

## Relevant literature

- https://arxiv.org/abs/2506.07567 (He, Wang)
- https://arxiv.org/abs/2601.07146 (He, Wang, 2026)
- https://arxiv.org/abs/2412.04944 (He, Wang)

## Open-status evidence

arXiv:2601.07146v1 (12 January 2026): "However, the structure of left-continuous t-norms on complete lattices remains an open problem." arXiv:2506.07567 (June 2025) states the existence question is open. OpenAlex (2026-11-27) shows 0 citations for the published version of 2506.07567, so no citing paper resolving it was found there; this is weak evidence only.

## Novelty search coverage and limitations

2026-11-27: one web search, three arXiv page fetches, one OpenAlex title search. Not checked: Semantic Scholar, zbMATH, citations of 2601.07146, the full text of either paper, the literature on commutative integral quantales/residuated lattices on small lattices (which may already enumerate such structures, e.g. residuated-lattice enumeration papers; not searched). A search of that literature is the first task: the finite existence question may be a corollary of known enumerations of finite integral commutative residuated lattices.

## Computational approaches

Enumerate non-isomorphic lattices (counts grow fast; lattices on up to about 12 to 14 elements are feasible), and for each decide by SAT/CSP whether a commutative associative join-preserving operation with unit 1 exists. Exact, finite, cheap for n <= 10. Output: the list of lattices admitting a t-norm, a conjectured characterisation, minimal obstructions.

## Mathematical approaches

Identify the structure with an integral commutative quantale on L; use known theory of residuated lattices (divisibility, local finiteness) to relate to 1-distributivity. Seek the minimal forbidden sublattices (as in the paper's Lemma 4.1).

## Formalization feasibility

Mathlib has lattices, `CompleteLattice`, and commutative quantale-like structure (`IsQuantale` / `CommSemigroup` with `CompleteLattice`) only partially. A finite instance can be stated and verified by `decide` on an explicit table (no `native_decide`). Medium.

## Prerequisites

Lattice theory (modular, distributive), residuated lattices/quantales, SAT encodings.

## Unverified items

All quotations are summariser output. The definition of 1-distributive, Example 4.1, Example 5.1 and Section 1's second problem were not read verbatim. Whether the problem is open for *finite* lattices (rather than only a general characterisation) is unverified; it may be already decidable by enumeration in the quantale literature. Journal DOI from OpenAlex only.

## Appendix: second scout dossier (merged 2026-11-27)

A second scout (scout E, same session) independently proposed the same problem as CJ-0043; that ID is not used. Its dossier follows, headings demoted.

### CJ-0043 — Existence of left-continuous t-norms on finite lattices (1-distributivity versus t-norm versus pseudo-t-norm)

*Compiled 2026-11-27 by the problem-scout subagent (model Sonnet 5.5). Not audited. Every quotation below comes from a page fetched in this session through a model-summarised fetch tool, so quotations were relayed by a summariser and should be re-read in the source before use.*

### Statement

Published open question (He and Wang, arXiv:2506.07567v1, Introduction, as relayed by the fetch tool):

- "the question of whether a left-continuous t-norm exists on it remains open." (here "it" is an arbitrarily given complete lattice)
- "what are the specific structural characterizations of the lattice in which left-continuous t-norms" (resp. pseudo-t-norms) "exist?"
- "the problem regarding the existence of left-continuous t-norms (resp. pseudo-t-norms) on a complete lattice is in urgent need of resolution."

The Conclusion says the paper "just partly answer[s] the two questions raised in Section 1."

Published facts, as relayed from arXiv:2506.07567v1:

- Definition 4.1: "An element c of L is called 1-distributive if, for any a, b in L, a v b = 1 implies c ^ (a v b) = (c ^ a) v (c ^ b)." A lattice is 1-distributive when each element is.
- Proposition 4.3: "Let L be a bounded lattice. If there exists a v-distributive pseudo-t-norm on L then L is 1-distributive." (Remark 2.1: for finite lattices v-distributive = left-continuous.)
- Theorem 5.1 (finite rectangular modular lattices): 1-distributive iff distributive iff there is a continuous t-norm iff a left-continuous t-norm iff a left-continuous pseudo-t-norm.
- Theorem 5.2 (finite planar modular, exactly one bi-irreducible element on a boundary chain): 1-distributive iff there is a v-distributive pseudo-t-norm. Example 5.1 is a lattice satisfying the hypotheses of Theorem 5.2 where the constructed T "is not a t-norm since T(T(f, g), h) = T(f, h) = a != 0 = T(f, e) = T(f, T(g, h))".
- Theorem 4.1 (complete atomistic lattices): 1-distributive iff left-continuous t-norm exists iff left-continuous pseudo-t-norm exists.

**Yes/no sub-questions formulated by the scout (not stated as conjectures in the source).** For finite bounded lattices L:

- (Q1) Does 1-distributivity of L imply the existence of a left-continuous (join-preserving in each argument) commutative pseudo-t-norm on L? (Converse of Proposition 4.3.)
- (Q2) Does the existence of a left-continuous pseudo-t-norm on L imply the existence of a left-continuous t-norm on L (associativity added)? (Theorem 5.1 says yes for rectangular modular lattices; Example 5.1 suggests the constructed pseudo-t-norm need not be associative.)

A "no" to either would be settled by one finite lattice given by its order relation, plus, for a "no" to Q2, a verified pseudo-t-norm table and a proof (or SAT-certified UNSAT) that no associative one exists; for Q1 a 1-distributive lattice with a certified UNSAT for join-preserving pseudo-t-norms.

**Source.** P. He, X.-p. Wang, "Left-continuous pseudo-t-norms on modular lattices", arXiv:2506.07567v1 (9 June 2025), https://arxiv.org/html/2506.07567v1; OpenAlex lists a journal version, Fuzzy Sets and Systems, DOI 10.1016/j.fss.2026.109847, publication date 2026-02-26 (journal page not opened).

**Statement checked against:** primary-source (arXiv HTML), via a summarising fetch tool; wording of Definition/Theorem statements should be re-read.

### Definitions and hypotheses

Pseudo-t-norm (Definition 2.1, as relayed): T: L^2 -> L with T(1,a)=a, T(0,a)=0, monotone in the second argument; the paper also assumes commutativity. t-norm: additionally associative. Left-continuous: T(a, join S) = join of T(a,s) for all nonempty S. On a finite lattice this is "preserves binary joins in each argument" (plus T(a,0)=0 here since T(0,a)=0 is part of the pseudo-t-norm axioms). Note that T(0,a)=0 is an axiom for pseudo-t-norms but is a consequence for t-norms. Hand check: M3 admits no left-continuous t-norm (T(a,1)=T(a,b v c)=T(a,b) v T(a,c) <= (a^b) v (a^c)=0, but T(a,1)=a); this is consistent with M3 not being 1-distributive. (Scout's hand computation, not from a source.)

### Known partial results

- Theorems 4.1, 5.1, 5.2 and Proposition 4.3 of arXiv:2506.07567v1 (fetched, relayed).
- arXiv:2601.07146v1 (He, Wang, 12 Jan 2026): "the structure of left-continuous t-norms on complete lattices remains an open problem"; gives constructions for semi-linear sums; Conclusions: "It is regrettable that we do not delve further into the construction of left-continuous t-norms on complete lattices" that do not admit a semi-linear-sum representation. (fetched)
- arXiv:2412.04944v1 (He, Wang, 6 Dec 2024), "Triangular norms on finite lattices": the question "is it possible to construct t-norms for all finite lattices?" is answered positively (non-left-continuous t-norms). A search summary (not the page) said every t-norm on a non-Boolean atomistic lattice is not left-continuous. (fetched)

### Relevant literature

- https://arxiv.org/html/2506.07567v1
- https://arxiv.org/html/2601.07146
- https://arxiv.org/html/2412.04944v1

### Open-status evidence

2026-01-12: arXiv:2601.07146 says the structure of left-continuous t-norms on complete lattices "remains an open problem". The specific sub-questions Q1 and Q2 are not asserted open anywhere; they are the scout's formulation, and the sources never state them as conjectures. OpenAlex (2026-11-27) shows 0 citations for both 2506.07567 (journal record) and 2601.07146, so no later resolution is indexed there.

### Novelty search coverage and limitations

Searched 2026-11-27: the web search tool (several queries on left-continuous t-norms on lattices, 1-distributive), arXiv HTML of the three He-Wang papers, OpenAlex title search for citation counts. NOT checked: Semantic Scholar, MathSciNet/zbMATH, the journal version of 2506.07567 (it may differ from v1), older literature on residuated structures on finite lattices (for example work on which lattices are reducts of residuated lattices or on integral commutative residuated lattices with given lattice reduct), Google Scholar. The classical residuated-lattice literature may already decide Q1 or Q2 for finite lattices; this is a serious risk.

### Computational approaches

Enumerate finite lattices up to 10 to 12 elements (counts of lattices: 1, 1, 1, 2, 5, 15, 53, 222, 1078, 5994, 37622 for n=1..11, quoted from memory, unverified). For each: test 1-distributivity; SAT-decide existence of a join-preserving commutative pseudo-t-norm (n^2 variables of domain n, constraints local); SAT-decide existence of a join-preserving commutative associative t-norm (cubic associativity constraints, n^3 clauses). Compare. Any lattice with 1-distributive and UNSAT, or pseudo-SAT and t-norm-UNSAT, is a counterexample to Q1 or Q2; a proof-checked table or certificate is then re-verified by an independent checker. If neither occurs up to n=11, the data suggest a conjecture (not a proof) and a smallest failing lattice class for generalisations.

### Mathematical approaches

Q1: attempt to build T from a 1-distributive structure (the papers do this for atomistic and planar modular classes); search for a general obstruction in the non-modular case. Q2: associativity is the likely obstruction; compare with Example 5.1.

### Formalization feasibility

Finite lattices, join-preservation and associativity are easy to state in Lean 4 with Mathlib (`Lattice`, `Fintype`); a refuting finite lattice could be checked by `decide` over a concrete type, without `native_decide`.

### Prerequisites

Lattice theory (modularity, join-irreducibles), residuated lattices, SAT encoding.

### Unverified items

All quotations are summariser-relayed. The journal version was not opened. The enumeration counts of lattices are from memory. Whether Q1 and Q2 are already decided in classical literature is unknown. The hand computation for M3 is the scout's own.
