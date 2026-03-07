#!/usr/bin/env python3
"""
Split the large Space Geodesy notes PDF into individual lecture PDFs.

Parses the TOC from the first 2 pages to identify lecture boundaries,
then uses pypdf to extract each lecture into its own file.
"""

import re
from pathlib import Path
from pypdf import PdfReader, PdfWriter

SRC = Path("lectures/space-odesy/01 Introduction to Space Geodesy Notes Lectures.pdf")
OUT_DIR = Path("lectures/space-geodesy")

# Lecture definitions derived from the TOC.
# (output_filename, start_page_in_document, title)
# Page numbers are the *document* page numbers from the TOC (1-indexed),
# which correspond to PDF page index = toc_page + 2 (because 2 TOC pages precede content).
LECTURES = [
    ("L02 - Concept of Reference Systems",       1,   "Concept of Reference Systems"),
    ("L03 - Earth Orientation",                  39,   "Earth Orientation"),
    ("L04 - GNSS Part 1",                       59,   "GNSS: Part 1"),
    ("L05 - GNSS Part 2",                       85,   "GNSS: Part 2"),
    ("L06 - GNSS Remote Sensing",              118,   "GNSS Remote Sensing"),
    ("L07 - Satellite Orbits",                 133,   "The Satellite Orbits"),
    ("L08 - Numerical Integration of Orbits",  153,   "Numerical Integration of Satellite Orbits"),
    ("L09 - Spherical Harmonics",              177,   "Spherical Harmonics"),
    ("L10 - SLR PRARE DORIS",                  205,   "SLR, PRARE, DORIS"),
    ("L11 - VLBI",                             228,   "VLBI"),
    ("L12 - IAG GGOS",                         236,   "IAG GGOS"),
    ("L13 - Altimetry",                        240,   "Introduction to Altimetry"),
    ("L14 - Orbit Perturbations",              261,   "Orbit Perturbations"),
    ("L15 - Satellite Gravity Missions",       268,   "Satellite Gravity Missions"),
    ("L16 - Introduction to Navigation",       286,   "Introduction to Navigation"),
]

TOC_PAGES = 2  # first 2 pages are table of contents


def main():
    reader = PdfReader(str(SRC))
    total_pages = len(reader.pages)
    print(f"Source: {SRC.name} ({total_pages} pages, {TOC_PAGES} TOC pages)")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for i, (name, doc_page, title) in enumerate(LECTURES):
        # Convert document page (from TOC) to 0-indexed PDF page
        start_idx = doc_page + TOC_PAGES - 1  # doc_page 1 → PDF index 2

        # End page is the start of the next lecture (exclusive), or end of PDF
        if i + 1 < len(LECTURES):
            next_doc_page = LECTURES[i + 1][1]
            end_idx = next_doc_page + TOC_PAGES - 1
        else:
            end_idx = total_pages

        num_pages = end_idx - start_idx
        print(f"  {name}: pages {start_idx+1}-{end_idx} ({num_pages} pages)")

        writer = PdfWriter()
        for p in range(start_idx, end_idx):
            writer.add_page(reader.pages[p])

        out_path = OUT_DIR / f"{name}.pdf"
        with open(out_path, "wb") as f:
            writer.write(f)

    print(f"\nDone! {len(LECTURES)} PDFs written to {OUT_DIR}/")


if __name__ == "__main__":
    main()
