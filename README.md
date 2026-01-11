# BUSI 721: Data-Driven Finance I - Lecture Slides

Quarto RevealJS slides for BUSI 721: Data-Driven Finance I.

**Live site:** [slides.derivative-securities.org](https://slides.derivative-securities.org)

## Contents

- `01_intro_options.qmd` - Introduction to Derivatives and Options (90 min lecture)

## Rendering Slides

To render the slides locally:

```bash
cd Slides
quarto render 01_intro_options.qmd
```

Output will be in `docs/` folder.

To render all slides and the index:

```bash
quarto render
```

To preview during development:

```bash
quarto preview 01_intro_options.qmd
```

## GitHub Pages Deployment

This repository is configured for GitHub Pages deployment from the `docs/` folder.

After making changes:

1. Render the slides: `quarto render`
2. Commit changes: `git add -A && git commit -m "Update slides"`
3. Push to GitHub: `git push origin main`

The slides will automatically be published to the custom domain specified in `CNAME`.

## Requirements

- Quarto
- Python 3.13+ with:
  - numpy
  - plotly
  - jupyter

## Course Information

**Course:** BUSI 721: Data-Driven Finance I
