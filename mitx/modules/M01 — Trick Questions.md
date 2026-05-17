---
tags: [module/m1, trick-questions]
module: 1
---

# M01 — Trick Questions

Counter-intuitive questions from the 15.455x transcripts. Each one is designed to expose a conceptual gap.

---

## Random Variables & Sample Spaces

**Q1.** You define X = 1 for heads, −1 for tails. Your friend defines Y = 12 for heads, −3 for tails. Are these the same random variable?

> **Trap:** Students often say "no, the numbers are different." Both are valid random variables over the same sample space. The mapping is arbitrary — only the probability structure matters. P(X=1) = P(Y=12) = 0.5. Neither is more "correct."

---

**Q2.** X ∈ {+1, −1} with equal probability. What is P(X² = 1)?

> **Trap:** Students say 0.5. But X² = 1 regardless of the sign of X. P(X²=1) = **1**, not 0.5. Functions of RVs can collapse the randomness entirely.

---

**Q3.** Is P(X = 3.14159) = 0 the same as saying "X can never equal 3.14159"?

> **Trap:** For continuous distributions, any exact value has probability zero — this is a measure-theoretic fact, not a statement about impossibility. The event can and does occur; it just has measure zero.

---

**Q4.** A PDF p(x) takes the value 5 at some point. Is this valid?

> **Trap:** Students confuse density with probability. PDF values can exceed 1 — the density integrates to 1, but locally it can be arbitrarily large (e.g., Uniform[0, 0.1] has p(x) = 10).

---

## Expectations

**Q5.** E[X²] = (E[X])²? True or false?

> **Trap:** False except when X is deterministic. E[X²] − (E[X])² = Var(X) ≥ 0. Equality holds iff Var(X) = 0. This is the most common Jensen's inequality error in finance.

---

**Q6.** You know E[X] = 0. What is E[X²]?

> **Trap:** "Zero" is the wrong answer. E[X²] = Var(X) + (E[X])² = Var(X). Without knowing the distribution you cannot determine E[X²] from the mean alone.

---

**Q7.** Linearity says E[aX + b] = aE[X] + b. Does this require X and some other variable to be independent?

> **Trap:** No. Linearity of expectation holds unconditionally — no independence, no identical distribution required. This is one of the most powerful (and underused) facts in probability.

---

**Q8.** Is E[1/X] = 1/E[X]?

> **Trap:** No — this is exactly Jensen's inequality. f(x) = 1/x is convex for x > 0, so E[1/X] > 1/E[X] (by Jensen). In finance: expected reciprocal ≠ reciprocal of expected value. This matters for harmonic means in returns.

---

## Variance and Covariance

**Q9.** Cov(X, Y) = 0. Does this mean X and Y are independent?

> **Trap:** No. Classic counterexample: let X take values ±a, ±b with equal prob so E[X]=0. Let Y = X². Y is completely determined by X — they are 100% dependent. Yet Cov(X, Y) = E[X³] − E[X]E[Y] = 0 (odd moments of a symmetric distribution vanish). **Covariance only detects linear dependence.**

---

**Q10.** If X and Y are independent, is Cov(X, Y) = 0?

> **Trap:** Yes — independence implies zero covariance. This direction is true. The trap is reversing the arrow (see Q9). Independence → Cov=0, but Cov=0 ↛ independence.

---

**Q11.** Adding a constant c to X increases Var(X) by c². True or false?

> **Trap:** False. Var(X + c) = Var(X). Variance measures spread around the mean; shifting the distribution doesn't change its spread. Only scaling changes variance: Var(cX) = c²Var(X).

---

**Q12.** You double every outcome of X (i.e., Y = 2X). Does the standard deviation double?

> **Trap:** Yes — σ(2X) = 2σ(X). Variance quadruples; standard deviation doubles. Students often forget this when scaling returns or positions.

---

## Fat Tails

**Q13.** You estimate the volatility of a stock using 100 daily returns. Then you use 1000 returns. Does your volatility estimate become more accurate?

> **Trap:** Only if the distribution has finite variance. For fat-tailed distributions (like p(x) ∝ 1/x²), more data causes the estimated variance to **grow without bound** — it diverges. The Law of Large Numbers does not apply when variance is infinite.

---

**Q14.** A distribution looks like a bell curve when plotted. Can its variance be infinite?

> **Trap:** Yes. The Cauchy distribution p(x) = c/(c²+x²) is unimodal and symmetric, visually resembling a Gaussian at low resolution. But its variance integral diverges. "Looks normal" ≠ finite variance.

---

**Q15.** If a distribution has no finite mean, can you still use it to model financial returns?

> **Trap:** It's valid as a probability law, but none of your standard tools (portfolio variance, Sharpe ratio, CLT) apply. The question isn't whether the distribution "exists" — it's whether your moment-based analytics are meaningful.

---

## Poisson vs. Binomial vs. Gaussian

**Q16.** As n → ∞ and p → 0, does Binomial(n, p) always approach a Gaussian?

> **Trap:** No. It depends on how p shrinks. If np = λ (fixed constant) as n → ∞, p → 0, then Binomial → **Poisson**, not Gaussian. You get Gaussian only when np → ∞ (i.e., the mean grows with n).

---

**Q17.** The Poisson distribution has mean λ. What is its variance?

> **Trap:** Also λ — exactly. Mean equals variance for Poisson. This is unusual (for most distributions variance and mean are independent parameters). In finance: Poisson models for rare events have volatility = √(mean number of events).

---

**Q18.** You observe 0 credit defaults in 1000 loans with p = 0.001. Is this surprising?

> **Trap:** Expected defaults = np = 1. P(0 defaults) = e^(−1) ≈ 0.37 (Poisson approximation). So about 37% of the time you'd see zero defaults even if the model is exactly right. Not surprising at all — students often mistake "rare outcome" for "model is wrong."

---

## Central Limit Theorem

**Q19.** The CLT says the sum of many IID variables is approximately normal. Does this apply to all distributions?

> **Trap:** No — requires finite variance. Fat-tailed distributions (Cauchy, stable distributions with tail exponent < 2) violate the CLT. The sum still has a limiting distribution but it's a stable distribution, not Gaussian.

---

**Q20.** The CLT says the distribution of the sum converges to Gaussian. Does this mean the PMF converges pointwise to the Gaussian PDF?

> **Trap:** The CLT is a statement about CDFs, not PMFs or PDFs. The CDF converges uniformly. The PMF of a discrete sum (e.g., Binomial) doesn't converge to the Gaussian PDF pointwise — it remains discrete. The CLT says nothing about individual probability atoms.

---

**Q21.** You apply the CLT to the average of 10 Uniform(0,1) variables. Does this give an exact Gaussian?

> **Trap:** No — the CLT is an asymptotic (n → ∞) result. For finite n, it's an approximation. The quality depends on the underlying distribution. For symmetric, light-tailed distributions like Uniform, convergence is fast and n=10 is already quite good — but it is never exact for finite n.

---

## Portfolio Theory

**Q22.** You hold 100 uncorrelated assets each with volatility 20%. You equally weight them. What is your portfolio volatility?

> **Trap:** 20%/√100 = **2%**, not 20%. The 1/√n diversification formula applies only for uncorrelated, equal-weight, equal-variance assets. Students often forget the √ and say 0.2%.

---

**Q23.** All your assets have correlation ρ = 1 with each other. How much does adding more assets reduce your portfolio volatility?

> **Trap:** Zero benefit. When ρ = 1 for all pairs, portfolio variance = (Σ wᵢσᵢ)² — the whole thing is a perfect square. There is no cancellation of risk regardless of how many assets you hold.

---

**Q24.** E[Rₚ] = Σ wᵢμᵢ always. But Var(Rₚ) = Σ wᵢ²σᵢ²? True or false?

> **Trap:** False — the full variance formula requires cross terms: Var(Rₚ) = Σᵢ wᵢ²σᵢ² + 2Σᵢ<ⱼ wᵢwⱼσᵢσⱼρᵢⱼ. Omitting correlations understates portfolio risk whenever assets are positively correlated (which they usually are).

---

## Characteristic Functions

**Q25.** The sum of two independent Gaussian variables is Gaussian. Does this hold for only large samples?

> **Trap:** No — this is exact for any finite N, not an asymptotic result. The characteristic function of a Gaussian is exp(−t²σ²/2 + iμt). The product of N such functions is another Gaussian with σ̂² = Σσᵢ², μ̂ = Σμᵢ. No limit needed. This is distinct from the CLT, which is about *non-Gaussian* inputs converging to Gaussian in the limit.

---

## Quick-fire conceptual traps

| Statement | True/False | Why |
|---|---|---|
| P(X = x) = 0 means X never equals x | False | Measure zero ≠ impossible |
| PDF p(x) ≤ 1 always | False | Density can exceed 1 |
| Cov=0 ⟹ independent | False | Only linear dependence detected |
| E[g(X)] = g(E[X]) | False | Only for linear g |
| CLT always gives Gaussian tails | False | Tail convergence is slow |
| More data → better variance estimate | False | Not for infinite-variance distributions |
| Sum of Gaussians is Gaussian (exact) | True | Via characteristic functions, finite N |
