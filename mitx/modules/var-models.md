---
difficulty: medium
status: in-progress
tags:
- time-series
- VAR
- multivariate
- stationarity
topic: Vector Autoregressive (VAR) Models
---

# Vector Autoregressive (VAR) Models

> **One-line summary:** A VAR model is just an AR(1) where the single variable becomes a vector of variables — the coefficient becomes a matrix, and the noise becomes a vector of shocks.

---

## What is a VAR Model?

A **Vector Autoregressive (VAR)** model is a multivariate time series model where multiple variables interact and are jointly driven by their past histories. Each variable's current value depends linearly on the previous values of *all* variables in the system, plus new independent noise.

**Why use them?**

- Capture complex cross-variable dynamics that a univariate AR model can't see
- In finance: identify common factors (market trends, industry exposures) driving multiple assets simultaneously
- Compact and tractable — the linear structure means we can use linear algebra to solve them exactly

---

## General Structure

For $N$ variables, stack them into a vector $\xi_t$ and write:

$$\xi_t = M \xi_{t-1} + \sigma \eta_t$$

where:
- $\xi_t \in \mathbb{R}^N$ — vector of variables at time $t$
- $M \in \mathbb{R}^{N \times N}$ — coefficient matrix encoding all cross-variable dependencies
- $\eta_t \in \mathbb{R}^N$ — vector of independent noise shocks, $E[\eta_t] = 0$, $E[\eta_t \eta_t^T] = I$
- $\sigma$ — scalar noise scaling

**Key difference from univariate AR(1):** The coefficient $\lambda$ becomes a matrix $M$. Stationarity, variance, and autocovariance all follow the same logic — but now we need linear algebra to handle the matrix structure.

---

## The Coupling Problem

In a VAR, variables are **coupled** — you can't solve for $x_t$ without knowing $y_{t-1}$, and vice versa. Naively trying to substitute is circular and messy.

**Example — HW2 system:**

$$x_t = \lambda y_{t-1} + \sigma z_t$$
$$y_t = \lambda x_{t-1} + \sigma w_t$$

In matrix form: $M = \begin{pmatrix} 0 & \lambda \\ \lambda & 0 \end{pmatrix}$

$M$ is a swap matrix — it exchanges $x$ and $y$ while scaling by $\lambda$. The variables are entangled because each feeds into the other with a one-period lag.

---

## Solving by Diagonalization

The core technique is to **diagonalize $M$**, finding linear combinations of the original variables that evolve independently.

**Step 1 — Eigendecompose $M$:**

$$M = V \Gamma V^{-1}$$

where $V$ = eigenvector matrix, $\Gamma$ = diagonal eigenvalue matrix.

**Step 2 — Change variables:** Define $\xi'_t = V^{-1} \xi_t$. Substituting:

$$\xi'_t = \Gamma \xi'_{t-1} + \sigma V^{-1}\eta_t$$

Since $\Gamma$ is diagonal, this is $N$ completely independent univariate AR(1) equations.

**Step 3 — Solve each AR(1)** using standard results, then apply $V$ to transform back.

> See the **linear-algebra-prereqs** note for the full derivation of eigenvalues, eigenvectors, and why $V^{-1} = V^T$ for symmetric $M$.

---

## Stationarity

A VAR is **weakly stationary** if all eigenvalues of $M$ satisfy $|\gamma_i| < 1$. This is the direct generalisation of the univariate AR(1) condition $|\lambda| < 1$.

**Why:** After diagonalizing, each decoupled component is an AR(1) with coefficient $\gamma_i$. For the process to have finite, time-invariant variance, each of those must be stationary.

**Example — HW2:** Eigenvalues are $+\lambda$ and $-\lambda$, so stationarity requires $|\lambda| < 1$.

---

## Variance and Autocovariance

Because diagonalization reduces everything to independent AR(1)s, you can reuse univariate results component by component.

**For each decoupled component with eigenvalue $\gamma_i$:**

$$\text{Var}(\xi'_{i,t}) = \frac{\sigma_i^2}{1 - \gamma_i^2}$$

$$\text{Cov}(\xi'_{i,t}, \xi'_{i,t-k}) = \gamma_i^k \cdot \text{Var}(\xi'_{i,t})$$

**Then invert back** using $\xi_t = V\xi'_t$ to get variances and covariances of the original variables.

**Example — HW2 full solution:**

After diagonalizing, the two independent modes are:

$$u_t = x_t + y_t, \quad \text{eigenvalue } +\lambda \implies \text{Var}(u_t) = \frac{2\sigma^2}{1-\lambda^2}$$

$$v_t = x_t - y_t, \quad \text{eigenvalue } -\lambda \implies \text{Var}(v_t) = \frac{2\sigma^2}{1-\lambda^2}$$

Since $x_t = \frac{u_t + v_t}{2}$:

$$\text{Var}(x_t) = \frac{1}{4}[\text{Var}(u_t) + \text{Var}(v_t)] = \frac{\sigma^2}{1-\lambda^2}$$

Same result as a univariate AR(1) with coefficient $\lambda$ — intuitive, since each variable is really just one mode in disguise.

---

## Finance Intuition

VAR models are widely used in finance because real assets don't move in isolation. A VAR captures:

- **Contagion:** a shock to one asset propagating to others
- **Common factors:** market-wide or sector-wide drivers that move multiple assets together
- **Lead-lag relationships:** one asset predicting another with a time lag

The eigendecomposition reveals the **underlying factor structure** — each eigenvector is a portfolio (linear combination of assets) that evolves independently, and each eigenvalue tells you how persistent that factor is.

---

## Summary

| Concept | Univariate AR(1) | VAR |
|---------|-----------------|-----|
| State | Scalar $x_t$ | Vector $\xi_t$ |
| Coefficient | Scalar $\lambda$ | Matrix $M$ |
| Stationarity | $|\lambda| < 1$ | All eigenvalues of $M$ inside unit circle |
| Variance | $\frac{\sigma^2}{1-\lambda^2}$ | Solve per decoupled component, then invert |
| Key tool | Algebra | Eigendecomposition + linear algebra |

> **The punchline:** A VAR is just $N$ AR(1)s in disguise. The eigenvectors of $M$ reveal which $N$ combinations of variables those are, and once you find them, everything reduces to tools you already know.
