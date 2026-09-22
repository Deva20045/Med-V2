# Chapters 2–15 — visual self-audit gate

Reviewed 2026-09-22, before live deployment. Source: `uploads/01.pdf`, 2× PyMuPDF renders. See [every-page map](PAGE_MAP.md) and machine-readable [inventory](coverage.json).

## Method and scope

- Read all educational headings, bullets, sub-bullets, notes, equations, tables, flowchart arms, annotated ECGs and morphology panels on printed p383–457 (PDF19–93). PDF13–18 were previously read for Chapter 1. All 103 PDF sheets were checked for printed page numbering.
- Reading order: top-to-bottom content blocks; parallel comparison columns treated as unified comparison blocks; diagrams remained with their adjacent text. Each unit is a contiguous slice of that sequence. Repeated publisher footers, lesson timestamps and 'Active space' furniture are excluded.
- Every inventoried point has an explicit question target. Strict quality control: zero predictable/trivial distractors, medically plausible answer choices, reasoning-first scenario/recall options in Chapters 9–15 (no fill-up or match worksheets), and exact citation references.
- Software verifies schema, exact app parsers, sequential IDs, page ordering, inventory ordering and full unit coverage. Semantic completeness is verified via visual self-audit.

## Rescue completed before new chapter authoring

Chapter 1 contains 49 questions (MED-C1-01 to MED-C1-49), including restored audit points MED-C1-02/03/20/32/43.

## Source discrepancies handled explicitly

| Page | Source-specific wording retained and qualified |
|---:|---|
| 383 | aVL is printed as 30° without a minus; explanation distinguishes conventional −30°. |
| 385 / 388 | 'Trifascicular' = bifascicular + increased PR is identified as source terminology, not anatomical proof of third-fascicle disease. |
| 385–386 | Proportional STE/S >25% is separated from absolute >5 mm; prose uses > while p386 panels use ≥. |
| 387 | Printed HFrEF <50% / HFpEF >50% leaves exactly 50% unspecified; older 'no drugs' diastolic-treatment row is not contemporary clinical advice. |
| 387–388 | TOK closure / IRK opening retained as printed; HCN 'Na channels' identified as shorthand for a mixed-cation current. |
| 389 | 'Up to 40' IVR and '40–100' AIVR overlap at 40; no question relies on that ambiguous boundary. |
| 390 | Printed PR >100 ms is explicitly contrasted with the usual first-degree definition >200 ms. Cannon waves are contextualised by unusually prolonged PR. |
| 391 | 'Sx' is retained without speculative expansion. Typical QRS widths and the observation/pacing branches are labelled source statements; the latter is not a universal guideline for Mobitz II/high-grade block. |
| 394 | Origin above His bifurcation (<0.12 s) vs below His bifurcation (≥0.16 s) vs supraventricular with BBB (0.12–0.16 s) qualified by conduction anatomy. |
| 395 | VT noted to occur strictly in structurally abnormal hearts (d/t prior infarction); re-entry noted as highly responsive to DC cardioversion. |
| 396 | SVT frequency hierarchy explicitly given as Sinus tachycardia > AF > AVNRT > AVRT > SART. |
| 397 | 2/3rd of AVNRT patients have buried P waves; sinus rate limit capped at 180 bpm; rates 200–250 bpm favor AVNRT >> AVRT. |
| 398 | Pseudo S, pseudo r', and pseudo Q waves defined by relationship to QRS deflections. |
| 399 | RP intervals: AVNRT < 80 ms vs AVRT 80–100 ms (both short-RP/long-PR); Atrial tachycardia is long-RP/short-PR. |
| 400 | Adenosine administration protocol notes 45° supine injection followed by shifting to prone and raising arm overhead; warning that AVRT + adenosine can induce AF -> VT -> VF -> death. |
| 401 | Multifocal AT linked to COPD/theophylline; unifocal AT shows warm-up and cool-down rate phenomenon. |
| 402 | Narrow tachycardia without P waves at 100–110 bpm favors junctional tachycardia over AVNRT/AVRT. |
| 403 | Valvular AF strictly defined as mitral stenosis or prosthetic valve + AF; all other AF is non-valvular. |
| 404 | LA dilation > 4 cm directs strategy to rate control; onset < 48 hrs allows direct rhythm control. |
| 405 | Vernakalant is global DOC for AF rhythm control (not available in India); Ibutilide is 2nd DOC (m/c used). Dabigatran is DOC except Valvular AF/ESRD (Warfarin). |
| 406 | Atrial flutter catheter ablation targets the cavotricuspid isthmus (CTI); initial cardioversion energy is 25–50 J. |
| 407 | Accelerated idioventricular rhythm (AIVT, 40–100 bpm) is a hallmark of successful reperfusion. Unifocal VPC coupling intervals are always constant. |
| 408 | Prophylactic antiarrhythmics are contraindicated in asymptomatic VPCs in the absence of significant VT. |
| 409 | Sustained VT cutoff defined as ≥ 30 seconds; 12-lead panel demonstrates VT transitioning to bigeminy. |
| 410 | Brugada sign (>100 ms to S nadir) and Josephson's sign (notched S nadir); Procainamide is DOC for stable VT without heart disease; Amiodarone for structural disease. |
| 411 | Vulnerable period of T wave is 20–30 ms where unsynchronized discharge precipitates VF. |
| 412 | Energy doses: Flutter (50 J), Monomorphic VT (100 J), AF (100–200 J), Polymorphic VT (200 J). |
| 413 | Concealed WPW has normal baseline 12-lead ECG, conducts antegradely via AV node only; AF in concealed WPW responds only to DC cardioversion. |
| 414 | Type A left-sided (m/c, small delta, positive tall R in V1) vs Type B right-sided (large delta, negative R in V1). Definitive Rx is catheter ablation. |
| 415–424 | Coronary-syndrome tables, lifestyle targets, drug lines and ECG morphology are transcribed as book-study material; current care must follow contemporary local ACS guidance. |
| 425–429 | Coronary territory, dominance, ECG-localisation and complication statements are attributed to the source rather than treated as universal angiographic rules. |
| 430–441 | MI definitions, fibrinolysis/PCI timing, dosing, thresholds and management algorithms are retained as printed and labelled book-study content, not patient-specific instructions. |
| 442–448 | Sjogren classification thresholds and treatment are source-specific; real diagnosis requires clinician assessment and current criteria. |
| 449–451 | IgG4 RCD criteria, percentages and therapy sequence are reproduced as source statements; overlap/mimic diagnosis requires clinical correlation. |
| 452–457 | SLE serology, antibody pattern and prognosis associations are source-specific teaching points; test results are not diagnostic in isolation. |

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
| 9 | 3. Imaging, Stable-Angina Therapy & ST-Segment Foundations | 419–422 | MED-C9-25–MED-C9-46 | 22 |
| 9 | 4. ST Depression, T-Waves & ACS Mimics | 423–424 | MED-C9-47–MED-C9-55 | 9 |
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

## Format distribution

| Chapter | Recall | Fill-up | Match | True/false | Scenario | Odd-one-out | Numeric | Management | Total |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 9 | 17 | 6 | 3 | 5 | 4 | 0 | 49 |
| 2 | 4 | 10 | 5 | 3 | 8 | 2 | 5 | 0 | 37 |
| 3 | 6 | 10 | 5 | 2 | 7 | 3 | 4 | 1 | 38 |
| 4 | 4 | 9 | 1 | 3 | 10 | 1 | 5 | 2 | 35 |
| 5 | 9 | 6 | 5 | 4 | 11 | 4 | 8 | 5 | 52 |
| 6 | 6 | 5 | 3 | 2 | 6 | 1 | 6 | 4 | 33 |
| 7 | 5 | 6 | 3 | 3 | 5 | 4 | 6 | 4 | 36 |
| 8 | 3 | 2 | 2 | 2 | 2 | 1 | 0 | 2 | 14 |
| 9 | 24 | 0 | 0 | 0 | 23 | 3 | 4 | 1 | 55 |
| 10 | 17 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 29 |
| 11 | 33 | 0 | 0 | 0 | 24 | 1 | 11 | 3 | 72 |
| 12 | 26 | 0 | 0 | 0 | 13 | 1 | 5 | 2 | 47 |
| 13 | 16 | 0 | 0 | 0 | 5 | 1 | 0 | 1 | 23 |
| 14 | 15 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 18 |
| 15 | 23 | 0 | 0 | 0 | 6 | 0 | 3 | 0 | 32 |
| Total | 196 | 57 | 41 | 25 | 136 | 28 | 62 | 25 | 570 |

## Page-by-page coverage summary

| Book page | PDF sheet | Inventoried points | Questions | Unasked |
|---:|---:|---:|---:|---:|
| 383 | 19 | 18 | 10 | 0 |
| 384 | 20 | 24 | 11 | 0 |
| 385 | 21 | 35 | 12 | 0 |
| 386 | 22 | 9 | 4 | 0 |
| 387 | 23 | 30 | 12 | 0 |
| 388 | 24 | 35 | 11 | 0 |
| 389 | 25 | 28 | 15 | 0 |
| 390 | 26 | 26 | 8 | 0 |
| 391 | 27 | 27 | 12 | 0 |
| 392 | 28 | 16 | 6 | 0 |
| 393 | 29 | 14 | 9 | 0 |
| 394 | 30 | 10 | 7 | 0 |
| 395 | 31 | 9 | 7 | 0 |
| 396 | 32 | 6 | 6 | 0 |
| 397 | 33 | 4 | 4 | 0 |
| 398 | 34 | 4 | 4 | 0 |
| 399 | 35 | 6 | 6 | 0 |
| 400 | 36 | 9 | 9 | 0 |
| 401 | 37 | 5 | 5 | 0 |
| 402 | 38 | 4 | 4 | 0 |
| 403 | 39 | 11 | 11 | 0 |
| 404 | 40 | 8 | 8 | 0 |
| 405 | 41 | 9 | 9 | 0 |
| 406 | 42 | 5 | 5 | 0 |
| 407 | 43 | 9 | 9 | 0 |
| 408 | 44 | 6 | 6 | 0 |
| 409 | 45 | 4 | 4 | 0 |
| 410 | 46 | 8 | 8 | 0 |
| 411 | 47 | 6 | 6 | 0 |
| 412 | 48 | 3 | 3 | 0 |
| 413 | 49 | 6 | 6 | 0 |
| 414 | 50 | 8 | 8 | 0 |
| 415 | 51 | 6 | 6 | 0 |
| 416 | 52 | 7 | 7 | 0 |
| 417 | 53 | 6 | 6 | 0 |
| 418 | 54 | 5 | 5 | 0 |
| 419 | 55 | 7 | 7 | 0 |
| 420 | 56 | 5 | 5 | 0 |
| 421 | 57 | 5 | 5 | 0 |
| 422 | 58 | 5 | 5 | 0 |
| 423 | 59 | 4 | 4 | 0 |
| 424 | 60 | 5 | 5 | 0 |
| 425 | 61 | 5 | 5 | 0 |
| 426 | 62 | 8 | 8 | 0 |
| 427 | 63 | 7 | 7 | 0 |
| 428 | 64 | 6 | 6 | 0 |
| 429 | 65 | 3 | 3 | 0 |
| 430 | 66 | 5 | 5 | 0 |
| 431 | 67 | 6 | 6 | 0 |
| 432 | 68 | 6 | 6 | 0 |
| 433 | 69 | 4 | 4 | 0 |
| 434 | 70 | 5 | 5 | 0 |
| 435 | 71 | 5 | 5 | 0 |
| 436 | 72 | 7 | 7 | 0 |
| 437 | 73 | 8 | 8 | 0 |
| 438 | 74 | 7 | 7 | 0 |
| 439 | 75 | 6 | 6 | 0 |
| 440 | 76 | 7 | 7 | 0 |
| 441 | 77 | 6 | 6 | 0 |
| 442 | 78 | 5 | 5 | 0 |
| 443 | 79 | 6 | 6 | 0 |
| 444 | 80 | 8 | 8 | 0 |
| 445 | 81 | 7 | 7 | 0 |
| 446 | 82 | 8 | 8 | 0 |
| 447 | 83 | 7 | 7 | 0 |
| 448 | 84 | 6 | 6 | 0 |
| 449 | 85 | 8 | 8 | 0 |
| 450 | 86 | 6 | 6 | 0 |
| 451 | 87 | 9 | 9 | 0 |
| 452 | 88 | 5 | 5 | 0 |
| 453 | 89 | 6 | 6 | 0 |
| 454 | 90 | 7 | 7 | 0 |
| 455 | 91 | 11 | 11 | 0 |
| 456 | 92 | 7 | 7 | 0 |
| 457 | 93 | 14 | 14 | 0 |

**Total: 678 mapped educational points; 570 questions; 55 units across 15 live chapters of 57.**

## Full printed-point → question ledger

### Book p383 / PDF19

| Printed point / call-out | Question |
|---|---|
| Atrial & Ventricular Enlargement heading | MED-C2-01 |
| Atrial enlargement heading | MED-C2-01 |
| Right atrial enlargement: abnormal P waves; pathology atrial origin | MED-C2-01 |
| Pointed P: P-pulmonale; right atrial enlargement | MED-C2-02 |
| Tall and peaked P: COPD | MED-C2-02 |
| Rate >100 bpm: atrial tachycardia | MED-C2-03 |
| Right atrial enlargement figure: II, III, aVF peaked P panels; V1 panel; full ECG arrows/circles | MED-C2-04 |
| Left atrial enlargement heading | MED-C2-05 |
| Bifid P: P mitrale | MED-C2-05 |
| Left atrial enlargement figure: I, II, aVF, V1 panels and annotated tracing | MED-C2-06 |
| Note: corrected QT interval QTc = QT / sqrt(RR) | MED-C2-07 |
| Ventricular hypertrophy heading | MED-C2-08 |
| LVH: axis aVL (printed 30°) to lead I (0°), leftward | MED-C2-08 |
| Leftward axis cause: LVH | MED-C2-09 |
| Increased left muscle mass pushes vector left | MED-C2-09 |
| LVH: increased positive deflection on left | MED-C2-10 |
| Increased negative deflection on right | MED-C2-10 |
| LVH ECG caption and circled I/aVL deflections | MED-C2-10 |

Unasked points: **none found**.

### Book p384 / PDF20

| Printed point / call-out | Question |
|---|---|
| Sokolow–Lyon lead alternatives: R in V5 or V6 plus S in V1 or V2 | MED-C2-11 |
| Sokolow Lyon index: V5 or V6 R + V1 or V2 S >35 mm | MED-C2-12 |
| Sokolow Lyon: aVL >11 mm gives LVH | MED-C2-13 |
| Secondary ST/T changes due to strain/pressure overload | MED-C2-14 |
| Aortic stenosis/chronic HTN | MED-C2-14 |
| Leftward-axis cause 2: LBBB | MED-C2-15 |
| Right ventricular hypertrophy heading | MED-C2-16 |
| RVH axis: III 120° to aVF 90°; rightward | MED-C2-16 |
| Rightward axis cause RVH | MED-C2-17 |
| V1 R/S >1 | MED-C2-17 |
| Secondary ST changes with mitral stenosis + RVH | MED-C2-17 |
| RVH ECG caption | MED-C2-17 |
| P-pulmonale: II, III, aVF | MED-C2-18 |
| Most common COPD | MED-C2-18 |
| COPD tracing circled inferior P waves | MED-C2-18 |
| COPD hyperinflated lung | MED-C2-19 |
| Downward diaphragm push | MED-C2-19 |
| Axis shifts to 90° | MED-C2-19 |
| 90° flowchart: prominent complexes aVF and II | MED-C2-20 |
| Absent lead I complexes: lead I sign | MED-C2-20 |
| Signs of COPD: narrow QRS | MED-C2-21 |
| V1–V6 poor R progression | MED-C2-21 |
| P-pulmonale | MED-C2-21 |
| Positive lead I sign | MED-C2-21 |

Unasked points: **none found**.

### Book p385 / PDF21

| Printed point / call-out | Question |
|---|---|
| Bundle Branch Blocks heading | MED-C2-22 |
| RBBB heading | MED-C2-22 |
| RVH with RBBB: axis I–aVL leftward | MED-C2-22 |
| R/S >1 RVH | MED-C2-22 |
| RVH + leftward axis = biventricular hypertrophy | MED-C2-22 |
| RVH with RBBB tracing labels R/S and RR′ | MED-C2-22 |
| RBBB conduction cartoon | MED-C2-23 |
| RBBB morphology: V1 rr′/RR′/rsR′ terminal R′ | MED-C2-23 |
| V6 qRS/RS with wide terminal S | MED-C2-23 |
| RBBB morphology variants rr′, RR′, rsR′ in V1 and qRS, RS in V6 | MED-C2-24 |
| Blocks: RBBB only unifascicular | MED-C2-25 |
| RBBB + LAFB/LPFB bifascicular | MED-C2-25 |
| LBBB itself bifascicular | MED-C2-25 |
| Bifascicular + prolonged PR/Mobitz trifascicular | MED-C2-26 |
| LBBB heading | MED-C2-27 |
| Axis I–aVL leftward | MED-C2-27 |
| LBBB morphology V5, V6, aVL | MED-C2-27 |
| LBBB ECG annotations LVH and LBBB | MED-C2-27 |
| LBBB conduction cartoons | MED-C2-28 |
| V1 W pattern: rS, QS variants | MED-C2-28 |
| V6 M pattern: RR′, R, RR′ variants | MED-C2-28 |
| LBBB onset intrinsicoid deflection R-peak time normal V1 | MED-C2-29 |
| V6 R-peak time prolonged >0.05 seconds | MED-C2-29 |
| Sgarbossa criteria heading | MED-C2-30 |
| Purpose: diagnose MI along with LBBB | MED-C2-30 |
| ECG findings: V1/V2 concordant depression | MED-C2-31 |
| V1/V2 discordant elevation | MED-C2-31 |
| V5/V6 concordant elevation | MED-C2-31 |
| Sgarbossa figure 1: concordant STE >1 mm with positive QRS | MED-C2-32 |
| Figure 2: concordant STD >1 mm V1–V3 | MED-C2-32 |
| Figure 3: J point | MED-C2-33 |
| Height of discordant STE 5 mm | MED-C2-33 |
| Height preceding S 15 mm | MED-C2-33 |
| STE/S >25% (>0.25) | MED-C2-33 |
| 5/15 =0.33 (>0.25) | MED-C2-33 |

Unasked points: **none found**.

### Book p386 / PDF22

| Printed point / call-out | Question |
|---|---|
| Criteria: V5/V6 concordant STE >1 mm | MED-C2-34 |
| V1/V2 discordant STE >5 mm | MED-C2-34 |
| V1/V2 concordant STD >1 mm | MED-C2-34 |
| V1–V3 panels: LBBB no MI discordant ST | MED-C2-35 |
| LBBB + acute MI concordant ST ≥1 mm | MED-C2-35 |
| Abnormally discordant ST ≥5 mm | MED-C2-35 |
| V5/V6/II/III/aVF panels: discordant ST no MI vs concordant ≥1 mm acute MI | MED-C2-36 |
| Bottom ECG left caption acute MI with LBBB concordant elevation >1 mm; arrows/circle | MED-C2-37 |
| Bottom ECG right caption discordant elevation >5 mm; arrows/circles | MED-C2-37 |

Unasked points: **none found**.

### Book p387 / PDF23

| Printed point / call-out | Question |
|---|---|
| Cardiac terminologies & Pacemaker potential heading | MED-C3-01 |
| Chronotropy: heart rate | MED-C3-01 |
| Chronotropy regulator SA node/pacemaker potential | MED-C3-01 |
| Inotropy: myocardial contractility | MED-C3-02 |
| Inotropy regulator ventricle Lt > Rt/ventricular potential | MED-C3-02 |
| Dromotropy: conduction velocity | MED-C3-03 |
| Bathmotropy: excitability | MED-C3-03 |
| Lusitropy: relaxation | MED-C3-03 |
| These three regulator cells are dashes | MED-C3-03 |
| HF flowchart heading | MED-C3-04 |
| Reduced EF HFrEF: EF <50% | MED-C3-04 |
| Preserved EF HFpEF: EF >50% | MED-C3-04 |
| Older classification: systolic impaired contractility | MED-C3-05 |
| Diastolic impaired relaxation | MED-C3-05 |
| Systolic always associated with diastolic dysfunction | MED-C3-06 |
| Diastolic ± systolic dysfunction | MED-C3-06 |
| Older table Rx options + systolic | MED-C3-07 |
| No drugs to Rx diastolic | MED-C3-07 |
| Pacemaker potential heading | MED-C3-08 |
| Automaticity: ability to beat without stimuli | MED-C3-08 |
| Automaticity SA node pacemaker maximum potential | MED-C3-09 |
| Automaticity distal AV node | MED-C3-10 |
| Atrial cells | MED-C3-10 |
| His–Purkinje system | MED-C3-10 |
| Ventricular myocardium | MED-C3-10 |
| Phases: pacemaker potential | MED-C3-11 |
| TOK transient outward K closure | MED-C3-11 |
| IRK inward rectifying K opening | MED-C3-11 |
| HCN hyperpolarization activated cyclic nucleotide channel | MED-C3-12 |
| Funny currents opening | MED-C3-12 |

Unasked points: **none found**.

### Book p388 / PDF24

| Printed point / call-out | Question |
|---|---|
| HCN continuation Na channels | MED-C3-13 |
| Sites rods cones olfactory epithelium | MED-C3-13 |
| Blocked by ivabradine | MED-C3-13 |
| Pacemaker potential T-type calcium opening | MED-C3-14 |
| Depolarisation L-type calcium | MED-C3-14 |
| Repolarisation L-type calcium closure | MED-C3-14 |
| DRK delayed rectifier K opening | MED-C3-14 |
| PM potential graph membrane potential mV vs time s | MED-C3-15 |
| Pacemaker slope and threshold | MED-C3-15 |
| Upstroke increased Ca permeability/influx | MED-C3-15 |
| Downstroke increased K and decreased Ca permeability/K efflux | MED-C3-15 |
| PM graph numbered call-out 1 maximum negative potential | MED-C3-16 |
| Call-out 2 threshold transition | MED-C3-16 |
| Call-out 3 upstroke | MED-C3-16 |
| Call-out 4 repolarisation | MED-C3-16 |
| PM graph voltage scale −60 to +20 mV | MED-C3-17 |
| PM graph 800 msec cycle label | MED-C3-17 |
| Heart Blocks heading | MED-C3-18 |
| Bradyarrhythmias heading | MED-C3-18 |
| Impulse pathway diagram sinus node atria AV node His bundle branches ventricles | MED-C3-18 |
| Diagram dense fibrous tissues between atria/ventricles | MED-C3-19 |
| AV conduction system bracket AV node His bundle branches | MED-C3-19 |
| Levels of block SA node | MED-C3-20 |
| Sinoatrial block | MED-C3-20 |
| AV block 1°,2°,3° | MED-C3-20 |
| Fascicular block | MED-C3-20 |
| Unifascicular LAFB LPFB RBBB | MED-C3-21 |
| Bifascicular RBBB + LAFB/LPFB or LBBB | MED-C3-21 |
| Trifascicular bifascicular + increased PR | MED-C3-21 |
| Sinus node dysfunction absent P waves | MED-C3-22 |
| Figure A sinus node dysfunction flat continuation | MED-C3-22 |
| Compensation junctional rhythm no P | MED-C3-23 |
| Atrial rhythm abnormal P | MED-C3-23 |
| Both 40–60 bpm | MED-C3-23 |
| Junctional escape strip caption | MED-C3-23 |

Unasked points: **none found**.

### Book p389 / PDF25

| Printed point / call-out | Question |
|---|---|
| Causes flowchart extrinsic/intrinsic | MED-C3-24 |
| Extrinsic hyperkalemia | MED-C3-24 |
| Extrinsic drugs digoxin beta blockers calcium channel blockers | MED-C3-25 |
| Increased PaCO2 hypercapnia: obstructive sleep apnoea syndrome | MED-C3-26 |
| Hypothermia | MED-C3-27 |
| Hypothyroidism myxedema coma | MED-C3-27 |
| Increased ICT bradycardia hypertension reflex | MED-C3-27 |
| Intrinsic sick sinus syndrome | MED-C3-28 |
| SA nodal dysfunction figure hyperkalemia circled waves | MED-C3-29 |
| Junctional rhythm circled complexes | MED-C3-29 |
| Sinus bradycardia heading | MED-C3-30 |
| Regular rhythm | MED-C3-30 |
| Rate 40–60 bpm | MED-C3-30 |
| Normal P | MED-C3-30 |
| Extrinsic much more than intrinsic | MED-C3-30 |
| Sinus bradycardia strip | MED-C3-30 |
| Other ECG manifestations heading | MED-C3-31 |
| Sinus pause/arrest diagram distance A > B | MED-C3-31 |
| Sinoatrial exit block diagram distance A = B | MED-C3-31 |
| Manifestation 3 tachy-brady syndrome and multi-lead strip | MED-C3-32 |
| Idioventricular rhythm IVR → wide QRS | MED-C3-33 |
| IVR HR up to 40 | MED-C3-34 |
| AIVR HR 40–100 | MED-C3-34 |
| AIVR marker successful reperfusion | MED-C3-35 |
| VT HR >100 | MED-C3-36 |
| AIVR figure circled broad complexes | MED-C3-37 |
| AV block absent QRS complexes | MED-C3-38 |
| Figure B AV block continuing P waves | MED-C3-38 |

Unasked points: **none found**.

### Book p390 / PDF26

| Printed point / call-out | Question |
|---|---|
| First Degree AV Block heading/features | MED-C4-01 |
| Causes beta blocker | MED-C4-01 |
| Calcium channel blockers | MED-C4-01 |
| Clinical features asymptomatic | MED-C4-02 |
| Soft S1 | MED-C4-02 |
| Cannon waves JVP | MED-C4-02 |
| Management no Rx needed | MED-C4-03 |
| Very good prognosis | MED-C4-03 |
| ECG delay atria to ventricle | MED-C4-04 |
| Prolonged PR interval | MED-C4-04 |
| Printed PR >100 ms | MED-C4-04 |
| AV block prolonged PR tracing | MED-C4-04 |
| Regular sinus rhythm | MED-C4-05 |
| Normal P and QRS | MED-C4-05 |
| Every P followed by QRS | MED-C4-05 |
| Unusually prolonged PR | MED-C4-06 |
| P superimposed on T | MED-C4-06 |
| Synchronous atrial and ventricular contraction | MED-C4-06 |
| Decreased cardiac output arm | MED-C4-06 |
| JVP cannon waves arm | MED-C4-06 |
| Lead II P arrows figure | MED-C4-06 |
| Second Degree AV Block heading | MED-C4-07 |
| Classification Mobitz Type I/Type II | MED-C4-07 |
| Advanced second degree criteria Mobitz not met | MED-C4-07 |
| Mobitz at a time only 1 beat missed | MED-C4-08 |
| At least 2 beats conducted | MED-C4-08 |

Unasked points: **none found**.

### Book p391 / PDF27

| Printed point / call-out | Question |
|---|---|
| Top Mobitz I strip 3 beats conducted 1 missed | MED-C4-09 |
| Advanced second degree strip >1 beat missed | MED-C4-10 |
| Second strip <2 beats conducted | MED-C4-10 |
| Advanced second degree caption | MED-C4-10 |
| Mobitz table pathology: I AV nodal / II infranodal | MED-C4-11 |
| QRS: I narrow / II wide | MED-C4-11 |
| Etiology: I benign / II malignant | MED-C4-11 |
| PR progressively prolonged I Wenckebach | MED-C4-12 |
| PR constant II | MED-C4-12 |
| RR progressively shortens I | MED-C4-13 |
| RR constant II | MED-C4-13 |
| Presentation I asymptomatic | MED-C4-14 |
| II symptomatic hemodynamic compromise | MED-C4-14 |
| II Stokes Adams syndrome | MED-C4-14 |
| Associated MI I inferior IWMI | MED-C4-15 |
| Associated MI II anterior AWMI | MED-C4-15 |
| Causes row Type I dash | MED-C4-16 |
| Type II Sx/SLE/increased K/amyloid | MED-C4-16 |
| Site-of-block cartoons I at AV node | MED-C4-17 |
| II below AV node at His/bundle levels | MED-C4-17 |
| ECG row I progressive PR/drop arrow | MED-C4-18 |
| ECG row II constant PR/drop star and P arrows | MED-C4-18 |
| AWMI infranodal block | MED-C4-19 |
| Rare due to structural heart disease | MED-C4-19 |
| IWMI AV nodal block | MED-C4-19 |
| Management asymptomatic Type I >II observe | MED-C4-20 |
| Symptomatic permanent pacemaker | MED-C4-20 |

Unasked points: **none found**.

### Book p392 / PDF28

| Printed point / call-out | Question |
|---|---|
| Upper tracing ST elevation II III aVF circles | MED-C4-21 |
| Mobitz second degree AV block stars/bracket | MED-C4-21 |
| IWMI with Mobitz AV block caption | MED-C4-21 |
| Second ECG IWMI advanced second degree 2:1 caption | MED-C4-22 |
| Alternating nonconducted P stars | MED-C4-22 |
| Third Degree AV Block heading | MED-C4-23 |
| Block anywhere conduction system | MED-C4-23 |
| No impulse atria to ventricle | MED-C4-23 |
| AV dissociation | MED-C4-23 |
| ECG regular P atrial | MED-C4-24 |
| Regular QRS junctional/ventricular | MED-C4-24 |
| P/QRS unrelated | MED-C4-24 |
| Diagram atria AV node bundle branch ventricle | MED-C4-25 |
| AV node escape junctional narrow QRS | MED-C4-25 |
| Ventricular escape wide QRS | MED-C4-25 |
| Complete AV dissociation strip arrows mark independent P waves | MED-C4-26 |

Unasked points: **none found**.

### Book p393 / PDF29

| Printed point / call-out | Question |
|---|---|
| Causes flowchart complete AV block | MED-C4-27 |
| VT with complete AV dissociation | MED-C4-27 |
| AIVR with complete AV dissociation | MED-C4-27 |
| Causes flowchart junctional tachycardia with complete dissociation | MED-C4-28 |
| Junctional rhythm with complete dissociation | MED-C4-28 |
| IWMI with 3° AV block ECG caption | MED-C4-29 |
| Inferior leads and independent P arrows on rhythm strip | MED-C4-29 |
| Summary row first degree | MED-C4-30 |
| Summary row Type I second degree | MED-C4-31 |
| Summary row Type II second degree broad/notched QRS intermittent drop | MED-C4-32 |
| Summary advanced 2:1 second degree row | MED-C4-33 |
| Summary advanced 3:1 second degree row | MED-C4-34 |
| Summary complete AV block AV nodal narrow row | MED-C4-35 |
| Summary complete AV block infranodal broad row | MED-C4-35 |

Unasked points: **none found**.

### Book p394 / PDF30

| Printed point / call-out | Question |
|---|---|
| Tachyarrhythmias definition: HR > 100 bpm | MED-C5-01 |
| QRS complex morphological classification: Narrow vs Wide | MED-C5-01 |
| Three fundamental causes of tachycardia: enhanced automaticity, triggered activity, and re-entry | MED-C5-02 |
| Ventricular origin above bifurcation of Bundle of His: Purkinje fibers -> B/L synchronous activation | MED-C5-03 |
| Ventricular origin above His bifurcation: normal/narrow QRS complex (< 0.12 s) | MED-C5-03 |
| Ventricular origin below bifurcation of Bundle of His: ventricular myocardium activates ventricles | MED-C5-04 |
| Ventricular origin below His bifurcation: wide QRS complex (≥ 0.16 s) | MED-C5-04 |
| Supraventricular origin associated with bundle branch block: QRS complex 0.12 - 0.16 s | MED-C5-05 |
| Classification triad: SVT (narrow QRS), SVT with conduction block (slightly wide QRS), VT (wide QRS) | MED-C5-06 |
| Enhanced automaticity normal mechanism: sinus tachycardia, normal sinus impulse originating from SA node | MED-C5-07 |

Unasked points: **none found**.

### Book p395 / PDF31

| Printed point / call-out | Question |
|---|---|
| Abnormal automaticity: atrial tachycardia (focal/multifocal, has all 3 mechanisms), junctional tachycardia, ischemic VT | MED-C5-08 |
| Paroxysmal atrial tachycardia with AV block: associated with digoxin toxicity, precipitated by hypokalemia, due to enhanced automaticity | MED-C5-09 |
| Triggered activity early afterdepolarisation (EAD): Long QT Syndrome leading to Torsades de pointes | MED-C5-10 |
| Triggered activity late afterdepolarisation (DAD): catecholamine sensitive arrhythmias d/t sympathetic activity and increased intracellular Ca2+ | MED-C5-11 |
| DAD arrhythmias: RVOT VT, LVOT VT, and sympathetic VT | MED-C5-11 |
| Re-entry mechanism: precipitated by PAC or PVC; highly responsive to DC cardioversion | MED-C5-12 |
| Micro re-entry circuits: AVNRT, Brugada Syndrome, Atrial Fibrillation | MED-C5-13 |
| Macro re-entry circuits: AVRT, Atrial Flutter, Scar VT | MED-C5-13 |
| Causes based on QRS: wide QRS VT occurs only in structurally abnormal heart (prior infarction); narrow QRS encompasses automaticity and re-entry | MED-C5-14 |

Unasked points: **none found**.

### Book p396 / PDF32

| Printed point / call-out | Question |
|---|---|
| Interpreting narrow QRS tachycardia: HR = 1500 / 10 = 150 bpm; every QRS preceded by P confirming SAN/atrial origin | MED-C5-15 |
| Relative frequency hierarchy: m/c SVT: Sinus tachycardia > AF > AVNRT > AVRT > SART | MED-C5-16 |
| AVNRT features: can occur in structurally normal heart, female predominance (F > M), good prognosis | MED-C5-17 |
| Normal dual AV nodal pathways: fast pathway conducts rapidly with longer refractory period; slow pathway conducts slowly with shorter refractory period where impulse dissolves | MED-C5-18 |
| AVNRT mechanism: premature SV impulse enters recovered slow pathway while fast pathway is refractory, splits to ventricles and retrograde fast pathway | MED-C5-19 |
| AVNRT retrograde atrial activation produces inverted P waves in inferior leads II, III, and aVF | MED-C5-20 |

Unasked points: **none found**.

### Book p397 / PDF33

| Printed point / call-out | Question |
|---|---|
| Simultaneous P & QRS formation in 2/3rd of AVNRT patients: P wave buried in QRS complex | MED-C5-21 |
| Rate limits: sinus rhythm cannot maintain rate > 180 bpm; rate 200 - 250 bpm favors AVNRT >> AVRT | MED-C5-22 |
| Typical AVNRT (95%, PAC trigger, Slow-Fast pathway) vs Atypical AVNRT (5%, PVC trigger, Fast-Slow pathway, D/d Atrial tachycardia) | MED-C5-23 |
| Atypical AVNRT conduction limb: enters fast pathway and exits slow pathway | MED-C5-24 |

Unasked points: **none found**.

### Book p398 / PDF34

| Printed point / call-out | Question |
|---|---|
| Typical AVNRT in 1/3rd patients: pseudo S wave (just outside QRS), pseudo r' wave (on r wave), pseudo Q wave (just before Q) | MED-C5-25 |
| Pharmacological conversion of AVNRT to normal sinus rhythm by intravenous adenosine | MED-C5-26 |
| AVRT clinical features: rarer than AVNRT, fundamentally associated with WPW syndrome | MED-C5-27 |
| AVRT types: Orthodromic (entry AV node, exit Bundle of Kent, narrow QRS) vs Antidromic (entry Bundle of Kent, exit AV node, wide QRS) | MED-C5-28 |

Unasked points: **none found**.

### Book p399 / PDF35

| Printed point / call-out | Question |
|---|---|
| Orthodromic AVRT mechanism: well timed PAC enters AV node slowly, ventricles activate synchronously, retrograde conduction via bypass tract re-enters AV node | MED-C5-29 |
| Orthodromic AVRT ECG: RP interval 2 boxes ~ 80 - 100 ms (AVRT > AVNRT), P falls just outside QRS | MED-C5-30 |
| AVNRT vs AVRT comparison: synchronous activation (+ in AVNRT, - in AVRT), P wave absent in 2/3rd vs outside QRS, structural heart disease absent vs WPW | MED-C5-31 |
| RP intervals: AVNRT < 80 ms vs AVRT 80 - 100 ms; both categorized as short RP, long PR tachycardias | MED-C5-32 |
| AVNRT hemodynamic stability (stable) vs AVRT (stable/unstable); micro re-entry circuit in AVNRT vs macro re-entry circuit in AVRT | MED-C5-33 |
| Interval pattern note: Atrial tachycardia exhibits long RP and short PR interval | MED-C5-34 |

Unasked points: **none found**.

### Book p400 / PDF36

| Printed point / call-out | Question |
|---|---|
| Management goal: AVNRT, AVRT, and Atrial tachycardia operate through AV node -> management is AV nodal block | MED-C5-35 |
| Hemodynamically unstable narrow-complex tachycardia management: synchronised DC cardioversion | MED-C5-36 |
| Hemodynamically stable DOC for AV nodal block: Adenosine (blocks PAC in AVNRT/AVRT, decreases HR in atrial tachycardia) | MED-C5-37 |
| Adenosine pharmacokinetics: T1/2 = 6 s, arm to arm circulation = 15 s, arm to heart circulation = 7.5 s | MED-C5-38 |
| Adenosine route and dose: 6 mg through brachial vein (repeat 12 mg + 12 mg, max 30 mg) followed by immediate saline flush | MED-C5-39 |
| Adenosine administration procedure: 45° supine position -> administer adenosine -> shift to prone position + raise arm overhead | MED-C5-40 |
| Safety protocol: have defibrillator ready; in AVRT, adenosine can induce AF -> VT -> VF -> Death | MED-C5-41 |
| Adenosine contraindication in COPD / bronchial asthma (causes bronchospasm); alternatives: verapamil 2.5-5 mg IV (max 15 mg), metoprolol 5 mg IV (max 15 mg), esmolol | MED-C5-42 |
| Special indication: Heart failure with AVNRT is managed with Digoxin | MED-C5-43 |

Unasked points: **none found**.

### Book p401 / PDF37

| Printed point / call-out | Question |
|---|---|
| Atrial tachycardia features: structurally abnormal heart, chronic tachyarrhythmia-related cardiomyopathy, follows all 3 mechanisms (m/c enhanced automaticity) | MED-C5-44 |
| Atrial tachycardia management: rate reduction to sinus rhythm via beta-blockers (metoprolol) or CCB (verapamil); antiarrhythmics on failure | MED-C5-45 |
| Unifocal AT ECG: narrow QRS, rate ~150 bpm, regular rhythm, uniform abnormal P wave, long RP / short PR, and warm-up & cool-down phenomenon | MED-C5-46 |
| Multifocal AT (MAT): irregular RR interval with ≥ 3 P wave morphologies; m/c cause COPD/theophylline; management: stop theophylline -> beta-blocker/CCB | MED-C5-47 |
| Atrial tachycardia with AV block: association with digoxin toxicity | MED-C5-48 |

Unasked points: **none found**.

### Book p402 / PDF38

| Printed point / call-out | Question |
|---|---|
| AT with AV block ECG: normal P wave + buried P wave, irregular RR intervals, conducted vs missed P waves in 2:1 block | MED-C5-49 |
| Junctional tachyarrhythmia: absent P waves at HR ~100 - 110 bpm favors Junctional >> AVNRT/AVRT | MED-C5-50 |
| Summary algorithm for irregular RR narrow tachycardias: MAT, Atrial flutter with variable block, Atrial fibrillation, and focal AT with varying AV block | MED-C5-51 |
| Summary algorithm for regular RR narrow tachycardias: P wave present (sinus tachycardia, flutter 2:1, SVT short RP vs long RP) vs P wave absent (AVNRT, junctional) | MED-C5-52 |

Unasked points: **none found**.

### Book p403 / PDF39

| Printed point / call-out | Question |
|---|---|
| Epidemiology of AF: 2nd most common sustained cardiac arrhythmia (1st is sinus tachycardia) | MED-C6-01 |
| Mechanical dysfunction in AF: chaotic, disorganised, ineffective contractions causing blood stasis, embolism, and stroke | MED-C6-02 |
| Risk factors for AF: Age and Hypertension | MED-C6-03 |
| Anatomical site for thrombus formation in AF: Appendages (most common site) | MED-C6-04 |
| ECG findings in AF: narrow QRS tachycardia, variable ventricular rate with atrial rate 300 - 600 bpm, irregular RR intervals, fibrillatory waves | MED-C6-05 |
| Classification: Paroxysmal (self terminating < 48 hrs or cardioverted < 7 days), Persistent (> 7 days), and Long standing persistent (> 1 year) | MED-C6-06 |
| Permanent AF: LA dilated > 4 cm in structural heart disease; management strategy is rate control (accepting AF) | MED-C6-07 |
| Valvular AF (mitral stenosis or prosthetic valve + AF) versus Non-valvular AF (all other AF) | MED-C6-08 |
| Systemic etiology of AF: OSAS, CKD, Psoriasis, Thyroid disease, Alcohol, cardiopulmonary disease | MED-C6-09 |
| Electrolyte disturbances triggering AF: Hypokalemia and Hypomagnesemia | MED-C6-10 |
| Symptom pathophysiology in AF: Angina (increased demand), Syncope (decreased circulation), Dyspnea (decreased cardiac output), Palpitation (increased HR) | MED-C6-11 |

Unasked points: **none found**.

### Book p404 / PDF40

| Printed point / call-out | Question |
|---|---|
| Heart rate calculation in irregular AF: 6 second marker rule (HR = number of QRS complexes in 30 large boxes x 10) | MED-C6-12 |
| Differential diagnosis of AF on ECG: MAT (≥ 3 P wave morphologies) and Atrial tachycardia with AV block (conducted + missed P waves) | MED-C6-13 |
| Treatment in hemodynamically unstable or WPW with AF: synchronised DC cardioversion (Start 100 J -> max 200 J) | MED-C6-14 |
| Initial evaluation of stable AF: 2D Echo of LA; dilated LA > 4 cm directs to rate control | MED-C6-15 |
| Stable AF with normal LA and onset < 48 hours: no risk of embolism -> direct rhythm control | MED-C6-16 |
| Stable AF with onset > 48 hours or unknown: risk of embolism (+) -> Trans Esophageal Echo (TEE) / Cardiac CT to detect clot | MED-C6-17 |
| TEE clot positive protocol: 3 weeks of anticoagulants -> pharmacological rhythm control | MED-C6-18 |
| Post-cardioversion protocol: 4 weeks of anticoagulants -> assess CHA2DS2-VASc score -> +/- long-term anticoagulation | MED-C6-19 |

Unasked points: **none found**.

### Book p405 / PDF41

| Printed point / call-out | Question |
|---|---|
| Class Ic antiarrhythmics for AF rhythm control: Flecainide and Propafenone | MED-C6-20 |
| Rhythm control DOC hierarchy: Vernakalant (DOC, not available in India) and Ibutilide (2nd DOC, m/c used: 1 mg IV over 10 mins) | MED-C6-21 |
| DOC for AF rhythm control in structurally abnormal heart: Amiodarone (150 mg IV bolus or 5 mg/kg over 1h -> 1 mg/kg over 8h -> 0.5 mg/kg over 16h) | MED-C6-22 |
| Rate control drugs: Verapamil (5-10 mg over 2 min, max 20 mg), Esmolol (500 mcg/kg over 1 min), Propranolol (1 mg over 2 min, max 5 mg), Digoxin (failed LV) | MED-C6-23 |
| CHA2DS2-VASc scoring components: CHF (1), HTN (1), Age ≥ 75 (2), DM (1), Stroke/TIA/embolus (2), Vascular disease (1), Age 65-75 (1), Female sex (1) | MED-C6-24 |
| CHA2DS2-VASc decision thresholds: Score ≥ 2 requires anticoagulants; Score = 1 ± anticoagulants | MED-C6-25 |
| Bleeding risk assessment tool: HAS-BLED score in AF | MED-C6-26 |
| Anticoagulants: DOC is Dabigatran; exception is Valvular AF and AF + ESRD where DOC is Warfarin | MED-C6-27 |
| Pills in the pocket technique: oral flecainide + beta-blockers in paroxysmal AF taken at symptom onset | MED-C6-28 |

Unasked points: **none found**.

### Book p406 / PDF42

| Printed point / call-out | Question |
|---|---|
| Typical atrial flutter: counterclockwise right atrial circuit, upward left atrial activation, inverted flutter waves in lead II | MED-C6-29 |
| Reverse typical atrial flutter: clockwise right atrial circuit, downward left atrial activation, upright flutter waves in lead II | MED-C6-30 |
| Atrial flutter features: lateral wall of right atrium (90%), onset < 1 week of open heart surgery, sawtooth ECG appearance | MED-C6-31 |
| Atrial flutter management: DC Cardioversion is TOC (25 - 50 J), Ibutilide | MED-C6-32 |
| Definitive catheter ablation for atrial flutter: targeting the cavotricuspid isthmus | MED-C6-33 |

Unasked points: **none found**.

### Book p407 / PDF43

| Printed point / call-out | Question |
|---|---|
| Pathophysiology of broad QRS tachyarrhythmias: ventricular impulse -> cell-to-cell transmission -> broad QRS | MED-C7-01 |
| Ventricular rhythms and rate ranges: IVT (15-40 bpm), AIVT (40-100 bpm), VT (> 100 bpm: monomorphic vs polymorphic) | MED-C7-02 |
| Accelerated Idioventricular Tachycardia (AIVT) clinical marker: indicates successful thrombolysis / reperfusion | MED-C7-03 |
| Etiology of wide QRS: QRS > 0.16 s indicates VT; QRS 0.12 - 0.16 s indicates SVT with BBB or Antidromic AVRT | MED-C7-04 |
| VPC mechanism: extrasystole, premature discharge from ventricle occurring earlier than next anticipated sinus beat | MED-C7-05 |
| Criteria for VPC: not preceded by P wave, very wide QRS, and ST/T changes in opposite direction (discordance) | MED-C7-06 |
| Coupling interval in unifocal VPC: distance between VPC and preceding QRS is always constant | MED-C7-07 |
| Compensatory pause in VPC: distance between 2 sinus impulses across VPC equals distance across normal beat (2 x RR interval) | MED-C7-08 |
| R on T phenomenon: VPC lies on previous T wave, creating risk for ventricular fibrillation | MED-C7-09 |

Unasked points: **none found**.

### Book p408 / PDF44

| Printed point / call-out | Question |
|---|---|
| Parasystole definition: VPCs with different / variable coupling intervals | MED-C7-10 |
| Multifocal VPCs: premature ventricular complexes presenting with different morphologies | MED-C7-11 |
| Interpolated VPC: premature ventricular complex sandwiched between two consecutive sinus impulses | MED-C7-12 |
| Frequency patterns: Ventricular bigeminy (VPB after every sinus beat), trigeminy (VPB after every 2 sinus beats), couplet (2 VPBs in a row) | MED-C7-13 |
| Definition of Ventricular Tachycardia: ≥ 3 VPBs in a row + HR > 100 bpm | MED-C7-14 |
| Clinical features and management of VPCs: asymptomatic or palpitations; no treatment required; prophylactic antiarrhythmics contraindicated without significant VT | MED-C7-15 |

Unasked points: **none found**.

### Book p409 / PDF45

| Printed point / call-out | Question |
|---|---|
| Warning signs for VPCs: increased frequency, multifocal, bigeminy/couplet, first episode > 40 yrs, not affected by exercise, parasystole, LV dysfunction | MED-C7-16 |
| Monomorphic VT ECG criteria: wide QRS tachycardia (> 0.16 s), rate > 200 bpm, all complexes look alike | MED-C7-17 |
| Sustained monomorphic VT definition: sustained duration ≥ 30 seconds | MED-C7-18 |
| 12-lead ECG panel demonstrating the transition from sustained monomorphic VT to ventricular bigeminy | MED-C7-19 |

Unasked points: **none found**.

### Book p410 / PDF46

| Printed point / call-out | Question |
|---|---|
| Cardinal features of VT: fusion beats (features of both sinus + VPC) and capture beats (point where sinus takes over) | MED-C7-20 |
| Brugada sign: distance from onset of QRS complex to nadir of S wave > 100 ms | MED-C7-21 |
| Josephson's sign: characteristic notching at the nadir of the S wave | MED-C7-22 |
| Precordial concordance: completely positive or completely negative concordance in chest leads indicating VT | MED-C7-23 |
| Brugada criteria for VT: RS complex absent or > 100 ms; no P waves / AV dissociation | MED-C7-24 |
| Stable VT management in structural heart disease: Amiodarone (150 mg IV bolus x 10 min, then 1 mg/min x 6h, then 0.5 mg/min x 18h) | MED-C7-25 |
| Stable VT management without structural heart disease: Procainamide DOC (20-50 mg/min, max 17 mg/kg); Lignocaine post-MI without structural disease; Sotalol | MED-C7-26 |
| Unstable VT management: synchronized DC cardioversion 100 - 360 J | MED-C7-27 |

Unasked points: **none found**.

### Book p411 / PDF47

| Printed point / call-out | Question |
|---|---|
| Polymorphic VT: multiple different complexes with changing polarities; usually associated with prolonged QT (Torsades de pointes) | MED-C7-28 |
| Acquired causes of TdP: MI, decreased K+, decreased Ca2+, decreased Mg2+, hypothermia, drugs (Class Ia, Ic, III; erythromycin; terfenadine) | MED-C7-29 |
| Congenital etiology of TdP: congenital Long QT syndrome | MED-C7-30 |
| Differential note on Short QT causes: Hypercalcemia, Digoxin, Hyperthermia | MED-C7-31 |
| Management of TdP: immediate defibrillation -> 2 g IV MgSO4 over 10 min -> rhythm stabilization (beta-blockers for congenital, treat cause for acquired) | MED-C7-32 |
| Cardioversion vs Defibrillation mechanism: current discharge at patient QRS vs machine discharge; T-wave vulnerable period (20 - 30 ms) risking VF | MED-C7-33 |

Unasked points: **none found**.

### Book p412 / PDF48

| Printed point / call-out | Question |
|---|---|
| Synchronized cardioversion (syncs with patient rhythm) vs unsynchronized defibrillation (no need to connect patient rhythm) | MED-C7-34 |
| Paddle placement positions: right side of upper sternum below clavicle and apex of heart (left of nipple) | MED-C7-35 |
| Energy settings across arrhythmias: start with 50 J; A. Flutter (50 J), Monomorphic VT (100 J), A. Fib (100 - 200 J), Polymorphic VT (200 J) | MED-C7-36 |

Unasked points: **none found**.

### Book p413 / PDF49

| Printed point / call-out | Question |
|---|---|
| WPW syndrome demographic profile: Male predominance (M > F) | MED-C8-01 |
| Classic ECG findings of WPW: normal P wave, short PR interval, delta waves, near normal QRS, secondary ST & T wave changes | MED-C8-02 |
| WPW mechanism: aberrant accessory pathway known as the Bundle of Kent causing ventricular pre-excitation | MED-C8-03 |
| Concealed vs Manifest WPW: 12-lead ECG (normal vs abnormal) and antegrade conduction (via AV node vs via Bundle of Kent) | MED-C8-04 |
| Arrhythmias triggered by PAC in concealed and manifest WPW: Orthodromic AVRT and Atrial Fibrillation | MED-C8-05 |
| Prognosis of Atrial Fibrillation: bad prognosis in concealed WPW responding only to DC cardioversion; better prognosis in manifest WPW d/t early diagnosis | MED-C8-06 |

Unasked points: **none found**.

### Book p414 / PDF50

| Printed point / call-out | Question |
|---|---|
| WPW anatomical classification: Left sided WPW is Type A (most common) | MED-C8-07 |
| Left-sided WPW (Type A): small delta wave, conduction Lt -> Rt, positive tall R wave and delta wave in lead V1 | MED-C8-08 |
| Right-sided WPW (Type B): large delta wave, conduction Rt -> Lt, negative R wave and delta wave in lead V1 | MED-C8-09 |
| Vector differentiation of Type A vs Type B: left-to-right vs right-to-left conduction and delta wave size | MED-C8-10 |
| Manifest WPW activation sequence: Bundle of Kent causes short PR and delta wave; AV node catches up to produce near normal QRS complex | MED-C8-11 |
| Concealed WPW management: AVRT treated with Adenosine and EP referral; A.fib treated with synchronised DC cardioversion | MED-C8-12 |
| Manifest WPW management: Early diagnosis managed definitively by catheter ablation (definitive Rx) | MED-C8-13 |
| Post-conversion finding in manifest WPW: termination of AVRT or A.fib reveals sinus rhythm + delta wave, followed by electrophysiologist referral | MED-C8-14 |

Unasked points: **none found**.

### Book p415 / PDF51

| Printed point / call-out | Question |
|---|---|
| The ACS flowchart links rupture/erosion with critical fibrin-rich thrombosis to STEMI; incomplete platelet-rich thrombosis leads to NSTEMI. | MED-C9-01 |
| Epicardial arteries larger than 400 μm are placed in macrocirculation; small arteries, arterioles and capillaries form the microcirculatory side. | MED-C9-02 |
| The diagram assigns flow and transport to epicardial arteries, pressure and regulation to small arteries/arterioles, and metabolites/exchange to capillaries. | MED-C9-03 |
| Syndrome X is described as critical microvascular disease with impaired coronary reserve, reduced NO and increased endothelin/CRP. | MED-C9-04 |
| The table labels this young-smoker, rest-angina, slow-flow phenotype as Syndrome Y; thickened wall/decreased lumen raise resting coronary resistance and prognosis includes arrhythmia/sudden death. | MED-C9-05 |
| Syndrome Y is linked to young male smokers, rest angina, slow flow, vasodilator response and risk of sudden death/arrhythmias; the benign/antianginal profile is Syndrome X. | MED-C9-06 |

Unasked points: **none found**.

### Book p416 / PDF52

| Printed point / call-out | Question |
|---|---|
| O2 demand: systemic SBP, HR, myocardial contractility and myocardial wall stress. Supply: coronary resistance/diameter, HR and perfusion pressure. | MED-C9-07 |
| Syndrome Z is associated with OSAS and is drawn with centripetal obesity, insulin resistance, hypertension and hyperlipidaemia. | MED-C9-08 |
| Large-vessel CAD causes listed are plaque, septic/other emboli, spasm (Prinzmetal angina), and vasculitis including Takayasu/Kawasaki. | MED-C9-09 |
| Smoking is explicitly marked as the most crucial preventable cause; family history, calcification, inactivity, diabetes, age and sex are also risk factors. | MED-C9-10 |
| The sheet marks hs-CRP <1 mg/dL as low, 1–3 as increased, and >3 mg/dL as markedly increased. | MED-C9-11 |
| The hyperlipidaemia list includes hs-CRP, Lp(a), Lp-PLA2, high small dense/oxidised LDL and low HDL. | MED-C9-12 |
| Plaque is termed atherosclerotic coronary vascular disease (ASCVD); stenosis around 60–70% or more is marked significant. | MED-C9-13 |

Unasked points: **none found**.

### Book p417 / PDF53

| Printed point / call-out | Question |
|---|---|
| Hibernation is chronic persistent ischaemic dysfunction; the table notes FDG-PET > MRI for differentiating ischaemia and infarction. | MED-C9-14 |
| Stunning is an acute, transient post-reperfusion segmental dysfunction, whereas hibernation is a chronic state. | MED-C9-15 |
| The page lists LDL >190 mg/dL with target <100 mg/dL, diabetes age 40–75 (moderate-intensity rosuvastatin 10–20 mg), and clinical atherosclerosis. | MED-C9-16 |
| The printed HOPE note reads ‘Ramipril ↓ fatal/non-vascular events → ACE inhibitors > ARBs.’ | MED-C9-17 |
| Agatston score is determined by coronary CT; calcification is noted as irreversible, and medial calcification is linked to increased PTH and Ca×PO4. | MED-C9-18 |
| The printed advice is salt <6 g/day, protein 1 g/kg/day, dietary cholesterol <200 mg/day, soluble fibre >10–25 g/day, and saturated fat <7%. | MED-C9-19 |

Unasked points: **none found**.

### Book p418 / PDF54

| Printed point / call-out | Question |
|---|---|
| In the diagram, >70% plaque with symptoms leads to angiography/stenting; the asymptomatic branch is labelled ACS. A roughly 20–30% plaque may rupture and cause MI. | MED-C9-20 |
| Chronic stable angina is exertional chest tightness/squeezing/burning behind or left of mediastinum, can radiate C8–T4, lasts <20 min, and responds well to SL/oral NTG; >30 min suggests ACS. | MED-C9-21 |
| Treadmill testing is indicated in chronic stable angina and asymptomatic risk-factor patients; rest symptoms, aortic stenosis and HOCM are contraindications. | MED-C9-22 |
| Positive treadmill test: 2 mm horizontal/downsloping ST segment before 6 minutes/before achieving maximum HR, followed by angiography. | MED-C9-23 |
| The presentation block states radiation may involve any dermatome from C8 to T4. | MED-C9-24 |

Unasked points: **none found**.

### Book p419 / PDF55

| Printed point / call-out | Question |
|---|---|
| MPS is done with Tc-99m or thallium; listed uses include rest symptoms, localisation, abnormal baseline ECG, and assessing completeness of revascularisation. | MED-C9-25 |
| FDG-PET distinguishes stunned from scarred myocardium. The source also states FDG-PET/MRI are preferred over MPS to distinguish ischaemia from infarction. | MED-C9-26 |
| The page identifies exercise radionuclide angiography/MUGA for cardiac volumes and functions. | MED-C9-27 |
| MRI is marked IOC for myocardial fibrosis/ejection fraction and gold standard for ejection fraction; IVUS is IOC for ostial left-main lesion/coronary dissection. | MED-C9-28 |
| After SL NTG 3 tablets/20 min without improvement, the flowchart flags ACS and lists NTG plus beta-blockers as first line. | MED-C9-29 |
| Ivabradine inhibits funny current and lowers HR; visual disturbance is its source-listed adverse effect. Trimetazidine inhibits pFOX with no BP/HR effect; ranolazine may prolong QT. | MED-C9-30 |
| Fasudil is shown as a Rho-kinase inhibitor; nicorandil is a K+ channel activator. | MED-C9-31 |

Unasked points: **none found**.

### Book p420 / PDF56

| Printed point / call-out | Question |
|---|---|
| The stenting note lists abciximab, eptifibatide and tirofiban as GP IIb–IIIa inhibitors and favours tacrolimus/paclitaxel drug-eluting over bare-metal stents. | MED-C9-32 |
| Prinzmetal angina is rest angina, lasts 5–15 min, has transient ST elevation and normal angiography; beta-blockers are to be avoided. | MED-C9-33 |
| Kingmaker segment is stated to be the ST segment: end of J point to onset of T wave. | MED-C9-34 |
| Systolic current from subepicardial/transmural injury flows toward injured myocardium and produces ST elevation (MI or pericarditis); subendocardial diastolic current flows away and produces non-localising ST depression. | MED-C9-35 |
| The diagrams contrast non-concave/convex ST elevation in MI with concave/saddle-shaped elevation in pericarditis. | MED-C9-36 |

Unasked points: **none found**.

### Book p421 / PDF57

| Printed point / call-out | Question |
|---|---|
| Listed alternatives are Prinzmetal angina, hyperkalaemia > hypokalaemia, LBBB, benign early repolarisation and LV aneurysm. | MED-C9-37 |
| Convex and coved morphologies are labelled ACS; horizontal/plateau is ‘ACS unless proven otherwise’; oblique is <30% ACS and concave <15% ACS. | MED-C9-38 |
| Significant V2–V3 elevation is ≥2.5 mm if <40 years, ≥2 mm if >40 years, and ≥1.5 mm in females; reciprocal changes must be present in the source's MI diagnosis note. | MED-C9-39 |
| The sequence progresses from hyperacute T wave to hyperacute T waves with ST elevation, then pathological Q/decreasing R and further ST/T changes over hours to days. | MED-C9-40 |
| The illustrated tracing is captioned ST elevation with reciprocal changes and marks a high lateral MI pattern. | MED-C9-41 |

Unasked points: **none found**.

### Book p422 / PDF58

| Printed point / call-out | Question |
|---|---|
| Benign early repolarisation has ST elevation and J-point hook effect; PR depression supports pericarditis instead. | MED-C9-42 |
| The pericarditis block gives clinical features/acute illness, global concave upward ST elevation, PR depression and no reciprocal changes. | MED-C9-43 |
| Hypothermia is labelled with an Osborne wave. The page also illustrates post-DC-cardioversion tracing and Takotsubo cardiomyopathy. | MED-C9-44 |
| Takotsubo cardiomyopathy is labelled catecholamine-induced cardiac failure/broken-heart syndrome and most common in middle-aged females. | MED-C9-45 |
| The printed differential says BER has no PR depression; pericarditis has PR depression, global concave elevation and no reciprocal changes. | MED-C9-46 |

Unasked points: **none found**.

### Book p423 / PDF59

| Printed point / call-out | Question |
|---|---|
| The summary panel lists LVH, LBBB, acute pericarditis, pseudo-infarction pattern (hyperkalaemia), acute anteroseptal MI, acute anterolateral MI and Brugada syndrome. | MED-C9-47 |
| The summary labels horizontal ST depression ‘probable ischemia’; sloping ST is strain-related and scoop-shaped ST is digoxin-related. | MED-C9-48 |
| The ‘scoop’ example is explicitly labelled digoxin related; morphology must be interpreted in clinical context. | MED-C9-49 |
| The final tracing is captioned ‘de Winter T waves: evolves to MI.’ | MED-C9-50 |

Unasked points: **none found**.

### Book p424 / PDF60

| Printed point / call-out | Question |
|---|---|
| The page contrasts normal myocardium, tall/peaked T waves in subendocardial ischaemia, and deep symmetrical inversion in transmural ischaemia. | MED-C9-51 |
| Deep symmetrical T inversion is labelled transmural ischaemia; tall/peaked T waves are subendocardial ischaemia. | MED-C9-52 |
| The lower paired ECGs show hyperacute T waves progressing to STEMI. | MED-C9-53 |
| The note beneath the strip states ‘U waves: Hypokalemia.’ | MED-C9-54 |
| The page presents serial ST-depression changes at 60, 90 and 120 minutes before its T-wave panels. | MED-C9-55 |

Unasked points: **none found**.

### Book p425 / PDF61

| Printed point / call-out | Question |
|---|---|
| Right coronary circulation is linked to IWMI, PWMI and RVMI; left circulation is linked to AWMI, septal MI and LWMI. | MED-C10-01 |
| Surface list: anterior sternocostal = RV; inferior diaphragmatic = RV+LV; posterior = LA. | MED-C10-02 |
| Dominance is based on the artery supplying posterior interventricular sulcus/PDA: RCA gives right dominance (85%); LCx gives left dominance (15%). | MED-C10-03 |
| Inferior leads are II, III, aVF; RV free-wall V3R/V4R/V5R and posterior V7/V8/V9 are not represented on a standard 12-lead ECG; lateral V5/V6 show reciprocal changes. | MED-C10-04 |
| Right free-wall leads are V3R–V5R. The source separately lists V7–V9 for posterior wall assessment. | MED-C10-05 |

Unasked points: **none found**.

### Book p426 / PDF62

| Printed point / call-out | Question |
|---|---|
| The RCA is shown arising in the right AV sulcus. | MED-C10-06 |
| The SA nodal branch section states proximal RCA occlusion can cause sinus bradycardia; bradycardia can also reflect vagal stimulation or nodal ischaemia. | MED-C10-07 |
| Atrial branches run in the right atrioventricular sulcus; proximal RCA occlusion is linked to atrial arrhythmias. | MED-C10-08 |
| Occlusion relation to acute marginal artery: proximal means RVMI always positive and poorer prognosis; distal means RVMI always negative. | MED-C10-09 |
| The acute marginal artery supplies the RV free wall. | MED-C10-10 |
| The page's RVMI triangle is hypotension, clear lung fields and raised JVP, with management IV fluids. | MED-C10-11 |
| RCA occlusion flowchart: right dominant proximal → RVMI+IWMI±PWMI; right dominant distal → IWMI±PWMI. Left-dominant distal RCA causes no MI. | MED-C10-12 |
| IWMI list includes SA node/AV node/complete heart block, atrial tachycardia, RVMI, and posteromedial papillary muscle rupture causing secondary MR. | MED-C10-13 |

Unasked points: **none found**.

### Book p427 / PDF63

| Printed point / call-out | Question |
|---|---|
| For RCA: ST↑ in II/III/aVF, reciprocal V1/V5/V6; III > II and ST↓ aVL > aVR. LCx instead has II > III. | MED-C10-14 |
| Proximal RCA: ST depression in V1 discordant to V2/V3 is marked RVMI positive. ‘Wrap around’ indicates RCA supplies all regions. | MED-C10-15 |
| The LCx note lists IWMI+PWMI and ST elevation in II > III; in left dominance, LCx lateral-wall supply may add LWMI. | MED-C10-16 |
| The page identifies papillary muscle rupture → secondary MR in post-IWMI PCI with CCF; it notes LV S3, absent murmur, good EF and normal/near-normal ECG. | MED-C10-17 |
| LCA branches into LCx and LAD; the LAD site is the left anterior interventricular sulcus. | MED-C10-18 |
| LCx/LAD branch map: D1 high lateral wall, S1 septal wall, D2 anterior wall, D3 lateral wall; D=diagonal and S=septal. | MED-C10-19 |
| LAD/LCx lead map: anterior V2–V4, lateral V5–V6, high lateral I/aVL, septal V1>>V2, apical V1. | MED-C10-20 |

Unasked points: **none found**.

### Book p428 / PDF64

| Printed point / call-out | Question |
|---|---|
| The localisation list proceeds: before D1; between D1 and S1; and below S1 (with branches S1–D2 or D2–D3). | MED-C10-21 |
| For anteroseptal high-lateral MI: V2–V4 elevation indicates LAD, V1 elevation indicates above S1, and I/aVL elevation indicates before D1. | MED-C10-22 |
| The wrap-around section says V2–V4 elevation is above D2; V1 no elevation is below S1; II/V5/V6 elevation identifies wrap-around. | MED-C10-23 |
| The page explicitly labels II, V5 and V6 elevation as wrap-around phenomenon; course enters posterior interventricular sulcus and anastomoses with PDA. | MED-C10-24 |
| The source states anterolateral MI has anatomical S1 before D1 and occlusion between S1 and D1. | MED-C10-25 |
| The anteroseptal section labels V1 ST elevation as above S1 and I/aVL ST depression as between D1 and S1. | MED-C10-26 |

Unasked points: **none found**.

### Book p429 / PDF65

| Printed point / call-out | Question |
|---|---|
| Proximal LCA occlusion: aVR ST elevation, all other leads ST depression, 100% mortality if untreated; immediate PCI is specified. | MED-C10-27 |
| AWMI LV involvement includes VT, VF and sudden cardiac death; mechanical complications include external cardiac rupture and septal rupture, plus infra-Hisian blocks. | MED-C10-28 |
| The AWMI complication list includes infra-Hisian blocks, in contrast to the nodal problems emphasised in IWMI. | MED-C10-29 |

Unasked points: **none found**.

### Book p430 / PDF66

| Printed point / call-out | Question |
|---|---|
| The obsolete scheme maps critical fibrin-rich thrombus to STEMI/STE-ACS and incomplete platelet-rich thrombus to NSTE-ACS; normal enzymes mean unstable angina and raised enzymes NSTEMI. | MED-C11-01 |
| The page replaces the older model with myocardial injury ± clinical evidence of myocardial ischaemia. | MED-C11-02 |
| Myocardial injury is cardiac troponin T/I with at least one value above the 99th percentile and an acute rise and fall. | MED-C11-03 |
| Non-cardiac causes listed include sepsis, subarachnoid haemorrhage, CKD, critical illness and pulmonary embolism. Cardiac causes include myocarditis, Takotsubo, defibrillator shocks, tachyarrhythmia and spasm/embolism/dissection. | MED-C11-04 |
| The causes tree lists increased O2 demand from tachyarrhythmia and decreased supply from spasm, embolism or dissection. | MED-C11-05 |

Unasked points: **none found**.

### Book p431 / PDF67

| Printed point / call-out | Question |
|---|---|
| Clinical evidence listed: symptoms, new ECG changes, pathological Q waves, imaging evidence of new RWMA, and angiographic evidence of coronary thrombus. | MED-C11-06 |
| Type 1 is atherothrombotic occlusion; Type 2 is supply/demand mismatch (ICU patients, severe anaemia); Type 3 sudden cardiac death; Type 4 post-PCI; Type 5 post-CABG. | MED-C11-07 |
| The list gives Type 4 as post-percutaneous coronary intervention and Type 5 as post-coronary artery bypass graft. | MED-C11-08 |
| The graph note says ultrasensitive troponin assays can detect as low as 0.01 ng/mL of enzyme elevation. | MED-C11-09 |
| Rise/fall with acute ischaemia is acute MI; the atherosclerosis/thrombosis arm is Type 1 (plaque rupture/erosion). Without acute ischaemia it is acute injury; stable troponin is chronic injury. | MED-C11-10 |
| The stable-troponin branch is chronic myocardial injury and gives structural heart disease and CKD as examples. | MED-C11-11 |

Unasked points: **none found**.

### Book p432 / PDF68

| Printed point / call-out | Question |
|---|---|
| The table defines reinfarction within 28 days and recurrence after 28 days. | MED-C11-12 |
| Two troponin values are obtained immediately and 3–6 h later; a >20% increase is specified. The table says no role for CPK-MB. | MED-C11-13 |
| Plaque rupture is 60–70% (most common), associated with men and elevated cholesterol; erosion 30–40% is associated with younger females and smoking. | MED-C11-14 |
| Vulnerable plaque features: thin cap, necrotic lipid core >40%, increased macrophages, reduced smooth-muscle cell content and spotty calcification. | MED-C11-15 |
| Hibernating myocardium is chronic, viable and has reduced function due to low perfusion; MRI should be used for evaluation. | MED-C11-16 |
| Stunned myocardium is acute/post-ischaemic: restoring perfusion for a few hours precedes low function in viable tissue. | MED-C11-17 |

Unasked points: **none found**.

### Book p433 / PDF69

| Printed point / call-out | Question |
|---|---|
| NSTEMI features listed are rest angina >20 min, new-onset severe/crescendo angina, ST depression/T inversion and elevated troponin. | MED-C11-18 |
| The NSTEMI feature list states TIMI score determines mortality risk. | MED-C11-19 |
| Clinical presentation states age 40–50 in India (50–60 outside), females > males in India (reverse outside), vague symptoms in females and absent classic pain in diabetic patients. | MED-C11-20 |
| The lower ECG caption identifies significant ST depression as NSTEMI; the comparison example is non-significant ST depression. | MED-C11-21 |

Unasked points: **none found**.

### Book p434 / PDF70

| Printed point / call-out | Question |
|---|---|
| The table gives right arm/shoulder radiation 4.7 (0.9–12.0), both arms 4.1, exertion 2.4, left arm 2.3, diaphoresis 2.0, nausea/vomiting 1.9 and pressure 1.3. | MED-C11-22 |
| ACA note: new chest pain in middle-aged/elderly, night presentation or being forced awake and unable to sleep is ‘cardiac unless proved otherwise.’ | MED-C11-23 |
| Angina equivalents listed are dyspnoea, fatigue, diaphoresis and atypical-site pain. | MED-C11-24 |
| Management continuum: pre-CCU morphine/sedation 30% one-month mortality; CCU beta-blocker/defibrillator 15%; reperfusion with thrombolysis/PCI 5%. | MED-C11-25 |
| The source places thrombolysis and percutaneous intervention under reperfusion (since 1975). | MED-C11-26 |

Unasked points: **none found**.

### Book p435 / PDF71

| Printed point / call-out | Question |
|---|---|
| STEMI salient feature: acute total occlusion due to plaque rupture (most common). | MED-C11-27 |
| The artery list ranks LAD most common, then RCA, then LCx. | MED-C11-28 |
| Golden hours are the first 6 h. After 6 h from pain onset, only one-sixth of myocardium remains viable in the source. | MED-C11-29 |
| Before 6 h myocardium can be salvaged; after 6 h the stated aims are pain reduction and prevention of electrical/mechanical complications. | MED-C11-30 |
| The graph says opening the artery is the primary goal (PCI/lysis) and time to treatment is critical for mortality/salvage. | MED-C11-31 |

Unasked points: **none found**.

### Book p436 / PDF72

| Printed point / call-out | Question |
|---|---|
| Determinants listed are collaterals, myocardial oxygen demand and ischaemic preconditioning. | MED-C11-32 |
| The source specifically notes reopening the artery is more important than the mode of reperfusion. | MED-C11-33 |
| The flowchart sets first medical contact <10 min and defines it as medical/paramedical staff able to take/interpret ECG and use a defibrillator. | MED-C11-34 |
| If a 24-hour PCI centre is available and diagnosis-to-wire crossing <60 min, wire crossing is to be done within 90 min (+30 min transfer). | MED-C11-35 |
| If timely transfer is not possible, thrombolysis within 10 min with tenecteplase or reteplase is shown, then transfer to a PCI centre. | MED-C11-36 |
| ST resolution >70% is successful and leads to pharmaco-invasive PCI; <70% is unsuccessful and calls for rescue/emergency PCI. | MED-C11-37 |
| Successful lysis is followed by PCI within 2–24 hours to prevent recurrence of thrombus formation. | MED-C11-38 |

Unasked points: **none found**.

### Book p437 / PDF73

| Printed point / call-out | Question |
|---|---|
| Streptokinase is non-specific, 50% potent, antigenic, has lowest ICH risk and is 1.5 million U in 100 mL NS over 1 hour. | MED-C11-39 |
| Tenecteplase is specific (max), 75% potent, half-life 10–12 min, dose 0.5 mg/kg, and highest fibrin selectivity. | MED-C11-40 |
| Reteplase is specific, 80% potent and dosed 10 U ×2, 30 min apart. | MED-C11-41 |
| Alteplase is specific, 75% potent and has a very short 4–8 minute half-life. | MED-C11-42 |
| The source states effect within 1 h of ACS: thrombolysis = PCI, while PCI is otherwise more superior and mandatory after thrombolysis. | MED-C11-43 |
| Thrombolysis benefits > risk within 6–12 h, risk > benefit after 12 h; pre-hospital lysis is noted to have a great outcome. | MED-C11-44 |
| Loading-dose section gives aspirin 325 mg, non-enteric chewable; statins: atorvastatin 40–80 mg or rosuvastatin 20–40 mg. | MED-C11-45 |
| Note: RVMI has hypotension, clear lung and raised JVP; IWMI has bradycardia due to proximal occlusion and V1–V2 discordance. | MED-C11-46 |

Unasked points: **none found**.

### Book p438 / PDF74

| Printed point / call-out | Question |
|---|---|
| For thrombolysis: clopidogrel 300 mg adult dose; age >75 receives 75 mg, with blood-cholesterol monitoring at 3–6 months. | MED-C11-47 |
| PCI section: aspirin/statin same dose; ticagrelor 180 mg best, clopidogrel 600 mg, prasugrel 60 mg. | MED-C11-48 |
| PCI aim is restore normal epicardial coronary flow (TIMI 3) and attain normal microvascular flow (MPG 3). | MED-C11-49 |
| Post-lysis hypotension + bradycardia indicates vessels reopening; hypertension + tachycardia suggests noncompliance/allergic reaction. | MED-C11-50 |
| Low BP causes listed: hypovolaemia → assess IVC; RVMI (IWMI) → IV fluids; cardiogenic shock → intra-aortic balloon pump. | MED-C11-51 |
| Prevention of recurrence: post-thrombolysis raw areas exposed → anticoagulants. LMWH: enoxaparin 30 mg bolus plus 1 mg/kg SC BD until revascularisation/8 days; UFH also listed. | MED-C11-52 |
| Young thrombus responds better if lysed within 1–2 h; if primary PCI cannot be performed after STEMI diagnosis, fibrinolytic therapy is recommended within 12 h. | MED-C11-53 |

Unasked points: **none found**.

### Book p439 / PDF75

| Printed point / call-out | Question |
|---|---|
| GP IIb–IIIa inhibitors are abciximab, tirofiban, eptifibatide; use is downstream bailout in cath lab if no TIMI 3/MPG 3 flow or high thrombus burden. | MED-C11-54 |
| ACE inhibitors/beta-blockers have survival advantage if started within first 24 h, but are avoided with heart-failure signs/low-output state. | MED-C11-55 |
| Available PCI centre branch lists aspirin 325 mg, ticagrelor 180 mg or clopidogrel 600 mg, rosuvastatin 40 mg, then cath lab. | MED-C11-56 |
| No-centre branch: thrombolysis with clopidogrel 300 mg + tenecteplase 0.5 mg/kg, repeat ECG after 60–90 min, then enoxaparin 30 mg IV and pharmaco-invasive/rescue PCI. | MED-C11-57 |
| CCU/discharge box: rosuvastatin 20 mg lifelong, aspirin 75 mg lifelong, clopidogrel 75 mg ×1 year. | MED-C11-58 |
| Contraindications include intracranial haemorrhage/structural mass, recent stroke, bleeding disorder/aortic dissection, recent severe head/facial trauma, intracranial/intraspinal surgery, uncontrolled HTN, and recent streptokinase use. | MED-C11-59 |

Unasked points: **none found**.

### Book p440 / PDF76

| Printed point / call-out | Question |
|---|---|
| Hemodynamic complication: RVMI hypotension presents with raised JVP and clear lungs; management is IV fluids. | MED-C11-60 |
| Acute LVF is linked to 25% myocardial damage and proximal LAD lesion; cardiogenic shock to 40% damage/proximal LAD. | MED-C11-61 |
| Electrical complications: RCA lesion → atrial arrhythmias; proximal LAD lesion → VT/VF. | MED-C11-62 |
| Septal rupture is described as rare, after 3–5 days, with pain, new LLSB murmur and thrill. | MED-C11-63 |
| Free-wall rupture causes electromechanical dissociation/PEA, no BP/no pulse and tamponade, with poor prognosis. | MED-C11-64 |
| Acute MR: RCA involvement affects posteromedial papillary muscle and presents as acute pulmonary oedema. | MED-C11-65 |
| NSTEMI pathogenesis is plaque rupture in elderly/comorbid people with critical/subtotal occlusion, ST/T changes, platelet-rich thrombus and decreased fibrin, so no thrombolytic role. | MED-C11-66 |

Unasked points: **none found**.

### Book p441 / PDF77

| Printed point / call-out | Question |
|---|---|
| Clinical presentation on p441 describes increasing nature/duration (>20 min)/frequency and pain not relieved by nitrates/rest. | MED-C11-67 |
| Treatment: O2 if SpO2<90%, aspirin 325 mg chewable non-enteric, rosuvastatin 40 mg, SL nitrate 5 mg repeated three times, morphine, PCI within 24 h (high risk within 2 h). | MED-C11-68 |
| Landmark changes list intervention-based guideline: PCI TOC; angiography within 24 h (high risk 2 h), with P2Y12 inhibitor in cath lab. | MED-C11-69 |
| Peri-interventional anticoagulation: enoxaparin 0.5 mg/kg bolus until cath lab. | MED-C11-70 |
| Cath-lab loading options: prasugrel 60 mg, ticagrelor 180 mg, or clopidogrel 600 mg. | MED-C11-71 |
| After discharge: aspirin 75 mg lifelong, rosuvastatin 20 mg lifelong, and ticagrelor 90 mg BD ×1 y or clopidogrel 75 mg OD ×1 y or prasugrel 10 mg ×1 y (best). | MED-C11-72 |

Unasked points: **none found**.

### Book p442 / PDF78

| Printed point / call-out | Question |
|---|---|
| The CTD map marks rheumatoid arthritis as most common and Sjogren syndrome as second most common. | MED-C12-01 |
| Sjogren syndrome is described as a multisystem autoimmune inflammatory CTD in middle-aged females (40–60) with F:M = 9:1. | MED-C12-02 |
| Secondary Sjogren has CTD association, ranked RA > SLE > IMD; primary has no such association. | MED-C12-03 |
| Classification by pathology divides glandular (50%) and extraglandular (50%); extraglandular disease is multisystem and 15% is severe/life-threatening. | MED-C12-04 |
| The clinical hallmark is dry eye and dry mouth; thyroid is noted as the simple endocrine organ involved and Sjogren can be an extrahepatic manifestation of HCV. | MED-C12-05 |

Unasked points: **none found**.

### Book p443 / PDF79

| Printed point / call-out | Question |
|---|---|
| HCV extrahepatic manifestations listed are cutaneous lichen planus, porphyria cutanea tarda, cryoglobulinaemia, Sjogren syndrome and MPGN. | MED-C12-06 |
| Genetic/environmental factors → autoantibodies → autoimmune lymphocytic exocrinopathy (periductal/perivascular) → ductal epithelial activation → the listed sicca symptoms. | MED-C12-07 |
| Genetic factors list HLA-DR3; the note identifies SLE as another disease associated with HLA-DR3. | MED-C12-08 |
| The inflammation line states T cell (Th1 > Th2) > B cell. | MED-C12-09 |
| IL-18-positive macrophages are linked to salivary-gland enlargement/painless parotid enlargement. | MED-C12-10 |
| Antibodies list anti-M3 (muscarinic) → cholinergic agonist cevimeline for treatment, and anti-α-fodrin. | MED-C12-11 |

Unasked points: **none found**.

### Book p444 / PDF80

| Printed point / call-out | Question |
|---|---|
| Histopathology states minor salivary gland is gold standard and shows focal lymphocytic sialadenitis with T cells; major gland has benign lymphoepithelial lesions with B cells. | MED-C12-12 |
| The major-gland B-cell infiltration panel is labelled CD20; the T-cell infiltration panel is CD3. | MED-C12-13 |
| Minor salivary gland biopsy is gold standard and demonstrates focal lymphocytic sialadenitis with T-cell infiltration. | MED-C12-14 |
| Dry eyes are non-specific and may result from aqueous plus lipid/meibomian-gland dysfunction, producing irritation, gritty/sandy sensation and glare. | MED-C12-15 |
| Dry-eye diagnosis: Schirmer <5 mm after 5 min; tear-film breakup time <10 s; ocular staining may use lissamine green or fluorescein. | MED-C12-16 |
| The source marks tear-film breakup time <10 seconds as dry eye. | MED-C12-17 |
| The source calls dry eyes non-specific and dry mouth more specific. | MED-C12-18 |
| Dry mouth manifestations: unable to swallow without water, chewing difficulty and dental caries. | MED-C12-19 |

Unasked points: **none found**.

### Book p445 / PDF81

| Printed point / call-out | Question |
|---|---|
| Continuation lists oral thrush, altered taste, and 25% salivary-gland swelling. | MED-C12-20 |
| The source gives 25% salivary-gland swelling, usually bilateral painless symmetric. | MED-C12-21 |
| Childhood Sjogren is described as recurrent acute parotitis due to duct blockage. | MED-C12-22 |
| Asymmetric painful swelling with palpable nodules signals B-cell lymphoma (extranodal marginal-zone B-cell lymphoma), associated with cryoglobulinaemia and low C3/C4. | MED-C12-23 |
| Predictors listed: low complement (C3/C4), anti-Ro/La (SS-A/SS-B), positive RF and cryoglobulins. | MED-C12-24 |
| Positive anti-Ro/La in diagnosed Sjogren indicates extraglandular disease, poorer prognosis, B-cell lymphoma risk and salivary-gland enlargement; ~5% may develop disease after 10–15 years. | MED-C12-25 |
| Manifestations include fatigue and arthralgia/arthritis with non-erosive Jaccoud arthropathy. | MED-C12-26 |

Unasked points: **none found**.

### Book p446 / PDF82

| Printed point / call-out | Question |
|---|---|
| Severe manifestations (15%) include CNS ganglionopathy from dorsal-root-ganglion involvement, causing truncal ataxia. | MED-C12-27 |
| Lung: risk ILD; most common NSIP. Most characteristic is lymphocytic interstitial pneumonia (LIP) with GGO, cysts and nodules. | MED-C12-28 |
| LIP is marked most characteristic and has GGO, cyst and nodules. | MED-C12-29 |
| Renal: tubulointerstitial kidney disease causes distal RTA and has minor CKD risk. | MED-C12-30 |
| Raynaud may precede sicca in one-third and may produce critical limb ischaemia. | MED-C12-31 |
| Small-vessel vasculitis is most common and hallmark lesion is palpable purpura. Medium-vessel disease is severe, with ulcers/gangrene, MPGN and neuropathy. | MED-C12-32 |
| The source describes severe medium-vessel vasculitis with ulcer/gangrene and association with MPGN and neuropathy. | MED-C12-33 |
| Lymphadenopathy prompts exclusion of lymphoma; indicators include persistent asymmetric painful nodular parotid enlargement with nodes, cryoglobulinaemia, low C3/C4, high Ro/La, purpura and leukopenia. | MED-C12-34 |

Unasked points: **none found**.

### Book p447 / PDF83

| Printed point / call-out | Question |
|---|---|
| Lymphocytic interstitial pneumonitis is associated with Sjogren and HIV. | MED-C12-35 |
| Cysts in lung: LIP, Langerhans-cell histiocytosis and lymphangioleiomyomatosis. | MED-C12-36 |
| ANA is a CTD screening test and is positive in 85% with Sjogren; if positive, ANA profile can detect anti-Ro/La. | MED-C12-37 |
| Anti-Ro is positive in 50%; anti-La has no independent value despite 33% positivity. | MED-C12-38 |
| Fine speckled is most common, metaphase cells negative, and suggests anti-Ro/La/Sjogren. Dense fine speckled has DFS-positive metaphase cells and rules out CTD. | MED-C12-39 |
| Minor salivary gland biopsy is IOC/gold standard and shows focal lymphocytic sialadenitis (T cell). | MED-C12-40 |
| Sialography note: unstimulated salivary flow rate <1.5 mL/15 min; it is marked ‘not done now.’ Ultrasound shows loss of gland homogeneity. | MED-C12-41 |

Unasked points: **none found**.

### Book p448 / PDF84

| Printed point / call-out | Question |
|---|---|
| Score 3: histopathology focus score ≥1/mm² and anti-Ro/SS-A. Score 1: ocular staining/Rose Bengal, Schirmer ≤5 mm/5 min, and salivary flow <0.1 mL/min. | MED-C12-42 |
| Rules: at least one symptom of ocular/oral dryness plus total score ≥4. | MED-C12-43 |
| Exclusions include prior head/neck radiation, active HCV, AIDS, sarcoidosis, amyloidosis, GVHD and IgG4-related disease. | MED-C12-44 |
| High anti-Ro/La in pregnancy increases congenital heart block risk (2–5%). The source contrasts offspring risk for CTD in Sjogren male versus SLE female contexts. | MED-C12-45 |
| Differential: sarcoidosis = ILD + uveitis + hilar adenopathy; IgG4-RD = storiform fibrosis + plasmacytic infiltrate + pancreatitis. | MED-C12-46 |
| Treatment: glandular saliva substitute/cevimeline/artificial tears. Fatigue/arthralgia uses low-dose steroid <7.5 mg/day + NSAIDs + HCQ; severe life-threatening disease uses high-dose steroid + immunosuppressant/MMF. | MED-C12-47 |

Unasked points: **none found**.

### Book p449 / PDF85

| Printed point / call-out | Question |
|---|---|
| The spectrum lists type 1 autoimmune pancreatitis, Mikulicz disease, Riedel thyroiditis, mediastinal fibrosis, primary sclerosing cholangitis and periaortitis; p450 calls type 1 AIP the most common manifestation. | MED-C13-01 |
| IgG4 is listed as least common (<5%). | MED-C13-02 |
| IgG4 is anti-inflammatory, blocks IgG–C1q binding, does not fix complement, and is a bispecific antibody with two antigen-binding sites that binds/sequesters antigen. | MED-C13-03 |
| Histology lists IgG4-predominant lymphoplasmacytic infiltrate, tumour-like lesions, storiform fibrosis, obliterative phlebitis and mild eosinophilia. | MED-C13-04 |
| Antigenic stimuli → IgG4 plasma-lymphocytic infiltrate → myofibroblast activation → TGF-β/PDGF → fibrosis; TGF-β is called most potent fibrogenic cytokine. | MED-C13-05 |
| The page's note pairs obliterative phlebitis with IgG4-related disease and Behcet disease. | MED-C13-06 |
| Clinical features: M>F, age 40–70 years, subacute onset; symptoms weight loss and myalgia. | MED-C13-07 |
| Features against IgG4-RD: fever, arthritis, neutrophil involvement and granuloma. Mild eosinophilia appears among histology/atopy-allergy history. | MED-C13-08 |

Unasked points: **none found**.

### Book p450 / PDF86

| Printed point / call-out | Question |
|---|---|
| Type 1 autoimmune pancreatitis is most common in IgG4-RD and presents with obstructive jaundice; ERCP is IOC and CT shows sausage pancreas/homogeneous enhancement. | MED-C13-09 |
| AIP is associated with endocrine insufficiency → type 3c DM and exocrine insufficiency → malabsorption. | MED-C13-10 |
| Salivary involvement is bilateral painless submandibular enlargement with minimal sicca symptoms. | MED-C13-11 |
| Orbital/periorbital lesions include orbital inflammatory pseudotumours; lacrimal enlargement/dacryoadenitis is marked most common orbital manifestation. | MED-C13-12 |
| Minor CNS manifestations are lymphocytic hypophysitis (postpartum women with ↑ICT) and pachymeningitis without parenchymal involvement. | MED-C13-13 |
| Tubulointerstitial disease is most common renal manifestation, with minimal CKD risk and no renal tubular acidosis; membranous nephropathy is glomerular involvement. | MED-C13-14 |

Unasked points: **none found**.

### Book p451 / PDF87

| Printed point / call-out | Question |
|---|---|
| The organ list continues with bile duct: primary sclerosing cholangitis. | MED-C13-15 |
| Lung: non-specific interstitial pneumonia (NSIP) and thickening of bronchovascular bundle. | MED-C13-16 |
| Aorta manifestation is periaortitis, associated with paravertebral mass. | MED-C13-17 |
| The page notes membranonephropathy manifestation of IgG4 disease → low complements. | MED-C13-18 |
| RCD 2020 criteria show pathologic/histologic features + serology + clinical features; serum IgG4 correlates with activity and is elevated in 40% cases. | MED-C13-19 |
| Other findings: IgG4/IgG ratio is a better marker. | MED-C13-20 |
| Mikulicz disease is enlargement of parotid, submandibular and lacrimal gland; history includes chronic sinusitis/nasal obstruction with eosinophilia. | MED-C13-21 |
| Steroids are first line with good response within two weeks but relapse risk; rituximab is the steroid-sparing agent to prevent relapse. | MED-C13-22 |
| Comparison: IgG4 has increased salivary enlargement, decreased sicca, good steroid response and relapse risk; Sjogren has decreased enlargement, increased sicca and sicca symptoms not steroid responsive. | MED-C13-23 |

Unasked points: **none found**.

### Book p452 / PDF88

| Printed point / call-out | Question |
|---|---|
| SLE is described as a disease of women of reproductive age (20–40) with 9:1 female predominance. | MED-C14-01 |
| The source lists positive concordance in >40% of identical twins and strong family history. | MED-C14-02 |
| Lupus nephritis is shown in adults 50–60% and childhood SLE 100%. | MED-C14-03 |
| Postmenopausal SLE has good prognosis, no CNS/renal symptoms, sicca/serositis/musculoskeletal symptoms, anti-Ro positive, anti-dsDNA negative and normal complements. | MED-C14-04 |
| The bottom notes state male SLE has poor prognosis; active SLE markers are anti-dsDNA positive and low complements. | MED-C14-05 |

Unasked points: **none found**.

### Book p453 / PDF89

| Printed point / call-out | Question |
|---|---|
| Genetic/environmental causes lead to defective clearance of apoptotic and NETotic debris, triggering immune dysregulation. | MED-C14-06 |
| TLR-7 and TLR-9 are labelled pattern-recognition receptors; hydroxychloroquine is drawn inhibiting this step. | MED-C14-07 |
| Activated plasmacytoid dendritic cells produce type I interferon/IFNα, identified as the central key pathogenic cytokine; anifrolumab is shown blocking it. | MED-C14-08 |
| The diagram depicts Th1, Th2 > Th17; Th2 cytokines IL-4, IL-5 and IL-13 aid B-cell activation. | MED-C14-09 |
| BAFF/B-lymphocyte stimulator (BLyS) is shown upregulated in SLE; belimumab inhibits it. | MED-C14-10 |
| B cells form immune complexes/type-III hypersensitivity that deposit in glomerulus (GN), synovial cavity (synovitis) and vessels (vasculitis). | MED-C14-11 |

Unasked points: **none found**.

### Book p454 / PDF90

| Printed point / call-out | Question |
|---|---|
| HLA factors listed: HLA-DR3 (seen in subacute cutaneous lupus) and HLA-DR2. | MED-C14-12 |
| Early complement deficiency affects debris clearance; ranking is C1q > C2 > C4 deficiency. | MED-C14-13 |
| Non-HLA factors include increased X-chromosome number → increased risk/IRAK gene, and chromosome 3 → TREX gene. | MED-C14-14 |
| Environmental factors include OCP, HRT, UV-B, EBV, silicosis (stimulates pulmonary alveolar macrophage → autoimmune trigger), vitamin-D deficiency and smoking. | MED-C14-15 |
| A bracket labels vitamin-D deficiency and smoking as minimal association; the source separately lists OCP, HRT, UV-B, EBV and silicosis. | MED-C14-16 |
| OCP and HRT head the environmental-factor list. | MED-C14-17 |
| HCQ is drawn over TLR-7/TLR-9; belimumab targets BLyS and anifrolumab blocks type-I interferon signalling in the diagram. | MED-C14-18 |

Unasked points: **none found**.

### Book p455 / PDF91

| Printed point / call-out | Question |
|---|---|
| Antibodies can appear before clinical features: SLE 3 years; Sjogren syndrome 10–15 years. | MED-C15-01 |
| ANA methodology: ELISA is only for quantitative assessment; IIF/indirect IF on HEp-2 cells, with titre >1:80, is used to look for pattern. | MED-C15-02 |
| The flowchart shows IIF (HEp-2) and titre >1:80, then look for pattern. | MED-C15-03 |
| Dense fine speckled pattern in mitotic-phase cells has no probable antibody listed and rules out CTD. | MED-C15-04 |
| Fine speckled pattern is linked to anti-Ro/La and Sjogren syndrome. | MED-C15-05 |
| Coarse speckled patterns include anti-Smith → SLE, anti-U1 RNP → MCTD, and anti-RNA polymerase 3 → systemic sclerosis. | MED-C15-06 |
| The coarse-speckled table maps anti-U1 RNP to MCTD. | MED-C15-07 |
| Nucleolar pattern with PM/Scl-70 is linked to polymyositis–scleroderma overlap. | MED-C15-08 |
| Cytoplasmic pattern with anti-Jo-1 is linked to polymyositis/dermatomyositis (antisynthetase syndrome). | MED-C15-09 |
| Homogeneous pattern: anti-dsDNA associates with SLE and antihistone with drug-induced SLE. | MED-C15-10 |
| The final row maps centromere pattern to CREST syndrome (scleroderma). | MED-C15-11 |

Unasked points: **none found**.

### Book p456 / PDF92

| Printed point / call-out | Question |
|---|---|
| Clinical suspicion → ANA positive → IIF pattern → further evaluation to confirm antibodies, using ANA profile or ENA profile. | MED-C15-12 |
| ANA profile: by immunoblot, costly/multiple antibody analysis, done once (no repeat values). ENA profile tests six antibodies. | MED-C15-13 |
| ANA positivity chart: 100% MCTD, DILE and type 1 autoimmune hepatitis; 85% Sjogren; 50% IgG4-related disease. In SLE it is positive in 97%. | MED-C15-14 |
| The source says RA is the most common multisystem CTD but ANA is not diagnostic. | MED-C15-15 |
| DILE features: 100% ANA positive, homogeneous IIF pattern, antihistone antibody positive, and procainamide cause. | MED-C15-16 |
| The DILE block lists procainamide as a cause. | MED-C15-17 |
| Note: elderly SLE → anti-Ro positive and ANA negative. | MED-C15-18 |

Unasked points: **none found**.

### Book p457 / PDF93

| Printed point / call-out | Question |
|---|---|
| Anti-dsDNA: ELISA for titre; Crithidia luciliae (flagella) is a qualitative IIF method marked obsolete. | MED-C15-19 |
| Crithidia luciliae (flagella) is specified as qualitative IIF, obsolete. | MED-C15-20 |
| Table: anti-dsDNA sensitivity 75% preferred; anti-Smith 25% more specific. | MED-C15-21 |
| The source states increased anti-dsDNA titres increase nephritis and vasculitis risk; no prognostic effect is listed for anti-Smith. | MED-C15-22 |
| Anti-Ro/La is non-specific in CTD and has no significance in asymptomatic patients. | MED-C15-23 |
| Within SLE, anti-Ro/La indicates secondary Sjogren; it is also linked to pregnancy CHB, SCLE/HLA-DR3/photosensitive lesions, good prognosis and lupus myocarditis. | MED-C15-24 |
| In pregnancy, anti-Ro/La is linked to 2–5% congenital heart block, increased in female child. | MED-C15-25 |
| Anti-Ro/La is associated with SCLE/HLA-DR3/photosensitivity and good prognosis: higher titres → reduced risk of nephritis/vasculitis; it is protective in skin/myocardium and linked to shrinking-lung syndrome. | MED-C15-26 |
| APS antibodies are positive in one-third of SLE patients. | MED-C15-27 |
| The antibody list identifies anti-RBC antibody in warm-antibody autoimmune haemolytic anaemia. | MED-C15-28 |
| Secondary ITP list: SLE, HIV, hepatitis C, H. pylori and RA, with bleeding/anaemia. | MED-C15-29 |
| Anti-ribosomal P is specific for psychosis/depression in CNS lupus; anti-glutamate/anti-neuronal antibody is most common in CNS lupus. | MED-C15-30 |
| The note names cognitive decline as the most common CNS manifestation in lupus. | MED-C15-31 |
| Biomarkers: anti-dsDNA titre, ↓C3/↓C4, and ↑ESR with ↓CRP. | MED-C15-32 |

Unasked points: **none found**.

## Post-build verification

- `python3 build_content.py` embedded 570 questions / 55 units / 15 live chapters into `pulse-medicine.html`.
- `python3 validate_content.py --embedded` passed exact source/HTML equality and all 57 roadmap flags.
- `tests/app_parsers.cjs` verified real offline-app parser compatibility across all 570 questions and match bijections.
- `python3 -m unittest discover -s tests -v` — 9 unit tests PASS.

