# PULSE Medicine Vol 2 — Progress

Updated 2026-09-22. Single offline HTML quiz for Medicine Vol 2, Book p377–702.

- Repository: `Deva20045/Med-V2`
- Session branch: `arena/01a0c840-med-v2`
- Published URL: https://deva20045.github.io/Med-V2/
- Source of truth: `data/chNN.json`; generated deliverable: `pulse-medicine.html`; `index.html` redirects to it.
- Build status: **8 live chapters / 57**, **294 questions / 34 units**. Chapters 9–57 remain `live:false`.

## This release (Chapters 5–8)

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

## Verified PDF → printed-page map

**Printed page numbers are ground truth.** All 103 pages of this copy of `uploads/01.pdf` were rendered with PyMuPDF `Matrix(2,2)` and visually checked. Full explicit mapping and source hash: [PAGE_MAP.md](audit/PAGE_MAP.md), [page-map.json](audit/page-map.json).

- PDF1–12: unnumbered front-matter and Contents.
- PDF13–18: 377–382 (Chapter 1).
- PDF19–22: 383–386 (Chapter 2).
- PDF23–25: 387–389 (Chapter 3).
- PDF26–29: 390–393 (Chapter 4).
- PDF30–38: 394–402 (Chapter 5: Tachyarrhythmias).
- PDF39–42: 403–406 (Chapter 6: Atrial Fibrillation and Flutter).
- PDF43–48: 407–412 (Chapter 7: Ventricular Arrhythmias).
- PDF49–50: 413–414 (Chapter 8: WPW Syndrome).
- PDF51–103: 415–467 (Chapter 9 onwards).

## Schema and order contract

- Chapter: `chapter`, exact roadmap `title`, `pageRange` beginning at the roadmap start, nonempty `questions` and `units`.
- Question: sequential `MED-C<N>-<seq>` IDs; `sec`, integer `page`, `fmt` in recall/fillup/match/truefalse/scenario/oddoneout/numeric/management; `q`; exactly four unique options; integer `ans` 0–3; `exp` ending exactly `(Book pX)` matching `page`.
- Unit: `MED-U<N>-<n>`, `ch`, `n`, `title`, `sec`, a 2–4-line `guide`; `qs` rebuilt from that section in question-array order. Flattened units must exactly equal the full chapter question sequence.
- Fill-up stems contain `____`. Match grammar: `<prompt> — 1) left 2) left … A) right B) right`. No nested reserved item-label tokens. Every option covers all left items; the correct mapping is a bijection.
- True/false has exactly two True and two False options. Answer options shuffle in the app; questions do not.
- Inventory order follows printed page/content blocks. Software checks the inventory's sequence and references; visual review checks semantic coverage and within-page placement.
- Source discrepancies are explicitly qualified in explanations. Questions are book-study material, not a substitute for current clinical guidelines.

## Build / audit / test workflow

```sh
# Python 3 and Node required for the fail-closed build gate.
python3 validate_content.py --ledger     # print every point before building
python3 -m unittest discover -s tests -v
python3 build_content.py
python3 validate_content.py --embedded
```

## Per-chapter units

| Ch | Unit | Pages | Question range | Count |
|---:|---|---|---|---:|
| 1 | ECG Interpretation & the QRS Complex | 377 | MED-C1-01–MED-C1-07 | 7 |
| 1 | Route of Depolarisation & Current Flow | 378 | MED-C1-08–MED-C1-13 | 6 |
| 1 | Ventricular Vectors & Chest Lead Positions | 379 | MED-C1-14–MED-C1-22 | 9 |
| 1 | Wide QRS Pathways, Rate & Regularity | 380 | MED-C1-23–MED-C1-26 | 4 |
| 1 | P Wave, PR Segment & PR Interval | 380 | MED-C1-27–MED-C1-36 | 10 |
| 1 | Approach to the QRS & the Limb Leads | 381 | MED-C1-37–MED-C1-41 | 5 |
| 1 | Axis Determination & the QT Interval | 382 | MED-C1-42–MED-C1-49 | 8 |
| 2 | Atrial Enlargement & Corrected QT | 383 | MED-C2-01–MED-C2-07 | 7 |
| 2 | LV Hypertrophy & Leftward Axis | 383–384 | MED-C2-08–MED-C2-15 | 8 |
| 2 | RV Hypertrophy, P-pulmonale & COPD | 384 | MED-C2-16–MED-C2-21 | 6 |
| 2 | Bundle Branch Blocks & Fascicular Patterns | 385 | MED-C2-22–MED-C2-29 | 8 |
| 2 | Sgarbossa Criteria & MI Panels | 385–386 | MED-C2-30–MED-C2-37 | 8 |
| 3 | Cardiac Terminology & Heart-Failure Tables | 387 | MED-C3-01–MED-C3-07 | 7 |
| 3 | Automaticity & Pacemaker Potential | 387–388 | MED-C3-08–MED-C3-17 | 10 |
| 3 | Heart Blocks & Escape Pathways | 388 | MED-C3-18–MED-C3-23 | 6 |
| 3 | Sinus Dysfunction: Causes & ECG Manifestations | 389 | MED-C3-24–MED-C3-38 | 15 |
| 4 | First-Degree AV Block | 390 | MED-C4-01–MED-C4-06 | 6 |
| 4 | Second-Degree Classification & Mobitz Comparison | 390–391 | MED-C4-07–MED-C4-20 | 14 |
| 4 | Infarct Examples & Third-Degree Block | 392 | MED-C4-21–MED-C4-26 | 6 |
| 4 | AV Dissociation Causes & Summary Strips | 393 | MED-C4-27–MED-C4-35 | 9 |
| 5 | 1. Classification & Mechanisms of Tachycardia | 394–395 | MED-C5-01–MED-C5-14 | 14 |
| 5 | 2. AVNRT Mechanisms, Types & ECG Features | 396–398 | MED-C5-15–MED-C5-28 | 14 |
| 5 | 3. AVRT vs AVNRT & Narrow-Complex Differentiation | 399 | MED-C5-29–MED-C5-34 | 6 |
| 5 | 4. Acute Management of Narrow-Complex Tachycardias | 400 | MED-C5-35–MED-C5-43 | 9 |
| 5 | 5. Atrial & Junctional Tachycardias & Diagnostic Summary | 401–402 | MED-C5-44–MED-C5-52 | 9 |
| 6 | 1. Atrial Fibrillation Features, Classification & Etiology | 403 | MED-C6-01–MED-C6-11 | 11 |
| 6 | 2. Investigations, Algorithmic Pathway & Cardioversion | 404 | MED-C6-12–MED-C6-19 | 8 |
| 6 | 3. Pharmacotherapy, Risk Scores & Anticoagulation | 405 | MED-C6-20–MED-C6-28 | 9 |
| 6 | 4. Atrial Flutter Mechanisms & Management | 406 | MED-C6-29–MED-C6-33 | 5 |
| 7 | 1. Broad QRS Mechanisms & Premature Complexes | 407–408 | MED-C7-01–MED-C7-15 | 15 |
| 7 | 2. Warning Signs, Monomorphic VT & Diagnostic Signs | 409–410 | MED-C7-16–MED-C7-27 | 12 |
| 7 | 3. Polymorphic VT, Torsades de Pointes & Defibrillation | 411–412 | MED-C7-28–MED-C7-36 | 9 |
| 8 | 1. Pathophysiology, ECG Manifestations & Types | 413 | MED-C8-01–MED-C8-06 | 6 |
| 8 | 2. Vector Differentiation & Algorithmic Management | 414 | MED-C8-07–MED-C8-14 | 8 |

## Full roadmap

| Ch | Title | Starts | State |
|---:|---|---:|---|
| 1 | Introduction to ECG | 377 | Live |
| 2 | Approach to Hypertrophy and Blocks | 383 | Live |
| 3 | SA Nodal Dysfunction | 387 | Live |
| 4 | AV Blocks | 390 | Live |
| 5 | Tachyarrhythmias | 394 | Live |
| 6 | Atrial Fibrillation and Flutter | 403 | Live |
| 7 | Ventricular Arrhythmias | 407 | Live |
| 8 | WPW Syndrome | 413 | Live |
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
