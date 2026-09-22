# PULSE Medicine Vol 2 — Progress

Updated 2026-09-22. Single offline HTML quiz for Medicine Vol 2, Book p377–702.

- Repository: `Deva20045/Med-V2`
- Session branch: `arena/01a0c7dc-med-v2`
- Published URL: https://deva20045.github.io/Med-V2/
- Source of truth: `data/chNN.json`; generated deliverable: `pulse-medicine.html`; `index.html` redirects to it.
- Build status: **4 live chapters / 57**, **159 questions / 20 units**. Chapters 5–57 remain `live:false`.

## This release

1. Restored the five absent Chapter 1 audit questions first (the local checkout had 44; commit `fb7a917` was absent). Chapter 1 now has 49, including MED-C1-02/03/20/32/43.
2. Authored Ch2 p383–386 (37 questions / 5 units), Ch3 p387–389 (38 / 4), Ch4 p390–393 (35 / 4).
3. Visual self-audit: **262 educational point-to-question mappings**, no unasked points found in the p383–393 inventory; fixes completed before build.
4. Schema, actual app regex parsers, bijections, unit coverage and book-order validation pass. Build now fails before writing HTML if these regress.
5. Embedded arrays and live flags verified; rebuild is byte-for-byte deterministic.
6. Offline Chromium tests pass at 1280×900 and 390×844: all 159 questions and 20 units, match boards, blanks, correct and wrong answers, citations, unlock order and persisted completion after reload. No JavaScript page errors.

Full evidence: [self-audit and page-by-page ledger](audit/SELF_AUDIT.md), [pre-build validation output](audit/PREBUILD_VALIDATION.txt), [machine-readable inventory](audit/coverage.json).

## Verified PDF → printed-page map

**Printed page numbers are ground truth.** All 103 pages of this copy of `uploads/01.pdf` were rendered with PyMuPDF `Matrix(2,2)` and visually checked. Full explicit mapping and source hash: [PAGE_MAP.md](audit/PAGE_MAP.md), [page-map.json](audit/page-map.json).

- PDF1–12: unnumbered cover, author/title/instructions and Contents. Contents entry numbers are not page numbers of those sheets.
- PDF13–18: 377–382 (Chapter 1 anchors reread).
- PDF19–22: 383–386 (Chapter 2).
- PDF23–25: 387–389 (Chapter 3).
- PDF26–29: 390–393 (Chapter 4), including visual confirmation of 391–393.
- PDF30–103: individually checked headers 394–467.

**Correction:** the previous progress notes claimed shuffled mappings such as PDF31=405 and PDF51=425. Those were inaccurate for this exact upload: PDF31 prints 395 and PDF51 prints 415. Do not infer page identities from those old samples. The verified content run in this copy happens to be sequential.

Uploads 02–05 were not mapped during this audit. Earlier approximate offsets and end-page assumptions for them are not verified evidence; render and read their printed numbers before building later chapters. Do not infer full-volume coverage merely from file counts.

## Schema and order contract

- Chapter: `chapter`, exact roadmap `title`, `pageRange` beginning at the roadmap start, nonempty `questions` and `units`.
- Question: sequential `MED-C<N>-<seq>` IDs; `sec`, integer `page`, `fmt` in recall/fillup/match/truefalse/scenario/oddoneout/numeric/management; `q`; exactly four unique options; integer `ans` 0–3; `exp` ending exactly `(Book pX)` matching `page`.
- Unit: `MED-U<N>-<n>`, `ch`, `n`, `title`, `sec`, a 2–4-line `guide`; `qs` rebuilt from that section in question-array order. Flattened units must exactly equal the full chapter question sequence.
- Fill-up stems contain `____`. Match grammar: `<prompt> — 1) left 2) left … A) right B) right`. No nested reserved item-label tokens. Every option covers all left items; the correct mapping is a bijection.
- True/false has exactly two True and two False options. Answer options shuffle in the app; questions do not.
- Inventory order follows printed page/content blocks. Software checks the inventory’s sequence and references; visual review checks semantic coverage and within-page placement.
- Source discrepancies are explicitly qualified in explanations. Questions are book-study material, not a substitute for current clinical guidelines.

## Build / audit / test workflow

```sh
# Python 3 and Node required for the fail-closed build gate.
python3 validate_content.py --ledger     # print every point before building
python3 -m unittest discover -s tests -v
python3 build_content.py
python3 validate_content.py --embedded

# Optional scan reproduction (virtualenv + pymupdf):
python3 tools/render_audit.py
# Optional browser tests (virtualenv + playwright + installed Chromium):
python3 tests/browser_smoke.py
# Or set CHROMIUM_EXECUTABLE to an available Chromium binary.
```

`tools/render_audit.py` writes ignored `.audit-render/` PNGs; do not commit generated scans, browser binaries, environments or dependencies. Only the standalone HTML is required at runtime; browser tests run with network disabled.

Release workflow: commit and push `arena/01a0c7dc-med-v2`, open a PR to `main`, then `gh pr merge --merge`. Never publish before the visual audit and validation gate are green.

## Per-chapter units

| Ch | Unit | Pages | Question range | Count |
|---:|---|---|---|---:|
| 1 | 1. ECG Interpretation & the QRS Complex | 377 | MED-C1-01–MED-C1-07 | 7 |
| 1 | 2. Route of Depolarisation & Current Flow | 378 | MED-C1-08–MED-C1-13 | 6 |
| 1 | 3. Ventricular Vectors & Chest Lead Positions | 379 | MED-C1-14–MED-C1-22 | 9 |
| 1 | 4. Wide QRS Pathways, Rate & Regularity | 380 | MED-C1-23–MED-C1-26 | 4 |
| 1 | 5. P Wave, PR Segment & PR Interval | 380 | MED-C1-27–MED-C1-36 | 10 |
| 1 | 6. Approach to the QRS & the Limb Leads | 381 | MED-C1-37–MED-C1-41 | 5 |
| 1 | 7. Axis Determination & the QT Interval | 382 | MED-C1-42–MED-C1-49 | 8 |
| 2 | 1. Atrial Enlargement & Corrected QT | 383 | MED-C2-01–MED-C2-07 | 7 |
| 2 | 2. LV Hypertrophy & Leftward Axis | 383–384 | MED-C2-08–MED-C2-15 | 8 |
| 2 | 3. RV Hypertrophy, P-pulmonale & COPD | 384 | MED-C2-16–MED-C2-21 | 6 |
| 2 | 4. Bundle Branch Blocks & Fascicular Patterns | 385 | MED-C2-22–MED-C2-29 | 8 |
| 2 | 5. Sgarbossa Criteria & MI Panels | 385–386 | MED-C2-30–MED-C2-37 | 8 |
| 3 | 1. Cardiac Terminology & Heart-Failure Tables | 387 | MED-C3-01–MED-C3-07 | 7 |
| 3 | 2. Automaticity & Pacemaker Potential | 387–388 | MED-C3-08–MED-C3-17 | 10 |
| 3 | 3. Heart Blocks & Escape Pathways | 388 | MED-C3-18–MED-C3-23 | 6 |
| 3 | 4. Sinus Dysfunction: Causes & ECG Manifestations | 389 | MED-C3-24–MED-C3-38 | 15 |
| 4 | 1. First-Degree AV Block | 390 | MED-C4-01–MED-C4-06 | 6 |
| 4 | 2. Second-Degree Classification & Mobitz Comparison | 390–391 | MED-C4-07–MED-C4-20 | 14 |
| 4 | 3. Infarct Examples & Third-Degree Block | 392 | MED-C4-21–MED-C4-26 | 6 |
| 4 | 4. AV Dissociation Causes & Summary Strips | 393 | MED-C4-27–MED-C4-35 | 9 |

## Full roadmap

| Ch | Title | Starts | State |
|---:|---|---:|---|
| 1 | Introduction to ECG | 377 | Live |
| 2 | Approach to Hypertrophy and Blocks | 383 | Live |
| 3 | SA Nodal Dysfunction | 387 | Live |
| 4 | AV Blocks | 390 | Live |
| 5 | Tachyarrhythmias | 394 | Soon |
| 6 | Atrial Fibrillation and Flutter | 403 | Soon |
| 7 | Ventricular Arrhythmias | 407 | Soon |
| 8 | WPW Syndrome | 413 | Soon |
| 9 | Introduction to ACS | 415 | Soon |
| 10 | ACS - Coronary Circulation | 425 | Soon |
| 11 | ACS - Evaluation and Management | 430 | Soon |
| 12 | Sjogren's Syndrome | 442 | Soon |
| 13 | IgG4 Related Disease | 449 | Soon |
| 14 | SLE - Basic Approach | 452 | Soon |
| 15 | SLE - Diagnosis | 455 | Soon |
| 16 | SLE - Clinical Profile and Management | 458 | Soon |
| 17 | Antiphospholipid Syndrome | 466 | Soon |
| 18 | Systemic Sclerosis | 470 | Soon |
| 19 | Inflammatory Muscle Diseases | 477 | Soon |
| 20 | Sarcoidosis and Mixed Connective Tissue Disease | 484 | Soon |
| 21 | Classification of Vasculitis and Large Vessel Vasculitis | 491 | Soon |
| 22 | Small Vessel Vasculitis | 499 | Soon |
| 23 | Henoch-Schonlein Purpura V/S Cryoglobulinemia | 509 | Soon |
| 24 | Variable Vessel Vasculitis | 514 | Soon |
| 25 | Basic Approach to Arthritis | 519 | Soon |
| 26 | Rheumatoid Arthritis | 521 | Soon |
| 27 | Spondyloarthritis | 532 | Soon |
| 28 | Crystal Arthropathies | 543 | Soon |
| 29 | Adult-Onset Still's Disease and Septic Arthritis | 552 | Soon |
| 30 | Frontal Lobe | 555 | Soon |
| 31 | Praxicons | 560 | Soon |
| 32 | Temporal and Occipital Lobe | 563 | Soon |
| 33 | Language V/S Speech | 566 | Soon |
| 34 | Memory | 569 | Soon |
| 35 | Dementia : Part 1 | 572 | Soon |
| 36 | Dementia : Part 2 | 577 | Soon |
| 37 | Parkinson's Disease | 583 | Soon |
| 38 | Headache | 593 | Soon |
| 39 | Seizure Semiology | 602 | Soon |
| 40 | Generalised Tonic-Clonic Seizure | 608 | Soon |
| 41 | CNS Infections | 613 | Soon |
| 42 | LMN Approach : Part 1 | 618 | Soon |
| 43 | LMN Approach : Part 2 | 624 | Soon |
| 44 | Inherited Neuropathies | 627 | Soon |
| 45 | Guillain-Barre Syndrome | 632 | Soon |
| 46 | LMN Approach : Part 3 | 637 | Soon |
| 47 | Muscular Dystrophies | 642 | Soon |
| 48 | Myasthenia Gravis | 646 | Soon |
| 49 | Amyotrophic Lateral Sclerosis | 650 | Soon |
| 50 | Anatomy of Spinal Cord | 653 | Soon |
| 51 | Diseases of Spinal Cord | 660 | Soon |
| 52 | Multiple Sclerosis | 668 | Soon |
| 53 | Vascular Anatomy of Brain | 674 | Soon |
| 54 | Approach to UMN Lesion | 681 | Soon |
| 55 | Approach to Stroke | 686 | Soon |
| 56 | Brainstem Stroke | 691 | Soon |
| 57 | Management of Stroke | 700 | Soon |
