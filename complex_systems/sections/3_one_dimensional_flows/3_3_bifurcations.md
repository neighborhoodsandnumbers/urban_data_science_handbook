# Bifurcations

Everything we have done so far treated $f(x)$ as given and fixed. But real dynamical systems come with parameters — a growth rate, a harvesting quota, a temperature, a coupling strength — and as those parameters change, the qualitative picture can transform completely. Fixed points can be born, collide, swap stability, or vanish. These qualitative changes in the phase portrait are called **bifurcations**, and they are the organizing principle of parameter-dependent dynamics.

The question is: how many essentially different ways can a one-dimensional phase portrait change? The answer is surprisingly small. There are three canonical forms, and every generic bifurcation in a 1D flow is equivalent to one of them.

### The Saddle-Node Bifurcation

The most fundamental bifurcation, and the only one that is truly generic. Consider the normal form

$$\dot{x} = r + x^2$$

For $r < 0$, the parabola dips below the $x$-axis, creating two fixed points at $x^* = \pm\sqrt{-r}$. Check stability using the tool from Section 3.2: $f'(x) = 2x$, so $f'(-\sqrt{-r}) = -2\sqrt{-r} < 0$ (stable) and $f'(+\sqrt{-r}) = +2\sqrt{-r} > 0$ (unstable). One stable fixed point, one unstable, separated by a gap that shrinks as $r$ increases toward zero.

At $r = 0$, the two fixed points merge at the origin. The parabola just touches the axis: $f(0) = 0$ but $f'(0) = 0$, so linear stability analysis is inconclusive — this is the degenerate case we flagged in Section 3.2. The fixed point is **half-stable**: attracting from the left, repelling from the right.

For $r > 0$, the parabola has lifted entirely above the axis. No fixed points exist. The velocity is everywhere positive and the system flows rightward without rest.

This is the **saddle-node bifurcation** (also called a fold or tangent bifurcation): as $r$ increases through zero, a stable and an unstable fixed point approach each other, coalesce, and annihilate. The name anticipates higher dimensions, where the colliding fixed points are a saddle and a node.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2.5, 2.5, 300)
fig, ax = plt.subplots(figsize=(7, 4))
for r, color, label in [(-1, '#93C5FD', r'$r = -1$ (two fixed points)'),
                         (0, '#D1B675', r'$r = 0$ (bifurcation)'),
                         (1, '#B91C1C', r'$r = +1$ (no fixed points)')]:
    ax.plot(x, r + x**2, color=color, lw=2, label=label)
    if r < 0:
        ax.plot(-np.sqrt(-r), 0, 'o', color=color, ms=8)            # stable
        ax.plot(np.sqrt(-r), 0, 'o', color=color, ms=8,
                mfc='none', mew=2)                                    # unstable
    elif r == 0:
        ax.plot(0, 0, 's', color=color, ms=8)                        # half-stable
ax.axhline(0, color='gray', ls='--', alpha=0.3)
ax.set(xlabel='$x$', ylabel=r'$f(x) = r + x^2$')
ax.set_title('Saddle-Node Bifurcation: Phase Portraits')
ax.legend(fontsize=9); plt.tight_layout(); plt.show()
```

The three curves show the parabola sinking, touching, and lifting past the axis. For $r = -1$ (blue), two intersections mark the stable (filled) and unstable (open) fixed points. At $r = 0$ (gold), the vertex just grazes the axis — the two fixed points have merged. For $r = +1$ (red), the parabola clears the axis entirely. The fixed points have vanished.

Why is the saddle-node the "default" bifurcation? Because it requires no special structure. Whenever two fixed points collide in a generic one-parameter family, the collision looks like this. The implicit function theorem tells us why: at a bifurcation point where $f(x^*, r^*) = 0$ and $\partial f / \partial x = 0$, if the second derivative $\partial^2 f / \partial x^2 \neq 0$ and $\partial f / \partial r \neq 0$, a smooth change of variables reduces the system to $r + x^2$ {cite}`strogatz2015nonlinear`. No symmetry required. No structural constraint. The saddle-node is, as one colleague put it, the cockroach of bifurcation theory — it survives everything.

### The Transcritical Bifurcation

Sometimes a fixed point *must* exist for structural reasons. Zero population is always a fixed point of any population model — if nothing is alive, nothing can be born. In such cases, fixed points cannot simply appear or disappear. Instead, they **exchange stability**.

The normal form is

$$\dot{x} = rx - x^2 = x(r - x)$$

Two fixed points exist for all $r$: $x^* = 0$ and $x^* = r$. Stability: $f'(x) = r - 2x$, so $f'(0) = r$ and $f'(r) = -r$.

For $r < 0$: the origin is stable ($f' = r < 0$) and $x^* = r < 0$ is unstable. For $r > 0$: the origin is unstable ($f' = r > 0$) and $x^* = r$ is now stable. At $r = 0$, both fixed points meet at the origin and swap roles. The stable branch passes through unstable territory and vice versa — a changing of the guard.

The transcritical bifurcation is **not generic**: it requires $f(0, r) = 0$ for all $r$, meaning the origin is always a fixed point. A small perturbation adding a constant term — $\dot{x} = \epsilon + rx - x^2$ — destroys the transcritical and replaces it with a nearby saddle-node. The transcritical persists only when there is a structural reason for a fixed point to exist at a particular location, as in population dynamics where extinction is a permanent state.

### The Pitchfork Bifurcation

The most visually dramatic of the three, and the one that embodies symmetry breaking.

**Supercritical pitchfork.** The normal form is $\dot{x} = rx - x^3$ — the very system from Sections 3.1 and 3.2, now parametrized by $r$. Factoring: $\dot{x} = x(r - x^2)$, giving fixed points at $x^* = 0$ and $x^* = \pm\sqrt{r}$ (the latter existing only for $r > 0$).

For $r < 0$: the origin is the only fixed point, and it is stable ($f'(0) = r < 0$). For $r > 0$: the origin becomes unstable ($f'(0) = r > 0$), and two new stable fixed points are born at $\pm\sqrt{r}$ (check: $f'(\pm\sqrt{r}) = r - 3r = -2r < 0$). The bifurcation diagram looks like its namesake — a single prong splitting into two.

**Subcritical pitchfork.** The dangerous cousin: $\dot{x} = rx + x^3$. For $r < 0$, three fixed points exist — $x^* = 0$ (stable) and $x^* = \pm\sqrt{-r}$ (both unstable). The unstable branches act as guardrails. At $r = 0$, the guardrails collapse onto the origin, and for $r > 0$ only the unstable origin remains. The system has lost all stable equilibria and trajectories escape to infinity. This is a **catastrophic** transition — the system doesn't gently shift to a nearby state; it jumps discontinuously to a distant one.

Both forms share a symmetry: $f(-x) = -f(x)$. The vector field is odd, so if $x^*$ is a fixed point, so is $-x^*$. The pitchfork is the generic bifurcation for systems with this $x \to -x$ symmetry, just as the saddle-node is generic for systems with no special structure. Break the symmetry — add a small $\epsilon$ term that destroys the oddness — and the pitchfork splits into a saddle-node plus an isolated branch. This is exactly the subject of Section 3.4.

```python
import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(-2, 2, 500)
fig, axes = plt.subplots(1, 3, figsize=(13, 4), sharey=True)

# Saddle-node: x* = ±sqrt(-r) for r ≤ 0
rn = r[r <= 0]
axes[0].plot(rn, -np.sqrt(-rn), '-', color='#93C5FD', lw=2, label='stable')
axes[0].plot(rn, np.sqrt(-rn), '--', color='#B91C1C', lw=2, label='unstable')
axes[0].set(title='Saddle-Node\n' + r'$\dot{x} = r + x^2$', xlabel='$r$', ylabel='$x^*$')

# Transcritical: x* = 0 (stable→unstable) and x* = r (unstable→stable)
axes[1].plot(r[r <= 0], np.zeros(sum(r <= 0)), '-', color='#93C5FD', lw=2)
axes[1].plot(r[r > 0], np.zeros(sum(r > 0)), '--', color='#B91C1C', lw=2)
axes[1].plot(r[r <= 0], r[r <= 0], '--', color='#B91C1C', lw=2)
axes[1].plot(r[r > 0], r[r > 0], '-', color='#93C5FD', lw=2)
axes[1].set(title='Transcritical\n' + r'$\dot{x} = rx - x^2$', xlabel='$r$')

# Supercritical pitchfork: x* = 0 and x* = ±sqrt(r) for r > 0
rp = r[r >= 0]
axes[2].plot(r[r <= 0], np.zeros(sum(r <= 0)), '-', color='#93C5FD', lw=2)
axes[2].plot(r[r > 0], np.zeros(sum(r > 0)), '--', color='#B91C1C', lw=2)
axes[2].plot(rp, np.sqrt(rp), '-', color='#93C5FD', lw=2)
axes[2].plot(rp, -np.sqrt(rp), '-', color='#93C5FD', lw=2)
axes[2].set(title='Supercritical Pitchfork\n' + r'$\dot{x} = rx - x^3$', xlabel='$r$')

for ax in axes:
    ax.axhline(0, color='gray', ls=':', alpha=0.3)
    ax.axvline(0, color='gray', ls=':', alpha=0.3)
    ax.legend(fontsize=8)
plt.tight_layout(); plt.show()
```

These three bifurcation diagrams are the visual signatures of the three canonical bifurcations. In the saddle-node (left), two branches meet and vanish. In the transcritical (center), two branches cross and exchange stability at the origin. In the pitchfork (right), a single stable branch becomes unstable and spawns two new stable branches symmetrically. Solid lines are stable equilibria; dashed lines are unstable. Every generic bifurcation in a one-dimensional flow looks like one of these three.

### Normal Forms and Structural Stability

Why exactly three? The answer comes from **normal form theory**: near a bifurcation point, a smooth change of coordinates can strip away all the inessential features of $f(x, r)$ and reduce it to the simplest equation exhibiting that qualitative behavior. The three normal forms — $r + x^2$, $rx - x^2$, $rx \mp x^3$ — are the canonical representatives. Higher-order terms can be added without changing the qualitative picture.

The key concept is **codimension**: the number of conditions that must be simultaneously satisfied for the bifurcation to occur. All three have codimension 1 — a single parameter crossing a critical value. But they differ in **structural stability**:

| Bifurcation | Normal form | Mechanism | Requires |
|---|---|---|---|
| Saddle-node | $r + x^2$ | Two fixed points collide and annihilate | Nothing (generic) |
| Transcritical | $rx - x^2$ | Two fixed points exchange stability | Persistent fixed point |
| Pitchfork | $rx - x^3$ | Symmetric branching | Symmetry ($f$ odd in $x$) |

The saddle-node is **structurally stable**: perturb $f$ slightly and you still get a saddle-node. The transcritical and pitchfork are structurally *unstable* — they require special structure that small perturbations can destroy. Add a constant $\epsilon$ to the transcritical and it splits into two saddle-nodes. Add a small $\epsilon x^2$ to the pitchfork and it unzips into a saddle-node plus an isolated branch. In the real world, perfect symmetry is an idealization. What actually happens when the symmetry is only approximate is the subject of Section 3.4.

### Tipping Points

Return to the logistic equation from Section 3.1, but now add a constant harvest rate $H$:

$$\dot{N} = rN\left(1 - \frac{N}{K}\right) - H$$

This is a population under pressure. The growth term $rN(1 - N/K)$ pushes the population upward; the harvest $H$ pulls it down. For small $H$, two positive equilibria exist — a large, stable population and a small, unstable threshold below which the population collapses. As $H$ increases, the two equilibria approach each other. At the critical value $H_c = rK/4$, they collide and vanish in a saddle-node bifurcation. Beyond $H_c$, no positive equilibrium exists and the population crashes to zero.

```python
import numpy as np
import matplotlib.pyplot as plt

r, K = 1.0, 100
H = np.linspace(0, 30, 500)
H_crit = r * K / 4  # critical harvest rate

# Fixed points: (K/2)(1 ± sqrt(1 - 4H/(rK)))
disc = 1 - 4 * H / (r * K)
mask = disc >= 0
N_upper = (K / 2) * (1 + np.sqrt(disc[mask]))
N_lower = (K / 2) * (1 - np.sqrt(disc[mask]))

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(H[mask], N_upper, '-', color='#93C5FD', lw=2, label='stable equilibrium')
ax.plot(H[mask], N_lower, '--', color='#B91C1C', lw=2, label='unstable threshold')
ax.axvline(H_crit, color='#D1B675', ls=':', lw=1.5,
           label=f'$H_c = rK/4 = {H_crit:.0f}$')
ax.fill_between(H[~mask], 0, 100, color='#B91C1C', alpha=0.08)
ax.annotate('collapse', xy=(27, 30), fontsize=11, color='#B91C1C', style='italic')
ax.set(xlabel='Harvest rate $H$', ylabel='Population $N^*$',
       title='Tipping Point: Harvested Population')
ax.legend(fontsize=9); plt.tight_layout(); plt.show()
```

The plot shows the stable population (solid blue) and the unstable threshold (dashed red) converging as the harvest rate increases. At $H_c = 25$, they merge and the population has nowhere to go but zero. The shaded region beyond $H_c$ is the collapse zone.

This is why bifurcation theory matters beyond the classroom. The saddle-node bifurcation is the mathematical skeleton of every **tipping point** — in ecology, in climate science, in financial systems. A parameter drifts slowly, nothing seems to change, and then the qualitative structure of the dynamics shifts in an instant. The system gives no gentle warning. The stable equilibrium exists right up until the moment it doesn't. We will study tipping points and the early warning signals that sometimes precede them in Chapter 7 {cite}`strogatz2015nonlinear`.

We have classified the three canonical bifurcations and seen that only the saddle-node is truly generic — the transcritical requires a persistent fixed point, the pitchfork requires symmetry. But real systems are never perfectly symmetric. A beam buckling under compression exhibits a pitchfork bifurcation — but only if the beam is perfectly straight, which no beam ever is. What happens when the symmetry is *almost* satisfied? The next section takes up this question and finds that imperfection, far from being a nuisance, reveals additional structure.
