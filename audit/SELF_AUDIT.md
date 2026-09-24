# Chapters 2–38 — visual self-audit gate

Reviewed 2026-09-24, before live deployment. Source: `uploads/01.pdf` PDF94–103 (Book p458–467), `uploads/02.pdf` PDF1–93 (Book p468–561; printed p527 is absent) and `uploads/03.pdf` PDF1–37 (Book p562–601; printed p586, p590 and p591 are absent), all read from 2× PyMuPDF renders. Chapters 30–31 were authored from `uploads/02.pdf` PDF87–93 (Book p555–561) plus `uploads/03.pdf` PDF1 (Book p562). See [every-page map](PAGE_MAP.md) and machine-readable [inventory](coverage.json).

## Method and scope

- Read every educational heading, bullet, sub-bullet, note, table cell, flowchart arm, diagram label, threshold, score, criteria and dose on printed p383–601 (the live chapters), top-to-bottom. Parallel comparison columns were treated as unified comparison blocks; diagrams remained with their adjacent text; publisher footers, lesson timestamps and 'Active space' furniture are excluded. Scans contain no extractable text, so every reading used 2× PyMuPDF renders (never `page.get_text()`); printed page numbers were verified against [PAGE_MAP.md](PAGE_MAP.md).
- Upside-down (rotated 180°) printed annotations on p461, p465, p474, p481, p483, p484, p485 and p487 were rotated and read; where a rotated value could not be resolved with confidence it is recorded in the discrepancy table below and no question relies on it.
- Every inventoried point has an explicit question target. Strict quality control: zero predictable/trivial distractors, medically plausible answer choices, reasoning-first scenario/recall options in Chapters 9–31 and 33–38 (no fill-up or match worksheets), and exact citation references.
- Questions in Chapters 9–31 and 33–38 use only recall, scenario, numeric, oddoneout and management formats, with four unique plausible options and exact page citations.
- Software gates verify schema, exact app parsers, sequential IDs, page ordering, inventory ordering, unit contiguity, ledger coverage and embedded data agreement. Semantic completeness is verified via visual self-audit.

## Source-specific notes retained as book-study material

| Pages | Note |
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
| 458–465 | Cutaneous-lupus terminology, the discoid 5/20 rule, lupus-nephritis class thresholds, the EULAR/ACR domain weights and every steroid/immunosuppressant dose are reproduced as printed book-study material, not as prescribing guidance. |
| 459 | The discoid '5/20 rule' percentages were enlarged and re-read before use (5% of discoid patients have SLE; 20% of SLE patients have discoid rash). |
| 461 | The rotated 'autoimmune hemolytic anaemia' annotation and the DAH-versus-viral/TB branch are read as source statements; distinguishing infection from DAH requires clinical correlation. |
| 462 | The prognosis cell shared by class III and class IV lupus nephritis prints 'and worst'; no question asks for a single class-specific value from that merged cell. |
| 464 | Methylprednisolone 500 mg–1 g in 100 ml normal saline over 1–2 hours, pulse × 3 days, then oral steroid 1 mg/kg/day tapered over 3 months to 5 mg/day is the source's regimen and is not a universal induction protocol. |
| 465 | The rotated 'switch to cyclophosphamide' arm and the CHImP drug mnemonic are transcribed as printed; drug-induced lupus lists historical culprits and the note that such drugs are safe in SLE patients is a source statement. |
| 466 | '50% primary / ≥50% secondary' APS split and the reduced-inhibition-of-coagulation-factors step are retained as printed pathophysiology. |
| 467 | Anticardiolipin >40 units, the 12-week persistence rule and dRVVT are Sapporo-era statements; current laboratory classification criteria differ. |
| 469 | INR 2.5–3 with heparin 5000 units TDS or LMWH 60 mg BD, and 'no role for NOACs', are printed management statements that do not replace current guidance. |
| 470 | The 'groove sign: aplastic anaemia' annotation is printed beside the scleroderma mimics and is transcribed as a source note. |
| 472 | The primary/secondary Raynaud columns (including the centromere annotation on the ANA row) are read as printed; the demographic cell 'middle aged female' is not attributed to either column by any question. |
| 474–475 | The antibody-to-complication map (anti-centromere/PAH, anti-RNA polymerase III/renal crisis) and the ACE-inhibitor drug of choice are source teaching, and the printed percentage for renal crisis in diffuse SSc is not legible enough to transcribe — no question relies on that numeral. |
| 476 | Nintedanib plus MMF for SSc-ILD and bosentan as second line for Raynaud phenomenon are transcribed as printed indications. |
| 479 | The Gottron-papule frequency is printed as a small fraction glyph that cannot be read with confidence; the question on this lesion tests its morphology and site, not the frequency. |
| 481 | The rotated 'Jaccoud's arthropathy: also seen in Sjogren syndrome' annotation is transcribed as printed. |
| 483 | The rotated dysphagia-frequency annotation beside inclusion body myositis was not legible; no question relies on it. Steroid-unresponsive disease and red-rimmed vacuoles are the tested points. |
| 484 | The '50/25/5' outcome split and the testicular sparing statement are printed source epidemiology. |
| 485 | The rotated 'HLA DRB1*03 — Lofgren syndrome (good prognosis)' annotation is read after rotation and transcribed as printed. |
| 487 | The rotated annotation linking lupus pernio to lytic or cystic bone change is transcribed as a source note. |
| 488 | The BAL CD4/CD8 cut-off numeral is too small to read with confidence; the question asks only for the raised ratio. The panda sign and the PET 'node to biopsy' role are transcribed as printed. |
| 489 | The therapeutic paradox (TNF-alpha blockade producing sarcoid-like skin lesions that resolve on dose reduction) is a source observation. |
| 490 | 'About 20% evolve into limited SSc' and pulmonary artery hypertension as the most common cause of death are printed MCTD statements. |

| 491–498 | Vasculitis classification, GCA/PMR, Takayasu criteria, imaging and steroid/tocilizumab/stenting treatment statements are reproduced as source-specific teaching points. |
| 499–508 | ANCA testing, GPA/MPA/EGPA/PAN scoring, doses, plasma-exchange indications and HBV-based PAN treatment are retained exactly as printed for study. |
| 509–513 | HSP versus cryoglobulinemia criteria, triads, complement/cryocrit findings and treatment branches are source-specific. |
| 514–518 | Behcet and Cogan diagnostic/treatment criteria, pathergy values and systemic warning signs are retained as printed. |
| 519–520 | Arthritis approach thresholds, inflammatory synovial-fluid cut-off and erosion table are study points, not a substitute for clinical assessment. |
| 521–531 | RA risk factors, antibodies, extra-articular manifestations, deformities and DMARD/biologic/JAK treatment algorithms are reproduced as book-study material. |
| 532–554 | Chapters 27–29 book-study notes: non-radiographic axial SpA 5%→radiographic in 5–10 y; Schober A–B 15 cm with normal ≥20; indomethacin 50 TID 2–3 wks; Reiter's triad; Chlamydia GU 9:1 vs Shigella India 1:1; keratoderma d/d palmo-plantar psoriasis; LMAP self-limiting vs SMAP-u→anti-TNF; 60/30/30 with 90% nail change; CASPER; pencil-in-cup; inflammasome→IL-1β; humans lack uricase; stone thresholds uric>7 / Ca>4 m/c / citrate<11; 4-compartment 100/50/40/10; >6F/>7M with 90% underexcretion; CANT LEAP; Kelley 6.8; first-MTP 85% with UA normal 40%; MSUM needles strong negative parallel; colchicine 1.2→0.6 schedule; ACR triad; 60% flare/yr; allopurinol 300 HLA-B5801; febuxostat cardiotoxic; oxalate envelope; AOSD 25–45 quotidian salmon poly knee>wrist; Yamaguchi >5; HLH 10% ESR↓ fibrinogen↓ TG↑ ferritin↑↑; NSAID→steroid+MTX→anti-IL1/6 with sulfasalazine avoided; gonococcal vs septic table; synovial WBC >50 000 gold standard; vanco+ceftriaxone; drainage thick pus/shoulder/hip — retained exactly as printed book-study material. |

| 555 | The MMSE is presented as a higher-mental-function screen 'based on' the printed ORAR LC list; the mnemonic is not expanded beyond those six bullets and no scoring cut-off (for example 24/30) is printed on this sheet. |
| 556 | Area 8 is printed twice, for the supplementary motor area (medially) and for the frontal eye field; areas 9–12 prefrontal, 44/45 Broca and the H-shaped orbital sulcus are transcribed as drawn. |
| 557 | Both the primary motor area and the premotor/supplementary block print 30% of motor fibres, while p560 prints the 40/30/30 split including primary sensory cortex; the percentages are reproduced as printed rather than reconciled. |
| 558 | The motor-cortex lesion line prints 'Fare & upper Limb' (read as Face) and 'Initiate lesion' (the irritative-lesion arm); the flowchart boxes 'Right PTO', 'DLPN', 'NPH VN' and 'Internal sagittal stratum' are printed without expansions, so no question asks what those abbreviations stand for. |
| 558 | The gaze rules ('frontal lobe lesion — look towards the side of the lesion', 'brain stem lesion (PPRF) — look away') are reproduced as printed bedside rules and are not extended to other causes of deviation. |
| 559 | JIPFA (Judgement, Insight, Problem solving/personality, Fluency, Abstract thinking) and the apathy → abulia → akinetic mutism ladder are printed mnemonics/gradings of this source, not validated clinical scales; the NPH gait line prints 'Ignition failure : Foot feels like stuck to floor'. |
| 560 | 'Origin of motor fibres' 40% sensory / 30% motor / 30% premotor-SMA is the source's own accounting; the parietal figure annotates the superior parietal lobule as Praxicons, the supramarginal gyrus as Gnosis and the angular gyrus as Gerstmann syndrome. |
| 561 | The visual-agnosia panel prints the four object captions snake, stereo or computer, bug and lamp as misreadings; the handedness table (right-handed 5% right / 90–95% left; left-handed 40% / 50–60%) is transcribed as printed. |
| 562 | 'Gerstman syndrome' (printed without the second 'n'), 'Left hemispatal neglect' (as printed), the ROCF A1/A2/A3 copies and the pie-in-floor/pie-in-sky table are reproduced exactly as drawn; macular sparing in the PCA branch is a source statement. |
| 566 | Broca (44,45) grammar/syntax/rhythm/fluency vs Wernicke (22) sound/comprehension, non-dominant prosody and 'pure word deafness' labelled on the connecting fibres are transcribed as printed. |
| 567 | The DESP non-fluent list and the four-arm comprehension/repetition flowchart (watershed infarct for transcortical motor) are reproduced as printed. |
| 568 | Four dysarthria types by anatomical level and the 'lesion of parietal lobe: inferior quadrantanopia' note (vs superior quadrantanopia in the Wernicke's arm) are source statements. |
| 572 | The definition is printed as 'major cognitive impairment + ≥1 out of 6 cognitive domains affected' (standard NIAAA criteria use two domains); the six-domain→area table is transcribed as printed. |
| 573 | The reversible-cause letter list, the B12 triad note and 'Rx of NPH: surgery' are source statements; '>85 years: 40% chance of Alzheimer's' is printed as such. |
| 574–575 | The APP pathway (β-secretase), Aβ40/42 divergence, brain-diabetes IDE step, chromosomes 14/1/19 and the printed 'Not risk factors: low IQ, smoking, NSAIDs' are transcribed as printed. |
| 577–578 | FTD 70% sporadic vs Alzheimer's 90–95% sporadic note; the DLB-vs-PD table including 'antipsychotics worsen (D2 receptor inhibition)' and the rocket-sign definition are source statements. |
| 580 | Flupirtine maleate listed as CJD treatment (centrally acting non-opioid analgesic) is a source statement, not contemporary care. |
| 583–585 | Basal-ganglia tree, nuclei diagram with lesion syndromes and the PD-vs-essential tremor table are reproduced as printed. |
| 587 | 'Froment's sign: activity-induced increase in c/l rigidity' is transcribed exactly as printed (the classical pencil-pinch test is not described on this page); the swallow-tail sign is attributed to the substantia nigra. |
| 586 / 590 / 591 | Missing from supplied scan — each carries one transparently-flagged bracketing question (MED-C37-13, MED-C37-33, MED-C37-34); content verification of these pages remains unresolved, as with p527. |
| 589–592 | 'COMT inhibitors not used now', trihexyphenidyl for drug-induced PD, amantadine's three mechanisms and the <60-year / >60-year protocol split are source statements. |
| 593–594 | GCA red flags, the herniation line (uncus m/c, 3rd nerve palsy) and the TTH-vs-migraine feature lists are reproduced as printed. |
| 595–596 | Common 80% / classical 20%, aura 15 min–1 hr, 4–72 hr duration, the triptan dose maxima (rizatriptan 30 mg, sumatriptan 200 mg) and the ergotamine note are book-study values. |
| 597–598 | TAC attack data (15 min–3 h, 2–30 min, 5–240 s) and cluster oxygen 12–15 L/min for 10–20 min are source values as printed. |
| 599 | HLA B-1502 before carbamazepine and HLA B-5801 before allopurinol are source statements; TN/MVD treatment ladder transcribed as printed. |
| 600–601 | Modified Dandy criteria (LP >25 cm H2O), acetazolamide DOC, repeated LP 20–30 ml 'best option' and the acute-ICP five steps (CPP >60 mmHg) are source statements. |

Source-map discrepancy found during merge: uploads/02.pdf PDF59 is printed p526, PDF60 is p528, PDF63 is p531, and PDF64 begins p532. Printed p527 is absent. The five existing upstream Chapter 26 questions citing p527 are preserved, but their source verification remains unresolved; software coverage does not establish visual completeness for that missing page.

Second source-map discrepancy (Chapters 33-38): uploads/03.pdf PDF25 is printed p587 and PDF28 is printed p592 (decisive 10× corner reads), and 28 printed pages (p566-p593) span only 25 sheets — printed p586, p590 and p591 are absent from the supplied scan. Three transparently-flagged bracketing questions (MED-C37-13 citing p586, MED-C37-33 citing p590, MED-C37-34 citing p591) keep the ledger's page set complete; their source verification remains unresolved, following the p527 precedent.

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
| 30 | 2. Areas on the frontal lobe: lateral map, medial surface and orbital surface | 556 | MED-C30-10–MED-C30-19 | 10 |
| 30 | 3. Area 4, premotor/SMA roles, the movement ladder and the motor homunculus | 557 | MED-C30-20–MED-C30-31 | 12 |
| 30 | 4. Vascular and motor-cortex lesions, the frontal eye field and Broca's area | 558 | MED-C30-32–MED-C30-48 | 17 |
| 30 | 5. Prefrontal cortex map, JIPFA behaviour and bilateral frontal pathology | 559 | MED-C30-49–MED-C30-64 | 16 |
| 31 | 1. Parietal lobe map, the 40/30/30 motor-fibre origins and the postcentral gyrus | 560 | MED-C31-01–MED-C31-12 | 12 |
| 31 | 2. Superior parietal praxicons, apraxia types and the inferior parietal lobule | 561 | MED-C31-13–MED-C31-26 | 14 |
| 31 | 3. Hemispatial neglect, the angular gyrus and alexia without agraphia | 562 | MED-C31-27–MED-C31-43 | 17 |
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

## Format distribution

| Chapter | Recall | Scenario | Numeric | Odd-one-out | Management | Other | Total | Ledger points |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 3 | 4 | 5 | 0 | 32 | 49 | 0 |
| 2 | 4 | 8 | 5 | 2 | 0 | 18 | 37 | 86 |
| 3 | 6 | 7 | 4 | 3 | 1 | 17 | 38 | 93 |
| 4 | 4 | 10 | 5 | 1 | 2 | 13 | 35 | 83 |
| 5 | 9 | 11 | 8 | 4 | 5 | 15 | 52 | 57 |
| 6 | 6 | 6 | 6 | 1 | 4 | 10 | 33 | 33 |
| 7 | 5 | 5 | 6 | 4 | 4 | 12 | 36 | 36 |
| 8 | 3 | 2 | 0 | 1 | 2 | 6 | 14 | 14 |
| 9 | 32 | 24 | 4 | 3 | 1 | 0 | 64 | 64 |
| 10 | 17 | 12 | 0 | 0 | 0 | 0 | 29 | 29 |
| 11 | 33 | 24 | 11 | 1 | 3 | 0 | 72 | 72 |
| 12 | 26 | 13 | 5 | 1 | 2 | 0 | 47 | 47 |
| 13 | 16 | 5 | 0 | 1 | 1 | 0 | 23 | 23 |
| 14 | 15 | 1 | 1 | 1 | 0 | 0 | 18 | 18 |
| 15 | 23 | 6 | 3 | 0 | 0 | 0 | 32 | 32 |
| 16 | 34 | 16 | 14 | 2 | 8 | 0 | 74 | 74 |
| 17 | 12 | 12 | 8 | 0 | 3 | 0 | 35 | 35 |
| 18 | 27 | 19 | 1 | 0 | 3 | 0 | 50 | 50 |
| 19 | 34 | 18 | 2 | 0 | 3 | 0 | 57 | 57 |
| 20 | 28 | 16 | 4 | 1 | 3 | 0 | 52 | 52 |
| 21 | 26 | 7 | 6 | 2 | 3 | 0 | 44 | 44 |
| 22 | 38 | 2 | 5 | 2 | 5 | 0 | 52 | 52 |
| 23 | 18 | 3 | 2 | 0 | 3 | 0 | 26 | 26 |
| 24 | 27 | 0 | 4 | 2 | 3 | 0 | 36 | 36 |
| 25 | 6 | 3 | 2 | 0 | 0 | 0 | 11 | 11 |
| 26 | 58 | 9 | 8 | 0 | 5 | 0 | 80 | 80 |
| 27 | 58 | 11 | 20 | 5 | 7 | 0 | 101 | 101 |
| 28 | 40 | 3 | 20 | 4 | 5 | 0 | 72 | 72 |
| 29 | 15 | 0 | 5 | 5 | 3 | 0 | 28 | 28 |
| 30 | 38 | 13 | 3 | 8 | 2 | 0 | 64 | 64 |
| 31 | 24 | 7 | 4 | 7 | 1 | 0 | 43 | 43 |
| 33 | 7 | 8 | 0 | 1 | 0 | 0 | 16 | 16 |
| 34 | 6 | 5 | 0 | 1 | 0 | 0 | 12 | 12 |
| 35 | 10 | 9 | 4 | 2 | 2 | 0 | 27 | 27 |
| 36 | 11 | 5 | 4 | 4 | 1 | 0 | 25 | 25 |
| 37 | 15 | 12 | 5 | 3 | 2 | 0 | 37 | 37 |
| 38 | 17 | 14 | 9 | 3 | 8 | 0 | 51 | 51 |

## Chapters 16–26 release table

| Ch | Title | Printed pages | Questions | Units | Ledger mappings |
|---:|---|---:|---:|---:|---:|
| 16 | SLE - Clinical Profile and Management | 458–465 | 74 | 7 | 74 |
| 17 | Antiphospholipid Syndrome | 466–469 | 35 | 4 | 35 |
| 18 | Systemic Sclerosis | 470–476 | 50 | 7 | 50 |
| 19 | Inflammatory Muscle Diseases | 477–483 | 57 | 7 | 57 |
| 20 | Sarcoidosis and Mixed Connective Tissue Disease | 484–490 | 52 | 7 | 52 |
| 21 | Classification of Vasculitis and Large Vessel Vasculitis | 491–498 | 44 | 3 | 44 |
| 22 | Small Vessel Vasculitis | 499–508 | 52 | 3 | 52 |
| 23 | Henoch-Schonlein Purpura V/S Cryoglobulinemia | 509–513 | 26 | 2 | 26 |
| 24 | Variable Vessel Vasculitis | 514–518 | 36 | 2 | 36 |
| 25 | Basic Approach to Arthritis | 519–520 | 11 | 1 | 11 |
| 26 | Rheumatoid Arthritis | 521–531 | 80 | 4 | 80 |

## Chapters 27–29 release table

| Ch | Title | Printed pages | Questions | Units | Ledger mappings |
|---:|---|---:|---:|---:|---:|
| 27 | Spondyloarthritis | 532–542 | 101 | 10 | 101 |
| 28 | Crystal Arthropathies | 543–551 | 72 | 8 | 72 |
| 29 | Adult-Onset Still's Disease and Septic Arthritis | 552–554 | 28 | 3 | 28 |

## Chapters 30–31 release table

| Ch | Title | Printed pages | Questions | Units | Ledger mappings |
|---:|---|---:|---:|---:|---:|
| 30 | Frontal Lobe | 555–559 | 64 | 5 | 64 |
| 31 | Praxicons | 560–562 | 43 | 3 | 43 |

## Chapters 33–38 release table

| Ch | Title | Printed pages | Questions | Units | Ledger mappings |
|---:|---|---:|---:|---:|---:|
| 33 | Language V/S Speech | 566–568 | 16 | 4 | 16 |
| 34 | Memory | 569–571 | 12 | 3 | 12 |
| 35 | Dementia : Part 1 | 572–576 | 27 | 5 | 27 |
| 36 | Dementia : Part 2 | 577–582 | 25 | 3 | 25 |
| 37 | Parkinson's Disease | 583–592 | 37 | 5 | 37 |
| 38 | Headache | 593–601 | 51 | 6 | 51 |

## Page-by-page coverage summary

| Book page | PDF sheet | Inventoried points | Questions | Unasked |
|---:|---:|---:|---:|---:|
| 383 | 01 PDF19 | 18 | 10 | 0 |
| 384 | 01 PDF20 | 24 | 11 | 0 |
| 385 | 01 PDF21 | 35 | 12 | 0 |
| 386 | 01 PDF22 | 9 | 4 | 0 |
| 387 | 01 PDF23 | 30 | 12 | 0 |
| 388 | 01 PDF24 | 35 | 11 | 0 |
| 389 | 01 PDF25 | 28 | 15 | 0 |
| 390 | 01 PDF26 | 26 | 8 | 0 |
| 391 | 01 PDF27 | 27 | 12 | 0 |
| 392 | 01 PDF28 | 16 | 6 | 0 |
| 393 | 01 PDF29 | 14 | 9 | 0 |
| 394 | 01 PDF30 | 10 | 7 | 0 |
| 395 | 01 PDF31 | 9 | 7 | 0 |
| 396 | 01 PDF32 | 6 | 6 | 0 |
| 397 | 01 PDF33 | 4 | 4 | 0 |
| 398 | 01 PDF34 | 4 | 4 | 0 |
| 399 | 01 PDF35 | 6 | 6 | 0 |
| 400 | 01 PDF36 | 9 | 9 | 0 |
| 401 | 01 PDF37 | 5 | 5 | 0 |
| 402 | 01 PDF38 | 4 | 4 | 0 |
| 403 | 01 PDF39 | 11 | 11 | 0 |
| 404 | 01 PDF40 | 8 | 8 | 0 |
| 405 | 01 PDF41 | 9 | 9 | 0 |
| 406 | 01 PDF42 | 5 | 5 | 0 |
| 407 | 01 PDF43 | 9 | 9 | 0 |
| 408 | 01 PDF44 | 6 | 6 | 0 |
| 409 | 01 PDF45 | 4 | 4 | 0 |
| 410 | 01 PDF46 | 8 | 8 | 0 |
| 411 | 01 PDF47 | 6 | 6 | 0 |
| 412 | 01 PDF48 | 3 | 3 | 0 |
| 413 | 01 PDF49 | 6 | 6 | 0 |
| 414 | 01 PDF50 | 8 | 8 | 0 |
| 415 | 01 PDF51 | 7 | 7 | 0 |
| 416 | 01 PDF52 | 10 | 10 | 0 |
| 417 | 01 PDF53 | 7 | 7 | 0 |
| 418 | 01 PDF54 | 5 | 5 | 0 |
| 419 | 01 PDF55 | 9 | 9 | 0 |
| 420 | 01 PDF56 | 6 | 6 | 0 |
| 421 | 01 PDF57 | 6 | 6 | 0 |
| 422 | 01 PDF58 | 5 | 5 | 0 |
| 423 | 01 PDF59 | 4 | 4 | 0 |
| 424 | 01 PDF60 | 5 | 5 | 0 |
| 425 | 01 PDF61 | 5 | 5 | 0 |
| 426 | 01 PDF62 | 8 | 8 | 0 |
| 427 | 01 PDF63 | 7 | 7 | 0 |
| 428 | 01 PDF64 | 6 | 6 | 0 |
| 429 | 01 PDF65 | 3 | 3 | 0 |
| 430 | 01 PDF66 | 5 | 5 | 0 |
| 431 | 01 PDF67 | 6 | 6 | 0 |
| 432 | 01 PDF68 | 6 | 6 | 0 |
| 433 | 01 PDF69 | 4 | 4 | 0 |
| 434 | 01 PDF70 | 5 | 5 | 0 |
| 435 | 01 PDF71 | 5 | 5 | 0 |
| 436 | 01 PDF72 | 7 | 7 | 0 |
| 437 | 01 PDF73 | 8 | 8 | 0 |
| 438 | 01 PDF74 | 7 | 7 | 0 |
| 439 | 01 PDF75 | 6 | 6 | 0 |
| 440 | 01 PDF76 | 7 | 7 | 0 |
| 441 | 01 PDF77 | 6 | 6 | 0 |
| 442 | 01 PDF78 | 5 | 5 | 0 |
| 443 | 01 PDF79 | 6 | 6 | 0 |
| 444 | 01 PDF80 | 8 | 8 | 0 |
| 445 | 01 PDF81 | 7 | 7 | 0 |
| 446 | 01 PDF82 | 8 | 8 | 0 |
| 447 | 01 PDF83 | 7 | 7 | 0 |
| 448 | 01 PDF84 | 6 | 6 | 0 |
| 449 | 01 PDF85 | 8 | 8 | 0 |
| 450 | 01 PDF86 | 6 | 6 | 0 |
| 451 | 01 PDF87 | 9 | 9 | 0 |
| 452 | 01 PDF88 | 5 | 5 | 0 |
| 453 | 01 PDF89 | 6 | 6 | 0 |
| 454 | 01 PDF90 | 7 | 7 | 0 |
| 455 | 01 PDF91 | 11 | 11 | 0 |
| 456 | 01 PDF92 | 7 | 7 | 0 |
| 457 | 01 PDF93 | 14 | 14 | 0 |
| 458 | 01 PDF94 | 7 | 7 | 0 |
| 459 | 01 PDF95 | 7 | 7 | 0 |
| 460 | 01 PDF96 | 10 | 10 | 0 |
| 461 | 01 PDF97 | 12 | 12 | 0 |
| 462 | 01 PDF98 | 8 | 8 | 0 |
| 463 | 01 PDF99 | 11 | 11 | 0 |
| 464 | 01 PDF100 | 9 | 9 | 0 |
| 465 | 01 PDF101 | 10 | 10 | 0 |
| 466 | 01 PDF102 | 9 | 9 | 0 |
| 467 | 01 PDF103 | 12 | 12 | 0 |
| 468 | 02 PDF1 | 7 | 7 | 0 |
| 469 | 02 PDF2 | 7 | 7 | 0 |
| 470 | 02 PDF3 | 8 | 8 | 0 |
| 471 | 02 PDF4 | 8 | 8 | 0 |
| 472 | 02 PDF5 | 6 | 6 | 0 |
| 473 | 02 PDF6 | 7 | 7 | 0 |
| 474 | 02 PDF7 | 9 | 9 | 0 |
| 475 | 02 PDF8 | 5 | 5 | 0 |
| 476 | 02 PDF9 | 7 | 7 | 0 |
| 477 | 02 PDF10 | 10 | 10 | 0 |
| 478 | 02 PDF11 | 7 | 7 | 0 |
| 479 | 02 PDF12 | 7 | 7 | 0 |
| 480 | 02 PDF13 | 8 | 8 | 0 |
| 481 | 02 PDF14 | 9 | 9 | 0 |
| 482 | 02 PDF15 | 6 | 6 | 0 |
| 483 | 02 PDF16 | 10 | 10 | 0 |
| 484 | 02 PDF17 | 8 | 8 | 0 |
| 485 | 02 PDF18 | 8 | 8 | 0 |
| 486 | 02 PDF19 | 7 | 7 | 0 |
| 487 | 02 PDF20 | 5 | 5 | 0 |
| 488 | 02 PDF21 | 9 | 9 | 0 |
| 489 | 02 PDF22 | 9 | 9 | 0 |
| 490 | 02 PDF23 | 6 | 6 | 0 |
| 491 | 02 PDF24 | 7 | 7 | 0 |
| 492 | 02 PDF25 | 7 | 7 | 0 |
| 493 | 02 PDF26 | 6 | 6 | 0 |
| 494 | 02 PDF27 | 6 | 6 | 0 |
| 495 | 02 PDF28 | 6 | 6 | 0 |
| 496 | 02 PDF29 | 6 | 6 | 0 |
| 497 | 02 PDF30 | 3 | 3 | 0 |
| 498 | 02 PDF31 | 3 | 3 | 0 |
| 499 | 02 PDF32 | 4 | 4 | 0 |
| 500 | 02 PDF33 | 6 | 6 | 0 |
| 501 | 02 PDF34 | 7 | 7 | 0 |
| 502 | 02 PDF35 | 4 | 4 | 0 |
| 503 | 02 PDF36 | 4 | 4 | 0 |
| 504 | 02 PDF37 | 5 | 5 | 0 |
| 505 | 02 PDF38 | 7 | 7 | 0 |
| 506 | 02 PDF39 | 6 | 6 | 0 |
| 507 | 02 PDF40 | 6 | 6 | 0 |
| 508 | 02 PDF41 | 3 | 3 | 0 |
| 509 | 02 PDF42 | 5 | 5 | 0 |
| 510 | 02 PDF43 | 4 | 4 | 0 |
| 511 | 02 PDF44 | 5 | 5 | 0 |
| 512 | 02 PDF45 | 6 | 6 | 0 |
| 513 | 02 PDF46 | 6 | 6 | 0 |
| 514 | 02 PDF47 | 6 | 6 | 0 |
| 515 | 02 PDF48 | 8 | 8 | 0 |
| 516 | 02 PDF49 | 6 | 6 | 0 |
| 517 | 02 PDF50 | 7 | 7 | 0 |
| 518 | 02 PDF51 | 9 | 9 | 0 |
| 519 | 02 PDF52 | 6 | 6 | 0 |
| 520 | 02 PDF53 | 5 | 5 | 0 |
| 521 | 02 PDF54 | 8 | 8 | 0 |
| 522 | 02 PDF55 | 6 | 6 | 0 |
| 523 | 02 PDF56 | 8 | 8 | 0 |
| 524 | 02 PDF57 | 7 | 7 | 0 |
| 525 | 02 PDF58 | 8 | 8 | 0 |
| 526 | 02 PDF59 | 6 | 6 | 0 |
| 527 | Missing from supplied scan | 5 | 5 | 0 |
| 528 | 02 PDF60 | 9 | 9 | 0 |
| 529 | 02 PDF61 | 4 | 4 | 0 |
| 530 | 02 PDF62 | 8 | 8 | 0 |
| 531 | 02 PDF63 | 11 | 11 | 0 |
| 532 | 02 PDF64 | 9 | 9 | 0 |
| 533 | 02 PDF65 | 15 | 15 | 0 |
| 534 | 02 PDF66 | 10 | 10 | 0 |
| 535 | 02 PDF67 | 7 | 7 | 0 |
| 536 | 02 PDF68 | 11 | 11 | 0 |
| 537 | 02 PDF69 | 8 | 8 | 0 |
| 538 | 02 PDF70 | 9 | 9 | 0 |
| 539 | 02 PDF71 | 11 | 11 | 0 |
| 540 | 02 PDF72 | 8 | 8 | 0 |
| 541 | 02 PDF73 | 7 | 7 | 0 |
| 542 | 02 PDF74 | 6 | 6 | 0 |
| 543 | 02 PDF75 | 9 | 9 | 0 |
| 544 | 02 PDF76 | 9 | 9 | 0 |
| 545 | 02 PDF77 | 9 | 9 | 0 |
| 546 | 02 PDF78 | 11 | 11 | 0 |
| 547 | 02 PDF79 | 7 | 7 | 0 |
| 548 | 02 PDF80 | 7 | 7 | 0 |
| 549 | 02 PDF81 | 7 | 7 | 0 |
| 550 | 02 PDF82 | 8 | 8 | 0 |
| 551 | 02 PDF83 | 5 | 5 | 0 |
| 552 | 02 PDF84 | 9 | 9 | 0 |
| 553 | 02 PDF85 | 11 | 11 | 0 |
| 554 | 02 PDF86 | 8 | 8 | 0 |
| 555 | 02 PDF87 | 9 | 9 | 0 |
| 556 | 02 PDF88 | 10 | 10 | 0 |
| 557 | 02 PDF89 | 12 | 12 | 0 |
| 558 | 02 PDF90 | 17 | 17 | 0 |
| 559 | 02 PDF91 | 16 | 16 | 0 |
| 560 | 02 PDF92 | 12 | 12 | 0 |
| 561 | 02 PDF93 | 14 | 14 | 0 |
| 562 | 03 PDF1 | 17 | 17 | 0 |
| 566 | 03 PDF5 | 6 | 6 | 0 |
| 567 | 03 PDF6 | 5 | 5 | 0 |
| 568 | 03 PDF7 | 5 | 5 | 0 |
| 569 | 03 PDF8 | 6 | 6 | 0 |
| 570 | 03 PDF9 | 4 | 4 | 0 |
| 571 | 03 PDF10 | 2 | 2 | 0 |
| 572 | 03 PDF11 | 6 | 6 | 0 |
| 573 | 03 PDF12 | 7 | 7 | 0 |
| 574 | 03 PDF13 | 6 | 6 | 0 |
| 575 | 03 PDF14 | 4 | 4 | 0 |
| 576 | 03 PDF15 | 4 | 4 | 0 |
| 577 | 03 PDF16 | 5 | 5 | 0 |
| 578 | 03 PDF17 | 5 | 5 | 0 |
| 579 | 03 PDF18 | 4 | 4 | 0 |
| 580 | 03 PDF19 | 4 | 4 | 0 |
| 581 | 03 PDF20 | 4 | 4 | 0 |
| 582 | 03 PDF21 | 3 | 3 | 0 |
| 583 | 03 PDF22 | 4 | 4 | 0 |
| 584 | 03 PDF23 | 4 | 4 | 0 |
| 585 | 03 PDF24 | 4 | 4 | 0 |
| 586 | Missing from supplied scan | 1 | 1 | 0 |
| 587 | 03 PDF27 | 7 | 7 | 0 |
| 588 | 03 PDF28 | 6 | 6 | 0 |
| 589 | 03 PDF29 | 6 | 6 | 0 |
| 590 | Missing from supplied scan | 1 | 1 | 0 |
| 591 | Missing from supplied scan | 1 | 1 | 0 |
| 592 | 03 PDF28 | 3 | 3 | 0 |
| 593 | 03 PDF29 | 5 | 5 | 0 |
| 594 | 03 PDF30 | 7 | 7 | 0 |
| 595 | 03 PDF31 | 8 | 8 | 0 |
| 596 | 03 PDF32 | 8 | 8 | 0 |
| 597 | 03 PDF33 | 4 | 4 | 0 |
| 598 | 03 PDF34 | 6 | 6 | 0 |
| 599 | 03 PDF35 | 5 | 5 | 0 |
| 600 | 03 PDF36 | 5 | 5 | 0 |
| 601 | 03 PDF37 | 3 | 3 | 0 |

**Total: 1680 mapped educational points; 1572 questions; 157 units across 37 live chapters of 57.**

## Full printed-point → question ledger

### Book p383 / 01 PDF19

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

### Book p384 / 01 PDF20

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

### Book p385 / 01 PDF21

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

### Book p386 / 01 PDF22

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

### Book p387 / 01 PDF23

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

### Book p388 / 01 PDF24

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

### Book p389 / 01 PDF25

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

### Book p390 / 01 PDF26

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

### Book p391 / 01 PDF27

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

### Book p392 / 01 PDF28

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

### Book p393 / 01 PDF29

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

### Book p394 / 01 PDF30

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

### Book p395 / 01 PDF31

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

### Book p396 / 01 PDF32

| Printed point / call-out | Question |
|---|---|
| Interpreting narrow QRS tachycardia: HR = 1500 / 10 = 150 bpm; every QRS preceded by P confirming SAN/atrial origin | MED-C5-15 |
| Relative frequency hierarchy: m/c SVT: Sinus tachycardia > AF > AVNRT > AVRT > SART | MED-C5-16 |
| AVNRT features: can occur in structurally normal heart, female predominance (F > M), good prognosis | MED-C5-17 |
| Normal dual AV nodal pathways: fast pathway conducts rapidly with longer refractory period; slow pathway conducts slowly with shorter refractory period where impulse dissolves | MED-C5-18 |
| AVNRT mechanism: premature SV impulse enters recovered slow pathway while fast pathway is refractory, splits to ventricles and retrograde fast pathway | MED-C5-19 |
| AVNRT retrograde atrial activation produces inverted P waves in inferior leads II, III, and aVF | MED-C5-20 |

Unasked points: **none found**.

### Book p397 / 01 PDF33

| Printed point / call-out | Question |
|---|---|
| Simultaneous P & QRS formation in 2/3rd of AVNRT patients: P wave buried in QRS complex | MED-C5-21 |
| Rate limits: sinus rhythm cannot maintain rate > 180 bpm; rate 200 - 250 bpm favors AVNRT >> AVRT | MED-C5-22 |
| Typical AVNRT (95%, PAC trigger, Slow-Fast pathway) vs Atypical AVNRT (5%, PVC trigger, Fast-Slow pathway, D/d Atrial tachycardia) | MED-C5-23 |
| Atypical AVNRT conduction limb: enters fast pathway and exits slow pathway | MED-C5-24 |

Unasked points: **none found**.

### Book p398 / 01 PDF34

| Printed point / call-out | Question |
|---|---|
| Typical AVNRT in 1/3rd patients: pseudo S wave (just outside QRS), pseudo r' wave (on r wave), pseudo Q wave (just before Q) | MED-C5-25 |
| Pharmacological conversion of AVNRT to normal sinus rhythm by intravenous adenosine | MED-C5-26 |
| AVRT clinical features: rarer than AVNRT, fundamentally associated with WPW syndrome | MED-C5-27 |
| AVRT types: Orthodromic (entry AV node, exit Bundle of Kent, narrow QRS) vs Antidromic (entry Bundle of Kent, exit AV node, wide QRS) | MED-C5-28 |

Unasked points: **none found**.

### Book p399 / 01 PDF35

| Printed point / call-out | Question |
|---|---|
| Orthodromic AVRT mechanism: well timed PAC enters AV node slowly, ventricles activate synchronously, retrograde conduction via bypass tract re-enters AV node | MED-C5-29 |
| Orthodromic AVRT ECG: RP interval 2 boxes ~ 80 - 100 ms (AVRT > AVNRT), P falls just outside QRS | MED-C5-30 |
| AVNRT vs AVRT comparison: synchronous activation (+ in AVNRT, - in AVRT), P wave absent in 2/3rd vs outside QRS, structural heart disease absent vs WPW | MED-C5-31 |
| RP intervals: AVNRT < 80 ms vs AVRT 80 - 100 ms; both categorized as short RP, long PR tachycardias | MED-C5-32 |
| AVNRT hemodynamic stability (stable) vs AVRT (stable/unstable); micro re-entry circuit in AVNRT vs macro re-entry circuit in AVRT | MED-C5-33 |
| Interval pattern note: Atrial tachycardia exhibits long RP and short PR interval | MED-C5-34 |

Unasked points: **none found**.

### Book p400 / 01 PDF36

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

### Book p401 / 01 PDF37

| Printed point / call-out | Question |
|---|---|
| Atrial tachycardia features: structurally abnormal heart, chronic tachyarrhythmia-related cardiomyopathy, follows all 3 mechanisms (m/c enhanced automaticity) | MED-C5-44 |
| Atrial tachycardia management: rate reduction to sinus rhythm via beta-blockers (metoprolol) or CCB (verapamil); antiarrhythmics on failure | MED-C5-45 |
| Unifocal AT ECG: narrow QRS, rate ~150 bpm, regular rhythm, uniform abnormal P wave, long RP / short PR, and warm-up & cool-down phenomenon | MED-C5-46 |
| Multifocal AT (MAT): irregular RR interval with ≥ 3 P wave morphologies; m/c cause COPD/theophylline; management: stop theophylline -> beta-blocker/CCB | MED-C5-47 |
| Atrial tachycardia with AV block: association with digoxin toxicity | MED-C5-48 |

Unasked points: **none found**.

### Book p402 / 01 PDF38

| Printed point / call-out | Question |
|---|---|
| AT with AV block ECG: normal P wave + buried P wave, irregular RR intervals, conducted vs missed P waves in 2:1 block | MED-C5-49 |
| Junctional tachyarrhythmia: absent P waves at HR ~100 - 110 bpm favors Junctional >> AVNRT/AVRT | MED-C5-50 |
| Summary algorithm for irregular RR narrow tachycardias: MAT, Atrial flutter with variable block, Atrial fibrillation, and focal AT with varying AV block | MED-C5-51 |
| Summary algorithm for regular RR narrow tachycardias: P wave present (sinus tachycardia, flutter 2:1, SVT short RP vs long RP) vs P wave absent (AVNRT, junctional) | MED-C5-52 |

Unasked points: **none found**.

### Book p403 / 01 PDF39

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

### Book p404 / 01 PDF40

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

### Book p405 / 01 PDF41

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

### Book p406 / 01 PDF42

| Printed point / call-out | Question |
|---|---|
| Typical atrial flutter: counterclockwise right atrial circuit, upward left atrial activation, inverted flutter waves in lead II | MED-C6-29 |
| Reverse typical atrial flutter: clockwise right atrial circuit, downward left atrial activation, upright flutter waves in lead II | MED-C6-30 |
| Atrial flutter features: lateral wall of right atrium (90%), onset < 1 week of open heart surgery, sawtooth ECG appearance | MED-C6-31 |
| Atrial flutter management: DC Cardioversion is TOC (25 - 50 J), Ibutilide | MED-C6-32 |
| Definitive catheter ablation for atrial flutter: targeting the cavotricuspid isthmus | MED-C6-33 |

Unasked points: **none found**.

### Book p407 / 01 PDF43

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

### Book p408 / 01 PDF44

| Printed point / call-out | Question |
|---|---|
| Parasystole definition: VPCs with different / variable coupling intervals | MED-C7-10 |
| Multifocal VPCs: premature ventricular complexes presenting with different morphologies | MED-C7-11 |
| Interpolated VPC: premature ventricular complex sandwiched between two consecutive sinus impulses | MED-C7-12 |
| Frequency patterns: Ventricular bigeminy (VPB after every sinus beat), trigeminy (VPB after every 2 sinus beats), couplet (2 VPBs in a row) | MED-C7-13 |
| Definition of Ventricular Tachycardia: ≥ 3 VPBs in a row + HR > 100 bpm | MED-C7-14 |
| Clinical features and management of VPCs: asymptomatic or palpitations; no treatment required; prophylactic antiarrhythmics contraindicated without significant VT | MED-C7-15 |

Unasked points: **none found**.

### Book p409 / 01 PDF45

| Printed point / call-out | Question |
|---|---|
| Warning signs for VPCs: increased frequency, multifocal, bigeminy/couplet, first episode > 40 yrs, not affected by exercise, parasystole, LV dysfunction | MED-C7-16 |
| Monomorphic VT ECG criteria: wide QRS tachycardia (> 0.16 s), rate > 200 bpm, all complexes look alike | MED-C7-17 |
| Sustained monomorphic VT definition: sustained duration ≥ 30 seconds | MED-C7-18 |
| 12-lead ECG panel demonstrating the transition from sustained monomorphic VT to ventricular bigeminy | MED-C7-19 |

Unasked points: **none found**.

### Book p410 / 01 PDF46

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

### Book p411 / 01 PDF47

| Printed point / call-out | Question |
|---|---|
| Polymorphic VT: multiple different complexes with changing polarities; usually associated with prolonged QT (Torsades de pointes) | MED-C7-28 |
| Acquired causes of TdP: MI, decreased K+, decreased Ca2+, decreased Mg2+, hypothermia, drugs (Class Ia, Ic, III; erythromycin; terfenadine) | MED-C7-29 |
| Congenital etiology of TdP: congenital Long QT syndrome | MED-C7-30 |
| Differential note on Short QT causes: Hypercalcemia, Digoxin, Hyperthermia | MED-C7-31 |
| Management of TdP: immediate defibrillation -> 2 g IV MgSO4 over 10 min -> rhythm stabilization (beta-blockers for congenital, treat cause for acquired) | MED-C7-32 |
| Cardioversion vs Defibrillation mechanism: current discharge at patient QRS vs machine discharge; T-wave vulnerable period (20 - 30 ms) risking VF | MED-C7-33 |

Unasked points: **none found**.

### Book p412 / 01 PDF48

| Printed point / call-out | Question |
|---|---|
| Synchronized cardioversion (syncs with patient rhythm) vs unsynchronized defibrillation (no need to connect patient rhythm) | MED-C7-34 |
| Paddle placement positions: right side of upper sternum below clavicle and apex of heart (left of nipple) | MED-C7-35 |
| Energy settings across arrhythmias: start with 50 J; A. Flutter (50 J), Monomorphic VT (100 J), A. Fib (100 - 200 J), Polymorphic VT (200 J) | MED-C7-36 |

Unasked points: **none found**.

### Book p413 / 01 PDF49

| Printed point / call-out | Question |
|---|---|
| WPW syndrome demographic profile: Male predominance (M > F) | MED-C8-01 |
| Classic ECG findings of WPW: normal P wave, short PR interval, delta waves, near normal QRS, secondary ST & T wave changes | MED-C8-02 |
| WPW mechanism: aberrant accessory pathway known as the Bundle of Kent causing ventricular pre-excitation | MED-C8-03 |
| Concealed vs Manifest WPW: 12-lead ECG (normal vs abnormal) and antegrade conduction (via AV node vs via Bundle of Kent) | MED-C8-04 |
| Arrhythmias triggered by PAC in concealed and manifest WPW: Orthodromic AVRT and Atrial Fibrillation | MED-C8-05 |
| Prognosis of Atrial Fibrillation: bad prognosis in concealed WPW responding only to DC cardioversion; better prognosis in manifest WPW d/t early diagnosis | MED-C8-06 |

Unasked points: **none found**.

### Book p414 / 01 PDF50

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

### Book p415 / 01 PDF51

| Printed point / call-out | Question |
|---|---|
| The ACS flowchart links rupture/erosion with critical fibrin-rich thrombosis to STEMI; incomplete platelet-rich thrombosis leads to NSTEMI. | MED-C9-01 |
| The ‘Types of plaque’ arm is explicitly divided into vulnerable and non-vulnerable plaque in the pathophysiology diagram. | MED-C9-02 |
| Epicardial arteries larger than 400 μm are placed in macrocirculation; small arteries, arterioles and capillaries form the microcirculatory side. | MED-C9-03 |
| The diagram assigns flow and transport to epicardial arteries, pressure and regulation to small arteries/arterioles, and metabolites/exchange to capillaries. | MED-C9-04 |
| Syndrome X is described as critical microvascular disease with impaired coronary reserve, reduced NO and increased endothelin/CRP. | MED-C9-05 |
| The table labels this young-smoker, rest-angina, slow-flow phenotype as Syndrome Y; thickened wall/decreased lumen raise resting coronary resistance and prognosis includes arrhythmia/sudden death. | MED-C9-06 |
| Syndrome Y is linked to young male smokers, rest angina, slow flow, vasodilator response and risk of sudden death/arrhythmias; the benign/antianginal profile is Syndrome X. | MED-C9-07 |

Unasked points: **none found**.

### Book p416 / 01 PDF52

| Printed point / call-out | Question |
|---|---|
| O2 demand: systemic SBP, HR, myocardial contractility and myocardial wall stress. Supply: coronary resistance/diameter, HR and perfusion pressure. | MED-C9-08 |
| Syndrome Z is associated with OSAS and is drawn with centripetal obesity, insulin resistance, hypertension and hyperlipidaemia. | MED-C9-09 |
| Large-vessel CAD causes listed are plaque, septic/other emboli, spasm (Prinzmetal angina), and vasculitis including Takayasu/Kawasaki. | MED-C9-10 |
| The R/F list begins with 1. Family history, 2. Degree of calcification and 3. Lifestyle: physical inactivity before smoking as the most crucial preventable cause. | MED-C9-11 |
| Smoking is explicitly marked as the most crucial preventable cause; family history, calcification, inactivity, diabetes, age and sex are also risk factors. | MED-C9-12 |
| The sheet marks hs-CRP <1 mg/dL as low, 1–3 as increased, and >3 mg/dL as markedly increased. | MED-C9-13 |
| The hyperlipidaemia list includes hs-CRP, Lp(a), Lp-PLA2, high small dense/oxidised LDL and low HDL. | MED-C9-14 |
| Hypertension is listed with alters vessel architecture, endothelial dysfunction and LVH increasing myocardial O2 demand. | MED-C9-15 |
| Diabetes (centripetal obesity with increased lipolysis and insulin resistance), Age 40–50 years and Gender F greater than M are listed after hyperlipidaemia. | MED-C9-16 |
| Plaque is termed atherosclerotic coronary vascular disease (ASCVD); stenosis around 60–70% or more is marked significant. | MED-C9-17 |

Unasked points: **none found**.

### Book p417 / 01 PDF53

| Printed point / call-out | Question |
|---|---|
| Hibernation is chronic persistent ischaemic dysfunction; the table notes FDG-PET > MRI for differentiating ischaemia and infarction. | MED-C9-18 |
| Stunning is an acute, transient post-reperfusion segmental dysfunction, whereas hibernation is a chronic state. | MED-C9-19 |
| The page lists LDL >190 mg/dL with target <100 mg/dL, diabetes age 40–75 (moderate-intensity rosuvastatin 10–20 mg), and clinical atherosclerosis. | MED-C9-20 |
| The printed HOPE note reads ‘Ramipril ↓ fatal/non-vascular events → ACE inhibitors > ARBs.’ | MED-C9-21 |
| Agatston score is determined by coronary CT; calcification is noted as irreversible, and medial calcification is linked to increased PTH and Ca×PO4. | MED-C9-22 |
| The printed advice is salt <6 g/day, protein 1 g/kg/day, dietary cholesterol <200 mg/day, soluble fibre >10–25 g/day, and saturated fat <7%. | MED-C9-23 |
| The page notes malnutrition-inflammation-atherosclerosis with protein malnutrition increasing CRP under the lifestyle modifications block. | MED-C9-24 |

Unasked points: **none found**.

### Book p418 / 01 PDF54

| Printed point / call-out | Question |
|---|---|
| In the diagram, >70% plaque with symptoms leads to angiography/stenting; the asymptomatic branch is labelled ACS. A roughly 20–30% plaque may rupture and cause MI. | MED-C9-25 |
| Chronic stable angina is exertional chest tightness/squeezing/burning behind or left of mediastinum, can radiate C8–T4, lasts <20 min, and responds well to SL/oral NTG; >30 min suggests ACS. | MED-C9-26 |
| Treadmill testing is indicated in chronic stable angina and asymptomatic risk-factor patients; rest symptoms, aortic stenosis and HOCM are contraindications. | MED-C9-27 |
| Positive treadmill test: 2 mm horizontal/downsloping ST segment before 6 minutes/before achieving maximum HR, followed by angiography. | MED-C9-28 |
| The presentation block states radiation may involve any dermatome from C8 to T4. | MED-C9-29 |

Unasked points: **none found**.

### Book p419 / 01 PDF55

| Printed point / call-out | Question |
|---|---|
| MPS is done with Tc-99m or thallium; listed uses include rest symptoms, localisation, abnormal baseline ECG, and assessing completeness of revascularisation. | MED-C9-30 |
| FDG-PET distinguishes stunned from scarred myocardium. The source also states FDG-PET/MRI are preferred over MPS to distinguish ischaemia from infarction. | MED-C9-31 |
| Electron beam CT is listed to quantify cardiac calcification in the miscellaneous points. | MED-C9-32 |
| The page identifies exercise radionuclide angiography/MUGA for cardiac volumes and functions. | MED-C9-33 |
| MRI is marked IOC for myocardial fibrosis/ejection fraction and gold standard for ejection fraction; IVUS is IOC for ostial left-main lesion/coronary dissection. | MED-C9-34 |
| After SL NTG 3 tablets/20 min without improvement, the flowchart flags ACS and lists NTG plus beta-blockers as first line. | MED-C9-35 |
| The table lists 1st line nitrates vasodilation with ↑HR ↓BP limitation tolerance, beta-blockers ↓pump function ↓HR ↓BP prolonging life post MI, and 2nd line CCBs ↓pump function plus vasodilation ↓HR ↓BP. | MED-C9-36 |
| Ivabradine inhibits funny current and lowers HR; visual disturbance is its source-listed adverse effect. Trimetazidine inhibits pFOX with no BP/HR effect; ranolazine may prolong QT. | MED-C9-37 |
| Fasudil is shown as a Rho-kinase inhibitor; nicorandil is a K+ channel activator. | MED-C9-38 |

Unasked points: **none found**.

### Book p420 / 01 PDF56

| Printed point / call-out | Question |
|---|---|
| The stenting note lists abciximab, eptifibatide and tirofiban as GP IIb–IIIa inhibitors and favours tacrolimus/paclitaxel drug-eluting over bare-metal stents. | MED-C9-39 |
| Prinzmetal angina is rest angina, lasts 5–15 min, has transient ST elevation and normal angiography; beta-blockers are to be avoided. | MED-C9-40 |
| Kingmaker segment is stated to be the ST segment: end of J point to onset of T wave. | MED-C9-41 |
| Systolic current from subepicardial/transmural injury flows toward injured myocardium and produces ST elevation (MI or pericarditis); subendocardial diastolic current flows away and produces non-localising ST depression. | MED-C9-42 |
| The diagrams contrast non-concave/convex ST elevation in MI with concave/saddle-shaped elevation in pericarditis. | MED-C9-43 |
| The diagram labels PR interval, ST interval, TP interval, QT interval and RR interval with calibration 0.04 s =40 ms and 0.20 s =200 ms. | MED-C9-44 |

Unasked points: **none found**.

### Book p421 / 01 PDF57

| Printed point / call-out | Question |
|---|---|
| Listed alternatives are Prinzmetal angina, hyperkalaemia > hypokalaemia, LBBB, benign early repolarisation and LV aneurysm. | MED-C9-45 |
| Convex and coved morphologies are labelled ACS; horizontal/plateau is ‘ACS unless proven otherwise’; oblique is <30% ACS and concave <15% ACS. | MED-C9-46 |
| Significant V2–V3 elevation is ≥2.5 mm if <40 years, ≥2 mm if >40 years, and ≥1.5 mm in females; reciprocal changes must be present in the source's MI diagnosis note. | MED-C9-47 |
| The sequence progresses from hyperacute T wave to hyperacute T waves with ST elevation, then pathological Q/decreasing R and further ST/T changes over hours to days. | MED-C9-48 |
| The illustrated tracing is captioned ST elevation with reciprocal changes and marks a high lateral MI pattern. | MED-C9-49 |
| The page marks normal ST elevation at the transient zone in V2–V3 without pathological reciprocal changes. | MED-C9-50 |

Unasked points: **none found**.

### Book p422 / 01 PDF58

| Printed point / call-out | Question |
|---|---|
| Benign early repolarisation has ST elevation and J-point hook effect; PR depression supports pericarditis instead. | MED-C9-51 |
| The pericarditis block gives clinical features/acute illness, global concave upward ST elevation, PR depression and no reciprocal changes. | MED-C9-52 |
| Hypothermia is labelled with an Osborne wave. The page also illustrates post-DC-cardioversion tracing and Takotsubo cardiomyopathy. | MED-C9-53 |
| Takotsubo cardiomyopathy is labelled catecholamine-induced cardiac failure/broken-heart syndrome and most common in middle-aged females. | MED-C9-54 |
| The printed differential says BER has no PR depression; pericarditis has PR depression, global concave elevation and no reciprocal changes. | MED-C9-55 |

Unasked points: **none found**.

### Book p423 / 01 PDF59

| Printed point / call-out | Question |
|---|---|
| The summary panel lists LVH, LBBB, acute pericarditis, pseudo-infarction pattern (hyperkalaemia), acute anteroseptal MI, acute anterolateral MI and Brugada syndrome. | MED-C9-56 |
| The summary labels horizontal ST depression ‘probable ischemia’; sloping ST is strain-related and scoop-shaped ST is digoxin-related. | MED-C9-57 |
| The ‘scoop’ example is explicitly labelled digoxin related; morphology must be interpreted in clinical context. | MED-C9-58 |
| The final tracing is captioned ‘de Winter T waves: evolves to MI.’ | MED-C9-59 |

Unasked points: **none found**.

### Book p424 / 01 PDF60

| Printed point / call-out | Question |
|---|---|
| The page contrasts normal myocardium, tall/peaked T waves in subendocardial ischaemia, and deep symmetrical inversion in transmural ischaemia. | MED-C9-60 |
| Deep symmetrical T inversion is labelled transmural ischaemia; tall/peaked T waves are subendocardial ischaemia. | MED-C9-61 |
| The lower paired ECGs show hyperacute T waves progressing to STEMI. | MED-C9-62 |
| The note beneath the strip states ‘U waves: Hypokalemia.’ | MED-C9-63 |
| The page presents serial ST-depression changes at 60, 90 and 120 minutes before its T-wave panels. | MED-C9-64 |

Unasked points: **none found**.

### Book p425 / 01 PDF61

| Printed point / call-out | Question |
|---|---|
| Right coronary circulation is linked to IWMI, PWMI and RVMI; left circulation is linked to AWMI, septal MI and LWMI. | MED-C10-01 |
| Surface list: anterior sternocostal = RV; inferior diaphragmatic = RV+LV; posterior = LA. | MED-C10-02 |
| Dominance is based on the artery supplying posterior interventricular sulcus/PDA: RCA gives right dominance (85%); LCx gives left dominance (15%). | MED-C10-03 |
| Inferior leads are II, III, aVF; RV free-wall V3R/V4R/V5R and posterior V7/V8/V9 are not represented on a standard 12-lead ECG; lateral V5/V6 show reciprocal changes. | MED-C10-04 |
| Right free-wall leads are V3R–V5R. The source separately lists V7–V9 for posterior wall assessment. | MED-C10-05 |

Unasked points: **none found**.

### Book p426 / 01 PDF62

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

### Book p427 / 01 PDF63

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

### Book p428 / 01 PDF64

| Printed point / call-out | Question |
|---|---|
| The localisation list proceeds: before D1; between D1 and S1; and below S1 (with branches S1–D2 or D2–D3). | MED-C10-21 |
| For anteroseptal high-lateral MI: V2–V4 elevation indicates LAD, V1 elevation indicates above S1, and I/aVL elevation indicates before D1. | MED-C10-22 |
| The wrap-around section says V2–V4 elevation is above D2; V1 no elevation is below S1; II/V5/V6 elevation identifies wrap-around. | MED-C10-23 |
| The page explicitly labels II, V5 and V6 elevation as wrap-around phenomenon; course enters posterior interventricular sulcus and anastomoses with PDA. | MED-C10-24 |
| The source states anterolateral MI has anatomical S1 before D1 and occlusion between S1 and D1. | MED-C10-25 |
| The anteroseptal section labels V1 ST elevation as above S1 and I/aVL ST depression as between D1 and S1. | MED-C10-26 |

Unasked points: **none found**.

### Book p429 / 01 PDF65

| Printed point / call-out | Question |
|---|---|
| Proximal LCA occlusion: aVR ST elevation, all other leads ST depression, 100% mortality if untreated; immediate PCI is specified. | MED-C10-27 |
| AWMI LV involvement includes VT, VF and sudden cardiac death; mechanical complications include external cardiac rupture and septal rupture, plus infra-Hisian blocks. | MED-C10-28 |
| The AWMI complication list includes infra-Hisian blocks, in contrast to the nodal problems emphasised in IWMI. | MED-C10-29 |

Unasked points: **none found**.

### Book p430 / 01 PDF66

| Printed point / call-out | Question |
|---|---|
| The obsolete scheme maps critical fibrin-rich thrombus to STEMI/STE-ACS and incomplete platelet-rich thrombus to NSTE-ACS; normal enzymes mean unstable angina and raised enzymes NSTEMI. | MED-C11-01 |
| The page replaces the older model with myocardial injury ± clinical evidence of myocardial ischaemia. | MED-C11-02 |
| Myocardial injury is cardiac troponin T/I with at least one value above the 99th percentile and an acute rise and fall. | MED-C11-03 |
| Non-cardiac causes listed include sepsis, subarachnoid haemorrhage, CKD, critical illness and pulmonary embolism. Cardiac causes include myocarditis, Takotsubo, defibrillator shocks, tachyarrhythmia and spasm/embolism/dissection. | MED-C11-04 |
| The causes tree lists increased O2 demand from tachyarrhythmia and decreased supply from spasm, embolism or dissection. | MED-C11-05 |

Unasked points: **none found**.

### Book p431 / 01 PDF67

| Printed point / call-out | Question |
|---|---|
| Clinical evidence listed: symptoms, new ECG changes, pathological Q waves, imaging evidence of new RWMA, and angiographic evidence of coronary thrombus. | MED-C11-06 |
| Type 1 is atherothrombotic occlusion; Type 2 is supply/demand mismatch (ICU patients, severe anaemia); Type 3 sudden cardiac death; Type 4 post-PCI; Type 5 post-CABG. | MED-C11-07 |
| The list gives Type 4 as post-percutaneous coronary intervention and Type 5 as post-coronary artery bypass graft. | MED-C11-08 |
| The graph note says ultrasensitive troponin assays can detect as low as 0.01 ng/mL of enzyme elevation. | MED-C11-09 |
| Rise/fall with acute ischaemia is acute MI; the atherosclerosis/thrombosis arm is Type 1 (plaque rupture/erosion). Without acute ischaemia it is acute injury; stable troponin is chronic injury. | MED-C11-10 |
| The stable-troponin branch is chronic myocardial injury and gives structural heart disease and CKD as examples. | MED-C11-11 |

Unasked points: **none found**.

### Book p432 / 01 PDF68

| Printed point / call-out | Question |
|---|---|
| The table defines reinfarction within 28 days and recurrence after 28 days. | MED-C11-12 |
| Two troponin values are obtained immediately and 3–6 h later; a >20% increase is specified. The table says no role for CPK-MB. | MED-C11-13 |
| Plaque rupture is 60–70% (most common), associated with men and elevated cholesterol; erosion 30–40% is associated with younger females and smoking. | MED-C11-14 |
| Vulnerable plaque features: thin cap, necrotic lipid core >40%, increased macrophages, reduced smooth-muscle cell content and spotty calcification. | MED-C11-15 |
| Hibernating myocardium is chronic, viable and has reduced function due to low perfusion; MRI should be used for evaluation. | MED-C11-16 |
| Stunned myocardium is acute/post-ischaemic: restoring perfusion for a few hours precedes low function in viable tissue. | MED-C11-17 |

Unasked points: **none found**.

### Book p433 / 01 PDF69

| Printed point / call-out | Question |
|---|---|
| NSTEMI features listed are rest angina >20 min, new-onset severe/crescendo angina, ST depression/T inversion and elevated troponin. | MED-C11-18 |
| The NSTEMI feature list states TIMI score determines mortality risk. | MED-C11-19 |
| Clinical presentation states age 40–50 in India (50–60 outside), females > males in India (reverse outside), vague symptoms in females and absent classic pain in diabetic patients. | MED-C11-20 |
| The lower ECG caption identifies significant ST depression as NSTEMI; the comparison example is non-significant ST depression. | MED-C11-21 |

Unasked points: **none found**.

### Book p434 / 01 PDF70

| Printed point / call-out | Question |
|---|---|
| The table gives right arm/shoulder radiation 4.7 (0.9–12.0), both arms 4.1, exertion 2.4, left arm 2.3, diaphoresis 2.0, nausea/vomiting 1.9 and pressure 1.3. | MED-C11-22 |
| ACA note: new chest pain in middle-aged/elderly, night presentation or being forced awake and unable to sleep is ‘cardiac unless proved otherwise.’ | MED-C11-23 |
| Angina equivalents listed are dyspnoea, fatigue, diaphoresis and atypical-site pain. | MED-C11-24 |
| Management continuum: pre-CCU morphine/sedation 30% one-month mortality; CCU beta-blocker/defibrillator 15%; reperfusion with thrombolysis/PCI 5%. | MED-C11-25 |
| The source places thrombolysis and percutaneous intervention under reperfusion (since 1975). | MED-C11-26 |

Unasked points: **none found**.

### Book p435 / 01 PDF71

| Printed point / call-out | Question |
|---|---|
| STEMI salient feature: acute total occlusion due to plaque rupture (most common). | MED-C11-27 |
| The artery list ranks LAD most common, then RCA, then LCx. | MED-C11-28 |
| Golden hours are the first 6 h. After 6 h from pain onset, only one-sixth of myocardium remains viable in the source. | MED-C11-29 |
| Before 6 h myocardium can be salvaged; after 6 h the stated aims are pain reduction and prevention of electrical/mechanical complications. | MED-C11-30 |
| The graph says opening the artery is the primary goal (PCI/lysis) and time to treatment is critical for mortality/salvage. | MED-C11-31 |

Unasked points: **none found**.

### Book p436 / 01 PDF72

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

### Book p437 / 01 PDF73

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

### Book p438 / 01 PDF74

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

### Book p439 / 01 PDF75

| Printed point / call-out | Question |
|---|---|
| GP IIb–IIIa inhibitors are abciximab, tirofiban, eptifibatide; use is downstream bailout in cath lab if no TIMI 3/MPG 3 flow or high thrombus burden. | MED-C11-54 |
| ACE inhibitors/beta-blockers have survival advantage if started within first 24 h, but are avoided with heart-failure signs/low-output state. | MED-C11-55 |
| Available PCI centre branch lists aspirin 325 mg, ticagrelor 180 mg or clopidogrel 600 mg, rosuvastatin 40 mg, then cath lab. | MED-C11-56 |
| No-centre branch: thrombolysis with clopidogrel 300 mg + tenecteplase 0.5 mg/kg, repeat ECG after 60–90 min, then enoxaparin 30 mg IV and pharmaco-invasive/rescue PCI. | MED-C11-57 |
| CCU/discharge box: rosuvastatin 20 mg lifelong, aspirin 75 mg lifelong, clopidogrel 75 mg ×1 year. | MED-C11-58 |
| Contraindications include intracranial haemorrhage/structural mass, recent stroke, bleeding disorder/aortic dissection, recent severe head/facial trauma, intracranial/intraspinal surgery, uncontrolled HTN, and recent streptokinase use. | MED-C11-59 |

Unasked points: **none found**.

### Book p440 / 01 PDF76

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

### Book p441 / 01 PDF77

| Printed point / call-out | Question |
|---|---|
| Clinical presentation on p441 describes increasing nature/duration (>20 min)/frequency and pain not relieved by nitrates/rest. | MED-C11-67 |
| Treatment: O2 if SpO2<90%, aspirin 325 mg chewable non-enteric, rosuvastatin 40 mg, SL nitrate 5 mg repeated three times, morphine, PCI within 24 h (high risk within 2 h). | MED-C11-68 |
| Landmark changes list intervention-based guideline: PCI TOC; angiography within 24 h (high risk 2 h), with P2Y12 inhibitor in cath lab. | MED-C11-69 |
| Peri-interventional anticoagulation: enoxaparin 0.5 mg/kg bolus until cath lab. | MED-C11-70 |
| Cath-lab loading options: prasugrel 60 mg, ticagrelor 180 mg, or clopidogrel 600 mg. | MED-C11-71 |
| After discharge: aspirin 75 mg lifelong, rosuvastatin 20 mg lifelong, and ticagrelor 90 mg BD ×1 y or clopidogrel 75 mg OD ×1 y or prasugrel 10 mg ×1 y (best). | MED-C11-72 |

Unasked points: **none found**.

### Book p442 / 01 PDF78

| Printed point / call-out | Question |
|---|---|
| The CTD map marks rheumatoid arthritis as most common and Sjogren syndrome as second most common. | MED-C12-01 |
| Sjogren syndrome is described as a multisystem autoimmune inflammatory CTD in middle-aged females (40–60) with F:M = 9:1. | MED-C12-02 |
| Secondary Sjogren has CTD association, ranked RA > SLE > IMD; primary has no such association. | MED-C12-03 |
| Classification by pathology divides glandular (50%) and extraglandular (50%); extraglandular disease is multisystem and 15% is severe/life-threatening. | MED-C12-04 |
| The clinical hallmark is dry eye and dry mouth; thyroid is noted as the simple endocrine organ involved and Sjogren can be an extrahepatic manifestation of HCV. | MED-C12-05 |

Unasked points: **none found**.

### Book p443 / 01 PDF79

| Printed point / call-out | Question |
|---|---|
| HCV extrahepatic manifestations listed are cutaneous lichen planus, porphyria cutanea tarda, cryoglobulinaemia, Sjogren syndrome and MPGN. | MED-C12-06 |
| Genetic/environmental factors → autoantibodies → autoimmune lymphocytic exocrinopathy (periductal/perivascular) → ductal epithelial activation → the listed sicca symptoms. | MED-C12-07 |
| Genetic factors list HLA-DR3; the note identifies SLE as another disease associated with HLA-DR3. | MED-C12-08 |
| The inflammation line states T cell (Th1 > Th2) > B cell. | MED-C12-09 |
| IL-18-positive macrophages are linked to salivary-gland enlargement/painless parotid enlargement. | MED-C12-10 |
| Antibodies list anti-M3 (muscarinic) → cholinergic agonist cevimeline for treatment, and anti-α-fodrin. | MED-C12-11 |

Unasked points: **none found**.

### Book p444 / 01 PDF80

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

### Book p445 / 01 PDF81

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

### Book p446 / 01 PDF82

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

### Book p447 / 01 PDF83

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

### Book p448 / 01 PDF84

| Printed point / call-out | Question |
|---|---|
| Score 3: histopathology focus score ≥1/mm² and anti-Ro/SS-A. Score 1: ocular staining/Rose Bengal, Schirmer ≤5 mm/5 min, and salivary flow <0.1 mL/min. | MED-C12-42 |
| Rules: at least one symptom of ocular/oral dryness plus total score ≥4. | MED-C12-43 |
| Exclusions include prior head/neck radiation, active HCV, AIDS, sarcoidosis, amyloidosis, GVHD and IgG4-related disease. | MED-C12-44 |
| High anti-Ro/La in pregnancy increases congenital heart block risk (2–5%). The source contrasts offspring risk for CTD in Sjogren male versus SLE female contexts. | MED-C12-45 |
| Differential: sarcoidosis = ILD + uveitis + hilar adenopathy; IgG4-RD = storiform fibrosis + plasmacytic infiltrate + pancreatitis. | MED-C12-46 |
| Treatment: glandular saliva substitute/cevimeline/artificial tears. Fatigue/arthralgia uses low-dose steroid <7.5 mg/day + NSAIDs + HCQ; severe life-threatening disease uses high-dose steroid + immunosuppressant/MMF. | MED-C12-47 |

Unasked points: **none found**.

### Book p449 / 01 PDF85

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

### Book p450 / 01 PDF86

| Printed point / call-out | Question |
|---|---|
| Type 1 autoimmune pancreatitis is most common in IgG4-RD and presents with obstructive jaundice; ERCP is IOC and CT shows sausage pancreas/homogeneous enhancement. | MED-C13-09 |
| AIP is associated with endocrine insufficiency → type 3c DM and exocrine insufficiency → malabsorption. | MED-C13-10 |
| Salivary involvement is bilateral painless submandibular enlargement with minimal sicca symptoms. | MED-C13-11 |
| Orbital/periorbital lesions include orbital inflammatory pseudotumours; lacrimal enlargement/dacryoadenitis is marked most common orbital manifestation. | MED-C13-12 |
| Minor CNS manifestations are lymphocytic hypophysitis (postpartum women with ↑ICT) and pachymeningitis without parenchymal involvement. | MED-C13-13 |
| Tubulointerstitial disease is most common renal manifestation, with minimal CKD risk and no renal tubular acidosis; membranous nephropathy is glomerular involvement. | MED-C13-14 |

Unasked points: **none found**.

### Book p451 / 01 PDF87

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

### Book p452 / 01 PDF88

| Printed point / call-out | Question |
|---|---|
| SLE is described as a disease of women of reproductive age (20–40) with 9:1 female predominance. | MED-C14-01 |
| The source lists positive concordance in >40% of identical twins and strong family history. | MED-C14-02 |
| Lupus nephritis is shown in adults 50–60% and childhood SLE 100%. | MED-C14-03 |
| Postmenopausal SLE has good prognosis, no CNS/renal symptoms, sicca/serositis/musculoskeletal symptoms, anti-Ro positive, anti-dsDNA negative and normal complements. | MED-C14-04 |
| The bottom notes state male SLE has poor prognosis; active SLE markers are anti-dsDNA positive and low complements. | MED-C14-05 |

Unasked points: **none found**.

### Book p453 / 01 PDF89

| Printed point / call-out | Question |
|---|---|
| Genetic/environmental causes lead to defective clearance of apoptotic and NETotic debris, triggering immune dysregulation. | MED-C14-06 |
| TLR-7 and TLR-9 are labelled pattern-recognition receptors; hydroxychloroquine is drawn inhibiting this step. | MED-C14-07 |
| Activated plasmacytoid dendritic cells produce type I interferon/IFNα, identified as the central key pathogenic cytokine; anifrolumab is shown blocking it. | MED-C14-08 |
| The diagram depicts Th1, Th2 > Th17; Th2 cytokines IL-4, IL-5 and IL-13 aid B-cell activation. | MED-C14-09 |
| BAFF/B-lymphocyte stimulator (BLyS) is shown upregulated in SLE; belimumab inhibits it. | MED-C14-10 |
| B cells form immune complexes/type-III hypersensitivity that deposit in glomerulus (GN), synovial cavity (synovitis) and vessels (vasculitis). | MED-C14-11 |

Unasked points: **none found**.

### Book p454 / 01 PDF90

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

### Book p455 / 01 PDF91

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

### Book p456 / 01 PDF92

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

### Book p457 / 01 PDF93

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

### Book p458 / 01 PDF94

| Printed point / call-out | Question |
|---|---|
| Constitutional symptoms are listed as fatigue and weight loss, pyrexia of unknown origin (PUO) and leucopenia. | MED-C16-01 |
| The cutaneous section opens with the Gilliam-Sontheimer classification into lupus specific and lupus non-specific lesions. | MED-C16-02 |
| ACLE is listed first among lupus-specific lesions and marked (m/c); its localised form (malar rash) is also marked m/c. | MED-C16-03 |
| Localised ACLE is symmetrical, erythematous, scaly and NON-scarring (with or without oedema); scarring belongs to discoid/CCLE disease. | MED-C16-04 |
| The ACLE block associates painless oral/nasopharyngeal ulcers and non-scarring alopecia with the malar rash. | MED-C16-05 |
| Generalised ACLE is annotated as sparing the knuckles; the TEN-like lupus image is attached to the same ACLE arm. | MED-C16-06 |
| SCLE is listed with anti-Ro/La (+), association with HLA DR3 and photosensitivity. | MED-C16-07 |

Unasked points: **none found**.

### Book p459 / 01 PDF95

| Printed point / call-out | Question |
|---|---|
| The note lists rash involving the nasolabial fold under acne rosacea (a) and dermatomyositis (b); SLE malar rash spares the nasolabial fold. | MED-C16-08 |
| The 5/20 rule: 5% of patients with discoid rash have SLE and 20% of patients with SLE have a discoid rash. | MED-C16-09 |
| CCLE/discoid rash: circular raised erythematous patching with scarring; biopsy shows follicular plugging, keratotic scaling and dermal atrophy; there is a risk of progression to squamous cell carcinoma. | MED-C16-10 |
| CCLE is associated with cicatricial (scarring) alopecia, shown with the carpet-track sign of DLE. | MED-C16-11 |
| SCLE patterns listed are annular and psoriasiform, the latter marked with increased conversion to SLE. | MED-C16-12 |
| SCLE: 20% of patients with SCLE have SLE, white population, association with HLA DR3, anti-Ro with reduced renal involvement. | MED-C16-13 |
| Lupus non-specific lesions listed are chilblain lupus and lupus panniculitis/profundus (subcutaneous, tender erythematous nodules). | MED-C16-14 |

Unasked points: **none found**.

### Book p460 / 01 PDF96

| Printed point / call-out | Question |
|---|---|
| The note states lupus pernio is sarcoidosis and lupus vulgaris is TB. | MED-C16-15 |
| Musculoskeletal manifestations are marked (m/c system involved); the site is upper limb >> lower limb with small-joint and wrist involvement progressing to arthritis. | MED-C16-16 |
| SLE arthritis is non-erosive and deforming from ligament laxity, producing Jaccoud arthropathy, which is also seen in Sjogren syndrome. | MED-C16-17 |
| SLE with erosive arthritis is labelled Rhupus (RA/SLE overlap) and anti-CCP is positive. | MED-C16-18 |
| Under complications, septic arthritis is the concern in a patient on SLE treatment with a single joint involved out of proportion; the monoarthritis note lists crystal arthropathy and septic arthritis in the differential. | MED-C16-19 |
| Avascular necrosis presents as acute joint pain after about three months of disease; MRI is marked as the investigation of choice. | MED-C16-20 |
| SLE with constitutional, skin and joint involvement is labelled non-organ/life-threatening SLE, in contrast to organ-system involvement which carries a bad prognosis. | MED-C16-21 |
| Organ-system involvement: kidney involved in 50-60%, and 10% progress to CKD. | MED-C16-22 |
| Immunosuppressive therapy leading to infection is the most common cause of death in the first 10 years; acute coronary syndrome is the most common cause of death after 10 years, in keeping with accelerated atherosclerosis being an MI equivalent. | MED-C16-23 |
| Vascular disease is noted in one-third of patients (thrombosis and accelerated atherosclerosis); dangerous vasculitis is medium-vessel, involving mesenteric and CNS vessels. | MED-C16-24 |

Unasked points: **none found**.

### Book p461 / 01 PDF97

| Printed point / call-out | Question |
|---|---|
| RBC: anaemia of chronic disease is the most common; rapidly progressive anaemia is autoimmune haemolytic anaemia. | MED-C16-25 |
| WBC: leucopenia/lymphopenia with a raised risk of DLBCL; the note contrasts Sjogren syndrome, which raises the risk of marginal zone B-cell lymphoma. | MED-C16-26 |
| Platelet: secondary ITP is listed in the haematological manifestations. | MED-C16-27 |
| The lung block states the lung parenchyma is spared in SLE, therefore there is no ILD; pleuritis and diffuse alveolar haemorrhage dominate instead. | MED-C16-28 |
| Pleuritis is the most common lung manifestation, with or without a small, bilateral, exudative effusion. | MED-C16-29 |
| Cough, haemoptysis and bilateral air-space opacification indicate diffuse alveolar haemorrhage, which requires active immunosuppression; the contrasting branch (viral/TB) is managed by stopping immunosuppression. | MED-C16-30 |
| DAH is flagged as carrying a poor prognosis and as the most important marker of SLE disease activity in the lung. | MED-C16-31 |
| Activity assessment: clinically active disease with new-onset rashes, rising anti-dsDNA titres, falling C3 and C4, and a raised ESR with a low CRP (below 10 mg/dL). | MED-C16-32 |
| Cardiac: pericarditis without tamponade is the most common manifestation; myocarditis is associated with anti-Ro antibody. | MED-C16-33 |
| Libman-Sacks endocarditis is described with vegetations on the undersurface of the valve leaflet; mitral regurgitation is the most common valvular lesion. | MED-C16-34 |
| GIT: generally spared. Hepatobiliary: type 1 autoimmune hepatitis (lupoid hepatitis). | MED-C16-35 |
| Indications for renal biopsy: proteinuria >1 g/day, or proteinuria ≥500 mg/day plus ≥3 RBCs in urine (microhaematuria). | MED-C16-36 |

Unasked points: **none found**.

### Book p462 / 01 PDF98

| Printed point / call-out | Question |
|---|---|
| Class I minimal mesangial lupus nephritis shows mesangial immune-complex deposits, is asymptomatic and has an excellent prognosis, whereas class II mesangial proliferative disease is marked as having a poor prognosis. | MED-C16-37 |
| Class III focal lupus nephritis has <50% glomerular involvement; class IV diffuse has >50% glomerular involvement. | MED-C16-38 |
| Class III focal lupus nephritis is linked with RPGN and the table states these patients require active immunosuppression. | MED-C16-39 |
| Class V shows membranous nephropathy with adult-onset nephrotic syndrome, is resistant to steroid, and carries a better prognosis. | MED-C16-40 |
| Class VI advanced sclerotic lupus has >90% glomerular sclerosis and CKD, and is marked as the worst prognosis. | MED-C16-41 |
| Class III and IV lupus nephritis: HP shows endocapillary plus mesangial proliferation. | MED-C16-42 |
| IF shows IgG, IgA, IgM, C1q and C3 deposits, the full-house pattern; the note adds that it is also seen in HIV. | MED-C16-43 |
| EM shows subendothelial (wire loop lesion) and mesangial deposits; hematoxylin bodies of Gross are described as most specific, and tubuloreticular inclusions are also shown. | MED-C16-44 |

Unasked points: **none found**.

### Book p463 / 01 PDF99

| Printed point / call-out | Question |
|---|---|
| CNS: cognitive decline is the most common manifestation, with a raised risk of stroke due to antiphospholipid antibodies; small-fibre neuropathy and CNS vasculitis are also listed. | MED-C16-45 |
| Constitutional domain: fever 2. Arthritis domain: synovitis or tenderness in at least 2 joints, 6. | MED-C16-46 |
| Cutaneous domain: non-scarring alopecia 2, oral ulcers 2, subacute cutaneous or discoid lupus 4 and acute cutaneous lupus 6. | MED-C16-47 |
| Neurologic domain: delirium 2, psychosis 3, seizure 5. | MED-C16-48 |
| Serositis domain: pleural or pericardial effusion 5 and acute pericarditis 6. | MED-C16-49 |
| Haematologic domain: leukopenia 3, thrombocytopenia 4, autoimmune haemolysis 4. | MED-C16-50 |
| Renal domain: proteinuria >0.5 g/24 hr = 4 points; class II or V lupus nephritis = 8; class III or IV lupus nephritis = 10. | MED-C16-51 |
| Antiphospholipid antibody domain: anticardiolipin IgG >40 GPL, or anti-β2 glycoprotein I IgG >40 units, or lupus anticoagulant scores 2. | MED-C16-52 |
| Complement proteins domain: low C3 or low C4 = 3; low C3 and low C4 = 4. Highly specific antibodies domain: anti-dsDNA = 6 and anti-Sm = 6. | MED-C16-53 |
| The table notes that all patients classified as having SLE must have ANA ≥1:80 (entry criterion) and patients must have ≥10 points to be classified as SLE. | MED-C16-54 |
| The note states that classification criteria are not diagnostic criteria. | MED-C16-55 |

Unasked points: **none found**.

### Book p464 / 01 PDF100

| Printed point / call-out | Question |
|---|---|
| Treat to target: SLE diagnosis to active disease to initial treatment to remission; the target is the SLE Disease Activity Index (SLEDAI) to 0, which is the indicator of remission. | MED-C16-56 |
| Initial Rx: constitutional symptoms are managed with HCQ (hydroxychloroquine) and observation. | MED-C16-57 |
| Non-life-threatening SLE: low-dose steroid (<7.5 mg/day) plus HCQ 5 mg/kg/day. | MED-C16-58 |
| Optical coherence tomography (OCT) is listed to look for retinal toxicity during HCQ therapy. | MED-C16-59 |
| IV steroid: methylprednisolone 500 mg to 1 g IV infusion in 100 ml normal saline over 1-2 hours, given as a pulse for 3 days. | MED-C16-60 |
| The pulse is followed by oral steroid 1 mg/kg/day, tapered over 3 months to 5 mg/day. | MED-C16-61 |
| Alongside IV steroid: oral MMF (mycophenolate mofetil) 2-3 g/day or IV cyclophosphamide 500 mg, two doses two weeks apart. | MED-C16-62 |
| Adverse effects with long-term cyclophosphamide use: secondary malignancy (AML) and gonadal toxicity. | MED-C16-63 |
| The algorithm states: assess remission after more than 3 months using the SLEDAI index. | MED-C16-64 |

Unasked points: **none found**.

### Book p465 / 01 PDF101

| Printed point / call-out | Question |
|---|---|
| Maintenance Rx: steroid (<7.5 mg/day) plus MMF (1 g/day) or azathioprine for 2-3 years. | MED-C16-65 |
| Belimumab is listed as the steroid-sparing agent in the maintenance block. | MED-C16-66 |
| The flowchart takes the no-remission (>3 months) branch to switching to cyclophosphamide, and if there is still no response the case is labelled refractory lupus. | MED-C16-67 |
| Refractory lupus: rituximab, voclosporin (a calcineurin inhibitor) with MMF, belimumab (anti-BLyS) and anifrolumab (anti type I interferon). | MED-C16-68 |
| The refractory-lupus block adds that plasma exchange is done if DAH or CNS vasculitis is present. | MED-C16-69 |
| Goals of Rx: asymptomatic, urine normal, complement normal, and no fever and no cytopenias. | MED-C16-70 |
| The CHImP mnemonic lists carbamazepine, chlorpromazine, hydralazine, isoniazid, interferon, infliximab, methyldopa, procainamide and phenytoin. | MED-C16-71 |
| Clinical features: M = F, CNS and renal not involved, anti-dsDNA negative, antihistone antibody positive, ANA positive in 100% and skin plus joint involvement. | MED-C16-72 |
| Drug-induced lupus spares the CNS and kidneys and is anti-dsDNA negative; nephritis with a rising anti-dsDNA belongs to SLE. | MED-C16-73 |
| The note states that drugs causing SLE (drug-induced lupus) are safe in lupus patients. | MED-C16-74 |

Unasked points: **none found**.

### Book p466 / 01 PDF102

| Printed point / call-out | Question |
|---|---|
| The heading notes the syndrome was earlier called antiphospholipid antibody syndrome (APLA). | MED-C17-01 |
| The chapter notes that one-third of SLE cases are APS positive. | MED-C17-02 |
| In the complications-of-SLE note, APS is described as increasing susceptibility to thrombus formation, with venous more than arterial events. | MED-C17-03 |
| The SLE complications note lists accelerated atherosclerosis, glomerular disease (class III/IV lupus nephritis), complications of immunosuppression, vasculitis of medium vessels (GIT/CNS) and APS. | MED-C17-04 |
| APS: 50% of cases are primary, associated with HLA DR4 and HLA DRw53; 50% or more are secondary, most commonly due to SLE (one-third of APS). | MED-C17-05 |
| The side note states the most common cause of secondary Sjogren is RA and that HLA DR3 positivity is associated with Sjogren syndrome and SLE. | MED-C17-06 |
| Antibodies are directed against phospholipid-binding proteins: beta-2 glycoprotein I, the prothrombin-phosphatidylserine complex and annexin, with platelet surface proteins shown alongside. | MED-C17-07 |
| The pathway ends in thrombocytopenia (50,000 to one lakh) with an increased propensity to thrombosis. | MED-C17-08 |
| The diagram shows the Ag-Ab complex with increased affinity for platelets, activation of the complement cascade, thrombocytopenia with a raised thrombotic tendency, and reduced inhibition of coagulation factors progressing to thrombosis. | MED-C17-09 |

Unasked points: **none found**.

### Book p467 / 01 PDF103

| Printed point / call-out | Question |
|---|---|
| The two hits are the antibody causing endothelial injury and a second hit such as oestrogen, smoking, obesity or other prothrombotic states. | MED-C17-10 |
| The most common cause of thrombophilia is acquired (APS), greater than inherited factor V Leiden mutation. | MED-C17-11 |
| Thrombosis: DVT is more common than arterial thrombosis (stroke), which is more common than Budd-Chiari syndrome. | MED-C17-12 |
| Veins involved: hepatic vein gives Budd-Chiari syndrome and cerebral veins give cerebral venous thrombosis. | MED-C17-13 |
| Microvascular involvement affects the kidneys more than the adrenals. | MED-C17-14 |
| Sneddon's syndrome is listed with livedo reticularis and stroke in the APS clinical-features block. | MED-C17-15 |
| The note gives the differential for hepatic vein thrombosis as APS, polycythemia rubra vera and PNH (paroxysmal nocturnal haemoglobinuria). | MED-C17-16 |
| The note describes the stroke as acute in onset with cranial nerve palsy and a pyramidal pattern of weakness. | MED-C17-17 |
| Laboratory criteria: any antibody positive twice over 12 weeks. | MED-C17-18 |
| Anti-beta-2 glycoprotein I (IgG/IgM) is detected by ELISA. | MED-C17-19 |
| Anti-cardiolipin antibody (IgG/IgM >40 units) is described as sensitive. | MED-C17-20 |
| Lupus anticoagulant is specific but not sensitive, with a raised aPTT and a raised dRVVT (diluted Russell's viper venom test). | MED-C17-21 |

Unasked points: **none found**.

### Book p468 / 02 PDF1

| Printed point / call-out | Question |
|---|---|
| Clinical criteria: a vascular event due to venous or arterial thrombosis. | MED-C17-22 |
| Pregnancy criteria: one miscarriage ≥10 weeks, or ≥3 miscarriages before 10 weeks, or premature delivery <34 weeks of a morphologically normal neonate due to pre-eclampsia, eclampsia or HELLP syndrome. | MED-C17-23 |
| The note states APS is the most common cause of second-trimester abortion (after 10 weeks). | MED-C17-24 |
| Non-criteria APS: CNS shows chorea, epilepsy and migraine; cardiac shows Libman-Sacks endocarditis and MR. | MED-C17-25 |
| Hematological: warm-antibody autoimmune haemolytic anaemia and Evan's syndrome, with thrombocytopenia not significant enough to cause bleeding. | MED-C17-26 |
| Renal: APS nephropathy is a thrombotic microangiopathy due to microvascular involvement of the kidney. | MED-C17-27 |
| Endocrine: infarction of adrenal vessels leads to adrenal insufficiency (shock); dermatological: venous obstruction with venular dilatation gives livedo reticularis. | MED-C17-28 |

Unasked points: **none found**.

### Book p469 / 02 PDF2

| Printed point / call-out | Question |
|---|---|
| Domains: clinical domains 1-6 (macrovascular venous, macrovascular arterial, microvascular, obstetric, cardiac valve, haematology) and laboratory domains 7-8 (lupus anticoagulant test, other antibody tests). | MED-C17-29 |
| Catastrophic APS: three or more organ systems involved within one week, with small vessels involved; presentations include thrombotic microangiopathy of the kidney and adrenal insufficiency. | MED-C17-30 |
| Management: an asymptomatic adult requires no treatment. | MED-C17-31 |
| To attain an INR of 2.5-3: heparin 5000 units TDS SC or LMWH 60 mg BD SC, with warfarin overlapped with heparin/LMWH and continued lifelong; the note adds there is no role for NOACs. | MED-C17-32 |
| Pregnancy management: prophylactic low-dose aspirin with heparin throughout pregnancy and for 6-12 weeks post-partum; warfarin is continued lifelong if APS is diagnosed. | MED-C17-33 |
| Catastrophic APS is managed with steroids, IV Ig and plasmapheresis. | MED-C17-34 |
| The note states there is no role for new oral anticoagulants (NOACs) in APS. | MED-C17-35 |

Unasked points: **none found**.

### Book p470 / 02 PDF3

| Printed point / call-out | Question |
|---|---|
| The general-features diagram contrasts inflammation: SLE +++ versus SSc + with a low or normal ESR. | MED-C18-01 |
| SSc pathogenesis: fibrosis (with interstitial lung disease), vasculopathy from small-vessel endothelial injury with anti-endothelial antibody causing thrombosis, and immune-complex-mediated small-vessel vasculitis producing capillary hypoxia. | MED-C18-02 |
| Severe form: involvement of medium vessels (mesenteric and CNS vessels) with TGF-beta release acting on mesenchymal cells to produce myofibroblasts. | MED-C18-03 |
| Pulmonary arteriolar hypertension (class 1) is attached to the vasculopathy arm and marked as carrying a bad prognosis. | MED-C18-04 |
| Scleroderma is defined as thickening and induration. | MED-C18-05 |
| Local manifestations are localised scleroderma (morphoea, linear scleroderma); systemic manifestation is systemic sclerosis, subdivided by extent of skin involvement into diffuse and limited SSc. | MED-C18-06 |
| Diffuse SSc: skin lesion over all parts of the body, complications of ILD, pathogenesis of fibrosis plus vasculopathy with minimal inflammation. Limited SSc: skin distal to elbow and face, pulmonary hypertension, vasculopathy predominant. | MED-C18-07 |
| Scleroderma mimics: eosinophilic fasciitis with groove sign, and nephrogenic systemic fibrosis, which is drug induced after gadolinium contrast. | MED-C18-08 |

Unasked points: **none found**.

### Book p471 / 02 PDF4

| Printed point / call-out | Question |
|---|---|
| Etiology: orphan disease with unknown cause; age 35-50 years; F:M = 5:1. | MED-C18-09 |
| Immune susceptibility is listed as HLA DRB1/II (DR5) and viral associations are EBV, CMV and parvovirus B19. | MED-C18-10 |
| Agents inducing scleroderma: vinyl chloride, bleomycin, pentazocine, contaminated L-tryptophan and silica, with silica carrying the maximum association with SSc. | MED-C18-11 |
| The note pairs HLA DR-3 with SLE and Sjogren syndrome, DR-4 with APS and RA, DR-5 with SSc, and adds that silica is also associated with SLE. | MED-C18-12 |
| Very early systemic sclerosis: 3-5 years, with two-thirds of cases progressing to SSc. | MED-C18-13 |
| The triad pairs Raynaud's phenomenon and ANA positivity with the investigation nail-fold capillaroscopy. | MED-C18-14 |
| Raynaud's phenomenon is episodic vasoconstriction in response to stimuli; triggers listed are cold, stress and vibration. | MED-C18-15 |
| Clinical manifestations listed: pallor, cyanosis, redness on rewarming, pain and tightness of digits and a puffy hand. | MED-C18-16 |

Unasked points: **none found**.

### Book p472 / 02 PDF5

| Printed point / call-out | Question |
|---|---|
| Primary (Raynaud's disease): ANA negative, family history positive, symptoms self-limiting and symmetric, and other features listed as a good prognosis. | MED-C18-17 |
| Secondary Raynaud phenomenon: severe with critical limb ischaemia, ulcer and gangrene of the extremities, and associated diseases (SSc, Sjogren syndrome, MCTD and inflammatory muscle disease). | MED-C18-18 |
| Nail-fold capillaroscopy in secondary disease: dropout of capillaries, dilated tortuous capillaries and microhaemorrhages; the primary column is normal. | MED-C18-19 |
| Limited SSc: ANA pattern centromere with anti-centromere antibody; diffuse SSc: fine speckled with anti-topoisomerase and anti-RNA polymerase III. | MED-C18-20 |
| Raynaud phenomenon: limited SSc is long standing and severe (due to predominant vasculopathy) with critical limb ischaemia present; diffuse SSc is short lasting and less severe (due to predominant fibrosis) with critical limb ischaemia not extensive. | MED-C18-21 |
| Diffuse SSc: anti-topoisomerase and anti-RNA polymerase III, with a fine-speckled ANA pattern. | MED-C18-22 |

Unasked points: **none found**.

### Book p473 / 02 PDF6

| Printed point / call-out | Question |
|---|---|
| CREST: C is calcinosis of the tissues; E is oesophagitis, marked limited much greater than diffuse. | MED-C18-23 |
| CREST: R is Raynaud's phenomenon, S is sclerodactyly (scleroderma of fingers) and T is telangiectasia, with minimal fibrosis noted for limited disease. | MED-C18-24 |
| Pulmonary artery hypertension is asymptomatic with normal FEV1, FVC and FEV1/FVC but a reduced DLCO. | MED-C18-25 |
| Pulmonary artery hypertension: poor prognosis due to increased mortality. | MED-C18-26 |
| Features against limited SSc: extensive fibrosis, ILD, cardiac involvement and renal involvement. | MED-C18-27 |
| Skin manifestations: dry tight skin, facial hypo- and hyperpigmentation (salt-and-pepper appearance), hair loss, intense itching, and progression to face tightening with microstomia, pursed lip, puckered mouth and mask facies. | MED-C18-28 |
| Diffuse SSc skin manifestations include bilateral symmetrical skin thickening. | MED-C18-29 |

Unasked points: **none found**.

### Book p474 / 02 PDF7

| Printed point / call-out | Question |
|---|---|
| Joint manifestations: diffuse SSc shows arthritis/myositis due to inflammation; limited SSc shows acral osteolysis (falling off of fingers) with diffuse severe Raynaud's phenomenon. | MED-C18-30 |
| Other manifestations include acral osteolysis, attributed to fibrosis or vasculopathy. | MED-C18-31 |
| Oesophageal hypomotility progresses to small-intestinal bacterial overgrowth and pneumatosis intestinalis. | MED-C18-32 |
| The watermelon-stomach image is labelled as seen on upper GI endoscopy. | MED-C18-33 |
| Disease progression: pulmonary manifestations leading to interstitial lung disease, which is the most common cause of death; cardiac and renal manifestations are also listed. | MED-C18-34 |
| Anti-centromere is limited-type SSc with CREST syndrome and pulmonary hypertension as the complication. | MED-C18-35 |
| Anti-RNA polymerase III (diffuse) is linked to scleroderma renal crisis, more than anti-topoisomerase, and to malignancy of lung and breast. | MED-C18-36 |
| Anti-topoisomerase-1 (anti-Scl-70), diffuse: renal TMA progressing to scleroderma renal crisis, lung ILD, tendon friction rubs on passive movement (diffuse more than limited), GAVE (watermelon stomach) and rapidly progressive skin involvement with joint contractures and tendon friction rubs. | MED-C18-37 |
| The antibody table lists anti-PM/Scl-70 in overlap disease with ILD positive and anti-Ku in overlap disease with no ILD. | MED-C18-38 |

Unasked points: **none found**.

### Book p475 / 02 PDF8

| Printed point / call-out | Question |
|---|---|
| Renal disease in diffuse SSc presents within the first 4 years, affects small vessels of the kidney and is a thrombotic microangiopathy. | MED-C18-39 |
| Thrombotic microangiopathy: accelerated hypertension plus microangiopathic haemolytic anaemia plus thrombocytopenia. | MED-C18-40 |
| Rx for scleroderma renal crisis: ACE inhibitors, described as the drug of choice. | MED-C18-41 |
| Phases of diffuse SSc: the oedematous phase, more common in diffuse disease and associated with non-pitting oedema, progresses to the fibrotic phase. | MED-C18-42 |
| Investigations: PFT for ILD shows DLCO markedly reduced and FRC reduced; the chest radiograph shows bilateral basal subpleural reticular infiltrates. | MED-C18-43 |

Unasked points: **none found**.

### Book p476 / 02 PDF9

| Printed point / call-out | Question |
|---|---|
| HRCT: IOC. Scleroderma: NSIP more than UIP. | MED-C18-44 |
| NSIP shows no destruction with ground-glass opacities and is treated with steroids and mycophenolate mofetil (better prognosis); UIP shows destruction with cystic changes, honeycombing and traction bronchiectasis with no treatment listed. | MED-C18-45 |
| The note attributes UIP to RA, LIP as characteristic of Sjogren's disease, and NSIP to others. | MED-C18-46 |
| Rx of RP: first line is a calcium-channel blocker, with or without a PDE-5 inhibitor (sildenafil). | MED-C18-47 |
| Second line for Raynaud phenomenon is bosentan, an endothelin antagonist. | MED-C18-48 |
| ILD: nintedanib plus MMF, and the source notes the disease is non-responsive to steroid. | MED-C18-49 |
| Treatment: skin is treated with mycophenolate mofetil, and joint plus muscle involvement with steroids and methotrexate; scleroderma renal crisis is treated with ACE inhibitors. | MED-C18-50 |

Unasked points: **none found**.

### Book p477 / 02 PDF10

| Printed point / call-out | Question |
|---|---|
| Definition: a multisystem autoimmune CTD characterised by mononuclear inflammation within skeletal muscle, with subacute muscle weakness and fatigue, lasting 6-8 weeks. | MED-C19-01 |
| Old classification: polymyositis, dermatomyositis, inclusion body myositis and immune-mediated necrotizing myopathy. | MED-C19-02 |
| Current classification opens with polymyositis, now an obsolete term, and then lists dermatomyositis, antisynthetase syndrome, necrotizing myopathies, juvenile DM, paraneoplastic myositis, inclusion body myositis and amyopathic DM. | MED-C19-03 |
| Criterion A: proximal and symmetrical muscle weakness of the pelvic and scapular girdle and anterior flexors of the neck, progressing for weeks to months, with or without dysphagia or involvement of respiratory muscles. | MED-C19-04 |
| Criterion B: elevation of serum levels of skeletal-muscle enzymes, namely creatine kinase, aspartate aminotransferase, lactate dehydrogenase and aldolase. | MED-C19-05 |
| Criterion C: EMG characteristic of myopathy with short and small motor units, fibrillation, positive sharp waves, insertional irritability and repetitive high-frequency firing. | MED-C19-06 |
| Criterion D: muscle biopsy showing necrosis, phagocytosis and inflammatory exudate. | MED-C19-07 |
| Typical cutaneous changes: heliotrope rash with periorbital oedema and violaceous erythema, and Gottron's sign with vasculitis in the elbow, metacarpophalangeal and proximal interphalangeal joints. | MED-C19-08 |
| Risk factors, genetic: HLA-DRB1-03 and HLA-DRB1-07. | MED-C19-09 |
| Environmental risk factors: UV B rays, Coxsackie and parvovirus B19 virus, and drugs including chloroquine, colchicine and statins. | MED-C19-10 |

Unasked points: **none found**.

### Book p478 / 02 PDF11

| Printed point / call-out | Question |
|---|---|
| The note lists 03 with SLE, Sjogren's and dermatomyositis, 04 with APS and RA, and 05 with scleroderma. | MED-C19-11 |
| Typical (55-60%): most commonly middle-aged; juvenile 5-15 years, adult 40-60 years, females more than males (2:1). | MED-C19-12 |
| Typical features: weakness that is bilateral and symmetrical, purely motor, proximal, autoimmune (acquired), persistent, with no significant pain and progressive motor weakness over weeks to months. | MED-C19-13 |
| Examination findings: bulk normal, power reduced, tone reduced, reflexes normal and sensory system intact. | MED-C19-14 |
| The note lists the muscle groups not involved in IMD as the extraocular muscles and the facial muscles. | MED-C19-15 |
| Atypical: 30% present with proximal pain and weakness with an acute-subacute onset, and 10% with chronic proximal plus distal weakness; the syndrome table gives the same 30 and 10 figures for the corresponding rows. | MED-C19-16 |
| The syndrome table lists insidious proximal and distal weakness over 1-10 years, contrasted with painless proximal weakness over 3-10 months and acute or subacute proximal pain and weakness over weeks to months. | MED-C19-17 |

Unasked points: **none found**.

### Book p479 / 02 PDF12

| Printed point / call-out | Question |
|---|---|
| Pathognomonic skin lesions: Gottron's papule (scaly erythematous flat-topped violaceous papule/plaque over the dorsal MCP, PIP and DIP) and heliotrope rash (violaceous periorbital oedema and erythema). | MED-C19-18 |
| Gottron's papule: scaly erythematous flat-topped violaceous papule/plaque on the dorsal surface of MCP, PIP and DIP joints. | MED-C19-19 |
| Heliotrope rash: violaceous periorbital oedema and erythema. | MED-C19-20 |
| Other skin lesions: Gottron rash/sign is macular erythema over Gottron's papule, typically on extensor surfaces, photosensitive, with linear erythema over the dorsum of the hand. | MED-C19-21 |
| V sign is located over the chest, shawl sign posteriorly over the back and holster sign is erythema on the lateral aspect of the thigh; scalp involvement is generally pruritic. | MED-C19-22 |
| Telangiectasia: nail-fold capillary involvement with periungual erythema or oedema, and cuticular hyperplasia also seen. | MED-C19-23 |
| Calcinosis cutis: also seen in CREST syndrome and in juvenile dermatomyositis, and due to deposition of calcium hydroxyapatite. | MED-C19-24 |

Unasked points: **none found**.

### Book p480 / 02 PDF13

| Printed point / call-out | Question |
|---|---|
| SLE rash: never involves the knuckles, may involve the nasolabial fold, associated with painless oral cavity ulcers and non-pruritic. Dermatomyositis rash: involves the knuckles (MCP joint), does not involve the nasolabial fold, not associated with oral cavity ulcers and pruritic. | MED-C19-25 |
| Mechanic's hand: not specific for dermatomyositis and part of the antisynthetase syndrome. | MED-C19-26 |
| Muscle biopsy is described as the gold standard test. | MED-C19-27 |
| Muscle biopsy shows a mononuclear lymphocytic infiltrate of CD4+ T cells and perifascicular atrophy. | MED-C19-28 |
| MRI: the STIR sequence shows hyperintense areas within muscle. | MED-C19-29 |
| EMG: polyphasic short-duration small-amplitude potentials, high-frequency discharges, and spontaneous fibrillation or denervation. | MED-C19-30 |
| Enzymes: CPK is greater than AST. | MED-C19-31 |
| Antibody associated: anti-Mi-2 alpha with good prognosis, low risk for ILD and responsiveness to conventional therapy (steroid plus MMF). | MED-C19-32 |

Unasked points: **none found**.

### Book p481 / 02 PDF14

| Printed point / call-out | Question |
|---|---|
| Age group: polymyositis only in adults; dermatomyositis seen in the elderly or juvenile. | MED-C19-33 |
| Skin changes are absent in polymyositis and present in dermatomyositis; calcinosis is rare in polymyositis and seen in dermatomyositis. Both share subacute onset, proximal symmetric weakness, systemic features and normal-to-high enzymes. | MED-C19-34 |
| Associated systemic conditions or overlap syndrome: yes for polymyositis, which never exists on its own, and yes for dermatomyositis, which can exist on its own. | MED-C19-35 |
| Biopsy findings: polymyositis shows CD8+ T-cell involvement while dermatomyositis shows CD4+ and B cells with perifascicular atrophy and perivascular inflammation. | MED-C19-36 |
| The antisynthetase syndrome block opens with the statement that it is treatable if diagnosed early. | MED-C19-37 |
| Antisynthetase syndrome clinical features: mechanic's hand, Raynaud's phenomenon, cardiomyopathy and an SLE-like arthritis (Jaccoud's arthropathy). | MED-C19-38 |
| Mechanic's hand is seen on the radial aspect of the index and middle finger and is characterised by crusted hyperkeratotic lesions. | MED-C19-39 |
| The note adds that Jaccoud's arthropathy is also seen in Sjogren's syndrome. | MED-C19-40 |
| Investigations: CXR shows fever with infiltrates, which can be mistaken for viral pneumonia and can progress into ILD; ILD can be the first presentation of the syndrome and is the most common cause of death. | MED-C19-41 |

Unasked points: **none found**.

### Book p482 / 02 PDF15

| Printed point / call-out | Question |
|---|---|
| ILD pattern: NSIP plus COP. NSIP is most common and identified by ground-glass opacities; COP is identified by consolidations. | MED-C19-42 |
| The note states UIP in the lung is identified by a honeycombing structure, that is destruction of the parenchyma. | MED-C19-43 |
| Amyopathic DM: poor prognosis and not treatable, with anti-MDA-5 antibody and a clinical triad featuring rapidly progressive ILD. | MED-C19-44 |
| Juvenile DM commonly affects girls aged 5-15 years and malignancy, cardiac involvement and ILD are absent. | MED-C19-45 |
| Juvenile DM antibodies are anti-NXP2 and anti-TIF1-gamma; if seen in adults they indicate cancer-associated myositis. | MED-C19-46 |
| Immune-mediated necrotizing DM: anti-SRP in severe disease with ILD and cardiac manifestations does not respond; anti-HMG-CoA reductase, seen with statin therapy, responds to steroid plus IVIG plus rituximab (rarely). | MED-C19-47 |

Unasked points: **none found**.

### Book p483 / 02 PDF16

| Printed point / call-out | Question |
|---|---|
| IBM: most common in the elderly (males more than females), presenting with recurrent falls and a chronic presentation. | MED-C19-48 |
| IBM weakness is asymmetrical, proximal plus distal, and involves the quadriceps, vastus and finger flexors. | MED-C19-49 |
| IBM histology shows red-rimmed vacuoles and the disease is steroid unresponsive. | MED-C19-50 |
| Cancers associated with DM: carcinoma ovary is characteristic and carcinoma lung is the most common. | MED-C19-51 |
| Antibodies specific to IMDs: dermatomyositis with anti-Mi-2 alpha, antisynthetase syndrome with anti-Jo-1, necrotizing myopathy with anti-SRP and anti-HMG-CoA reductase, amyopathic DM with anti-MDA-5, and juvenile DM and cancer-associated myositis with anti-NXP2 and anti-TIF1-gamma. | MED-C19-52 |
| Other associated antibodies: anti-Ro; anti-Ku, which may develop ILD; and anti-PM/Scl, seen in polymyositis with scleroderma with or without ILD and showing an ANA nucleolar pattern. | MED-C19-53 |
| Both juvenile DM and cancer-associated myositis are listed with anti-NXP2 and anti-TIF1-gamma. | MED-C19-54 |
| Treatment: the goal is clinical elimination of all disease activity; first line is steroid plus MTX or steroid plus MMF. | MED-C19-55 |
| Second-line treatment: rituximab and JAK inhibitors (tofacitinib). | MED-C19-56 |
| The treatment goal is clinical elimination of all disease activity. | MED-C19-57 |

Unasked points: **none found**.

### Book p484 / 02 PDF17

| Printed point / call-out | Question |
|---|---|
| Sarcoidosis is defined as a chronic, multisystem, granulomatous, immunological disorder; biopsy usually shows non-caseating granulomas. | MED-C20-01 |
| Biopsy usually shows non-caseating granulomas, but caseating granulomas can occur in one-third of cases. | MED-C20-02 |
| Outcome: 50% spontaneous resolution, 25% become chronic (mostly the lung is affected) and 5% mortality, attributed to interstitial lung disease and infections. | MED-C20-03 |
| Diseases that can have non-caseating granulomas: 30% of TB cases, lymphoma, berylliosis, hypersensitivity pneumonitis (HP), Crohn's disease and cat-scratch disease. | MED-C20-04 |
| ACR criteria: compatible clinical picture, histological non-caseating granulomas and exclusion of other causes. | MED-C20-05 |
| Classification: acute sarcoidosis is represented by Lofgren syndrome and chronic sarcoidosis by Heerfordt syndrome; hilar adenopathy is the important finding. | MED-C20-06 |
| Major manifestations: lung (ILD) more than skin more than eyes more than joints; multisystem manifestations include cardiac and renal disease, and the only organ spared is the testes. | MED-C20-07 |
| Risk factors: Propionibacterium acnes infection and excessive firewood burning. | MED-C20-08 |

Unasked points: **none found**.

### Book p485 / 02 PDF18

| Printed point / call-out | Question |
|---|---|
| HLA DRB1*03 is associated with Lofgren syndrome and a good prognosis. | MED-C20-09 |
| HLA DRB1*04 has a protective role, while HLA DRB1*11 is associated with CNS and cardiac sarcoidosis, which carries a bad prognosis. | MED-C20-10 |
| The note repeats: HLA DRB1*03 with SLE, Sjogren syndrome and dermatomyositis; DRB1*04 with APS and RA; DRB1*05 with scleroderma. | MED-C20-11 |
| Immune paradox/anergy: lymphopenia in blood leading to increased risk of infection, and a Mantoux test that is false negative because of low lymphocytes. | MED-C20-12 |
| The note states HIV positivity leads to lymphopenia and a reduced risk of sarcoidosis. | MED-C20-13 |
| Lofgren syndrome is drawn with erythema nodosum, arthritis and hilar adenopathy. | MED-C20-14 |
| Erythema nodosum in Lofgren syndrome is described with the 3 P's: painful, pretibial, papule. | MED-C20-15 |
| Arthritis/tenosynovitis is acute, involves the ankle joint, is bilateral and symmetrical and is seen in the young. | MED-C20-16 |

Unasked points: **none found**.

### Book p486 / 02 PDF19

| Printed point / call-out | Question |
|---|---|
| In Behcet's disease, erythema nodosum has 4 P's: painful, pretibial, papules with pigmentation. | MED-C20-17 |
| Hilar adenopathy is described as the most consistent feature and is generally bilateral, with right paratracheal and left hilar nodes shown. | MED-C20-18 |
| Heerfordt-Waldenstrom syndrome: uveitis, bilateral LMN seventh-nerve palsy and parotitis. | MED-C20-19 |
| Uveitis: any type or compartment, acute anterior uveitis more common, and the most common ocular manifestation of sarcoid. | MED-C20-20 |
| Bilateral LMN seventh-nerve palsy is the most common neurological manifestation in sarcoid; the note pairs it with Guillain-Barre syndrome as its main differential. | MED-C20-21 |
| Clinical paradox: it helps identify chronicity, because as the lung disease worsens the nodal enlargement regresses. | MED-C20-22 |
| Stages: 1 bilateral hilar lymphadenopathy with nodal enlargement only, 2 nodal enlargement plus parenchymal disease (node size starts to fall as infiltrate rises), 3 parenchymal disease only, 4 fibrosis. | MED-C20-23 |

Unasked points: **none found**.

### Book p487 / 02 PDF20

| Printed point / call-out | Question |
|---|---|
| Fibrosis pattern: thickening of bronchovascular bundles and traction bronchiectasis of the upper lobe; upper-lobe fibrosis is also listed for ankylosing spondylitis and sarcoidosis. | MED-C20-24 |
| Lupus pernio: violaceous or erythematous, indurated, infiltrative plaques on the central face that are less responsive to treatment; bone changes (lytic or cystic) are also associated. | MED-C20-25 |
| Eye involvement: chronic bilateral panuveitis is the most common manifestation. | MED-C20-26 |
| Features unlikely of sarcoidosis: pleural involvement and a UIP-like pattern with honeycombing and parenchymal destruction in the lung; episcleritis, scleritis and sicca in the eye. | MED-C20-27 |
| The note lists episcleritis, scleritis and sicca as ocular features unlikely of sarcoidosis. | MED-C20-28 |

Unasked points: **none found**.

### Book p488 / 02 PDF21

| Printed point / call-out | Question |
|---|---|
| Endocrine manifestation: hypercalcaemia. | MED-C20-29 |
| CNS: bilateral LMN seventh-nerve palsy (most common), neurosarcoidosis with a pituitary mass causing stalk effect and central diabetes insipidus, basilar meningitis and acute transverse myelitis. | MED-C20-30 |
| CVS: dilated cardiomyopathy more than restrictive cardiomyopathy, and AV blocks. | MED-C20-31 |
| Hematology: pancytopenia with splenomegaly. | MED-C20-32 |
| Renal: AKI is hypercalcaemia-induced pre-renal failure, CKD is chronic tubulointerstitial disease (CTID) and the glomerulus is rarely affected, with membranous nephropathy. | MED-C20-33 |
| The note lists rheumatological disorders causing CTID as Sjogren's syndrome, IgG4-related disease and sarcoidosis. | MED-C20-34 |
| Investigations: gallium-67 scintigraphy (panda sign) and PET scan, which is the investigation of choice to identify nodes to take a biopsy from. | MED-C20-35 |
| Blood markers: angiotensin-converting enzyme (if normal, sarcoidosis can be ruled out) and soluble interleukin-2 (sIL-2) receptor. | MED-C20-36 |
| Bronchoalveolar lavage is listed with a raised CD4/CD8 ratio above the cut-off printed on the page. | MED-C20-37 |

Unasked points: **none found**.

### Book p489 / 02 PDF22

| Printed point / call-out | Question |
|---|---|
| Treatment: acute sarcoidosis requires no treatment; chronic disease is treated in steps. | MED-C20-38 |
| Chronic: first line steroids, second line methotrexate and azathioprine, third line anti-TNF-alpha (adalimumab). | MED-C20-39 |
| Therapeutic paradox: in a patient treated with TNF-alpha (adalimumab), skin lesions similar to sarcoidosis can appear, and they disappear on reducing the dose. | MED-C20-40 |
| Overlap syndrome: features of two or more out of the six autoimmune systemic connective tissue diseases. | MED-C20-41 |
| The overlap list is Sjogren syndrome (most common, most having anti-Ro antibody), SLE, polymyositis, dermatomyositis, systemic sclerosis and rheumatoid arthritis. | MED-C20-42 |
| The source states that treatment is based on the predominant disease in the overlap. | MED-C20-43 |
| Undifferentiated CTD: patients presenting with some features of CTD who do not fulfil the criteria to be classified under a disease. | MED-C20-44 |
| MCTD is introduced as a specific type of overlap syndrome, with patients presenting unique features, in middle-aged females (female:male about 15:1). | MED-C20-45 |
| Serology: ANA positive in 100% with a coarse speckled pattern and anti-U1 RNP antibody positive. | MED-C20-46 |

Unasked points: **none found**.

### Book p490 / 02 PDF23

| Printed point / call-out | Question |
|---|---|
| Clinical features: Raynaud's phenomenon is the most common manifestation, followed by oedema of hands, nail pitting, acrosclerosis, myositis and erosive synovitis. | MED-C20-47 |
| Acrosclerosis is defined as Raynaud's phenomenon plus MCTD plus the systemic-sclerosis features of the hand. | MED-C20-48 |
| Clinical features note that the CNS and renal system are usually spared in MCTD. | MED-C20-49 |
| HLA association for MCTD: HLA DRB1*04. | MED-C20-50 |
| Complications: ILD is the most common, and about 20% evolve into limited SSc with pulmonary artery hypertension, which is the most common cause of death. | MED-C20-51 |
| The capillaroscopy panel in RP shows normal, dilated, tortuous, bushy and meandering capillaries with microhaemorrhage. | MED-C20-52 |

Unasked points: **none found**.

### Book p491 / 02 PDF24

| Printed point / call-out | Question |
|---|---|
| Vasculitis is defined as vessel-wall inflammation, with raised ESR/CRP and ischemia or organ damage. | MED-C21-01 |
| The page explicitly notes no gold standard test to diagnose vasculitis and no diagnostic criteria. | MED-C21-02 |
| The vasculopathy note uses systemic sclerosis as the example and lists endothelial injury through TGF-beta fibrosis with low ESR/CRP. | MED-C21-03 |
| The classification criteria are the revised Chapel Hill consensus 2012 classification and are based on predominantly affected vessel size. | MED-C21-04 |
| Large vessels are the aorta and its branches, with temporal/giant-cell arteritis and Takayasu arteritis listed. | MED-C21-05 |
| The ANCA-associated list contains GPA, allergic/eosinophilic GPA and microscopic polyangiitis. | MED-C21-06 |
| The immune-complex mediated list includes anti-GBM disease, HSP and cryoglobulinemia-associated vasculitis. | MED-C21-07 |

Unasked points: **none found**.

### Book p492 / 02 PDF25

| Printed point / call-out | Question |
|---|---|
| HUV is marked by anti-C1q antibody, SLE-overlap features and pathognomonic interface dermatitis. | MED-C21-08 |
| The margin note states most common vasculitis: adults temporal/giant-cell arteritis worldwide, children HSP. | MED-C21-09 |
| Variable vessel vasculitis consists of Behcet disease and Cogan syndrome in the printed list. | MED-C21-10 |
| Single-organ vasculitis examples list skin capillaries/post-capillary venules as cutaneous leukocytoclastic angiitis. | MED-C21-11 |
| Among CTD-associated exceptions, RA and Sjogren are bracketed with medium-vessel vasculitis. | MED-C21-12 |
| Drug-induced ANCA-associated vasculitis lists hydralazine and propylthiouracil, while penicillins, sulfonamides and thiazides are immune-complex mediated. | MED-C21-13 |
| The infection list pairs HCV with cryoglobulinemia-like vasculitis and HBV with PAN-like disease. | MED-C21-14 |

Unasked points: **none found**.

### Book p493 / 02 PDF26

| Printed point / call-out | Question |
|---|---|
| Malignancy-related vasculitis is noted to involve small vessels and is associated with lymphoma, hairy-cell leukemia, bladder carcinoma and RCC. | MED-C21-15 |
| Both large-vessel diseases have similar histology: transmural inflammation involving intima/media/adventitia, lymphocytes/macrophages, granuloma and few giant cells, seen in 50% cases. | MED-C21-16 |
| GCA synonyms are temporal arteritis, cranial arteritis and granulomatous arteritis; vessels are extracranial vessels with internal elastic lamina, sparing intracranial vessels. | MED-C21-17 |
| GCA presents after 50 years, mean age of diagnosis is 72 years and the female:male ratio is 2:1. | MED-C21-18 |
| The most common artery sequence in GCA is superficial temporal, then vertebral, ophthalmic and posterior ciliary. | MED-C21-19 |
| The GCA-PMR syndrome note states PMR symptoms occur in 50% of GCA cases and GCA symptoms occur in 20% of PMR cases. | MED-C21-20 |

Unasked points: **none found**.

### Book p494 / 02 PDF27

| Printed point / call-out | Question |
|---|---|
| PMR features are tendinitis/bursitis/enthesitis with early morning pain and stiffness in shoulder, hip and pelvic girdle, ESR >50, and differential diagnosis is late-onset RA. | MED-C21-21 |
| PMR pathology is listed as IL-6 predominant inflammation type and IFN-gamma mediated ischemia type. | MED-C21-22 |
| Associations include smoking, VZV isolated from biopsy with no role of acyclovir, and genetic HLA DRB1-04/MICA A5 allele. | MED-C21-23 |
| Typical GCA headache is new onset, moderate-severe, recurring, unusual type and boring in nature. | MED-C21-24 |
| The clinical-features page prints ESR >100 mm/hr and notes ACR >50 mm/hr. | MED-C21-25 |
| Jaw claudication due to maxillary artery involvement, along with ophthalmoplegia, is noted as 100% positive predictive value for GCA. | MED-C21-26 |

Unasked points: **none found**.

### Book p495 / 02 PDF28

| Printed point / call-out | Question |
|---|---|
| Atypical GCA includes pyrexia of unknown origin in age over 50 years, cervical radiculopathy and recurrent throat pain/cough. | MED-C21-27 |
| Temporal artery biopsy is the investigation of choice, and a 4–6 cm long segment is taken to overcome skip lesions. | MED-C21-28 |
| Color Doppler is listed with 70% sensitivity and 80% specificity; the halo sign is a hypoechoic area around the temporal artery in longitudinal and transverse sections. | MED-C21-29 |
| ACR criteria shown are onset age >50, new localized headache, temporal artery tenderness or decreased pulsations, ESR ≥50 mm/hr and biopsy with transmural inflammation. | MED-C21-30 |
| Treatment lists steroids as first line, 40–60 mg/day or 1 mg/kg/day, tapered down. | MED-C21-31 |
| Tocilizumab is anti-IL-6 and is indicated for flares, especially common at low-dose steroids with increased ESR. | MED-C21-32 |

Unasked points: **none found**.

### Book p496 / 02 PDF29

| Printed point / call-out | Question |
|---|---|
| Takayasu synonyms listed are aortic arch syndrome, nonspecific aortoarteritis, occlusive thromboaortopathy, pulseless disease and middle aortic syndrome. | MED-C21-33 |
| Takayasu arteritis presents before 40 years, mean age of diagnosis 24 years, with female:male ratio 9:1. | MED-C21-34 |
| The 9:1 note lists Sjogren, SLE, Takayasu, fibromyalgia, chronic fatigue syndrome and primary biliary cirrhosis. | MED-C21-35 |
| The note lists pulmonary artery involvement in Takayasu arteritis and Behcet disease. | MED-C21-36 |
| Takayasu pathology includes HLA-B52/B67, TLR expression differing by vessel, segmental stenosis more than aneurysm and subclavian artery as the most common vessel. | MED-C21-37 |
| Takayasu clinical features include upper-extremity claudication, pulse inequality, unequal arm BP >10 mmHg and abdominal/carotid/aortic/femoral bruits. | MED-C21-38 |

Unasked points: **none found**.

### Book p497 / 02 PDF30

| Printed point / call-out | Question |
|---|---|
| Takayasu ACR criteria include onset <40 years, limb claudication, decreased brachial artery pulse, unequal arm BP >10 mmHg, subclavian/aortic bruit and angiographic stenosis. | MED-C21-39 |
| MR angiography is IOC for diagnosis and follow-up and gives the best measure of vessel wall thickness. | MED-C21-40 |
| Conventional angiography is marked gold standard and done if vessel intervention is planned. | MED-C21-41 |

Unasked points: **none found**.

### Book p498 / 02 PDF31

| Printed point / call-out | Question |
|---|---|
| Treatment lists steroids as DOC, tocilizumab and percutaneous transluminal renal angiogram with stenting. | MED-C21-42 |
| Takayasu shows F:M 9:1, age <40 years, average onset 25 years and Asian highest incidence; temporal arteritis has visual loss 10–30%, average age 72 and Scandinavian incidence. | MED-C21-43 |
| Temporal arteritis has visual loss 10–30%, one-third aorta/major branch involvement, rare renal HTN/claudication and rare need for surgical intervention. | MED-C21-44 |

Unasked points: **none found**.

### Book p499 / 02 PDF32

| Printed point / call-out | Question |
|---|---|
| Small-vessel vasculitis is split into immune-complex mediated and ANCA-associated; ANCA-associated examples are GPA, MPA and allergic/eosinophilic GPA. | MED-C22-01 |
| ANCA targets are in azurophilic granules of resting neutrophils more than lysosomes of monocytes and include PR3 and MPO. | MED-C22-02 |
| The ANCA pathogenesis flowchart starts with infection/LPS, primes neutrophils to express PR3/MPO and proceeds through ANCA, alternate complement activation, degranulation and NETosis. | MED-C22-03 |
| NETosis forms neutrophil extracellular traps; ineffective degradation exposes NET components, stimulates ANCA production and attacks primed neutrophils. | MED-C22-04 |

Unasked points: **none found**.

### Book p500 / 02 PDF33

| Printed point / call-out | Question |
|---|---|
| The ANCA screening test shown is indirect immunofluorescence. | MED-C22-05 |
| The cytoplasmic pattern is anti-PR3; confirmation is by ELISA, producing true c-ANCA positivity. | MED-C22-06 |
| True c-ANCA causes are ordered GPA > MPA > renal-limited vasculitis > EGPA. | MED-C22-07 |
| True p-ANCA against MPO is ordered renal-limited vasculitis > MPA > EGPA > GPA and includes drug-induced hydralazine, PTU, levamisole-adulterated cocaine and minocycline. | MED-C22-08 |
| False p-ANCA causes include autoimmune hepatitis type 1, primary sclerosing cholangitis, RA, IBD, infective endocarditis and cystic fibrosis. | MED-C22-09 |
| Biopsy and immunofluorescence of skin are marked most preferred; no deposits indicate pauci-immune disease. | MED-C22-10 |

Unasked points: **none found**.

### Book p501 / 02 PDF34

| Printed point / call-out | Question |
|---|---|
| ANCA cutaneous palpable purpura is labelled non-thrombocytopenic palpable purpura and hallmark feature. | MED-C22-11 |
| Petechiae are described as non-blanchable pinpoint macules due to capillary inflammation. | MED-C22-12 |
| Small-vessel involvement is capillaries and post-capillary venules in superficial capillary dermis with purpura, petechiae, bulla and urticaria. | MED-C22-13 |
| Medium-vessel vasculitis involves muscular arteries in the reticular dermis and features nodules, gangrene, mononeuritis multiplex and deep ulcers. | MED-C22-14 |
| The page states ANCA titres are a predictor of relapse. | MED-C22-15 |
| GPA features include necrotising vasculitis plus fibrinoid necrosis due to neutrophils plus granuloma. | MED-C22-16 |
| GPA lists c-ANCA 70% > p-ANCA 25%, age group >40 years, sex M=F and HLA DPB1 04. | MED-C22-17 |

Unasked points: **none found**.

### Book p502 / 02 PDF35

| Printed point / call-out | Question |
|---|---|
| GPA major manifestations list upper respiratory tract involvement in 95% with midline nasal deformities, including septal ulcers/crusting/perforation and saddle nose deformity. | MED-C22-18 |
| Lower respiratory involvement in GPA is 90%, with thick-walled cavitating nodules and DAH. | MED-C22-19 |
| Renal involvement in GPA is 60%; RPGN is type 3 and pauci-immune. | MED-C22-20 |
| GPA minor systemic manifestations include joints arthralgia, CNS peripheral neuropathy, skin palpable purpura and ocular scleritis, orbital pseudotumour and rare lacrimal involvement. | MED-C22-21 |

Unasked points: **none found**.

### Book p503 / 02 PDF36

| Printed point / call-out | Question |
|---|---|
| The note lists thick-walled cavitating nodules in Wegener granulomatosis, SCC of lung, histoplasmosis and lung abscess. | MED-C22-22 |
| MPA is described in elderly 50–65 years, male>female, necrotising vasculitis with fibrinoid necrosis but no granuloma, and p-ANCA > c-ANCA. | MED-C22-23 |
| MPA lists lower respiratory 50% DAH, upper respiratory 30% sinusitis and renal 100%, most commonly RPGN type 3. | MED-C22-24 |
| MPA minor manifestations are ocular unlikely, joints not significant, skin more common than GPA and CNS minimal neuropathy. | MED-C22-25 |

Unasked points: **none found**.

### Book p504 / 02 PDF37

| Printed point / call-out | Question |
|---|---|
| Induction shows methylprednisolone IV 500 mg–1 g for 3 days, then oral 1 mg/kg/day tapering over 2–3 months to 5 mg/day, plus cyclophosphamide as DOC. | MED-C22-26 |
| Rituximab is shown as an alternative if unwilling for cyclophosphamide and is used in relapse. | MED-C22-27 |
| Minimal disease is treated with steroid plus methotrexate; maintenance is low-dose steroid plus azathioprine. | MED-C22-28 |
| Plasma exchange indications are ongoing DAH, serum creatinine >5.5 mg/dL and CNS involvement. | MED-C22-29 |
| In the GPA table, cANCA or anti-PR3 ANCA positive scores +5, higher than +3 or +2 items. | MED-C22-30 |

Unasked points: **none found**.

### Book p505 / 02 PDF38

| Printed point / call-out | Question |
|---|---|
| For GPA, total score of ≥5 is needed, with sensitivity 93% and specificity 94%. | MED-C22-31 |
| The MPA table assigns eosinophil count ≥1×10^9/L a score of -4; pANCA/MPO is +6, pauci-immune GN +3 and fibrosis/ILD +3. | MED-C22-32 |
| Churg-Strauss syndrome is AKA eosinophilic granulomatosis with polyangiitis and allergic granulomatosis with polyangiitis. | MED-C22-33 |
| EGPA features include necrotising vasculitis, fibrinoid necrosis, extravascular granuloma, eosinophilic disease and predominantly ANCA-negative status; ANCA positivity is bad prognosis. | MED-C22-34 |
| The asthmatic phase is seen in adolescents and includes recurrent allergic rhinitis plus asthma and migratory lung infiltrations in CXR. | MED-C22-35 |
| The vasculitic phase includes eosinophilic gastroenteritis, eosinophilic myocarditis as the most common cause of death, and severe neuropathy including cranial nerves. | MED-C22-36 |
| High-titre ANCA-positive cases have DAH, RPGN, mononeuritis multiplex that may involve medium vessels, predominant skin lesions and bad prognosis. | MED-C22-37 |

Unasked points: **none found**.

### Book p506 / 02 PDF39

| Printed point / call-out | Question |
|---|---|
| ACR criteria for EGPA are asthma, eosinophilia >10%, mono/polyneuropathy, migratory pulmonary infiltrates, paranasal sinus abnormality and extravascular eosinophils on biopsy. | MED-C22-38 |
| EGPA treatment lists steroid plus IL-5 antagonist mepolizumab. | MED-C22-39 |
| PAN is described as transmural necrotising inflammation without granuloma, neutrophil predominant, focal and segmental necrosis and ANCA negative. | MED-C22-40 |
| The PAN association note states Hepatitis B 30/1 rule: 30% of PAN cases have hepatitis B and 1% of hepatitis B cases have PAN. | MED-C22-41 |
| Aneurysms/microaneurysms in PAN are linked to conventional angiography as the investigation. | MED-C22-42 |
| PAN systemic manifestations include constitutional symptoms as first symptom, nodules/ulcers/gangrene, hemoptysis, renal failure from renal artery stenosis with abdominal pain, testicular pain and mononeuritis multiplex. | MED-C22-43 |

Unasked points: **none found**.

### Book p507 / 02 PDF40

| Printed point / call-out | Question |
|---|---|
| PAN danger signs are abdominal pain due to mesenteric vasculitis, renal artery stenosis and CNS vasculitis. | MED-C22-44 |
| Findings against PAN due to capillary involvement include DAH, RPGN, petechiae, purpura, bulla, ecchymosis, ENT/ocular manifestations, asthma, positive ANCA and cryoglobulinemia. | MED-C22-45 |
| ACR criteria for PAN include weight loss >4 kg, livedo reticularis, testicular pain/tenderness, mono/polyneuropathy, diastolic BP >90, elevated BUN/creatinine, HBV, arteriographic abnormality and polymorphonuclear neutrophils on biopsy. | MED-C22-46 |
| Cutaneous PAN involves small arteries/arterioles, spares venules and is non-progressive. | MED-C22-47 |
| PAN investigation lists MR angiogram as first investigation and conventional angiography as DOC. | MED-C22-48 |
| The note states ADA-2 deficiency in children resembles PAN. | MED-C22-49 |

Unasked points: **none found**.

### Book p508 / 02 PDF41

| Printed point / call-out | Question |
|---|---|
| The treatment flowchart gives hepatitis B positive as steroid, antiviral and plasma exchange with good prognosis, and negative as steroid plus cyclophosphamide with poor prognosis. | MED-C22-50 |
| The table comments note asthma and eosinophilia in CSS and peripheral nervous system involvement often prominent in CSS. | MED-C22-51 |
| The differential table shows WG with high pulmonary infiltrates/nodules, alveolar hemorrhage, glomerulonephritis and upper airway disease; the comment says ENT disease usually favors WG. | MED-C22-52 |

Unasked points: **none found**.

### Book p509 / 02 PDF42

| Printed point / call-out | Question |
|---|---|
| The comparison table shows ANCA vasculitis is ANCA positive with immune-complex deposits negative, while immune-complex mediated vasculitis is ANCA negative with deposits present. | MED-C23-01 |
| The immune-complex mediated biopsy row lists leukocytoclasis with fragmented neutrophils/neutrophilic debris. | MED-C23-02 |
| Primary immune-complex mediated small-vessel vasculitis list includes HSP, CAV, HUV with anti-C1q positivity and Goodpasture syndrome. | MED-C23-03 |
| Secondary immune-complex mediated vasculitis is listed under SLE, RA, drugs and infections. | MED-C23-04 |
| Single-organ vasculitis is cutaneous leukocytoclastic angiitis, involving only skin and AKA hypersensitive vasculitis. | MED-C23-05 |

Unasked points: **none found**.

### Book p510 / 02 PDF43

| Printed point / call-out | Question |
|---|---|
| The pathogenesis diagram shows small immune complexes not effectively cleared by RES, leading to complement activation and neutrophil recruitment in small vessels of superficial capillary dermis. | MED-C23-06 |
| Cutaneous palpable purpura is explicitly labelled the most characteristic skin lesion. | MED-C23-07 |
| The HSP section states AKA IgA vasculitis. | MED-C23-08 |
| HSP is most common in children around 5 years, boys; non-thrombocytopenic palpable purpura in a child is HSP unless proven otherwise, symmetrical on extensor lower limbs especially buttocks and occurring in crops. | MED-C23-09 |

Unasked points: **none found**.

### Book p511 / 02 PDF44

| Printed point / call-out | Question |
|---|---|
| Joint involvement occurs in 70%, 15% initially present with joint symptoms, and features are KLNNO: knee predominant, large joint, migratory, non-deforming oligoarthritis. | MED-C23-10 |
| GIT involvement is 50%; complications include hemorrhage, bowel ischemia, scrotal swelling and intussusception, specifically ileoileal as most dangerous. | MED-C23-11 |
| HSP renal involvement is 20–50%, with asymptomatic microhematuria; adults can have type 2 RPGN, ESRD risk and high relapse rate. | MED-C23-12 |
| ACR criteria shown are palpable purpura, age at onset <20 years, bowel angina and biopsy with vessel wall granulocytes. | MED-C23-13 |
| Treatment is supportive care because HSP is self-limiting with no disease/recurrence treatment; steroids are for severe joint/GIT symptoms or adult HSP with RPGN. | MED-C23-14 |

Unasked points: **none found**.

### Book p512 / 02 PDF45

| Printed point / call-out | Question |
|---|---|
| Cryoglobulins are immunoglobulins that precipitate in cold and dissolve on rewarming. | MED-C23-15 |
| Cryoglobulinemia pathogenesis shows increased production of immunoglobulins adhering to small vessel surfaces more than medium vessels and is seen in middle-aged elderly females. | MED-C23-16 |
| Type 1 cryoglobulinemia is monoclonal IgG/IgM kappa or lambda, RF negative, with multiple myeloma and Waldenstrom macroglobulinemia including IgM and hyperviscosity symptoms. | MED-C23-17 |
| Mixed cryoglobulinemia is type 2 plus type 3; type 2 is associated with hepatitis C in 90% and Sjogren/SLE. | MED-C23-18 |
| Extrahepatic HCV manifestations listed are porphyria cutanea tarda and lichen planus. | MED-C23-19 |
| Cryoglobulinemia manifestations include non-thrombocytopenic palpable purpura, ulcers/gangrene due to medium-vessel involvement in HCV-positive disease, arthralgia similar to SLE, HCV GIT involvement and MPGN. | MED-C23-20 |

Unasked points: **none found**.

### Book p513 / 02 PDF46

| Printed point / call-out | Question |
|---|---|
| The neurology note states mononeuritis multiplex is medium vessel and small fibre neuropathy is small vessel. | MED-C23-21 |
| The triangle labels Meltzer triad as purpura, arthralgia and myalgia or weakness. | MED-C23-22 |
| Investigations list direct immunofluorescence showing IgG/IgM and cryocrit with decreased C3/C4. | MED-C23-23 |
| The treatment branch for type 1 high IgM lists PLEX, steroid and cyclophosphamide. | MED-C23-24 |
| For type 2/3, HCV positive leads to treating HCV; HCV negative leads to rituximab. | MED-C23-25 |
| The bottom note states increased risk of conversion to DLBCL, diffuse large B-cell lymphoma. | MED-C23-26 |

Unasked points: **none found**.

### Book p514 / 02 PDF47

| Printed point / call-out | Question |
|---|---|
| Variable vessel vasculitis types are Behcet disease and Cogan syndrome. | MED-C24-01 |
| The Behcet section notes it was previously classified under large-vessel vasculitis. | MED-C24-02 |
| The comparison table lists Takayasu panarteritis with lymphocyte predominance and granulomas, while Behcet has panarteritis, non-necrotizing inflammation without fibrinoid necrosis/RBC extravasation, panniculitis, obliterative phlebitis, neutrophils and absent granulomas. | MED-C24-03 |
| The note states differential diagnosis for obliterative phlebitis is IgG4 disease. | MED-C24-04 |
| The arteritis-without-granuloma column lists Behcet disease and MPA; the granuloma column lists large-vessel vasculitis, GPA, EGPA, rheumatoid vasculitis and Cogan syndrome. | MED-C24-05 |
| Risk factors list HLA-B51 as associated with Behcet disease, with other HLA-A26, HLA-B27 and HLA-B57. | MED-C24-06 |

Unasked points: **none found**.

### Book p515 / 02 PDF48

| Printed point / call-out | Question |
|---|---|
| Pathophysiology is T-cell mediated inflammation, Th1 greater than Th17. | MED-C24-07 |
| Factors expressed include ASCA antibody, anti-selenium binding protein, anti-enolase, MICA gene and ER aminopeptidase. | MED-C24-08 |
| The note states ASCA antibody is also found in Crohn disease and GIT manifestations are similar. | MED-C24-09 |
| Behcet disease most affected age group is 30–50 years, severe disease occurs in young males and it is chronic relapsing multisystem autoimmune disease. | MED-C24-10 |
| The clinical manifestations line explicitly states Behcet spares the kidney. | MED-C24-11 |
| The note says pulmonary artery vasculitis/aneurysm is seen in Takayasu arteritis and Behcet disease. | MED-C24-12 |
| The International criteria column states diagnosis is established by score ≥4. | MED-C24-13 |
| The table assigns 2 points each to oral aphthosis, genital aphthosis and ocular lesions. | MED-C24-14 |

Unasked points: **none found**.

### Book p516 / 02 PDF49

| Printed point / call-out | Question |
|---|---|
| Oral aphthous ulcers are mandatory/pathognomonic, recurrent ≥3 times/year painful ulcers, commonly at lips, buccal mucosa, tongue and soft palate. | MED-C24-15 |
| The page notes to rule out HIV during diagnosis of ulcer. | MED-C24-16 |
| Behcet genital ulcers most commonly involve scrotum and labia; they are deep, painful, less recurrent, heal with scarring and spare glans penis/urethra. | MED-C24-17 |
| Pathergy test is hypersensitivity to long scratch/intradermal saline injection, oblique skin puncture using a 25-gauge needle, with papule/pustule and erythema after 24–48 hours. | MED-C24-18 |
| The pathergy test is described as low sensitivity 60% and high specificity 80%. | MED-C24-19 |
| Cutaneous manifestations include all types of skin lesions and list papulopustular lesions as most common. | MED-C24-20 |

Unasked points: **none found**.

### Book p517 / 02 PDF50

| Printed point / call-out | Question |
|---|---|
| The note states erythema nodosum in sarcoidosis has all P's except pigmentation. | MED-C24-21 |
| Ophthalmic table: characteristic feature is chronic relapsing bilateral panuveitis; Behcet has retinal vasculitis and hypopyon, and chamber involvement PC > AC, while sarcoidosis has AC > PC. | MED-C24-22 |
| Behcet joint manifestation is asymmetrical non-erosive oligoarthritis. | MED-C24-23 |
| Warning signs include vascular thrombosis, GI involvement resembling Crohn disease, CNS involvement and very rare cardiac involvement. | MED-C24-24 |
| CNS involvement is under influence of IL-6 and types listed are vascular, parenchymal and brainstem encephalitis. | MED-C24-25 |
| Sweet syndrome is acute febrile neutrophilic dermatosis and is stated to be only seen in Behcet. | MED-C24-26 |
| MAGIC syndrome is mouth and genital ulcers with inflamed cartilage, a combination of Behcet disease and relapsing polychondritis. | MED-C24-27 |

Unasked points: **none found**.

### Book p518 / 02 PDF51

| Printed point / call-out | Question |
|---|---|
| Diagnosis section states it is a clinical diagnosis. | MED-C24-28 |
| Skin lesions are predominantly neutrophilic with cutaneous leukocytoclastic vasculitis; immunoglobulins are mixed infiltrate IgG/IgM/C3. | MED-C24-29 |
| The treatment table lists mucocutaneous disease as topical steroid plus PGE2 gel. | MED-C24-30 |
| Severe mucocutaneous disease treatment is thalidomide plus methotrexate plus topical steroid. | MED-C24-31 |
| Systemic treatment includes oral steroid prednisolone plus methotrexate or MMF; more severe disease uses MMF and less severe uses methotrexate. | MED-C24-32 |
| Cogan syndrome age group is 20–30 years. | MED-C24-33 |
| The Cogan triad shows aortitis, interstitial keratitis and vestibulitis with sensorineural hearing loss similar to Meniere disease, with less than 2 years shown between ocular and vestibular components. | MED-C24-34 |
| Cogan clinical manifestations include fever with systemic manifestations and gaze-induced nystagmus. | MED-C24-35 |
| The note says SNHL is also seen in Wegener granulomatosis. | MED-C24-36 |

Unasked points: **none found**.

### Book p519 / 02 PDF52

| Printed point / call-out | Question |
|---|---|
| The approach lists articular versus periarticular, inflammatory versus non-inflammatory, axial versus peripheral, acute <6 weeks versus chronic >6 weeks, small versus large joints, upper/lower/combined involvement, symmetrical/asymmetrical involvement and number of joints. | MED-C25-01 |
| The number-of-joints branch defines monoarthritis as 1 joint, oligoarthritis 1–4 joints and polyarthritis ≥5 joints. | MED-C25-02 |
| Periarticular disease has localized point tenderness, pain away from the joint capsule along tendon/bony prominences and painful active movement against gravity. | MED-C25-03 |
| Articular arthritis has deep diffuse pain, pain in the vicinity of the joint, both passive and active painful movements, and additional crepitation/locking/deformity/instability/swelling. | MED-C25-04 |
| Inflammatory arthritis has early morning stiffness >45 minutes, relieved with activity and worsened by rest; synovial fluid WBC >2000 cells/µL is best to differentiate inflammatory versus non-inflammatory. | MED-C25-05 |
| The note states the structure involved in RA is synovium and in OA is articular cartilage, with joint stiffness worsening with activity. | MED-C25-06 |

Unasked points: **none found**.

### Book p520 / 02 PDF53

| Printed point / call-out | Question |
|---|---|
| Types based on predominant joints list peripheral predominant RA as peripheral joints plus C-spine. | MED-C25-07 |
| The approach to inflammatory arthritis splits monoarthritis into septic arthritis and acute crystal arthropathy, which then branches to gout and pseudogout. | MED-C25-08 |
| The erosive arthritis column includes RA, psoriatic arthritis, chronic crystal arthropathy, CTDs including mixed CTDs and sarcoidosis, multicentric reticulohistiocytosis and Rhupus. | MED-C25-09 |
| The non-erosive column includes SLE/SLE-like arthritis, acute rheumatic fever Jaccoud arthropathy, relapsing polychondritis, Behcet disease and acute crystal arthropathies. | MED-C25-10 |
| MAGIC syndrome is Behcet disease plus relapsing polychondritis, with mouth and genital ulcers and inflamed cartilage. | MED-C25-11 |

Unasked points: **none found**.

### Book p521 / 02 PDF54

| Printed point / call-out | Question |
|---|---|
| Diagnosis of RA is based on duration of symptoms greater than 6 weeks. | MED-C26-01 |
| 0–3 months is labelled very early rheumatoid arthritis. | MED-C26-02 |
| More than 2 years is labelled chronic stabilized rheumatoid arthritis with deformities. | MED-C26-03 |
| RA is described as the most common multisystem autoimmune inflammatory CTD with arthritis/arthralgia and chronic inflammatory symmetrical peripheral polyarthritis. | MED-C26-04 |
| Upper-limb RA involves PIP, MCP and rarely elbow; spared joints include DIP due to least synovium and 1st CMC. | MED-C26-05 |
| RA lower limb involves 5th MTP and rarely knee, spares 1st MTP; axial skeleton involves C1-C2 and spares thoracic, lumbar and sacral vertebrae. | MED-C26-06 |
| The page states 40% of RA patients have extra-articular manifestations, with rheumatoid nodule most common. | MED-C26-07 |
| The DIP note lists psoriatic arthritis, osteoarthritis as the most common arthritis, multicentric reticulohistiocytosis and calcium pyrophosphate dihydrate disease. | MED-C26-08 |

Unasked points: **none found**.

### Book p522 / 02 PDF55

| Printed point / call-out | Question |
|---|---|
| The RA pathogenesis diagram starts with genetics plus environment, abnormal protein modification such as citrullination/carbamylation, detection as antigen by Langerhans dendritic cells and DC-T interaction. | MED-C26-09 |
| The diagram labels TNF-alpha as the key pathogenic cytokine. | MED-C26-10 |
| The normal joint progresses to chronic synovitis with synovial hypertrophy, pannus and periarticular erosion/osteopenia. | MED-C26-11 |
| TNF-alpha activates osteoclast via RANK ligand pathway and inhibits osteoblast via Dkk-1, leading to osteoporosis. | MED-C26-12 |
| HLA DRB1-04 is listed in 70%, increases risk five times and has shared epitope QKRAA motif. | MED-C26-13 |
| The genetic HLA list notes DR-13 is associated with protection. | MED-C26-14 |

Unasked points: **none found**.

### Book p523 / 02 PDF56

| Printed point / call-out | Question |
|---|---|
| PADI-4 is peptidyl arginine deiminase IV, post-translationally modifying arginine to citrulline and is seen in Asian populations. | MED-C26-15 |
| PTPN22 is specifically noted as not seen in the Asian population. | MED-C26-16 |
| Smoking is the strongest environmental risk factor, increases PADI-4 expression in airway and increases risk for ILD with bad prognosis. | MED-C26-17 |
| Protective environmental factors listed are alcohol and OCP. | MED-C26-18 |
| Other factors list females > males 3:1, most common presentation in males as ILD/vasculitis, and infection Porphyromonas gingivalis chronic periodontitis. | MED-C26-19 |
| Pregnancy is listed as increased IL-10 inducing remission. | MED-C26-20 |
| The risk-prediction flow shows acute inflammatory polyarthritis at 6 weeks: persistent goes to undifferentiated arthritis and reduced goes to post-viral. | MED-C26-21 |
| Undifferentiated arthritis branches into one-third remission, one-third persistent/progress to other disease and one-third evolve to RA. | MED-C26-22 |

Unasked points: **none found**.

### Book p524 / 02 PDF57

| Printed point / call-out | Question |
|---|---|
| The predicted-risk score lists age, female, joint distribution, swollen joints, tender joints, CRP, rheumatoid factor and anti-CCP antibody. | MED-C26-23 |
| The page states if score >8 there is >80% chance to progress to RA. | MED-C26-24 |
| Anti-CCP/ACPA/MCV is used for diagnostic purpose and not repeated, specificity >90%, best marker for preclinical infection and high titre suggests extra-articular manifestations. | MED-C26-25 |
| RF specificity is 75–80%, it is a marker of preclinical infection and extra-articular manifestations, and is nonspecific in cryoglobulinemia, Sjogren, JIA, 5% normal population, infections and other diseases. | MED-C26-26 |
| RF antibodies are shown as IgM most common against IgG Fc, with IgA in Caplan syndrome. | MED-C26-27 |
| For relapse, the page lists CRP and ESR. | MED-C26-28 |
| The clinical manifestation section begins with chronic inflammatory symmetric peripheral polyarthritis and notes insidious presentation in 55–65% as most common. | MED-C26-29 |

Unasked points: **none found**.

### Book p525 / 02 PDF58

| Printed point / call-out | Question |
|---|---|
| Elderly RA is >60 years, acute destructive polyarthritis with painful erosions and mimics PMR with shoulder/pelvic pain, increased ESR and periarticular enthesitis/bursitis. | MED-C26-30 |
| Arthritis robustus is described as minimal symptoms, blissfully unaware, with erosions on X-ray. | MED-C26-31 |
| Palindromic rheumatism occurs in young girls, acute episodic monoarthritis with complete resolution and later other joints, anti-CARP positive, with 30% progressing to RA. | MED-C26-32 |
| The deformities triangle is labelled synovitis, tendinitis and bursitis. | MED-C26-33 |
| Zig-zag deformity is the first change and includes wrist radial deviation, MCP ulnar deviation plus subluxation and interphalangeal joints extended. | MED-C26-34 |
| Piano-key deformity is due to rupture of the ulnar collateral ligament and deformity of the ulnar styloid. | MED-C26-35 |
| Hitchhiker thumb is a Z-shaped deformity with abduction and hyperextension of the thumb. | MED-C26-36 |
| Trigger finger is listed as tenosynovitis. | MED-C26-37 |

Unasked points: **none found**.

### Book p526 / 02 PDF59

| Printed point / call-out | Question |
|---|---|
| Swan-neck deformity has hyperextended PIP, flexion of DIP and rupture of FDS tendon. | MED-C26-38 |
| Boutonniere deformity is flexion of PIP and hyperextension of DIP due to synovitis of PIP causing subluxation of the lateral band. | MED-C26-39 |
| Opera glass hand deformity is labelled arthritis mutilans. | MED-C26-40 |
| Vaughan-Jackson syndrome is impaired medial extensor tendons. | MED-C26-41 |
| Intrinsic plus deformity is tightness of intrinsic muscles, hyperflexion of MCP and extension of interphalangeal joints. | MED-C26-42 |
| The note states pointing index finger is median nerve palsy. | MED-C26-43 |

Unasked points: **none found**.

### Book p527 / Missing from supplied scan

| Printed point / call-out | Question |
|---|---|
| The RA pulmonary row includes interstitial lung disease, pleural effusion, rheumatoid lung nodules and Caplan syndrome. | MED-C26-44 |
| The pulmonary row notes rheumatoid lung nodules, usually upper lobe, and Caplan syndrome as rheumatoid nodules plus pneumoconiosis. | MED-C26-45 |
| The pulmonary row describes rheumatoid interstitial lung disease with organizing pneumonia/BOOP and lower-lobe peripheral reticular shadowing. | MED-C26-46 |
| The table note states worst prognosis is rheumatoid lung disease. | MED-C26-47 |
| The page expands BOOP as bronchiolitis obliterans organizing pneumonia. | MED-C26-48 |

Unasked points: **none found**.

### Book p528 / 02 PDF60

| Printed point / call-out | Question |
|---|---|
| RA CNS row lists normal cognitive function and C1-C2 atlantoaxial subluxation with acute-onset quadriparesis and erosion of odontoid process; SLE lists cognitive decline as most common. | MED-C26-49 |
| The ocular row notes keratoconjunctivitis sicca symptoms RA > SLE and no uveitis. | MED-C26-50 |
| Episcleritis is most common, seen with increased activity and not associated with visual loss. | MED-C26-51 |
| Scleritis causes granulomatous resorption leading to scleromalacia perforans and visual loss. | MED-C26-52 |
| The vascular/cardiovascular area lists accelerated atherosclerosis as MI equivalent and APS. | MED-C26-53 |
| RA vasculitis is associated with history of smoking, men>women, long-standing radiodamage, RF positivity, low complements, and small vessel more than medium vessel involving muscular arteries in dermis. | MED-C26-54 |
| The RA vasculitis row notes ulcers and digital gangrene with instruction to start rituximab. | MED-C26-55 |
| The SLE vascular column lists mesenteric vasculitis and CNS vasculitis with mononeuritis multiplex. | MED-C26-56 |
| The hematologic row lists anemia of chronic disease as most common cause of anemia, warm antibody autoimmune hemolytic anemia, secondary immune thrombocytopenic purpura with thrombocytosis, and SLE leukopenia. | MED-C26-57 |

Unasked points: **none found**.

### Book p529 / 02 PDF61

| Printed point / call-out | Question |
|---|---|
| Felty syndrome is RA with neutropenia and splenomegaly, long-standing deformities, RF positive, HLA DRB1-04, nodules present and antibody against citrullinated histones. | MED-C26-58 |
| The row notes increased risk of conversion to DLBCL and LGL, large granular lymphocytic leukemia. | MED-C26-59 |
| RA cardiovascular row lists pericarditis without tamponade as most common CVS cause, mitral regurgitation as most common valvular heart disease, and ACS as most common cause of death. | MED-C26-60 |
| The endocrine row lists osteoporosis and hypoadrenalism; skin row lists rheumatoid nodule and pyoderma gangrenosum. | MED-C26-61 |

Unasked points: **none found**.

### Book p530 / 02 PDF62

| Printed point / call-out | Question |
|---|---|
| Management states newly diagnosed RA should achieve remission/low disease activity on treatment. | MED-C26-62 |
| Best response to treatment is stated as <3 months in very early rheumatoid arthritis. | MED-C26-63 |
| The conventional DMARD table pairs methotrexate with increased adenosine levels. | MED-C26-64 |
| Leflunomide is listed as a dihydroorotate dehydrogenase inhibitor and pyrimidine pathway blocker. | MED-C26-65 |
| Hydroxychloroquine is paired with toll-like receptor inhibitor. | MED-C26-66 |
| Among anti-TNF-alpha biological agents, etanercept is noted as a fusion molecule with least side effect. | MED-C26-67 |
| The biologic list pairs anti-CD20 with rituximab, anti-IL-1 with anakinra unavailable in India, anti-IL-6 with tocilizumab and fusion CTLA4-FcIgG with abatacept. | MED-C26-68 |
| Small-molecule oral JAK inhibitors list tofacitinib as 1/3 inhibitor and baricitinib as 1/2 inhibitor. | MED-C26-69 |

Unasked points: **none found**.

### Book p531 / 02 PDF63

| Printed point / call-out | Question |
|---|---|
| The algorithm shows bridge therapy with steroid for active inflammation because action of DMARDs starts by 6–8 weeks. | MED-C26-70 |
| First-line methotrexate is printed as 5 mg to 20 mg weekly for 3 months. | MED-C26-71 |
| Methotrexate complications list mucositis as most common, with oral ulcers and hair loss. | MED-C26-72 |
| Liver failure is marked the most dangerous methotrexate complication; monitor LFT and stop if enzymes are elevated >4 times. | MED-C26-73 |
| The Boolean definition of remission lists tender joints ≤1, swollen joints ≤1, C-reactive protein ≤1 and patient global assessment ≤1. | MED-C26-74 |
| The adequate-response branch directs continuing methotrexate. | MED-C26-75 |
| The MTX plus sulfasalazine branch lists sulfasalazine 500 mg BD/TDS with maximum 2 g. | MED-C26-76 |
| The sulfasalazine branch includes G6-PD deficiency. | MED-C26-77 |
| The branch lists HCQ 5 mg/kg, corneal complication as most common and retinal complication as most dangerous, specifically bull's-eye maculopathy. | MED-C26-78 |
| The anti-TNF branch lists increased risk of infection, malignancy, hepatitis B and TB reactivation. | MED-C26-79 |
| The JAK inhibitor branch lists less costly, most preferred, cardiac toxicity and hyperlipidemia. | MED-C26-80 |

Unasked points: **none found**.

### Book p532 / 02 PDF64

| Printed point / call-out | Question |
|---|---|
| The classification tree places shoulder and hip (root joints) under axial SpA, which then divides into non-radiographic and radiographic axial SpA. | MED-C27-01 |
| Peripheral SpA (peripheral involvement greater than axial) lists reactive arthritis, psoriatic arthritis and IBD enteropathic arthritis. | MED-C27-02 |
| The tree annotates juvenile idiopathic arthritis as AKA juvenile onset SpA. | MED-C27-03 |
| Shared features begin with HLA B27 association (varying degrees). | MED-C27-04 |
| Features list m/c extra-articular manifestation as acute anterior alternating asymmetric uveitis (4A uveitis). | MED-C27-05 |
| SpA features print absence of rheumatoid factor and absence of subcutaneous nodules and extra-articular features of RA. | MED-C27-06 |
| Non-radiographic axial SpA clinical features are inflammatory back pain (exacerbated by rest, relieved by activity), alternating buttock pain due to sacroiliitis and deep low back pain, with no radiographic evidence of sacroiliitis. | MED-C27-07 |
| Non-radiographic axial SpA: no radiographic evidence (x-ray features of sacroiliitis), MRI may show active sacroiliitis and it may have HLA B27 association. | MED-C27-08 |
| The conversion arrow prints 5% in 5–10 years to radiographic axial SpA whose x-ray features of sacroiliitis are syndesmophytes, bony ankylosis, bamboo spine and spinal fracture; extra-articular manifestations may be seen. | MED-C27-09 |

Unasked points: **none found**.

### Book p533 / 02 PDF65

| Printed point / call-out | Question |
|---|---|
| Inflammatory granulation tissue lists erosion of annulus fibrosis and nucleus pulposus, and calcification of peripheral fibres of annulus fibrosis as syndesmophytes. | MED-C27-10 |
| Under the calcification arm the vertical osteophyte is annotated thin, delicate, marginal, symmetrical. | MED-C27-11 |
| Gliding of vertebra over one another leads to bony ankylosis, producing bamboo spine and square wave vertebra (loss of concavity). | MED-C27-12 |
| Complication lists spinal fracture with m/c site C5–C6. | MED-C27-13 |
| Inflammatory mediators listed are TNF alpha and IL-17, IL-23. | MED-C27-14 |
| Presentation is structured as synovitis plus enthesitis (inflammation of tendon, ligament, capsule, fascia). | MED-C27-15 |
| Under synovitis, B/L sacroiliitis is annotated as hallmark and earliest manifestation. | MED-C27-16 |
| Presentation prints M:F = 3:1, age early 20s and HLA B27 association in 90% of AS. | MED-C27-17 |
| Enthesitis examples: Achilles tendinitis is annotated classical; plantar fasciitis and costochondritis follow. | MED-C27-18 |
| Inflammatory back pain aspects: duration >3 months (chronic), improvement with exercise, improvement with NSAIDs and no improvement of pain with rest; morning stiffness minimum 30 minutes. | MED-C27-19 |
| Aspects list onset before 45 yrs, location lower back and alternating buttock pain. | MED-C27-20 |
| Aspects include waking up from sleep due to back pain and morning stiffness (minimum 30 mins). | MED-C27-21 |
| The final inflammatory-back-pain aspect annotates involvement of shoulders and hip joint as poor prognosis. | MED-C27-22 |
| Extra-articular features print 4A uveitis m/c; CVS aortic regurgitation, ascending aortitis, conduction blocks; renal secondary IgA nephropathy; lungs upper lobe interstitial lung disease (NSIP); chest pain from costochondritis/manubriosternal enthesitis plus ascending thoracic spine; and osteoporosis. | MED-C27-23 |
| Chest pain is d/t enthesitis at costochondritis or manubriosternal joint plus ascending thoracic spine. | MED-C27-24 |

Unasked points: **none found**.

### Book p534 / 02 PDF66

| Printed point / call-out | Question |
|---|---|
| Note: Upper Lobe ILD — sarcoidosis, ankylosing spondylitis. | MED-C27-25 |
| Note prints osteoporosis: RA > AS > sarcoidosis > SLE. | MED-C27-26 |
| Investigation: MRI — STIR sequence; STIR = Short Tau Inversion Recovery; hyperintensity: inconclusive. | MED-C27-27 |
| The MRI strip is captioned semi-coronal T1, semi-coronal T1FS, semi-coronal STIR and semi-axial STIR. | MED-C27-28 |
| Grade 0 caption reads normal joints. | MED-C27-29 |
| Grade 1 shows slight blurring of cortical margins of lower 1/3rd of each joint and is marked earliest x-ray sign. | MED-C27-30 |
| Grade 2 caption: blurring + sclerosis. | MED-C27-31 |
| Grade 3 lists loss of margins and widening of joint space. | MED-C27-32 |
| Grade 4 caption: joint ankylosis. | MED-C27-33 |
| The page captions B/L sacroiliitis (grade 2/3) and a bamboo spine image. | MED-C27-34 |

Unasked points: **none found**.

### Book p535 / 02 PDF67

| Printed point / call-out | Question |
|---|---|
| Dagger sign: calcification of interspinous ligament; shown with dagger spine, rail-road sign and trolley-track sign panels. | MED-C27-35 |
| Trolley track sign: calcification of joint capsule. | MED-C27-36 |
| Romanus sign: erosion of corner; shiny corner sign: sclerosis of vertebra; square wave vertebra: vertebra become square-like. | MED-C27-37 |
| Landmark is posterior superior iliac spine; diagram labels A to B = 15 cm with 10 cm and 5 cm segments. | MED-C27-38 |
| Forward bending with knee in extension; A to B 20 cm (minimum) is normal, less than 20 cm is abnormal. | MED-C27-39 |
| Treatment: non-radiological axial SpA — NSAIDs when needed; AS — exercise, physiotherapy (most important). | MED-C27-40 |
| NSAID: indomethacin 50 mg TID, naproxen, ibuprofen — first line, prevent progression of disease, duration 2–3 wks. | MED-C27-41 |

Unasked points: **none found**.

### Book p536 / 02 PDF68

| Printed point / call-out | Question |
|---|---|
| The treatment continuation prints anti TNF alpha: adalimumab and anti IL-17: secukinumab. | MED-C27-42 |
| Intra-articular steroids: for pain relief. | MED-C27-43 |
| DISH (diffuse idiopathic skeletal hyperostosis): elderly male, non-inflammatory, part of metabolic syndrome. | MED-C27-44 |
| DISH lists ligamentous calcification and flowing wax appearance in x-ray; dorsal and lumbar spine films illustrate the flow. | MED-C27-45 |
| Reactive arthritis was previously known as Reiter's syndrome (urethritis, arthritis, conjunctivitis). | MED-C27-46 |
| m/c extra-articular manifestation: 4A uveitis; m > F, 20–40 yrs. | MED-C27-47 |
| Flowchart: infection → 2–4 weeks → arthritis with peripheral and axial (30%) arms. | MED-C27-48 |
| The flowchart prints 20% progressing to chronic arthritis. | MED-C27-49 |
| Genitourinary: Chlamydia trachomatis (m/c cause worldwide) with M:F = 9:1. | MED-C27-50 |
| Gastrointestinal: Shigella flexneri (m/c cause in India) with M:F = 1:1; Salmonella and Campylobacter follow. | MED-C27-51 |
| Note: E. coli and neisseria are not causative agents. | MED-C27-52 |

Unasked points: **none found**.

### Book p537 / 02 PDF69

| Printed point / call-out | Question |
|---|---|
| Acute sterile arthritis: organism not isolated from synovial fluid; organisms inside monocytes of synovium are detected by PCR of synovial fluid. | MED-C27-53 |
| HLA B-27 association in 50%–70% cases is linked to chronicity and prognosis. | MED-C27-54 |
| Asymmetrical peripheral arthritis: starts at knee joint; oligoarthritis greater than monoarthritis; additive — progressive involvement of joints; painful. | MED-C27-55 |
| Clinical manifestations: synovitis plus predominant enthesitis plus dactylitis; images show Achilles enthesitis and sausage-digit dactylitis. | MED-C27-56 |
| 1. Keratoderma blennorrhagicum: hyperkeratotic, crusty vesicles on palms and soles, painless. 2. Circinate balanitis: shallow erythematous ulcers of glans penis, painless. | MED-C27-57 |
| Note: D/d for keratoderma blennorrhagicum — palmo-plantar psoriasis. | MED-C27-58 |
| Axial involvement of reactive arthritis (30%) with asymmetric sacroiliitis. | MED-C27-59 |
| Syndesmophytes d/t paravertebral ossification: thick, large, coarse, fluffy, non-marginal. | MED-C27-60 |

Unasked points: **none found**.

### Book p538 / 02 PDF70

| Printed point / call-out | Question |
|---|---|
| Other manifestations: heart — aortic regurgitation (m/c), conduction blocks; kidney — secondary IgA nephropathy. | MED-C27-61 |
| Outcome/chronicity: unrelated to initial severity. | MED-C27-62 |
| Investigations: ESR CRP increased; synovial fluid PCR identifies organism. | MED-C27-63 |
| Note: gonococcal arthritis has migratory upper limb and lower limb arthritis. | MED-C27-64 |
| Treatment: NSAIDs — indomethacin 50 mg TID; intraarticular steroid to alleviate pain; DMARD — sulfasalazine for chronic reactive arthritis (15%–20%). | MED-C27-65 |
| Enteropathic arthritis AKA IBD associated arthritis; M:F = 1:1; Crohn's disease greater than ulcerative colitis. | MED-C27-66 |
| Peripheral (25%) greater than axial pattern (10%). | MED-C27-67 |
| Axial arthritis: presentation similar to ankylosing spondylitis; HLA B-27 association in 50% cases; symmetric sacroiliitis; no correlation to bowel activity; no enthesitis, dactylitis. | MED-C27-68 |
| Type 1 LMAP arthritis: more common; flares correlate with bowel disease; associated factors episcleritis, erythema nodosum, arthritis — versus Type 2 SMAP-u: less common, no correlation, uveitis. | MED-C27-69 |

Unasked points: **none found**.

### Book p539 / 02 PDF71

| Printed point / call-out | Question |
|---|---|
| Type 1 LMAP arthritis row: large joint (knee predominant), migratory, asymmetric, pauciarticular arthritis (lower limb greater than upper limb). | MED-C27-70 |
| Type 1 treatment/prognosis: self-limiting, good prognosis. | MED-C27-71 |
| Type 2 SMAP-u arthritis: small joint (MCP), migratory, aggressive, chronic, symmetrical, polyarticular arthritis. | MED-C27-72 |
| Type 2 treatment: anti TNF alpha — DOC, infliximab. | MED-C27-73 |
| Note: calprotectin, lactoferrin in stools for bowel flare. | MED-C27-74 |
| Psoriatic arthritis: 7%–40% of psoriatic cases develop arthritis; plaque type psoriasis. | MED-C27-75 |
| Age greater than 40 yrs; M:F = 1:1; HLA CW-06 02, HLA B27 (arthritis). | MED-C27-76 |
| 60/30/30 rule: 60% psoriasis → arthritis, 20% psoriasis + arthritis, 20% arthritis → psoriasis, plus nail changes in 90%. | MED-C27-77 |
| Clinical manifestation: synovitis + dactylitis + enthesitis + axial involvement (cervical spine). | MED-C27-78 |
| Thick, non-marginal, asymmetric arthritis; no mucocutaneous involvement is listed in the manifestation block. | MED-C27-79 |
| CVS: aortic regurgitation, conduction block; renal: 2° IgA nephropathy; B/L chronic posterior uveitis. | MED-C27-80 |

Unasked points: **none found**.

### Book p540 / 02 PDF72

| Printed point / call-out | Question |
|---|---|
| The captions guttate psoriasis and erythrodermis psoriasis carry the note not associated with arthritis. | MED-C27-81 |
| Pustular psoriasis: most destructive arthritis; rule out HIV. | MED-C27-82 |
| Nail changes (90%): yellow nail margin (longitudinal). | MED-C27-83 |
| Nail panels: deep and coarse nail pitting; onycholysis with subungual hyperkeratosis; oil drop sign (classical); longitudinal ridging. | MED-C27-84 |
| The oil drop sign panel is annotated classical. | MED-C27-85 |
| Wright and Moll: symmetric polyarthritis (m/c type) — involvement of DIP, skin lesion, nail changes; D/d RA (involvement of small joints). | MED-C27-86 |
| Classification continues with asymmetrical oligoarthritis, predominant DIP arthritis, predominant spondyloarthritis (axial pattern 5%, cervical predominance) and arthritis mutilans: complete destruction. | MED-C27-87 |
| Predominant spondyloarthritis: axial pattern (5%), cervical predominance. | MED-C27-88 |

Unasked points: **none found**.

### Book p541 / 02 PDF73

| Printed point / call-out | Question |
|---|---|
| Image captions: arthritis mutilans; dactylitis; corn foot. | MED-C27-89 |
| Difference table row Psoriasis: psoriatic arthritis +, rheumatoid arthritis −. | MED-C27-90 |
| Symmetric: RA ++ greater than PsA +, while asymmetric, enthesopathy, dactylitis, nail dystrophy and HIV association favor PsA. | MED-C27-91 |
| Table rows enthesopathy, dactylitis, nail dystrophy and HIV association are + for PsA and − for RA. | MED-C27-92 |
| Progression: rapid progression to bony ankylosis; CASPER criteria; no diagnostic testing. | MED-C27-93 |
| The page pairs an ivory phalanx hand film with the progression and CASPER notes for psoriatic arthritis. | MED-C27-94 |
| Syndesmophytes: thin, vertical and symmetrical in the AP illustration. | MED-C27-95 |

Unasked points: **none found**.

### Book p542 / 02 PDF74

| Printed point / call-out | Question |
|---|---|
| Paravertebral ossification: large, coarse, asymmetrical; seen in Reiter's syndrome and psoriatic arthropathy; the film is captioned non-marginal syndesmophyte. | MED-C27-96 |
| Pencil-in-cup deformity is illustrated radiographically and schematically versus a normal phalanx. | MED-C27-97 |
| Whiskering: marginal erosion with adjacent bone proliferation. | MED-C27-98 |
| Telescoping of digits; ray pattern — erosion of MCP, PIP, DIP in same finger; 100% psoriatic X-ray. | MED-C27-99 |
| Treatment lists anti TNF alpha drugs, apremilast (PDE 4 inhibitor), methotrexate, leflunomide, ustekinumab, secukinumab and tofacitinib. | MED-C27-100 |
| Apremilast is annotated PDE 4 inhibitor. | MED-C27-101 |

Unasked points: **none found**.

### Book p543 / 02 PDF75

| Printed point / call-out | Question |
|---|---|
| Types: 1. monosodium urate monohydrate (msum); 2. calcium pyrophosphate dihydrate (CPPD); 3. basic calcium phosphate (BCP) — calcium hydroxy apatite; 4. calcium oxalate. | MED-C28-01 |
| BCP is written as calcium hydroxy apatite Ca5(PO4)3OH. | MED-C28-02 |
| Pathogenesis: autoinflammatory syndrome; activation of inflammasomal pathway; inflammasomes are innate-immunity intracellular protein complexes containing caspases that convert Pro-IL1β to IL-1β. | MED-C28-03 |
| Parenthetical note: inflammasomes — innate immunity, intracellular protein complex containing caspases. | MED-C28-04 |
| MSUM presentations: asymptomatic hyperuricemia, renal manifestations, gouty arthritis. | MED-C28-05 |
| URIC ACID source: purines (adenine, guanine). | MED-C28-06 |
| The metabolism diagram places xanthine oxidase on the hypoxanthine→xanthine→uric acid steps. | MED-C28-07 |
| Note: uric acid —uricase→ allantoin (not present in humans → uric acid not metabolised). | MED-C28-08 |
| AMP → adenosine —(adenosine deaminase)→ inosine → hypoxanthine → xanthine → uric acid. | MED-C28-09 |

Unasked points: **none found**.

### Book p544 / 02 PDF76

| Printed point / call-out | Question |
|---|---|
| Diagram: uric acid pool 1.2 g; intestine (0.2 g/day); kidney (0.5 g/day); excretion (0.7 g/day). | MED-C28-10 |
| Excretion greater than 7 mg/kg/d → uricosuria. | MED-C28-11 |
| Important causes of stone formation: >7 uric acid — hyperuricosuria; >4 calcium — hypercalciuria (m/c); <11 citrate — hypocitraturia. | MED-C28-12 |
| The calcium row is annotated m/c for stone formation. | MED-C28-13 |
| 4 compartment model: 100 / 50 / 40 / 10. | MED-C28-14 |
| Model: 100% filtered in glomerulus; 100% reabsorbed at S1; 50% secreted at S2; 40% reabsorbed at S3; 10% excreted in urine. | MED-C28-15 |
| Net reabsorption of 90% of filtered uric acid. | MED-C28-16 |
| Uric acid and phosphorus metabolism takes place only in PCT. | MED-C28-17 |
| Fractional excretion of uric acid and phosphorus: increased in proximal RTA; normal in distal RTA. | MED-C28-18 |

Unasked points: **none found**.

### Book p545 / 02 PDF77

| Printed point / call-out | Question |
|---|---|
| Asymptomatic hyperuricemia: hyperuricemia is a part of metabolic syndrome. | MED-C28-19 |
| Levels: greater than 6 mg/dl in females, greater than 7 mg/dl in males. | MED-C28-20 |
| Age at pregnancy flow: ↑age → small for gestational age babies → pre-eclampsia → ↓nephron number → metabolic syndrome as adults. | MED-C28-21 |
| Unidentified (majority): 90% under-excretion, 10% over-production of urate. | MED-C28-22 |
| HGPRTase deficiency → Lesch Nyhan syndrome: hyperuricemia, self-mutilation, mental retardation. | MED-C28-23 |
| Glucose 6 phosphatase deficiency → von Gierke's disease / glycogen storage disease type 1 with hepatomegaly, hyperlipidemia, hyperuricemia, doll facies, hypoglycemia and seizures. | MED-C28-24 |
| Table rows: fructose 1 phosphate aldolase deficiency; phosphoribosyl pyrophosphate (PRPP) synthase overactivity. | MED-C28-25 |
| Secondary drug-induced hyperuricemia mnemonic CANT LEAP: cyclosporine, alcohol, nicotine, thiazide diuretics, loop diuretics, ethambutol, aspirin low dose, pyrazinamide. | MED-C28-26 |
| Progression: prolonged asymptomatic hyperuricemia → increased risk of acute gout with multiple episodes → chronic tophaceous gout. | MED-C28-27 |

Unasked points: **none found**.

### Book p546 / 02 PDF78

| Printed point / call-out | Question |
|---|---|
| Note: greater than 6.8 mg/dl (Kelley's textbook). | MED-C28-28 |
| Factors affecting: age, blood pressure, alcohol, diet (sea food, red meat), Sr. creatinine — platelet count is not listed. | MED-C28-29 |
| Sr. urate increases in men at puberty, women at menopause; pregnancy is a hyperuricemic state. | MED-C28-30 |
| Renal manifestations table: uric acid nephropathy via TLS precipitation in tubules → AKI; urate nephropathy via chronic tubulo-interstitial disease → CKD; urolithiasis when excretion exceeds 7 mg/kg/day. | MED-C28-31 |
| Uric acid nephropathy pathogenesis: tumour lysis syndrome → precipitation of uric acid in tubules → AKI. | MED-C28-32 |
| Acute gouty arthritis: sex M (80%) greater than F (post-menopausal); age 40–60 yrs. | MED-C28-33 |
| Trigger: alcohol (m/c); AKA disease of King (d/t presentation in King Henry). | MED-C28-34 |
| First attack: 1st MTP joint (85%); uric acid normal or low in 40%. | MED-C28-35 |
| 15% have polyarticular involvement, associated with myeloproliferative neoplasm and post transplantation. | MED-C28-36 |
| Duration 3–14 days; signs hot, red, dusky, swollen joint plus periarticular erythema; max intensity of pain 4–12 hrs. | MED-C28-37 |
| Staging: 1. high uric acid levels; 2. acute gout; 3. intercritical gout; 4. chronic gout with frequent pain and tophi formation. | MED-C28-38 |

Unasked points: **none found**.

### Book p547 / 02 PDF79

| Printed point / call-out | Question |
|---|---|
| Subsequent attacks: involvement of ankle / knee / wrist; variable course. | MED-C28-39 |
| Symptom-free baseline seen in gout and palindromic rheumatology. | MED-C28-40 |
| Acute monoarticular arthritis seen in gout and septic arthritis. | MED-C28-41 |
| Cytology table: WBC crystal arthritis 10,000–50,000; septic arthritis greater than 50,000. | MED-C28-42 |
| Table rows: focus of infection − versus +; culture and gram stain negative versus positive; other features — presence of crystals versus immunosuppression +. | MED-C28-43 |
| Polarized light microscopy: needle shaped crystals with strong negative birefringence. | MED-C28-44 |
| Note polarising light microscopy: needle-shaped crystals kept parallel to light ray. | MED-C28-45 |

Unasked points: **none found**.

### Book p548 / 02 PDF80

| Printed point / call-out | Question |
|---|---|
| First line: NSAIDs indomethacin 50 mg TDS; colchicine; intra-articular steroids. | MED-C28-46 |
| Colchicine: prevents neutrophil migration & chemotaxis; 1.2 mg stat → 0.6 mg after 1 hr → 0.6 mg BD × 1 week → 0.6 mg OD × 3–6 months. | MED-C28-47 |
| Second line: anakinra anti IL-1; IM ACTH injection (single dose); IV pegloticase (recombinant uricase). | MED-C28-48 |
| ACR criteria of gout: acute monoarticular arthritis; hyperuricemia; dramatic response to colchicine. | MED-C28-49 |
| Intercritical period: symptom-free period, classical feature of crystal arthropathy; 60% second flare within a year; continued deposition of tophaceous gout and erosion. | MED-C28-50 |
| Chronic gout x-ray: asymmetric, punched out lytic, overhanging edges — martel sign / G sign; sclerotic margins — rat bite erosions; joint space maintained. | MED-C28-51 |
| Ultrasound of knee labels uric acid crystals, hypoechoic hyaline cartilage and femoral cortex. | MED-C28-52 |

Unasked points: **none found**.

### Book p549 / 02 PDF81

| Printed point / call-out | Question |
|---|---|
| Tophi: irregular asymmetric moderately discrete tumescence of fingers d/t s/c deposition of msum crystals; painless; acute on chronic — acute inflammation surrounding tophi. | MED-C28-53 |
| Sites: olecranon (m/c), prepatellar bursa, ulnar surface, Achilles surface, myocardium, heart valves. | MED-C28-54 |
| Xanthine oxidase inhibitors: febuxostat (s/e cardiotoxicity); allopurinol 300 mg daily (s/e hypersensitivity in HLA B58-01 susceptibility, hairfall, liver and renal disease). | MED-C28-55 |
| Allopurinol 300 mg daily; s/e hypersensitivity in HLA B58-01 susceptibility. | MED-C28-56 |
| Uricosuric agents: probenecid, sulfinpyrazone, benzbromarone, losartan (ACE inhibitor), lesinurad. | MED-C28-57 |
| Recombinant uricase: rasburicase, pegloticase — also used in acute gout and TLS. | MED-C28-58 |
| Features: 12 yrs between first attack and chronic gout; rate of tophus formation correlates with degree and duration of hyperuricemia. | MED-C28-59 |

Unasked points: **none found**.

### Book p550 / 02 PDF82

| Printed point / call-out | Question |
|---|---|
| CPPD: age elderly; asymptomatic; non-inflammatory; gene ANKH. | MED-C28-60 |
| 1. Chondrocalcinosis: asymptomatic; calcification of articular cartilage; predominantly knee. | MED-C28-61 |
| Acute monoarticular CPPD: bloody aspiration; no hematogenous source of foci; no response to antibiotics and colchicine; rhomboid crystals with weak positive birefringence; pseudo-gout. | MED-C28-62 |
| Rhomboid crystals with weak positive birefringence. | MED-C28-63 |
| 3. Chronic inflammatory polyarthritis: waxing & waning progression; non-erosive; pseudo RA. | MED-C28-64 |
| 4. Involvement of MCP (2nd, 3rd), wrist: hook like osteophytes (seen in hemochromatosis); pseudo-OA. | MED-C28-65 |
| 5. Pseudo neuropathic disease presents like Charcot's; 6. spondyloarthritis — crowned dens syndrome (dens in atlas); 7. septic arthritis (m/c knee): fever. | MED-C28-66 |
| Associations: hyperparathyroidism; hypophosphatasia (d/d of rickets with ↓ alkaline phosphatase); hypomagnesemia (seen in Gitelman syndrome); hemochromatosis. | MED-C28-67 |

Unasked points: **none found**.

### Book p551 / 02 PDF83

| Printed point / call-out | Question |
|---|---|
| Basic calcium phosphate: deposition of calcium hydroxyapatite crystals; non-birefringent. | MED-C28-68 |
| Presentations: chronic calcific periarthritis m/c supraspinatus tendon; Milwaukee shoulder — rotator cuff arthropathy + glenohumeral destruction; calcinosis cutis. | MED-C28-69 |
| Calcinosis cutis seen in CREST syndrome and juvenile dermatomyositis (lipodystrophy, myofascial involvement). | MED-C28-70 |
| Calcium oxalate: strong positive birefringence; pyramidal, envelope shaped crystals; primary — hyperoxaluria, secondary — CKD. | MED-C28-71 |
| Note: mx of hyperoxaluria → combined kidney & liver transplantation. | MED-C28-72 |

Unasked points: **none found**.

### Book p552 / 02 PDF84

| Printed point / call-out | Question |
|---|---|
| Adult Onset Still's Disease: age 25–45 yrs; systemic form of presentation. | MED-C29-01 |
| Features: prodromal phase — sore throat. | MED-C29-02 |
| Clinical triad: fever — persistent high spiking reaches subnormal levels during day (quotidian). | MED-C29-03 |
| Salmon colored rash: transient evanescent maculo papular rash. | MED-C29-04 |
| Arthritis: symmetric, polyarticular (knee greater than wrist greater than ankle greater than elbow). | MED-C29-05 |
| Progress to severe/destructive arthritis in 25% of cases; joint erosions m/c in children. | MED-C29-06 |
| Serositis, lymphadenopathy and hepatosplenomegaly are bracketed as bad prognosis. | MED-C29-07 |
| Blood parameters: leukocytosis; ESR increased; CRP increased; ferritin increased; S. albumin decreased. | MED-C29-08 |
| Yamaguchi criteria (greater than 5): major — fever (>39°C) for 7 days; arthritis/arthralgia for 2 weeks; rash; leukocytosis. | MED-C29-09 |

Unasked points: **none found**.

### Book p553 / 02 PDF85

| Printed point / call-out | Question |
|---|---|
| minor: sore throat; negative ANA, RF; hepatosplenomegaly, lymphadenopathy; abnormal ALT/AST. | MED-C29-10 |
| HLH: rheumatological emergency; seen in 10% of AOSD. | MED-C29-11 |
| Features: pancytopenia; ESR decreased; unsubsiding fever; fibrinogen decreased; ferritin increased increased; triglycerides increased. | MED-C29-12 |
| Complications: bleeding d/t thrombocytopenia; transient thrombocytopenic purpura; DIC with consumptive coagulopathy; AA amyloidosis. | MED-C29-13 |
| Treatment: steroid — pulse therapy then oral therapy. | MED-C29-14 |
| Treatment of AOSD: mild — NSAID; no response → steroid + methotrexate → anti IL-1, IL-6. | MED-C29-15 |
| Note: sulfasalazine is avoided. | MED-C29-16 |
| Susceptible host: children, elderly; immunocompromised; IV drug abuse (oligo/polyarticular). | MED-C29-17 |
| Clinical presentation: fever; pain + limited range of motion (m/c: knee); no h/o similar episode. | MED-C29-18 |
| Causes: infection (20%) — staph. aureus greater than strep. pneumonia greater than gram-negative bacillus; spread: hematogenous. | MED-C29-19 |
| Other causes: trauma; tumour; osteoarthritis of single joint; sarcoidosis. | MED-C29-20 |

Unasked points: **none found**.

### Book p554 / 02 PDF86

| Printed point / call-out | Question |
|---|---|
| D/d: tendinitis, bursitis to be ruled out; hemophilia — similar presentation. | MED-C29-21 |
| Table: host — gonococcal young healthy versus septic immunocompromised; pattern — migratory polyarthralgia/arthritis versus monoarticular arthritis. | MED-C29-22 |
| Tenosynovitis + and skin rash + favor gonococcal, with less culture yield and good prognosis versus septic negative for both, more yield and poor prognosis. | MED-C29-23 |
| Diagnosis: synovial fluid analysis — gold standard; WBC greater than 50000 /μL. | MED-C29-24 |
| Rx: antibiotics — vancomycin + ceftriaxone; drainage indications — thick pus; shoulder, hip joint involvement. | MED-C29-25 |
| Chronic monoarticular arthritis causes: TB; fungal disease; Lyme; sarcoidosis; spondyloarthritis; non-inflammatory. | MED-C29-26 |
| Approach to arthritis begins with monoarticular arthritis and polyarticular arthritis branches. | MED-C29-27 |
| Monoarticular branches septic and crystal; polyarticular branches acute (undifferentiated, post viral) and chronic inflammatory: RA with d/d SLE and psoriatic arthritis. | MED-C29-28 |

Unasked points: **none found**.

### Book p555 / 02 PDF87

| Printed point / call-out | Question |
|---|---|
| The page introduces the mini-mental State Examination (mmse) with the line 'Helps to assess Higher mental functions/cognitive status.' | MED-C30-01 |
| 'Based on :' is followed by the red mnemonic ORAR LC and then the six bulleted components. | MED-C30-02 |
| The printed bullets read Orientation, Registration, Attention, Recall, Language, Copying; naming is not listed among them. | MED-C30-03 |
| Written output is the Language component and the figure-copying task is the Copying component of the printed ORAR LC list. | MED-C30-04 |
| 'Anatomy of Frontal Lobe' is immediately followed by the line 'Superolateral surface :' above the coloured lateral-view diagram. | MED-C30-05 |
| The figure shades the frontal lobe pink, the parietal lobe yellow behind the central sulcus, the temporal lobe green and leaves the occipital lobe unshaded. | MED-C30-06 |
| The inferior frontal gyrus label carries the printed sub-labels 'Pars opercularis' and 'Pars triangularis'. | MED-C30-07 |
| The functional map points the Auditory cortex label into the temporal lobe region, while the Visual cortex label is placed on the occipital pole. | MED-C30-08 |
| The functional map points out Motor cortex, Somatosensory cortex, Auditory cortex and Visual cortex; no olfactory cortex is labelled. | MED-C30-09 |

Unasked points: **none found**.

### Book p556 / 02 PDF88

| Printed point / call-out | Question |
|---|---|
| The right-hand column of the list prints 'Area : 4 Primary motor area (Pre central gyrus)'. | MED-C30-10 |
| The list assigns area 6 to premotor area only, while both the supplementary motor area (medially) and the frontal eye field are printed as area 8. | MED-C30-11 |
| A brace collects the area 6 and area 8 entries under the note 'Anterior to 1 degree motor area'. | MED-C30-12 |
| The prefrontal entry reads 'Area : 9,10,11,12' with the line '(Anterior to area 6 & 8)'. | MED-C30-13 |
| The functional map prints area 44, 45 as the motor speech area of Broca in the inferior frontal gyrus. | MED-C30-14 |
| The right-side label of the functional figure reads 'Lateral sulcus/ Sylvian fissure', and the caption below states 'Functional frontal lobe anatomy'. | MED-C30-15 |
| The medial-surface drawing labels CINGULATE GYRUS between the cingulate sulcus above and the corpus callosum below. | MED-C30-16 |
| The medial-surface drawing boxes PARACENTRAL LOBULE in pink at the superior medial margin, with the marginal ramus labelled just in front of it. | MED-C30-17 |
| The orbital figure prints GYRUS RECTUS, then 'Olfactory sulcus' with an arrow, then MED. ORB. GYRUS. | MED-C30-18 |
| The arrow to the orbital sulcus carries the printed note 'Orbital sulcus (H shaped)', with ANTr., POST., MED. and LAT. orbital gyri labelled around it. | MED-C30-19 |

Unasked points: **none found**.

### Book p557 / 02 PDF89

| Printed point / call-out | Question |
|---|---|
| The area 4 block opens with 'Only 30% motor fibres originate from here.' | MED-C30-20 |
| 'Betz cells present :' is followed by 'Specialized cells.' and 'Lowest threshold to initiate motor activity.' | MED-C30-21 |
| The third bullet of the area 4 block reads Initiate fine skilled voluntary movement, while planning and finesse are given to the basal ganglia and cerebellum. | MED-C30-22 |
| The PMA and SMA block prints '30% motor fibers originate here.' | MED-C30-23 |
| The preparation list is exactly tone of posture, proximal muscle alignment and antagonist muscle inhibition. | MED-C30-24 |
| The block lists 'B/I lesion spasticity (Tone issue).' with the sub-bullet 'Primitive reflexes.' | MED-C30-25 |
| The ladder begins with Planning and coordination credited to the basal ganglia. | MED-C30-26 |
| The second step of the ladder assigns Prepare (setting up) to PMA/SMA. | MED-C30-27 |
| The ladder ends 'Finesse : by Cerebellum', while Initiation is given to the 1 degree motor area. | MED-C30-28 |
| The homunculus note states 'Face & upper limb : Superolateral surface (supplied by middle Cerebral Artery/MCA).' | MED-C30-29 |
| The left-hand note reads 'Lower limb : medial surface (Supplied by anterior cerebral artery (ACA)).' | MED-C30-30 |
| Along the face region the figure prints Jaw, Tongue, Swallowing and then the arrowed labels MASTICATION, SALIVATION and VOCALIZATION. | MED-C30-31 |

Unasked points: **none found**.

### Book p558 / 02 PDF90

| Printed point / call-out | Question |
|---|---|
| The first line under the homunculus continuation reads 'MCA lesion : Face & U/L weakness.' | MED-C30-32 |
| The printed ACA line pairs lower limb weakness with urinary incontinence, the bladder representation being in the paracentral lobule on the medial surface. | MED-C30-33 |
| The ACA line attributes incontinence to the 'paracentral lobule on medial surface'. | MED-C30-34 |
| The list opens 'C/l weakness (Fine skilled voluntary movements).' | MED-C30-35 |
| The second bullet reads 'uMN lesion : Spasticity (Hypertonia).' | MED-C30-36 |
| The page prints 'Fare & upper Limb (Lower limb predominant weakness depending on vessel/side affected) (motor Homunculus)', so dominance is vessel- and side-dependent, never always the leg. | MED-C30-37 |
| The final lesion bullet reads 'Initiate lesion : C/l motor simple partial seizure : Jacksonian march.' (printed as an irritative-type lesion). | MED-C30-38 |
| The last bullet of the lesion block reads 'upper motor Neuron (uMN) : From cortex till anterior horn cell (In grey matter).' | MED-C30-39 |
| The legend lists PPRF - Para Pontine Reticular Formation, LR - Lateral Rectus, MR - medial Rectus and MLF - medial Longitudinal Fasciculus. | MED-C30-40 |
| The legend beside the flowchart reads PPRF - Para Pontine Reticular Formation, alongside LR - Lateral Rectus and MR - medial Rectus. | MED-C30-41 |
| The bullet reads '(L) FEF -> Activates (R) LR & (L) MR -> look to (R).' | MED-C30-42 |
| '(L) FEF lesion -> Cannot look (R) -> patient looks (L) (side of lesion)', concluded as 'Frontal lobe lesion -> Patient look towards side of lesion.' | MED-C30-43 |
| The printed rules contrast a frontal lobe lesion, where the patient looks towards the side of the lesion, with a brainstem PPRF lesion, where the eyes look away from the side of the lesion. | MED-C30-44 |
| The flowchart shows the VI box with a red arrow to 'Right lateral rectus', and PPRF driving VI. | MED-C30-45 |
| The pink highlighted label pointing at that crossing red tract is 'MLF'; the III box in turn points to 'Medial rectus'. | MED-C30-46 |
| The Broca block reads 'Fluency affected (Non fluent aphasia).' | MED-C30-47 |
| The page assigns fluency loss to lesions anterior to the central sulcus and the closing Note assigns comprehension loss to lesions posterior to it. | MED-C30-48 |

Unasked points: **none found**.

### Book p559 / 02 PDF91

| Printed point / call-out | Question |
|---|---|
| The page title reads 'pre Frontal Cortex (PFC) / Area. 9, 10, 11, 12 :'. | MED-C30-49 |
| Row one of the table pairs Dorsolateral PFC with 'Executive function'. | MED-C30-50 |
| The table prints 'medial PFC (cingulate gyrus)' against 'Emotion & motivation'. | MED-C30-51 |
| The table assigns executive function to the dorsolateral PFC, while orbital, medial and polar rows are exactly behavioural response, emotion & motivation and theory of mind. | MED-C30-52 |
| The three printed components are cognitive inhibition, response inhibition and set shifting (flexibility); antagonist muscle inhibition belongs to the premotor list on p557. | MED-C30-53 |
| The third bullet reads 'Set shifting (flexibility).' | MED-C30-54 |
| The energisation block prints 'when lost : Apathy (mild) -> Abulia -> Akinetic mutism (severe).' | MED-C30-55 |
| The behavioural response block reads 'Based on reward/punishment.' | MED-C30-56 |
| The list prints 'Includes : JIPFA.' followed by the five expansions. | MED-C30-57 |
| JIPFA expands to Judgement, Insight, Problem solving/personality, Fluency and Abstract thinking. | MED-C30-58 |
| The theory-of-mind bullets read 'Sympathy, empathy.' and 'metacognition : understanding oneself.' | MED-C30-59 |
| The table pairs the Frontal pole with 'Theory of mind', the block that lists sympathy, empathy and metacognition. | MED-C30-60 |
| The B/L FRONTAL LOBE PATHOLOGY list prints 'Primitive reflexes (d/t pre motor cortex involvement).' | MED-C30-61 |
| The list states 'Akinetic mutism : worst form of apathy.' | MED-C30-62 |
| The final bullet reads 'Gait apraxia : Seen in Normal Pressure Hydrocephalus (Ignition failure : Foot feels like stuck to floor).' | MED-C30-63 |
| The MMSE components are printed on p555 as Orientation, Registration, Attention, Recall, Language and Copying, and p559 grades lost energisation as Apathy (mild) -> Abulia -> Akinetic mutism (severe). | MED-C30-64 |

Unasked points: **none found**.

### Book p560 / 02 PDF92

| Printed point / call-out | Question |
|---|---|
| Under the 'Parietal lobe' heading the printed line reads 'Posterior to central sulcus.' | MED-C31-01 |
| The highlighted label reads 'Primary sensory cortex (area 3, 1, 2)'. | MED-C31-02 |
| The grey annotation on the figure states 'Superior parietal lobule (Praxicons)'. | MED-C31-03 |
| The green label for the inferior parietal lobule carries no syndrome name, while the posterior parietal lobule is highlighted, the supramarginal gyrus is annotated Gnosis and the angular gyrus carries the Gerstmann syndrome note. | MED-C31-04 |
| The figure labels 'intraparietal sulcus' running between the SUP. PARIETAL LOBULE and INF. PARIETAL LOBULE. | MED-C31-05 |
| The three branches read 1 degree sensory cortex (40%), 1 degree motor cortex (30%) and Premotor and supplementary motor cortex (30%). | MED-C31-06 |
| The note gives 30% to the 1 degree motor cortex and 30% to the premotor and supplementary motor cortex. | MED-C31-07 |
| The postcentral gyrus list reads C/L upper motor Neuron (UMN) weakness : middle cerebral artery. | MED-C31-08 |
| The postcentral gyrus list prints tone as less affected and the frontal eye field as spared. | MED-C31-09 |
| The note states 'Association with Pre-motor and Supplementary motor area : Tone, FEF.' | MED-C31-10 |
| The four printed cortical sensations are tactile localization, two point discrimination, stereognosis and graphesthesia; vibration is not listed. | MED-C31-11 |
| Stereognosis, the recognition of an object by touch, is one of the four cortical sensations listed as impaired. | MED-C31-12 |

Unasked points: **none found**.

### Book p561 / 02 PDF93

| Printed point / call-out | Question |
|---|---|
| Under SUPERIOR PARIETAL LOBULE the text reads 'generate Praxicons : movement formula/sensory guidance for movement.' | MED-C31-13 |
| Apraxia is defined as 'Inability to execute a learnt voluntary skilled action despite normal cerebellum, motor & sensory function and comprehension.' | MED-C31-14 |
| The second bullet reads 'Lesion in SPL : Inability to generate praxicons.' | MED-C31-15 |
| The types are printed as 'Ideational apraxia : Idea absent.' and 'Ideomotor apraxia : Idea present -> Execution poor.' | MED-C31-16 |
| Under Supramarginal gyrus the text reads 'gnosis : Ability to recognize object by touch/vision/sound.' | MED-C31-17 |
| The visual agnosia block reads 'Inability to identify by vision' with areas 'Supramarginal gyrus' and 'Parieto-occipital association area : Visuospatial orientation'. | MED-C31-18 |
| The figure labels 'Parieto-occipital association area : Visuospatial orientation' beside the parieto-occipital region. | MED-C31-19 |
| The printed captions under the four drawings are snake, stereo or computer, bug and lamp; spider is not one of them. | MED-C31-20 |
| The table prints Right handed as right lobe 5% and left lobe 90-95%. | MED-C31-21 |
| The second table row prints Left handed: right lobe 40% and left lobe 50-60%. | MED-C31-22 |
| Beneath the handedness table the line reads 'Language is part of dominant lobe.' | MED-C31-23 |
| The non-dominant parietal lobe heading lists pseudoapraxia with constructional apraxia and dressing apraxia, the latter illustrated by being unable to put on a jacket. | MED-C31-24 |
| The bullet reads 'Constructional apraxia : Inability to perceive and imagine geometric relation.' | MED-C31-25 |
| The last bullet of the page defines visuospatial disorientation as the inability to differentiate places, illustrated by the bedroom and bathroom example. | MED-C31-26 |

Unasked points: **none found**.

### Book p562 / 03 PDF1

| Printed point / call-out | Question |
|---|---|
| The bullet reads 'Hemispatial neglect (Anosognosia/Asomatognosia) : visual scanning (Body schema) -> Neglect of activities related to one of the hemispheres.' | MED-C31-27 |
| The printed gloss is 'visual scanning (Body schema)' before the neglect definition. | MED-C31-28 |
| The table prints left parietal extrapersonal space as 'Right' and its lesion row as 'No abnormality', so neglect of the right field is not a left parietal sign. | MED-C31-29 |
| The right parietal column lists the lesion row as 'Left hemispatal neglect' (as printed). | MED-C31-30 |
| The bullet reads 'Topographic agnosia : Loss of orientation to topography.' | MED-C31-31 |
| The flower and clock drawings on the right of the page are captioned Hemispatial neglect, while the copied geometric figures are captioned Constructional apraxia By patient. | MED-C31-32 |
| The left-hand drawing is labelled as the Rey-Osterrieth Complex Figure (ROCF) figure versus patient, with the A1, A2 and A3 patient copies beneath it. | MED-C31-33 |
| The functions column prints Reading, Writing, Naming and 'Spatial orientation with respect to finger, number, body sites'; calculation appears only as acalculia in Gerstman syndrome. | MED-C31-34 |
| The fourth function bullet reads 'Spatial orientation with respect to finger, number, body sites.' | MED-C31-35 |
| The Gerstman column opens 'Lesion of dominant angular gyrus.' | MED-C31-36 |
| The printed syndrome lists alexia with agraphia, anomia and finger anomia/acalculia/right-to-left disorientation; limb-kinetic apraxia is not named. | MED-C31-37 |
| The note reads 'Left Posterior Cerebral Artery (PCA) Infarct + Splenium of corpus callosum', with the disconnection arm giving 'Alexia without agraphia'. | MED-C31-38 |
| The right-hand branch states 'Disconnection syndrome (Loss of connection between cortices).' | MED-C31-39 |
| The branch prints 'Vision normal (macular sparing)' and 'C/L (Right) homonymous hemianopia'. | MED-C31-40 |
| The bullet reads 'Pure Alexia : Lesion of fusiform gyrus.' | MED-C31-41 |
| The list prints frontal lobe as C/L hemianopia, parietal as inferior quadrantanopia (pie in floor) and temporal as superior quadrantanopia (pie in sky). | MED-C31-42 |
| The printed table assigns the temporal lobe 'U/L superior homonymous quadrantanopia (Pie in sky)', the parietal lobe the pie-in-floor counterpart and the frontal lobe a C/L hemianopia. | MED-C31-43 |

Unasked points: **none found**.

### Book p566 / 03 PDF5

| Printed point / call-out | Question |
|---|---|
| Language is defined as the basic concept of communication and is a dominant-hemisphere function; its abnormality is aphasia. | MED-C33-01 |
| Speech is the motor output of language; its abnormality is dysarthria, whereas the abnormality of language is aphasia. | MED-C33-02 |
| The diagram marks prosody - emotional intonation of language - as a non-dominant hemisphere function. | MED-C33-03 |
| The auditory-pathway diagram labels connecting-fibre abnormality as pure word deafness; the peripheral muscles (larynx vocal cords, pharynx palate, oesophagus) are driven below the brainstem nuclei. | MED-C33-04 |
| Broca's speech area (44,45) carries grammar, syntax, rhythm and fluency while Wernicke's area (22) processes sound and comprehension; the companion Areas-of-Brain diagram labels the perisylvian region, premotor, primary motor, supplementary motor, Rolandic fissure, primary sensory, supramarginal and arcuate gyri, Sylvian fissure and primary auditory area. | MED-C33-05 |
| The diagram's final line lists the peripheral muscles: larynx (vocal cords), pharynx (palate) and oesophagus. | MED-C33-06 |

Unasked points: **none found**.

### Book p567 / 03 PDF6

| Printed point / call-out | Question |
|---|---|
| Notes: auditory association fibres abnormality -> auditory agnosia; connecting fibres abnormality -> pure word deafness; lesion in fusiform gyrus -> pure alexia. | MED-C33-07 |
| Lesion/disease table: anterior to central sulcus -> fluency; posterior to central sulcus -> comprehension; in and around Sylvian fissure -> repetition; dominant lobe -> naming. Prosody of speech is d/t non-dominant lobe disease. | MED-C33-08 |
| Preserved comprehension with preserved repetition leads to transcortical motor aphasia (d/t watershed infarct MCA, PCA); impaired repetition in that branch gives Broca's aphasia. | MED-C33-09 |
| Broca's aphasia in the flowchart: agrammatic (telegraphic), poor reading/writing, associated sign weakness and good comprehension; motor aphasia overall is non-fluent speech: DESP (dysarthria, effortful, sparse with reduced word output, prosody lost, naming impaired). | MED-C33-10 |
| Sensory aphasia: fluent speech with jargon substitution (eg pen -> hen), neologisms (create new words), logorrhoea (increased word output) and naming impaired (paraphasia). | MED-C33-11 |

Unasked points: **none found**.

### Book p568 / 03 PDF7

| Printed point / call-out | Question |
|---|---|
| Preserved comprehension with impaired repetition = conduction aphasia (arcuate fasciculus lesion); preserved repetition in that branch = anomic aphasia (angular gyrus lesion); impaired comprehension with preserved repetition = transcortical sensory aphasia (d/t infarct). | MED-C33-12 |
| Impaired comprehension with impaired repetition = Wernicke's aphasia (d/t infarct; reading loud, writing formed with errors, preservation poor, associated sign superior quadrantanopia, no weakness). | MED-C33-13 |
| Note beneath the flowchart: lesion of parietal lobe -> inferior quadrantanopia (the Wernicke's arm separately lists superior quadrantanopia). | MED-C33-14 |
| The four printed types: cortical (in Broca's aphasia), pseudo-bulbar/spastic (corticobulbar fibres abnormality), bulbar/flaccid (LMN - brain stem nuclei and below; test sounds produced from lip, tongue and oropharynx) and cerebellar (slow scanning staccato speech). | MED-C33-15 |
| Pseudo-bulbar (spastic) dysarthria = corticobulbar fibres abnormality (UMN -> cortex to anterior horn cell); bulbar (flaccid) is LMN at brain stem nuclei and below. | MED-C33-16 |

Unasked points: **none found**.

### Book p569 / 03 PDF8

| Printed point / call-out | Question |
|---|---|
| Processes of memory: encoding (registration), consolidation (storage) and retrieval. | MED-C34-01 |
| Duration table: immediate/working memory = no storage, e.g. recalling a phone number within 1 min; short term/recent = hippocampus storage, e.g. recalling breakfast; long term = neocortex, e.g. recalling something from distant past. | MED-C34-02 |
| Storage row: immediate = no storage; short term/recent = hippocampus (medial temporal lobe); long term = neocortex - and retrieval in all three columns is the prefrontal cortex. | MED-C34-03 |
| Mode of retrieval (current classifications): explicit (declarative) - episodic and semantic - and implicit (non-declaratives): procedural, priming, associative (conditional), non associative. | MED-C34-04 |
| Episodic: based on time and context (autobiographical), area hippocampus, affected early in Alzheimer's disease; semantic: based on facts, association areas, rarely affected in late Alzheimer's disease. | MED-C34-05 |
| Implicit (non-declaratives) listed: procedural, priming, associative (conditional) and non associative; episodic belongs to explicit (declarative) memory. | MED-C34-06 |

Unasked points: **none found**.

### Book p570 / 03 PDF9

| Printed point / call-out | Question |
|---|---|
| Procedural: basal ganglia, supplementary motor area, cerebellum (e.g. driving); priming: neo cortex (remembering facts d/t exposure, duration or intensity); associative (conditional): amygdala (not seen in humans - animals associating fear to lion and environment); non-associative: reflex pathway (habitual response). | MED-C34-07 |
| Associative (conditional) memory: amygdala; characteristics - not seen in humans; animals associating fear to lion and environment. | MED-C34-08 |
| Cortex table: frontal (prefrontal cortex, all types), parietal (association area parieto-occipital, semantic), temporal (hippocampus, episodic semantic), occipital (area '-', semantic). | MED-C34-09 |
| Sub-cortex table: amygdala -> conditional; cerebellum -> procedural; entorhinal cortex -> long term memory (gateway of memory); basal ganglia -> procedural. The zones-of-brain medial diagram follows. | MED-C34-10 |

Unasked points: **none found**.

### Book p571 / 03 PDF10

| Printed point / call-out | Question |
|---|---|
| Papez circuit aka mammillo-thalamic circuit: hippocampus/subiculum -> fornix -> mammillary body (Wernicke-Korsakoff syndromes) -> mammillo-thalamic tract -> thalamus -> internal capsule -> cingulate gyrus -> parahippocampal gyrus -> entorhinal cortex (gateway of memory) -> back to hippocampus. | MED-C34-11 |
| The circuit closes via the parahippocampal gyrus into the entorhinal cortex, labelled gateway of memory, which returns to the hippocampus/subiculum. | MED-C34-12 |

Unasked points: **none found**.

### Book p572 / 03 PDF11

| Printed point / call-out | Question |
|---|---|
| ADL: basic = self-care related; instrumental = handling own phone, money, etc. Cognitive impairment: minor = ADL unaffected; major = ADL affected. | MED-C35-01 |
| Definition as printed: major cognitive impairment + >=1 out of 6 cognitive domains affected. | MED-C35-02 |
| Domain table: episodic memory -> hippocampus (median temporal lobe); language -> inferior frontal gyrus (Broca's) + superior temporal gyrus (Wernicke's); complex attention, executive function and social cognition -> prefrontal cortex; perceptual motor (praxicons) -> superior parietal lobule. | MED-C35-03 |
| Causes: 1. Alzheimer's disease (m/c); 2. diffuse Lewy body (DLB) dementia; 3. vascular dementia (branches: post-stroke, multi-infarct dementia, white matter dementia/Binswanger disease); 4. normal pressure hydrocephalus (NPH). | MED-C35-04 |
| Dementia -> cortical; subcortical -> diffuse Lewy body (DLB) dementia, progressive supranuclear palsy, Binswanger disease, NPH. | MED-C35-05 |
| Note - functions of PFC: dorsolateral PFC executive function; medial PFC energisation and motivation; orbital PFC behaviour. | MED-C35-06 |

Unasked points: **none found**.

### Book p573 / 03 PDF12

| Printed point / call-out | Question |
|---|---|
| Reversible causes: D drugs (benzodiazepines, tricyclic antidepressants, lithium); E endocrine (hypothyroidism: metabolic slowing); M metabolic (vit B12 deficiency); E chronic infections of ear; N normal pressure hydrocephalus; T trauma, tumors; I infections (chronic meningitis); A anemia, autoimmune encephalitis. | MED-C35-07 |
| Note: vit B12 deficiency -> peripheral neuropathy, dementia and subacute combined cord degeneration; Rx of NPH: surgery. | MED-C35-08 |
| Note under reversible causes: Rx of NPH - surgery. | MED-C35-09 |
| Young onset dementia: frontotemporal dementia (Pick's disease) m/c, prion disease, Huntington's disease, DLB dementia. | MED-C35-10 |
| Rapidly progressive: FTD (Pick's) m/c, prion, DLB, HIV and Whipple's (bracketed non-degenerative), tumors (based on location). | MED-C35-11 |
| Atrophy of: entorhinal cortex - specific for Alzheimer's; dentate nucleus - occurs with ageing. Alzheimer's disease: m/c cause of dementia; most important risk factor age; sporadic. | MED-C35-12 |
| Most important risk factor: age (>85 years: 40% chance of Alzheimer's). | MED-C35-13 |

Unasked points: **none found**.

### Book p574 / 03 PDF13

| Printed point / call-out | Question |
|---|---|
| APP (amyloid precursor protein, gene on chr 21) with abnormal kinetics is metabolised by beta-secretase producing A-beta amyloid (beta-pleated sheets); note: normal metabolism uses alpha-secretase. | MED-C35-14 |
| A-beta 40 -> cerebral amyloid angiopathy (microhemorrhages in brain); A-beta 42 -> Alzheimer's disease -> depositions of hyperphosphorylated tau proteins (tauopathy). | MED-C35-15 |
| Inside neuron: neurofibrillary tangles -> mitochondrial injury to neurons -> progressive neuronal destruction; outside neuron: amyloid/neuritic plaques elicit toxic response from oligodendrocytes, microglia, astrocytes. | MED-C35-16 |
| Normal physiology: insulin degrading enzyme (IDE) degrades insulin and A-beta 42; in diabetes hyperinsulinemia -> IDE used up in degrading insulin -> A-beta 42 accumulates. | MED-C35-17 |
| Pathology: atrophy of median temporal lobe, lateral temporal lobe, cingulate gyrus and entorhinal cortex (gateway of memory) - seen on MRI; plus Hirano bodies and granulovacuolar degeneration. | MED-C35-18 |
| Depleted cholinergic neurons of nucleus basalis of meynert -> DOC: cholinesterase inhibitors. | MED-C35-19 |

Unasked points: **none found**.

### Book p575 / 03 PDF14

| Printed point / call-out | Question |
|---|---|
| Genetic basis: Presenilin-1 (chr 14) and Presenilin-2 (chr 1) - m/c defect in familial AD -> early onset -> characteristic features (<45 years, seizures, sleep disturbances); ApoE4 (chr 19) in late-onset dementia, ineffective degradation of A-beta amyloid, most important risk factor (biomarker) for sporadic AD in elderly. | MED-C35-20 |
| Risk factors: age, positive family history (Presenilin 1 > 2), F > m, h/o head trauma/concussions, h/o stroke, metabolic syndrome, hypertension, diabetes. Printed NOT risk factors: low IQ, smoking, NSAIDs. Note: theory of cognitive reserve - individuals with daily use of cognitive domains are protected from AD. | MED-C35-21 |
| Note - theory of cognitive reserve: individuals with daily use of cognitive domains -> protected from AD. | MED-C35-22 |
| Loop: hippocampus -> stage I (Korsakoff amnestic stage: episodic memory loss, difficulty in consolidating memory) -> angular gyrus -> association areas (stage II: stage of anomia, naming and comprehension abnormalities) -> superior parietal lobe praxicons (stage III: visuo-spatial disorientation; apraxia) -> PFC (stage IV: behavioural abnormalities and personality changes). Note: memory = time dependant, contextual, autobiographic. | MED-C35-23 |

Unasked points: **none found**.

### Book p576 / 03 PDF15

| Printed point / call-out | Question |
|---|---|
| Investigations: EEG normal/non-specific slowing; CSF analysis down A-beta 42 levels, up hyperphosphorylated tau levels; PET scan IOC detecting hypometabolism and amyloid fibrils (PiB PET scans shown for AD vs control). | MED-C35-24 |
| PET scan: IOC; detects hypometabolism and amyloid fibrils. | MED-C35-25 |
| Treatment: 1. cholinesterase inhibitors (DOC): donepezil, rivastigmine, galantamine; 2. NMDA antagonist: memantine; 3. monoclonal antibody against A-beta 42: aducanumab. | MED-C35-26 |
| Note: tacrine - obsolete (d/t hepatotoxicity). | MED-C35-27 |

Unasked points: **none found**.

### Book p577 / 03 PDF16

| Printed point / call-out | Question |
|---|---|
| FTD (Pick's disease): 70% sporadic, young onset dementia (50-60 years), rapidly progressive dementia; note contrasts Alzheimer's -> 90-95% sporadic (cerebral atrophy MRI pair). | MED-C36-01 |
| Pathology involves MAPT gene chromosome 17; proteins involved: TDP-43 (m/c), tau (hyperphosphorylated: loss of function of tau molecule) -> Pick's bodies, FUS; b/l prefrontal cortex atrophy. | MED-C36-02 |
| Clinical features: m/c type behavioural variant; loss of social embarrassment; social and emotional systems dysfunction (apathy, overeating - temporal); impaired planning and judgement; memory relatively preserved; hyperorality - temporal lobe involvement. | MED-C36-03 |
| Notes: tauopathy -> hypophosphorylated tau / hyperphosphorylated tau (Alzheimer's, Pick's); PFC -> Id, superego, ego. Diffuse Lewy Body Dementia: 2nd m/c cause of dementia; part of Parkinson-plus/atypical Parkinson's syndrome. | MED-C36-04 |
| Components of Parkinson plus syndrome: 'Tau'opathies - progressive supranuclear palsy, corticobasal degeneration; 'alpha synuclein'-opathies - multiple system atrophy, diffuse Lewy Body dementia. | MED-C36-05 |

Unasked points: **none found**.

### Book p578 / 03 PDF17

| Printed point / call-out | Question |
|---|---|
| Lewy bodies: intraneuronal cytoplasmic inclusions; content alpha-synuclein. Note: Parkinson's = alpha synucleinopathy; Alzheimer's = 'Tau'pathy (degenerated cholinergic neurons in the nucleus basalis of meynert); anticholinergics are the Rx of drug-induced parkinsonism. | MED-C36-06 |
| Characteristic changes 5-10 years before onset of disease: 1. REM sleep disorders; 2. autonomic nervous system symptoms - postural hypotension, erectile > ejaculatory dysfunction, urinary abnormalities. | MED-C36-07 |
| Listed ANS symptoms: postural hypotension, erectile > ejaculatory dysfunction and urinary abnormalities. | MED-C36-08 |
| DLB v/s PD table: DLB - cognitive impairment precedes/within 1 year (predominant rapidly progressive dementia), visual hallucinations and fluctuating alertness precede motor symptoms, tremors uncommon, b/l axial rigidity (rocket sign +), gait abnormalities common, antipsychotics worsen (d/t D2 receptor inhibition), L-dopa no improvement, treatment none available; PD - after 4-5 years of motor manifestations, tremor common, asymmetrical rigidity, gait uncommon, L-dopa improves, Rx L-dopa and deep brain stimulation. | MED-C36-09 |
| Note: rocket sign - falling backwards immediately after trying to get up from a chair. | MED-C36-10 |

Unasked points: **none found**.

### Book p579 / 03 PDF18

| Printed point / call-out | Question |
|---|---|
| Cortical column: examples Alzheimer's, FTD; affected hippocampus, medial temporal lobe; memory severe; apraxia (superior parietal lobe lesion) / agnosia (association areas) / acalculia (angular gyrus) (+); early dysphasia; visuo-spatial more severe; personality indifferent; mood depressed (subcortical > cortical); coordination normal; cognitive and motor speed normal; abnormal movements rare; extrapyramidal symptoms -. | MED-C36-11 |
| Subcortical column: examples DLB dementia, PSP, NPH, Binswanger's disease; regions subcortical grey matter (basal ganglia, thalamus) plus subcortical white matter (corticospinal, corticobulbar fibres); memory less severe; language normal; personality apathetic; coordination impaired; speed slow; abnormal movements common; extrapyramidal symptoms +. | MED-C36-12 |
| Subcortical column values: language normal (cortical: early dysphasia), personality apathetic, speed slow, abnormal movements common. | MED-C36-13 |
| Prion: infectious protein with no nucleic acid; genetic/sporadic. Pathology: beta-pleated PrPsc protein -> spongiform degeneration of cortex -> neuronal loss. | MED-C36-14 |

Unasked points: **none found**.

### Book p580 / 03 PDF19

| Printed point / call-out | Question |
|---|---|
| Types of prion diseases: 1. CJD, 2. familial fatal insomnia, 3. kuru, 4. Gerstmann Straussler Scheinker disease. Common features: young onset dementia, rapidly progressive dementia, no immune response. (Whipple's appears only in the p573 rapidly-progressive list.) | MED-C36-15 |
| CJD investigations: EEG - low voltage background, high voltage sharp waves; CSF normal; brain biopsy to confirm diagnosis; Rx flupirtine maleate (centrally acting non-opioid analgesic). | MED-C36-16 |
| Dementia-protein table: Alzheimer's A-beta; FTD tau; DLB alpha synuclein; CJD PrPsc. Vascular dementia: types large vessel disease (post-CVA dementia) and small vessel disease. | MED-C36-17 |
| Large vessel disease: m/c site of infarct b/l PCA lesion; criteria: 1. dementia; a. cerebrovascular disease - multi-infarct state with 'strategic territory' infarct (infarct in these areas leads to dementia). | MED-C36-18 |

Unasked points: **none found**.

### Book p581 / 03 PDF20

| Printed point / call-out | Question |
|---|---|
| 3. Relationship between the two disorders: onset of dementia within 3 months of stroke; stepwise decline in cognitive function (stepwise graph). | MED-C36-19 |
| Small vessel disease - Binswanger disease: most important risk factor HTN; lacunar infarct; pathology lipohyalinotic infarct involving penetrating vessels (size 30-300 um); MRI finding white matter hyperintensities in elderly (gradual cognitive-decline graph); features similar to vascular Parkinson's. | MED-C36-20 |
| Fibres affected -> manifestation: corticobulbar tract -> pseudobulbar palsy; corticospinal tract (affects lower limb fibres close to the ventricle) -> gait disturbances and falls, gait apraxia, magnetic/ignition foot phenomenon (feet 'stuck' to floor); fibres from paracentral lobule -> urinary abnormalities; corticostriate fibres (PFC to striatum) -> personality changes. | MED-C36-21 |
| Cerebral amyloid angiopathy: A-beta 40 protein deposition, elderly, microhemorrhages. (NOTCH3 is the CADASIL mutation.) | MED-C36-22 |

Unasked points: **none found**.

### Book p582 / 03 PDF21

| Printed point / call-out | Question |
|---|---|
| CADASIL: cerebral autosomal dominant arteriopathy with small vessel ischemic change/leukoencephalopathy, or CADA with stroke and ischemic leukoencephalopathy; m/c inherited vascular dementia; NOTCH3 mutation; presentation aura + migraine + dementia + stroke. | MED-C36-23 |
| Hydrocephalus: occlusive (non-communicating) -> aqueductal stenosis; non-occlusive (communicating) -> up CSF production or down CSF adsorption -> idiopathic (NPH) / familial (congenital: arachnoid granulations; acquired: trauma, SAH). Note: atrophy - obtuse interventricular angle. | MED-C36-24 |
| NPH pathology: adsorption defect > outflow resistance of CSF -> ventriculomegaly, no atrophy. Clinical: symptoms progress over weeks to months; GUD - gait (gait apraxia/magnetic foot), urinary (incontinence), dementia (subcortical type); arrest in initiation of ambulation; gait instability with multiple falls; generalized slow movements; CSF pressure normal (20 ml/day produced); Rx shunting (good prognosis if effective); MRI - interventricular angle acute. | MED-C36-25 |

Unasked points: **none found**.

### Book p583 / 03 PDF22

| Printed point / call-out | Question |
|---|---|
| Subcortex -> grey matter -> basal ganglion; white matter -> corticospinal tract, corticobulbar fibres (pass through internal capsule). | MED-C37-01 |
| Nuclei: caudate nucleus (CN), putamen, globus pallidus (GP: GPi, GPe), subthalamic nucleus (STN), substantia nigra (SN); corpus striatum = CN + putamen; lenticular nucleus = putamen + GP. | MED-C37-02 |
| Lesion -> hypokinetic movements: caudate -> chorea; putamen/striatum -> dystonia/athetosis; STN -> hemiballismus. | MED-C37-03 |
| Functions: complex motor activity; initiation and scaling of movement; cognitive part of motor activity; activity set for movement (planning, programming and initiation). Note: premotor cortex and supplementary motor area also involved in planning and programming. | MED-C37-04 |

Unasked points: **none found**.

### Book p584 / 03 PDF23

| Printed point / call-out | Question |
|---|---|
| General features: 1. all input from cortex -> striatum; 2. all output leave through GPi; 3. the only excitatory nucleus in BG: subthalamus. | MED-C37-05 |
| Nigrostriatal pathway: via D1 activate direct pathway; via D2 inhibits indirect pathway - together stimulating of cortex. | MED-C37-06 |
| Applied aspect: degeneration of NS pathway (Parkinson's disease) -> inhibition of cortex -> akinesia, bradyphrenia (slowness of thoughts). Disorders of BG: hyperkinetic vs hypokinetic (paucity of movement - down amplitude, slowness - unrelated to weakness/spasticity). Idiopathic PD: and m/c neurodegenerative disease; majority cases sporadic, elderly > 60 years. | MED-C37-07 |
| Idiopathic Parkinson's disease: and m/c neurodegenerative disease; majority cases: distribution sporadic, age elderly > 60 years. | MED-C37-08 |

Unasked points: **none found**.

### Book p585 / 03 PDF24

| Printed point / call-out | Question |
|---|---|
| Figure labels: stooped posture, masked facial expression, rigidity, forward tilt of trunk, flexed elbows and wrists, reduced arm swinging, slightly flexed hips and knees, trembling of extremities, shuffling short-stepped gait. | MED-C37-09 |
| Frequency row: PD tremor 4-6 Hz; essential tremor 5-12 Hz. | MED-C37-10 |
| PD column: at rest +/- re-emergent tremor, asymmetric, hands +/- legs, small writing (micrographia), progressive, family history uncommon (1%), extrapyramidal signs (bradykinesia, rigidity, loss of postural reflex) present, relieved by levodopa/dopamine agonists/anticholinergics, DBS site subthalamic nucleus or globus pallidus interna. Essential column: postural tremor, mostly symmetric, hands/head/voice, large and tremulous writing, stable or slowly progressive, family history common (>30%), EPS absent, relieved by alcohol/propranolol/primidone/topiramate/gabapentin/clonazepam, DBS ventral intermediate thalamus. | MED-C37-11 |
| PD relieving factors: levodopa, dopamine agonists, anticholinergics; essential tremor relieving factors include alcohol, propranolol, primidone, topiramate, gabapentin, clonazepam. | MED-C37-12 |

Unasked points: **none found**.

### Book p586 / Missing from supplied scan

| Printed point / call-out | Question |
|---|---|
| Printed p586 is absent from the supplied scan (it proceeds p585 -> p587); its bracketing content is the p585 PD-versus-essential tremor table and the p587 rigidity/akinesia list. Content verification of p586 remains unresolved, as with the missing p527 in Chapter 26. | MED-C37-13 |

Unasked points: **none found**.

### Book p587 / 03 PDF27

| Printed point / call-out | Question |
|---|---|
| Hypertonia - 2 types: cogwheel rigidity (rigidity + tremor) at wrist; lead pipe rigidity at elbow. Froment's sign: activity-induced increase in c/l rigidity (as printed on the page). | MED-C37-14 |
| Akinesia/bradykinesia: bradyphrenia; reduced arm swing (difficulty with limb movements); flexion hypertonia (stooped posture); short quick steps and freeze in between; festinant gait (narrow-based); micrographia; hypomimia (minimal expression); hypophonia (down voice); reduced blinking - glabellar tap sign positive. | MED-C37-15 |
| Note: atypical PD - b/l axial rigidity: difficulty turning in bed, rising from a chair (wheelchair sign); non-parkinsonian lesion having hypokinesia: hypothyroidism. (Visual hallucinations with fluctuating alertness are DLB features on p588.) | MED-C37-16 |
| Postural instability: unsteadiness and falls; pull test - patient falls backward (normal: takes 2-3 steps backwards to correct posture). | MED-C37-17 |
| Investigation: clinical diagnosis. | MED-C37-18 |
| MRI midbrain level: hyperintensities b/l in grey matter surrounded by hypointense red nuclei and crural fibres; absence of swallow tail sign (swallow tail sign d/t SN). | MED-C37-19 |
| PD patients can also have sensory symptoms (pain, anosmia), neuropsychiatric symptoms (depression > dementia) and gastrointestinal symptoms (dysphagia). | MED-C37-20 |

Unasked points: **none found**.

### Book p588 / 03 PDF28

| Printed point / call-out | Question |
|---|---|
| Atypical PD aka Parkinson plus syndromes: rapid progression, early onset dementia, symmetrical bradykinesia, facial dyskinesia. Classifications: tauopathy (PSP, CBD) and alpha synucleinopathy (MSA, DLB). | MED-C37-21 |
| Atypical PD: absence of tremor, unresponsiveness to L-dopa, rapidly progressive; DLB: dementia at presentation, visual hallucination, fluctuating alertness; CBD: myoclonus, cortical signs; PSP: falls d/t postural instability, dementia component, b/l axial rigidity, supranuclear gaze palsy; MSA: ANS symptoms, disproportionate cerebellar signs. | MED-C37-22 |
| PSP: falls d/t postural instability, dementia component, b/l axial rigidity, supranuclear gaze palsy. | MED-C37-23 |
| CBD: myoclonus, cortical signs; DLB: dementia at presentation, visual hallucination, fluctuating alertness; MSA: ANS symptoms, disproportionate cerebellar signs. | MED-C37-24 |
| MSA: 45-55 yrs; glial cytoplasmic inclusions (stain for alpha synuclein) - alpha synucleinopathy; REM sleep disorders (years before diagnosis); ANS predominant. | MED-C37-25 |
| MSA classification: MSA-P (80%) parkinson predominant; MSA-C cerebellar predominant; MSA-A/Shy-Drager syndrome (15%) ANS predominant. | MED-C37-26 |

Unasked points: **none found**.

### Book p589 / 03 PDF29

| Printed point / call-out | Question |
|---|---|
| Drugs: L-Dopa - peripheral metabolism is high; combined with: dopa decarboxylase inhibitor (carbidopa, benserazide); COMT inhibitors - not used now: tolcapone (hepatotoxic), entacapone (hepatotoxic, orange coloured urine); L-Dopa + dopa decarboxylase inhibitor is the combination started. | MED-C37-27 |
| All patients are started on L-dopa: small doses, multiple times, crushed and mixed with carbonated water. Symptoms non-responsive to L-dopa: freezing, falls, dysphagia, dysarthria, ANS symptoms. | MED-C37-28 |
| Symptoms non-responsive to L-dopa: freezing, falls, dysphagia, dysarthria, ANS symptoms. | MED-C37-29 |
| Side effects: nausea/vomiting, postural hypotension; motor fluctuations - wearing off (space drug without much gap), on/off, delayed onset of action, drug failure; dyskinesias - peak dose dyskinesia: choreiform movements (d/t high dose), off period dyskinesia: dystonia (d/t low drug concentration). | MED-C37-30 |
| Motor fluctuations (wearing off, on/off, delayed onset of action, drug failure) - to tackle: amantadine. | MED-C37-31 |
| Central anticholinergics: trihexyphenidyl; used in drug-induced PD. Dopaminergic agonists: found as replacement for L-dopa; disadvantages - dopamine dysregulation syndrome (neuropsychiatric manifestations: visual hallucinations, impulse control issues, addiction). | MED-C37-32 |

Unasked points: **none found**.

### Book p590 / Missing from supplied scan

| Printed point / call-out | Question |
|---|---|
| Printed p590 and p591 are absent from the supplied scan, so the dopaminergic-agonist material between the p589 disadvantages list and the p592 examples list cannot be visually verified; this follows the unresolved-missing-page precedent set by p527 in Chapter 26. | MED-C37-33 |

Unasked points: **none found**.

### Book p591 / Missing from supplied scan

| Printed point / call-out | Question |
|---|---|
| With p591 (and p590) absent from the supplied scan, the next visible sheet - p592 - opens with the dopaminergic-agonist examples list: pramipexole (antidepressant action also), ropinirole, rotigotine, apomorphine (used in rescue therapy, IV route). | MED-C37-34 |

Unasked points: **none found**.

### Book p592 / 03 PDF28

| Printed point / call-out | Question |
|---|---|
| Example: pramipexole (antidepressant action also), ropinirole, rotigotine, apomorphine - i. used in rescue therapy, ii. IV route. | MED-C37-35 |
| Amantadine: 3 mechanisms of action - dopaminergic agonist, anticholinergic, NMDA antagonist. Newer drugs: istradefylline (A2a antagonist - minimizes motor fluctuations), pimavanserin (5HTa antagonist). | MED-C37-36 |
| Treatment protocol: <60 yrs old + mild symptoms -> dopaminergic agonist; >60 yrs / significant disease present -> L-dopa + carbidopa. | MED-C37-37 |

Unasked points: **none found**.

### Book p593 / 03 PDF29

| Printed point / call-out | Question |
|---|---|
| Pain sensitive: dural venous sinuses, dura around vessels, large veins, circle of Willis, dural arteries (meningeal arteries), first few centimeters of medium sized vessels, pia mater, small cerebral vessels; pain insensitive: choroid plexus, ependyma. | MED-C38-01 |
| Classification: primary (benign, recurrent, no organic cause) - tension headache m/c, migraine 2nd m/c, TACs (eg cluster headache); secondary - systemic infection, brain tumour (rare). | MED-C38-02 |
| Dangerous headache - new onset headache after 55 yrs: seen in giant cell arteritis, associated with scalp tenderness, thick/nodular vessels, jaw claudication, PUO, ESR raised. | MED-C38-03 |
| Up intracranial tension: subacute, rapidly progressive over a few weeks, nocturnal awakening, vomiting (precede/relieve headache), up intensity by bending/coughing (seen in meningeal inflammation), blurring of vision - do direct ophthalmoscopy, if papilledema (+) -> imaging (MRI, MRA, MRV). | MED-C38-04 |
| Investigation line for the raised-ICP/dangerous-headache block: MRI, MRA, MRV (after direct ophthalmoscopy; papilledema (+) -> imaging). | MED-C38-05 |

Unasked points: **none found**.

### Book p594 / 03 PDF30

| Printed point / call-out | Question |
|---|---|
| Signs of up ICT: bradycardia, bradypnoea, hypertension, cardiac arrhythmia. | MED-C38-06 |
| Complication: herniation -> coning -> death; m/c site: uncus (inferior part of temporal lobe); signs: 3rd nerve palsy; Rx: decompression. | MED-C38-07 |
| Tension type headache (TTH): middle-aged female; 1/3rd cases associated with depression; holocranial band-like or pressure sensation; does not affect activities of daily living; no danger signs. Mx: acute NSAIDs; chronic amitriptyline (TCA) d/t associated depression (prophylactic). | MED-C38-08 |
| Against TTH: vomiting, photophobia, phonophobia, aggravated by movement. | MED-C38-09 |
| Migraine features: episodic; adolescence onset; severity up with age; F > m; family history +; not attributable to other diseases; normal systemic examination. | MED-C38-10 |
| Types: common (80%) - not associated with aura; classical (20%) - associated with aura. | MED-C38-11 |
| Aura: subjective, duration 15 mins - 1 hr; visual (m/c) - fortification spectra (m/c): zig-zag lines in peripheral vision, hazy spot in centre of vision; sensory (tingling and numbness); auditory; motor. | MED-C38-12 |

Unasked points: **none found**.

### Book p595 / 03 PDF31

| Printed point / call-out | Question |
|---|---|
| Stages of migraine: 1. prodrome -> 2. aura (zig-zag lines m/c) -> 3. headache -> 4. postdrome (lethargy, low mood/depressed). | MED-C38-13 |
| Prodrome: mood disturbance, irritability, depressive symptoms; aura: zig-zag lines (m/c); headache: unilateral -> holocranial, frontotemporal, throbbing/pounding type, nausea/vomiting (rare), photophobia/phonophobia/osmophobia, photopsia (flashing lights), scintillating scotomas; postdrome: lethargy, low mood/depressed. | MED-C38-14 |
| Headache stage duration: 4-72 hrs. | MED-C38-15 |
| Triggers: sleep deprivation (m/c) d/t serotonin-melatonin cycle disruption; menstruation d/t hormonal fluctuation; excess stress; traffic, climate, mosquito, henna, food etc. | MED-C38-16 |
| Common migraine: minimum 5 attacks lasting 4-72 hrs; characteristics (at least 2): unilateral, pulsatile, moderate to severe intensity, aggravated by routine physical activity/movement; clinical features (at least 1): nausea/vomiting (rare), photophobia/phonophobic; not attributed to another disorder. | MED-C38-17 |
| Classical migraine: at least 3 attacks lasting 4-72 hrs; aura - at least 3 of: gradual, duration <60 mins, reversible, headache within 60 mins of aura OR headache preceding/simultaneous with aura; not attributable to another disorder. | MED-C38-18 |
| Pathogenesis: vascular theory - vasoconstriction -> aura, vasodilation -> headache; serotonin theory - down level of serotonin. Important pathogenic cytokine: CGRP (calcitonin gene-related peptide); pathway: trigeminovascular complex. | MED-C38-19 |
| Serotonin theory Rx: 5-HT1b/1d agonist: triptans (DOC); 5-HT1F agonist: ditans (Lasmiditan). | MED-C38-20 |

Unasked points: **none found**.

### Book p596 / 03 PDF32

| Printed point / call-out | Question |
|---|---|
| Other types of migraine with aura: 1. ophthalmoplegic (transient 3rd nerve palsy, involvement of pupil +); 2. retinal (unilocular visual impairment); 3. basilar type (occipital involvement, ataxia, tinnitus, vertigo); 4. familial hemiplegic migraine: Ca2+ channelopathy. | MED-C38-21 |
| Acute attack - antiemetics: metoclopramide 5-10 mg/D; domperidone. | MED-C38-22 |
| Treatment table - mild: paracetamol, NSAID (naproxen 550 mg BD, ibuprofen 400 mg QID); moderate to severe: triptan (5HT1b/1d agonists) - eletriptan, rizatriptan, almotriptan, sumatriptan; very severe: sumatriptan 6 mg S/C x 2 doses intranasal, zolmitriptan intranasal. | MED-C38-23 |
| Moderate to severe: rizatriptan 5-10 mg (max: 30mg); sumatriptan 50-100 mg (max: 200mg); eletriptan; almotriptan. | MED-C38-24 |
| Disadvantages of triptan: C/I in cardiovascular or cerebrovascular disease; efficacy depends on Tmax; ineffective in migraine with aura. Note: ergotamine -> least recurrence of migraine. | MED-C38-25 |
| Prophylaxis: first line beta-blocker, valproate, topiramate; second line SNRI (venlafaxine), TCA; third line pizotifen (5-HTa antagonist), flunarizine (Ca2+ channel blocker), clonidine, candesartan. | MED-C38-26 |
| Note S/E: topiramate - weight loss, renal calculi; valproate - weight gain, liver disease, hyperammonemia, thrombocytopenia. | MED-C38-27 |
| Newer drugs and therapy: erenumab (CGRP antagonist), supraorbital transcutaneous stimulation, onabotulinum toxin A, greater occipital nerve block. | MED-C38-28 |

Unasked points: **none found**.

### Book p597 / 03 PDF33

| Printed point / call-out | Question |
|---|---|
| Trigeminal Autonomic Cephalalgias includes: cluster headaches, paroxysmal hemicrania, SUNCT (short-lasting unilateral neuralgic headache with conjunctival congestion and tear), hemicrania continua. | MED-C38-29 |
| Features: headache (short-lasting, severe, unilateral, neuralgic) + ipsilateral ANS symptoms; ANS symptoms at least 1: conjunctival congestion/lacrimation, nasal congestion/rhinorrhoea, eyelid edema, forehead and facial sweating, forehead and facial flushing, sensation of fullness in ear, miosis and/or ptosis. | MED-C38-30 |
| Cluster headache: young males (M > F); unilateral periorbital non-throbbing, stabbing/boring, excruciating (most painful headache), associated with ipsilateral ANS, nocturnal; frequency 1-8 attacks/day, symptoms for 8-10 weeks followed by symptom-free period; migrainous features (photophobia may be seen); 20% chronic symptoms; trigger alcohol, no cutaneous trigger. | MED-C38-31 |
| Duration of attack: 15 min - 3 hours (30 mins). | MED-C38-32 |

Unasked points: **none found**.

### Book p598 / 03 PDF34

| Printed point / call-out | Question |
|---|---|
| Management - treatment: 100% oxygen: treatment of choice, 12-15 L/min for 10-20 mins; sumatriptan 6 mg S/C. | MED-C38-33 |
| Prevention - short-term: steroid (DOC), verapamil, galcanezumab, greater occipital nerve injection; long-term: verapamil (best), topiramate, lithium. | MED-C38-34 |
| Paroxysmal hemicrania: F = m; type throbbing/boring/stabbing; severity excruciating; 1-30 attacks/day; duration 2-30 mins (average 5 mins); ANS symptoms +; no migraine-like feature, no alcoholic trigger, no nocturnal preponderance; treatment: indomethacin (reduce frequency of attack); no effective treatment during attack. | MED-C38-35 |
| SUNCT: M = F, unilateral, orbital or temporal pain, stabbing/throbbing, 3-200 attacks/day; duration of attack 5-240 sec; no migraine-like features; no alcohol preponderance; cutaneous trigger +, no refractory period. | MED-C38-36 |
| SUNCT management: treatment IV lignocaine; prevention lamotrigine or topiramate. | MED-C38-37 |
| Hemicrania continua: elderly females; continuous nature of unilateral background headache with episodic TAC; migrainous features +; ANS symptoms +; responsive to indomethacin. | MED-C38-38 |

Unasked points: **none found**.

### Book p599 / 03 PDF35

| Printed point / call-out | Question |
|---|---|
| Investigation of TAC: MRI brain; polysomnography; pituitary function test. | MED-C38-39 |
| Trigeminal neuralgia (00:55:15): F > m, 50-60 yrs; paroxysms of intense pain; unilateral d/t compression on superior cerebellar artery; bilateral d/t demyelination (multiple sclerosis); type brief, electric, shock-like superficial pain; tic douloureux - wincing d/t pain; maxillary (V2) and mandibular (V3) divisions; no objective sensory loss; cutaneous trigger +, refractory period +; investigation: specialized MRI. | MED-C38-40 |
| Treatment: carbamazepine >> lamotrigine - HLA B-1502 tested before administration of carbamazepine; subcutaneous botulinum toxin; microvascular decompression in medical refractory cases. Note: HLA B-5801 tested before administration of allopurinol. | MED-C38-41 |
| Unilateral: d/t compression on superior cerebellar artery; bilateral: d/t demyelination (multiple sclerosis). | MED-C38-42 |
| Glossopharyngeal neuralgia: aka eagle syndrome; d/t elongation of styloid process; type sudden, severe, short-lasting, recurrent bouts of pain; site tonsil bed, throat and angle of jaw; aggravation factors coughing, yawning, swallowing; associated with cardiac conduction abnormalities. | MED-C38-43 |

Unasked points: **none found**.

### Book p600 / 03 PDF36

| Printed point / call-out | Question |
|---|---|
| Evaluation protocol: papilledema + no neurologic signs except 6th nerve paresis: false localizing sign -> CT/MRI normal -> LP -> up opening pressure (>25 cm H2O) -> MRI: BIH or IIH. Papilledema seen in: hypertension, bradycardia, bradypnoea. | MED-C38-44 |
| LP: up opening pressure (>25 cm H2O) -> MRI: benign intracranial hypertension (BIH) or idiopathic intracranial hypertension (IIH). | MED-C38-45 |
| Modified Dandy criteria: symptoms of up ICP; no localising signs except 6th nerve palsy; normal CT, MRI findings; LP opening pressure >25 cm of H2O, CSF biochemistry/cytology normal; no other explanation for raised ICP. | MED-C38-46 |
| Secondary causes - drugs: outdated tetracycline, nalidixic acid, NSAIDs, retinol, danazol, tamoxifen; endocrine: steroid withdrawal, growth hormone, anabolic steroid. Primary empty sella syndrome: benign intracranial hypertension, thin rim of pituitary intact. | MED-C38-47 |
| Endocrine: steroid withdrawal, growth hormone, anabolic steroid. | MED-C38-48 |

Unasked points: **none found**.

### Book p601 / 03 PDF37

| Printed point / call-out | Question |
|---|---|
| Clinical features - headache m/c: type orthostatic, frequency daily, bilateral, worse in morning; aggravating factors coughing, straining; associated with retrobulbar pain. Visual symptoms: transient visual obscuration (2nd m/c), blackouts/grayouts, duration seconds to minutes, unilateral/bilateral. Tinnitus: 3rd m/c, pulsatile, heard in silent surroundings, unilateral > bilateral. | MED-C38-49 |
| Treatment: weight loss; acetazolamide (DOC); topiramate; repeated lumbar puncture (upto 20-30 ml): best option; surgery - optic nerve sheath fenestrations, shunting. | MED-C38-50 |
| Mx of acute up ICP: 1. elevate head; 2. mannitol; 3. sedation; 4. hyperventilation; 5. pressor therapy to maintain CPP >60 mmHg. | MED-C38-51 |

Unasked points: **none found**.

## Post-build verification

- `python3 build_content.py` embedded 1572 questions / 157 units / 37 live chapters into `pulse-medicine.html`.
- `python3 validate_content.py --embedded` passed exact source/HTML equality and all 57 roadmap flags.
- `tests/app_parsers.cjs` verified real offline-app parser compatibility across all 1572 questions and match bijections.
- `python3 -m unittest discover -s tests -v` — 9 unit tests PASS.

## Gate summary

Live chapter artifacts present: **37/57**. Embedded question total after build: **1572**; units: **157**. Ledger points: **1680**. Unasked points: **NONE** in the visually recorded inventory.

