# MITx 6.86x — Project 2: Digit Recognition (Softmax, PCA, Cubic Features, Kernels)

Everything below is built around one running example: classifying MNIST digit images (784 raw pixel features) with softmax regression, then progressively changing (a) the labels, (b) the feature representation, and (c) the model, to see what actually moves the needle on test error.

For the matching flashcard drills, see **kernel-perceptron** and **digit-recognition-u2** in this notebook.

## 1. Changing the labels: predicting digit mod 3

### The idea
Instead of predicting the digit 0–9, predict `digit mod 3`, i.e. 3 classes: `{0,3,6,9} → 0`, `{1,4,7} → 1`, `{2,5,8} → 2`.

There are **two completely different ways** to get a "mod 3" classifier, and the whole point of this exercise is that they behave very differently:

**Approach A — reuse the existing model.** Train softmax once on the original 10 digit labels (as always). At prediction time, take the model's predicted digit and reduce it mod 3. You never retrain anything.

\[ \hat y^{(i)}_{\bmod 3} = \big(\arg\max_j\, h_j(x^{(i)})\big) \bmod 3 \]

This is what `compute_test_error_mod3` does: it calls `get_classification` (the *existing* 10-class model) and takes `% 3` of the output before comparing to the true mod-3 label.

**Approach B — retrain from scratch.** Relabel the training set itself with `update_y` (`train_y % 3`, `test_y % 3`), and run `softmax_regression` again with `k=3` instead of `k=10`. Now the model's parameters `theta` are learned specifically to separate the three mod-3 groups.

### Why B is worse than A here
Intuition says "fewer classes = easier problem," so B should win. It doesn't, empirically:

| Method | Test error |
|---|---|
| A: mod-3 of original 10-class model's predictions | **0.0768** |
| B: retrained directly on mod-3 labels | **0.1881** |

Why? Softmax regression is a *linear* classifier — each class gets one hyperplane (per class, in the augmented feature space). The digits `{0,3,6,9}` don't look alike as images; grouping them into a single label forces one linear decision region to contain four visually unrelated pixel patterns. That region is not convex/linearly-separable-friendly, so the linear model does a much worse job than it did on the original 10 classes (where each digit's images *do* cluster reasonably well in pixel space). Approach A sidesteps this: the original 10-class model still draws 10 "good" linear boundaries, and only lumps the outputs together after the fact.

**Takeaway:** merging classes doesn't always make a linear problem easier — it depends on whether the merged classes are close together in *feature space*, not whether there are numerically fewer of them.

## 2. Manually crafted features: PCA

### Motivation
Raw pixels are a poor representation: 784 dimensions, most of them redundant (neighboring pixels are highly correlated, background pixels carry ~no information). **Principal Components Analysis (PCA)** finds a small number of new axes that capture most of the variation in the data, so a simple linear model has less noise to fight through.

### The math
1. **Center** the data: \( \widetilde X = X - \bar x \) (subtract the feature-wise mean so the cloud of points is centered at the origin). This matters because PCA is about *directions of variation*, not raw magnitude.
2. Form the scatter/covariance matrix \( \widetilde X^T \widetilde X \) (a \(d \times d\) matrix).
3. Its eigenvectors are the **principal component directions**; sorted by eigenvalue (largest first), the top \(k\) eigenvectors are the \(k\) directions that capture the most variance.
4. **Project**: a centered point \(x\) becomes \( V^T (x - \bar x) \) where \(V\) is the \(d \times k\) matrix of top-\(k\) eigenvectors (equivalently \( (x-\bar x)\, V\) in row-vector/matrix form, which is what `project_onto_PC` computes: `(X - feature_means) @ pcs[:, :n_components]`).
5. **Reconstruct** (approximately) by going back: \( x \approx V\, z + \bar x \), where \(z\) is the low-dimensional PCA representation. This is lossy — you threw away the low-variance directions — but for MNIST the top ~18 components already capture most of the digit "shape" information.

### What you should notice in the scatter plot
Projecting onto just the first 2 principal components already separates digits that look very different (e.g. `0` and `1` end up far apart) but leaves visually-similar digits mixed together (`3`/`5`/`8`, `4`/`9`). That's expected: PCA only knows about variance, not about class labels — it's an unsupervised method. Two dimensions are nowhere near enough to fully separate 10 digit classes; that's why the project uses **18** components for the actual classifier, not 2 (2 is only used for visualization).

### Empirical results
| Representation | Softmax test error |
|---|---|
| Raw 784-dim pixels | 0.1005 |
| 18-dim PCA | 0.1474 |
| 10-dim PCA | 0.2059 |

Note PCA-18 is *worse* than raw pixels here! PCA is a *lossy compression* — with only 18 (or 10) numbers you've thrown away information a linear softmax model could otherwise have used. PCA's real value shows up once you combine it with a nonlinear feature map (next section): it makes the *subsequent* explicit feature expansion computationally feasible, because expanding 784 raw pixels through a cubic map would be enormous, while expanding 10 PCA numbers is cheap.

## 3. Cubic feature mapping

### Motivation
Softmax/SVM decision boundaries are linear in whatever feature vector you hand them. If the true boundary between classes is curved in the original space, you need to either (a) explicitly map the input into a higher-dimensional space where a straight line *can* separate the classes, or (b) use the kernel trick (Section 4) to get the same effect without ever forming that high-dimensional vector.

The **cubic feature mapping** \(\phi(x)\) is defined so that
\[ \phi(x)^T \phi(x') = (x^T x' + 1)^3 \]
i.e. it contains every monomial of `x`'s coordinates up to degree 3 (with specific scaling constants so the dot product identity holds).

### Explicit derivation for \(d=2\)
Let \(x = [x_1, x_2]\). Expand \((x_1 x_1' + x_2 x_2' + 1)^3\) with the multinomial theorem and split each cross term \(c \cdot A(x)A(x')\) into \((\sqrt{c}A(x))\cdot(\sqrt{c}A(x'))\):
\[ \phi(x) = \big[x_1^3,\ \sqrt3\,x_1^2 x_2,\ \sqrt3\,x_1 x_2^2,\ \sqrt6\,x_1 x_2,\ \sqrt3\,x_1^2,\ \sqrt3\,x_1,\ x_2^3,\ \sqrt3\,x_2^2,\ \sqrt3\,x_2,\ 1\big] \]
10 output coordinates for 2 input coordinates. In general, mapping a \(d\)-dimensional input through this cubic map produces \(\frac{(d+1)(d+2)(d+3)}{6}\) coordinates — for the 784 raw pixel dimensions that would be **~80 million** features per image, which is why the project has you apply the cubic map only *after* PCA has cut the input down to 10 dimensions (giving a manageable 286-dimensional cubic feature vector).

### Empirical result
| Representation | Softmax test error |
|---|---|
| 10-dim PCA (no cubic map) | 0.2059 |
| 10-dim PCA → cubic features | **0.0735** |

Big improvement — going from linear to cubic boundaries in the same 10 "useful" PCA dimensions lets the model separate classes that PCA alone (linear boundaries only) couldn't.

## 4. Kernel methods

### The trick
Explicitly forming \(\phi(x)\) is expensive (or, for RBF, impossible — its implicit feature space is infinite-dimensional). The **kernel trick** notices that both the perceptron and softmax updates only ever need *dot products* \(\phi(x_i)\cdot\phi(x_j)\), never \(\phi(x)\) itself. Define a **kernel function** \(K(x,y) = \phi(x)\cdot\phi(y)\) and compute `K` directly, skipping `phi` entirely.

Dual/kernelized form of the weights: \( \theta_j = \sum_i \alpha_i^{(j)} \phi(x^{(i)}) \), so predictions become
\[ h(x) \propto \exp\Big(\tfrac{1}{\tau}\sum_i \alpha_i^{(j)} K(x^{(i)}, x)\Big) \]
— everything is expressed through `K`, never `phi`.

### The two kernels you implemented
**Polynomial kernel** (generalizes the cubic map above to any degree \(p\) and trade-off constant \(c\)):
\[ K(x,y) = (x^T y + c)^p \]
```python
def polynomial_kernel(X, Y, c, p):
    return (X @ Y.T + c) ** p
```

**Gaussian RBF kernel** (implicit feature space is infinite-dimensional — no finite \(\phi\) exists):
\[ K(x,y) = \exp(-\gamma \lVert x-y\rVert^2) \]
```python
def rbf_kernel(X, Y, gamma):
    X_sq = (X**2).sum(1)[:, None]
    Y_sq = (Y**2).sum(1)[None, :]
    sq_dists = np.maximum(X_sq + Y_sq - 2 * X @ Y.T, 0)
    return np.exp(-gamma * sq_dists)
```
(`sq_dists` uses \(\lVert x-y\rVert^2 = \lVert x\rVert^2 + \lVert y\rVert^2 - 2x^Ty\) — the `maximum(...,0)` guards against tiny negative values from floating-point rounding.)

RBF measures *similarity by distance*: points close together get \(K \approx 1\), far-apart points get \(K \approx 0\). This is why it tends to draw smooth, local decision boundaries that hug the actual data clusters rather than being constrained to any fixed polynomial shape.

### Empirical results (SVM on the 10-dim PCA features, via scikit-learn)
| Kernel | Test error |
|---|---|
| Polynomial (degree 3) | 0.0734 |
| RBF | **0.0636** |

RBF wins slightly here — no surprise, since it's strictly more flexible (infinite-dimensional implicit feature space vs. a fixed-degree polynomial), and MNIST digit clusters are curved/blob-shaped rather than polynomial-shaped.

## 5. Full comparison table (10-dim / 18-dim PCA features, MNIST test set)

| Representation + Model | Test error |
|---|---|
| Raw pixels, closed-form linear regression | 0.7697 (essentially useless — regression loss is the wrong tool for classification) |
| Raw pixels, linear SVM (multiclass, one-vs-rest) | 0.0820 |
| Raw pixels, softmax regression | 0.1005 |
| 18-dim PCA, softmax | 0.1474 |
| 10-dim PCA, softmax | 0.2059 |
| 10-dim PCA + cubic features, softmax | 0.0735 |
| 10-dim PCA, SVM (polynomial kernel) | 0.0734 |
| 10-dim PCA, SVM (RBF kernel) | 0.0636 |

**Big-picture lesson:** the model class matters more than you'd think. Once you allow nonlinear decision boundaries (cubic features or kernels), 10 PCA dimensions beat 784 raw pixels *and* beat 18 PCA dimensions used linearly — nonlinearity recovers more than what was "lost" by compressing to 10 numbers.

---

## Check your understanding (self-test — try before reading the answer)

**Q1.** Why does training directly on mod-3 labels give a *higher* error than taking mod-3 of a model trained on the original 10 digit labels, even though the mod-3 task has fewer classes?
> *Because softmax draws linear boundaries. `{0,3,6,9}` are visually dissimilar, so forcing them into one linear decision region is harder than keeping 10 separate (visually coherent) linear regions and merging predictions afterward.*

**Q2.** If you skip centering (`center_data`) before computing PCA, what breaks?
> *PCA's covariance/scatter matrix \(\widetilde X^T \widetilde X\) is only meaningful for variance around the mean. Without centering, the "first principal component" would just point toward the overall data centroid (the dominant direction becomes "distance from the origin," not "direction of spread"), corrupting every downstream component.*

**Q3.** Why is 18-dim PCA *worse* than raw 784-dim pixels for plain (linear) softmax, but 10-dim PCA + cubic features *beats* raw pixels?
> *PCA alone is a lossy linear compression — with linear softmax on top, you've simply thrown away information the raw-pixel linear model could use. The cubic map adds nonlinearity, which recovers separating power that no amount of *linear* processing (raw pixels or PCA) can provide.*

**Q4.** What is `new_d`, the output dimension of the cubic feature map, for \(d=784\) raw pixels? Why does the project apply it to PCA-10 instead?
> *\(\frac{(784+1)(784+2)(784+3)}{6} \approx 8.1\times10^7\) — computationally infeasible to store or train on directly. PCA-10 keeps `new_d = (10+1)(10+2)(10+3)/6 = 286`, which is cheap.*

**Q5.** Write the polynomial kernel and RBF kernel formulas from memory, and state one qualitative difference between the shapes of decision boundary each tends to produce.
> *Polynomial: \(K(x,y)=(x^Ty+c)^p\) — boundaries limited to degree-\(p\) polynomial shapes. RBF: \(K(x,y)=\exp(-\gamma\lVert x-y\rVert^2)\) — boundaries can be arbitrarily smooth/local "blobs" around clusters, since the implicit feature space is infinite-dimensional.*

**Q6.** In the kernel trick, what mathematical object do we avoid ever computing, and what do we compute instead?
> *We avoid computing \(\phi(x)\) (the explicit, possibly huge or infinite-dimensional feature vector). Instead we compute \(K(x,y)=\phi(x)\cdot\phi(y)\) directly as a scalar, and express \(\theta\) implicitly as \(\theta=\sum_i \alpha_i \phi(x^{(i)})\).*

**Q7.** Why does the `maximum(sq_dists, 0)` clamp exist in the RBF kernel implementation?
> *\(\lVert x-y\rVert^2 = \lVert x\rVert^2+\lVert y\rVert^2-2x^Ty\) can come out very slightly negative due to floating-point rounding when \(x\approx y\). A negative value inside `exp(-gamma * sq_dists)` would be mathematically wrong (squared distances can't be negative) and could blow up the exponential.*

**Q8.** Between the SVM-polynomial (0.0734) and SVM-RBF (0.0636) results on the same 10-dim PCA features, which model has the larger *hypothesis space* (can represent more possible decision boundaries), and does the empirical result agree with what that implies?
> *RBF — its implicit feature space is infinite-dimensional, a strict superset of what any fixed-degree polynomial kernel can represent. Yes, RBF's lower error is consistent with it being the more expressive model class here.*
