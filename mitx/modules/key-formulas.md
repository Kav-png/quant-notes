# MITx — Key Formulas

A running reference of core formulas. Sourced from ML notes.

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
d(\mathbf{x}) = \frac{\theta \cdot \mathbf{x} + \theta_0}{\|\theta\|}
\]
- \(d > 0\): point is on the **positive** side (same direction as \(\theta\))
- \(d < 0\): point is on the **negative** side
- \(d = 0\): point lies **on** the plane

### Perpendicular Distance
\[
\text{dist}(\mathbf{x}, H) = \frac{|\theta \cdot \mathbf{x} + \theta_0|}{\|\theta\|}
\]
SVM margin \(= \frac{2}{\|\theta\|}\) (distance between support hyperplanes \(\theta \cdot \mathbf{x} + \theta_0 = \pm 1\))

### Projection of a Point onto the Hyperplane
\[
\mathbf{x}_{\text{proj}} = \mathbf{x} - \frac{\theta \cdot \mathbf{x} + \theta_0}{\|\theta\|^2}\,\theta
\]
```python
x_proj = x - ((theta @ x + theta_0) / np.linalg.norm(theta)**2) * theta
```

### How \(\theta_0\) Offsets the Plane
Changing \(\theta_0\) slides the plane along \(\theta\) without rotating it:
\[
\text{shift} = -\frac{\theta_0}{\|\theta\|}
\]

---

## Probability & Distributions

### PDF of a Transformed Gaussian: Y = 2X

**Setup:** Let \( X \sim \mathcal{N}(\mu, \sigma^2) \), and define \( Y = 2X \).

Since \( \mathbf{E}[Y] = 2\mu \) and \( \text{Var}[Y] = 4\sigma^2 \):

\[
f_Y(y) = \frac{1}{2\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(y - 2\mu)^2}{8\sigma^2}\right)
\]

**Change of Variables formula** (for monotone \( g \)):
\[
f_Y(y) = \frac{f_X(g^{-1}(y))}{|g'(g^{-1}(y))|}
\]

---

## Calculus

### Chain Rule
\[
\frac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x)
\]

### Exponential Derivative
\[
\frac{d}{dx} e^{-\theta x} = -\theta e^{-\theta x}
\]
\[
\frac{\partial}{\partial \theta} e^{-\theta x} = -x e^{-\theta x}
\]
