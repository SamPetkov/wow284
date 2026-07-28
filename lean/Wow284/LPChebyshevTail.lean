import Wow284.LPDualFinite

namespace Wow284.LP

noncomputable section

open Polynomial

/-- The interval on which the scaled Chebyshev representation is used. -/
def chebyshevInterval (k : ℕ) : Set ℝ :=
  Set.Icc
    (-2 * Real.sqrt (((k - 1 : ℕ) : ℝ)))
    (2 * Real.sqrt (((k - 1 : ℕ) : ℝ)))

/-- The elementary radical inequality behind inclusion of the WOW window in
the scaled Chebyshev interval. -/
theorem support_radius_inequality (k : ℕ) (hk : 4 ≤ k) :
    1 + Real.sqrt (2 * (((k - 1 : ℕ) : ℝ))) ≤
      2 * Real.sqrt (((k - 1 : ℕ) : ℝ)) := by
  have hk1 : 1 ≤ k := by omega
  have hrNat : 3 ≤ k - 1 := by omega
  have hr : (3 : ℝ) ≤ ((k - 1 : ℕ) : ℝ) := by exact_mod_cast hrNat
  have hr0 : 0 ≤ ((k - 1 : ℕ) : ℝ) := by positivity
  have h2r0 : 0 ≤ 2 * ((k - 1 : ℕ) : ℝ) := by positivity
  have hsqr :
      (Real.sqrt (((k - 1 : ℕ) : ℝ))) ^ 2 = ((k - 1 : ℕ) : ℝ) :=
    Real.sq_sqrt hr0
  have hsq2r :
      (Real.sqrt (2 * (((k - 1 : ℕ) : ℝ)))) ^ 2 =
        2 * ((k - 1 : ℕ) : ℝ) :=
    Real.sq_sqrt h2r0
  have hmargin :
      8 * ((k - 1 : ℕ) : ℝ) ≤
        (2 * ((k - 1 : ℕ) : ℝ) - 1) ^ 2 := by
    nlinarith
  have htwo :
      2 * Real.sqrt (2 * (((k - 1 : ℕ) : ℝ))) ≤
        2 * ((k - 1 : ℕ) : ℝ) - 1 := by
    apply (sq_le_sq₀ (by positivity) (by nlinarith)).mp
    nlinarith
  apply (sq_le_sq₀ (by positivity) (by positivity)).mp
  nlinarith

/-- The complete WOW interval lies in the interval where the scaled
Chebyshev formula is valid. -/
theorem wowInterval_subset_chebyshevInterval (k : ℕ) (hk : 4 ≤ k) :
    wowInterval k ⊆ chebyshevInterval k := by
  intro x hx
  rcases hx with ⟨hxlo, hxhi⟩
  have hk1 : 1 ≤ k := by omega
  have hcast :
      2 * (k : ℝ) - 2 = 2 * (((k - 1 : ℕ) : ℝ)) := by
    rw [Nat.cast_sub hk1]
    ring
  have hrad := support_radius_inequality k hk
  have hsqrt : 0 ≤ Real.sqrt (2 * (((k - 1 : ℕ) : ℝ))) :=
    Real.sqrt_nonneg _
  change
    -2 * Real.sqrt (((k - 1 : ℕ) : ℝ)) ≤ x ∧
      x ≤ 2 * Real.sqrt (((k - 1 : ℕ) : ℝ))
  change
    -1 - Real.sqrt (2 * (k : ℝ) - 2) ≤ x at hxlo
  change
    x ≤ -1 + Real.sqrt (2 * (k : ℝ) - 2) at hxhi
  rw [hcast] at hxlo hxhi
  constructor <;> linarith

/-- A direct induction form of the elementary estimate
`|sin (m θ)| ≤ m |sin θ|`. -/
theorem abs_sin_nat_mul_le (m : ℕ) (θ : ℝ) :
    |Real.sin ((m : ℝ) * θ)| ≤ (m : ℝ) * |Real.sin θ| := by
  induction m with
  | zero => simp
  | succ m ih =>
      rw [Nat.cast_succ, add_mul, one_mul, Real.sin_add]
      calc
        |Real.sin ((m : ℝ) * θ) * Real.cos θ +
            Real.cos ((m : ℝ) * θ) * Real.sin θ| ≤
            |Real.sin ((m : ℝ) * θ) * Real.cos θ| +
              |Real.cos ((m : ℝ) * θ) * Real.sin θ| := abs_add_le _ _
        _ =
            |Real.sin ((m : ℝ) * θ)| * |Real.cos θ| +
              |Real.cos ((m : ℝ) * θ)| * |Real.sin θ| := by
                simp only [abs_mul]
        _ ≤
            |Real.sin ((m : ℝ) * θ)| +
              |Real.sin θ| := by
                apply add_le_add
                · simpa using
                    mul_le_mul_of_nonneg_left
                      (Real.abs_cos_le_one θ)
                      (abs_nonneg (Real.sin ((m : ℝ) * θ)))
                · simpa using
                    mul_le_mul_of_nonneg_right
                      (Real.abs_cos_le_one ((m : ℝ) * θ))
                      (abs_nonneg (Real.sin θ))
        _ ≤ ((m : ℝ) + 1) * |Real.sin θ| := by
              nlinarith [abs_nonneg (Real.sin θ)]

/-- The sharp elementary uniform bound for Chebyshev polynomials of the
second kind on `[-1,1]`. -/
theorem abs_chebyshevU_eval_le (n : ℕ) {z : ℝ} (hz : |z| ≤ 1) :
    |(Polynomial.Chebyshev.U ℝ (n : ℤ)).eval z| ≤ (n : ℝ) + 1 := by
  have hzlo : -1 ≤ z := (abs_le.mp hz).1
  have hzhi : z ≤ 1 := (abs_le.mp hz).2
  by_cases hz1 : z = 1
  · subst z
    simp [Polynomial.Chebyshev.U_eval_one,
      abs_of_nonneg (show 0 ≤ (n : ℝ) + 1 by positivity)]
  by_cases hzm1 : z = -1
  · subst z
    simp [abs_mul,
      abs_of_nonneg (show 0 ≤ (n : ℝ) + 1 by positivity)]
  have hzlo' : -1 < z := lt_of_le_of_ne hzlo (Ne.symm hzm1)
  have hzhi' : z < 1 := lt_of_le_of_ne hzhi hz1
  have hprod : 0 < (z + 1) * (1 - z) :=
    mul_pos (by linarith) (by linarith)
  have hsinpos : 0 < Real.sin (Real.arccos z) := by
    rw [Real.sin_arccos]
    apply Real.sqrt_pos.2
    nlinarith
  have hU :=
    Polynomial.Chebyshev.U_real_cos
      (θ := Real.arccos z) (n := (n : ℤ))
  rw [Real.cos_arccos hzlo hzhi] at hU
  have hmul :
      |(Polynomial.Chebyshev.U ℝ (n : ℤ)).eval z| *
          |Real.sin (Real.arccos z)| ≤
        ((n : ℝ) + 1) * |Real.sin (Real.arccos z)| := by
    rw [← abs_mul, hU]
    simpa only [Int.cast_add, Int.cast_natCast, Int.cast_one,
      Nat.cast_add, Nat.cast_one] using
      abs_sin_nat_mul_le (n + 1) (Real.arccos z)
  exact le_of_mul_le_mul_right hmul (abs_pos.mpr hsinpos.ne')

/-- Evaluation form of the standard scaled Chebyshev representation of the
nonbacktracking polynomials.  The statement is valid from degree one; in
degree one the `U_{-1}` term vanishes. -/
theorem nbPoly_eval_scaled_chebyshev
    (k i : ℕ) (hk : 1 ≤ k) (hi : 1 ≤ i) (z : ℝ) :
    (nbPoly k i).eval
        (2 * Real.sqrt (((k - 1 : ℕ) : ℝ)) * z) =
      (Real.sqrt (((k - 1 : ℕ) : ℝ))) ^ i *
          (Polynomial.Chebyshev.U ℝ (i : ℤ)).eval z -
        (Real.sqrt (((k - 1 : ℕ) : ℝ))) ^ (i - 2) *
          (Polynomial.Chebyshev.U ℝ ((i : ℤ) - 2)).eval z := by
  let s : ℝ := Real.sqrt (((k - 1 : ℕ) : ℝ))
  change
    (nbPoly k i).eval (2 * s * z) =
      s ^ i * (Polynomial.Chebyshev.U ℝ (i : ℤ)).eval z -
        s ^ (i - 2) *
          (Polynomial.Chebyshev.U ℝ ((i : ℤ) - 2)).eval z
  have hr0 : 0 ≤ ((k - 1 : ℕ) : ℝ) := by positivity
  have hsquare : s ^ 2 = ((k - 1 : ℕ) : ℝ) := by
    exact Real.sq_sqrt hr0
  induction i using Nat.strong_induction_on with
  | h i ih =>
      rcases i with (_ | _ | i)
      · omega
      · simp [nbPoly, Polynomial.Chebyshev.U_one]
        ring
      · rcases i with (_ | i)
        · simp [nbPoly, Polynomial.Chebyshev.U_two]
          ring_nf
          rw [hsquare, Nat.cast_sub hk]
          ring
        · rw [nbPoly_add_three]
          simp only [eval_sub, eval_mul, eval_X, eval_C]
          rw [ih (i + 2) (by omega) (by omega),
            ih (i + 1) (by omega) (by omega)]
          rw [← hsquare]
          rcases i with (_ | i)
          · have hUthree :=
              congrArg (fun p : ℝ[X] => p.eval z)
                (Polynomial.Chebyshev.U_add_two ℝ (1 : ℤ))
            norm_num [Polynomial.Chebyshev.U_one,
              Polynomial.Chebyshev.U_two] at hUthree
            norm_num [Polynomial.Chebyshev.U_one,
              Polynomial.Chebyshev.U_two]
            rw [hUthree]
            ring
          · have hUhigh :=
              congrArg (fun p : ℝ[X] => p.eval z)
                (Polynomial.Chebyshev.U_add_two ℝ ((i + 2 : ℕ) : ℤ))
            have hUlow :=
              congrArg (fun p : ℝ[X] => p.eval z)
                (Polynomial.Chebyshev.U_add_two ℝ (i : ℤ))
            simp only [eval_sub, eval_mul, eval_ofNat, eval_X] at hUhigh hUlow
            push_cast at hUhigh hUlow ⊢
            simp only [pow_succ]
            linear_combination
              (norm := ring_nf)
              -s ^ (i + 4) * hUhigh + s ^ (i + 2) * hUlow

/-- The scaled Chebyshev representation plus the sharp `U` bound gives the
uniform pointwise estimate used in the tail certificate. -/
theorem abs_nbPoly_eval_le_scaled
    (k i : ℕ) (hk : 4 ≤ k) (hi : 2 ≤ i) {t : ℝ}
    (ht : t ∈ chebyshevInterval k) :
    |(nbPoly k i).eval t| ≤
      (Real.sqrt (((k - 1 : ℕ) : ℝ))) ^ i * ((i : ℝ) + 1) +
        (Real.sqrt (((k - 1 : ℕ) : ℝ))) ^ (i - 2) *
          (((i - 2 : ℕ) : ℝ) + 1) := by
  let s : ℝ := Real.sqrt (((k - 1 : ℕ) : ℝ))
  have hk1 : 1 ≤ k := by omega
  have hrNat : 3 ≤ k - 1 := by omega
  have hr : (0 : ℝ) < ((k - 1 : ℕ) : ℝ) := by
    exact_mod_cast (show 0 < k - 1 by omega)
  have hspos : 0 < s := by
    exact Real.sqrt_pos.2 hr
  have ht' : -2 * s ≤ t ∧ t ≤ 2 * s := ht
  have habst : |t| ≤ 2 * s := by
    apply (abs_le).2
    constructor <;> linarith [ht'.1, ht'.2]
  let z : ℝ := t / (2 * s)
  have hden : 0 < 2 * s := by positivity
  have hz : |z| ≤ 1 := by
    change |t / (2 * s)| ≤ 1
    rw [abs_div, abs_of_pos hden]
    exact (div_le_one hden).2 habst
  have hscale : 2 * s * z = t := by
    dsimp [z]
    field_simp
  have hrepr :=
    nbPoly_eval_scaled_chebyshev k i hk1 (by omega) z
  change
    (nbPoly k i).eval (2 * s * z) =
      s ^ i * (Polynomial.Chebyshev.U ℝ (i : ℤ)).eval z -
        s ^ (i - 2) *
          (Polynomial.Chebyshev.U ℝ ((i : ℤ) - 2)).eval z at hrepr
  rw [hscale] at hrepr
  have hUi := abs_chebyshevU_eval_le i hz
  have hUlow := abs_chebyshevU_eval_le (i - 2) hz
  have hindex : ((i - 2 : ℕ) : ℤ) = (i : ℤ) - 2 := by omega
  rw [hindex] at hUlow
  rw [hrepr]
  calc
    |s ^ i * (Polynomial.Chebyshev.U ℝ (i : ℤ)).eval z -
        s ^ (i - 2) *
          (Polynomial.Chebyshev.U ℝ ((i : ℤ) - 2)).eval z| ≤
        |s ^ i * (Polynomial.Chebyshev.U ℝ (i : ℤ)).eval z| +
          |s ^ (i - 2) *
            (Polynomial.Chebyshev.U ℝ ((i : ℤ) - 2)).eval z| := by
              simpa only [sub_eq_add_neg, abs_neg] using
                abs_add_le
                  (s ^ i * (Polynomial.Chebyshev.U ℝ (i : ℤ)).eval z)
                  (-(s ^ (i - 2) *
                    (Polynomial.Chebyshev.U ℝ ((i : ℤ) - 2)).eval z))
    _ =
        s ^ i * |(Polynomial.Chebyshev.U ℝ (i : ℤ)).eval z| +
          s ^ (i - 2) *
            |(Polynomial.Chebyshev.U ℝ ((i : ℤ) - 2)).eval z| := by
              rw [abs_mul, abs_mul, abs_of_nonneg (pow_nonneg hspos.le _),
                abs_of_nonneg (pow_nonneg hspos.le _)]
    _ ≤
        s ^ i * ((i : ℝ) + 1) +
          s ^ (i - 2) * (((i - 2 : ℕ) : ℝ) + 1) := by
            exact add_le_add
              (mul_le_mul_of_nonneg_left hUi (pow_nonneg hspos.le _))
              (mul_le_mul_of_nonneg_left hUlow (pow_nonneg hspos.le _))

/-- The previous estimate in the conventional `i-1` form. -/
theorem abs_nbPoly_eval_le
    (k i : ℕ) (hk : 4 ≤ k) (hi : 2 ≤ i) {t : ℝ}
    (ht : t ∈ chebyshevInterval k) :
    |(nbPoly k i).eval t| ≤
      (Real.sqrt (((k - 1 : ℕ) : ℝ))) ^ i * ((i : ℝ) + 1) +
        (Real.sqrt (((k - 1 : ℕ) : ℝ))) ^ (i - 2) * ((i : ℝ) - 1) := by
  have h := abs_nbPoly_eval_le_scaled k i hk hi ht
  convert h using 1
  rw [Nat.cast_sub hi]
  ring

/-- The elementary exponential-versus-linear inequality that closes the
all-degree tail.  It is stated for an abstract scale `s`; the application has
`s = sqrt (k-1)`. -/
theorem tail_power_dominates
    (s : ℝ) (hs : 0 ≤ s) (hsquare : 3 ≤ s ^ 2)
    (i : ℕ) (hi : 10 ≤ i) :
    2 * (i : ℝ) + 1 < 3 * s ^ (i - 6) := by
  have hspos : 0 < s := by
    nlinarith [sq_nonneg s]
  have hs_three_halves : (3 : ℝ) / 2 ≤ s := by
    apply (sq_le_sq₀ (by norm_num) hs).mp
    nlinarith
  induction i, hi using Nat.le_induction with
  | base =>
      norm_num
      have hsfour : (9 : ℝ) ≤ s ^ 4 := by
        nlinarith [sq_nonneg (s ^ 2 - 3)]
      nlinarith
  | succ i hi ih =>
      rw [show i + 1 - 6 = (i - 6) + 1 by omega, pow_succ]
      push_cast
      have hlinear :
          2 * ((i : ℝ) + 1) + 1 <
            s * (2 * (i : ℝ) + 1) := by
        have hmul :
            (3 / 2 : ℝ) * (2 * (i : ℝ) + 1) ≤
              s * (2 * (i : ℝ) + 1) :=
          mul_le_mul_of_nonneg_right hs_three_halves (by positivity)
        have hiR : (10 : ℝ) ≤ (i : ℝ) := by exact_mod_cast hi
        nlinarith
      calc
        2 * ((i : ℝ) + 1) + 1 <
            s * (2 * (i : ℝ) + 1) := hlinear
        _ < s * (3 * s ^ (i - 6)) :=
          mul_lt_mul_of_pos_left ih hspos
        _ = 3 * (s ^ (i - 6) * s) := by ring

/-- The denominator-free ratio estimate in the form used by the dual
certificate. -/
theorem tail_ratio_numerator_lt
    (k i : ℕ) (hk : 4 ≤ k) (hi : 10 ≤ i) :
    ((((k - 1 : ℕ) : ℝ)) ^ 2 +
          4 * (((k - 1 : ℕ) : ℝ)) + 6) *
        (((i : ℝ) + 1) * (((k - 1 : ℕ) : ℝ)) + (i : ℝ) - 1) <
      6 * (Real.sqrt (((k - 1 : ℕ) : ℝ))) ^ i := by
  let r : ℝ := ((k - 1 : ℕ) : ℝ)
  let s : ℝ := Real.sqrt r
  change
    (r ^ 2 + 4 * r + 6) *
        (((i : ℝ) + 1) * r + (i : ℝ) - 1) <
      6 * s ^ i
  have hrNat : 3 ≤ k - 1 := by omega
  have hr : (3 : ℝ) ≤ r := by
    change (3 : ℝ) ≤ ((k - 1 : ℕ) : ℝ)
    exact_mod_cast hrNat
  have hr0 : 0 ≤ r := by linarith
  have hs : 0 ≤ s := Real.sqrt_nonneg _
  have hsquare : s ^ 2 = r := Real.sq_sqrt hr0
  have hA : r ^ 2 + 4 * r + 6 ≤ 3 * r ^ 2 := by
    nlinarith [sq_nonneg (r - 3)]
  have hBnonneg :
      0 ≤ ((i : ℝ) + 1) * r + (i : ℝ) - 1 := by
    have hiR : (10 : ℝ) ≤ (i : ℝ) := by exact_mod_cast hi
    have hmul0 : 0 ≤ ((i : ℝ) + 1) * r :=
      mul_nonneg (by linarith) hr0
    linarith
  have hprod :
      0 ≤ ((i : ℝ) - 1) * (r - 3) := by
    have hiR : (10 : ℝ) ≤ (i : ℝ) := by exact_mod_cast hi
    exact mul_nonneg (by linarith) (by linarith)
  have hB :
      3 * (((i : ℝ) + 1) * r + (i : ℝ) - 1) ≤
        (4 * (i : ℝ) + 2) * r := by
    nlinarith
  have hfirst :
      (r ^ 2 + 4 * r + 6) *
          (((i : ℝ) + 1) * r + (i : ℝ) - 1) ≤
        3 * r ^ 2 *
          (((i : ℝ) + 1) * r + (i : ℝ) - 1) :=
    mul_le_mul_of_nonneg_right hA hBnonneg
  have hsecond :
      3 * r ^ 2 *
          (((i : ℝ) + 1) * r + (i : ℝ) - 1) ≤
        (4 * (i : ℝ) + 2) * r ^ 3 := by
    have :=
      mul_le_mul_of_nonneg_left hB (sq_nonneg r)
    nlinarith
  have htail :=
    tail_power_dominates s hs (by nlinarith [hsquare]) i hi
  have hmul :
      2 * (2 * (i : ℝ) + 1) * r ^ 3 <
        6 * r ^ 3 * s ^ (i - 6) := by
    have hr3pos : 0 < 2 * r ^ 3 := by positivity
    have := mul_lt_mul_of_pos_right htail hr3pos
    nlinarith
  have hpow :
      6 * r ^ 3 * s ^ (i - 6) = 6 * s ^ i := by
    rw [← hsquare]
    calc
      6 * (s ^ 2) ^ 3 * s ^ (i - 6) =
          6 * s ^ 6 * s ^ (i - 6) := by ring
      _ = 6 * (s ^ 6 * s ^ (i - 6)) := by ring
      _ = 6 * s ^ (6 + (i - 6)) := by rw [pow_add]
      _ = 6 * s ^ i := by
        congr 2
        omega
  calc
    (r ^ 2 + 4 * r + 6) *
        (((i : ℝ) + 1) * r + (i : ℝ) - 1) ≤
        3 * r ^ 2 *
          (((i : ℝ) + 1) * r + (i : ℝ) - 1) := hfirst
    _ ≤ (4 * (i : ℝ) + 2) * r ^ 3 := hsecond
    _ = 2 * (2 * (i : ℝ) + 1) * r ^ 3 := by ring
    _ < 6 * r ^ 3 * s ^ (i - 6) := hmul
    _ = 6 * s ^ i := hpow

/-- The total dual mass times the uniform pointwise bound is strictly
smaller than the principal nonbacktracking evaluation.  This is the
dual-independent numerical core of the all-degree tail argument. -/
theorem dual_mass_point_bound_lt_principal
    (k i : ℕ) (hk : 4 ≤ k) (hi : 10 ≤ i) :
    ((k : ℝ) * ((k : ℝ) ^ 2 + 2 * (k : ℝ) + 3) / 6) *
        ((Real.sqrt (((k - 1 : ℕ) : ℝ))) ^ i * ((i : ℝ) + 1) +
          (Real.sqrt (((k - 1 : ℕ) : ℝ))) ^ (i - 2) * ((i : ℝ) - 1)) <
      (k : ℝ) * (((k - 1 : ℕ) : ℝ) ^ (i - 1)) := by
  let r : ℝ := ((k - 1 : ℕ) : ℝ)
  let s : ℝ := Real.sqrt r
  change
    ((k : ℝ) * ((k : ℝ) ^ 2 + 2 * (k : ℝ) + 3) / 6) *
        (s ^ i * ((i : ℝ) + 1) + s ^ (i - 2) * ((i : ℝ) - 1)) <
      (k : ℝ) * r ^ (i - 1)
  have hk1 : 1 ≤ k := by omega
  have hk_cast : (k : ℝ) = r + 1 := by
    dsimp [r]
    rw [Nat.cast_sub hk1]
    ring
  have hrNat : 3 ≤ k - 1 := by omega
  have hr : (3 : ℝ) ≤ r := by
    change (3 : ℝ) ≤ ((k - 1 : ℕ) : ℝ)
    exact_mod_cast hrNat
  have hr0 : 0 ≤ r := by linarith
  have hs : 0 ≤ s := Real.sqrt_nonneg _
  have hspos : 0 < s := Real.sqrt_pos.2 (by linarith)
  have hsquare : s ^ 2 = r := Real.sq_sqrt hr0
  have hratio := tail_ratio_numerator_lt k i hk hi
  change
    (r ^ 2 + 4 * r + 6) *
        (((i : ℝ) + 1) * r + (i : ℝ) - 1) <
      6 * s ^ i at hratio
  have hbound :
      s ^ i * ((i : ℝ) + 1) + s ^ (i - 2) * ((i : ℝ) - 1) =
        s ^ (i - 2) *
          (((i : ℝ) + 1) * r + (i : ℝ) - 1) := by
    have hs_i : s ^ i = s ^ (i - 2) * s ^ 2 := by
      calc
        s ^ i = s ^ ((i - 2) + 2) := by
          congr 1
          omega
        _ = s ^ (i - 2) * s ^ 2 := by rw [pow_add]
    rw [hs_i, hsquare]
    ring
  have hpower :
      s ^ (i - 2) * s ^ i = r ^ (i - 1) := by
    calc
      s ^ (i - 2) * s ^ i = s ^ ((i - 2) + i) := by
        rw [pow_add]
      _ = s ^ (2 * (i - 1)) := by
        congr 1
        omega
      _ = (s ^ 2) ^ (i - 1) := by rw [pow_mul]
      _ = r ^ (i - 1) := by rw [hsquare]
  have hfactor :
      0 < (r + 1) * s ^ (i - 2) / 6 := by
    positivity
  rw [hk_cast, hbound]
  calc
    ((r + 1) * ((r + 1) ^ 2 + 2 * (r + 1) + 3) / 6) *
        (s ^ (i - 2) *
          (((i : ℝ) + 1) * r + (i : ℝ) - 1)) =
        ((r + 1) * s ^ (i - 2) / 6) *
          ((r ^ 2 + 4 * r + 6) *
            (((i : ℝ) + 1) * r + (i : ℝ) - 1)) := by ring
    _ <
        ((r + 1) * s ^ (i - 2) / 6) * (6 * s ^ i) :=
      mul_lt_mul_of_pos_left hratio hfactor
    _ = (r + 1) * r ^ (i - 1) := by
      rw [← hpower]
      ring

/-- Every tail dual slack is strictly positive.  The proof uses only the
positive three-point weights, their exact total mass, the uniform Chebyshev
bound, and the strict numerical comparison above. -/
theorem slack_pos_of_ten_le
    (k i : ℕ) (hk : 4 ≤ k) (hi : 10 ≤ i) :
    0 < slack k i := by
  let B : ℝ :=
    (Real.sqrt (((k - 1 : ℕ) : ℝ))) ^ i * ((i : ℝ) + 1) +
      (Real.sqrt (((k - 1 : ℕ) : ℝ))) ^ (i - 2) * ((i : ℝ) - 1)
  have hdelta : 1 ≤ delta k := by
    have hdelta0 : 0 ≤ delta k := Real.sqrt_nonneg _
    apply (sq_le_sq₀ (by norm_num) hdelta0).mp
    rw [delta_sq k hk]
    have hkR : (4 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
    nlinarith
  have hminus_wow : xiMinus k ∈ wowInterval k := by
    change
      -1 - delta k ≤ xiMinus k ∧
        xiMinus k ≤ -1 + delta k
    rw [xiMinus]
    constructor
    · rfl
    · linarith
  have hzero_wow : xiZero ∈ wowInterval k := by
    change -1 - delta k ≤ -2 ∧ -2 ≤ -1 + delta k
    constructor <;> linarith
  have hplus_wow : xiPlus k ∈ wowInterval k := by
    change
      -1 - delta k ≤ xiPlus k ∧
        xiPlus k ≤ -1 + delta k
    rw [xiPlus]
    constructor
    · linarith
    · rfl
  have hsubset := wowInterval_subset_chebyshevInterval k hk
  have hminus :
      |(nbPoly k i).eval (xiMinus k)| ≤ B := by
    exact abs_nbPoly_eval_le k i hk (by omega) (hsubset hminus_wow)
  have hzero :
      |(nbPoly k i).eval xiZero| ≤ B := by
    exact abs_nbPoly_eval_le k i hk (by omega) (hsubset hzero_wow)
  have hplus :
      |(nbPoly k i).eval (xiPlus k)| ≤ B := by
    exact abs_nbPoly_eval_le k i hk (by omega) (hsubset hplus_wow)
  have hwminus := weightMinus_pos k hk
  have hwzero := weightZero_pos k hk
  have hwplus := weightPlus_pos k hk
  have habs :
      |dual k (nbPoly k i)| ≤
        (weightMinus k + weightZero k + weightPlus k) * B := by
    rw [dual]
    calc
      |weightMinus k * (nbPoly k i).eval (xiMinus k) +
          weightZero k * (nbPoly k i).eval xiZero +
          weightPlus k * (nbPoly k i).eval (xiPlus k)| ≤
          |weightMinus k * (nbPoly k i).eval (xiMinus k) +
            weightZero k * (nbPoly k i).eval xiZero| +
            |weightPlus k * (nbPoly k i).eval (xiPlus k)| :=
        abs_add_le _ _
      _ ≤
          (|weightMinus k * (nbPoly k i).eval (xiMinus k)| +
            |weightZero k * (nbPoly k i).eval xiZero|) +
            |weightPlus k * (nbPoly k i).eval (xiPlus k)| := by
        have hadd :=
          abs_add_le
            (weightMinus k * (nbPoly k i).eval (xiMinus k))
            (weightZero k * (nbPoly k i).eval xiZero)
        linarith
      _ =
          weightMinus k * |(nbPoly k i).eval (xiMinus k)| +
            weightZero k * |(nbPoly k i).eval xiZero| +
              weightPlus k * |(nbPoly k i).eval (xiPlus k)| := by
        simp only [abs_mul, abs_of_pos hwminus, abs_of_pos hwzero,
          abs_of_pos hwplus]
      _ ≤
          weightMinus k * B + weightZero k * B + weightPlus k * B := by
        gcongr
      _ = (weightMinus k + weightZero k + weightPlus k) * B := by
        ring
  have hmass :
      weightMinus k + weightZero k + weightPlus k =
        (k : ℝ) * ((k : ℝ) ^ 2 + 2 * (k : ℝ) + 3) / 6 := by
    simpa [dual] using dual_mass k hk
  have hstrict :
      (weightMinus k + weightZero k + weightPlus k) * B <
        (k : ℝ) * (((k - 1 : ℕ) : ℝ) ^ (i - 1)) := by
    rw [hmass]
    exact dual_mass_point_bound_lt_principal k i hk hi
  have heval :
      (nbPoly k i).eval (k : ℝ) =
        (k : ℝ) * (((k - 1 : ℕ) : ℝ) ^ (i - 1)) :=
    nbPoly_eval_at_degree k i (by omega) (by omega)
  rw [slack, heval]
  have hdual_lower :
      -|dual k (nbPoly k i)| ≤ dual k (nbPoly k i) :=
    neg_abs_le _
  linarith

/-- Strict positivity of every dual slack in the admissible coefficient
range, combining the exact finite calculation with the Chebyshev tail. -/
theorem all_slacks_positive
    (k i : ℕ) (hk : 4 ≤ k) (hi : 5 ≤ i) :
    0 < slack k i := by
  by_cases hi9 : i ≤ 9
  · exact slack_pos_of_five_le_of_le_nine k i hk hi hi9
  · exact slack_pos_of_ten_le k i hk (by omega)

end

end Wow284.LP
