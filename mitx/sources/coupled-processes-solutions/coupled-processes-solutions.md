---
difficulty: hard
status: in-progress
tags:
- time-series
- coupled-processes
- autocovariance
- stationarity
- forecasting
topic: Solving Coupled Processes — Full Generic Reference
---
# Solving Coupled Processes — Full Generic Reference

> **Setup:** A stationary coupled system of two variables \(x_t\) and \(y_t\):
>
> \(x_t = \lambda y_{t-1} + \sigma z_t\)
>
> \(y_t = \lambda x_{t-1} + \sigma w_t\)
>
> where \(z_t, w_t \sim \mathcal{N}(0,1)\) are i.i.d., independent of each other across all \(t, s\).

---

## 1. Stationarity Conditions

**What stationarity means:** The mean, variance, and autocovariance of \(x_t\) and \(y_t\) do not depend on time \(t\) — the process has settled into a stable, time-invariant distribution.

**How to find the condition:** Write the system in matrix form \(C_t = M C_{t-1} + \sigma \eta_t\) where \(M = \begin{pmatrix} 0 & \lambda \\ \lambda & 0 \end{pmatrix}\). The system is stationary if and only if all eigenvalues of \(M\) lie strictly inside the unit circle.

**Proof — finding eigenvalues of \(M\):**

\(\det(M - \gamma I) = 0\)

\(\det\begin{pmatrix} -\gamma & \lambda \\ \lambda & -\gamma \end{pmatrix} = \gamma^2 - \lambda^2 = 0\)

\(\implies \gamma_1 = +\lambda, \quad \gamma_2 = -\lambda\)

**Stationarity condition:** \(|\gamma_1| < 1\) and \(|\gamma_2| < 1\), which both reduce to:

\(\boxed{|\lambda| < 1}\)

**Proof that stationarity implies time-invariant moments:** If the process is stationary then \(\text{Var}(x_t) = \text{Var}(x_{t-1}) \equiv \sigma_x^2\) for all \(t\). We use this self-consistency condition to solve for \(\sigma_x^2\) below.

---

## 2. Mean

**Goal:** Find \(E[x_t]\) and \(E[y_t]\).

**Step 1 — Take expectations of both equations:**

\(E[x_t] = \lambda E[y_{t-1}] + \sigma E[z_t]\)

\(E[y_t] = \lambda E[x_{t-1}] + \sigma E[w_t]\)

**Step 2 — Apply \(E[z_t] = E[w_t] = 0\):**

\(E[x_t] = \lambda E[y_{t-1}]\)

\(E[y_t] = \lambda E[x_{t-1}]\)

**Step 3 — Apply stationarity:** \(E[x_t] = E[x_{t-1}] \equiv \mu_x\) and \(E[y_t] = E[y_{t-1}] \equiv \mu_y\):

\(\mu_x = \lambda \mu_y\)

\(\mu_y = \lambda \mu_x\)

**Step 4 — Solve the system:** Substitute the first into the second:

\(\mu_y = \lambda(\lambda \mu_y) = \lambda^2 \mu_y\)

\(\mu_y(1 - \lambda^2) = 0\)

Since \(|\lambda| < 1\) we have \(\lambda^2 \neq 1\), so:

\(\boxed{\mu_x = \mu_y = 0}\)

---

## 3. Variance

**Goal:** Find \(\text{Var}(x_t)\) and \(\text{Var}(y_t)\).

Since \(\mu_x = \mu_y = 0\), variance equals the second moment: \(\text{Var}(x_t) = E[x_t^2]\).

**Step 1 — Square both sides of \(x_t = \lambda y_{t-1} + \sigma z_t\):**

\(x_t^2 = \lambda^2 y_{t-1}^2 + 2\lambda\sigma y_{t-1} z_t + \sigma^2 z_t^2\)

**Step 2 — Take expectations:**

\(E[x_t^2] = \lambda^2 E[y_{t-1}^2] + 2\lambda\sigma E[y_{t-1} z_t] + \sigma^2 E[z_t^2]\)

**Step 3 — Simplify each term:**

- \(E[y_{t-1}^2] = \text{Var}(y_{t-1}) \equiv \sigma_y^2\) (stationarity)
- \(E[y_{t-1} z_t] = 0\) because \(y_{t-1}\) depends only on shocks up to time \(t-1\), and \(z_t\) is a fresh shock at time \(t\), independent of everything before it
- \(E[z_t^2] = 1\) since \(z_t \sim \mathcal{N}(0,1)\)

\(\sigma_x^2 = \lambda^2 \sigma_y^2 + \sigma^2\)

**Step 4 — By symmetry** of the system (\(x\) and \(y\) play identical roles), \(\sigma_x^2 = \sigma_y^2 \equiv \sigma_{xy}^2\):

\(\sigma_{xy}^2 = \lambda^2 \sigma_{xy}^2 + \sigma^2\)

\(\sigma_{xy}^2 (1 - \lambda^2) = \sigma^2\)

\(\boxed{\text{Var}(x_t) = \text{Var}(y_t) = \frac{\sigma^2}{1 - \lambda^2}}\)

---

## 4. Autocovariance at Lag \(k\)

**Definition:** \(\gamma_x(k) = \text{Cov}(x_t, x_{t-k}) = E[x_t x_{t-k}]\) (since \(\mu_x = 0\)).

### Lag 1

**Step 1 — Write out \(E[x_t x_{t-1}]\). Substitute \(x_t = \lambda y_{t-1} + \sigma z_t\):**

\(E[x_t x_{t-1}] = E[(\lambda y_{t-1} + \sigma z_t) x_{t-1}]\)

\(= \lambda E[y_{t-1} x_{t-1}] + \sigma E[z_t x_{t-1}]\)

**Step 2 — Simplify each term:**

- \(E[y_{t-1} x_{t-1}] = \text{Cov}(x_{t-1}, y_{t-1}) \equiv \gamma_{xy}(0)\) (the contemporaneous cross-covariance, derived in §5)
- \(E[z_t x_{t-1}] = 0\) because \(x_{t-1}\) depends on shocks up to \(t-1\), and \(z_t\) is independent of all of them

\(\gamma_x(1) = \lambda \gamma_{xy}(0)\)

We derive \(\gamma_{xy}(0)\) in §5. Substituting the result \(\gamma_{xy}(0) = \frac{\lambda \sigma^2}{1 - \lambda^2}\):

\(\boxed{\gamma_x(1) = \frac{\lambda^2 \sigma^2}{1 - \lambda^2}}\)

### Generic Lag \(k\)

**Step 1 — Multiply both sides of \(x_t = \lambda y_{t-1} + \sigma z_t\) by \(x_{t-k}\) and take expectations:**

\(E[x_t x_{t-k}] = \lambda E[y_{t-1} x_{t-k}] + \sigma E[z_t x_{t-k}]\)

**Step 2 — For \(k \geq 1\):** \(x_{t-k}\) depends only on shocks up to time \(t-k\), so \(E[z_t x_{t-k}] = 0\).

\(\gamma_x(k) = \lambda \cdot \text{Cov}(y_{t-1}, x_{t-k}) = \lambda \cdot \gamma_{xy}(k-1)\)

where \(\gamma_{xy}(k-1) = \text{Cov}(y_t, x_{t-(k-1)})\) is the cross-covariance at lag \(k-1\) (derived in §5).

**Result for even \(k = 2m\):**

\(\boxed{\gamma_x(k) = \lambda^k \cdot \frac{\sigma^2}{1-\lambda^2}} \quad \text{for } k \geq 0\)

**Intuition:** Each extra lag multiplies by \(\lambda\) — the autocovariance decays geometrically, exactly like a univariate AR(1). This is because after decoupling, each mode is an AR(1).

---

## 5. Cross-Covariance Between \(x\) and \(y\)

**Definition:** \(\gamma_{xy}(k) = \text{Cov}(x_t, y_{t-k}) = E[x_t y_{t-k}]\).

### Contemporaneous: \(k = 0\)

**Step 1 — Compute \(E[x_t y_t]\). Substitute both equations:**

\(E[x_t y_t] = E[(\lambda y_{t-1} + \sigma z_t)(\lambda x_{t-1} + \sigma w_t)]\)

**Step 2 — Expand:**

\(= \lambda^2 E[y_{t-1} x_{t-1}] + \lambda\sigma E[y_{t-1} w_t] + \lambda\sigma E[z_t x_{t-1}] + \sigma^2 E[z_t w_t]\)

**Step 3 — Simplify each term:**

- \(E[y_{t-1} x_{t-1}] = \gamma_{xy}(0)\) (what we're solving for — self-consistency)
- \(E[y_{t-1} w_t] = 0\) (\(y_{t-1}\) is in the past, \(w_t\) is a fresh shock)
- \(E[z_t x_{t-1}] = 0\) (\(x_{t-1}\) is in the past, \(z_t\) is fresh)
- \(E[z_t w_t] = 0\) (\(z_t\) and \(w_t\) are independent by assumption)

\(\gamma_{xy}(0) = \lambda^2 \gamma_{xy}(0)\)

\(\gamma_{xy}(0)(1 - \lambda^2) = 0 \implies \gamma_{xy}(0) = 0\)

Wait — this gives zero, but lag-1 cross-covariance is non-zero. Let's check lag 1:

### Lag 1: \(k = 1\)

**Step 1 — Compute \(E[x_t y_{t-1}]\). Substitute \(x_t = \lambda y_{t-1} + \sigma z_t\):**

\(E[x_t y_{t-1}] = E[(\lambda y_{t-1} + \sigma z_t) y_{t-1}]\)

\(= \lambda E[y_{t-1}^2] + \sigma E[z_t y_{t-1}]\)

**Step 2 — Simplify:**

- \(E[y_{t-1}^2] = \sigma_y^2 = \frac{\sigma^2}{1-\lambda^2}\)
- \(E[z_t y_{t-1}] = 0\) (past \(y\) independent of future shock \(z_t\))

\(\boxed{\gamma_{xy}(1) = \frac{\lambda\sigma^2}{1-\lambda^2}}\)

### Generic Lag \(k\)

\(\boxed{\gamma_{xy}(k) = \begin{cases} 0 & k = 0 \\ \lambda^k \cdot \dfrac{\sigma^2}{1-\lambda^2} & k \geq 1 \end{cases}}\)

**Intuition:** \(x_t\) and \(y_{t-k}\) share information only through the lagged transmission channel. At lag 0 they are contemporaneously uncorrelated (their shared information only shows up with a lag), but at lag 1 and beyond the coupling kicks in.

---

## 6. Autocorrelation Function (ACF)

**Definition:** The ACF is the autocovariance normalised by the variance:

\(\rho_x(k) = \frac{\gamma_x(k)}{\gamma_x(0)} = \frac{\text{Cov}(x_t, x_{t-k})}{\text{Var}(x_t)}\)

**Derivation:**

\(\rho_x(k) = \frac{\lambda^k \cdot \frac{\sigma^2}{1-\lambda^2}}{\frac{\sigma^2}{1-\lambda^2}} = \lambda^k\)

\(\boxed{\rho_x(k) = \lambda^k, \quad k \geq 0}\)

**Properties:**

- \(\rho_x(0) = 1\) always (a variable is perfectly correlated with itself)
- For \(0 < \lambda < 1\): ACF decays smoothly to zero — persistent positive autocorrelation
- For \(-1 < \lambda < 0\): ACF alternates in sign — oscillating mean reversion
- ACF is the same for \(y_t\) by symmetry

**Why this looks like a univariate AR(1):** After decoupling, each mode is exactly an AR(1). The ACF of a coupled system inherits the AR(1) shape from its eigenvalues.

---

## 7. MA(\(\infty\)) Representation

**Goal:** Express \(x_t\) purely in terms of current and past shocks \(z_s, w_s\).

**Method:** Use the decoupled modes \(u_t = x_t + y_t\) and \(v_t = x_t - y_t\).

**Step 1 — Decoupled AR(1)s:**

\(u_t = \lambda u_{t-1} + \sigma(z_t + w_t)\)

\(v_t = -\lambda v_{t-1} + \sigma(z_t - w_t)\)

**Step 2 — Apply MA(\(\infty\)) recursion to each** (same as univariate AR(1)):

\(u_t = \sigma \sum_{j=0}^{\infty} \lambda^j (z_{t-j} + w_{t-j})\)

\(v_t = \sigma \sum_{j=0}^{\infty} (-\lambda)^j (z_{t-j} - w_{t-j})\)

**Step 3 — Recover \(x_t = \frac{u_t + v_t}{2}\):**

\(x_t = \frac{\sigma}{2} \sum_{j=0}^{\infty} \left[\lambda^j + (-\lambda)^j\right] z_{t-j} + \frac{\sigma}{2} \sum_{j=0}^{\infty} \left[\lambda^j - (-\lambda)^j\right] w_{t-j}\)

**Step 4 — Simplify using \(\lambda^j + (-\lambda)^j = 2\lambda^j\) for even \(j\), \(0\) for odd \(j\):**

\(\boxed{x_t = \sigma \sum_{m=0}^{\infty} \lambda^{2m} z_{t-2m} + \sigma \sum_{m=0}^{\infty} \lambda^{2m+1} w_{t-2m-1}}\)

**Intuition:** \(x_t\) depends on its own past shocks \(z\) at even lags (0, 2, 4, ...) and on \(y\)'s past shocks \(w\) at odd lags (1, 3, 5, ...). The coupling propagates shocks across variables every other period.

---

## 8. Forecasting and Conditional Expectation

**Goal:** Given information up to time \(t\), forecast \(x_{t+h}\) for horizon \(h \geq 1\).

Define \(\mathcal{F}_t = \{x_t, y_t, x_{t-1}, y_{t-1}, \ldots\}\) as all information available at time \(t\).

### One-step ahead (\(h = 1\))

\(E[x_{t+1} | \mathcal{F}_t] = E[\lambda y_t + \sigma z_{t+1} | \mathcal{F}_t]\)

\(= \lambda E[y_t | \mathcal{F}_t] + \sigma E[z_{t+1} | \mathcal{F}_t]\)

- \(E[y_t | \mathcal{F}_t] = y_t\) (already observed)
- \(E[z_{t+1} | \mathcal{F}_t] = 0\) (future shock, independent of all past)

\(\boxed{E[x_{t+1} | \mathcal{F}_t] = \lambda y_t}\)

### Two-step ahead (\(h = 2\))

\(E[x_{t+2} | \mathcal{F}_t] = E[\lambda y_{t+1} + \sigma z_{t+2} | \mathcal{F}_t] = \lambda E[y_{t+1} | \mathcal{F}_t]\)

Now compute \(E[y_{t+1} | \mathcal{F}_t] = \lambda x_t\) (by the same logic applied to \(y\)).

\(\boxed{E[x_{t+2} | \mathcal{F}_t] = \lambda^2 x_t}\)

### Generic horizon \(h\)

By induction, alternating between \(x\) and \(y\) at each step:

\(\boxed{E[x_{t+h} | \mathcal{F}_t] = \begin{cases} \lambda^h x_t & h \text{ even} \\ \lambda^h y_t & h \text{ odd} \end{cases}}\)

**Forecast error variance at horizon \(h\):**

\(\text{Var}(x_{t+h} - E[x_{t+h}|\mathcal{F}_t]) = \sigma^2 \sum_{j=0}^{h-1} \lambda^{2j} = \sigma^2 \cdot \frac{1 - \lambda^{2h}}{1 - \lambda^2}\)

As \(h \to \infty\), this converges to \(\frac{\sigma^2}{1-\lambda^2} = \text{Var}(x_t)\) — long-run forecasts are no better than the unconditional distribution.

---

## Cheatsheet

| Quantity | Formula | Notes |
| --- | --- | --- |
| **Stationarity** |  | Eigenvalues of \(M\) inside unit circle |
| **Mean** |  | From \(E[z_t] = E[w_t] = 0\) |
| **Variance** |  | Same for \(x\) and \(y\) by symmetry |
| **Autocovariance** |  | Geometric decay in \(k\) |
| **ACF** |  | Pure geometric — same as AR(1) |
| **Cross-cov (lag 0)** |  | \(x_t, y_t\) contemporaneously uncorrelated |
| **Cross-cov (lag \(k \geq 1\))** |  | Coupling only through lags |
| **1-step forecast** |  | Depends on \(y\), not \(x\) |
| **2-step forecast** |  | Back to own variable |
| **\(h\)-step forecast** | \(\lambda^h x_t\) (even \(h\)), \(\lambda^h y_t\) (odd \(h\)) | Alternates each period |
| **Forecast error var** |  | Grows with \(h\), caps at \(\text{Var}(x_t)\) |
| **MA(\(\infty\))** |  | Even lags: own shocks; odd: cross shocks |

> **The master trick:** Decouple using \(u_t = x_t + y_t\) (eigenvalue \(+\lambda\)) and \(v_t = x_t - y_t\) (eigenvalue \(-\lambda\)). Each is an independent AR(1). Solve, then invert: \(x_t = \frac{u_t + v_t}{2}\), \(y_t = \frac{u_t - v_t}{2}\).

 