# PULSE Medicine Vol 2 — Progress

Updated **2026-09-23**. Standalone offline quiz based on *PULSE Medicine Vol 2*, printed Book p377–702.

- Repository: `Deva20045/Med-V2`
- Session branch: `arena/01a0cd13-med-v2`
- Published URL: https://deva20045.github.io/Med-V2/
- Editable source of truth: `data/chNN.json`; generated offline deliverable: `pulse-medicine.html`; `index.html` redirects to it.
- **Build status: 20 live chapters / 57 · 847 questions / 87 units.** Chapters 21–57 remain `live:false`.

## This release — Chapters 16–20

Five consecutive rheumatology chapters were rendered from the scans, read block by block, source-ordered and made live:

| Ch | Title | Printed pages | Questions | Units |
|---:|---|---:|---:|---:|
| 16 | SLE - Clinical Profile and Management | 458–465 | 74 | 7 |
| 17 | Antiphospholipid Syndrome | 466–469 | 35 | 4 |
| 18 | Systemic Sclerosis | 470–476 | 50 | 7 |
| 19 | Inflammatory Muscle Diseases | 477–483 | 57 | 7 |
| 20 | Sarcoidosis and Mixed Connective Tissue Disease | 484–490 | 52 | 7 |
| **Release total** |  | **33 pages** | **268** | **32** |

### Quality and ordering contract delivered

1. All pages were read in printed order (`uploads/01.pdf` PDF94–103 = Book p458–467 and `uploads/02.pdf` PDF1–23 = Book p468–490), including flowchart arms, comparison tables, numeric thresholds, morphology images, rotated annotations, notes, management ladders and drug doses.
2. Every source-mapped learning target has a four-option, citation-backed question in `audit/coverage.json`; Chapters 16–20 add **268 ordered mappings**, bringing the audited ledger to **955 mappings** for Chapters 2–20. Every target is marked asked.
   Chapters 16–20 are unusually dense (a six-class lupus-nephritis table, the weighted EULAR/ACR domain table, two management ladders with doses, four antibody-to-organ tables and three comparison tables), so the block-by-block inventory resolved into more discrete printed points than the 120–150 planning estimate; no point was dropped to meet a round number.
3. New questions are reasoning-first: **no fill-up or matching worksheets** in Chapters 9–20. Scenarios, mechanism-based recall, numeric interpretation, management decisions and discriminating odd-one-out cases use plausible medical distractors.
4. IDs are sequential, question arrays remain strictly nondecreasing in book page, unit question lists are exact contiguous slices of source order, and every explanation ends with its exact `(Book pX)` citation.
5. Source-specific algorithms, medication doses, clinical thresholds and historical terminology are retained as book-study material and qualified in the audit; they are not a replacement for current local clinical guidance.
6. Chapters 16–20 are embedded in the standalone app and all twenty roadmap flags are live.

Full evidence: [visual audit and page-by-page ledger](audit/SELF_AUDIT.md), [machine-readable inventory](audit/coverage.json), [verified PDF-page map](audit/PAGE_MAP.md) and [pre-build validation output](audit/PREBUILD_VALIDATION.txt).

## Verified PDF → printed-page map

Printed page numbers are ground truth. Every sheet used so far was rendered at 2× and checked visually. `uploads/01.pdf` is sequential after 12 unnumbered front-matter sheets; `uploads/02.pdf` continues the same volume at Book p468. Full mappings and hashes are in [PAGE_MAP.md](audit/PAGE_MAP.md), [page-map.json](audit/page-map.json) and [page-map-02.json](audit/page-map-02.json).

- PDF13–18: Book p377–382 (Ch1)
- PDF19–29: p383–393 (Ch2–4)
- PDF30–38: p394–402 (Ch5)
- PDF39–42: p403–406 (Ch6)
- PDF43–48: p407–412 (Ch7)
- PDF49–50: p413–414 (Ch8)
- PDF51–60: p415–424 (Ch9)
- PDF61–65: p425–429 (Ch10)
- PDF66–77: p430–441 (Ch11)
- PDF78–84: p442–448 (Ch12)
- PDF85–87: p449–451 (Ch13)
- PDF88–90: p452–454 (Ch14)
- PDF91–93: p455–457 (Ch15)
- **PDF94–101: p458–465 (Ch16)**
- **PDF102–103 + 02.pdf PDF1–2: p466–469 (Ch17)**
- **02.pdf PDF3–9: p470–476 (Ch18)**
- **02.pdf PDF10–16: p477–483 (Ch19)**
- **02.pdf PDF17–23: p484–490 (Ch20)**
- 02.pdf PDF24 onward: p491+ (Ch21 onward, not yet live)

## Schema and order contract

- Chapter: exact roadmap number/title, `pageRange` starts at the roadmap page, nonempty `questions` and `units`.
- Question: sequential `MED-C<N>-<seq>` ID; section/page/format/stem; exactly four unique options; one answer; explanation ending exactly `(Book pX)` matching `page`.
- Units: sequential `MED-U<N>-<n>` IDs; each has a 2–4-line guide; its IDs are rebuilt from exactly one section in original question order; flattened units equal the full chapter sequence.
- Questions are in printed book-page order; all printed pages in every live chapter are represented.
- The source-order inventory is fail-closed: the validator requires a ledger mapping for every question in audited Chapters 2–20, in exact question order and with matching book page.
- Questions are educational book-study material, not a substitute for current clinical guidelines or patient care.

## Build, audit and test workflow

```sh
# Generate/edit chapter artifacts only when source artefacts need regeneration.
python3 tools/generate_ch09_15.py        # Chapters 9-15
python3 tools/generate_ch16_20.py        # Chapters 16-20
python3 tools/generate_ch09_15_audit.py  # rebuild the source-order ledger (Ch9-20)
python3 tools/generate_self_audit.py     # rebuild audit/SELF_AUDIT.md

# Fail-closed source gate, standalone-app build, and embedded-array gate.
python3 validate_content.py --ledger
python3 -m unittest discover -s tests -v
python3 build_content.py
python3 validate_content.py --embedded
node tests/app_parsers.cjs
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
| 9 | 1. ACS Mechanism, Vascular Beds & Cardiac Syndromes | 415 | MED-C9-01–MED-C9-07 | 7 |
| 9 | 2. ACS Risk, Prevention & Chronic Stable Angina | 416–418 | MED-C9-08–MED-C9-29 | 22 |
| 9 | 3. Imaging, Stable-Angina Therapy & ST-Segment Foundations | 419–422 | MED-C9-30–MED-C9-55 | 26 |
| 9 | 4. ST Depression, T-Waves & ACS Mimics | 423–424 | MED-C9-56–MED-C9-64 | 9 |
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
| 16 | 1. Constitutional & Cutaneous Manifestations | 458–459 | MED-C16-01–MED-C16-14 | 14 |
| 16 | 2. Musculoskeletal, Organ & System Involvement | 460 | MED-C16-15–MED-C16-24 | 10 |
| 16 | 3. Haematological, Lung, Cardiac, GI & Renal | 461 | MED-C16-25–MED-C16-36 | 12 |
| 16 | 4. Lupus Nephritis Classification & Histology | 462 | MED-C16-37–MED-C16-42 | 6 |
| 16 | 5. CNS Involvement & SLE Classification Criteria | 462–463 | MED-C16-43–MED-C16-55 | 13 |
| 16 | 6. Treat-to-Target, Induction & Maintenance Therapy | 464–465 | MED-C16-56–MED-C16-70 | 15 |
| 16 | 7. Drug Induced Lupus | 465 | MED-C16-71–MED-C16-74 | 4 |
| 17 | 1. APS Overview, SLE Association & Pathophysiology | 466 | MED-C17-01–MED-C17-06 | 6 |
| 17 | 2. Two-Hit Model, Clinical Features & Thrombophilia | 466–467 | MED-C17-07–MED-C17-17 | 11 |
| 17 | 3. Sapporo Classification & Clinical Criteria | 467–468 | MED-C17-18–MED-C17-24 | 7 |
| 17 | 4. Non-Criteria APS, Catastrophic APS & Management | 468–469 | MED-C17-25–MED-C17-35 | 11 |
| 18 | 1. General Features, Classification & Mimics | 470 | MED-C18-01–MED-C18-08 | 8 |
| 18 | 2. Etiology, Very Early SSc & Raynaud's Phenomenon | 471 | MED-C18-09–MED-C18-16 | 8 |
| 18 | 3. Primary vs Secondary Raynaud's & Diffuse vs Limited SSc | 472 | MED-C18-17–MED-C18-22 | 6 |
| 18 | 4. Limited SSc, PAH & Diffuse Cutaneous Features | 473 | MED-C18-23–MED-C18-29 | 7 |
| 18 | 5. Joint, Gastrointestinal & Antibody Associations | 474 | MED-C18-30–MED-C18-38 | 9 |
| 18 | 6. Renal Crisis, Phases & Investigations | 475 | MED-C18-39–MED-C18-43 | 5 |
| 18 | 7. HRCT Patterns & Treatment | 476 | MED-C18-44–MED-C18-50 | 7 |
| 19 | 1. Definition, Classification & Bohan-Peter Criteria | 477 | MED-C19-01–MED-C19-08 | 8 |
| 19 | 2. Risk Factors, HLA Links & Muscular Presentation | 477–478 | MED-C19-09–MED-C19-17 | 9 |
| 19 | 3. Skin Manifestations | 479 | MED-C19-18–MED-C19-24 | 7 |
| 19 | 4. Rash Comparison & Investigations | 480 | MED-C19-25–MED-C19-32 | 8 |
| 19 | 5. Polymyositis vs Dermatomyositis & Antisynthetase Syndrome | 481 | MED-C19-33–MED-C19-41 | 9 |
| 19 | 6. ILD Patterns, Amyopathic & Juvenile DM, Necrotizing Myopathy | 482 | MED-C19-42–MED-C19-47 | 6 |
| 19 | 7. Inclusion Body Myositis, Antibodies & Treatment | 483 | MED-C19-48–MED-C19-57 | 10 |
| 20 | 1. Sarcoidosis Definition, ACR Criteria & Classification | 484 | MED-C20-01–MED-C20-08 | 8 |
| 20 | 2. HLA Associations, Immune Paradox & Lofgren Syndrome | 485 | MED-C20-09–MED-C20-16 | 8 |
| 20 | 3. Hilar Adenopathy, Heerfordt Syndrome & Chronic Sarcoidosis | 486 | MED-C20-17–MED-C20-23 | 7 |
| 20 | 4. Fibrosis, Skin & Eye Involvement | 487 | MED-C20-24–MED-C20-28 | 5 |
| 20 | 5. Multisystem Manifestations & Investigations | 488 | MED-C20-29–MED-C20-37 | 9 |
| 20 | 6. Treatment, Therapeutic Paradox & Overlap Syndromes | 489 | MED-C20-38–MED-C20-44 | 7 |
| 20 | 7. MCTD: Serology, Clinical Features & Complications | 489–490 | MED-C20-45–MED-C20-52 | 8 |

## Full roadmap

| Ch | Title | Starts | State |
|---:|---|---:|---|
| 1 | Introduction to ECG | 377 | **Live** |
| 2 | Approach to Hypertrophy and Blocks | 383 | **Live** |
| 3 | SA Nodal Dysfunction | 387 | **Live** |
| 4 | AV Blocks | 390 | **Live** |
| 5 | Tachyarrhythmias | 394 | **Live** |
| 6 | Atrial Fibrillation and Flutter | 403 | **Live** |
| 7 | Ventricular Arrhythmias | 407 | **Live** |
| 8 | WPW Syndrome | 413 | **Live** |
| 9 | Introduction to ACS | 415 | **Live** |
| 10 | ACS - Coronary Circulation | 425 | **Live** |
| 11 | ACS - Evaluation and Management | 430 | **Live** |
| 12 | Sjogren's Syndrome | 442 | **Live** |
| 13 | IgG4 Related Disease | 449 | **Live** |
| 14 | SLE - Basic Approach | 452 | **Live** |
| 15 | SLE - Diagnosis | 455 | **Live** |
| 16 | SLE - Clinical Profile and Management | 458 | **Live** |
| 17 | Antiphospholipid Syndrome | 466 | **Live** |
| 18 | Systemic Sclerosis | 470 | **Live** |
| 19 | Inflammatory Muscle Diseases | 477 | **Live** |
| 20 | Sarcoidosis and Mixed Connective Tissue Disease | 484 | **Live** |
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
