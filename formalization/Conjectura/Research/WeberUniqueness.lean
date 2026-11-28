/-
RESEARCH — problem CJ-0024 ((S,N)- and QL-implications that are residuals of
non-border-continuous t-norms), Theorems A and B.

Source statement: Theorem A of
`research/active/CJ-0024-sn-r-nonborder-intersection/notes/weber-uniqueness.md`
(revision 1, 2026-11-27), with Lemma 4 of the same note (Theorem B is quoted
before its formalization below):

  Let `1 < c < 2`, `N_c(x) = min(1, c − x)` for `0 ≤ x < 1`, `N_c(1) = 0`,
  `T_c(x,y) = min(x,y)` if `max(x,y) = 1`, `T_c(x,y) = max(0, x + y − c)` if
  `x, y < 1`. Then
  1. `T_c` is a t-norm; it is neither border-continuous nor left-continuous;
  2. its residual is `I_c(x,y) = min(1, c − x + y)` for `x < 1`, `I_c(1,y) = y`;
  3. `I_c(x,y) = S_L(N_c(x), y)`;
  4. `I_c(x,y) = S_L(N_c(x), T_M(x,y))`;
  5. `I_c(c − 1, 0) = 1` although `c − 1 > 0`; hence `I_c` is not the residual
     of any left-continuous t-norm (Lemma 4: if `T(x,·)` is left-continuous at
     `1` for every `x` and `I_T(x,y) = 1`, then `x ≤ y`);
  6. `I_c ≠ I_WB`, and `I_c ≠ I_{c'}` for `c ≠ c'`.

Encoding:

* all operations are functions `ℝ → ℝ → ℝ` (or `ℝ → ℝ`); every property is
  quantified over arguments in `Set.Icc 0 1` only, so values outside the unit
  square are irrelevant;
* `IsTNorm T`: values in `[0,1]`, commutativity, associativity, `T x 1 = x`,
  and monotonicity in the first variable (monotonicity in the second follows
  from commutativity: `IsTNorm.mono_right`); `IsTConorm S` likewise with
  neutral element `0`; `IsFuzzyNegation N`: values in `[0,1]`, antitone,
  `N 0 = 1`, `N 1 = 0`;
* `residual T x y = sSup {t ∈ [0,1] | T x t ≤ y}` (the real `sSup`; the set is
  non-empty and bounded above for a t-norm, so this is the textbook supremum);
* "`T(x,·)` is left-continuous at `1`" is `ContinuousWithinAt (T x) (Icc 0 1) 1`
  (since `1` is the right end of `[0,1]`, this is continuity from the left);
* "not border-continuous" is formalized as: `T_c`, as a function of two
  variables, is not continuous within `[0,1]²` at the boundary point `(x,1)`
  for every `0 < x < 1`;
* `N_c`, `T_c`, `I_c`, `S_L`, `I_WB` are written with `if` exactly as in the
  note (`Nc`, `Tc`, `Ic`, `SL`, `weberImp`); `T_M` is `min`.
* every theorem about `c` keeps the note's standing hypothesis `1 < c < 2` as
  `(hc1 : 1 < c) (hc2 : c < 2)`, also where the proof uses only one half of it
  or neither (this is the source of the unused-variable warnings of the
  build).

Theorem B of the note (`T'_c`, `S*_c`, `J_c`) is formalized in the second
half of the file with the same encoding: `Tc'`, `Sstar`, `Jc`. `J_c` is written
`J_c(1,y) = y`, `J_c(x,y) = 1` if `x < 1` and `x ≤ y`, and
`max(min(1, c − x), y)` if `y < x < 1`; on `[0,1]²` this is the note's
three-case definition (the cases overlap only at `(1,1)`, where both give `1`).

Not formalized: that `I_c` and `J_c` are fuzzy implications (Definition 2.1),
and the phrases "is an (S,N)-implication / QL-implication" beyond the identities
of Theorem A items 3–4 and Theorem B item 3 together with `IsTConorm SL`,
`IsTConorm (Sstar c)` and `IsFuzzyNegation (Nc c)`; the Corollary of the note
(statements about the classes of implications and the cardinality of the
intersection) is not formalized. Lemmas 1–3 of the note are not stated
separately: their content is proved directly for `T_c` and `T'_c`.
-/
import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

namespace Conjectura.Research.WeberUniqueness

open Set

/-! ### Definitions -/

/-- A t-norm on `[0,1]`, for a function `ℝ → ℝ → ℝ` (only its values on
`[0,1]²` matter). -/
structure IsTNorm (T : ℝ → ℝ → ℝ) : Prop where
  mem : ∀ x ∈ Icc (0 : ℝ) 1, ∀ y ∈ Icc (0 : ℝ) 1, T x y ∈ Icc (0 : ℝ) 1
  comm : ∀ x ∈ Icc (0 : ℝ) 1, ∀ y ∈ Icc (0 : ℝ) 1, T x y = T y x
  assoc : ∀ x ∈ Icc (0 : ℝ) 1, ∀ y ∈ Icc (0 : ℝ) 1, ∀ z ∈ Icc (0 : ℝ) 1,
    T (T x y) z = T x (T y z)
  one_right : ∀ x ∈ Icc (0 : ℝ) 1, T x 1 = x
  mono_left : ∀ x ∈ Icc (0 : ℝ) 1, ∀ x' ∈ Icc (0 : ℝ) 1, ∀ y ∈ Icc (0 : ℝ) 1,
    x ≤ x' → T x y ≤ T x' y

/-- A t-conorm on `[0,1]`. -/
structure IsTConorm (S : ℝ → ℝ → ℝ) : Prop where
  mem : ∀ x ∈ Icc (0 : ℝ) 1, ∀ y ∈ Icc (0 : ℝ) 1, S x y ∈ Icc (0 : ℝ) 1
  comm : ∀ x ∈ Icc (0 : ℝ) 1, ∀ y ∈ Icc (0 : ℝ) 1, S x y = S y x
  assoc : ∀ x ∈ Icc (0 : ℝ) 1, ∀ y ∈ Icc (0 : ℝ) 1, ∀ z ∈ Icc (0 : ℝ) 1,
    S (S x y) z = S x (S y z)
  zero_right : ∀ x ∈ Icc (0 : ℝ) 1, S x 0 = x
  mono_left : ∀ x ∈ Icc (0 : ℝ) 1, ∀ x' ∈ Icc (0 : ℝ) 1, ∀ y ∈ Icc (0 : ℝ) 1,
    x ≤ x' → S x y ≤ S x' y

/-- A fuzzy negation: non-increasing on `[0,1]`, `N 0 = 1`, `N 1 = 0`. -/
structure IsFuzzyNegation (N : ℝ → ℝ) : Prop where
  mem : ∀ x ∈ Icc (0 : ℝ) 1, N x ∈ Icc (0 : ℝ) 1
  anti : ∀ x ∈ Icc (0 : ℝ) 1, ∀ y ∈ Icc (0 : ℝ) 1, x ≤ y → N y ≤ N x
  map_zero : N 0 = 1
  map_one : N 1 = 0

/-- The residual (R-implication) `I_T(x,y) = sup {t ∈ [0,1] : T(x,t) ≤ y}`. -/
noncomputable def residual (T : ℝ → ℝ → ℝ) (x y : ℝ) : ℝ :=
  sSup {t | t ∈ Icc (0 : ℝ) 1 ∧ T x t ≤ y}

/-- The t-norm `T_c` of Theorem A. -/
noncomputable def Tc (c : ℝ) (x y : ℝ) : ℝ :=
  if max x y = 1 then min x y else max 0 (x + y - c)

/-- The negation `N_c`. -/
noncomputable def Nc (c : ℝ) (x : ℝ) : ℝ :=
  if x = 1 then 0 else min 1 (c - x)

/-- The Łukasiewicz t-conorm `S_L(a,b) = min(1, a + b)`. -/
noncomputable def SL (a b : ℝ) : ℝ := min 1 (a + b)

/-- The implication `I_c` of Theorem A. -/
noncomputable def Ic (c : ℝ) (x y : ℝ) : ℝ :=
  if x = 1 then y else min 1 (c - x + y)

/-- The Weber implication `I_WB(x,y) = 1` for `x < 1`, `I_WB(1,y) = y`. -/
noncomputable def weberImp (x y : ℝ) : ℝ := if x < 1 then 1 else y

/-! ### General facts about t-norms -/

theorem IsTNorm.mono_right {T : ℝ → ℝ → ℝ} (hT : IsTNorm T) {x y y' : ℝ}
    (hx : x ∈ Icc (0 : ℝ) 1) (hy : y ∈ Icc (0 : ℝ) 1) (hy' : y' ∈ Icc (0 : ℝ) 1)
    (h : y ≤ y') : T x y ≤ T x y' := by
  rw [hT.comm x hx y hy, hT.comm x hx y' hy']
  exact hT.mono_left y hy y' hy' x hx h

theorem IsTNorm.zero_right {T : ℝ → ℝ → ℝ} (hT : IsTNorm T) {x : ℝ}
    (hx : x ∈ Icc (0 : ℝ) 1) : T x 0 = 0 := by
  have h0 : (0 : ℝ) ∈ Icc (0 : ℝ) 1 := ⟨le_rfl, zero_le_one⟩
  have h1 : (1 : ℝ) ∈ Icc (0 : ℝ) 1 := ⟨zero_le_one, le_rfl⟩
  have hle : T x 0 ≤ T 1 0 := hT.mono_left x hx 1 h1 0 h0 hx.2
  rw [hT.comm 1 h1 0 h0, hT.one_right 0 h0] at hle
  exact le_antisymm hle (hT.mem x hx 0 h0).1

/-- **Lemma 4 of the note.** If `T` is a t-norm, `T(x,·)` is left-continuous at
`1` (within `[0,1]`) and `I_T(x,y) = 1`, then `x ≤ y`. -/
theorem le_of_residual_eq_one {T : ℝ → ℝ → ℝ} (hT : IsTNorm T) {x y : ℝ}
    (hx : x ∈ Icc (0 : ℝ) 1) (hy : y ∈ Icc (0 : ℝ) 1)
    (hcont : ContinuousWithinAt (T x) (Icc (0 : ℝ) 1) 1)
    (hres : residual T x y = 1) : x ≤ y := by
  by_contra hxy
  push_neg at hxy
  set S := {t | t ∈ Icc (0 : ℝ) 1 ∧ T x t ≤ y} with hS
  have h0 : (0 : ℝ) ∈ Icc (0 : ℝ) 1 := ⟨le_rfl, zero_le_one⟩
  have h1 : (1 : ℝ) ∈ Icc (0 : ℝ) 1 := ⟨zero_le_one, le_rfl⟩
  have hne : S.Nonempty := ⟨0, h0, by rw [hT.zero_right hx]; exact hy.1⟩
  -- every `s ∈ [0,1)` satisfies `T x s ≤ y`
  have hbelow : ∀ s ∈ Icc (0 : ℝ) 1, s < 1 → T x s ≤ y := by
    intro s hs hs1
    have hlt : s < sSup S := by
      have : sSup S = 1 := hres
      rw [this]; exact hs1
    obtain ⟨t, ⟨ht, htle⟩, hst⟩ := exists_lt_of_lt_csSup hne hlt
    exact le_trans (hT.mono_right hx hs ht hst.le) htle
  rw [Metric.continuousWithinAt_iff] at hcont
  obtain ⟨δ, hδ, hδ'⟩ := hcont (x - y) (by linarith)
  set s : ℝ := max 0 (1 - δ / 2) with hs_def
  have hs0 : 0 ≤ s := le_max_left _ _
  have hs1 : s < 1 := max_lt (by norm_num) (by linarith)
  have hsI : s ∈ Icc (0 : ℝ) 1 := ⟨hs0, hs1.le⟩
  have hdist : dist s 1 < δ := by
    rw [Real.dist_eq, abs_of_neg (by linarith)]
    have : 1 - δ / 2 ≤ s := le_max_right _ _
    linarith
  have key := hδ' hsI hdist
  rw [Real.dist_eq, hT.one_right x hx] at key
  have hle := hbelow s hsI hs1
  have := neg_abs_le (T x s - x)
  linarith

/-! ### The t-norm `T_c` -/

theorem Tc_one_left (c : ℝ) {y : ℝ} (hy : y ≤ 1) : Tc c 1 y = y := by
  unfold Tc
  rw [max_eq_left hy, if_pos rfl, min_eq_right hy]

theorem Tc_one_right (c : ℝ) {x : ℝ} (hx : x ≤ 1) : Tc c x 1 = x := by
  unfold Tc
  rw [max_eq_right hx, if_pos rfl, min_eq_left hx]

theorem Tc_of_lt (c : ℝ) {x y : ℝ} (hx : x < 1) (hy : y < 1) :
    Tc c x y = max 0 (x + y - c) := by
  unfold Tc
  rw [if_neg (ne_of_lt (max_lt hx hy))]

private theorem max_aux (a z c : ℝ) (hz : z ≤ c) :
    max 0 (max 0 a + z - c) = max 0 (a + z - c) := by
  rcases le_total a 0 with h | h
  · rw [max_eq_left h, max_eq_left (by linarith : (0 : ℝ) + z - c ≤ 0),
      max_eq_left (by linarith : a + z - c ≤ 0)]
  · rw [max_eq_right h]

private theorem lt_one_of_mem_ne {x : ℝ} (hx : x ∈ Icc (0 : ℝ) 1) (h : x ≠ 1) : x < 1 :=
  lt_of_le_of_ne hx.2 h

/-- **Theorem A, item 1 (first part).** `T_c` is a t-norm. -/
theorem Tc_isTNorm {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2) : IsTNorm (Tc c) := by
  have hmem : ∀ x ∈ Icc (0 : ℝ) 1, ∀ y ∈ Icc (0 : ℝ) 1, Tc c x y ∈ Icc (0 : ℝ) 1 := by
    intro x hx y hy
    unfold Tc
    split_ifs
    · exact ⟨le_min hx.1 hy.1, min_le_of_left_le hx.2⟩
    · exact ⟨le_max_left _ _, max_le zero_le_one (by linarith [hx.2, hy.2])⟩
  refine ⟨hmem, ?_, ?_, ?_, ?_⟩
  · intro x _ y _
    unfold Tc
    rw [max_comm, min_comm, add_comm x y]
  · intro x hx y hy z hz
    by_cases hx1 : x = 1
    · subst hx1
      rw [Tc_one_left c hy.2, Tc_one_left c (hmem y hy z hz).2]
    by_cases hz1 : z = 1
    · subst hz1
      rw [Tc_one_right c (hmem x hx y hy).2, Tc_one_right c hy.2]
    by_cases hy1 : y = 1
    · subst hy1
      rw [Tc_one_right c hx.2, Tc_one_left c hz.2]
    have hx' := lt_one_of_mem_ne hx hx1
    have hy' := lt_one_of_mem_ne hy hy1
    have hz' := lt_one_of_mem_ne hz hz1
    have hxy : max 0 (x + y - c) < 1 := max_lt zero_lt_one (by linarith)
    have hyz : max 0 (y + z - c) < 1 := max_lt zero_lt_one (by linarith)
    rw [Tc_of_lt c hx' hy', Tc_of_lt c hy' hz', Tc_of_lt c hxy hz', Tc_of_lt c hx' hyz,
      max_aux _ _ _ (by linarith : z ≤ c),
      show x + max 0 (y + z - c) - c = max 0 (y + z - c) + x - c by ring,
      max_aux _ _ _ (by linarith : x ≤ c)]
    congr 1
    ring
  · intro x hx
    exact Tc_one_right c hx.2
  · intro x hx x' hx' y hy hle
    by_cases hy1 : y = 1
    · subst hy1
      rw [Tc_one_right c hx.2, Tc_one_right c hx'.2]
      exact hle
    have hy' := lt_one_of_mem_ne hy hy1
    by_cases hx'1 : x' = 1
    · subst hx'1
      rw [Tc_one_left c hy.2]
      by_cases hx1 : x = 1
      · subst hx1
        rw [Tc_one_left c hy.2]
      · rw [Tc_of_lt c (lt_one_of_mem_ne hx hx1) hy']
        exact max_le hy.1 (by linarith [hx.2])
    · have hx'' := lt_one_of_mem_ne hx' hx'1
      rw [Tc_of_lt c (lt_of_le_of_lt hle hx'') hy', Tc_of_lt c hx'' hy']
      exact max_le_max le_rfl (by linarith)

/-- **Theorem A, item 1 (second part): `T_c` is not left-continuous.** For every
`0 < x < 1`, `T_c(x,·)` is not left-continuous at `1` (within `[0,1]`). -/
theorem Tc_not_leftContinuous {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2) {x : ℝ}
    (hx0 : 0 < x) (hx1 : x < 1) :
    ¬ ContinuousWithinAt (Tc c x) (Icc (0 : ℝ) 1) 1 := by
  intro hcont
  rw [Metric.continuousWithinAt_iff] at hcont
  have hε : 0 < x - max 0 (x + 1 - c) := by
    have : max 0 (x + 1 - c) < x := max_lt hx0 (by linarith)
    linarith
  obtain ⟨δ, hδ, hδ'⟩ := hcont _ hε
  set s : ℝ := max 0 (1 - δ / 2) with hs_def
  have hs0 : 0 ≤ s := le_max_left _ _
  have hs1 : s < 1 := max_lt (by norm_num) (by linarith)
  have hdist : dist s 1 < δ := by
    rw [Real.dist_eq, abs_of_neg (by linarith)]
    have : 1 - δ / 2 ≤ s := le_max_right _ _
    linarith
  have key := hδ' ⟨hs0, hs1.le⟩ hdist
  rw [Real.dist_eq, Tc_one_right c hx1.le, Tc_of_lt c hx1 hs1] at key
  have hle : max 0 (x + s - c) ≤ max 0 (x + 1 - c) := max_le_max le_rfl (by linarith)
  have := neg_abs_le (max 0 (x + s - c) - x)
  linarith

/-- **Theorem A, item 1 (second part): `T_c` is not border-continuous.** For
every `0 < x < 1`, `T_c` (as a function of two variables) is not continuous
within `[0,1]²` at the boundary point `(x,1)`. -/
theorem Tc_not_borderContinuous {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2) {x : ℝ}
    (hx0 : 0 < x) (hx1 : x < 1) :
    ¬ ContinuousWithinAt (Function.uncurry (Tc c)) (Icc (0 : ℝ) 1 ×ˢ Icc (0 : ℝ) 1) (x, 1) := by
  intro h
  apply Tc_not_leftContinuous hc1 hc2 hx0 hx1
  have hf : ContinuousWithinAt (fun s : ℝ => (x, s)) (Icc (0 : ℝ) 1) 1 :=
    (continuous_const.prodMk continuous_id).continuousWithinAt
  have hmaps : MapsTo (fun s : ℝ => (x, s)) (Icc (0 : ℝ) 1) (Icc (0 : ℝ) 1 ×ˢ Icc (0 : ℝ) 1) :=
    fun s hs => ⟨⟨hx0.le, hx1.le⟩, hs⟩
  exact h.comp hf hmaps

/-! ### The residual of `T_c` -/

/-- **Theorem A, item 2.** The residual of `T_c` is `I_c` on `[0,1]²`. -/
theorem residual_Tc {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2) {x y : ℝ}
    (hx : x ∈ Icc (0 : ℝ) 1) (hy : y ∈ Icc (0 : ℝ) 1) :
    residual (Tc c) x y = Ic c x y := by
  unfold residual Ic
  by_cases hx1 : x = 1
  · subst hx1
    rw [if_pos rfl]
    have : {t | t ∈ Icc (0 : ℝ) 1 ∧ Tc c 1 t ≤ y} = Icc 0 y := by
      ext t
      simp only [mem_setOf_eq, mem_Icc]
      constructor
      · rintro ⟨⟨ht0, ht1⟩, h⟩
        rw [Tc_one_left c ht1] at h
        exact ⟨ht0, h⟩
      · rintro ⟨ht0, hty⟩
        have ht1 : t ≤ 1 := le_trans hty hy.2
        exact ⟨⟨ht0, ht1⟩, by rw [Tc_one_left c ht1]; exact hty⟩
    rw [this, csSup_Icc hy.1]
  rw [if_neg hx1]
  have hx' := lt_one_of_mem_ne hx hx1
  by_cases hxy : x ≤ y
  · rw [min_eq_left (by linarith : (1 : ℝ) ≤ c - x + y)]
    apply IsGreatest.csSup_eq
    refine ⟨⟨⟨zero_le_one, le_rfl⟩, ?_⟩, ?_⟩
    · rw [Tc_one_right c hx.2]; exact hxy
    · rintro t ⟨ht, _⟩
      exact ht.2
  push_neg at hxy
  -- the set is `{t ∈ [0,1) : t ≤ c - x + y}`
  have hset : {t | t ∈ Icc (0 : ℝ) 1 ∧ Tc c x t ≤ y} =
      {t | t ∈ Ico (0 : ℝ) 1 ∧ t ≤ c - x + y} := by
    ext t
    simp only [mem_setOf_eq, mem_Icc, mem_Ico]
    constructor
    · rintro ⟨⟨ht0, ht1⟩, h⟩
      have ht1' : t ≠ 1 := by
        rintro rfl
        rw [Tc_one_right c hx.2] at h
        linarith
      have ht1'' : t < 1 := lt_of_le_of_ne ht1 ht1'
      rw [Tc_of_lt c hx' ht1''] at h
      exact ⟨⟨ht0, ht1''⟩, by linarith [le_max_right 0 (x + t - c)]⟩
    · rintro ⟨⟨ht0, ht1⟩, h⟩
      refine ⟨⟨ht0, ht1.le⟩, ?_⟩
      rw [Tc_of_lt c hx' ht1]
      exact max_le hy.1 (by linarith)
  rw [hset]
  by_cases hb : c - x + y < 1
  · rw [min_eq_right hb.le]
    have : {t | t ∈ Ico (0 : ℝ) 1 ∧ t ≤ c - x + y} = Icc 0 (c - x + y) := by
      ext t
      simp only [mem_setOf_eq, mem_Ico, mem_Icc]
      constructor
      · rintro ⟨⟨ht0, _⟩, h⟩
        exact ⟨ht0, h⟩
      · rintro ⟨ht0, h⟩
        exact ⟨⟨ht0, by linarith⟩, h⟩
    rw [this, csSup_Icc (by linarith [hx.2, hy.1])]
  · push_neg at hb
    rw [min_eq_left hb]
    have : {t | t ∈ Ico (0 : ℝ) 1 ∧ t ≤ c - x + y} = Ico 0 1 := by
      ext t
      simp only [mem_setOf_eq, mem_Ico]
      constructor
      · rintro ⟨h, _⟩
        exact h
      · rintro ⟨ht0, ht1⟩
        exact ⟨⟨ht0, ht1⟩, by linarith⟩
    rw [this, csSup_Ico zero_lt_one]

/-! ### `I_c` as an (S,N)- and a QL-operation -/

private theorem min_aux (a b : ℝ) (hb : 0 ≤ b) : min 1 (min 1 a + b) = min 1 (a + b) := by
  rcases le_total a 1 with h | h
  · rw [min_eq_right h]
  · rw [min_eq_left h, min_eq_left (by linarith : (1 : ℝ) ≤ 1 + b),
      min_eq_left (by linarith : (1 : ℝ) ≤ a + b)]

/-- **Theorem A, item 3 (the t-conorm).** `S_L` is a t-conorm. -/
theorem SL_isTConorm : IsTConorm SL := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · intro x hx y hy
    exact ⟨le_min zero_le_one (by linarith [hx.1, hy.1]), min_le_left _ _⟩
  · intro x _ y _
    unfold SL
    rw [add_comm]
  · intro x hx y hy z hz
    unfold SL
    rw [min_aux _ _ hz.1, add_comm x (min 1 (y + z)), min_aux _ _ hx.1]
    congr 1
    ring
  · intro x hx
    unfold SL
    rw [add_zero, min_eq_right hx.2]
  · intro x _ x' _ y _ h
    unfold SL
    exact min_le_min le_rfl (by linarith)

/-- **Theorem A, item 3 (the negation).** `N_c` is a fuzzy negation. -/
theorem Nc_isFuzzyNegation {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2) : IsFuzzyNegation (Nc c) := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro x hx
    unfold Nc
    split_ifs
    · exact ⟨le_rfl, zero_le_one⟩
    · exact ⟨le_min zero_le_one (by linarith [hx.2]), min_le_left _ _⟩
  · intro x hx y hy hxy
    unfold Nc
    by_cases hy1 : y = 1
    · rw [if_pos hy1]
      split_ifs
      · exact le_rfl
      · exact le_min zero_le_one (by linarith [hx.2])
    · have hy' := lt_one_of_mem_ne hy hy1
      rw [if_neg hy1, if_neg (ne_of_lt (lt_of_le_of_lt hxy hy'))]
      exact min_le_min le_rfl (by linarith)
  · unfold Nc
    rw [if_neg zero_ne_one, sub_zero, min_eq_left hc1.le]
  · unfold Nc
    rw [if_pos rfl]

/-- **Theorem A, item 3.** `I_c(x,y) = S_L(N_c(x), y)` on `[0,1]²`. -/
theorem Ic_eq_SL_Nc (c : ℝ) {x y : ℝ} (hy : y ∈ Icc (0 : ℝ) 1) :
    Ic c x y = SL (Nc c x) y := by
  unfold Ic SL Nc
  by_cases hx1 : x = 1
  · rw [if_pos hx1, if_pos hx1, zero_add, min_eq_right hy.2]
  · rw [if_neg hx1, if_neg hx1, min_aux _ _ hy.1]

/-- **Theorem A, item 4.** `I_c(x,y) = S_L(N_c(x), T_M(x,y))` on `[0,1]²`. -/
theorem Ic_eq_SL_Nc_min {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2) {x y : ℝ}
    (hx : x ∈ Icc (0 : ℝ) 1) (hy : y ∈ Icc (0 : ℝ) 1) :
    Ic c x y = SL (Nc c x) (min x y) := by
  unfold Ic SL Nc
  by_cases hx1 : x = 1
  · subst hx1
    rw [if_pos rfl, if_pos rfl, zero_add, min_eq_right hy.2, min_eq_right hy.2]
  · rw [if_neg hx1, if_neg hx1, min_aux _ _ (le_min hx.1 hy.1)]
    rcases le_total y x with h | h
    · rw [min_eq_right h]
    · rw [min_eq_left h, min_eq_left (by linarith : (1 : ℝ) ≤ c - x + y),
        min_eq_left (by linarith : (1 : ℝ) ≤ c - x + x)]

/-! ### Failure of (OP) and consequences -/

/-- **Theorem A, item 5 (first part).** `0 < c − 1 ≤ 1` and
`I_{T_c}(c − 1, 0) = 1`. -/
theorem residual_Tc_violates_OP {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2) :
    0 < c - 1 ∧ c - 1 ≤ 1 ∧ residual (Tc c) (c - 1) 0 = 1 := by
  refine ⟨by linarith, by linarith, ?_⟩
  rw [residual_Tc hc1 hc2 ⟨by linarith, by linarith⟩ ⟨le_rfl, zero_le_one⟩]
  unfold Ic
  rw [if_neg (by linarith : c - 1 ≠ 1)]
  rw [show c - (c - 1) + 0 = 1 by ring, min_self]

/-- **Theorem A, item 5 (second part).** The residual of `T_c` is not the
residual of any t-norm `T'` such that `T'(x,·)` is left-continuous at `1` for
every `x ∈ [0,1]` (in particular of no left-continuous t-norm): the two
residuals differ at some point of `[0,1]²`. -/
theorem residual_ne_of_leftContinuous {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2)
    {T' : ℝ → ℝ → ℝ} (hT' : IsTNorm T')
    (hcont : ∀ x ∈ Icc (0 : ℝ) 1, ContinuousWithinAt (T' x) (Icc (0 : ℝ) 1) 1) :
    ∃ x ∈ Icc (0 : ℝ) 1, ∃ y ∈ Icc (0 : ℝ) 1, residual T' x y ≠ residual (Tc c) x y := by
  obtain ⟨h0, h1, hres⟩ := residual_Tc_violates_OP hc1 hc2
  have hxI : c - 1 ∈ Icc (0 : ℝ) 1 := ⟨h0.le, h1⟩
  have h0I : (0 : ℝ) ∈ Icc (0 : ℝ) 1 := ⟨le_rfl, zero_le_one⟩
  refine ⟨c - 1, hxI, 0, h0I, ?_⟩
  rw [hres]
  intro h
  have := le_of_residual_eq_one hT' hxI h0I (hcont _ hxI) h
  linarith

/-- **Theorem A, item 6 (first part).** `I_c ≠ I_WB` on `[0,1]²`. -/
theorem Ic_ne_weberImp {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2) :
    ∃ x ∈ Icc (0 : ℝ) 1, ∃ y ∈ Icc (0 : ℝ) 1, Ic c x y ≠ weberImp x y := by
  refine ⟨c / 2, ⟨by linarith, by linarith⟩, 0, ⟨le_rfl, zero_le_one⟩, ?_⟩
  unfold Ic weberImp
  rw [if_neg (by linarith : c / 2 ≠ 1), if_pos (by linarith : c / 2 < 1),
    min_eq_right (by linarith : c - c / 2 + 0 ≤ 1)]
  linarith

/-- **Theorem A, item 6 (second part).** `I_c ≠ I_{c'}` for `c ≠ c'`. -/
theorem Ic_ne_Ic {c c' : ℝ} (hc1 : 1 < c) (hc2 : c < 2) (hc1' : 1 < c') (hc2' : c' < 2)
    (hne : c ≠ c') :
    ∃ x ∈ Icc (0 : ℝ) 1, ∃ y ∈ Icc (0 : ℝ) 1, Ic c x y ≠ Ic c' x y := by
  -- `x = max c c' / 2` lies in `(max c c' − 1, 1)`
  set m := max c c' with hm
  have hcm : c ≤ m := le_max_left _ _
  have hc'm : c' ≤ m := le_max_right _ _
  have hm2 : m < 2 := max_lt hc2 hc2'
  have hm1 : 1 < m := lt_of_lt_of_le hc1 hcm
  refine ⟨m / 2, ⟨by linarith, by linarith⟩, 0, ⟨le_rfl, zero_le_one⟩, ?_⟩
  unfold Ic
  rw [if_neg (by linarith : m / 2 ≠ 1), if_neg (by linarith : m / 2 ≠ 1),
    min_eq_right (by linarith : c - m / 2 + 0 ≤ 1),
    min_eq_right (by linarith : c' - m / 2 + 0 ≤ 1)]
  intro h
  exact hne (by linarith)

/-! ## Theorem B

Source statement (same note, Theorem B): for `1 < c < 2` let
`T'_c(x,y) = min(x,y)` if `max(x,y) = 1` or `x + y > c`, `T'_c(x,y) = 0`
otherwise, and `S*_c(a,b) = max(a,b)` if `a + b < c`, `S*_c(a,b) = 1` if
`a + b ≥ c`. Then
1. `T'_c` is a t-norm, neither border-continuous nor left-continuous; `S*_c` is
   a t-conorm;
2. the residual of `T'_c` is `J_c(x,y) = 1` if `x ≤ y`,
   `J_c(x,y) = max(min(1, c − x), y)` if `y < x < 1`, `J_c(1,y) = y`;
3. `J_c(x,y) = S*_c(N_c(x), y) = S*_c(N_c(x), T_M(x,y))` for all `x, y`;
4. `J_c(c − 1, 0) = 1`, so `J_c` violates (OP) and is not the residual of any
   left-continuous t-norm;
5. `J_c ≠ I_WB`, `J_c ≠ I_c`, and `J_c ≠ J_{c'}` for `c ≠ c'`.
-/

/-- The t-norm `T'_c` of Theorem B. -/
noncomputable def Tc' (c : ℝ) (x y : ℝ) : ℝ :=
  if max x y = 1 ∨ c < x + y then min x y else 0

/-- The t-conorm `S*_c` of Theorem B. -/
noncomputable def Sstar (c : ℝ) (a b : ℝ) : ℝ :=
  if a + b < c then max a b else 1

/-- The implication `J_c` of Theorem B. -/
noncomputable def Jc (c : ℝ) (x y : ℝ) : ℝ :=
  if x = 1 then y else if x ≤ y then 1 else max (min 1 (c - x)) y

theorem Tc'_one_left (c : ℝ) {y : ℝ} (hy : y ≤ 1) : Tc' c 1 y = y := by
  unfold Tc'
  rw [max_eq_left hy, if_pos (Or.inl rfl), min_eq_right hy]

theorem Tc'_one_right (c : ℝ) {x : ℝ} (hx : x ≤ 1) : Tc' c x 1 = x := by
  unfold Tc'
  rw [max_eq_right hx, if_pos (Or.inl rfl), min_eq_left hx]

theorem Tc'_of_lt (c : ℝ) {x y : ℝ} (hx : x < 1) (hy : y < 1) :
    Tc' c x y = if c < x + y then min x y else 0 := by
  unfold Tc'
  have h : max x y ≠ 1 := ne_of_lt (max_lt hx hy)
  simp only [h, false_or]

/-- **Theorem B, item 1 (first part).** `T'_c` is a t-norm. -/
theorem Tc'_isTNorm {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2) : IsTNorm (Tc' c) := by
  have hmem : ∀ x ∈ Icc (0 : ℝ) 1, ∀ y ∈ Icc (0 : ℝ) 1, Tc' c x y ∈ Icc (0 : ℝ) 1 := by
    intro x hx y hy
    unfold Tc'
    split_ifs
    · exact ⟨le_min hx.1 hy.1, min_le_of_left_le hx.2⟩
    · exact ⟨le_rfl, zero_le_one⟩
  refine ⟨hmem, ?_, ?_, ?_, ?_⟩
  · intro x _ y _
    unfold Tc'
    rw [max_comm, min_comm, add_comm x y]
  · intro x hx y hy z hz
    by_cases hx1 : x = 1
    · subst hx1
      rw [Tc'_one_left c hy.2, Tc'_one_left c (hmem y hy z hz).2]
    by_cases hz1 : z = 1
    · subst hz1
      rw [Tc'_one_right c (hmem x hx y hy).2, Tc'_one_right c hy.2]
    by_cases hy1 : y = 1
    · subst hy1
      rw [Tc'_one_right c hx.2, Tc'_one_left c hz.2]
    have hx' := lt_one_of_mem_ne hx hx1
    have hy' := lt_one_of_mem_ne hy hy1
    have hz' := lt_one_of_mem_ne hz hz1
    have hxy : Tc' c x y < 1 := by
      rw [Tc'_of_lt c hx' hy']
      split_ifs
      · exact lt_of_le_of_lt (min_le_left _ _) hx'
      · exact zero_lt_one
    have hyz : Tc' c y z < 1 := by
      rw [Tc'_of_lt c hy' hz']
      split_ifs
      · exact lt_of_le_of_lt (min_le_left _ _) hy'
      · exact zero_lt_one
    rw [Tc'_of_lt c hxy hz', Tc'_of_lt c hx' hyz, Tc'_of_lt c hx' hy', Tc'_of_lt c hy' hz']
    obtain ⟨hx0, -⟩ := hx
    obtain ⟨hy0, -⟩ := hy
    obtain ⟨hz0, -⟩ := hz
    simp only [min_def]
    split_ifs <;> linarith
  · intro x hx
    exact Tc'_one_right c hx.2
  · intro x hx x' hx' y hy hle
    by_cases hy1 : y = 1
    · subst hy1
      rw [Tc'_one_right c hx.2, Tc'_one_right c hx'.2]
      exact hle
    have hy' := lt_one_of_mem_ne hy hy1
    by_cases hx'1 : x' = 1
    · subst hx'1
      rw [Tc'_one_left c hy.2]
      by_cases hx1 : x = 1
      · subst hx1
        rw [Tc'_one_left c hy.2]
      · rw [Tc'_of_lt c (lt_one_of_mem_ne hx hx1) hy']
        split_ifs
        · exact min_le_right _ _
        · exact hy.1
    · have hx'' := lt_one_of_mem_ne hx' hx'1
      rw [Tc'_of_lt c (lt_of_le_of_lt hle hx'') hy', Tc'_of_lt c hx'' hy']
      split_ifs with h1 h2
      · exact min_le_min hle le_rfl
      · exact absurd (by linarith : c < x' + y) h2
      · exact le_min hx'.1 hy.1
      · exact le_rfl

/-- **Theorem B, item 1 (second part).** For every `0 < x ≤ c − 1`, `T'_c(x,·)`
is not left-continuous at `1` (within `[0,1]`). -/
theorem Tc'_not_leftContinuous {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2) {x : ℝ}
    (hx0 : 0 < x) (hxc : x ≤ c - 1) :
    ¬ ContinuousWithinAt (Tc' c x) (Icc (0 : ℝ) 1) 1 := by
  intro hcont
  have hx1 : x < 1 := by linarith
  rw [Metric.continuousWithinAt_iff] at hcont
  obtain ⟨δ, hδ, hδ'⟩ := hcont x hx0
  set s : ℝ := max 0 (1 - δ / 2) with hs_def
  have hs0 : 0 ≤ s := le_max_left _ _
  have hs1 : s < 1 := max_lt (by norm_num) (by linarith)
  have hdist : dist s 1 < δ := by
    rw [Real.dist_eq, abs_of_neg (by linarith)]
    have : 1 - δ / 2 ≤ s := le_max_right _ _
    linarith
  have key := hδ' ⟨hs0, hs1.le⟩ hdist
  rw [Real.dist_eq, Tc'_one_right c hx1.le, Tc'_of_lt c hx1 hs1,
    if_neg (by linarith : ¬ c < x + s), zero_sub, abs_neg, abs_of_pos hx0] at key
  exact lt_irrefl _ key

/-- **Theorem B, item 1 (second part).** For every `0 < x ≤ c − 1`, `T'_c` is
not continuous within `[0,1]²` at the boundary point `(x,1)`. -/
theorem Tc'_not_borderContinuous {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2) {x : ℝ}
    (hx0 : 0 < x) (hxc : x ≤ c - 1) :
    ¬ ContinuousWithinAt (Function.uncurry (Tc' c)) (Icc (0 : ℝ) 1 ×ˢ Icc (0 : ℝ) 1) (x, 1) := by
  intro h
  apply Tc'_not_leftContinuous hc1 hc2 hx0 hxc
  have hf : ContinuousWithinAt (fun s : ℝ => (x, s)) (Icc (0 : ℝ) 1) 1 :=
    (continuous_const.prodMk continuous_id).continuousWithinAt
  have hmaps : MapsTo (fun s : ℝ => (x, s)) (Icc (0 : ℝ) 1) (Icc (0 : ℝ) 1 ×ˢ Icc (0 : ℝ) 1) :=
    fun s hs => ⟨⟨hx0.le, by linarith⟩, hs⟩
  exact h.comp hf hmaps

/-- **Theorem B, item 1 (third part).** `S*_c` is a t-conorm. -/
theorem Sstar_isTConorm {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2) : IsTConorm (Sstar c) := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · intro x hx y hy
    unfold Sstar
    split_ifs
    · exact ⟨le_max_of_le_left hx.1, max_le hx.2 hy.2⟩
    · exact ⟨zero_le_one, le_rfl⟩
  · intro x _ y _
    unfold Sstar
    rw [add_comm, max_comm]
  · intro x hx y hy z hz
    obtain ⟨hx0, hx1⟩ := hx
    obtain ⟨hy0, hy1⟩ := hy
    obtain ⟨hz0, hz1⟩ := hz
    unfold Sstar
    simp only [max_def]
    split_ifs <;> linarith
  · intro x hx
    unfold Sstar
    rw [add_zero, if_pos (by linarith [hx.2]), max_eq_left hx.1]
  · intro x hx x' hx' y hy h
    unfold Sstar
    split_ifs with h1 h2
    · exact max_le_max h le_rfl
    · exact max_le hx.2 hy.2
    · exact absurd (by linarith : x + y < c) h1
    · exact le_rfl

/-- **Theorem B, item 2.** The residual of `T'_c` is `J_c` on `[0,1]²`. -/
theorem residual_Tc' {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2) {x y : ℝ}
    (hx : x ∈ Icc (0 : ℝ) 1) (hy : y ∈ Icc (0 : ℝ) 1) :
    residual (Tc' c) x y = Jc c x y := by
  unfold residual Jc
  by_cases hx1 : x = 1
  · subst hx1
    rw [if_pos rfl]
    have : {t | t ∈ Icc (0 : ℝ) 1 ∧ Tc' c 1 t ≤ y} = Icc 0 y := by
      ext t
      simp only [mem_setOf_eq, mem_Icc]
      constructor
      · rintro ⟨⟨ht0, ht1⟩, h⟩
        rw [Tc'_one_left c ht1] at h
        exact ⟨ht0, h⟩
      · rintro ⟨ht0, hty⟩
        have ht1 : t ≤ 1 := le_trans hty hy.2
        exact ⟨⟨ht0, ht1⟩, by rw [Tc'_one_left c ht1]; exact hty⟩
    rw [this, csSup_Icc hy.1]
  rw [if_neg hx1]
  have hx' := lt_one_of_mem_ne hx hx1
  by_cases hxy : x ≤ y
  · rw [if_pos hxy]
    apply IsGreatest.csSup_eq
    refine ⟨⟨⟨zero_le_one, le_rfl⟩, ?_⟩, ?_⟩
    · rw [Tc'_one_right c hx.2]; exact hxy
    · rintro t ⟨ht, _⟩
      exact ht.2
  rw [if_neg hxy]
  push_neg at hxy
  have hset : {t | t ∈ Icc (0 : ℝ) 1 ∧ Tc' c x t ≤ y} =
      {t | t ∈ Ico (0 : ℝ) 1 ∧ t ≤ max (c - x) y} := by
    ext t
    simp only [mem_setOf_eq, mem_Icc, mem_Ico, le_max_iff]
    constructor
    · rintro ⟨⟨ht0, ht1⟩, h⟩
      have ht1' : t ≠ 1 := by
        rintro rfl
        rw [Tc'_one_right c hx.2] at h
        linarith
      have ht1'' : t < 1 := lt_of_le_of_ne ht1 ht1'
      rw [Tc'_of_lt c hx' ht1''] at h
      refine ⟨⟨ht0, ht1''⟩, ?_⟩
      split_ifs at h with hc
      · right
        rcases le_total x t with hxt | htx
        · rw [min_eq_left hxt] at h; linarith
        · rw [min_eq_right htx] at h; exact h
      · left; linarith
    · rintro ⟨⟨ht0, ht1⟩, h⟩
      refine ⟨⟨ht0, ht1.le⟩, ?_⟩
      rw [Tc'_of_lt c hx' ht1]
      split_ifs with hc
      · rcases h with h | h
        · linarith
        · exact le_trans (min_le_right _ _) h
      · exact hy.1
  rw [hset]
  by_cases hb : max (c - x) y < 1
  · have hcx : c - x < 1 := lt_of_le_of_lt (le_max_left _ _) hb
    rw [min_eq_right hcx.le]
    have : {t | t ∈ Ico (0 : ℝ) 1 ∧ t ≤ max (c - x) y} = Icc 0 (max (c - x) y) := by
      ext t
      simp only [mem_setOf_eq, mem_Ico, mem_Icc]
      constructor
      · rintro ⟨⟨ht0, _⟩, h⟩
        exact ⟨ht0, h⟩
      · rintro ⟨ht0, h⟩
        exact ⟨⟨ht0, by linarith⟩, h⟩
    rw [this, csSup_Icc (le_max_of_le_right hy.1)]
  · push_neg at hb
    have hcx : 1 ≤ c - x := by
      rcases le_max_iff.mp hb with h | h
      · exact h
      · linarith
    rw [min_eq_left hcx, max_eq_left hy.2]
    have : {t | t ∈ Ico (0 : ℝ) 1 ∧ t ≤ max (c - x) y} = Ico 0 1 := by
      ext t
      simp only [mem_setOf_eq, mem_Ico]
      constructor
      · rintro ⟨h, _⟩
        exact h
      · rintro ⟨ht0, ht1⟩
        exact ⟨⟨ht0, ht1⟩, by linarith⟩
    rw [this, csSup_Ico zero_lt_one]

/-- **Theorem B, item 3 (first identity).** `J_c(x,y) = S*_c(N_c(x), y)` on
`[0,1]²`. -/
theorem Jc_eq_Sstar_Nc {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2) {x y : ℝ}
    (hx : x ∈ Icc (0 : ℝ) 1) (hy : y ∈ Icc (0 : ℝ) 1) :
    Jc c x y = Sstar c (Nc c x) y := by
  obtain ⟨hx0, hx1⟩ := hx
  obtain ⟨hy0, hy1⟩ := hy
  unfold Jc Sstar Nc
  by_cases h1 : x = 1
  · rw [if_pos h1, if_pos h1, zero_add, if_pos (by linarith), max_eq_right hy0]
  · rw [if_neg h1, if_neg h1]
    have hx' : x < 1 := lt_of_le_of_ne hx1 h1
    simp only [min_def, max_def]
    split_ifs <;> linarith

/-- **Theorem B, item 3 (second identity).** `J_c(x,y) = S*_c(N_c(x), T_M(x,y))`
on `[0,1]²`. -/
theorem Jc_eq_Sstar_Nc_min {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2) {x y : ℝ}
    (hx : x ∈ Icc (0 : ℝ) 1) (hy : y ∈ Icc (0 : ℝ) 1) :
    Jc c x y = Sstar c (Nc c x) (min x y) := by
  obtain ⟨hx0, hx1⟩ := hx
  obtain ⟨hy0, hy1⟩ := hy
  unfold Jc Sstar Nc
  by_cases h1 : x = 1
  · subst h1
    rw [if_pos rfl, if_pos rfl, zero_add, min_eq_right hy1, if_pos (by linarith),
      max_eq_right hy0]
  · rw [if_neg h1, if_neg h1]
    have hx' : x < 1 := lt_of_le_of_ne hx1 h1
    simp only [min_def, max_def]
    split_ifs <;> linarith

/-- **Theorem B, item 4 (first part).** `0 < c − 1 ≤ 1` and
`I_{T'_c}(c − 1, 0) = 1`. -/
theorem residual_Tc'_violates_OP {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2) :
    0 < c - 1 ∧ c - 1 ≤ 1 ∧ residual (Tc' c) (c - 1) 0 = 1 := by
  refine ⟨by linarith, by linarith, ?_⟩
  rw [residual_Tc' hc1 hc2 ⟨by linarith, by linarith⟩ ⟨le_rfl, zero_le_one⟩]
  unfold Jc
  rw [if_neg (by linarith : c - 1 ≠ 1), if_neg (by linarith : ¬ c - 1 ≤ 0),
    show c - (c - 1) = 1 by ring, min_self, max_eq_left zero_le_one]

/-- **Theorem B, item 4 (second part).** The residual of `T'_c` is not the
residual of any t-norm `T'` such that `T'(x,·)` is left-continuous at `1` for
every `x ∈ [0,1]`. -/
theorem residual_Tc'_ne_of_leftContinuous {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2)
    {T' : ℝ → ℝ → ℝ} (hT' : IsTNorm T')
    (hcont : ∀ x ∈ Icc (0 : ℝ) 1, ContinuousWithinAt (T' x) (Icc (0 : ℝ) 1) 1) :
    ∃ x ∈ Icc (0 : ℝ) 1, ∃ y ∈ Icc (0 : ℝ) 1, residual T' x y ≠ residual (Tc' c) x y := by
  obtain ⟨h0, h1, hres⟩ := residual_Tc'_violates_OP hc1 hc2
  have hxI : c - 1 ∈ Icc (0 : ℝ) 1 := ⟨h0.le, h1⟩
  have h0I : (0 : ℝ) ∈ Icc (0 : ℝ) 1 := ⟨le_rfl, zero_le_one⟩
  refine ⟨c - 1, hxI, 0, h0I, ?_⟩
  rw [hres]
  intro h
  have := le_of_residual_eq_one hT' hxI h0I (hcont _ hxI) h
  linarith

/-- **Theorem B, item 5.** `J_c ≠ I_WB`, `J_c ≠ I_c`, and `J_c ≠ J_{c'}` for
`c ≠ c'` (each: the two functions differ at some point of `[0,1]²`). -/
theorem Jc_ne_weberImp {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2) :
    ∃ x ∈ Icc (0 : ℝ) 1, ∃ y ∈ Icc (0 : ℝ) 1, Jc c x y ≠ weberImp x y := by
  refine ⟨c / 2, ⟨by linarith, by linarith⟩, 0, ⟨le_rfl, zero_le_one⟩, ?_⟩
  unfold Jc weberImp
  rw [if_neg (by linarith : c / 2 ≠ 1), if_neg (by linarith : ¬ c / 2 ≤ 0),
    if_pos (by linarith : c / 2 < 1), min_eq_right (by linarith : c - c / 2 ≤ 1),
    max_eq_left (by linarith : (0 : ℝ) ≤ c - c / 2)]
  linarith

theorem Jc_ne_Ic {c : ℝ} (hc1 : 1 < c) (hc2 : c < 2) :
    ∃ x ∈ Icc (0 : ℝ) 1, ∃ y ∈ Icc (0 : ℝ) 1, Jc c x y ≠ Ic c x y := by
  refine ⟨(2 + c) / 4, ⟨by linarith, by linarith⟩, (2 - c) / 4, ⟨by linarith, by linarith⟩, ?_⟩
  unfold Jc Ic
  rw [if_neg (by linarith : (2 + c) / 4 ≠ 1), if_neg (by linarith : ¬ (2 + c) / 4 ≤ (2 - c) / 4),
    if_neg (by linarith : (2 + c) / 4 ≠ 1),
    min_eq_right (by linarith : c - (2 + c) / 4 ≤ 1),
    max_eq_left (by linarith : (2 - c) / 4 ≤ c - (2 + c) / 4),
    min_eq_right (by linarith : c - (2 + c) / 4 + (2 - c) / 4 ≤ 1)]
  intro h
  linarith

theorem Jc_ne_Jc {c c' : ℝ} (hc1 : 1 < c) (hc2 : c < 2) (hc1' : 1 < c') (hc2' : c' < 2)
    (hne : c ≠ c') :
    ∃ x ∈ Icc (0 : ℝ) 1, ∃ y ∈ Icc (0 : ℝ) 1, Jc c x y ≠ Jc c' x y := by
  set m := max c c' with hm
  have hcm : c ≤ m := le_max_left _ _
  have hc'm : c' ≤ m := le_max_right _ _
  have hm2 : m < 2 := max_lt hc2 hc2'
  have hm1 : 1 < m := lt_of_lt_of_le hc1 hcm
  refine ⟨m / 2, ⟨by linarith, by linarith⟩, 0, ⟨le_rfl, zero_le_one⟩, ?_⟩
  unfold Jc
  rw [if_neg (by linarith : m / 2 ≠ 1), if_neg (by linarith : ¬ m / 2 ≤ 0),
    if_neg (by linarith : m / 2 ≠ 1), if_neg (by linarith : ¬ m / 2 ≤ 0),
    min_eq_right (by linarith : c - m / 2 ≤ 1), min_eq_right (by linarith : c' - m / 2 ≤ 1),
    max_eq_left (by linarith : (0 : ℝ) ≤ c - m / 2),
    max_eq_left (by linarith : (0 : ℝ) ≤ c' - m / 2)]
  intro h
  exact hne (by linarith)

/-! ### Non-vacuity -/

/-- The minimum `T_M` is a t-norm. -/
theorem min_isTNorm : IsTNorm (fun x y : ℝ => min x y) := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · intro x hx y hy
    exact ⟨le_min hx.1 hy.1, min_le_of_left_le hx.2⟩
  · intro x _ y _
    exact min_comm x y
  · intro x _ y _ z _
    exact min_assoc x y z
  · intro x hx
    exact min_eq_left hx.2
  · intro x _ x' _ y _ h
    exact min_le_min h le_rfl

/-- Non-vacuity of the hypotheses of the registered theorems: `c = 6/5` and
`c' = 7/5` satisfy `1 < c < 2`, `1 < c' < 2`, `c ≠ c'`; `x = 1/5` satisfies
`0 < x < 1` and `0 < x ≤ c − 1` for `c = 6/5`; the minimum t-norm satisfies the
t-norm and left-continuity hypotheses of `le_of_residual_eq_one`,
`residual_ne_of_leftContinuous` and `residual_Tc'_ne_of_leftContinuous`, and
`x = y = 0` with `T = min` satisfies all hypotheses of `le_of_residual_eq_one`
including `I_T(x,y) = 1`. -/
theorem hypotheses_nonvacuous :
    ((1 : ℝ) < 6 / 5 ∧ (6 / 5 : ℝ) < 2) ∧
    ((1 : ℝ) < 7 / 5 ∧ (7 / 5 : ℝ) < 2) ∧ (6 / 5 : ℝ) ≠ 7 / 5 ∧
    ((0 : ℝ) < 1 / 5 ∧ (1 / 5 : ℝ) < 1 ∧ (1 / 5 : ℝ) ≤ 6 / 5 - 1) ∧
    IsTNorm (fun x y : ℝ => min x y) ∧
    (∀ x ∈ Icc (0 : ℝ) 1, ContinuousWithinAt (fun y : ℝ => min x y) (Icc (0 : ℝ) 1) 1) ∧
    ((0 : ℝ) ∈ Icc (0 : ℝ) 1 ∧ residual (fun x y : ℝ => min x y) 0 0 = 1) := by
  refine ⟨⟨by norm_num, by norm_num⟩, ⟨by norm_num, by norm_num⟩, by norm_num,
    ⟨by norm_num, by norm_num, by norm_num⟩, min_isTNorm, ?_, ⟨le_rfl, zero_le_one⟩, ?_⟩
  · intro x _
    exact (continuous_const.min continuous_id).continuousWithinAt
  · unfold residual
    apply IsGreatest.csSup_eq
    refine ⟨⟨⟨zero_le_one, le_rfl⟩, min_le_left 0 1⟩, ?_⟩
    rintro t ⟨ht, _⟩
    exact ht.2

end Conjectura.Research.WeberUniqueness
