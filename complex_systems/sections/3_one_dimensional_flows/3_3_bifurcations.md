# Bifurcations

Until now we have taken the velocity function $f(x)$ as given — a fixed rule for how $x$ changes. But the systems we care about are rarely so obliging. The growth rate of a population depends on rainfall; the stiffness of a beam depends on temperature; the infectivity of a pathogen depends on contact rates, seasonality, and whether schools are open. Real models come with **parameters**, and when those parameters change, the dynamics can change with them.

Usually the change is dull. A parameter shifts, a fixed point drifts a little, life carries on. But occasionally a parameter crosses a threshold where the *qualitative* structure of the phase portrait changes: a fixed point appears from nothing, two fixed points collide and annihilate, a single stable state splits into two. These qualitative changes are called **bifurcations**, and they are where one-dimensional dynamics starts to get interesting.

A bifurcation is the simplest signature of what systems researchers mean by a "tipping point." Hemingway's Mike Campbell, asked in *The Sun Also Rises* how he went bankrupt, answers, "Two ways. Gradually, then suddenly." That is the rhythm of a bifurcation. The parameter drifts for a long time with nothing much happening, and then in a single moment the fixed point structure reorganizes and the system behaves differently. We will meet gradual-then-sudden repeatedly over the next several chapters, most dramatically in Chapter 7 on critical transitions; this section is where the machinery begins.

### Normal Forms and Bifurcation Diagrams

A remarkable fact about one-dimensional bifurcations is that there are essentially only three of them. Every way that fixed points can be born, die, or swap stability near a single parameter threshold reduces — by a smooth change of coordinates — to one of three **normal forms**: the saddle-node, the transcritical, and the pitchfork. Thousands of specific models turn out, when you zoom in on the transition, to be the same dynamical organism wearing different clothes. This is our first encounter with *universality*, a theme that will return with full force in the scaling-law chapters of Part IV.

The standard way to visualize a bifurcation is the **bifurcation diagram**: a plot of the fixed points $x^*$ as a function of the parameter $r$ (or $\mu$, $\lambda$, whatever the system uses). Stable branches are drawn solid; unstable branches are dashed. A single diagram compresses the entire family of phase portraits — one portrait per vertical slice — into a single picture.

### Saddle-Node Bifurcation

The saddle-node, sometimes called the **fold** or **tangent** bifurcation, is the mechanism by which two fixed points are born from empty space (or conversely, annihilate one another and vanish). Its normal form is

$$\dot{x} = r + x^2.$$

The fixed points satisfy $x^2 = -r$, which has two real solutions $x^*_\pm = \pm\sqrt{-r}$ when $r < 0$, one degenerate solution $x^* = 0$ at $r = 0$, and no real solutions at all when $r > 0$. Linear stability comes from $f'(x^*) = 2x^*$: the negative root is stable, the positive root unstable. As $r$ climbs toward zero the two fixed points migrate toward each other, collide at the origin, and annihilate. On the bifurcation diagram the two branches form a sideways parabola opening to the left, with a stable lower arm and an unstable upper arm meeting tangentially at $r = 0$.

```python
import numpy as np

# Saddle-node: x* = ±sqrt(-r) for r < 0, none for r > 0
for r in [-1.0, -0.25, -0.01, 0.0, 0.25]:
    if r <= 0:
        x_star = np.sqrt(-r)
        print(f"r = {r:+.2f}:  x* = ±{x_star:.3f}  (stable: -, unstable: +)")
    else:
        print(f"r = {r:+.2f}:  no fixed points")
# r = -1.00:  x* = ±1.000  (two fixed points)
# r = -0.25:  x* = ±0.500
# r = -0.01:  x* = ±0.100  (about to collide)
# r = +0.00:  x* = ±0.000  (collision)
# r = +0.25:  no fixed points (annihilated)
```

The saddle-node is the archetype of **catastrophic** change. Before the bifurcation, the system sits comfortably at its stable fixed point, responding smoothly to small perturbations. After the bifurcation the stable state simply does not exist — there is nowhere nearby for the system to rest, and the trajectory must leave the region entirely.

A classic example is the **constant-harvest fishery**. Start with a logistic population under a steady extraction rate $h$:

$$\dot{N} = rN\left(1 - \frac{N}{K}\right) - h.$$

Without harvesting, the stable fixed point sits at $N^* = K$. As $h$ grows, the parabola $rN(1 - N/K)$ is pushed downward by $h$, and the two roots of $f(N)$ move toward each other: the upper root (stable carrying capacity) drifts down, the lower root (unstable threshold) drifts up. When $h$ reaches $rK/4$ — the peak of the logistic's parabola — the two fixed points collide and annihilate. For any harvest rate above this critical value, $\dot{N} < 0$ for all positive $N$, and the population crashes to zero. The fishery does not gracefully announce its collapse; it simply runs out of stable equilibria. The Atlantic cod fishery off Newfoundland, closed in 1992 after decades of rising quotas, is a textbook example of a saddle-node played out in the real world — and of the corollary that recovery after a fold is much harder than decline, because restoring the parameter below its critical value is not enough if the population has already collapsed into the basin of zero.

### Transcritical Bifurcation

Some fixed points refuse to disappear. In population biology, $N = 0$ is always a fixed point — you cannot have negative population, and zero of anything stays zero regardless of rates. In epidemic models the disease-free state $I = 0$ is likewise fixed by construction. When such a permanent fixed point exists, the only available bifurcation is for a second fixed point to pass *through* it and exchange stability. This is the **transcritical** bifurcation, with normal form

$$\dot{x} = rx - x^2.$$

The fixed points are $x^* = 0$ and $x^* = r$. From $f'(x) = r - 2x$, the origin has stability exponent $r$ (stable for $r < 0$, unstable for $r > 0$), while the moving fixed point has exponent $-r$ (unstable for $r < 0$, stable for $r > 0$). As $r$ crosses zero the two fixed points cross, trade their stability labels, and continue on their separate ways. The bifurcation diagram is an "X": two straight lines intersecting at the origin, with stability alternating on each segment.

The transcritical is the bifurcation of *thresholds*. The clearest example is the **SIS epidemic model**. Let $I$ be the fraction of a population infected with a non-immunizing pathogen:

$$\dot{I} = \beta I (1 - I) - \gamma I.$$

Rearranged, $\dot{I} = (\beta - \gamma)I - \beta I^2$ — exactly the transcritical normal form with $r = \beta - \gamma$. The disease-free state $I^* = 0$ is always a fixed point. When the basic reproduction number $R_0 = \beta/\gamma$ is less than one (so $r < 0$), the disease-free state is stable and the endemic fixed point lies at negative prevalence, which is biologically meaningless. When $R_0$ crosses one, the disease-free state loses stability, and the endemic fixed point $I^* = 1 - 1/R_0$ emerges into the positive region as the new attractor. This is the transcritical signature of the epidemic threshold — the same mathematics that underlies the laser threshold in physics, where the "off" state of an optical cavity is always available but only becomes unstable once the pump rate exceeds a critical value {cite}`strogatz2015nonlinear`. We will return to epidemic thresholds with more structure in Chapter 10.

### Pitchfork Bifurcation

The third and most interesting case arises in systems with a built-in symmetry — typically the reflection $x \to -x$. When the dynamics respect this symmetry, the velocity function must be an odd function of $x$, so only odd powers can appear in its Taylor expansion around $x = 0$. The lowest-order such expansion gives the **supercritical pitchfork**,

$$\dot{x} = rx - x^3,$$

whose fixed points are $x^* = 0$ for all $r$ and, additionally, $x^* = \pm\sqrt{r}$ for $r > 0$. Stability comes from $f'(x) = r - 3x^2$: the origin has exponent $r$ (stable below, unstable above), and the outer branches have exponent $-2r$ (stable wherever they exist). One fixed point becomes three. The bifurcation diagram looks exactly like its name — a trident handle extending through $r < 0$, splitting at $r = 0$ into two stable tines.

This is **symmetry breaking**. The equation $\dot{x} = rx - x^3$ is unchanged under $x \to -x$, but its stable solutions for $r > 0$ are not. The system must choose — positive or negative, left or right — and whichever it picks, the mirror-image state is equally valid. The choice is determined by the initial condition or, in noisy settings, by chance. Frost's two roads that diverged in a wood are the pitchfork's tines: a single path becomes two, and taking one excludes the other.

```python
import numpy as np
from scipy.integrate import solve_ivp

# Supercritical pitchfork: dx/dt = r*x - x^3
# Above the bifurcation, tiny differences in initial condition pick a branch
r = 1.0
f = lambda t, x: [r * x[0] - x[0]**3]
for x0 in [-1e-3, +1e-3, -0.5, +0.5]:
    sol = solve_ivp(f, [0, 30], [x0], rtol=1e-10, atol=1e-12)
    print(f"x(0) = {x0:+.4f}  →  x(30) = {sol.y[0,-1]:+.4f}")
# x(0) = -0.0010  →  x(30) = -1.0000
# x(0) = +0.0010  →  x(30) = +1.0000
# x(0) = -0.5000  →  x(30) = -1.0000
# x(0) = +0.5000  →  x(30) = +1.0000
```

The supercritical pitchfork is sometimes called a **second-order** or **continuous** transition, because as $r$ crosses zero the distance from the chosen branch to the origin grows smoothly from zero: $|x^*| = \sqrt{r}$. There is no jump. The square-root scaling $|x^*| \sim r^{1/2}$ is our first brush with a critical exponent, and it is not a coincidence that precisely this exponent governs the magnetization near the Curie point of an Ising magnet in mean-field theory. Chapter 13 will close the loop on that correspondence; for now it is worth noticing that the same normal form is describing a one-variable ODE and, lurking underneath, the phase transition of a thermodynamic system.

If instead the cubic coefficient has the *opposite* sign, we get the **subcritical pitchfork**,

$$\dot{x} = rx + x^3.$$

Now the non-trivial fixed points exist only for $r < 0$ (at $x^* = \pm\sqrt{-r}$) and are unstable. When the origin loses stability at $r = 0$, there is no nearby stable fixed point to catch the trajectory — the system's amplitude explodes. Something else, further out in the state space, must eventually stabilize the dynamics. The standard fix is to add a stabilizing fifth-order term:

$$\dot{x} = rx + x^3 - x^5.$$

This more realistic equation has five fixed points over part of its parameter range, and the resulting bifurcation diagram is the cleanest possible cartoon of **hysteresis**. As $r$ is increased past zero, the origin loses stability and the system jumps abruptly to a large-amplitude stable state. As $r$ is then *decreased*, the system does not return to zero at $r = 0$ — it stays locked onto the outer branch until $r$ falls well below zero, at which point the outer branch annihilates (via a saddle-node) with the middle unstable branch and the system jumps back. The forward and reverse jumps happen at different parameter values. The system remembers its history.

Hysteresis is a hallmark of **first-order** transitions — the sudden jumps, the history dependence, the possibility of bistability in a range of parameters. A buckled steel beam, pressed above its buckling load, snaps abruptly into one of two curved states and resists returning to straight even as the load is reduced. Shallow lakes that shift from clear to turbid as nutrient loading rises rarely recover when the loading is merely returned to its previous level {cite}`strogatz2015nonlinear`. We will build out the full theory of hysteresis and alternative stable states in Chapter 7, where it becomes the engine of regime shifts.

### The Three in One Picture

The three normal forms are not three unrelated phenomena. They are three possible fates for a fixed point that has gone critical — that is, one where $f(x^*) = 0$ and $f'(x^*) = 0$ simultaneously. If the leading non-vanishing term is $x^2$ with a generic coefficient, you get a saddle-node. If the system's structure forces $f(0) = 0$ for all parameters, the quadratic becomes transcritical. If there is an additional symmetry that kills the quadratic, you fall through to the cubic and get a pitchfork. The classification is *structural*, determined by which terms in the Taylor expansion are allowed to vanish and which are not.

What all three share is **codimension one**: they happen on adjusting a single parameter. To get something qualitatively richer — say, two fixed points colliding simultaneously with a symmetry being broken — you need to tune two parameters at once, which is the subject of the next section. Section 3.4 begins by asking what happens to the perfect pitchfork when the symmetry is slightly violated, leading into the cusp catastrophe and codimension-two unfoldings. In Chapter 4, when we move from the real line to the plane, the saddle-node and pitchfork will reappear almost unchanged, but a genuinely new one-parameter bifurcation becomes available — the **Hopf**, which creates oscillations and cannot occur in one dimension for the reason we proved in Section 3.2. And in Chapter 13, the pitchfork will reappear yet again, this time as the mean-field portrait of a second-order phase transition. The same handful of normal forms keeps turning up because the mathematics of local failure is parsimonious: there are only so many ways a fixed point can go bad.
