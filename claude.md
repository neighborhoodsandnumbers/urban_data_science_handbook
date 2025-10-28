# Urban Data Science Handbook

## Project Overview

This is a **Jupyter Book** project that serves as a comprehensive handbook on Urban Data Science. The book explores the intersection of data science, urban planning, economics, network science, and governance to understand and improve cities.

**Author:** A.C. Shannon-Ding

**Website:** https://goodresearch.dev/

## Project Structure

```
urban_data_science_handbook/
├── _config.yml              # Jupyter Book configuration
├── _toc.yml                 # Table of contents structure
├── _static/                 # Static assets (CSS, etc.)
├── images/                  # Book images and figures
├── sections/                # Main content organized by chapter
│   ├── 0_introduction/
│   ├── 1_statistical_foundations/
│   ├── 2_adv_stats_ml/
│   ├── 3_network_science/
│   ├── 4_geospatial_analysis/
│   ├── 5_complexity_and_urban_science/
│   ├── 6_urban_economics/
│   ├── 7_modeling/
│   ├── 8_gathering_good_data/
│   ├── 9_architecture_and_design/
│   ├── 10_governance_and_policy/
│   ├── 11_conclusions/
│   └── 12_resources/
├── references.bib           # Bibliography for citations
├── requirements.txt         # Python dependencies
└── _build/                  # Build output (generated)
```

## Content Structure

The handbook is organized into 12 major sections:

1. **Introduction** - Role of data in cities, goals and audience
2. **Statistical Foundations** - Distributions, regression, hypothesis testing, causality
3. **Advanced Stats & ML** - Bayesian stats, time series, prediction, clustering
4. **Network Science** - Urban networks, street grids, routing algorithms
5. **Geospatial Analytics** - Spatial autocorrelation, point patterns, spatial regression
6. **Complexity & Urban Science** - Scaling laws, fractal networks
7. **Urban Economics** - Economic complexity, game theory
8. **Modeling** - Agent-based modeling, urban simulation, epidemic modeling
9. **Architecture & Design** - Urban architecture concepts
10. **Governance & Policy** - Governance systems, voting methods
11. **Closing Thoughts** - Ethics, limitations, recommendations
12. **Additional Resources** - Data sources, markdown guides

## Technology Stack

- **Framework:** Jupyter Book
- **Languages:** Python, Markdown
- **Core Libraries:**
  - jupyter-book (documentation framework)
  - matplotlib (plotting)
  - numpy (numerical computing)
- **Build Tool:** Jupyter Book CLI

## File Types

- **`.md` files** - Markdown content for prose and documentation
- **`.ipynb` files** - Jupyter notebooks with executable code examples
- **`.yml` files** - Configuration and table of contents
- **`.bib` files** - BibTeX references for citations
- **`.css` files** - Custom styling (Tufte CSS in `_static/`)

## Building the Book

```bash
# Install dependencies
pip install -r requirements.txt

# Build the HTML book
jupyter-book build .

# Clean previous builds
jupyter-book clean .
```

The built HTML will be in `_build/html/`.

## Jupyter Book Configuration

Key settings from `_config.yml`:

- **Notebook Execution:** All notebooks are re-executed on each build (`execute_notebooks: force`)
- **Timeout:** 30 seconds per notebook
- **Pre-execution:** `plot_config.setup_plot_style()` is run before each notebook (standardizes plotting)
- **Custom CSS:** Tufte-style formatting for elegant typography
- **Citations:** Uses BibTeX from `references.bib`

## Content Guidelines

### Adding New Content

1. Create your file in the appropriate `sections/` subdirectory
2. Use `.md` for text-heavy content
3. Use `.ipynb` for content with code examples and visualizations
4. Add the file to `_toc.yml` in the correct position
5. Build and test locally

### Naming Conventions

- Section folders: `{number}_{topic_name}/`
- Content files: `{chapter}_{section}_{title}.{md|ipynb}`
- Example: `sections/3_network_science/3_1_urban_networks.ipynb`

### Writing Style

- Focus on urban applications of data science
- Include practical examples and case studies
- Balance theory with implementation
- Use visualizations to illustrate concepts
- Cite sources using BibTeX references

## Plot Configuration

The book uses a standardized plotting style via `plot_config.setup_plot_style()` which is automatically imported before each notebook executes. This ensures visual consistency across all figures.

## Development Workflow

1. **Edit Content:** Modify `.md` or `.ipynb` files in `sections/`
2. **Update TOC:** Add new files to `_toc.yml` if needed
3. **Build Locally:** Run `jupyter-book build .` to test
4. **Review:** Check `_build/html/index.html` in a browser
5. **Commit:** Commit changes to git
6. **Deploy:** Build system generates the final site

## Important Notes

- All notebooks are re-executed during build, so code must be reproducible
- Notebooks timeout after 30 seconds - optimize long-running code
- The book uses Tufte CSS for elegant, margin-note-friendly formatting
- Citations use BibTeX format from `references.bib`
- Custom JavaScript/CSS can be added to `_static/`

## Common Tasks

### Adding a New Chapter

1. Create directory: `sections/{number}_{topic}/`
2. Add content files: `{chapter}_{section}_{title}.{md|ipynb}`
3. Update `_toc.yml` with new entries
4. Build and verify

### Adding Citations

1. Add BibTeX entry to `references.bib`
2. Reference in markdown/notebook: `{cite}citationkey`
3. Bibliography automatically generated

### Debugging Build Errors

```bash
# Clean build cache
jupyter-book clean . --all

# Rebuild with verbose output
jupyter-book build . --verbose

# Check specific notebook
jupyter execute sections/path/to/notebook.ipynb
```

## Resources

- [Jupyter Book Documentation](https://jupyterbook.org/)
- [MyST Markdown Guide](https://myst-parser.readthedocs.io/)
- [Sphinx Documentation](https://www.sphinx-doc.org/)
