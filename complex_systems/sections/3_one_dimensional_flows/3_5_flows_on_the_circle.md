# Flows on the Circle

We proved in Section 3.1 that one-dimensional flows on the line cannot oscillate. The argument was topological: a trajectory moving rightward would have to reverse direction to return, and reversing direction requires passing through a point where the velocity is zero — a fixed point, from which it can never depart. The line is too simply connected. There is no room to turn around without getting stuck.

But the line is not the only one-dimensional state space. Bend it into a circle — identify $\theta$ with $\theta + 2\pi$ — and the obstruction dissolves. A trajectory moving "rightward" (increasing $\theta$) no longer escapes to infinity. It comes back. The state space is the same dimension, and the equation $\dot{\theta} = f(\theta)$ looks identical, but the topology is different, and the new topology admits a phenomenon the line forbids: **sustained oscillation**.

This is not a mathematical curiosity. Many of the most important variables in physics and biology are naturally angular. The phase of a pendulum, the angular position of a rotor, the firing phase of a neuron, the time within a 24-hour circadian cycle — all live on a circle, because they are periodic in kind. Christiaan Huygens, inventor of the pendulum clock, noticed in 1665 that two of his clocks hanging from a shared wooden beam would, after about half an hour, settle into exactly opposite swing — one left when the other went right. He called it "odd sympathy," and as far as anyone can tell he was the first person to write down that coupled oscillators synchronize. The state space was not the position of the pendulum bobs but the difference of their phases on a shared circle.

### Uniform Rotation

The simplest flow on $S^1$ is the uniform oscillator:

$$\dot{\theta} = \omega$$

The solution is $\theta(t) = \theta_0 + \omega t$, taken modulo $2\pi$. There are no fixed points — $\omega \neq 0$ everywhere — and the motion is periodic with period $T = 2\pi/\omega$. This is a limit cycle, although the word "limit" is strong for something this trivial: every trajectory is already the cycle, not merely approaching it. The circle itself is the attractor, and the dynamics on it are uniform angular drift.

```python
import numpy as np
import matplotlib.pyplot as plt

omega = 2.0
t = np.linspace(0, 4 * np.pi / omega, 600)
theta = omega * t

fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4))
a1.plot(np.cos(theta), np.sin(theta), color='#93C5FD', lw=1.8)
a1.plot(1, 0, 'o', color='#D1B675', ms=8)
a1.set_aspect('equal'); a1.set(xlabel='cos θ', ylabel='sin θ',
                                title='Trajectory on $S^1$')
a2.plot(t, np.sin(theta), color='#93C5FD', lw=1.5)
a2.set(xlabel='t', ylabel='sin θ(t)', title=f'Period T = 2π/ω = {2*np.pi/omega:.2f}')
plt.tight_layout(); plt.show()
```

The first panel shows the trajectory circling the unit circle at constant angular speed. The second projects the angular motion to a Cartesian coordinate, $\sin\theta(t)$, and we recover a pure sinusoid. Uniform rotation on the circle is the dynamical origin of every idealized oscillation in physics — the imaginary rotation of an electron, the hands of a clock, the phase of a steady-state AC current. The topology is doing the work the line could not.

### The Nonuniform Oscillator

Uniform rotation is too simple. Real oscillators slow in some parts of their cycle and hurry through others: a heart rests longer in diastole than systole, a pendulum swinging at large amplitude loiters near the top of its arc. To capture this, add a position-dependent brake:

$$\dot{\theta} = \omega - a\sin\theta$$

This is **Adler's equation**, which Robert Adler introduced in 1946 to describe the phase of an electronic oscillator being pulled by an injected signal {cite}`strogatz2015nonlinear`. It is deceptively general. Under surprisingly mild conditions, any weakly coupled pair of nearly identical oscillators reduces to this one-line equation for their phase difference. We will earn that claim at the end of this section.

Everything depends on the ratio $a/\omega$. Plot the velocity $f(\theta) = \omega - a\sin\theta$ and read off the fixed points.

**Case 1: $a < \omega$** (weak brake). The sine oscillates between $\pm 1$, so $f(\theta)$ ranges between $\omega - a > 0$ and $\omega + a > 0$. The velocity never vanishes — no fixed points. Every trajectory rotates indefinitely, but not uniformly: near $\theta = \pi/2$, where $\sin\theta = 1$, the oscillator slows to a crawl; near $\theta = 3\pi/2$, where $\sin\theta = -1$, it races through. A metronome laboring against an uneven load. A runner on a track with a headwind on the back straight. The geometry is right there in the curve.

We can compute the period exactly. The time to traverse a full cycle is

$$T = \oint \frac{d\theta}{\dot\theta} = \int_0^{2\pi} \frac{d\theta}{\omega - a\sin\theta}$$

This integral yields to the standard Weierstrass substitution $u = \tan(\theta/2)$, or more quickly to contour methods, with the result

$$\boxed{\;T = \frac{2\pi}{\sqrt{\omega^2 - a^2}}\;}$$

When $a = 0$ we recover $T = 2\pi/\omega$. As $a$ grows toward $\omega$, the denominator shrinks — the period grows — and at $a = \omega$, it diverges. The brake has become strong enough that the oscillator takes infinite time to pass through its slowest point.

**Case 2: $a > \omega$** (strong brake). Now $f(\theta) = \omega - a\sin\theta$ crosses zero. Fixed points exist where $\sin\theta = \omega/a$, giving two solutions in $[0, 2\pi)$:

$$\theta_1^* = \arcsin(\omega/a), \qquad \theta_2^* = \pi - \arcsin(\omega/a)$$

Linear stability follows from $f'(\theta) = -a\cos\theta$: at $\theta_1^*$, $\cos\theta > 0$ and $f' < 0$ (stable); at $\theta_2^*$, $\cos\theta < 0$ and $f' > 0$ (unstable). Every trajectory slides to $\theta_1^*$ and stops. The oscillation has been killed. In the injection-locking language of Adler's original paper, the oscillator has been **phase-locked** to the drive: its phase settles to a fixed offset and stays there.

```python
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 400)
omega = 1.0
fig, axes = plt.subplots(1, 3, figsize=(13, 3.5), sharey=True)
for ax, a, title in zip(axes, [0.6, 1.0, 1.4],
        [r'$a < \omega$: rotation', r'$a = \omega$: SNIC', r'$a > \omega$: phase-locked']):
    f = omega - a * np.sin(theta)
    ax.plot(theta, f, color='#93C5FD', lw=2)
    ax.axhline(0, color='gray', lw=0.8, ls=':')
    roots = np.where(np.diff(np.sign(f)))[0]
    for r in roots:
        ax.plot(theta[r], 0, 'o', color='#D1B675', ms=8)
    ax.set(title=title, xlabel=r'$\theta$',
           xticks=[0, np.pi, 2*np.pi], xticklabels=['0', 'π', '2π'])
axes[0].set_ylabel(r'$\dot\theta = \omega - a\sin\theta$')
plt.tight_layout(); plt.show()
```

The three panels record the qualitative progression. When $a < \omega$ the velocity curve sits entirely above zero and the oscillator rotates with a slow spot near $\theta = \pi/2$. When $a = \omega$ the curve just grazes zero at $\theta = \pi/2$ — a tangency — and we are on the knife-edge. When $a > \omega$ the curve cuts through zero twice and two fixed points are born, one stable, one unstable.

### The Saddle-Node on the Circle

The transition at $a = \omega$ is a bifurcation, and it is a special one. Two fixed points are born at $\theta^* = \pi/2$ — a saddle-node, exactly as in Section 3.3. But this saddle-node occurs *on a closed invariant orbit*, the circle itself. The limit cycle doesn't collide with anything external; it gets punctured from within. When the two fixed points appear, one of them chops the circle into a basin, trapping every trajectory.

This is the **saddle-node on an invariant circle**, or **SNIC**, bifurcation. It is also called the **infinite-period bifurcation**, for a reason we can already see: approach $a = \omega$ from below and the exact period formula gives

$$T = \frac{2\pi}{\sqrt{\omega^2 - a^2}} = \frac{2\pi}{\sqrt{(\omega - a)(\omega + a)}} \sim \frac{\text{const}}{\sqrt{\omega - a}} \quad \text{as } a \to \omega^-$$

The period doesn't just grow — it diverges with a square-root singularity. Set $\mu = \omega - a$; then $T \sim \mu^{-1/2}$.

Why the exponent $-1/2$? It is the signature of the bottleneck being crossed. Near $\theta = \pi/2$ and $a \approx \omega$, expand: $\sin\theta \approx 1 - \tfrac{1}{2}(\theta - \pi/2)^2$, so locally $\dot\theta \approx \mu + \tfrac{a}{2}(\theta - \pi/2)^2$. This is the saddle-node normal form of Section 3.3, $\dot u = \mu + u^2$, rescaled. The time to cross this local bottleneck is $\int d u / (\mu + u^2) = \pi/\sqrt{\mu}$ — up to constants, independent of the width of the initial and final intervals. As $\mu \to 0$ the bottleneck dominates the full cycle, and the entire period inherits its $\mu^{-1/2}$ divergence.

This square-root scaling is our first concrete example of a **critical exponent**. We already glimpsed one in Section 3.3 — $|x^*| \sim \sqrt{r}$ on the pitchfork's stable branch. The exponent $1/2$ will reappear, with the same origin, in critical slowing down near tipping points (Chapter 7) and in mean-field phase transitions (Chapter 13). The common denominator is a *quadratic tangency*: whenever a system is trying to do something that requires escaping a potential well with vanishing curvature, the relevant timescale or amplitude picks up a square root.

```python
import numpy as np
from scipy.integrate import solve_ivp

omega = 1.0
mus = np.logspace(-3, -0.2, 12)  # ω - a
periods = []
for mu in mus:
    a = omega - mu
    def cross_pi(t, theta): return theta[0] - 2*np.pi
    cross_pi.terminal = True
    sol = solve_ivp(lambda t, th: [omega - a*np.sin(th[0])],
                    [0, 500], [1e-4], events=cross_pi,
                    rtol=1e-10, atol=1e-12, max_step=0.01)
    periods.append(sol.t_events[0][0])

periods = np.array(periods)
exact = 2*np.pi / np.sqrt(omega**2 - (omega - mus)**2)
slope, _ = np.polyfit(np.log(mus[:6]), np.log(periods[:6]), 1)
print(f"Measured slope near criticality: {slope:.3f}  (theory: -0.500)")
# Measured slope near criticality: -0.500
```

Near the bifurcation the simulated period collapses onto $T \sim \mu^{-1/2}$ to four decimal places. The constant prefactor depends on the details of the oscillator; the exponent does not. That is what we mean by universality — the term the next chapter and Part IV are going to dwell on. The details of Adler's equation are particular; the $-1/2$ scaling is generic.

### From One Oscillator to Many

Adler's equation looks artificial — why a sine? — until you derive it from something more fundamental. Take two nearly identical oscillators, one with natural frequency $\omega_1$ and the other with $\omega_2$, coupled weakly. Strip away fast oscillation by working with slow phase variables $\theta_1, \theta_2$. The phase *difference* $\phi = \theta_1 - \theta_2$ obeys, to leading order,

$$\dot\phi = \Delta\omega - K\sin\phi$$

where $\Delta\omega = \omega_1 - \omega_2$ is the frequency mismatch and $K$ is the coupling strength. This is Adler's equation in disguise. Everything we just derived now has a direct interpretation. If $K < |\Delta\omega|$, the phase difference drifts forever — the oscillators are **unsynchronized**, each keeping its own time. If $K > |\Delta\omega|$, a stable fixed point appears at some phase offset $\phi^*$ — the oscillators are **phase-locked**, beating in sync with a constant lag. The transition between these regimes is a SNIC bifurcation, and the slow crossing through it near criticality is the source of the intermittent, stuttering synchronization one sees in real coupled oscillators as coupling is dialed up.

This is what Huygens's clocks were doing on their shared beam: tiny mechanical couplings through the wood pulled their phase difference into a stable attractor at $\phi^* = \pi$ — antiphase locking. It is what fireflies in the mangroves of Thailand are doing when a whole tree flashes as one, and what happened on London's Millennium Bridge on its opening day in June 2000, when the bridge swayed with the pedestrians' footfalls, which then synchronized to the sway, which grew, until the bridge had to be closed and retrofitted. One-dimensional flows on a circle, in unlikely numbers, coordinating.

We will return to the many-oscillator case in Chapter 10, where the Kuramoto model generalizes Adler's equation to $N$ oscillators coupled through a global mean-field — the canonical model of synchronization. The threshold phenomenon will still be there; it will simply have become a collective phase transition rather than a pairwise lock.

### What the Line and the Circle Can and Can't Do

The line and the circle are the only two connected one-dimensional manifolds. We have now mapped the dynamical possibilities on both. On the line: fixed points, basins of attraction, and three canonical bifurcations (saddle-node, transcritical, pitchfork) together with their imperfect cousins. On the circle: add uniform rotation, nonuniform oscillation, and the SNIC bifurcation. That is the complete catalogue. Oscillation is possible on the circle only because of its topology, not because of anything the equation $\dot x = f(x)$ knows.

Two dimensions will break this ceiling in a different way. Trajectories no longer have to lie on a prescribed loop to close — they can carve out their own closed orbits in the plane, and those orbits can be born and destroyed in a new kind of bifurcation, the Hopf, that has no analog in one dimension. The computational lab at the end of this chapter (Section 3.6) assembles the tools we have built so far into a working bifurcation-diagram pipeline. Then we cross into the plane.
