

## Card 1

**Q:** What are the two core requirements for the list of outcomes in a sample space $\Omega$?

**A:** The outcomes must be mutually exclusive and collectively exhaustive.

---

## Card 2

**Q:** Probability Axiom 1: What is the required range for the probability of any event $A$?

**A:** The probability $P(A)$ must be non-negative ($P(A) \ge 0$).

---

## Card 3

**Q:** Probability Axiom 2: What is the probability of the entire sample space $\Omega$?

**A:** The probability of the entire sample space is exactly 1 ($P(\Omega) = 1$).

---

## Card 4

**Q:** Probability Axiom 3: If two events $A$ and $B$ are disjoint, how is $P(A \cup B)$ calculated?

**A:** It is the sum of their individual probabilities ($P(A) + P(B)$).

---

## Card 5

**Q:** What does 'collectively exhaustive' mean in the context of a sample space?

**A:** It means that no matter what happens in the experiment, one of the listed outcomes must occur.

---

## Card 6

**Q:** What does 'mutually exclusive' mean regarding outcomes in a sample space?

**A:** It means that at the end of the experiment, exactly one of the outcomes can be said to have occurred.

---

## Card 7

**Q:** Under the discrete uniform law, if a sample space has $N$ equally likely outcomes, what is the probability of a subset $A$ containing $n$ elements?

**A:** The probability is $\frac{n}{N}$.

---

## Card 8

**Q:** Which axiom is required to handle the union of an infinite sequence of disjoint events?

**A:** The Countable Additivity Axiom.

---

## Card 9

**Q:** How is a random variable mathematically defined?

**A:** It is a function that assigns a numerical value to every possible outcome in the sample space.

---

## Card 10

**Q:** What is the Probability Mass Function (PMF) of a discrete random variable $X$?

**A:** It is a function $p_X(x)$ that gives the probability that $X$ takes the specific numerical value $x$.

---

## Card 11

**Q:** What is the required sum of the values of a PMF over all possible numerical values of $x$?

**A:** The sum must always be equal to 1.

---

## Card 12

**Q:** Definition: Expected Value ($E[X]$)

**A:** The probability-weighted average of all possible values of the random variable, calculated as $\sum_x x p_X(x)$.

---

## Card 13

**Q:** What physical concept serves as a visual interpretation of the expected value of a random variable?

**A:** The expected value represents the center of gravity of the probability mass distribution.

---

## Card 14

**Q:** How is the expected value of a constant $c$ defined?

**A:** The expected value of a constant is simply the constant itself ($E[c] = c$).

---

## Card 15

**Q:** What is the general formula for the expected value of a linear function $aX + b$?

**A:** It is $aE[X] + b$.

---

## Card 16

**Q:** What does the 'Law of the Unconscious Statistician' allow one to calculate without finding the PMF of $Y$?

**A:** It allows the calculation of $E[g(X)]$ using only the PMF of $X$ via the formula $\sum_x g(x) p_X(x)$.

---

## Card 17

**Q:** Definition: Variance ($Var(X)$)

**A:** The expected squared deviation of a random variable from its mean, defined as $E[(X - E[X])^2]$.

---

## Card 18

**Q:** What is the alternative computational formula for $Var(X)$?

**A:** It is $E[X^2] - (E[X])^2$.

---

## Card 19

**Q:** How does adding a constant $b$ to a random variable $X$ affect its variance?

**A:** Adding a constant does not change the variance ($Var(X + b) = Var(X)$).

---

## Card 20

**Q:** What is the scaling property of variance for the random variable $aX$?

**A:** The variance is scaled by the square of the constant ($Var(aX) = a^2 Var(X)$).

---

## Card 21

**Q:** Under what condition is the expected value of a function $g(X)$ equal to the function of the expected value $g(E[X])$?

**A:** This equality holds only when the function $g$ is linear.

---

## Card 22

**Q:** Scenario: Tossing a coin with probability $p$ of heads until the first head appears. What distribution describes the number of tosses $X$?

**A:** The Geometric Distribution.

---

## Card 23

**Q:** Formula: Geometric PMF for parameter $p$

**A:** $p_X(k) = (1-p)^{k-1}p$ for $k = 1, 2, \dots$.

---

## Card 24

**Q:** Scenario: $n$ independent trials with probability $p$ of success. What distribution describes the total number of successes $k$?

**A:** The Binomial Distribution.

---

## Card 25

**Q:** Formula: Binomial PMF for parameters $n$ and $p$

**A:** $p_X(k) = \binom{n}{k} p^k (1-p)^{n-k}$ for $k = 0, 1, \dots, n$.

---

## Card 26

**Q:** What are the mean and variance of a Binomial($n, p$) random variable?

**A:** The mean is $np$ and the variance is $np(1-p)$.

---

## Card 27

**Q:** A sequence of independent trials where each trial results in success with probability $p$ is called a _____.

**A:** Bernoulli Process

---

## Card 28

**Q:** What defines the 'memorylessness' property of a Bernoulli process?

**A:** The probability of future successes does not depend on the history of previous trials.

---

## Card 29

**Q:** The Poisson process is the continuous-time version of the _____.

**A:** Bernoulli Process

---

## Card 30

**Q:** In a Poisson process with arrival rate $\lambda$, what is the expected number of arrivals in a time interval $t$?

**A:** The expected number of arrivals is $\lambda t$.

---

## Card 31

**Q:** Formula: Poisson PMF for $k$ arrivals in time $t$ with rate $\lambda$

**A:** $P(k, t) = \frac{(\lambda t)^k e^{-\lambda t}}{k!}$.

**E:** The Poisson Probability Mass Function (PMF) models the probability of observing exactly \(k\) discrete events (or arrivals) over a continuous time interval \(t\) [1, 2]. Intuitively, you can think of the Poisson process as the **continuous-time limit of a discrete Bernoulli process** [3]. If you divide the time \(t\) into \(n\) infinitesimally small slots, each slot has a tiny probability of a single arrival equal to \(\lambda \frac{t}{n}\) [4, 5]. Taking the limit as \(n \to \infty\) yields the Poisson PMF:
\[ P(k, t) = \frac{(\lambda t)^k e^{-\lambda t}}{k!} \]
where \(\lambda t\) represents the **expected number of arrivals** during the overall interval [6, 7]. A unique mathematical property of this distribution is that **its variance is exactly equal to its mean**, \(\lambda t\) [8]. 

For this model to be valid, the underlying stochastic process must satisfy three strict mathematical assumptions. First, **time homogeneity**: the probability distribution of arrivals depends only on the length of the time interval, not on its specific placement on the time axis [9, 10]. Second, **independent increments**: the number of arrivals in disjoint (non-overlapping) time intervals must be statistically independent; observing an arrival now provides no information about future arrivals [11-13]. Third, **negligible simultaneous arrivals**: the probability of observing more than one arrival in a microscopic fraction of time \(\delta\) must be negligibly small (mathematically, on the order of \(\delta^2\)) [14-16].

A common pitfall when applying this model to finance—such as modeling the arrival of market orders or credit defaults [1]—is blindly assuming that the arrival rate \(\lambda\) is constant over a long horizon [17]. In reality, **arrival rates often fluctuate throughout the day**, such as increased trading volume near the market open and close [17, 18]. Applying a standard, constant-\(\lambda\) Poisson PMF over a full trading day ignores these variations, thereby violating the time homogeneity assumption and producing inaccurate probabilities [18].

---

## Card 32

**Q:** What is unique about the variance of a Poisson random variable relative to its mean?

**A:** The variance is exactly equal to the mean ($\lambda t$).

---

## Card 33

**Q:** What distribution describes the time until the first arrival in a Poisson process?

**A:** The Exponential Distribution.

---

## Card 34

**Q:** Formula: PDF of an Exponential random variable with rate $\lambda$

**A:** $f_X(x) = \lambda e^{-\lambda x}$ for $x \ge 0$.

---

## Card 35

**Q:** If two independent Poisson processes with rates $\lambda_1$ and $\lambda_2$ are merged, what is the rate of the resulting process?

**A:** The resulting rate is $\lambda_1 + \lambda_2$.

---

## Card 36

**Q:** What is the expected value of a discrete uniform random variable on the range $[0, n]$?

**A:** The expected value is $\frac{n}{2}$.

---

## Card 37

**Q:** Formula: Variance of a continuous uniform distribution on $[0, 1]$

**A:** The variance is $\frac{1}{12}$.

---

## Card 38

**Q:** Formula: PDF of a Gaussian (Normal) distribution with mean $\mu$ and variance $\sigma^2$

**A:** $f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$.

---

## Card 39

**Q:** In a Gaussian distribution, what physical characteristics do $\mu$ and $\sigma$ represent?

**A:** $\mu$ represents the center (peak) and $\sigma$ represents the width of the distribution.

---

## Card 40

**Q:** What defines a standard normal random variable $Z$?

**A:** A normal random variable with mean $\mu = 0$ and standard deviation $\sigma = 1$.

---

## Card 41

**Q:** Concept: Log-normal Distribution

**A:** Definition: A distribution where the logarithm of the random variable follows a normal distribution ($X = \ln Y$).

**E:** A random variable \(Y\) follows a log-normal distribution if its natural logarithm, \(X = \ln(Y)\), is normally distributed [1]. In quantitative finance, this concept is foundational because it serves as the standard starting model for asset prices and return distributions [1]. Intuitively, if we assume that the continuously compounded (logarithmic) returns of an asset follow a normal distribution, then the asset prices themselves are log-normally distributed [1, 2]. This inherently respects the reality of limited liability assets: by modeling prices via the exponentiation of a real-valued normal random variable, it naturally ensures that asset prices remain strictly positive, bounding the domain of \(Y\) to \((0, \infty)\).

The key assumption linking these concepts relies on the formal relationship between a simple return \(R\) and a logarithmic return \(r\), which is defined by the equation:
\[ e^{r} - 1 = R \]
[2]. When deriving the analytical properties of the log-normal distribution, a common pitfall is mishandling the probability density function (PDF). Because the PDF represents a density that must be integrated to yield a probability, you cannot simply substitute \(\ln(Y)\) directly into the normal PDF equation. You must rigorously apply the change of variables formula, which incorporates the derivative of the inverse transformation, to ensure the resulting probability density still integrates to \(1\) [1]. 

Another frequent quantitative pitfall involves computing expected values. Students often incorrectly assume that the expected value of the log-normal variable \(Y\) is simply \(e^{\mu}\), where \(\mu\) is the expected value of the normal variable \(X\). However, because the exponential function \(Y = e^X\) is strictly convex, Jensen's Inequality dictates that the expectation of the exponential is strictly greater than the exponential of the expectation. In finance, failing to account for this convexity—and the variance drag it represents—will lead to fundamentally incorrect asset valuations and expected return calculations.

---

## Card 42

**Q:** What is the 'two-step procedure' for finding the distribution of $Y = g(X)$?

**A:** First find the Cumulative Distribution Function $F_Y(y)$, then differentiate to find the PDF $f_Y(y)$.

---

## Card 43

**Q:** For $Y = aX + b$ (where $a > 0$), how is the PDF $f_Y(y)$ related to $f_X$?

**A:** $f_Y(y) = \frac{1}{a} f_X\left(\frac{y-b}{a}\right)$.

---

## Card 44

**Q:** What is the general formula for the Characteristic Function $\phi_X(t)$?

**A:** $\phi_X(t) = E[e^{itX}]$.

---

## Card 45

**Q:** How can the $n$-th moment of a random variable be recovered from its characteristic function?

**A:** By taking the $n$-th derivative of $\phi_X(t)$ and evaluating it at $t = 0$.

---

## Card 46

**Q:** What is the characteristic function of the sum of two independent random variables $X$ and $Y$?

**A:** It is the product of their individual characteristic functions ($\phi_X(t) \phi_Y(t)$).

---

## Card 47

**Q:** Concept: Convolution

**A:** Definition: The mathematical operation used to find the PDF of the sum of two independent random variables.

---

## Card 48

**Q:** What distribution describes the time until the $k$-th success in a Bernoulli process?

**A:** The Pascal Distribution.

---

## Card 49

**Q:** What distribution describes the time until the $k$-th arrival in a Poisson process?

**A:** The Erlang Distribution (sum of $k$ independent exponentials).

---

## Card 50

**Q:** In Bayesian Inference, what is the 'Prior' distribution?

**A:** The probability distribution that captures initial beliefs about an unknown parameter before any data is observed.

---

## Card 51

**Q:** What is the 'Posterior' distribution in the context of Bayesian Inference?

**A:** The probability distribution of an unknown parameter after accounting for observed data.

---

## Card 52

**Q:** How is the Maximum a Posteriori (MAP) estimate chosen?

**A:** It is the value of the parameter that maximises the posterior probability density or mass function.

---

## Card 53

**Q:** What is the Least Mean Squares (LMS) estimate of an unknown parameter $\Theta$?

**A:** It is the conditional expectation $E[\Theta | X]$.

---

## Card 54

**Q:** The conditional expectation $E[\Theta | X]$ is the best estimate if the objective is to minimise the _____.

**A:** Mean Squared Error

---

## Card 55

**Q:** What does it mean for the LMS estimator to be 'unbiased'?

**A:** It means the expected value of the estimation error is zero ($E[\hat{\Theta} - \Theta] = 0$).

---

## Card 56

**Q:** What is the relationship between the LMS estimation error and the estimate itself?

**A:** The error is uncorrelated with the estimate (their covariance is zero).

---

## Card 57

**Q:** Under the Linear LMS model, how is the slope coefficient $a$ calculated for a single observation $X$?

**A:** $a = \frac{Cov(\Theta, X)}{Var(X)}$.

---

## Card 58

**Q:** What is the Mean Squared Error (MSE) for the optimal Linear LMS estimator with correlation coefficient $\rho$?

**A:** $MSE = (1 - \rho^2) Var(\Theta)$.

**E:** PLAIN ENGLISH
Imagine you are trying to guess a hidden number, like tomorrow's temperature, but you only have a related measurement, like today's barometric pressure. If you have absolutely no measurements, your best guess is just the historical average temperature. In that case, your "error" is just the natural, everyday fluctuation of the temperature—which is its variance [1]. 

However, if you can draw a straight line (a linear model) to connect today's pressure to tomorrow's temperature, you can make a much better guess. The Mean Squared Error (MSE) formula tells us exactly how much your guessing error shrinks when you use that straight line. The shrink depends entirely on the correlation coefficient—how tightly the two measurements move together [2]. If they move together perfectly, your error drops to zero. If they are completely unrelated, your measurement doesn't help at all, and your error remains the original variance [1].

STEP-BY-STEP
While the lecture skips the heavy algebra [3], we can build this beautiful result by combining the optimal slope of a line with the definition of correlation. 

Step 1: Identify the optimal slope. When creating a linear estimator \( \hat{\Theta} = aX + b \), calculus tells us the optimal slope \( a \) that minimizes error is the covariance of the two variables divided by the variance of our data \( X \). 
\[ a = \frac{Cov(X, \Theta)}{Var(X)} \]

Step 2: Recall the definition of the correlation coefficient, \( \rho \). Correlation is the covariance standardized by the standard deviations (the square roots of the variances) of both variables [4]. 
\[ \rho = \frac{Cov(X, \Theta)}{\sqrt{Var(X)Var(\Theta)}} \]

Step 3: Rewrite the covariance using \( \rho \). By multiplying both sides of the Step 2 equation by the denominator, we isolate covariance. We do this so we can substitute it back into our slope formula.
\[ Cov(X, \Theta) = \rho \sqrt{Var(X)Var(\Theta)} \]

Step 4: Substitute the covariance back into the slope formula from Step 1.
\[ a = \frac{\rho \sqrt{Var(X)Var(\Theta)}}{Var(X)} \]
Since \( Var(X) \) is the same as \( \sqrt{Var(X)} \times \sqrt{Var(X)} \), one of the square roots cancels out, leaving:
\[ a = \rho \sqrt{\frac{Var(\Theta)}{Var(X)}} \]

Step 5: Set up the Mean Squared Error (MSE) formula. For an optimal linear estimator, the remaining error variance is always the original variance of \( \Theta \) minus the variance explained by our slope and data, which is \( a^2 Var(X) \).
\[ MSE = Var(\Theta) - a^2 Var(X) \]

Step 6: Substitute our new slope \( a \) into the MSE formula. First, square the slope \( a \):
\[ a^2 = \rho^2 \frac{Var(\Theta)}{Var(X)} \]
Now plug it into the MSE equation:
\[ MSE = Var(\Theta) - \left( \rho^2 \frac{Var(\Theta)}{Var(X)} \right) Var(X) \]

Step 7: Simplify the expression. The \( Var(X) \) in the numerator and denominator cancel out perfectly.
\[ MSE = Var(\Theta) - \rho^2 Var(\Theta) \]

Step 8: Factor out \( Var(\Theta) \) to arrive at our final flashcard formula.
\[ MSE = (1 - \rho^2) Var(\Theta) \]

THE TAKEAWAY
The Mean Squared Error of the best linear guess is simply the original variance of your parameter reduced by the square of the correlation. It proves mathematically that highly correlated data drastically shrinks our uncertainty [3].

CONCRETE EXAMPLE
Let's say we are predicting a student's final exam score (\( \Theta \)). Without knowing anything else, the historical variance of all final scores is \( 100 \). We observe the student's midterm score (\( X \)). The correlation \( \rho \) between midterm and final scores is \( 0.8 \). 

First, we square the correlation: \( 0.8^2 = 0.64 \). 
Now we calculate the MSE: 
\[ MSE = (1 - 0.64) \times 100 \]
\[ MSE = 0.36 \times 100 = 36 \]
By simply drawing a line from the midterm score to the final score, our guessing error (uncertainty) drops from \( 100 \) down to \( 36 \).

WATCH OUT
A common pitfall is thinking that a *negative* correlation increases your error, or forgetting to square \( \rho \). Because \( \rho \) is squared in the formula, a negative correlation (like \( -0.8 \)) becomes a positive \( 0.64 \). A strong negative correlation shrinks your error just as much as a strong positive one!

Does it make sense why a strong negative relationship is just as useful for making predictions as a positive one?

---

## Card 59

**Q:** In Linear LMS with multiple independent observations of the same parameter, how are the observations weighted?

**A:** Observations are weighted inversely proportional to their individual noise variances.

---

## Card 60

**Q:** Under what specific distribution assumption is the optimal LMS estimator guaranteed to be linear?

**A:** When all random variables involved follow a Normal (Gaussian) distribution.

---

## Card 61

**Q:** Formula: Bayes' Rule for continuous variables

**A:** $f_{X|Y}(x|y) = \frac{f_X(x) f_{Y|X}(y|x)}{f_Y(y)}$.

---

## Card 62

**Q:** How is the denominator $f_Y(y)$ calculated in continuous Bayes' Rule?

**A:** By integrating the joint density over all possible values of $x$ ($\int f_X(x) f_{Y|X}(y|x) dx$).

---

## Card 63

**Q:** What is a 'mixed' Bayes' Rule?

**A:** An inference model where one random variable is discrete and the other is continuous.

---

## Card 64

**Q:** In a Poisson process, how is the probability of exactly one arrival in a small interval $\delta$ approximated?

**A:** It is approximately $\lambda \delta$.

---

## Card 65

**Q:** How is the probability of zero arrivals in a small interval $\delta$ represented in a Poisson process?

**A:** It is approximately $1 - \lambda \delta$.

**E:** PLAIN ENGLISH

Imagine you are watching a completely random event, like shooting stars in the night sky or customers walking into a bank [1]. If you look at a window of time that is incredibly tiny—like a millisecond—what are the chances that a customer walks in? Because the window is so incredibly small, there is only a tiny chance that exactly one person arrives, and it is virtually impossible for two or more people to arrive at the exact same split second [2, 3]. 

Because those are the only options, the chance that *nothing* happens is simply 100% minus that tiny chance that exactly one person arrived [2]. This simple idea is the foundational building block for the entire Poisson process!

STEP-BY-STEP

Let's break down exactly how we get this mathematical approximation.

Step 1: We define our variables. Let \(\lambda\) be the arrival rate (how many events happen on average per unit of time) and let \(\delta\) be a very small interval of time [2]. 

Step 2: We find the probability of exactly one arrival. By the core definition of the Poisson process, the probability of getting exactly one arrival in a tiny interval is proportional to the rate and the time interval [2]. 
\[P(1 \text{ arrival}) \approx \lambda \delta\]

Step 3: We look at the probability of two or more arrivals. Because the interval \(\delta\) is extremely small, the chance of getting more than one arrival is so miniscule that it is effectively zero (it involves \(\delta^2\) terms, which are negligibly small) [3, 4].
\[P(\text{more than 1 arrival}) \approx 0\]

Step 4: We use the rule that all probabilities in a sample space must add up to 1 [5]. The only possible outcomes in this tiny window are 0 arrivals, 1 arrival, or more than 1 arrival. 
\[P(0 \text{ arrivals}) + P(1 \text{ arrival}) + P(\text{more than 1 arrival}) = 1\]

Step 5: We substitute our known values into the equation and solve for the probability of zero arrivals.
\[P(0 \text{ arrivals}) + \lambda \delta + 0 \approx 1\]
\[P(0 \text{ arrivals}) \approx 1 - \lambda \delta\]

THE TAKEAWAY

In a continuous Poisson process, if you zoom in on an infinitely small slice of time, the system essentially becomes binary: either exactly one thing happens (with probability \(\lambda \delta\)), or absolutely nothing happens (with probability \(1 - \lambda \delta\)) [3]. This microscopic view allows mathematicians to build the full formulas for events over long periods of time.

CONCRETE EXAMPLE

Let's say emails arrive at your inbox at a rate of \(\lambda = 5\) emails per hour [6]. We want to know the probability of getting zero emails in a tiny fraction of an hour, let's say \(\delta = 0.01\) hours (about 36 seconds). 

The probability of getting exactly one email in that tiny window is \(\lambda \delta = 5 \times 0.01 = 0.05\) (or 5%). Therefore, the probability of getting zero emails in that 36-second window is approximately \(1 - 0.05 = 0.95\) (or 95%).

WATCH OUT

A very easy mistake to make is trying to use the \(1 - \lambda \delta\) approximation for a *large* time interval instead of a tiny one. If \(\delta\) is large (for example, 2 hours when the rate is 5), the formula would give a negative probability (\(1 - 10 = -9\)), which is impossible! This approximation only works when \(\delta\) is extremely close to zero [4]; for larger intervals, you must use the full Poisson probability formula involving the exponential function.

Does this step-by-step breakdown make the concept click for you?

---

## Card 66

**Q:** What is the standard formula for $n$ choose $k$ (the binomial coefficient)?

**A:** $\frac{n!}{k!(n-k)!}$.

---

## Card 67

**Q:** Formula: Cumulative Distribution Function $F_X(x)$

**A:** $F_X(x) = P(X \le x)$.

---

## Card 68

**Q:** How is the PDF $f_X(x)$ derived from the CDF $F_X(x)$?

**A:** By taking the first derivative of the CDF ($f_X(x) = \frac{d}{dx} F_X(x)$).

**E:** PLAIN ENGLISH
The Cumulative Distribution Function (CDF) measures the *total accumulated probability* up to a certain point. If you want to know the probability that a random event yields a value less than or equal to 5, the CDF gives you that exact number. 

The Probability Density Function (PDF), on the other hand, tells you the *rate* at which that probability is accumulating at an exact specific spot. 

Think of it like driving a car: the CDF is your odometer telling you the total distance you have traveled so far. The PDF is your speedometer telling you how fast you are covering ground right at this exact second. If you know your total distance over time, you can find your speed by looking at the rate of change. In math, finding the rate of change means taking the derivative [1].

STEP-BY-STEP
Here is how we mathematically arrive at the fact that the PDF is the derivative of the CDF [2]:

1. **Define the probability of a tiny interval:** Let's look at the probability that a random variable \(X\) falls in a very small interval between \(x\) and \(x + \Delta x\). Using the CDF, which gives running totals, this is the total probability up to \(x + \Delta x\) minus the total probability up to \(x\). 
   \[P(x < X \le x + \Delta x) = F_X(x + \Delta x) - F_X(x)\]

2. **Define density for that same interval:** We also know that for a very small interval, the probability of falling in that interval is approximately the density at \(x\) multiplied by the width of the interval [3].
   \[P(x < X \le x + \Delta x) \approx f_X(x) \cdot \Delta x\]

3. **Set the two expressions equal to each other:** Because both equations represent the exact same probability, we can link them together.
   \[f_X(x) \cdot \Delta x \approx F_X(x + \Delta x) - F_X(x)\]

4. **Isolate the PDF:** We want to solve for the density, \(f_X(x)\), so we divide both sides of the equation by the interval width, \(\Delta x\).
   \[f_X(x) \approx \frac{F_X(x + \Delta x) - F_X(x)}{\Delta x}\]

5. **Take the limit to make it exact:** We use the fundamental definition of a derivative from calculus. By shrinking our interval \(\Delta x\) until it approaches zero, the approximation becomes exact. The right side of the equation becomes the formal definition of a derivative!
   \[f_X(x) = \lim_{\Delta x \to 0} \frac{F_X(x + \Delta x) - F_X(x)}{\Delta x}\]
   \[f_X(x) = \frac{d}{dx} F_X(x)\]

THE TAKEAWAY
The Probability Density Function is simply the rate of change (the first derivative) of the Cumulative Distribution Function [2]. This matters because it gives us a foolproof, mechanical way to extract the local "density" of a continuous random variable anytime we already know its total running probability [1]. 

CONCRETE EXAMPLE
Imagine the CDF for the lifespan of a lightbulb in years is given by the formula:
\[F_X(x) = 1 - e^{-3x}\]

To find the PDF, we take the derivative of this function with respect to \(x\).
First, the derivative of the constant \(1\) is just \(0\). 
Next, we use the chain rule for the exponential term — the derivative of \(e^{u}\) is \(e^{u}\) times the derivative of \(u\). Here, \(u = -3x\), so its derivative is \(-3\).
\[f_X(x) = 0 - (-3)e^{-3x}\]
\[f_X(x) = 3e^{-3x}\]

WATCH OUT
A very common mistake students make is forgetting that while the CDF always outputs a valid probability (a number between 0 and 1), the PDF does *not* output a probability [4]. Because the PDF is a rate of change (a density), its value can absolutely be greater than 1! It just represents probability *per unit length* [5].

Does this relationship between the "running total" and the "rate of change" make sense, or would you like to try calculating a PDF from a different CDF together?

---

## Card 69

**Q:** If $X$ and $Y$ are independent random variables, how is $E[XY]$ simplified?

**A:** It is the product of their individual expectations ($E[X]E[Y]$).

---

## Card 70

**Q:** What does the Law of Total Probability state for an event $A$ and a partition $B_1, \dots, B_n$?

**A:** $P(A) = \sum_{i=1}^n P(B_i) P(A | B_i)$.

---

## Card 71

**Q:** What happens to the mean squared error as the correlation coefficient $\rho$ approaches 1?

**A:** The mean squared error approaches zero, indicating perfect estimation.

---

## Card 72

**Q:** How is the joint PDF $f_{X,Y}(x,y)$ related to conditional and marginal PDFs?

**A:** $f_{X,Y}(x,y) = f_X(x) f_{Y|X}(y|x)$.

---

## Card 73

**Q:** In discrete probability, what is the union of two events $P(A \cup B)$ if they are NOT disjoint?

**A:** $P(A) + P(B) - P(A \cap B)$.

---

## Card 74

**Q:** In the Poisson process, what is the probability of two arrivals in the same 'mini slot' $\delta$ as $\delta \to 0$?

**A:** The probability is negligible and treated as zero in the limit.

---

## Card 75

**Q:** What is the sum of $P(A)$ and $P(A^c)$?

**A:** The sum is always exactly 1.

---

## Card 76

**Q:** How is the conditional probability $P(A|B)$ defined?

**A:** $\frac{P(A \cap B)}{P(B)}$, provided $P(B) > 0$.

---

## Card 77

**Q:** What visual shape does the Binomial PMF take when $n$ is very large?

**A:** It takes the shape of a bell curve.

---

## Card 78

**Q:** In a continuous sample space like a unit square, what is the probability of hitting exactly one specific point?

**A:** The probability is zero because a single point has zero area.

---

## Card 79

**Q:** If all outcomes in a sample space are equally likely, what type of probability law is being used?

**A:** A uniform probability law.

---

## Card 80

**Q:** In the context of LMS estimation, what does the 'error variance' $Var(\Theta | X)$ represent?

**A:** The mean squared error associated with a specific observation $X$.

---

## Card 81

**Q:** How does the variance of a constant $\alpha$ differ from the variance of a random variable $X$?

**A:** The variance of a constant is always zero.

---

## Card 82

**Q:** What is the relationship between the joint density and conditional density for $f_{Y|X}$?

**A:** $f_{Y|X}(y|x) = \frac{f_{X,Y}(x,y)}{f_X(x)}$.

---

## Card 83

**Q:** Why is problem solving considered the key part of mastering probability?

**A:** It allows one to appreciate the subtleties and difficulties that reading theory alone cannot reveal.

---

## Card 84

**Q:** In derived distributions, why is the probability $P(Y=y)$ usually zero for continuous variables?

**A:** Because any single value in a continuous range has zero probability density.

---

## Card 85

**Q:** How is the marginal PDF $f_X(x)$ obtained from the joint PDF $f_{X,Y}(x,y)$?

**A:** By integrating the joint PDF over all possible values of $y$ ($\int_{-\infty}^{\infty} f_{X,Y}(x,y) dy$).

---

## Card 86

**Q:** What does a correlation coefficient $\rho = 0$ imply for the Linear LMS estimator?

**A:** It implies the observation $X$ provides no information for adjusting the estimate from the prior mean.

---

## Card 87

**Q:** What is the first step in constructing any probabilistic model?

**A:** Defining the sample space of the experiment.

---

## Card 88

**Q:** When finding $E[g(X)]$, if $g(x) = x^2$, what is being calculated?

**A:** The second moment of the random variable.

---
