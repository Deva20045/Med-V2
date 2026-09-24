"""Regenerate PROGRESS.md from the chapter artifacts, the ledger and the roadmap."""
import json
from collections import Counter
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from build_content import CHAPTERS  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
cov = json.loads((ROOT / "audit" / "coverage.json").read_text(encoding="utf-8"))
numbers = sorted({c["chapter"] for c in
                  [json.loads((ROOT / "data" / f"ch{n:02d}.json").read_text()) for n in range(1, 58)]
                  } ) if False else None

chapters_data = []
for n in range(1, 58):
    path = ROOT / "data" / f"ch{n:02d}.json"
    if path.exists():
        chapters_data.append(json.loads(path.read_text(encoding="utf-8")))

live = {c["chapter"] for c in chapters_data}
total_q = sum(len(c["questions"]) for c in chapters_data)
total_u = sum(len(c["units"]) for c in chapters_data)
release = [c for c in chapters_data if 33 <= c["chapter"] <= 38]
release_q = sum(len(c["questions"]) for c in release)
release_u = sum(len(c["units"]) for c in release)
release_pages = sum(
    int(c["pageRange"].split("-")[1]) - int(c["pageRange"].split("-")[0]) + 1 for c in release
)
latest = [c for c in chapters_data if 30 <= c["chapter"] <= 31]
latest_q = sum(len(c["questions"]) for c in latest)
latest_u = sum(len(c["units"]) for c in latest)
latest_pages = sum(
    int(c["pageRange"].split("-")[1]) - int(c["pageRange"].split("-")[0]) + 1 for c in latest
)
cur = [c for c in chapters_data if 27 <= c["chapter"] <= 29]
cur_q = sum(len(c["questions"]) for c in cur)
cur_u = sum(len(c["units"]) for c in cur)
cur_pages = sum(
    int(c["pageRange"].split("-")[1]) - int(c["pageRange"].split("-")[0]) + 1 for c in cur
)
previous = [c for c in chapters_data if 16 <= c["chapter"] <= 26]
previous_q = sum(len(c["questions"]) for c in previous)
previous_u = sum(len(c["units"]) for c in previous)
previous_pages = sum(
    int(c["pageRange"].split("-")[1]) - int(c["pageRange"].split("-")[0]) + 1 for c in previous
)


def compress(numbers):
    out, start, prev = [], None, None
    for n in numbers:
        if start is None:
            start = prev = n
        elif n == prev + 1:
            prev = n
        else:
            out.append((start, prev))
            start = prev = n
    if start is not None:
        out.append((start, prev))
    return ", ".join(f"{a}" if a == b else f"{a}–{b}" for a, b in out)


not_live = compress(sorted(set(range(1, 58)) - live))

out = []
out.append("# PULSE Medicine Vol 2 — Progress\n")
out.append("Updated **2026-09-24**. Standalone offline quiz based on *PULSE Medicine Vol 2*, printed Book p377–702.\n")
out.append("- Repository: `Deva20045/Med-V2`")
out.append("- Session branch: `arena/01a0d219-med-v2`")
out.append("- Published URL: https://deva20045.github.io/Med-V2/")
out.append("- Editable source of truth: `data/chNN.json`; generated offline deliverable: `pulse-medicine.html`; `index.html` redirects to it.")
out.append(f"- **Build status: {len(live)} live chapters / 57 · {total_q} questions / {total_u} units.** "
           f"Chapters {not_live} remain `live:false`.\n")

out.append("## This release — Chapters 30–31\n")
out.append("Two consecutive neurology chapters were rendered line-to-line from `uploads/02.pdf` PDF87–93 and `uploads/03.pdf` PDF1 (Book p555–562), source-ordered and made live:\n")
out.append("| Ch | Title | Printed pages | Questions | Units |")
out.append("|---:|---|---:|---:|---:|")
for c in latest:
    out.append(f"| {c['chapter']} | {c['title']} | {c['pageRange'].replace('-', '–')} "
               f"| {len(c['questions'])} | {len(c['units'])} |")
out.append(f"| **Release total** |  | **{latest_pages} book pages** | **{latest_q}** | **{latest_u}** |\n")
out.append("### Quality and ordering contract delivered\n")
out.append("1. Every supplied sheet was read top-to-bottom at 2×, including diagrams, tables, percentages, lesion patterns, gaze rules and visual-field notes; the p562 handoff is verified and no sheet in p555–562 is missing.")
out.append(f"2. Chapters 30–31 add **{latest_q} ordered mappings** to `audit/coverage.json`, bringing the audited ledger to **{len(cov)} mappings** for Chapters 2–38.")
out.append("3. Questions use no fill-up, matching or true/false worksheets; distractors are plausible and questions are reasoning-first.")
out.append("4. IDs, book-page order, contiguous unit slices and exact `(Book pX)` explanation suffixes pass the fail-closed validator.")
out.append(f"5. Chapters 30–31 are embedded in the standalone app and all {len(live)} roadmap flags for live chapters are set.\n")

out.append("## Previous release — Chapters 27–29\n")
out.append("Three consecutive rheumatology chapters were rendered from `uploads/02.pdf`, read block by block, "
           "source-ordered and made live (Book p532–554, all in `uploads/02.pdf` PDF64–86):\n")
out.append("| Ch | Title | Printed pages | Questions | Units |")
out.append("|---:|---|---:|---:|---:|")
for c in cur:
    out.append(f"| {c['chapter']} | {c['title']} | {c['pageRange'].replace('-', '–')} "
               f"| {len(c['questions'])} | {len(c['units'])} |")
out.append(f"| **Release total** |  | **{cur_pages} book pages** | **{cur_q}** | **{cur_u}** |\n")
out.append("### Quality and ordering contract delivered\n")
out.append("1. All pages were read in printed order (`uploads/02.pdf` PDF64–86 = Book p532–554), including "
           "flowchart arms, comparison tables, numeric thresholds, diagram labels, notes, management ladders "
           "and drug doses. Scans have no extractable text: every reading used 2× PyMuPDF renders with "
           "FILE-tagged verification, and every printed page number was verified against the page map.")
out.append(f"2. Every source-mapped learning target has a four-option, citation-backed question in "
           f"`audit/coverage.json`; Chapters 27–29 add **{cur_q} ordered mappings**, bringing the audited "
           f"ledger to **{len(cov)} mappings** for Chapters 2–38.")
out.append("3. New questions are reasoning-first: **no fill-up or matching worksheets**. Scenarios, "
           "mechanism-based recall, numeric interpretation, management decisions and discriminating "
           "odd-one-out cases use plausible medical distractors.")
out.append("4. IDs are sequential, question arrays remain strictly nondecreasing in book page, unit question "
           "lists are exact contiguous slices of source order, and every explanation ends with its exact "
           "`(Book pX)` citation.")
out.append(f"5. Chapters 27–29 are embedded in the standalone app and all {len(live)} roadmap flags for live "
           "chapters are set.\n")

out.append("## Previous release — Chapters 33–38\n")
out.append("Six consecutive neurology chapters were rendered from the scans, read block by block, "
           "source-ordered and made live (Book p566–601, all in `uploads/03.pdf`; printed p586, p590 and p591 "
           "are absent from the supplied scan and are transparently flagged in the ledger):\n")
out.append("| Ch | Title | Printed pages | Questions | Units |")
out.append("|---:|---|---:|---:|---:|")
for c in release:
    out.append(f"| {c['chapter']} | {c['title']} | {c['pageRange'].replace('-', '–')} "
               f"| {len(c['questions'])} | {len(c['units'])} |")
out.append(f"| **Release total** |  | **{release_pages} book pages (p586/p590/p591 absent from scan)** | **{release_q}** | **{release_u}** |\n")

out.append("### Quality and ordering contract delivered\n")
out.append("1. All pages were read in printed order (`uploads/03.pdf` PDF5–37 = Book p566–601; printed p586, "
           "p590 and p591 are absent from the scan), including flowchart arms, comparison tables, numeric "
           "thresholds, diagram labels, notes, management ladders and drug doses. Scans have no extractable "
           "text: every reading used 2× PyMuPDF renders, and every printed page number was verified against the "
           "page map (decisive 10× corner reads settled the missing sheets).")
out.append(f"2. Every source-mapped learning target has a four-option, citation-backed question in "
           f"`audit/coverage.json`; Chapters 33–38 add **{release_q} ordered mappings**, bringing the audited "
           f"ledger to **{len(cov)} mappings** for Chapters 2–38. Every target is marked asked.")
out.append("3. New questions are reasoning-first: **no fill-up or matching worksheets** in Chapters 9–29 or 33–38. "
           "Scenarios, mechanism-based recall, numeric interpretation, management decisions and discriminating "
           "odd-one-out cases use plausible medical distractors.")
out.append("4. IDs are sequential, question arrays remain strictly nondecreasing in book page, unit question "
           "lists are exact contiguous slices of source order, and every explanation ends with its exact "
           "`(Book pX)` citation.")
out.append("5. Source-specific algorithms, medication doses, clinical thresholds and historical terminology are "
           "retained as book-study material and qualified in the audit; they are not a replacement for current "
           "local clinical guidance.")
out.append(f"6. Chapters 33–38 are embedded in the standalone app and all {len(live)} roadmap flags for live "
           "chapters are set.\n")

out.append("## Previous release — Chapters 16–26\n")
out.append("Eleven consecutive rheumatology chapters (Book p458–531): ")
out.append("| Ch | Title | Printed pages | Questions | Units |")
out.append("|---:|---|---:|---:|---:|")
for c in previous:
    out.append(f"| {c['chapter']} | {c['title']} | {c['pageRange'].replace('-', '–')} "
               f"| {len(c['questions'])} | {len(c['units'])} |")
out.append(f"| **Release total** |  | **{previous_pages} pages** | **{previous_q}** | **{previous_u}** |\n")
out.append("Full evidence: [Chapter 30–31 read notes](audit/READ_NOTES_30_31.md), "
           "[visual audit and page-by-page ledger](audit/SELF_AUDIT.md), [machine-readable inventory](audit/coverage.json), "
           "[verified PDF-page map](audit/PAGE_MAP.md) and [pre-build validation output](audit/PREBUILD_VALIDATION.txt).\n")

out.append("## Verified PDF → printed-page map\n")
out.append("Printed page numbers are ground truth. Every sheet used so far was rendered at 2× and checked "
           "visually. `uploads/01.pdf` is sequential after 12 unnumbered front-matter sheets; `uploads/02.pdf` "
           "continues the same volume at Book p468; `uploads/03.pdf` continues at Book p562 (printed p586, p590 "
           "and p591 are absent from the scan); `uploads/04.pdf` begins at Book p626. Full mappings are in "
           "[PAGE_MAP.md](audit/PAGE_MAP.md), [page-map.json](audit/page-map.json) and "
           "[page-map-02.json](audit/page-map-02.json).\n")
out.append("- PDF13–18: Book p377–382 (Ch1)")
out.append("- PDF19–29: p383–393 (Ch2–4)")
out.append("- PDF30–38: p394–402 (Ch5)")
out.append("- PDF39–42: p403–406 (Ch6)")
out.append("- PDF43–48: p407–412 (Ch7)")
out.append("- PDF49–50: p413–414 (Ch8)")
out.append("- PDF51–60: p415–424 (Ch9)")
out.append("- PDF61–65: p425–429 (Ch10)")
out.append("- PDF66–77: p430–441 (Ch11)")
out.append("- PDF78–84: p442–448 (Ch12)")
out.append("- PDF85–87: p449–451 (Ch13)")
out.append("- PDF88–90: p452–454 (Ch14)")
out.append("- PDF91–93: p455–457 (Ch15)")
out.append("- **PDF94–101: p458–465 (Ch16)**")
out.append("- **PDF102–103 + 02.pdf PDF1–2: p466–469 (Ch17)**")
out.append("- **02.pdf PDF3–9: p470–476 (Ch18)**")
out.append("- **02.pdf PDF10–16: p477–483 (Ch19)**")
out.append("- **02.pdf PDF17–23: p484–490 (Ch20)**")
out.append("- **02.pdf PDF24–63: p491–531 (printed p527 absent) (Ch21–26)**")
out.append("- **02.pdf PDF64–86: p532–554 (Ch27–29)**")
out.append("- **02.pdf PDF87–93: p555–561 (Ch30–31)**")
out.append("- **03.pdf PDF1: p562 (Ch31)**")
out.append("- 03.pdf PDF2–4: p563–565 (Ch32 territory, not yet live)")
out.append("- **03.pdf PDF5–10: p566–571 (Ch33–34)**")
out.append("- **03.pdf PDF11–21: p572–582 (Ch35–36)**")
out.append("- **03.pdf PDF22–31: p583–592 (printed p586, p590, p591 absent) (Ch37)**")
out.append("- **03.pdf PDF29–37: p593–601 (Ch38)**")
out.append("- 03.pdf PDF38–61: p602–622 (Ch39 onward, not yet live); 04.pdf: p626 onward\n")

out.append("## Schema and order contract\n")
out.append("- Chapter: exact roadmap number/title, `pageRange` starts at the roadmap page, nonempty `questions` and `units`.")
out.append("- Question: sequential `MED-C<N>-<seq>` ID; section/page/format/stem; exactly four unique options; one answer; explanation ending exactly `(Book pX)` matching `page`.")
out.append("- Units: sequential `MED-U<N>-<n>` IDs; each has a 2–4-line guide; its IDs are rebuilt from exactly one section in original question order; flattened units equal the full chapter sequence.")
out.append("- Questions are in printed book-page order; all printed pages in every live chapter are represented.")
out.append("- The source-order inventory is fail-closed: the validator requires a ledger mapping for every question in audited Chapters 2–38, in exact question order and with matching book page.")
out.append("- Questions are educational book-study material, not a substitute for current clinical guidelines or patient care.\n")

out.append("## Build, audit and test workflow\n")
out.append("```sh")
out.append("# Generate/edit chapter artifacts only when source artefacts need regeneration.")
out.append("python3 tools/generate_ch09_15.py        # Chapters 9-15")
out.append("python3 tools/generate_ch16_20.py        # Chapters 16-20")
out.append("python3 tools/generate_ch21_26.py        # Chapters 21-26")
out.append("python3 tools/generate_ch27_29.py        # Chapters 27-29")
out.append("python3 tools/generate_ch30_31.py        # Chapters 30-31")
out.append("python3 tools/generate_ch33_38.py        # Chapters 33-38")
out.append("python3 tools/generate_ch09_15_audit.py  # rebuild the source-order ledger (Ch9-31, Ch33-38)")
out.append("python3 tools/generate_self_audit.py     # rebuild audit/SELF_AUDIT.md")
out.append("")
out.append("# Fail-closed source gate, standalone-app build, and embedded-array gate.")
out.append("python3 validate_content.py --ledger")
out.append("python3 -m unittest discover -s tests -v")
out.append("python3 build_content.py")
out.append("python3 validate_content.py --embedded")
out.append("node tests/app_parsers.cjs")
out.append("```\n")

out.append("## Per-chapter units\n")
out.append("| Ch | Unit | Pages | Question range | Count |")
out.append("|---:|---|---|---|---:|")
for c in chapters_data:
    for u in c["units"]:
        q_start, q_end = u["qs"][0], u["qs"][-1]
        pages_in_unit = sorted({next(q["page"] for q in c["questions"] if q["id"] == qid) for qid in u["qs"]})
        p_str = f"{pages_in_unit[0]}" if len(pages_in_unit) == 1 else f"{pages_in_unit[0]}–{pages_in_unit[-1]}"
        q_range = f"{q_start}–{q_end}" if q_start != q_end else q_start
        out.append(f"| {c['chapter']} | {u['title']} | {p_str} | {q_range} | {len(u['qs'])} |")

out.append("\n## Full roadmap\n")
out.append("| Ch | Title | Starts | State |")
out.append("|---:|---|---:|---|")
for num, title, start in CHAPTERS:
    state = "**Live**" if num in live else "Soon"
    out.append(f"| {num} | {title} | {start} | {state} |")

(ROOT / "PROGRESS.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"Successfully updated PROGRESS.md: {len(live)} live chapters, {total_q} questions, {total_u} units.")
