

## Card 1

**Q:** What are the **setup equations** for the coupled stationary system of two variables \(x_t\) and \(y_t\)?

**A:** The setup equations are:
\[x_t = \lambda y_{t-1} + \sigma z_t\]
\[y_t = \lambda x_{t-1} + \sigma w_t\]
where \(z_t, w_t \sim \mathcal{N}(0,1)\) are **i.i.d.** and **independent of each other** across all \(t, s\).

---

## Card 2

**Q:** What does **stationarity** mean for the variables \(x_t\) and \(y_t\)?

**A:** It means that their **mean, variance, and autocovariance** do not depend on time \(t\) — the process has settled into a **stable, time-invariant distribution**.

---

## Card 3

**Q:** How do we write the coupled system in **matrix form** \(C_t = M C_{t-1} + \sigma \eta_t\)?

**A:** The matrix form is:
\[\begin{pmatrix} x_t \\ y_t \end{pmatrix} = \begin{pmatrix} 0 & \lambda \\ \lambda & 0 \end{pmatrix} \begin{pmatrix} x_{t-1} \\ y_{t-1} \end{pmatrix} + \sigma \begin{pmatrix} z_t \\ w_t \end{pmatrix}\]
where \(M = \begin{pmatrix} 0 & \lambda \\ \lambda & 0 \end{pmatrix}\).

---

## Card 4

**Q:** What is the general condition for **stationarity** in terms of the transition matrix \(M\)?

**A:** The system is stationary if and only if **all eigenvalues** of \(M\) lie **strictly inside the unit circle**.

---

## Card 5

**Q:** What are the **eigenvalues** of the transition matrix \(M = \begin{pmatrix} 0 & \lambda \\ \lambda & 0 \end{pmatrix}\)?

**A:** The eigenvalues are:
\[\gamma_1 = +\lambda, \quad \gamma_2 = -\lambda\]

---

## Card 6

**Q:** What is the specific **stationarity condition** for the parameter \(\lambda\)?

**A:** Since the eigenvalues of \(M\) are \(\pm\lambda\), the stationarity condition requires:
\[|\lambda| < 1\]

---

## Card 7

**Q:** What are the **unconditional expectations (means)** \(E[x_t]\) and \(E[y_t]\) of the stationary coupled process?

**A:** The unconditional means are:
\[E[x_t] = E[y_t] = 0\]

---

## Card 8

**Q:** How do we prove that the **unconditional means** are zero?

**A:** Taking expectations on both equations yields \(\mu_x = \lambda \mu_y\) and \(\mu_y = \lambda \mu_x\). Substituting the first into the second gives \(\mu_y(1 - \lambda^2) = 0\). Since \(|\lambda| < 1\), \(\lambda^2 \neq 1\), which implies **\(\mu_x = \mu_y = 0\)**.

---

## Card 9

**Q:** Why does **\(\text{Var}(x_t) = E[x_t^2]\)** hold for this system?

**A:** Because the **unconditional mean is zero** (\(\mu_x = 0\)), and variance is defined as \(\text{Var}(x_t) = E[(x_t - \mu_x)^2]\).

---

## Card 10

**Q:** What is the **squared equation** for \(x_t\) used as the first step to compute variance?

**A:** Squaring both sides of \(x_t = \lambda y_{t-1} + \sigma z_t\) yields:
\[x_t^2 = \lambda^2 y_{t-1}^2 + 2\lambda\sigma y_{t-1} z_t + \sigma^2 z_t^2\]

---

## Card 11

**Q:** In the variance derivation, why is the expectation of the cross term **\(E[y_{t-1} z_t] = 0\)**?

**A:** Because \(y_{t-1}\) depends only on **shocks up to time \(t-1\)**, whereas \(z_t\) is a **fresh shock at time \(t\)**, making them independent.

---

## Card 12

**Q:** What is the **unconditional variance** of \(x_t\) and \(y_t\)?

**A:** By symmetry and stationarity, the variance is:
\[\text{Var}(x_t) = \text{Var}(y_t) = \frac{\sigma^2}{1 - \lambda^2}\]

---

## Card 13

**Q:** How is the **autocovariance** of \(x_t\) at lag \(k\) defined?

**A:** Since \(\mu_x = 0\), it is defined as:
\[\gamma_x(k) = \text{Cov}(x_t, x_{t-k}) = E[x_t x_{t-k}]\]

---

## Card 14

**Q:** What is the **lag-1 autocovariance** \(\gamma_x(1)\) of \(x_t\)?

**A:** The lag-1 autocovariance is:
\[\gamma_x(1) = \frac{\lambda^2 \sigma^2}{1 - \lambda^2}\]

---

## Card 15

**Q:** What is the relation between the lag-1 autocovariance \(\gamma_x(1)\) and the **cross-covariance \(\gamma_{xy}(0)\)**?

**A:** Substituting the system equations yields:
\[\gamma_x(1) = \lambda \gamma_{xy}(0)\]
where \(\gamma_{xy}(0)\) is the contemporaneous cross-covariance.

---

## Card 16

**Q:** What is the **generic autocovariance** \(\gamma_x(k)\) for an **even lag** \(k = 2m\)?

**A:** For even \(k \geq 0\):
\[\gamma_x(k) = \lambda^k \cdot \frac{\sigma^2}{1 - \lambda^2}\]

---

## Card 17

**Q:** What is the physical **intuition** behind the geometric decay of the autocovariance \(\gamma_x(k)\)?

**A:** Each extra lag multiplies the autocovariance by \(\lambda\). This **geometric decay** is identical to a univariate **\(\text{AR}(1)\)** because, after decoupling, each mode is an independent **\(\text{AR}(1)\)**.

---

## Card 18

**Q:** How is the **cross-covariance** \(\gamma_{xy}(k)\) between \(x\) and \(y\) at lag \(k\) defined?

**A:** It is defined as:
\[\gamma_{xy}(k) = \text{Cov}(x_t, y_{t-k}) = E[x_t y_{t-k}]\]

---

## Card 19

**Q:** What is the **contemporaneous cross-covariance** \(\gamma_{xy}(0)\) between \(x_t\) and \(y_t\)?

**A:** The contemporaneous cross-covariance is:
\[\gamma_{xy}(0) = 0\]

---

## Card 20

**Q:** Why are \(x_t\) and \(y_t\) **contemporaneously uncorrelated** (i.e., \(\gamma_{xy}(0) = 0\))?

**A:** Because \(x_t\) and \(y_t\) share information **only through the lagged transmission channel**; their shared information takes a period to propagate.

---

## Card 21

**Q:** What is the **lag-1 cross-covariance** \(\gamma_{xy}(1)\)?

**A:** The lag-1 cross-covariance is:
\[\gamma_{xy}(1) = \frac{\lambda \sigma^2}{1 - \lambda^2}\]

---

## Card 22

**Q:** What is the general formula for the **cross-covariance** \(\gamma_{xy}(k)\) for all \(k \geq 0\)?

**A:** The formula is:
\[\gamma_{xy}(k) = \begin{cases} 0 & k = 0 \\ \lambda^k \cdot \dfrac{\sigma^2}{1-\lambda^2} & k \geq 1 \end{cases}\]

---

## Card 23

**Q:** What is the definition and formula for the **Autocorrelation Function (ACF)** \(\rho_x(k)\)?

**A:** The ACF is the autocovariance normalized by the variance:
\[\rho_x(k) = \frac{\gamma_x(k)}{\gamma_x(0)} = \lambda^k \quad \text{for } k \geq 0\]

---

## Card 24

**Q:** How does the **Autocorrelation Function (ACF)** behave for \(0 < \lambda < 1\) versus \(-1 < \lambda < 0\)?

**A:** For \(0 < \lambda < 1\), the ACF **decays smoothly to zero** (persistent positive autocorrelation). For \(-1 < \lambda < 0\), the ACF **alternates in sign** (oscillating mean reversion).

---

## Card 25

**Q:** What are the two **decoupled AR(1) modes**, \(u_t\) and \(v_t\), used to solve the system?

**A:** The decoupled modes are:
\[u_t = x_t + y_t \quad \text{with eigenvalue } +\lambda\]
\[v_t = x_t - y_t \quad \text{with eigenvalue } -\lambda\]

---

## Card 26

**Q:** What are the **decoupled AR(1) process equations** for \(u_t\) and \(v_t\)?

**A:** The decoupled equations are:
\[u_t = \lambda u_{t-1} + \sigma(z_t + w_t)\]
\[v_t = -\lambda v_{t-1} + \sigma(z_t - w_t)\]

---

## Card 27

**Q:** What is the **\(\text{MA}(\infty)\) representation** of \(x_t\)?

**A:** The \(\text{MA}(\infty)\) representation is:
\[x_t = \sigma \sum_{m=0}^{\infty} \lambda^{2m} z_{t-2m} + \sigma \sum_{m=0}^{\infty} \lambda^{2m+1} w_{t-2m-1}\]

---

## Card 28

**Q:** What is the physical intuition of the **\(\text{MA}(\infty)\) lags** for \(x_t\)?

**A:** \(x_t\) depends on its **own past shocks (\(z\)) at even lags** (\(0, 2, 4, \dots\)) and on **\(y\)'s past shocks (\(w\)) at odd lags** (\(1, 3, 5, \dots\)). Shocks propagate across variables every other period.

---

## Card 29

**Q:** What is the **one-step ahead forecast** \(E[x_{t+1} | \mathcal{F}_t]\)?

**A:** The one-step ahead forecast is:
\[E[x_{t+1} | \mathcal{F}_t] = \lambda y_t\]

---

## Card 30

**Q:** What is the **generic \(h\)-step ahead forecast** \(E[x_{t+h} | \mathcal{F}_t]\) for horizon \(h \geq 1\)?

**A:** The generic forecast is:
\[E[x_{t+h} | \mathcal{F}_t] = \begin{cases} \lambda^h x_t & h \text{ even} \\ \lambda^h y_t & h \text{ odd} \end{cases}\]

---
