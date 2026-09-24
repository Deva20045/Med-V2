#!/usr/bin/env python3
"""Crop a region of a rendered PDF page and OCR it, for precise re-reads."""
from __future__ import annotations

import sys
from pathlib import Path

import pymupdf
from rapidocr_onnxruntime import RapidOCR

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    ocr = RapidOCR()
    pdf = sys.argv[1]          # uploads/03.pdf
    page_no = int(sys.argv[2]) # 1-based
    # bbox in fractions of the page: x0 y0 x1 y1
    x0, y0, x1, y1 = map(float, sys.argv[3:7])
    doc = pymupdf.open(ROOT / pdf)
    page = doc[page_no - 1]
    r = page.rect
    clip = pymupdf.Rect(x0 * r.width, y0 * r.height, x1 * r.width, y1 * r.height)
    out = ROOT / ".renders" / "_crop.png"
    page.get_pixmap(matrix=pymupdf.Matrix(6, 6), clip=clip).save(out)
    result = ocr(str(out))
    print(f"== crop {pdf} p{page_no} [{x0},{y0},{x1},{y1}] ==")
    if not result or not result[0]:
        print("(no text)")
        return
    rows = []
    for box, text, score in result[0]:
        ys = [p[1] for p in box]
        xs = [p[0] for p in box]
        rows.append((min(ys), min(xs), str(text)))
    rows.sort(key=lambda r: (round(r[0] / 12), r[1]))
    for y, x, text in rows:
        print(f"{y:7.1f} {x:7.1f}  {text}")


if __name__ == "__main__":
    main()
