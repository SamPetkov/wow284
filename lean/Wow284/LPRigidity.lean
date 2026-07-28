import Wow284.LPWeakDuality

namespace Wow284.LP

noncomputable section

open scoped Topology

open Polynomial
open Filter

/-- The three support points of the exact dual certificate are strictly
ordered.  In particular, the middle point `-2` lies in the interior of the
WOW interval. -/
theorem xiMinus_lt_xiZero_lt_xiPlus (k : ℕ) (hk : 4 ≤ k) :
    xiMinus k < xiZero ∧ xiZero < xiPlus k := by
  have hkR : (4 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hdelta_nonneg : 0 ≤ delta k := Real.sqrt_nonneg _
  have hdelta_sq : delta k ^ 2 = 2 * (k : ℝ) - 2 := delta_sq k hk
  have hdelta_one : 1 < delta k := by nlinarith
  constructor <;> simp [xiMinus, xiZero, xiPlus] <;> linarith

/-- Vanishing of the three-point dual functional, together with
nonpositivity at its support and positivity of its weights, forces
pointwise vanishing at every support point. -/
theorem support_roots_of_dual_eq_zero
    (k : ℕ) (hk : 4 ≤ k) (p : ℝ[X])
    (hminus : p.eval (xiMinus k) ≤ 0)
    (hzero : p.eval xiZero ≤ 0)
    (hplus : p.eval (xiPlus k) ≤ 0)
    (hdual : dual k p = 0) :
    p.eval (xiMinus k) = 0 ∧
      p.eval xiZero = 0 ∧
        p.eval (xiPlus k) = 0 := by
  have hwminus := weightMinus_pos k hk
  have hwzero := weightZero_pos k hk
  have hwplus := weightPlus_pos k hk
  have htminus :
      weightMinus k * p.eval (xiMinus k) ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos hwminus.le hminus
  have htzero :
      weightZero k * p.eval xiZero ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos hwzero.le hzero
  have htplus :
      weightPlus k * p.eval (xiPlus k) ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos hwplus.le hplus
  have hsum :
      weightMinus k * p.eval (xiMinus k) +
          weightZero k * p.eval xiZero +
            weightPlus k * p.eval (xiPlus k) = 0 := by
    simpa [dual] using hdual
  have hzminus :
      weightMinus k * p.eval (xiMinus k) = 0 := by
    linarith
  have hzzero :
      weightZero k * p.eval xiZero = 0 := by
    linarith
  have hzplus :
      weightPlus k * p.eval (xiPlus k) = 0 := by
    linarith
  constructor
  · exact (mul_eq_zero.mp hzminus).resolve_left (ne_of_gt hwminus)
  constructor
  · exact (mul_eq_zero.mp hzzero).resolve_left (ne_of_gt hwzero)
  · exact (mul_eq_zero.mp hzplus).resolve_left (ne_of_gt hwplus)

/-- A polynomial which is nonpositive on the WOW interval and vanishes at
its interior support point has zero derivative there. -/
theorem derivative_eval_xiZero_eq_zero_of_nonpos
    (k : ℕ) (hk : 4 ≤ k) (p : ℝ[X])
    (hp : ∀ x ∈ wowInterval k, p.eval x ≤ 0)
    (hzero : p.eval xiZero = 0) :
    p.derivative.eval xiZero = 0 := by
  have horder := xiMinus_lt_xiZero_lt_xiPlus k hk
  have hnhds : wowInterval k ∈ 𝓝 xiZero := by
    simpa [wowInterval, xiMinus, xiPlus, delta] using
      (Icc_mem_nhds horder.1 horder.2)
  have hmaxOn : IsMaxOn (fun x : ℝ => p.eval x) (wowInterval k) xiZero := by
    intro x hx
    change p.eval x ≤ p.eval xiZero
    rw [hzero]
    exact hp x hx
  have hlocal : IsLocalMax (fun x : ℝ => p.eval x) xiZero :=
    hmaxOn.localize.isLocalMax hnhds
  exact hlocal.hasDerivAt_eq_zero (p.hasDerivAt xiZero)

/-- The monic quartic with the three dual support roots, with the middle
root repeated. -/
def rootQuartic (k : ℕ) : ℝ[X] :=
  (X - C (xiMinus k)) * (X - C xiZero) ^ 2 * (X - C (xiPlus k))

theorem rootQuartic_monic (k : ℕ) : (rootQuartic k).Monic := by
  exact
    ((monic_X_sub_C (xiMinus k)).mul
      ((monic_X_sub_C xiZero).pow 2)).mul
        (monic_X_sub_C (xiPlus k))

theorem rootQuartic_natDegree (k : ℕ) :
    (rootQuartic k).natDegree = 4 := by
  have hm := monic_X_sub_C (xiMinus k)
  have hz := monic_X_sub_C xiZero
  have hp := monic_X_sub_C (xiPlus k)
  rw [rootQuartic, (hm.mul (hz.pow 2)).natDegree_mul hp,
    hm.natDegree_mul (hz.pow 2), hz.natDegree_pow]
  simp

/-- The root-factor quartic is exactly the scaled explicit optimizer. -/
theorem rootQuartic_eq_scaled_extremal (k : ℕ) (hk : 4 ≤ k) :
    rootQuartic k =
      C (6 * ((k : ℝ) + 2)) * extremal k := by
  have hdelta_sq : delta k ^ 2 = 2 * (k : ℝ) - 2 := delta_sq k hk
  have hden : 6 * ((k : ℝ) + 2) ≠ 0 := by positivity
  apply Polynomial.funext
  intro x
  simp [rootQuartic, extremal, xiMinus, xiZero, xiPlus]
  field_simp [hden]
  nlinarith

/-- Four roots counted with multiplicity and a quartic degree bound identify
the polynomial up to its leading coefficient. -/
theorem eq_leadingCoeff_mul_rootQuartic
    (k : ℕ) (hk : 4 ≤ k) (p : ℝ[X])
    (hdeg : p.natDegree ≤ 4)
    (hminus : p.eval (xiMinus k) = 0)
    (hzero : p.eval xiZero = 0)
    (hplus : p.eval (xiPlus k) = 0)
    (hderiv : p.derivative.eval xiZero = 0) :
    p = C p.leadingCoeff * rootQuartic k := by
  by_cases hpzero : p = 0
  · simp [hpzero]
  · have horder := xiMinus_lt_xiZero_lt_xiPlus k hk
    have hdvdMinus : X - C (xiMinus k) ∣ p :=
      (dvd_iff_isRoot).2 hminus
    have hdvdPlus : X - C (xiPlus k) ∣ p :=
      (dvd_iff_isRoot).2 hplus
    have hmult :
        1 < p.rootMultiplicity xiZero :=
      (one_lt_rootMultiplicity_iff_isRoot hpzero).2 ⟨hzero, hderiv⟩
    have hdvdZero : (X - C xiZero) ^ 2 ∣ p :=
      (le_rootMultiplicity_iff hpzero).1 (by omega)
    have hcopMinusZero :
        IsCoprime (X - C (xiMinus k)) (X - C xiZero) :=
      isCoprime_X_sub_C_of_isUnit_sub
        (sub_ne_zero_of_ne (ne_of_lt horder.1)).isUnit
    have hcopMinusPlus :
        IsCoprime (X - C (xiMinus k)) (X - C (xiPlus k)) :=
      isCoprime_X_sub_C_of_isUnit_sub
        (sub_ne_zero_of_ne (ne_of_lt (horder.1.trans horder.2))).isUnit
    have hcopZeroPlus :
        IsCoprime (X - C xiZero) (X - C (xiPlus k)) :=
      isCoprime_X_sub_C_of_isUnit_sub
        (sub_ne_zero_of_ne (ne_of_lt horder.2)).isUnit
    have hdvdMinusZero :
        (X - C (xiMinus k)) * (X - C xiZero) ^ 2 ∣ p :=
      hcopMinusZero.pow_right.mul_dvd hdvdMinus hdvdZero
    have hcopProductPlus :
        IsCoprime
          ((X - C (xiMinus k)) * (X - C xiZero) ^ 2)
          (X - C (xiPlus k)) :=
      hcopMinusPlus.mul_left hcopZeroPlus.pow_left
    have hdvd : rootQuartic k ∣ p := by
      exact hcopProductPlus.mul_dvd hdvdMinusZero hdvdPlus
    apply eq_leadingCoeff_mul_of_monic_of_dvd_of_natDegree_le
      (rootQuartic_monic k) hdvd
    simpa [rootQuartic_natDegree k] using hdeg

/-- The nonbacktracking polynomial in degree `i` has degree at most `i`. -/
theorem nbPoly_natDegree_le (k i : ℕ) :
    (nbPoly k i).natDegree ≤ i := by
  induction i using Nat.strong_induction_on with
  | h i ih =>
      rcases i with (_ | _ | _ | n)
      · simp [nbPoly]
      · simp [nbPoly]
      · apply (natDegree_sub_le _ _).trans
        simp
      · rw [nbPoly_add_three]
        apply (natDegree_sub_le _ _).trans
        apply max_le
        · calc
            (X * nbPoly k (n + 2)).natDegree
                ≤ X.natDegree + (nbPoly k (n + 2)).natDegree :=
              natDegree_mul_le
            _ ≤ 1 + (n + 2) := by
              exact Nat.add_le_add (by simp) (ih (n + 2) (by omega))
            _ = n + 3 := by omega
        · calc
            (C (((k - 1 : ℕ) : ℝ)) * nbPoly k (n + 1)).natDegree
                ≤ (nbPoly k (n + 1)).natDegree :=
              natDegree_C_mul_le _ _
            _ ≤ n + 1 := ih (n + 1) (by omega)
            _ ≤ n + 3 := by omega

/-- If every coefficient in nonbacktracking degree at least five vanishes,
then the represented polynomial has degree at most four. -/
theorem polynomial_natDegree_le_four_of_high_coeff_zero
    (k : ℕ) (c : Coefficients)
    (hhigh : ∀ i, 5 ≤ i → c i = 0) :
    (polynomial k c).natDegree ≤ 4 := by
  classical
  rw [polynomial]
  apply natDegree_sum_le_of_forall_le
  intro i hi
  have hci : c i ≠ 0 := Finsupp.mem_support_iff.mp hi
  have hi4 : i ≤ 4 := by
    by_contra hnot
    have hi5 : 5 ≤ i := by omega
    exact hci (hhigh i hi5)
  exact (natDegree_C_mul_le _ _).trans
    ((nbPoly_natDegree_le k i).trans hi4)

/-- Equality in the nonnegative slack sum forces every coefficient in
degree at least five to vanish. -/
theorem high_coeff_eq_zero_of_slack_sum_eq
    (k : ℕ) (c : Coefficients)
    (hc0 : 0 < c 0)
    (hcoeff : ∀ i, 5 ≤ i → 0 ≤ c i)
    (hmass : slack k 0 = ceiling k)
    (hmoment : ∀ i, 1 ≤ i → i ≤ 4 → slack k i = 0)
    (hslack : ∀ i, 5 ≤ i → 0 < slack k i)
    (hsum :
      c.sum (fun i a => a * slack k i) = ceiling k * c 0) :
    ∀ i, 5 ≤ i → c i = 0 := by
  classical
  intro i hi5
  by_contra hci
  have hzero_mem : 0 ∈ c.support := by
    simpa [Finsupp.mem_support_iff] using ne_of_gt hc0
  have hi_mem : i ∈ c.support := by
    simpa [Finsupp.mem_support_iff] using hci
  have hi0 : i ≠ 0 := by omega
  have hcomparison :
      (∑ j ∈ c.support,
          if j = 0 then c j * slack k j
          else if j = i then c j * slack k j
          else 0) ≤
        ∑ j ∈ c.support, c j * slack k j := by
    apply Finset.sum_le_sum
    intro j hj
    by_cases hj0 : j = 0
    · simp [hj0]
    by_cases hji : j = i
    · simp [hji]
    simp only [hj0, hji, ↓reduceIte]
    by_cases hj4 : j ≤ 4
    · have hj1 : 1 ≤ j := Nat.one_le_iff_ne_zero.mpr hj0
      rw [hmoment j hj1 hj4]
      simp
    · have hj5 : 5 ≤ j := by omega
      exact mul_nonneg (hcoeff j hj5) (le_of_lt (hslack j hj5))
  have hleft :
      (∑ j ∈ c.support,
          if j = 0 then c j * slack k j
          else if j = i then c j * slack k j
          else 0) =
        ceiling k * c 0 + c i * slack k i := by
    calc
      (∑ j ∈ c.support,
          if j = 0 then c j * slack k j
          else if j = i then c j * slack k j
          else 0) =
          (∑ j ∈ c.support,
            if j = 0 then c j * slack k j else 0) +
            ∑ j ∈ c.support,
              if j = i then c j * slack k j else 0 := by
                rw [← Finset.sum_add_distrib]
                apply Finset.sum_congr rfl
                intro j hj
                by_cases hj0 : j = 0
                · subst j
                  simp [Ne.symm hi0]
                · simp [hj0]
      _ = ceiling k * c 0 + c i * slack k i := by
            rw [Finset.sum_ite_eq', if_pos hzero_mem,
              Finset.sum_ite_eq', if_pos hi_mem]
            rw [hmass]
            ring
  rw [hleft] at hcomparison
  change
    ceiling k * c 0 + c i * slack k i ≤
      c.sum (fun j a => a * slack k j) at hcomparison
  rw [hsum] at hcomparison
  have hci_nonneg := hcoeff i hi5
  have hslack_pos := hslack i hi5
  have hci_pos : 0 < c i :=
    lt_of_le_of_ne hci_nonneg (Ne.symm hci)
  have hproduct_pos : 0 < c i * slack k i :=
    mul_pos hci_pos hslack_pos
  linarith

/-- Rigidity after the two equality quantities furnished by weak duality
have been identified: equality of the slack sum and vanishing of the dual
functional.  This theorem contains the complete complementary-slackness,
interior-double-root, and quartic-factorization argument. -/
theorem polynomial_eq_extremal_of_certificate_equalities
    (k : ℕ) (hk : 4 ≤ k) (c : Coefficients)
    (hc : Admissible k c)
    (hmass : slack k 0 = ceiling k)
    (hmoment : ∀ i, 1 ≤ i → i ≤ 4 → slack k i = 0)
    (hslack : ∀ i, 5 ≤ i → 0 < slack k i)
    (hsum :
      c.sum (fun i a => a * slack k i) = ceiling k * c 0)
    (hdual : dual k (polynomial k c) = 0)
    (hobjective :
      (polynomial k c).eval (k : ℝ) = ceiling k * c 0) :
    polynomial k c = C (c 0) * extremal k := by
  have hhigh :=
    high_coeff_eq_zero_of_slack_sum_eq k c hc.1 hc.2.1
      hmass hmoment hslack hsum
  have hdeg :=
    polynomial_natDegree_le_four_of_high_coeff_zero k c hhigh
  have horder := xiMinus_lt_xiZero_lt_xiPlus k hk
  have hminus_mem : xiMinus k ∈ wowInterval k := by
    simpa [wowInterval, xiMinus, xiPlus, delta] using
      (show xiMinus k ∈ Set.Icc (xiMinus k) (xiPlus k) from
        ⟨le_rfl, horder.1.le.trans horder.2.le⟩)
  have hzero_mem : xiZero ∈ wowInterval k := by
    simpa [wowInterval, xiMinus, xiPlus, delta] using
      (show xiZero ∈ Set.Icc (xiMinus k) (xiPlus k) from
        ⟨horder.1.le, horder.2.le⟩)
  have hplus_mem : xiPlus k ∈ wowInterval k := by
    simpa [wowInterval, xiMinus, xiPlus, delta] using
      (show xiPlus k ∈ Set.Icc (xiMinus k) (xiPlus k) from
        ⟨horder.1.le.trans horder.2.le, le_rfl⟩)
  obtain ⟨hminus, hzero, hplus⟩ :=
    support_roots_of_dual_eq_zero k hk (polynomial k c)
      (hc.2.2 _ hminus_mem) (hc.2.2 _ hzero_mem)
      (hc.2.2 _ hplus_mem) hdual
  have hderiv :=
    derivative_eval_xiZero_eq_zero_of_nonpos
      k hk (polynomial k c) hc.2.2 hzero
  have hfactor :=
    eq_leadingCoeff_mul_rootQuartic
      k hk (polynomial k c) hdeg hminus hzero hplus hderiv
  let scale : ℝ :=
    (polynomial k c).leadingCoeff * (6 * ((k : ℝ) + 2))
  have hscalar :
      polynomial k c = C scale * extremal k := by
    rw [hfactor, rootQuartic_eq_scaled_extremal k hk]
    simp [scale, mul_assoc]
  have heval :
      (polynomial k c).eval (k : ℝ) = scale * ceiling k := by
    rw [hscalar]
    simp [extremal_eval_at_degree]
  have hceiling : 0 < ceiling k := by
    have hkR : (4 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
    have hkp2 : 0 < (k : ℝ) + 2 := by linarith
    have hkquad : 0 < (k : ℝ) ^ 2 + 3 := by positivity
    exact div_pos (mul_pos hkp2 hkquad) (by norm_num)
  have hscale : scale = c 0 := by
    rw [heval] at hobjective
    nlinarith
  simpa [hscale] using hscalar

/-- Equality in the sharp objective bound forces the unique normalized
quartic optimizer.  All certificate hypotheses are discharged by the exact
finite and all-degree tail theorems. -/
theorem polynomial_eq_extremal_of_objective_eq
    (k : ℕ) (hk : 4 ≤ k) (c : Coefficients)
    (hc : Admissible k c)
    (hobjective :
      (polynomial k c).eval (k : ℝ) = ceiling k * c 0) :
    polynomial k c = C (c 0) * extremal k := by
  have hsum_lower :=
    ceiling_mul_le_slack_sum k hk c hc
  have hdual_nonpos :=
    dual_polynomial_nonpos k hk c hc
  have hidentity :=
    dual_add_eval_eq_slack_sum k c
  have hsum_upper :
      c.sum (fun i a => a * slack k i) ≤ ceiling k * c 0 := by
    rw [← hidentity, hobjective]
    linarith
  have hsum :
      c.sum (fun i a => a * slack k i) = ceiling k * c 0 :=
    le_antisymm hsum_upper hsum_lower
  have hdual : dual k (polynomial k c) = 0 := by
    rw [hobjective, hsum] at hidentity
    linarith
  exact
    polynomial_eq_extremal_of_certificate_equalities
      k hk c hc
      (slack_zero_eq_ceiling k hk)
      (slack_eq_zero_of_one_le_of_le_four k · hk)
      (all_slacks_positive k · hk)
      hsum hdual hobjective

/-- The explicit normalized optimizer attains equality in the objective. -/
theorem objective_eq_of_polynomial_eq_extremal
    (k : ℕ) (c : Coefficients)
    (hpoly : polynomial k c = C (c 0) * extremal k) :
    (polynomial k c).eval (k : ℝ) = ceiling k * c 0 := by
  rw [hpoly]
  simp [extremal_eval_at_degree, mul_comm]

/-- Equality in the sharp bound is equivalent to being the explicit
normalized extremal polynomial. -/
theorem twoSidedLP_equality_iff
    (k : ℕ) (hk : 4 ≤ k) (c : Coefficients)
    (hc : Admissible k c) :
    ((polynomial k c).eval (k : ℝ) = ceiling k * c 0 ↔
      polynomial k c = Polynomial.C (c 0) * extremal k) := by
  constructor
  · exact polynomial_eq_extremal_of_objective_eq k hk c hc
  · exact objective_eq_of_polynomial_eq_extremal k c

/-- Equality in the sharp objective determines the complete finitely
supported coefficient family, not only the represented polynomial. -/
theorem coefficients_eq_smul_extremalCoefficients_of_objective_eq
    (k : ℕ) (hk : 4 ≤ k) (c : Coefficients)
    (hc : Admissible k c)
    (hobjective :
      (polynomial k c).eval (k : ℝ) = ceiling k * c 0) :
    c = c 0 • extremalCoefficients k := by
  apply polynomial_injective k
  rw [polynomial_smul,
    polynomial_extremalCoefficients k (by omega)]
  exact polynomial_eq_extremal_of_objective_eq k hk c hc hobjective

/-- The coefficient-level form of equality rigidity. -/
theorem twoSidedLP_coefficient_equality_iff
    (k : ℕ) (hk : 4 ≤ k) (c : Coefficients)
    (hc : Admissible k c) :
    ((polynomial k c).eval (k : ℝ) = ceiling k * c 0 ↔
      c = c 0 • extremalCoefficients k) := by
  constructor
  · exact
      coefficients_eq_smul_extremalCoefficients_of_objective_eq
        k hk c hc
  · intro hcoeff
    apply objective_eq_of_polynomial_eq_extremal
    calc
      polynomial k c =
          polynomial k (c 0 • extremalCoefficients k) :=
        congrArg (polynomial k) hcoeff
      _ = C (c 0) * extremal k := by
        rw [polynomial_smul,
          polynomial_extremalCoefficients k (by omega)]

/-- Manuscript-shaped rigidity: every equality case is a positive scalar
multiple of the unique normalized finite coefficient family. -/
theorem twoSidedLP_positive_ray_equality_iff
    (k : ℕ) (hk : 4 ≤ k) (c : Coefficients)
    (hc : Admissible k c) :
    ((polynomial k c).eval (k : ℝ) = ceiling k * c 0 ↔
      ∃ a : ℝ, 0 < a ∧ c = a • extremalCoefficients k) := by
  constructor
  · intro hobjective
    exact
      ⟨c 0, hc.1,
        coefficients_eq_smul_extremalCoefficients_of_objective_eq
          k hk c hc hobjective⟩
  · rintro ⟨a, ha, rfl⟩
    rw [polynomial_smul,
      polynomial_extremalCoefficients k (by omega)]
    simp [extremal_eval_at_degree, mul_comm]

end

end Wow284.LP
