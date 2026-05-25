# Finance Flashcards

## Card 1

**Q:** Term: Stochastic Process

**A:** Definition: A random variable that evolves over time, either in continuous or discrete intervals. Example: The daily closing price of a specific stock over a year.

---

## Card 2

**Q:** How is a discrete-time process typically constructed from its components?

**A:** It is built by adding successive increments to an initial value, represented as $S_t = S_{t-1} + x_t$.

---

## Card 3

**Q:** Formula for the elementary random walk model

**A:** $S_T = z_1 + z_2 + \dots + z_T$, where $z_t$ are IID random variables with zero mean and unit variance.

---

## Card 4

**Q:** What is the expected value of an elementary random walk $S_T$?

**A:** The expected value is $E[S_T] = 0$.

---

## Card 5

**Q:** Formula for the variance of an elementary $T$-step random walk

**A:** $Var(S_T) = T$, where $T$ is the number of steps taken.

---

## Card 6

**Q:** Term: Innovation

**A:** Definition: The random 'shock' or new information occurring in each period of a time series model. Example: The $\sigma z_t$ term in a generalized random walk.

---

## Card 7

**Q:** How is a model considered 'solved' in the context of time series analysis?

**A:** A model is solved when the analyst can describe or forecast the probability distribution of future values.

---

## Card 8

**Q:** What property of the expectation operator allows for the calculation of sums of random variables?

**A:** The property of linearity.

---

## Card 9

**Q:** Formula for a single period return in a generalized random walk

**A:** $r_t = \mu + \sigma z_t$, where $\mu$ is the mean (offset) and $\sigma$ is the volatility (scale).

---

## Card 10

**Q:** What is the expected value of the sum $X_T$ in a generalized random walk model?

**A:** $E[X_T] = T\mu$, where $\mu$ is the constant mean return per step.

---

## Card 11

**Q:** Formula for the variance of the sum $X_T$ in a generalized random walk

**A:** $Var(X_T) = T\sigma^2$, where $\sigma^2$ is the variance of an individual step.

---

## Card 12

**Q:** Term: Moving Average Model of order 1 (MA(1))

**A:** Definition: A linear model where the current realization depends on the current innovation and the immediately preceding innovation. Example: $r_t = \mu + \sigma z_t + \phi z_{t-1}$.

---

## Card 13

**Q:** Why is an MA(1) model not considered IID?

**A:** It is not IID because the observations are drawn from different distributions due to the inclusion of an observed lagged variable $z_{t-1}$.

---

## Card 14

**Q:** How does a GARCH model differ from a standard random walk?

**A:** In a GARCH model, the volatility coefficient $\sigma$ is itself time-dependent and evolves according to its own dynamical equation.

---

## Card 15

**Q:** Formula for an Autoregressive model of order $p$ (AR(p))

**A:** $R_t = c_0 + c_1 R_{t-1} + \dots + c_p R_{t-p} + \sigma z_t$, where $c_i$ are constant coefficients and $z_t \sim IID(0,1)$.

---

## Card 16

**Q:** What is the key insight behind using recursive structures to solve time series models?

**A:** The present value is determined by relating it to previous values from the past plus a new innovation.

---

## Card 17

**Q:** Term: Strong Stationarity

**A:** Definition: A property where the joint probability distribution of a process is invariant under a shift in time. Example: A dice game in a casino where the odds never change day-to-day.

---

## Card 18

**Q:** Term: Weak Stationarity

**A:** Definition: A property where only the first and second moments (mean and autocovariance) of a process are time-invariant. Example: An AR(1) process with a constant mean and variance over time.

---

## Card 19

**Q:** How is the stationarity assumption practically applied to solve for model parameters?

**A:** It allows unconditional expectations to be treated as constant across time, enabling the calculation of long-run means and variances.

---

## Card 20

**Q:** Formula for the lag-$k$ autocovariance coefficient $\gamma_k$

**A:** $\gamma_k = E[(R_t - \mu)(R_{t-k} - \mu)]$, which relates the influence of past excess returns on current values.

---

## Card 21

**Q:** What is the relationship between $\gamma_k$ and $\gamma_{k-1}$ in an AR(1) model with coefficient $-\lambda$?

**A:** $\gamma_k = -\lambda \gamma_{k-1}$, indicating that the autocovariance decays geometrically with the lag.

---

## Card 22

**Q:** Formula for the variance of a stationary AR(1) process

**A:** $\gamma_0 = \frac{\sigma^2}{1 - \lambda^2}$, where $\sigma^2$ is the innovation variance and $\lambda$ is the autoregressive coefficient.

---

## Card 23

**Q:** What identifies an ARMA(p,q) model?

**A:** It combines $p$ autoregressive (lagged dependent variable) terms and $q$ moving average (lagged innovation) terms.

---

## Card 24

**Q:** Pitfall: The 'Static Process' Misconception

**A:** Stationarity does not mean a process is static or unchanging; it means the underlying probability laws governing its evolution are time-invariant.

---

## Card 25

**Q:** Formula for logarithmic returns ($r_t$)

**A:** $r_t = \log(P_t / P_{t-1})$, where $P_t$ is the asset price at time $t$.

---

## Card 26

**Q:** Why are asset prices often modelled as log-normal variables?

**A:** This assumption implies that continuously compounded returns are normally distributed, ensuring that prices remain non-negative.

---

## Card 27

**Q:** What is the distribution of the sum of log returns $r(T)$ over $T$ periods in a log-normal model?

**A:** $r(T) \sim \mathcal{N}(T\mu, T\sigma^2)$, assuming individual returns are IID normal.

---

## Card 28

**Q:** Formula for the price of an asset $P_T$ in terms of log returns

**A:** $P_T = P_0 \exp(r_1 + r_2 + \dots + r_T)$, where $P_0$ is the initial price.

---

## Card 29

**Q:** Formula for the expected simple return $E[R]$ of a log-normal process

**A:** $E[R] = e^{\mu + \sigma^2/2} - 1$, where $\mu$ and $\sigma^2$ are the mean and variance of the log returns.

---

## Card 30

**Q:** Formula for the variance of the simple return $Var(R)$ in a log-normal model

**A:** $Var(R) = e^{2\mu + \sigma^2}(e^{\sigma^2} - 1)$, where $\mu$ and $\sigma$ are parameters of the underlying normal distribution.

---

## Card 31

**Q:** What is the first step in simulating a log-normal price process?

**A:** Determine the parameters (mean and volatility) for the underlying normal distribution of returns.

---

## Card 32

**Q:** How must annualized parameters be adjusted for a sampling interval $dt$?

**A:** Drift is scaled by $dt$ and volatility is scaled by $\sqrt{dt}$ to reflect the specific time step.

---

## Card 33

**Q:** Term: Monte Carlo Method

**A:** Definition: A computational technique using random number generators to simulate data following a specific model or distribution. Example: Simulating 10,000 possible price paths for a stock to estimate option value.

---

## Card 34

**Q:** What serves as the 'best case' setting for testing financial theory in Monte Carlo simulations?

**A:** Simulations provide an environment where the true data-generating process is known and results can be repeated.

---

## Card 35

**Q:** What is a major limitation of Monte Carlo simulations compared to closed-form analytics?

**A:** Results are subject to sampling error and machine limitations rather than being exact solutions.

---

## Card 36

**Q:** How is a random walk represented in log-price space?

**A:** $X_t = X_{t-1} + r_t$, where $X_t \equiv \log(P_t/P_0)$ and $r_t$ are the log returns.

---

## Card 37

**Q:** Term: RW1 (IID Random Walk)

**A:** Definition: The strictest form of random walk where increments are both independent and identically distributed. Example: A process where each step is drawn from the same $\mathcal{N}(0, 1)$ distribution.

---

## Card 38

**Q:** Term: RW2 (INID Random Walk)

**A:** Definition: A random walk where increments are independent but not identically distributed. Example: A stock whose daily returns are independent but have differing daily volatility parameters.

---

## Card 39

**Q:** Term: RW3 (Uncorrelated Random Walk)

**A:** Definition: A random walk where increments are uncorrelated but may have dependent higher-order moments. Example: Volatility clustering where the squares of increments are correlated over time.

---

## Card 40

**Q:** What does the variance ratio test by Lo & MacKinlay evaluate?

**A:** It analyses whether the variance of returns scales linearly with the observation frequency, as predicted by the random walk model.

---

## Card 41

**Q:** Pitfall: Assuming Linear Variance Scaling in all Models

**A:** Linear variance scaling is a specific property of the random walk; models with temporal dependence (like AR or MA) do not follow this rule.

---

## Card 42

**Q:** What is the primary implication of rejecting the random walk hypothesis for an asset?

**A:** It suggests that asset prices may have some level of predictability or causal influence from past values.

---

## Card 43

**Q:** Formula for the variance ratio $VR(q)$

**A:** $VR(q) = \frac{Var(r_t[q])}{q \cdot Var(r_t)}$, which should equal 1 if the process follows a random walk.

---

## Card 44

**Q:** How does one calculate the variance of the sum of two independent variables $z$ and $z'$?

**A:** Using linearity and independence, $Var(z + z') = Var(z) + Var(z')$.

---

## Card 45

**Q:** What trig identity is used to prove the weak stationarity of $X_t = z \cos(\omega t) + z' \sin(\omega t)$?

**A:** The identity $\cos^2(\theta) + \sin^2(\theta) = 1$ is used to show the variance is constant.

---

## Card 46

**Q:** In the process $X_t = z \cos(\omega t) + z' \sin(\omega t)$, what is the autocovariance $E[X_t X_s]$?

**A:** $E[X_t X_s] = \cos(\omega(t-s))$, which depends only on the time difference $t-s$.

---

## Card 47

**Q:** What is the significance of $t-s$ appearing alone in an autocovariance function?

**A:** It confirms that the process is weakly stationary as the covariance is invariant under time translation.

---

## Card 48

**Q:** Pitfall: Confusing Independence and Uncorrelatedness

**A:** Two variables can be uncorrelated ($E[z_t z_s] = 0$) while still being dependent (e.g., $E[z_t^2 z_s^2] \ne 0$), as seen in RW3 models.

---

## Card 49

**Q:** What is the key insight behind 'causal influence' in time series?

**A:** The present state of the system is influenced by its specific historical path rather than just being a random draw from a fixed distribution.

---

## Card 50

**Q:** How is a multi-period return $r(T)$ constructed from single-period returns $r_t$?

**A:** It is the simple summation of the individual single-period log returns: $r(T) = \sum_{t=1}^T r_t$.

---

## Card 51

**Q:** Formula for the autocovariance of an MA(1) process

**A:** $\gamma_1 = \sigma^2 \phi$ for lag 1, and $\gamma_k = 0$ for all $k > 1$.

---

## Card 52

**Q:** What is the effect of a positive $\phi$ in an MA(1) return model?

**A:** It creates a positive correlation between the current return and the previous period's innovation.

---

## Card 53

**Q:** What does the term 'Time-Invariant' mean in the context of stationarity?

**A:** It means that the statistical properties of the process do not depend on the absolute time at which the process is observed.

---

## Card 54

**Q:** How is 'Volatility Clustering' modelled in an RW3 framework?

**A:** It is modelled by assuming that the magnitudes of shocks (squared increments) are correlated, even if the directions are not.

---

## Card 55

**Q:** In an AR(1) model for mean reversion, what does the coefficient $-\lambda$ represent?

**A:** It represents the speed at which the process pulls back toward its long-run mean $\mu$.

---
