#!/usr/bin/env python3
"""Regenerate audited source-order ledger entries for authored scan chapters.

Existing Chapter 2–8 visual inventory entries are preserved.  Chapters 9–20 and
21–26 use one concise inventory point per authored question; the explanation text
is the human-readable point inventory and the question id is the explicit target.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
coverage_path = ROOT / "audit" / "coverage.json"
ledger = json.loads(coverage_path.read_text(encoding="utf-8"))
authored = set(range(9, 21)) | set(range(21, 27))
ledger = [row for row in ledger if row["chapter"] not in authored]

for chapter_number in list(range(9, 21)) + list(range(21, 27)):
    path = ROOT / "data" / f"ch{chapter_number:02d}.json"
    if not path.exists():
        continue
    chapter = json.loads(path.read_text(encoding="utf-8"))
    for question in chapter["questions"]:
        suffix = f" (Book p{question['page']})"
        point = question["exp"][:-len(suffix)] if question["exp"].endswith(suffix) else question["exp"]
        ledger.append({
            "chapter": chapter_number,
            "page": question["page"],
            "point": point,
            "question": question["id"],
        })
coverage_path.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(
    f"Wrote {len(ledger)} inventory mappings "
    f"({sum(9 <= r['chapter'] <= 20 for r in ledger)} for Chapters 9–20; "
    f"{sum(21 <= r['chapter'] <= 26 for r in ledger)} for Chapters 21–26)."
)
