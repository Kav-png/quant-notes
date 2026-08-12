# Projections, Planes & Orthogonality

A deep-dive into the geometry behind projecting points onto hyperplanes.

---

## 1. What is a Hyperplane?

A **hyperplane** is a flat subspace of dimension \(n-1\) inside \(\mathbb{R}^n\). It is defined by: $
\theta \cdot \mathbf{x} + \theta_0 = 0
$

- In 2D: this is a **line**
- In 3D: this is a **plane**
- In \(n\)D: it is a hyperplane

The vector \(\theta\) is **orthogonal (perpendicular)** to every vector that lies within the plane. This is what makes it the **normal vector**.

---

## 2. Orthogonality

Two vectors \(\mathbf{u}\) and \(\mathbf{v}\) are **orthogonal** if: $
\mathbf{u} \cdot \mathbf{v} = 0
$Geometrically: they meet at a **90° angle**.

The normal vector \(\theta\) is orthogonal to the plane — meaning for any two points \(\mathbf{a}, \mathbf{b}\) on the plane: $
\theta \cdot (\mathbf{a} - \mathbf{b}) = 0
\(This is why subtracting in the direction of \)\theta$ moves you **straight toward** the plane — it is the shortest path.

---

## 3. Signed Distance

The **signed distance** from point \(\mathbf{x}\) to the plane \((\theta, \theta_0)\) is: $
d = \frac{\theta \cdot \mathbf{x} + \theta_0}{\|\theta\|}
$

| Value of \(d\) | Meaning |
| --- | --- |
|  | \(\mathbf{x}\) is on the \(\theta\)-side of the plane |
|  | \(\mathbf{x}\) is on the opposite side |
|  | \(\mathbf{x}\) lies **on** the plane |

The **sign** is meaningful — it tells you *which side* of the decision boundary a point is on. This is central to classifiers like SVMs.

The **magnitude** \(|d|\) is the Euclidean distance from \(\mathbf{x}\) to its nearest point on the plane.

---

## 4. Projection onto the Plane

### Intuition

Any point \(\mathbf{x}\) off the plane can be split into: \(\mathbf{x} = \underbrace{\mathbf{x}_{\text{proj}}}_{\text{lies on plane}} + \underbrace{d \cdot \hat{\theta}}_{\text{perpendicular "overhang"}}\)To project, we **remove the overhang**: $
\mathbf{x}_{\text{proj}} = \mathbf{x} - d \cdot \hat{\theta}
$

### Full Formula (substituting \(d\) and \(\hat{\theta} = \theta / \|\theta\|\))

$
\mathbf{x}_{\text{proj}} = \mathbf{x} - \frac{\theta \cdot \mathbf{x} + \theta_0}{\|\theta\|^2} \cdot \theta
$

The two \(\|\theta\|\) factors combine:

- One from the distance formula \(d = (\theta \cdot \mathbf{x} + \theta_0) / \|\theta\|\)
- One from the unit normal \(\hat{\theta} = \theta / \|\theta\|\)

### Code

```python
x - ((theta @ x + theta_0) / norm(theta)**2) * theta
```

### Sanity Check

If \(\mathbf{x}\) is already on the plane, then \(\theta \cdot \mathbf{x} + \theta_0 = 0\), so \(d = 0\) and nothing is subtracted. ✓

---

## 5. Summary of Key Ideas

| Concept | Formula | Meaning |
| --- | --- | --- |
| Plane equation |  | Defines the hyperplane |
| Normal vector |  | Points perpendicularly away from plane |
| Signed distance |  | How far & which side |
| Projection |  | Nearest point on plane |

 