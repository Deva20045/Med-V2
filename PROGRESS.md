# PULSE Medicine Vol 2 — Progress

Updated **2026-09-25** (Chapters 55–57 shipped — the book is complete). Standalone offline quiz based on *PULSE Medicine Vol 2*, printed Book p377–702.

- Repository: `Deva20045/Med-V2`
- Session branch: `arena/01a0d830-med-v2`
- Published URL: https://deva20045.github.io/Med-V2/
- Editable source of truth: `data/chNN.json`; generated offline deliverable: `pulse-medicine.html`; `index.html` redirects to it.
- **Build status: 57 live chapters / 57 · 3429 questions / 291 units.** All roadmap chapters are live; Book p377–702 is fully covered.

## This release — Chapters 55 to 57 (final release — book complete)

The last three neurology chapters — Approach to Stroke, Brainstem Stroke and Management of Stroke — cover Book p686–702 (`uploads/04.pdf` PDF61–76 plus the single sheet of `uploads/05.pdf`), were read line-to-line, source-ordered and made live. With this release every chapter of the printed book (p377–702) is live and the roadmap is finished.

| Ch | Title | Printed pages | Questions | Units |
|---:|---|---:|---:|---:|
| 55 | Approach to Stroke | 686–690 | 112 | 11 |
| 56 | Brainstem Stroke | 691–699 | 156 | 11 |
| 57 | Management of Stroke | 700–702 | 65 | 6 |
| **Release total** |  | **17 book pages** | **333** | **28** |

### Quality and ordering contract delivered

1. All 17 pages were read top-to-bottom in printed order. The scan has no text layer and image review was unavailable in this session, so RapidOCR transcripts of the 3×/4× renders (`.audit-render/ocr_0461.txt` … `ocr_0476.txt`, `ocr_051.txt`) served as the mechanical read, and every numeric, abbreviation, label and table cell was then re-read from 8×–100× crops with contrast-boosted glyph inspection (`tools/crop_ocr.py`): the ABCD² points column cell by cell, the High-row risk values 8.1/11.7/17.8 (matching the Johnston Lancet-2007 table the book reproduces), the "(within 4-10 wks)" myocardial-infarction window, the insular-ribbon 6-48 hr window, the ≥220/110 and >185/110 mmHg BP thresholds, the alteplase/tenecteplase/labetalol doses, the 10/20 ml/100 g/min perfusion thresholds and the >50%/>70% carotid thresholds. The decode log and every resolved ambiguity are disclosed in `audit/READ_NOTES_55_57.md`; no claim rests on visual confirmation of the scans. Verified page map: 04.pdf PDF61 = p686 Ch55 start, PDF65 = p690 Ch55 end, PDF66 = p691 Ch56 start, PDF74 = p699 Ch56 end (folio prints "669" — a printed quirk), PDF75 = p700 Ch57 start, PDF76 = p701, 05.pdf sheet 1 = p702 Ch57 end (book end). No sheets missing in p686–702.
2. Chapters 55–57 add **333 ordered mappings** to `audit/coverage.json`, bringing the audited ledger to **3725 mappings** for Chapters 2–57; `tools/generate_ch55_57.py` regenerates all three chapter files and appends the ledger idempotently, and every ledger point resolves to exactly one question.
3. Questions use no fill-up, matching or true/false worksheets and no predictable stems; only recall, scenario, numeric, oddoneout and management formats are used, with plausible medical distractors and reasoning-first stems (Ch55 69/10/27/4/2, Ch56 133/15/3/5/0, Ch57 37/5/19/1/3 for recall/scenario/numeric/oddoneout/management). Printed quirks and OCR-resolved readings (`Pseudo abducent pupil` as printed for the pseudo-Abducens phenomenon, `Spared: CN 1,2,3,4,6,12` best-read, the p701 FLAIR timing cells disclosed but not tested as differentiators, the Raymond `(SH Syndrome)` mnemonic read, `stiology`-class typo rows quoted as intended) are documented in `audit/READ_NOTES_55_57.md` and qualified in the audit; nothing was silently corrected.
4. IDs are sequential `MED-C55-01..112`, `MED-C56-01..156`, `MED-C57-01..65`; question arrays are strictly nondecreasing in book page, unit question lists are exact contiguous slices of source order, every unit guide is 2–4 lines, and every explanation ends with its exact `(Book pX)` citation.
5. All three chapters are embedded in the standalone app and live flags for 55–57 are set; **57/57 roadmap chapters are now live with 3429 questions and 291 units — the book is complete.**

## Previous release — Chapters 51 to 54

Four consecutive neurology chapters — Diseases of Spinal Cord, Multiple Sclerosis, Vascular Anatomy of Brain and Approach to UMN Lesion — were rendered line-to-line from `uploads/04.pdf` at 3× (PDF35–60 = Book p660–685, all 26 sheets upright portrait, no rotation needed), source-ordered and made live. This completes the spinal-cord-disease → demyelination → cerebral-vascular → UMN-lesion block and leaves only the stroke chapters (p686–702) unread.

| Ch | Title | Printed pages | Questions | Units |
|---:|---|---:|---:|---:|
| 51 | Diseases of Spinal Cord | 660–667 | 154 | 9 |
| 52 | Multiple Sclerosis | 668–673 | 99 | 9 |
| 53 | Vascular Anatomy of Brain | 674–680 | 133 | 11 |
| 54 | Approach to UMN Lesion | 681–685 | 93 | 9 |
| **Release total** |  | **26 book pages** | **479** | **38** |

### Quality and ordering contract delivered

1. All 26 pages were read top-to-bottom in printed order at 3× (`.audit-render/r04_35_3x.png` … `r04_60_3x.png`), because the scan has no text layer; a 4× RapidOCR pass (`tools/ocr_pages.py`, `.audit-render/ocr_0435.txt` … `ocr_0460.txt`) served only as a mechanical first pass and every numeric, abbreviation and table cell was confirmed visually, with 6× crops used to settle the p664 conus/cauda involvement cells, the p674 "OPAAm" mnemonic line and the handwritten p677 "M2 SEGMENT" heading. Visual extraction covered every heading, table cell, flowchart arm, arterial and tract diagram label, MRI-panel caption, photograph caption, numeric dose/percentage/root value, lecture timer, note and mnemonic in exact book order. Verified page map: 04.pdf PDF35 = p660 Ch51 start, PDF42 = p667 Ch51 end, PDF43 = p668 Ch52 start, PDF48 = p673 Ch52 end, PDF49 = p674 Ch53 start, PDF55 = p680 Ch53 end, PDF56 = p681 Ch54 start, PDF60 = p685 Ch54 end, PDF61 = p686 Ch55 title page ("APPROACH TO STROKE"). No sheets missing in p660–685.
2. Chapters 51–54 add **667 ordered mappings** to `audit/coverage.json`, bringing the audited ledger to **3392 mappings** for Chapters 2–54; `tools/generate_ch51_54.py` regenerates all four chapter files and appends the ledger idempotently, and every ledger point resolves to exactly one question.
3. Questions use no fill-up, matching or true/false worksheets and no predictable stems; only recall, scenario, numeric, oddoneout and management formats are used, with plausible medical distractors and reasoning-first stems (Ch51 113/21/9/10/1, Ch52 62/19/5/10/3, Ch53 103/15/12/3, Ch54 65/10/8/9/1 for recall/oddoneout/scenario/numeric/management). Printed quirks (`IVDP (m/c)`, conus `C1` for the coccygeal segment, `FRATAXIN (Chr 9)`, `Diabetic mellitus`, `Ta-weighted`, `myelin oligo dendrocyte glycoprotein (MOAP)`, `Loss of tone … spasticity`, `unstructured/ dressing apraxia`, `Posterior cerebreal artery (PCA)`, `Middle 3/5th`, `Corticorubral fibers`, `30-300µm`, `Type IIB / Artery of percheron (AOP)`, `Anterior a/3 of Post limb`) are quoted as printed and qualified in the audit. A word-overlap key audit over all 479 questions flagged ten answer keys whose correct option did not match the printed sentence (upper-half vs lower-half facial weakness, largest fibre share, velocity/length dependence, elbow and knee posture, cord-lesion laterality, homunculus artery, PCA field defect, corticospinal function list); all ten were corrected in the generator, not patched in the JSON.
4. IDs are sequential `MED-C51-01..154`, `MED-C52-01..99`, `MED-C53-01..133`, `MED-C54-01..93`; question arrays are strictly nondecreasing in book page, unit question lists are exact contiguous slices of source order, every unit guide is 2–4 lines, and every explanation ends with its exact `(Book pX)` citation.
5. All four chapters are embedded in the standalone app and live flags for 51–54 are set; 54/57 roadmap chapters are now live with 3096 questions and 263 units.

## Previous release — Chapters 48 to 50

Three consecutive neurology chapters — Myasthenia Gravis, Amyotrophic Lateral Sclerosis and Anatomy of Spinal Cord — were rendered line-to-line from `uploads/04.pdf` at 3× (PDF21–34 = Book p646–659; PDF27 = p652 is a landscape sheet read upright via a 90° CCW prerotate), source-ordered and made live. This completes the MG–ALS–spinal-cord-anatomy block.

| Ch | Title | Printed pages | Questions | Units |
|---:|---|---:|---:|---:|
| 48 | Myasthenia Gravis | 646–649 | 82 | 4 |
| 49 | Amyotrophic Lateral Sclerosis | 650–652 | 45 | 3 |
| 50 | Anatomy of Spinal Cord | 653–659 | 127 | 7 |
| **Release total** |  | **14 book pages** | **254** | **14** |

### Quality and ordering contract delivered

1. All 14 pages were read top-to-bottom in printed order at 3× (`.audit-render/r04_21_3x..r04_34_3x.png`; PDF27 also as `r04_27_3x_ccw.png`), because the scan has no text layer. Visual extraction covered every heading, table cell, flowchart arm, NMJ/cord/vascular diagram label, photograph caption, numeric dose/percentage, note and mnemonic in exact book order. Verified page map: 04.pdf PDF21 = p646 Ch48 start, PDF24 = p649 Ch48 end, PDF25 = p650 Ch49 start, PDF27 = p652 Ch49 end (landscape), PDF28 = p653 Ch50 start, PDF34 = p659 Ch50 end. No sheets missing in p646–659.
2. Chapters 48–50 add **254 ordered mappings** to `audit/coverage.json`, bringing the audited ledger to **2725 mappings** for Chapters 2–50.
3. Questions use no fill-up, matching or true/false worksheets; only recall, scenario, numeric, oddoneout and management formats are used, with plausible medical distractors and reasoning-first stems. Printed quirks (`3,4 di-aminopyramidine`, `Corticospinal tract (CBT)`, `sensory output`, conus `C0` vs `C1`, `Medial leminiscus` / `Lateral laminiscus`, `Ascending tracks`, `L4 > L3`) are quoted as printed and qualified in the audit.
4. IDs are sequential `MED-C48-01..82`, `MED-C49-01..45`, `MED-C50-01..127`; question arrays are strictly nondecreasing in book page, unit question lists are exact contiguous slices of source order, and every explanation ends with its exact `(Book pX)` citation.
5. All three chapters are embedded in the standalone app and live flags for 48–50 are set; 50/57 roadmap chapters are now live with 2617 questions.

## Previous release — Chapters 42 to 47

Six consecutive neurology chapters — LMN Approach Part 1, LMN Approach Part 2, Inherited Neuropathies, Guillain-Barre Syndrome, LMN Approach Part 3 and Muscular Dystrophies — were rendered line-to-line from the scans at 3× (`uploads/03.pdf` PDF54–61 = Book p618–625, PDF54 being a landscape sheet read upright via a 90° prerotate; `uploads/04.pdf` PDF1–20 = Book p626–645), source-ordered and made live. This completes the LMN approach to muscular dystrophies block.

| Ch | Title | Printed pages | Questions | Units |
|---:|---|---:|---:|---:|
| 42 | LMN Approach : Part 1 | 618–623 | 93 | 6 |
| 43 | LMN Approach : Part 2 | 624–626 | 42 | 3 |
| 44 | Inherited Neuropathies | 627–631 | 75 | 5 |
| 45 | Guillain-Barre Syndrome | 632–636 | 78 | 5 |
| 46 | LMN Approach : Part 3 | 637–641 | 68 | 5 |
| 47 | Muscular Dystrophies | 642–645 | 65 | 4 |
| **Release total** |  | **28 book pages** | **421** | **28** |

### Quality and ordering contract delivered

1. All 28 pages were read top-to-bottom in printed order at 3× (`.audit-render/r03_54_3x..r03_61_3x.png` and `.audit-render/r04_01_3x..r04_20_3x.png`), because the scans have no text layer. Visual extraction covered every heading, table cell, flowchart arm, timeline year, photograph caption, histology label, numeric root value, note, mnemonic and management dose in exact book order. Verified page map: 03.pdf PDF54 = p618 Ch42 start (landscape sheet, 90° prerotate), PDF59 = p623 Ch42 end, PDF60 = p624 Ch43 start, PDF61 = p625, 04.pdf PDF1 = p626 Ch43 end, PDF2 = p627 Ch44 start, PDF6 = p631 Ch44 end, PDF7 = p632 Ch45 start, PDF11 = p636 Ch45 end, PDF12 = p637 Ch46 start, PDF16 = p641 Ch46 end, PDF17 = p642 Ch47 start, PDF20 = p645 Ch47 end. No sheets missing in p618–645; the earlier "PDF54–61 = p618–622" guess in PAGE_MAP.md is superseded.
2. Chapters 42–47 add **421 ordered mappings** to `audit/coverage.json`, bringing the audited ledger to **2471 mappings** for Chapters 2–47.
3. Questions use no fill-up, matching or true/false worksheets; only recall, scenario, numeric, oddoneout and management formats are used, with plausible medical distractors and reasoning-first stems. Printed quirks (L5 ankle jerk row, "radical", "moto-sensory", "Dejerine sottas", "Common motor axonal potential", "compliment", "bathing suite", "ATP binding cascade protein", "phytanic oxidase", Chr 19 trinucleotide repeat) are quoted as printed and qualified in the audit.
4. IDs are sequential `MED-C42-01..93`, `MED-C43-01..42`, `MED-C44-01..75`, `MED-C45-01..78`, `MED-C46-01..68`, `MED-C47-01..65`; question arrays are strictly nondecreasing in book page, unit question lists are exact contiguous slices of source order, and every explanation ends with its exact `(Book pX)` citation.
5. All six chapters are embedded in the standalone app and live flags for 42–47 are set; 47/57 roadmap chapters are now live with 2363 questions.

## Previous release — Chapters 39, 40 and 41

Three neurology chapters — Seizure Semiology, Generalised Tonic-Clonic Seizure and CNS Infections — were rendered line-to-line from `uploads/03.pdf` at 3× zoom (PDF38–53 = Book p602–617), source-ordered and made live. This completes the seizure semiology to CNS infections block.

| Ch | Title | Printed pages | Questions | Units |
|---:|---|---:|---:|---:|
| 39 | Seizure Semiology | 602–607 | 91 | 6 |
| 40 | Generalised Tonic-Clonic Seizure | 608–612 | 124 | 9 |
| 41 | CNS Infections | 613–617 | 114 | 6 |
| **Release total** |  | **16 book pages** | **329** | **21** |

### Quality and ordering contract delivered

1. All 16 pages were read top-to-bottom in printed order at 3× (`pymupdf.Matrix(3,3)` renders in `.audit-render/03_pdf38_3x..53_3x`), because the scan has no text layer. Visual extraction covered every heading, table cell, flowchart arrow, MRI/EEG panel label, numeric threshold, note, side-effect, management dose and histopathology image in exact book order. Verified page map: PDF38=p602 Ch39 start, PDF43=p607 Ch39 end, PDF44=p608 Ch40 start, PDF48=p612 Childhood Seizures table, PDF49=p613 Ch41 start, PDF53=p617 Ch41 end. No sheets missing in p602–617.
2. Chapters 39–41 add **329 ordered mappings** to `audit/coverage.json`, bringing the audited ledger to **2050 mappings** for Chapters 2–41.
3. Questions use no fill-up, matching or true/false worksheets; only recall, scenario, numeric, oddoneout and management formats are used, with plausible distractors and reasoning-first stems.
4. IDs are sequential `MED-C39-01..91`, `MED-C40-01..124`, `MED-C41-01..114`, question arrays are strictly nondecreasing in book page, unit question lists are exact contiguous slices of source order, and every explanation ends with its exact `(Book pX)` citation.
5. All three chapters are embedded in the standalone app and live flags for 39, 40 and 41 are set; 41/57 roadmap chapters are now live with 1942 questions.

## Previous release — Chapters 30–31

Two consecutive neurology chapters — Frontal Lobe and Praxicons — were rendered from the scans, read block by block, source-ordered and made live (Book p555–562: `uploads/02.pdf` PDF87–93 = p555–561 and `uploads/03.pdf` PDF1 = p562):

| Ch | Title | Printed pages | Questions | Units |
|---:|---|---:|---:|---:|
| 30 | Frontal Lobe | 555–559 | 67 | 5 |
| 31 | Praxicons | 560–562 | 44 | 3 |
| **Release total** |  | **8 book pages** | **111** | **8** |

### Quality and ordering contract delivered

1. All pages were read in printed order (`uploads/02.pdf` PDF87–93 = Book p555–561 and `uploads/03.pdf` PDF1 = Book p562), including the MMSE list, every gyral and sulcal figure label, the frontal-area map, the motor-homunculus and frontal-eye-field flowcharts, both comparison tables, the Rey-Osterrieth and clock-drawing panels and the lobe-wise visual field ladder. Scans have no extractable text: every reading used 2× PyMuPDF renders, printed numbers were re-read at 10×, and 02.pdf PDF92 (p560) is fixed by bracketing — PDF91 prints 559, PDF93 prints 561 and 03.pdf PDF2 prints 563 where Chapter 32 begins.
2. Every source-mapped learning target has a four-option, citation-backed question in `audit/coverage.json`; Chapters 30–31 add **111 ordered mappings**, bringing the audited ledger to **1684 mappings** for Chapters 2–38.
3. New questions are reasoning-first: **no fill-up or matching worksheets**. Scenarios, mechanism-based recall, numeric interpretation, bedside-test decisions and discriminating odd-one-out cases use plausible medical distractors, and printed typos (Fare & upper Limb, hemispatal, Gerstman) are read charitably with the discrepancy recorded in the audit.
4. IDs are sequential, question arrays remain strictly nondecreasing in book page, unit question lists are exact contiguous slices of source order, and every explanation ends with its exact `(Book pX)` citation.
5. Source-specific mnemonics (ORAR LC, JIPFA), the 30%/30% and 40/30/30 motor-fibre accounts, the unexpanded flowchart boxes (Right PTO, DLPN, NPH VN, internal sagittal stratum) and the visual-field ladder are retained as book-study material and qualified in the audit; they are not a replacement for current local clinical guidance.
6. Chapters 30–31 are embedded in the standalone app and all 41 roadmap flags for live chapters are set.

_Note:_ an earlier 62-question pass for these two chapters reached `main` from a parallel session. It is superseded here: every page was re-read line to line and the release now carries 111 questions (67 + 44), so no printed learning target that the first pass inventoried is left unasked. The printed typos it did not flag — *Fare & upper Limb*, *hemispatal*, *Gerstman*, *Initiate lesion* — are recorded in [audit/READ_NOTES_30_31.md](audit/READ_NOTES_30_31.md) and the self-audit.

## Previous release — Chapters 27–29

Three consecutive rheumatology chapters were rendered from `uploads/02.pdf`, read block by block, source-ordered and made live (Book p532–554, all in `uploads/02.pdf` PDF64–86):

| Ch | Title | Printed pages | Questions | Units |
|---:|---|---:|---:|---:|
| 27 | Spondyloarthritis | 532–542 | 101 | 10 |
| 28 | Crystal Arthropathies | 543–551 | 72 | 8 |
| 29 | Adult-Onset Still's Disease and Septic Arthritis | 552–554 | 28 | 3 |
| **Release total** |  | **23 book pages** | **201** | **21** |

### Quality and ordering contract delivered

1. All pages were read in printed order (`uploads/02.pdf` PDF64–86 = Book p532–554), including flowchart arms, comparison tables, numeric thresholds, diagram labels, notes, management ladders and drug doses, with 2× PyMuPDF renders and FILE-tagged verification of every printed page number.
2. Every source-mapped learning target has a four-option, citation-backed question in `audit/coverage.json`; Chapters 27–29 added **201 ordered mappings**.
3. New questions are reasoning-first: **no fill-up or matching worksheets**. Scenarios, mechanism-based recall, numeric interpretation, management decisions and discriminating odd-one-out cases use plausible medical distractors.
4. IDs are sequential, question arrays remain strictly nondecreasing in book page, unit question lists are exact contiguous slices of source order, and every explanation ends with its exact `(Book pX)` citation.

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
2. Every source-mapped learning target has a four-option, citation-backed question in `audit/coverage.json`; Chapters 33–38 add **168 ordered mappings**, bringing the audited ledger to **1372 mappings** for Chapters 2–38. Every target is marked asked.
3. New questions are reasoning-first: **no fill-up or matching worksheets** in Chapters 9–29 or 33–38. Scenarios, mechanism-based recall, numeric interpretation, management decisions and discriminating odd-one-out cases use plausible medical distractors.
4. IDs are sequential, question arrays remain strictly nondecreasing in book page, unit question lists are exact contiguous slices of source order, and every explanation ends with its exact `(Book pX)` citation.
5. Source-specific algorithms, medication doses, clinical thresholds and historical terminology are retained as book-study material and qualified in the audit; they are not a replacement for current local clinical guidance.
6. Chapters 33–38 are embedded in the standalone app and all 41 roadmap flags for live chapters are set.

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

Full evidence: [Chapter 32 read notes](audit/READ_NOTES_32.md), [visual audit and page-by-page ledger](audit/SELF_AUDIT.md), [machine-readable inventory](audit/coverage.json), [verified PDF-page map](audit/PAGE_MAP.md) and [pre-build validation output](audit/PREBUILD_VALIDATION.txt).

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
- **02.pdf PDF87–93: p555–561 (Ch30–31; p560 fixed by bracketing)**
- **03.pdf PDF1: p562 (Ch31 close)**
- **03.pdf PDF2–4: p563–565 (Ch32)**
- **03.pdf PDF5–10: p566–571 (Ch33–34)**
- **03.pdf PDF11–21: p572–582 (Ch35–36)**
- **03.pdf PDF22–31: p583–592 (printed p586, p590, p591 absent) (Ch37)**
- **03.pdf PDF29–37: p593–601 (Ch38)**
- **03.pdf PDF38–43: p602–607 (Ch39)**
- **03.pdf PDF44–48: p608–612 (Ch40)**
- **03.pdf PDF49–53: p613–617 (Ch41)**
- **03.pdf PDF54–61: p618–625 (Ch42–43; PDF54 landscape, read upright via 90° prerotate)**
- **04.pdf PDF1–20: p626–645 (Ch43 close–Ch47)**
- **04.pdf PDF21–34: p646–659 (Ch48–50; PDF27 = p652 landscape, 90° CCW prerotate)**
- 04.pdf PDF35–76: p660 onward (Ch51 onward, not yet live)

## Schema and order contract

- Chapter: exact roadmap number/title, `pageRange` starts at the roadmap page, nonempty `questions` and `units`.
- Question: sequential `MED-C<N>-<seq>` ID; section/page/format/stem; exactly four unique options; one answer; explanation ending exactly `(Book pX)` matching `page`.
- Units: sequential `MED-U<N>-<n>` IDs; each has a 2–4-line guide; its IDs are rebuilt from exactly one section in original question order; flattened units equal the full chapter sequence.
- Questions are in printed book-page order; all printed pages in every live chapter are represented.
- The source-order inventory is fail-closed: the validator requires a ledger mapping for every question in audited Chapters 2–41, in exact question order and with matching book page.
- Questions are educational book-study material, not a substitute for current clinical guidelines or patient care.

## Build, audit and test workflow

```sh
# Generate/edit chapter artifacts only when source artefacts need regeneration.
python3 tools/generate_ch09_15.py        # Chapters 9-15
python3 tools/generate_ch16_20.py        # Chapters 16-20
python3 tools/generate_ch21_26.py        # Chapters 21-26
python3 tools/generate_ch27_29.py        # Chapters 27-29
python3 tools/generate_ch30_31.py        # Chapters 30-31
python3 tools/generate_ch32.py           # Chapter 32
python3 tools/generate_ch33_38.py        # Chapters 33-38
python3 tools/generate_ch39_41.py        # Chapters 39 and 41
python3 tools/generate_ch40.py           # Chapter 40
python3 tools/generate_ch42_47.py        # Chapters 42-47
python3 tools/generate_ch48_50.py        # Chapters 48-50
python3 tools/generate_ch09_15_audit.py  # rebuild the source-order ledger (Ch9-50)
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
| 30 | 1. Frontal-lobe entry: MMSE screening and the superolateral surface map | 555 | MED-C30-01–MED-C30-09 | 9 |
| 30 | 2. Areas on the frontal lobe: lateral map, medial surface and orbital surface | 556 | MED-C30-10–MED-C30-22 | 13 |
| 30 | 3. Area 4, premotor/SMA roles, the movement ladder and the motor homunculus | 557 | MED-C30-23–MED-C30-34 | 12 |
| 30 | 4. Vascular and motor-cortex lesions, the frontal eye field and Broca's area | 558 | MED-C30-35–MED-C30-51 | 17 |
| 30 | 5. Prefrontal cortex map, JIPFA behaviour and bilateral frontal pathology | 559 | MED-C30-52–MED-C30-67 | 16 |
| 31 | 1. Parietal lobe map, the 40/30/30 motor-fibre origins and the postcentral gyrus | 560 | MED-C31-01–MED-C31-13 | 13 |
| 31 | 2. Superior parietal praxicons, apraxia types and the inferior parietal lobule | 561 | MED-C31-14–MED-C31-27 | 14 |
| 31 | 3. Hemispatial neglect, the angular gyrus and alexia without agraphia | 562 | MED-C31-28–MED-C31-44 | 17 |
| 32 | 1. Superolateral temporal lobe and the auditory cortex | 563 | MED-C32-01–MED-C32-09 | 9 |
| 32 | 2. Medial temporal lobe (limbic cortex) and its circuits | 563 | MED-C32-10–MED-C32-12 | 3 |
| 32 | 3. Components of the medial temporal lobe and their functions | 564 | MED-C32-13–MED-C32-18 | 6 |
| 32 | 4. Kluver-Bucy syndrome and Korsakoff's amnestic state | 564 | MED-C32-19–MED-C32-25 | 7 |
| 32 | 5. Apathy, occipital lesions and Balint's syndrome | 565 | MED-C32-26–MED-C32-37 | 12 |
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
| 39 | 1. Definitions, Semiology and Pseudo Seizure | 602 | MED-C39-01–MED-C39-09 | 9 |
| 39 | 2. Classification (ILAE 2017), Focal and Generalized Onset | 602–603 | MED-C39-10–MED-C39-22 | 13 |
| 39 | 3. Epilepsy Evaluation and Focal Seizures | 603–604 | MED-C39-23–MED-C39-34 | 12 |
| 39 | 4. Focal Presentation, Investigations and Medial Temporal Lobe Epilepsy | 604 | MED-C39-35–MED-C39-52 | 18 |
| 39 | 5. Generalized Seizures and Typical Childhood Absence | 605–606 | MED-C39-53–MED-C39-73 | 21 |
| 39 | 6. Juvenile Myoclonic Epilepsy, Myoclonic and Atonic Seizures | 606–607 | MED-C39-74–MED-C39-91 | 18 |
| 40 | 1. GTCS Causes: Metabolic, Encephalopathy and Encephalitis | 608 | MED-C40-01–MED-C40-14 | 14 |
| 40 | 2. Brain Injury, Post Stroke, Drugs, Withdrawal and Syncope Types | 608 | MED-C40-15–MED-C40-21 | 7 |
| 40 | 3. Seizure vs Syncope Table | 609 | MED-C40-22–MED-C40-42 | 21 |
| 40 | 4. Management Flowchart and Antiepileptic Drugs | 609 | MED-C40-43–MED-C40-53 | 11 |
| 40 | 5. Pregnancy and AED Side Effects | 610 | MED-C40-54–MED-C40-64 | 11 |
| 40 | 6. Status Epilepticus Definition, Time Points and Classification | 610 | MED-C40-65–MED-C40-76 | 12 |
| 40 | 7. Clinical Features and EEG Monitoring | 611 | MED-C40-77–MED-C40-84 | 8 |
| 40 | 8. Status Epilepticus Management | 611 | MED-C40-85–MED-C40-100 | 16 |
| 40 | 9. Childhood Seizures and Lafora Disease | 612 | MED-C40-101–MED-C40-124 | 24 |
| 41 | 1. Bacterial vs Viral Meningitis vs Viral Encephalitis | 613 | MED-C41-01–MED-C41-12 | 12 |
| 41 | 2. Viral Encephalitis Etiology, Investigations and Autoimmune Encephalitis Notes | 613–614 | MED-C41-13–MED-C41-26 | 14 |
| 41 | 3. Acute Meningitis and Etiology by Age Group | 614–615 | MED-C41-27–MED-C41-42 | 16 |
| 41 | 4. Pathogenesis, Pneumococcus Features and Predisposing Factors | 615 | MED-C41-43–MED-C41-57 | 15 |
| 41 | 5. Clinical Presentation, Meningeal Signs and LP Contraindications | 616–617 | MED-C41-58–MED-C41-78 | 21 |
| 41 | 6. CSF Analysis, Treatment and Eosinophilic Meningitis | 617 | MED-C41-79–MED-C41-114 | 36 |
| 42 | 1. Anatomy of Spinal Cord & LMN Tract | 618 | MED-C42-01–MED-C42-17 | 17 |
| 42 | 2. Site of Lesion, Pathology and Radiculopathy | 619 | MED-C42-18–MED-C42-33 | 16 |
| 42 | 3. Foot Drop, Upper Limb DTR Values, Neuropathy Patterns | 620 | MED-C42-34–MED-C42-52 | 19 |
| 42 | 4. Polyneuropathy Types, Sensory Columns and Fibre Types | 621 | MED-C42-53–MED-C42-70 | 18 |
| 42 | 5. Large vs Small Fibre Neuropathy | 622 | MED-C42-71–MED-C42-85 | 15 |
| 42 | 6. Ganglionopathy | 623 | MED-C42-86–MED-C42-93 | 8 |
| 43 | 1. Radiculopathies: Axonal vs Demyelinating Features and Causes | 624 | MED-C43-01–MED-C43-19 | 19 |
| 43 | 2. Notes, ANS Predominant Neuropathies and Patterns of LMN Lesions | 625 | MED-C43-20–MED-C43-35 | 16 |
| 43 | 3. Nerve Conduction Studies and the CMAP Trace | 626 | MED-C43-36–MED-C43-42 | 7 |
| 44 | 1. Types of Inherited Neuropathy and CMT-1 vs CMT-2 | 627 | MED-C44-01–MED-C44-18 | 18 |
| 44 | 2. CMT-4, Features of CMT-1 and Thickened Nerves | 628 | MED-C44-19–MED-C44-34 | 16 |
| 44 | 3. Familial Amyloid Polyneuropathy and Porphyric Neuropathy | 629 | MED-C44-35–MED-C44-50 | 16 |
| 44 | 4. Porphyric ANS and CNS Features, Tangier's and Refsum Disease | 630 | MED-C44-51–MED-C44-67 | 17 |
| 44 | 5. Romberg's Sign, Wash Basin Sign, Fabry's and Autonomic Neuropathies | 631 | MED-C44-68–MED-C44-75 | 8 |
| 45 | 1. Definition, Classification Subtypes and AIDP Pathophysiology | 632 | MED-C45-01–MED-C45-13 | 13 |
| 45 | 2. Clinical Presentation, Examination, Progression and Prognosis | 633 | MED-C45-14–MED-C45-30 | 17 |
| 45 | 3. Inciting Factors and Diagnostic Criteria | 634 | MED-C45-31–MED-C45-47 | 17 |
| 45 | 4. Treatment, MFS/Bickerstaff Encephalitis and CIDP vs AIDP | 635 | MED-C45-48–MED-C45-65 | 18 |
| 45 | 5. CIDP Affected Systems, POEMS Syndrome and MMN-CB | 636 | MED-C45-66–MED-C45-78 | 13 |
| 46 | 1. Pure Motor LMN Comparison, NMJ Disorders and Power Grades | 637–638 | MED-C46-01–MED-C46-19 | 19 |
| 46 | 2. Muscle Etiology A and the Inherited Myopathy Classes | 638 | MED-C46-20–MED-C46-28 | 9 |
| 46 | 3. Episodic vs Persistent Matrix, Symptoms and Weakness Tasks | 639 | MED-C46-29–MED-C46-39 | 11 |
| 46 | 4. Exception Patterns, Fatigue/Exercise Intolerance and Myalgia | 640 | MED-C46-40–MED-C46-54 | 15 |
| 46 | 5. Fibromyalgia, Cramps vs Contractures and Myotonia vs Paramyotonia | 641 | MED-C46-55–MED-C46-68 | 14 |
| 47 | 1. Structural Myopathies, Dystrophin Defect, DMD Timeline and Becker | 642 | MED-C47-01–MED-C47-19 | 19 |
| 47 | 2. Limb Girdle, Emery Dreifuss, Facioscapulohumeral, Oculopharyngeal and Myotonic Dystrophy | 643 | MED-C47-20–MED-C47-35 | 16 |
| 47 | 3. Myotonic Dystrophy Presentation and Metabolic/Mitochondrial Myopathies | 644 | MED-C47-36–MED-C47-50 | 15 |
| 47 | 4. Channelopathies and the Periodic Paralyses | 645 | MED-C47-51–MED-C47-65 | 15 |

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
| 30 | Frontal Lobe | 555 | **Live** |
| 31 | Praxicons | 560 | **Live** |
| 32 | Temporal and Occipital Lobe | 563 | **Live** |
| 33 | Language V/S Speech | 566 | **Live** |
| 34 | Memory | 569 | **Live** |
| 35 | Dementia : Part 1 | 572 | **Live** |
| 36 | Dementia : Part 2 | 577 | **Live** |
| 37 | Parkinson's Disease | 583 | **Live** |
| 38 | Headache | 593 | **Live** |
| 39 | Seizure Semiology | 602 | **Live** |
| 40 | Generalised Tonic-Clonic Seizure | 608 | **Live** |
| 41 | CNS Infections | 613 | **Live** |
| 42 | LMN Approach : Part 1 | 618 | **Live** |
| 43 | LMN Approach : Part 2 | 624 | **Live** |
| 44 | Inherited Neuropathies | 627 | **Live** |
| 45 | Guillain-Barre Syndrome | 632 | **Live** |
| 46 | LMN Approach : Part 3 | 637 | **Live** |
| 47 | Muscular Dystrophies | 642 | **Live** |
| 48 | Myasthenia Gravis | 646 | **Live** |
| 49 | Amyotrophic Lateral Sclerosis | 650 | **Live** |
| 50 | Anatomy of Spinal Cord | 653 | **Live** |
| 51 | Diseases of Spinal Cord | 660 | Soon |
| 52 | Multiple Sclerosis | 668 | Soon |
| 53 | Vascular Anatomy of Brain | 674 | Soon |
| 54 | Approach to UMN Lesion | 681 | Soon |
| 55 | Approach to Stroke | 686 | Soon |
| 56 | Brainstem Stroke | 691 | Soon |
| 57 | Management of Stroke | 700 | Soon |