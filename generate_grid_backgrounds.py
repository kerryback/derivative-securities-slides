"""
Generate grid background images for Quarto presentations
This script creates PNG images with dark backgrounds and varying grid patterns
"""

import numpy as np
from PIL import Image, ImageDraw
import os

# Configuration
WIDTH = 1920
HEIGHT = 1080
DARK_BG = (26, 26, 26)  # #1a1a1a
OUTPUT_DIR = "backgrounds"

# Grid configurations: (spacing, opacity, line_width)
GRID_CONFIGS = {
    'grid_fine': (40, 15, 1),
    'grid_medium': (60, 10, 1),
    'grid_coarse': (80, 5, 1),
    'grid_dense': (25, 18, 1),
    'grid_sparse': (100, 8, 1),
    'grid_none': (0, 0, 0),  # No grid
}

def create_grid_background(spacing, opacity, line_width=1):
    """
    Create a dark background image with grid lines

    Args:
        spacing: Distance between grid lines in pixels
        opacity: Opacity of grid lines (0-255)
        line_width: Width of grid lines in pixels

    Returns:
        PIL Image object
    """
    # Create dark background
    img = Image.new('RGB', (WIDTH, HEIGHT), DARK_BG)
    draw = ImageDraw.Draw(img, 'RGBA')

    if spacing == 0:  # No grid
        return img

    # Grid line color with opacity
    grid_color = (255, 255, 255, opacity)

    # Draw vertical lines
    for x in range(0, WIDTH, spacing):
        draw.line([(x, 0), (x, HEIGHT)], fill=grid_color, width=line_width)

    # Draw horizontal lines
    for y in range(0, HEIGHT, spacing):
        draw.line([(0, y), (WIDTH, y)], fill=grid_color, width=line_width)

    return img

def create_diagonal_grid(spacing=50, opacity=10):
    """Create a diagonal grid pattern"""
    img = Image.new('RGB', (WIDTH, HEIGHT), DARK_BG)
    draw = ImageDraw.Draw(img, 'RGBA')
    grid_color = (255, 255, 255, opacity)

    # Draw diagonal lines (bottom-left to top-right)
    for offset in range(-HEIGHT, WIDTH, spacing):
        draw.line([(offset, HEIGHT), (offset + HEIGHT, 0)],
                 fill=grid_color, width=1)

    # Draw diagonal lines (top-left to bottom-right)
    for offset in range(-HEIGHT, WIDTH, spacing):
        draw.line([(offset, 0), (offset + HEIGHT, HEIGHT)],
                 fill=grid_color, width=1)

    return img

def create_random_opacity_grid(base_spacing=50):
    """Create a grid with randomly varying opacity for visual interest"""
    img = Image.new('RGB', (WIDTH, HEIGHT), DARK_BG)
    draw = ImageDraw.Draw(img, 'RGBA')

    # Draw vertical lines with random opacity
    for x in range(0, WIDTH, base_spacing):
        opacity = np.random.randint(5, 20)
        grid_color = (255, 255, 255, opacity)
        draw.line([(x, 0), (x, HEIGHT)], fill=grid_color, width=1)

    # Draw horizontal lines with random opacity
    for y in range(0, HEIGHT, base_spacing):
        opacity = np.random.randint(5, 20)
        grid_color = (255, 255, 255, opacity)
        draw.line([(0, y), (WIDTH, y)], fill=grid_color, width=1)

    return img

def main():
    """Generate all grid background images"""
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Generating grid background images...")

    # Generate standard grid patterns
    for name, (spacing, opacity, line_width) in GRID_CONFIGS.items():
        print(f"  Creating {name}.png...")
        img = create_grid_background(spacing, opacity, line_width)
        img.save(os.path.join(OUTPUT_DIR, f'{name}.png'))

    # Generate diagonal grid
    print("  Creating grid_diagonal.png...")
    img_diag = create_diagonal_grid(spacing=70, opacity=8)
    img_diag.save(os.path.join(OUTPUT_DIR, 'grid_diagonal.png'))

    # Generate random opacity grid
    print("  Creating grid_random.png...")
    img_random = create_random_opacity_grid(base_spacing=50)
    img_random.save(os.path.join(OUTPUT_DIR, 'grid_random.png'))

    print(f"\nDone! Generated {len(GRID_CONFIGS) + 2} background images in '{OUTPUT_DIR}/' directory")
    print("\nTo use these images in your slides:")
    print("1. Add the following to your YAML header:")
    print("   background-image: backgrounds/grid_fine.png")
    print("   background-size: cover")
    print("\n2. Or use per-slide backgrounds:")
    print("   ## Slide Title {background-image='backgrounds/grid_medium.png'}")

if __name__ == '__main__':
    main()
