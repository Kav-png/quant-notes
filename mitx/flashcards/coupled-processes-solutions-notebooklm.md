# Stochastic Flashcards

## Card 1

**Q:** In a stationary coupled system, what is the equation for the variable $x_t$?

**A:** $x_t = \lambda y_{t-1} + \sigma z_t$, where $\lambda$ is the coupling coefficient, $\sigma$ is volatility, and $z_t \sim \mathcal{N}(0,1)$.

---

## Card 2

**Q:** In a stationary coupled system, what is the equation for the variable $y_t$?

**A:** $y_t = \lambda x_{t-1} + \sigma w_t$, where $\lambda$ is the coupling coefficient, $\sigma$ is volatility, and $w_t \sim \mathcal{N}(0,1)$.

---

## Card 3

**Q:** What is the specific distribution and relationship of the shocks $z_t$ and $w_t$ in this coupled process model?

**A:** They are i.i.d. standard normal variables, $z_t, w_t \sim \mathcal{N}(0,1)$, and are independent of each other across all $t$ and $s$.

---

## Card 4

**Q:** How is the system matrix $M$ defined when representing the coupled system in the form $C_t = M C_{t-1} + \sigma \eta_t$?

**A:** $M = \begin{pmatrix} 0 & \lambda \\ \lambda & 0 \end{pmatrix}$.

---

## Card 5

**Q:** What are the eigenvalues of the coupling matrix $M = \begin{pmatrix} 0 & \lambda \\ \lambda & 0 \end{pmatrix}$?

**A:** $\gamma_1 = +\lambda$ and $\gamma_2 = -\lambda$.

---

## Card 6

**Q:** Formula: Stationarity condition for the coupled system

**A:** $|\lambda| < 1$. All eigenvalues of the transition matrix must lie strictly inside the unit circle for the process to be stable.

---

## Card 7

**Q:** How is the stationarity condition for this coupled system derived?

**A:** By finding the eigenvalues of the transition matrix $M$ and ensuring their absolute values are less than 1.

---

## Card 8

**Q:** What does stationarity imply regarding the moments of $x_t$ and $y_t$?

**A:** The mean, variance, and autocovariance are time-invariant and do not depend on $t$.

---

## Card 9

**Q:** What is the unconditional mean $\mu_x$ and $\mu_y$ of the stationary coupled process?

**A:** $\mu_x = \mu_y = 0$.

---

## Card 10

**Q:** How is the result $\mu_x = \mu_y = 0$ derived using the stationarity assumption?

**A:** Take expectations of the process equations and solve the resulting system $\mu_x = \lambda \mu_y$ and $\mu_y = \lambda \mu_x$ for $|\lambda| < 1$.

---

## Card 11

**Q:** Formula: Variance of $x_t$ in the coupled system

**A:** $\text{Var}(x_t) = \frac{\sigma^2}{1 - \lambda^2}$, where $\sigma$ is the shock scale and $\lambda$ is the coupling coefficient.

---

## Card 12

**Q:** Why is $\text{Var}(x_t) = \text{Var}(y_t)$ in this specific system?

**A:** The system is symmetric; $x$ and $y$ play identical roles in the coupling equations with identical shock distributions.

---

## Card 13

**Q:** What is the key insight behind calculating the variance $\sigma_x^2$ in this system?

**A:** Squaring the equation for $x_t$ and using the self-consistency condition $\text{Var}(x_t) = \text{Var}(y_{t-1})$ due to stationarity.

---

## Card 14

**Q:** In the derivation of variance, why is $E[y_{t-1} z_t] = 0$?

**A:** The variable $y_{t-1}$ depends only on shocks up to time $t-1$, whereas $z_t$ is a fresh shock independent of the past.

---

## Card 15

**Q:** Formula: Autocovariance at lag 1 for $x_t$

**A:** $\gamma_x(1) = \frac{\lambda^2 \sigma^2}{1 - \lambda^2}$.

---

## Card 16

**Q:** How is $\gamma_x(1)$ expressed in terms of cross-covariance?

**A:** $\gamma_x(1) = \lambda \gamma_{xy}(0)$, where $\gamma_{xy}(0)$ is the contemporaneous cross-covariance.

---

## Card 17

**Q:** Formula: Autocovariance at generic lag $k$ for $x_t$ (even $k$)

**A:** $\gamma_x(k) = \lambda^k \cdot \frac{\sigma^2}{1 - \lambda^2}$ for $k \geq 0$.

---

## Card 18

**Q:** Term: Autocorrelation Function (ACF)

**A:** Definition: The autocovariance of a process at lag $k$ normalised by its variance. Example: In this coupled system, $\rho_x(k) = \lambda^k$.

---

## Card 19

**Q:** Formula: ACF of $x_t$ at lag $k$

**A:** $\rho_x(k) = \lambda^k$ for $k \geq 0$.

---

## Card 20

**Q:** How does the ACF of $x_t$ behave if $-1 < \lambda < 0$?

**A:** The ACF exhibits oscillating mean reversion, alternating in sign at each lag.

---

## Card 21

**Q:** How does the ACF of $x_t$ behave if $0 < \lambda < 1$?

**A:** The ACF decays smoothly and geometrically toward zero, representing persistent positive autocorrelation.

---

## Card 22

**Q:** Formula: Contemporaneous cross-covariance $\gamma_{xy}(0)$

**A:** $\gamma_{xy}(0) = 0$.

---

## Card 23

**Q:** What is the physical intuition for $\gamma_{xy}(0) = 0$ in this system?

**A:** Shocks are independent and the variables only influence each other through a lag; information has not yet propagated cross-variable at $k=0$.

---

## Card 24

**Q:** Formula: Cross-covariance at lag 1, $\gamma_{xy}(1)$

**A:** $\gamma_{xy}(1) = \frac{\lambda \sigma^2}{1 - \lambda^2}$.

---

## Card 25

**Q:** Formula: Generic lag cross-covariance $\gamma_{xy}(k)$ for $k \geq 1$

**A:** $\gamma_{xy}(k) = \lambda^k \cdot \frac{\sigma^2}{1 - \lambda^2}$.

---

## Card 26

**Q:** Term: Decoupled Modes

**A:** Definition: Linear combinations of variables that evolve as independent univariate processes. Example: $u_t = x_t + y_t$ and $v_t = x_t - y_t$ in a two-variable coupled system.

---

## Card 27

**Q:** What are the two decoupled AR(1) equations for the system modes $u_t$ and $v_t$?

**A:** $u_t = \lambda u_{t-1} + \sigma(z_t + w_t)$ and $v_t = -\lambda v_{t-1} + \sigma(z_t - w_t)$.

---

## Card 28

**Q:** What is the MA($\infty$) representation of $x_t$ in terms of past shocks?

**A:** $x_t = \sigma \sum_{m=0}^{\infty} \lambda^{2m} z_{t-2m} + \sigma \sum_{m=0}^{\infty} \lambda^{2m+1} w_{t-2m-1}$.

---

## Card 29

**Q:** In the MA($\infty$) representation of $x_t$, which shocks appear at even lags?

**A:** Only the variable's own shocks $z_{t-2m}$ appear at even lags.

---

## Card 30

**Q:** In the MA($\infty$) representation of $x_t$, which shocks appear at odd lags?

**A:** Only the cross-variable shocks $w_{t-2m-1}$ appear at odd lags.

---

## Card 31

**Q:** Formula: One-step ahead forecast for $x_{t+1}$ given information $\mathcal{F}_t$

**A:** $E[x_{t+1} | \mathcal{F}_t] = \lambda y_t$.

---

## Card 32

**Q:** Formula: Two-step ahead forecast for $x_{t+2}$ given information $\mathcal{F}_t$

**A:** $E[x_{t+2} | \mathcal{F}_t] = \lambda^2 x_t$.

---

## Card 33

**Q:** Formula: $h$-step ahead forecast for $x_{t+h}$ when $h$ is odd

**A:** $E[x_{t+h} | \mathcal{F}_t] = \lambda^h y_t$.

---

## Card 34

**Q:** Formula: $h$-step ahead forecast for $x_{t+h}$ when $h$ is even

**A:** $E[x_{t+h} | \mathcal{F}_t] = \lambda^h x_t$.

---

## Card 35

**Q:** Formula: Forecast error variance at horizon $h$

**A:** $\text{Var}(x_{t+h} - E[x_{t+h}|\mathcal{F}_t]) = \sigma^2 \cdot \frac{1 - \lambda^{2h}}{1 - \lambda^2}$.

---

## Card 36

**Q:** What is the limit of the forecast error variance as the horizon $h \to \infty$?

**A:** It converges to the unconditional variance $\frac{\sigma^2}{1 - \lambda^2}$.

---

## Card 37

**Q:** What is the 'master trick' for solving coupled systems of this type?

**A:** Decouple the system into independent AR(1) processes using the eigenvectors of the transition matrix, solve them, and then invert the transformation.

---

## Card 38

**Q:** How is the cross-covariance $\gamma_{xy}(1)$ derived?

**A:** Multiply the $x_t$ equation by $y_{t-1}$, take expectations, and substitute $E[y_{t-1}^2] = \sigma_y^2$.

---

## Card 39

**Q:** Pitfall: What common mistake is made regarding the contemporaneous cross-covariance of coupled variables?

**A:** Assuming $\gamma_{xy}(0)$ is non-zero because the variables are coupled; in this lagged model, they are actually uncorrelated at lag 0.

---

## Card 40

**Q:** Pitfall: What happens if the coupling coefficient $|\lambda| \geq 1$?

**A:** The process is non-stationary, meaning moments like variance are undefined and the system does not settle into a stable distribution.

---

## Card 41

**Q:** Pitfall: Why can't you calculate $\text{Var}(x_t)$ simply by treating $x_t$ as a univariate AR(1) of $x_{t-1}$?

**A:** The system depends on the lag of the *other* variable, requiring a joint solution or decoupling to find the correct variance.

---

## Card 42

**Q:** How does the coupling propagate shocks between $x$ and $y$ over time?

**A:** A shock to $x$ at time $t$ influences $y$ at $t+1$, which then influences $x$ again at $t+2$, creating a 'ping-pong' effect every other period.

---

## Card 43

**Q:** What is the key assumption regarding the relationship between $z_t$ and the past information $\mathcal{F}_{t-1}$?

**A:** $E[z_t | \mathcal{F}_{t-1}] = 0$, as $z_t$ is an independent shock occurring at time $t$.

---

## Card 44

**Q:** Why does the forecast $E[x_{t+h}|\mathcal{F}_t]$ alternate between $x_t$ and $y_t$?

**A:** The coupled structure dictates that $x$ is determined by the previous value of $y$, and $y$ is determined by the previous value of $x$.

---

## Card 45

**Q:** Concept: Self-consistency condition

**A:** The requirement that for a stationary process, statistical properties must be identical at all time steps. Example: Setting $\text{Var}(x_t) = \text{Var}(x_{t-1})$ to solve for the steady-state variance.

---
