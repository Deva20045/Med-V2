import json
from collections import Counter

cov = json.load(open('audit/coverage.json'))
chapters_data = [json.load(open(f'data/ch{n:02d}.json')) for n in range(1, 9)]

out = []
out.append("# PULSE Medicine Vol 2 — Progress\n")
out.append("Updated 2026-09-22. Single offline HTML quiz for Medicine Vol 2, Book p377–702.\n")
out.append("- Repository: `Deva20045/Med-V2`")
out.append("- Session branch: `arena/01a0c840-med-v2`")
out.append("- Published URL: https://deva20045.github.io/Med-V2/")
out.append("- Source of truth: `data/chNN.json`; generated deliverable: `pulse-medicine.html`; `index.html` redirects to it.")
out.append("- Build status: **8 live chapters / 57**, **294 questions / 34 units**. Chapters 9–57 remain `live:false`.\n")

out.append("## This release (Chapters 5–8)")
out.append("""
1. Authored and verified four consecutive cardiology chapters from printed pages 394–414 of `uploads/01.pdf`:
   - **Chapter 5: Tachyarrhythmias** (p394–402): 52 questions / 5 units.
   - **Chapter 6: Atrial Fibrillation and Flutter** (p403–406): 33 questions / 4 units.
   - **Chapter 7: Ventricular Arrhythmias** (p407–412): 36 questions / 3 units.
   - **Chapter 8: WPW Syndrome** (p413–414): 14 questions / 2 units.
2. Complete visual self-audit: **402 total educational point-to-question mappings** (262 existing + 140 new across p394–414), with **0 unasked points**.
3. High-quality clinical question authoring: strictly non-predictable options, realistic clinical distractors, true/false balanced pairs, match bijections, exact `(Book pX)` citations.
4. Schema, actual app regex parsers (`parseMatch`, `fillupHtml`, `matchOptHtml`, `splitExp`), bijections, unit coverage, and book-order validation all pass.
5. All 294 questions and 34 units successfully compiled and embedded into standalone offline deliverable `pulse-medicine.html`.
6. Full test suite passing: `python3 validate_content.py --embedded`, `tests/app_parsers.cjs`, and `python3 -m unittest discover -s tests -v`.

Full evidence: [self-audit and page-by-page ledger](audit/SELF_AUDIT.md), [pre-build validation output](audit/PREBUILD_VALIDATION.txt), [machine-readable inventory](audit/coverage.json).
""")

out.append("## Verified PDF → printed-page map\n")
out.append("**Printed page numbers are ground truth.** All 103 pages of this copy of `uploads/01.pdf` were rendered with PyMuPDF `Matrix(2,2)` and visually checked. Full explicit mapping and source hash: [PAGE_MAP.md](audit/PAGE_MAP.md), [page-map.json](audit/page-map.json).\n")
out.append("- PDF1–12: unnumbered front-matter and Contents.")
out.append("- PDF13–18: 377–382 (Chapter 1).")
out.append("- PDF19–22: 383–386 (Chapter 2).")
out.append("- PDF23–25: 387–389 (Chapter 3).")
out.append("- PDF26–29: 390–393 (Chapter 4).")
out.append("- PDF30–38: 394–402 (Chapter 5: Tachyarrhythmias).")
out.append("- PDF39–42: 403–406 (Chapter 6: Atrial Fibrillation and Flutter).")
out.append("- PDF43–48: 407–412 (Chapter 7: Ventricular Arrhythmias).")
out.append("- PDF49–50: 413–414 (Chapter 8: WPW Syndrome).")
out.append("- PDF51–103: 415–467 (Chapter 9 onwards).\n")

out.append("## Schema and order contract\n")
out.append("- Chapter: `chapter`, exact roadmap `title`, `pageRange` beginning at the roadmap start, nonempty `questions` and `units`.")
out.append("- Question: sequential `MED-C<N>-<seq>` IDs; `sec`, integer `page`, `fmt` in recall/fillup/match/truefalse/scenario/oddoneout/numeric/management; `q`; exactly four unique options; integer `ans` 0–3; `exp` ending exactly `(Book pX)` matching `page`.")
out.append("- Unit: `MED-U<N>-<n>`, `ch`, `n`, `title`, `sec`, a 2–4-line `guide`; `qs` rebuilt from that section in question-array order. Flattened units must exactly equal the full chapter question sequence.")
out.append("- Fill-up stems contain `____`. Match grammar: `<prompt> — 1) left 2) left … A) right B) right`. No nested reserved item-label tokens. Every option covers all left items; the correct mapping is a bijection.")
out.append("- True/false has exactly two True and two False options. Answer options shuffle in the app; questions do not.")
out.append("- Inventory order follows printed page/content blocks. Software checks the inventory's sequence and references; visual review checks semantic coverage and within-page placement.")
out.append("- Source discrepancies are explicitly qualified in explanations. Questions are book-study material, not a substitute for current clinical guidelines.\n")

out.append("## Build / audit / test workflow\n")
out.append("""```sh
# Python 3 and Node required for the fail-closed build gate.
python3 validate_content.py --ledger     # print every point before building
python3 -m unittest discover -s tests -v
python3 build_content.py
python3 validate_content.py --embedded
```
""")

out.append("## Per-chapter units\n")
out.append("| Ch | Unit | Pages | Question range | Count |")
out.append("|---:|---|---|---|---:|")
for c in chapters_data:
    for u in c['units']:
        q_start = u['qs'][0]
        q_end = u['qs'][-1]
        pages_in_unit = sorted(list({next(q['page'] for q in c['questions'] if q['id'] == qid) for qid in u['qs']}))
        p_str = f"{pages_in_unit[0]}" if len(pages_in_unit) == 1 else f"{pages_in_unit[0]}–{pages_in_unit[-1]}"
        q_range = f"{q_start}–{q_end}" if q_start != q_end else q_start
        out.append(f"| {c['chapter']} | {u['title']} | {p_str} | {q_range} | {len(u['qs'])} |")

import sys
sys.path.insert(0, '.')
from build_content import CHAPTERS
out.append("\n## Full roadmap\n")
out.append("| Ch | Title | Starts | State |")
out.append("|---:|---|---:|---|")
live_chapters = {c['chapter'] for c in chapters_data}
for num, title, start in CHAPTERS:
    state = "Live" if num in live_chapters else "Soon"
    out.append(f"| {num} | {title} | {start} | {state} |")

with open('PROGRESS.md', 'w') as f:
    f.write('\n'.join(out) + '\n')
print("Successfully updated PROGRESS.md!")
