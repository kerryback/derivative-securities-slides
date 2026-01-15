# Dark Theme with Grid Backgrounds

This theme creates a dark background with varying grid lines across slides, similar to the style in `demo.pdf`.

## Features

- Dark background (#1a1a1a) with light text
- Multiple grid patterns that vary in spacing and opacity:
  - **grid-fine**: 40px spacing, most visible
  - **grid-medium**: 60px spacing, medium visibility
  - **grid-coarse**: 80px spacing, subtle
  - **grid-dense**: 25px spacing, densest grid
  - **grid-diagonal**: Diagonal pattern
  - **grid-none**: Plain dark background without grid
- Randomly assigned grid patterns to slides
- Title slide with gradient background and no grid
- Optimized for plots and figures

## Usage

### 1. Basic Setup (Random Grid Patterns)

Update your `.qmd` file to include the theme and embed the grid script:

```yaml
---
title: Your Title
format:
  revealjs:
    theme: custom-dark.scss
    transition: slide
    slide-number: true
---

```{=html}
<script>
// Grid background randomizer for Reveal.js slides
Reveal.on('ready', function() {
  const gridClasses = ['grid-fine', 'grid-medium', 'grid-coarse', 'grid-dense', 'grid-diagonal', 'grid-none'];
  const slideBackgrounds = document.querySelectorAll('.slide-background');
  slideBackgrounds.forEach((bg, index) => {
    if (index === 0) { bg.classList.add('grid-none'); return; }
    const randomGrid = gridClasses[Math.floor(Math.random() * gridClasses.length)];
    bg.classList.add(randomGrid);
  });
});
</script>
```

## Your content starts here...
```

This will randomly assign different grid patterns to each slide.

### 2. Manual Grid Control

If you want to manually specify which grid pattern to use for specific slides, you can use Quarto's slide attributes:

```markdown
## Slide with Fine Grid {.grid-fine}

Content here...

## Slide with No Grid {.grid-none}

Content here...

## Slide with Diagonal Grid {.grid-diagonal}

Content here...
```

Available classes: `.grid-fine`, `.grid-medium`, `.grid-coarse`, `.grid-dense`, `.grid-diagonal`, `.grid-none`

### 3. Customizing the JavaScript

The `grid-backgrounds.js` file contains three different approaches:

1. **Random assignment** (default, active)
2. **Sequential patterns** (commented out) - cycles through patterns in order
3. **Content-based patterns** (commented out) - applies patterns based on slide content

To switch approaches, comment/uncomment the relevant sections in the JavaScript file.

### 4. Custom Grid Patterns

To create your own grid pattern, add to `custom-dark.scss`:

```scss
.reveal .slide-background.grid-custom {
  background-image:
    repeating-linear-gradient(0deg, rgba(255, 255, 255, 0.08) 0px,
                              rgba(255, 255, 255, 0.08) 1px,
                              transparent 1px, transparent 50px),
    repeating-linear-gradient(90deg, rgba(255, 255, 255, 0.08) 0px,
                              rgba(255, 255, 255, 0.08) 1px,
                              transparent 1px, transparent 50px);
  background-size: 50px 50px;
}
```

Then add `'grid-custom'` to the `gridClasses` array in `grid-backgrounds.js`.

## Customizing Colors

Edit the color variables in `custom-dark.scss`:

```scss
$dark-bg: #1a1a1a;              // Main background color
$grid-color: rgba(255, 255, 255, 0.06);  // Grid line color (most visible)
$grid-color-medium: rgba(255, 255, 255, 0.04);  // Medium visibility
$grid-color-light: rgba(255, 255, 255, 0.02);   // Least visible
$accent-cyan: #00d9ff;          // Accent color for links, highlights
```

## Tips

1. **For slides with plots**: Use `.grid-none` to avoid visual interference
2. **For text-heavy slides**: Use `.grid-medium` or `.grid-coarse`
3. **For title/section slides**: Use `.grid-none`
4. **For visual variety**: Let the random assignment handle it

## Plotly Integration

The theme includes dark mode styling for Plotly figures. To ensure your plots look good on the dark background:

```python
import plotly.graph_objects as go

fig = go.Figure(...)
fig.update_layout(
    template="plotly_dark",  # Use dark template
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
    plot_bgcolor='rgba(0,0,0,0)',   # Transparent plot area
)
```

The grid will automatically be removed from slides containing plots if you use the content-based approach in the JavaScript.

## Example

See the updated `01_intro_options.qmd` for a complete example of the dark theme in action.
