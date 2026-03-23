# Linear Algebra Essentials

If there is one toolkit that earns its keep across every chapter of this book, it is linear algebra. When we linearize a dynamical system around a fixed point, we get a matrix. When we encode a network, we get a matrix. When we analyze correlations in data, we get a matrix. The question is always the same: *what does this matrix do?* The answer, almost always, comes from its eigenvalues.

This section is not a first course in linear algebra. We assume you have seen vectors, matrices, and matrix multiplication before, and we will move quickly through the basics to reach the ideas that matter most for complex systems: eigenvalues and eigenvectors, the spectral properties of symmetric matrices, and the singular value decomposition. If you want the full story, Strang's *Linear Algebra and Its Applications* {cite}`strang2006linear` is the definitive reference — lucid, deep, and full of applications. What follows is the subset you will need, with the emphasis shifted toward the specific structures that recur throughout this book.

## Vectors, Matrices, and Transformations

A vector $\mathbf{x} \in \mathbb{R}^n$ is a column of $n$ real numbers. An $m \times n$ matrix $A$ maps $\mathbb{R}^n$ to $\mathbb{R}^m$ via the rule $\mathbf{x} \mapsto A\mathbf{x}$. This is the *transformation viewpoint*, and it is the right way to think about matrices for our purposes. Forget for a moment the mechanical rules of matrix multiplication. Instead, think of $A$ as a machine: you feed it a vector, and it returns a new vector — stretched, rotated, projected, or some combination of all three.

```python
import numpy as np

# A 2x2 matrix that stretches by 2 along one axis and rotates by 30°
theta = np.pi / 6
A = np.array([[2 * np.cos(theta), -np.sin(theta)],
              [2 * np.sin(theta),  np.cos(theta)]])

x = np.array([1.0, 0.0])        # input vector
y = A @ x                        # transformed vector
print(f"Input:  {x}")            # [1. 0.]
print(f"Output: {y.round(3)}")   # [1.732 1.   ]
```

The columns of $A$ tell you where the standard basis vectors land. If $A$ is square and invertible (its columns are linearly independent), the transformation is reversible. The **rank** of $A$ is the dimension of its column space — the number of independent directions in the output. When $\text{rank}(A) < n$, the transformation crushes some directions to zero; the set of vectors sent to zero is the **null space** (or kernel). These concepts — rank, null space, linear independence — are the grammatical foundations. We will use them freely without further ceremony.

## Eigenvalues and Eigenvectors

Here is the central idea. Most vectors change direction when you multiply them by a matrix. But some special vectors $\mathbf{v}$ pass through unchanged in direction — only their magnitude scales:

$$A\mathbf{v} = \lambda\mathbf{v}$$

The scalar $\lambda$ is an **eigenvalue** and $\mathbf{v}$ is the corresponding **eigenvector**. To find them, we solve the characteristic equation $\det(A - \lambda I) = 0$, which for an $n \times n$ matrix gives an $n$th-degree polynomial in $\lambda$. An $n \times n$ matrix has exactly $n$ eigenvalues, counted with multiplicity (some may be complex, even for real matrices).

Why do eigenvalues dominate this book? Because they answer the question that drives almost every analysis: *does a small perturbation grow or shrink?* Near a fixed point $\mathbf{x}^*$ of a dynamical system $\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x})$, the dynamics are governed by the **Jacobian matrix** $J = \partial \mathbf{f} / \partial \mathbf{x} \big|_{\mathbf{x}^*}$. The eigenvalues of $J$ determine everything:

- All eigenvalues have $\text{Re}(\lambda) < 0$: the fixed point is **stable** (perturbations decay).
- Any eigenvalue has $\text{Re}(\lambda) > 0$: the fixed point is **unstable** (perturbations grow).
- Complex eigenvalues $\lambda = \alpha \pm i\beta$: the system **spirals** (oscillations with growth or decay set by $\alpha$).
- Purely real eigenvalues: the system moves along straight lines — a **node** (same sign) or **saddle** (opposite signs).

We will use this classification exhaustively in Chapters 4 and 5.

```python
import numpy as np

def classify_fixed_point(J):
    """Classify a 2D fixed point from its Jacobian matrix."""
    eigenvalues = np.linalg.eigvals(J)
    tr = np.trace(J)          # = sum of eigenvalues
    det = np.linalg.det(J)    # = product of eigenvalues

    if det < 0:
        return "saddle", eigenvalues
    elif tr**2 - 4*det < 0:   # complex eigenvalues
        kind = "stable spiral" if tr < 0 else "unstable spiral"
        return kind, eigenvalues
    else:
        kind = "stable node" if tr < 0 else "unstable node"
        return kind, eigenvalues

# Damped pendulum near the downward equilibrium:
# x'' + 0.5x' + sin(x) ≈ x'' + 0.5x' + x = 0  (linearized)
# As a system: x' = v, v' = -x - 0.5v
J = np.array([[0, 1], [-1, -0.5]])
kind, eigs = classify_fixed_point(J)
print(f"Classification: {kind}")
print(f"Eigenvalues: {eigs.round(4)}")
# Classification: stable spiral
# Eigenvalues: [-0.25+0.9682j -0.25-0.9682j]
```

Notice the shortcut: for a $2 \times 2$ matrix, the **trace** $\text{tr}(A) = \lambda_1 + \lambda_2$ and the **determinant** $\det(A) = \lambda_1 \lambda_2$. You can classify a fixed point from just these two numbers without computing eigenvalues explicitly. This is a theorem, not a trick: for any $n \times n$ matrix, the trace equals the sum of eigenvalues and the determinant equals their product {cite}`strang2006linear`.

**Diagonalization.** If $A$ has $n$ linearly independent eigenvectors, we can write $A = PDP^{-1}$, where $P$ is the matrix of eigenvectors and $D$ is the diagonal matrix of eigenvalues. This makes matrix powers trivial: $A^k = PD^kP^{-1}$, because raising a diagonal matrix to a power just raises each diagonal entry. This is why eigenvalues control the long-run behavior of iterated maps (Chapter 7) and Markov chains (Chapter 11).

**The spectral theorem.** Symmetric matrices — where $A = A^T$ — are especially well-behaved. Every symmetric matrix has *real* eigenvalues and a *full set of orthogonal eigenvectors*. That is: not only can you diagonalize it, but you can do so with an orthogonal matrix $Q$ (meaning $Q^{-1} = Q^T$), so $A = QDQ^T$. This is the spectral theorem, and it is one of the most useful results in applied mathematics. Every graph Laplacian and every covariance matrix is symmetric, so this theorem applies to much of what we study.

## Special Matrices in Complex Systems

Three families of matrices appear so often in this book that they deserve their own introduction.

**Positive definite and positive semidefinite matrices.** A symmetric matrix $A$ is **positive definite** if $\mathbf{x}^T A \mathbf{x} > 0$ for every nonzero vector $\mathbf{x}$. Equivalently, all its eigenvalues are strictly positive. If we relax to $\geq 0$, we get **positive semidefinite** (PSD). Covariance matrices are always PSD — this is a consequence of the definition $\Sigma = \mathbb{E}[(\mathbf{x} - \boldsymbol{\mu})(\mathbf{x} - \boldsymbol{\mu})^T]$. Positive definite matrices also arise as the Hessians of energy functions at stable equilibria, connecting linear algebra to the stability of physical systems.

**Stochastic matrices.** A nonnegative matrix whose rows each sum to 1 is called **(row) stochastic**. It represents transition probabilities: entry $a_{ij}$ is the probability of moving from state $i$ to state $j$. Every stochastic matrix has an eigenvalue equal to 1, and all other eigenvalues satisfy $|\lambda| \leq 1$. Under mild conditions (irreducibility and aperiodicity), the matrix powers $A^k$ converge to a rank-1 matrix whose rows are the **stationary distribution** — this is the Perron-Frobenius theorem. We will use it extensively when studying random walks and diffusion on networks in Chapter 11.

**The graph Laplacian.** Given a network with adjacency matrix $A$ (where $a_{ij} = 1$ if nodes $i$ and $j$ are connected), define the degree matrix $D = \text{diag}(d_1, \ldots, d_n)$ where $d_i = \sum_j a_{ij}$. The **graph Laplacian** is $L = D - A$. It is always symmetric and positive semidefinite. Its smallest eigenvalue is always 0 (with eigenvector $\mathbf{1}$, the all-ones vector), and the *multiplicity* of the zero eigenvalue equals the number of connected components of the graph. The second-smallest eigenvalue $\lambda_2$ — the **spectral gap** or **algebraic connectivity** — measures how well-connected the network is. We will lean on these properties heavily in Chapter 9.

```python
import numpy as np

# A small friendship network: 6 people, 7 connections
edges = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4), (4,5)]
n = 6
A = np.zeros((n, n))
for i, j in edges:
    A[i, j] = A[j, i] = 1       # undirected: symmetric

D = np.diag(A.sum(axis=1))       # degree matrix
L = D - A                        # graph Laplacian

eigs = np.sort(np.linalg.eigvalsh(L))
print(f"Laplacian eigenvalues: {eigs.round(3)}")
# Smallest eigenvalue ≈ 0 (connected graph)
# Second eigenvalue = spectral gap (algebraic connectivity)
print(f"Spectral gap λ₂ = {eigs[1]:.3f}")
```

## The Singular Value Decomposition

Not every matrix is square, and not every square matrix is diagonalizable. The **singular value decomposition** (SVD) works regardless. Every $m \times n$ matrix $A$ can be written as

$$A = U \Sigma V^T$$

where $U$ is $m \times m$ orthogonal, $V$ is $n \times n$ orthogonal, and $\Sigma$ is $m \times n$ diagonal with nonnegative entries $\sigma_1 \geq \sigma_2 \geq \cdots \geq 0$ called the **singular values**. Geometrically, any linear transformation is a rotation ($V^T$), followed by a scaling along coordinate axes ($\Sigma$), followed by another rotation ($U$).

The power of the SVD is truncation. Keep only the $k$ largest singular values and the corresponding columns of $U$ and $V$, and you get the **best rank-$k$ approximation** to $A$ in both the operator norm and the Frobenius norm (the Eckart-Young theorem). This is the mathematical engine behind dimensionality reduction: when you have a high-dimensional dataset, the leading singular values capture the dominant patterns and the trailing ones capture noise.

The connection to **principal component analysis** (PCA) is direct. If $X$ is a centered data matrix (observations as rows), its SVD gives $X = U\Sigma V^T$, and the columns of $V$ are the principal component directions — the axes of maximum variance. When we encounter PCA in Chapter 21 and covariance estimation in Chapter 19, the SVD will be the workhorse.

## Norms and the Matrix Exponential

We will frequently need to measure the "size" of vectors and matrices. The most common vector norms are the **Euclidean norm** $\|\mathbf{x}\|_2 = \sqrt{\sum x_i^2}$, the **$\ell^1$ norm** $\|\mathbf{x}\|_1 = \sum |x_i|$, and the **$\ell^\infty$ norm** $\|\mathbf{x}\|_\infty = \max |x_i|$. For matrices, the **operator norm** $\|A\| = \max_{\|\mathbf{x}\|=1} \|A\mathbf{x}\|$ measures the maximum stretching factor (it equals the largest singular value), while the **Frobenius norm** $\|A\|_F = \sqrt{\sum_{ij} a_{ij}^2}$ treats the matrix as a long vector.

The **matrix exponential** $e^{At}$ bridges linear algebra and differential equations. The system $\dot{\mathbf{x}} = A\mathbf{x}$ has the solution $\mathbf{x}(t) = e^{At}\mathbf{x}(0)$, defined by the power series $e^{At} = I + At + \frac{(At)^2}{2!} + \cdots$. If $A$ is diagonalizable as $A = PDP^{-1}$, then $e^{At} = P e^{Dt} P^{-1}$, where $e^{Dt}$ is just the diagonal matrix of $e^{\lambda_i t}$. This makes the connection to stability explicit: if all eigenvalues of $A$ have negative real parts, then every $e^{\lambda_i t} \to 0$ as $t \to \infty$, so every solution decays to the origin. This is exactly how we will analyze continuous-time linear systems starting in Chapter 4.

---

The tools in this section — eigenvalues, the spectral theorem, positive definiteness, stochastic matrices, the graph Laplacian, the SVD, and the matrix exponential — will reappear in nearly every chapter that follows. When you encounter a new system and are not sure where to start, compute the eigenvalues. They are, more often than not, the skeleton key. For deeper treatment, see Strang {cite}`strang2006linear`; for the computational side, Trefethen and Bau {cite}`trefethen1997numerical` is superb.
