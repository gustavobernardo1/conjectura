/-
RESEARCH — problem CJ-0001 (Collins–Shor peak conjecture), supporting
algebra ("cone arithmetic") for the note
`research/active/CJ-0001-collins-shor-peak/notes/lower-bound.md`.

Source statements in that note:

* Proposition S34(b), last display (plant rule for `E`):
  `E^ = x [E + Ω + 2G + x(3 + 2x)H]`;
* Proposition S35 (two planted trees): the displayed identity, the bracket
  `H_1 W_2 + H_2 W_1 − 2 J_1 J_2 = Σ_{v,v′} (δ_v − δ_{v′})² a_v a_{v′}` of its
  proof, and its "Consequently";
* Theorem T5, proof of (iii) (`R(A, e_u) = E + (1+x)Ω + x(1+x)H ∈ K_{a+1}`)
  and the paragraph "The terms `E^_i P_i`" of the proof of (ii)
  (`E^_i ∈ K_{a_i+2}`).

What this module is. It proves only the algebraic steps: polynomial identities
in `Polynomial ℝ`, and memberships in the cones `K_d` (`WienerCone d`) that
follow from other memberships taken as HYPOTHESES. Nothing about trees,
Laplacians, determinants, adjugates, distances or the states
`(Ψ, H, G, Ω, R, E)` of a rooted tree is formalized: every polynomial below is
an arbitrary element of `Polynomial ℝ`, every `δ` an arbitrary function to
`ℕ`. In particular the plant and merge rules themselves (S19, S34(a)–(d)), the
memberships of Proposition S33, Lemma K, Lemma S32, the induction of Theorem
T5 and Theorem T6 are NOT formalized here.

Encoding:

* coefficients are real; `p ∈ K_d` is `WienerCone d p` (see `WienerCone.lean`,
  including what is not proved about that predicate);
* the cone index is a natural number. To avoid natural subtraction the orders
  are written `a = b + 2` (`a_i = b_i + 2`), so `K_{a−2} = K_b`,
  `K_{a−1} = K_{b+1}`, `K_a = K_{b+2}`, `K_{a+1} = K_{b+3}`,
  `K_{a+2} = K_{b+4}` and `K_{a_1+a_2+2} = K_{b_1+b_2+6}`. The statements
  therefore cover orders `a ≥ 2` only; the case `a = 1` of the note (where
  `H = G = 0` and the vertex sums are empty) is not an instance of the
  index-shifted statements;
* `G/x` of the note is a separate polynomial `Gh` and `G` is `X * Gh`, so
  `2G` is `2 * X * Gh`;
* the vertex sets `A_1 ∖ u_1`, `A_2 ∖ u_2` are arbitrary finite types `ι`, `κ`
  (possibly empty), `a_v` arbitrary families of polynomials, and the distances
  `δ_v` arbitrary natural numbers cast to `Polynomial ℝ`; the subtraction
  `δ_v − δ_{v′}` is taken in `Polynomial ℝ`, after the cast, so it is a true
  subtraction;
* `H_i`, `J_i`, `W_i`, `R¹_i` are written out as `∑ v, a v`,
  `∑ v, δ v * a v`, `∑ v, δ v ^ 2 * a v` and `Q + X ^ 2 * ∑ v, δ v ^ 2 * a v`
  in the identities; in `two_planted_mem` they are free polynomials with
  memberships as hypotheses.
-/
import Conjectura.Research.CollinsShorPeak.WienerCone
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Tactic.Ring

namespace Conjectura.Research.CollinsShorPeak

open Polynomial

/-! ### Closure lemmas for the cone -/

/-- The cone `K_d` is closed under finite sums. -/
theorem WienerCone.sum {d : ℕ} {ι : Type*} (s : Finset ι) (f : ι → Polynomial ℝ)
    (h : ∀ i ∈ s, WienerCone d (f i)) : WienerCone d (∑ i ∈ s, f i) :=
  Finset.sum_induction f (WienerCone d) (fun _ _ hp hq => WienerCone.add hp hq)
    WienerCone.zero h

/-- `x^k ∈ K_{2k}`. -/
theorem WienerCone.X_pow_mem (k : ℕ) : WienerCone (2 * k) ((X : Polynomial ℝ) ^ k) := by
  have h := WienerCone.gen (d := 2 * k) k 0 (by omega)
  simpa using h

/-- **(K2), iterated.** `x^k · K_d ⊆ K_{d+2k}`. -/
theorem WienerCone.X_pow_mul_mem {d : ℕ} (k : ℕ) {p : Polynomial ℝ} (hp : WienerCone d p) :
    WienerCone (d + 2 * k) (X ^ k * p) := by
  rw [mul_comm (X ^ k) p]
  exact hp.mul (WienerCone.X_pow_mem k)

/-- The cone `K_d` is closed under multiplication by a non-negative constant. -/
theorem WienerCone.C_mul {d : ℕ} {p : Polynomial ℝ} {c : ℝ} (hc : 0 ≤ c)
    (hp : WienerCone d p) : WienerCone d (C c * p) :=
  WienerCone.smul c hc hp

/-! ### Theorem T5: the plant step of (ii) and statement (iii) -/

/-- **Plant step in the proof of Theorem T5(ii)** (`lower-bound.md`, paragraph
"The terms `E^_i P_i`", with the formula for `E^` of Proposition S34(b)).
Orders `a = b + 2 ≥ 2`. If `E ∈ K_{a+1}`, `Ω ∈ K_a`, `G/x = Gh ∈ K_{a−1}` and
`H ∈ K_{a−2}`, then `x [E + Ω + 2G + x(3 + 2x)H] ∈ K_{a+2}`, where `G = x·Gh`.
The polynomials are arbitrary; no tree is involved. -/
theorem plant_E_mem {b : ℕ} {E Ω Gh H : Polynomial ℝ}
    (hE : WienerCone (b + 3) E) (hΩ : WienerCone (b + 2) Ω)
    (hGh : WienerCone (b + 1) Gh) (hH : WienerCone b H) :
    WienerCone (b + 4) (X * (E + Ω + 2 * X * Gh + X * (3 + 2 * X) * H)) := by
  have h2 : (C (2 : ℝ) : Polynomial ℝ) = 2 := C_ofNat 2
  have h3 : (C (3 : ℝ) : Polynomial ℝ) = 3 := C_ofNat 3
  have e : X * (E + Ω + 2 * X * Gh + X * (3 + 2 * X) * H) =
      X * E + X * Ω + C (2 : ℝ) * (X ^ 2 * Gh) + C (3 : ℝ) * (X ^ 2 * H)
        + C (2 : ℝ) * (X ^ 3 * H) := by
    rw [h2, h3]
    ring
  rw [e]
  have t1 : WienerCone (b + 4) (X * E) := hE.X_mul_mem_add_two.mono (by omega)
  have t2 : WienerCone (b + 4) (X * Ω) := hΩ.X_mul_mem_add_two.mono (by omega)
  have t3 : WienerCone (b + 4) (C (2 : ℝ) * (X ^ 2 * Gh)) :=
    WienerCone.C_mul (by norm_num) ((hGh.X_pow_mul_mem 2).mono (by omega))
  have t4 : WienerCone (b + 4) (C (3 : ℝ) * (X ^ 2 * H)) :=
    WienerCone.C_mul (by norm_num) ((hH.X_pow_mul_mem 2).mono (by omega))
  have t5 : WienerCone (b + 4) (C (2 : ℝ) * (X ^ 3 * H)) :=
    WienerCone.C_mul (by norm_num) ((hH.X_pow_mul_mem 3).mono (by omega))
  exact (((t1.add t2).add t3).add t4).add t5

/-- **Theorem T5, the step "(iii) follows from (i) and (ii)"** (`lower-bound.md`).
Orders `a = b + 2 ≥ 2`. If `E ∈ K_{a+1}`, `Ω ∈ K_a` and `H ∈ K_{a−2}`, then
`E + (1+x)Ω + x(1+x)H ∈ K_{a+1}`. That this polynomial is `R(A, e_u)`
(Proposition S34(a)) is not formalized; the polynomials are arbitrary. -/
theorem raised_R_mem {b : ℕ} {E Ω H : Polynomial ℝ}
    (hE : WienerCone (b + 3) E) (hΩ : WienerCone (b + 2) Ω) (hH : WienerCone b H) :
    WienerCone (b + 3) (E + (1 + X) * Ω + X * (1 + X) * H) := by
  rw [mul_assoc X (1 + X) H]
  have t2 : WienerCone (b + 3) ((1 + X) * Ω) := hΩ.one_add_X_mul_mem_succ.mono (by omega)
  have t3 : WienerCone (b + 3) (X * ((1 + X) * H)) :=
    hH.one_add_X_mul_mem_succ.X_mul_mem_add_two.mono (by omega)
  exact (hE.add t2).add t3

/-! ### Proposition S35: two planted trees -/

/-- **The bracket in the proof of Proposition S35** (`lower-bound.md`). For
finite index types `ι`, `κ`, families of polynomials `a`, `a'` and natural
numbers `δ`, `δ'`, with `H = Σ a_v`, `J = Σ δ_v a_v`, `W = Σ δ_v² a_v` (and
`H'`, `J'`, `W'` likewise, all written out):
`H W' + H' W − 2 J J' = Σ_{v,w} (δ_v − δ'_w)² a_v a'_w`. -/
theorem sum_sq_identity {ι κ : Type*} [Fintype ι] [Fintype κ]
    (a : ι → Polynomial ℝ) (a' : κ → Polynomial ℝ) (δ : ι → ℕ) (δ' : κ → ℕ) :
    (∑ v, a v) * (∑ w, (δ' w : Polynomial ℝ) ^ 2 * a' w)
        + (∑ w, a' w) * (∑ v, (δ v : Polynomial ℝ) ^ 2 * a v)
        - 2 * (∑ v, (δ v : Polynomial ℝ) * a v) * (∑ w, (δ' w : Polynomial ℝ) * a' w)
      = ∑ v, ∑ w, ((δ v : Polynomial ℝ) - (δ' w : Polynomial ℝ)) ^ 2 * a v * a' w := by
  rw [mul_comm (∑ w, a' w), mul_assoc 2, Finset.sum_mul_sum, Finset.sum_mul_sum,
    Finset.sum_mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib, ← Finset.sum_sub_distrib]
  refine Finset.sum_congr rfl fun v _ => ?_
  rw [Finset.mul_sum, ← Finset.sum_add_distrib, ← Finset.sum_sub_distrib]
  refine Finset.sum_congr rfl fun w _ => ?_
  ring

/-- **The displayed identity of Proposition S35** (`lower-bound.md`), as an
identity between arbitrary polynomials. With `H = Σ a_v`, `J = Σ δ_v a_v`,
`W = Σ δ_v² a_v`, `R¹ = Q + x² W` (and the primed analogues), all written out,
and arbitrary `Ψ`, `Ψ'`, `Q`, `Q'`:
`x((Ψ + xH) R¹' + (Ψ' + xH') R¹) − 2 (x²J)(x²J')
   = x(Ψ R¹' + Ψ' R¹) + x²(H Q' + H' Q) + x⁴ Σ_{v,w} (δ_v − δ'_w)² a_v a'_w`.
That the left side is `x(H^_1 Ω^_2 + H^_2 Ω^_1) − 2 G^_1 G^_2` for two planted
trees (S34(b), S33) is not formalized. -/
theorem two_planted_identity {ι κ : Type*} [Fintype ι] [Fintype κ]
    (a : ι → Polynomial ℝ) (a' : κ → Polynomial ℝ) (δ : ι → ℕ) (δ' : κ → ℕ)
    (Ψ Ψ' Q Q' : Polynomial ℝ) :
    X * ((Ψ + X * ∑ v, a v) * (Q' + X ^ 2 * ∑ w, (δ' w : Polynomial ℝ) ^ 2 * a' w)
          + (Ψ' + X * ∑ w, a' w) * (Q + X ^ 2 * ∑ v, (δ v : Polynomial ℝ) ^ 2 * a v))
        - 2 * (X ^ 2 * ∑ v, (δ v : Polynomial ℝ) * a v)
          * (X ^ 2 * ∑ w, (δ' w : Polynomial ℝ) * a' w)
      = X * (Ψ * (Q' + X ^ 2 * ∑ w, (δ' w : Polynomial ℝ) ^ 2 * a' w)
            + Ψ' * (Q + X ^ 2 * ∑ v, (δ v : Polynomial ℝ) ^ 2 * a v))
        + X ^ 2 * ((∑ v, a v) * Q' + (∑ w, a' w) * Q)
        + X ^ 4 * ∑ v, ∑ w,
            ((δ v : Polynomial ℝ) - (δ' w : Polynomial ℝ)) ^ 2 * a v * a' w := by
  rw [← sum_sq_identity a a' δ δ']
  ring

/-- **Cone membership of the right side of the identity of Proposition S35**
(`lower-bound.md`, last paragraph of the proof). Orders `a_i = b_i + 2 ≥ 2`.
For arbitrary polynomials with `Ψ ∈ K_{a_1−1}`, `Ψ' ∈ K_{a_2−1}`,
`R1 ∈ K_{a_1+1}`, `R1' ∈ K_{a_2+1}`, `H ∈ K_{a_1−2}`, `H' ∈ K_{a_2−2}`,
`Q ∈ K_{a_1}`, `Q' ∈ K_{a_2}`, `a_v ∈ K_{a_1−2}`, `a'_w ∈ K_{a_2−2}` and
arbitrary natural numbers `δ_v`, `δ'_w`:
`x(Ψ R1' + Ψ' R1) + x²(H Q' + H' Q) + x⁴ Σ_{v,w} (δ_v − δ'_w)² a_v a'_w
   ∈ K_{a_1+a_2+2}`.
Here `R1`, `H`, `Q` are free: no relation between them and the family `a` is
assumed (see `two_planted_lhs_mem` for the statement with the relations). -/
theorem two_planted_mem {ι κ : Type*} [Fintype ι] [Fintype κ] {b1 b2 : ℕ}
    {a : ι → Polynomial ℝ} {a' : κ → Polynomial ℝ} (δ : ι → ℕ) (δ' : κ → ℕ)
    {Ψ Ψ' R1 R1' H H' Q Q' : Polynomial ℝ}
    (hΨ : WienerCone (b1 + 1) Ψ) (hΨ' : WienerCone (b2 + 1) Ψ')
    (hR1 : WienerCone (b1 + 3) R1) (hR1' : WienerCone (b2 + 3) R1')
    (hH : WienerCone b1 H) (hH' : WienerCone b2 H')
    (hQ : WienerCone (b1 + 2) Q) (hQ' : WienerCone (b2 + 2) Q')
    (ha : ∀ v, WienerCone b1 (a v)) (ha' : ∀ w, WienerCone b2 (a' w)) :
    WienerCone (b1 + b2 + 6)
      (X * (Ψ * R1' + Ψ' * R1) + X ^ 2 * (H * Q' + H' * Q)
        + X ^ 4 * ∑ v, ∑ w,
            ((δ v : Polynomial ℝ) - (δ' w : Polynomial ℝ)) ^ 2 * a v * a' w) := by
  have hsq : ∀ v w, ((δ v : Polynomial ℝ) - (δ' w : Polynomial ℝ)) ^ 2 =
      C (((δ v : ℝ) - (δ' w : ℝ)) ^ 2) := by
    intro v w
    simp
  have t1a : WienerCone (b1 + b2 + 4) (Ψ * R1') := (hΨ.mul hR1').mono (by omega)
  have t1b : WienerCone (b1 + b2 + 4) (Ψ' * R1) := (hΨ'.mul hR1).mono (by omega)
  have t1 : WienerCone (b1 + b2 + 6) (X * (Ψ * R1' + Ψ' * R1)) :=
    (t1a.add t1b).X_mul_mem_add_two.mono (by omega)
  have t2a : WienerCone (b1 + b2 + 2) (H * Q') := (hH.mul hQ').mono (by omega)
  have t2b : WienerCone (b1 + b2 + 2) (H' * Q) := (hH'.mul hQ).mono (by omega)
  have t2 : WienerCone (b1 + b2 + 6) (X ^ 2 * (H * Q' + H' * Q)) :=
    ((t2a.add t2b).X_pow_mul_mem 2).mono (by omega)
  have t3 : WienerCone (b1 + b2 + 6)
      (X ^ 4 * ∑ v, ∑ w,
        ((δ v : Polynomial ℝ) - (δ' w : Polynomial ℝ)) ^ 2 * a v * a' w) := by
    refine (WienerCone.X_pow_mul_mem 4 (d := b1 + b2) ?_).mono (by omega)
    refine WienerCone.sum _ _ fun v _ => WienerCone.sum _ _ fun w _ => ?_
    rw [hsq, mul_assoc]
    exact WienerCone.C_mul (sq_nonneg _) ((ha v).mul (ha' w))
  exact (t1.add t2).add t3

/-- **The "Consequently" of Proposition S35** (`lower-bound.md`), for the left
side of its identity. Orders `a_i = b_i + 2 ≥ 2`. Let `a_v ∈ K_{a_1−2}`,
`a'_w ∈ K_{a_2−2}`, `Ψ ∈ K_{a_1−1}`, `Ψ' ∈ K_{a_2−1}`, `Q ∈ K_{a_1}`,
`Q' ∈ K_{a_2}`, and suppose `R¹ = Q + x² Σ δ_v² a_v ∈ K_{a_1+1}` and
`R¹' = Q' + x² Σ δ'_w² a'_w ∈ K_{a_2+1}`. Then, with `H = Σ a_v`,
`J = Σ δ_v a_v` (and primes),
`x((Ψ + xH) R¹' + (Ψ' + xH') R¹) − 2 (x²J)(x²J') ∈ K_{a_1+a_2+2}`. -/
theorem two_planted_lhs_mem {ι κ : Type*} [Fintype ι] [Fintype κ] {b1 b2 : ℕ}
    {a : ι → Polynomial ℝ} {a' : κ → Polynomial ℝ} (δ : ι → ℕ) (δ' : κ → ℕ)
    {Ψ Ψ' Q Q' : Polynomial ℝ}
    (hΨ : WienerCone (b1 + 1) Ψ) (hΨ' : WienerCone (b2 + 1) Ψ')
    (hR1 : WienerCone (b1 + 3) (Q + X ^ 2 * ∑ v, (δ v : Polynomial ℝ) ^ 2 * a v))
    (hR1' : WienerCone (b2 + 3) (Q' + X ^ 2 * ∑ w, (δ' w : Polynomial ℝ) ^ 2 * a' w))
    (hQ : WienerCone (b1 + 2) Q) (hQ' : WienerCone (b2 + 2) Q')
    (ha : ∀ v, WienerCone b1 (a v)) (ha' : ∀ w, WienerCone b2 (a' w)) :
    WienerCone (b1 + b2 + 6)
      (X * ((Ψ + X * ∑ v, a v) * (Q' + X ^ 2 * ∑ w, (δ' w : Polynomial ℝ) ^ 2 * a' w)
            + (Ψ' + X * ∑ w, a' w) * (Q + X ^ 2 * ∑ v, (δ v : Polynomial ℝ) ^ 2 * a v))
        - 2 * (X ^ 2 * ∑ v, (δ v : Polynomial ℝ) * a v)
          * (X ^ 2 * ∑ w, (δ' w : Polynomial ℝ) * a' w)) := by
  rw [two_planted_identity]
  exact two_planted_mem δ δ' hΨ hΨ' hR1 hR1'
    (WienerCone.sum _ _ fun v _ => ha v) (WienerCone.sum _ _ fun w _ => ha' w) hQ hQ' ha ha'

/-! ### Non-vacuity -/

/-- The hypotheses of `plant_E_mem`, `raised_R_mem`, `two_planted_mem` and
`two_planted_lhs_mem` are satisfiable for every `b`: the powers `(1 + x)^j`
lie in `K_j` (hence `(1 + x)^{b+3} ∈ K_{b+2}` as well), and with the one-point
index type `Fin 1`, `δ = 1`, `a_v = (1 + x)^b`, `Q = (1 + x)^{b+3}`:
`Q + x² Σ_v δ_v² a_v ∈ K_{b+3}`. -/
theorem lowerBoundCone_hypotheses_witness (b : ℕ) :
    WienerCone (b + 3) ((1 + X : Polynomial ℝ) ^ (b + 3)) ∧
      WienerCone (b + 2) ((1 + X : Polynomial ℝ) ^ (b + 3)) ∧
      WienerCone (b + 2) ((1 + X : Polynomial ℝ) ^ (b + 2)) ∧
      WienerCone (b + 1) ((1 + X : Polynomial ℝ) ^ (b + 1)) ∧
      WienerCone b ((1 + X : Polynomial ℝ) ^ b) ∧
      WienerCone (b + 3) ((1 + X : Polynomial ℝ) ^ (b + 3)
        + X ^ 2 * ∑ _v : Fin 1, ((1 : ℕ) : Polynomial ℝ) ^ 2 * (1 + X) ^ b) := by
  refine ⟨WienerCone.one_add_X_pow_mem _, (WienerCone.one_add_X_pow_mem _).mono (by omega),
    WienerCone.one_add_X_pow_mem _, WienerCone.one_add_X_pow_mem _,
    WienerCone.one_add_X_pow_mem _, ?_⟩
  refine (WienerCone.one_add_X_pow_mem _).add ?_
  refine (WienerCone.X_pow_mul_mem 2 (d := b) ?_).mono (by omega)
  refine WienerCone.sum _ _ fun _ _ => ?_
  rw [← C_eq_natCast, ← C_pow]
  exact WienerCone.C_mul (sq_nonneg _) (WienerCone.one_add_X_pow_mem b)

end Conjectura.Research.CollinsShorPeak
