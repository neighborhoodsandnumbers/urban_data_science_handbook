# Limit Cycles

In one dimension, the only possible long-term behavior was convergence to a fixed point — we proved this in Section 3.2 using the no-crossing theorem. In two dimensions, fixed points are still important, but the plane admits something new: **periodic orbits**. A trajectory can loop around and return exactly to its starting point, tracing the same path forever.

Not all periodic orbits are created equal. A **limit cycle** is an *isolated* closed orbit — isolated in the sense that nearby trajectories are not periodic but instead spiral toward the cycle (stable limit cycle) or away from it (unstable limit cycle). This is qualitatively different from the closed orbits around a center, which come in continuous families. Perturb a center slightly and the closed orbits typically disintegrate; perturb a limit cycle and it deforms but persists. Limit cycles are **structurally stable** — they are the robust form of oscillation in dissipative systems.

This distinction matters enormously. A heartbeat, a circadian rhythm, the firing of a neuron, the oscillation of a predator-prey system in a fluctuating environment — these are all limit cycles, not centers. They are self-sustained oscillations that persist despite perturbation, not fragile closed orbits that exist only under ideal conditions.

### The Poincaré-Bendixson Theorem

How do you prove a limit cycle exists without finding it explicitly? The answer is one of the most elegant results in the qualitative theory of differential equations.

**Theorem** (Poincaré-Bendixson). *Suppose a trajectory of a 2D continuous dynamical system is confined to a closed, bounded region of the plane that contains no fixed points. Then the trajectory must approach a periodic orbit as $t \to \infty$.*

The proof (which we sketch rather than give in full — see Strogatz {cite}`strogatz2015nonlinear` for details) uses the topology of the plane. A trajectory confined to a bounded region must accumulate somewhere — its $\omega$-limit set is nonempty. In 2D, the Jordan curve theorem constrains what this limit set can be: it cannot be a strange attractor or a chaotic trajectory, because those require the trajectory to fold and stretch in ways that are impossible without crossing itself in the plane. The only options are fixed points and periodic orbits. If we have excluded fixed points from the trapping region, only periodic orbits remain.

The practical recipe for applying Poincaré-Bendixson:

1. **Find a trapping region** — a closed curve in the phase plane such that all trajectories on the boundary point inward. Any trajectory that enters this region can never leave.
2. **Show the region contains no fixed points.** Check that $f$ and $g$ don't vanish simultaneously anywhere inside.
3. **Conclude** that a periodic orbit exists inside the region.

The theorem tells you the limit cycle *exists* but not where it is or what it looks like. For that, you need numerics.

```python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Van der Pol oscillator: the canonical limit cycle
# x'' - mu*(1-x^2)*x' + x = 0, rewritten as a system
mu = 1.0

def vdp(t, state):
    x, y = state
    return [y, mu * (1 - x**2) * y - x]

fig, ax = plt.subplots(figsize=(7, 6))

# Trajectories from several initial conditions
for x0, y0, color in [(0.1, 0.1, '#93C5FD'), (3.0, 0.0, '#D1B675'),
                        (-2.0, 3.0, '#d1d1d1'), (0.5, -2.5, '#d1d1d1')]:
    sol = solve_ivp(vdp, [0, 30], [x0, y0], max_step=0.05, dense_output=True)
    t_eval = np.linspace(0, 30, 3000)
    x, y = sol.sol(t_eval)
    ax.plot(x, y, color=color, lw=0.8, alpha=0.7)

# Mark the unstable fixed point at the origin
ax.plot(0, 0, 'o', color='#B91C1C', ms=8, mfc='none', mew=2, zorder=5)
ax.set(xlabel='$x$', ylabel='$y$',
       title=f'Van der Pol Oscillator ($\\mu = {mu}$): Limit Cycle')
plt.tight_layout(); plt.show()
```

The van der Pol oscillator $\ddot{x} - \mu(1 - x^2)\dot{x} + x = 0$ is the textbook limit cycle. The origin is an unstable spiral (check: the Jacobian at $(0,0)$ has trace $\mu > 0$). Trajectories starting near the origin spiral outward. Trajectories starting far away spiral inward. They all converge to the same closed orbit — the stable limit cycle. The cycle is an attractor, and its basin of attraction is the entire plane minus the origin.

### Ruling Out Limit Cycles

The Poincaré-Bendixson theorem tells you when a limit cycle must exist. The **Bendixson-Dulac criterion** tells you when one *cannot*.

**Theorem** (Bendixson-Dulac). *If there exists a smooth function $\varphi(x, y)$ such that $\nabla \cdot (\varphi \mathbf{F})$ — the divergence of $\varphi$ times the vector field — has constant sign (and is not identically zero) in a simply connected region, then no closed orbit exists in that region.*

The proof uses the divergence theorem: the integral of $\nabla \cdot (\varphi \mathbf{F})$ over the interior of a closed orbit equals the line integral of $\varphi \mathbf{F} \cdot \hat{n}$ around the orbit. But on a closed orbit, $\mathbf{F}$ is tangent to the curve, so $\mathbf{F} \cdot \hat{n} = 0$ everywhere. The integral vanishes — contradicting the assumption that the integrand has constant sign.

The art is choosing the right $\varphi$. For $\varphi = 1$ (the plain Bendixson criterion), you just check whether $\nabla \cdot \mathbf{F} = \partial f/\partial x + \partial g/\partial y$ has constant sign. If the divergence is everywhere negative, the area of any closed curve shrinks under the flow — no room for a periodic orbit. If everywhere positive, the area expands — same conclusion.

```python
import numpy as np

# Bendixson test: competing species cannot oscillate
# dx1/dt = r1*x1*(1 - (x1 + a12*x2)/K1)
# dx2/dt = r2*x2*(1 - (x2 + a21*x1)/K2)
# Divergence: df/dx1 + dg/dx2

r1, r2, K1, K2 = 1.0, 1.0, 1.0, 1.0
a12, a21 = 0.5, 0.5

# df/dx1 = r1*(1 - (2*x1 + a12*x2)/K1)
# dg/dx2 = r2*(1 - (2*x2 + a21*x1)/K2)
# In the positive quadrant near the coexistence equilibrium:
x1_star, x2_star = 2/3, 2/3
div_f = r1 * (1 - (2*x1_star + a12*x2_star)/K1)
div_g = r2 * (1 - (2*x2_star + a21*x1_star)/K2)
divergence = div_f + div_g
print(f"Divergence at ({x1_star:.2f}, {x2_star:.2f}): {divergence:.4f}")
print("Negative everywhere near equilibrium → no limit cycles (Bendixson)")
```

This is why the competing species model from Section 4.1 cannot oscillate: the divergence of the vector field is negative throughout the positive quadrant (for biologically reasonable parameters). The flow contracts area, squeezing trajectories toward fixed points. No room for a limit cycle. The classification as a stable node from Section 4.2 was not an accident — it was forced by the structure of the equations.

### What Two Dimensions Can and Cannot Do

The Poincaré-Bendixson theorem has a corollary that is as important as the theorem itself: **chaos is impossible in two-dimensional continuous flows.** In a bounded region of the 2D plane without fixed points, the only attractor is a periodic orbit. There is no room for the sensitive dependence on initial conditions, the fractal attractors, or the exponential divergence of nearby trajectories that characterize chaos. Those require at least three dimensions, where the Jordan curve theorem no longer applies and trajectories can fold without crossing.

This is a sharp topological constraint. Two dimensions give us oscillation — the heartbeat, the circadian clock, the predator-prey cycle. But they cannot give us the irregular, never-repeating dynamics of weather, turbulence, or the Lorenz system. For that, we will need Chapter 5.

Here is the hierarchy of dynamical complexity by dimension:

| Dimension | Possible long-term behaviors |
|---|---|
| 1 (line) | Fixed points only |
| 1 (circle) | Fixed points, uniform rotation |
| 2 (plane) | Fixed points, limit cycles |
| 3+ | Fixed points, limit cycles, chaos, strange attractors |

Each increase in dimension unlocks a qualitatively new phenomenon. The next section asks how limit cycles are *born* — the mechanism by which a stable fixed point loses stability and gives rise to oscillation. This is the **Hopf bifurcation**, the genuinely new bifurcation that has no analog in one dimension.
