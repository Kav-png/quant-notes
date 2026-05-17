# Finance Flashcards

## Card 1

**Q:** Term: Return

**A:** Definition: The percentage growth in the value of an asset, including accumulated dividends, over a specific time period. Example: A stock rising from $100$ to $105$ provides a $5\%$ return.

---

## Card 2

**Q:** Formula: Asset Return (Discrete)

**A:** $R_i = \frac{S_{i+1} - S_i}{S_i}$, where $R_i$ is the return, $S_i$ is the price today, and $S_{i+1}$ is the price tomorrow.

---

## Card 3

**Q:** How is the importance of returns over absolute prices derived?

**A:** The key insight is that investors care about percentage growth (interest rates/yields) rather than the absolute level, making returns a more universal metric across different asset scales.

---

## Card 4

**Q:** Why is 'randomness' considered the crucial element in derivative modelling?

**A:** Because of Jensen's inequality, where the expected value of an option payoff is not equal to the payoff of the expected future asset price.

---

## Card 5

**Q:** Concept: Jensen's Inequality

**A:** Definition: A mathematical property where the average of a non-linear function is greater than the function of the average. Example: A call option's value is higher if the stock is volatile rather than fixed at its mean price.

---

## Card 6

**Q:** Under the widely accepted model, what distribution is assumed for asset returns?

**A:** The Normal (Gaussian) distribution.

---

## Card 7

**Q:** Term: Drift

**A:** Definition: The annualized average rate at which an asset's price rises or falls. Example: A stock with a $\mu$ of $0.15$ is expected to grow by $15\%$ per year on average.

---

## Card 8

**Q:** Term: Volatility

**A:** Definition: A measure of the randomness or unpredictability in an asset's returns, representing the annualized standard deviation. Example: A volatility $\sigma$ of $0.25$ indicates a $25\%$ standard deviation in annual returns.

---

## Card 9

**Q:** Formula: Mean Return Scaling

**A:** $\text{mean} = \mu \delta t$, where $\mu$ is the annualized drift and $\delta t$ is the time step.

---

## Card 10

**Q:** Formula: Standard Deviation Scaling

**A:** $\text{standard deviation} = \sigma \sqrt{\delta t}$, where $\sigma$ is the annualized volatility and $\delta t$ is the time step.

---

## Card 11

**Q:** What is the key insight behind scaling the standard deviation with $\sqrt{\delta t}$?

**A:** It ensures that the standard deviation remains finite and non-zero as the time step $\delta t$ tends towards zero.

---

## Card 12

**Q:** Formula: Discrete Random Walk (Asset Price)

**A:** $S_{i+1} - S_i = \mu S_i \delta t + \sigma S_i \phi \sqrt{\delta t}$, where $\phi$ is a standardized Normal variable $N(0,1)$.

---

## Card 13

**Q:** Pitfall: What is the risk of modelling absolute price changes (additive) instead of percentage changes (multiplicative)?

**A:** An additive model (Arithmetic Random Walk) allows the asset price to potentially become negative, which is financially unrealistic.

---

## Card 14

**Q:** Term: Lognormal Random Walk

**A:** Definition: A model where the logarithm of the asset price follows an arithmetic random walk, ensuring the price itself stays positive. Example: Geometric Brownian Motion used for stock prices.

---

## Card 15

**Q:** Concept: Central Limit Theorem

**A:** Definition: The principle that the sum of a large number of independent, identically distributed random variables will be approximately Normally distributed. Example: Adding $12$ uniform random variables to approximate a Normal distribution.

---

## Card 16

**Q:** Term: Wiener Process ($dX$)

**A:** Definition: A continuous-time stochastic process with a mean of $0$ and a variance of $dt$. Example: The source of randomness in the Black-Scholes equation.

---

## Card 17

**Q:** Formula: Expected Value of a Wiener Process Increment

**A:** $E[dX] = 0$, where $dX$ is the increment of a Wiener process.

---

## Card 18

**Q:** Formula: Variance of a Wiener Process Increment

**A:** $E[dX^2] = dt$, where $dt$ is the infinitesimal time step.

---

## Card 19

**Q:** Formula: Continuous Stochastic Differential Equation (SDE) for Assets

**A:** $dS = \mu S dt + \sigma S dX$, where $S$ is the asset price, $\mu$ is drift, $\sigma$ is volatility, and $dX$ is a Wiener process.

---

## Card 20

**Q:** What is the key insight behind the '12 RAND' method for simulating Normal variables?

**A:** By the Central Limit Theorem, the sum of $12$ uniform random variables minus $6$ provides a fast approximation of $N(0,1)$ with a mean of $0$ and variance of $1$.

---

## Card 21

**Q:** Formula: 12-RAND Normal Approximation

**A:** $\phi \approx (\sum_{i=1}^{12} \text{RAND}_i) - 6$, where $\text{RAND}$ is a uniform random variable between $0$ and $1$.

---

## Card 22

**Q:** How does Wilmott's treatment of asset price distribution differ from Hull's market practice?

**A:** Wilmott focuses on deriving the lognormal distribution from the scaling properties of $dS$, whereas Hull emphasizes the lognormal property as an empirical starting point for pricing.

---

## Card 23

**Q:** Formula: Simple Volatility Estimator

**A:** $\sigma \approx \sqrt{\frac{1}{(M-1)\delta t} \sum_{i=1}^{M} (R_i - \bar{R})^2}$, where $M$ is the number of samples and $R_i$ is the return.

---

## Card 24

**Q:** Why can the mean return $\bar{R}$ be ignored in volatility estimation when $\delta t$ is small?

**A:** Because the standard deviation of returns (scaling with $\sqrt{\delta t}$) is much larger than the mean return (scaling with $\delta t$) over short intervals.

---

## Card 25

**Q:** Pitfall: What is the 'Catch-22' in choosing the number of days for historical volatility estimation?

**A:** Using too much data includes stale, irrelevant regimes, while using too little data results in high statistical error.

---

## Card 26

**Q:** What happens to the asset price growth in the absence of randomness ($\sigma = 0$)?

**A:** The asset exhibits exponential growth, $S_T = S_0 e^{\mu T}$, behaving exactly like cash in a bank.

---

## Card 27

**Q:** In the discrete random walk recipe $S_{i+1} = S_i (1 + \mu \delta t + \sigma \phi \sqrt{\delta t})$, what does $\phi$ represent?

**A:** A random number drawn from a standardized Normal distribution $N(0,1)$.

---

## Card 28

**Q:** How does a Binomial Random Walk differ from a Normal Random Walk?

**A:** The Binomial model assumes only two possible states (up/down) in the next step, while the Normal model allows for a continuous range of outcomes.

---

## Card 29

**Q:** What is the 'Markov property' as applied to the asset price model?

**A:** The future price distribution depends only on the current price, not the historical path taken to reach that price.

---

## Card 30

**Q:** Pitfall: What is the danger of assuming constant volatility in the Black-Scholes model?

**A:** Market data shows 'smiles' and 'skews', indicating that volatility actually varies with the strike price and time to expiry.

---

## Card 31

**Q:** Concept: Arithmetic Random Walk

**A:** Definition: A process where changes in the asset price are independent of the current price level. Example: A coin toss where you win or lose exactly $1$ pound regardless of your total wealth.

---

## Card 32

**Q:** Why is the multiplicative rule (Geometric Random Walk) preferred over the additive rule for stock prices?

**A:** It ensures the magnitude of price changes is proportional to the current price, reflecting how markets actually operate and preventing negative values.

---

## Card 33

**Q:** What is the mathematical notation for a Normal distribution with mean $m$ and standard deviation $s$?

**A:** $N(m, s^2)$.

---

## Card 34

**Q:** Term: Standardized Normal Variable

**A:** Definition: A Normal random variable with a mean of $0$ and a standard deviation of $1$. Example: The variable $\phi$ used in the random walk equation.

---

## Card 35

**Q:** How does the asset price path behave qualitatively in a lognormal random walk as $S$ approaches zero?

**A:** The increments $dS$ become smaller and smaller, making it harder for the price to reach or cross zero.

---

## Card 36

**Q:** Formula: Probability Density Function of a Standard Normal Distribution

**A:** $\frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}\phi^2}$, where $\phi$ is the random variable.

---

## Card 37

**Q:** What is the effect of increasing the time horizon $T$ on the distribution of future asset prices?

**A:** The distribution spreads out (variance increases linearly with time), reflecting greater uncertainty.

---

## Card 38

**Q:** Concept: Efficient Market Hypothesis (Implicit in Ch 4)

**A:** Definition: The idea that current prices reflect all available information, implying that price changes follow a random walk. Example: The inability to consistently predict tomorrow's stock price from today's data.

---

## Card 39

**Q:** How is the annualized volatility $\sigma$ calculated from daily returns?

**A:** Calculate the standard deviation of daily returns and multiply by $\sqrt{252}$ (assuming $252$ trading days in a year).

---

## Card 40

**Q:** Why does the binomial tree lead to a bell-shaped distribution of future prices?

**A:** Because there are many more paths leading to the interior (middle) nodes of the tree than to the extreme top or bottom nodes.

---

## Card 41

**Q:** Term: Drift Rate ($\mu$)

**A:** Definition: The deterministic component of an asset's price change per unit of time. Example: The 'mean' slope in a price chart over long periods.

---

## Card 42

**Q:** If $\delta t$ is $1/252$ (one day), how does the volatility component relate to the daily standard deviation?

**A:** The daily standard deviation is $\sigma \sqrt{1/252}$.

---

## Card 43

**Q:** How does the 'Time Out' on coin tossing justify the geometric random walk?

**A:** It explains that as the asset price gets larger, so do the changes from one day to the next, necessitating modelling returns rather than absolute values.

---

## Card 44

**Q:** What is the 'risk-neutral expectation' in the context of the binomial model?

**A:** The probability of an asset rise that makes the expected return equal to the risk-free interest rate.

---

## Card 45

**Q:** Formula: Asset price at step $n$, node $j$ ($S_n^j$)

**A:** $S_n^j = S u^j v^{n-j}$, where $u$ is the up-factor and $v$ is the down-factor.

---

## Card 46

**Q:** What is the key insight behind the 'Wiener Process' as a limit?

**A:** It is the limit of a discrete random walk as the time step goes to zero, providing the foundation for continuous-time calculus (Itô calculus).

---

## Card 47

**Q:** Under what condition does the approximation $\log(1 + \mu \delta t) \approx \mu \delta t$ hold?

**A:** When the time step $\delta t$ is very small (infinitesimal).

---

## Card 48

**Q:** Concept: Path Independence

**A:** Definition: The property that the probability of future prices depends only on the current state, not how it was reached. Example: A stock at $100$ today has the same future distribution regardless of whether it was at $50$ or $150$ yesterday.

---

## Card 49

**Q:** Formula: Standardized Normal in Excel

**A:** $\text{NORMSINV(RAND())}$, which returns a value from the inverse cumulative standard Normal distribution.

---

## Card 50

**Q:** Why does Wilmott suggest that interest rate modelling is harder than equity modelling?

**A:** Because interest rates do not have the 'clue' of absolute price irrelevance; unlike stocks, the absolute level of an interest rate matters significantly for its future behaviour.

---

## Card 51

**Q:** What characterizes a 'Martingale' process?

**A:** A process where the conditional expectation of the next value, given all current and past values, is equal to the current value.

---

## Card 52

**Q:** In the model $dS = \mu S dt + \sigma S dX$, what part is deterministic?

**A:** The term $\mu S dt$.

---

## Card 53

**Q:** In the model $dS = \mu S dt + \sigma S dX$, what part is stochastic?

**A:** The term $\sigma S dX$.

---

## Card 54

**Q:** How does the 'law of large numbers' relate to Monte Carlo simulations of asset paths?

**A:** As the number of simulated paths increases, the average of the payoffs converges to the true expected value (theoretical price).

---

## Card 55

**Q:** What is the primary difference between Arithmetic and Geometric Brownian Motion?

**A:** Arithmetic BM has constant volatility in price terms ($dS = \dots + \sigma dX$), whereas Geometric BM has volatility proportional to the price level ($dS = \dots + \sigma S dX$).

---

## Card 56

**Q:** Why is the term $O(\delta t^{1/2})$ critical in stochastic modelling?

**A:** It represents the randomness (volatility) which dominates the deterministic drift $O(\delta t)$ over short time scales.

---
