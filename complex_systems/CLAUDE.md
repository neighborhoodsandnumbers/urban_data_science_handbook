# Complex Systems Textbook — Working Reference

## Book Identity
- **Title**: Complex Systems
- **Author**: A.C. Shannon-Ding
- **Format**: Jupyter Book (dark Tufte CSS theme, ET Book fonts)
- **Audience**: Graduate students and researchers
- **Scope**: ~700–800 pages, two-semester sequence
  - Semester 1: Parts I–IV (foundations, dynamical systems, networks/spatial, stat mech/scaling)
  - Semester 2: Parts V–VII (adaptive/evolutionary, inference/methodology, case studies)

## Structure
- 7 parts, 26 chapters, 4 appendices
- ~145 sections, 21 computational labs
- Each chapter: analytical exposition + worked examples + computational lab
- Python is the medium of exploration, not an afterthought

### Chapter numbering (after Session 6 restructure)
- Part I (Foundations): Ch 1–2
- Part II (Dynamical Systems): Ch 3–7
- Part III (Spatial and Network Systems): Ch 8–11
- Part IV (Information, Statistical Mechanics, and Scaling): Ch 12–15
- Parts V–VII: Ch 16–26

Note: Folder and file names now match displayed chapter numbers (e.g., `3_one_dimensional_flows` displays as Ch 3). The TOC is still the source of truth for ordering.

## Key Design Decisions
- Part IV now opens with Information and Entropy (moved from Part I) — creates a tighter story: information → stat mech → scaling → SOC, all connected by entropy and distribution tails
- Part VI (Inference and Methodology) sits alongside theory, not in a separate stats course — inference *is* complex systems science
- Part VII case studies are capstone, not decoration — students learn to combine formalisms on messy real systems
- Labs are `.ipynb` files; expository sections are `.md`
- **Chapter 2 (Math Preliminaries): hybrid backfill approach.** Section 2.1 (Linear Algebra) is written. Sections 2.2–2.7 will be backfilled AFTER writing Part II+ chapters, so coverage matches actual downstream demand. As each chapter is written, note specific math prerequisites below. Chapter 2 stays as a real chapter (not an appendix) — its pedagogical orientation ("here's the math and here's WHY you need it") earns its place. Appendix B is the pure notation reference.

### Chapter 2 Prerequisites Tracker
As we write chapters, log the specific math each section requires here. This drives the backfill of sections 2.2–2.7.

| Downstream section | Math concept needed | Target Ch 2 section |
|---|---|---|
| 2.1 (written) | Eigenvalues, spectral theorem, matrix exponential, graph Laplacian | 2.1 ✓ |
| 3.1 (Phase Portraits) | What an ODE is, what a solution means, direction fields, continuity of functions | 2.3 (ODEs), 2.2 (Calculus) |
| 3.2 (Fixed Points) | Taylor expansion around a point, $\dot{u} = au$ has solution $u(0)e^{at}$, existence/uniqueness theorem (Picard-Lindelöf), potential functions $\dot{x} = -dV/dx$ | 2.2 (Calculus), 2.3 (ODEs) |
| 3.3 (Bifurcations) | Taylor expansion of $f(x;r)$ around a degenerate fixed point, square-root/cube-root scaling from normal forms, implicit function theorem (when does $f(x,r) = 0$ define $x(r)$?), smooth change of variables | 2.2 (Calculus) |
| 3.4 (Imperfect Bifurcations) | Discriminant of a cubic, two-parameter implicit function theorem, cusp geometry | 2.2 (Calculus) |
| 3.5 (Flows on the Circle) | Trig identities, periodicity, $S^1$ as topological space, improper integrals for oscillation period | 2.2 (Calculus), 2.3 (ODEs) |
| 3.6 (Lab) | Numerical ODE integration (`solve_ivp`), root finding, continuation methods | 2.6 (Numerical Methods) |
| 4.1 (Phase Planes) | Systems of ODEs, vector fields in $\mathbb{R}^2$, existence-uniqueness for systems, implicit curves $f(x,y)=0$ | 2.3 (ODEs), 2.2 (Calculus) |
| 4.2 (Classification) | Jacobian $J_{ij} = \partial f_i/\partial x_j$, trace-det formula for 2×2 eigenvalues, complex eigenvalues, matrix exponential $e^{Jt}$ | 2.1 ✓, 2.3 (ODEs) |
| 4.3 (Limit Cycles) | Jordan curve theorem (Poincaré-Bendixson), Green's/divergence theorem (Bendixson-Dulac), Poincaré maps | 2.2 (Calculus), 2.3 (ODEs) |
| 4.4 (Hopf) | Eigenvalues crossing imaginary axis, polar coordinates, amplitude equations $\dot{r} = \mu r - r^3$ | 2.1 ✓, 2.2, 2.3 |
| 4.5 (Relaxation) | Singular perturbation / slow-fast decomposition, fast/slow manifolds | 2.3 (ODEs) |
| 4.6 (Conservative/Gradient) | Hamiltonian $H(x,y)$, gradient $\nabla V$, Lyapunov functions, conserved quantities | 2.2 (Calculus), 2.3 (ODEs) |
| 4.7 (Lab) | `streamplot`, `contour` for nullclines, ODE system integration, event detection | 2.6 (Numerical Methods) |

## Style Guide

### Voice & Register
- **Conversational, first-person.** Direct address ("we will see that..."), accessible like Strogatz's *Nonlinear Dynamics and Chaos*.
- **Clearly smart, occasionally hip.** Cultural references to literature (Shakespeare, Dostoyevsky, Camus), music (Coltrane, Beatles, Bob Dylan) woven in naturally — the author has a life beyond the equations. These should feel earned, not forced.
- NOT dry or impersonal. The narrator is present, has opinions, and talks to the reader like a sharp colleague.

### Intellectual Stance
- **Present both sides, take a position.** On controversies (SOC, scale-free networks, edge of chaos, etc.): lay out the debate fairly, then state where the evidence points. The author has a view and shares it.
- This is a textbook with a perspective, not a neutral survey.

### Mathematical Rigor
- **State theorems, sketch proofs.** Key results stated precisely with proof sketches or intuitive arguments; full proofs cited. Like Strogatz or Newman.
- Not theorem-proof-corollary formalism, but not hand-waving either. The reader should trust the math.

### Historical Context
- **Chapter openings only.** Each chapter opens with brief historical framing (who, when, why it mattered), then shifts to pure exposition.
- History is scene-setting, not the main act. Keep it to 1–3 paragraphs at the top.

### Code in Prose
- **Frequent inline snippets.** Short code blocks (5–15 lines) appear mid-exposition in `.md` files to ground ideas immediately ("here's what this looks like in NumPy").
- Labs (`.ipynb`) are the full computational experience; prose code is illustrative, not exhaustive.

### Notation
- **Global consistency.** One unified notation system across all 26 chapters; deviations from field conventions flagged explicitly.
- Appendix B is the master reference. Symbol collisions (β as inverse temperature vs. infection rate) are resolved by choosing one system and sticking with it.

### Citations
- **Curated essentials.** 5–15 refs per chapter: the original paper, the best review, and 2–3 key follow-ups.
- The bibliography should be a quality reading list, not an exhaustive literature dump.

### Worked Examples
- **Always both synthetic and real.** Each concept shown first on synthetic/toy data for clarity, then immediately on a real dataset (city populations, earthquake catalogs, contact networks) to show what changes.
- Messiness is pedagogically important — it's where intuition gets tested.

### General Principles
- Python is woven in as the medium of exploration, never an afterthought or appendix
- Code is not supplementary — the computational labs are where intuition is built
- Each chapter should feel self-contained enough to assign independently, but reward sequential reading
- The two-semester split (I–IV / V–VII) should feel natural, not arbitrary

## Progress Log
- **Session 1**: Created full book scaffold (all 7 parts, 26 chapters, 4 appendices, 21 labs). CSS/fonts copied from urban_data_science_handbook. Conducted style interview and established voice, rigor, notation, citation, and example conventions.
- **Session 2**: Wrote section 1.1 (Emergence, Self-Organization, and Adaptation) with chapter-opening historical vignette (Bénard 1900). Covers Anderson's "More Is Different", Goldstein's emergence hallmarks, weak/strong emergence (Chalmers/Bedau), self-organization ingredients (Camazine et al.), Deneubourg's double-bridge ant experiment, Grassé's stigmergy, Holland's CAS definition. Includes two inline code snippets (Game of Life, ant bridge model) and taxonomy table. Populated references.bib with 8 entries. Fact-checked: corrected "whale oil" to "spermaceti" per Bénard's actual experimental setup.
- **Session 3**: Wrote section 1.2 (Reductionism and Its Limits). Covers Descartes's method (1637), Anderson's reductionist vs constructionist distinction, three case studies of constructionist failure (three-body problem/Poincaré, protein folding/Levinthal paradox, phantom traffic jams/Nagel-Schreckenberg), Weinberg's grand vs petty reductionism as counterargument, Laplace's demon demolished three ways (QM, chaos, computational irreducibility). Inline code: Nagel-Schreckenberg traffic CA. Added 7 new bibliography entries. All facts verified.
- **Session 4**: Major structural work on the book scaffold and build pipeline.
  - Fixed CI build failure: added missing `repository.url` to `_config.yml` (required by `use_repository_button: true`).
  - Added `numbered: true` to all TOC parts (except Appendices) for consistent `X.Y.` section numbering in sidebar.
  - Created dedicated chapter intro files (`X_0_chapter_intro.md`) for all 26 chapters so sidebar shows proper chapter titles (e.g., "Mathematical Preliminaries" not "Linear Algebra Essentials").
  - Simplified ~80 verbose section titles across the book (e.g., "Simon's Near-Decomposability and the Architecture of Complexity" → "The Architecture of Complexity"). Preserved subtopic details as HTML comments for future writing.
  - Enabled notebook execution (`execute_notebooks: force`) and created `plot_config.py` with the handbook's dark Tufte matplotlib theme.
  - Fixed sidebar CSS: removed native `<summary>` disclosure triangle (kept chevron), scoped `▼`/`▶` pseudo-element selectors to `.bd-article` only, collapsed extra spacing on sidebar TOC items.
  - Wrote initial draft of section 2.1 (Linear Algebra Essentials).
  - **User feedback & learnings**:
    - User wants chapter titles to be *crisp* — avoid overloaded compound titles. Prefer "The Architecture of Complexity" over "Simon's Near-Decomposability and the Architecture of Complexity." Subtopics go in the body, not the title.
    - User cares about sidebar layout details: no native disclosure triangles, no `▼` characters, compact spacing between TOC items. The chevron icon should stay.
    - User wants notebooks pre-executed so charts render automatically in the built book.
    - Always update CLAUDE.md with progress AND feedback/learnings, not just a changelog.
    - Plan sections in detail before writing. Evaluate the plan. Take time to do a great job.
- **Session 5**: Revised section 2.1 (Linear Algebra Essentials) based on planning agent feedback — initial draft was too slim relative to sections 1.1/1.2.
  - Restructured to match plan: (1) Opening hook with "most overloaded data structure" framing, (2) "Matrices as Descriptions of Systems" — expanded from ~200 to ~450 words with adjacency/Jacobian/covariance triptych, (3) "Eigenvalues and Eigenvectors" — added conjugate pair theorem, sharpened spectral theorem statement, explicit trace-det quadratic formula, (4) "Spectral Decomposition and the Matrix Exponential" — new section combining matrix powers, Markov chains, Perron-Frobenius, and matrix exponential, (5) "Worked Example: The Graph Laplacian" — major expansion (~500 words) with barbell graph, Fiedler vector community detection, quadratic form interpretation, (6) "What We'll Need Later" — new closing with forward-reference table mapping concepts to chapters.
  - Removed: standalone SVD subsection (deferred to Part VI with brief mention in closing table), norms subsection (premature — introduce when needed), "Special Matrices" grab-bag section (positive definite folded into covariance discussion, stochastic matrices folded into Perron-Frobenius discussion).
  - Added Newman (2018) and Chung (1997) to references.bib for graph Laplacian citations. Total section refs: Strang, Chung, Newman (Trefethen removed from inline citation since section now focuses on conceptual rather than computational).
  - Three code blocks: (1) three matrix types with eigenvalues, (2) Jacobian classifier with damped pendulum, (3) barbell graph Laplacian with Fiedler vector.
  - **User feedback & learnings**:
    - **CRITICAL WORKFLOW**: When a planning agent is running, WAIT for it to complete before beginning to write. Do not start writing in parallel with planning. The plan's structure and depth targets should guide the writing, not be reconciled after the fact.
    - Section depth should match the baseline set by earlier sections (1.1, 1.2 are ~2300-2500 words). A math section being noticeably thinner than narrative sections signals inadequate coverage.
    - The plan agent's detailed subsection word counts, topic orderings, and "what this section is NOT" guidance are essential inputs — they prevent scope creep and ensure deliberate omissions.
- **Session 6**: Major outline restructure based on critical review, plus Chapter 1 review and tightening.
  - **Outline changes** (5 structural improvements):
    1. **Moved Information & Entropy (Ch 3) from Part I to Part IV** — renamed Part IV to "Information, Statistical Mechanics, and Scaling." Rationale: info theory's biggest payoffs are Lyapunov exponents, stat mech, and causal inference; placing it as the opener of Part IV creates a tighter information → stat mech → scaling → SOC narrative. Part I now has 2 chapters (What Are Complex Systems? + Math Preliminaries). All chapter references in written sections (1.1, 1.2, 2.1) updated to reflect the renumbering.
    2. **Removed logistic map duplication** — deleted standalone section 6.5 (Logistic Map) from Chaos chapter. Period-doubling route to chaos noted in 6.4 (Routes to Chaos) with forward reference to Ch 7 (Discrete Dynamical Systems), which is the canonical home for the logistic map.
    3. **Expanded synchronization coverage** — renamed section 11.5 from "Synchronization on Networks" to "Synchronization and Coupled Oscillators" with expanded scope: phase oscillators, coupling functions, Arnold tongues, Kuramoto model, chimera states, master stability function.
    4. **Added network controllability** — new section 11.8 covering Liu-Slotine-Barabasi structural controllability, minimum driver nodes, observability, control profiles.
    5. **Trimmed Ch 14 (Scaling Laws)** — folded Zipf/Gibrat/size distributions (was 14.6) into 14.2 (Power Laws in Nature). Chapter reduced from 8 to 7 sections.
  - **Chapter 1 restructure** — tightened from 6 sections to 4:
    - Kept: 1.1 (Emergence), 1.2 (Reductionism), 1.3 (Architecture of Complexity)
    - Merged: old 1.4 (Taxonomy) + old 1.5 (Why Model?) → new 1.4 (Modeling Complex Systems)
    - Removed: 1.6 (History of Complexity Science) — contradicts style guide rule that history belongs in chapter openings, not as standalone sections. Historical milestones to be woven into sections where relevant.
    - New Ch 1 arc: phenomenon (1.1) → problem (1.2) → structure (1.3) → method (1.4)
  - Added Simon (1962) "The Architecture of Complexity" to references.bib (19 total entries).
  - **Chapter 1 content review**: Sections 1.1 and 1.2 are strong — correct voice, good code integration, well-curated citations, appropriate depth (~2300–2500 words each). No content changes needed to written sections beyond chapter number references.
  - Wrote section 1.3 (The Architecture of Complexity). Covers Simon's watchmaker parable (Hora vs Tempus, ~1000-part watches, p≈0.01 interruption probability, ~4000x speed advantage for hierarchical assembly), evolutionary argument ("hierarchies are the ones that have time to evolve" — plausibility, not necessity), protein folding as hierarchy in action (callback to Levinthal's paradox in 1.2), near-decomposability ($A = A_0 + \epsilon C$, two properties: short-run independence + long-run aggregation), timescale separation (building thermal example from Simon's paper), hierarchy across domains (biological, social, engineered), limitations (scale-free networks violate neat hierarchy), and compressibility of hierarchical descriptions as bridge to 1.4. One code block: near-decomposable Markov chain demonstrating eigenvalue gap / timescale separation. Citations: Simon (1962), Anderson (1972). Fact-checked against Simon's original paper: "about" 1000 parts (Simon's deliberate phrasing), three levels of ~10, "four thousand times" is Simon's approximation. All claims verified.
  - **Workflow note**: Planning agent completed first, then fact-checking agent, then writing — correct workflow followed per Session 5 lesson.
  - Wrote section 1.4 (Modeling Complex Systems). Closes Chapter 1 by answering "how do we study complex systems?" Covers Epstein's "Why Model?" (2008) — 16 reasons beyond prediction, grouped as understanding/communication/design; "you are already a modeler" rhetorical move; explanation ≠ prediction. Box & Draper's "all models are wrong, but some are useful" (1987, NOT 1976 — fact-checked). Borges's 1:1 map as cultural reference. Taxonomy of five modeling paradigms (equation-based, agent-based, network, data-driven, hybrid) threaded through epidemic spreading as unifying example. SIR code block (~8 lines) as rhetorical device — "a deliberate act of omission." Connection back to near-decomposability: the choice of modeling paradigm is a choice of level. Roadmap of Parts II–VII keyed to paradigms. Closes with return to Bénard convection from chapter intro (1.0), full circle. Added Epstein (2008) and Box & Draper (1987) to references.bib (21 total entries).
  - **Chapter 1 complete** — all 4 sections written: phenomenon (1.1) → problem (1.2) → structure (1.3) → method (1.4). Total ~7500 words across 4 sections + chapter intro. 5 code blocks, 12 citations.
  - Established **Chapter 2 hybrid backfill approach**: skip ahead to Part II, note math prerequisites as we write, backfill sections 2.2–2.7 with precision once downstream demand is clear. Added prerequisites tracker table to CLAUDE.md.
  - Began **Chapter 3 (One-Dimensional Flows)** — first chapter of Part II: Dynamical Systems.
    - Wrote chapter intro (4_0): Malthus (1798) → Verhulst (1838) vignette. The logistic equation as the simplest system where geometry tells you everything.
    - Wrote section 3.1 (Phase Portraits on the Line). Core geometric method: read dynamics from the graph of $f(x)$. Covers: velocity function, fixed points, arrows/flow direction, phase portrait construction, sin(x) example, qualitative analysis (basins of attraction, no-oscillation theorem, finite-time blowup), x − x³ example with two attractors, logistic equation as real-world application, Pearl & Reed's 1920 fit and its failure. Two code blocks: (1) sin(x) trajectories from multiple ICs, (2) logistic convergence to K. Closes with what 1D cannot do (no oscillations → motivates Ch 4). Citation: Strogatz (2015).
    - Chapter arc planned: geometry (3.1) → formalize stability (3.2) → parameter variation / bifurcations (3.3) → symmetry breaking (3.4) → circle topology (3.5).
    - Populated Ch 2 prerequisites tracker with all Ch 3 section requirements.
    - Added Strogatz (2015) to references.bib (22 total entries).
- **Session 7**: Wrote section 3.3 (Bifurcations). Covers the three codimension-one 1D bifurcations — saddle-node, transcritical, pitchfork (supercritical and subcritical) — unified as the three possible fates of a critical fixed point (where $f = f' = 0$) depending on which Taylor terms are forced to vanish by the system's structure. Opens with Hemingway's "gradually, then suddenly" from *The Sun Also Rises* as the rhythm of a bifurcation (cultural reference, sets up tipping-point narrative for Ch 7). Sets up universality theme (same three normal forms describe thousands of specific models) as a forward reference to Part IV scaling laws. Saddle-node: normal form $\dot{x} = r + x^2$, constant-harvest fishery ($\dot{N} = rN(1-N/K) - h$, collapse at $h_c = rK/4$), Newfoundland cod fishery 1992 as real-world example, and the corollary that recovery requires more than reversing the parameter. Transcritical: $\dot{x} = rx - x^2$, SIS epidemic model ($R_0 = \beta/\gamma$ crossing 1), laser threshold analogy, forward ref to Ch 10. Supercritical pitchfork: $\dot{x} = rx - x^3$, symmetry breaking, Frost's "two roads diverged" cultural reference, $|x^*| \sim \sqrt{r}$ critical exponent noted with forward ref to Ising/Ch 13. Subcritical pitchfork: $\dot{x} = rx + x^3 - x^5$ with hysteresis, buckled beam + shallow-lake regime shift examples, forward ref to Ch 7. Closes with the unifying picture: all three are what happens when $f(x^*) = f'(x^*) = 0$ — classification by which Taylor terms vanish. Forward refs to 3.4 (imperfect pitchfork, cusp), Ch 4 (Hopf as the genuinely new 2D bifurcation), Ch 13 (mean-field pitchfork = second-order phase transition). Two inline code blocks: (1) saddle-node fixed points as $r$ varies, (2) supercritical pitchfork branch selection by initial condition. Single citation (Strogatz 2015). Word count: ~2250, matching baseline set by prior sections. No new bibliography entries.
  - **Design choices**:
    - Chose *not* to add Ludwig-Jones-Holling (1978) or Scheffer citations despite using fishery/lake examples — keeping citation density to Strogatz only for this section preserves the "5-15 refs per chapter" guidance (Chapter 3 is already well-cited via Strogatz across sections). Scheffer will be the primary citation for regime shifts in Ch 7.
    - Emphasized codimension-one framing throughout so that Section 3.4 (Imperfect Bifurcations) can naturally open with codimension-two unfoldings of the pitchfork without extensive setup.
    - Hysteresis treatment is deliberately compact here (normal form + two one-line examples) since the full machinery belongs in Ch 7. This section introduces the phenomenon; Ch 7 does the theory.
- **Session 9**: Wrote section 4.4 (Hopf Bifurcation). Opens by framing Hopf as the genuinely new 2D bifurcation — the one that requires a pair of complex-conjugate eigenvalues and so has no 1D analog. Historical vignette: Eberhard Hopf's 1942 Leipzig paper alongside the earlier planar-case work by the Gorky school (Andronov and students, late 1920s); recommends "Andronov-Hopf" as the fair compound attribution. Arc: supercritical normal form $\dot{r} = \mu r - r^3$, $\dot\theta = \omega$ framed as "a pitchfork lifted into 2D" — the radial equation is literally the supercritical pitchfork normal form of Section 3.3, making the $\sqrt{\mu}$ amplitude scaling a direct inheritance of the $1/2$ critical exponent that keeps recurring (pitchfork amplitude, SNIC period, mean-field Ising — deliberate forward reference to Ch 13). Subcritical variant $\dot{r} = \mu r + r^3 - r^5$ with nested stable/unstable cycles, hard loss of stability, hysteresis, saddle-node of cycles at $\mu = -1/4$. Subcritical examples: aeroelastic flutter (aircraft wings), cardiac arrhythmia. Formal theorem statement: transversality ($\alpha'(0) \neq 0$), non-resonance ($\omega(0) \neq 0$), non-degeneracy ($\ell_1 \neq 0$), supercritical/subcritical determined by sign of first Lyapunov coefficient. Brief mention of center-manifold reduction (Hopf as a 2D phenomenon embedded in arbitrary dimension) and numerical continuation (AUTO/MatCont) for computing $\ell_1$. Worked example: Rosenzweig-MacArthur predator-prey model with Holling type II response, as parameter $K$ (prey carrying capacity) crosses a threshold the coexistence equilibrium loses stability via Hopf and predator-prey oscillations emerge — Rosenzweig's 1971 **paradox of enrichment**, with inline derivation of $K_{\text{Hopf}} = 1/(ah) + 2N^*$. Jacobian verified by hand against equations. Closes with the list of phenomena born from Hopf bifurcations: laser threshold, neural firing, BZ reaction, cardiac pacemaker, circadian rhythms, vortex shedding at Re≈47. Forward refs: Section 4.5 (relaxation oscillations as the large-amplitude limit of Hopf cycles), Chapter 10 (Kuramoto model is coupled near-Hopf oscillators), Chapter 13 (mean-field critical exponent), Chapter 23 (paradox of enrichment revisited in food-web context), Chapter 25 (Hodgkin-Huxley firing). Two inline code blocks: (1) three-panel phase portraits for $\mu = -0.3, 0, 0.4$ showing stable spiral → critical → limit cycle, (2) paradox of enrichment — Hopf point detection via eigenvalue scan plus limit-cycle visualization in $(N, P)$ plane.
  - **Citations**: Strogatz (2015) + two new entries: Kuznetsov (2004) *Elements of Applied Bifurcation Theory* for the rigorous theorem statement and Lyapunov coefficient computation; Rosenzweig (1971) for the paradox of enrichment. 24 total bibliography entries.
  - **Design choices**:
    - Chose to add Kuznetsov despite the Session 7/8 citation-restraint lessons because we explicitly state the theorem formally and need the canonical rigorous reference. Rosenzweig added because the paradox of enrichment is a named result used pedagogically — attribution without a bib entry would be weaker than is earned for a primary citation.
    - Framed the Hopf as "the pitchfork lifted into 2D" to build narrative continuity with Section 3.3 and prepare the $\sqrt{\mu}$-scaling motif as a recurring critical-exponent thread through the book. This makes the section feel less like a new topic and more like the 2D instance of a pattern the reader already knows.
    - Held off on a full derivation of the first Lyapunov coefficient $\ell_1$ — stated it exists, noted its unpleasantness by hand, and pointed to numerical continuation. The algebraic derivation belongs in a bifurcation-theory book, not here. Pointed students to Kuznetsov.
    - Used the Rosenzweig-MacArthur predator-prey model rather than Van der Pol for the worked example since (a) Van der Pol was already introduced in 4.3 as a limit-cycle archetype and reusing it would feel thin, (b) the paradox of enrichment makes the Hopf bifurcation matter — it is not just a mathematical curiosity but a substantive ecological prediction, and (c) ties forward to Chapter 23 (Ecology case studies).
  - Updated Ch 2 prerequisites tracker row for 4.4: eigenvalues crossing imaginary axis, polar coordinates, amplitude equations $\dot{r} = \mu r - r^3$ — all within scope of planned 2.1 (done), 2.2 (Calculus), 2.3 (ODEs).
- **Session 8**: Wrote section 3.5 (Flows on the Circle) — completes Chapter 3. Opens by framing the chapter's central topological move: the no-oscillation theorem of 3.1/3.2 was a consequence of the line being simply connected; bending the line into $S^1$ dissolves the obstruction and makes sustained oscillation possible with no change to the form of the equation. Historical vignette: Huygens 1665, "odd sympathy," two pendulum clocks on a shared beam settling into antiphase — the first coupled-oscillator observation on record. Arc: uniform rotation ($\dot\theta = \omega$, period $2\pi/\omega$) → nonuniform oscillator / Adler's equation ($\dot\theta = \omega - a\sin\theta$, two regimes controlled by $a/\omega$), with exact period $T = 2\pi/\sqrt{\omega^2 - a^2}$ derived by contour/Weierstrass substitution → SNIC (saddle-node on invariant circle, a.k.a. infinite-period bifurcation) at $a = \omega$, with $T \sim \mu^{-1/2}$ scaling where $\mu = \omega - a$, derived by rescaling to the saddle-node normal form $\dot u = \mu + u^2$ of Section 3.3. Framed the $1/2$ exponent as the first concrete **critical exponent** of the book — signature of quadratic tangency, reappears in pitchfork amplitude ($|x^*| \sim \sqrt{r}$), critical slowing down (Ch 7), and mean-field phase transitions (Ch 13). Preview of coupled oscillators: Adler's equation as the universal normal form for two weakly coupled near-identical oscillators ($\dot\phi = \Delta\omega - K\sin\phi$), with phase-locking threshold $K = |\Delta\omega|$ being a SNIC bifurcation. Cultural references: Huygens (opening), Thai firefly synchronization and Millennium Bridge 2000 (closing). Forward refs: Ch 4 (Hopf as the 2D analog allowing self-generated limit cycles, not just topologically forced ones), Ch 10 (Kuramoto model and synchronization on networks), Lab 3.6 (computational assembly). Three inline code blocks: (1) uniform rotation trajectory + projection to sinusoid, (2) three-panel phase line for $a < \omega, a = \omega, a > \omega$, (3) numerical measurement of period scaling recovering slope $-0.500$. Single citation (Strogatz 2015), consistent with 3.3 and 3.4 citation density. Word count: ~2100, near lower end of baseline band. Adler's equation cited by name (canonical term) without adding Adler 1946 to references.bib — the Strogatz citation covers it; adding a single paper for one inline mention would inflate Ch 3's ref list beyond the baseline it has already set.
  - **Chapter 3 now complete** — all five expository sections written (3.1–3.5) plus chapter intro (3.0); only Lab 3.6 remains. Chapter arc: geometry (3.1) → stability analysis (3.2) → bifurcations (3.3) → imperfect pitchfork / cusp catastrophe (3.4) → circle topology and SNIC (3.5). Total ~11,500 words across five sections. Citation density exactly what Session 7 forecast: Strogatz 2015 is the sole reference across 3.3–3.5, with the richer citation tapestry saved for chapters where it is pedagogically justified (e.g., Ch 7 Scheffer for regime shifts, Ch 10 Pikovsky-Rosenblum-Kurths for synchronization).
  - **Design choice**: Held off on adding Pikovsky-Rosenblum-Kurths (2001) even for the coupled-oscillator preview — the forward reference to Ch 10 is enough here. The synchronization book is best cited in its home chapter. Same reasoning for Adler 1946.
  - Updated Ch 2 prerequisites tracker row for 3.5: required trig identities, periodicity, $S^1$ as topological space, improper integrals for oscillation period — all within scope of planned 2.2 (Calculus) and 2.3 (ODEs).
