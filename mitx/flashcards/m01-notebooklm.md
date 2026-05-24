# Probability Flashcards

## Card 1

**Q:** Term: Random Variable

**A:** Definition: A function that assigns a numerical value to each event within a sample space, effectively acting as a random-valued function. Example: Assigning 1 to 'heads' and -1 to 'tails' in a coin toss experiment.

---

## Card 2

**Q:** In a continuous probability distribution, why is the probability of the random variable taking any specific single value $x_0$ equal to zero?

**A:** Because there are an uncountably infinite number of possible values, any individual point has a 'measure zero' despite the event not being impossible.

---

## Card 3

**Q:** Formula: Probability of a continuous random variable falling within a specific range

**A:** $Prob(a < X < b) = \int_{a}^{b} p(x)dx$, where $p(x)$ is the probability density function, and $a$ and $b$ are the lower and upper bounds of the range.

---

## Card 4

**Q:** What is the normalization condition for a discrete probability distribution?

**A:** The sum of probabilities for all possible discrete outcomes $x_k$ must equal one: $\sum_{k} p(x_k) = 1$.

---

## Card 5

**Q:** What is the normalization condition for a continuous probability distribution?

**A:** The total area under the probability density function $p(x)$ across the entire sample space must equal one: $\int_{-\infty}^{\infty} p(x)dx = 1$.

---

## Card 6

**Q:** Term: Cumulative Distribution Function (CDF)

**A:** Definition: A function $F(x)$ that provides the probability that a random variable $X$ is less than or equal to a specific value $x$. Example: Calculating the probability that a student's test score is at most 80%.

---

## Card 7

**Q:** Formula: Relationship between the Probability Density Function and the Cumulative Distribution Function

**A:** $p(x) = \frac{dF(x)}{dx}$, where $p(x)$ is the density function and $F(x)$ is the cumulative distribution function.

---

## Card 8

**Q:** Formula: Calculation of range probability using the Cumulative Distribution Function

**A:** $Prob(a < X < b) = F(b) - F(a)$, where $F$ is the cumulative distribution function and $a$ and $b$ are the range boundaries.

---

## Card 9

**Q:** Formula: Change of variable for a probability density function

**A:** $g(y) = \frac{p(x)}{|dy/dx|}$, where $g(y)$ is the density of the new variable $y(x)$, $p(x)$ is the original density, and $|dy/dx|$ is the absolute value of the derivative of the transformation.

---

## Card 10

**Q:** Pitfall: What is a critical assumption when applying the simple change of variable formula $p(x)dx = g(y)dy$?

**A:** It assumes $y$ is a strictly increasing function of $x$; if not, an absolute value is required, and care must be taken if $y$ has critical points.

---

## Card 11

**Q:** Formula: Expected value of a function of a continuous random variable

**A:** $E[f] = \int_{-\infty}^{\infty} f(x)p(x)dx$, where $f(x)$ is the function of the random variable and $p(x)$ is the probability density function.

---

## Card 12

**Q:** Formula: Expected value of a function of a discrete random variable

**A:** $E[f(X)] = \sum_{k=1}^{n} f(x_k)p(x_k)$, where $x_k$ are the possible outcomes and $p(x_k)$ are their respective probabilities.

---

## Card 13

**Q:** Pitfall: Under what condition is the mean of a distribution not guaranteed to exist?

**A:** In cases of an infinite sample space, the mean may not exist if the integral or sum used to calculate the expectation fails to converge.

---

## Card 14

**Q:** How is the linearity of the expectation operator expressed for the sum of two functions?

**A:** The expectation of a sum equals the sum of the expectations: $E[f(X) + g(X)] = E[f(X)] + E[g(X)]$.

---

## Card 15

**Q:** Formula: Definition of the $l$-th moment of a distribution

**A:** $\mu_l \equiv E[X^l] = \int x^l p(x)dx$ (continuous) or $\sum_k x_k^l p(x_k)$ (discrete), where $l$ is the power of the random variable.

---

## Card 16

**Q:** Formula: Variance in terms of the first and second moments

**A:** $\sigma^2 = E[X^2] - (E[X])^2$, where $E[X^2]$ is the second moment and $E[X]$ is the mean (the first moment).

---

## Card 17

**Q:** How do the units of standard deviation compare to the units of the underlying random variable?

**A:** They are identical, allowing for direct comparison with the random variable's values (e.g. dollars or rates of return).

---

## Card 18

**Q:** Term: Skewness

**A:** Definition: A dimensionless asymmetry parameter based on the third moment of a distribution relative to its standard deviation. Example: Identifying if asset returns are more likely to have extreme negative outliers than positive ones.

---

## Card 19

**Q:** Term: Kurtosis

**A:** Definition: A measure of the 'weight' or thickness of the tails of a probability distribution based on the fourth moment. Example: Determining if a financial model understates the probability of extreme market crashes compared to a Gaussian model.

---

## Card 20

**Q:** Formula: Covariance of two random variables

**A:** $Cov(X, Y) = E[XY] - \mu_x \mu_y$, where $E[XY]$ is the expectation of the product and $\mu_x, \mu_y$ are the respective means.

---

## Card 21

**Q:** Formula: Correlation coefficient between two random variables

**A:** $\rho(X, Y) = \frac{Cov(X, Y)}{\sigma_x \sigma_y}$, where $Cov(X, Y)$ is the covariance and $\sigma_x, \sigma_y$ are the standard deviations of $X$ and $Y$.

---

## Card 22

**Q:** What is the numerical range of the correlation coefficient $\rho(X, Y)$?

**A:** The correlation coefficient is bounded between $-1$ and $+1$ inclusive: $-1 \le \rho(X, Y) \le +1$.

---

## Card 23

**Q:** Pitfall: If the covariance between two variables is zero, can we conclude they are independent?

**A:** No; vanishing covariance is a necessary but not sufficient condition for independence, as non-linear dependencies can still exist while $Cov(X,Y)=0$.

---

## Card 24

**Q:** Term: Uniform Distribution (Standard Form)

**A:** Definition: A continuous distribution where all values within a specified interval $[0, 1]$ are equally likely. Example: A computer generating a random number between zero and one for a simulation.

---

## Card 25

**Q:** What are the mean and variance of a standard uniform distribution on the interval $[0, 1]$?

**A:** The mean $\mu$ is $\frac{1}{2}$ and the variance $\sigma^2$ is $\frac{1}{12}$.

---

## Card 26

**Q:** Term: Binomial Distribution

**A:** Definition: A discrete distribution modelling the number of successes in a fixed number of independent trials with a constant probability of success. Example: Counting the number of heads achieved in ten tosses of a fair coin.

---

## Card 27

**Q:** What are the two parameters that define a binomial distribution?

**A:** The probability of success $p$ and the number of trials $n$.

---

## Card 28

**Q:** Formula: Probability mass function of the binomial distribution

**A:** $f(k; n, p) = \binom{n}{k} p^k q^{n-k}$, where $n$ is the number of trials, $k$ is the number of successes, $p$ is success probability, and $q = 1-p$.

---

## Card 29

**Q:** Formula: Mean of a binomial distribution

**A:** $\mu = np$, where $n$ is the number of trials and $p$ is the probability of success per trial.

---

## Card 30

**Q:** How is the mean of a binomial distribution derived using the expectation formula?

**A:** The key insight is factoring out $np$ from the summation, which allows the remaining terms to be re-indexed and simplified into a sum of probabilities for a binomial distribution with $n-1$ trials.

---

## Card 31

**Q:** How is the variance of a portfolio $R_p$ calculated when assets are correlated?

**A:** $\sigma_p^2 = \sum_{i=1}^{N} w_i^2 \sigma_i^2 + 2 \sum_{i < j} w_i w_j Cov(R_i, R_j)$, where $w$ are weights, $\sigma$ are standard deviations, and $Cov$ is covariance.

---

## Card 32

**Q:** If a set of random variables are independent and identically distributed (IID) with identical weights and variances, how does the portfolio variance $\sigma_p^2$ behave?

**A:** The variance of the sum equals the sum of the individual variances, effectively reducing the portfolio variance relative to the number of assets.

---

## Card 33

**Q:** Term: Characteristic Function

**A:** Definition: A function that completely defines a probability distribution and is defined as the expectation of $e^{itX}$. Example: Using the Fourier transform of a density function to simplify the analysis of sums of random variables.

---

## Card 34

**Q:** Formula: Moment generation from a characteristic function

**A:** $E[X^l] = (-i)^l \left. \frac{d^l}{dt^l} \tilde{f}(t) \right|_{t=0}$, where $l$ is the moment order and $\tilde{f}(t)$ is the characteristic function.

---

## Card 35

**Q:** What is the relationship between the characteristic function of a sum of independent variables and the individual characteristic functions?

**A:** The characteristic function of the sum is the product of the individual characteristic functions.

---

## Card 36

**Q:** How is the moment-generating property of the characteristic function derived?

**A:** The key insight is that differentiating the expectation $E[e^{itX}]$ with respect to $t$ brings down factors of $iX$, allowing moments to be recovered by evaluating at $t=0$.

---

## Card 37

**Q:** What does the Central Limit Theorem (CLT) state regarding the sum of a large number of IID random variables?

**A:** The sum approaches a Gaussian (normal) distribution regardless of the individual variables' original distributions, provided they are well-behaved and have finite variance.

---

## Card 38

**Q:** In the limit of a large number of trials $n$, what distribution does the binomial distribution approach?

**A:** It approaches a Gaussian (Normal) distribution centred at $np$ with variance $npq$.

---

## Card 39

**Q:** Formula: Scaling variable used to demonstrate the Gaussian limit of a binomial distribution

**A:** $z_k = \frac{k - np}{\sqrt{npq}}$, where $k$ is the number of successes, $n$ is trials, $p$ is success probability, and $q = 1-p$.

---

## Card 40

**Q:** Term: Bernoulli Trial

**A:** Definition: A random experiment with exactly two possible outcomes, usually termed 'success' and 'failure', with a fixed probability $p$ for success. Example: A single flip of a coin or a single trade resulting in either a profit or a loss.

---

## Card 41

**Q:** Formula: Mean waiting time to achieve a single success in repeated Bernoulli trials

**A:** $E[T] = \frac{1}{p}$, where $p$ is the probability of success in each independent trial.

---

## Card 42

**Q:** Formula: Variance of the waiting time $T$ in a sequence of Bernoulli trials

**A:** $Var(T) = \frac{1-p}{p^2}$, where $p$ is the constant probability of success.

---

## Card 43

**Q:** How is the variance of the waiting time in Bernoulli trials derived?

**A:** The critical insight is using a derivative trick on the geometric series $\sum q^n = 1/(1-q)$ to evaluate the second moment $E[T^2]$ before applying the variance formula.

---

## Card 44

**Q:** Why is the characteristic function particularly useful for continuous distributions?

**A:** It corresponds to the Fourier transform of the density function, converting the difficult operation of convolution (for sums) into simple multiplication.

---

## Card 45

**Q:** What is a unique property of Gaussians regarding Fourier transforms and characteristic functions?

**A:** The Fourier transform of a Gaussian is itself a Gaussian, meaning the characteristic function of a normal distribution remains normal.

---

## Card 46

**Q:** Term: Binomial Coefficient

**A:** Definition: The number of ways to choose $k$ successes from $n$ trials regardless of order, calculated using factorials. Example: Determining there are 6 ways to get exactly 2 heads in 4 coin flips.

---

## Card 47

**Q:** Formula: Binomial Coefficient (n choose k)

**A:** $\binom{n}{k} = \frac{n!}{k!(n-k)!}$, where $n$ is total items and $k$ is the number of items being selected.

---

## Card 48

**Q:** What defines the standard deviation in terms of the variance?

**A:** The standard deviation is the positive square root of the variance: $\sigma = \sqrt{\sigma^2}$.

---

## Card 49

**Q:** How does correlation relate to covariance conceptually?

**A:** Correlation is a standardised version of covariance that removes units, making it a 'pure number' to facilitate comparison across different variables.

---

## Card 50

**Q:** In the context of asset pricing, why is choosing the right distribution considered a mix of theory and empirical observation?

**A:** While theory provides models like the CLT-justified Gaussian, empirical observations are 'always' required to account for real-world deviations like fat tails or skewness.

---

## Card 51

**Q:** Formula: Probability of an event $X$ taking value $1$ or $0$ in a Bernoulli trial

**A:** $P(Z = 1) = p$ and $P(Z = 0) = q$, where $p + q = 1$.

---

## Card 52

**Q:** What is the key takeaway of using the 'derivative trick' in calculating moments for discrete variables like waiting times?

**A:** It allows one to avoid complex summations by differentiating a known power series (like the geometric series) and evaluating it at a specific value.

---

## Card 53

**Q:** In the 'Bloomberg terminals' example with 120 students and 9 terminals ($p=7.5\%$), what does the cumulative probability $58.75\%$ represent?

**A:** The probability that 9 or fewer students will attempt to use the terminals at the same time.

---
