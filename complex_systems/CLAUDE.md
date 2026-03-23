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
- 149 sections, 21 computational labs
- Each chapter: analytical exposition + worked examples + computational lab
- Python is the medium of exploration, not an afterthought

## Key Design Decisions
- Part VI (Inference and Methodology) sits alongside theory, not in a separate stats course — inference *is* complex systems science
- Part VII case studies are capstone, not decoration — students learn to combine formalisms on messy real systems
- Labs are `.ipynb` files; expository sections are `.md`

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
  - Wrote section 2.1 (Linear Algebra Essentials). Covers vectors/matrices as transformations, eigenvalues/eigenvectors (centerpiece — stability classification, trace/det shortcuts, diagonalization), special matrices (positive definite, stochastic/Perron-Frobenius, graph Laplacian), SVD and PCA connection, norms and matrix exponential. Three inline code blocks: 2D linear transformation, Jacobian eigenvalue classifier, graph Laplacian construction. Referenced Strang (2006) and Trefethen & Bau (1997). All mathematical claims verified against Strang.
  - **User feedback & learnings**:
    - User wants chapter titles to be *crisp* — avoid overloaded compound titles. Prefer "The Architecture of Complexity" over "Simon's Near-Decomposability and the Architecture of Complexity." Subtopics go in the body, not the title.
    - User cares about sidebar layout details: no native disclosure triangles, no `▼` characters, compact spacing between TOC items. The chevron icon should stay.
    - User wants notebooks pre-executed so charts render automatically in the built book.
    - Always update CLAUDE.md with progress AND feedback/learnings, not just a changelog.
    - Plan sections in detail before writing. Evaluate the plan. Take time to do a great job.
