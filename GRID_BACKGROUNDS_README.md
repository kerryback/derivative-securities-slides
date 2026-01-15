# Grid Backgrounds for Quarto Slides

This document explains how to add subtle grid backgrounds to Quarto reveal.js presentations.

## Quick Start

### Using the Python Script (Recommended)

The easiest way to add grid backgrounds is using the automated script:

```bash
# Add grids to a file (updates in place)
python add_grid_backgrounds.py slides.qmd

# Create a new file with grids
python add_grid_backgrounds.py slides.qmd -o slides_with_grids.qmd

# Use a seed for reproducible results
python add_grid_backgrounds.py slides.qmd --seed 42
```

The script:
- ✓ Randomly assigns grid patterns to text slides
- ✓ Automatically skips slides with plots/iframes (assigns `grid-none`)
- ✓ Is idempotent (can run multiple times safely)
- ✓ Handles files that already have grid attributes

### Manual Method

Add `{data-state="grid-pattern"}` to any slide heading:

```markdown
## My Slide Title {data-state="grid-medium"}

Slide content here...
```

## Available Grid Patterns

| Pattern | Spacing | Best For |
|---------|---------|----------|
| `grid-dense` | 30px | Very tight grid, high density |
| `grid-fine` | 40px | Tight grid, moderate density |
| `grid-medium` | 60px | Balanced spacing |
| `grid-coarse` | 80px | Wide spacing, subtle |
| `grid-sparse` | 100px | Very wide spacing, minimal |
| `grid-none` | - | No grid (for plots/figures) |

## Theme Setup

### Light Theme (custom.scss)

The light theme uses dark grids (6% opacity) on a cream background. The grid CSS is already included in [custom.scss](custom.scss).

### Dark Theme (custom-dark.scss)

The dark theme uses white grids (6% opacity) on a dark background. The grid CSS is already included in [custom-dark.scss](custom-dark.scss).

## How It Works

The grid patterns use Reveal.js's `data-state` feature, which applies CSS classes to the `<body>` element when a slide is displayed. The CSS creates grids using `repeating-linear-gradient`:

```css
body.grid-medium {
  background-image:
    repeating-linear-gradient(to bottom, rgba(0, 0, 0, 0.06) 0px, rgba(0, 0, 0, 0.06) 1px, transparent 1px, transparent 60px),
    repeating-linear-gradient(to right, rgba(0, 0, 0, 0.06) 0px, rgba(0, 0, 0, 0.06) 1px, transparent 1px, transparent 60px);
  background-size: 60px 60px;
}
```

## Examples

### Example 1: Mixed Patterns

```markdown
## Introduction {data-state="grid-medium"}

Text slide with medium grid.

## Data Visualization {data-state="grid-none"}

```{python}
#| label: fig-plot
# Plot code here
```

No grid behind the plot.

## Analysis {data-state="grid-fine"}

Text slide with fine grid.
```

### Example 2: Using the Script

```bash
# Process your slides
python add_grid_backgrounds.py my_presentation.qmd

# The script will automatically:
# - Add random grids to text slides
# - Skip plot slides
# - Preserve existing attributes
```

## Customization

To adjust grid opacity or spacing, edit the grid patterns in your theme file:

**For light theme** (`custom.scss`):
```scss
body.grid-medium {
  background-image:
    repeating-linear-gradient(to bottom, rgba(0, 0, 0, 0.06) 0px, rgba(0, 0, 0, 0.06) 1px, transparent 1px, transparent 60px),
    repeating-linear-gradient(to right, rgba(0, 0, 0, 0.06) 0px, rgba(0, 0, 0, 0.06) 1px, transparent 1px, transparent 60px);
  background-size: 60px 60px;
}
```

Change `0.06` to adjust opacity (0.02 = very subtle, 0.10 = more visible).
Change `60px` to adjust spacing (smaller = denser grid).

## Troubleshooting

**Grids not visible?**
- Check that your theme file (custom.scss or custom-dark.scss) includes the grid CSS
- Ensure reveal.js containers are transparent (they should be by default)
- Verify the data-state attribute is spelled correctly

**Wrong pattern on plot slides?**
- Re-run the script to automatically detect and fix plot slides
- Manually change to `{data-state="grid-none"}`

**Script not working?**
- Ensure Python 3.6+ is installed
- Check file path is correct
- Verify the .qmd file uses `## ` for slide headings (level 2)
