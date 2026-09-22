# Chapters 2–4 — visual self-audit gate

Reviewed 2026-09-22, before the first HTML build. Source: `uploads/01.pdf`, 2× PyMuPDF renders. See [every-page map](PAGE_MAP.md) and machine-readable [inventory](coverage.json).

## Method and scope

- Read all educational headings, bullets, sub-bullets, notes, equations, tables, flowchart arms, annotated ECGs and morphology panels on printed p383–393. PDF13–18 were reread for the Chapter 1 rescue and anchor verification. All 103 PDF sheets were checked for their printed number or unnumbered front-matter status.
- Reading order: top-to-bottom content blocks; parallel comparison columns treated as a single comparison block, otherwise the left column precedes the right. Diagrams remain with their adjacent text. Each unit is a contiguous slice of that sequence. Repeated publisher footers, lesson timestamps and “Active space” furniture are not educational points.
- One question can test several tightly related points. Every inventoried point below has an explicit question target, not only a guide mention. Repeated facts at later locations retain later-page questions.
- Software verifies schema, exact app parsers, sequential IDs, page ordering, inventory ordering and full unit coverage. It cannot prove semantic completeness from an image: that part is the visual self-audit documented here.

## Rescue completed before new chapter authoring

`git log --oneline -3` returned only the shallow base `f6d6633`. `git cat-file -t fb7a917` found no local object. The existing artifact contained 44 questions, so the five supplied gaps were restored before Ch2–4 authoring; all later IDs and unit lists were rebuilt. Chapter 1 now contains 49 questions.

| Restored ID | Printed point |
|---|---|
| MED-C1-02 | p377 QRS call-outs: V1 small R/deep S; V5–V6 small Q/big R |
| MED-C1-03 | p377 start from lead II / rhythm strip |
| MED-C1-20 | p379 sternal angle = second ICS |
| MED-C1-32 | p380 upright II / biphasic V1 / inferior P-pulmonale panels |
| MED-C1-43 | p382 +90° aVF “Rightward axis” |

The 44 inherited question bodies were otherwise retained. Existing guides were split into two source lines to satisfy the guide-line gate. This rescue is not a claim to have rewritten or independently re-audited all inherited Ch1 wording.

## Gaps/order issues found and fixed before build

- Added the full Sokolow–Lyon lead alternatives (R in V5 **or V6**, S in V1 **or V2**), not just a single numerical example.
- Added all four numbered pacemaker-potential curve markers and checked the small-print voltage/time labels from a magnified render.
- Separated the first two terminology-table rows so meaning and regulator stay together in printed row order.
- Kept the LBBB-alone classification before the trifascicular line.
- Put intrinsic sick sinus syndrome after the complete extrinsic-cause column.
- Put the AIVR reperfusion sub-bullet before the VT rate bullet, then separately covered the AIVR figure caption.
- Rebuilt all IDs sequentially and each unit’s `qs` from its `sec` in question-array order after these changes.

**Final unasked educational points found: none in the reviewed p383–393 inventory.**

## Source discrepancies handled explicitly

| Page | Source-specific wording retained and qualified |
|---:|---|
| 383 | aVL is printed as 30° without a minus; explanation distinguishes conventional −30°. |
| 385 / 388 | “Trifascicular” = bifascicular + increased PR is identified as source terminology, not anatomical proof of third-fascicle disease. |
| 385–386 | Proportional STE/S >25% is separated from absolute >5 mm; prose uses > while p386 panels use ≥. |
| 387 | Printed HFrEF <50% / HFpEF >50% leaves exactly 50% unspecified; older “no drugs” diastolic-treatment row is not contemporary clinical advice. |
| 387–388 | TOK closure / IRK opening retained as printed; HCN “Na channels” identified as shorthand for a mixed-cation current. |
| 389 | “Up to 40” IVR and “40–100” AIVR overlap at 40; no question relies on that ambiguous boundary. |
| 390 | Printed PR >100 ms is explicitly contrasted with the usual first-degree definition >200 ms. Cannon waves are contextualised by unusually prolonged PR. |
| 391 | “Sx” is retained without speculative expansion. Typical QRS widths and the observation/pacing branches are labelled source statements; the latter is not a universal guideline for Mobitz II/high-grade block. |

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

## Format distribution

| Chapter | Recall | Fill-up | Match | True/false | Scenario | Odd-one-out | Numeric | Management | Total |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 9 | 17 | 6 | 3 | 5 | 4 | 0 | 49 |
| 2 | 4 | 10 | 5 | 3 | 8 | 2 | 5 | 0 | 37 |
| 3 | 6 | 10 | 5 | 2 | 7 | 3 | 4 | 1 | 38 |
| 4 | 4 | 9 | 1 | 3 | 10 | 1 | 5 | 2 | 35 |

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

**Total: 262 mapped points; 110 new questions; 13 new units.** With the Ch1 rescue: 159 questions, 20 units, four live chapters of 57.

## Pre-build checks

- `python3 validate_content.py --ledger` — PASS, full ledger printed before build.
- Actual `parseMatch`, `fillupHtml`, `matchOptHtml`, `splitExp` extracted from the app and executed by Node — PASS on all 159 questions, including correct-answer bijections and every option’s left-item coverage.
- Five JavaScript rejection controls — PASS.
- `python3 -m unittest discover -s tests -v` — 9 tests PASS, including corruption of schemas, blanks, True/False balance, page order, guides, unit coverage and ledger references.
- `build_content.py` now invokes the validation gate before it can write the HTML. Python 3 and Node are required to build; the delivered HTML has no runtime dependency on either.

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


## Post-build verification (still before publication)

- `python3 build_content.py` embedded 159 questions / 20 units / 4 live chapters.
- `python3 validate_content.py --embedded` passed exact source/HTML equality and all 57 roadmap flags.
- A second build preserved the HTML SHA-256 exactly.
- Real Chromium, network disabled, `file://` HTML: all 159 questions and 20 units passed at both 1280×900 and 390×844. Tested every format renderer, answer/citation feedback, fixed question order, sequential unlock, completion persistence after reload and the wrong-answer path; no JavaScript page errors.
- The sandbox browser used the npm-distributed Chromium binary because the Playwright browser-download host was unreachable. Browser binaries and render artifacts are excluded from Git.
