#!/usr/bin/env python3
"""
Extract specific PDF page as image for visual analysis.

Usage: python extract_page_image.py <pdf_path> <page_number>

This script extracts a specific page from a PDF as a high-resolution
PNG image, useful for analyzing complex diagrams or formulas that don't
extract cleanly as text.
"""

import sys
import hashlib
from pathlib import Path

try:
    from pdf2image import convert_from_path
except ImportError:
    print("Error: pdf2image not installed. Install with: pip install pdf2image", file=sys.stderr)
    sys.exit(1)


def get_pdf_hash(pdf_path):
    """Generate SHA256 hash of PDF for caching."""
    with open(pdf_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()[:16]


def extract_page_image(pdf_path, page_num):
    """
    Extract specific PDF page as PNG image.

    Args:
        pdf_path: Path to PDF file
        page_num: Page number to extract (1-indexed)

    Returns:
        Path to cached image file
    """
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        print(f"Error: PDF file not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    if page_num < 1:
        print(f"Error: Page number must be >= 1, got {page_num}", file=sys.stderr)
        sys.exit(1)

    # Set up cache
    pdf_hash = get_pdf_hash(pdf_path)
    cache_dir = Path('.cache/images')
    cache_dir.mkdir(parents=True, exist_ok=True)
    image_file = cache_dir / f"{pdf_hash}_page_{page_num}.png"

    if image_file.exists():
        print(f"{image_file}", file=sys.stdout)
        print(f"# Using cached image: page {page_num} from {pdf_path.name}", file=sys.stderr)
        return image_file

    print(f"# Extracting page {page_num} from {pdf_path.name}...", file=sys.stderr)

    try:
        # Convert specific page to image
        images = convert_from_path(
            str(pdf_path),
            first_page=page_num,
            last_page=page_num,
            dpi=200  # High resolution for formulas and diagrams
        )

        if not images:
            print(f"Error: Page {page_num} not found in PDF", file=sys.stderr)
            sys.exit(1)

        # Save image
        images[0].save(image_file, 'PNG')
        print(f"# Image extracted successfully", file=sys.stderr)
        print(f"{image_file}", file=sys.stdout)
        return image_file

    except Exception as e:
        print(f"Error extracting page image: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python extract_page_image.py <pdf_path> <page_number>", file=sys.stderr)
        sys.exit(1)

    pdf_path = sys.argv[1]
    try:
        page_num = int(sys.argv[2])
    except ValueError:
        print(f"Error: Page number must be an integer, got '{sys.argv[2]}'", file=sys.stderr)
        sys.exit(1)

    output_file = extract_page_image(pdf_path, page_num)
