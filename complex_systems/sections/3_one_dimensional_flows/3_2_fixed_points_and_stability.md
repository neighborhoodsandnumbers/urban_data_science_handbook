# Fixed Points and Stability

In the previous section, we classified fixed points as "stable" or "unstable" by reading the arrows on the phase portrait. Arrows pointing toward a fixed point meant stable; arrows pointing away meant unstable. This is correct, but it is not a *proof*. What if $f(x)$ touches zero without crossing it? What if $f'(x^*) = 0$? We need analytical tools to make the geometric intuition precise.

### Linear Stability Analysis

The idea is simple: zoom in. Near a fixed point $x^*$, write $x(t) = x^* + \delta(t)$ where $\delta$ is a small perturbation. Substitute into $\dot{x} = f(x)$ and expand $f$ in a Taylor series:

$$\dot{\delta} = f(x^* + \delta) = f(x^*) + f'(x^*)\delta + \frac{1}{2}f''(x^*)\delta^2 + \cdots$$

Since $x^*$ is a fixed point, $f(x^*) = 0$. If $\delta$ is small enough, the higher-order terms are negligible compared to the linear term, giving

$$\dot{\delta} \approx f'(x^*)\delta$$

This is a linear ODE with solution $\delta(t) = \delta(0)\, e^{f'(x^*)t}$. The behavior is determined entirely by the sign of $f'(x^*)$:

- **$f'(x^*) < 0$**: perturbations decay exponentially. The fixed point is **stable** (also called a *sink* or *attractor*).
- **$f'(x^*) > 0$**: perturbations grow exponentially. The fixed point is **unstable** (a *source* or *repeller*).
- **$f'(x^*) = 0$**: the linear approximation is inconclusive. We need higher-order terms, and the fixed point may be stable, unstable, or *half-stable* (attracting from one side, repelling from the other).

This is the one-dimensional version of the eigenvalue analysis from Section 2.1. In 1D, the Jacobian is a $1 \times 1$ matrix — just the number $f'(x^*)$ — and the single eigenvalue is $f'(x^*)$ itself. Everything we said about eigenvalues determining stability applies here, stripped to its simplest form. The trace-determinant classification of 2D fixed points in Chapter 4 will be the natural generalization.

```python
import numpy as np

# Linear stability analysis: classify fixed points of dx/dt = x - x^3
f = lambda x: x - x**3
fp = lambda x: 1 - 3*x**2  # f'(x)

fixed_points = [-1.0, 0.0, 1.0]
for x_star in fixed_points:
    slope = fp(x_star)
    if slope < 0:
        label = "stable"
    elif slope > 0:
        label = "unstable"
    else:
        label = "inconclusive (need higher-order terms)"
    print(f"x* = {x_star:+.1f}:  f'(x*) = {slope:+.1f}  →  {label}")
# x* = -1.0:  f'(x*) = -2.0  →  stable
# x* = +0.0:  f'(x*) = +1.0  →  unstable
# x* = +1.0:  f'(x*) = -2.0  →  stable
```

This confirms what we saw geometrically in Section 3.1: the origin is unstable, while $\pm 1$ are stable. But now we have a quantitative tool. The magnitude of $f'(x^*)$ tells us the *rate* of approach or departure — the **characteristic timescale** is $\tau = 1/|f'(x^*)|$. For the stable fixed points at $\pm 1$, $f'(x^*) = -2$, so $\tau = 0.5$. Perturbations decay by a factor of $e$ in half a time unit. This is something the phase portrait alone cannot tell you.

### Existence, Uniqueness, and the No-Crossing Theorem

The geometric method assumes something we have not yet justified: that trajectories are well-defined and don't do anything pathological. The **existence and uniqueness theorem** provides the guarantee.

**Theorem** (Picard-Lindelöf). *If $f(x)$ is continuous and its derivative $f'(x)$ is continuous (or more generally, if $f$ satisfies a Lipschitz condition), then for any initial condition $x(0) = x_0$, the ODE $\dot{x} = f(x)$ has a unique solution on some time interval.*

We will not prove this — the proof uses a contraction mapping argument that belongs in an analysis course (see Strogatz {cite}`strogatz2015nonlinear`, Appendix). But the consequence is critical: **trajectories cannot cross.** If two solutions started from different initial conditions could meet at a point $x$ at the same time, then the value $x$ would have two histories — contradicting uniqueness. On the real line, this means trajectories are strictly ordered: if $x_1(0) < x_2(0)$, then $x_1(t) < x_2(t)$ for all time.

This is why the phase portrait works. Between two consecutive fixed points, $f(x)$ has constant sign (by the intermediate value theorem, if it changed sign there would be another fixed point). The flow is monotone in each interval. No trajectory can reverse direction without passing through a fixed point, and no trajectory can reach a fixed point in finite time (because near $x^*$, the velocity $f(x) \to 0$, slowing the approach asymptotically).

The no-crossing theorem has a profound implication that we stated informally in Section 3.1: **in one dimension, the only possible long-term behaviors are convergence to a fixed point or escape to infinity.** There are no cycles. There is no chaos. The reason is topological: a trajectory on the real line that tried to oscillate would have to pass through a point going rightward on one occasion and leftward on another — but at that point, the velocity $f(x)$ has a definite value, so the trajectory must always go in the same direction there. Oscillation requires at least two dimensions, where trajectories can go *around* each other rather than *through* each other.

### Potential Functions

There is a beautiful restatement of one-dimensional dynamics that connects to physics and will reappear in statistical mechanics (Chapter 13) and optimization throughout Part VI.

If $f(x)$ can be written as the negative gradient of a **potential function** $V(x)$,

$$\dot{x} = f(x) = -\frac{dV}{dx}$$

then the dynamics are those of a particle rolling downhill on the landscape $V(x)$. Fixed points are the extrema of $V$: minima are stable (the ball rolls back), maxima are unstable (the ball rolls away), and inflection points with $V'' = 0$ are the degenerate cases.

The connection is exact: $f(x) = -V'(x)$ means $f'(x^*) = -V''(x^*)$. A stable fixed point ($f' < 0$) corresponds to $V'' > 0$ — a local minimum. An unstable fixed point ($f' > 0$) corresponds to $V'' < 0$ — a local maximum. The potential provides a global picture: the system always moves toward lower $V$, so $V$ is a **Lyapunov function** — it decreases monotonically along trajectories.

```python
import numpy as np

# Potential for dx/dt = x - x^3: integrate to get V(x) = -x^2/2 + x^4/4
V = lambda x: -x**2/2 + x**4/4
Vpp = lambda x: -1 + 3*x**2  # V''(x)

for x_star in [-1.0, 0.0, 1.0]:
    curvature = Vpp(x_star)
    kind = "minimum (stable)" if curvature > 0 else "maximum (unstable)"
    print(f"x* = {x_star:+.1f}:  V(x*) = {V(x_star):+.2f},  V''(x*) = {curvature:+.1f}  →  {kind}")
# x* = -1.0: minimum (stable), x* = 0.0: maximum (unstable), x* = +1.0: minimum (stable)
```

The potential landscape for $\dot{x} = x - x^3$ is a symmetric double well: two minima at $\pm 1$ separated by a maximum at the origin. A particle placed anywhere on this landscape rolls into the nearest well. The potential tells you at a glance which fixed point wins — and in Chapter 7, when we add noise to the dynamics, the depth of the wells will determine how long the system stays in each state before a random fluctuation kicks it over the barrier.

Not every one-dimensional system has a potential. The condition $f = -dV/dx$ requires $f$ to be the derivative of something, which in 1D is always true (just integrate). So every one-dimensional flow is a gradient flow. This is a special feature of one dimension that fails spectacularly in higher dimensions — most 2D systems are *not* gradient systems, which is why they can exhibit limit cycles and other phenomena that gradient flows cannot. We will encounter the distinction in Chapter 4.

### What We Have and What We Need

We now have a complete analytical toolkit for one-dimensional flows. Given $\dot{x} = f(x)$:

1. Find the fixed points by solving $f(x^*) = 0$.
2. Classify each one by computing $f'(x^*)$: negative means stable, positive means unstable.
3. Handle the degenerate case $f'(x^*) = 0$ by examining higher-order terms or the potential.
4. Sketch the phase portrait: arrows between fixed points determined by the sign of $f$.
5. Identify basins of attraction and long-term behavior for every initial condition.

This is sufficient for any *fixed* parameter value. But most systems of interest have parameters — a growth rate, a coupling strength, a temperature — and the qualitative behavior can change as those parameters vary. Fixed points can be born, merge, change stability, or vanish. These qualitative changes are called **bifurcations**, and they are the subject of the next section.
