# Phase Planes and Nullclines

In Chapter 3, the phase portrait was a line with arrows. Now it is a plane with vectors — more information, more possibilities, but the same geometric philosophy: read the dynamics from the picture.

The system is now a pair of coupled ODEs:

$$\dot{x} = f(x, y), \qquad \dot{y} = g(x, y)$$

The state is a point $(x, y)$ in the plane. At every point, the functions $f$ and $g$ assign a velocity vector $(f, g)$ — how fast and in which direction the state is moving. The phase portrait is the family of trajectories that fill the plane, each one tangent to the velocity field at every point. By the existence-uniqueness theorem (Picard-Lindelöf, now applied to systems), trajectories through distinct initial conditions never cross. This is the same no-crossing result we used in 1D, and it is just as fundamental here: it guarantees that the phase portrait is an organized structure, not a tangle.

The question is: how do we read this structure without solving the system?

### The Vector Field

Start by plotting the velocity vector $(f, g)$ at a grid of points in the $(x, y)$ plane. This is the **vector field** — the 2D generalization of plotting $f(x)$ versus $x$ on the line. Where the vectors are large, the flow is fast. Where they are small, the flow is slow. Where they vanish, we have a **fixed point**: a state $(x^*, y^*)$ where $f(x^*, y^*) = 0$ and $g(x^*, y^*) = 0$ simultaneously.

In one dimension, fixed points were zeros of a single function — easy to find and always isolated (generically). In two dimensions, fixed points are solutions to a *system* of two equations in two unknowns. They are still generically isolated, but finding them algebraically can be harder. This is where nullclines come in.

### Nullclines

The **$x$-nullcline** is the set of points where $f(x, y) = 0$ — where the horizontal component of velocity vanishes. On this curve, the velocity vector points purely vertically (up or down). The **$y$-nullcline** is the set of points where $g(x, y) = 0$ — the vertical component vanishes, and the velocity points purely horizontally (left or right).

These two curves are the skeleton of the phase plane. They divide it into regions where the velocity vector has a definite sign pattern — northeast, northwest, southeast, or southwest — depending on the signs of $f$ and $g$. This is the 2D analog of reading the sign of $f(x)$ between consecutive zeros in 1D. And where the two nullclines intersect, *both* components of velocity vanish: we have a fixed point.

The workflow for reading a 2D phase portrait:

1. **Draw the nullclines.** Sketch or plot the curves $f(x,y) = 0$ and $g(x,y) = 0$.
2. **Mark the fixed points.** They are the intersections.
3. **Determine the flow direction in each region.** Pick a test point in each region bounded by nullclines and evaluate the signs of $f$ and $g$.
4. **Sketch trajectories.** Draw curves consistent with the flow arrows, tangent to the velocity field, respecting the no-crossing theorem.

This gives you the qualitative picture — which fixed points attract, which repel, whether trajectories spiral or approach directly — without solving a single equation.

### Competing Species

To see nullclines in action, consider two species competing for the same resource. Their populations $x_1$ and $x_2$ each grow logistically but suppress each other:

$$\dot{x}_1 = r_1 x_1\left(1 - \frac{x_1 + \alpha_{12} x_2}{K_1}\right), \qquad \dot{x}_2 = r_2 x_2\left(1 - \frac{x_2 + \alpha_{21} x_1}{K_2}\right)$$

The competition coefficients $\alpha_{12}$ and $\alpha_{21}$ measure how much each species suppresses the other. Setting each right-hand side to zero gives the nullclines. The $x_1$-nullcline is the union of $x_1 = 0$ (the $x_2$-axis) and the line $x_1 + \alpha_{12} x_2 = K_1$. The $x_2$-nullcline is $x_2 = 0$ (the $x_1$-axis) and the line $x_2 + \alpha_{21} x_1 = K_2$.

Everything depends on how these two lines intersect. If the nullclines cross in the positive quadrant, a coexistence equilibrium exists. If they don't cross — if one species' nullcline lies entirely inside the other's — one species drives the other to extinction. The geometry of two straight lines determines the ecological outcome.

```python
import numpy as np
import matplotlib.pyplot as plt

# Competing species: coexistence case
r1, r2, K1, K2 = 1.0, 1.0, 1.0, 1.0
a12, a21 = 0.5, 0.5  # weak competition → coexistence

x = np.linspace(0, 1.4, 30)
y = np.linspace(0, 1.4, 30)
X, Y = np.meshgrid(x, y)
U = r1 * X * (1 - (X + a12 * Y) / K1)
V = r2 * Y * (1 - (Y + a21 * X) / K2)

fig, ax = plt.subplots(figsize=(7, 6))
ax.streamplot(X, Y, U, V, color='#d1d1d1', linewidth=0.6, density=1.5,
              arrowsize=1.2)

# Nullclines
x_line = np.linspace(0, 1.4, 100)
ax.plot(x_line, (K1 - x_line) / a12, '--', color='#D1B675', lw=2,
        label=r'$x_1$-nullcline: $x_1 + \alpha_{12} x_2 = K_1$')
ax.plot(x_line, K2 - a21 * x_line, '--', color='#93C5FD', lw=2,
        label=r'$x_2$-nullcline: $x_2 + \alpha_{21} x_1 = K_2$')

# Fixed points
fps = [(0, 0), (K1, 0), (0, K2)]
det = 1 - a12 * a21
if det != 0:
    x_star = (K1 - a12 * K2) / det
    y_star = (K2 - a21 * K1) / det
    if x_star > 0 and y_star > 0:
        fps.append((x_star, y_star))
        ax.plot(x_star, y_star, 'o', color='#93C5FD', ms=10, zorder=5)

ax.set(xlim=(0, 1.4), ylim=(0, 1.4),
       xlabel='Species 1 ($x_1$)', ylabel='Species 2 ($x_2$)',
       title='Competing Species: Coexistence')
ax.legend(fontsize=9, loc='upper right'); plt.tight_layout(); plt.show()
```

Matplotlib's `streamplot` is the 2D analog of the flow arrows we drew on the line in Chapter 3 — it integrates the velocity field and draws curves tangent to it everywhere. The dashed lines are the nullclines: where the gold line crosses a trajectory, the flow is purely vertical; where the blue line crosses, it is purely horizontal. The coexistence fixed point sits at the intersection, and trajectories from all initial conditions in the positive quadrant spiral into it.

Change the competition coefficients to $\alpha_{12} = 1.5$, $\alpha_{21} = 1.5$ (strong competition) and the nullclines no longer intersect in the interior. Instead, two exclusion equilibria appear on the axes — one where species 1 wins and one where species 2 wins — separated by a **separatrix** that acts as a boundary between their basins of attraction. The qualitative outcome flips from coexistence to bistable exclusion, determined entirely by the geometry of two lines.

```python
# Strong competition: bistable exclusion
a12, a21 = 1.5, 1.5
U = r1 * X * (1 - (X + a12 * Y) / K1)
V = r2 * Y * (1 - (Y + a21 * X) / K2)

fig, ax = plt.subplots(figsize=(7, 6))
ax.streamplot(X, Y, U, V, color='#d1d1d1', linewidth=0.6, density=1.5,
              arrowsize=1.2)
ax.plot(x_line, (K1 - x_line) / a12, '--', color='#D1B675', lw=2,
        label=r'$x_1$-nullcline')
ax.plot(x_line, K2 - a21 * x_line, '--', color='#93C5FD', lw=2,
        label=r'$x_2$-nullcline')
ax.plot(K1, 0, 'o', color='#93C5FD', ms=10, zorder=5)
ax.plot(0, K2, 'o', color='#93C5FD', ms=10, zorder=5)
ax.set(xlim=(0, 1.4), ylim=(0, 1.4),
       xlabel='Species 1 ($x_1$)', ylabel='Species 2 ($x_2$)',
       title='Competing Species: Bistable Exclusion')
ax.legend(fontsize=9, loc='upper right'); plt.tight_layout(); plt.show()
```

Same equations, different parameters, qualitatively different dynamics. The nullcline geometry — how the lines sit relative to each other — is all you need to see this. No eigenvalues, no Jacobians, no explicit solutions. Just two curves and a picture.

### What Nullclines Cannot Tell You

Nullclines are powerful but not omniscient. They tell you *where* fixed points are and the *gross flow direction* in each region of the plane. But they do not tell you:

- **Whether trajectories spiral or approach directly.** A trajectory converging to a fixed point might approach along a straight line (a node) or wind around it (a spiral). The nullclines can't distinguish these.
- **How fast the system moves.** Nullclines say nothing about timescales. A trajectory might spend most of its time crawling along a slow manifold and then jump rapidly across the phase plane — the phenomenon of relaxation oscillations in Section 4.5.
- **Whether limit cycles exist.** An isolated periodic orbit is the signature new phenomenon of 2D dynamics, and nullclines alone cannot detect one. For that, we need the Poincaré-Bendixson theorem (Section 4.3).

For the local behavior near each fixed point — node, spiral, saddle, or center — we need the eigenvalues of the Jacobian matrix, the analytical tool we previewed in Section 2.1 and developed for 1D in Section 3.2. The next section extends it to two dimensions, where a $2 \times 2$ matrix and the trace-determinant formula replace the single derivative $f'(x^*)$.
