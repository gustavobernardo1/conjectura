/-
RESEARCH — problem CJ-0001 (Collins–Shor peak conjecture), supporting lemma.

Source statement: Lemma L4 ("vertex principle") in
`research/active/CJ-0001-collins-shor-peak/notes/vertex-principle.md`:

  Let `f : ℝ^s → ℝ` be a polynomial of degree at most 1 in each variable, let
  `λ ∈ ℤ^s` and let `S > Σ λ_i` be an integer. Suppose that for all `i ≠ k` the
  mixed partial derivative `∂²f/∂x_i∂x_k` is non-negative at every real point
  `x ≥ λ`. Then for every integer point `c ≥ λ` with `Σ c_i = S`,
  `f(c) ≥ min_p f(λ + (S − Σ λ_i) e_p)`.

This module formalizes the DISCRETE CORE of Lemma L4 in `s` variables, not
Lemma L4 as written. `vertex_principle_discrete` has the same domain, the same
slice and the same conclusion as L4, and it contains the induction on the
coordinates above their lower bound. Its hypothesis is different:

* L4 assumes that `f` is a polynomial of degree at most 1 in each variable
  whose mixed partial derivatives are non-negative at the real points `x ≥ λ`.
* Here `f` is an arbitrary function `(ι → ℤ) → ℝ` (no polynomial, no
  derivative, no real points), and the hypothesis is the exchange inequality
  `f(c + e_i − e_k) + f(c + e_k − e_i) ≤ 2 f(c)`, assumed for all `i ≠ k` at
  the integer points `c ≥ λ` of the slice `Σ c_j = S` with `c_i > λ_i` and
  `c_k > λ_k`.

For a multi-affine `f` one has
`f(c + e_i − e_k) + f(c + e_k − e_i) − 2 f(c) = −2 ∂²f/∂x_i∂x_k (c)`, so the
hypothesis of L4 implies the hypothesis used here. That implication (the bridge
from multi-affine polynomials) is NOT formalized in this module.

Encoding:

* the index set is any finite type `ι` with decidable equality (`Fin s` is the
  case of the written lemma); points are functions `ι → ℤ`;
* `e_i` is `Pi.single i 1`, and the vertex `λ + (S − Σ λ_j) e_p` is
  `lam + Pi.single p (S - ∑ j, lam j)`, with true integer subtraction;
* "`f(c) ≥ min_p f(v_p)`" is stated as `∃ p, f (v_p) ≤ f c`, which is the same
  statement for a minimum over a finite non-empty index set;
  `vertex_principle_discrete_min` restates it with `Finset.inf'`;
* `S > Σ λ_j` is the hypothesis `∑ j, lam j < S`; it forces `ι` to be
  non-empty.

The proof is the proof of the written lemma: induction on the set of
coordinates above their lower bound, with `min_endpoints_le_of_concave` of
`ExtremalReduction.lean` applied along the line `c + t (e_i − e_k)`.
-/
import Conjectura.Research.CollinsShorPeak.ExtremalReduction
import Mathlib.Algebra.BigOperators.Pi
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.FinCases

namespace Conjectura.Research.CollinsShorPeak

section

variable {ι : Type*} [DecidableEq ι]

/-- The point `c + u (e_i − e_k)`: `u` units are moved from coordinate `k` to
coordinate `i`. Auxiliary to the proof of `vertex_principle_discrete`; it does
not occur in the statement of that theorem. -/
def lineShift (c : ι → ℤ) (i k : ι) (u : ℤ) : ι → ℤ :=
  c + Pi.single i u - Pi.single k u

theorem lineShift_apply (c : ι → ℤ) (i k : ι) (u : ℤ) (j : ι) :
    lineShift c i k u j = c j + (if j = i then u else 0) - (if j = k then u else 0) := by
  simp [lineShift, Pi.single_apply]

theorem lineShift_self (c : ι → ℤ) {i k : ι} (hik : i ≠ k) (u : ℤ) :
    lineShift c i k u i = c i + u := by
  simp [lineShift_apply, hik]

theorem lineShift_other (c : ι → ℤ) {i k : ι} (hik : i ≠ k) (u : ℤ) :
    lineShift c i k u k = c k - u := by
  simp [lineShift_apply, hik.symm]

theorem lineShift_ne (c : ι → ℤ) {i k j : ι} (hji : j ≠ i) (hjk : j ≠ k) (u : ℤ) :
    lineShift c i k u j = c j := by
  simp [lineShift_apply, hji, hjk]

theorem lineShift_zero (c : ι → ℤ) (i k : ι) : lineShift c i k 0 = c := by
  funext j
  simp [lineShift_apply]

theorem lineShift_lineShift (c : ι → ℤ) (i k : ι) (u v : ℤ) :
    lineShift (lineShift c i k u) i k v = lineShift c i k (u + v) := by
  funext j
  simp only [lineShift_apply]
  split_ifs <;> ring

theorem lineShift_swap (c : ι → ℤ) (i k : ι) (u : ℤ) :
    lineShift c k i u = lineShift c i k (-u) := by
  funext j
  simp only [lineShift_apply]
  split_ifs <;> ring

theorem lineShift_ge {lam c : ι → ℤ} {i k : ι} (hik : i ≠ k) (hc : ∀ j, lam j ≤ c j) (u : ℤ)
    (h1 : lam i ≤ c i + u) (h2 : lam k ≤ c k - u) : ∀ j, lam j ≤ lineShift c i k u j := by
  intro j
  by_cases hji : j = i
  · rw [hji, lineShift_self c hik]
    exact h1
  · by_cases hjk : j = k
    · rw [hjk, lineShift_other c hik]
      exact h2
    · rw [lineShift_ne c hji hjk]
      exact hc j

variable [Fintype ι]

/-- Moving units between two coordinates does not change the coordinate sum. -/
theorem sum_lineShift (c : ι → ℤ) (i k : ι) (u : ℤ) :
    ∑ j, lineShift c i k u j = ∑ j, c j := by
  simp [lineShift_apply, Finset.sum_add_distrib, Finset.sum_sub_distrib]

/-- One application of discrete concavity along the line `c + t (e_i − e_k)`:
the value at `c` is at least the smaller of the values at the two points of
the line where coordinate `i`, respectively coordinate `k`, reaches its lower
bound. -/
theorem min_lineEnds_le (f : (ι → ℤ) → ℝ) (lam : ι → ℤ) (S : ℤ)
    (hex : ∀ (c : ι → ℤ) (i k : ι), i ≠ k → (∀ j, lam j ≤ c j) → ∑ j, c j = S →
      lam i < c i → lam k < c k →
      f (c + Pi.single i 1 - Pi.single k 1) + f (c + Pi.single k 1 - Pi.single i 1) ≤ 2 * f c)
    (c : ι → ℤ) (i k : ι) (hik : i ≠ k) (hc : ∀ j, lam j ≤ c j) (hS : ∑ j, c j = S) :
    min (f (lineShift c i k (-(c i - lam i)))) (f (lineShift c i k (c k - lam k))) ≤ f c := by
  have hci := hc i
  have hck := hc k
  obtain ⟨T, hT⟩ : ∃ T : ℕ, (T : ℤ) = c i - lam i :=
    ⟨(c i - lam i).toNat, Int.toNat_of_nonneg (by omega)⟩
  obtain ⟨N, hN⟩ : ∃ N : ℕ, (N : ℤ) = (c i - lam i) + (c k - lam k) :=
    ⟨((c i - lam i) + (c k - lam k)).toNat, Int.toNat_of_nonneg (by omega)⟩
  have hconc : ∀ t : ℕ, t + 2 ≤ N →
      f (lineShift c i k ((t : ℤ) - T)) + f (lineShift c i k (((t + 2 : ℕ) : ℤ) - T)) ≤
        2 * f (lineShift c i k (((t + 1 : ℕ) : ℤ) - T)) := by
    intro t ht
    have h := hex (lineShift c i k (((t + 1 : ℕ) : ℤ) - T)) i k hik
      (lineShift_ge hik hc _ (by omega) (by omega))
      (by rw [sum_lineShift]; exact hS)
      (by rw [lineShift_self c hik]; omega)
      (by rw [lineShift_other c hik]; omega)
    have e1 : lineShift c i k (((t + 1 : ℕ) : ℤ) - T) + Pi.single i 1 - Pi.single k 1 =
        lineShift c i k (((t + 2 : ℕ) : ℤ) - T) := by
      show lineShift (lineShift c i k (((t + 1 : ℕ) : ℤ) - T)) i k 1 = _
      rw [lineShift_lineShift]
      congr 1
      omega
    have e2 : lineShift c i k (((t + 1 : ℕ) : ℤ) - T) + Pi.single k 1 - Pi.single i 1 =
        lineShift c i k ((t : ℤ) - T) := by
      show lineShift (lineShift c i k (((t + 1 : ℕ) : ℤ) - T)) k i 1 = _
      rw [lineShift_swap, lineShift_lineShift]
      congr 1
      omega
    rw [e1, e2] at h
    linarith
  have key : min (f (lineShift c i k (((0 : ℕ) : ℤ) - T))) (f (lineShift c i k ((N : ℤ) - T))) ≤
      f (lineShift c i k ((T : ℤ) - T)) :=
    min_endpoints_le_of_concave (fun t : ℕ => f (lineShift c i k ((t : ℤ) - T))) N hconc T
      (by omega)
  have e0 : lineShift c i k (((0 : ℕ) : ℤ) - T) = lineShift c i k (-(c i - lam i)) := by
    congr 1
    omega
  have eN : lineShift c i k ((N : ℤ) - T) = lineShift c i k (c k - lam k) := by
    congr 1
    omega
  have eT : lineShift c i k ((T : ℤ) - T) = c := by
    rw [sub_self, lineShift_zero]
  rw [e0, eN, eT] at key
  exact key

/-- The induction of Lemma L4, on a finite set `s` that contains every
coordinate above its lower bound. -/
theorem vertex_principle_discrete_aux (f : (ι → ℤ) → ℝ) (lam : ι → ℤ) (S : ℤ)
    (hlt : ∑ j, lam j < S)
    (hex : ∀ (c : ι → ℤ) (i k : ι), i ≠ k → (∀ j, lam j ≤ c j) → ∑ j, c j = S →
      lam i < c i → lam k < c k →
      f (c + Pi.single i 1 - Pi.single k 1) + f (c + Pi.single k 1 - Pi.single i 1) ≤ 2 * f c) :
    ∀ (s : Finset ι) (c : ι → ℤ), (∀ j, lam j ≤ c j) → ∑ j, c j = S →
      (∀ j, lam j < c j → j ∈ s) → ∃ p, f (lam + Pi.single p (S - ∑ j, lam j)) ≤ f c := by
  intro s
  induction s using Finset.strongInduction with
  | H s ih =>
    intro c hc hS hsupp
    by_cases h2 : ∃ i k, i ≠ k ∧ lam i < c i ∧ lam k < c k
    · obtain ⟨i, k, hik, hi, hk⟩ := h2
      have hmin := min_lineEnds_le f lam S hex c i k hik hc hS
      rcases min_le_iff.mp hmin with h | h
      · -- the end of the line where coordinate `i` is at its lower bound
        have hsupp' : ∀ j, lam j < lineShift c i k (-(c i - lam i)) j → j ∈ s.erase i := by
          intro j hj
          have hji : j ≠ i := by
            intro hji
            rw [hji, lineShift_self c hik] at hj
            omega
          rw [Finset.mem_erase]
          refine ⟨hji, ?_⟩
          by_cases hjk : j = k
          · rw [hjk]
            exact hsupp k hk
          · rw [lineShift_ne c hji hjk] at hj
            exact hsupp j hj
        obtain ⟨p, hp⟩ := ih (s.erase i) (Finset.erase_ssubset (hsupp i hi))
          (lineShift c i k (-(c i - lam i)))
          (lineShift_ge hik hc _ (by omega) (by omega))
          (by rw [sum_lineShift]; exact hS) hsupp'
        exact ⟨p, le_trans hp h⟩
      · -- the end of the line where coordinate `k` is at its lower bound
        have hsupp' : ∀ j, lam j < lineShift c i k (c k - lam k) j → j ∈ s.erase k := by
          intro j hj
          have hjk : j ≠ k := by
            intro hjk
            rw [hjk, lineShift_other c hik] at hj
            omega
          rw [Finset.mem_erase]
          refine ⟨hjk, ?_⟩
          by_cases hji : j = i
          · rw [hji]
            exact hsupp i hi
          · rw [lineShift_ne c hji hjk] at hj
            exact hsupp j hj
        obtain ⟨p, hp⟩ := ih (s.erase k) (Finset.erase_ssubset (hsupp k hk))
          (lineShift c i k (c k - lam k))
          (lineShift_ge hik hc _ (by omega) (by omega))
          (by rw [sum_lineShift]; exact hS) hsupp'
        exact ⟨p, le_trans hp h⟩
    · -- at most one coordinate is above its lower bound: `c` is a vertex
      have hex1 : ∃ p, lam p < c p := by
        by_contra hno
        have hle : ∀ j, c j ≤ lam j := fun j => not_lt.mp (fun hj => hno ⟨j, hj⟩)
        have hsum : ∑ j, c j ≤ ∑ j, lam j := Finset.sum_le_sum (fun j _ => hle j)
        linarith
      obtain ⟨p, hp⟩ := hex1
      have hrest : ∀ j, j ≠ p → c j = lam j := by
        intro j hjp
        by_contra hne
        exact h2 ⟨j, p, hjp, lt_of_le_of_ne (hc j) (Ne.symm hne), hp⟩
      have hceq : c = lam + Pi.single p (c p - lam p) := by
        funext j
        by_cases hjp : j = p
        · rw [hjp]
          simp
        · simp [hjp, hrest j hjp]
      have hsum : ∑ j, c j = ∑ j, lam j + (c p - lam p) := by
        have h1 : ∑ j, c j = ∑ j, (lam j + (Pi.single p (c p - lam p) : ι → ℤ) j) :=
          Finset.sum_congr rfl (fun j _ => congrFun hceq j)
        rw [h1, Finset.sum_add_distrib]
        simp
      have hcp : c p - lam p = S - ∑ j, lam j := by linarith
      have hval : f (lam + Pi.single p (S - ∑ j, lam j)) = f c := by
        rw [← hcp, ← hceq]
      exact ⟨p, hval.le⟩

/-- **Discrete core of Lemma L4 (vertex principle) in `s` variables.** Let `ι`
be a finite index set, `f : (ι → ℤ) → ℝ` any function, `lam : ι → ℤ` and
`S > ∑ j, lam j` an integer. Suppose that for all `i ≠ k` and every integer
point `c ≥ lam` with coordinate sum `S`, `c i > lam i` and `c k > lam k`,

`f (c + e_i − e_k) + f (c + e_k − e_i) ≤ 2 f c`.

Then for every integer point `c ≥ lam` with coordinate sum `S` there is an
index `p` with `f (lam + (S − ∑ j, lam j) e_p) ≤ f c`; that is, `f c` is at
least the minimum of `f` over the vertices of the slice.

This is not Lemma L4 as written: the exchange inequality replaces "`f` is a
polynomial of degree at most 1 in each variable with non-negative mixed
partial derivatives at the real points `x ≥ lam`". That hypothesis implies the
exchange inequality, but the implication is not formalized here. -/
theorem vertex_principle_discrete (f : (ι → ℤ) → ℝ) (lam : ι → ℤ) (S : ℤ)
    (hlt : ∑ j, lam j < S)
    (hex : ∀ (c : ι → ℤ) (i k : ι), i ≠ k → (∀ j, lam j ≤ c j) → ∑ j, c j = S →
      lam i < c i → lam k < c k →
      f (c + Pi.single i 1 - Pi.single k 1) + f (c + Pi.single k 1 - Pi.single i 1) ≤ 2 * f c)
    (c : ι → ℤ) (hc : ∀ j, lam j ≤ c j) (hS : ∑ j, c j = S) :
    ∃ p, f (lam + Pi.single p (S - ∑ j, lam j)) ≤ f c :=
  vertex_principle_discrete_aux f lam S hlt hex Finset.univ c hc hS
    (fun j _ => Finset.mem_univ j)

/-- `vertex_principle_discrete` with the conclusion written as a minimum over
the index set, as in the written lemma. The instance `Nonempty ι` is needed to
state the minimum; it also follows from `∑ j, lam j < S`. -/
theorem vertex_principle_discrete_min [Nonempty ι] (f : (ι → ℤ) → ℝ) (lam : ι → ℤ) (S : ℤ)
    (hlt : ∑ j, lam j < S)
    (hex : ∀ (c : ι → ℤ) (i k : ι), i ≠ k → (∀ j, lam j ≤ c j) → ∑ j, c j = S →
      lam i < c i → lam k < c k →
      f (c + Pi.single i 1 - Pi.single k 1) + f (c + Pi.single k 1 - Pi.single i 1) ≤ 2 * f c)
    (c : ι → ℤ) (hc : ∀ j, lam j ≤ c j) (hS : ∑ j, c j = S) :
    (Finset.univ.inf' Finset.univ_nonempty
      fun p => f (lam + Pi.single p (S - ∑ j, lam j))) ≤ f c := by
  obtain ⟨p, hp⟩ := vertex_principle_discrete f lam S hlt hex c hc hS
  exact le_trans (Finset.inf'_le _ (Finset.mem_univ p)) hp

end

/-- Non-vacuity witness for `vertex_principle_discrete`, in three variables:
`f c = c₀ c₁ + c₀ c₂ + c₁ c₂` (multi-affine, every mixed partial derivative
equal to `1`), `lam = 0`, `S = 3`. The exchange hypothesis holds; it is
exercised at `c = (1, 1, 1)`, where two coordinates are above their lower
bound, and the conclusion is not trivial there: `f c = 3` is strictly larger
than the value `0` of `f` at each of the three vertices `3 e_p`. -/
theorem vertex_principle_nonvacuous :
    ∃ (f : (Fin 3 → ℤ) → ℝ) (lam : Fin 3 → ℤ) (S : ℤ),
      ∑ j, lam j < S ∧
      (∀ (c : Fin 3 → ℤ) (i k : Fin 3), i ≠ k → (∀ j, lam j ≤ c j) → ∑ j, c j = S →
        lam i < c i → lam k < c k →
        f (c + Pi.single i 1 - Pi.single k 1) + f (c + Pi.single k 1 - Pi.single i 1) ≤
          2 * f c) ∧
      ∃ c : Fin 3 → ℤ, (∀ j, lam j ≤ c j) ∧ ∑ j, c j = S ∧
        (∃ i k, i ≠ k ∧ lam i < c i ∧ lam k < c k) ∧
        ∀ p, f (lam + Pi.single p (S - ∑ j, lam j)) < f c := by
  refine ⟨fun c => ((c 0 * c 1 + c 0 * c 2 + c 1 * c 2 : ℤ) : ℝ), fun _ => 0, 3, by simp, ?_,
    fun _ => 1, fun _ => by norm_num, by simp, ⟨0, 1, by decide, by norm_num, by norm_num⟩, ?_⟩
  · intro c i k hik _ _ _ _
    have key : ∀ g : (Fin 3 → ℤ) → ℤ, g = (fun c => c 0 * c 1 + c 0 * c 2 + c 1 * c 2) →
        g (c + Pi.single i 1 - Pi.single k 1) + g (c + Pi.single k 1 - Pi.single i 1) + 2 =
          2 * g c := by
      intro g hg
      subst hg
      fin_cases i <;> fin_cases k <;>
        first
          | exact absurd rfl hik
          | (simp; ring)
    have key' := congrArg (fun z : ℤ => (z : ℝ)) (key _ rfl)
    push_cast at key' ⊢
    linarith
  · intro p
    fin_cases p <;> simp

end Conjectura.Research.CollinsShorPeak
