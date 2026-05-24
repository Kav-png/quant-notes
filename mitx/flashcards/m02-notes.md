

## Card 1

**Q:** What is a **Stochastic Process**?

**A:** A time-dependent random variable, observed in either continuous time \( S(t) \) or discrete time \( S_1, S_2, \dots, S_t \) [1, 2]. Concrete example: the daily closing price of a stock recorded at the end of each trading day [2].

---

## Card 2

**Q:** What characterizes a **Time Series** model in the context of discrete-time stochastic processes?

**A:** It samples a variable at uniform, discrete intervals using integer indices, a time-zero origin, and equal spacing [1, 2]. Concrete example: Tracking cumulative daily income excluding non-business days [1, 2].

---

## Card 3

**Q:** Generalized Random Walk (Asset Price Returns)

**A:** \[ r_t = \sigma z_t + \mu \] where \( r_t \) is the log return, \( \sigma \) is the volatility scale, \( z_t \) is a standard IID random variable, and \( \mu \) is the constant drift or mean return [3, 4].

---

## Card 4

**Q:** What is a common pitfall regarding the time variance assumption of an elementary **Random Walk** model?

**A:** Assuming variance remains constant over time is incorrect; in a true \( T \)-step random walk, the variance actually grows linearly with \( T \) [5, 6]. The standard deviation grows proportionally to the square root of \( T \) [5, 6].

---

## Card 5

**Q:** How is the infinite Moving Average (MA) representation derived from an Autoregressive AR(1) process?

**A:** By recursive substitution [7]. You repeatedly substitute the lagged term \( Y_{t-1} \) with its own AR(1) definition, pushing the dependence infinitely into the past to get a sum of prior shocks \( z_{t-k} \) [7].

---

## Card 6

**Q:** What is a hidden assumption or pitfall when analyzing returns distributions using just histograms of asset *prices*?

**A:** Prices themselves are non-stationary and do not follow standard symmetric distributions [8]. Histograms should evaluate *returns* (which can be stationary or normally distributed), not raw price levels [8].

---

## Card 7

**Q:** What does it mean for a time series process to be **Weakly Stationary**?

**A:** A process is weakly stationary if its first and second moments (mean and covariance) are invariant under time translation [9]. Concrete example: An AR(1) model for mean reversion with \( |\lambda| < 1 \) has a constant mean and variance regardless of \( t \) [10, 11].

---

## Card 8

**Q:** What is a critical pitfall to remember regarding Random Number Generators (RNGs) in Monte Carlo simulations?

**A:** The generated numbers are pseudo-random because the machine is deterministic, meaning they only approximate theoretical distributions [12, 13]. For instance, normal approximations are bounded, meaning extreme tail events might be systematically under-represented [12, 13].

---

## Card 9

**Q:** If the Variance Ratio \( \frac{\text{Var}(r_t^{(q)})}{q \text{Var}(r_t)} \) is significantly greater than 1, what does this imply about the asset's returns?

**A:** It rejects the random walk hypothesis and implies the returns are serially correlated rather than uncorrelated [14, 15]. This means past price changes carry predictive information for future behavior, challenging market efficiency [16, 17].

---

## Card 10

**Q:** Lag-\( k \) Autocovariance Coefficient for an AR(1) Process

**A:** \[ \gamma_k = (-\lambda)^k \gamma_0 = \frac{(-\lambda)^k}{1 - \lambda^2} \sigma^2 \] where \( \gamma_k \) is the covariance at lag \( k \), \( \lambda \) is the mean reversion strength (\( |\lambda| < 1 \)), \( \gamma_0 \) is the constant variance, and \( \sigma \) is the shock scale [11, 18].

---
