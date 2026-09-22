#!/usr/bin/env python3
"""Append the source-order Chapter 9–15 audit ledger entries.

Each question's accompanying explanation states the printed source concept(s), so
it acts as the concise human-readable point inventory. Existing Chapter 2–8
multi-point inventory entries are intentionally preserved.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
coverage_path = ROOT / "audit" / "coverage.json"
ledger = json.loads(coverage_path.read_text(encoding="utf-8"))
ledger = [row for row in ledger if not 9 <= row["chapter"] <= 15]

for chapter_number in range(9, 16):
    chapter = json.loads((ROOT / "data" / f"ch{chapter_number:02d}.json").read_text(encoding="utf-8"))
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
print(f"Wrote {len(ledger)} inventory mappings ({sum(r['chapter'] >= 9 for r in ledger)} for Chapters 9–15).")
