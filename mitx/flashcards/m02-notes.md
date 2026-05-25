

## Card 1

**Q:** Why is the autocovariance of a stationary stochastic process independent of the mean?

**A:** Autocovariance is calculated using the expected value of the product of deviations from the mean: \[\gamma_k = E[(R_t - \mu)(R_{t-k} - \mu)]\] By subtracting the constant mean \(\mu\) from each observation, the calculation isolate the covariance of the fluctuations, rendering the absolute value of the mean irrelevant [1].

---

## Card 2

**Q:** What defines a weakly stationary stochastic process?

**A:** A process is weakly stationary if its first and second moments—specifically its mean and covariance—remain constant and invariant under time translation [2, 3].

---

## Card 3

**Q:** How is an AR(1) model structured to represent mean reversion?

**A:** It is written as \(R_t - \mu = -\lambda(R_{t-1} - \mu) + \sigma z_t\), where \(\lambda\) controls the direction and magnitude of the variable's change relative to its previous deviation from the mean \(\mu\) [4].

---

## Card 4

**Q:** What is the formula for the lag-\(k\) autocovariance coefficient \(\gamma_k\) in a stationary AR(1) process?

**A:** \[\gamma_k = (-\lambda)^k \gamma_0 = \frac{(-\lambda)^k}{1 - \lambda^2}\sigma^2\] [5].

---

## Card 5

**Q:** How do the mean and variance of a \(T\)-step generalized random walk scale with time?

**A:** Due to the independence of increments, both moments scale linearly with time: the mean is \(T\mu\) and the variance is \(T\sigma^2\) [6-8].

---

## Card 6

**Q:** What is the defining equation of a Moving Average MA(1) model?

**A:** The MA(1) model defines the current return using both a current and a previous random shock: \[r_t = \mu + \sigma z_t + \phi z_{t-1}\] [9].

---

## Card 7

**Q:** What is the core hypothesis tested by the Lo & MacKinlay variance ratio test?

**A:** It tests the random walk hypothesis by checking if the variance of returns scales linearly with the aggregation interval, meaning the variance ratio \(\frac{Var(r_t^{(q)})}{q Var(r_t)}\) should equal 1 [10].

---

## Card 8

**Q:** What is the primary purpose of using Monte Carlo simulations for asset price dynamics?

**A:** Monte Carlo simulation generates an ensemble of hypothetical price paths using random number generators, providing a "best case" environment to approximate exact statistical results when closed-form analytical solutions are unavailable [11, 12].

---

## Card 9

**Q:** How does a GARCH model fundamentally differ from a generalized random walk?

**A:** While a generalized random walk assumes a constant volatility parameter \(\sigma\), a GARCH model uses a time-dependent volatility parameter \(\sigma_t\) that evolves dynamically over time [13, 14].

---

## Card 10

**Q:** Why are asset prices frequently modeled as lognormal variables rather than normal variables?

**A:** Because continuously compounded (log) returns, defined as \(r_t = \log(P_t/P_{t-1})\), are typically modeled as being drawn from a normal distribution. This exponential relationship \(P_T = P_0 \exp(r_1 + \dots + r_T)\) results in a lognormally distributed price path [15, 16].

---
