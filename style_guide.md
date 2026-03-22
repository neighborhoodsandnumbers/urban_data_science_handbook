# CSS Style Guide

This document provides an overview of the CSS styling used in the Urban Data Science Handbook Jupyter Book.

## Architecture

The book uses the **Sphinx Book Theme** with a custom **Tufte-inspired** CSS overlay. The styling stack is:

1. **Bootstrap 5.3.2** - Base framework (via PyData Sphinx Theme)
2. **Sphinx Book Theme** - Jupyter Book's default theme
3. **`_static/tufte.css`** - Custom overrides loaded via `_config.yml`

The custom CSS is injected through the `html.extra_css` setting in `_config.yml`:

```yaml
html:
  extra_css:
    - _static/tufte.css
```

An older variant, `_static/tufte_old.css`, is also present but not actively loaded.

## Color Scheme

The book uses a **dark theme** with the following palette:

| Role | Color | Hex |
|------|-------|-----|
| Background | Dark navy | `#192738` |
| Code background | Deeper navy | `#16202d` |
| Header bar | Dark maroon | `#660000` |
| Primary accent | Warm gold | `#d09937` |
| Secondary accent | Teal | `#29A8AB` |
| Body text | Light gray | `#ddd` |
| Secondary text | Soft gray | `#c0c6dc` |
| Code text | Near-white | `#E5E7EB` |

### Syntax Highlighting

Python code blocks use a custom color scheme:

| Token | Color | Hex |
|-------|-------|-----|
| Keywords | Teal | `#29A8AB` |
| Strings | Golden | `#e1a53c` |
| Functions/Classes | Red | `#e44949` |
| Numbers/Constants | Light blue | `#93C5FD` |
| Comments/Operators | Medium gray | `#b0b0b0` |
| Identifiers | Light gray | `#E5E7EB` |

## Typography

### Font Stack

The book uses the **ET Book** typeface family (a Tufte staple), loaded via `@font-face` from `_static/et-book/`. The font files ship in ttf, woff, eot, and svg formats for broad browser support.

```css
body {
  font-family: et-book, Palatino, "Palatino Linotype", "Palatino LT STD",
               "Book Antiqua", Georgia, serif;
  font-size: 19px;
  font-weight: 250;
}
```

Code blocks use a monospace stack:

```css
font-family: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
font-size: 14px;
```

### Heading Hierarchy

| Level | Size | Weight | Style | Color |
|-------|------|--------|-------|-------|
| h1 | 34px | 700 | Italic | Default |
| h2 | 26px | 700 | Italic | Default |
| h3 | 24px | 300 | Italic | Teal (`#29A8AB`) |
| h4 | 20px | 300 | Normal | Default |

## Layout

### Sidebar

- Fixed height (`100vh`), sticky positioning
- Max-width: `335px`
- Custom thin scrollbar: `#c0c6dc` thumb on `#192738` track

### Main Content

- Max-width: `2800px`, centered with `margin: 0 auto`
- Padding: `10px`

### Secondary TOC

- Max-width: `220px`

## Key Component Styles

### Code Cells

Jupyter notebook cells are styled with:

- Background: `#16202d`
- Border-radius: `4px`
- Left padding: `24px`
- No borders or box shadows
- Consecutive cells have collapsed margins (`.cell + .cell { margin-top: 0 }`)

### Toggle / Collapse Elements

Toggle buttons for hiding/showing code inputs use:

- Full-width layout
- Left border: `2px solid #d09937`
- Padding: `8px 16px`
- Hover: background shifts to `#243447`, text turns gold
- Smooth transitions: `0.2s ease`

### Admonitions

Note and warning boxes (`.admonition`) support collapsible behavior via toggle buttons with arrow icon rotation.

### Margin Notes

Following the Tufte style, margin notes are supported:

- Desktop: `40%` width, floated right
- Mobile: Hidden by default, toggled into view as block elements
- Print: `33%` width

Relevant classes: `.margin`, `.margin-caption`, `span.marginnote`, `span.sidenote`, `.cell.tag_margin`.

### Copy Button

Code blocks include a copy-to-clipboard button:

- Absolute positioned (top-right)
- Appears on hover (opacity `0.7` to `1.0`)
- Success state: green border flash

## Responsive Breakpoints

| Breakpoint | Target |
|------------|--------|
| `max-width: 768px` | Mobile / tablet |
| `min-width: 992px` | Desktop |
| `min-width: 1200px` | Large desktop |

A `@media print` query hides toggles and interactive elements.

## Animations & Transitions

- **Buttons/toggles**: `all 0.2s ease`
- **Copy button**: `opacity 0.2s ease-in-out`
- **Theme switch**: `color 0.25s ease-out`
- **Toggle arrows**: `transform 0.2s ease` (rotates 0deg to 90deg)
- **Header shadow**: `0 6px 6px -6px` appears on scroll

## File Inventory

### Source Files (checked in)

| File | Purpose |
|------|---------|
| `_static/tufte.css` | Primary custom stylesheet |
| `_static/tufte_old.css` | Archived variant (not loaded) |
| `_static/et-book/` | ET Book font family (12 files) |

### Generated Files (in `_build/`)

Built by Jupyter Book / Sphinx during `jb build`:

- `basic.css` - Sphinx base
- `bootstrap.css` - Bootstrap 5
- `pygments.css` - Syntax highlighting
- `mystnb.*.css` - MyST notebook cell styles
- `copybutton.css` - Copy button
- `togglebutton.css` - Toggle/collapse
- `sphinx-thebe.css` - Interactive cell support
- `sphinx-book-theme.css` - Theme styles
