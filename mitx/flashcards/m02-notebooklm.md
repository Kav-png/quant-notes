# Stochastic Flashcards

## Card 1

**Q:** Term: Stochastic Process

**A:** Definition: A time-dependent random variable that can be observed in continuous time as $S(t)$ or discrete time as $S_1, S_2, \dots, S_t$. Example: The daily closing price of a stock over a calendar year.

---

## Card 2

**Q:** In a discrete-time stochastic process, how are the variable levels $S_t$ constructed from increments $x_t$?

**A:** They are constructed by adding increments recursively: $S_t = S_{t-1} + x_t = x_0 + x_1 + \dots + x_t$.

---

## Card 3

**Q:** Formula: Increment recovery through differencing

**A:** $x_t = S_t - S_{t-1}$, where $x_t$ is the increment and $S_t$ is the value of the process at time $t$.

---

## Card 4

**Q:** What three characteristics define the sampling of a standard time series model?

**A:** Uniform intervals (integer indices), equal spacing (e.g. business days), and a time zero origin.

---

## Card 5

**Q:** Term: Innovation

**A:** Definition: The random component or shock added to a process in a recursive definition to determine the next value. Example: The $\sigma z_t$ term in a generalized random walk.

---

## Card 6

**Q:** What is the simplest form of a time-series model?

**A:** The random walk model.

---

## Card 7

**Q:** What does it mean for increments in a random walk to be 'IID'?

**A:** It means the increments are Independent and Identically Distributed.

---

## Card 8

**Q:** Does a simple random walk have a dependence on past history?

**A:** No, it has no dependence on past history as each increment is independent.

---

## Card 9

**Q:** List the three properties of a 'standard' random variable $z_t$ used in random walks.

**A:** Mean is 0 ($E[z_t] = 0$), variance is 1 ($E[z_t^2] = 1$), and correlation is 0 for different times ($E[z_t z_{t'}] = 0$ if $t \neq t'$).

---

## Card 10

**Q:** Formula: Gaussian random variable probability distribution

**A:** $p(z_t) = \frac{1}{\sqrt{2\pi}} e^{-z_t^2/2}$, representing a standard normal distribution $N(0,1)$.

---

## Card 11

**Q:** How does the variance of a $T$-step random walk scale with time?

**A:** The variance grows linearly with the number of steps $T$.

---

## Card 12

**Q:** How does the standard deviation of a $T$-step random walk scale with time?

**A:** The standard deviation grows as the square root of time, or $\sqrt{T}$.

---

## Card 13

**Q:** What is the key insight behind the linear growth of variance in a sum of independent random variables?

**A:** Because the increments are uncorrelated, the expectation of all cross-terms $E[z_t z_{t'}]$ is zero, leaving only the sum of individual variances.

---

## Card 14

**Q:** Term: Generalized Random Walk

**A:** Definition: A model where the standard random variable is scaled by a volatility parameter and offset by a constant mean return. Example: Modelling stock returns as $r_t = \sigma z_t + \mu$.

---

## Card 15

**Q:** In the generalized random walk model $r_t = \sigma z_t + \mu$, what do the parameters $\sigma$ and $\mu$ represent?

**A:** $\sigma$ represents the risk (volatility) and $\mu$ represents the return (mean).

---

## Card 16

**Q:** Formula: Mean of a $T$-step generalized random walk $X_T$

**A:** $E[X_T] = T\mu$, where $T$ is the number of time steps and $\mu$ is the mean of each individual step.

---

## Card 17

**Q:** Formula: Variance of a $T$-step generalized random walk $X_T$

**A:** $Var(X_T) = T\sigma^2$, where $T$ is the number of time steps and $\sigma^2$ is the variance of each individual step.

---

## Card 18

**Q:** Term: MA(1) Model

**A:** Definition: A first-order moving average model where the current value depends on the current shock and the immediately preceding shock. Example: $r_t = \mu + \sigma z_t + \phi z_{t-1}$.

---

## Card 19

**Q:** How does an MA(1) model differ from an IID process regarding temporal correlation?

**A:** The MA(1) model is not IID because the term $\phi z_{t-1}$ introduces a correlation with the previous period's random shock.

---

## Card 20

**Q:** Term: GARCH Model

**A:** Definition: A model where the distribution of the random variable (specifically the variance) is itself time-varying. Example: Modelling market returns where volatility 'clusters' during certain periods.

---

## Card 21

**Q:** Term: AR(p) Model

**A:** Definition: An autoregressive model of order $p$ where the current value is a linear combination of its $p$ past values plus a random shock. Example: $R_t = c_0 + c_1 R_{t-1} + \dots + c_p R_{t-p} + \sigma z_t$.

---

## Card 22

**Q:** Term: ARMA(p, q) Model

**A:** Definition: A model that combines autoregressive (AR) and moving average (MA) structures to determine the likelihood of future outcomes. Example: $R_t = c_0 + c_1 R_{t-1} + \sigma z_t + \phi_1 z_{t-1}$.

---

## Card 23

**Q:** Term: Stationarity (Strong)

**A:** Definition: A property where the joint distribution of all values in a time series is invariant under time translation. Example: A process where the probability of seeing a specific sequence of values is the same today as it is next year.

---

## Card 24

**Q:** Term: Weak Stationarity

**A:** Definition: A property where the first and second moments (means and covariances) of a process are invariant over time. Example: A process where $E[R_t]$ and $Var(R_t)$ are constants that do not depend on $t$.

---

## Card 25

**Q:** What is the key insight behind solving for the mean of an AR(1) process?

**A:** The key insight is assuming stationarity, which allows setting $E[R_t] = E[R_{t-1}]$ to solve the recursive expectation equation.

---

## Card 26

**Q:** Formula: Unconditional mean of an AR(1) process

**A:** $E[R_t] = \frac{c_0}{1 - c_1}$, where $c_0$ is the constant intercept and $c_1$ is the autoregressive coefficient.

---

## Card 27

**Q:** Formula: Mean reversion form of an AR(1) model

**A:** $R_t - \mu = -\lambda(R_{t-1} - \mu) + \sigma z_t$, where $\mu$ is the mean and $\lambda$ is the mean-reversion coefficient (equal to $-c_1$).

---

## Card 28

**Q:** In the mean-reverting AR(1) model, what is the effect of a positive coefficient $\lambda$?

**A:** An excess value in one period leads to a change in the opposite direction (toward the mean) in the following period.

---

## Card 29

**Q:** Formula: Variance ($\gamma_0$) of a stationary AR(1) process

**A:** $\gamma_0 = \frac{\sigma^2}{1 - \lambda^2}$, where $\sigma^2$ is the innovation variance and $\lambda$ is the mean-reversion coefficient.

---

## Card 30

**Q:** Term: Lag-$k$ Autocovariance

**A:** Definition: The covariance between observations in a time series taken $k$ periods apart. Example: $\gamma_k = E[(R_t - \mu)(R_{t-k} - \mu)]$.

---

## Card 31

**Q:** Formula: Lag-$k$ autocovariance for a stationary AR(1) process

**A:** $\gamma_k = (-\lambda)^k \gamma_0 = \frac{(-\lambda)^k}{1 - \lambda^2} \sigma^2$, where $\lambda$ is the mean-reversion coefficient and $\sigma^2$ is the innovation variance.

---

## Card 32

**Q:** How do unconditional expectations differ from conditional expectations in time series modelling?

**A:** Unconditional expectations are taken with respect to all future values, while conditional expectations treat past observations as known fixed values.

---

## Card 33

**Q:** Term: Monte Carlo Simulation

**A:** Definition: The use of random number generators to simulate many hypothetical realisations of a stochastic process to approximate statistical results. Example: Simulating 10,000 different price paths for a stock to estimate the probability of it hitting a certain level.

---

## Card 34

**Q:** Why is Monte Carlo simulation described as a 'test lab' for financial analytics?

**A:** It provides a 'best case' dataset from a known distribution, allowing for the testing of algorithms and theory where the 'true' process is controlled.

---

## Card 35

**Q:** What is a major limitation of Monte Carlo results compared to closed-form solutions?

**A:** Monte Carlo results are statistical approximations subject to sampling error and machine limitations.

---

## Card 36

**Q:** Term: Log-return

**A:** Definition: The natural logarithm of the ratio of a price to its previous price, representing continuously compounded returns. Example: $r_t = \log(P_t / P_{t-1})$.

---

## Card 37

**Q:** Term: RW1 (IID Random Walk)

**A:** Definition: A random walk where increments are independent and identically distributed. Example: A process where every daily return follows the exact same $N(\mu, \sigma^2)$ distribution independently.

---

## Card 38

**Q:** Term: RW2 (INID Random Walk)

**A:** Definition: A random walk with independent but non-identically distributed increments. Example: A stock model where returns are independent each day, but the volatility parameter changes daily.

---

## Card 39

**Q:** Term: RW3 (Uncorrelated Random Walk)

**A:** Definition: A random walk where innovations are dependent and non-identical, but the increments remain uncorrelated. Example: Volatility clustering where the squares of increments are correlated even if the increments themselves are not.

---

## Card 40

**Q:** Term: Variance Ratio Test

**A:** Definition: A test by Lo & MacKinlay that analyses how variances scale as observation frequency changes to check for random walk behaviour. Example: Comparing the variance of weekly returns to five times the variance of daily returns.

---

## Card 41

**Q:** What does the variance ratio test predict for a true random walk?

**A:** It predicts that the variance ratio should be one, as variances should scale linearly with time.

---

## Card 42

**Q:** How is the process $X_t = z \cos(\omega t) + z' \sin(\omega t)$ shown to be weakly stationary?

**A:** By showing its mean is zero, its variance is a constant ($1$), and its autocovariance depends only on the time difference $|t-s|$.

---

## Card 43

**Q:** Formula: Autocovariance of the trigonometric process $X_t = z \cos(\omega t) + z' \sin(\omega t)$

**A:** $E[X_t X_s] = \cos(\omega(t-s))$, which confirms the process is stationary as it depends only on the lag.

---

## Card 44

**Q:** Pitfall: Assuming parameter stability

**A:** A common mistake is assuming that parameters $\mu$ and $\sigma$ estimated in one period remain constant across all future periods, whereas historical data often shows significant variation.

---

## Card 45

**Q:** Pitfall: Volatility Clustering in RW1

**A:** The RW1 model fails to capture 'volatility clustering' because it assumes innovations are identically distributed, ignoring that high-volatility days often follow high-volatility days.

---

## Card 46

**Q:** Pitfall: Log-normality assumption

**A:** Standard random walk models for stock prices often assume returns are drawn from a log-normal distribution, which may fail to account for 'fat tails' or extreme market events seen in reality.

---

## Card 47

**Q:** In the process $X_t = z_t + \theta z_{t-2}$, what is the autocovariance $\gamma_k$ for a lag of $k = 2$?

**A:** $\gamma_2 = \theta$, derived from $E[(z_t + \theta z_{t-2})(z_{t-2} + \theta z_{t-4})]$, where only the $E[\theta z_{t-2}^2]$ term is non-zero.

---

## Card 48

**Q:** What is the expected value of the increment $z_t$ in relation to a semi-infinite sum of past increments $Y_{t-1}$?

**A:** The expectation $E[z_t Y_{t-1}]$ is $0$ because the current increment is independent of all previous increments in the sum.

---

## Card 49

**Q:** If we define $R_t = \sigma z_t + \mu$, what is the variance of $r_t - \mu$?

**A:** $E[(r_t - \mu)^2] = \sigma^2$, which represents the variance of the innovation scaled by $\sigma$.

---

## Card 50

**Q:** What is the key insight behind 'Universality' in random walk models?

**A:** The essential features of the walk, such as variance scaling, are independent of many of the specific details of the individual steps.

---

## Card 51

**Q:** Term: Ensemble

**A:** Definition: A collection of a large number of hypothetical realisations of a stochastic process used in Monte Carlo methods. Example: Generating 5,000 potential future paths for an interest rate index.

---

## Card 52

**Q:** Formula: Expected value of the trigonometric process $X_t = z \cos(\omega t) + z' \sin(\omega t)$

**A:** $E[X_t] = 0$, given that the random variables $z$ and $z'$ are independent with zero mean.

---

## Card 53

**Q:** Formula: Variance of the trigonometric process $X_t = z \cos(\omega t) + z' \sin(\omega t)$

**A:** $Var(X_t) = \cos^2(\omega t) + \sin^2(\omega t) = 1$, using the Pythagorean trigonometric identity.

---

## Card 54

**Q:** How is the autocovariance of a stationary process denoted?

**A:** It is denoted as $\gamma_k$, where $k$ represents the lag (the number of time steps between observations).

---

## Card 55

**Q:** What happens to the precision of a Monte Carlo simulation as the sample size increases?

**A:** The precision increases, as the statistical approximations converge toward the exact results.

---

## Card 56

**Q:** In an AR(1) model, what condition on the parameter $\lambda$ (or $c_1$) is required for stationarity?

**A:** The absolute value must be less than one ($|\lambda| < 1$ or $|c_1| < 1$).

---

## Card 57

**Q:** What does rejecting the random walk model imply about asset prices?

**A:** It opens the possibility that asset prices may be predictable or that a more complex model is required to describe market efficiency.

---

## Card 58

**Q:** Why can Monte Carlo methods provide results even when closed-form analytics do not exist?

**A:** Because they rely on numerical simulation of the process rather than the derivation of a precise mathematical formula.

---

## Card 59

**Q:** Term: Lag-k Autocovariance Coefficient

**A:** Definition: A value that relates the influence of an excess return value at one point in time with values $k$ periods in the past. Example: $\gamma_k$ in an AR(1) process showing how past shocks decay over time.

---

## Card 60

**Q:** If $X_t = X_{t-1} + r_t$, and $r_t$ is IID, what is $Var(X_t | X_0)$?

**A:** $Var(X_t | X_0) = \sigma^2 t$, assuming $r_t \sim IID(0, \sigma^2)$.

---
