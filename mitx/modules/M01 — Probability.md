---
due: 2026-04-23
module: 1
problem_set: 1
status: in-progress
tags:
- module/m1
---
# M01 — Probability

**Source transcripts:** `Prob01_S01–S04` · `Prob02_S01–S03` · `Prob03_S01–S03` · `Prob04_S01–S02`\
**Prereq notes:** [[6.041-index]]\
**Flashcards:** `flashcards/m01-probability-notebooklm.md` (88 cards)\
**Trick questions:** [[M01 — Trick Questions]]

---

## Prereq checklist (MIT 6.041)

- [ ] L01 — [[6.041-L01-probability-models-and-axioms]]

- [ ] L02 — [[6.041-L02-conditioning-and-bayes]]

- [ ] L03 — [[6.041-L03-independence]]

- [ ] L04 — [[6.041-L04-counting]]

- [ ] L05 — [[6.041-L05-discrete-rv-I]]

- [ ] L06 — [[6.041-L06-discrete-rv-II]]

- [ ] L07 — [[6.041-L07-discrete-rv-III]]

- [ ] L08 — [[6.041-L08-continuous-rv]]

- [ ] L09 — [[6.041-L09-multiple-continuous-rv]]

- [ ] L10 — [[6.041-L10-bayes-derived-distributions]]

- [ ] L11 — [[6.041-L11-covariance-convolution]]

- [ ] L12 — [[6.041-L12-iterated-expectations]]

- [ ] L13 — [[6.041-L13-bernoulli-process]]

- [ ] L19 — [[6.041-L19-weak-law-of-large-numbers]]

- [ ] L20 — [[6.041-L20-central-limit-theorem]]

---

## 1. Random Variables

> *Prob01_S01*

A **random variable** is a deterministic function mapping outcomes in sample space Ω → ℝ, so we can do math on abstract events.

- Randomness lives in the experiment, not the mapping
- The mapping is **arbitrary**: heads/tails → {1,−1} or {12,−3} — both valid
- Functions of RVs are also RVs: if X ∈ {+1,−1} with equal prob, then P(X²=1) = **1** (not 0.5)

**Finance link:** Gains/losses on an investment are a binary RV. The number choice doesn't change the probability structure.

---

## 2. Probability Distributions

> *Prob01_S01–S02 · Prob02_S01–S03*

### Requirements

1. **Non-negativity:** p(x) ≥ 0
2. **Normalisation:** Σ p(x) = 1 (discrete) or ∫ p(x) dx = 1 (continuous)

### Continuous — key subtleties

- P(X = exact value) = 0 always (measure zero) — this does **not** mean impossible
- PDF value p(x) **can exceed 1** — it is density (prob per unit length), not probability
- Always ask for P(a ≤ X ≤ b) = ∫ₐᵇ p(x) dx

### CDF

F(x) = P(X ≤ x). Always 0 → 1, never decreasing.\
P(a ≤ X ≤ b) = F(b) − F(a)\
p(x) = F'(x) — differentiate to recover PDF

### Change of variables

If Y = y(X): **g(y) = p(x) / |dy/dx|**\
Absolute value handles decreasing functions. Density rescales to conserve total probability.

### Key distributions

| Distribution | PMF/PDF | Mean | Variance | Finance use |
| --- | --- | --- | --- | --- |
| Uniform \[0,1\] | p(x)=1 | 1/2 | 1/12 | Baseline |
| Binomial(n,p) | C(n,k)pᵏqⁿ⁻ᵏ | np | npq | Binomial option tree |
| Poisson(λ) | e^(−λ)λᵏ/k! | λ | λ | Defaults, jumps, order flow |
| Normal N(μ,σ²) | (2πσ²)^(−½)exp(−(x−μ)²/2σ²) | μ | σ² | Returns, Black-Scholes |
| Log-normal | X=ln Y, X∼Normal | — | — | Asset prices |
| Fat-tailed | p(x)∝c/(c²+x²) \~ 1/x² | ∞ | ∞ | Empirical stock returns |

**Poisson as Binomial limit:** n→∞, p→0, holding λ=np fixed → Binomial → Poisson. Useful when n large and p small (e.g. birthday problem with n=65 students, λ=0.178).

**Log-normal:** eʳ − 1 = R links log-returns r to simple returns R. If log-returns are normal → prices are log-normal.

**Gaussian normalisation:** ∫e^(−ax²)dx = √(π/a). Setting a=1/(2σ²) confirms normalisation constant 1/√(2πσ²).

**Fat tails warning:** p(x)∝c/(c²+x²) looks like a bell curve at low resolution but falls as 1/x². The variance integral diverges. With more data, estimated volatility **diverges** rather than converges — the Law of Large Numbers does not rescue you.

---

## 3. Expectations and Moments

> *Prob01_S03*

### The expectation operator

**Discrete:** E\[f(X)\] = Σ f(xₖ) p(xₖ)\
**Continuous:** E\[f(X)\] = ∫ f(x) p(x) dx

**Linearity (always holds — no independence needed):**

- E\[cf\] = c·E\[f\]
- E\[f + g\] = E\[f\] + E\[g\]

**Non-linearity warning:** E\[g(X)\] ≠ g(E\[X\]) unless g is linear. This is the source of many finance errors (Jensen's inequality).

### Moments

| Moment | Formula | Interpretation |
| --- | --- | --- |
| Mean | μ = E\[X\] | Centre |
| Variance | σ² = E\[(X−μ)²\] = E\[X²\] − μ² | Spread |
| Skewness | s = E\[(X−μ)³\]/σ³ | Asymmetry (0 for symmetric) |
| Kurtosis | κ = E\[(X−μ)⁴\]/σ⁴ − 3 | Tail fatness (0 for Gaussian) |

**Variance shortcut derivation:**\
E\[(X−μ)²\] = E\[X²−2μX+μ²\] = E\[X²\] − 2μ·E\[X\] + μ² = **E\[X²\] − μ²**

**Finance:** σ lives in the same units as X. Return σ=30%/yr is natural; variance of 0.09%²/yr is not.

**Moments may not exist:** Fat-tailed distributions have valid probability laws but divergent moments. You cannot assume finite variance just because a distribution exists.

### Covariance and Correlation

Cov(X,Y) = E\[(X−μₓ)(Y−μᵧ)\] = E\[XY\] − E\[X\]E\[Y\]\
ρ = Cov(X,Y)/(σₓσᵧ) ∈ \[−1,+1\]

**Zero covariance ≠ independence (critical):**\
Let X take ±a, ±b with equal prob (E\[X\]=0). Let Y=X². Y is 100% determined by X. But:\
Cov(X,Y) = E\[X³\] − 0 = 0 (X symmetric → odd moments vanish)\
→ **Covariance only detects linear relationships.**\
Independence → zero covariance. Zero covariance ↛ independence.

---

## 4. Sums of RVs and Portfolio Theory

> *Prob03_S01–S03*

### Linearity of expectations (always)

E\[Σ Xᵢ\] = Σ E\[Xᵢ\] — no independence required, holds even under full dependence

Full distribution of the sum requires n-fold convolution integrals — hard. Moments are always easy.

### Portfolio formulas

**Return:** Rₚ = Σ wᵢRᵢ\
**Expected return:** E\[Rₚ\] = Σ wᵢμᵢ

**Variance (full):**\
Var(Rₚ) = Σᵢ wᵢ²σᵢ² + 2Σᵢ&lt;ⱼ wᵢwⱼσᵢσⱼρᵢⱼ

**Derivation:** Expand E\[(Σwᵢ(Rᵢ−μᵢ))²\]. Diagonal = Σwᵢ²σᵢ². Cross terms = 2ΣwᵢwⱼCov(Rᵢ,Rⱼ).

| Condition | Portfolio variance |
| --- | --- |
| ρᵢⱼ=0 | Σwᵢ²σᵢ² |
| ρᵢⱼ=1 | (Σwᵢσᵢ)² — no diversification at all |
| Equal weight, equal σ₀, ρ=0 | σ₀²/n → volatility = σ₀/√n |

**Diversification:** Volatility ∝ 1/√n for uncorrelated equal-weighted assets. Correlation limits this benefit. At ρ=1, zero benefit regardless of n.

### Binomial mean/variance — elegant method

Let Xᵢ = 1{trial i succeeds}. S = Σ Xᵢ.

- E\[Xᵢ\]=p, E\[Xᵢ²\]=p, E\[XᵢXⱼ\]=p² (independent)
- E\[S\] = np ✓
- Var(S) = E\[S²\] − (np)² = np + n(n−1)p² − n²p² = **npq** ✓

No factorials. No combinatorics. Just linearity and independence.

---

## 5. CLT and Characteristic Functions

> *Prob03_S03 · Prob04_S01–S02*

### Law of Large Numbers

As n→∞, empirical average converges in probability to true mean. Distribution narrows around μ.

### Central Limit Theorem

Standardise: zₖ = (k − np)/√(npq)\
As n→∞, the **CDF** of the standardised sum → standard normal CDF, regardless of original distribution (provided moments exist).

**R demo:** Sum of 6 uniform RVs looks Gaussian. With n=1000, binomial around np=100 looks Gaussian.

**Finance:** Adding many independent economic shocks → Gaussian. Bloomberg terminal example: 120 students, p=7.5%, approximate binomial with Normal.

### CLT caveats — when it fails

| Caveat | Reason |
| --- | --- |
| Fat-tailed distributions | Moments don't exist → scaling argument breaks |
| p changes as n grows | Binomial(n, λ/n) → Poisson, not Gaussian |
| CLT is about CDFs not PMFs | PMF may still look bumpy |
| Tail convergence is slow | Centre converges fast, tails lag |

### Characteristic functions

φ(t) = E\[e^(itX)\] = ∫ e^(itx) p(x) dx (Fourier transform of PDF)

**Why useful:** Convolution in prob space → **multiplication** in Fourier space → **addition** of log CFs (cumulants)

| CF | Formula |
| --- | --- |
| Binomial | (pe^(it) + q)ⁿ |
| Gaussian | exp(−t²σ²/2 + iμt) — note σ² is in **numerator** |

**Gaussian closed under addition:** Product of N Gaussian CFs = exp(−t²Σσᵢ²/2 + iΣμᵢt) = Gaussian with σ̂²=Σσᵢ², μ̂=Σμᵢ. Exact for **any** finite N, not just large N.

### Cumulant expansion and CLT proof

ln φ(t) = Σ Cₙ(it)ⁿ/n!

| Cumulant | Value | Gaussian |
| --- | --- | --- |
| C₁ | E\[X\] | μ |
| C₂ | Var(X) | σ² |
| C₃ | E\[(X−μ)³\] | 0 |
| C₄ | E\[(X−μ)⁴\] − 3σ⁴ | 0 |

**CLT proof:** For N IID variables, the n-th cumulant scales as N·Cₙ. Normalised by aggregate σ (∝√N), dimensionless cumulant for n&gt;2 scales as 1/N^(n/2−1) → 0. All higher cumulants vanish → Gaussian.

---

## 6. R Practice

Work in `r/m1/`. Before PS1:

- [ ] Sample from Normal, Log-normal; plot with ggplot2

- [ ] Empirical vs theoretical mean/variance

- [ ] CLT demo: averages of Uniform(0,1) → Normal (vary n)

- [ ] Simulate correlated normals (Cholesky); compute Cov/Corr empirically

- [ ] Monte Carlo: P(|X|&gt;k) for fat-tailed vs Gaussian

---

## 7. PS1 Plan

- [ ] Day 1 (Apr 20 — today): transcripts Prob01–02, distributions, moments

- [ ] Day 2 (Apr 21): Prob03–04, CLT, characteristic functions, R demos

- [ ] Day 3 (Apr 22): start and complete PS1

- [ ] Apr 23 07:39 GMT+1: hard deadline

---

## 8. Debrief (fill after PS1)

- What was hardest:
- What R skill was missing:
- Flashcards that failed recall:
- Confidence 1–5: