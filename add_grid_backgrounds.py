#!/usr/bin/env python3
"""
Add random grid backgrounds to Quarto reveal.js slides.

This script adds {data-state="grid-xxx"} attributes to slide headings
in a Quarto .qmd file. Slides with figures or iframes get grid-none,
while other slides get randomly assigned grid patterns.

The script is idempotent - you can run it multiple times on the same file
and it will update existing data-state attributes.

Usage:
    python add_grid_backgrounds.py input.qmd
    python add_grid_backgrounds.py input.qmd -o output.qmd
"""

import re
import sys
import random
import argparse
from pathlib import Path

# Available grid patterns for regular slides
GRID_PATTERNS = ['grid-dense', 'grid-fine', 'grid-medium', 'grid-coarse', 'grid-sparse']

def has_figure_or_iframe(lines, start_idx):
    """
    Check if a slide (starting at start_idx) contains a figure or iframe.
    Look ahead until the next slide heading or end of file.

    Args:
        lines: List of file lines
        start_idx: Index of the slide heading

    Returns:
        bool: True if slide contains figure/iframe, False otherwise
    """
    i = start_idx + 1
    while i < len(lines):
        line = lines[i]

        # Stop at next slide heading (level 2)
        if line.startswith('## '):
            break

        # Check for Python figure labels (Quarto convention)
        if '#| label: fig-' in line:
            return True

        # Check for HTML iframes
        if '<iframe' in line.lower():
            return True

        i += 1

    return False

def process_qmd_file(input_file, output_file=None, seed=None):
    """
    Process a .qmd file and add/update grid data-state attributes.

    Args:
        input_file: Path to input .qmd file
        output_file: Path to output file (None = overwrite input)
        seed: Random seed for reproducibility (None = random)
    """
    # Set random seed if provided
    if seed is not None:
        random.seed(seed)

    # Read the input file
    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modified_count = 0
    added_count = 0

    # Process each line
    for i, line in enumerate(lines):
        # Check if this is a level-2 slide heading (## )
        if line.startswith('## '):
            # Check if slide has figure/iframe
            has_plot = has_figure_or_iframe(lines, i)

            # Determine grid pattern
            if has_plot:
                grid_pattern = 'grid-none'
            else:
                grid_pattern = random.choice(GRID_PATTERNS)

            # Check if line already has data-state or class-based grid
            # Patterns: {data-state="..."} or {.grid-...}
            has_data_state = re.search(r'\{data-state="[^"]+"\}', line)
            has_grid_class = re.search(r'\{\.grid-[^}]+\}', line)

            if has_data_state:
                # Replace existing data-state
                new_line = re.sub(
                    r'\{data-state="[^"]+"\}',
                    f'{{data-state="{grid_pattern}"}}',
                    line
                )
                lines[i] = new_line
                modified_count += 1
            elif has_grid_class:
                # Replace grid class with data-state
                new_line = re.sub(
                    r'\{\.grid-[^}]+\}',
                    f'{{data-state="{grid_pattern}"}}',
                    line
                )
                lines[i] = new_line
                modified_count += 1
            else:
                # Add data-state before the newline
                line_stripped = line.rstrip('\n\r')
                lines[i] = f'{line_stripped} {{data-state="{grid_pattern}"}}\n'
                added_count += 1

    # Write output
    output_path = Path(output_file) if output_file else input_path
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    # Print summary
    total_changes = modified_count + added_count
    print(f"Successfully processed {input_path.name}")
    print(f"  - Added grid attributes: {added_count}")
    print(f"  - Updated existing attributes: {modified_count}")
    print(f"  - Total slides modified: {total_changes}")

    if output_file:
        print(f"  - Output written to: {output_path}")
    else:
        print(f"  - File updated in place")

def main():
    parser = argparse.ArgumentParser(
        description='Add random grid backgrounds to Quarto reveal.js slides',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s slides.qmd              # Update file in place
  %(prog)s slides.qmd -o new.qmd   # Write to new file
  %(prog)s slides.qmd --seed 42    # Use seed for reproducibility
        """
    )

    parser.add_argument(
        'input_file',
        help='Input .qmd file'
    )

    parser.add_argument(
        '-o', '--output',
        help='Output file (default: overwrite input file)',
        default=None
    )

    parser.add_argument(
        '--seed',
        type=int,
        help='Random seed for reproducibility',
        default=None
    )

    args = parser.parse_args()

    # Validate input file extension
    if not args.input_file.endswith('.qmd'):
        print("Error: Input file must be a .qmd file", file=sys.stderr)
        sys.exit(1)

    try:
        # Process the file
        process_qmd_file(args.input_file, args.output, args.seed)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
