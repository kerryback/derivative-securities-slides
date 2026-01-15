# Dark Theme Quick Start

## Copy-Paste Template

```yaml
---
title: Your Presentation Title
subtitle: Your Subtitle
format:
  revealjs:
    theme: custom-dark.scss
    transition: slide
    slide-number: true
    chalkboard: true
---

```{=html}
<script>
Reveal.on('ready', function() {
  const gridClasses = ['grid-fine', 'grid-medium', 'grid-coarse', 'grid-dense', 'grid-diagonal', 'grid-none'];
  const slideBackgrounds = document.querySelectorAll('.slide-background');
  slideBackgrounds.forEach((bg, index) => {
    if (index === 0) { bg.classList.add('grid-none'); return; }
    bg.classList.add(gridClasses[Math.floor(Math.random() * gridClasses.length)]);
  });
});
</script>
```

## Your First Slide

Content here...
```

## Grid Options

Manually control grid on specific slides:

```markdown
## Slide with Fine Grid {.grid-fine}

## Slide with No Grid (for plots) {.grid-none}

## Slide with Diagonal Grid {.grid-diagonal}
```

## Plotly Dark Theme

```python
import plotly.io as pio
pio.templates.default = "plotly_dark"

# Or per-figure:
fig.update_layout(
    template="plotly_dark",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(26,26,26,0.5)'
)
```

## Key Colors

- Background: `#1a1a1a` (dark gray)
- Text: `#e5e5e5` (light gray)
- Accent: `#00d9ff` (cyan)
- Grid: `rgba(255,255,255,0.06)` (subtle white)

## Render

```bash
quarto render your_slides.qmd
```

That's it! 🎉
