# A general construction: rescaled left-continuous t-norms with the drastic boundary

*Note written 2026-11-27 by `claude-opus-5-5` (session 1 of CJ-0024). Status:
candidate, not reviewed. Revision 1. Generalises Theorems A and B of
[`weber-uniqueness.md`](weber-uniqueness.md) (which stays as reviewed or under
review); definitions and Lemmas 1, 2, 4 are those of that note.*

## Statement

Let T₀ be a left-continuous t-norm whose natural negation
N₀(v) = sup{t ∈ [0,1] : T₀(v,t) = 0} is strong (N₀∘N₀ = id), and let
e ∈ ]0,1[ be the fixed point of N₀. Let S₀(p,q) = N₀(T₀(N₀(p), N₀(q))) be the
N₀-dual t-conorm. Let 0 < a < 1 and let ψ : [0,1] → [0,a] be an increasing
bijection (for instance ψ(x) = a·x). Define

    T(x,y) = min(x,y)                         if max(x,y) = 1,
    T(x,y) = ψ⁻¹(T₀(ψ(x), ψ(y)))              if x, y < 1;

    N(x) = ψ⁻¹(min(a, N₀(ψ(x))))  (x < 1),   N(1) = 0;
    S(p,q) = ψ⁻¹(min(a, S₀(ψ(p), ψ(q)))).

**Theorem C.**
1. T is a t-norm, S is a t-conorm and N is a fuzzy negation.
2. For x < 1, I_T(x,y) = ψ⁻¹(min(a, I_{T₀}(ψ(x), ψ(y)))); I_T(1,y) = y.
3. I_T(x,y) = S(N(x), y) = S(N(x), min(x,y)) for all x, y ∈ [0,1]; so I_T is
   an (S,N)-implication and a QL-implication.
4. If a ≤ e, then I_T = I_WB.
5. If e < a < 1, then I_T(x,0) = 1 for 0 < x ≤ ψ⁻¹(N₀(a)) (so (OP) fails and
   I_T is not the residual of any left-continuous t-norm), T is not
   border-continuous, and I_T ≠ I_WB.

Theorems A and B of `weber-uniqueness.md` are the cases T₀ = T_L
(Łukasiewicz), respectively T₀ = T_nM (nilpotent minimum, with
T_nM(x,y) = min(x,y) if x + y > 1 and 0 otherwise), N₀ = N_C, e = 1/2,
ψ(x) = x/c, a = 1/c. For a ≤ e the construction returns the Weber
implication, so I_WB is the degenerate member of the family.

## Facts used about T₀

(F1) Residuation: T₀ left-continuous gives T₀(u,t) ≤ v ⟺ t ≤ I_{T₀}(u,v)
(the property (RP) quoted in the 2013 chapter, p. 188, for left-continuous
t-norms).
(F2) I_{T₀}(u,v) = S₀(N₀(u), v) for all u, v: Theorem 5.13 of Baczyński–Jayaram,
FSS 161 (2010) (= Theorem 6.2 of their 2008 survey): for a left-continuous
t-norm, I_T = I_{S,N} iff N = N_T is strong and (T, N, S) is a De Morgan
triple; here N₀ is strong and S₀ is the N₀-dual of T₀ by definition.
(F3) I_{T₀}(u,u) = 1 and I_{T₀}(u,0) = N₀(u) (definitions).
(F4) N₀ is a continuous strictly decreasing bijection of [0,1]; hence
N₀(u) ≥ a ⟺ u ≤ N₀(a); and a > e ⟺ N₀(a) < e < a.
(F5) T₀(u,v) = 0 whenever u ≤ N₀(v): by (F1) with value 0, T₀(v, N₀(v)) = 0
since N₀(v) = I_{T₀}(v,0); then use commutativity and monotonicity.

## Proof

**1.** M(x,y) = ψ⁻¹(T₀(ψ(x), ψ(y))) is well defined because
T₀(ψ(x),ψ(y)) ≤ min(ψ(x),ψ(y)) ≤ a. It is commutative and non-decreasing,
associative (it is conjugate by ψ to the restriction of T₀ to [0,a]², which is
closed under T₀), and M(x,y) ≤ min(x,y) because T₀(ψx,ψy) ≤ min(ψx,ψy) and
ψ⁻¹ is increasing. By Lemma 1 of `weber-uniqueness.md`, T is a t-norm.
For S: put U(u,v) = min(a, S₀(u,v)) on [0,a]². Then
U(U(u,v),w) = min(a, S₀(S₀(u,v),w)): if S₀(u,v) ≥ a both sides equal a
(S₀ ≥ max); otherwise U(u,v) = S₀(u,v). The right side is symmetric in
(u,v,w) by associativity and commutativity of S₀, so U is associative; U is
commutative, non-decreasing and U(u,0) = min(a,u) = u. S is the conjugate of
U by ψ, hence a t-conorm on [0,1] (S(p,0) = ψ⁻¹(ψ(p)) = p).
N: N(0) = ψ⁻¹(min(a, N₀(0))) = ψ⁻¹(a) = 1, N(1) = 0, and N is
non-increasing on [0,1[ with values ≥ 0 = N(1).

**2.** Let x < 1. By Lemma 2, I_T(x,y) = sup({t < 1 : M(x,t) ≤ y} ∪ {1 : x ≤ y}).
For t < 1: M(x,t) ≤ y ⟺ T₀(ψx, ψt) ≤ ψy ⟺ ψ(t) ≤ r with
r := I_{T₀}(ψx, ψy) (F1). If r ≥ a, every t < 1 qualifies and the supremum
is 1 = ψ⁻¹(a). If r < a, the set is {t : t ≤ ψ⁻¹(r)} (ψ is a continuous
increasing bijection onto [0,a]), with supremum ψ⁻¹(r). If x ≤ y then
ψx ≤ ψy, r = 1 ≥ a, and the value 1 agrees. So
I_T(x,y) = ψ⁻¹(min(a, r)). For x = 1, Lemma 2.

**3.** x = 1: S(0,y) = ψ⁻¹(min(a, ψ(y))) = y, and min(1,y) = y. Let x < 1
and put u = ψ(x), v = ψ(y). Then ψ(N(x)) = min(a, N₀(u)) and
S(N(x), y) = ψ⁻¹(min(a, S₀(min(a, N₀(u)), v))). If N₀(u) ≥ a, this is
ψ⁻¹(a) = 1, and also min(a, S₀(N₀(u), v)) = a; otherwise
min(a, N₀(u)) = N₀(u). In both cases S(N(x), y) = ψ⁻¹(min(a, S₀(N₀(u), v)))
= ψ⁻¹(min(a, I_{T₀}(u,v))) (F2) = I_T(x,y) by 2. For the QL form: if y < x,
min(x,y) = y; if y ≥ x, S(N(x), x) = ψ⁻¹(min(a, I_{T₀}(u,u))) = ψ⁻¹(a) = 1
(F3) = I_T(x,y). I_T is a fuzzy implication (an (S,N)-implication).

**4.** If a ≤ e then N₀(a) ≥ N₀(e) = e ≥ a. For x < 1, ψ(x) < a, so
N₀(ψx) ≥ N₀(a) ≥ a (N₀ non-increasing), hence
I_T(x,0) = ψ⁻¹(min(a, N₀(ψx))) = 1 (part 2 and F3), and then
I_T(x,y) = 1 for all y (monotone in y). With I_T(1,y) = y this is I_WB.

**5.** Let e < a < 1; by (F4) 0 < N₀(a) < a. For 0 < x ≤ ψ⁻¹(N₀(a)):
ψ(x) ≤ N₀(a), so N₀(ψx) ≥ a (F4) and I_T(x,0) = 1 although x > 0; by
Lemma 4 of `weber-uniqueness.md`, I_T is not the residual of any
left-continuous t-norm. For the same x and t < 1, ψ(t) < a, and
T₀(ψx, ψt) ≤ T₀(ψx, a) = 0 by (F5) (ψx ≤ N₀(a)); so T(x,t) = 0 for t < 1
but T(x,1) = x > 0: T is discontinuous at the boundary point (x,1). Finally,
for x with N₀(a) < ψ(x) < a (such x exist), N₀(ψx) < a and
I_T(x,0) = ψ⁻¹(N₀(ψx)) < 1 = I_WB(x,0). ∎

## Remarks

- The construction gives, for each pair (T₀, ψ) with e < a = ψ(1) < 1, an
  element of I_{S,N} ∩ I_QL ∩ (I_T \ I_{T_LC}). Whether every element of
  I_{S,N} ∩ (I_T \ I_{T_LC}) arises from a drastic-boundary t-norm of this
  kind is open (it would answer Problem 4.2(ii)); no attempt was made.
- Left-continuity of T₀ is used in (F1), (F2) and (F5); strongness of N₀ in
  (F2) and (F4).

## Verification status

Exact grid checks for T₀ ∈ {T_L, T_nM, nilpotent minimum of a piecewise-linear
strong negation} and linear and piecewise-linear ψ:
`experiments/CJ-0024-sn-r-nonborder-intersection/check_theorem_c.py` (to be
run). Not reviewed. Not formalized.
