

## Card 1

**Q:** What is a stochastic process, and what are the two time domains it can live in?

**A:** A stochastic process is a time-dependent random variable. It can exist in **continuous time** \( S(t) \) or **discrete time** \( S_1, S_2, \ldots, S_t \). Time series models sample at uniform intervals with integer indices, equal spacing, and a time-zero origin.

---

## Card 2

**Q:** Formula: How are levels \( S_t \) constructed from increments, and how are increments recovered?

**A:** Construction (cumulative sum): \[ S_t = S_{t-1} + x_t = x_0 + x_1 + \cdots + x_t \] Recovery (differencing): \[ x_t = S_t - S_{t-1} \]

---

## Card 3

**Q:** Formula: Elementary random walk model — definition and required properties of increments.

**A:** The elementary random walk is a sum of IID "standard" random variables: \[ S_T = z_1 + z_2 + \cdots + z_T \] where each \( z_t \) satisfies \( E[z_t] = 0 \), \( E[z_t^2] = 1 \), and \( E[z_t z_{t'}] = 0 \) for \( t \neq t' \). Two examples: coin toss (\(\pm 1\) with \( p = \tfrac{1}{2} \)) and Gaussian \( z_t \sim N(0,1) \).

---

## Card 4

**Q:** Formula: Derive \( E[S_T] \) and \( \text{Var}(S_T) \) for the elementary random walk, explaining why cross-terms vanish.

**A:** \[ E[S_T] = E[z_1] + \cdots + E[z_T] = 0 \] \[ \text{Var}(S_T) = E[S_T^2] = \sum_{t=1}^T E[z_t^2] + 2\sum_{t < t'} E[z_t z_{t'}] = T + 0 = T \] **Key**: cross-terms \( E[z_t z_{t'}] = 0 \) by independence, leaving only the \( T \) diagonal terms. Standard deviation scales as \( \sqrt{T} \).

---

## Card 5

**Q:** What does "universality" mean in the context of random walk models, and why does it matter?

**A:** **Universality**: The mean-zero, variance-\(T\) results hold for *any* standard increments (Gaussian or discrete), not just a specific distribution. The key statistical features depend on the first two moments only, not the full distributional form. This makes the random walk a universal building block.

---

## Card 6

**Q:** Formula: Generalized random walk — single-step return, its moments, and connection to asset prices.

**A:** Each step: \( r_t = \mu + \sigma z_t \), where \( \mu \) = mean (drift/return) and \( \sigma \) = volatility (risk). From linearity: \[ E[r_t] = \mu, \quad E[(r_t - \mu)^2] = \sigma^2, \quad E[(r_t - \mu)(r_{t'} - \mu)] = 0 \text{ for } t \neq t' \] Log return application: \( r_t \equiv \log(P_t / P_{t-1}) \), giving \( P_T = P_0 e^{r_1 + r_2 + \cdots + r_T} \).

---

## Card 7

**Q:** Formula: Mean and variance of the \( T \)-step sum \( X_T \) in the generalized random walk.

**A:** For \( X_T = r_1 + r_2 + \cdots + r_T \): \[ E[X_T] = T\mu \] \[ \text{Var}(X_T) = T\sigma^2 \] Both mean and variance scale **linearly with \( T \)**. The mean and variance of the sum are \( T \) times the per-step parameters. Standard deviation scales as \( \sigma\sqrt{T} \).

---

## Card 8

**Q:** How are annualized parameters \( \mu \) and \( \sigma \) scaled for a daily time step \( dt = 1/252 \), and how do you reverse the process to annualize from daily estimates?

**A:** With time step \( dt = 1/252 \) (one trading day), the per-step parameters are: \[ \mu_{\text{daily}} = \mu_{\text{annual}} \cdot dt \] \[ \sigma_{\text{daily}} = \sigma_{\text{annual}} \cdot \sqrt{dt} \] To annualize estimates from daily data: multiply mean by 252, multiply standard deviation by \( \sqrt{252} \). **Key**: variance scales linearly, but standard deviation scales with square root — never annualize std by multiplying by 252.

---

## Card 9

**Q:** What does it mean to "solve" a time series model?

**A:** A model is "solved" when we can **describe or forecast the probability distribution** of future values — not just simulate paths, but characterise the full distribution (mean, variance, shape) of outcomes at future times.

---

## Card 10

**Q:** Formula: MA(1) model — equation, why it is not IID, and its autocovariance structure. Contrast with GARCH.

**A:** **MA(1)**: \( r_t = \mu + \sigma z_t + \theta z_{t-1} \) — current value depends on current and one lagged innovation. Not IID because \( z_{t-1} \) is a *known* (observed) quantity at time \( t \), introducing correlation at lag 1: \[ \gamma_1 = \theta\sigma^2, \quad \gamma_k = 0 \text{ for } k > 1 \] **GARCH**: \( r_t = \mu + \sigma_t z_t \) where \( \sigma_t^2 \) is itself time-varying (its own dynamics). Models volatility clustering.

---

## Card 11

**Q:** Formula: AR(p) and ARMA(p,q) models — equations and the structural difference between them.

**A:** **AR(p)**: \[ R_t = c_0 + c_1 R_{t-1} + \cdots + c_p R_{t-p} + z_t, \quad z_t \sim \text{IID}(0,1) \] Past *observations* appear on the right-hand side. **ARMA(p,q)**: \[ R_t = c_0 + c_1 R_{t-1} + \cdots + c_p R_{t-p} + z_t + \theta_1 z_{t-1} + \cdots + \theta_q z_{t-q} \] Combines AR (lagged dependent variable) and MA (lagged innovation) structure. Coefficients are estimated from data.

---

## Card 12

**Q:** Distinguish strong stationarity from weak stationarity, and explain which is used in practice for solving AR models.

**A:** **Strong stationarity**: the *joint distribution* of all values is invariant under time translation \( t \to t + s \). **Weak (covariance) stationarity**: only the **first and second moments** are time-invariant — mean \( E[R_t] \) and autocovariance \( E[(R_t - \mu)(R_{t-k} - \mu)] \) do not depend on \( t \). Weak stationarity is the workhorse assumption for solving linear time series models.

---

## Card 13

**Q:** Formula: Derive the unconditional mean of AR(1) using stationarity, then rewrite in mean-reversion form with the stationarity condition.

**A:** Starting from \( R_t = c_0 + c_1 R_{t-1} + z_t \), apply expectations and use stationarity \( E[R_t] = E[R_{t-1}] \equiv \bar{R} \): \[ \bar{R} = c_0 + c_1 \bar{R} \implies \bar{R} = \frac{c_0}{1 - c_1} \] Reparameterize as \( \mu = c_0/(1-c_1) \) and \( \lambda = -c_1 \) to get the mean-reversion form: \[ R_t - \mu = -\lambda(R_{t-1} - \mu) + z_t, \quad |\lambda| < 1 \text{ required for stationarity} \]

---

## Card 14

**Q:** Formula: Derive the unconditional variance \( \gamma_0 \) of the stationary AR(1) process using stationarity, and explain why the cross term vanishes.

**A:** From \( R_t - \mu = -\lambda(R_{t-1} - \mu) + z_t \), square both sides and take expectations. The cross term \( E[z_t(R_{t-1} - \mu)] = 0 \) by independence (current shock is independent of all past values): \[ \gamma_0 = \lambda^2 \gamma_0 + \sigma^2 \implies \gamma_0 = \frac{\sigma^2}{1 - \lambda^2} \] This requires \( |\lambda| < 1 \) for the variance to be finite and positive.

---

## Card 15

**Q:** Formula: Lag-\(k\) autocovariance of a stationary AR(1) process — derive the recursion and closed form.

**A:** The lag-\(k\) autocovariance \( \gamma_k = E[(R_t - \mu)(R_{t-k} - \mu)] \). Using stationarity and the AR(1) recursion: \[ \gamma_k = -\lambda \, \gamma_{k-1} \] Iterating gives: \[ \gamma_k = (-\lambda)^k \gamma_0 = \frac{(-\lambda)^k \sigma^2}{1 - \lambda^2} \] The autocovariance **decays geometrically** with lag \( k \). For positive \( \lambda \) (mean reversion), the sign alternates; for \( \lambda \) near 1, decay is slow.

---

## Card 16

**Q:** Explain the difference between unconditional and conditional expectations in time series, and when each is applied.

**A:** **Unconditional expectations**: taken with respect to *all* future random variables as if standing at time \(-\infty\). Used to derive long-run means and variances (assumes stationarity). **Conditional expectations**: taken at a fixed point in time \( t \), treating all past observations \( R_{t-1}, R_{t-2}, \ldots \) as **known constants** (not random variables). Used for forecasting. The same past value can be random (unconditional) or fixed (conditional) depending on the perspective.

---

## Card 17

**Q:** Why are asset prices modeled as lognormal? Give the full price equation and the distribution of cumulative log returns.

**A:** Asset prices are often modeled as **lognormal** because log returns \( r_t = \log(P_t/P_{t-1}) \sim N(\mu, \sigma^2) \) are normally distributed. Then: \[ P_T = P_0 e^{r(T)}, \quad r(T) = r_1 + r_2 + \cdots + r_T \sim N(T\mu, T\sigma^2) \] Key properties of the lognormal model: **prices stay positive** (no negative prices), log returns are **additive** (convenient for sums), and the simple return \( R = P_T/P_0 - 1 \) has a skewed distribution with heavier right tail.

---

## Card 18

**Q:** Formula: Expected simple return and variance of simple return for a one-year lognormal price process. Explain the Jensen's inequality effect.

**A:** Simple return \( R = P_T/P_0 - 1 = e^{r(T)} - 1 \). From the lognormal moment formulas: \[ E[R] = e^{\mu + \sigma^2/2} - 1 \] \[ \text{Var}(R) = e^{2\mu + \sigma^2}(e^{\sigma^2} - 1) \] **Note**: \( E[R] > e^\mu - 1 \) due to the \( +\sigma^2/2 \) Jensen's inequality correction — higher volatility increases the expected simple return even with fixed \( \mu \).

---

## Card 19

**Q:** List the 6-step procedure for simulating a lognormal asset price process via Monte Carlo.

**A:** Six steps: (1) Determine annualized parameters \( \mu, \sigma \). (2) Scale by \( dt = 1/252 \): use \( \mu \cdot dt \) and \( \sigma\sqrt{dt} \). (3) Draw standard normal random numbers. (4) Generate daily returns \( r_t = \mu \cdot dt + z_t \cdot \sigma\sqrt{dt} \). (5) Construct log-price paths via cumulative sum; exponentiate to get price paths \( P = e^S \). (6) Compute statistics (mean, std) over the ensemble and verify against theoretical formulas.

---

## Card 20

**Q:** Why is Monte Carlo called a "best case" environment for testing financial models? What are its key limitations?

**A:** Monte Carlo provides a **"best case" testing environment** because: (1) The true data-generating process is *known* (we set it). (2) We can generate unlimited realisations — unlike real markets where history happens once and can never be repeated. (3) Closed-form results exist to validate against. **Limitations**: statistical sampling error, pseudo-random numbers are only approximations, bounded tails (rnorm is not truly infinite-tailed).

---

## Card 21

**Q:** Define and contrast RW1, RW2, and RW3. What distinguishes RW3 from RW1/RW2 in terms of moment conditions?

**A:** **RW1 (IID)**: Increments are independent *and* identically distributed. \( E[\epsilon_t \epsilon_{t'}] = \sigma^2 \delta_{tt'} \). Strictest form. **RW2 (INID)**: Independent but non-identically distributed (e.g., volatility varies by day). **RW3 (Uncorrelated)**: Increments uncorrelated but *dependent* via higher moments: \[ E[\epsilon_t \epsilon_{t'}] = 0 \text{ (uncorrelated)}, \quad E[\epsilon_t^2 \epsilon_{t'}^2] \neq 0 \text{ (dependent squares — volatility clustering)} \] RW3 is the weakest form; passes autocorrelation tests but fails independence tests.

---

## Card 22

**Q:** Formula: Define the \( q \)-period aggregated return and the variance ratio \( VR(q) \), and state its null-hypothesis value for a random walk.

**A:** The \( q \)-period (aggregated) return is: \[ r_t^{(q)} = r_t + r_{t-1} + \cdots + r_{t-q+1} = \log(P_t / P_{t-q}) \] Under any random walk (RW1, RW2, or RW3), uncorrelated increments imply: \[ \text{Var}(r_t^{(q)}) = q \cdot \text{Var}(r_t) \] Therefore the **variance ratio** should equal 1: \[ VR(q) = \frac{\text{Var}(r_t^{(q)})}{q \cdot \text{Var}(r_t)} = 1 \]

---

## Card 23

**Q:** Formula: The three variance estimators \( \hat{\sigma}_a^2 \), \( \hat{\sigma}_b^2(q) \), \( \hat{\sigma}_c^2(q) \) in the Lo-MacKinlay variance ratio test. What does each measure?

**A:** Three estimators used to compute \( VR(q) \): \[ \hat{\mu} = \frac{1}{T}(X_T - X_0) \] \[ \hat{\sigma}_a^2 = \frac{1}{T}\sum_{t=1}^T (r_t - \hat{\mu})^2 \quad \text{(base frequency)} \] \[ \hat{\sigma}_b^2(q) = \frac{1}{nq}\sum_{k=1}^{n}(X_{qk} - X_{q(k-1)} - q\hat{\mu})^2 \quad \text{(non-overlapping } q\text{-period)} \] \[ \hat{\sigma}_c^2(q) = \frac{1}{nq^2}\sum_{t=q}^{nq}(X_t - X_{t-q} - q\hat{\mu})^2 \quad \text{(overlapping, more power)} \]

---

## Card 24

**Q:** Why does the overlapping estimator \( \hat{\sigma}_c^2(q) \) have higher statistical power than the non-overlapping \( \hat{\sigma}_b^2(q) \)?

**A:** The overlapping estimator \( \hat{\sigma}_c^2 \) uses all \( nq - q + 1 \) possible \( q \)-period windows (shifted by one period each time), vs. only \( n \) non-overlapping windows in \( \hat{\sigma}_b^2 \). **Why overlapping is better**: more data points → more efficient estimator → higher statistical power to detect departures from random walk. The effective sample size of \( \hat{\sigma}_c^2 \) grows with \( T \) instead of \( T/q \).

---

## Card 25

**Q:** Formula: Lo-MacKinlay test statistic \( z(q) \) for the variance ratio test — write the full formula and state its null distribution.

**A:** The test statistic (with bias correction) for the overlapping estimator: \[ z(q) = \sqrt{nq}\left(VR(q) - 1\right) \cdot \sqrt{\frac{3q}{2(2q-1)(q-1)}} \sim N(0,1) \] Under the null hypothesis (random walk), \( z(q) \) is asymptotically standard normal. **Large \( |z(q)| \)** → reject the random walk. The denominator corrects for the asymptotic variance of \( VR(q) \), which depends on \( q \).

---

## Card 26

**Q:** What were Lo & MacKinlay's empirical findings when testing the random walk? Distinguish equal-weighted vs value-weighted index results.

**A:** Lo & MacKinlay (1988) tested weekly stock returns (CRSP data, 1962–1985): **Equal-weighted index**: VR strongly and significantly **above 1** (e.g., VR ≈ 1.30–2.05 for \(q = 2\)–16), with z-stats 5–9. Random walk **firmly rejected**. **Value-weighted index**: VR closer to 1 (≈1.08–1.22), with smaller z-stats (≈2.3). Some rejections. **Key finding**: rejections driven largely by *small stocks*; cannot be fully attributed to infrequent trading or time-varying volatility. Rejection does *not* support a simple mean-reverting model.

---

## Card 27

**Q:** What questions does rejecting the random walk open, and what does it *not* imply about market efficiency?

**A:** Rejecting the random walk: (1) Does **not** automatically imply inefficiency (prices could still be unpredictable in an economic sense). (2) Does not identify a better model. (3) Does not determine whether excess returns are exploitable after transaction costs. Possible interpretations: the generating process is RW3 (uncorrelated but dependent), a more complex model is needed, or markets are inefficient. The question of **predictability** and **efficiency** remains empirical and open.

---

## Card 28

**Q:** Why should histograms (and other distributional analyses) be applied to returns rather than to price levels?

**A:** **Prices** are non-stationary (they trend and compound over time), so their histogram is meaningless as a distribution descriptor. **Returns** (log returns or simple returns) are stationary under random walk assumptions, so their histogram reveals the true distributional shape. The random walk model is stated in terms of returns (IID increments), not price levels. Also, returns are scale-independent — comparing prices across different stocks or periods requires normalization.

---

## Card 29

**Q:** Why are log returns preferred over simple returns for time series modelling? What property makes them especially convenient?

**A:** Log returns are **additive**: \( r_t = \log(P_t/P_{t-1}) \) so \( r(T) = \sum r_t = \log(P_T/P_0) \). Simple returns are **not** additive: \( R_t = P_t/P_{t-1} - 1 \) so the multi-period simple return is multiplicative. Additivity makes log returns the natural choice for time series modelling — variances sum, CLT applies directly, and the lognormal price model is self-consistent. **Pitfall**: using simple returns in an AR or random walk model creates inconsistencies because their multi-period composition is non-linear.

---

## Card 30

**Q:** How do you interpret a QQ plot against the standard normal for financial return data? What does curvature indicate?

**A:** A **QQ plot** plots empirical quantiles of the data against theoretical quantiles of the standard normal. If data are exactly normal: points fall on the 45° line. **Fat tails (leptokurtosis)**: points curve upward on the right and downward on the left (common in financial returns — more extreme observations than Gaussian predicts). For a *lognormal simple return* \( R \), the QQ plot curves strongly upward (right-skewed distribution). A QQ plot for log returns \( \log(1+R) \) should be closer to linear if the lognormal model holds.

---

## Card 31

**Q:** Pitfall: Why can the variance ratio test fail to detect the dependence in an RW3 process? What type of model would capture it?

**A:** **Pitfall**: Uncorrelated ≠ Independent. For RW3, increments satisfy \( E[\epsilon_t \epsilon_{t'}] = 0 \) (uncorrelated), so the variance ratio test (which tests only linear dependence) **will not reject**. But \( E[\epsilon_t^2 \epsilon_{t'}^2] \neq 0 \) — squared returns are correlated (volatility clustering). GARCH models capture this. **Implication**: a stock passing the variance ratio test may still exhibit predictable volatility, which has important options pricing implications.

---

## Card 32

**Q:** What is the null hypothesis of the variance ratio test, and what assumptions does it require? What are its limitations?

**A:** The variance ratio test only requires that increments are **uncorrelated** (not necessarily IID) under the null. It tests: \[ H_0: VR(q) = 1 \text{ for all } q \] vs serial correlation in any direction. It does **not** assume normality (heteroscedasticity-robust versions exist via White's correction). It can be applied to individual stocks, portfolios, or any return series. It is sensitive to the choice of \( q \) — no single \( q \) captures all alternatives.

---

## Card 33

**Q:** How does the AR(1) model's autocorrelation structure manifest in the variance ratio? What do VR > 1 and VR < 1 indicate economically?

**A:** For an AR(1) with mean-reversion coefficient \( |\lambda| < 1 \): \[ \gamma_0 = \frac{\sigma^2}{1 - \lambda^2} \] The **variance ratio** for \(q\)-period returns under an AR(1) is *not* 1 — serial correlation inflates or deflates it. For positive serial correlation in returns (momentum), VR > 1; for negative serial correlation (mean reversion), VR < 1. This is why the variance ratio test can distinguish the random walk from mean-reversion models.

---

## Card 34

**Q:** Tootsie Roll case study: What were the estimated annualized mean return and volatility, and what did exploratory data analysis reveal about the random walk hypothesis?

**A:** For Tootsie Roll (TR, 1988–2017, Yahoo Finance): \[ \hat{\mu}_{\text{annual}} = 252 \times \bar{r}_{\text{daily}} \approx 8.5\% \] \[ \hat{\sigma}_{\text{annual}} = \sqrt{252} \times \text{sd}(r_{\text{daily}}) \approx 24.4\% \] Exploratory plots showed: (1) Price series trending upward over time (non-stationary, lognormal-like). (2) Daily return series showing **non-constant variance** — periods of higher volatility visible (inconsistent with RW1 but consistent with RW3/GARCH). (3) White noise simulation with same overall volatility looked notably smoother.

---

## Card 35

**Q:** How can parameter stability across sub-periods and variance scaling across frequencies both be used as informal tests of the random walk model?

**A:** The random walk model has **time-homogeneous** parameters — \( \mu \) and \( \sigma \) should be the same in every sub-period. To test: re-estimate parameters in different sub-periods and check whether variations exceed what sampling error alone would predict. **Scaling test**: if the model holds, the variance computed from \(n\)-day returns should equal \(n\) times the 1-day variance. Plotting this vs \(n\) should give a straight line through the origin. Systematic deviation (curvature, slope change) is evidence against the model.

---

## Card 36

**Q:** Summarise the contributions of Fama (1965) and Samuelson (1965) to random walk theory and market efficiency.

**A:** Fama (1965): developed random walk theory for stock prices; argued technical analysis ("charting") is largely without value if prices follow a random walk. Samuelson (1965): proved that **properly anticipated prices fluctuate randomly** — if all available information is already incorporated in prices, future price changes must be unpredictable. Both papers established the theoretical foundation for the **Efficient Market Hypothesis (EMH)**: prices reflect all available information.

---

## Card 37

**Q:** Explain the mean-reversion mechanism in AR(1). How does \( \lambda \) control the speed of reversion, and what happens at the boundary \( |\lambda| = 1 \)?

**A:** Positive \( \lambda \): excess value \( R_{t-1} > \mu \) → change \( R_t - R_{t-1} \) is in the *opposite* direction → pulls toward \( \mu \). Speed of reversion is proportional to the deviation. Autocovariance alternates in sign: \( \gamma_k = (-\lambda)^k \gamma_0 \). The process oscillates around \( \mu \). As \( \lambda \to 0 \), the model approaches an IID (white noise) process. As \( \lambda \to 1 \), reversion slows (nearly a random walk). **Requires \( |\lambda| < 1 \)** for stationarity; otherwise variance diverges.

---

## Card 38

**Q:** Pitfall: Why should you be cautious about concluding that parameters are "unstable" just from seeing different estimates in different sub-periods?

**A:** **Pitfall**: Model parameters estimated from historical data (\( \hat{\mu} \), \( \hat{\sigma} \)) are themselves random variables. They will always show some variation across sub-periods even if the true model has constant parameters. The question is whether the variation is **statistically significant** — i.e., larger than what sampling error alone predicts. Without formal testing, visual differences in estimates across periods can mislead. Use confidence intervals and formal tests (e.g., the z-statistic) to assess significance.

---

## Card 39

**Q:** In Monte Carlo simulation, what is the "ensemble" and how are cross-sectional vs time-series statistics used to characterise the process?

**A:** The "ensemble" is the collection of all simulated paths. **Cross-sectional statistics** at a fixed time \( t \) across the ensemble approximate the probability distribution at that time — e.g., the histogram of \( P_T \) across all paths estimates the terminal price distribution. **Time series statistics** along a single path (e.g., mean and std of one path's returns) estimate the ergodic distribution if the process is stationary. For finite samples, ensemble statistics are more reliable than single-path statistics.

---

## Card 40

**Q:** Write the AR(1) simulation update equation and explain what the autocorrelation function (ACF) plot reveals for different values of \( \lambda \).

**A:** The AR(1) simulation in R implements: \[ R[t] = (1 + \lambda)(\mu \cdot dt) - \lambda \cdot R[t-1] + \epsilon[t] \] where \( \epsilon[t] \sim N(0, \sigma^2 dt) \). This is the mean-reversion form \( R_t - \mu \cdot dt = -\lambda(R_{t-1} - \mu \cdot dt) + \epsilon_t \) rearranged. The `acf()` function reveals the lag-autocorrelation structure — for \( \lambda = 0.4 \), small positive autocorrelations at lag 1; for \( \lambda = 0.8 \), strong and slowly decaying autocorrelations.

---

## Card 41

**Q:** Compare the coin toss and Gaussian random walk increments: properties, distributions of \( S_T \), and the role of the CLT.

**A:** **Coin toss**: \( z_t = \pm 1 \) each with probability \( 1/2 \). Check: \( E[z_t] = 0 \), \( E[z_t^2] = 1 \). **Gaussian**: \( z_t \sim N(0,1) \), \( p(z_t) = \frac{1}{\sqrt{2\pi}}e^{-z_t^2/2} \). Both satisfy the three standard properties. The distribution of \( S_T \) differs (binomial vs Gaussian) but means and variances are identical — illustrating universality. For large \( T \), the CLT ensures both converge to the same Gaussian shape for \( S_T \).

---

## Card 42

**Q:** What are the key R functions for Monte Carlo simulation, and what are their important limitations compared to true random variables?

**A:** Key R functions for Monte Carlo: **`runif(n)`** — uniform on \([0,1]\); **`rnorm(n, mean=0, sd=1)`** — normal draws; **`sample`** — discrete values with specified probabilities. These are *pseudo-random* (deterministic algorithms), not truly random. **Important limitations**: `rnorm` produces bounded approximations to the Gaussian (not truly infinite tails); `runif` assigns nonzero probability to \( X = 1/2 \) (impossible for a true continuous uniform). Scaling: `rnorm(n, mean=mu*dt, sd=sigma*sqrt(dt))` generates daily returns directly.

---

## Card 43

**Q:** Derive the autocovariance recursion \( \gamma_k = -\lambda \gamma_{k-1} \) for AR(1), carefully explaining why the cross-term \( E[z_t(R_{t-k} - \mu)] = 0 \).

**A:** The **lag-k autocovariance** \( \gamma_k \) of a stationary AR(1) satisfies: \[ \gamma_k = E[(R_t - \mu)(R_{t-k} - \mu)] \] From the recursion \( R_t - \mu = -\lambda(R_{t-1} - \mu) + z_t \): \[ \gamma_k = E[(-\lambda(R_{t-1} - \mu) + z_t)(R_{t-k} - \mu)] = -\lambda \gamma_{k-1} + \underbrace{E[z_t(R_{t-k}-\mu)]}_{=0 \text{ for } k > 0} = -\lambda\gamma_{k-1} \] The cross-term vanishes because \( z_t \) is independent of all \( R_{t-k} \) for \( k > 0 \) (future innovations are independent of past values).

---

## Card 44

**Q:** Describe the shape of the empirical CDF and sorted barplot for the simple return \( R = P_T/P_0 - 1 \) under lognormal dynamics. Why does median differ from mean?

**A:** The **empirical CDF** (ECDF) of \( 1 + R \) for a lognormal process is right-skewed: median \( < \) mean, bounded below at 0, long right tail. The median \( P_{T,\text{median}} = P_0 e^{T\mu} \) (below the mean \( P_0 e^{T\mu + T\sigma^2/2} \) by Jensen's correction). The **sorted barplot** of \( 1+R \) visually shows the skewed shape: most outcomes cluster near the median, with rare very large outcomes pulling up the mean. This is a key feature distinguishing lognormal from normal returns.

---

## Card 45

**Q:** What does it mean for a time series model to be "recursive," and how does this structure relate to causality and simulation?

**A:** A time series model is **recursive (causal)** if the current value is defined in terms of past values plus a new innovation: \[ R_t = f(R_{t-1}, R_{t-2}, \ldots, z_t) \] This structure means: (1) future values are determined sequentially from the present; (2) past observations influence the likelihood of future outcomes; (3) the model can be simulated forward in time step by step. The coefficients encode how much weight past history has. Both AR and ARMA are recursive; pure random walk has zero weight on past history.

---

## Card 46

**Q:** What are the three tools used to "solve" a linear time series model analytically, and how do they work together?

**A:** Three tools used together: (1) **Linearity of expectation** — \( E[aX + bY] = aE[X] + bE[Y] \), allowing moments of sums to be computed term-by-term. (2) **Recursion** — substitute the model equation into itself or into moment expressions. (3) **Weak stationarity** — set \( E[R_t] = E[R_{t-1}] \) and \( \text{Var}(R_t) = \text{Var}(R_{t-1}) \), converting the recursive system into an algebraic equation. Together these three steps fully solve for unconditional means, variances, and autocovariances of any linear time series model.

---

## Card 47

**Q:** What is an "innovation" in a time series model, and what key independence property makes it analytically useful in deriving moments?

**A:** In a recursive time series model, the **innovation** is the component of the current value that is genuinely new and unpredictable given the past. For AR(1): \( z_t \) is the innovation — independent of all \( R_{t-k} \) for \( k \geq 1 \). This independence is what makes cross-terms in moment calculations vanish: \[ E[z_t \cdot g(R_{t-1}, R_{t-2}, \ldots)] = 0 \] for any function \( g \) of past values. This is the fundamental property exploited in every derivation.

---

## Card 48

**Q:** Explain the nesting relationship RW1 ⊇ RW2 ⊇ RW3. Give an example at each boundary, and state which statistical test is appropriate for each level.

**A:** RW1 → RW2 → RW3 are **progressively weaker** conditions: RW1 (IID) implies RW2 (INID) implies RW3 (uncorrelated). But *not* vice versa. A process can be: RW3 but not RW2 (e.g. GARCH: uncorrelated returns, but correlated squared returns, non-identical distributions). RW2 but not RW1 (independent returns but with different volatility each day). **Practical importance**: the variance ratio test detects violations of RW3 (linear autocorrelation); ARCH/GARCH tests detect violations at the RW2 level (dependence in squared returns).

---

## Card 49

**Q:** Define the log-price random walk \( X_t \). What are its conditional mean and variance, and why is this representation useful?

**A:** The log-price process is: \[ X_t \equiv \log(P_t / P_0), \quad X_t = X_{t-1} + r_t \] This is a random walk in *log-price space*. Increments are log returns \( r_t = \log(P_t/P_{t-1}) \). Under the generalized model: \[ E[X_t | X_0] = X_0 + t\mu, \quad \text{Var}(X_t | X_0) = t\sigma^2 \] Then \( P_t = P_0 e^{X_t} \). **Key**: working in log-price space converts a multiplicative price process into an additive random walk — all the linear time series tools apply.

---

## Card 50

**Q:** Formula: Derive the variance and lag-1 autocovariance of MA(1). What is the key structural difference from AR(1) autocovariance?

**A:** The **MA(1) autocovariance derivation**: with \( r_t = \mu + \sigma z_t + \theta z_{t-1} \): \[ \gamma_0 = E[(r_t - \mu)^2] = \sigma^2(1 + \theta^2) \] \[ \gamma_1 = E[(r_t - \mu)(r_{t-1} - \mu)] = E[(\sigma z_t + \theta z_{t-1})(\sigma z_{t-1} + \theta z_{t-2})] = \theta\sigma^2 \] \[ \gamma_k = 0 \text{ for all } k \geq 2 \] MA(1) has **finite memory** — correlation cuts off after one lag. This is the "MA" identification signature. Compare AR(1): autocovariance decays but never reaches zero exactly.

---

## Card 51

**Q:** Define white noise. How does it relate to RW3, and why is the random walk itself not white noise?

**A:** **White noise**: a process \( \epsilon_t \) with \( E[\epsilon_t] = 0 \), \( E[\epsilon_t^2] = \sigma^2 \), and \( E[\epsilon_t \epsilon_{t'}] = 0 \) for \( t \neq t' \). It is **uncorrelated** but not necessarily independent (satisfies RW3 conditions). All random walk innovations and AR/MA error terms are white noise. A white noise process with constant variance looks structurally like a random walk's increments — but the random walk itself (the cumulative sum) is *not* white noise; its variance grows with time.

---

## Card 52

**Q:** Explain Jensen's inequality and its role in the lognormal \( \sigma^2/2 \) correction. Why does higher volatility raise the expected price level?

**A:** **Jensen's inequality**: for a convex function \( f \), \( E[f(X)] \geq f(E[X]) \). Applied to lognormal returns: \( f(x) = e^x \) is convex, so \[ E[e^{r(T)}] \geq e^{E[r(T)]} = e^{T\mu} \] The exact expected simple gross return is \( e^{T\mu + T\sigma^2/2} \). The **\( \sigma^2/2 \) correction** reflects the convexity premium — higher volatility raises the expected price level, even with the same log drift \( \mu \). This gap between \( E[\log P_T] \) and \( \log E[P_T] \) is a fundamental lognormal property.

---

## Card 53

**Q:** How do you read an ACF plot? Describe the expected ACF shape for an IID process, AR(1) with small and large \( \lambda \), and MA(1).

**A:** The **ACF (autocorrelation function)** plot shows the sample autocorrelation \( \hat{\rho}_k = \hat{\gamma}_k / \hat{\gamma}_0 \) at each lag \( k \). Blue confidence bands at \( \pm 2/\sqrt{T} \) show the 95% critical region under the null of zero autocorrelation. **AR(1) with \( \lambda = 0.4 \)**: spike at lag 1, quickly decays within bands. **AR(1) with \( \lambda = 0.8 \)**: strong lag-1 spike, slow alternating decay over many lags. **IID**: all lags within bands. **MA(1)**: single spike at lag 1, all higher lags exactly zero (in population).

---

## Card 54

**Q:** Explain the R logic for generating a binomial random walk using `sign(p - z)`, and the full pipeline for a lognormal price simulation using `rnorm`, `cumsum`, and `exp`.

**A:** In R, to simulate a binomial (±1) random walk: `z <- matrix(runif(Nt*Np), nrow=Nt)` generates uniform draws; `x <- sign(p - z)` converts to +1 with probability \( p \) and −1 with probability \( 1-p \) (since \( p - z > 0 \) with probability \( p \)). Then accumulate: `s[t+1,] <- s[t,] + x[t,]`. For lognormal price paths: draw `r <- matrix(rnorm(Nt*Np, mean=mu*dt, sd=sigma*sqrt(dt)), nrow=Nt)`, accumulate with `cumsum`, then exponentiate: `P <- exp(s)`. The `apply(r, 2, cumsum)` call applies cumsum column-wise across all simulated paths at once.

---

## Card 55

**Q:** How is the p-value computed for the variance ratio test statistic \( z(q) \), and what is the correct interpretation of a small p-value? What does it not measure?

**A:** The **p-value** of a test statistic \( z(q) \) is the probability of observing a value at least as extreme as the computed statistic under \( H_0 \) (random walk). In R: `2 * pnorm(-abs(zstats))` (two-sided). **Interpretation**: small p-value (e.g., \( p < 0.05 \)) → reject random walk at 5% significance. A statistic marked with an asterisk in Lo-MacKinlay's tables indicates rejection at the 5% level. The p-value does *not* measure the size of the departure from random walk — only whether it is statistically distinguishable from zero given the sample size.

---

## Card 56

**Q:** Why do variance ratio estimates become less reliable for larger aggregation windows \( q \)? How does this affect test strategy?

**A:** Longer base periods use fewer non-overlapping observations: \( n = T/q \) windows for \( q \)-period returns. As \( q \) increases, \( n \) decreases → more sampling noise in the variance estimate → wider confidence intervals for \( VR(q) \). The **overlapping estimator** partially mitigates this but the effective sample size still decreases. **Practical implication**: test results for large \( q \) (e.g., \( q = 16 \)) are less reliable than for small \( q \) (e.g., \( q = 2 \)). This is why researchers test multiple values of \( q \) and look for consistent patterns.

---

## Card 57

**Q:** Compare the histogram shape of log returns vs simple returns under the lognormal model. What departures from the model are typically observed in real financial data?

**A:** **Histogram of \( r = \log(P_t/P_{t-1}) \)** (log returns): Should look bell-shaped and approximately normal under the lognormal model. In practice, financial returns show **fat tails** (leptokurtosis) and sometimes slight negative skew — more extreme events than Gaussian predicts. **Histogram of \( R = P_T/P_0 - 1 \)** (simple return): Right-skewed (lognormal shape), mean > median, lower bound above −1. The log-return histogram is a direct test of the normality assumption; the simple return histogram illustrates the skewness inherent in compounding.

---

## Card 58

**Q:** What is the modeling rationale for combining AR and MA components in an ARMA(p,q) model? When would a pure AR or pure MA be insufficient?

**A:** **ARMA(p,q) purpose**: combines AR (captures persistence / autocorrelation) and MA (captures transient shock propagation) in a parsimonious model. AR alone: needs many lags to fit processes with persistent but fast-decaying autocorrelation. MA alone: limited to \( q \)-period memory. Together: ARMA(1,1) can approximate processes that would require high-order AR or MA alone. **Identification**: AR lag order \( p \) and MA lag order \( q \) chosen by comparing AIC/BIC across candidate models. AR dominates for slowly decaying ACF; MA dominates for sharp ACF cutoff.

---

## Card 59

**Q:** State the stationarity condition for AR(1) and explain what happens at \( |\lambda| = 1 \) and \( |\lambda| > 1 \). How does this generalise to AR(p)?

**A:** **Stationarity condition for AR(1)**: \( |\lambda| < 1 \) (equivalently \( |c_1| < 1 \)). If \( |\lambda| = 1 \): random walk (non-stationary, variance grows without bound). If \( |\lambda| > 1 \): explosive process (variance diverges, prices go to infinity or zero). For **AR(p)**, stationarity requires all roots of the characteristic polynomial \( 1 - c_1 z - c_2 z^2 - \cdots - c_p z^p = 0 \) to lie **outside the unit circle**. Stationarity is required for the unconditional variance \( \gamma_0 = \sigma^2 / (1 - \lambda^2) \) to be finite.

---

## Card 60

**Q:** Describe volatility clustering. How is it captured by GARCH, and at which level of the RW hierarchy (RW1/2/3) does it represent a violation?

**A:** **Volatility clustering** (GARCH-type behaviour): large returns (in absolute value) tend to be followed by large returns — "quiet periods" and "turbulent periods" cluster together. This means \( E[\epsilon_t^2 \epsilon_{t-1}^2] > (E[\epsilon_t^2])^2 \) — squared returns are positively autocorrelated. **GARCH(1,1) model**: \( \sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2 \). This violates RW2 (non-identical distributions) and RW1, but can satisfy RW3 (uncorrelated levels). The return series passes linear autocorrelation tests but the **squared** return series does not.

---

## Card 61

**Q:** Formula: How do you compute annualized volatility from \( n \)-day observations to produce a flat plot if the random walk holds? What does non-flatness indicate?

**A:** The **standard deviation (volatility) scaling rule**: if variance scales as \( \text{Var}(r^{(n)}) = n \cdot \sigma_1^2 \), then the annualized volatility from \( n \)-day returns is: \[ \hat{\sigma}_{\text{annual}}(n) = \sqrt{252/n} \cdot \text{sd}(r^{(n)}) \] Under the random walk this should be **constant** across all \( n \). In R: `sigma[n] <- sqrt(252/n) * sd(diff(log(P[seq(from=n, to=N, by=n)])))`. A barplot of \( \hat{\sigma}(n) \) vs \( n \) that is flat (within noise) is visual evidence for the square-root-of-time rule. Systematic slope or curvature suggests long-range dependence or mean reversion.

---

## Card 62

**Q:** Pitfall: In a lognormal model with positive drift, why might most individual price paths end up below the expected (mean) price at time \( T \)?

**A:** **Pitfall: Confusing drift direction with variance growth.** In a generalized random walk with \( \mu > 0 \), the price *drifts upward on average* but individual paths can fall arbitrarily (variance also grows as \( T\sigma^2 \)). The majority of paths may lie *below* the mean path (since the distribution of \( P_T \) is right-skewed: mean > median). **Corollary**: the median path is \( P_0 e^{T\mu} \) (using log-return mean directly), while the mean path is \( P_0 e^{T(\mu + \sigma^2/2)} \). Investors experiencing median outcomes see lower returns than the ensemble mean suggests.

---

## Card 63

**Q:** State the two mathematical conditions for weak (covariance) stationarity and explain why satisfying them is important for statistical estimation.

**A:** A **time series** is said to be **covariance stationary** (weakly stationary) if: \[ E[R_t] = \mu \text{ (constant, independent of } t) \] \[ \text{Cov}(R_t, R_{t-k}) = \gamma_k \text{ (depends only on lag } k, \text{ not on } t) \] This is sufficient to use the method of moments for parameter estimation and to derive the Yule-Walker equations for AR models. **Why it matters**: stationarity guarantees that estimators computed from a finite sample converge to population parameters as \( T \to \infty \) (ergodicity).

---

## Card 64

**Q:** Explain the matrix data structure used in Monte Carlo path simulation in R. Why is the vectorised approach computationally efficient?

**A:** When simulating \( N_p \) paths simultaneously in R, the `matrix` structure stores results as an \( (N_t + 1) \times N_p \) array where: each **column** is one simulated path, each **row** is a time step. Operations like `s[t+1,] <- s[t,] + x[t,]` update *all* paths at once using vectorisation — no inner loop over paths needed. `matplot(s[,1:3], type="l")` plots the first 3 paths. This vectorised approach is key to computational efficiency: generating 10,000 paths takes almost the same time as generating 1 path in R.

---

## Card 65

**Q:** Summarise Samuelson's (1965) argument for why "properly anticipated prices fluctuate randomly." What is the economic mechanism?

**A:** **Samuelson's proof (1965)** in one sentence: if a price fully reflects all available information at every point in time (i.e., prices satisfy an equilibrium condition), then price *changes* must be unforecastable — i.e., they must fluctuate randomly. **Logic**: if a future price change were predictable, rational traders would already have exploited it, moving the current price until the predictable profit is eliminated. Therefore any "properly anticipated" price series must appear to be a martingale (a process with no predictable increments), which is equivalent to the random walk under constant discount rates.

---

## Card 66

**Q:** Reference card: List all major formulas from Module 2 in one place (random walk, generalized RW, lognormal, AR(1) moments, variance ratio test).

**A:** **Summary of all major formulas in Module 2:** | Model | Key Formula | | Random walk | \( S_T = \sum z_t \), \( E[S_T]=0 \), \( \text{Var}(S_T)=T \) | | Generalized RW | \( r_t = \mu + \sigma z_t \), \( E[X_T]=T\mu \), \( \text{Var}(X_T)=T\sigma^2 \) | | Lognormal | \( r(T)\sim N(T\mu,T\sigma^2) \), \( E[R]=e^{\mu+\sigma^2/2}-1 \) | | AR(1) mean | \( \bar{R} = c_0/(1-c_1) \) | | AR(1) variance | \( \gamma_0 = \sigma^2/(1-\lambda^2) \) | | AR(1) autocovariance | \( \gamma_k = (-\lambda)^k \gamma_0 \) | | Variance ratio | \( VR(q) = \hat{\sigma}_c^2(q)/\hat{\sigma}_a^2 \approx 1 \) under \( H_0 \) | | VR test stat | \( z(q) = \sqrt{nq}(VR-1)\sqrt{3q/[2(2q-1)(q-1)]} \sim N(0,1) \) |

---

## Card 67

**Q:** What is the Markov property, and does the random walk satisfy it? Contrast with path-dependent processes.

**A:** The **Markov property**: the future distribution of \( S_t \) depends only on the present state \( S_{t-1} \), not the full history. The random walk satisfies this because increments are IID — past path is irrelevant once you know the current position. **Path dependence**: a process where outcomes depend on the entire history (e.g., Asian options, certain credit models). The random walk has *no* path dependence; AR(p) has *bounded* path dependence (depth \( p \)); ARMA extends this with MA lags on innovations.

---

## Card 68

**Q:** Formula: Conditional (forecasting) expectation for AR(1) — one-step and \( k \)-steps ahead. What is the long-run forecast?

**A:** For AR(1) with current state \( R_{t-1} = r \) known: \[ E[R_t \mid R_{t-1} = r] = \mu - \lambda(r - \mu) + 0 = \mu(1 + \lambda) - \lambda r \] One step ahead: \( E[R_t \mid R_{t-1}] = \mu + (1-\lambda)(r - \mu) \cdot \ldots \) More cleanly, using the deviation form: \[ E[R_t - \mu \mid R_{t-1} = r] = -\lambda(r - \mu) \] \( k \)-steps ahead: \[ E[R_{t+k} - \mu \mid R_t = r] = (-\lambda)^k (r - \mu) \] The forecast reverts to \( \mu \) geometrically; for \( |\lambda| < 1 \) it converges as \( k \to \infty \).

---

## Card 69

**Q:** Is weak stationarity equivalent to strong stationarity? Give counterexamples in each direction.

**A:** A process that is weakly stationary need **not** be strongly stationary, and vice versa. **Example where weak ≠ strong**: a process with time-varying higher moments (skewness) but constant mean and variance is weakly stationary but not strongly stationary. **Example where strong ≠ weak**: an IID process with infinite variance (e.g., Cauchy distribution) is strongly stationary but not weakly stationary (second moments don't exist). In practice, weak stationarity is sufficient for most time series tools (ARMA, autocorrelation analysis).

---

## Card 70

**Q:** Formula: Define the autocorrelation function (ACF) \( \rho_k \) and describe how to interpret an ACF plot in R, including the confidence bands.

**A:** **Autocorrelation function (ACF)** at lag \( k \): \[ \rho_k = \frac{\gamma_k}{\gamma_0} \] the correlation (not just covariance) between \( R_t \) and \( R_{t-k} \). For AR(1): \( \rho_k = (-\lambda)^k \), decaying geometrically. For random walk increments: \( \rho_k = 0 \) for all \( k > 0 \). The `acf()` function in R computes sample autocorrelations and plots them with confidence bands (blue dashed lines) at \( \pm 1.96/\sqrt{T} \) — spikes outside these bands signal statistically significant autocorrelation.

---

## Card 71

**Q:** Compare the ACF patterns for AR(1) with \( \lambda = 0.4 \) vs \( \lambda = 0.8 \). What does the sign pattern reveal about mean reversion?

**A:** For AR(1) with \( \lambda = 0.4 \): ACF at lag 1 ≈ \(-0.4\), decaying quickly — small, short-lived autocorrelations, barely visible. For \( \lambda = 0.8 \): ACF at lag 1 ≈ \(-0.8\), decaying slowly — strong, persistent alternating autocorrelations visible for many lags. **Pattern**: alternating signs (positive-negative-positive…) because coefficient is negative (mean-reverting). High \( \lambda \) → slowly decaying ACF → strong memory → easy to detect with statistical tests. Low \( \lambda \) → fast decay → weak memory → hard to distinguish from random walk in finite samples.

---

## Card 72

**Q:** Formula: Full autocovariance structure of MA(1) — compute \( \gamma_0 \), \( \gamma_1 \), \( \gamma_k \). What is the signature pattern in the ACF?

**A:** MA(1) autocovariance structure: \[ \gamma_0 = (1 + \theta^2)\sigma^2, \quad \gamma_1 = \theta\sigma^2, \quad \gamma_k = 0 \text{ for } k \geq 2 \] The ACF **cuts off sharply** after lag 1 — this is the signature of an MA process. Contrast with AR(1) where the ACF decays geometrically and never reaches exactly zero. **Intuition**: the current value \( r_t = \mu + \sigma z_t + \theta z_{t-1} \) shares the innovation \( z_{t-1} \) with \( r_{t-1} \) only, creating exactly one lag of memory and no further dependence.

---

## Card 73

**Q:** State the linearity of expectation and the condition needed for variance of a sum to equal the sum of variances. Are independence and zero covariance equivalent?

**A:** **Linearity of expectation**: for any constants \( a, b \) and random variables \( X, Y \): \[ E[aX + bY] = aE[X] + bE[Y] \] regardless of dependence between \( X \) and \( Y \). This is the **only** tool needed to compute means of sums. **For variances**, independence (not just zero correlation) is needed to get \( \text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) \). Zero covariance (uncorrelated) is sufficient for variance additivity: \[ \text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X,Y) \] Covariance = 0 → variance additive.

---

## Card 74

**Q:** How are \( \mu \) and \( \sigma \) estimated from a daily return series and annualized? What estimation principle do these formulas use?

**A:** **Calibration**: fitting model parameters \( (\mu, \sigma) \) to match observed data moments. Standard estimates from a return series \( \{r_1, \ldots, r_T\} \): \[ \hat{\mu} = \frac{1}{T}\sum_{t=1}^T r_t \quad \text{(sample mean)} \] \[ \hat{\sigma}^2 = \frac{1}{T}\sum_{t=1}^T (r_t - \hat{\mu})^2 \quad \text{(or divide by } T-1 \text{)} \] Then annualize: \( \hat{\mu}_{\text{ann}} = 252\hat{\mu} \), \( \hat{\sigma}_{\text{ann}} = \sqrt{252}\hat{\sigma} \). These are **moment estimators** (method of moments). Under IID normality they are also the MLE estimates.

---

## Card 75

**Q:** How does Monte Carlo sampling error scale with the number of paths, and how did the Tootsie Roll / lognormal simulation validate the theoretical moment formulas?

**A:** Under the Law of Large Numbers, the sample mean converges to the true mean as \( T \to \infty \). For Monte Carlo: with \( N_p \) simulation paths, the sampling error in any estimated statistic shrinks as \( 1/\sqrt{N_p} \). To halve the error, **quadruple** the number of paths. The simulation of the lognormal process confirmed: \[ \hat{E}[R] = 0.1548 \approx e^{\mu + \sigma^2/2} - 1 = 0.1560 \] \[ \hat{\text{sd}}(R) = 0.3564 \approx \sqrt{e^{2\mu+\sigma^2}(e^{\sigma^2}-1)} = 0.3548 \] Close agreement validates both the simulation code and the theoretical formulas.

---

## Card 76

**Q:** State the three forms of the Efficient Market Hypothesis. Which form does the random walk test directly address?

**A:** The **Efficient Market Hypothesis (EMH)** has three forms: **Weak form**: prices reflect all *past price* information — technical analysis cannot generate excess returns. Directly implies random walk for prices. **Semi-strong form**: prices reflect all *publicly available* information — fundamental analysis cannot generate excess returns. **Strong form**: prices reflect *all* information including private (insider) information. The random walk test is a direct test of the weak form. Fama (1965) and Samuelson (1965) provided the theoretical foundation; Lo-MacKinlay (1988) found empirical evidence against weak-form efficiency for small stocks.

---

## Card 77

**Q:** Why is 252 used to annualize daily return statistics, and what is the correct formula for annualizing the mean vs the standard deviation?

**A:** 252 is the conventional number of **trading days per year** in US equity markets (approx. 365 calendar days minus weekends and ~10 holidays). It is the scaling constant for annualizing daily statistics: \[ \sigma_{\text{annual}} = \sigma_{\text{daily}} \times \sqrt{252}, \quad \mu_{\text{annual}} = \mu_{\text{daily}} \times 252 \] Note: some practitioners use 250 or 260. The square root rule for volatility arises from variance scaling: \( \text{Var}(X_T) = T\sigma^2 \), so \( \text{sd}(X_T) = \sigma\sqrt{T} \). **Never** scale volatility linearly by 252.

---

## Card 78

**Q:** Formula: How is the p-value computed from the variance ratio z-statistic? What do small and large p-values mean — and what do they NOT mean?

**A:** A p-value is the probability of observing a test statistic as extreme as the one measured, under the null hypothesis. In the variance ratio context: \[ \text{p-value} = 2 \times P(Z > |z(q)|), \quad Z \sim N(0,1) \] In R: `2*pnorm(-abs(zstats))`. Convention: p-value \( < 0.05 \) → reject at 5% significance level. **Important**: a small p-value says the data are inconsistent with the random walk, not that you have a better model. A large p-value does **not** prove the random walk holds — only that the test lacks power to reject it with available data.

---

## Card 79

**Q:** Define volatility clustering. How does it relate to the RW1/RW2/RW3 taxonomy? How can it be detected empirically?

**A:** **Volatility clustering**: periods of high volatility tend to follow periods of high volatility, and low follows low. This is a violation of RW1 (identical distributions) but consistent with RW3 (uncorrelated but dependent). Formally: \( E[\epsilon_t^2 \epsilon_{t-k}^2] \neq E[\epsilon_t^2]E[\epsilon_{t-k}^2] \) for small \( k \). The ACF of squared returns (not raw returns) shows significant positive autocorrelation. GARCH models capture this by making \( \sigma_t^2 \) a function of past squared residuals. **Implication for options**: volatility is predictable even if returns are not.

---

## Card 80

**Q:** What are the shapes of the distributions of \( P_T \) (price) vs \( \log(P_T/P_0) \) (log return) under lognormal dynamics? How does skewness appear in the sorted barplot?

**A:** The distribution of \( P_T \) is **lognormal** (right-skewed, bounded below at 0). The distribution of \( \log P_T / P_0 = r(T) \) is **normal** (symmetric, unbounded). **Key shape difference**: the lognormal has a longer right tail and compressed left tail compared to a normal with the same mean. As \( \sigma \) increases, the lognormal becomes more skewed. Most \( P_T \) values cluster below the mean (median \( < \) mean). The sorted barplot in simulation shows most paths ending below their mean outcome — a few outlier paths drag the mean far above the typical outcome.

---

## Card 81

**Q:** Why is the variance ratio test applied for multiple values of \( q \), and what statistical complication does this create?

**A:** The **test statistic \( z(q) \) varies with \( q \)** — no single \( q \) captures all deviations. If autocorrelation is at lag 3, \( z(2) \) may miss it while \( z(4) \) detects it. Lo-MacKinlay present results for \( q = 2, 4, 8, 16 \) to show robustness. Using **multiple \( q \)** values and requiring consistent rejection strengthens the evidence. However, testing multiple \( q \) simultaneously inflates the type I error (multiple testing problem). Practical solution: report all \( q \) tested, assess the overall pattern, and apply Bonferroni or similar corrections if needed.

---

## Card 82

**Q:** What practical constraint limits the non-overlapping variance estimator for large \( q \), and how does the overlapping estimator solve this?

**A:** With \( T = nq + 1 \) observations, **non-overlapping** windows: only \( n \) independent \( q \)-period returns available. For large \( q \), \( n \) becomes small, reducing precision. **Practical limitation**: for \( T = 252 \) and \( q = 50 \), only \( n \approx 5 \) non-overlapping windows — far too few for statistical inference. The overlapping estimator avoids this by using all \( T - q \) possible windows of length \( q \), but these windows are not independent. The overlapping estimator corrects for this dependence in the asymptotic variance formula used to construct \( z(q) \).

---

## Card 83

**Q:** Pitfall: What errors arise from confusing log returns \( r_t = \log(P_t/P_{t-1}) \) with simple returns \( R_t = P_t/P_{t-1} - 1 \) in a random walk model?

**A:** **Pitfall: confusing log return \( r_t \) with simple return \( R_t \)**. They are related by \( R_t = e^{r_t} - 1 \approx r_t \) for small values, but diverge significantly over long horizons or with large moves. The random walk model is stated in log returns (additive, Gaussian). If you mistakenly apply it to simple returns, you get: (a) inconsistent aggregation (multi-period compounding is nonlinear), (b) incorrect variance formulas, (c) possible negative prices in simulation. Always specify whether \( r_t \) or \( R_t \) is being modelled.

---

## Card 84

**Q:** What is the "fat tails" problem with the Gaussian random walk model for financial returns? How does it show up in QQ plots and historical data?

**A:** **Thin-tailed (platykurtic)** vs **fat-tailed (leptokurtic)**: financial return distributions empirically exhibit excess kurtosis (fatter tails than Gaussian). The Gaussian random walk model **underestimates** the probability of extreme moves. Evidence: (1) QQ plots of returns curve above the normal reference line in both tails. (2) Historical market crashes (1987, 2008) had probability \( < 10^{-10} \) under the Gaussian model. The lognormal model preserves Gaussian log returns — so it inherits this fat-tail problem. GARCH and jump-diffusion models are partial remedies.

---

## Card 85

**Q:** How does the discrete-time random walk relate to continuous-time Brownian motion as \( dt \to 0 \)?

**A:** The random walk is the **discrete-time analogue** of Brownian motion (Wiener process). As the time step \( dt \to 0 \): \[ \Delta S = \mu \, dt + \sigma \, \epsilon\sqrt{dt}, \quad \epsilon \sim N(0,1) \] becomes the continuous-time SDE: \[ dS = \mu \, dt + \sigma \, dW \] where \( W_t \) is a Wiener process. The variance scaling property \( \text{Var}(S_T) = T\sigma^2 \) in discrete time maps to \( \text{Var}(W_T) = T \) in continuous time. This connection motivates why the random walk is the foundational building block for continuous-time finance (Black-Scholes etc.).

---

## Card 86

**Q:** What is the heteroscedasticity-robust version of the variance ratio test, and why is it needed for RW3 processes?

**A:** A **heteroscedasticity-robust** variance ratio test (Lo-MacKinlay's \( z^*(q) \)) replaces the constant-variance assumption with a non-parametric estimate of the asymptotic variance that is valid under RW3 (uncorrelated but dependent increments, including time-varying volatility). This uses a weighted sum of sample autocovariances: \[ \hat{\delta}(j) = \frac{\sum_{t=j+1}^{T} (r_t - \hat{\mu})^2(r_{t-j} - \hat{\mu})^2}{\left[\sum_{t=1}^T (r_t - \hat{\mu})^2\right]^2} \] The robust test does not assume constant volatility, making it valid even in the presence of GARCH-type effects.

---

## Card 87

**Q:** Carry out the full algebraic expansion proving \( \text{Var}(S_T) = T \) for the elementary random walk. Count the diagonal and cross-terms explicitly.

**A:** Step-by-step expansion of \( \text{Var}(S_T) \): \[ \text{Var}(S_T) = E\left[\left(\sum_{t=1}^T z_t\right)^2\right] = E\left[\sum_{t=1}^T z_t^2 + 2\sum_{t < t'} z_t z_{t'}\right] \] \[ = \sum_{t=1}^T E[z_t^2] + 2\sum_{t < t'} E[z_t z_{t'}] = \sum_{t=1}^T 1 + 2\sum_{t < t'} 0 = T \] The first sum has \( T \) terms each equal to 1 (unit variance). The second sum has \( \binom{T}{2} \) cross-terms each equal to 0 (independence). Therefore \( \text{Var}(S_T) = T \). This computation uses only linearity of \( E \) and the two moment conditions on \( z_t \).

---

## Card 88

**Q:** Why is the random walk described as a "building block" for quantitative finance? List five contexts where it appears as a foundation.

**A:** The random walk model is **not just** a building block but a benchmark: (1) **Theoretical baseline**: if we can't beat a random walk forecast, there is no predictive value in more complex models. (2) **Building block**: AR, MA, ARMA, GARCH all reduce to the random walk when their extra parameters are zero. (3) **Option pricing**: Black-Scholes assumes log prices follow a random walk (geometric Brownian motion). (4) **Risk management**: VaR calculations often assume random walk dynamics. (5) **Portfolio theory**: Markowitz mean-variance optimisation implicitly uses random walk moment structure.

---

## Card 89

**Q:** Explain the R code `S <- exp(apply(r, 2, cumsum))` step by step. What does each function do, and what does the output represent?

**A:** In R: `S <- exp(apply(r, 2, cumsum))` where `r` is an \( N_t \times N_p \) matrix of log returns. **Step by step**: (1) `apply(r, 2, cumsum)` applies `cumsum` (cumulative sum) to each *column* (path), producing a matrix of cumulative log returns \( X_t = \sum_{s=1}^t r_s \). (2) `exp(...)` converts to price levels \( P_t = e^{X_t} \) (assuming \( P_0 = 1 \)). This vectorised approach simulates all \( N_p \) paths simultaneously without an explicit loop, making it fast. The resulting matrix has rows = time steps, columns = paths.

---

## Card 90

**Q:** Why is the random walk level \( S_T \) non-stationary, while the AR(1) process (with \( |\lambda| < 1 \)) is stationary? What practical implication does this have for empirical analysis?

**A:** The random walk has **no memory** — its variance grows without bound as \( T \to \infty \). This makes it **non-stationary**: \( \text{Var}(S_T) = T\sigma^2 \to \infty \). The AR(1) process has **finite unconditional variance** \( \gamma_0 = \sigma^2/(1-\lambda^2) \) because mean reversion acts as a restoring force, keeping the process near \( \mu \). **Key implication**: you cannot apply the standard stationarity-based tools (autocovariance analysis, variance ratio test in log-price space) to a random walk level \( S_T \) directly — you must work in return (increment) space where the process *is* stationary.

---

## Card 91

**Q:** Compare the cumulative income and stock price time series models as applications of the random walk. What mathematical difference determines whether to sum additively or multiplicatively?

**A:** **Cumulative income model**: \( I_1 + I_2 + I_3 + \cdots \) — each period's income is an increment (IID or structured). **Stock price model**: \( P_t = P_0 e^{r_1 + r_2 + \cdots + r_t} \) — log price is a random walk; the cumulative sum of log returns determines the price level. Both share the recursive structure \( S_t = S_{t-1} + x_t \). The difference is that income is *additive* (the level is the quantity of interest), while price is *multiplicative* (the log is the quantity of interest for applying random walk properties).

---

## Card 92

**Q:** Explain Samuelson's theorem "properly anticipated prices fluctuate randomly." What is the logical chain from market efficiency to the random walk?

**A:** "Properly anticipated prices fluctuate randomly" (Samuelson, 1965): In a competitive market, if all information is known and incorporated, any *predictable* price movement would already be acted upon, pushing the price to the level where the expected return equals the required return. Only *unpredictable* (random) shocks — new information — can move prices. Therefore: **if markets are efficient, prices must follow a random walk**. Equivalently, if prices do *not* follow a random walk, there exists predictable, exploitable information — a potential violation of efficiency.

---

## Card 93

**Q:** How is Monte Carlo simulation used as a "testbed" for financial statistics algorithms? What properties of an estimator can be evaluated this way?

**A:** Simulation is a **testbed for algorithms designed for real-world data**: (1) Run your statistical estimator on simulated data from a *known* process. (2) Check whether the estimator recovers the true parameters. (3) Check whether hypothesis tests have correct size (rejection rate ≈ 5% when null is true). (4) Estimate statistical power (rejection rate when null is false — e.g., true process is AR(1)). This is called **Monte Carlo evaluation of estimator performance** — widely used in econometrics to validate methods before applying to real data where the true DGP is unknown.

---

## Card 94

**Q:** Pitfall: Why does statistical rejection of the random walk NOT imply tradeable excess profits?

**A:** **Pitfall: equating random walk rejection with trading profitability.** Even if the random walk is rejected (VR ≠ 1), it does not follow that excess profits are achievable, because: (1) Transaction costs may exceed any predictable edge. (2) The anomaly may be too small to exploit at scale. (3) Risk adjustments may eliminate the excess return. (4) The effect may disappear once known (Samuelson's reflexivity). Lo-MacKinlay explicitly note this: their findings relate to statistical predictability, not to tradeable strategies or market efficiency in the economic sense.

---

## Card 95

**Q:** Describe the two diagnostic plots used to assess variance scaling in the random walk model (variance vs \( n \) and volatility/\(\sqrt{n}\) vs \( n \)). What do deviations from the expected shape indicate?

**A:** **Variance scaling plot** (slide 48): plots \( \hat{\sigma}^2(n) \) vs \( n \), where \( \hat{\sigma}^2(n) \) is the variance of \( n \)-day returns. Under random walk, should be **linear through origin** with slope \( \sigma^2 \). Curvature upward (superlinear) → positive autocorrelation at short lags; curvature downward → mean reversion. **Volatility scaling plot** (slide 55): plots \( \hat{\sigma}(n)/\sqrt{n} \) vs \( n \) — should be **constant** if model holds. A flat line confirms square-root time scaling. Systematic variation (e.g., humped shape) signals departures such as microstructure effects at short lags or long-range dependence at long lags.

---

## Card 96

**Q:** What are the financial interpretations of the parameters \( \mu \) and \( \sigma \) in the generalized random walk? How do they combine in the Sharpe ratio?

**A:** In the generalized random walk, \( \sigma \) and \( \mu \) have specific financial interpretations: **\( \sigma \) (volatility)**: measures risk — the magnitude of unpredictable fluctuations per unit time. Higher \( \sigma \) → wider distribution of outcomes → more uncertainty. **\( \mu \) (drift)**: measures expected return — the systematic, predictable component per unit time. Positive \( \mu \) → upward drift in expected log price. The **Sharpe ratio** \( = \mu/\sigma \) captures return per unit of risk, normalising both parameters into a single risk-adjusted performance measure.

---

## Card 97

**Q:** Define "innovation" formally in the context of a time series. How does it differ from the noise term \( z_t \), and how does it propagate in ARMA models?

**A:** An **innovation** is the component of new information arriving at time \( t \) that was *not* predictable from the past: \( \epsilon_t = r_t - E[r_t \mid \mathcal{F}_{t-1}] \). For IID random walk: \( \epsilon_t = r_t - \mu = \sigma z_t \). For AR(1): \( \epsilon_t = R_t - E[R_t \mid R_{t-1}] = \sigma z_t \). The innovation is always **mean zero**, **serially uncorrelated**, and represents the "surprise" or new information content of the observation. It propagates through linear filters (MA terms) to affect future values in MA/ARMA models.

---

## Card 98

**Q:** State the three moment conditions for the generalized random walk return \( r_t = \mu + \sigma z_t \) and prove each from the standard properties of \( z_t \).

**A:** \( E[r_t] = \mu \), \( E[(r_t - \mu)^2] = \sigma^2 \), \( E[(r_t - \mu)(r_{t'} - \mu)] = 0 \) for \( t \neq t' \). These three conditions fully characterise the second-order structure of IID returns. **Proof sketch**: mean follows from \( E[\mu + \sigma z_t] = \mu + \sigma \cdot 0 = \mu \). Variance: \( E[(\sigma z_t)^2] = \sigma^2 E[z_t^2] = \sigma^2 \cdot 1 = \sigma^2 \). Covariance: \( E[\sigma z_t \cdot \sigma z_{t'}] = \sigma^2 E[z_t z_{t'}] = \sigma^2 \cdot 0 = 0 \). All three follow directly from the linearity of \( E \) and the standard properties of \( z_t \).

---

## Card 99

**Q:** Coverage map: List all major topics in Week 2 of MITx 15.455x and confirm which are covered in the m02-master flashcard set.

**A:** **Completeness check across Week 2 topics**: ✅ Random walk (elementary, generalized, variance proof, universality) ✅ Linear time series (MA, AR, ARMA, GARCH) ✅ Stationarity (strong vs weak, AR(1) solution) ✅ AR(1) mean, variance, autocovariance derivations ✅ Lognormal model (log returns, P_T, E[R], Var(R)) ✅ Annualization and time scaling ✅ Monte Carlo (procedure, validation, limitations) ✅ RW1/RW2/RW3 taxonomy ✅ Variance ratio test (VR formula, estimators, z-stat, p-value) ✅ Lo-MacKinlay empirical findings ✅ Market efficiency (EMH, Fama, Samuelson) ✅ Volatility clustering, fat tails ✅ ACF, QQ plots, diagnostic tools ✅ R implementation details

---
