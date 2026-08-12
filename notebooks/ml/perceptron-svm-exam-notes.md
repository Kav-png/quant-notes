# Perceptron, SVM & Linear Classifiers — Complete Exam Notes

---

## 1. LINEAR CLASSIFIERS

A **linear classifier** separates data using a hyperplane (a line in 2D, a plane in 3D).

### Without offset (through origin)
Decision rule: classify as +1 if \(\theta \cdot x > 0\), else −1.
The boundary is \(\theta \cdot x = 0\) — always passes through the origin.

### With offset
Decision rule: classify as +1 if \(\theta \cdot x + \theta_0 > 0\), else −1.
The boundary is \(\theta \cdot x + \theta_0 = 0\) — can be anywhere.

> **Convention:** Points ON the boundary (\(= 0\)) are considered **misclassified**.

### Which classifier families are LINEAR?
- ✅ Line through origin with normal \(\theta\): \(\theta \cdot x > 0\)
- ✅ Line with offset: \(\theta \cdot x + \theta_0 > 0\)
- ❌ Origin-centered circle (radius \(r\)): \(\|x\|^2 < r^2\) — quadratic
- ❌ General circle centered at \([a,b]\): \((x_1-a)^2 + (x_2-b)^2 < r^2\) — quadratic

---

## 2. DISTANCE FROM A POINT TO A LINE

Line: \(ax + by + c = 0\). Point: \(P = (x_0, y_0)\).

\[
d = \frac{|ax_0 + by_0 + c|}{\sqrt{a^2 + b^2}}
\]

**Derivation idea:** Project the vector from any point on the line to \(P\) onto the unit normal \(\hat{n} = (a,b)/\sqrt{a^2+b^2}\).

In the SVM context, the decision boundary is \(\theta \cdot x = 0\) and the margin boundaries are \(\theta \cdot x = \pm 1\). The distance from the boundary to each margin line is:

\[
d = \frac{1}{\|\theta\|}
\]

---

## 3. PERCEPTRON ALGORITHM

### Setup
- Binary labels: \(y \in \{+1, -1\}\)
- Start: \(\theta^{(0)} = 0\) (and \(\theta_0 = 0\) if no offset)
- A point is a **mistake** if \(y^{(i)}(\theta \cdot x^{(i)}) \leq 0\)

### Update rule (no offset)
On a mistake on point \((x^{(i)}, y^{(i)})\):
\[
\theta \leftarrow \theta + y^{(i)} x^{(i)}
\]

### Update rule (with offset)
\[
\theta \leftarrow \theta + y^{(i)} x^{(i)}, \qquad \theta_0 \leftarrow \theta_0 + y^{(i)}
\]

### Key property
After \(k\) mistakes, the final \(\theta\) is just the **sum of all \(y^{(i)} x^{(i)}\)** for each mistake:
\[
\theta = \sum_{\text{mistakes}} y^{(i)} x^{(i)}, \qquad \theta_0 = \sum_{\text{mistakes}} y^{(i)}
\]

### Algorithm flow
1. Start with the chosen first point (always a mistake since \(\theta = 0\))
2. Cycle through points in order
3. On each point: check if \(y(\theta \cdot x) \leq 0\); if yes, update
4. Stop when a full cycle produces zero mistakes

### Important observations
- **Iteration order matters** — different starting points → different number of mistakes
- The algorithm always converges if data is linearly separable (Perceptron Convergence Theorem)

---

## 4. PERCEPTRON CONVERGENCE THEOREM

Assumes data is **linearly separable through the origin** with:
- \(\gamma > 0\): the margin (how easily separable the data is)
- \(R\): max norm of data points, \(R = \max_i \|x^{(i)}\|\)

There exists \(\theta^*\) such that \(\frac{y^{(i)}(\theta^* \cdot x^{(i)})}{\|\theta^*\|} \geq \gamma\) for all \(i\).

### Upper bound on mistakes (initialized at 0)
\[
k \leq \frac{R^2}{\gamma^2}
\]

### Two key inductive lemmas (initialized at 0)
1. **Dot product grows:** \(\theta^{(k)} \cdot \frac{\theta^*}{\|\theta^*\|} \geq k\gamma\)
2. **Norm bounded:** \(\|\theta^{(k)}\|^2 \leq kR^2\)

Since \(\cos(\alpha) \leq 1\): dot product \(\leq\) norm, so \(k\gamma \leq \sqrt{k}R\), giving \(k \leq R^2/\gamma^2\).

---

## 5. PERCEPTRON WITH GENERAL INITIALIZATION

If \(\theta\) is initialized to \(\theta^{(0)} \neq 0\) (not necessarily zero):

### Modified lemma 1 — dot product
\[
\theta^{(k)} \cdot \frac{\theta^*}{\|\theta^*\|} \geq a + k\gamma, \qquad \text{where } a = \theta^{(0)} \cdot \frac{\theta^*}{\|\theta^*\|}
\]
\(a\) is the **initial alignment** with the perfect separator — how much "head start" (or deficit) you begin with.

### Modified lemma 2 — norm
\[
\|\theta^{(k)}\|^2 \leq kR^2 + c^2, \qquad \text{where } c^2 = \|\theta^{(0)}\|^2
\]
\(c\) is the **initial size** of \(\theta\).

This implies \(\|\theta^{(k)}\| \leq c + \sqrt{k}R\) (using \(\sqrt{x+y} \leq \sqrt{x} + \sqrt{y}\)).

### General bound on mistakes
Combining \(a + k\gamma \leq \|\theta^{(k)}\| \leq c + \sqrt{k}R\):
\[
k\gamma - \sqrt{k}R - (c - a) \leq 0
\]
Let \(u = \sqrt{k}\) → quadratic in \(u\): \(\gamma u^2 - Ru - (c-a) \leq 0\). Solving:
\[
k \leq \left(\frac{R + \sqrt{R^2 + 4\gamma(c-a)}}{2\gamma}\right)^2
\]

> **Key insight:** Initialization does NOT prevent convergence — it just shifts the bound via \(a\) and \(c\).

---

## 6. FACTORS AFFECTING NUMBER OF PERCEPTRON MISTAKES

From the convergence bound \(k \leq (R/\gamma)^2\):

| Factor | Effect |
|---|---|
| **Iteration order** | Changes which mistakes are made and when (not in the bound, but practically important) |
| **Maximum norm \(R = \max \|x^{(i)}\|\)** | Larger \(R\) → more mistakes allowed |
| **Margin \(\gamma\)** | Smaller \(\gamma\) → harder to separate → more mistakes |
| **Initialization \(\theta^{(0)}\)** | Shifts bound via \(a\) and \(c\) |

> **Exam trap:** Only choose factors that *actually changed* between runs, not all factors that *could* affect mistakes.

---

## 7. BOOLEAN FUNCTIONS AND LINEAR SEPARABILITY

### Function: \(f(x_1, x_2, x_3) = \neg x_1 \wedge \neg x_2 \wedge \neg x_3\)
- Output is 1 **only** when all inputs are 0: \(x = [0,0,0]\)
- All other inputs give 0

**Without offset (\(\theta_0 = 0\)):** Need \(\theta \cdot [0,0,0] > 0\), but this equals 0. **Impossible → No**

**With offset:** Use \(\theta = [-1,-1,-1], \theta_0 = 0.5\):
- \([0,0,0]\): \(0 + 0.5 = 0.5 > 0\) ✓
- \([1,0,0]\): \(-1 + 0.5 = -0.5 < 0\) ✓ (and similarly for all other inputs)

**→ Yes, learnable with offset**

### General rule
If the positive class includes the **origin** \([0,0,\ldots,0]\), you **cannot** learn it without an offset because \(\theta \cdot 0 = 0\) always.

---

## 8. CIRCLE CLASSIFIERS (Feature Transformation)

### Origin-centered circle
Classify as +1 if inside: \(\|x\|^2 < r^2\), i.e. \(x_1^2 + x_2^2 < r^2\).
- Decision depends only on **distance from origin**
- If two points of different labels have the same \(\|x\|\), no \(r\) works

### General circle centered at \([a,b]\)
Classify as +1 if inside: \((x_1-a)^2 + (x_2-b)^2 < r^2\)
- Much more flexible — center can be anywhere
- **Strategy:** Find a center equidistant from all positives but farther from all negatives

**Example:** Positives \([-1,1], [1,-1]\); Negatives \([1,1], [2,2]\)
- Center \([-1,-1]\): distances² are 4, 4 (pos) and 8, 18 (neg)
- Use \(r = 2.5\): all positives inside, all negatives outside ✓

---

## 9. SVM — SUPPORT VECTOR MACHINE

### Objective (hinge loss + regularization)
\[
J(\theta) = \frac{1}{n}\sum_{i=1}^n \text{Loss}_h(y^{(i)}\theta \cdot x^{(i)}) + \frac{\lambda}{2}\|\theta\|^2
\]

### Hinge loss
\[
\text{Loss}_h(y(\theta \cdot x)) = \max\{0,\ 1 - y(\theta \cdot x)\}
\]
- Zero when \(y(\theta \cdot x) \geq 1\) (correctly classified AND outside margin)
- Positive when \(y(\theta \cdot x) < 1\) (inside margin or misclassified)

### Geometric interpretation
- Decision boundary: \(\theta \cdot x = 0\)
- Margin boundaries: \(\theta \cdot x = \pm 1\)
- Distance from boundary to margin: \(d = \frac{1}{\|\theta\|}\)
- **Larger \(\lambda\)** → smaller \(\|\theta\|\) → larger margin \(d\)

### Regularization parameter \(\lambda\)
- \(\lambda\) controls the trade-off between fitting data and keeping \(\theta\) small
- **Increasing \(\lambda\)** → penalises large \(\theta\) more → \(\|\theta\|\) decreases → margin \(d = 1/\|\theta\|\) **increases**

---

## 10. SVM OPTIMISATION — SOLVING FOR \(\hat{\theta}\)

For \(n=1\) (single training example), the objective is:
\[
J(\theta) = \text{Loss}_h(y\theta \cdot x) + \frac{\lambda}{2}\|\theta\|^2
\]

### Case 1: Hinge loss is active (\(y(\hat\theta \cdot x) < 1\))
Loss = \(1 - y(\theta \cdot x)\), so:
\[
J(\theta) = 1 - y(\theta \cdot x) + \frac{\lambda}{2}\|\theta\|^2
\]
Take gradient, set to zero:
\[
\nabla_\theta J = -yx + \lambda\theta = 0 \implies \hat\theta = \frac{y}{\lambda}x
\]

### Case 2: Hinge loss is zero (\(y(\hat\theta \cdot x) \geq 1\))
Loss = 0, so minimise just \(\frac{\lambda}{2}\|\theta\|^2\):
\[
\hat\theta = 0
\]

### How to determine which case applies
1. Assume Case 1: compute \(\hat\theta = \frac{y}{\lambda}x\)
2. Check: is \(y(\hat\theta \cdot x) < 1\)?
   - \(y \cdot \frac{y}{\lambda}(x \cdot x) = \frac{\|x\|^2}{\lambda}\)
   - If \(\frac{\|x\|^2}{\lambda} < 1\) → Case 1 is self-consistent ✓
   - If \(\frac{\|x\|^2}{\lambda} \geq 1\) → Case 2 applies, \(\hat\theta = 0\)... but check again

> **General rule:** \(\hat\theta = \frac{yx}{\lambda}\) when \(\|x\|^2 < \lambda\); otherwise the hinge loss is zero and the optimal \(\theta\) lies at the boundary where \(y(\theta \cdot x) = 1\).

### Special value: always misclassified
The point \(\hat\theta(\lambda)\) **always** misclassifies when \(\|x\|^2 = 0\) (i.e. \(x = \mathbf{0}\)), because \(y(\hat\theta \cdot 0) = 0 \leq 0\) for any \(\hat\theta\) and any \(\lambda\). So \(c = 0\).

---

## 11. QUICK REFERENCE — KEY FORMULAS

| Concept | Formula |
|---|---|
| Distance: point to line | \(d = \frac{\|ax_0 + by_0 + c\|}{\sqrt{a^2+b^2}}\) |
| SVM margin width | \(d = \frac{1}{\|\theta\|}\) |
| Hinge loss | \(\max\{0, 1 - y(\theta \cdot x)\}\) |
| Perceptron update | \(\theta \leftarrow \theta + y^{(i)}x^{(i)}\) |
| Perceptron mistake bound | \(k \leq \frac{R^2}{\gamma^2}\) |
| SVM optimal \(\hat\theta\) (loss active) | \(\hat\theta = \frac{y}{\lambda}x\) |
| General init: \(a\) | \(a = \theta^{(0)} \cdot \frac{\theta^*}{\|\theta^*\|}\) |
| General init: \(c^2\) | \(c^2 = \|\theta^{(0)}\|^2\) |
| General init: mistake bound | \(k \leq \left(\frac{R + \sqrt{R^2 + 4\gamma(c-a)}}{2\gamma}\right)^2\) |

---

## 12. EXAM STRATEGY TIPS

1. **Perceptron by hand:** Always track \(\theta\) after each update. Check ALL points from the beginning after each update.

2. **SVM case check:** Always verify which case (loss active or zero) after computing \(\hat\theta\) — the assumption must be consistent with the result.

3. **Factors that change mistakes:** Read carefully — "what changed between these two runs" vs "what could in general affect mistakes" are different questions.

4. **Linear separability check:** If two points of opposite labels satisfy \(\theta \cdot x = 0\) for the same \(\theta\), they're on the boundary — not separable without offset.

5. **Circle classifiers:** Compute \(\|x - \text{centre}\|^2\) for all points. Positives need smaller distance than negatives. Pick \(r\) strictly between the two groups.

6. **Boolean functions with origin:** If the positive class contains the zero vector, you **need** an offset — \(\theta \cdot 0 = 0\) always.
