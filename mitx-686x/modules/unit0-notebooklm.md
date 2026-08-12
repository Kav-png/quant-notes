# Probability Flashcards

## Card 1

**Q:** Term: Sample Space

**A:** Definition: The set of all possible, mutually exclusive, and collectively exhaustive outcomes of a random experiment. Example: In a coin flip, the sample space is $\{H, T\}$.

---

## Card 2

**Q:** What are the three axioms of probability?

**A:** 1. Non-negativity: $P(A) \ge 0$; 2. Normalisation: $P(\Omega) = 1$; 3. Additivity: For disjoint events, $P(A \cup B) = P(A) + P(B)$.

---

## Card 3

**Q:** Term: Event

**A:** Definition: A subset of the sample space to which a probability is assigned. Example: Rolling an even number on a die, representing the subset $\{2, 4, 6\}$.

---

## Card 4

**Q:** What is a common pitfall regarding the relationship between disjoint (mutually exclusive) events and independent events?

**A:** Disjoint events with non-zero probability are never independent; if one occurs, the probability of the other becomes zero, conveying maximum information.

---

## Card 5

**Q:** How is the conditional probability of $A$ given $B$ calculated?

**A:** $P(A|B) = \frac{P(A \cap B)}{P(B)}$, where $P(A|B)$ is the likelihood of $A$ occurring given that $B$ has occurred and $P(B) > 0$.

---

## Card 6

**Q:** What is the key insight behind the Multiplication Rule for multiple events?

**A:** The probability of a joint event is the product of the probability of the first event and the conditional probabilities of subsequent events given previous ones.

---

## Card 7

**Q:** Formula: Total Probability Theorem

**A:** $P(B) = \sum_{i} P(A_i) P(B|A_i)$, where $\{A_i\}$ is a partition of the sample space $\Omega$ into disjoint scenarios.

---

## Card 8

**Q:** Formula: Bayes' Rule

**A:** $P(A_i|B) = \frac{P(A_i)P(B|A_i)}{\sum_j P(A_j)P(B|A_j)}$, where $P(A_i)$ are priors, $P(B|A_i)$ are likelihoods, and $P(A_i|B)$ are posteriors.

---

## Card 9

**Q:** What is the core intuition behind using Bayes' Rule for inference?

**A:** It allows us to 'reverse' a causal model to update our beliefs about an unobserved cause based on an observed effect.

---

## Card 10

**Q:** Term: Independence of Events

**A:** Definition: Two events are independent if the occurrence of one does not change the probability of the other. Example: Two consecutive flips of a fair coin.

---

## Card 11

**Q:** How does the mathematical definition of independent events $A$ and $B$ differ from the conditional definition?

**A:** The mathematical definition $P(A \cap B) = P(A)P(B)$ is universal and applies even if $P(B) = 0$, whereas the conditional definition requires $P(B) > 0$.

---

## Card 12

**Q:** What is the requirement for three events $A, B,$ and $C$ to be 'mutually independent'?

**A:** They must be pairwise independent and also satisfy the joint condition $P(A \cap B \cap C) = P(A)P(B)P(C)$.

---

## Card 13

**Q:** How does pairwise independence differ from mutual independence?

**A:** Pairwise independence only ensures any two events are unrelated; mutual independence ensures the combination of any subset provides no info about the remaining events.

---

## Card 14

**Q:** Term: Random Variable (RV)

**A:** Definition: A function that maps every outcome in the sample space to a real number. Example: Counting the number of 'Heads' in three coin tosses.

---

## Card 15

**Q:** Term: Probability Mass Function (PMF)

**A:** Definition: A function $p_X(x)$ that gives the probability that a discrete random variable $X$ is exactly equal to some value $x$. Example: $p_X(1) = 0.5$ for a fair coin.

---

## Card 16

**Q:** Formula: Expectation of a discrete random variable $X$

**A:** $E[X] = \sum_{x} x p_X(x)$, where $x$ represents the possible values and $p_X(x)$ is the probability of each value.

---

## Card 17

**Q:** How is the 'Expected Value Rule' used to find $E[g(X)]$?

**A:** $E[g(X)] = \sum_{x} g(x) p_X(x)$; this insight allows us to find the mean of a function without first deriving the PMF of $g(X)$.

---

## Card 18

**Q:** Formula: Variance of a random variable $X$

**A:** $Var(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2$, representing the average squared deviation from the mean.

---

## Card 19

**Q:** Term: Standard Deviation

**A:** Definition: The square root of the variance, denoted as $\sigma$. Example: If $Var(X) = 16$ metres squared, the standard deviation is 4 metres.

---

## Card 20

**Q:** How do the expectation and variance of $X$ change under the linear transformation $Y = aX + b$?

**A:** $E[Y] = aE[X] + b$ and $Var(Y) = a^2 Var(X)$.

---

## Card 21

**Q:** Formula: Bernoulli PMF

**A:** $p_X(k) = p^k (1-p)^{1-k}$ for $k \in \{0, 1\}$, where $p$ is the probability of success.

---

## Card 22

**Q:** Formula: Binomial PMF

**A:** $p_X(k) = \binom{n}{k} p^k (1-p)^{n-k}$, where $n$ is the number of trials and $k$ is the number of successes.

---

## Card 23

**Q:** Formula: Geometric PMF

**A:** $p_X(k) = (1-p)^{k-1} p$ for $k = 1, 2, \dots$, where $X$ is the number of trials until the first success.

---

## Card 24

**Q:** What is the 'Memorylessness' property of the Geometric distribution?

**A:** The probability that the first success occurs in $n$ additional trials is independent of the number of previous failed trials.

---

## Card 25

**Q:** Term: Joint PMF

**A:** Definition: A function $p_{X,Y}(x,y)$ giving the probability that $X=x$ and $Y=y$ simultaneously. Example: The probability that a dice roll yields 3 and a coin flip yields Heads.

---

## Card 26

**Q:** Formula: Marginal PMF from a Joint PMF

**A:** $p_X(x) = \sum_{y} p_{X,Y}(x,y)$, obtained by summing the joint probabilities over all possible values of the other variable.

---

## Card 27

**Q:** How is the conditional PMF of $X$ given $Y=y$ derived?

**A:** By taking the 'slice' of the joint PMF at $Y=y$ and rescaling it: $p_{X|Y}(x|y) = \frac{p_{X,Y}(x,y)}{p_Y(y)}$.

---

## Card 28

**Q:** What is the condition for two random variables $X$ and $Y$ to be independent?

**A:** $p_{X,Y}(x,y) = p_X(x) p_Y(y)$ for all $x, y$.

---

## Card 29

**Q:** How is the expectation of the sum of random variables calculated?

**A:** $E[\sum X_i] = \sum E[X_i]$; this property of linearity holds even if the variables are dependent.

---

## Card 30

**Q:** Under what condition does $Var(X + Y) = Var(X) + Var(Y)$ hold?

**A:** The variables $X$ and $Y$ must be independent.

---

## Card 31

**Q:** Term: Probability Density Function (PDF)

**A:** Definition: A function $f_X(x)$ used to find the probability of a continuous RV falling in an interval: $P(a \le X \le b) = \int_a^b f_X(x)dx$. Example: A uniform density between 0 and 1.

---

## Card 32

**Q:** What is the probability that a continuous random variable $X$ takes an exact value $c$?

**A:** The probability is 0, as the integral over a single point has zero width.

---

## Card 33

**Q:** How is the expectation of a continuous random variable $X$ defined?

**A:** $E[X] = \int_{-\infty}^{\infty} x f_X(x) dx$, where $f_X(x)$ is the probability density function.

---

## Card 34

**Q:** Formula: Uniform PDF

**A:** $f_X(x) = \frac{1}{b-a}$ for $a \le x \le b$, where $a$ and $b$ are the interval bounds.

---

## Card 35

**Q:** Term: Cumulative Distribution Function (CDF)

**A:** Definition: A function $F_X(x) = P(X \le x)$ that describes the probability distribution for both discrete and continuous RVs. Example: A staircase function for a die roll.

---

## Card 36

**Q:** How is the PDF $f_X(x)$ recovered from the CDF $F_X(x)$?

**A:** By taking the derivative: $f_X(x) = \frac{d}{dx} F_X(x)$.

---

## Card 37

**Q:** Formula: Standard Normal PDF

**A:** $f_X(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$, representing a normal distribution with mean $\mu=0$ and variance $\sigma^2=1$.

---

## Card 38

**Q:** How is a general normal random variable $X \sim N(\mu, \sigma^2)$ standardised into a $Z \sim N(0, 1)$ variable?

**A:** $Z = \frac{X - \mu}{\sigma}$, where $\mu$ is the mean and $\sigma$ is the standard deviation.

---

## Card 39

**Q:** Formula: Poisson PMF

**A:** $p_X(k) = e^{-\lambda} \frac{\lambda^k}{k!}$ for $k=0, 1, 2, \dots$, where $\lambda$ is the average number of arrivals in a fixed interval.

---

## Card 40

**Q:** What is the key insight behind the 'Law of Iterated Expectations'?

**A:** $E[E[X|Y]] = E[X]$; the average of conditional averages is the unconditional average.

---

## Card 41

**Q:** Formula: Law of Total Variance

**A:** $Var(X) = E[Var(X|Y)] + Var(E[X|Y])$, where the total variance is the sum of 'within-section' and 'between-section' variability.

---

## Card 42

**Q:** How is the covariance between two random variables $X$ and $Y$ defined?

**A:** $Cov(X,Y) = E[(X-E[X])(Y-E[Y])] = E[XY] - E[X]E[Y]$, measuring linear association.

---

## Card 43

**Q:** Why does zero covariance not necessarily imply independence?

**A:** Covariance only measures linear dependence; non-linear dependencies (e.g. $Y=X^2$ for symmetric $X$) can result in zero covariance while being perfectly dependent.

---

## Card 44

**Q:** Formula: Convolution for independent discrete random variables

**A:** $p_W(w) = \sum_x p_X(x) p_Y(w-x)$, which calculates the PMF of the sum $W = X + Y$.

---

## Card 45

**Q:** What is the primary difference between a Bernoulli process and a Poisson process?

**A:** A Bernoulli process occurs in discrete time slots with probability $p$, while a Poisson process occurs in continuous time with rate $\lambda$.

---

## Card 46

**Q:** Term: Erlang Distribution

**A:** Definition: The distribution of the time until the $k$-th arrival in a Poisson process with rate $\lambda$. Example: Waiting time for the 3rd customer in a store.

---

## Card 47

**Q:** What defines a 'Markov Chain'?

**A:** A stochastic process where the future state depends only on the current state, and not on the history of how the system reached that state.

---

## Card 48

**Q:** What is the core claim of the Central Limit Theorem (CLT)?

**A:** The sum of a large number of independent, identically distributed (IID) random variables tends toward a normal distribution, regardless of the original distribution shape.

---

## Card 49

**Q:** Term: Bayesian Inference

**A:** Definition: A method of statistical inference in which Bayes' Rule is used to update the probability for a hypothesis as more evidence becomes available. Example: Updating the probability of a medical condition after a test.

---

## Card 50

**Q:** What is Maximum Likelihood Estimation (MLE)?

**A:** A classical inference method that chooses the parameter value $\theta$ that makes the observed data $X$ most likely: $\max_{\theta} P(X; \theta)$.

---

## Card 51

**Q:** How do 'Classical' and 'Bayesian' statistics differ in their treatment of parameters?

**A:** Bayesian statistics treats parameters as random variables with prior distributions; Classical statistics treats parameters as unknown constants.

---

## Card 52

**Q:** What is the 'Sample Mean' and how does it relate to the 'Expected Value'?

**A:** The sample mean $M_n = \frac{1}{n} \sum X_i$ is a random variable that converges to the constant expected value $E[X]$ as $n$ increases.

---

## Card 53

**Q:** Term: Correlation Coefficient

**A:** Definition: A dimensionless measure $\rho = \frac{Cov(X,Y)}{\sigma_X \sigma_Y}$ ranging from -1 to 1 that quantifies linear correlation. Example: $\rho=1$ means perfect positive linear relationship.

---

## Card 54

**Q:** What is a common pitfall when interpreting conditional independence?

**A:** Conditional independence (given $C$) does not imply unconditional independence, and unconditional independence does not imply conditional independence.

---

## Card 55

**Q:** Formula: Variance of the Sample Mean

**A:** $Var(M_n) = \frac{\sigma^2}{n}$, where $\sigma^2$ is the population variance and $n$ is the sample size.

---

## Card 56

**Q:** How is the probability of a union $P(A \cup B)$ calculated if the events are not disjoint?

**A:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.

---

## Card 57

**Q:** What is the 'indicator' method used for when calculating expectations of sums?

**A:** Decomposing a complex variable into a sum of simple Bernoulli $0/1$ variables to simplify the calculation using linearity of expectation.

---

## Card 58

**Q:** Term: Steady-state Probability (Markov Chain)

**A:** Definition: The long-term probability $\pi_i$ that the system is in state $i$, which becomes independent of the initial state. Example: The long-term occupancy rate of a queue.

---

## Card 59

**Q:** Formula: Probability of a partition $A$ in a continuous space

**A:** $P(A) = \iint_A f_{X,Y}(x,y) dx dy$, where $f_{X,Y}$ is the joint PDF.

---

## Card 60

**Q:** Insight: Convolution vs. Summing RVs

**A:** Convolution is the mathematical operation performed on the densities (PDFs) or mass functions (PMFs) to find the distribution of the sum of two independent RVs.

---

## Card 61

**Q:** What is the variance of a Binomial distribution?

**A:** $Var(X) = np(1-p)$, derived from the sum of $n$ independent Bernoulli trials each with variance $p(1-p)$.

---

## Card 62

**Q:** Term: Transition Probability

**A:** Definition: The conditional probability $p_{ij}$ of moving from state $i$ to state $j$ in one step of a Markov chain. Example: $P(\text{Rain tomorrow} | \text{Sunny today})$.

---

## Card 63

**Q:** What defines a 'Poisson Arrival'?

**A:** An arrival process characterized by stationarity, independence of disjoint intervals, and a very low probability of multiple arrivals in an infinitesimal window.

---

## Card 64

**Q:** Formula: Characteristic Function

**A:** $\phi_X(t) = E[e^{itX}]$, a transform that uniquely identifies a distribution and simplifies the calculation of moments.

---
