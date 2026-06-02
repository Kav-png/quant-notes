---
difficulty: hard
status: in-progress
tags:
- linear-algebra
- prerequisites
- eigenvectors
- matrices
topic: Linear Algebra Prerequisites for Multivariate Time Series
---
# Linear Algebra Prerequisites for VAR Models

> **Goal:** Build up all the tools needed to solve a coupled multivariate time series like the HW2 system \(x_t = \lambda y_{t-1} + \sigma z_t\), \(y_t = \lambda x_{t-1} + \sigma w_t\) — step by step, from scratch.

---

## 1. Vectors and Matrix Notation

**Definition:** A vector is just a column of numbers stacked together. For two variables \(x_t\) and \(y_t\) we write:

\(C_t = \begin{pmatrix} x_t \\ y_t \end{pmatrix}\)

A matrix is a rectangular array of numbers that acts on vectors — it transforms one vector into another.

**Intuition:** Think of a matrix as a machine: you feed in a vector, it spits out a new vector. The coefficient matrix \(M\) in a VAR model tells you how today's variables depend on yesterday's.

**Why we care:** Writing the coupled system as \(C_t = M C_{t-1} + \sigma \eta_t\) is just notation — nothing has changed mathematically. But now we can use all the tools of linear algebra on \(M\).

**Example — our HW2 system:**

\(M = \begin{pmatrix} 0 & \lambda \\ \lambda & 0 \end{pmatrix}, \quad C_t = \begin{pmatrix} x_t \\ y_t \end{pmatrix}, \quad \eta_t = \begin{pmatrix} z_t \\ w_t \end{pmatrix}\)

Check: \(M C_{t-1} = \begin{pmatrix} 0 & \lambda \\ \lambda & 0 \end{pmatrix} \begin{pmatrix} x_{t-1} \\ y_{t-1} \end{pmatrix} = \begin{pmatrix} \lambda y_{t-1} \\ \lambda x_{t-1} \end{pmatrix}\) — exactly the original equations. \(M\) is just swapping and scaling.

---

## 2. Eigenvalues

**Definition:** A scalar \(\gamma\) is an **eigenvalue** of matrix \(M\) if there exists a non-zero vector \(v\) such that:

\(Mv = \gamma v\)

The matrix acting on \(v\) just scales it — no rotation, no mixing. That's the key property.

**Intuition:** Most vectors get rotated and stretched when you apply \(M\). Eigenvectors are the special directions that \(M\) only stretches (or flips), never rotates. The eigenvalue \(\gamma\) tells you the stretch factor.

**How to find eigenvalues — the characteristic equation:**

Rearranging \(Mv = \gamma v\) gives \((M - \gamma I)v = 0\). For a non-zero solution \(v\) to exist, the matrix \((M - \gamma I)\) must be singular, i.e. its determinant is zero:

\(\det(M - \gamma I) = 0\)

This is the **characteristic equation**. Solving it gives the eigenvalues.

**Example — HW2 matrix:**

\(\det\begin{pmatrix} -\gamma & \lambda \\ \lambda & -\gamma \end{pmatrix} = \gamma^2 - \lambda^2 = 0\)

\(\implies \gamma = +\lambda \quad \text{or} \quad \gamma = -\lambda\)

Two eigenvalues, one for each independent mode of the system.

---

## 3. Eigenvectors

**Definition:** For each eigenvalue \(\gamma\), an **eigenvector** \(v\) satisfies \(Mv = \gamma v\). You find it by solving \((M - \gamma I)v = 0\).

**Intuition:** Eigenvectors are the "natural axes" of the transformation — the directions the system likes to move along. In our VAR, they reveal the hidden combinations of \(x\) and \(y\) that evolve independently.

**How to find eigenvectors — step by step:**

For each eigenvalue, substitute back and solve the linear system \((M - \gamma I)v = 0\).

**Example — \(\gamma_1 = +\lambda\):**

\((M - \lambda I)v = \begin{pmatrix} -\lambda & \lambda \\ \lambda & -\lambda \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}\)

Row 1: \(-\lambda v_1 + \lambda v_2 = 0 \implies v_1 = v_2\)

So \(v_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}\) (unnormalized). This means \(x + y\) is a natural mode — the sum evolves on its own.

**Example — \(\gamma_2 = -\lambda\):**

\((M + \lambda I)v = \begin{pmatrix} \lambda & \lambda \\ \lambda & \lambda \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}\)

Row 1: \(\lambda v_1 + \lambda v_2 = 0 \implies v_1 = -v_2\)

So \(v_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}\) (unnormalized). The difference \(x - y\) is the other natural mode.

**Normalization:** Since \(M\) is symmetric, its eigenvectors are orthogonal. We normalize using the Euclidean norm \(\|v\| = \sqrt{v_1^2 + v_2^2}\):

\(\hat{v}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}, \quad \hat{v}_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}\)

---

## 4. Diagonalization — \(M = V \Gamma V^{-1}\)

**Definition:** A matrix \(M\) is **diagonalized** by writing it as:

\(M = V \Gamma V^{-1}\)

where:

- \(V\) = matrix whose **columns are the eigenvectors**
- \(\Gamma\) = **diagonal matrix of eigenvalues** (zeros everywhere off-diagonal)
- \(V^{-1}\) = inverse of \(V\)

**Intuition:** \(V\) is a change-of-basis matrix. It rotates from the "original" coordinates \((x, y)\) to the "natural" coordinates (eigenvector directions). In those natural coordinates, \(M\) just scales each direction independently — that's what the diagonal \(\Gamma\) means.

**Example — HW2:**

\(V = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}, \quad \Gamma = \begin{pmatrix} \lambda & 0 \\ 0 & -\lambda \end{pmatrix}\)

You can verify: \(M V = V \Gamma\), i.e. \(M\) times each column of \(V\) gives that column scaled by its eigenvalue.

---

## 5. Matrix Inverse

**Definition:** The inverse \(V^{-1}\) satisfies \(V V^{-1} = V^{-1} V = I\) (the identity matrix).

**General 2×2 formula:** For \(A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}\):

\(A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}\)

The quantity \(ad - bc\) is the **determinant** — if it's zero, the matrix has no inverse.

**Special case — orthogonal matrices:** When \(M\) is symmetric, its normalized eigenvectors are orthogonal to each other, making \(V\) an **orthogonal matrix**. Orthogonal matrices have the special property:

\(V^{-1} = V^T \quad \text{(transpose, not full inversion)}\)

**Intuition:** Transposing just flips rows and columns. For orthogonal matrices, this is all you need to invert — no division, no determinants. This is because orthogonal columns form a "pure rotation" with no stretching.

**Example — HW2:**

\(V^{-1} = V^T = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}^T = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\)

(This matrix happens to equal its own transpose — it's symmetric.)

---

## 6. Change of Variables — Decoupling

**The key move:** Substitute \(M = V\Gamma V^{-1}\) into the VAR equation and multiply both sides by \(V^{-1}\):

\(C_t = V\Gamma V^{-1} C_{t-1} + \sigma \eta_t\)

\(V^{-1} C_t = \Gamma (V^{-1} C_{t-1}) + \sigma V^{-1}\eta_t\)

Define \(C'_t = V^{-1} C_t\) (the transformed variables). Then:

\(C'_t = \Gamma C'_{t-1} + \sigma \eta'_t\)

Since \(\Gamma\) is **diagonal**, this is \(N\) fully independent univariate equations — one per eigenvalue. The coupling is gone.

**Example — HW2 decoupled equations:**

Let \(u_t = x_t + y_t\) and \(v_t = x_t - y_t\) (the two components of \(C'_t = V^{-1}C_t\), up to the \(\frac{1}{\sqrt{2}}\) factor):

\(u_t = \lambda u_{t-1} + \sigma(z_t + w_t) \quad \text{(AR(1) with coefficient } +\lambda\text{)}\)

\(v_t = -\lambda v_{t-1} + \sigma(z_t - w_t) \quad \text{(AR(1) with coefficient } -\lambda\text{)}\)

Each is a standard AR(1) you already know how to solve.

**Inverting back:** Once you have \(\text{Var}(u_t)\) and \(\text{Var}(v_t)\), use:

\(x_t = \frac{u_t + v_t}{2}, \quad y_t = \frac{u_t - v_t}{2}\)

to get back to the original variables.

---

## Summary — The Full Pipeline

| Step | What you do | Why |
| --- | --- | --- |
| **1. Stack** | Write \(C_t = MC_{t-1} + \sigma\eta_t\) | Compact notation, reveals structure |
| **2. Eigenvalues** | Solve \(\det(M - \gamma I) = 0\) | Find the natural stretch factors |
| **3. Eigenvectors** | Solve \((M - \gamma I)v = 0\) for each \(\gamma\) | Find the natural independent directions |
| **4. Build \(V\), \(\Gamma\)** | Columns of \(V\) = eigenvectors; \(\Gamma\) = diagonal eigenvalues | Set up the decomposition \(M = V\Gamma V^{-1}\) |
| **5. Invert \(V\)** | Use \(V^{-1} = V^T\) for symmetric \(M\) | Need this to change coordinates |
| **6. Decouple** | Define \(C'_t = V^{-1}C_t\), get \(N\) independent AR(1)s | Now solvable with standard tools |
| **7. Solve & invert** | Solve each AR(1), apply \(V\) to get back to \(x, y\) | Final answer in original variables |

> **The big idea:** A coupled system of \(N\) variables isn't really \(N\) entangled things — it's \(N\) independent modes in disguise. Eigenvectors reveal those modes, diagonalization separates them, and \(V^{-1}\) is the coordinate change that makes it all work.

---

## Resources

All from 3Blue1Brown's *Essence of Linear Algebra* series — visuals-first, no prerequisites needed.

| Topic in this note | Video | Chapter |
| --- | --- | --- |
| Vectors and matrix notation | [Vectors, what even are they?](https://www.youtube.com/watch?v=fNk_zzaMoSs) | Ch 1 |
| Matrices as transformations | [Linear transformations and matrices](https://www.youtube.com/watch?v=kYB8IZa5AuE) | Ch 3 |
| Determinant (needed for eigenvalues) | [The determinant](https://www.youtube.com/watch?v=Ip3X9LOh2dk) | Ch 6 |
| Matrix inverse | [Inverse matrices, column space and null space](https://www.youtube.com/watch?v=uQhTuRlWMxw) | Ch 7 |
| Change of variables / decoupling | [Change of basis](https://www.youtube.com/watch?v=P2LTAUO1TdA) | Ch 13 |
| Eigenvalues and eigenvectors | [Eigenvectors and eigenvalues](https://www.youtube.com/watch?v=PFDu9oVAE-g) | Ch 14 |

> **Recommended order:** Watch Ch 1 → 3 → 6 → 7 → 13 → 14. Each builds on the last. The full playlist is \~3 hours and covers everything in this note from scratch.

 