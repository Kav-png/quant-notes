# Stochastic Flashcards

## Card 1

**Q:** Term: Markov Process

**A:** Definition: A particular type of stochastic process where only the current value of a variable is relevant for predicting the future, making the past history and the path taken to reach the present irrelevant. Example: Predicting the future probability distribution of IBM stock based solely on its current price of \( \$100 \).

---

## Card 2

**Q:** How does the Markov property relate to the weak form of market efficiency?

**A:** The Markov property implies that the current price incorporates all information contained in past prices, meaning technical analysis of past trends cannot predict future movements.

---

## Card 3

**Q:** Term: Wiener Process (Brownian Motion)

**A:** Definition: A continuous-time Markov stochastic process with a mean change of zero and a variance rate of 1.0 per year. Example: The motion of a small particle subject to a large number of molecular shocks in physics.

---

## Card 4

**Q:** Formula: Change in a Wiener process over a small time interval

**A:** \[ \Delta z = \epsilon \sqrt{\Delta t} \]
\( \Delta z \): change in Wiener process; \( \epsilon \): random variable from a standardised normal distribution \( \phi(0, 1) \); \( \Delta t \): small time interval.

---

## Card 5

**Q:** What is the mean and variance of the change in a Wiener process \( \Delta z \) over a small time interval \( \Delta t \)?

**A:** The mean is 0 and the variance is \( \Delta t \).

---

## Card 6

**Q:** What is the standard deviation of the change in a Wiener process \( \Delta z \) over time \( \Delta t \)?

**A:** The standard deviation is \( \sqrt{\Delta t} \).

---

## Card 7

**Q:** Formula: Distribution of a Wiener process change over a long time interval \( T \)

**A:** \[ z(T) - z(0) \sim \phi(0, T) \]
\( z(T) \): value at time \( T \); \( z(0) \): value at time 0; \( \phi(0, T) \): normal distribution with mean 0 and variance \( T \).

---

## Card 8

**Q:** How does uncertainty about the future value of a Wiener process variable scale with the time horizon?

**A:** Uncertainty, measured by the standard deviation, increases as the square root of the time horizon \( \sqrt{T} \).

---

## Card 9

**Q:** Property: Path of a Wiener process

**A:** The path followed by a variable in a Wiener process is 'jagged' because its standard deviation \( \sqrt{\Delta t} \) is much larger than the time step \( \Delta t \) as \( \Delta t \to 0 \).

---

## Card 10

**Q:** Term: Generalized Wiener Process

**A:** Definition: A stochastic process for a variable that incorporates both a constant drift rate per unit of time and a constant variance rate. Example: Modelling the cash position of a company that grows by a fixed average amount annually but with added random noise.

---

## Card 11

**Q:** Formula: Generalized Wiener Process

**A:** \[ dx = a dt + b dz \]
\( a \): constant drift rate; \( b \): constant volatility; \( dt \): small time increment; \( dz \): Wiener process increment.

---

## Card 12

**Q:** In a Generalized Wiener Process \( dx = a dt + b dz \), what does the term \( a dt \) represent?

**A:** It represents the expected drift of the variable, showing that without noise, the variable would grow linearly at rate \( a \).

---

## Card 13

**Q:** What are the mean and variance of the change in a Generalized Wiener Process variable \( x \) over time interval \( T \)?

**A:** The mean change is \( aT \) and the variance is \( b^2 T \).

---

## Card 14

**Q:** Term: Itô Process

**A:** Definition: A generalised Wiener process where the drift and variance rates are functions of the underlying variable \( x \) and time \( t \). Example: A stock price process where volatility and expected return change as the price changes.

---

## Card 15

**Q:** Formula: Itô Process

**A:** \[ dx = a(x, t) dt + b(x, t) dz \]
\( a(x, t) \): drift as a function of \( x \) and \( t \); \( b(x, t) \): volatility as a function of \( x \) and \( t \); \( dz \): Wiener process increment.

---

## Card 16

**Q:** Pitfall: Why is a Generalized Wiener Process (constant drift/variance) inappropriate for modelling stock prices?

**A:** It fails to capture that the expected percentage return required by investors is independent of the stock price level; a constant drift would imply the percentage return decreases as the price rises.

---

## Card 17

**Q:** What is the key assumption regarding stock price variability in the most widely used model?

**A:** The variability of the percentage return in a short period is assumed to be the same regardless of the stock price level.

---

## Card 18

**Q:** Formula: Geometric Brownian Motion (GBM) for stock prices

**A:** \[ dS = \mu S dt + \sigma S dz \]
\( S \): stock price; \( \mu \): expected rate of return; \( \sigma \): volatility; \( dt \): time increment; \( dz \): Wiener process increment.

---

## Card 19

**Q:** Formula: Discrete-time model for stock price behavior

**A:** \[ \frac{\Delta S}{S} = \mu \Delta t + \sigma \epsilon \sqrt{\Delta t} \]
\( \Delta S \): change in stock price; \( S \): current stock price; \( \mu \): expected return; \( \sigma \): volatility; \( \epsilon \): sample from \( \phi(0, 1) \).

---

## Card 20

**Q:** What does the parameter \( \sigma^2 \) represent in the Geometric Brownian Motion model?

**A:** It represents the variance rate of the percentage return provided by the stock.

---

## Card 21

**Q:** How is a stock price at time \( T \) related to its initial price \( S_0 \) in a world with no uncertainty (\( \sigma = 0 \))?

**A:** The stock price grows at a continuously compounded rate of \( \mu \), resulting in \( S_T = S_0 e^{\mu T} \).

---

## Card 22

**Q:** How are two correlated Wiener processes \( dz_1 \) and \( dz_2 \) simulated?

**A:** They are simulated by sampling from a bivariate normal distribution where each variable is \( \phi(0, 1) \) and their correlation is \( \rho \).

---

## Card 23

**Q:** What is the key insight behind Itô's Lemma?

**A:** It shows that a function of an Itô process also follows an Itô process, and critically, both the underlying variable and the function are affected by the same source of uncertainty \( dz \).

---

## Card 24

**Q:** Formula: Itô's Lemma for a function \( G(x, t) \)

**A:** \[ dG = \left( \frac{\partial G}{\partial x} a + \frac{\partial G}{\partial t} + \frac{1}{2} \frac{\partial^2 G}{\partial x^2} b^2 \right) dt + \frac{\partial G}{\partial x} b dz \]
\( a, b \): drift and volatility of \( x \); \( G \): function of \( x \) and \( t \); \( dz \): Wiener process.

---

## Card 25

**Q:** What is the drift rate of the process followed by the function \( G \) in Itô's Lemma?

**A:** \[ \frac{\partial G}{\partial x} a + \frac{\partial G}{\partial t} + \frac{1}{2} \frac{\partial^2 G}{\partial x^2} b^2 \]

---

## Card 26

**Q:** What is the variance rate of the process followed by the function \( G \) in Itô's Lemma?

**A:** \[ \left( \frac{\partial G}{\partial x} \right)^2 b^2 \]

---

## Card 27

**Q:** Formula: Itô's Lemma applied to a function of stock price \( G(S, t) \)

**A:** \[ dG = \left( \frac{\partial G}{\partial S} \mu S + \frac{\partial G}{\partial t} + \frac{1}{2} \frac{\partial^2 G}{\partial S^2} \sigma^2 S^2 \right) dt + \frac{\partial G}{\partial S} \sigma S dz \]
\( \mu \): expected return; \( \sigma \): volatility; \( S \): stock price; \( G \): derivative price.

---

## Card 28

**Q:** Formula: Process for the forward price \( F \) of a non-dividend-paying stock

**A:** \[ dF = (\mu - r)F dt + \sigma F dz \]
\( \mu \): stock's expected return; \( r \): risk-free rate; \( \sigma \): volatility; \( F \): forward price; \( dz \): Wiener process.

---

## Card 29

**Q:** How does the expected growth rate of a forward price \( F \) differ from the spot price \( S \)?

**A:** The forward price grows at the rate \( \mu - r \) (the excess return over the risk-free rate), whereas the spot price grows at rate \( \mu \).

---

## Card 30

**Q:** Formula: Process for \( \ln S \) given GBM

**A:** \[ d(\ln S) = (\mu - \frac{\sigma^2}{2}) dt + \sigma dz \]
\( \mu \): expected return; \( \sigma \): volatility; \( S \): stock price; \( dz \): Wiener process.

---

## Card 31

**Q:** Pitfall: Why is the drift of \( \ln S \) equal to \( \mu - \sigma^2/2 \) instead of \( \mu \)?

**A:** This result arises from the non-linear nature of the logarithm and the application of the second-order term in Itô's Lemma, specifically \( \frac{1}{2} \frac{\partial^2 G}{\partial S^2} \sigma^2 S^2 \).

---

## Card 32

**Q:** What is the distribution of the change in \( \ln S \) between time 0 and time \( T \)?

**A:** It is normally distributed: \( \ln S_T - \ln S_0 \sim \phi[(\mu - \sigma^2/2)T, \sigma^2 T] \).

---

## Card 33

**Q:** Formula: Probability distribution of stock price \( S_T \) at time \( T \)

**A:** \[ \ln S_T \sim \phi[ \ln S_0 + (\mu - \frac{\sigma^2}{2})T, \sigma^2 T ] \]
\( S_T \): price at time \( T \); \( S_0 \): initial price; \( \mu \): expected return; \( \sigma \): volatility.

---

## Card 34

**Q:** Term: Lognormal Distribution

**A:** Definition: A distribution of a variable where the natural logarithm of the variable is normally distributed. Example: Modelling stock prices, as they cannot fall below zero and their percentage returns are approximately normal.

---

## Card 35

**Q:** What is the standard deviation of \( \ln S_T \)?

**A:** \[ \sigma \sqrt{T} \]
\( \sigma \): stock volatility; \( T \): time to maturity.

---

## Card 36

**Q:** Pitfall: What is a hidden assumption when using a basic Wiener process to model financial variables?

**A:** The model assumes a constant variance rate of 1.0 per year and independent increments, which may not hold during periods of market stress or high volatility.

---

## Card 37

**Q:** Difference: Hull vs Wilmott on Itô's Lemma application

**A:** Hull emphasizes the application to observable market prices like forward contracts and stock returns, whereas Wilmott often focuses on the rigorous mathematical derivation from Taylor series expansions.

---

## Card 38

**Q:** How is the discrete-time stock price change \( \Delta S \) calculated for the start of a period?

**A:** \[ \Delta S = \mu S \Delta t + \sigma S \epsilon \sqrt{\Delta t} \]
This models the absolute change in price as being proportional to the current price level.

---

## Card 39

**Q:** If a stock price follows a Markov process and was \( \$80 \) last month and is \( \$100 \) today, what information is used for tomorrow's forecast?

**A:** Only today's price of \( \$100 \) is relevant; the previous price of \( \$80 \) is ignored.

---

## Card 40

**Q:** Why is the expected length of a Wiener process path in any time interval infinite?

**A:** Because the path is continuous but nowhere differentiable, consisting of infinite 'jagged' movements as the time step approaches zero.

---

## Card 41

**Q:** In Monte Carlo simulation, why is it usually more accurate to simulate \( \ln S \) rather than \( S \)?

**A:** Simulating \( \ln S \) is more accurate because its process has constant drift and volatility coefficients, whereas the process for \( S \) depends on the value of \( S \) itself.

---

## Card 42

**Q:** What does the drift rate \( a \) represent in the generalized Wiener process \( dx = a dt + b dz \)?

**A:** The average drift (expected change) per unit of time.

---

## Card 43

**Q:** What does the variance rate \( b^2 \) represent in a generalized Wiener process?

**A:** The variance of the change in the variable per unit of time.

---

## Card 44

**Q:** What happens to the standard deviation of a Wiener process as the time interval \( \Delta t \) becomes very small?

**A:** The standard deviation \( \sqrt{\Delta t} \) becomes much larger than \( \Delta t \), making the noise component dominate the deterministic component.

---

## Card 45

**Q:** If a variable follows a Wiener process and starts at 25, what is its standard deviation after 5 years?

**A:** \[ \sqrt{5} \approx 2.236 \]

---

## Card 46

**Q:** Under what condition does an Itô process become a Generalized Wiener Process?

**A:** When the drift function \( a(x, t) \) and the volatility function \( b(x, t) \) are both constants.

---

## Card 47

**Q:** In the GBM model, if the stock price increases, what happens to the expected dollar drift?

**A:** The dollar drift \( \mu S dt \) increases because it is proportional to the stock price \( S \).

---

## Card 48

**Q:** What is the key decision point when deciding between a Wiener process and a Generalized Wiener process for a model?

**A:** Whether the variable has a non-zero expected growth rate (drift) and whether the variance per unit time is 1.0 or some other constant.

---

## Card 49

**Q:** In the context of Itô's Lemma, what does \( \frac{\partial G}{\partial t} \) represent?

**A:** The rate of change of the function (derivative) value with respect to the passage of time, also known as Theta.

---

## Card 50

**Q:** Formula: Process for \( S^n \) where \( S \) follows GBM

**A:** \[ d(S^n) = [ n\mu + \frac{1}{2} n(n-1)\sigma^2 ] S^n dt + n\sigma S^n dz \]
\( n \): power; \( \mu \): expected return; \( \sigma \): volatility; \( S \): stock price.

---

## Card 51

**Q:** Why is the expected number of times a Wiener process equals any particular value infinite?

**A:** Due to the fractal, 'jagged' nature of the process, it crosses any value in its path an infinite number of times within any time interval, however small.

---

## Card 52

**Q:** What does a negative cash position represent in a Wiener process simulation?

**A:** It represents a situation where the company is borrowing funds.

---

## Card 53

**Q:** How is the volatility of a stock \( \sigma \) related to the standard deviation of its logarithm?

**A:** The standard deviation of \( \ln S_T \) is \( \sigma \sqrt{T} \), meaning volatility is the annualised standard deviation of the log-return.

---

## Card 54

**Q:** If two variables follow Wiener processes with correlation \( \rho \), what is the correlation of their discrete increments \( \Delta z_1 \) and \( \Delta z_2 \)?

**A:** The correlation remains \( \rho \).

---

## Card 55

**Q:** Insight: How is Itô's Lemma related to Taylor Series expansion?

**A:** Itô's Lemma is an extension of the Taylor Series expansion that keeps terms of order \( \Delta x^2 \) because in stochastic calculus, \( dz^2 \) is equal to \( dt \).

---

## Card 56

**Q:** Pitfall: Assuming log-normality for very short intraday timeframes.

**A:** While stock prices are lognormal over longer periods, high-frequency intraday data may exhibit different distributions due to market microstructure effects.

---

## Card 57

**Q:** What is the drift of a variable that follows a martingale?

**A:** Zero.

---

## Card 58

**Q:** What is the relationship between \( \Delta z \) and \( dz \)?

**A:** \( dz \) is the limit of \( \Delta z \) as the time step \( \Delta t \) tends to zero.

---

## Card 59

**Q:** In the GBM model, what is the expected stock price at time \( T \)?

**A:** \[ E(S_T) = S_0 e^{\mu T} \]

---

## Card 60

**Q:** Why is \( z(T) - z(0) \) the sum of independent normal distributions?

**A:** Because Property 2 of a Wiener process states that changes in disjoint time intervals are independent, and the sum of independent normal variables is also normal.

---
