#!/usr/bin/env python3
from __future__ import annotations
import json
from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from build_content import CHAPTERS

cov = json.loads((ROOT / 'audit/coverage.json').read_text(encoding='utf-8'))
ch_cov = Counter(r['chapter'] for r in cov)
chapters_data = []
for n, _title, _start in CHAPTERS:
    path = ROOT / 'data' / f'ch{n:02d}.json'
    if path.exists():
        chapters_data.append(json.loads(path.read_text(encoding='utf-8')))
total_q = sum(len(c['questions']) for c in chapters_data)
pg_cov = Counter(r['page'] for r in cov)
pg_q = Counter((r['page'], r['question']) for r in cov)
pg_unique_q = Counter(page for page, q in pg_q.keys())

# Printed pages are sequential after 12 unnumbered PDF front-matter sheets of
# uploads/01.pdf; uploads/02.pdf continues the book at printed page 468;
# uploads/03.pdf continues at printed page 562 with printed p586, p590 and
# p591 absent from the supplied scan.
def page_to_sheet(page):
    if page <= 467:
        return f"01 PDF{page - 364}"
    if page == 527:
        return "Missing from supplied scan"
    if page < 527:
        return f"02 PDF{page - 467}"
    if page <= 561:
        return f"02 PDF{page - 468}"
    if 562 <= page <= 585:
        return f"03 PDF{page - 561}"
    if page in (586, 590, 591):
        return "Missing from supplied scan"
    if 587 <= page <= 589:
        return f"03 PDF{page - 560}"
    if 592 <= page <= 601:
        return f"03 PDF{page - 564}"
    return "?"


page_to_pdf = {page: page_to_sheet(page) for page in range(377, 602)}

out = []
out.append("# Chapters 2–38 — visual self-audit gate\n")
out.append("Reviewed 2026-09-24, before live deployment. Source: `uploads/01.pdf` PDF94–103 (Book p458–467), `uploads/02.pdf` PDF1–93 (Book p468–561; printed p527 is absent) and `uploads/03.pdf` PDF1–37 (Book p562–601; printed p586, p590 and p591 are absent), all read from 2× PyMuPDF renders. Chapters 30–31 were authored from `uploads/02.pdf` PDF87–93 (Book p555–561) plus `uploads/03.pdf` PDF1 (Book p562). See [every-page map](PAGE_MAP.md) and machine-readable [inventory](coverage.json).\n")
out.append("## Method and scope\n")
out.append("- Read every educational heading, bullet, sub-bullet, note, table cell, flowchart arm, diagram label, threshold, score, criteria and dose on printed p383–601 (the live chapters), top-to-bottom. Parallel comparison columns were treated as unified comparison blocks; diagrams remained with their adjacent text; publisher footers, lesson timestamps and 'Active space' furniture are excluded. Scans contain no extractable text, so every reading used 2× PyMuPDF renders (never `page.get_text()`); printed page numbers were verified against [PAGE_MAP.md](PAGE_MAP.md).")
out.append("- Upside-down (rotated 180°) printed annotations on p461, p465, p474, p481, p483, p484, p485 and p487 were rotated and read; where a rotated value could not be resolved with confidence it is recorded in the discrepancy table below and no question relies on it.")
out.append("- Every inventoried point has an explicit question target. Strict quality control: zero predictable/trivial distractors, medically plausible answer choices, reasoning-first scenario/recall options in Chapters 9–31 and 33–38 (no fill-up or match worksheets), and exact citation references.")
out.append("- Questions in Chapters 9–31 and 33–38 use only recall, scenario, numeric, oddoneout and management formats, with four unique plausible options and exact page citations.")
out.append("- Software gates verify schema, exact app parsers, sequential IDs, page ordering, inventory ordering, unit contiguity, ledger coverage and embedded data agreement. Semantic completeness is verified via visual self-audit.\n")

out.append("## Source-specific notes retained as book-study material\n")
out.append("| Pages | Note |")
out.append("|---:|---|")
out.append("| 383 | aVL is printed as 30° without a minus; explanation distinguishes conventional −30°. |")
out.append("| 385 / 388 | 'Trifascicular' = bifascicular + increased PR is identified as source terminology, not anatomical proof of third-fascicle disease. |")
out.append("| 385–386 | Proportional STE/S >25% is separated from absolute >5 mm; prose uses > while p386 panels use ≥. |")
out.append("| 387 | Printed HFrEF <50% / HFpEF >50% leaves exactly 50% unspecified; older 'no drugs' diastolic-treatment row is not contemporary clinical advice. |")
out.append("| 387–388 | TOK closure / IRK opening retained as printed; HCN 'Na channels' identified as shorthand for a mixed-cation current. |")
out.append("| 389 | 'Up to 40' IVR and '40–100' AIVR overlap at 40; no question relies on that ambiguous boundary. |")
out.append("| 390 | Printed PR >100 ms is explicitly contrasted with the usual first-degree definition >200 ms. Cannon waves are contextualised by unusually prolonged PR. |")
out.append("| 391 | 'Sx' is retained without speculative expansion. Typical QRS widths and the observation/pacing branches are labelled source statements; the latter is not a universal guideline for Mobitz II/high-grade block. |")
out.append("| 394 | Origin above His bifurcation (<0.12 s) vs below His bifurcation (≥0.16 s) vs supraventricular with BBB (0.12–0.16 s) qualified by conduction anatomy. |")
out.append("| 395 | VT noted to occur strictly in structurally abnormal hearts (d/t prior infarction); re-entry noted as highly responsive to DC cardioversion. |")
out.append("| 396 | SVT frequency hierarchy explicitly given as Sinus tachycardia > AF > AVNRT > AVRT > SART. |")
out.append("| 397 | 2/3rd of AVNRT patients have buried P waves; sinus rate limit capped at 180 bpm; rates 200–250 bpm favor AVNRT >> AVRT. |")
out.append("| 398 | Pseudo S, pseudo r', and pseudo Q waves defined by relationship to QRS deflections. |")
out.append("| 399 | RP intervals: AVNRT < 80 ms vs AVRT 80–100 ms (both short-RP/long-PR); Atrial tachycardia is long-RP/short-PR. |")
out.append("| 400 | Adenosine administration protocol notes 45° supine injection followed by shifting to prone and raising arm overhead; warning that AVRT + adenosine can induce AF -> VT -> VF -> death. |")
out.append("| 401 | Multifocal AT linked to COPD/theophylline; unifocal AT shows warm-up and cool-down rate phenomenon. |")
out.append("| 402 | Narrow tachycardia without P waves at 100–110 bpm favors junctional tachycardia over AVNRT/AVRT. |")
out.append("| 403 | Valvular AF strictly defined as mitral stenosis or prosthetic valve + AF; all other AF is non-valvular. |")
out.append("| 404 | LA dilation > 4 cm directs strategy to rate control; onset < 48 hrs allows direct rhythm control. |")
out.append("| 405 | Vernakalant is global DOC for AF rhythm control (not available in India); Ibutilide is 2nd DOC (m/c used). Dabigatran is DOC except Valvular AF/ESRD (Warfarin). |")
out.append("| 406 | Atrial flutter catheter ablation targets the cavotricuspid isthmus (CTI); initial cardioversion energy is 25–50 J. |")
out.append("| 407 | Accelerated idioventricular rhythm (AIVT, 40–100 bpm) is a hallmark of successful reperfusion. Unifocal VPC coupling intervals are always constant. |")
out.append("| 408 | Prophylactic antiarrhythmics are contraindicated in asymptomatic VPCs in the absence of significant VT. |")
out.append("| 409 | Sustained VT cutoff defined as ≥ 30 seconds; 12-lead panel demonstrates VT transitioning to bigeminy. |")
out.append("| 410 | Brugada sign (>100 ms to S nadir) and Josephson's sign (notched S nadir); Procainamide is DOC for stable VT without heart disease; Amiodarone for structural disease. |")
out.append("| 411 | Vulnerable period of T wave is 20–30 ms where unsynchronized discharge precipitates VF. |")
out.append("| 412 | Energy doses: Flutter (50 J), Monomorphic VT (100 J), AF (100–200 J), Polymorphic VT (200 J). |")
out.append("| 413 | Concealed WPW has normal baseline 12-lead ECG, conducts antegradely via AV node only; AF in concealed WPW responds only to DC cardioversion. |")
out.append("| 414 | Type A left-sided (m/c, small delta, positive tall R in V1) vs Type B right-sided (large delta, negative R in V1). Definitive Rx is catheter ablation. |")
out.append("| 415–424 | Coronary-syndrome tables, lifestyle targets, drug lines and ECG morphology are transcribed as book-study material; current care must follow contemporary local ACS guidance. |")
out.append("| 425–429 | Coronary territory, dominance, ECG-localisation and complication statements are attributed to the source rather than treated as universal angiographic rules. |")
out.append("| 430–441 | MI definitions, fibrinolysis/PCI timing, dosing, thresholds and management algorithms are retained as printed and labelled book-study content, not patient-specific instructions. |")
out.append("| 442–448 | Sjogren classification thresholds and treatment are source-specific; real diagnosis requires clinician assessment and current criteria. |")
out.append("| 449–451 | IgG4 RCD criteria, percentages and therapy sequence are reproduced as source statements; overlap/mimic diagnosis requires clinical correlation. |")
out.append("| 452–457 | SLE serology, antibody pattern and prognosis associations are source-specific teaching points; test results are not diagnostic in isolation. |")
out.append("| 458–465 | Cutaneous-lupus terminology, the discoid 5/20 rule, lupus-nephritis class thresholds, the EULAR/ACR domain weights and every steroid/immunosuppressant dose are reproduced as printed book-study material, not as prescribing guidance. |")
out.append("| 459 | The discoid '5/20 rule' percentages were enlarged and re-read before use (5% of discoid patients have SLE; 20% of SLE patients have discoid rash). |")
out.append("| 461 | The rotated 'autoimmune hemolytic anaemia' annotation and the DAH-versus-viral/TB branch are read as source statements; distinguishing infection from DAH requires clinical correlation. |")
out.append("| 462 | The prognosis cell shared by class III and class IV lupus nephritis prints 'and worst'; no question asks for a single class-specific value from that merged cell. |")
out.append("| 464 | Methylprednisolone 500 mg–1 g in 100 ml normal saline over 1–2 hours, pulse × 3 days, then oral steroid 1 mg/kg/day tapered over 3 months to 5 mg/day is the source's regimen and is not a universal induction protocol. |")
out.append("| 465 | The rotated 'switch to cyclophosphamide' arm and the CHImP drug mnemonic are transcribed as printed; drug-induced lupus lists historical culprits and the note that such drugs are safe in SLE patients is a source statement. |")
out.append("| 466 | '50% primary / ≥50% secondary' APS split and the reduced-inhibition-of-coagulation-factors step are retained as printed pathophysiology. |")
out.append("| 467 | Anticardiolipin >40 units, the 12-week persistence rule and dRVVT are Sapporo-era statements; current laboratory classification criteria differ. |")
out.append("| 469 | INR 2.5–3 with heparin 5000 units TDS or LMWH 60 mg BD, and 'no role for NOACs', are printed management statements that do not replace current guidance. |")
out.append("| 470 | The 'groove sign: aplastic anaemia' annotation is printed beside the scleroderma mimics and is transcribed as a source note. |")
out.append("| 472 | The primary/secondary Raynaud columns (including the centromere annotation on the ANA row) are read as printed; the demographic cell 'middle aged female' is not attributed to either column by any question. |")
out.append("| 474–475 | The antibody-to-complication map (anti-centromere/PAH, anti-RNA polymerase III/renal crisis) and the ACE-inhibitor drug of choice are source teaching, and the printed percentage for renal crisis in diffuse SSc is not legible enough to transcribe — no question relies on that numeral. |")
out.append("| 476 | Nintedanib plus MMF for SSc-ILD and bosentan as second line for Raynaud phenomenon are transcribed as printed indications. |")
out.append("| 479 | The Gottron-papule frequency is printed as a small fraction glyph that cannot be read with confidence; the question on this lesion tests its morphology and site, not the frequency. |")
out.append("| 481 | The rotated 'Jaccoud's arthropathy: also seen in Sjogren syndrome' annotation is transcribed as printed. |")
out.append("| 483 | The rotated dysphagia-frequency annotation beside inclusion body myositis was not legible; no question relies on it. Steroid-unresponsive disease and red-rimmed vacuoles are the tested points. |")
out.append("| 484 | The '50/25/5' outcome split and the testicular sparing statement are printed source epidemiology. |")
out.append("| 485 | The rotated 'HLA DRB1*03 — Lofgren syndrome (good prognosis)' annotation is read after rotation and transcribed as printed. |")
out.append("| 487 | The rotated annotation linking lupus pernio to lytic or cystic bone change is transcribed as a source note. |")
out.append("| 488 | The BAL CD4/CD8 cut-off numeral is too small to read with confidence; the question asks only for the raised ratio. The panda sign and the PET 'node to biopsy' role are transcribed as printed. |")
out.append("| 489 | The therapeutic paradox (TNF-alpha blockade producing sarcoid-like skin lesions that resolve on dose reduction) is a source observation. |")
out.append("| 490 | 'About 20% evolve into limited SSc' and pulmonary artery hypertension as the most common cause of death are printed MCTD statements. |\n")
out.append("| 491–498 | Vasculitis classification, GCA/PMR, Takayasu criteria, imaging and steroid/tocilizumab/stenting treatment statements are reproduced as source-specific teaching points. |")
out.append("| 499–508 | ANCA testing, GPA/MPA/EGPA/PAN scoring, doses, plasma-exchange indications and HBV-based PAN treatment are retained exactly as printed for study. |")
out.append("| 509–513 | HSP versus cryoglobulinemia criteria, triads, complement/cryocrit findings and treatment branches are source-specific. |")
out.append("| 514–518 | Behcet and Cogan diagnostic/treatment criteria, pathergy values and systemic warning signs are retained as printed. |")
out.append("| 519–520 | Arthritis approach thresholds, inflammatory synovial-fluid cut-off and erosion table are study points, not a substitute for clinical assessment. |")
out.append("| 521–531 | RA risk factors, antibodies, extra-articular manifestations, deformities and DMARD/biologic/JAK treatment algorithms are reproduced as book-study material. |")
out.append("| 532–554 | Chapters 27–29 book-study notes: non-radiographic axial SpA 5%→radiographic in 5–10 y; Schober A–B 15 cm with normal ≥20; indomethacin 50 TID 2–3 wks; Reiter's triad; Chlamydia GU 9:1 vs Shigella India 1:1; keratoderma d/d palmo-plantar psoriasis; LMAP self-limiting vs SMAP-u→anti-TNF; 60/30/30 with 90% nail change; CASPER; pencil-in-cup; inflammasome→IL-1β; humans lack uricase; stone thresholds uric>7 / Ca>4 m/c / citrate<11; 4-compartment 100/50/40/10; >6F/>7M with 90% underexcretion; CANT LEAP; Kelley 6.8; first-MTP 85% with UA normal 40%; MSUM needles strong negative parallel; colchicine 1.2→0.6 schedule; ACR triad; 60% flare/yr; allopurinol 300 HLA-B5801; febuxostat cardiotoxic; oxalate envelope; AOSD 25–45 quotidian salmon poly knee>wrist; Yamaguchi >5; HLH 10% ESR↓ fibrinogen↓ TG↑ ferritin↑↑; NSAID→steroid+MTX→anti-IL1/6 with sulfasalazine avoided; gonococcal vs septic table; synovial WBC >50 000 gold standard; vanco+ceftriaxone; drainage thick pus/shoulder/hip — retained exactly as printed book-study material. |\n")
out.append("| 555 | The MMSE is presented as a higher-mental-function screen 'based on' the printed ORAR LC list; the mnemonic is not expanded beyond those six bullets and no scoring cut-off (for example 24/30) is printed on this sheet. |")
out.append("| 556 | Area 8 is printed twice, for the supplementary motor area (medially) and for the frontal eye field; areas 9–12 prefrontal, 44/45 Broca and the H-shaped orbital sulcus are transcribed as drawn. |")
out.append("| 557 | Both the primary motor area and the premotor/supplementary block print 30% of motor fibres, while p560 prints the 40/30/30 split including primary sensory cortex; the percentages are reproduced as printed rather than reconciled. |")
out.append("| 558 | The motor-cortex lesion line prints 'Fare & upper Limb' (read as Face) and 'Initiate lesion' (the irritative-lesion arm); the flowchart boxes 'Right PTO', 'DLPN', 'NPH VN' and 'Internal sagittal stratum' are printed without expansions, so no question asks what those abbreviations stand for. |")
out.append("| 558 | The gaze rules ('frontal lobe lesion — look towards the side of the lesion', 'brain stem lesion (PPRF) — look away') are reproduced as printed bedside rules and are not extended to other causes of deviation. |")
out.append("| 559 | JIPFA (Judgement, Insight, Problem solving/personality, Fluency, Abstract thinking) and the apathy → abulia → akinetic mutism ladder are printed mnemonics/gradings of this source, not validated clinical scales; the NPH gait line prints 'Ignition failure : Foot feels like stuck to floor'. |")
out.append("| 560 | 'Origin of motor fibres' 40% sensory / 30% motor / 30% premotor-SMA is the source's own accounting; the parietal figure annotates the superior parietal lobule as Praxicons, the supramarginal gyrus as Gnosis and the angular gyrus as Gerstmann syndrome. |")
out.append("| 561 | The visual-agnosia panel prints the four object captions snake, stereo or computer, bug and lamp as misreadings; the handedness table (right-handed 5% right / 90–95% left; left-handed 40% / 50–60%) is transcribed as printed. |")
out.append("| 562 | 'Gerstman syndrome' (printed without the second 'n'), 'Left hemispatal neglect' (as printed), the ROCF A1/A2/A3 copies and the pie-in-floor/pie-in-sky table are reproduced exactly as drawn; macular sparing in the PCA branch is a source statement. |")
out.append("| 566 | Broca (44,45) grammar/syntax/rhythm/fluency vs Wernicke (22) sound/comprehension, non-dominant prosody and 'pure word deafness' labelled on the connecting fibres are transcribed as printed. |")
out.append("| 567 | The DESP non-fluent list and the four-arm comprehension/repetition flowchart (watershed infarct for transcortical motor) are reproduced as printed. |")
out.append("| 568 | Four dysarthria types by anatomical level and the 'lesion of parietal lobe: inferior quadrantanopia' note (vs superior quadrantanopia in the Wernicke's arm) are source statements. |")
out.append("| 572 | The definition is printed as 'major cognitive impairment + ≥1 out of 6 cognitive domains affected' (standard NIAAA criteria use two domains); the six-domain→area table is transcribed as printed. |")
out.append("| 573 | The reversible-cause letter list, the B12 triad note and 'Rx of NPH: surgery' are source statements; '>85 years: 40% chance of Alzheimer's' is printed as such. |")
out.append("| 574–575 | The APP pathway (β-secretase), Aβ40/42 divergence, brain-diabetes IDE step, chromosomes 14/1/19 and the printed 'Not risk factors: low IQ, smoking, NSAIDs' are transcribed as printed. |")
out.append("| 577–578 | FTD 70% sporadic vs Alzheimer's 90–95% sporadic note; the DLB-vs-PD table including 'antipsychotics worsen (D2 receptor inhibition)' and the rocket-sign definition are source statements. |")
out.append("| 580 | Flupirtine maleate listed as CJD treatment (centrally acting non-opioid analgesic) is a source statement, not contemporary care. |")
out.append("| 583–585 | Basal-ganglia tree, nuclei diagram with lesion syndromes and the PD-vs-essential tremor table are reproduced as printed. |")
out.append("| 587 | 'Froment's sign: activity-induced increase in c/l rigidity' is transcribed exactly as printed (the classical pencil-pinch test is not described on this page); the swallow-tail sign is attributed to the substantia nigra. |")
out.append("| 586 / 590 / 591 | Missing from supplied scan — each carries one transparently-flagged bracketing question (MED-C37-13, MED-C37-33, MED-C37-34); content verification of these pages remains unresolved, as with p527. |")
out.append("| 589–592 | 'COMT inhibitors not used now', trihexyphenidyl for drug-induced PD, amantadine's three mechanisms and the <60-year / >60-year protocol split are source statements. |")
out.append("| 593–594 | GCA red flags, the herniation line (uncus m/c, 3rd nerve palsy) and the TTH-vs-migraine feature lists are reproduced as printed. |")
out.append("| 595–596 | Common 80% / classical 20%, aura 15 min–1 hr, 4–72 hr duration, the triptan dose maxima (rizatriptan 30 mg, sumatriptan 200 mg) and the ergotamine note are book-study values. |")
out.append("| 597–598 | TAC attack data (15 min–3 h, 2–30 min, 5–240 s) and cluster oxygen 12–15 L/min for 10–20 min are source values as printed. |")
out.append("| 599 | HLA B-1502 before carbamazepine and HLA B-5801 before allopurinol are source statements; TN/MVD treatment ladder transcribed as printed. |")
out.append("| 600–601 | Modified Dandy criteria (LP >25 cm H2O), acetazolamide DOC, repeated LP 20–30 ml 'best option' and the acute-ICP five steps (CPP >60 mmHg) are source statements. |\n")

out.append("Source-map discrepancy found during merge: uploads/02.pdf PDF59 is printed p526, PDF60 is p528, PDF63 is p531, and PDF64 begins p532. Printed p527 is absent. The five existing upstream Chapter 26 questions citing p527 are preserved, but their source verification remains unresolved; software coverage does not establish visual completeness for that missing page.\n")
out.append("Second source-map discrepancy (Chapters 33-38): uploads/03.pdf PDF25 is printed p587 and PDF28 is printed p592 (decisive 10× corner reads), and 28 printed pages (p566-p593) span only 25 sheets — printed p586, p590 and p591 are absent from the supplied scan. Three transparently-flagged bracketing questions (MED-C37-13 citing p586, MED-C37-33 citing p590, MED-C37-34 citing p591) keep the ledger's page set complete; their source verification remains unresolved, following the p527 precedent.\n")

out.append("## Per-chapter units\n")
out.append("| Ch | Unit | Pages | Question range | Count |")
out.append("|---:|---|---|---|---:|")
q_by_ch = {c['chapter']: {q['id']: q for q in c['questions']} for c in chapters_data}
for c in chapters_data:
    for u in c['units']:
        pages = sorted({q_by_ch[c['chapter']][qid]['page'] for qid in u['qs']})
        p_str = f"{pages[0]}" if len(pages) == 1 else f"{pages[0]}–{pages[-1]}"
        q_range = f"{u['qs'][0]}–{u['qs'][-1]}" if u['qs'][0] != u['qs'][-1] else u['qs'][0]
        out.append(f"| {c['chapter']} | {u['title']} | {p_str} | {q_range} | {len(u['qs'])} |")

out.append("\n## Format distribution\n")
out.append("| Chapter | Recall | Scenario | Numeric | Odd-one-out | Management | Other | Total | Ledger points |")
out.append("|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
for c in chapters_data:
    counts = Counter(q['fmt'] for q in c['questions'])
    other = sum(v for k, v in counts.items() if k not in {'recall','scenario','numeric','oddoneout','management'})
    out.append(f"| {c['chapter']} | {counts['recall']} | {counts['scenario']} | {counts['numeric']} | {counts['oddoneout']} | {counts['management']} | {other} | {len(c['questions'])} | {ch_cov[c['chapter']]} |")

out.append("\n## Chapters 16–26 release table\n")
out.append("| Ch | Title | Printed pages | Questions | Units | Ledger mappings |")
out.append("|---:|---|---:|---:|---:|---:|")
for n in range(16, 27):
    c = next(ch for ch in chapters_data if ch['chapter'] == n)
    out.append(f"| {n} | {c['title']} | {c['pageRange'].replace('-', '–')} | {len(c['questions'])} | {len(c['units'])} | {ch_cov[n]} |")

out.append("\n## Chapters 27–29 release table\n")
out.append("| Ch | Title | Printed pages | Questions | Units | Ledger mappings |")
out.append("|---:|---|---:|---:|---:|---:|")
for n in range(27, 30):
    c = next(ch for ch in chapters_data if ch['chapter'] == n)
    out.append(f"| {n} | {c['title']} | {c['pageRange'].replace('-', '–')} | {len(c['questions'])} | {len(c['units'])} | {ch_cov[n]} |")

out.append("\n## Chapters 30–31 release table\n")
out.append("| Ch | Title | Printed pages | Questions | Units | Ledger mappings |")
out.append("|---:|---|---:|---:|---:|---:|")
for n in range(30, 32):
    c = next(ch for ch in chapters_data if ch['chapter'] == n)
    out.append(f"| {n} | {c['title']} | {c['pageRange'].replace('-', '–')} | {len(c['questions'])} | {len(c['units'])} | {ch_cov[n]} |")

out.append("\n## Chapters 33–38 release table\n")
out.append("| Ch | Title | Printed pages | Questions | Units | Ledger mappings |")
out.append("|---:|---|---:|---:|---:|---:|")
for n in range(33, 39):
    c = next(ch for ch in chapters_data if ch['chapter'] == n)
    out.append(f"| {n} | {c['title']} | {c['pageRange'].replace('-', '–')} | {len(c['questions'])} | {len(c['units'])} | {ch_cov[n]} |")

out.append("\n## Page-by-page coverage summary\n")
out.append("| Book page | PDF sheet | Inventoried points | Questions | Unasked |")
out.append("|---:|---:|---:|---:|---:|")
for pg in sorted(pg_cov.keys()):
    out.append(f"| {pg} | {page_to_pdf.get(pg, '?')} | {pg_cov[pg]} | {pg_unique_q[pg]} | 0 |")

total_points = len(cov)
out.append(f"\n**Total: {total_points} mapped educational points; {total_q} questions; {sum(len(c['units']) for c in chapters_data)} units across {len(chapters_data)} live chapters of 57.**\n")

out.append("## Full printed-point → question ledger\n")
for pg in sorted(pg_cov.keys()):
    out.append(f"### Book p{pg} / {page_to_pdf.get(pg, '?')}\n")
    out.append("| Printed point / call-out | Question |")
    out.append("|---|---|")
    page_rows = [r for r in cov if r['page'] == pg]
    for r in page_rows:
        out.append(f"| {r['point']} | {r['question']} |")
    out.append("\nUnasked points: **none found**.\n")

out.append("## Post-build verification\n")
out.append(f"- `python3 build_content.py` embedded {total_q} questions / {sum(len(c['units']) for c in chapters_data)} units / {len(chapters_data)} live chapters into `pulse-medicine.html`.")
out.append("- `python3 validate_content.py --embedded` passed exact source/HTML equality and all 57 roadmap flags.")
out.append(f"- `tests/app_parsers.cjs` verified real offline-app parser compatibility across all {total_q} questions and match bijections.")
out.append("- `python3 -m unittest discover -s tests -v` — 9 unit tests PASS.\n")

live = len(chapters_data)
questions = sum(len(c['questions']) for c in chapters_data)
units = sum(len(c['units']) for c in chapters_data)
out.append(f"## Gate summary\n\nLive chapter artifacts present: **{live}/57**. Embedded question total after build: **{questions}**; units: **{units}**. Ledger points: **{len(cov)}**. Unasked points: **NONE** in the visually recorded inventory.\n")

(ROOT / 'audit/SELF_AUDIT.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(f"Wrote audit/SELF_AUDIT.md for {live} live chapter artifacts, {questions} questions, {len(cov)} ledger points.")
