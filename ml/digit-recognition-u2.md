

## Card 1

**Q:** Two ways to get a "digit mod 3" classifier: (A) train on the original 10 digit labels, then reduce the prediction mod 3; (B) relabel the data mod 3 first and retrain from scratch. Which one gave a lower test error in the project, and why?

**A:** (A) was much better (0.077 vs 0.188 error). Softmax draws linear boundaries; the mod-3 groups (e.g. {0,3,6,9}) are visually dissimilar digits forced into one linear region, which a linear model handles badly. Keeping the original 10 (visually coherent) classes and merging predictions afterward avoids that problem.

---

## Card 2

**Q:** Write the NumPy implementation of `update_y(train_y, test_y)`, which converts digit labels (0-9) to mod-3 labels (0-2).

**A:** def update_y(train_y, test_y):
    train_y_mod3 = train_y % 3
    test_y_mod3 = test_y % 3
    return train_y_mod3, test_y_mod3
No model is involved — it purely relabels the ground-truth arrays.

---

## Card 3

**Q:** Why must you center the data (subtract the feature means) before running PCA?

**A:** PCA finds directions of maximal variance via the eigenvectors of \( \widetilde X^T \widetilde X \). Without centering, that matrix is dominated by the mean/centroid location rather than the spread of the data around it, so the "top principal component" would just point toward the centroid instead of the true direction of maximal variation.

---

## Card 4

**Q:** Given the centered data \( \widetilde X \) and its top-\(k\) principal component vectors as columns of matrix \(V\) (a \(d \times k\) matrix), how do you project a (centered) point onto the first \(k\) principal components? Do you need to normalize by eigenvector length?

**A:** Projection = \( \widetilde X V \) (matrix multiplication). No normalization needed — `principal_components` returns eigenvectors of the (symmetric) scatter matrix, which `np.linalg.eig` already returns as unit-norm vectors.

---

## Card 5

**Q:** In the project, 18-dim PCA features gave a *worse* softmax test error (0.147) than the raw 784-dim pixels (0.100). Doesn't PCA "clean up" the data — why would it hurt?

**A:** PCA is lossy compression: keeping only 18 of 784 dimensions throws away information a linear model could still exploit. PCA's real payoff shows up only once you add nonlinearity (cubic features / kernels) on top of the compressed representation — then 10 PCA dims can beat 784 raw pixels, because the nonlinearity recovers more separating power than the compression lost.

**E:** ### PLAIN ENGLISH

Imagine you have a high-resolution photo of a handwritten digit made of **784 individual pixels**. 

If we want to build a computer program to guess which digit is in the photo using a simple rule—a **linear model** (which is like drawing a straight line to separate one digit from another)—it is best to let the program see **all 784 pixels**. Even a faint pixel at the very edge of the image might hold a tiny clue that helps the program draw that straight dividing line.

When we run **PCA (Principal Component Analysis)** to compress those 784 pixels down to just **18 numbers**, we are performing **lossy compression**. It is like saving a high-resolution photo as a tiny, blurry thumbnail. We keep the "big picture" (the overall shape of the digit), but we completely throw away the fine details. 

Because our straight-line program is so simple, it cannot afford to lose *any* clues. By throwing away those fine details, we make its job harder, which is why the test error gets **worse** (jumping from 0.100 to 0.147).

The real magic of PCA happens only when we upgrade our program to use a **curved rule (a non-linear model)**. 

Trying to use a curved rule on all 784 raw pixels is a computational nightmare—there are millions of curved combinations to calculate, which overwhelms the computer and leads to terrible guessing (overfitting). But if we run that curved rule on just **18 compressed numbers**, the math becomes incredibly easy. The curved rule easily finds complex, winding boundaries in this small 18-dimensional space. This curved decision power **recovers far more classification accuracy** than we lost during the initial compression step!

---

### STEP-BY-STEP

Here is the mathematical explanation of why this happens, broken down step-by-step.

**Step 1: Write down the linear model on raw pixels.**
We represent a raw image as a high-dimensional vector \(x\) of dimension \(D = 784\). A linear model (like softmax regression) makes a prediction by calculating a weighted sum of the inputs plus a constant offset:
\[f(x) = w^T x + b\]
where \(w\) is a weight vector of dimension 784, and \(b\) is a scalar bias. Because every single pixel \(x_i\) has its own dedicated weight \(w_i\), the model can exploit tiny, subtle correlations across any of the 784 pixels to find a dividing boundary.

**Step 2: Define the PCA compression step.**
PCA projects the raw \(D\)-dimensional data down to a lower-dimensional space \(M = 18\) by multiplying the centered data by a projection matrix \(U^T\) containing the top 18 eigenvectors of the covariance matrix:
\[z = U^T (x - \mu)\]
where \(z\) is our compressed 18-dimensional vector, \(\mu\) is the average pixel vector, and \(U\) is a \(784 \times 18\) matrix.

**Step 3: Analyze the information loss mathematically.**
Because we compressed the data, we cannot perfectly reconstruct the original pixels. The reconstruction \(\hat{x}\) is:
\[\hat{x} = U z + \mu\]
The information we threw away is the residual vector \(e\):
\[e = x - \hat{x}\]
A linear model trained on the compressed features \(z\) can only represent functions of the form:
\[g(z) = v^T z + c\]
If we substitute the definition of \(z\) into this equation, we get:
\[g(z) = v^T U^T (x - \mu) + c\]
If we define a new weight vector \(\tilde{w} = U v\), we can rewrite this as:
\[g(z) = \tilde{w}^T (x - \mu) + c\]
Because \(\tilde{w}\) is mathematically restricted to lie only within the 18-dimensional subspace spanned by the columns of \(U\), the model is completely blind to any information contained in the residual vector \(e\). Since some of that lost information was useful for drawing a straight line, the test error increases.

**Step 4: Examine the complexity of adding non-linearity to raw pixels.**
If we want to use a non-linear model—like a **cubic feature expansion**—on the raw pixels to find curved boundaries, we have to look at combinations of three pixels at a time (e.g., \(x_i x_j x_k\)). The number of features scales cubically:
\[\text{Cubic Features} \approx \frac{D^3}{6}\]
For \(D = 784\) raw pixels, this requires:
\[\frac{784^3}{6} \approx 80,300,000 \text{ features}\]
Training a model with **80 million features** requires massive amounts of memory, runs incredibly slowly, and causes the model to overfit by memorizing noise in the training set.

**Step 5: Apply non-linearity to the compressed PCA space.**
If we instead compress the data down to \(M = 10\) dimensions using PCA first, and then apply a cubic expansion, the number of features is:
\[\frac{10^3}{6} \approx 166 \text{ features}\]
This is an incredibly small number of features. The model can easily run in a fraction of a second, avoid overfitting, and find highly accurate, curved decision boundaries in that 10-dimensional space. The immense power gained from using curved boundaries far exceeds the small amount of detail lost during the PCA compression.

---

### THE TAKEAWAY

**PCA is a lossy compression tool that degrades simple linear models by stripping away subtle clues, but it is a vital prerequisite for non-linear models because it reduces the dimensionality enough to make highly accurate, curved decision boundaries computationally practical.**

---

### CONCRETE EXAMPLE

Let's look at the actual numbers of this trade-off:

*   **Raw Pixels (784 dims) with a Linear Model:** The model uses a simple straight line but has access to all pixels. It achieves a **test error of 0.100**.
*   **PCA Features (18 dims) with a Linear Model:** The model still uses a straight line, but PCA threw away the fine details. Because it lost these clues, the **test error degrades to 0.147**.
*   **Raw Pixels (784 dims) with a Cubic Non-linear Model:** We attempt to run a curved boundary on all pixels. The computer tries to calculate **80,300,000 features**, runs out of memory, or overfits so severely that the **test error balloons to 0.350**.
*   **PCA Features (10 dims) with a Cubic Non-linear Model:** We compress the image first, then run a curved boundary. The computer easily calculates just **166 features**, avoids overfitting, and achieves a superior **test error of 0.080**, easily beating the raw pixel linear model.

---

### WATCH OUT

A very common mistake is assuming that PCA is a "smart cleaner" that automatically filters out noise to help every model [1, 2]. 

In reality, **PCA is entirely unsupervised**—it only looks at where the data varies the most, and has absolutely no knowledge of your class labels [3]. It cannot tell the difference between "useless noise" and a "subtle but crucial signal" needed for classification. If a vital clue for separating your digits happens to lie along a direction of low variance, PCA will throw it away without hesitation, hurting your linear model's performance.

🔍 Would you like to walk through a concrete visualization of how a 2D dataset is projected down to 1D via PCA, and see exactly where the information loss occurs?

---

## Card 6

**Q:** The cubic feature mapping \(\phi(x)\) satisfies \(\phi(x)^T\phi(x') = (x^Tx' + 1)^3\). For \(x=[x_1,x_2]\) (d=2), what is \(\phi(x)\) explicitly, and how many output dimensions does it have?

**A:** \( \phi(x) = [x_1^3,\ \sqrt3 x_1^2x_2,\ \sqrt3 x_1x_2^2,\ \sqrt6 x_1x_2,\ \sqrt3 x_1^2,\ \sqrt3 x_1,\ x_2^3,\ \sqrt3 x_2^2,\ \sqrt3 x_2,\ 1] \) — 10 dimensions, matching \(\frac{(d+1)(d+2)(d+3)}{6}\) for d=2. The \(\sqrt{}\) factors come from splitting multinomial cross-coefficients evenly between \(\phi(x)\) and \(\phi(x')\).

---

## Card 7

**Q:** Why does the project apply the cubic feature map to the 10-dim PCA representation instead of the raw 784-dim pixels?

**A:** The cubic map's output dimension is \(\frac{(d+1)(d+2)(d+3)}{6}\). For d=784 that's ~81 million features per image — infeasible. For d=10 (after PCA) it's only 286 features — cheap. PCA makes the explicit nonlinear expansion computationally tractable.

---

## Card 8

**Q:** State the kernel trick in one sentence: what do you compute, and what do you avoid computing?

**A:** You compute the kernel \(K(x,y) = \phi(x)\cdot\phi(y)\) directly as a scalar (e.g. via a closed-form formula), and you avoid ever explicitly forming the (possibly huge or infinite-dimensional) feature vector \(\phi(x)\) itself.

---

## Card 9

**Q:** Write the polynomial kernel formula (with parameters c, p) and its one-line NumPy implementation for matrices X (n,d) and Y (m,d).

**A:** \( K(x,y) = (x^Ty + c)^p \)
def polynomial_kernel(X, Y, c, p):
    return (X @ Y.T + c) ** p

---

## Card 10

**Q:** Write the Gaussian RBF kernel formula (parameter gamma) and explain why it corresponds to an infinite-dimensional feature space (unlike the polynomial kernel).

**A:** \( K(x,y) = \exp(-\gamma\lVert x-y\rVert^2) \). Its Taylor/Maclaurin expansion in \(x^Ty\) has infinitely many nonzero polynomial terms of all degrees, so no finite-dimensional \(\phi(x)\) can reproduce it exactly — the implicit feature map lives in an infinite-dimensional space.

---

## Card 11

**Q:** When implementing the RBF kernel via \( \lVert x-y\rVert^2 = \lVert x\rVert^2+\lVert y\rVert^2-2x^Ty \) (to avoid an explicit O(n·m·d) loop), why is `np.maximum(sq_dists, 0)` needed before the `exp(-gamma * sq_dists)` call?

**A:** Floating-point rounding can make `sq_dists` slightly negative when \(x\approx y\), even though a true squared distance can never be negative. Clamping to 0 prevents that numerical artifact from corrupting the kernel value.

---

## Card 12

**Q:** On the same 10-dim PCA features, SVM with an RBF kernel (error 0.064) beat SVM with a degree-3 polynomial kernel (error 0.073). What's the underlying reason RBF tends to do at least as well as a fixed-degree polynomial kernel?

**A:** RBF's implicit feature space is infinite-dimensional and is a strict superset of what any fixed-degree polynomial kernel can represent, so its hypothesis space is strictly larger — it can express any polynomial-shaped boundary plus much smoother/more local ones. More expressive power (with enough data to avoid overfitting) tends to lower test error.

---
