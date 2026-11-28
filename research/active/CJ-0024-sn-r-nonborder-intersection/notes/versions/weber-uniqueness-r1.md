# Residuals of non-border-continuous t-norms that are (S,N)- and QL-implications

*Note written 2026-11-27 by `claude-opus-5-5` (session 1 of CJ-0024). Status:
candidate answer, not reviewed. Revision 1.*

## 1. The questions

Sources: M. Baczyński, B. Jayaram, *Fuzzy Implications: Some Recently Solved
Problems*, in: Advances in Fuzzy Implication Functions, STUDFUZZ 300,
Springer 2013, pp. 177–204, Section 4 (author copy
<https://people.iith.ac.in/jbala/publications/book_chapters/mb_bj_adv_fi.pdf>,
read 2026-11-27); M. Baczyński, B. Jayaram, *QL-implications: some properties
and intersections*, Fuzzy Sets Syst. 161 (2010) 158–188, Problem 9.4 (author
copy <https://people.iith.ac.in/jbala/publications/fss/fss_ql_imp.pdf>, read
2026-11-27). Quoted verbatim from the 2013 chapter, p. 202:

> **Problem 4.2.** (i) Is there a fuzzy implication I, other than the Weber
> implication I_WB, which is both an (S,N)-implication and an R-implication
> which is obtained from a non-border continuous t-norm and cannot be obtained
> as the residual of any other left-continuous t-norm?
> (ii) If the answer to the above question is in the affirmative, characterize
> the above non-empty intersection.

> **Problem 4.5.** […] (ii) Is the Weber implication I_WB the only
> QL-implication that is also an R-implication obtained from a non-left
> continuous t-norm? If not, give other examples from the above intersection
> and hence, characterize the non-empty intersection I_QL ∩ I_T.

The chapter (Section 3.1.3) gives the monograph form of Problem 4.2 (Problem
4.8.1 of Baczyński–Jayaram, *Fuzzy Implications*, STUDFUZZ 231, 2008): "is
the following equality true I_{S,N} ∩ (I_T \ I_{T*}) = {I_WB}?", where
I_{T*} denotes the R-implications of left-continuous t-norms; it notes that the
intersection is empty when T is border-continuous. Problem 4.5(ii) is Problem
9.4(ii) of the 2010 paper. The chapter introduces Problem 4.5 with "The
following problems originally appeared as open in [2] and still remain so".

## 2. Definitions (as in the sources)

- *Fuzzy negation*: N : [0,1] → [0,1] non-increasing, N(0) = 1, N(1) = 0.
- *t-norm* T (*t-conorm* S): commutative, associative, non-decreasing in each
  variable, with neutral element 1 (0).
- *Fuzzy implication* (Definition 2.1 of the chapter): I : [0,1]² → [0,1]
  non-increasing in the first variable, non-decreasing in the second, with
  I(0,0) = I(1,1) = 1 and I(1,0) = 0.
- *(S,N)-implication* (chapter, Definition 2.11): I(x,y) = S(N(x), y) for a
  t-conorm S and a fuzzy negation N.
- *R-implication* (chapter, Definition 3.1): I_T(x,y) = sup{t ∈ [0,1] :
  T(x,t) ≤ y} for a t-norm T (no continuity assumed).
- *QL-operation* (2010 paper, Definition 4.1): I(x,y) = S(N(x), T(x,y)); a
  QL-implication is a QL-operation that is a fuzzy implication.
- *Border-continuous* (chapter, Definition 3.3): continuous on
  [0,1]² \ ]0,1[².
- *Weber implication*: I_WB(x,y) = 1 if x < 1, I_WB(1,y) = y (chapter p. 181
  and p. 189, the residual of the drastic product T_D).
- *(OP)*: I(x,y) = 1 ⟺ x ≤ y.
- Łukasiewicz t-conorm S_L(a,b) = min(1, a + b); minimum T_M(x,y) = min(x,y).

## 3. Results

Throughout, c is a real number with 1 < c < 2, and

    N_c(x) = min(1, c − x) for 0 ≤ x < 1,   N_c(1) = 0.

N_c is a fuzzy negation (non-increasing, N_c(0) = 1 because c > 1,
N_c(1) = 0). It equals 1 on [0, c−1] and is discontinuous at 1.

**Theorem A.** Let

    T_c(x,y) = min(x,y)            if max(x,y) = 1,
    T_c(x,y) = max(0, x + y − c)   if x, y < 1.

Then:
1. T_c is a t-norm; it is neither border-continuous nor left-continuous.
2. Its residual is I_c(x,y) = min(1, c − x + y) for x < 1 and I_c(1,y) = y.
3. I_c(x,y) = S_L(N_c(x), y) for all x, y: I_c is an (S,N)-implication.
4. I_c(x,y) = S_L(N_c(x), T_M(x,y)) for all x, y: I_c is a QL-implication.
5. I_c(c − 1, 0) = 1 although c − 1 > 0, so I_c violates (OP). Hence I_c is
   not the residual of any left-continuous t-norm.
6. I_c ≠ I_WB, and I_c ≠ I_{c'} for c ≠ c'.

**Theorem B.** Let

    T'_c(x,y) = min(x,y)   if max(x,y) = 1 or x + y > c,
    T'_c(x,y) = 0          otherwise,

and S*_c(a,b) = max(a,b) if a + b < c, S*_c(a,b) = 1 if a + b ≥ c. Then:
1. T'_c is a t-norm, neither border-continuous nor left-continuous; S*_c is a
   t-conorm.
2. The residual of T'_c is J_c(x,y) = 1 if x ≤ y; J_c(x,y) =
   max(min(1, c − x), y) if y < x < 1; J_c(1,y) = y.
3. J_c(x,y) = S*_c(N_c(x), y) = S*_c(N_c(x), T_M(x,y)) for all x, y: J_c is
   both an (S,N)- and a QL-implication.
4. J_c(c − 1, 0) = 1, so J_c violates (OP) and is not the residual of any
   left-continuous t-norm.
5. J_c ≠ I_WB, J_c ≠ I_c, and J_c ≠ J_{c'} for c ≠ c'.

**Corollary.** The answer to Problem 4.2(i) (2013 chapter) is *yes*: each
I_c and each J_c (1 < c < 2) is an (S,N)-implication and the residual of a
non-border-continuous t-norm, is not the residual of any left-continuous
t-norm, and differs from I_WB. Equivalently, the equality
I_{S,N} ∩ (I_T \ I_{T*}) = {I_WB} of Problem 4.8.1 of the 2008 monograph is
false; the intersection has the cardinality of the continuum. The answer to
the first question of Problem 4.5(ii) (= Problem 9.4(ii) of the 2010 paper) is
*no*: I_c and J_c are QL-implications that are residuals of non-left-continuous
t-norms (and of no left-continuous one), other than I_WB. The
characterisation parts (Problem 4.2(ii), the rest of 4.5(ii)) remain open.

## 4. Proofs

**Lemma 1 (drastic boundary).** Let M : [0,1]² → [0,1] be commutative,
associative, non-decreasing in each variable, with M(x,y) ≤ min(x,y) (a
t-subnorm). Define T(x,y) = min(x,y) if max(x,y) = 1 and T(x,y) = M(x,y)
otherwise. Then T is a t-norm.

*Proof.* T(x,1) = x and commutativity are immediate. Monotonicity: for x = 1,
T(1,·) is the identity; for x < 1 and t < t' < 1, T(x,t) = M(x,t) ≤ M(x,t')
= T(x,t'), and T(x,t) = M(x,t) ≤ min(x,t) ≤ x = T(x,1). Associativity: if
x = 1, both sides of T(T(x,y),z) = T(x,T(y,z)) equal T(y,z); if z = 1, both
equal T(x,y); if y = 1, both equal T(x,z). If x, y, z < 1 then T(x,y) =
M(x,y) ≤ x < 1 and T(y,z) = M(y,z) < 1, so both sides are M(M(x,y),z) =
M(x,M(y,z)). ∎

**Lemma 2 (residual).** For T as in Lemma 1 and x < 1:
I_T(x,y) = sup( {t ∈ [0,1[ : M(x,t) ≤ y} ∪ {1 : x ≤ y} ); and I_T(1,y) = y.

*Proof.* T(x,t) = M(x,t) for t < 1 and T(x,1) = x. For x = 1, T(1,t) = t, so
the set is [0,y]. ∎

**Lemma 3 (threshold minimum).** For a real θ let F_θ(x,y) = min(x,y) if
x + y > θ and F_θ(x,y) = 0 otherwise, on [0,1]². F_θ is commutative,
non-decreasing, F_θ ≤ min, and associative.

*Proof.* Only associativity needs an argument. If x + y ≤ θ then
F_θ(F_θ(x,y),z) = F_θ(0,z) = 0. If x + y > θ then F_θ(F_θ(x,y),z) equals
min(x,y,z) when min(x,y) + z > θ and 0 otherwise. So F_θ(F_θ(x,y),z) =
min(x,y,z) if [x + y > θ and min(x,y) + z > θ], and 0 otherwise. Let
a ≤ b ≤ d be x, y, z in increasing order. The bracketed condition is
equivalent to a + b > θ: if z = a then min(x,y) = b, the second inequality is
a + b > θ and the first, b + d > θ, follows from it; if z = b then
min(x,y) = a, the second inequality is a + b > θ and the first is a + d ≥
a + b; if z = d then min(x,y) = a, the first inequality is a + b > θ and
the second is a + d ≥ a + b. Hence F_θ(F_θ(x,y),z) is a symmetric function of
(x,y,z), and with commutativity F_θ(x,F_θ(y,z)) = F_θ(F_θ(y,z),x) equals
the same symmetric expression. ∎

**Lemma 4 (residuals of left-continuous t-norms).** If T is a t-norm such
that T(x,·) is left-continuous at 1 for every x, and I_T(x,y) = 1, then
x ≤ y.

*Proof.* If 1 belongs to {t : T(x,t) ≤ y}, then x = T(x,1) ≤ y. Otherwise
the supremum 1 is not attained, so for every s < 1 there is t ∈ ]s,1[ with
T(x,t) ≤ y, and by monotonicity T(x,s) ≤ y for all s < 1. Left-continuity at
1 gives x = T(x,1) = lim_{s→1⁻} T(x,s) ≤ y. ∎

A left-continuous t-norm satisfies the hypothesis of Lemma 4; therefore an
implication I with I(x₀,y₀) = 1 for some x₀ > y₀ is not the residual of any
left-continuous t-norm.

**Proof of Theorem A.**
1. M(x,y) = max(0, x + y − c) is commutative, non-decreasing, and
   M(x,y) ≤ min(x,y) because x + y − c < x + y − 1 ≤ min(x,y). It is
   associative: if x + y ≤ c, M(M(x,y),z) = max(0, z − c) = 0 and
   x + y + z − 2c ≤ z − c < 0; if x + y > c, M(M(x,y),z) =
   max(0, x + y + z − 2c). So M(M(x,y),z) = max(0, x + y + z − 2c), which is
   symmetric. By Lemma 1, T_c is a t-norm. For 0 < x < 1 and t < 1,
   T_c(x,t) ≤ max(0, x + t − c) ≤ max(0, x + 1 − c), and
   max(0, x + 1 − c) < x because c > 1; but T_c(x,1) = x. So T_c(x,·) is
   not left-continuous at 1, and T_c is discontinuous at the boundary point
   (x,1).
2. By Lemma 2, for x < 1: if x ≤ y the set contains 1, so
   I_{T_c}(x,y) = 1, and also min(1, c − x + y) = 1 because
   c − x + y ≥ c > 1. If x > y, the set is
   {t < 1 : max(0, x + t − c) ≤ y} = {t < 1 : t ≤ c − x + y} (as y ≥ 0), and
   c − x + y > 0, so its supremum is min(1, c − x + y). For x = 1, I = y.
3. For x ≤ c − 1: N_c(x) = 1 and S_L(1, y) = 1 = min(1, c − x + y), since
   c − x + y ≥ 1. For c − 1 < x < 1: S_L(c − x, y) = min(1, c − x + y).
   For x = 1: S_L(0, y) = y.
4. For x = 1: S_L(0, min(1,y)) = y. For x ≤ c − 1: both sides are 1. For
   c − 1 < x < 1: if y ≤ x, S_L(c − x, min(x,y)) = min(1, c − x + y); if
   y > x, S_L(c − x, x) = min(1, c) = 1 = I_c(x,y) (as c − x + y > c). I_c
   is a fuzzy implication, being an R-implication (or an (S,N)-implication).
5. 0 < c − 1 < 1 and I_c(c − 1, 0) = min(1, 1) = 1. Apply Lemma 4.
6. For c − 1 < x < 1, I_c(x, 0) = c − x < 1 = I_WB(x, 0). If
   1 < c < c' < 2 and c' − 1 < x < 1, then I_c(x,0) = c − x ≠ c' − x =
   I_{c'}(x,0). ∎

**Proof of Theorem B.**
1. On [0,1[², T'_c coincides with F_c of Lemma 3, a t-subnorm; by Lemma 1,
   T'_c is a t-norm. Take 0 < x ≤ c − 1: for t < 1, x + t < c, so
   T'_c(x,t) = 0, while T'_c(x,1) = x > 0. Hence T'_c(x,·) is not
   left-continuous at 1 and T'_c is discontinuous at the boundary point
   (x,1).
   S*_c is the N_C-dual of F_{2−c} extended by min on the border: put
   T*(u,v) = F_{2−c}(u,v). Since u + 1 > 2 − c for u ≥ 0, T*(u,1) = u, so
   T* is a t-norm by Lemma 3; and 1 − T*(1 − a, 1 − b) = max(a,b) if
   (1 − a) + (1 − b) > 2 − c, i.e. a + b < c, and 1 otherwise. So S*_c is a
   t-conorm.
2. Lemma 2 with M = F_c. If x ≤ y, J_c = 1. If y < x < 1: for t < 1,
   F_c(x,t) ≤ y iff x + t ≤ c or [x + t > c and min(x,t) ≤ y], and since
   x > y the last condition means t ≤ y. The set is
   ([0, c − x] ∪ ]c − x, y]) ∩ [0,1[ (the second part empty if y ≤ c − x).
   If c − x ≥ 1 its supremum is 1 = max(min(1, c − x), y); otherwise it is
   max(c − x, y). For x = 1, J_c = y.
3. x = 1: S*_c(0, y) = y because 0 + y ≤ 1 < c; and T_M(1,y) = y.
   x ≤ c − 1: N_c(x) = 1, S*_c(1, b) = 1 for every b; J_c = 1 because either
   x ≤ y or min(1, c − x) = 1. c − 1 < x < 1: N_c(x) = c − x. If y ≥ x,
   (c − x) + y ≥ c and (c − x) + T_M(x,y) = c, so both expressions are 1 =
   J_c(x,y). If y < x, (c − x) + y < c, so both expressions are
   max(c − x, y) = J_c(x,y).
4. As in Theorem A: J_c(c − 1, 0) = max(min(1, 1), 0) = 1; Lemma 4.
5. For c − 1 < x < 1: J_c(x,0) = c − x < 1 = I_WB(x,0). With x = 1 − ε and
   y = ε for small ε > 0 (y < x, c − x = c − 1 + ε < 1):
   I_c(x,y) = min(1, c − 1 + 2ε) and J_c(x,y) = max(c − 1 + ε, ε) =
   c − 1 + ε; these differ. If 1 < c < c' < 2 and c' − 1 < x < 1, then
   J_c(x,0) = c − x ≠ c' − x = J_{c'}(x,0). ∎

## 5. Remarks

- Both families share the natural negation N_c; I_c and J_c are two different
  (S,N)-implications with the same non-continuous negation. (For continuous
  negations the representation is unique, chapter Theorem 2.12.)
- φ-conjugation (2010 paper, Theorem 4.8, and the analogous facts for
  R- and (S,N)-implications) turns each example into further ones.
- The construction is the classical extension of a t-subnorm by the drastic
  boundary (Lemma 1). Its residual for x < 1 depends only on the subnorm.
  This suggests a general sufficient condition, not attempted here.
- Nothing here addresses Problem 9.4(iii) of the 2010 paper
  ((I_QL ∩ I_T) \ I_{S,N} = ∅?) or Problem 9.3: all examples above are
  (S,N)-implications.

## 6. Verification status

- Exact checks on rational grids: `experiments/CJ-0024-sn-r-nonborder-intersection/`
  (see its README; to be run).
- Lean: not started at the time of writing.
- Independent review: none yet.
- Literature: whether these examples or an answer to the problems appeared
  after 2013 is being audited; until that audit is recorded, novelty is
  `unknown`.
