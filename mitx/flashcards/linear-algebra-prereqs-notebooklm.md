# Matrix Flashcards

## Card 1

**Q:** Term: Vector

**A:** Definition: A mathematical object represented as a column of numbers stacked together. Example: The state of a system at time \(t\) represented as \(C_t = \begin{pmatrix} x_t \\ y_t \end{pmatrix}\).

---

## Card 2

**Q:** Term: Matrix

**A:** Definition: A rectangular array of numbers that acts as a linear transformation on vectors, mapping an input vector to a new output vector. Example: A coefficient matrix \(M\) that determines how current variables depend on previous states.

---

## Card 3

**Q:** How is a coupled multivariate time series represented using matrix notation?

**A:** \[ C_t = M C_{t-1} + \sigma \eta_t \]

---

## Card 4

**Q:** In the HW2 system, what is the structure of the coefficient matrix \(M\) given \(x_t = \lambda y_{t-1}\) and \(y_t = \lambda x_{t-1}\)?

**A:** \[ M = \begin{pmatrix} 0 & \lambda \\ \lambda & 0 \end{pmatrix} \]

---

## Card 5

**Q:** What is the primary intuition for thinking of a matrix as a 'machine'?

**A:** You feed in an input vector, and the matrix transforms (stretches, rotates, or scales) it to produce a specific output vector.

---

## Card 6

**Q:** Term: Eigenvalue

**A:** Definition: A scalar \(\gamma\) that represents the stretch or flip factor for a specific direction under a linear transformation. Example: If \(Mv = 3v\), then 3 is the eigenvalue associated with vector \(v\).

---

## Card 7

**Q:** Term: Eigenvector

**A:** Definition: A non-zero vector \(v\) whose direction remains unchanged (it is only scaled) when a linear transformation \(M\) is applied. Example: A 'natural axis' of a system that evolves independently without mixing with other directions.

---

## Card 8

**Q:** What is the characteristic equation used to find the eigenvalues of a matrix \(M\)?

**A:** \[ \det(M - \gamma I) = 0 \]

---

## Card 9

**Q:** How is the eigenvalue equation \(Mv = \gamma v\) rearranged to show that \(M - \gamma I\) must be singular?

**A:** \[ (M - \gamma I)v = 0 \]

---

## Card 10

**Q:** What is the intuition behind eigenvectors in the context of a VAR model?

**A:** They represent the 'natural axes' or combinations of variables that evolve independently of one another.

---

## Card 11

**Q:** For the matrix \(M = \begin{pmatrix} 0 & \lambda \\ \lambda & 0 \end{pmatrix}\), what are the calculated eigenvalues?

**A:** \[ \gamma = +\lambda \quad \text{and} \quad \gamma = -\lambda \]

---

## Card 12

**Q:** How is an eigenvector found once an eigenvalue \(\gamma\) is known?

**A:** By substituting \(\gamma\) back into the equation \((M - \gamma I)v = 0\) and solving the resulting linear system for the components of \(v\).

---

## Card 13

**Q:** For the eigenvalue \(\gamma = +\lambda\) in the HW2 system, what is the resulting unnormalised eigenvector?

**A:** \[ v_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix} \]

---

## Card 14

**Q:** What 'natural mode' of the system is represented by the eigenvector \(v_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}\)?

**A:** The sum of the variables, \(x + y\), which evolves as a single unit.

---

## Card 15

**Q:** For the eigenvalue \(\gamma = -\lambda\) in the HW2 system, what is the resulting unnormalised eigenvector?

**A:** \[ v_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix} \]

---

## Card 16

**Q:** What 'natural mode' of the system is represented by the eigenvector \(v_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}\)?

**A:** The difference between variables, \(x - y\), which evolves as a single unit.

---

## Card 17

**Q:** What is the formula for the Euclidean norm used to normalise a vector \(v\)?

**A:** \[ |v| = \sqrt{v_1^2 + v_2^2} \]

---

## Card 18

**Q:** How is the normalised eigenvector \(\hat{v}_1\) expressed for the HW2 system?

**A:** \[ \hat{v}_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix} \]

---

## Card 19

**Q:** Term: Diagonalization

**A:** Definition: The process of decomposing a matrix \(M\) into the product of its eigenvectors and eigenvalues to simplify computations. Example: Writing \(M = V \Gamma V^{-1}\) to decouple a system of equations.

---

## Card 20

**Q:** What is the formula for the diagonalization of a matrix \(M\)?

**A:** \[ M = V \Gamma V^{-1} \]

---

## Card 21

**Q:** In the diagonalization \(M = V \Gamma V^{-1}\), what do the columns of matrix \(V\) represent?

**A:** The columns are the eigenvectors of the matrix \(M\).

---

## Card 22

**Q:** In the diagonalization \(M = V \Gamma V^{-1}\), what does the matrix \(\Gamma\) contain?

**A:** It is a diagonal matrix where the diagonal elements are the eigenvalues of \(M\).

---

## Card 23

**Q:** What is the intuition behind the matrix \(V\) in the diagonalization process?

**A:** It acts as a change-of-basis matrix that rotates original coordinates into the 'natural' coordinate system of the eigenvectors.

---

## Card 24

**Q:** What is the general formula for the inverse of a \(2 \times 2\) matrix \(A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}\)?

**A:** \[ A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix} \]

---

## Card 25

**Q:** Term: Determinant

**A:** Definition: A scalar value calculated from a square matrix that indicates if the matrix is invertible. Example: For \(A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}\), the determinant is \(ad - bc\).

---

## Card 26

**Q:** Under what condition regarding the determinant does a matrix have no inverse?

**A:** A matrix has no inverse if its determinant is exactly zero.

---

## Card 27

**Q:** What special property do orthogonal matrices \(V\) have regarding their inverse?

**A:** \[ V^{-1} = V^T \]

---

## Card 28

**Q:** Why can the transpose be used instead of a full inversion for the HW2 eigenvector matrix \(V\)?

**A:** Because the matrix \(M\) is symmetric, its normalised eigenvectors are orthogonal, making \(V\) an orthogonal matrix.

---

## Card 29

**Q:** How is the transformed variable vector \(C'_t\) defined in the decoupling process?

**A:** \[ C'_t = V^{-1} C_t \]

---

## Card 30

**Q:** What is the resulting decoupled equation for \(C'_t\) after the change of variables?

**A:** \[ C'_t = \Gamma C'_{t-1} + \sigma \eta'_t \]

---

## Card 31

**Q:** Why does the diagonal nature of \(\Gamma\) allow for the 'decoupling' of a system?

**A:** It ensures that each variable in the transformed vector evolves independently as a univariate AR(1) process with no cross-variable terms.

---

## Card 32

**Q:** In the HW2 system, what are the two independent AR(1) equations generated by decoupling?

**A:** \[ u_t = \lambda u_{t-1} + \sigma(z_t + w_t) \] and \[ v_t = -\lambda v_{t-1} + \sigma(z_t - w_t) \]

---

## Card 33

**Q:** Once the decoupled variables \(u_t\) and \(v_t\) are solved, how is \(x_t\) recovered?

**A:** \[ x_t = \frac{u_t + v_t}{2} \]

---

## Card 34

**Q:** Once the decoupled variables \(u_t\) and \(v_t\) are solved, how is \(y_t\) recovered?

**A:** \[ y_t = \frac{u_t - v_t}{2} \]

---

## Card 35

**Q:** What is the first step in the pipeline to solve a coupled multivariate time series?

**A:** Stack the variables into vector notation \(C_t\) and identify the coefficient matrix \(M\).

---

## Card 36

**Q:** What is the purpose of finding the eigenvalues and eigenvectors (Steps 2 and 3) in the VAR solution pipeline?

**A:** To identify the natural stretch factors and the independent directions (modes) along which the system moves.

---

## Card 37

**Q:** Pitfall: What is a common mistake when assuming \(V^{-1} = V^T\)?

**A:** Assuming this property holds for all matrices; it only applies to orthogonal matrices (e.g. when \(M\) is symmetric and eigenvectors are normalised).

---

## Card 38

**Q:** Pitfall: What happens to the decoupling process if the determinant of \(V\) is zero?

**A:** The matrix \(V\) cannot be inverted, meaning the change of variables into natural coordinates is impossible.

---

## Card 39

**Q:** Pitfall: Why must eigenvectors be non-zero vectors?

**A:** The zero vector is a trivial solution to \(Mv = \gamma v\) and provides no information about the natural directions of the transformation.

---

## Card 40

**Q:** How does the matrix \(M\) transform the vector \(C_{t-1} = \begin{pmatrix} x_{t-1} \\ y_{t-1} \end{pmatrix}\) in the HW2 example?

**A:** It swaps the variables and scales them by \(\lambda\), resulting in \(\begin{pmatrix} \lambda y_{t-1} \\ \lambda x_{t-1} \end{pmatrix}\).

---

## Card 41

**Q:** What is the key insight behind diagonalization in time series analysis?

**A:** A coupled system of \(N\) variables is actually \(N\) independent modes in disguise; diagonalization reveals and separates these modes.

---

## Card 42

**Q:** How is the 'sum mode' \(u_t = x_t + y_t\) classified in terms of standard time series models?

**A:** It is an AR(1) process with an autoregressive coefficient of \(+\lambda\).

---

## Card 43

**Q:** How is the 'difference mode' \(v_t = x_t - y_t\) classified in terms of standard time series models?

**A:** It is an AR(1) process with an autoregressive coefficient of \(-\lambda\).

---

## Card 44

**Q:** Identify the diagonal matrix \(\Gamma\) for the HW2 system.

**A:** \[ \Gamma = \begin{pmatrix} \lambda & 0 \\ 0 & -\lambda \end{pmatrix} \]

---

## Card 45

**Q:** Identify the eigenvector matrix \(V\) for the HW2 system (normalised).

**A:** \[ V = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \]

---

## Card 46

**Q:** What is the property of an identity matrix \(I\) in the context of matrix inversion?

**A:** It satisfies the equation \(V V^{-1} = V^{-1} V = I\).

---

## Card 47

**Q:** What visual resource is recommended to understand matrices as linear transformations?

**A:** 3Blue1Brown's 'Essence of Linear Algebra' series, specifically Chapter 3.

---

## Card 48

**Q:** Why is \(V^{-1}\) called the 'change-of-basis' matrix in the decoupling process?

**A:** It maps the original observations from the standard \((x, y)\) basis into the basis formed by the system's eigenvectors.

---

## Card 49

**Q:** What does a zero eigenvalue imply for the evolution of its corresponding eigenvector mode?

**A:** The mode has no persistence; the transformation completely collapses that direction to zero in the next time step.

---

## Card 50

**Q:** In the HW2 system, how does the noise term \(\eta_t\) change after the decoupling transformation?

**A:** It is transformed by \(V^{-1}\) into \(\eta'_t = V^{-1}\eta_t\), which represents noise in the natural mode coordinates.

---

## Card 51

**Q:** Term: Orthogonal Matrix

**A:** Definition: A square matrix whose columns and rows are orthogonal unit vectors. Example: The matrix \(V = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\) where \(V^T V = I\).

---

## Card 52

**Q:** How is the characteristic equation derived from the eigenvalue definition?

**A:** By rearranging \(Mv = \gamma v\) to \((M - \gamma I)v = 0\) and requiring the determinant of the operator to be zero for non-trivial \(v\).

---

## Card 53

**Q:** Solve for the determinant of \(\begin{pmatrix} -\gamma & \lambda \\ \lambda & -\gamma \end{pmatrix}\).

**A:** \[ \gamma^2 - \lambda^2 \]

---

## Card 54

**Q:** What is the physical meaning of a negative eigenvalue in a VAR model, such as \(\gamma = -\lambda\)?

**A:** It indicates that the corresponding mode alternates or 'flips' sign at each time step (if \(\lambda > 0\)).

---

## Card 55

**Q:** What does it mean for a matrix to be 'singular'?

**A:** It means the matrix has a determinant of zero and therefore does not have an inverse.

---
