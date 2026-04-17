# Flows on the Circle

In Section 3.1 we proved a theorem that seemed to close the book on one-dimensional dynamics: a trajectory on the real line cannot oscillate. It can only drift toward a fixed point or escape to infinity. The argument was topological — a trajectory trying to cycle would have to pass through the same point twice with different velocities, contradicting the fact that $\dot{x} = f(x)$ assigns a single velocity to each $x$.

Now we loosen one assumption and watch the conclusion collapse. Suppose the state space is not the real line but a **circle**, $S^1$, parameterized by an angle $\theta$ with $\theta$ and $\theta + 2\pi$ identified as the same point. The vector field is still a single-valued function, $\dot{\theta} = f(\theta)$, but now a trajectory that keeps moving in one direction will eventually return to where it started. Recurrence becomes possible. Oscillations become possible. "In my end is my beginning," wrote T. S. Eliot, and the geometry of the circle is his four words made topology.

This innocent-looking change — bend the line until its ends meet — is the minimal modification of the real line that produces genuine oscillation without requiring a second dimension. The study of flows on $S^1$ is therefore the bridge from Chapter 3 to Chapter 4, and the phenomena we discover here (phase locking, critical slowing near a bifurcation, entrainment to an external drive) will reappear in richer form when we move to two dimensions and the Kuramoto model in Chapter 10.

### The Uniform Oscillator

The simplest flow on the circle is the one with no fixed points at all:

$$\dot{\theta} = \omega$$

with $\omega > 0$ a constant angular velocity. The trajectory is $\theta(t) = \theta_0 + \omega t \pmod{2\pi}$ — a point moving around the circle at uniform speed. The period of a full revolution is

$$T = \frac{2\pi}{\omega}.$$

This is the mathematical idealization of a perfect clock, and it is almost too simple to be interesting. There is no fixed point. There is no asymmetry. Every point on the circle is equivalent to every other, and the dynamics are invariant under the rotation $\theta \to \theta + \phi$ for any $\phi$. But the uniform oscillator sets the baseline: it is the reference against which all non-uniform oscillators are compared, and the rotation symmetry it possesses is the symmetry that will be *broken* by almost any perturbation — much as the odd symmetry of $\dot{x} = rx - x^3$ was the symmetry broken by the imperfection parameter in Section 3.4.

### The Non-Uniform Oscillator

The next level of complication is

$$\dot{\theta} = \omega - a \sin\theta$$

which we will call the **non-uniform oscillator** (it goes by several names in the literature — Adler's equation in radio engineering, the overdamped Josephson junction in solid-state physics, the overdamped pendulum with constant torque in mechanics). All three applications reduce to the same normal form. The parameter $\omega$ is the driving rate; $a$ is the strength of a sinusoidal obstacle that speeds the trajectory up on half the circle and slows it down on the other half.

The behavior depends on the ratio $|a|/\omega$, which measures how much of an obstacle the sine is compared to the drive.

**Regime 1: $\omega > a > 0$ (drift).** The right-hand side $\omega - a\sin\theta$ is everywhere positive — it reaches its minimum $\omega - a > 0$ at $\theta = \pi/2$ and its maximum $\omega + a$ at $\theta = 3\pi/2$. There are no fixed points. The trajectory moves around the circle indefinitely, but with variable speed: it crawls through the "slow region" near $\theta = \pi/2$ and sprints through the "fast region" near $\theta = 3\pi/2$. This is oscillation — genuine, periodic, recurrent — in a one-dimensional system. The no-oscillation theorem of Section 3.1 does not apply here because the state space is not the line.

**Regime 2: $a > \omega > 0$ (phase locking).** Now the sine function is strong enough to overcome the drive at some point. The equation $\omega = a\sin\theta$ has two solutions in $[0, 2\pi)$: a stable fixed point $\theta_s = \arcsin(\omega/a)$ and an unstable fixed point $\theta_u = \pi - \arcsin(\omega/a)$. (Check by computing $f'(\theta) = -a\cos\theta$: at $\theta_s$, where $\cos\theta > 0$, we get $f' < 0$ — stable. At $\theta_u$, where $\cos\theta < 0$, we get $f' > 0$ — unstable.) The drive is no longer strong enough to push the trajectory past the obstacle. Instead, trajectories slide to $\theta_s$ and freeze there. The oscillator has been **phase-locked** to the external influence. Strobe the Josephson junction with a microwave and watch its voltage lock to a rational multiple of the drive. Couple two clocks through a common beam and watch them synchronize.

**The boundary: $a = \omega$ (bifurcation).** At this critical value, $\omega - a\sin\theta$ has a single zero at $\theta = \pi/2$ where the function touches zero without crossing: $f(\pi/2) = 0$ and $f'(\pi/2) = 0$, but $f''(\pi/2) = a > 0$. This is a half-stable fixed point — exactly the signature of a saddle-node bifurcation from Section 3.3. But now the saddle-node occurs *on the circle*, where the flow has nowhere else to go. As $a$ decreases below $\omega$, the fixed points vanish and the trajectory, which had been stuck near $\theta = \pi/2$, resumes its journey around the loop.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

omega = 1.0
theta = np.linspace(0, 2*np.pi, 400)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Left: vector field f(theta) for three regimes
for a, color, label in [(0.5, '#93C5FD', r'$a = 0.5$ (drift)'),
                         (1.0, '#D1B675', r'$a = 1.0$ (bifurcation)'),
                         (1.5, '#B91C1C', r'$a = 1.5$ (phase-locked)')]:
    axes[0].plot(theta, omega - a*np.sin(theta), color=color, lw=2, label=label)
axes[0].axhline(0, color='gray', ls=':', alpha=0.5)
axes[0].set(xlabel=r'$\theta$', ylabel=r'$\dot{\theta} = \omega - a\sin\theta$',
            title='Vector field on $S^1$', xlim=(0, 2*np.pi))
axes[0].legend(fontsize=9)

# Right: trajectories theta(t) showing oscillation, slowing, and locking
for a, color in [(0.5, '#93C5FD'), (0.95, '#D1B675'), (1.5, '#B91C1C')]:
    sol = solve_ivp(lambda t, th: omega - a*np.sin(th),
                    [0, 40], [0.1], dense_output=True, rtol=1e-10)
    t = np.linspace(0, 40, 800)
    axes[1].plot(t, sol.sol(t)[0] / np.pi, color=color, lw=1.8,
                 label=fr'$a = {a}$')
axes[1].set(xlabel='$t$', ylabel=r'$\theta(t) / \pi$',
            title='Trajectories: drift, slowing, locking')
axes[1].legend(fontsize=9)
plt.tight_layout(); plt.show()
```

The left panel plots the velocity function for three values of $a$ with $\omega = 1$ fixed. The blue curve stays above zero everywhere — pure drift. The red curve dips below zero, intersecting the axis at two fixed points. The gold curve is the knife-edge: it just touches zero at $\theta = \pi/2$. The right panel shows what these look like as trajectories. The blue case climbs steadily (with visible speed variation). The gold case climbs, then hesitates near $\theta = \pi/2$, then continues — a single ghostly pause at the vanished fixed point. The red case climbs to $\theta_s = \arcsin(1/1.5) \approx 0.73$ and stops.

### The Period and Critical Slowing

How long does a revolution take in the drift regime $\omega > a$? The period is computed by the **improper integral**

$$T = \oint \frac{d\theta}{\dot{\theta}} = \int_0^{2\pi} \frac{d\theta}{\omega - a\sin\theta}.$$

This is a standard integral — evaluated by the Weierstrass substitution $u = \tan(\theta/2)$, which converts the trigonometric integrand into a rational one. The result is

$$T = \frac{2\pi}{\sqrt{\omega^2 - a^2}}.$$

Two limits are instructive. For $a = 0$, we recover $T = 2\pi/\omega$ — the uniform oscillator. For $a \to \omega$ from below, the period diverges as

$$T \sim \frac{2\pi}{\sqrt{2\omega(\omega - a)}} \propto \frac{1}{\sqrt{\omega - a}}.$$

The exponent $-1/2$ is not incidental. It is the same square-root scaling we encountered in Section 3.3 for the position of a saddle-node fixed point, now appearing in the *period* of an oscillation near a saddle-node on the circle. The oscillator spends almost all of its cycle crawling through the "ghost" of the bifurcation point — the narrow bottleneck near $\theta = \pi/2$ where the velocity is nearly zero. This phenomenon, called **critical slowing down** or the **bottleneck effect**, is a universal signature of a saddle-node-type bifurcation approached from either side. We will encounter it again as an early-warning signal for tipping points in Chapter 7 and in the theory of critical phenomena in Chapter 13. A square-root divergence that keeps showing up in unrelated-looking contexts is a clue that the same normal form is at work underneath. That is the universality story from Section 3.3, continued.

```python
import numpy as np
import matplotlib.pyplot as plt

omega = 1.0
a_vals = np.linspace(0, 0.99, 200)
T_exact = 2*np.pi / np.sqrt(omega**2 - a_vals**2)
T_asymp = 2*np.pi / np.sqrt(2*omega*(omega - a_vals))

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(a_vals, T_exact, color='#93C5FD', lw=2.2, label=r'$T = 2\pi/\sqrt{\omega^2 - a^2}$')
ax.plot(a_vals, T_asymp, '--', color='#D1B675', lw=1.6,
        label=r'asymptotic $\propto (\omega - a)^{-1/2}$')
ax.axhline(2*np.pi, color='gray', ls=':', alpha=0.4)
ax.text(0.02, 2*np.pi + 0.3, r'uniform oscillator: $T = 2\pi/\omega$',
        fontsize=9, color='gray')
ax.set(xlabel='$a$ (with $\omega = 1$ fixed)', ylabel='Period $T$',
       title='Critical Slowing Near the SNIC Bifurcation', ylim=(0, 30))
ax.legend(fontsize=9); plt.tight_layout(); plt.show()
```

The blue curve is the exact period; the gold dashed curve is the asymptotic approximation. The two agree closely as $a \to \omega$, confirming that the divergence is square-root. A trajectory that used to complete a cycle in about $2\pi$ time units takes over thirty as the bifurcation is approached — the oscillator is stalling out, caught in the gravitational pull of the ghost fixed point that is about to be born.

### The Saddle-Node on the Invariant Circle

The bifurcation at $a = \omega$ has a name: it is a **saddle-node on the invariant circle**, abbreviated SNIC. The adjective "invariant" refers to the fact that the circle is an invariant set of the flow — trajectories live on it and cannot leave it — and the saddle-node appears on this circle rather than in an ambient phase plane. When the SNIC happens, a pair of fixed points (stable + unstable) is born from the oscillation and the oscillation ceases. Running the parameter in reverse, a saddle-node collision produces an infinite-period oscillation.

The SNIC is one of the three ways a limit cycle can be destroyed in a two-dimensional flow, the other two being the supercritical Hopf bifurcation (Chapter 4, Section 4.4), where the cycle shrinks to a point, and homoclinic collision, where the cycle crashes into a saddle. Each of the three has a different fingerprint in the period: Hopf gives a finite period at destruction, homoclinic gives a logarithmic divergence, SNIC gives the $1/\sqrt{}$ divergence we just computed. An experimentalist who measures how the period diverges as a parameter is tuned can distinguish these bifurcations without ever observing the phase space directly. Universality, in other words, is not just an organizing principle — it is an inference tool.

### Synchronization: Huygens, Josephson, and the Fireflies of Southeast Asia

In February of 1665, the Dutch physicist Christiaan Huygens, confined to bed by illness and surrounded by his newly invented pendulum clocks, noticed that two clocks hung from the same wooden beam settled into perfect anti-phase oscillation within half an hour, regardless of how they were started. He called it the "odd kind of sympathy." What he had discovered, in modern language, was a phase-locked solution of a system of two weakly coupled oscillators — the simplest case of the non-uniform oscillator with the "drive" supplied by a neighboring clock through vibrations in the beam.

A single firefly species in the mangrove forests of Thailand and Malaysia — *Pteroptyx malaccae* — synchronizes its flashing across entire trees, sometimes whole riverbanks. Each male has his own natural flashing frequency $\omega_i$; he observes his neighbor's flashes and nudges his own phase slightly faster or slower depending on when the neighbor lit up. Model the phase of the $i$-th firefly by $\theta_i$ and the aggregate influence by a sinusoid:

$$\dot{\theta}_i = \omega_i + K \sin(\bar{\theta} - \theta_i)$$

where $\bar{\theta}$ is a population-averaged phase and $K$ is the coupling strength. For a single firefly forced by an external drive, this is exactly the non-uniform oscillator — rewrite $\dot{\theta} = \omega - K\sin(\theta - \bar{\theta})$ and absorb the shift. For the entire swarm, you get the Kuramoto model, which we will study in Chapter 10. The transition from unsynchronized to synchronized as $K$ crosses a critical value is a population-level analogue of the phase-locking bifurcation we have just analyzed for a single oscillator.

The Josephson junction is the most precisely measured example of the non-uniform oscillator in physics. In a superconducting loop interrupted by a thin insulating barrier, the phase difference $\phi$ of the superconducting wave function obeys $\dot{\phi} \propto V - V_c \sin\phi$, where $V$ is an applied voltage. The phase-locking plateaus ("Shapiro steps") observed in Josephson junction experiments were used, until recently, to define the international volt. A pure mathematical structure — the non-uniform oscillator and its SNIC — underwrites a metrological standard.

### What We Have and What Is Missing

Bending the line into a circle restored oscillations. A single first-order ODE $\dot{\theta} = f(\theta)$ on $S^1$ can have fixed points and can have rotations, and the transition between the two is a saddle-node bifurcation that produces the characteristic $1/\sqrt{}$ divergence of the period. This is a real gain: we now have access to sustained periodic motion without leaving one dimension.

But the oscillations we have found are, in a precise sense, *inherited* from the topology rather than generated by the dynamics. The period is fixed by the parameters; perturb the initial condition and you return to exactly the same cycle (because there is only one cycle — the entire circle). There is no amplitude to decay or grow. There is no asymptotic attraction of a neighboring trajectory toward a cycle embedded in a larger space. For that — for **limit cycles**, oscillations that exist as isolated attractors in an open state space — we need two dimensions. That is the subject of Chapter 4, which opens the geometry of the phase plane, classifies its fixed points by trace and determinant, and then discovers the genuinely two-dimensional phenomenon of a closed orbit surrounded by spiraling neighbors. Everything we have learned in Chapter 3 — phase portraits, linear stability, bifurcations, the ghost of a fixed point — will carry over. What changes is that the trajectories now have room to turn {cite}`strogatz2015nonlinear`.
