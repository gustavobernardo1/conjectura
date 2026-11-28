# Independent review — CJ-0024 — Theorem C (rescaled left-continuous t-norms with the drastic boundary)

- **Reviewer:** `claude-opus-5-5` (Claude Code subagent, role `adversarial-reviewer`).
- **Date:** 2026-11-27 (about 23:40 to 00:00 local time).
- **Independence:** fresh subagent context. It was given the task statement, the
  paths of the claim and of the primary sources, and a list of points to
  assess. It was not given the author's reasoning trail or conclusion. **The
  reviewer is the same model as the author (`claude-opus-5-5`)**, so
  independence is limited to the context and does not extend to the model. The
  reviewer read the primary sources before the proof. It did not read the
  earlier review `reviews/2026-11-27-review-1.md` or the recheck
  `reviews/2026-11-27-recheck-r2.md`. While this review was running, the
  repository moved and the reviewer saw the diff between revisions 1 and 2 of
  `weber-uniqueness.md`. The reading caveat on Problem 4.5(ii) below (row
  "Novelty coverage", item 2) was found before that diff was seen; the diff
  shows that review-1 (its G2) reached the same conclusion on its own.
- **Revision reviewed:**
  - Claim: `research/active/CJ-0024-sn-r-nonborder-intersection/notes/rescaled-tnorms.md`,
    revision 1, SHA-256 `77385d89d9d58a8e6dbde2e5ffe4f68cb04d28830f6a1603d32fa0a9797ccae5`.
    At the start of the review this was an untracked working-tree file on branch
    `research` with `HEAD = e23d59c8b8e1d93e91058e3027b75cdafd6cec97`. During the
    review the same bytes (same SHA-256) were committed in
    `88d33c6cc01800a2466de80d8b537f7f32613c25`. At the end, `HEAD` was
    `a9562254877cdb496d765823bad511d78571592e`, and the file was unchanged there.
  - Dependencies (definitions and Lemmas 1, 2, 4): `notes/weber-uniqueness.md`
    revision 1, SHA-256 `6c004c91d0e65a07518e4e7edaa0b878307510c3e64de2e1c8b20ab45d70f155`.
    It is now kept byte-identical as `notes/versions/weber-uniqueness-r1.md`.
    The current file is revision 2 (`48686378da728f0260db61f813714c5be0cfc09239f897988f643d0af337753d`).
    The block running from "**Lemma 1" to "**Proof of Theorem A" is identical
    in both revisions (SHA-256 of the extracted block in both:
    `ada5c5e2bb78222d7f720d417e969b44f312ed33af608549aad8e86a1210fa31`).
  - Author check script: `experiments/CJ-0024-sn-r-nonborder-intersection/check_theorem_c.py`,
    SHA-256 `6bcad128546ad35896d082007ed287b58782b4deb2f1d5704f4a2b55477f9ad8`.
- **Material given to the reviewer:** the task message (claim path, dependency
  note, the primary sources and points to assess). Primary sources read
  directly, with their local copies:
  - M. Baczyński, B. Jayaram, *QL-implications: some properties and
    intersections*, FSS 161 (2010) 158–188, author PDF, SHA-256
    `e153075c…59cd29`, and its text extraction.
  - M. Baczyński, B. Jayaram, *Fuzzy Implications: Some Recently Solved
    Problems*, STUDFUZZ 300 (2013) 177–204, author PDF, SHA-256
    `caf6cb73…9434a7`, and its text extraction.

## Statement as read from the primary source

Written before reading the proof.

**Definitions (2013 chapter and 2010 paper).**
- A *fuzzy negation* is a non-increasing N with N(0) = 1 and N(1) = 0 (2010,
  Def. 2.1). It is *strong* if N∘N = id.
- A *fuzzy implication* (2013, Def. 2.1) satisfies (I1) non-increasing in x,
  (I2) non-decreasing in y, and I(0,0) = I(1,1) = 1, I(1,0) = 0.
- An *(S,N)-implication* (2013, Def. 2.11) is I = S(N(x), y) for some t-conorm
  S and some fuzzy negation N; no continuity is required. It is called an
  S-implication when N is strong.
- An *R-implication* (2013, Def. 3.1) is I_T(x,y) = sup{t : T(x,t) ≤ y} for a
  t-norm T; no continuity is required.
- (RP), 2013 p. 188: T(x,z) ≤ y ⟺ I_T(x,y) ≥ z for all x, y, z holds iff T is
  left-continuous.
- *Border-continuous* (2013, Def. 3.3): continuous on [0,1]² \ ]0,1[². The
  reading that makes Proposition 3.4 non-trivial (T border-continuous ⟺ I_T
  satisfies (OP)) is continuity of T, as a function on [0,1]², at every
  boundary point. Every t-norm restricted to the boundary is min, hence
  continuous.
- A *QL-operation* (2010, Def. 4.1) is S(N(x), T(x,y)) for a t-norm T, a
  t-conorm S and a fuzzy negation N. A QL-implication is a QL-operation that is
  a fuzzy implication. Earlier works required N to be strong (2010, Remark 4.22).
- *De Morgan triple* (2010, Def. 2.24): (T,S,N) with N strict,
  T = N⁻¹(S(N,N)) and S = N⁻¹(T(N,N)). By Thm. 2.25 this is equivalent to N
  strong and S the N-dual of T.

**Theorem 5.13 of the 2010 paper (= [4, Thm. 6.2]), exact hypotheses.** Let T
be a left-continuous t-norm, S a t-conorm and N a fuzzy negation. Then
I_T = I_{S,N} if and only if N = N_T is strong and (T, N, S) is a De Morgan
triple.

**Corollary 2.15 (2010).** For any t-norm T: N_T strictly decreasing ⟺
continuous ⟺ strict ⟺ strong.

**Problems.**
- 2013 Problem 4.2(i): is there an I ≠ I_WB that is an (S,N)-implication and
  an R-implication of a non-border-continuous t-norm, and is not the residual
  of any left-continuous t-norm?
- 2013 Problem 4.5(ii) (= 2010 Problem 9.4(ii)): is I_WB the only
  QL-implication that is also an R-implication obtained from a
  non-left-continuous t-norm?
- 2010 Section 7 shows I_QL ∩ I_TLC = I_{S,N} ∩ I_TLC (Theorem 7.2) and
  records I_WB ∈ I_QL \ I_TLC (Fig. 3).

**Claim (Theorem C, as stated in the note).** Hypotheses:
- T₀ is a left-continuous t-norm whose natural negation N₀ is strong, with
  fixed point e.
- S₀ is the N₀-dual of T₀.
- 0 < a < 1, and ψ : [0,1] → [0,a] is an increasing bijection.

Defined objects: T is the drastic-boundary extension of
M(x,y) = ψ⁻¹(T₀(ψx, ψy)); N(x) = ψ⁻¹(min(a, N₀(ψx))) for x < 1, N(1) = 0;
S = ψ⁻¹∘min(a, S₀(ψ·, ψ·)).

Claims:
1. T is a t-norm, S a t-conorm and N a fuzzy negation.
2. The residual of T is given by a closed formula.
3. I_T = S(N(x), y) = S(N(x), min(x,y)).
4. If a ≤ e, then I_T = I_WB.
5. If e < a < 1, then:
   - I_T(x,0) = 1 for 0 < x ≤ ψ⁻¹(N₀(a)), so (OP) fails and I_T is not the
     residual of any left-continuous t-norm;
   - T is not border-continuous;
   - I_T ≠ I_WB.

The claim is about objects of the same type as in the sources' definitions.
Under those definitions, part 5 yields elements of
I_{S,N} ∩ I_QL ∩ (I_T \ I_TLC) other than I_WB. That is the set of Problem
4.2(i), and of Problem 4.5(ii) under its strong reading (see the
"Novelty coverage" row).

## Findings

| Item | Finding |
| --- | --- |
| Hypotheses | **No gap.** (a) *"Left-continuous with strong natural negation" is exactly what (F1), (F2), (F5) use.* (F1) is (RP), which holds iff T₀ is left-continuous (2013 p. 188). (F5) uses only (F1) at value 0. (F2) needs left-continuity, N₀ = N_{T₀} strong, and S₀ the N₀-dual. With N₀ strong, Def. 2.24 / Thm. 2.25 make (T₀, N₀, S₀) a De Morgan triple, so direction (ii)⇒(i) of Thm. 5.13 applies; its hypotheses (left-continuous T, any t-conorm, any negation) are met. I also re-derived (F2) without the citation. For all t: t ≤ N₀(T₀(x, N₀y)) ⟺ T₀(x, N₀y) ≤ N₀t ⟺ T₀(T₀(x,N₀y), t) = 0 ⟺ T₀(T₀(x,t), N₀y) = 0 ⟺ T₀(x,t) ≤ y. This uses T₀(w,s) = 0 ⟺ s ≤ N₀(w), which holds by left-continuity; associativity; commutativity; and involutivity. Hence I_{T₀}(x,y) = N₀(T₀(x,N₀y)) = S₀(N₀x, y). (b) *The fixed point e is well defined.* A strong negation is a continuous, strictly decreasing bijection, so x ↦ x − N₀(x) is strictly increasing from −1 to 1 and has exactly one zero, which lies in ]0,1[. (c) *ψ.* The statement does not assume continuity. It is automatic, because a monotone bijection between intervals has no jumps, and it forces ψ(0) = 0 and ψ(1) = a. The proof only needs ψ(t) ≤ r ⟺ t ≤ ψ⁻¹(r) for r ∈ [0,a], which holds for any strictly increasing bijection. Minor presentational point, not a gap: part 2 says "ψ is a continuous increasing bijection" without noting that continuity is automatic. (d) The hypotheses are not vacuous: T_L, T_nM, φ-conjugates of T_L, nilpotent minima for other strong negations, and Jenei's rotation of the product all qualify (several were checked below). |
| Quantifiers | **No gap.** The theorem is universal over (T₀, a, ψ) satisfying the hypotheses. Parts 1–3 hold for every a ∈ ]0,1[, part 4 for a ≤ e, part 5 for e < a < 1. The existential "such x exist" in part 5 is justified: N₀(a) < a (by F4) and ψ maps onto [0,a], so ψ⁻¹ of any point of ]N₀(a), a[ is an admissible x < 1. |
| Mathematical definitions | **No gap.** T, S, N, I_T, (S,N)- and QL-implication, border-continuity and (OP) are used in the sources' sense (see above). **Well-definedness:** ψ⁻¹ is applied only to values in [0,a]. For x, y < 1, T₀(ψx,ψy) ≤ min(ψx,ψy) < a. min(a, N₀(ψx)) and min(a, S₀(ψp,ψq)) lie in [0,a]. The ranges are [0,1]. **Border-continuity:** part 5 exhibits a jump of T along the interior segment t ↦ (x,t), t → 1⁻, at the boundary point (x,1). This defeats border-continuity under the joint-continuity reading, and also under the weaker reading "T(x,·) continuous at 1". It does not defeat it under the trivial reading "restriction to the boundary is continuous". That reading would make every t-norm border-continuous, contradict 2013 Prop. 3.4 (T_D is not border-continuous), and cannot be meant. **Representations are forced:** the negation of any (S,N)- or QL-representation is N(x) = I(x,0) (2010 Prop. 4.2), so it must be the N of the note. For e < a < 1 this N equals 1 on [0, ψ⁻¹(N₀(a))] and jumps at 1, so it is neither continuous nor strong. I_T is therefore an (S,N)- and a QL-implication in the sense of 2013 Def. 2.11 and 2010 Def. 4.1, but it is **not** an S-implication, and not a QL-implication under the older convention that requires a strong N (2010 Remark 4.22). The note makes no claim under those conventions; this is recorded only to fix the scope. |
| Boundary cases | **No gap.** All of the following were checked by hand. **x = 1:** I_T(1,y) = y = S(0,y) = S(0, min(1,y)) (S(0,y) = ψ⁻¹(min(a, ψy)) = y). **x = 0:** ψ0 = 0, so r = I_{T₀}(0, ψy) = 1 and I_T(0,y) = 1 = S(1,y). **y = 1:** r = I_{T₀}(ψx, a) = 1 because ψx ≤ a. **y = 0:** I_T(x,0) = ψ⁻¹(min(a, N₀ψx)) by (F3). **x ≤ y:** r = 1 ≥ a, so I_T = 1, which agrees with the set {1 : x ≤ y} of Lemma 2. **r = a exactly:** every t < 1 satisfies ψt < a ≤ r. The value is 1, and for x > y the supremum is not attained, because T(x,1) = x > y. Checked exactly below. **ψ(x) = N₀(a) exactly** (x = x₀ := ψ⁻¹(N₀(a))): N₀(ψx₀) = a, min(a,a) = a, I_T(x₀,0) = 1. This endpoint is correctly included in part 5's interval. The interval is sharp: for ψx slightly above N₀(a), I_T(x,0) < 1 (checked exactly). **a = e:** falls under part 4. N₀(ψx) > N₀(e) = e = a for x < 1, so I_T = I_WB. **a → 1⁻:** checked at a = 99/100. **Attainment of suprema:** handled correctly. In the case r < a the set {t < 1 : ψt ≤ r} = [0, ψ⁻¹(r)] is closed, with ψ⁻¹(r) < 1. In the case r ≥ a the supremum 1 may be unattained, and this is exactly where (OP) fails. |
| Lemma 1 of weber-uniqueness r1 (drastic boundary) | **Verified.** The note applies it to the t-subnorm M on [0,1]², including M(x,1) = ψ⁻¹(T₀(ψx, a)) ≤ x. Monotonicity: T(x,·) equals M(x,·) on [0,1[ and x at 1, and M(x,t) ≤ x. Associativity: the cases with some argument equal to 1 are direct. If x, y, z < 1, then M(x,y) ≤ min(x,y) < 1, so both sides reduce to M(M(x,y),z) = M(x,M(y,z)). Commutativity and the neutral element are immediate. M is associative because it is ψ-conjugate to the restriction of T₀ to [0,a]², and that restriction is closed under T₀ since T₀ ≤ min. The construction is classical (revision 2 of the companion note attributes it to Klement–Mesiar–Pap, Cor. 1.8; the reviewer did not check that citation). |
| Lemma 2 of weber-uniqueness r1 (residual) | **Verified.** For x < 1, T(x,t) = M(x,t) for t < 1 and T(x,1) = x. So {t : T(x,t) ≤ y} = {t < 1 : M(x,t) ≤ y} ∪ ({1} if x ≤ y). For x = 1, T(1,t) = t, so I_T(1,y) = y. |
| Lemma 4 of weber-uniqueness r1 | **Verified.** If 1 is in the sublevel set, then x = T(x,1) ≤ y. Otherwise the supremum 1 is not attained, so the down-set contains [0,1[, and left-continuity of T(x,·) at 1 gives x ≤ y. Only left-continuity at 1 in the second variable is used, which every left-continuous t-norm has. Consequence used in part 5: if I_T = I_{T'} with T' left-continuous, then I_{T'}(x,0) = 1 with x > 0, a contradiction. |
| Facts (F1)–(F5) | **Verified.** (F1) is (RP), as cited. (F2) is verified above, both from Thm. 5.13 (ii)⇒(i) and by a direct derivation. (F3): I_{T₀}(u,u) = 1 because T₀(u,1) = u; I_{T₀}(u,0) = sup{t : T₀(u,t) = 0} = N₀(u) by definition. (F4) holds because N₀ is a decreasing involution: N₀(u) ≥ a ⟺ u ≤ N₀(a), and a > e ⟺ N₀(a) < e. Then e < a gives N₀(a) < e < a, and a < 1 gives N₀(a) > 0. (F5): T₀(v, N₀v) = 0 by (F1) at value 0, then commutativity and monotonicity. It uses left-continuity only, not strongness. |
| Part 1 (T, S, N) | **Verified.** T: Lemma 1. S: U = min(a, S₀) on [0,a]². If S₀(u,v) ≥ a, then U(U(u,v),w) = min(a, S₀(a,w)) = a = min(a, S₀(S₀(u,v),w)), because S₀ ≥ max. Otherwise U(u,v) = S₀(u,v). So U(U(u,v),w) = min(a, S₀(u,v,w)), which is symmetric; with commutativity, U(u,U(v,w)) = U(U(v,w),u) is the same expression. U(u,0) = u on [0,a], and U is monotone and commutative. Conjugation by the order isomorphism ψ gives a t-conorm on [0,1]. N: N(0) = ψ⁻¹(min(a,1)) = 1, N(1) = 0. On [0,1[, N is a composite of increasing, decreasing, increasing and increasing maps, hence non-increasing, and its values are ≥ 0 = N(1). |
| Part 2 (residual formula) | **Verified.** For x < 1 and t < 1: M(x,t) ≤ y ⟺ T₀(ψx,ψt) ≤ ψy ⟺ ψt ≤ r := I_{T₀}(ψx,ψy) (by F1). If r ≥ a, every t < 1 qualifies and the supremum is 1 = ψ⁻¹(a). If r < a, the set is [0, ψ⁻¹(r)], and x ≤ y is impossible, because x ≤ y forces r = 1. So I_T(x,y) = ψ⁻¹(min(a, r)). The set always contains t = 0. |
| Part 3 ((S,N) and QL forms) | **Verified.** For x < 1, with u = ψx and v = ψy: if N₀(u) ≥ a, both S(N(x),y) and ψ⁻¹(min(a, S₀(N₀u, v))) equal 1, because S₀(a,v) ≥ a and S₀(N₀u,v) ≥ N₀u ≥ a. Otherwise min(a, N₀u) = N₀u. In both cases S(N(x),y) = ψ⁻¹(min(a, S₀(N₀u,v))) = ψ⁻¹(min(a, I_{T₀}(u,v))) (by F2), which is I_T(x,y) by part 2. QL form: for y ≥ x, S(N(x), x) = I_T(x,x) = ψ⁻¹(min(a, 1)) = 1 = I_T(x,y). For y < x the identity is trivial. I_T is a fuzzy implication: it is an R-implication (2010, Thm. 5.10), and directly an (S,N)-implication. So it is a QL-implication from (T_M, S, N) under 2010 Def. 4.1. |
| Part 4 (a ≤ e gives I_WB) | **Verified.** For x < 1, ψx < a ≤ e, so N₀(ψx) > N₀(a) ≥ N₀(e) = e ≥ a. Hence I_T(x,0) = 1, and I_T(x,·) ≡ 1 by monotonicity. With I_T(1,y) = y this is I_WB. **Observation (not a gap):** something stronger holds. For u, v < a ≤ e, u < e < N₀(v), so T₀(u,v) = 0 by (F5). Hence M ≡ 0 on [0,1[² and **T = T_D itself**, not merely a t-norm with residual I_WB. The note's "degenerate member" remark is consistent with this. |
| Part 5 (e < a < 1) | **Verified.** 0 < N₀(a) < a (by F4). For 0 < x ≤ x₀: ψx ≤ N₀(a), so N₀(ψx) ≥ N₀(N₀(a)) = a and I_T(x,0) = 1 with x > 0. So (OP) fails, and by Lemma 4 I_T is not the residual of any left-continuous t-norm; this follows rigorously. For t < 1, ψt < a and T₀(ψx,ψt) ≤ T₀(ψx, a) = 0 (by F5, since ψx ≤ N₀(a)), so T(x,t) = 0 while T(x,1) = x > 0. That is a jump at the boundary point (x,1), so T is neither border-continuous nor left-continuous. The same conclusion also follows from 2013 Prop. 3.4, since (OP) fails. Finally, for N₀(a) < ψx < a, I_T(x,0) = ψ⁻¹(N₀ψx) < ψ⁻¹(a) = 1 = I_WB(x,0). |
| Reduction to Theorems A and B | **Verified.** With ψ(x) = x/c and a = 1/c: T_L gives T = max(0, x+y−c) on [0,1[², N = min(1, c−x) = N_c, S = min(1, p+q) = S_L, and I = min(1, c−x+y). T_nM gives T'_c, S*_c and J_c = max(min(1,c−x), y). And 1 < c < 2 ⟺ e = 1/2 < a < 1. |
| Logical implications | **No gap.** The chain (F1)⇒2, (2, F2)⇒3, (2, F3, F4)⇒4, and (2, F3, F4, F5, Lemma 4)⇒5 covers every case of each part. In part 2 the cases are x = 1, and x < 1 split into r ≥ a and r < a. In part 3 the cases are x = 1, and x < 1 split into N₀ψx ≥ a and N₀ψx < a; the QL form splits into y < x and y ≥ x. Part 5's three conclusions are proved separately. No circularity: part 3 uses part 2, and part 2 does not use part 3. |
| Dependency assumptions | The external dependencies are Thm. 5.13 of the 2010 paper (used in direction (ii)⇒(i) only, and re-derived independently here) and (RP) for left-continuous t-norms (standard). The internal dependencies are Lemmas 1, 2 and 4 of `weber-uniqueness.md` revision 1, all verified here; their text is unchanged in revision 2. Theorem C does **not** use 2010 Thm. 5.14 (whose printed form revision 2 of the companion note reports as defective) or Cor. 2.15. |
| Counterexample attempts | **None found.** (i) *Hand attempts:* T₀ with zero divisors on the line u = N₀(v), as in the nilpotent minimum, where the jump of T₀ is not continuous. The proof never uses continuity of T₀, only (RP) and (F5), and the attempt fails. (ii) *Rotation-type T₀* (Jenei rotation of the product, N_C), whose zero set is the closed region v ≤ 1 − u: same outcome. (iii) *a just above e, r = a exactly, ψx = N₀(a) exactly:* all consistent. (iv) *Exact computer checks* on new configurations not in the author's script (see Reproduction): all passed. |
| Formalization scope | Theorem C is not formalized: the note says so, and `formalization/Conjectura/Research/WeberUniqueness.lean` covers Theorems A and B only. Not assessed further; no Lean claim is made for Theorem C. |
| Novelty coverage | **Not established by this review.** Searches run: four web searches on combinations of "(S,N)-implication", "R-implication", "non-border continuous", "Weber implication", "QL-implication", "non-left-continuous", "Problem 4.8.1", "Problem 9.4". These found no source that answers Problems 4.2(i) or 4.5(ii) or that contains Theorem C. One paper was read: Jayaram, Baczyński, Mesiar, *R-implications and the exchange principle: the case of border continuous t-norms*, FSS 224 (2013) 93–105 (author copy, SHA-256 `dd8795d3…e5d5e`). Its Section 4 treats ordinal sums with **t-norm** summands (Thm. 4.5, Cor. 4.6) and does not contain the construction of Theorem C (there M is a t-subnorm without neutral element). **Not read:** Klement–Mesiar–Pap (2000), Baczyński–Jayaram (2008 monograph), the EUSFLAT 2011 paper by Jayaram–Baczyński–Mesiar (*… a complete characterization*). Revision 2 of the companion note states that the EUSFLAT 2011 paper uses the drastic-boundary extension of t-subnorms and its residual (their equations (5), (6)). That paper is therefore the most likely place for a prior occurrence of Theorem C's construction or examples, and it must be read before any novelty statement. Post-2013 literature was not systematically searched. **Reading caveat on Problem 4.5(ii)**, relevant to how Theorem C may be used. Read literally ("a QL-implication that is also an R-implication obtained from a non-left continuous t-norm"), the question is already answered *no* inside the sources. The non-left-continuous nilpotent minimum (0 if x + y < 1, min otherwise) has residual I_FD (2013 chapter, p. 189), and I_FD is a QL-implication (2010, Example 4.15(i), triple (T_M, S_nM^{N_C}, N_C)); I_FD ≠ I_WB. Only the strong reading, I_QL ∩ (I_T \ I_TLC), is non-trivial. Theorem C's Remarks use exactly that set, so the note itself is consistent. |
| Unresolved gaps | **None in the mathematics of Theorem C.** Points to note, none of them a gap: (1) continuity of ψ is used in the wording but not assumed; it is automatic and not needed; (2) part 4 could state the stronger T = T_D; (3) under the strong-negation conventions for S- and QL-implications, I_T is not covered, and the note claims nothing there; (4) novelty is open, and the EUSFLAT 2011 paper is unread. |

## Reproduction

All commands were run by the reviewer on 2026-11-27 against the files and
hashes listed above.

1. Author script:
   `cd experiments/CJ-0024-sn-r-nonborder-intersection && uv run python check_theorem_c.py`.
   Exit code 0, final line `ALL CHECKS PASSED for 30 configurations`, wall
   time 2 min 37 s.
2. Reviewer's independent script, written without reusing the author's code:
   `uv run --no-project python -I indep_check.py 14`. It ran from the session
   scratchpad, which is not durable; script SHA-256 `534601ad371aef79aec9001dbb901082706be061a84db1a8a7927fb5a9d64015`.
   Exit code 0, final line `ALL PASSED 30`, wall time 1 min 52 s.
   - **New base t-norms** (none in the author's script):
     - φ-conjugate of Łukasiewicz with φ(x) = x/(2−x), with e = 2/3;
     - Jenei's rotation of the product with N_C, with e = 1/2, given by
       2xy − x − y + 1 on ]1/2,1]², max(0, (x+y−1)/(2·max(x,y)−1)) on the
       mixed region, and 0 on [0,1/2]²;
     - nilpotent minimum for the Sugeno negation (1−x)/(1+3x), with e = 1/3.
   - **New nonlinear ψ:** a·x/(2−x) and 2a·x/(1+x), both with rational
     inverse.
   - **a values:** e/2, e, e + 1/1000, (e+1)/2 and 99/100.
   - **What was checked, in exact rational arithmetic:**
     - the base t-norm axioms and natural negation (T₀(u,N₀u) = 0 and
       T₀(u, N₀u + 10⁻⁴⁰) > 0) on a grid;
     - the t-norm axioms for T and t-conorm axioms for S (commutativity,
       neutral element, monotonicity, full associativity on the grid), and the
       negation axioms for N;
     - for every grid pair, that v = S(N(x),y) lies in a rigorous enclosure of
       sup{t : T(x,t) ≤ y}. Because the sublevel set is a down-set,
       T(x, v−δ) ≤ y and T(x, v+δ) > y put the supremum in [v−δ, v+δ], and
       T(x, 1−δ) ≤ y puts it in [1−δ, 1], with δ = 10⁻⁴⁰. This is independent
       of the formula in part 2;
     - S(N(x), min(x,y)) = S(N(x),y) exactly;
     - for a ≤ e, equality with I_WB;
     - for a > e, at x₀ and x₀/2: I_T(x,0) = 1, T(x, 1−10⁻⁴⁰) = 0 and
       T(x,1) = x > 0; I_T(x,0) < 1 at ψ⁻¹((N₀(a)+a)/2); and sharpness of the
       (OP)-violation interval at x₀ + 10⁻⁶.
   - **Grid:** k/14 plus the special points x₀, x₀/2, x₀ ± 10⁻³,
     ψ⁻¹((N₀(a)+a)/2), ψ⁻¹(e) and ψ⁻¹(N₀(a + (1−a)/3)) where defined; 15 to
     22 points per configuration.
3. Edge case r = a exactly (part 2):
   `uv run --no-project python -I edge_r_eq_a.py`. Scratchpad, SHA-256
   `9ff87fc93b9cd3d061da1940644ae6bd94d4428bc1d202ecb95aace42596c75c`.
   - Setup: φ-conjugate Łukasiewicz base, both Möbius ψ, and a ∈ {3/4, 9/10,
     2003/3000}. Points (x,y) with x > y were chosen so that the closed-form
     I_{T₀}(ψx,ψy) equals a exactly.
   - Checked: T(x,1) > y (the supremum is not attained at 1), the enclosure
     gives a supremum ≥ 1 − 10⁻⁴⁰, and S(N(x),y) = S(N(x),min(x,y)) = 1. For y
     slightly below, the value is < 1 and lies inside its enclosure.
   - Result: `EDGE PASSED` (6 configurations × 5 points).
4. Independent derivations by hand: (F2) as derived in the "Hypotheses" row;
   parts 1–5 as reconstructed in the table; the reduction to Theorems A and B.

Grid checks are finite evidence for the identities on [0,1] and are not a
proof of them. The proof of Theorem C was reconstructed by hand, step by step,
as recorded above.

## Verdict

**`no gap found within stated scope`**

Scope:
- **Covered:** the mathematical correctness of Theorem C, parts 1–5, of
  `notes/rescaled-tnorms.md` revision 1 (SHA-256 `77385d89…797ccae5`); the
  facts (F1)–(F5); Lemmas 1, 2 and 4 of `notes/weber-uniqueness.md` revision 1
  (unchanged in revision 2); and the reduction to Theorems A and B. All of
  this is under the definitions of the 2013 chapter (Defs. 2.1, 2.11, 3.1,
  3.3) and the 2010 paper (Def. 4.1), with border-continuity read as
  continuity at boundary points.
- **Not covered:**
  - novelty: limited searches only, and the EUSFLAT 2011 paper and the
    Klement–Mesiar–Pap book were not read;
  - formalization: none exists for Theorem C;
  - the companion note's Theorems A and B themselves, beyond the lemmas
    Theorem C uses;
  - whether Theorem C or its examples answer Problem 4.5(ii) under any
    particular reading. Under the literal reading the sources already answer
    it, through I_FD.

The review is limited in independence: same model as the author, fresh
context. It applies only to the revision and hashes named above; any material
change to the note or to the lemmas it uses invalidates it until rechecked.
