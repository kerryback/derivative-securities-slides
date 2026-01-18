// Grid background randomizer for Reveal.js slides
// This script randomly assigns different grid patterns to slides

Reveal.on('ready', function() {
  // Available grid classes
  const gridClasses = [
    'grid-fine',      // Fine grid with good visibility
    'grid-medium',    // Medium spacing grid
    'grid-coarse',    // Coarse grid with low visibility
    'grid-dense',     // Very dense grid
    'grid-diagonal',  // Diagonal pattern
    'grid-none'       // No grid (plain dark background)
  ];

  // Get all slide backgrounds (excluding title slide)
  const slideBackgrounds = document.querySelectorAll('.slide-background');

  // Apply random grid patterns
  slideBackgrounds.forEach((bg, index) => {
    // Skip the first slide (title slide)
    if (index === 0) {
      bg.classList.add('grid-none');
      return;
    }

    // Randomly select a grid pattern
    const randomGrid = gridClasses[Math.floor(Math.random() * gridClasses.length)];
    bg.classList.add(randomGrid);
  });
});

// Alternative: Apply specific patterns in sequence (uncomment to use)
/*
Reveal.on('ready', function() {
  const gridSequence = [
    'grid-none',      // Title slide
    'grid-fine',
    'grid-medium',
    'grid-coarse',
    'grid-dense',
    'grid-diagonal',
    'grid-none'
  ];

  const slideBackgrounds = document.querySelectorAll('.slide-background');

  slideBackgrounds.forEach((bg, index) => {
    const gridClass = gridSequence[index % gridSequence.length];
    bg.classList.add(gridClass);
  });
});
*/

// Alternative: Apply patterns based on slide content (uncomment to use)
/*
Reveal.on('ready', function() {
  const slides = document.querySelectorAll('.slides > section');
  const slideBackgrounds = document.querySelectorAll('.slide-background');

  slides.forEach((slide, index) => {
    const bg = slideBackgrounds[index];

    // Title slide: no grid
    if (index === 0) {
      bg.classList.add('grid-none');
      return;
    }

    // Slides with plots: no grid or subtle grid
    if (slide.querySelector('.js-plotly-plot') || slide.querySelector('img')) {
      bg.classList.add('grid-none');
    }
    // Slides with lots of text: medium grid
    else if (slide.textContent.length > 500) {
      bg.classList.add('grid-medium');
    }
    // Other slides: random selection
    else {
      const options = ['grid-fine', 'grid-coarse', 'grid-diagonal'];
      const randomGrid = options[Math.floor(Math.random() * options.length)];
      bg.classList.add(randomGrid);
    }
  });
});
*/
