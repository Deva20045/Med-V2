# Chapters 2–8 — visual self-audit gate

Reviewed 2026-09-22, before live deployment. Source: `uploads/01.pdf`, 2× PyMuPDF renders. See [every-page map](PAGE_MAP.md) and machine-readable [inventory](coverage.json).

## Method and scope

- Read all educational headings, bullets, sub-bullets, notes, equations, tables, flowchart arms, annotated ECGs and morphology panels on printed p383–414 (PDF19–50). PDF13–18 were previously read for Chapter 1. All 103 PDF sheets were checked for printed page numbering.
- Reading order: top-to-bottom content blocks; parallel comparison columns treated as unified comparison blocks; diagrams remained with their adjacent text. Each unit is a contiguous slice of that sequence. Repeated publisher footers, lesson timestamps and 'Active space' furniture are excluded.
- Every inventoried point has an explicit question target. Strict quality control: zero predictable/trivial distractors, medically plausible answer choices, bijections on match items, balanced true/false pairs, and exact citation references.
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
| Total | 42 | 57 | 41 | 25 | 52 | 21 | 38 | 18 | 294 |

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

**Total: 402 mapped educational points; 294 questions; 34 units across 8 live chapters of 57.**

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

## Post-build verification

- `python3 build_content.py` embedded 294 questions / 34 units / 8 live chapters into `pulse-medicine.html`.
- `python3 validate_content.py --embedded` passed exact source/HTML equality and all 57 roadmap flags.
- `tests/app_parsers.cjs` verified real offline-app parser compatibility across all 294 questions and match bijections.
- `python3 -m unittest discover -s tests -v` — 9 unit tests PASS.

