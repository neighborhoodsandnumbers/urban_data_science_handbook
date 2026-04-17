# Phase Portraits on the Line

Every dynamical system in this book begins with the same question: given a rule for how things change, what happens in the long run? For one-dimensional flows, the rule takes the form

$$\dot{x} = f(x)$$

where $x$ is a real number — a population, a temperature, a concentration, the fraction of a population that is infected — and $f(x)$ is a smooth function that specifies the velocity: how fast and in which direction $x$ is changing at each moment. The conventional approach to this equation is to solve it. Find $x(t)$ explicitly. Compute the trajectory.

We are going to do something different. We are going to look at the picture.

The approach in this chapter is geometric. Instead of solving differential equations, we will learn to *read* them — extracting the full qualitative behavior from the shape of $f(x)$ alone. This turns out to be surprisingly powerful. For one-dimensional systems, the geometry gives you everything: where the system goes, how fast it gets there, and what happens when parameters change. The technique extends (with more effort) to two dimensions in Chapter 4 and to networks in Part III.

### Reading the Flow

Plot $f(x)$ versus $x$. Not a time series — not $x$ versus $t$ — but the velocity function itself. This single curve contains all the qualitative information about the dynamics. Here is why.

Where $f(x) > 0$, the velocity is positive, so $x$ is increasing — place a rightward arrow on the $x$-axis. Where $f(x) < 0$, the velocity is negative, so $x$ is decreasing — place a leftward arrow. Where $f(x) = 0$, the system sits still: these are the **fixed points** $x^*$ where the flow comes to rest. If you start at a fixed point, you stay there forever.

The arrows between fixed points constitute the **phase portrait** on the line. It tells you, at a glance, where every initial condition ends up.

Consider $\dot{x} = \sin x$. The fixed points are at $x^* = 0, \pm\pi, \pm 2\pi, \ldots$ — the zeros of sine. Between $0$ and $\pi$, $\sin x > 0$, so the flow pushes rightward toward $\pi$. Between $\pi$ and $2\pi$, $\sin x < 0$, so the flow pushes leftward — also toward $\pi$. The fixed point at $\pi$ attracts from both sides; we call it **stable**. The fixed point at $0$ repels to both sides; we call it **unstable**. The pattern alternates: stable, unstable, stable, unstable, all the way along the real line.

We haven't solved anything. We have read the dynamics directly from the shape of the sine function — its zeros and its sign between the zeros. This is the method.

```python
import numpy as np
from scipy.integrate import solve_ivp

# dx/dt = sin(x): where does each initial condition end up?
for x0 in [0.5, 1.5, 2.5, 4.0, 5.0, 6.0]:
    sol = solve_ivp(lambda t, x: np.sin(x), [0, 50], [x0],
                    rtol=1e-10, atol=1e-12)
    x_final = sol.y[0, -1]
    print(f"x(0) = {x0:.1f}  →  x(∞) ≈ {x_final:.4f}  ≈ {x_final/np.pi:.1f}π")
# Every trajectory converges to the nearest stable fixed point (odd multiple of π)
```

Every trajectory slides along the number line until it reaches a stable fixed point and stops. No trajectory can pass through a fixed point — at $x^*$, the velocity is zero, so arrival takes infinite time. And no trajectory can reverse direction — $\dot{x}$ has a definite sign between consecutive fixed points, so the flow is monotone in each interval. This monotonicity is a fundamental constraint of one-dimensional dynamics that will have deep consequences later.

### Qualitative Analysis

The phase portrait answers the questions that matter without ever producing an explicit formula for $x(t)$.

**Where does the system end up?** Follow the arrows from the initial condition to the nearest stable fixed point. The set of initial conditions that flow to a given fixed point is its **basin of attraction** — a concept we will formalize in Chapter 7.

**Can the system oscillate?** No. In one dimension, a trajectory moving rightward would have to reverse direction to oscillate, which would require passing through a point where $\dot{x} = 0$ — a fixed point. But trajectories that reach a fixed point stay there. So oscillations are impossible. This is not a failure of one-dimensional flows; it is a *theorem*, and it is the single most important reason we will need two dimensions (Chapter 4) to study anything more interesting than approach to equilibrium.

**Can the system blow up?** It can escape to $\pm\infty$ if $f(x)$ doesn't change sign for large $|x|$. For $\dot{x} = x^2$, the flow is rightward for all $x > 0$ and accelerates as $x$ grows — the system reaches infinity in finite time. For $\dot{x} = x - x^3$, the cubic term dominates at large $|x|$ and pushes trajectories back, preventing escape. The behavior of $f$ at the boundaries determines whether solutions exist for all time.

Consider the system $\dot{x} = x - x^3$. The velocity function is a cubic with three zeros: $x^* = -1, 0, 1$. For $x > 1$, $f(x) < 0$ — the flow pushes leftward, toward $x^* = 1$. For $0 < x < 1$, $f(x) > 0$ — the flow pushes rightward, also toward $x^* = 1$. For $-1 < x < 0$, $f(x) < 0$ — leftward, toward $x^* = -1$. And for $x < -1$, $f(x) > 0$ — rightward, toward $x^* = -1$. The origin is unstable; $\pm 1$ are stable. The basin of attraction of $x^* = 1$ is the entire positive half-line $(0, \infty)$, and the basin of $x^* = -1$ is $(-\infty, 0)$. The origin is the boundary between them — a repeller poised between two attractors.

### Population Growth

These are not just mathematical exercises. Return to the logistic equation from the chapter opening:

$$\dot{N} = rN\left(1 - \frac{N}{K}\right)$$

The velocity function is a downward-opening parabola with zeros at $N^* = 0$ and $N^* = K$. For $0 < N < K$, the parabola is positive — the population grows. For $N > K$, it is negative — the population shrinks back toward the carrying capacity. The phase portrait is immediate: $N^* = 0$ is unstable, $N^* = K$ is stable, and every positive initial condition converges to $K$.

This is Verhulst's insight recast in geometric language: the carrying capacity is not just a number you fit to data. It is a **stable fixed point** of the flow — a value toward which the system is actively pulled by the dynamics. Perturb the population above $K$ (by immigration, say) and it declines. Perturb it below $K$ (by a harvest) and it recovers. The stability is structural, encoded in the shape of $f(N)$.

```python
import numpy as np
from scipy.integrate import solve_ivp

# Logistic growth: all roads lead to K
r, K = 0.5, 100
f = lambda t, N: [r * N[0] * (1 - N[0] / K)]

for N0 in [2, 10, 50, 120, 200]:
    sol = solve_ivp(f, [0, 40], [N0], dense_output=True)
    t_eval = np.linspace(0, 40, 5)
    trajectory = sol.sol(t_eval)[0]
    print(f"N(0)={N0:3d}  →  N(10)={trajectory[2]:.1f}  →  N(40)={trajectory[-1]:.1f}")
# Regardless of starting point, the population converges to K = 100
```

Pearl and Reed rediscovered Verhulst's equation in 1920 and fit it to United States census data from 1790 to 1910 — the fit was excellent, and they predicted the population would level off around 197 million. The prediction held for decades and then failed spectacularly: the post-war baby boom, the immigration waves of the late twentieth century, and the rise of industrial agriculture all violated the model's assumption of a fixed carrying capacity {cite}`strogatz2015nonlinear`. The logistic equation was right about the mechanism (growth limited by resources) and wrong about the parameter (the carrying capacity is not constant). This is a pattern we will see repeatedly: a model captures the qualitative dynamics correctly while getting the quantitative details wrong, and the *way* it fails is itself informative.

### What One Dimension Cannot Do

We have extracted a remarkable amount from the simple equation $\dot{x} = f(x)$. Fixed points, stability, basins of attraction, convergence — all read directly from the graph of $f$, without solving the equation.

But one-dimensional flows have a hard ceiling. We proved, informally, that oscillations are impossible on the line. The only long-term behavior is convergence to a fixed point (or escape to infinity). No cycles. No chaos. No sustained oscillation. A heartbeat, a predator-prey cycle, a business cycle — none of these can be captured by a single first-order ODE.

The next section formalizes the stability analysis we have been doing by eye — making precise the intuition that "arrows pointing toward a fixed point" means stability. After that, Section 3.3 asks what happens when a parameter changes and fixed points are born, merge, or disappear. And Section 3.5 shows that changing the topology of the state space — from a line to a circle — opens the door to oscillations, bridging toward the richer dynamics of Chapter 4.
