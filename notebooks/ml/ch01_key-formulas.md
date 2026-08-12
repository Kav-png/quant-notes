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
