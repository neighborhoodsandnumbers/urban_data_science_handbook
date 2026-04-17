# Flows on the Circle

The days of the week form a circle. So does the phase of the moon, the hour on a clock, the angular position of a runner on a track, and the firing phase of a neuron between spikes. In each case, the state is an angular variable — a quantity that returns to itself after a full rotation. Angles are not points on the real line. They live on the circle $S^1$, and the difference between a line and a circle, though it sounds like a topological footnote, changes the dynamics in a way that matters.

In Section 3.1 we proved that one-dimensional flows on the line cannot oscillate. The reason was topological: a trajectory that tried to oscillate would have to reverse direction at some point, but reversing means passing through a point where $\dot x = 0$, which is a fixed point, which traps the trajectory there forever. The impossibility was not about the rule $\dot x = f(x)$; it was about the stage on which the dynamics unfolded. Change the stage — bend the line into a circle — and oscillations become not only possible but generic. A trajectory flowing always in the same angular direction wraps around and returns to where it started, having never once reversed itself. This chapter's promise that 1D flows could only converge or diverge was conditional on the state space being $\mathbb{R}$. On $S^1$, the rules change.

### The Circle as a State Space

A flow on the circle is governed by the same-looking equation as before:

$$\dot{\theta} = f(\theta)$$

with one crucial modification: $\theta$ and $\theta + 2\pi$ are the *same point*. The state space is not $\mathbb{R}$ but $\mathbb{R}/2\pi\mathbb{Z}$ — the real line with every pair of points differing by a full rotation identified. Geometrically, it is a circle of circumference $2\pi$. For the dynamics to be consistent with this identification, the velocity function $f$ must also respect it:

$$f(\theta + 2\pi) = f(\theta)$$

In other words, $f$ must be $2\pi$-periodic. A function that isn't periodic cannot define a vector field on the circle, because the "velocity at $\theta$" would be different from the "velocity at $\theta + 2\pi$" — two values at the same point.

Every other tool from the previous sections still applies. Fixed points are solutions of $f(\theta^*) = 0$. Linear stability is determined by $f'(\theta^*)$: negative means stable, positive means unstable, zero is degenerate. Phase portraits are read from the sign of $f$ between fixed points. The only thing that has changed — but it has changed everything — is that the two "ends" of the interval are glued together.

### The Uniform Oscillator

The simplest possible flow on the circle is

$$\dot{\theta} = \omega$$

with $\omega$ a positive constant. No fixed points (the velocity is never zero), constant angular speed, and solution $\theta(t) = \theta_0 + \omega t \pmod{2\pi}$. This is a **uniform oscillator**: it rotates around the circle at constant angular velocity $\omega$, completing one full revolution every $T = 2\pi/\omega$ units of time. On the real line, the same equation would describe unbounded drift to infinity. On the circle, it describes a periodic orbit.

This is the first genuine oscillation in this book. No differential equation on the real line can produce one. The minute hand of a clock, the rotation of the Earth, the rhythmic discharge of a pacemaker neuron between spikes — these are all instances of the same one-line equation, interpreted on $S^1$.

But a uniform oscillator is a bit boring. It has no room to respond to a perturbation, to slow down or speed up. A real oscillator — a biological clock, a mechanical rotor, a driven pendulum — has internal dynamics that modulate its angular speed. The interesting case is the non-uniform oscillator.

### The Non-Uniform Oscillator

Consider

$$\dot{\theta} = \omega - a \sin\theta$$

with $\omega > 0$ and $a \geq 0$. This is the **Adler equation**, first derived in the 1940s as a model for phase-locking in radio-frequency oscillators and subsequently found to describe an astonishing range of systems: Josephson junctions in superconductors, injection-locked lasers, charge density waves, and the firing of certain neurons. What it captures, stripped to essentials, is the competition between an intrinsic tendency to rotate (rate $\omega$) and a position-dependent force that pulls the phase toward a preferred value. The parameter $a$ is the strength of that force.

Three qualitatively different regimes emerge as $a$ crosses $\omega$.

**$a < \omega$ (the oscillating regime).** The restoring term $a\sin\theta$ can never fully cancel $\omega$ — at worst it subtracts $a$ from it, and $\omega - a > 0$. The angular velocity is always positive, so $\theta$ keeps winding around the circle. There are no fixed points. But the motion is *non-uniform*: near $\theta = \pi/2$, where $\sin\theta = 1$, the velocity drops to $\omega - a$, a small positive number; near $\theta = 3\pi/2$, where $\sin\theta = -1$, the velocity peaks at $\omega + a$. The oscillator speeds and slows as it goes around, spending disproportionately long in the region near $\theta = \pi/2$.

**$a > \omega$ (the phase-locked regime).** Now the restoring force is strong enough to halt rotation somewhere. Setting $\dot\theta = 0$ gives $\sin\theta^* = \omega/a$, and since $|\omega/a| < 1$, this equation has two solutions on the circle:

$$\theta_1^* = \arcsin(\omega/a), \qquad \theta_2^* = \pi - \arcsin(\omega/a)$$

Stability follows from $f'(\theta) = -a\cos\theta$. At $\theta_1^*$ (first quadrant), $\cos\theta_1^* > 0$, so $f' < 0$ — **stable**. At $\theta_2^*$ (second quadrant), $\cos\theta_2^* < 0$, so $f' > 0$ — **unstable**. The stable fixed point attracts all trajectories; the unstable one is the basin boundary. The oscillator no longer rotates. It has **locked** to a fixed phase relative to whatever is driving $a\sin\theta$ — this is the essence of phase-locking.

**$a = \omega$ (the bifurcation).** At the knife-edge value, $\sin\theta^* = 1$ has the unique solution $\theta^* = \pi/2$. Linear stability is inconclusive: $f'(\pi/2) = -a\cos(\pi/2) = 0$. Expanding to second order, $f(\pi/2 + \delta) = \omega - a\cos\delta \approx \omega - a + (a/2)\delta^2$, which at $a = \omega$ reduces to $\dot\delta \approx (a/2)\delta^2$. The fixed point is half-stable — attracting from one side, repelling from the other — which is exactly the saddle-node normal form from Section 3.3, now playing out on a circle. The two fixed points that exist for $a > \omega$ have collided at $a = \omega$ and disappeared; for $a < \omega$ they are gone, and the trajectory flows freely around the loop.

```python
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 400)
omega = 1.0

fig, ax = plt.subplots(figsize=(7.5, 4.5))
for a, color, label in [(0.5, '#93C5FD', r'$a = 0.5 < \omega$ (oscillating)'),
                         (1.0, '#D1B675', r'$a = 1.0 = \omega$ (bifurcation)'),
                         (1.5, '#B91C1C', r'$a = 1.5 > \omega$ (locked)')]:
    f = omega - a * np.sin(theta)
    ax.plot(theta, f, color=color, lw=2, label=label)
    if a > omega:
        th_stable = np.arcsin(omega / a)
        th_unstable = np.pi - th_stable
        ax.plot(th_stable, 0, 'o', color=color, ms=8)            # stable
        ax.plot(th_unstable, 0, 'o', color=color, ms=8,
                mfc='none', mew=2)                                # unstable
    elif a == omega:
        ax.plot(np.pi/2, 0, 's', color=color, ms=8)               # half-stable
ax.axhline(0, color='gray', ls='--', alpha=0.3)
ax.set(xlabel=r'$\theta$', ylabel=r'$\dot{\theta} = \omega - a\sin\theta$',
       title='The Adler Equation on the Circle',
       xticks=[0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
       xticklabels=['$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
ax.legend(fontsize=9, loc='lower right'); plt.tight_layout(); plt.show()
```

The three curves show $\dot\theta(\theta)$ as $a$ crosses $\omega$. For $a = 0.5$ (blue), the curve never touches zero: the oscillator keeps rotating, though unevenly. For $a = 1.5$ (red), the curve dips below zero between two zeros on the $\theta$-axis: a stable fixed point (filled) and an unstable one (open) trap every trajectory. For $a = 1$ (gold), the curve just grazes zero at $\theta = \pi/2$ — the two fixed points have merged into a half-stable point about to vanish. This is the **saddle-node on an invariant circle** (SNIC) bifurcation, and it is genuinely new: the saddle-node from Section 3.3 lived on the line and could annihilate the system's equilibria entirely; the saddle-node on a circle destroys the equilibria and replaces them with a limit cycle, because the topology forces the freed trajectory to wrap around.

### The Period of Oscillation

For $a < \omega$, the oscillator goes around, but not at constant speed. How long does one revolution take?

The time to traverse an infinitesimal arc $d\theta$ at angular speed $\dot\theta$ is $dt = d\theta/\dot\theta$. Summing over a full revolution gives the period:

$$T = \oint \frac{d\theta}{\dot\theta} = \int_0^{2\pi} \frac{d\theta}{\omega - a\sin\theta}$$

This is a textbook improper integral — "improper" in the technical sense because the integrand is a ratio on a closed interval (not that it diverges, for $a < \omega$). The standard tool is the **Weierstrass substitution** $u = \tan(\theta/2)$, which converts trigonometric integrals to rational ones. After substitution and some algebra, the integral evaluates cleanly to

$$T = \frac{2\pi}{\sqrt{\omega^2 - a^2}}$$

This compact formula packs in the whole story. When $a = 0$, we recover the uniform oscillator's period $2\pi/\omega$. As $a$ approaches $\omega$ from below, the denominator shrinks toward zero and $T \to \infty$ — the oscillator grinds to a halt just as the saddle-node is about to appear. The closer $a$ gets to the threshold, the longer each cycle takes.

```python
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

omega = 1.0
a_vals = np.linspace(0, 0.98, 200)

# Compute period two ways: numerical integration and closed form
T_numerical = [quad(lambda th: 1.0 / (omega - a * np.sin(th)), 0, 2*np.pi)[0]
               for a in a_vals]
T_closed = 2 * np.pi / np.sqrt(omega**2 - a_vals**2)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(a_vals, T_numerical, 'o', color='#93C5FD', ms=3,
        label='numerical integration')
ax.plot(a_vals, T_closed, '-', color='#D1B675', lw=2,
        label=r'$T = 2\pi/\sqrt{\omega^2 - a^2}$')
ax.axvline(omega, color='#B91C1C', ls=':', lw=1.5, label=r'$a = \omega$ (SNIC)')
ax.set(xlabel=r'coupling $a$', ylabel='period $T$',
       title=r'Oscillation Period of the Adler Equation ($\omega = 1$)',
       ylim=(0, 40))
ax.legend(fontsize=9); plt.tight_layout(); plt.show()
```

Two methods — `scipy.integrate.quad` on the defining integral, and the closed-form result from the Weierstrass substitution — agree to within numerical precision, as they must. The striking feature is the vertical asymptote. The period grows like $(\omega - a)^{-1/2}$ as the coupling approaches its critical value: a **square-root divergence**, the same scaling that will reappear in Section 3.3's saddle-node normal form and again in the critical exponents of Chapter 13. The exponent $1/2$ is not a coincidence. It is the signature of the saddle-node bifurcation, visible through the lens of this particular observable (the period).

The physical intuition is the **bottleneck**. For $a$ just below $\omega$, the velocity function $\omega - a\sin\theta$ is positive everywhere but nearly zero near $\theta = \pi/2$ — the "ghost" of the impending fixed point. The oscillator sprints through most of the circle and then crawls through a narrow region near $\pi/2$, where it is almost (but not quite) stuck. As $a \to \omega^-$, the crawl dominates and the total time diverges. A trajectory looking at its own behavior near $\pi/2$ would be indistinguishable from one approaching a fixed point — until, eventually, it breaks through and races around the rest of the loop. **Critical slowing down** near a saddle-node bifurcation will reappear in Chapter 7 as a core **early warning signal** for tipping points in ecological and climate systems. Here it shows up in its cleanest possible form: a single-line equation on a circle.

### Phase-Locking

The Adler equation's bifurcation describes one of the most common phenomena in nonlinear physics: **phase-locking**, where an oscillator's natural rhythm is entrained by a periodic forcing. Read the equation as follows. The phase $\theta$ is the *difference* between the oscillator's own phase and the driver's phase, rotating at some detuning rate $\omega$. The term $-a\sin\theta$ is the coupling — it tries to pull the phase difference toward a preferred value. When the coupling is strong enough ($a > \omega$), the phase difference locks to a constant: the oscillator runs in exact synchrony with the driver, adjusted by a fixed phase lag $\arcsin(\omega/a)$. When the coupling is too weak ($a < \omega$), the phase difference drifts around the circle, slowly near $\pi/2$ and quickly near $3\pi/2$ — the oscillator and the driver have almost the same frequency but never quite lock, so they slip by one cycle every $T = 2\pi/\sqrt{\omega^2 - a^2}$ units of time. This "beat frequency" is directly observable in laboratory systems.

Every term in that paragraph corresponds to a real measurement in real hardware. Josephson junctions — quantum-mechanical devices used in SQUID magnetometers and superconducting qubits — obey the Adler equation exactly, with $\theta$ the phase difference of the superconducting order parameter across the junction, $\omega$ set by the applied voltage, and $a$ by the critical current. The SNIC bifurcation shows up as a sharp transition in the current-voltage curve. In neuroscience, certain neurons near their spiking threshold follow dynamics that are well approximated by the Adler equation, and the SNIC bifurcation is one of the canonical mechanisms by which a neuron begins to fire repetitively — with the characteristic property that the firing rate starts not at some finite value but arbitrarily slowly, growing as $\sqrt{I - I_c}$ above the threshold current. And Strogatz's beloved fireflies, whose flashing synchronizes across a mangrove swamp, phase-lock through a mechanism that on a single-firefly level looks very much like the Adler equation {cite}`strogatz2015nonlinear`.

These are not variations on a theme. They are instances of the same theme, revealed by the universality of normal forms. The saddle-node on an invariant circle is to oscillators what the saddle-node on the line is to equilibria: the generic codimension-one way that periodic motion is created or destroyed.

### The Ceiling of One Dimension

We now have the full qualitative picture of one-dimensional flows. On the line, the only long-term behaviors are convergence to a fixed point or escape to infinity. On the circle, a third possibility opens up: rotation around the loop, either at constant speed or bottlenecked through a ghost. Three canonical bifurcations (saddle-node, transcritical, pitchfork) govern qualitative change on the line; one additional canonical bifurcation (the SNIC) lives on the circle, where it connects equilibrium to rotation.

But even the richest one-dimensional flow is still deeply limited. The Adler equation's oscillation is pure phase: the state is an angle, and nothing else. There is no notion of amplitude, no trajectory that can overshoot or ring, no possibility of the oscillation being *born* continuously out of a resting state with amplitude growing smoothly from zero. Real oscillators have both phase and amplitude. A pendulum swings wider when you give it more energy; a laser's output grows continuously as you crank the gain; a heartbeat has a characteristic amplitude that the body actively regulates. To capture these, we need two dimensions. In the plane, trajectories can spiral outward, converge to a closed orbit, or pass around each other without crashing into fixed points. The analogue of the SNIC becomes the **Hopf bifurcation** — an equilibrium that spawns a small-amplitude oscillation growing continuously out of itself — and the generic picture of oscillation shifts from "driven and locked" to "self-sustaining and autonomous." That is the subject of Chapter 4.
