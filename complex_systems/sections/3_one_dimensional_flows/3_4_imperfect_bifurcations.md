# Imperfect Bifurcations

The supercritical pitchfork from Section 3.3 required exact symmetry: $f(-x) = -f(x)$. But no real system is perfectly symmetric. A column under compression has a slight initial curvature. A magnetic material has residual magnetization. An ecosystem's two stable states are never exactly mirror images of each other. The question is not whether the symmetry is broken but *how* the breaking changes the dynamics.

Add a single imperfection parameter $h$ to the pitchfork normal form:

$$\dot{x} = h + rx - x^3$$

When $h = 0$, this is the supercritical pitchfork. When $h \neq 0$, the oddness is destroyed — $f(-x) \neq -f(x)$ — and the pitchfork breaks apart. The result is not a mess. It is a richer and more physically relevant structure.

### Breaking the Pitchfork

Fixed points satisfy the depressed cubic $x^3 - rx - h = 0$. For $h = 0$, the roots are $x^* = 0$ and $x^* = \pm\sqrt{r}$ (the pitchfork). For $h \neq 0$, the picture changes qualitatively: the two symmetric branches detach. One becomes a smooth, connected curve — the system's "preferred" state, selected by the sign of $h$. The other appears as an isolated pair of fixed points (one stable, one unstable) born in a saddle-node bifurcation at a shifted value of $r$.

The imperfection picks a winner. For $h > 0$, positive $x$ is favored: the upper branch connects smoothly to the pre-bifurcation state, while the lower branch requires a discontinuous jump to reach. For $h < 0$, the mirror image. The perfect pitchfork's democracy between $+x$ and $-x$ is broken by an arbitrarily small bias.

```python
import numpy as np
import matplotlib.pyplot as plt

r_vals = np.linspace(-1, 3, 600)
fig, axes = plt.subplots(1, 3, figsize=(13, 4), sharey=True)

for ax, h, title in zip(axes, [0, 0.3, -0.3],
    ['$h = 0$ (perfect)', '$h = +0.3$ (broken)', '$h = -0.3$ (broken)']):
    stable_r, stable_x = [], []
    unstable_r, unstable_x = [], []
    for r in r_vals:
        roots = np.roots([1, 0, -r, -h])
        real_roots = roots[np.abs(roots.imag) < 1e-8].real
        for xr in real_roots:
            if r - 3 * xr**2 < 0:
                stable_r.append(r); stable_x.append(xr)
            else:
                unstable_r.append(r); unstable_x.append(xr)
    ax.plot(stable_r, stable_x, '.', color='#93C5FD', ms=1.5, label='stable')
    ax.plot(unstable_r, unstable_x, '.', color='#B91C1C', ms=1.5, label='unstable')
    ax.set(title=title, xlabel='$r$')
    ax.axhline(0, color='gray', ls=':', alpha=0.3)
    ax.axvline(0, color='gray', ls=':', alpha=0.3)
axes[0].set_ylabel('$x^*$')
axes[0].legend(fontsize=8, markerscale=5)
plt.suptitle(r'Imperfect Pitchfork: $\dot{x} = h + rx - x^3$', fontsize=12)
plt.tight_layout(); plt.show()
```

The left panel shows the familiar pitchfork: a single stable branch splitting into two at $r = 0$. The center and right panels show what happens when $h \neq 0$. The pitchfork has been unzipped. One branch remains smoothly connected — the preferred direction — while the other appears as a disconnected island, born and destroyed by saddle-node bifurcations. The perfect pitchfork is the knife-edge between these two asymmetric pictures.

### The Cusp Catastrophe

Where, exactly, does the number of fixed points change? The cubic $x^3 - rx - h = 0$ has three real roots inside some region of the $(r, h)$ parameter plane and one real root outside it. The boundary is where two roots merge — a saddle-node — and it traces a distinctive curve.

The conditions for a repeated root are $f(x^*) = 0$ and $f'(x^*) = 0$ simultaneously:

$$x^3 - rx - h = 0, \qquad 3x^2 - r = 0$$

From the second equation, $r = 3x^2$. Substituting into the first: $x^3 - 3x^3 = h$, so $h = -2x^3$. Eliminating $x$ gives the boundary curve parametrically:

$$(r, h) = (3t^2, -2t^3)$$

This is a **cusp** opening to the right, with its point at the origin. Inside the cusp: three fixed points (two stable, one unstable). Outside: one fixed point. On the cusp boundary: a saddle-node. At the cusp point itself: the perfect pitchfork, the most degenerate case.

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1.3, 1.3, 300)
r_cusp = 3 * t**2
h_cusp = -2 * t**3

fig, ax = plt.subplots(figsize=(7, 5))
ax.fill(r_cusp, h_cusp, color='#93C5FD', alpha=0.15, label='3 fixed points')
ax.plot(r_cusp, h_cusp, color='#D1B675', lw=2.5, label='saddle-node boundary')
ax.plot(0, 0, 'o', color='#D1B675', ms=8, zorder=5, label='cusp point (pitchfork)')
# Two example parameter paths
ax.annotate('', xy=(3.5, 0.5), xytext=(-0.5, 0.5),
            arrowprops=dict(arrowstyle='->', color='#B91C1C', lw=1.5))
ax.annotate('', xy=(3.5, 1.5), xytext=(-0.5, 1.5),
            arrowprops=dict(arrowstyle='->', color='gray', lw=1.5, ls='--'))
ax.text(1.5, 0.65, 'crosses cusp → hysteresis', fontsize=9, color='#B91C1C')
ax.text(1.5, 1.65, 'avoids cusp → smooth', fontsize=9, color='gray')
ax.set(xlabel='$r$', ylabel='$h$', title='Cusp Catastrophe in Parameter Space')
ax.legend(fontsize=9, loc='lower right'); plt.tight_layout(); plt.show()
```

The cusp is the organizing center of the imperfect pitchfork. Every horizontal slice $h = \text{const}$ through this diagram produces a different bifurcation diagram. Only $h = 0$ yields a perfect pitchfork. Slices with small $|h|$ that pass through the cusp interior encounter two saddle-node bifurcations — and between them, three coexisting fixed points. Slices with large $|h|$ that miss the cusp entirely show a single fixed point that deforms smoothly as $r$ varies, with no qualitative transition at all.

This is one of the seven **elementary catastrophes** classified by René Thom — the simplest two-parameter singularity in gradient systems. The classification was the subject of intense excitement (and controversy) in the 1970s; the mathematics has endured even as the grander claims have not {cite}`strogatz2015nonlinear`.

### Hysteresis

The cusp's most consequential implication is **hysteresis**: the system's state depends not just on the current parameter values but on the path taken to reach them.

Fix $h \neq 0$ and slowly increase $r$. The system sits on one stable branch. When $r$ crosses the saddle-node boundary — the edge of the cusp — that branch disappears and the system jumps discontinuously to the other stable branch. Now reverse: decrease $r$. The system stays on the new branch, past the original jump point, until $r$ crosses the *other* saddle-node boundary, and only then jumps back. The forward and backward paths trace different curves. The enclosed region is the **hysteresis loop**, and it means the system has memory — its current state depends on its history, not just its parameters.

```python
import numpy as np
import matplotlib.pyplot as plt

h = 0.3
r_vals = np.linspace(-1, 3.5, 800)

def stable_roots(r, h):
    roots = np.roots([1, 0, -r, -h])
    real_r = sorted(roots[np.abs(roots.imag) < 1e-8].real)
    return [x for x in real_r if r - 3*x**2 < 0]

# Forward sweep: start on lowest stable branch
x_fwd = []
x_cur = stable_roots(r_vals[0], h)[0]
for r in r_vals:
    sr = stable_roots(r, h)
    nearest = min(sr, key=lambda x: abs(x - x_cur))
    x_cur = nearest
    x_fwd.append(x_cur)

# Backward sweep: start on highest stable branch
x_bwd = []
x_cur = stable_roots(r_vals[-1], h)[-1]
for r in reversed(r_vals):
    sr = stable_roots(r, h)
    nearest = min(sr, key=lambda x: abs(x - x_cur))
    x_cur = nearest
    x_bwd.append(x_cur)
x_bwd.reverse()

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(r_vals, x_fwd, '-', color='#93C5FD', lw=2, label='increasing $r$')
ax.plot(r_vals, x_bwd, '-', color='#D1B675', lw=2, label='decreasing $r$')
ax.set(xlabel='$r$', ylabel='$x^*$',
       title=f'Hysteresis Loop ($h = {h}$)')
ax.legend(fontsize=9); plt.tight_layout(); plt.show()
```

The two traces separate where the system jumps — the blue path (increasing $r$) rides the lower branch until it vanishes, then leaps up; the gold path (decreasing $r$) rides the upper branch until it vanishes, then drops down. The gap between the two jump points is the width of the hysteresis loop.

This is not an abstraction. A column under axial compression (Euler buckling) follows exactly this pattern: load the column gradually and it deflects smoothly in the preferred direction until it snaps through to large deflection; unload it and it snaps back at a different load. The imperfection — the column's initial curvature — is $h$. The load is $r$. The cusp catastrophe governs which loads produce smooth deflection and which produce catastrophic buckling {cite}`strogatz2015nonlinear`.

Hysteresis loops and discontinuous jumps are the signature of **bistability** — the coexistence of two stable states separated by an unstable threshold. In Chapter 7, we will add noise to bistable systems and discover that transitions between the wells become stochastic, governed by the potential-well depths from Section 3.2. The cusp catastrophe is the skeleton underlying critical transitions in ecosystems, climate models, and financial markets.

We have now exhausted the qualitative possibilities for flows on the real line: fixed points, three canonical bifurcations, and the imperfect variants that arise when symmetry breaks. One-dimensional flows on the line can only approach fixed points or escape to infinity — we proved this in Section 3.2. But what if the state space is not a line? Bend the real line into a circle, and the topological constraint changes: a trajectory flowing in one direction wraps around and returns to where it started. Oscillations become possible. The next section explores this idea and bridges toward the richer dynamics of Chapter 4.
