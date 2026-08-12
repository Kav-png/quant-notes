# Probability Flashcards

## Card 1

**Q:** Probability Axiom: Non-negativity

**A:** $P(A) \ge 0$ for any event $A$.

---

## Card 2

**Q:** Probability Axiom: Normalisation

**A:** $P(\Omega) = 1$, where $\Omega$ represents the entire sample space.

---

## Card 3

**Q:** Probability Axiom: Additivity

**A:** If $A$ and $B$ are disjoint events, then $P(A \cup B) = P(A) + P(B)$.

---

## Card 4

**Q:** Term: Sample Space

**A:** Definition: The set of all possible outcomes of an experiment, which must be mutually exclusive and collectively exhaustive. Example: For a coin flip, $\Omega = \{\text{Heads, Tails}\}$.

---

## Card 5

**Q:** What criteria must a list of outcomes meet to form a valid sample space?

**A:** The outcomes must be mutually exclusive (no two can happen at once) and collectively exhaustive (one must happen).

---

## Card 6

**Q:** Common Pitfall: Confusing independence with disjointness

**A:** Disjoint events are not independent; knowing one occurred makes the probability of the other zero. Example: Rolling a 1 and a 2 on the same die are disjoint but highly dependent.

---

## Card 7

**Q:** Term: Event

**A:** Definition: Any subset of the sample space to which a probability is assigned. Example: Rolling an even number on a die, which is the subset $\{2, 4, 6\}$.

---

## Card 8

**Q:** Condition for the independence of events $A$ and $B$

**A:** $P(A \cap B) = P(A)P(B)$.

---

## Card 9

**Q:** Formula: Bayes' Rule (Discrete)

**A:** $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$, where $P(A|B)$ is the posterior and $P(A)$ is the prior.

---

## Card 10

**Q:** Formula: Total Probability Theorem

**A:** $P(B) = \sum_{i} P(B|A_i)P(A_i)$, where $A_i$ is a partition of the sample space.

---

## Card 11

**Q:** Term: Random Variable

**A:** Definition: A function that maps every possible outcome in the sample space to a real numerical value. Example: Letting $X=1$ for Heads and $X=0$ for Tails.

---

## Card 12

**Q:** Term: Probability Mass Function (PMF)

**A:** Definition: A function $P_X(x)$ that gives the probability that a discrete random variable $X$ is exactly equal to $x$. Example: $P_X(1) = 0.5$ for a fair coin flip.

---

## Card 13

**Q:** Formula: Expected value of a discrete random variable $X$

**A:** $E[X] = \sum_{x} x P_X(x)$, representing the weighted average of all possible values.

---

## Card 14

**Q:** Formula: Variance of a random variable $X$

**A:** $Var(X) = E[X^2] - (E[X])^2$, measuring the average squared deviation from the mean.

---

## Card 15

**Q:** Common Pitfall: Linearity of expectation vs. functions of random variables

**A:** While $E[aX + b] = aE[X] + b$, $E[g(X)]$ is generally not equal to $g(E[X])$ for non-linear $g$. Example: $E[X^2] \ne (E[X])^2$ unless the variance is zero.

---

## Card 16

**Q:** Formula: Binomial Probability Mass Function

**A:** $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$, where $n$ is trials, $k$ is successes, and $p$ is success probability.

---

## Card 17

**Q:** Term: Cumulative Distribution Function (CDF)

**A:** Definition: The function $F_X(x) = P(X \le x)$, representing the total probability up to a point $x$. Example: $F_X(3)$ for a die roll is $P(X \in \{1, 2, 3\}) = 0.5$.

---

## Card 18

**Q:** Term: Probability Density Function (PDF)

**A:** Definition: A function $f_X(x)$ used for continuous random variables where the integral over an interval gives the probability. Example: $f_X(x) = 1$ for $x \in [0, 1]$ for a uniform distribution.

---

## Card 19

**Q:** What is the probability $P(X=x)$ for a continuous random variable $X$?

**A:** $P(X=x) = 0$ for any specific value $x$.

---

## Card 20

**Q:** Formula: Expected value of a continuous random variable $X$

**A:** $E[X] = \int_{-\infty}^{\infty} x f_X(x) dx$.

---

## Card 21

**Q:** How is $E[g(X)]$ calculated for a continuous random variable?

**A:** $E[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x) dx$, known as the Law of the Unconscious Statistician.

---

## Card 22

**Q:** Formula: PDF of a Normal (Gaussian) Distribution

**A:** $f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}$, where $\mu$ is the mean and $\sigma$ is the standard deviation.

---

## Card 23

**Q:** Term: Standard Normal Distribution

**A:** Definition: A normal distribution with a mean $\mu = 0$ and a standard deviation $\sigma = 1$. Example: The $Z$-distribution used in statistical tables.

---

## Card 24

**Q:** Formula: Standardising a normal random variable $X \sim N(\mu, \sigma^2)$

**A:** $Z = \frac{X - \mu}{\sigma}$, transforming $X$ into a standard normal variable.

---

## Card 25

**Q:** Condition for the independence of random variables $X$ and $Y$

**A:** $f_{X,Y}(x,y) = f_X(x)f_Y(y)$ for all $x, y$ (joint density equals product of marginals).

---

## Card 26

**Q:** Formula: Marginal PDF $f_X(x)$ from a joint PDF $f_{X,Y}(x,y)$

**A:** $f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) dy$.

---

## Card 27

**Q:** Formula: Conditional PDF $f_{X|Y}(x|y)$

**A:** $f_{X|Y}(x|y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}$, where $f_Y(y) > 0$.

---

## Card 28

**Q:** Formula: Bayes' Rule for continuous random variables

**A:** $f_{\Theta|X}(\theta|x) = \frac{f_{X|\Theta}(x|\theta) f_{\Theta}(\theta)}{f_X(x)}$.

---

## Card 29

**Q:** Term: Memorylessness

**A:** Definition: A property where the remaining time until an event occurs does not depend on how much time has already passed. Example: The exponential distribution in a Poisson process.

---

## Card 30

**Q:** Formula: Law of Iterated Expectations

**A:** $E[X] = E[E[X|Y]]$, averaging conditional expectations over all possible values of $Y$.

---

## Card 31

**Q:** Formula: Law of Total Variance

**A:** $Var(X) = E[Var(X|Y)] + Var(E[X|Y])$.

---

## Card 32

**Q:** Term: Bernoulli Process

**A:** Definition: A sequence of independent and identically distributed Bernoulli trials. Example: Repeated independent coin tosses with the same $p$.

---

## Card 33

**Q:** Term: Poisson Process

**A:** Definition: A continuous-time process where arrivals occur independently at a constant rate $\lambda$. Example: Modelling the number of emails received per hour.

---

## Card 34

**Q:** Formula: Poisson PMF for $k$ arrivals in time $t$

**A:** $P(k, t) = \frac{(\lambda t)^k e^{-\lambda t}}{k!}$, where $\lambda$ is the arrival rate.

---

## Card 35

**Q:** Term: Markov Chain

**A:** Definition: A stochastic process where the future state depends only on the current state and not on the sequence of events that preceded it. Example: A simple weather model (Sunny/Rainy).

---

## Card 36

**Q:** Term: Central Limit Theorem (CLT)

**A:** Definition: The theory that the sum of many independent, identically distributed variables tends toward a normal distribution as $n$ increases. Example: The distribution of sample means from any population becoming Gaussian.

---

## Card 37

**Q:** Term: Weak Law of Large Numbers

**A:** Definition: As sample size $n$ grows, the sample mean converges in probability to the true population mean. Example: The average of many die rolls approaching 3.5.

---

## Card 38

**Q:** Common Pitfall: Covariance vs. Independence

**A:** Zero covariance does not imply independence; it only indicates a lack of linear correlation. Example: $X$ and $X^2$ can have zero covariance if $X$ is symmetric about zero.

---

## Card 39

**Q:** What is the key insight behind the derived PDF of $Y = g(X)$ for monotonic $g$?

**A:** $f_Y(y) = f_X(x) |\frac{dx}{dy}|$, where the derivative accounts for the stretching or compressing of the probability mass.

---

## Card 40

**Q:** How is the probability $P(A|B)$ revised if $A$ and $B$ are independent?

**A:** $P(A|B) = P(A)$, as the occurrence of $B$ provides no new information about $A$.

---

## Card 41

**Q:** Term: Maximum Likelihood Estimation (MLE)

**A:** Definition: A method of estimating parameters by choosing values that maximise the likelihood of the observed data. Example: Estimating $p$ for a coin by the frequency of heads.

---

## Card 42

**Q:** Term: Maximum a Posteriori (MAP) Estimation

**A:** Definition: A Bayesian method that estimates parameters by finding the mode of the posterior distribution. Example: Updating a prior belief about a parameter using observed data samples.

---

## Card 43

**Q:** What is the difference between Bayesian and Classical inference?

**A:** Bayesian inference treats parameters as random variables with prior distributions; Classical inference treats them as unknown constants.

---

## Card 44

**Q:** Formula: Covariance of $X$ and $Y$

**A:** $Cov(X,Y) = E[XY] - E[X]E[Y]$.

---

## Card 45

**Q:** Formula: Expected value of a Bernoulli random variable

**A:** $E[X] = p$, where $p$ is the probability of success.

---

## Card 46

**Q:** Formula: Variance of a Bernoulli random variable

**A:** $Var(X) = p(1-p)$.

---

## Card 47

**Q:** Formula: Expected value of a Geometric random variable

**A:** $E[X] = \frac{1}{p}$.

---

## Card 48

**Q:** How are inter-arrival times distributed in a Poisson process?

**A:** They are independent and identically distributed exponential random variables with parameter $\lambda$.

---

## Card 49

**Q:** Formula: PDF of an Exponential random variable

**A:** $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$.

---

## Card 50

**Q:** What is the result of merging two independent Poisson processes with rates $\lambda_1$ and $\lambda_2$?

**A:** A new Poisson process with an arrival rate of $\lambda = \lambda_1 + \lambda_2$.

---

## Card 51

**Q:** Term: Pairwise Independence

**A:** Definition: A condition where every pair of events in a set is independent, but the set as a whole may not be mutually independent. Example: Three events where any two don't affect each other, but the third is determined by the first two.

---

## Card 52

**Q:** Formula: Expectation of the sum of random variables

**A:** $E[X_1 + ... + X_n] = E[X_1] + ... + E[X_n]$, regardless of whether they are independent.

---

## Card 53

**Q:** Condition for $Var(X + Y) = Var(X) + Var(Y)$

**A:** The random variables $X$ and $Y$ must be independent (or at least uncorrelated).

---

## Card 54

**Q:** Formula: Expected value of a continuous Uniform distribution on $[a, b]$

**A:** $E[X] = \frac{a+b}{2}$.

---

## Card 55

**Q:** Formula: Variance of a continuous Uniform distribution on $[a, b]$

**A:** $Var(X) = \frac{(b-a)^2}{12}$.

---

## Card 56

**Q:** Term: Joint PMF

**A:** Definition: A function giving the probability that several discrete random variables take on specific values simultaneously. Example: $P_{X,Y}(x,y) = P(X=x, Y=y)$.

---

## Card 57

**Q:** What defines the 'memorylessness' of the geometric distribution?

**A:** The probability of needing $k$ more trials for a success is the same regardless of how many failures occurred previously.

---

## Card 58

**Q:** Formula: Mean of a Poisson random variable

**A:** $E[X] = \lambda$.

---

## Card 59

**Q:** Formula: Variance of a Poisson random variable

**A:** $Var(X) = \lambda$.

---

## Card 60

**Q:** How does the sample mean $\bar{X}$ behave as $n \to \infty$ according to the CLT?

**A:** The distribution of $\bar{X}$ becomes normal with mean $\mu$ and variance $\frac{\sigma^2}{n}$.

---

## Card 61

**Q:** Term: Likelihood Ratio

**A:** Definition: The ratio of the probability of observed data under hypothesis $H_1$ to the probability under $H_0$. Example: $L(x) = \frac{P(x|H_1)}{P(x|H_0)}$.

---

## Card 62

**Q:** Formula: Bayes' Rule for mixed variables (Discrete $\Theta$, Continuous $X$)

**A:** $P(\Theta = \theta | X = x) = \frac{f_{X|\Theta}(x|\theta) P(\Theta = \theta)}{f_X(x)}$.

---

## Card 63

**Q:** What is the key insight behind the 'Poisson approximation' of the Binomial?

**A:** It is valid when $n$ is large and $p$ is small, such that $np = \lambda$ is a constant moderate value.

---

## Card 64

**Q:** Term: Standard Deviation

**A:** Definition: The positive square root of the variance, measuring dispersion in the same units as the data. Example: $\sigma = \sqrt{Var(X)}$.

---

## Card 65

**Q:** Formula: Expectation of a product of independent random variables

**A:** $E[XY] = E[X]E[Y]$.

---

## Card 66

**Q:** What property do all legitimate probability laws share regarding total mass?

**A:** The total probability assigned to the sample space must always sum (discrete) or integrate (continuous) to 1.

---

## Card 67

**Q:** Term: Prior Probability

**A:** Definition: The probability of an event or parameter value before any new data is observed. Example: Assuming a coin is fair ($p=0.5$) before flipping it.

---

## Card 68

**Q:** Term: Posterior Probability

**A:** Definition: The revised probability of an event or parameter after taking into account new evidence. Example: Updating the probability a coin is biased after seeing 10 heads in a row.

---

## Card 69

**Q:** How is the conditional expectation $E[X|Y=y]$ viewed when $y$ is not specified?

**A:** It is viewed as a random variable $E[X|Y]$ that is a function of the random variable $Y$.

---

## Card 70

**Q:** Formula: Number of ways to arrange $n$ distinct items (Permutations)

**A:** $n! = n \times (n-1) \times ... \times 1$.

---
