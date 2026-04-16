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

Note: Folder names (e.g., `4_one_dimensional_flows`) no longer match displayed chapter numbers (that chapter displays as Ch 3). The TOC is the source of truth for ordering; folder names are organizational hints only.

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
| *To be filled as chapters are written* | | |

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
