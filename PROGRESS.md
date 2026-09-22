# PULSE Medicine Vol 2 — Progress

Updated **2026-09-22**. Standalone offline quiz based on *PULSE Medicine Vol 2*, printed Book p377–702.

- Repository: `Deva20045/Med-V2`
- Session branch: `arena/01a0c857-med-v2`
- Published URL: https://deva20045.github.io/Med-V2/
- Editable source of truth: `data/chNN.json`; generated offline deliverable: `pulse-medicine.html`; `index.html` redirects to it.
- **Build status: 15 live chapters / 57 · 570 questions / 55 units.** Chapters 16–57 remain `live:false`.

## This release — Chapters 9–15

Seven consecutive chapters have been written, visual-audited from the scans, source-ordered, and made live:

| Ch | Title | Printed pages | Questions | Units |
|---:|---|---:|---:|---:|
| 9 | Introduction to ACS | 415–424 | 55 | 4 |
| 10 | ACS - Coronary Circulation | 425–429 | 29 | 3 |
| 11 | ACS - Evaluation and Management | 430–441 | 72 | 4 |
| 12 | Sjogren's Syndrome | 442–448 | 47 | 3 |
| 13 | IgG4 Related Disease | 449–451 | 23 | 2 |
| 14 | SLE - Basic Approach | 452–454 | 18 | 2 |
| 15 | SLE - Diagnosis | 455–457 | 32 | 3 |
| **Release total** |  | **43 pages** | **276** | **21** |

### Quality and ordering contract delivered

1. All pages were read in printed order (PDF51–93 = Book p415–457), including flowchart arms, comparison tables, numeric thresholds, diagrams, notes, morphology panels, contraindications and treatment branches.
2. Every source-mapped learning target has a four-option, citation-backed question in `audit/coverage.json`; Chapters 9–15 add **276 ordered mappings**, bringing the audited ledger to **678 mappings** for Chapters 2–15. Every target is marked asked.
3. New questions are reasoning-first: **no fill-up or matching worksheets** in Chapters 9–15. Scenarios, mechanism-based recall, numeric interpretation, management decisions and discriminating odd-one-out cases use plausible medical distractors.
4. IDs are sequential, question arrays remain strictly nondecreasing in book page, unit question lists are exact contiguous slices of source order, and every explanation ends with its exact `(Book pX)` citation.
5. Source-specific algorithms, medication doses, clinical thresholds and historical terminology are retained as book-study material and qualified in the audit; they are not a replacement for current local clinical guidance.
6. Chapters 9–15 are embedded in the standalone app and all seven roadmap flags are live.

Full evidence: [visual audit and page-by-page ledger](audit/SELF_AUDIT.md), [machine-readable inventory](audit/coverage.json), [verified PDF-page map](audit/PAGE_MAP.md), and [pre-build validation output](audit/PREBUILD_VALIDATION.txt).

## Verified PDF → printed-page map

Printed page numbers are ground truth. Every sheet of `uploads/01.pdf` was rendered at 2× and checked visually. The verified source is sequential after 12 unnumbered front-matter sheets; full mapping and hash are in [PAGE_MAP.md](audit/PAGE_MAP.md).

- PDF13–18: Book p377–382 (Ch1)
- PDF19–29: p383–393 (Ch2–4)
- PDF30–38: p394–402 (Ch5)
- PDF39–42: p403–406 (Ch6)
- PDF43–48: p407–412 (Ch7)
- PDF49–50: p413–414 (Ch8)
- **PDF51–60: p415–424 (Ch9)**
- **PDF61–65: p425–429 (Ch10)**
- **PDF66–77: p430–441 (Ch11)**
- **PDF78–84: p442–448 (Ch12)**
- **PDF85–87: p449–451 (Ch13)**
- **PDF88–90: p452–454 (Ch14)**
- **PDF91–93: p455–457 (Ch15)**
- PDF94–103: p458–467 (Ch16 onward)

## Schema and order contract

- Chapter: exact roadmap number/title, `pageRange` starts at the roadmap page, nonempty `questions` and `units`.
- Question: sequential `MED-C<N>-<seq>` ID; section/page/format/stem; exactly four unique options; one answer; explanation ending exactly `(Book pX)` matching `page`.
- Units: sequential `MED-U<N>-<n>` IDs; each has a 2–4-line guide; its IDs are rebuilt from exactly one section in original question order; flattened units equal the full chapter sequence.
- Questions are in printed book-page order; all printed pages in every live chapter are represented.
- The source-order inventory is fail-closed: the validator requires a ledger mapping for every question in audited Chapters 2–15, in exact question order and with matching book page.
- Questions are educational book-study material, not a substitute for current clinical guidelines or patient care.

## Build, audit and test workflow

```sh
# Generate/edit chapters 9–15 only when source artefacts need regeneration.
python3 tools/generate_ch09_15.py
python3 tools/generate_ch09_15_audit.py
python3 tools/generate_self_audit.py

# Fail-closed source gate, standalone-app build, and embedded-array gate.
python3 validate_content.py --ledger
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
| 9 | 1. ACS Mechanism, Vascular Beds & Cardiac Syndromes | 415 | MED-C9-01–MED-C9-06 | 6 |
| 9 | 2. ACS Risk, Prevention & Chronic Stable Angina | 416–418 | MED-C9-07–MED-C9-24 | 18 |
| 9 | 3. Imaging, Stable-Angina Therapy & ST-Segment Foundations | 419–422 | MED-C9-25–MED-C9-45 | 21 |
| 9 | 4. ST Depression, T-Waves & ACS Mimics | 423–424 | MED-C9-46–MED-C9-55 | 10 |
| 10 | 1. Coronary Territories, Dominance & Right Coronary Artery | 425–426 | MED-C10-01–MED-C10-13 | 13 |
| 10 | 2. Inferior MI Localisation & Left Coronary Anatomy | 427 | MED-C10-14–MED-C10-20 | 7 |
| 10 | 3. LAD Localisation, Left-Main Occlusion & Complications | 428–429 | MED-C10-21–MED-C10-29 | 9 |
| 11 | 1. Universal MI Definition, Injury & MI Types | 430–431 | MED-C11-01–MED-C11-11 | 11 |
| 11 | 2. Reinfarction, Vulnerable Plaque & NSTEMI Recognition | 432–433 | MED-C11-12–MED-C11-21 | 10 |
| 11 | 3. Acute Chest Pain, STEMI Salvage & Reperfusion Timing | 434–436 | MED-C11-22–MED-C11-38 | 17 |
| 11 | 4. Thrombolysis, PCI, Antithrombotics & STEMI Complications | 437–441 | MED-C11-39–MED-C11-72 | 34 |
| 12 | 1. Classification, Association & Pathogenesis | 442–443 | MED-C12-01–MED-C12-11 | 11 |
| 12 | 2. Histology & Glandular Clinical Features | 444–445 | MED-C12-12–MED-C12-26 | 15 |
| 12 | 3. Extraglandular Disease, Investigations & Classification | 446–448 | MED-C12-27–MED-C12-47 | 21 |
| 13 | 1. IgG4 Biology, Pathology & Core Clinical Profile | 449 | MED-C13-01–MED-C13-08 | 8 |
| 13 | 2. Organ Manifestations, Diagnosis & Treatment | 450–451 | MED-C13-09–MED-C13-23 | 15 |
| 14 | 1. SLE Profile & Clinical Phenotypes | 452–453 | MED-C14-01–MED-C14-11 | 11 |
| 14 | 2. Genetic & Environmental Etiology | 454 | MED-C14-12–MED-C14-18 | 7 |
| 15 | 1. ANA Methodology, Titre & Pattern Interpretation | 455 | MED-C15-01–MED-C15-11 | 11 |
| 15 | 2. ANA Profile, DILE & Clinical Approach | 456 | MED-C15-12–MED-C15-18 | 7 |
| 15 | 3. SLE Antibodies, Prognosis & Activity | 457 | MED-C15-19–MED-C15-32 | 14 |

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
| 9 | Introduction to ACS | 415 | **Live** |
| 10 | ACS - Coronary Circulation | 425 | **Live** |
| 11 | ACS - Evaluation and Management | 430 | **Live** |
| 12 | Sjogren's Syndrome | 442 | **Live** |
| 13 | IgG4 Related Disease | 449 | **Live** |
| 14 | SLE - Basic Approach | 452 | **Live** |
| 15 | SLE - Diagnosis | 455 | **Live** |
| 16–57 | Remaining Volume 2 roadmap | 458–700 | Soon |
