#!/usr/bin/env python3
"""Embed the chapter JSON artifacts into the standalone PULSE Medicine Vol 2 app.

The browser app is intentionally a single offline HTML file. Structured chapter
artifacts in data/chNN.json are the editable source of truth; run this script
whenever a chapter artifact changes. Chapters without an artifact remain on
the roadmap as "Soon" (live: false).
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APP_PATH = ROOT / "pulse-medicine.html"
DATA_PATH = ROOT / "data"

# Full Volume-2 roadmap (Book p377-702) from the book's Contents pages,
# cross-verified against the scanned chapter title pages. Number, title,
# starting Book page. The "p" shown on the roadmap is the starting page.
CHAPTERS = [
    (1, "Introduction to ECG", 377),
    (2, "Approach to Hypertrophy and Blocks", 383),
    (3, "SA Nodal Dysfunction", 387),
    (4, "AV Blocks", 390),
    (5, "Tachyarrhythmias", 394),
    (6, "Atrial Fibrillation and Flutter", 403),
    (7, "Ventricular Arrhythmias", 407),
    (8, "WPW Syndrome", 413),
    (9, "Introduction to ACS", 415),
    (10, "ACS - Coronary Circulation", 425),
    (11, "ACS - Evaluation and Management", 430),
    (12, "Sjogren's Syndrome", 442),
    (13, "IgG4 Related Disease", 449),
    (14, "SLE - Basic Approach", 452),
    (15, "SLE - Diagnosis", 455),
    (16, "SLE - Clinical Profile and Management", 458),
    (17, "Antiphospholipid Syndrome", 466),
    (18, "Systemic Sclerosis", 470),
    (19, "Inflammatory Muscle Diseases", 477),
    (20, "Sarcoidosis and Mixed Connective Tissue Disease", 484),
    (21, "Classification of Vasculitis and Large Vessel Vasculitis", 491),
    (22, "Small Vessel Vasculitis", 499),
    (23, "Henoch-Schonlein Purpura V/S Cryoglobulinemia", 509),
    (24, "Variable Vessel Vasculitis", 514),
    (25, "Basic Approach to Arthritis", 519),
    (26, "Rheumatoid Arthritis", 521),
    (27, "Spondyloarthritis", 532),
    (28, "Crystal Arthropathies", 543),
    (29, "Adult-Onset Still's Disease and Septic Arthritis", 552),
    (30, "Frontal Lobe", 555),
    (31, "Praxicons", 560),
    (32, "Temporal and Occipital Lobe", 563),
    (33, "Language V/S Speech", 566),
    (34, "Memory", 569),
    (35, "Dementia : Part 1", 572),
    (36, "Dementia : Part 2", 577),
    (37, "Parkinson's Disease", 583),
    (38, "Headache", 593),
    (39, "Seizure Semiology", 602),
    (40, "Generalised Tonic-Clonic Seizure", 608),
    (41, "CNS Infections", 613),
    (42, "LMN Approach : Part 1", 618),
    (43, "LMN Approach : Part 2", 624),
    (44, "Inherited Neuropathies", 627),
    (45, "Guillain-Barre Syndrome", 632),
    (46, "LMN Approach : Part 3", 637),
    (47, "Muscular Dystrophies", 642),
    (48, "Myasthenia Gravis", 646),
    (49, "Amyotrophic Lateral Sclerosis", 650),
    (50, "Anatomy of Spinal Cord", 653),
    (51, "Diseases of Spinal Cord", 660),
    (52, "Multiple Sclerosis", 668),
    (53, "Vascular Anatomy of Brain", 674),
    (54, "Approach to UMN Lesion", 681),
    (55, "Approach to Stroke", 686),
    (56, "Brainstem Stroke", 691),
    (57, "Management of Stroke", 700),
]


def compact(value: object) -> str:
    """Use compact, UTF-8 JSON so the standalone app remains easy to ship."""
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def between(text: str, start: str, end: str) -> tuple[int, int]:
    first = text.index(start)
    second = text.index(end, first)
    return first, second


def main() -> None:
    # Fail before touching the offline HTML if schema, inventory or app parsing
    # regresses. The visual self-audit is recorded separately in audit/SELF_AUDIT.md.
    from validate_content import validate_all
    validate_all()

    questions: list[dict] = []
    units: list[dict] = []
    live: dict[int, dict] = {}

    for number, title, start_page in CHAPTERS:
        path = DATA_PATH / f"ch{number:02d}.json"
        if not path.exists():
            continue
        chapter = json.loads(path.read_text(encoding="utf-8"))
        if chapter["chapter"] != number:
            raise ValueError(f"{path.name}: chapter number does not match filename")
        if chapter["title"] != title:
            raise ValueError(
                f"{path.name}: expected title {title!r}, got {chapter['title']!r}"
            )
        first = int(chapter["pageRange"].split("-", 1)[0])
        if first != start_page:
            raise ValueError(
                f"{path.name}: pageRange starts at {first}, expected {start_page}"
            )
        questions.extend(chapter["questions"])
        units.extend(chapter["units"])
        live[number] = chapter

    html = APP_PATH.read_text(encoding="utf-8")
    q_start, _ = between(html, "const QUESTIONS = ", "\nconst UNITS = ")
    u_start, _ = between(html, "const UNITS = ", "\nconst CHAPTERS = ")
    c_start, c_end = between(html, "const CHAPTERS = ", "\nconst QBYID = ")

    roadmap = []
    for number, title, start_page in CHAPTERS:
        if number in live:
            first = int(live[number]["pageRange"].split("-", 1)[0])
            roadmap.append({"n": number, "t": title, "p": first, "live": True})
        else:
            roadmap.append({"n": number, "t": title, "p": start_page, "live": False})

    html = (
        html[:q_start]
        + "const QUESTIONS = "
        + compact(questions)
        + ";\nconst UNITS = "
        + compact(units)
        + ";\nconst CHAPTERS = "
        + json.dumps(roadmap, ensure_ascii=False, indent=2)
        + ";"
        + html[c_end:]
    )
    APP_PATH.write_text(html, encoding="utf-8")
    live_count = len(live)
    print(
        f"Embedded {len(questions)} questions and {len(units)} units across "
        f"{live_count} live chapter(s) of {len(CHAPTERS)} roadmap chapters "
        f"in {APP_PATH.name}."
    )


if __name__ == "__main__":
    main()
