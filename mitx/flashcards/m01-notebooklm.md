

## Card 1

**Q:** Term: Random Variable

**A:** Definition: A function that assigns a numerical value to each event within a sample space. Example: Assigning 1 to 'heads' and -1 to 'tails' in a coin-flip experiment.

---

## Card 2

**Q:** What is the probability that a continuous random variable takes on a specific, exact value $x_0$?

**A:** The probability is zero, as points on a line have 'measure zero' in a continuous distribution.

---

## Card 3

**Q:** Under what condition is an event with zero probability in a continuous distribution considered possible?

**A:** An event with zero probability is possible if it corresponds to a point within a continuous sample space, such as picking a specific real number between 0 and 1.

---

## Card 4

**Q:** What two conditions must a function $p(x)$ satisfy to be a valid probability distribution?

**A:** The function must be non-negative ($p(x) \ge 0$) and its sum or integral over the sample space must equal 1.

---

## Card 5

**Q:** Term: Cumulative Distribution Function (CDF)

**A:** Definition: A function $F(x)$ that gives the probability that a random variable $X$ is less than or equal to a specific value $x$. Example: Using a normal CDF to find the probability that a daily stock return is less than 2%.

---

## Card 6

**Q:** Formula: Probability density function ($p(x)$) derived from the CDF ($F(x)$)

**A:** $p(x) = \frac{dF(x)}{dx}$, where $p(x)$ is the probability density and $F(x)$ is the cumulative distribution function.

---

## Card 7

**Q:** Formula: Probability that a random variable $X$ lies within the range $(a, b)$ using its CDF

**A:** $Prob(a < X < b) = F(b) - F(a)$, where $F$ is the cumulative distribution function.

---

## Card 8

**Q:** Formula: Change of variable for a probability density $p(x)$ under the transformation $x \to y(x)$

**A:** $g(y) = \frac{p(x)}{|dy/dx|}$, where $g(y)$ is the density of the new variable and $p(x)$ is the original density.

---

## Card 9

**Q:** Pitfall: What must be used in the change of variable formula if the transformation function $y(x)$ is not strictly increasing?

**A:** An absolute value ($|dy/dx|$) is required to ensure the resulting density remains positive.

---

## Card 10

**Q:** Term: Expected Value (Expectation)

**A:** Definition: The weighted average of all possible values of a random variable, using probabilities as weights. Example: Calculating the average outcome of a dice roll by multiplying each face value by $1/6$.

---

## Card 11

**Q:** Formula: Expected value $E[f(X)]$ for a continuous random variable

**A:** $E[f] = \int_{-\infty}^{\infty} f(x)p(x)dx$, where $f(x)$ is the function of the random variable and $p(x)$ is its density.

---

## Card 12

**Q:** Term: Mean of a distribution

**A:** Definition: The first moment of a distribution, representing the expectation of the random variable itself. Example: The mean of a standard fair die roll is 3.5.

---

## Card 13

**Q:** Pitfall: Under what circumstances might the mean of a distribution fail to exist?

**A:** The mean may not exist if the sample space is infinite and the associated integral or sum does not converge.

---

## Card 14

**Q:** Term: Variance

**A:** Definition: A measure of dispersion representing the expectation of the squared deviation of a random variable from its mean. Example: Measuring the volatility of asset returns over a specific period.

---

## Card 15

**Q:** Formula: Variance ($\sigma^2$)

**A:** $\sigma^2 = E[(X - \mu)^2] = \int (x - \mu)^2 p(x)dx$, where $X$ is the random variable, $\mu$ is the mean, and $p(x)$ is the density.

---

## Card 16

**Q:** Term: Skewness

**A:** Definition: A dimensionless asymmetry parameter based on the third moment of a distribution. Example: A distribution of wealth typically shows positive skewness with a long tail to the right.

---

## Card 17

**Q:** Formula: Skewness ($s$)

**A:** $s = E[(\frac{X - \mu}{\sigma})^3]$, where $\mu$ is the mean and $\sigma$ is the standard deviation.

---

## Card 18

**Q:** Term: Kurtosis

**A:** Definition: A measure of the 'weight' of the distribution tails based on the fourth moment. Example: Financial returns often exhibit 'fat tails' or high kurtosis compared to a normal distribution.

---

## Card 19

**Q:** Formula: Kurtosis ($\kappa$) for a distribution relative to a Gaussian

**A:** $\kappa = \frac{E[(X - \mu)^4]}{\sigma^4} - 3$, where $\mu$ is the mean and $\sigma$ is the standard deviation.

---

## Card 20

**Q:** Formula: Covariance of two random variables $X$ and $Y$

**A:** $Cov(X, Y) = E[XY] - \mu_x \mu_y$, where $E[XY]$ is the expectation of their product and $\mu$ represents their respective means.

---

## Card 21

**Q:** Formula: Correlation coefficient $\rho(X, Y)$

**A:** $\rho(X, Y) = \frac{Cov(X, Y)}{\sqrt{Var(X)Var(Y)}}$, where $Cov$ is covariance and $Var$ is variance.

---

## Card 22

**Q:** What is the numerical range of the correlation coefficient $\rho(X, Y)$?

**A:** $-1 \le \rho(X, Y) \le +1$.

---

## Card 23

**Q:** Pitfall: If $Cov(X, Y) = 0$, can we conclude that $X$ and $Y$ are independent?

**A:** No; zero covariance (uncorrelatedness) does not imply independence, as demonstrated by non-linear dependencies like $Y = X^2$ for symmetric distributions.

---

## Card 24

**Q:** Formula: Probability density of a standard Uniform distribution on $[0, 1]$

**A:** $p(x) = 1$ for $x \in [0, 1]$ and $0$ otherwise.

---

## Card 25

**Q:** Formula: Mean of a standard Uniform distribution $[0, 1]$

**A:** $\mu = 1/2$.

---

## Card 26

**Q:** Formula: Variance of a standard Uniform distribution $[0, 1]$

**A:** $\sigma^2 = 1/12$.

---

## Card 27

**Q:** Term: Binomial Distribution

**A:** Definition: A discrete distribution modelling the number of successes in $n$ independent Bernoulli trials with success probability $p$. Example: Modelling the number of bond defaults in a portfolio of 100 independent loans.

---

## Card 28

**Q:** Formula: Binomial probability mass function $f(k; n, p)$

**A:** $f(k; n, p) = \binom{n}{k} p^k q^{n-k}$, where $n$ is trials, $k$ is successes, $p$ is success probability, and $q = 1 - p$.

---

## Card 29

**Q:** Formula: Binomial coefficient $\binom{n}{k}$

**A:** $\binom{n}{k} = \frac{n!}{k!(n - k)!}$, representing the number of ways to choose $k$ items from $n$.

---

## Card 30

**Q:** How is the mean of a Binomial distribution derived using the 'easy way'?

**A:** The total number of successes is treated as a sum of $n$ independent Bernoulli random variables, each with an expectation of $p$.

---

## Card 31

**Q:** Formula: Mean of a Binomial distribution

**A:** $\mu = np$, where $n$ is the number of trials and $p$ is the probability of success.

---

## Card 32

**Q:** What is the key insight behind using a scaling variable $z$ for the Binomial distribution?

**A:** It allows the Binomial distribution to be approximated by a standard Gaussian distribution as the number of trials $n$ becomes large.

**E:** The core intuition behind the scaling variable \(z\) is standardization. As the number of trials \(n\) increases in a Binomial distribution, its expected value \(np\) shifts to the right and its variance \(npq\) grows [1, 2]. To analyze its limiting shape without the bulk of the distribution shifting away and spreading infinitely, we must re-center and resize it [3]. We define the scaling variable \(z\) by subtracting the mean and dividing by the standard deviation: 
\[z = \frac{k - np}{\sqrt{npq}}\] 
This creates a standardized random variable with a mean of \(0\) and a variance of \(1\) [4, 5]. Holding the distribution on this stable scale reveals its underlying symmetry, showing that it asymptotically converges to the standard Gaussian (normal) probability density function, \(\frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}}\) [6, 7].

This elegant result relies fundamentally on the Central Limit Theorem [8]. A Binomial random variable is defined as the sum of \(n\) independent and identically distributed (IID) Bernoulli random variables (where each trial is a success or failure) [9]. The Central Limit Theorem proves that as \(n\) becomes sufficiently large, the standardized sum of any IID variables will converge to a normal distribution [10]. This is a powerful computational shortcut in quantitative modeling, allowing us to replace computationally heavy factorials with simple Gaussian integrals [11, 12]. 

However, practitioners must be wary of two common pitfalls when applying this approximation. First, you must account for the fact that the Binomial distribution is discrete, whereas the Gaussian is continuous [13]. To accurately map discrete outcomes to a continuous curve, you must apply a **continuity correction**; for example, to approximate the probability of exactly \(19\) successes, you should integrate the normal distribution over the continuous interval \([18.5, 19.5]\) [14]. Second, while the Gaussian approximation is highly accurate in the "bulk" of the distribution near the mean, convergence is much slower in the extreme tails [15]. Because the Binomial is bounded between \(0\) and \(n\) while the Gaussian extends to infinity, relying on the Gaussian limit to estimate extreme tail probabilities can lead to significant errors [16, 17].

---

## Card 33

**Q:** In the Bloomberg terminal example with $n=120$ students and demand probability $p=7.5\%$, what does the cumulative probability for $k \le 9$ represent?

**A:** It represents the probability that 9 or fewer terminals will be demanded simultaneously, ensuring no student has to wait.

---

## Card 34

**Q:** How is the distribution of the sum of two independent random variables calculated?

**A:** It is calculated using the convolution of their individual probability density functions.

---

## Card 35

**Q:** Formula: Convolution of densities $p_1$ and $p_2$ for the sum $X_1 + X_2$

**A:** $p(x) = \int_{-\infty}^{\infty} p_1(x_1)p_2(x - x_1)dx_1$, where $p$ is the resulting density of the sum.

---

## Card 36

**Q:** What is the characteristic shape of the distribution formed by the sum of two independent standard Uniform distributions $[0, 1]$?

**A:** A triangular distribution on the interval $[0, 2]$.

---

## Card 37

**Q:** In a series of Bernoulli trials, how is the probability of the first success occurring at exactly trial $n$ calculated?

**A:** $Prob(T = n) = q^{n-1}p$, which accounts for $n-1$ failures followed by a single success.

**E:** To understand the probability of the first success occurring at exactly trial \(n\), we model the scenario as a Bernoulli process. This process consists of a sequence of independent trials, each yielding either a success with probability \(p\) or a failure with probability \(q = 1 - p\) [1], [2]. For the very first success to occur on the \(n\)-th attempt, a precise sequence of events must happen: the first \(n-1\) trials must all be failures, and the \(n\)-th trial must be a success [3], [4]. Because the trials are strictly independent, the joint probability of this exact sequence is simply the product of their individual probabilities [4]. This derivation yields the probability mass function for a geometric random variable: 
\[ \text{Prob}(T = n) = q^{n-1}p \]
where \(T\) represents the discrete random variable for the number of trials until the first success [5], [6].

This mathematical formulation relies heavily on two rigorous assumptions. First, the probability of success, \(p\), must remain absolutely constant across all trials [7]. Second, the trials must be statistically independent, meaning the outcome of any given trial conveys zero information about the outcomes of future trials [2], [8]. This strict independence gives rise to the "memoryless" property of the geometric distribution. If you have already observed a string of failures, the probability distribution of the *remaining* number of trials until a success is mathematically identical to that of a process that is just starting from scratch [9], [10]. 

A common pitfall for students is confusing the geometric distribution with the binomial distribution. The geometric formulation calculates the exact trial of the *first* success, whereas the binomial distribution calculates the probability of seeing a certain number of successes *anywhere* within a fixed window of \(n\) trials [11]. Another frequent trap involves the "gambler's fallacy," which is a failure to internalize the memoryless property [12]. In a true Bernoulli process, a long streak of failures does not mean a success is somehow "due"; the conditional probability of success on the very next trial remains exactly \(p\), irrespective of how many failures have previously occurred [12], [10].

---

## Card 38

**Q:** Term: Markov Property

**A:** Definition: The property where future expectations depend only on the current state, not on the history of events. Example: In a series of fair coin flips, the probability of the next flip being heads is $1/2$ regardless of the previous ten results.

---

## Card 39

**Q:** Term: Central Limit Theorem (CLT)

**A:** Definition: The theorem stating that the sum of a large number of independent, identically distributed (IID) variables approaches a Gaussian distribution. Example: The distribution of the average height of 10,000 randomly selected people approaching a bell curve.

---

## Card 40

**Q:** Formula: Characteristic function $\tilde{f}(t)$ of a distribution

**A:** $\tilde{f}(t) = E[e^{itX}]$, where $i$ is the imaginary unit and $X$ is the random variable.

---

## Card 41

**Q:** How do characteristic functions behave when independent random variables are added?

**A:** The characteristic function of the sum is the product of the individual characteristic functions.

---

## Card 42

**Q:** Formula: First cumulant $C_1$ in terms of moments

**A:** $C_1 = \langle X \rangle$, which corresponds to the mean of the distribution.

---

## Card 43

**Q:** Formula: Second cumulant $C_2$ in terms of moments

**A:** $C_2 = \langle X^2 \rangle - \langle X \rangle^2$, which corresponds to the variance of the distribution.

---

## Card 44

**Q:** What is a unique property of the cumulants of a Gaussian distribution for $n > 2$?

**A:** All cumulants of a Gaussian distribution are exactly zero for $n > 2$.

**E:** To understand this property, we must look at how cumulants are mathematically defined. Cumulants, denoted as \( C_n \), are derived from the cumulant-generating function, which is simply the natural logarithm of a distribution's characteristic function [1]. To extract the \( n \)-th cumulant, you take the \( n \)-th derivative of this logarithmic function and evaluate it at zero [2]. For a Gaussian distribution, the characteristic function inherently takes the form of an exponential of a quadratic polynomial [3]. When you take the natural logarithm of this characteristic function, the exponential cancels out, leaving you with only a strictly quadratic function [4]. Because taking the derivative of a quadratic equation more than twice mathematically yields zero, any derivative of order \( n > 2 \) vanishes identically. Thus, all higher-order cumulants for a Gaussian are exactly zero [2], [4].

Intuitively, you can think of cumulants as isolation metrics for the "non-Gaussian" characteristics of a random variable. The first two cumulants, \( C_1 \) and \( C_2 \), correspond to the mean and the variance—the only two parameters needed to completely map a Gaussian distribution [2], [4]. Higher-order cumulants measure further shape deviations from the normal curve, such as asymmetry (skewness, tied to \( C_3 \)) and the weight of the tails (excess kurtosis, tied to \( C_4 \)) [5], [6], [2]. Because a true Gaussian is perfectly symmetric and lacks fat tails, its skewness and excess kurtosis are exactly zero [7]. This specific phenomenon is the fundamental mechanical engine driving the Central Limit Theorem: as you add many independent random variables together, their scaled higher-order cumulants decay to zero, stripping away all non-normal shape characteristics and leaving only the universal Gaussian structure defined by the first two cumulants [8], [9]. 

A common pitfall is confusing cumulants with raw or central **moments**. While all cumulants above the second order are zero for a Gaussian [4], the higher-order raw moments (such as \( E[X^4] \)) and even central moments are strictly non-zero. Students often mistakenly assume that because a Gaussian has zero excess kurtosis, its fourth moment itself must be zero; in reality, it is only the cumulant—which is a specific linear combination of moments designed to isolate the "excess" shape—that vanishes [2], [4]. Another key assumption to keep in mind is the existence of the moments themselves. If a distribution exhibits severe power-law "fat tails," the higher-order moments and expectations diverge to infinity [10], [11]. In such cases, the cumulants do not exist, the expansion breaks down, and the Gaussian convergence guaranteed by the Central Limit Theorem fails [12], [13].

---

## Card 45

**Q:** How do the dimensionless, normalised cumulants of a sum of $N$ IID variables scale with $N$?

**A:** They have a power-law dependence on $N$, specifically vanishing as $N \to \infty$ for $n > 2$.

---

## Card 46

**Q:** Pitfall: Does the Central Limit Theorem provide information about the rate of convergence in the tails of a distribution?

**A:** No; the CLT describes the approach to a Gaussian but provides no specific information about convergence rates for different values of $x$, particularly in the tails.

---

## Card 47

**Q:** What happens to the Fourier transform of a Gaussian distribution?

**A:** The Fourier transform of a Gaussian distribution is also a Gaussian distribution.

**E:** The flashcard highlights a beautiful and unique property of the normal distribution: it retains its exponential quadratic shape when mapped into the frequency domain. In quantitative finance and probability, we typically encounter the Fourier transform of a probability density function as the characteristic function, defined as the expectation \( \mathbb{E}[\exp(itX)] \) [1, 2]. If a random variable \( X \) follows a Gaussian distribution with mean \( \mu \) and variance \( \sigma^2 \), its probability density function contains an exponential of the form \( \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right) \). Taking the Fourier transform yields \( \exp\left(-\frac{\sigma^2 t^2}{2} + i\mu t\right) \) [3, 4]. This transformed function remains an exponential with a squared argument, meaning it is still fundamentally a Gaussian curve.

The intuition for why this property is so powerful lies in the aggregation of risk and the addition of random variables. When you add independent random variables, their resulting probability distribution is the convolution of their individual distributions [5]. Convolution is mathematically tedious, but the Fourier transform converts a convolution into a simple multiplication [6]. Because multiplying Gaussian Fourier transforms just involves adding their quadratic exponents, the sum of Gaussian random variables is always exactly Gaussian [4, 7, 8]. The key assumption required to leverage this additive property is that the random variables being summed must be statistically independent [9]. 

A common pitfall for students is misplacing the variance parameter \( \sigma^2 \) when mapping between the spatial and frequency domains. In the standard probability density function, the variance \( \sigma^2 \) sits in the denominator of the exponent. However, in the Fourier transform, the \( \sigma^2 \) term moves to the numerator [3, 4]. Conceptually, this demonstrates the uncertainty principle inherent to Fourier transforms: a narrow probability distribution (small \( \sigma^2 \)) translates to a very wide, spread-out characteristic function, and vice versa. Failing to invert the position of the variance is a frequent source of algebraic errors when deriving moments from the characteristic function.

---

## Card 48

**Q:** How is the variance of a sum of random variables calculated when they are perfectly correlated ($\rho = 1$)?

**A:** The variance of the sum equals the square of the sum of the individual standard deviations.

---

## Card 49

**Q:** Formula: Variance of a sum of $N$ uncorrelated variables with identical weights and variances

**A:** $\sigma_p^2 = \frac{\sigma_0^2}{N}$, where $\sigma_0^2$ is the individual variance and $N$ is the number of variables.

---

## Card 50

**Q:** What constitutes a 'stochastic process' in the context of sums of random variables?

**A:** A sequence of sums where the variables are ordered in time.

---

## Card 51

**Q:** In the context of Bernoulli trials, what does 'lack of memory' imply for expected waiting times?

**A:** The expected waiting time from any point forward remains constant, regardless of how long the observer has already been waiting.

---

## Card 52

**Q:** Why is the CDF often easier to approximate from empirical data than the PDF?

**A:** The CDF is based on cumulative counts which are less sensitive to noise in small data samples compared to local density estimates.

---

## Card 53

**Q:** How does the linearity of the expectation operator simplify the analysis of sums of random variables?

**A:** It allows the expectation of a sum to be calculated as the sum of the individual expectations, regardless of whether the variables are independent.

---

## Card 54

**Q:** In the Binomial PMF, what does the term $p^k q^{n-k}$ represent for a single string of results?

**A:** It represents the joint probability of exactly $k$ independent successes and $n-k$ independent failures occurring in a specific sequence.

---

## Card 55

**Q:** If $Y = X_1 + X_2$, what is the relationship between their characteristic functions $\tilde{p}_1(t)$ and $\tilde{p}_2(t)$?

**A:** $\tilde{p}(t) = \tilde{p}_1(t) \tilde{p}_2(t)$.

---

## Card 56

**Q:** The expectation of powers of a random variable are collectively known as the _____ of a distribution.

**A:** Moments

---

## Card 57

**Q:** A random variable that can take an uncountably infinite number of values is classified as _____.

**A:** Continuous

---

## Card 58

**Q:** What is the result of integrating a probability density function from $-\infty$ to $+\infty$?

**A:** 1

**E:** PLAIN ENGLISH

Imagine a probability density function as a map of sand spread out over a table. The height of the sand at any given spot tells you how likely it is for a random event to land there. If you want to know the chance of the event landing in a specific section, you simply measure the amount of sand in that area. 

If you sweep your hands across the *entire* table, gathering up every single grain of sand from one end to the other, you have collected 100% of the sand [1, 2]. In probability, 100% certainty is represented by the number 1. Because it is absolutely guaranteed that your random event will have *some* outcome, gathering up all the probabilities across every possible outcome will always give you a total of 1 [2, 3]. 

STEP-BY-STEP

Here is how we formally derive this result using the rules of continuous probability:

**Step 1:** We use the continuous probability definition — the probability that a continuous random variable \(X\) falls between two values, \(a\) and \(b\), is calculated by taking the definite integral of its probability density function, \(p(x)\), between those two limits [4, 5]. 
\[ P(a \le X \le b) = \int_{a}^{b} p(x) \,dx \]

**Step 2:** We use the infinite limits substitution — to find the probability of all possible outcomes, we must extend our interval to cover the entire real number line. We do this by replacing \(a\) with \(-\infty\) and \(b\) with \(+\infty\) [3].
\[ P(-\infty < X < +\infty) = \int_{-\infty}^{+\infty} p(x) \,dx \]

**Step 3:** We use the total probability axiom — it is a foundational rule of probability that an outcome is absolutely certain to be *some* real number, and the probability of a certain event is exactly \(1\) [2]. 
\[ P(-\infty < X < +\infty) = 1 \]

**Step 4:** We use the transitive property of equality — since the integral from negative to positive infinity represents the total probability (from Step 2), and the total probability must equal \(1\) (from Step 3), the integral itself must equal \(1\) [3].
\[ \int_{-\infty}^{+\infty} p(x) \,dx = 1 \]

THE TAKEAWAY

The single most important thing to remember is that the total area under any valid probability density function curve must always be exactly \(1\), representing 100% certainty that some outcome will occur [2]. In practice, this "normalization" rule is essential because it allows us to check if a probability model is valid, or to solve for missing constants to ensure the density function behaves correctly [6, 7].

CONCRETE EXAMPLE

Let's look at a "uniform distribution," where an event is equally likely to happen anywhere within a specific window [8]. Imagine a computer program generates a completely random number between \(0\) and \(4\). 

Because the number is guaranteed to be between \(0\) and \(4\), the density function \(p(x)\) is \(0\) everywhere outside this window. To make the total area equal to \(1\), the height of the density function must be a constant \(1/4\) over this interval [6].

Let's integrate this density function from \(-\infty\) to \(+\infty\):
\[ \int_{-\infty}^{+\infty} p(x) \,dx = \int_{0}^{4} \frac{1}{4} \,dx \]

We find the antiderivative and evaluate it from \(0\) to \(4\):
\[ \left[ \frac{x}{4} \right]_{0}^{4} = \frac{4}{4} - \frac{0}{4} = 1 \]
The total area perfectly sums to \(1\).

WATCH OUT

A very common mistake students make is confusing the *value* of the density function, \(p(x)\), with an actual probability. Remember, densities are *not* probabilities; they are probabilities per unit length [9]. Therefore, a density function can actually have a value greater than \(1\) at a specific point [10]. For example, if a random number is always between \(0\) and \(0.5\), the height of the density function would be \(2\). This is perfectly fine, as long as the *total area* under the curve (the integral from \(-\infty\) to \(+\infty\)) still equals exactly \(1\) [10].

---

## Card 59

**Q:** In the expression $E[(X - \mu)^2]$, the term $\mu$ represents the _____ of the distribution.

**A:** Mean

---

## Card 60

**Q:** Which moment-based parameter would you use to determine if a distribution has fat tails?

**A:** Kurtosis

---

## Card 61

**Q:** How does correlation differ from covariance in terms of units?

**A:** Covariance has units (the product of the variables' units), whereas correlation is a dimensionless 'pure' number.

---

## Card 62

**Q:** In the Binomial distribution, what is the probability of failure $q$ defined as?

**A:** $q = 1 - p$.

---

## Card 63

**Q:** What is the variance of a single Bernoulli trial with success probability $p$?

**A:** $pq$ (or $p(1-p)$).

---

## Card 64

**Q:** The process of using a scaling variable to compare different Gaussian distributions is called _____.

**A:** Standardisation

---

## Card 65

**Q:** If $X$ is a random variable, what is $E[X - E[X]]$?

**A:** 0

---

## Card 66

**Q:** What is the third central moment of a perfectly symmetric distribution?

**A:** 0

---

## Card 67

**Q:** In the wait-time example, if $p = 6/36$, what is the average number of rolls needed to get a seven?

**A:** 6

---

## Card 68

**Q:** What is the key difference between a discrete and continuous sample space regarding the summation of probabilities?

**A:** Discrete spaces use summations ($Σ$), while continuous spaces use integrals ($∫$).

---

## Card 69

**Q:** What is the value of the CDF $F(x)$ as $x \to \infty$?

**A:** 1

---

## Card 70

**Q:** What is the value of the CDF $F(x)$ as $x \to -\infty$?

**A:** 0

---

## Card 71

**Q:** If two random variables are independent, their joint density is the _____ of their individual densities.

**A:** Product

---

## Card 72

**Q:** The standard deviation is the _____ of the variance.

**A:** Square root

---

## Card 73

**Q:** What is the mean of a random variable $Z$ that represents 'success' (1) or 'failure' (0) with probability $p$?

**A:** $p$

---

## Card 74

**Q:** What happens to the variance of the average of $N$ IID variables as $N$ increases?

**A:** It decreases toward zero at a rate of $1/N$.

---

## Card 75

**Q:** Does the sum of two independent Gaussian variables always result in a Gaussian variable?

**A:** Yes.

---
