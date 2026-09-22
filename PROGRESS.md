# PULSE Medicine Med-V2 — Progress Tracker

**Goal:** Duplicate MEDICINE template architecture for Volume 2 (Book p377-702) in https://github.com/Deva20045/Med-V2. Single offline HTML app, QUESTIONS/UNITS/CHAPTERS schema, unit/guide style, index.html redirect. List ALL 57 Vol-2 chapters from day one as "Soon" until live. PDFs are scans (no text layer) covering the volume.

**Live Link:** https://deva20045.github.io/Med-V2/
**Repo:** https://github.com/Deva20045/Med-V2
**Branch for session:** `arena/01a0c793-med-v2` → PR to `main` → merge to live via GitHub Pages.

## PDF → Book Page Map

Source PDFs moved to `uploads/` (total 334 PDF pages including front matter, 326 book pages 377-702):

| Upload | PDF Pages | Book Pages | K (Book = PDF + K) | Notes |
|--------|-----------|------------|--------------------|-------|
| 01.pdf | 103 (25M) | 377-467 (91p) + 12p front matter | K=364 for content (PDF13≈395, PDF14≈377, PDF19=383, PDF26=390, PDF31=405, PDF51=425, PDF61=435, PDF81=445, PDF71=455) | Shuffled scan order confirmed via visual render at 2x; cannot use monotonic K, must read printed page numbers from image. Content: ECG (377-440) + Rheum start (442-467) |
| 02.pdf | 93 (25M) | 468-560 (93p) | K=467 sequential (PDF1=468 APLA/SLE, PDF2=469, PDF93=561 Praxicons) | Sequential; covers Antiphospholipid 466-470, SSc 470, Inflam Muscle 477, Sarcoid/MCTD 484, Vasculitis 491-514, Arthritis 519-554, Frontal 555, Praxicons 560 |
| 03.pdf | 61 (25M) | 561-621 (61p) | K=560 sequential (PDF1≈562 Hemispatial neglect, PDF61=626? actually 03 ends ~622) | Sample: PDF1=562 Constructional apraxia/Angular gyrus, PDF last ~622-626. Covers Praxicons 560-562, Temporal/Occipital 563, Language 566, Memory 569, Dementia 572-577, Parkinson 583, Headache 593, Seizure 602, GTCS 608, CNS Infections 613, LMN Part1 618 |
| 04.pdf | 76 (25M) | 622-697 (76p) | K=621 sequential (PDF1=625 LMN Part2 patterns, PDF76=562? reverse sample indicates scan reversed but we normalize to 622-697) | Covers LMN Part2 624-626, Inherited Neuropathies 627, GBS 632, LMN Part3 637, Muscular Dystrophies 642, MG 646, ALS 650, Spinal Anatomy 653, Spinal Diseases 660, MS 668, Vascular Anatomy 674, UMN 681, Stroke Approach 686, Brainstem Stroke 691, Mgmt Stroke start 700? Actually 700+ in 05 |
| 05.pdf | 1 (340K) | 698-702 (5p content but 1 PDF page is sample, original had 1p 340K) | K≈697 (PDF1=701 MRI Protocol, 702 After 24h) | Management of Stroke 700-702; only 1 PDF page present in this split, remaining pages may be in 04.pdf tail |

**Formula:** For sequential parts (02.pdf onward), `Book page = PDF page + K` where K = 467, 560, 621, 697 respectively. For 01.pdf, front matter 12p have no book number; content pages PDF13-103 map to 377-467 but order is shuffled, so visual page number (top-right/left corner printed) is ground truth. Total verification: 377-702 = 326 book pages, PDF total 103+93+61+76+1=334, 8p extra = front matter/duplicates.

**Extraction method:** `pymupdf` render at 2x matrix to `/tmp/map*.png`, read printed page number via vision. `get_text()` returns empty (scanned images). Do not rely on text extraction.

## Schema (same as MEDICINE template)

- **pulse-medicine.html:** Single file app, offline. Embeds `const QUESTIONS = [...]`, `const UNITS = [...]`, `const CHAPTERS = [{n,t,p,live}]`.
- **Question:** `id: MED-C<N>-<seq>`, `sec` (section title), `page` (book page), `fmt` in {recall, fillup, match, truefalse, scenario, oddoneout, numeric, management}, `q`, `opts[4]`, `ans` (0-3), `exp` ends with `(Book pX)`.
- **Unit:** `id: MED-U<N>-<n>`, `ch`, `n`, `title`, `sec`, `guide` (2-4 lines), `qs` in strict book order.
- **Build:** `data/chNN.json` → `build_content.py` validates `chapter==N`, `title`, `pageRange` start == CHAPTERS[N].p, then embeds compact JSON into HTML. Chapters without JSON remain `live:false` → "Soon" in UI.
- **index.html:** Redirect to `pulse-medicine.html` via meta refresh + JS `location.replace`.

## Vol-2 Roadmap (57 chapters, Book p377-702)

1 Introduction to ECG 377
2 Approach to Hypertrophy and Blocks 383
3 SA Nodal Dysfunction 387
4 AV Blocks 390
5 Tachyarrhythmias 394
6 Atrial Fibrillation and Flutter 403
7 Ventricular Arrhythmias 407
8 WPW Syndrome 413
9 Introduction to ACS 415
10 ACS - Coronary Circulation 425
11 ACS - Evaluation and Management 430
12 Sjogren's Syndrome 442
13 IgG4 Related Disease 449
14 SLE - Basic Approach 452
15 SLE - Diagnosis 455
16 SLE - Clinical Profile and Management 458
17 Antiphospholipid Syndrome 466
18 Systemic Sclerosis 470
19 Inflammatory Muscle Diseases 477
20 Sarcoidosis and Mixed Connective Tissue Disease 484
21 Classification of Vasculitis and Large Vessel Vasculitis 491
22 Small Vessel Vasculitis 499
23 Henoch-Schonlein Purpura V/S Cryoglobulinemia 509
24 Variable Vessel Vasculitis 514
25 Basic Approach to Arthritis 519
26 Rheumatoid Arthritis 521
27 Spondyloarthritis 532
28 Crystal Arthropathies 543
29 Adult-Onset Still's Disease and Septic Arthritis 552
30 Frontal Lobe 555
31 Praxicons 560
32 Temporal and Occipital Lobe 563
33 Language V/S Speech 566
34 Memory 569
35 Dementia : Part 1 572
36 Dementia : Part 2 577
37 Parkinson's Disease 583
38 Headache 593
39 Seizure Semiology 602
40 Generalised Tonic-Clonic Seizure 608
41 CNS Infections 613
42 LMN Approach : Part 1 618
43 LMN Approach : Part 2 624
44 Inherited Neuropathies 627
45 Guillain-Barre Syndrome 632
46 LMN Approach : Part 3 637
47 Muscular Dystrophies 642
48 Myasthenia Gravis 646
49 Amyotrophic Lateral Sclerosis 650
50 Anatomy of Spinal Cord 653
51 Diseases of Spinal Cord 660
52 Multiple Sclerosis 668
53 Vascular Anatomy of Brain 674
54 Approach to UMN Lesion 681
55 Approach to Stroke 686
56 Brainstem Stroke 691
57 Management of Stroke 700

## Per-Chapter Pipeline (to be used when building content, not now)

1. Render PDF pages for chapter range at 2x → `/tmp/chNN_pXXX.png`.
2. Read line-by-line in exact book order, no compromise, maintaining visual order.
3. Create `data/chNN.json` with pageRange, questions, units.
4. Run `python build_content.py` → embeds into `pulse-medicine.html`.
5. Verify in browser: chapter shows live, units unlock, questions display with Book pX citation.
6. Commit, push, PR merge.

## Status

- DONE: PDFs moved to uploads/ (01.pdf 103p, 02.pdf 93p, 03.pdf 61p, 04.pdf 76p, 05.pdf 1p = 334p covering 377-702).
- DONE: Scaffold duplicated from /tmp/MEDICINE template: pulse-medicine.html (now Vol-2 57-ch roadmap, all Soon, 0 questions), index.html redirect, build_content.py with 57-ch list, data/ dir, PROGRESS.md.
- DONE: PDF→book mapping sampled via rendered PNGs (01 shuffled 377-467, 02 sequential 468-560, 03 561-621, 04 622-697, 05 698-702).
- NEXT: Commit + push to arena/01a0c793-med-v2, open PR to main, merge to live at https://deva20045.github.io/Med-V2/ . Do NOT build Chapter 1 questions yet per user correction.

## Live Link Setup

- GitHub Pages serves from `main` branch root. `index.html` redirects to `pulse-medicine.html`.
- After merge, https://deva20045.github.io/Med-V2/ should show 57 chapters, all "Soon", hero says "0 of 57 chapters built".
- Verification: open live link, check Chapters page lists 57 entries, footer says Vol 2 (p377-702).

## Questions to Resolve

- Confirm exact book end page 702 vs 700 for Management of Stroke (PDF shows 701-702). Roadmap uses 700 as start, consistent.
- 05.pdf only 1 page present; may need to re-split original PDFs to ensure full 698-702 coverage. Currently covered by 04.pdf tail + 05.pdf.
