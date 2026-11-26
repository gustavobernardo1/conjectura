# CJ-0004 — Liang–So–Zhang per-tensor product conjecture (with Pate's conjecture)

*Compiled 2026-11-26 from the record of a literature-scout subagent (Claude, model `claude-fable-5-2`), lightly reformatted. It is a preliminary dossier: it has not been independently audited, and every item under “Unverified items” must be checked before it is relied upon.*

## Statement

Quoted from Zhang (arXiv:1608.02844, Section 7): 'Liang-So-Zhang per-tensor product conjecture 1992 [59]. Let A and B be n x n and m x m positive semidefinite matrices, respectively. Then (per A)^m (per B)^n <= per(A \otimes B)'. Special case (Pate 1984): 'If M \in M_m is positive semidefinite and J_k is the all one matrix of size k, then (k!)^m (per M)^k <= per(J_k \otimes M) (19) which has been confirmed for k = 2 by Pate 1984 [45] and for m = 2 [59].' For k = 2 the inequality reads 2^m (per M)^2 <= per([[M, M],[M, M]]). Companion conjecture in the same section: 'Liang-So-Zhang Hadamard-Kronecker product conjecture 1992 [59]. Let A and B be n x n positive semidefinite matrices. Then (per(A \circ B))^n <= per(A \otimes B)' (proved in [59, Theorem 2] for any PSD A and special B with all diagonal entries equal and all entries above the main diagonal equal).

**Source.** Liang, So and Zhang (1992) and Pate (1984), as stated in F. Zhang, An update on a few permanent conjectures, arXiv:1608.02844 (2016), Section 7, inequality (19). <https://arxiv.org/abs/1608.02844>

**Statement checked against:** secondary-source. Statement quoted from Zhang's survey; the primary papers were not accessed and their bibliographic data were not read.

## Definitions and hypotheses

A and B are complex Hermitian positive semidefinite, of sizes n and m (possibly different); A \otimes B is the nm x nm Kronecker product; per is the permanent. For entrywise NONNEGATIVE A in M_n and B in M_m the inequality is a theorem of Brualdi 1966 (Zhang), so only PSD matrices with negative or complex entries are at issue. Sanity check: A = J_n, B = J_m gives (n!)^m (m!)^n <= (nm)!. Known weaker theorems (Zhang): Ando 1981, max{(n!)^{-m}, (m!)^{-n}} (per A)^m (per B)^n <= per(A \otimes B); Marcus 1966 with constant (n!)^{-m}(m!)^{-n}. Do not confuse with Chollet's conjecture (Hadamard product, opposite direction).

## Known partial results

- Brualdi 1966: (per A)^m (per B)^n <= per(A \otimes B) for entrywise nonnegative A, B. — As reported in F. Zhang, arXiv:1608.02844, Section 7 <https://arxiv.org/abs/1608.02844> (source fetched)
- Ando 1981 and Marcus 1966: the inequality with the weaker constants max{(n!)^{-m}, (m!)^{-n}} and (n!)^{-m}(m!)^{-n} for PSD A, B. — As reported in F. Zhang, arXiv:1608.02844, Section 7 <https://arxiv.org/abs/1608.02844> (source fetched)
- Pate's special case (19) confirmed for k = 2 (Pate 1984) and for m = 2 (Liang–So–Zhang). Zhang: 'It would be interesting for one to consider the case where M is 3 x 3 in (19) and the case where J_k is 3 x 3 in (19).' — F. Zhang, arXiv:1608.02844, Section 7 <https://arxiv.org/abs/1608.02844> (source fetched)
- A 2020 paper describes the J_k special case as proved in the case n = 2 (snippet), consistent with the 2016 status. — 'Maximizing Products of Linear Forms, and The Permanent of Positive Semidefinite Matrices', arXiv:2002.04149 (search snippet only; authors not confirmed in this session) <https://arxiv.org/abs/2002.04149> (source not fetched)

## Relevant literature

- Liang, So and Zhang (1992) and Pate (1984), as stated in F. Zhang, An update on a few permanent conjectures, arXiv:1608.02844 (2016), Section 7, inequality (19). <https://arxiv.org/abs/1608.02844>
- As reported in F. Zhang, arXiv:1608.02844, Section 7 <https://arxiv.org/abs/1608.02844>
- F. Zhang, arXiv:1608.02844, Section 7 <https://arxiv.org/abs/1608.02844>
- 'Maximizing Products of Linear Forms, and The Permanent of Positive Semidefinite Matrices', arXiv:2002.04149 (search snippet only; authors not confirmed in this session) <https://arxiv.org/abs/2002.04149>

## Open-status evidence

- Most recent source: F. Zhang, 'An update on a few permanent conjectures', arXiv:1608.02844 (9 August 2016), Section 7 'A few more open conjectures on permanent'; plus a 2020 search snippet (arXiv:2002.04149) still describing only the small special case as proved.
- URL: <https://arxiv.org/abs/1608.02844>
- Date: 2016-08-09 (latest source read in full); 2020 (snippet)
- Content: Zhang introduces the section with: 'Below are a few conjectures and research problems that virtually have no progress made in the past years. They are easily stated and understood, but appear to be forgotten.' My November 2026 web search found no proof or counterexample from 2025–2026. THIS IS THE WEAKEST OPEN-STATUS EVIDENCE IN THIS FILE: no 2024–2026 source explicitly stating the conjecture is open was found.

This is evidence that the statement was regarded as open at the stated date. It is not proof that no resolution exists.

## Novelty search coverage and limitations

Queries run:

- Pate conjecture permanent positive semidefinite "per(J_k ⊗ M)" OR "Liang-So-Zhang" OR "per(A ⊗ B)" (per A)^m (per B)^n tensor product conjecture 2025 OR 2026 proof OR counterexample

Sources checked:

- General web search (1 dedicated query)
- F. Zhang survey arXiv:1608.02844 (PDF pages 1–13 read)

Limitations: Only one targeted query; no arXiv listing search, no citation trawl of the 1992 paper or of Pate 1984, no check of the Cheon–Wanless / Wanless open-problem updates. 2026 saw many unrefereed computer-assisted preprints on neighbouring permanent conjectures (Chollet, Lieb, a Pate–Wanless question per a snippet about preprints.org 202609.2464), so this one may have been attacked without my search surfacing it. Treat 'open' as probable, not established.

## Computational approaches

Exact evaluation is easy: per(A \otimes B) is an nm x nm permanent (Ryser/Glynn, about nm * 2^{nm} operations; exact up to nm around 25 on a desktop, e.g. (n,m) = (3,3), (3,4), (4,4), (3,5), (5,5)). Counterexample search: minimize per(A \otimes B) / ((per A)^m (per B)^n) over PSD A, B given as Gram matrices of low-rank complex or real vectors (start with rank 2 and with matrices having many negative entries, since nonnegative matrices are covered by Brualdi). First open cases suggested by the survey: Pate's inequality (19) with M of size 3 x 3 and k = 3 (a 9 x 9 permanent that is an explicit polynomial in the entries of M), then k = 3 with general m, then M 3 x 3 with general k. For fixed small sizes the inequality is a polynomial inequality in the Gram-vector coordinates and may admit an SOS certificate verifiable in exact arithmetic.

## Mathematical approaches

Symmetric tensor interpretation: for A = V*V the permanent is the squared norm of the symmetrized tensor v_1 ∨ ... ∨ v_n, and per(A \otimes B) is the squared norm of the symmetrization of the nm vectors v_i \otimes w_j; the conjecture compares it with a product of norms (a Brascamp–Lieb / Lieb-inequality flavour). Lieb's inequality per A >= per A_11 per A_22 applied to block structure of J_k \otimes M gives weaker constants; Pate's k = 2 proof and the Liang–So–Zhang m = 2 proof are the templates to generalize; induction on k via per-in-per (Marcus) type statements; expansion formulas for per(J_k \otimes M) as sums over k-regular 'transport' patterns weighted by products of entries of M.

Scout's tractability assessment: Probably the most approachable of the permanent conjectures: the survey itself names the next small cases (M of size 3x3, or k = 3) and says there has been virtually no progress, so either a numerical counterexample or a proof of a new small case would be a genuine, publishable partial result, and the computations fit easily on one PC. The main risk is status: the open-status evidence is from 2016 (plus a 2020 snippet); a proper citation search must precede any work.

## Formalization feasibility

Not checked in this session. From memory: Mathlib has Matrix.permanent, Matrix.PosSemidef and the Kronecker product (Matrix.kronecker), so the statement is directly expressible in Lean 4; a proof of a fixed small case would be a polynomial inequality certificate.

## Prerequisites

Positive semidefinite matrices and Gram factorizations, permanents (Ryser/Glynn formulas, Laplace-type expansions), Kronecker products, symmetric tensor powers, Lieb's and Marcus's permanent inequalities, numerical optimization, SOS certificates.

## Unverified items

- Full names, title and journal of reference [59] (Liang, So, Zhang 1992) and of Pate 1984: not read.
- Whether any progress occurred between 2016 and 2026 beyond what the single search surfaced.
- Authors of arXiv:2002.04149 and the exact content of its remark (snippet only).
- The preprints.org 202609.2464 item (a Pate–Wanless question, snippet only) is a different inequality according to the snippet; not fetched.
- Mathlib API names quoted from memory.
