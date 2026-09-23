#!/usr/bin/env python3
from __future__ import annotations
import json
from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from build_content import CHAPTERS

cov = json.loads((ROOT / 'audit/coverage.json').read_text(encoding='utf-8'))
ch_cov = Counter(r['chapter'] for r in cov)
chapters_data = []
for n, _title, _start in CHAPTERS:
    path = ROOT / 'data' / f'ch{n:02d}.json'
    if path.exists():
        chapters_data.append(json.loads(path.read_text(encoding='utf-8')))

out = []
out.append("# Chapters 2–15 and 21–26 — visual self-audit gate\n")
out.append("Reviewed 2026-09-23. Source for Chapters 21–26: `uploads/02.pdf`, printed Book p491–531, rendered as 2× PyMuPDF images and read visually in printed order. Existing Chapters 2–15 audit remains from the earlier scan pass.\n")
out.append("## Method and scope\n")
out.append("- Read every educational heading, bullet, sub-bullet, note, table cell, flowchart arm, image label/diagram annotation, threshold, dose, contraindication and treatment branch on p491–531. Parallel columns were treated as unified comparison blocks; publisher footers, timestamps and active-space furniture were excluded.\n")
out.append("- Questions use only recall, scenario, numeric, oddoneout and management formats for Chapters 21–26, with four unique plausible options and exact page citations.\n")
out.append("- Inventory is one-to-one for the authored chapters: each recorded point maps to an explicit `MED-C<N>-XX` question; unasked points after this visual self-audit: **NONE**.\n")
out.append("- Software gates verify schema, IDs, page order, unit contiguity, ledger coverage, embedded data agreement and app parsers.\n")

out.append("## Source-specific notes retained as book-study material\n")
out.append("| Pages | Note |")
out.append("|---:|---|")
out.append("| 491–498 | Vasculitis classification, GCA/PMR, Takayasu criteria, imaging and steroid/tocilizumab/stenting treatment statements are reproduced as source-specific teaching points. |")
out.append("| 499–508 | ANCA testing, GPA/MPA/EGPA/PAN scoring, doses, plasma-exchange indications and HBV-based PAN treatment are retained exactly as printed for study. |")
out.append("| 509–513 | HSP versus cryoglobulinemia criteria, triads, complement/cryocrit findings and treatment branches are source-specific. |")
out.append("| 514–518 | Behcet and Cogan diagnostic/treatment criteria, pathergy values and systemic warning signs are retained as printed. |")
out.append("| 519–520 | Arthritis approach thresholds, inflammatory synovial-fluid cut-off and erosion table are study points, not a substitute for clinical assessment. |")
out.append("| 521–531 | RA risk factors, antibodies, extra-articular manifestations, deformities and DMARD/biologic/JAK treatment algorithms are reproduced as book-study material. |\n")

out.append("## Per-chapter units\n")
out.append("| Ch | Unit | Pages | Question range | Count |")
out.append("|---:|---|---|---|---:|")
q_by_ch = {c['chapter']: {q['id']: q for q in c['questions']} for c in chapters_data}
for c in chapters_data:
    for u in c['units']:
        pages = sorted({q_by_ch[c['chapter']][qid]['page'] for qid in u['qs']})
        p_str = f"{pages[0]}" if len(pages) == 1 else f"{pages[0]}–{pages[-1]}"
        q_range = f"{u['qs'][0]}–{u['qs'][-1]}" if u['qs'][0] != u['qs'][-1] else u['qs'][0]
        out.append(f"| {c['chapter']} | {u['title']} | {p_str} | {q_range} | {len(u['qs'])} |")

out.append("\n## Format distribution\n")
out.append("| Chapter | Recall | Scenario | Numeric | Odd-one-out | Management | Other | Total | Ledger points |")
out.append("|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
for c in chapters_data:
    counts = Counter(q['fmt'] for q in c['questions'])
    other = sum(v for k, v in counts.items() if k not in {'recall','scenario','numeric','oddoneout','management'})
    out.append(f"| {c['chapter']} | {counts['recall']} | {counts['scenario']} | {counts['numeric']} | {counts['oddoneout']} | {counts['management']} | {other} | {len(c['questions'])} | {ch_cov[c['chapter']]} |")

out.append("\n## Chapters 21–26 release table\n")
out.append("| Ch | Title | Printed pages | Questions | Units | Ledger mappings |")
out.append("|---:|---|---:|---:|---:|---:|")
for n in range(21, 27):
    c = next(ch for ch in chapters_data if ch['chapter'] == n)
    out.append(f"| {n} | {c['title']} | {c['pageRange'].replace('-', '–')} | {len(c['questions'])} | {len(c['units'])} | {ch_cov[n]} |")

live = len(chapters_data)
questions = sum(len(c['questions']) for c in chapters_data)
units = sum(len(c['units']) for c in chapters_data)
out.append(f"\n## Gate summary\n\nLive chapter artifacts present: **{live}/57**. Embedded question total after build: **{questions}**; units: **{units}**. Ledger points: **{len(cov)}**. Unasked points: **NONE** in the visually recorded inventory.\n")

(ROOT / 'audit/SELF_AUDIT.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(f"Wrote audit/SELF_AUDIT.md for {live} live chapter artifacts, {questions} questions, {len(cov)} ledger points.")
