/-
RESEARCH — problem CJ-0001 (Collins–Shor peak conjecture), supporting lemma.

Source statement: the proof of Lemma L4 ("vertex principle") in
`research/active/CJ-0001-collins-shor-peak/notes/vertex-principle.md`.

This module does NOT formalize Lemma L4. It formalizes the reusable core of its
proof, in a discrete form:

* `min_endpoints_le_of_concave` is the step "on an interval a concave function
  is at least the smaller of its values at the two ends", for a sequence
  `φ 0, …, φ N` whose second differences are non-positive;
* `min_vertices_le_of_exchange` is that step applied along a line
  `a + b = S` in two integer variables: one exchange step of the induction of
  L4, for the pair of coordinates that is moved.

Differences from the written lemma (all of them deliberate):

* L4 is about a polynomial `f : ℝ^s → ℝ` of degree at most 1 in each variable
  and assumes that the mixed partial derivatives `∂²f/∂x_i∂x_k` are
  non-negative at real points `x ≥ λ`. Here there are no polynomials and no
  derivatives: the hypothesis is the inequality on second differences
  `φ t + φ (t + 2) ≤ 2 * φ (t + 1)` at integer points. For a multi-affine `f`
  and `φ(t) = f(c + t(e_i − e_k))` one has
  `φ(t − 1) + φ(t + 1) − 2 φ(t) = −2 ∂²f/∂x_i∂x_k`, so the hypothesis of L4
  implies the hypothesis used here; that implication is NOT formalized.
* L4 has `s` variables and an induction on the number of coordinates above
  their lower bound. Only the two-variable exchange step is stated here; the
  induction and the `s`-variable conclusion are not formalized.
* In `min_vertices_le_of_exchange` the exchange inequality is assumed only at
  integer points `(a, b)` of the line with `a > a₀` and `b > b₀`, which is
  what the proof of L4 uses.

Encoding:

* `φ : ℕ → ℝ`; only the values `φ 0, …, φ N` are constrained or mentioned;
* concavity is written with the middle index shifted by one
  (`t + 2 ≤ N`, middle point `t + 1`), which avoids subtraction in `ℕ`;
* in the two-variable statement `f : ℤ → ℤ → ℝ` and `a₀ b₀ S : ℤ`, so `b - 1`,
  `a - 1`, `S - a₀` and `S - b₀` are true integer subtractions.
-/
import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace Conjectura.Research.CollinsShorPeak

/-- **Discrete concavity on an interval.** If the second differences of
`φ 0, …, φ N` are non-positive, then every `φ t` with `t ≤ N` is at least the
smaller of the two end values `φ 0`, `φ N`. -/
theorem min_endpoints_le_of_concave (φ : ℕ → ℝ) (N : ℕ)
    (hc : ∀ t, t + 2 ≤ N → φ t + φ (t + 2) ≤ 2 * φ (t + 1)) :
    ∀ t ≤ N, min (φ 0) (φ N) ≤ φ t := by
  intro t ht
  by_cases hdec : t + 1 ≤ N ∧ φ (t + 1) ≤ φ t
  · -- a non-increase at `t` propagates to the right: `φ N ≤ φ t`
    obtain ⟨_, hd⟩ := hdec
    have dec : ∀ d, t + d + 1 ≤ N → φ (t + d + 1) ≤ φ (t + d) := by
      intro d
      induction d with
      | zero =>
        intro _
        exact hd
      | succ d ih =>
        intro hd'
        have h1 : φ (t + d + 1) ≤ φ (t + d) := ih (by omega)
        have h2 : φ (t + d) + φ (t + d + 2) ≤ 2 * φ (t + d + 1) := hc (t + d) (by omega)
        have e1 : t + (d + 1) + 1 = t + d + 2 := by omega
        have e2 : t + (d + 1) = t + d + 1 := by omega
        rw [e1, e2]
        linarith
    have key : ∀ d, t + d ≤ N → φ (t + d) ≤ φ t := by
      intro d
      induction d with
      | zero =>
        intro _
        exact le_rfl
      | succ d ih =>
        intro hd'
        exact le_trans (dec d hd') (ih (by omega))
    have hk := key (N - t) (by omega)
    have e : t + (N - t) = N := by omega
    rw [e] at hk
    exact le_trans (min_le_right _ _) hk
  · by_cases htN : t = N
    · rw [htN]
      exact min_le_right _ _
    · -- a strict increase at `t` propagates to the left: `φ 0 ≤ φ t`
      have hinc : φ t < φ (t + 1) := by
        by_contra hcon
        exact hdec ⟨by omega, not_lt.mp hcon⟩
      have inc : ∀ d k, k + d = t → φ k < φ (k + 1) := by
        intro d
        induction d with
        | zero =>
          intro k hk
          have hkt : k = t := by omega
          rw [hkt]
          exact hinc
        | succ d ih =>
          intro k hk
          have h1 : φ (k + 1) < φ (k + 1 + 1) := ih (k + 1) (by omega)
          have h2 : φ k + φ (k + 2) ≤ 2 * φ (k + 1) := hc k (by omega)
          have e1 : k + 1 + 1 = k + 2 := by omega
          rw [e1] at h1
          linarith
      have key : ∀ d, d ≤ t → φ 0 ≤ φ d := by
        intro d
        induction d with
        | zero =>
          intro _
          exact le_rfl
        | succ d ih =>
          intro hd'
          exact le_trans (ih (by omega)) (inc (t - d) d (by omega)).le
      exact le_trans (min_le_left _ _) (key t le_rfl)

/-- **Exchange step along a line `a + b = S`.** Let `f : ℤ → ℤ → ℝ`, and let
`a₀`, `b₀`, `S` be integers. If moving one unit from `b` to `a` and one unit
from `a` to `b` does not increase the sum of the two values above twice the
value at `(a, b)`, at every point of the line with `a > a₀` and `b > b₀`, then
at every point of the line with `a ≥ a₀` and `b ≥ b₀` the value of `f` is at
least the smaller of its values at the two end points `(a₀, S − a₀)` and
`(S − b₀, b₀)`. -/
theorem min_vertices_le_of_exchange (f : ℤ → ℤ → ℝ) (a₀ b₀ S : ℤ)
    (hex : ∀ a b, a₀ < a → b₀ < b → a + b = S →
      f (a + 1) (b - 1) + f (a - 1) (b + 1) ≤ 2 * f a b) :
    ∀ a b, a₀ ≤ a → b₀ ≤ b → a + b = S →
      min (f a₀ (S - a₀)) (f (S - b₀) b₀) ≤ f a b := by
  intro a b ha hb hab
  obtain ⟨N, hN⟩ : ∃ N : ℕ, (N : ℤ) = S - a₀ - b₀ :=
    ⟨(S - a₀ - b₀).toNat, Int.toNat_of_nonneg (by omega)⟩
  obtain ⟨T, hT⟩ : ∃ T : ℕ, (T : ℤ) = a - a₀ :=
    ⟨(a - a₀).toNat, Int.toNat_of_nonneg (by omega)⟩
  have hf : ∀ {x y x' y' : ℤ}, x = x' → y = y' → f x y = f x' y' := by
    intro x y x' y' h1 h2
    rw [h1, h2]
  have hc : ∀ t : ℕ, t + 2 ≤ N →
      f (a₀ + (t : ℤ)) (S - a₀ - (t : ℤ)) +
          f (a₀ + ((t + 2 : ℕ) : ℤ)) (S - a₀ - ((t + 2 : ℕ) : ℤ)) ≤
        2 * f (a₀ + ((t + 1 : ℕ) : ℤ)) (S - a₀ - ((t + 1 : ℕ) : ℤ)) := by
    intro t ht
    have h := hex (a₀ + ((t + 1 : ℕ) : ℤ)) (S - a₀ - ((t + 1 : ℕ) : ℤ))
      (by omega) (by omega) (by omega)
    have e1 : f (a₀ + ((t + 1 : ℕ) : ℤ) + 1) (S - a₀ - ((t + 1 : ℕ) : ℤ) - 1) =
        f (a₀ + ((t + 2 : ℕ) : ℤ)) (S - a₀ - ((t + 2 : ℕ) : ℤ)) :=
      hf (by omega) (by omega)
    have e2 : f (a₀ + ((t + 1 : ℕ) : ℤ) - 1) (S - a₀ - ((t + 1 : ℕ) : ℤ) + 1) =
        f (a₀ + (t : ℤ)) (S - a₀ - (t : ℤ)) :=
      hf (by omega) (by omega)
    rw [e1, e2] at h
    linarith
  have key := min_endpoints_le_of_concave
    (fun t : ℕ => f (a₀ + (t : ℤ)) (S - a₀ - (t : ℤ))) N hc T (by omega)
  have e0 : f a₀ (S - a₀) = f (a₀ + ((0 : ℕ) : ℤ)) (S - a₀ - ((0 : ℕ) : ℤ)) :=
    hf (by omega) (by omega)
  have eN : f (S - b₀) b₀ = f (a₀ + (N : ℤ)) (S - a₀ - (N : ℤ)) :=
    hf (by omega) (by omega)
  have et : f a b = f (a₀ + (T : ℤ)) (S - a₀ - (T : ℤ)) :=
    hf (by omega) (by omega)
  rw [e0, eN, et]
  exact key

/-- Non-vacuity witness for `min_endpoints_le_of_concave`: the sequence
`φ t = t (4 − t)`, that is `0, 3, 4, 3, 0` on `0 ≤ t ≤ 4`, satisfies the
concavity hypothesis with `N = 4` (so the hypothesis is exercised at
`t = 0, 1, 2`) and is not constant. -/
theorem concave_nonvacuous :
    ∃ (φ : ℕ → ℝ) (N : ℕ),
      (∀ t, t + 2 ≤ N → φ t + φ (t + 2) ≤ 2 * φ (t + 1)) ∧ 2 ≤ N ∧ φ 0 < φ 1 := by
  refine ⟨fun t => (t : ℝ) * (4 - (t : ℝ)), 4, ?_, by norm_num, by norm_num⟩
  intro t _
  have h : 2 * (((t + 1 : ℕ) : ℝ) * (4 - ((t + 1 : ℕ) : ℝ))) -
      ((t : ℝ) * (4 - (t : ℝ)) + ((t + 2 : ℕ) : ℝ) * (4 - ((t + 2 : ℕ) : ℝ))) = 2 := by
    push_cast
    ring
  show (t : ℝ) * (4 - (t : ℝ)) + ((t + 2 : ℕ) : ℝ) * (4 - ((t + 2 : ℕ) : ℝ)) ≤
    2 * (((t + 1 : ℕ) : ℝ) * (4 - ((t + 1 : ℕ) : ℝ)))
  linarith

/-- Non-vacuity witness for `min_vertices_le_of_exchange`: `f a b = a b`
(multi-affine, with mixed partial derivative `1`), `a₀ = b₀ = 0`, `S = 4`
satisfies the exchange hypothesis; the hypothesis is exercised (the point
`(2, 2)` lies on the line with `a > a₀`, `b > b₀`), and the conclusion is not
trivial there (`f 2 2 = 4` exceeds both end values, which are `0`). -/
theorem exchange_nonvacuous :
    ∃ (f : ℤ → ℤ → ℝ) (a₀ b₀ S : ℤ),
      (∀ a b, a₀ < a → b₀ < b → a + b = S →
        f (a + 1) (b - 1) + f (a - 1) (b + 1) ≤ 2 * f a b) ∧
      (∃ a b, a₀ < a ∧ b₀ < b ∧ a + b = S ∧ f a₀ (S - a₀) < f a b) := by
  refine ⟨fun a b => (a : ℝ) * (b : ℝ), 0, 0, 4, ?_, 2, 2, by norm_num, by norm_num,
    by norm_num, by norm_num⟩
  intro a b _ _ _
  have h : 2 * ((a : ℝ) * (b : ℝ)) -
      (((a + 1 : ℤ) : ℝ) * ((b - 1 : ℤ) : ℝ) + ((a - 1 : ℤ) : ℝ) * ((b + 1 : ℤ) : ℝ)) = 2 := by
    push_cast
    ring
  show ((a + 1 : ℤ) : ℝ) * ((b - 1 : ℤ) : ℝ) + ((a - 1 : ℤ) : ℝ) * ((b + 1 : ℤ) : ℝ) ≤
    2 * ((a : ℝ) * (b : ℝ))
  linarith

end Conjectura.Research.CollinsShorPeak
