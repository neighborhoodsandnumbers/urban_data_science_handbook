# Flows on the Circle

Every section of this chapter so far has taken the state space for granted: $x$ lives on the real line $\mathbb{R}$. Populations, concentrations, positions — all things measured on an infinite ruler. But many of the most interesting scalars in science do not live on a line. They live on a circle. An angle is the canonical example: $\theta$ and $\theta + 2\pi$ are the same orientation. So is the phase of an oscillator, the time of day on a 24-hour clock, the position of a bead on a loop of wire, the longitude of a point on the Earth. The state space is $S^1$, the circle, and the change is more profound than it first appears.

On a circle, the topological argument that forbade oscillations in Section 3.1 breaks. A trajectory moving steadily in one direction on a line must flee to infinity or stop at a fixed point. A trajectory moving steadily in one direction on a circle *comes back*. Oscillations, impossible in one dimension on a line, are generic in one dimension on a circle. The reason is not dynamical but geometric — the same differential equation has different futures depending on whether we identify its endpoints. This section develops the machinery of flows on $S^1$, introduces a new bifurcation (the saddle-node on an invariant circle), and previews the phenomenon of *entrainment* that will organize Chapter 10's discussion of coupled oscillators.

### The Circle as State Space

We describe a flow on the circle by an ODE of the same form as before,

$$\dot{\theta} = f(\theta),$$

with one new requirement: $f$ is $2\pi$-periodic, $f(\theta + 2\pi) = f(\theta)$, so the vector field is well-defined on $S^1$. Fixed points are still the zeros of $f$; their stability is still determined by $f'(\theta^*)$. Picard-Lindelöf still guarantees unique trajectories. The phase-portrait method we developed in Section 3.1 works without modification — plot $f$, read off the arrows, identify the fixed points.

What changes is the set of possible long-term behaviors. On the line, every non-escaping trajectory converges to a fixed point. On the circle, there is a new option: if $f$ has no zeros at all, the state simply runs around the circle forever. The flow is *periodic*. A sustained oscillation, with no dissipation and no restoring mechanism beyond the topology of the state space itself.

The no-crossing theorem still applies locally — trajectories cannot cross in any small patch — but it no longer rules out cycles, because on a closed curve a trajectory can return to its starting point without crossing any other. We have, in effect, gotten periodic motion for free, by changing one topological assumption.

### The Uniform Oscillator

The simplest flow on a circle is

$$\dot{\theta} = \omega,$$

with $\omega$ a constant. The solution is $\theta(t) = \theta_0 + \omega t \bmod 2\pi$. The state rotates at a constant angular speed. The period is

$$T = \frac{2\pi}{\omega},$$

and every trajectory is equivalent up to a shift in phase. This is the Platonic oscillator: a metronome that never loses time, a pendulum with no air resistance and a pulse pushing it along at exactly the right rate, the imaginary clock we teach children to draw.

Uniform oscillators are rare in nature. Real oscillators — hearts, circuits, insect wings, orbiting bodies — deviate from perfect uniformity, sometimes subtly and sometimes drastically. The mathematically interesting question is what happens when the velocity along the circle is not constant, and in particular, when it nearly vanishes somewhere. That is where one-dimensional flows on a circle develop all their character.

### The Non-Uniform Oscillator

The canonical non-uniform oscillator is

$$\dot{\theta} = \omega - a\sin\theta,$$

with $\omega > 0$ and $a \geq 0$. The parameter $\omega$ sets a baseline drift rate; $a$ is an amplitude that speeds the oscillator up on one side of the circle and slows it down on the other. The equation is not just a toy: it is, up to rescaling, the overdamped pendulum driven by a constant torque, the Josephson junction in the resistive regime, and — as we will see — the phase equation for a weakly forced oscillator near threshold.

Three qualitatively different regimes appear as $a$ increases through $\omega$.

**Case 1: $a < \omega$.** The velocity $f(\theta) = \omega - a\sin\theta$ is bounded below by $\omega - a > 0$. It is positive everywhere, so $\theta$ rotates monotonically through $2\pi$. There are no fixed points. The oscillator keeps time, but not uniformly: it is fastest where $\sin\theta = -1$ (at $\theta = 3\pi/2$, where the restoring force aids the drift) and slowest where $\sin\theta = +1$ (at $\theta = \pi/2$, where the restoring force opposes it). The closer $a$ is to $\omega$, the more time the oscillator spends crawling through the slow region.

**Case 2: $a = \omega$.** The velocity touches zero at a single point, $\theta^* = \pi/2$. This is a half-stable fixed point (the signature saddle-node geometry from Section 3.3), and the oscillator can no longer complete its rotation: a trajectory approaches $\theta^*$ from the left and asymptotes to it in infinite time. The period has diverged to infinity. This is a bifurcation — a bifurcation *on* the invariant circle — and it has a standard name: **SNIC**, for *saddle-node on invariant circle*.

**Case 3: $a > \omega$.** The velocity now changes sign. Solving $\omega - a\sin\theta = 0$ gives two fixed points,

$$\theta_s = \arcsin(\omega/a), \qquad \theta_u = \pi - \arcsin(\omega/a),$$

a stable one (where $f'(\theta_s) = -a\cos\theta_s < 0$) and an unstable one (where $f'(\theta_u) > 0$). Every trajectory now converges to $\theta_s$. The oscillation is dead. The system has become bistable only in the topological sense — there is a single basin that covers all of $S^1$ except the unstable point.

```python
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 400)
omega = 1.0
fig, ax = plt.subplots(figsize=(7, 4))
for a, color, label in [(0.5, '#93C5FD', r'$a = 0.5 < \omega$ (rotating)'),
                         (1.0, '#D1B675', r'$a = 1.0 = \omega$ (SNIC)'),
                         (1.5, '#B91C1C', r'$a = 1.5 > \omega$ (locked)')]:
    ax.plot(theta, omega - a*np.sin(theta), color=color, lw=2, label=label)
ax.axhline(0, color='gray', ls='--', alpha=0.3)
ax.set(xlabel=r'$\theta$', ylabel=r'$\dot{\theta} = \omega - a\sin\theta$',
       title='Non-Uniform Oscillator: Three Regimes')
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
ax.legend(fontsize=9); plt.tight_layout(); plt.show()
```

The picture tells the whole story. The blue curve sits entirely above the axis — rotation. The gold curve kisses the axis at $\theta = \pi/2$ — the SNIC. The red curve dips below, producing a stable and an unstable fixed point — locking. The transition between rotation and locking is controlled by a single dimensionless ratio, $a/\omega$, which we will meet again in the discussion of entrainment below.

### Bottlenecks and the Ghost of a Saddle-Node

The most striking feature of the non-uniform oscillator is what happens to the period as $a$ approaches $\omega$ from below. The oscillation survives — no fixed point has appeared yet — but its period grows without bound. The system rotates more and more slowly not everywhere but *in a particular place*, near $\theta = \pi/2$, where the velocity is shrinking toward zero. This sluggish region is called a **bottleneck**, and it is the leading fingerprint of a nearby saddle-node bifurcation.

The period can be computed exactly. It is the time to traverse the circle once,

$$T = \oint \frac{d\theta}{\dot{\theta}} = \int_0^{2\pi} \frac{d\theta}{\omega - a\sin\theta}.$$

This integral is a classic of the subject and evaluates to

$$T = \frac{2\pi}{\sqrt{\omega^2 - a^2}},$$

valid whenever $\omega > a$. The result is remarkable. The period diverges as $a \to \omega^-$, and it does so with a specific scaling:

$$T \sim \frac{2\pi}{\sqrt{2\omega}} \, (\omega - a)^{-1/2}.$$

The inverse square root is the same exponent we saw in the saddle-node amplitude $|x^*| \sim \sqrt{|r|}$ in Section 3.3, and it is not a coincidence. Near the bifurcation, the dynamics in the bottleneck are governed by a local Taylor expansion whose normal form is $\dot{y} = \epsilon + y^2$ — the saddle-node. The time to flow through this region scales as the integral of $dy/(\epsilon + y^2)$, which gives $\pi/\sqrt{\epsilon}$. Every detail of the non-uniform oscillator drops out near threshold; the square-root divergence is universal.

```python
import numpy as np
import matplotlib.pyplot as plt

omega = 1.0
a_vals = np.linspace(0, 0.99, 200)
T = 2*np.pi / np.sqrt(omega**2 - a_vals**2)
T_asym = 2*np.pi / np.sqrt(2*omega * (omega - a_vals))

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(a_vals, T, color='#93C5FD', lw=2, label=r'$T = 2\pi/\sqrt{\omega^2 - a^2}$')
ax.plot(a_vals, T_asym, color='#D1B675', lw=1.5, ls='--',
        label=r'$T \sim (\omega - a)^{-1/2}$ asymptote')
ax.set(xlabel=r'$a/\omega$', ylabel='Period $T$',
       title='Period Divergence at the SNIC', ylim=(0, 50))
ax.legend(fontsize=9); plt.tight_layout(); plt.show()
```

A physicist would call the slow region the **ghost** of the saddle-node. The fixed point has not yet been born, but the system *feels* its coming arrival — it slows down as if something were tugging on it, and that tug grows stronger the closer the parameter creeps to threshold. The language is poetic but the mathematics is precise: the bottleneck is the residue of a collapsed geometry, the place where the phase portrait is remembering what it will become. This same phenomenon — slowing down near a bifurcation — will return in Chapter 7 as the basis for **early-warning signals**. When a complex system approaches a tipping point, it becomes more sluggish in recovering from perturbations. Critical slowing down is the ghost, promoted from a mathematical curiosity to an experimental diagnostic.

### Fireflies and Entrainment

The non-uniform oscillator's real importance comes from a physical scenario: one oscillator being driven, or coupled, to another. The canonical biological example is the synchronous firefly of Southeast Asia. Along the tidal rivers of Thailand and Malaysia, thousands of male fireflies (principally *Pteroptyx malaccae*) perch in the mangroves at dusk and flash in unison — whole trees pulsing once per second, entire riverbanks locking into step {cite}`buck1988synchronous`. Western entomologists spent decades insisting that the synchronization was an optical illusion caused by the observer blinking, or a coincidence of the fireflies all responding to the same sunset cue. It is neither. The insects are genuinely coupling to one another.

Hanson's 1978 experiments made the mechanism explicit. Put a single firefly in a jar, expose it to an artificial flash repeated at some period $T_{\text{stim}}$, and the firefly adjusts its own flashing frequency to match — provided the stimulus frequency is close enough to the firefly's natural rate. If the stimulus is too slow or too fast, the firefly reverts to its own rhythm but drifts through the stimulus, speeding up when the two are near-aligned and slowing down when they fall behind. This is precisely what the non-uniform oscillator describes, in the following way.

Let $\theta$ be the firefly's phase and $\Theta$ the stimulus phase. Define the phase difference $\psi = \theta - \Theta$. If the firefly's natural frequency is $\omega_f$, the stimulus frequency is $\omega_s$, and the coupling is sinusoidal with strength $A$, then

$$\dot\psi = (\omega_f - \omega_s) - A\sin\psi \equiv \Delta\omega - A\sin\psi.$$

This is our non-uniform oscillator, with $\psi$ playing the role of $\theta$, $\Delta\omega$ the role of $\omega$, and $A$ the role of $a$. The analysis transfers instantly:

- **$A > |\Delta\omega|$**: a fixed point $\psi^*$ exists. The firefly is **phase-locked** to the stimulus, maintaining a constant phase offset. This is entrainment. The firefly keeps the stimulus's time.
- **$A < |\Delta\omega|$**: no fixed point. The phase difference drifts monotonically. The firefly cannot keep up, and the two rhythms slide past each other with a period determined by the bottleneck integral.
- **$A = |\Delta\omega|$**: the SNIC. Entrainment appears or disappears via a saddle-node bifurcation, with the signature $T \sim (A - |\Delta\omega|)^{-1/2}$ divergence.

The locking band — the range of stimulus frequencies that the oscillator can match — is called an **Arnold tongue**, and its edges are SNIC bifurcations. A musician would call it locking in: two players find a tempo, and the groove takes over. A biologist calls it entrainment. Jet lag is what happens when the circadian pacemaker's $\Delta\omega$ is too large for the ambient light's coupling $A$ to overcome — the body drifts through the solar cycle until, day by day, the bottleneck narrows and the lock finally takes.

Pulse coupling, rather than sinusoidal coupling, gives rise to a richer theory worked out by Mirollo and Strogatz {cite}`mirollo1990synchronization`: an ensemble of $N$ integrate-and-fire oscillators with excitatory pulse coupling synchronizes from almost any initial condition, no matter how large $N$. The proof uses absorbing sets on the torus and a beautiful monotonicity argument. This is the one-dimensional tip of a much larger iceberg — the Kuramoto model of $N$ coupled phase oscillators, which occupies Chapter 10.

### Closing the Chapter

We set out at the start of Chapter 3 to read dynamics from the geometry of $f(x)$ alone. We did it on the line, classified the three canonical ways the picture could change as a parameter varied, understood how a small imperfection deforms a symmetric bifurcation into the cusp catastrophe, and finally bent the line into a circle — gaining oscillations for free and, with them, a new bifurcation and a universal period-divergence law.

One dimension is now genuinely exhausted. Every fixed point, every bifurcation, every periodic orbit attainable by a single first-order ODE has been catalogued. What we cannot get from one dimension is richness of *phase structure*: trajectories that spiral rather than march, limit cycles born from nowhere via a Hopf bifurcation, the interplay of two state variables that underlies every predator-prey model and every neuron. Chapter 4 opens the phase plane and releases these constraints. The tools we developed here — linearization, Taylor expansion around a fixed point, normal forms, the geometric eye — all survive the transition. What is added is a second degree of freedom, and with it, the real heart of dynamical systems theory.
