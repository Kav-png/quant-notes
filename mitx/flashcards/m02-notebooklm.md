

## Card 1

**Q:** Term: Stochastic Process

**A:** Definition: A random variable that evolves over time, either in continuous or discrete intervals. Example: The daily closing price of a specific stock over a year.

**S:** {"card_id": 1, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051068+00:00", "last_review": null}

---

## Card 2

**Q:** How is a discrete-time process typically constructed from its components?

**A:** It is built by adding successive increments to an initial value, represented as $S_t = S_{t-1} + x_t$.

**S:** {"card_id": 2, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051105+00:00", "last_review": null}

---

## Card 3

**Q:** Formula for the elementary random walk model

**A:** $S_T = z_1 + z_2 + \dots + z_T$, where $z_t$ are IID random variables with zero mean and unit variance.

**S:** {"card_id": 3, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051116+00:00", "last_review": null}

---

## Card 4

**Q:** What is the expected value of an elementary random walk $S_T$?

**A:** The expected value is $E[S_T] = 0$.

**S:** {"card_id": 4, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051124+00:00", "last_review": null}

---

## Card 5

**Q:** Formula for the variance of an elementary $T$-step random walk

**A:** $Var(S_T) = T$, where $T$ is the number of steps taken.

**S:** {"card_id": 5, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051133+00:00", "last_review": null}

---

## Card 6

**Q:** Term: Innovation

**A:** Definition: The random 'shock' or new information occurring in each period of a time series model. Example: The $\sigma z_t$ term in a generalized random walk.

**S:** {"card_id": 6, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051146+00:00", "last_review": null}

---

## Card 7

**Q:** How is a model considered 'solved' in the context of time series analysis?

**A:** A model is solved when the analyst can describe or forecast the probability distribution of future values.

**S:** {"card_id": 7, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051157+00:00", "last_review": null}

---

## Card 8

**Q:** What property of the expectation operator allows for the calculation of sums of random variables?

**A:** The property of linearity.

**S:** {"card_id": 8, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051165+00:00", "last_review": null}

---

## Card 9

**Q:** Formula for a single period return in a generalized random walk

**A:** $r_t = \mu + \sigma z_t$, where $\mu$ is the mean (offset) and $\sigma$ is the volatility (scale).

**S:** {"card_id": 9, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051175+00:00", "last_review": null}

---

## Card 10

**Q:** What is the expected value of the sum $X_T$ in a generalized random walk model?

**A:** $E[X_T] = T\mu$, where $\mu$ is the constant mean return per step.

**S:** {"card_id": 10, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051184+00:00", "last_review": null}

---

## Card 11

**Q:** Formula for the variance of the sum $X_T$ in a generalized random walk

**A:** $Var(X_T) = T\sigma^2$, where $\sigma^2$ is the variance of an individual step.

**S:** {"card_id": 11, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051193+00:00", "last_review": null}

---

## Card 12

**Q:** Term: Moving Average Model of order 1 (MA(1))

**A:** Definition: A linear model where the current realization depends on the current innovation and the immediately preceding innovation. Example: $r_t = \mu + \sigma z_t + \phi z_{t-1}$.

**S:** {"card_id": 12, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051208+00:00", "last_review": null}

---

## Card 13

**Q:** Why is an MA(1) model not considered IID?

**A:** It is not IID because the observations are drawn from different distributions due to the inclusion of an observed lagged variable $z_{t-1}$.

**S:** {"card_id": 13, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051219+00:00", "last_review": null}

---

## Card 14

**Q:** How does a GARCH model differ from a standard random walk?

**A:** In a GARCH model, the volatility coefficient $\sigma$ is itself time-dependent and evolves according to its own dynamical equation.

**S:** {"card_id": 14, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051229+00:00", "last_review": null}

---

## Card 15

**Q:** Formula for an Autoregressive model of order $p$ (AR(p))

**A:** $R_t = c_0 + c_1 R_{t-1} + \dots + c_p R_{t-p} + \sigma z_t$, where $c_i$ are constant coefficients and $z_t \sim IID(0,1)$.

**S:** {"card_id": 15, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051239+00:00", "last_review": null}

---

## Card 16

**Q:** What is the key insight behind using recursive structures to solve time series models?

**A:** The present value is determined by relating it to previous values from the past plus a new innovation.

**S:** {"card_id": 16, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051250+00:00", "last_review": null}

---

## Card 17

**Q:** Term: Strong Stationarity

**A:** Definition: A property where the joint probability distribution of a process is invariant under a shift in time. Example: A dice game in a casino where the odds never change day-to-day.

**S:** {"card_id": 17, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051261+00:00", "last_review": null}

---

## Card 18

**Q:** Term: Weak Stationarity

**A:** Definition: A property where only the first and second moments (mean and autocovariance) of a process are time-invariant. Example: An AR(1) process with a constant mean and variance over time.

**S:** {"card_id": 18, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051272+00:00", "last_review": null}

---

## Card 19

**Q:** How is the stationarity assumption practically applied to solve for model parameters?

**A:** It allows unconditional expectations to be treated as constant across time, enabling the calculation of long-run means and variances.

**S:** {"card_id": 19, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051287+00:00", "last_review": null}

---

## Card 20

**Q:** Formula for the lag-$k$ autocovariance coefficient $\gamma_k$

**A:** $\gamma_k = E[(R_t - \mu)(R_{t-k} - \mu)]$, which relates the influence of past excess returns on current values.

**S:** {"card_id": 20, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051296+00:00", "last_review": null}

---

## Card 21

**Q:** What is the relationship between $\gamma_k$ and $\gamma_{k-1}$ in an AR(1) model with coefficient $-\lambda$?

**A:** $\gamma_k = -\lambda \gamma_{k-1}$, indicating that the autocovariance decays geometrically with the lag.

**S:** {"card_id": 21, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051307+00:00", "last_review": null}

---

## Card 22

**Q:** Formula for the variance of a stationary AR(1) process

**A:** $\gamma_0 = \frac{\sigma^2}{1 - \lambda^2}$, where $\sigma^2$ is the innovation variance and $\lambda$ is the autoregressive coefficient.

**S:** {"card_id": 22, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051318+00:00", "last_review": null}

---

## Card 23

**Q:** What identifies an ARMA(p,q) model?

**A:** It combines $p$ autoregressive (lagged dependent variable) terms and $q$ moving average (lagged innovation) terms.

**S:** {"card_id": 23, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051327+00:00", "last_review": null}

---

## Card 24

**Q:** Pitfall: The 'Static Process' Misconception

**A:** Stationarity does not mean a process is static or unchanging; it means the underlying probability laws governing its evolution are time-invariant.

**S:** {"card_id": 24, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051337+00:00", "last_review": null}

---

## Card 25

**Q:** Formula for logarithmic returns ($r_t$)

**A:** $r_t = \log(P_t / P_{t-1})$, where $P_t$ is the asset price at time $t$.

**S:** {"card_id": 25, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051345+00:00", "last_review": null}

---

## Card 26

**Q:** Why are asset prices often modelled as log-normal variables?

**A:** This assumption implies that continuously compounded returns are normally distributed, ensuring that prices remain non-negative.

**S:** {"card_id": 26, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051355+00:00", "last_review": null}

---

## Card 27

**Q:** What is the distribution of the sum of log returns $r(T)$ over $T$ periods in a log-normal model?

**A:** $r(T) \sim \mathcal{N}(T\mu, T\sigma^2)$, assuming individual returns are IID normal.

**S:** {"card_id": 27, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051365+00:00", "last_review": null}

---

## Card 28

**Q:** Formula for the price of an asset $P_T$ in terms of log returns

**A:** $P_T = P_0 \exp(r_1 + r_2 + \dots + r_T)$, where $P_0$ is the initial price.

**S:** {"card_id": 28, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051374+00:00", "last_review": null}

---

## Card 29

**Q:** Formula for the expected simple return $E[R]$ of a log-normal process

**A:** $E[R] = e^{\mu + \sigma^2/2} - 1$, where $\mu$ and $\sigma^2$ are the mean and variance of the log returns.

**S:** {"card_id": 29, "state": 2, "step": null, "stability": 1.0, "difficulty": 3.6400000000000006, "due": "2026-05-24T18:10:04.363000+00:00", "last_review": "2026-05-23T18:10:04.363000+00:00"}

---

## Card 30

**Q:** Formula for the variance of the simple return $Var(R)$ in a log-normal model

**A:** $Var(R) = e^{2\mu + \sigma^2}(e^{\sigma^2} - 1)$, where $\mu$ and $\sigma$ are parameters of the underlying normal distribution.

**S:** {"card_id": 30, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051395+00:00", "last_review": null}

---

## Card 31

**Q:** What is the first step in simulating a log-normal price process?

**A:** Determine the parameters (mean and volatility) for the underlying normal distribution of returns.

**S:** {"card_id": 31, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051405+00:00", "last_review": null}

---

## Card 32

**Q:** How must annualized parameters be adjusted for a sampling interval $dt$?

**A:** Drift is scaled by $dt$ and volatility is scaled by $\sqrt{dt}$ to reflect the specific time step.

**S:** {"card_id": 32, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051415+00:00", "last_review": null}

---

## Card 33

**Q:** Term: Monte Carlo Method

**A:** Definition: A computational technique using random number generators to simulate data following a specific model or distribution. Example: Simulating 10,000 possible price paths for a stock to estimate option value.

**S:** {"card_id": 33, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051427+00:00", "last_review": null}

---

## Card 34

**Q:** What serves as the 'best case' setting for testing financial theory in Monte Carlo simulations?

**A:** Simulations provide an environment where the true data-generating process is known and results can be repeated.

**S:** {"card_id": 34, "state": 2, "step": null, "stability": 1.0, "difficulty": 3.6400000000000006, "due": "2026-05-24T18:15:42.855000+00:00", "last_review": "2026-05-23T18:15:42.855000+00:00"}

---

## Card 35

**Q:** What is a major limitation of Monte Carlo simulations compared to closed-form analytics?

**A:** Results are subject to sampling error and machine limitations rather than being exact solutions.

**S:** {"card_id": 35, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051448+00:00", "last_review": null}

---

## Card 36

**Q:** How is a random walk represented in log-price space?

**A:** $X_t = X_{t-1} + r_t$, where $X_t \equiv \log(P_t/P_0)$ and $r_t$ are the log returns.

**S:** {"card_id": 36, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051457+00:00", "last_review": null}

---

## Card 37

**Q:** Term: RW1 (IID Random Walk)

**A:** Definition: The strictest form of random walk where increments are both independent and identically distributed. Example: A process where each step is drawn from the same $\mathcal{N}(0, 1)$ distribution.

**S:** {"card_id": 37, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051469+00:00", "last_review": null}

---

## Card 38

**Q:** Term: RW2 (INID Random Walk)

**A:** Definition: A random walk where increments are independent but not identically distributed. Example: A stock whose daily returns are independent but have differing daily volatility parameters.

**S:** {"card_id": 38, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051480+00:00", "last_review": null}

---

## Card 39

**Q:** Term: RW3 (Uncorrelated Random Walk)

**A:** Definition: A random walk where increments are uncorrelated but may have dependent higher-order moments. Example: Volatility clustering where the squares of increments are correlated over time.

**S:** {"card_id": 39, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051492+00:00", "last_review": null}

---

## Card 40

**Q:** What does the variance ratio test by Lo & MacKinlay evaluate?

**A:** It analyses whether the variance of returns scales linearly with the observation frequency, as predicted by the random walk model.

**S:** {"card_id": 40, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051502+00:00", "last_review": null}

---

## Card 41

**Q:** Pitfall: Assuming Linear Variance Scaling in all Models

**A:** Linear variance scaling is a specific property of the random walk; models with temporal dependence (like AR or MA) do not follow this rule.

**S:** {"card_id": 41, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051515+00:00", "last_review": null}

---

## Card 42

**Q:** What is the primary implication of rejecting the random walk hypothesis for an asset?

**A:** It suggests that asset prices may have some level of predictability or causal influence from past values.

**S:** {"card_id": 42, "state": 2, "step": null, "stability": 1.0, "difficulty": 3.6400000000000006, "due": "2026-05-24T18:15:40.174000+00:00", "last_review": "2026-05-23T18:15:40.174000+00:00"}

---

## Card 43

**Q:** Formula for the variance ratio $VR(q)$

**A:** $VR(q) = \frac{Var(r_t[q])}{q \cdot Var(r_t)}$, which should equal 1 if the process follows a random walk.

**S:** {"card_id": 43, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051535+00:00", "last_review": null}

---

## Card 44

**Q:** How does one calculate the variance of the sum of two independent variables $z$ and $z'$?

**A:** Using linearity and independence, $Var(z + z') = Var(z) + Var(z')$.

**S:** {"card_id": 44, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051545+00:00", "last_review": null}

---

## Card 45

**Q:** What trig identity is used to prove the weak stationarity of $X_t = z \cos(\omega t) + z' \sin(\omega t)$?

**A:** The identity $\cos^2(\theta) + \sin^2(\theta) = 1$ is used to show the variance is constant.

**S:** {"card_id": 45, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051555+00:00", "last_review": null}

---

## Card 46

**Q:** In the process $X_t = z \cos(\omega t) + z' \sin(\omega t)$, what is the autocovariance $E[X_t X_s]$?

**A:** $E[X_t X_s] = \cos(\omega(t-s))$, which depends only on the time difference $t-s$.

**S:** {"card_id": 46, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051566+00:00", "last_review": null}

---

## Card 47

**Q:** What is the significance of $t-s$ appearing alone in an autocovariance function?

**A:** It confirms that the process is weakly stationary as the covariance is invariant under time translation.

**S:** {"card_id": 47, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051576+00:00", "last_review": null}

---

## Card 48

**Q:** Pitfall: Confusing Independence and Uncorrelatedness

**A:** Two variables can be uncorrelated ($E[z_t z_s] = 0$) while still being dependent (e.g., $E[z_t^2 z_s^2] \ne 0$), as seen in RW3 models.

**S:** {"card_id": 48, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051586+00:00", "last_review": null}

---

## Card 49

**Q:** What is the key insight behind 'causal influence' in time series?

**A:** The present state of the system is influenced by its specific historical path rather than just being a random draw from a fixed distribution.

**S:** {"card_id": 49, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051598+00:00", "last_review": null}

---

## Card 50

**Q:** How is a multi-period return $r(T)$ constructed from single-period returns $r_t$?

**A:** It is the simple summation of the individual single-period log returns: $r(T) = \sum_{t=1}^T r_t$.

**S:** {"card_id": 50, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051608+00:00", "last_review": null}

---

## Card 51

**Q:** Formula for the autocovariance of an MA(1) process

**A:** $\gamma_1 = \sigma^2 \phi$ for lag 1, and $\gamma_k = 0$ for all $k > 1$.

**S:** {"card_id": 51, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051616+00:00", "last_review": null}

---

## Card 52

**Q:** What is the effect of a positive $\phi$ in an MA(1) return model?

**A:** It creates a positive correlation between the current return and the previous period's innovation.

**S:** {"card_id": 52, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051626+00:00", "last_review": null}

---

## Card 53

**Q:** What does the term 'Time-Invariant' mean in the context of stationarity?

**A:** It means that the statistical properties of the process do not depend on the absolute time at which the process is observed.

**S:** {"card_id": 53, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051637+00:00", "last_review": null}

---

## Card 54

**Q:** How is 'Volatility Clustering' modelled in an RW3 framework?

**A:** It is modelled by assuming that the magnitudes of shocks (squared increments) are correlated, even if the directions are not.

**S:** {"card_id": 54, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051647+00:00", "last_review": null}

---

## Card 55

**Q:** In an AR(1) model for mean reversion, what does the coefficient $-\lambda$ represent?

**A:** It represents the speed at which the process pulls back toward its long-run mean $\mu$.

**S:** {"card_id": 55, "state": 1, "step": 0, "stability": null, "difficulty": null, "due": "2026-08-09T15:25:32.051657+00:00", "last_review": null}

---
