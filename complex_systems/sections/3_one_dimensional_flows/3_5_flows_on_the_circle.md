# Flows on the Circle

The previous four sections built a complete analytic toolkit for $\dot{x} = f(x)$ on the real line, and the conclusion was a constraint: on the line, the only long-term behaviors are convergence to a fixed point or escape to infinity. No cycles, no sustained oscillation, nothing that returns. This is a theorem about topology masquerading as a theorem about dynamics — a trajectory on $\mathbb{R}$ cannot reverse direction without passing through a zero of $f$, and once it arrives at a zero it stays there forever.

Change the topology and the verdict changes. Take the real line, bend it, and glue its ends together at $\theta = 0 \sim 2\pi$. We now live on the circle $S^1$. A trajectory moving at constant positive velocity no longer escapes to infinity — it wraps around and returns to its starting point. Oscillation, which was impossible on the line, becomes the *generic* behavior on the circle. Eliot called this "in my beginning is my end." The circle is what it means for a one-dimensional state to have nowhere to run.

This is not a mathematical curiosity. Angles are genuine state variables in a great many systems: the phase of an oscillator, the orientation of a compass needle, the argument of a complex amplitude, the position of a point on a closed track. The equations governing them live naturally on $S^1$, and as we will see, a remarkably small set of normal forms captures the dynamics of phase-locking, rhythm, and synchronization across physics, biology, and engineering.

### The Circle as a State Space

A dynamical system on the circle is an ODE

$$\dot{\theta} = f(\theta)$$

with the single requirement that $f$ be $2\pi$-periodic: $f(\theta + 2\pi) = f(\theta)$. Without periodicity, the velocity at $\theta = 2\pi^{-}$ would not match the velocity at $\theta = 0^+$ after identification, and the flow would be discontinuous at the seam. The periodicity condition is geometry talking: the manifold has no seam, so the vector field can't either.

Everything from Section 3.2 still applies *locally*. Fixed points are zeros of $f$; stability is governed by the sign of $f'(\theta^*)$; trajectories between fixed points are still monotone. What is new is the possibility that *no* fixed point exists. On $\mathbb{R}$, a velocity field with no zeros sends trajectories to infinity. On $S^1$, a velocity field with no zeros sends trajectories around and around forever — a periodic orbit.

The simplest example is **uniform rotation**:

$$\dot{\theta} = \omega, \qquad \omega > 0$$

This is the prototype of every phase oscillator in the book. The solution is $\theta(t) = \theta_0 + \omega t \pmod{2\pi}$, and the period is $T = 2\pi/\omega$. A metronome, a quartz crystal, an idealized heartbeat, the pendulum of a grandfather clock with its escapement compensating for friction — all are approximations of $\dot{\theta} = \omega$, and this modest equation will reappear in Chapter 10 as one oscillator in the Kuramoto ensemble and in Chapter 16 as a model of biological clocks.

### The Non-Uniform Oscillator

Uniform rotation is too simple to show us anything new. The equation that opens the door is the **non-uniform oscillator**,

$$\dot{\theta} = \omega - a\sin\theta, \qquad \omega, a > 0$$

which introduces a single $2\pi$-periodic perturbation to the baseline rotation. The behavior depends sharply on whether $a$ is smaller or larger than $\omega$.

**Case $a < \omega$.** The velocity $\omega - a\sin\theta$ is everywhere positive — it cannot vanish, because the perturbation is too weak to cancel the baseline. The system rotates around the circle forever, but non-uniformly. It moves slowly near $\theta = \pi/2$, where $\sin\theta = 1$ subtracts most from the velocity, and quickly near $\theta = 3\pi/2$, where $\sin\theta = -1$ adds to it. The rhythm is intact, but the beats are uneven.

**Case $a > \omega$.** Now the perturbation dominates: the velocity changes sign, so zeros exist. Setting $\omega - a\sin\theta = 0$ gives $\sin\theta^* = \omega/a$, which has two solutions per period — one in the first quadrant (with $\cos\theta^* > 0$) and one in the second (with $\cos\theta^* < 0$). Computing $f'(\theta^*) = -a\cos\theta^*$: the first is stable, the second unstable. Every trajectory converges to the stable one. The system no longer rotates; it is **phase-locked** to a particular angle on the circle.

**The borderline, $a = \omega$.** The two fixed points have merged into a single half-stable point at $\theta^* = \pi/2$ — where $\sin\theta = 1$ exactly cancels the baseline rotation. A trajectory approaching from below is attracted; a trajectory approaching from above is repelled and must loop all the way around the circle before returning. This is a saddle-node bifurcation, but occurring on a closed invariant curve — the **saddle-node on an invariant circle**, or **SNIC** bifurcation. The geometry matters: the two fixed points are born on the circle, split it into two flow regions, and as $a$ decreases back through $\omega$ they collide again and the circle becomes one connected flow, restoring rotation.

The SNIC is qualitatively different from the saddle-node on the line (Section 3.3). On the line, after the fixed points vanish, trajectories escape to infinity. On the circle, after the fixed points vanish, trajectories rotate — a periodic orbit appears out of nothing, inherited from the topology of the state space. A SNIC is one of the canonical ways a limit cycle can be born, and we will meet it again in Chapter 4 as one entry in the bestiary of two-dimensional bifurcations.

```python
import numpy as np
from scipy.integrate import solve_ivp

omega = 1.0
for a, regime in [(0.5, 'a < ω: rotation'),
                  (1.0, 'a = ω: SNIC'),
                  (1.5, 'a > ω: locked')]:
    f = lambda t, th: omega - a * np.sin(th[0])
    sol = solve_ivp(f, [0, 30], [0.0], dense_output=True,
                    rtol=1e-9, atol=1e-11)
    theta_final = sol.y[0, -1]
    print(f"{regime:18s}  θ(0)=0  →  θ(30)={theta_final:7.3f}  "
          f"({theta_final/(2*np.pi):.2f} turns)")
# a < ω: rotation       θ(30)= 26.0 (4.13 turns) — many revolutions
# a = ω: SNIC           θ(30)=  ~π/2 — crawling toward the half-stable point
# a > ω: locked         θ(30)≈ arcsin(ω/a) — phase-locked
```

Three regimes, three fates: perpetual (non-uniform) rotation, eventual capture at a half-stable ghost, and rapid locking to a stable phase. The only parameter that changed was the ratio $a/\omega$.

### The Period and the Bottleneck

When the system is rotating ($a < \omega$), how long does one revolution take? For any flow on the circle with $\dot\theta > 0$, the period is an integral of $d\theta/\dot\theta$ around the full circle:

$$T = \oint_0^{2\pi} \frac{d\theta}{\dot\theta} = \int_0^{2\pi} \frac{d\theta}{\omega - a\sin\theta}$$

This integral yields to the Weierstrass substitution $u = \tan(\theta/2)$, which turns the transcendental integrand into a rational one {cite}`strogatz2015nonlinear`. After completing the square and integrating, the result is

$$T = \frac{2\pi}{\sqrt{\omega^2 - a^2}}$$

The formula is worth staring at. For $a \ll \omega$, $T \approx 2\pi/\omega$, the uniform-rotation period — a small perturbation barely changes the rhythm. But as $a \to \omega^{-}$, the denominator vanishes and $T \to \infty$. The period diverges as the non-uniform oscillator approaches the SNIC bifurcation, and it does so with a square-root singularity:

$$T \sim \frac{\text{const}}{\sqrt{\omega - a}}$$

The same $1/\sqrt{r}$ scaling that appeared at the saddle-node on the line reappears here. This is not a coincidence. Near a saddle-node, the velocity $f(\theta)$ has a minimum close to zero — a "ghost" of the fixed points that will appear when $a$ crosses $\omega$. Trajectories crawl through this narrow region of near-zero velocity, spending the overwhelming majority of the cycle time traversing a small arc where $\dot\theta$ is tiny. This is the **bottleneck effect**, and it is the signature of a SNIC: before the bifurcation you see long, nearly periodic oscillations interrupted by slow passages through the bottleneck, and after it you see phase-locking with long relaxation times near the former bottleneck location. Oscillators that are "barely oscillating" produce the distinctive pattern of fast bursts separated by long, almost-stationary pauses.

```python
import numpy as np

omega = 1.0
for a in [0.0, 0.5, 0.9, 0.99, 0.999]:
    T_formula = 2 * np.pi / np.sqrt(omega**2 - a**2)
    T_uniform = 2 * np.pi / omega
    print(f"a/ω = {a:.3f}:  T = {T_formula:7.2f}   "
          f"(uniform baseline {T_uniform:.2f}, "
          f"slowdown ×{T_formula/T_uniform:.1f})")
# a/ω = 0.000:  T =  6.28  (slowdown ×1.0)
# a/ω = 0.500:  T =  7.26  (slowdown ×1.2)
# a/ω = 0.900:  T = 14.41  (slowdown ×2.3)
# a/ω = 0.990:  T = 44.56  (slowdown ×7.1)
# a/ω = 0.999:  T =140.55  (slowdown ×22.4)
```

The period is not smoothly diverging — it is accelerating toward infinity as $a/\omega \to 1$. A system poised near a SNIC is *exquisitely* sensitive to parameter changes: moving $a$ from $0.99\omega$ to $0.999\omega$ triples the period. This is an important piece of intuition for Chapter 7, where we will use the divergence of relaxation times as one of the early warning signals for approaching critical transitions. The math of the bottleneck is older than the theory of tipping points, but it is the same math.

### Synchronization and the Adler Equation

The non-uniform oscillator's most consequential application is to **synchronization** — the phenomenon whereby coupled oscillators settle into a common rhythm. The theory begins, unassumingly, with two clocks.

Consider two oscillators with intrinsic frequencies $\omega_1$ and $\omega_2$, coupled so that each one's phase is pulled toward the other's. A minimal model for their phase difference $\psi = \theta_1 - \theta_2$ is

$$\dot{\psi} = \Delta\omega - a\sin\psi$$

where $\Delta\omega = \omega_1 - \omega_2$ is the frequency mismatch and $a > 0$ is the coupling strength. This is the **Adler equation** — Adler derived it in 1946 for electronic oscillator injection-locking {cite}`adler1946study` — and it is precisely the non-uniform oscillator in disguise, with the frequency difference playing the role of $\omega$ and the coupling playing the role of $a$.

The consequences are everything we have already worked out. For weak coupling ($a < |\Delta\omega|$), $\psi$ rotates forever: the oscillators drift apart in phase, each running at its own pace with intermittent near-alignments. This is what physicists call **phase drift**. For strong coupling ($a > |\Delta\omega|$), $\psi$ locks to the stable equilibrium $\sin\psi^* = \Delta\omega/a$: the oscillators lose their independent identities and run at a common frequency, their phases locked at a fixed offset. This is **phase-locking**, the universal mechanism of entrainment. The transition between the two — at $a = |\Delta\omega|$ — is a SNIC.

The applications of this single equation are disproportionate to its simplicity:

**Fireflies.** The *Pteroptyx* fireflies that congregate on mangrove trees along the tidal rivers of Thailand and Malaysia flash in near-perfect unison — trees with thousands of them pulsing as a single strobe. Buck and Buck documented the phenomenon in the field, and the mathematical skeleton is the Adler equation: each firefly adjusts its phase in response to neighbors' flashes, and when the coupling strength exceeds the frequency spread across the population, the community phase-locks {cite}`buck1968mechanism`. The firefly is the subject; the SNIC is the mechanism.

**Josephson junctions.** Two superconductors separated by a thin insulating barrier support a supercurrent $I = I_c\sin\phi$, where $\phi$ is the superconducting phase difference across the junction and $I_c$ is the critical current. In the overdamped limit, a current-biased junction obeys $\dot\phi \propto I - I_c\sin\phi$ — the Adler equation, with driving current in the role of $\omega$ and critical current in the role of $a$. Below $I_c$ the phase locks (a DC supercurrent with zero voltage, the DC Josephson effect); above $I_c$ the phase rotates, producing an oscillating current whose frequency is set by the voltage across the junction (the AC Josephson effect). Josephson junctions are the heart of superconducting qubits and magnetometers, and the transition between the locked and rotating states is a SNIC on the circle {cite}`strogatz2015nonlinear`.

**Phase-locked loops.** Every modern radio, cell phone, and clock-distribution network contains a PLL — a circuit that forces a local oscillator to track an input signal. The dynamics reduce to the Adler equation; the locking range is set by $a$, the loop gain. The SNIC is the boundary between "lock" and "slip," and engineers spend a great deal of effort on staying comfortably inside the locked regime.

The Adler equation is thus the simplest nontrivial mathematical theory of synchronization, and the non-uniform oscillator on the circle is its natural home. Kuramoto's model (Chapter 10) generalizes from two oscillators to $N$, from pairwise coupling to mean-field coupling, from the SNIC on $S^1$ to the transition to coherence of an order parameter. The intuition we have built here — frequency spread versus coupling strength, bottlenecks near the locking threshold, the square-root divergence of relaxation times — survives almost without modification to the many-body case.

### Beyond One Dimension

We have now seen what a one-dimensional flow can do when the state space is compactified from a line into a circle: oscillation becomes possible, and a new bifurcation — the SNIC — organizes the transition between rotation and locking. Even so, the dynamics remain constrained. On $S^1$, a single trajectory is either a fixed point or wraps around the entire circle; there is no way for two distinct periodic orbits to coexist, because nested cycles would have to cross and Picard-Lindelöf forbids crossings. All the richness of chaos, limit cycles that are born from equilibria, spiral approaches to attractors — none of it fits on $S^1$.

Genuine oscillation without topological gimmickry requires the plane. In $\mathbb{R}^2$, trajectories can encircle one another without crossing, and fixed points can be surrounded by closed orbits that attract nearby initial conditions. Chapter 4 opens this world. The phase portrait becomes two-dimensional, the linear stability analysis generalizes from a single derivative to a $2\times 2$ Jacobian, and a genuinely new bifurcation — the Hopf bifurcation, where a stable fixed point spawns a stable limit cycle as it loses stability — replaces the SNIC as the canonical route from equilibrium to oscillation. The non-uniform oscillator of this section survives as a building block: every two-dimensional limit cycle can be parametrized by a phase on $S^1$, and the techniques we have developed here return as the leading-order theory of phase reduction. But the dynamics we can capture expand enormously.
