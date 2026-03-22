"""Plot configuration for Complex Systems textbook.

Matches the dark Tufte theme used across the Urban Data Science Handbook.
Import and call setup_plot_style() at the top of each notebook.
"""

import matplotlib.pyplot as plt
from matplotlib import cycler
from matplotlib.font_manager import findfont, FontProperties


def setup_plot_style():
    """Apply the handbook's dark Tufte-inspired plot style."""
    font_stack = [
        'et-book', 'Palatino', 'Palatino Linotype', 'Palatino LT STD',
        'Book Antiqua', 'Georgia', 'DejaVu Serif'
    ]

    selected_font = 'DejaVu Serif'
    for font in font_stack:
        try:
            if findfont(FontProperties(family=font)) is not None:
                selected_font = font
                break
        except Exception:
            continue

    dark_theme = {
        'figure.facecolor': 'none',
        'axes.facecolor': 'none',
        'savefig.transparent': True,
        'font.family': 'serif',
        'font.serif': [selected_font],
        'font.size': 12,
        'font.weight': 250,
        'grid.color': '#FFFFFF',
        'grid.alpha': 0.3,
        'text.color': '#ddd',
        'axes.labelcolor': '#ddd',
        'xtick.color': '#ddd',
        'ytick.color': '#ddd',
        'axes.edgecolor': '#ddd',
        'axes.prop_cycle': cycler(color=[
            '#D1B675',   # Tan/gold
            '#93C5FD',   # Light blue
            '#B91C1C',   # Red
            '#d1d1d1',   # Light gray
            '#C3FF5B',   # Lime green
            '#FF88FF',   # Magenta
            '#FFD700',   # Gold
            '#8BE9FD',   # Cyan
        ]),
    }

    plt.style.use('dark_background')
    plt.rcParams.update(dark_theme)
