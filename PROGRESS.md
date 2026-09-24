# PULSE Medicine Vol 2 — Progress

Updated **2026-09-24**. Standalone offline quiz based on *PULSE Medicine Vol 2*, printed Book p377–702.

- Repository: `Deva20045/Med-V2`
- Session branch: `arena/01a0d219-med-v2`
- Published URL: https://deva20045.github.io/Med-V2/
- Editable source of truth: `data/chNN.json`; generated offline deliverable: `pulse-medicine.html`; `index.html` redirects to it.
- **Build status: 35 live chapters / 57 · 1465 questions / 149 units.** Chapters 30–32, 39–57 remain `live:false`.

## This release — Chapters 27–29

Three consecutive rheumatology chapters were rendered from `uploads/02.pdf`, read block by block, source-ordered and made live (Book p532–554, all in `uploads/02.pdf` PDF64–86):

| Ch | Title | Printed pages | Questions | Units |
|---:|---|---:|---:|---:|
| 27 | Spondyloarthritis | 532–542 | 101 | 10 |
| 28 | Crystal Arthropathies | 543–551 | 72 | 8 |
| 29 | Adult-Onset Still's Disease and Septic Arthritis | 552–554 | 28 | 3 |
| **Release total** |  | **23 book pages** | **201** | **21** |

### Quality and ordering contract delivered

1. All pages were read in printed order (`uploads/02.pdf` PDF64–86 = Book p532–554), including flowchart arms, comparison tables, numeric thresholds, diagram labels, notes, management ladders and drug doses. Scans have no extractable text: every reading used 2× PyMuPDF renders with FILE-tagged verification, and every printed page number was verified against the page map.
2. Every source-mapped learning target has a four-option, citation-backed question in `audit/coverage.json`; Chapters 27–29 add **201 ordered mappings**, bringing the audited ledger to **1573 mappings** for Chapters 2–38.
3. New questions are reasoning-first: **no fill-up or matching worksheets**. Scenarios, mechanism-based recall, numeric interpretation, management decisions and discriminating odd-one-out cases use plausible medical distractors.
4. IDs are sequential, question arrays remain strictly nondecreasing in book page, unit question lists are exact contiguous slices of source order, and every explanation ends with its exact `(Book pX)` citation.
5. Chapters 27–29 are embedded in the standalone app and all 35 roadmap flags for live chapters are set.

## Previous release — Chapters 33–38

Six consecutive neurology chapters were rendered from the scans, read block by block, source-ordered and made live (Book p566–601, all in `uploads/03.pdf`; printed p586, p590 and p591 are absent from the supplied scan and are transparently flagged in the ledger):

| Ch | Title | Printed pages | Questions | Units |
|---:|---|---:|---:|---:|
| 33 | Language V/S Speech | 566–568 | 16 | 4 |
| 34 | Memory | 569–571 | 12 | 3 |
| 35 | Dementia : Part 1 | 572–576 | 27 | 5 |
| 36 | Dementia : Part 2 | 577–582 | 25 | 3 |
| 37 | Parkinson's Disease | 583–592 | 37 | 5 |
| 38 | Headache | 593–601 | 51 | 6 |
| **Release total** |  | **36 book pages (p586/p590/p591 absent from scan)** | **168** | **26** |

### Quality and ordering contract delivered

1. All pages were read in printed order (`uploads/03.pdf` PDF5–37 = Book p566–601; printed p586, p590 and p591 are absent from the scan), including flowchart arms, comparison tables, numeric thresholds, diagram labels, notes, management ladders and drug doses. Scans have no extractable text: every reading used 2× PyMuPDF renders, and every printed page number was verified against the page map (decisive 10× corner reads settled the missing sheets).
2. Every source-mapped learning target has a four-option, citation-backed question in `audit/coverage.json`; Chapters 33–38 add **168 ordered mappings**, bringing the audited ledger to **1573 mappings** for Chapters 2–38. Every target is marked asked.
3. New questions are reasoning-first: **no fill-up or matching worksheets** in Chapters 9–29 or 33–38. Scenarios, mechanism-based recall, numeric interpretation, management decisions and discriminating odd-one-out cases use plausible medical distractors.
4. IDs are sequential, question arrays remain strictly nondecreasing in book page, unit question lists are exact contiguous slices of source order, and every explanation ends with its exact `(Book pX)` citation.
5. Source-specific algorithms, medication doses, clinical thresholds and historical terminology are retained as book-study material and qualified in the audit; they are not a replacement for current local clinical guidance.
6. Chapters 33–38 are embedded in the standalone app and all 35 roadmap flags for live chapters are set.

## Previous release — Chapters 16–26

Eleven consecutive rheumatology chapters (Book p458–531): 
| Ch | Title | Printed pages | Questions | Units |
|---:|---|---:|---:|---:|
| 16 | SLE - Clinical Profile and Management | 458–465 | 74 | 7 |
| 17 | Antiphospholipid Syndrome | 466–469 | 35 | 4 |
| 18 | Systemic Sclerosis | 470–476 | 50 | 7 |
| 19 | Inflammatory Muscle Diseases | 477–483 | 57 | 7 |
| 20 | Sarcoidosis and Mixed Connective Tissue Disease | 484–490 | 52 | 7 |
| 21 | Classification of Vasculitis and Large Vessel Vasculitis | 491–498 | 44 | 3 |
| 22 | Small Vessel Vasculitis | 499–508 | 52 | 3 |
| 23 | Henoch-Schonlein Purpura V/S Cryoglobulinemia | 509–513 | 26 | 2 |
| 24 | Variable Vessel Vasculitis | 514–518 | 36 | 2 |
| 25 | Basic Approach to Arthritis | 519–520 | 11 | 1 |
| 26 | Rheumatoid Arthritis | 521–531 | 80 | 4 |
| **Release total** |  | **74 pages** | **517** | **47** |

Full evidence: [visual audit and page-by-page ledger](audit/SELF_AUDIT.md), [machine-readable inventory](audit/coverage.json), [verified PDF-page map](audit/PAGE_MAP.md) and [pre-build validation output](audit/PREBUILD_VALIDATION.txt).

## Verified PDF → printed-page map

Printed page numbers are ground truth. Every sheet used so far was rendered at 2× and checked visually. `uploads/01.pdf` is sequential after 12 unnumbered front-matter sheets; `uploads/02.pdf` continues the same volume at Book p468; `uploads/03.pdf` continues at Book p562 (printed p586, p590 and p591 are absent from the scan); `uploads/04.pdf` begins at Book p626. Full mappings are in [PAGE_MAP.md](audit/PAGE_MAP.md), [page-map.json](audit/page-map.json) and [page-map-02.json](audit/page-map-02.json).

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
- **02.pdf PDF24–63: p491–531 (printed p527 absent) (Ch21–26)**
- **02.pdf PDF64–86: p532–554 (Ch27–29)**
- 02.pdf PDF87–93: p555–561 (Ch30–32 territory, not yet live)
- 03.pdf PDF1–4: p562–565 (Ch30–32 territory, not yet live)
- **03.pdf PDF5–10: p566–571 (Ch33–34)**
- **03.pdf PDF11–21: p572–582 (Ch35–36)**
- **03.pdf PDF22–31: p583–592 (printed p586, p590, p591 absent) (Ch37)**
- **03.pdf PDF29–37: p593–601 (Ch38)**
- 03.pdf PDF38–61: p602–622 (Ch39 onward, not yet live); 04.pdf: p626 onward

## Schema and order contract

- Chapter: exact roadmap number/title, `pageRange` starts at the roadmap page, nonempty `questions` and `units`.
- Question: sequential `MED-C<N>-<seq>` ID; section/page/format/stem; exactly four unique options; one answer; explanation ending exactly `(Book pX)` matching `page`.
- Units: sequential `MED-U<N>-<n>` IDs; each has a 2–4-line guide; its IDs are rebuilt from exactly one section in original question order; flattened units equal the full chapter sequence.
- Questions are in printed book-page order; all printed pages in every live chapter are represented.
- The source-order inventory is fail-closed: the validator requires a ledger mapping for every question in audited Chapters 2–38, in exact question order and with matching book page.
- Questions are educational book-study material, not a substitute for current clinical guidelines or patient care.

## Build, audit and test workflow

```sh
# Generate/edit chapter artifacts only when source artefacts need regeneration.
python3 tools/generate_ch09_15.py        # Chapters 9-15
python3 tools/generate_ch16_20.py        # Chapters 16-20
python3 tools/generate_ch21_26.py        # Chapters 21-26
python3 tools/generate_ch27_29.py        # Chapters 27-29
python3 tools/generate_ch33_38.py        # Chapters 33-38
python3 tools/generate_ch09_15_audit.py  # rebuild the source-order ledger (Ch9-29, Ch33-38)
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
| 21 | 1. Vasculitis definition and Chapel-Hill vessel-size classification | 491–493 | MED-C21-01–MED-C21-15 | 15 |
| 21 | 2. Giant cell arteritis and PMR | 493–495 | MED-C21-16–MED-C21-32 | 17 |
| 21 | 3. Takayasu arteritis | 496–498 | MED-C21-33–MED-C21-44 | 12 |
| 22 | 1. ANCA biology, testing and skin-vessel clinical framework | 499–501 | MED-C22-01–MED-C22-15 | 15 |
| 22 | 2. GPA and MPA manifestations, management and classification | 501–505 | MED-C22-16–MED-C22-32 | 17 |
| 22 | 3. EGPA and PAN | 505–508 | MED-C22-33–MED-C22-52 | 20 |
| 23 | 1. Immune-complex small-vessel vasculitis and HSP | 509–511 | MED-C23-01–MED-C23-14 | 14 |
| 23 | 2. Cryoglobulinemia | 512–513 | MED-C23-15–MED-C23-26 | 12 |
| 24 | 1. Behcet disease classification, criteria and manifestations | 514–517 | MED-C24-01–MED-C24-27 | 27 |
| 24 | 2. Diagnosis, treatment and Cogan syndrome | 518 | MED-C24-28–MED-C24-36 | 9 |
| 25 | 1. Differentiating arthritis patterns and inflammatory arthritis | 519–520 | MED-C25-01–MED-C25-11 | 11 |
| 26 | 1. RA diagnosis duration, joint involvement and etiopathogenesis | 521–523 | MED-C26-01–MED-C26-22 | 22 |
| 26 | 2. RA prediction markers, clinical manifestations and deformities | 524–526 | MED-C26-23–MED-C26-43 | 21 |
| 26 | 3. Extra-articular RA and RA versus SLE | 527–529 | MED-C26-44–MED-C26-61 | 18 |
| 26 | 4. RA management | 530–531 | MED-C26-62–MED-C26-80 | 19 |
| 27 | 1. Spondyloarthritis classification, shared features and non-radiographic axial SpA | 532 | MED-C27-01–MED-C27-09 | 9 |
| 27 | 2. Radiographic axial SpA pathogenesis, presentation and inflammatory back pain | 533 | MED-C27-10–MED-C27-24 | 15 |
| 27 | 3. Investigation: MRI-STIR, sacroiliitis x-ray grading and radiographic signs | 534–535 | MED-C27-25–MED-C27-41 | 17 |
| 27 | 4. Advanced therapy, DISH and reactive arthritis onset | 536 | MED-C27-42–MED-C27-52 | 11 |
| 27 | 5. Reactive arthritis clinical course, mucocutaneous lesions and axial involvement | 537 | MED-C27-53–MED-C27-60 | 8 |
| 27 | 6. Reactive arthritis systemic features, treatment and enteropathic arthritis | 538 | MED-C27-61–MED-C27-69 | 9 |
| 27 | 7. LMAP versus SMAP-u, stool markers and psoriatic arthritis basics | 539 | MED-C27-70–MED-C27-80 | 11 |
| 27 | 8. Psoriasis variants, nail signs and Wright–Moll classification | 540 | MED-C27-81–MED-C27-88 | 8 |
| 27 | 9. Psoriatic versus rheumatoid features, progression and hand radiographs | 541 | MED-C27-89–MED-C27-95 | 7 |
| 27 | 10. Psoriatic spinal and hand radiographic signs plus systemic therapy | 542 | MED-C27-96–MED-C27-101 | 6 |
| 28 | 1. Crystal types, inflammasome pathogenesis and uric-acid metabolism | 543 | MED-C28-01–MED-C28-09 | 9 |
| 28 | 2. Purine pools, stone thresholds and the four-compartment renal model | 544 | MED-C28-10–MED-C28-18 | 9 |
| 28 | 3. Asymptomatic hyperuricemia: thresholds, genetics and drug causes | 545 | MED-C28-19–MED-C28-27 | 9 |
| 28 | 4. Hyperuricemia modifiers, renal manifestations and acute gouty arthritis | 546 | MED-C28-28–MED-C28-38 | 11 |
| 28 | 5. Subsequent attacks, synovial-fluid distinction and polarized-light proof | 547 | MED-C28-39–MED-C28-45 | 7 |
| 28 | 6. Acute gout treatment, ACR criteria, intercritical course and chronic imaging | 548 | MED-C28-46–MED-C28-52 | 7 |
| 28 | 7. Tophi, xanthine-oxidase inhibitors, uricosurics and uricases | 549 | MED-C28-53–MED-C28-59 | 7 |
| 28 | 8. CPPD presentations, associations and the basic crystal remainder | 550–551 | MED-C28-60–MED-C28-72 | 13 |
| 29 | 1. Adult-onset Still's disease phenotype, triad and Yamaguchi major criteria | 552 | MED-C29-01–MED-C29-09 | 9 |
| 29 | 2. Yamaguchi minor criteria, HLH, AOSD therapy and septic-arthritis foundations | 553 | MED-C29-10–MED-C29-20 | 11 |
| 29 | 3. Gonococcal versus septic comparison, septic-arthritis management and arthritis approach | 554 | MED-C29-21–MED-C29-28 | 8 |
| 33 | 1. Language vs Speech & the Auditory Pathway | 566 | MED-C33-01–MED-C33-06 | 6 |
| 33 | 2. Aphasia Lesion Map & Flowchart | 567 | MED-C33-07–MED-C33-11 | 5 |
| 33 | 3. Aphasia Flowchart Continued | 568 | MED-C33-12–MED-C33-14 | 3 |
| 33 | 4. Dysarthria | 568 | MED-C33-15–MED-C33-16 | 2 |
| 34 | 1. Processes & Classification | 569 | MED-C34-01–MED-C34-06 | 6 |
| 34 | 2. Implicit Memory & Anatomy | 570 | MED-C34-07–MED-C34-10 | 4 |
| 34 | 3. Papez Circuit | 571 | MED-C34-11–MED-C34-12 | 2 |
| 35 | 1. Definition, Domains & Causes | 572 | MED-C35-01–MED-C35-06 | 6 |
| 35 | 2. Reversible Causes & Onset Patterns | 573 | MED-C35-07–MED-C35-13 | 7 |
| 35 | 3. Alzheimer's Pathogenesis | 574 | MED-C35-14–MED-C35-19 | 6 |
| 35 | 4. Genetics, Risk & Clinical Stages | 575 | MED-C35-20–MED-C35-23 | 4 |
| 35 | 5. Investigations & Treatment | 576 | MED-C35-24–MED-C35-27 | 4 |
| 36 | 1. Frontotemporal & Lewy Body Dementia | 577–578 | MED-C36-01–MED-C36-10 | 10 |
| 36 | 2. Subcortical vs Cortical & Prion | 579–580 | MED-C36-11–MED-C36-17 | 7 |
| 36 | 3. Vascular Dementia & NPH | 580–582 | MED-C36-18–MED-C36-25 | 8 |
| 37 | 1. Basal Ganglia Anatomy & Circuits | 583–584 | MED-C37-01–MED-C37-07 | 7 |
| 37 | 2. Idiopathic PD: Appearance & Tremor | 584–586 | MED-C37-08–MED-C37-13 | 6 |
| 37 | 3. Motor Signs, Posture & Investigations | 587 | MED-C37-14–MED-C37-20 | 7 |
| 37 | 4. Atypical PD & MSA | 588 | MED-C37-21–MED-C37-26 | 6 |
| 37 | 5. Treatment & Protocols | 589–592 | MED-C37-27–MED-C37-37 | 11 |
| 38 | 1. Anatomy, Classification & Dangerous Headache | 593–594 | MED-C38-01–MED-C38-07 | 7 |
| 38 | 2. Tension-Type & Migraine | 594–595 | MED-C38-08–MED-C38-16 | 9 |
| 38 | 3. Migraine Criteria, Pathogenesis & Treatment | 595–596 | MED-C38-17–MED-C38-28 | 12 |
| 38 | 4. TAC, Cluster & Variants | 597–599 | MED-C38-29–MED-C38-39 | 11 |
| 38 | 5. Trigeminal & Glossopharyngeal Neuralgia | 599 | MED-C38-40–MED-C38-43 | 4 |
| 38 | 6. Benign Intracranial Hypertension | 600–601 | MED-C38-44–MED-C38-51 | 8 |

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
| 21 | Classification of Vasculitis and Large Vessel Vasculitis | 491 | **Live** |
| 22 | Small Vessel Vasculitis | 499 | **Live** |
| 23 | Henoch-Schonlein Purpura V/S Cryoglobulinemia | 509 | **Live** |
| 24 | Variable Vessel Vasculitis | 514 | **Live** |
| 25 | Basic Approach to Arthritis | 519 | **Live** |
| 26 | Rheumatoid Arthritis | 521 | **Live** |
| 27 | Spondyloarthritis | 532 | **Live** |
| 28 | Crystal Arthropathies | 543 | **Live** |
| 29 | Adult-Onset Still's Disease and Septic Arthritis | 552 | **Live** |
| 30 | Frontal Lobe | 555 | Soon |
| 31 | Praxicons | 560 | Soon |
| 32 | Temporal and Occipital Lobe | 563 | Soon |
| 33 | Language V/S Speech | 566 | **Live** |
| 34 | Memory | 569 | **Live** |
| 35 | Dementia : Part 1 | 572 | **Live** |
| 36 | Dementia : Part 2 | 577 | **Live** |
| 37 | Parkinson's Disease | 583 | **Live** |
| 38 | Headache | 593 | **Live** |
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
