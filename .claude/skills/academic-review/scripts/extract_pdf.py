#!/usr/bin/env python3
"""
Extract PDF to markdown with LaTeX formulas using Marker.

Usage: python extract_pdf.py <pdf_path>

This script extracts text and formulas from PDF lecture slides,
preserving mathematical formulas in LaTeX format. Results are cached
for fast repeated access.
"""

import sys
import hashlib
import json
from pathlib import Path

try:
    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict
    from marker.output import text_from_rendered
except ImportError:
    print("Error: marker-pdf not installed. Install with: pip install marker-pdf", file=sys.stderr)
    sys.exit(1)


def get_pdf_hash(pdf_path):
    """Generate SHA256 hash of PDF for caching."""
    with open(pdf_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()[:16]


def extract_pdf(pdf_path):
    """
    Extract PDF to markdown with LaTeX formulas.

    Args:
        pdf_path: Path to PDF file

    Returns:
        Path to cached markdown file
    """
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        print(f"Error: PDF file not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    # Check cache
    pdf_hash = get_pdf_hash(pdf_path)
    cache_dir = Path('.cache/extracted')
    cache_file = cache_dir / f"{pdf_hash}.md"
    metadata_file = cache_dir / f"{pdf_hash}.json"

    if cache_file.exists():
        print(f"{cache_file}", file=sys.stdout)
        print(f"# Using cached extraction from {pdf_path.name}", file=sys.stderr)
        return cache_file

    print(f"# Extracting {pdf_path.name}... This may take a minute.", file=sys.stderr)

    try:
        # Extract with Marker
        converter = PdfConverter(artifact_dict=create_model_dict())
        rendered = converter(str(pdf_path))
        markdown_text, _, _ = text_from_rendered(rendered)

        # Save to cache
        cache_dir.mkdir(parents=True, exist_ok=True)
        cache_file.write_text(markdown_text, encoding='utf-8')

        # Save metadata
        metadata = {
            'pdf_path': str(pdf_path.absolute()),
            'pdf_name': pdf_path.name,
            'hash': pdf_hash
        }
        metadata_file.write_text(json.dumps(metadata, indent=2), encoding='utf-8')

        print(f"# Extraction complete", file=sys.stderr)
        print(f"{cache_file}", file=sys.stdout)
        return cache_file

    except Exception as e:
        print(f"Error extracting PDF: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf.py <pdf_path>", file=sys.stderr)
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_file = extract_pdf(pdf_path)
