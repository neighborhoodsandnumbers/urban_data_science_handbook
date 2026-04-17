# Classification of Fixed Points

Nullclines tell us *where* the fixed points are. Now we need to know *what kind* they are. Does a fixed point attract or repel? Do trajectories approach along straight lines or spiral inward? Is the fixed point a saddle — attracting along one direction, repelling along another?

In one dimension, the answer was a single number: the derivative $f'(x^*)$. Negative meant stable, positive meant unstable. In two dimensions, the answer is a $2 \times 2$ matrix — the **Jacobian** — and its two eigenvalues produce a much richer taxonomy.

### The Jacobian Matrix

Given the system $\dot{x} = f(x, y)$, $\dot{y} = g(x, y)$ and a fixed point $(x^*, y^*)$, write $\mathbf{u} = (x - x^*, y - y^*)$ for the displacement from equilibrium. Taylor-expand to first order:

$$\dot{\mathbf{u}} \approx J\,\mathbf{u}, \qquad J = \begin{pmatrix} \partial f/\partial x & \partial f/\partial y \\ \partial g/\partial x & \partial g/\partial y \end{pmatrix}\bigg|_{(x^*, y^*)}$$

The Jacobian $J$ is the matrix we introduced in Section 2.1 as one of the three fundamental matrix types — alongside the adjacency matrix and the covariance matrix. Now it earns its place. The linearized system $\dot{\mathbf{u}} = J\mathbf{u}$ has the solution $\mathbf{u}(t) = e^{Jt}\mathbf{u}(0)$, and the eigenvalues of $J$ determine everything about the local dynamics: whether perturbations grow or decay, whether they oscillate, and how fast.

### The Trace-Determinant Plane

For a $2 \times 2$ matrix, the eigenvalues are determined by two numbers: the **trace** $\tau = \text{tr}(J) = \lambda_1 + \lambda_2$ and the **determinant** $\Delta = \det(J) = \lambda_1 \lambda_2$. The eigenvalues themselves are

$$\lambda_{1,2} = \frac{\tau \pm \sqrt{\tau^2 - 4\Delta}}{2}$$

This is the formula from Section 2.1, and it organizes the entire classification into regions of the $(\tau, \Delta)$ plane:

- **$\Delta < 0$**: eigenvalues are real with opposite signs. **Saddle point.** Trajectories approach along one eigendirection and flee along the other.
- **$\Delta > 0$, $\tau^2 - 4\Delta > 0$**: eigenvalues are real with the same sign. **Node.** Stable if $\tau < 0$ (both eigenvalues negative), unstable if $\tau > 0$ (both positive). Trajectories approach (or leave) along straight lines.
- **$\Delta > 0$, $\tau^2 - 4\Delta < 0$**: eigenvalues are complex conjugates $\lambda = \alpha \pm i\beta$, where $\alpha = \tau/2$ and $\beta = \sqrt{4\Delta - \tau^2}/2$. **Spiral.** Stable if $\tau < 0$ (the real part $\alpha$ is negative, so the spiral winds inward), unstable if $\tau > 0$ (outward spiral).
- **$\tau = 0$, $\Delta > 0$**: eigenvalues are purely imaginary $\pm i\beta$. **Center.** Trajectories form closed orbits around the fixed point — but this classification is fragile. Nonlinear terms can turn a center into a stable or unstable spiral. Centers are *not structurally stable* in generic nonlinear systems, a point we will return to in Section 4.6.
- **$\Delta = 0$**: at least one eigenvalue is zero. The fixed point is **non-isolated** — it sits on a line of fixed points. This is the degenerate case, analogous to $f'(x^*) = 0$ in 1D.
- **$\tau^2 = 4\Delta$** (the boundary parabola): eigenvalues are real and equal. **Star node** or **degenerate node**, depending on whether the Jacobian is diagonalizable. These are the transitions between nodes and spirals.

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

tau = np.linspace(-4, 4, 500)
fig, ax = plt.subplots(figsize=(8, 6))

# Parabola: tau^2 = 4*Delta (node-spiral boundary)
delta_parab = tau**2 / 4
ax.plot(tau, delta_parab, '-', color='#d1d1d1', lw=1.5, label=r'$\tau^2 = 4\Delta$')
ax.axhline(0, color='#d1d1d1', lw=1, alpha=0.5)
ax.axvline(0, color='#d1d1d1', lw=1, alpha=0.5)

# Shade regions
ax.fill_between(tau, 0, -5, color='#B91C1C', alpha=0.1)
ax.fill_between(tau[tau < 0], delta_parab[tau < 0], 6, color='#93C5FD', alpha=0.12)
ax.fill_between(tau[tau > 0], delta_parab[tau > 0], 6, color='#B91C1C', alpha=0.08)

# Labels
ax.text(-2.5, 3.5, 'stable\nspiral', fontsize=11, color='#93C5FD', ha='center')
ax.text(2.5, 3.5, 'unstable\nspiral', fontsize=11, color='#B91C1C', ha='center')
ax.text(-2.5, 0.5, 'stable\nnode', fontsize=11, color='#93C5FD', ha='center')
ax.text(2.5, 0.5, 'unstable\nnode', fontsize=11, color='#B91C1C', ha='center')
ax.text(0, 4.5, 'center', fontsize=11, color='#D1B675', ha='center')
ax.text(0, -2.5, 'saddle', fontsize=11, color='#B91C1C', ha='center')

ax.set(xlim=(-4, 4), ylim=(-4, 6), xlabel=r'trace $\tau$',
       ylabel=r'determinant $\Delta$',
       title='Classification of 2D Fixed Points')
ax.legend(fontsize=9); plt.tight_layout(); plt.show()
```

This is one of the most important diagrams in dynamical systems. Every $2 \times 2$ Jacobian maps to a point in the $(\tau, \Delta)$ plane, and that point determines the local phase portrait. The parabola $\tau^2 = 4\Delta$ separates nodes (real eigenvalues) from spirals (complex eigenvalues). The $\Delta = 0$ line separates saddles from nodes. The $\tau = 0$ line separates stable from unstable. The entire classification is encoded in two scalar quantities that you can read off the Jacobian in seconds.

### Seeing the Classification

To build geometric intuition, let us compute the Jacobian for the competing species system from Section 4.1 and see how the eigenvalue classification matches the phase portrait.

At the coexistence fixed point of the weak-competition case ($\alpha_{12} = \alpha_{21} = 0.5$, $K_1 = K_2 = 1$), the fixed point is at $(x_1^*, x_2^*) = (2/3, 2/3)$. The Jacobian is:

$$J = \begin{pmatrix} -r_1 x_1^*/K_1 & -r_1 \alpha_{12} x_1^*/K_1 \\ -r_2 \alpha_{21} x_2^*/K_2 & -r_2 x_2^*/K_2 \end{pmatrix} = \begin{pmatrix} -2/3 & -1/3 \\ -1/3 & -2/3 \end{pmatrix}$$

```python
import numpy as np

# Jacobian at the coexistence fixed point
J = np.array([[-2/3, -1/3],
              [-1/3, -2/3]])

tau = np.trace(J)
delta = np.linalg.det(J)
eigenvalues = np.linalg.eigvals(J)
disc = tau**2 - 4*delta

print(f"Trace:       τ = {tau:.4f}")
print(f"Determinant: Δ = {delta:.4f}")
print(f"Discriminant: τ²-4Δ = {disc:.4f}")
print(f"Eigenvalues: {eigenvalues.round(4)}")

if delta < 0:
    print("Classification: saddle")
elif disc < 0:
    print(f"Classification: {'stable' if tau < 0 else 'unstable'} spiral")
else:
    print(f"Classification: {'stable' if tau < 0 else 'unstable'} node")
# τ = -1.333, Δ = 0.333, τ²-4Δ = 0.444 > 0 → stable node
```

The trace is negative and the discriminant $\tau^2 - 4\Delta$ is positive: a **stable node**. Both eigenvalues are real and negative ($\lambda_1 = -1/3$, $\lambda_2 = -1$), so trajectories approach the coexistence equilibrium along straight lines without spiraling. This matches what we saw in the streamplot — trajectories converged directly, not spiraling. Had the competition coefficients been different (asymmetric, say), the eigenvalues could become complex and the approach would be a spiral.

### The Saddle: Geometry of Instability

The saddle deserves special attention because it is the most important unstable fixed point in applications. A saddle has one attracting direction (the **stable manifold**) and one repelling direction (the **unstable manifold**). Trajectories that start exactly on the stable manifold approach the saddle, but any perturbation off this manifold gets amplified along the unstable direction.

In the competing species model with strong competition ($\alpha_{12} = \alpha_{21} = 1.5$), the interior fixed point at $(x_1^*, x_2^*) = (0.4, 0.4)$ is a saddle. Its stable manifold is the separatrix we saw in the streamplot — the curve that divides the basins of attraction of the two exclusion equilibria. Trajectories that start above the separatrix flow to the $x_2$-wins equilibrium; trajectories below flow to $x_1$-wins. The saddle's stable manifold is the boundary between ecological fates.

This pattern — saddle points as gatekeepers between competing attractors — recurs throughout the book: in bistable gene regulatory circuits (Chapter 25), in climate tipping points (Chapter 7), and in the dynamics of cooperation and defection (Chapter 16). Wherever a system has two stable states, there is a saddle between them.

### From Local to Global

The Jacobian gives exact information in the linearized neighborhood of each fixed point, but it says nothing about the global phase portrait. Two systems can have identical fixed-point classifications — same eigenvalues at every fixed point — yet have qualitatively different global dynamics, because the way trajectories connect between fixed points differs.

In one dimension, the global picture was determined by the local picture: between two consecutive fixed points, the flow had a definite direction, and that was that. In two dimensions, global dynamics can be far richer. Trajectories can spiral outward from an unstable fixed point and be captured by a limit cycle that the Jacobian knows nothing about. They can form heteroclinic connections — trajectories linking one saddle to another — that organize the global flow.

The next section takes up the genuinely new phenomenon of two-dimensional dynamics: the **limit cycle**, an isolated periodic orbit that attracts (or repels) all nearby trajectories. Its existence cannot be deduced from the Jacobian alone. We need a new theorem — the Poincaré-Bendixson theorem — and a new way of thinking about what the topology of the plane allows.
