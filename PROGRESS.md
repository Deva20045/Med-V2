# PULSE Medicine Vol 2 — Progress

Updated 2026-09-23. Single offline HTML quiz for Medicine Vol 2, Book p377–702.

- Repository: `Deva20045/Med-V2`
- Session branch: `arena/01a0cd1a-med-v2`
- Source of truth: `data/chNN.json`; generated deliverable: `pulse-medicine.html`; `index.html` redirects to it.
- Build status after this release: **21 live chapter artifacts / 57 roadmap chapters**, **828 questions / 70 units**.
- Chapters 16–20 are not present as authored chapter JSON in this checkout; this release therefore makes the requested **Chapters 21–26** live without authoring out-of-scope Chapters 16–20.

## This release — Chapters 21–26

Six requested rheumatology/immunology chapters have been written, visually audited from scanned Book p491–531, source-ordered, and made live:

| Ch | Title | Printed pages | Questions | Units |
|---:|---|---:|---:|---:|
| 21 | Classification of Vasculitis and Large Vessel Vasculitis | 491–498 | 44 | 3 |
| 22 | Small Vessel Vasculitis | 499–508 | 52 | 3 |
| 23 | Henoch-Schonlein Purpura V/S Cryoglobulinemia | 509–513 | 26 | 2 |
| 24 | Variable Vessel Vasculitis | 514–518 | 36 | 2 |
| 25 | Basic Approach to Arthritis | 519–520 | 11 | 1 |
| 26 | Rheumatoid Arthritis | 521–531 | 80 | 4 |
| **Release total** |  | **41 pages** | **249** | **15** |

### Quality and ordering contract delivered

1. Printed pages p491–531 were rendered at 2× and read visually in strict book order, including headings, bullets, sub-bullets, notes, comparison tables, criteria, flowchart arms, diagrams, thresholds, doses, contraindications and treatment branches.
2. Every recorded Chapter 21–26 learning target maps to an explicit question ID in `audit/coverage.json`; the release adds **249 ordered mappings**, bringing the ledger to **936 mapped points**. Unasked points in the recorded visual inventory: **NONE**.
3. New Chapter 21–26 questions use only `recall`, `scenario`, `numeric`, `oddoneout` and `management` formats, with four unique options, plausible distractors and exact explanation suffixes ending `(Book pX)`.
4. IDs are sequential (`MED-C21-01` … `MED-C26-80`), question arrays are nondecreasing by printed page, and unit question lists are exact contiguous slices of source order.
5. Source-specific doses, criteria, treatment algorithms and historical terminology are retained as book-study material; they are not a substitute for current patient-specific clinical guidance.
6. Chapters 21–26 are embedded in the standalone offline app and their roadmap flags are live.

Full evidence: [visual audit](audit/SELF_AUDIT.md), [machine-readable inventory](audit/coverage.json), [verified page map](audit/PAGE_MAP.md), and [pre-build validation output](audit/PREBUILD_VALIDATION.txt).

## Source scope and page map

Printed page numbers are ground truth. The user-specified source for this release is `uploads/02.pdf` with the prior verified convention of 12 unnumbered front-matter pages and visual 2× renders only. The audited release scope is:

- Ch21: Book p491–498
- Ch22: Book p499–508
- Ch23: Book p509–513
- Ch24: Book p514–518
- Ch25: Book p519–520
- Ch26: Book p521–531
- Next chapter starts at Book p532 and was not authored in this scope.

## Schema and order contract

- Chapter: exact roadmap number/title, `pageRange` starts at the roadmap page, nonempty `questions` and `units`.
- Question: sequential `MED-C<N>-<seq>` ID; section/page/format/stem; exactly four unique options; one answer; explanation ending exactly `(Book pX)` matching `page`.
- Units: sequential `MED-U<N>-<n>` IDs; each has a 2–4-line guide; `qs` is rebuilt from exactly one section in original question order; flattened units equal the full chapter sequence.
- Questions are in printed book-page order; all printed pages in every live chapter artifact are represented.
- The source-order inventory is fail-closed for audited chapters 2–15 and 21–26.

## Build, audit and test workflow

```sh
python3 tools/generate_ch21_26.py
python3 tools/generate_ch09_15_audit.py
python3 tools/generate_self_audit.py
python3 validate_content.py --ledger
python3 -m unittest discover -s tests -v
python3 build_content.py
python3 validate_content.py --embedded
node tests/app_parsers.cjs
```

## Per-chapter units

| Ch | Unit | Pages | Question range | Count |
|---:|---|---|---|---:|
| 21 | 1. Vasculitis definition and Chapel-Hill vessel-size classification | 491–493 | MED-C21-01–MED-C21-15 | 15 |
| 21 | 2. Giant cell arteritis and PMR | 493–495 | MED-C21-16–MED-C21-32 | 17 |
| 21 | 3. Takayasu arteritis | 496–498 | MED-C21-33–MED-C21-44 | 12 |
| 22 | 1. ANCA biology, testing and skin-vessel clinical framework | 499–501 | MED-C22-01–MED-C22-15 | 15 |
| 22 | 2. GPA and MPA manifestations, management and classification | 501–505 | MED-C22-16–MED-C22-33 | 18 |
| 22 | 3. EGPA and PAN | 505–508 | MED-C22-34–MED-C22-52 | 19 |
| 23 | 1. Immune-complex small-vessel vasculitis and HSP | 509–511 | MED-C23-01–MED-C23-14 | 14 |
| 23 | 2. Cryoglobulinemia | 512–513 | MED-C23-15–MED-C23-26 | 12 |
| 24 | 1. Behcet disease classification, criteria and manifestations | 514–517 | MED-C24-01–MED-C24-27 | 27 |
| 24 | 2. Diagnosis, treatment and Cogan syndrome | 518 | MED-C24-28–MED-C24-36 | 9 |
| 25 | 1. Differentiating arthritis patterns and inflammatory arthritis | 519–520 | MED-C25-01–MED-C25-11 | 11 |
| 26 | 1. RA diagnosis duration, joint involvement and etiopathogenesis | 521–523 | MED-C26-01–MED-C26-22 | 22 |
| 26 | 2. RA prediction markers, clinical manifestations and deformities | 524–526 | MED-C26-23–MED-C26-43 | 21 |
| 26 | 3. Extra-articular RA and RA versus SLE | 527–529 | MED-C26-44–MED-C26-61 | 18 |
| 26 | 4. RA management | 530–531 | MED-C26-62–MED-C26-80 | 19 |

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
| 9 | Introduction to ACS | 415 | Live |
| 10 | ACS - Coronary Circulation | 425 | Live |
| 11 | ACS - Evaluation and Management | 430 | Live |
| 12 | Sjogren's Syndrome | 442 | Live |
| 13 | IgG4 Related Disease | 449 | Live |
| 14 | SLE - Basic Approach | 452 | Live |
| 15 | SLE - Diagnosis | 455 | Live |
| 16 | SLE - Clinical Profile and Management | 458 | Soon |
| 17 | Antiphospholipid Syndrome | 466 | Soon |
| 18 | Systemic Sclerosis | 470 | Soon |
| 19 | Inflammatory Muscle Diseases | 477 | Soon |
| 20 | Sarcoidosis and Mixed Connective Tissue Disease | 484 | Soon |
| 21 | Classification of Vasculitis and Large Vessel Vasculitis | 491 | Live |
| 22 | Small Vessel Vasculitis | 499 | Live |
| 23 | Henoch-Schonlein Purpura V/S Cryoglobulinemia | 509 | Live |
| 24 | Variable Vessel Vasculitis | 514 | Live |
| 25 | Basic Approach to Arthritis | 519 | Live |
| 26 | Rheumatoid Arthritis | 521 | Live |
| 27–57 | Remaining Volume 2 roadmap | 532–700 | Soon |
