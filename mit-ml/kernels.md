---
status: in_progress
tags:
- kernels
- perceptron
topic: Kernels and the kernel perceptron
---

## Card 1

**Q:** Derive the update rule of the kernel perceptron from the ordinary perceptron's \( \theta \leftarrow \theta + y_i x_i \). What replaces \(\theta\), and what is the new prediction rule?

**A:** Unroll \( \theta = \sum_j \alpha_j y_j x_j \) where \( \alpha_j \) counts mistakes on point \(j\). Substituting into \( \text{sign}(\theta\cdot x) \) gives \( \text{sign}\left(\sum_j \alpha_j y_j (x_j\cdot x)\right) \). Replacing the dot product with a kernel \(K\) gives \( \hat y_i = \text{sign}\left(\sum_j \alpha_j y_j K(x_j,x_i)\right) \). Update on a mistake: \( \alpha_i \mathrel{+}=1 \). \(\theta\) is never computed explicitly.

---

## Card 2

**Q:** Why does the kernel perceptron with the RBF kernel always halt in finite time on any finite set of distinct training points, while the ordinary perceptron on the same raw data might not?

**A:** The RBF kernel corresponds to an infinite-dimensional feature map. With enough dimensions relative to the number of points, any finite set of distinct points is linearly separable for any labeling. So the kernel perceptron is guaranteed to find a separating hyperplane in that implicit space and halt. The ordinary perceptron only has the original (low) dimensional space to work with, where the data may not be linearly separable, so it can loop forever.

---

## Card 3

**Q:** Does the polynomial kernel \(K(x,x')=(xx')^2\) (1D) give the same "always separable" guarantee as RBF? Justify with a concrete counterexample.

**A:** No. Its feature map is \(\phi(x) = x^2\) — a single, finite coordinate. A finite feature space cannot shatter an arbitrary labeling: e.g. 5 points on the real line labeled \(+,-,+,-,+\) in order cannot be separated by any single threshold in that 1D feature space. RBF avoids this ceiling because its feature space has no fixed finite dimension.

---
