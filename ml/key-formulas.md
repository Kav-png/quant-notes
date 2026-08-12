# Machine Learning — Key Formulas

A running reference of all core formulas covered. New topics will be appended here as we go.

---

## Geometry & Linear Algebra

### Hyperplane Definition
A hyperplane in \(\mathbb{R}^n\) is the set of all points \(\mathbf{x}\) satisfying:
\[
\theta \cdot \mathbf{x} + \theta_0 = 0
\]
- \(\theta\) is the **normal vector** (perpendicular to the plane)
- \(\theta_0\) is the **bias / offset**

### Signed Distance from a Point to a Hyperplane
\[
d = \frac{\theta \cdot \mathbf{x} + \theta_0}{\|\theta\|}
\]
- Positive \(d\): point is on the same side as \(\theta\)
- Negative \(d\): point is on the opposite side
- Zero: point lies **on** the plane

### Projection of a Point onto a Hyperplane
\[
\mathbf{x}_{\text{proj}} = \mathbf{x} - \frac{\theta \cdot \mathbf{x} + \theta_0}{\|\theta\|^2} \cdot \theta
\]
Code: `x - ((theta*x + theta_0) / norm(theta)**2) * theta`

---

<!-- Add new topics below this line -->


---

## Geometry & Linear Algebra

### Hyperplane Definition
A hyperplane in \(\mathbb{R}^n\) is the set of all points \(\mathbf{x}\) satisfying:
\[
\theta \cdot \mathbf{x} + \theta_0 = 0
\]
- \(\theta\) is the **normal vector** (perpendicular to the plane)
- \(\theta_0\) is the **bias / offset**

### Signed Distance from a Point to a Hyperplane
\[
d = \frac{\theta \cdot \mathbf{x} + \theta_0}{\|\theta\|}
\]
- Positive \(d\): point is on the same side as \(\theta\)
- Negative \(d\): point is on the opposite side
- Zero: point lies **on** the plane

### Projection of a Point onto a Hyperplane
\[
\mathbf{x}_{\text{proj}} = \mathbf{x} - \frac{\theta \cdot \mathbf{x} + \theta_0}{\|\theta\|^2} \cdot \theta
\]
Code: `x - ((theta*x + theta_0) / norm(theta)**2) * theta`


---

## Planes, Signed Distances & Projections

### Hyperplane (recap)
A hyperplane is defined by all points \(\mathbf{x}\) satisfying:
\[
\theta \cdot \mathbf{x} + \theta_0 = 0
\]
- \(\theta\) — normal vector, points perpendicularly away from the plane
- \(\theta_0\) — bias / offset that **shifts** the plane parallel to itself (see below)

---

### Signed Distance from Point to Hyperplane
\[
d(\mathbf{x}) = \frac{\theta \cdot \mathbf{x} + \theta_0}{\|\theta\|}
\]
- \(d > 0\): \(\mathbf{x}\) lies on the **positive** side (same direction as \(\theta\))
- \(d < 0\): \(\mathbf{x}\) lies on the **negative** side
- \(d = 0\): \(\mathbf{x}\) is **on** the plane

The sign encodes which side of the decision boundary a point falls on — critical for classifiers.

---

### Perpendicular (Euclidean) Distance from Point to Hyperplane
\[
\text{dist}(\mathbf{x}, H) = |d(\mathbf{x})| = \frac{|\theta \cdot \mathbf{x} + \theta_0|}{\|\theta\|}
\]
Always non-negative. Used in SVM margin calculations:
- Margin \(= \frac{2}{\|\theta\|}\) (distance between the two support hyperplanes \(\theta \cdot \mathbf{x} + \theta_0 = \pm 1\))

---

### Projection of a Point onto the Hyperplane
Drop \(\mathbf{x}\) perpendicularly onto the plane:
\[
\mathbf{x}_{\text{proj}} = \mathbf{x} - \frac{\theta \cdot \mathbf{x} + \theta_0}{\|\theta\|^2}\,\theta
\]
The subtracted term \(\frac{\theta \cdot \mathbf{x} + \theta_0}{\|\theta\|^2}\,\theta\) is the **component of \(\mathbf{x}\) along the normal** — removing it leaves only the in-plane component.

```python
x_proj = x - ((theta @ x + theta_0) / np.linalg.norm(theta)**2) * theta
```

---

### How \(\theta_0\) Offsets the Plane

When \(\theta_0 = 0\) the hyperplane passes through the **origin**.  
Changing \(\theta_0\) slides the plane along \(\theta\) **without rotating it**:

\[
\text{shift} = -\frac{\theta_0}{\|\theta\|}
\]

Intuition:
- \(\theta_0 > 0\) → plane moves in the **opposite** direction to \(\theta\)  
- \(\theta_0 < 0\) → plane moves in the **same** direction as \(\theta\)

You can verify: the point \(-\frac{\theta_0}{\|\theta\|^2}\,\theta\) always satisfies \(\theta \cdot \mathbf{x} + \theta_0 = 0\), confirming it lies on the plane regardless of \(\theta_0\).

In a linear classifier \(\hat{y} = \text{sign}(\theta \cdot \mathbf{x} + \theta_0)\), \(\theta_0\) lets the decision boundary sit anywhere in feature space — without it, every boundary is forced through the origin.



## PDF of a Transformed Gaussian: Y = 2X

**Setup:** Let \( X \sim \mathcal{N}(\mu, \sigma^2) \), and define \( Y = 2X \).

### Method 1: Properties of Normal Distribution

Using linearity of expectation and variance scaling:
- \( \mathbf{E}[Y] = 2\mu \)
- \( \text{Var}[Y] = 4\sigma^2 \)

So \( Y \sim \mathcal{N}(2\mu, 4\sigma^2) \), giving:

\[
f_Y(y) = \frac{1}{2\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(y - 2\mu)^2}{8\sigma^2}\right)
\]

### Method 2: Change of Variables

For \( Y = g(X) \) with \( g \) monotone:

\[
f_Y(y) = \frac{f_X(g^{-1}(y))}{|g'(g^{-1}(y))|}
\]

Here \( g(x) = 2x \), so \( g^{-1}(y) = y/2 \) and \( g'(x) = 2 \). Substituting:

\[
f_Y(y) = \frac{1}{2} \cdot \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(y/2 - \mu)^2}{2\sigma^2}\right) = \frac{1}{2\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(y - 2\mu)^2}{8\sigma^2}\right)
\]

Both methods agree. ✓
