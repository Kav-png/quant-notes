# Probability Flashcards

## Card 1

**Q:** Term: Sample Space

**A:** Definition: The set of all possible outcomes of a random experiment. Example: For a single coin flip, the sample space is $\{\text{Heads, Tails}\}$.

---

## Card 2

**Q:** In a probabilistic model, what two properties must the list of possible outcomes in a sample space satisfy?

**A:** The outcomes must be mutually exclusive and collectively exhaustive.

---

## Card 3

**Q:** What does it mean for a set of outcomes to be 'mutually exclusive'?

**A:** It means that if one outcome occurs, no other outcome in the set can happen at the same time.

---

## Card 4

**Q:** What does it mean for a set of outcomes to be 'collectively exhaustive'?

**A:** It means that the set includes every possible result of the experiment; nothing outside the set can happen.

---

## Card 5

**Q:** Axiom: Non-negativity of Probability

**A:** For any event $A$, the probability is greater than or equal to zero: $P(A) \ge 0$.

---

## Card 6

**Q:** Axiom: Normalisation

**A:** The probability of the entire sample space $\Omega$ is exactly one: $P(\Omega) = 1$.

---

## Card 7

**Q:** Axiom: Additivity for Disjoint Events

**A:** If $A$ and $B$ are disjoint ($A \cap B = \emptyset$), then $P(A \cup B) = P(A) + P(B)$.

---

## Card 8

**Q:** How is the probability of the complement of an event $A$ (denoted $A^c$) calculated?

**A:** $P(A^c) = 1 - P(A)$.

---

## Card 9

**Q:** Formula: Conditional Probability

**A:** The probability of $A$ given $B$ is $P(A|B) = \frac{P(A \cap B)}{P(B)}$, where $P(B) > 0$.

---

## Card 10

**Q:** Formula: Multiplication Rule

**A:** $P(A \cap B) = P(B)P(A|B)$ or $P(A \cap B) = P(A)P(B|A)$.

---

## Card 11

**Q:** Formula: Total Probability Theorem (for a partition $A_1, A_2, ...$)

**A:** $P(B) = \sum_{i} P(A_i)P(B|A_i)$.

---

## Card 12

**Q:** Formula: Bayes' Rule

**A:** $P(A_i|B) = \frac{P(A_i)P(B|A_i)}{\sum_{j} P(A_j)P(B|A_j)}$, where $A_j$ are disjoint scenarios covering the sample space.

---

## Card 13

**Q:** How is the probability of an intersection of three events $P(A \cap B \cap C)$ calculated using the chain rule?

**A:** $P(A \cap B \cap C) = P(A)P(B|A)P(C|A \cap B)$.

---

## Card 14

**Q:** What is the key insight behind Bayes' Rule in terms of 'Cause and Effect'?

**A:** It allows us to perform inference by reversing a causal model to find the probability of a cause given an observed effect.

---

## Card 15

**Q:** How is independence between two events $A$ and $B$ mathematically defined?

**A:** $P(A \cap B) = P(A)P(B)$.

---

## Card 16

**Q:** Pitfall: Does disjointness imply independence?

**A:** No; disjoint events are highly dependent because if one occurs, the probability of the other becoming zero changes from its original value.

---

## Card 17

**Q:** Under what condition are two events $A$ and $B$ 'conditionally independent' given event $C$?

**A:** $P(A \cap B | C) = P(A|C)P(B|C)$.

---

## Card 18

**Q:** True or False: If two events are independent, they must also be conditionally independent given any third event $C$.

**A:** False; the presence of a third event can introduce dependencies between previously independent events.

---

## Card 19

**Q:** What requirement is added to pairwise independence to satisfy mutual independence for three events?

**A:** $P(A \cap B \cap C) = P(A)P(B)P(C)$.

---

## Card 20

**Q:** Term: Random Variable

**A:** Definition: A function that assigns a numerical value to every possible outcome in the sample space. Example: Assigning '1' to Heads and '0' to Tails.

---

## Card 21

**Q:** Term: Probability Mass Function (PMF)

**A:** Definition: A function for a discrete random variable $X$ that gives the probability $P(X=x)$ for each possible value $x$. Example: $p_X(k) = \frac{1}{6}$ for a fair six-sided die.

---

## Card 22

**Q:** Formula: Expected Value of a Discrete Random Variable $X$

**A:** $E[X] = \sum_{x} x p_X(x)$, where $p_X(x)$ is the PMF.

---

## Card 23

**Q:** What is the Expected Value Rule for a function $g(X)$?

**A:** $E[g(X)] = \sum_{x} g(x) p_X(x)$.

---

## Card 24

**Q:** Formula: Variance of $X$ (standard definition)

**A:** $Var(X) = E[(X - E[X])^2]$.

---

## Card 25

**Q:** Formula: Variance of $X$ (shortcut formula)

**A:** $Var(X) = E[X^2] - (E[X])^2$.

---

## Card 26

**Q:** Formula: Variance of a scaled and shifted random variable $aX + b$

**A:** $Var(aX + b) = a^2 Var(X)$.

---

## Card 27

**Q:** What is the expected value of a random variable whose PMF is symmetric around a point $c$?

**A:** The expected value is the point of symmetry, $c$.

---

## Card 28

**Q:** Term: Bernoulli Random Variable

**A:** Definition: A discrete random variable that takes the value 1 with probability $p$ and 0 with probability $1-p$. Example: A single success/failure trial.

---

## Card 29

**Q:** What is the expected value $E[X]$ and variance $Var(X)$ for a Bernoulli random variable with parameter $p$?

**A:** $E[X] = p$ and $Var(X) = p(1-p)$.

---

## Card 30

**Q:** Term: Binomial Random Variable

**A:** Definition: The number of successes in $n$ independent Bernoulli trials, each with success probability $p$. Example: Number of Heads in 10 coin tosses.

---

## Card 31

**Q:** Formula: Binomial PMF ($n$ trials, probability $p$)

**A:** $p_X(k) = \binom{n}{k} p^k (1-p)^{n-k}$ for $k = 0, 1, ..., n$.

---

## Card 32

**Q:** How is the expected value of a Binomial random variable derived using indicator variables?

**A:** By expressing $X$ as the sum of $n$ independent Bernoulli trials, $X = X_1 + ... + X_n$, and using linearity: $E[X] = \sum E[X_i] = np$.

---

## Card 33

**Q:** Term: Geometric Random Variable

**A:** Definition: The number of independent Bernoulli trials until the first success occurs. Example: Tossing a coin until Heads appears for the first time.

---

## Card 34

**Q:** Formula: Geometric PMF (probability $p$)

**A:** $p_X(k) = (1-p)^{k-1}p$ for $k = 1, 2, ...$.

---

## Card 35

**Q:** What is the expected value $E[X]$ of a Geometric random variable with success probability $p$?

**A:** $E[X] = \frac{1}{p}$.

---

## Card 36

**Q:** Term: Probability Density Function (PDF)

**A:** Definition: A function $f_X(x)$ for a continuous random variable $X$ such that probabilities are areas under its curve. Example: $P(a \le X \le b) = \int_a^b f_X(x)dx$.

---

## Card 37

**Q:** Pitfall: Is the value $f_X(x)$ of a PDF at a specific point equal to a probability?

**A:** No; for continuous variables, $P(X=x) = 0$. The PDF represents probability per unit length (density).

---

## Card 38

**Q:** How is the probability of a small interval $[x, x+\delta]$ approximated for a continuous random variable?

**A:** $P(x \le X \le x+\delta) \approx f_X(x) \cdot \delta$.

---

## Card 39

**Q:** Formula: Expected Value of a Continuous Random Variable

**A:** $E[X] = \int_{-\infty}^{\infty} x f_X(x) dx$.

---

## Card 40

**Q:** Term: Uniform Random Variable on $[a, b]$

**A:** Definition: A continuous random variable with a constant PDF over the interval $[a, b]$. Example: Pick a random number between 0 and 1.

---

## Card 41

**Q:** What is the PDF and Variance for a Uniform random variable on $[a, b]$?

**A:** $f_X(x) = \frac{1}{b-a}$ for $a \le x \le b$ and $Var(X) = \frac{(b-a)^2}{12}$.

---

## Card 42

**Q:** Term: Cumulative Distribution Function (CDF)

**A:** Definition: The function $F_X(x) = P(X \le x)$, describing the probability that $X$ falls to the left of $x$. Example: Used to unify discrete and continuous models.

---

## Card 43

**Q:** How can the PDF $f_X(x)$ be recovered from the CDF $F_X(x)$ for a continuous random variable?

**A:** $f_X(x) = \frac{d}{dx} F_X(x)$.

---

## Card 44

**Q:** Formula: PDF of a Normal (Gaussian) Random Variable

**A:** $f_X(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$, where $\mu$ is the mean and $\sigma$ is the standard deviation.

---

## Card 45

**Q:** How is a general normal random variable $X \sim N(\mu, \sigma^2)$ transformed into a standard normal $Z \sim N(0, 1)$?

**A:** $Z = \frac{X - \mu}{\sigma}$.

---

## Card 46

**Q:** What does a 'jump' in a Cumulative Distribution Function (CDF) indicate?

**A:** It indicates a discrete point that has a non-zero (positive) probability mass.

---

## Card 47

**Q:** Formula: Joint PMF of $X$ and $Y$

**A:** $p_{X,Y}(x, y) = P(X=x, Y=y)$.

---

## Card 48

**Q:** How is the marginal PMF $p_X(x)$ obtained from the joint PMF $p_{X,Y}(x, y)$?

**A:** By summing over all possible values of $y$: $p_X(x) = \sum_y p_{X,Y}(x, y)$.

---

## Card 49

**Q:** Formula: Conditional PDF of $X$ given $Y=y$

**A:** $f_{X|Y}(x|y) = \frac{f_{X,Y}(x, y)}{f_Y(y)}$.

---

## Card 50

**Q:** How is independence of continuous random variables $X$ and $Y$ defined via their PDFs?

**A:** $f_{X,Y}(x, y) = f_X(x)f_Y(y)$ for all $x, y$.

---

## Card 51

**Q:** Formula: Expectation of a product of independent random variables $E[XY]$

**A:** $E[XY] = E[X]E[Y]$.

---

## Card 52

**Q:** Formula: Variance of the sum of independent random variables $Var(X + Y)$

**A:** $Var(X + Y) = Var(X) + Var(Y)$.

---

## Card 53

**Q:** Formula: Covariance of $X$ and $Y$

**A:** $Cov(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]$.

---

## Card 54

**Q:** Pitfall: If $Cov(X, Y) = 0$, are $X$ and $Y$ necessarily independent?

**A:** No; zero covariance only implies a lack of linear correlation, not complete statistical independence.

---

## Card 55

**Q:** Formula: Correlation Coefficient $\rho(X, Y)$

**A:** $\rho(X, Y) = \frac{Cov(X, Y)}{\sigma_X \sigma_Y}$, where $-1 \le \rho \le 1$.

---

## Card 56

**Q:** Formula: Law of Iterated Expectations

**A:** $E[E[X|Y]] = E[X]$.

---

## Card 57

**Q:** What is the key insight behind the Law of Total Variance?

**A:** Total variance consists of the average of the conditional variances plus the variance of the conditional expectation.

---

## Card 58

**Q:** Term: Bernoulli Process

**A:** Definition: A sequence of independent Bernoulli trials with the same probability $p$. Example: Repeatedly flipping the same coin forever.

---

## Card 59

**Q:** What is the 'Memoryless' property of the Bernoulli process?

**A:** The future of the process does not depend on past outcomes; starting from any time $t$, the process looks like it just began.

---

## Card 60

**Q:** In a Bernoulli process, what is the distribution of the time between consecutive successes?

**A:** A Geometric distribution with parameter $p$.

---

## Card 61

**Q:** Term: Poisson Process

**A:** Definition: A continuous-time arrival process where the number of arrivals in disjoint intervals is independent and proportional to the interval length. Example: Customers arriving at a bank.

---

## Card 62

**Q:** Formula: Poisson PMF (number of arrivals in time $t$ with rate $\lambda$)

**A:** $P(k, t) = \frac{(\lambda t)^k e^{-\lambda t}}{k!}$ for $k = 0, 1, 2, ...$.

---

## Card 63

**Q:** In a Poisson process, what is the distribution of the time until the first arrival?

**A:** An Exponential distribution with parameter $\lambda$.

---

## Card 64

**Q:** Formula: PDF of an Exponential random variable

**A:** $f_T(t) = \lambda e^{-\lambda t}$ for $t \ge 0$.

---

## Card 65

**Q:** What is the expected value and variance of a Poisson random variable with parameter $\lambda t$?

**A:** The mean and variance are both equal to $\lambda t$.

---

## Card 66

**Q:** How is a Poisson process derived from a Bernoulli process?

**A:** By taking the limit as the number of trials $n \to \infty$ and trial probability $p \to 0$, while $np = \lambda t$ remains constant.

---

## Card 67

**Q:** Term: Markov Chain

**A:** Definition: A random process where the probability of the next state depends only on the current state, not the past history. Example: A queue length changing over time.

---

## Card 68

**Q:** What are 'transition probabilities' in a Markov Chain?

**A:** $P_{ij} = P(X_{n+1} = j | X_n = i)$, the probability of moving from state $i$ to state $j$ in one step.

---

## Card 69

**Q:** What is a 'steady-state' probability $\pi_j$ in a Markov Chain?

**A:** The long-term probability of being in state $j$, regardless of the initial starting state.

---

## Card 70

**Q:** What is the key insight behind the Central Limit Theorem (CLT)?

**A:** The sum of a large number of independent, identically distributed (IID) random variables tends toward a normal distribution.

---

## Card 71

**Q:** Term: Maximum Likelihood Estimation (MLE)

**A:** Definition: A method of estimating parameters by choosing the value $\hat{\theta}$ that makes the observed data most likely. Example: Estimating a coin's bias from 100 flips.

---

## Card 72

**Q:** What is the 'Prior Probability' in Bayesian inference?

**A:** The initial belief about a parameter's distribution before any data is observed.

---

## Card 73

**Q:** What is the 'Posterior Probability' in Bayesian inference?

**A:** The updated belief about a parameter's distribution after incorporating observed data via Bayes' Rule.

---

## Card 74

**Q:** Formula: Standard Deviation

**A:** $\sigma = \sqrt{Var(X)}$.

---

## Card 75

**Q:** How do you calculate the probability of an event using a joint PDF $f_{X,Y}(x, y)$?

**A:** By calculating the double integral of the joint PDF over the region $S$ representing the event: $P((X,Y) \in S) = \iint_S f_{X,Y}(x, y) dx dy$.

---

## Card 76

**Q:** What happens to the distribution of a Bernoulli process if you observe it backward in time?

**A:** It remains a Bernoulli process with the same parameter $p$, as it is statistically identical forward and backward.

---
