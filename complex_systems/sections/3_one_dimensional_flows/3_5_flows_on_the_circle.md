# Flows on the Circle

We proved in Section 3.2 that one-dimensional flows on the line cannot oscillate. The argument was topological: a trajectory wanting to come back to where it started would have to reverse direction, which means passing through a zero of $f(x)$, which means a fixed point — and once a trajectory hits a fixed point, it stays there. No cycles. No periodic motion of any kind.

That argument has a quiet assumption: the state space is the real line. Bend the line into a circle, identify the endpoints, and the topology changes. A trajectory can now keep going in one direction and *come back to where it started without ever reversing*. Periodic motion becomes possible without any change to the form of the equation. This is not a sleight of hand. It is the simplest example of a deeper truth in dynamical systems: the state space is part of the model. Same equation, different manifold, different phase portrait, different long-term behavior.

This section develops dynamics on the circle as the gentlest passage from fixed-point dynamics to oscillation. Along the way we will meet our first periodic orbit, our first bifurcation that creates rather than destroys motion, and a small preview of synchronization — a topic that will dominate Chapter 10.

### The Circle as a State Space

A flow on the circle takes the form

$$\dot{\theta} = f(\theta), \qquad \theta \in S^1$$

where $S^1$ is the unit circle, parametrized by an angle $\theta$ with the identification $\theta \equiv \theta + 2\pi$. Concretely, $\theta = 0$ and $\theta = 2\pi$ refer to the same point. The function $f$ must respect this identification: $f(\theta) = f(\theta + 2\pi)$. Periodic state requires periodic vector field.

Everything we learned about fixed points still applies. Zeros of $f$ are still fixed points; the sign of $f'(\theta^*)$ still classifies their stability. What changes is the **global** structure. On the line, between any two fixed points the flow is monotone and trajectories pile up at one end. On the circle, if there are *no* fixed points anywhere, trajectories cannot pile up — they have nowhere to pile. They must keep moving, all the way around, forever. That is a periodic orbit.

The simplest case is the **uniform oscillator**:

$$\dot{\theta} = \omega$$

with $\omega > 0$ a constant angular frequency. There are no fixed points (the equation $\omega = 0$ has no solutions). The solution is $\theta(t) = \theta_0 + \omega t$, taken modulo $2\pi$. The motion is periodic with period

$$T = \frac{2\pi}{\omega}$$

This is the prototype of every oscillator in this book. Strip away the nonlinearity, the noise, the coupling, the spatial structure — keep only the bare fact that something goes around — and you are left with $\dot{\theta} = \omega$. It will reappear as the "free" motion of a Hopf-bifurcating system in Chapter 4, as the natural frequency in the Kuramoto model in Chapter 10, and as the carrier of biological rhythms in Chapter 23.

```python
import numpy as np
from scipy.integrate import solve_ivp

# Uniform oscillator on the circle
omega = 1.5
sol = solve_ivp(lambda t, th: omega, [0, 20], [0.0],
                t_eval=np.linspace(0, 20, 1000), rtol=1e-9)

theta = sol.y[0]
T_observed = 2 * np.pi / omega
print(f"Predicted period:  T = 2π/ω = {T_observed:.4f}")
print(f"Position at t = T: θ ≈ {theta[np.argmin(np.abs(sol.t - T_observed))] % (2*np.pi):.4f}")
# Trajectory wraps the circle every T time units; angle mod 2π returns to its start
```

### The Nonuniform Oscillator

The uniform oscillator is too uniform to be interesting. Real oscillators slow down somewhere and speed up elsewhere — the swing of a pendulum is sluggish at the top and quick at the bottom; a heart beats faster after exertion than at rest; a firefly's flash duty cycle is longer in the dark phase than the bright one. The minimal one-parameter model that captures this asymmetry is the **nonuniform oscillator**:

$$\dot{\theta} = \omega - a\sin\theta$$

with $\omega > 0$ a baseline drive and $a \geq 0$ an amplitude of nonuniformity. The sine term speeds the flow up where $\sin\theta < 0$ (the bottom of the circle) and slows it down where $\sin\theta > 0$ (the top).

The qualitative behavior depends on the ratio $a/\omega$:

- **$a < \omega$**: $f(\theta) = \omega - a\sin\theta > 0$ for all $\theta$, since $a\sin\theta$ never reaches $\omega$. No fixed points exist. Trajectories rotate around the circle, fast at $\theta = -\pi/2$ and slow near $\theta = \pi/2$, but they never stop. Oscillation persists, but it is non-uniform.
- **$a = \omega$**: The flow stalls at $\theta^* = \pi/2$, where $\sin\theta = 1$ and $f = 0$. A single fixed point appears, and it is **half-stable** — attracting from below, repelling from above. This is the borderline case.
- **$a > \omega$**: Two fixed points emerge, located where $\sin\theta = \omega/a$. Linear stability analysis ($f'(\theta) = -a\cos\theta$) shows that the lower one (closer to $\pi/2$) is stable and the upper one (closer to $\pi/2$ from above) is unstable. The system no longer rotates; it gets stuck at the stable fixed point. Oscillation is dead.

The transition between the rotating and the stuck regime — at $a = \omega$ — is a saddle-node bifurcation. The new feature, compared to Section 3.3, is that the bifurcation occurs *on a closed loop*, and the consequence is that an entire periodic orbit is created or destroyed in a single event.

The most striking signature is the period. For $a < \omega$ the period of rotation can be computed by separation of variables:

$$T = \int_0^{2\pi} \frac{d\theta}{\omega - a\sin\theta} = \frac{2\pi}{\sqrt{\omega^2 - a^2}}$$

This is one of the few oscillator periods in this book that has a clean closed form. As $a \to \omega^-$, the denominator vanishes and $T \to \infty$. The oscillator does not gradually slow to a stop; it does something more peculiar — it lingers ever longer near $\theta = \pi/2$ before the rest of the circuit, because the velocity is becoming arbitrarily small there. The trajectory still completes one full revolution, but most of the time is spent on a vanishingly small arc. This phenomenon — slow passage through a "ghost" of a fixed point — recurs throughout dynamical systems and is the universal signature of a saddle-node nearby.

```python
import numpy as np
from scipy.integrate import solve_ivp

omega = 1.0
print("    a    |  T (analytic)  |  T (numerical)  |  ω - a")
print("---------+----------------+-----------------+--------")
for a in [0.0, 0.5, 0.9, 0.99, 0.999]:
    T_exact = 2 * np.pi / np.sqrt(omega**2 - a**2)
    # Numerical: integrate from theta = 0 until theta crosses 2π
    def event(t, th):  return th[0] - 2 * np.pi
    event.terminal = True
    sol = solve_ivp(lambda t, th: omega - a * np.sin(th[0]), [0, 1e4], [0.0],
                    events=event, rtol=1e-10, atol=1e-12, max_step=0.01)
    T_num = sol.t_events[0][0]
    print(f"  {a:5.3f}  |   {T_exact:10.4f}   |   {T_num:11.4f}   | {omega - a:7.4f}")
# The period diverges like 1/sqrt(ω - a) as a → ω⁻ — the ghost of the saddle-node
```

The numerical integration confirms the analytic formula and makes the divergence visceral: at $a = 0.999$, the period is more than 70 times the value at $a = 0$, even though the oscillator's "drive" $\omega$ has not changed at all. The motion has become bottlenecked.

### Saddle-Node on an Invariant Circle

The bifurcation at $a = \omega$ deserves a name of its own because the global picture is genuinely new. Locally — zooming in near $\theta = \pi/2$ — it looks identical to the saddle-node we studied in Section 3.3: two fixed points colliding and annihilating, with the same normal form $\dot{u} = r + u^2$ after a smooth change of variables. The local mechanism is the cockroach. But globally, the fixed points sit on a closed invariant circle, and their disappearance leaves the entire circle as a periodic orbit. A bifurcation that destroys two fixed points has *created* an oscillation.

This goes by various names — **saddle-node on an invariant circle**, **SNIC bifurcation**, or **saddle-node infinite-period (SNIPER) bifurcation** — all referring to the same picture {cite}`strogatz2015nonlinear`. The "infinite-period" name advertises the diagnostic feature: the period of the newborn oscillation diverges as $T \sim 1/\sqrt{a - \omega}$ from the oscillating side, in contrast to the **Hopf bifurcation** of Chapter 4, where oscillations are born with finite period and infinitesimal amplitude. SNIC is amplitude-from-the-start, period-from-infinity. Hopf is the opposite. The two are the canonical mechanisms by which periodic motion appears in dissipative systems, and a great deal of the dynamics-on-networks literature in Part III hinges on which one a given system uses.

In neuroscience, the distinction is named: neurons whose firing emerges via SNIC are **Type I excitable** (firing rate continuously tunable from zero, Hodgkin's classification); those that emerge via Hopf are **Type II** (firing rate jumps abruptly to a finite value at threshold). The mathematics of one-dimensional flows on a circle is, at it turns out, the mathematics of how a quiescent neuron starts to fire.

### Coupled Oscillators

The single biggest reason to care about flows on the circle is that two of them, weakly coupled, give rise to **synchronization** — and the simplest model of synchronization reduces *exactly* to the nonuniform oscillator above.

Take two phase oscillators with intrinsic frequencies $\omega_1$ and $\omega_2$, coupled through a sinusoidal interaction:

$$\dot{\theta}_1 = \omega_1 + K\sin(\theta_2 - \theta_1), \qquad \dot{\theta}_2 = \omega_2 + K\sin(\theta_1 - \theta_2)$$

The coupling strength $K \geq 0$ measures how strongly each oscillator pulls the other toward its own phase. Define the phase difference $\phi = \theta_2 - \theta_1$ and subtract:

$$\dot{\phi} = (\omega_2 - \omega_1) - 2K\sin\phi = \Delta\omega - 2K\sin\phi$$

This is the nonuniform oscillator from above, with $\omega \to \Delta\omega$ and $a \to 2K$. We have already solved it. If the coupling is weak ($2K < |\Delta\omega|$), no fixed point of $\phi$ exists — the oscillators **drift**, with the phase difference slowly winding around the circle. If the coupling is strong ($2K > |\Delta\omega|$), a stable fixed point of $\phi$ appears: the oscillators **lock**, holding a constant phase offset and ticking together at a common compromise frequency.

The transition — at $K = |\Delta\omega|/2$ — is a SNIC bifurcation in the phase difference. Below threshold, no synchronization; above threshold, synchronization is automatic. The threshold scales with the natural frequency mismatch: more dissimilar oscillators need stronger coupling to lock.

```python
import numpy as np
from scipy.integrate import solve_ivp

omega1, omega2 = 1.0, 1.3                # natural frequencies (different)
K_values = [0.10, 0.20]                  # below / above sync threshold
K_critical = abs(omega2 - omega1) / 2    # 0.15

for K in K_values:
    def rhs(t, th):
        return [omega1 + K * np.sin(th[1] - th[0]),
                omega2 + K * np.sin(th[0] - th[1])]
    sol = solve_ivp(rhs, [0, 200], [0.0, 0.5], t_eval=np.linspace(0, 200, 4000))
    phase_diff = (sol.y[1] - sol.y[0])
    locked = "LOCKED" if K > K_critical else "drifting"
    print(f"K = {K:.2f}  ({K:.2f} {'>' if K > K_critical else '<'} K_c = {K_critical:.2f})  "
          f"→  Δθ(t→∞) ≈ {phase_diff[-1] % (2*np.pi):.3f}  [{locked}]")
# Below threshold the phase difference grows without bound (drifting);
# above threshold it settles to a constant (locked).
```

This is the simplest mathematical model of synchronization, and it punches well above its weight. It captures the entrainment of fireflies along an Indonesian river bank, of pacemaker cells in the sinoatrial node, of laser arrays, of crowds clapping in a concert hall, and of generators on the AC power grid. Scale it up to $N$ oscillators with a distribution of natural frequencies and you have the **Kuramoto model**, which we will study in detail in Chapter 10. The phase transition between disorder and synchrony in the Kuramoto model is precisely the many-body version of the SNIC bifurcation we have just analyzed for $N = 2$.

### What One-Dimensional Topology Cannot Reach

The wheel is come full circle, as Edmund put it on a different occasion. We have now seen that changing the *topology* of the state space — without touching the equation — buys us oscillation. The same machinery (fixed points, linear stability, bifurcations) works on $S^1$ as on $\mathbb{R}$, but the global picture is richer because trajectories can return to their starting point without reversing direction.

This is, however, the modest end of what topology can do. The circle is still one-dimensional. Every trajectory either heads toward a fixed point or goes around the loop — there is no third option. Genuinely two-dimensional flows on the plane open up phenomena that no 1D state space can host: spiraling approach to fixed points, limit cycles that are not just rotations of a circular state space, structurally stable periodic orbits, and (when we add a third dimension in Chapter 5) deterministic chaos. The transition to two dimensions is not just "more of the same with an extra coordinate." It is qualitatively new. The next chapter takes that step.

We close Chapter 3 with the toolkit complete for dynamics on one-dimensional manifolds: phase portraits read by eye, fixed points classified by the sign of $f'$, the three canonical 1D bifurcations, the imperfect pitchfork and its cusp, and oscillations born by changing the topology of the state space. From this point onward, every system we study will have at least two coupled state variables — and the geometry will get correspondingly more interesting.
