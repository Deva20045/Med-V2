# Read Notes — Chapters 55–57 (Book p686–702)

## Scope and method

- Source sheets: `uploads/04.pdf` PDF61–76 (= Book p686–701) and `uploads/05.pdf` PDF1
  (= Book p702). None of the sheets carries a text layer.
- Visual (image) review was **not** available in this session, so every page was read
  line-to-line from RapidOCR (rapidocr_onnxruntime) transcripts of 3x/4x renders
  (`.audit-render/ocr_0461.txt … ocr_0476.txt`, `ocr_051.txt`), and every uncertain
  number, label or table cell was re-read from 8x–100x crops of the PDF pages
  (`tools/crop_ocr.py` plus pixel-level glyph inspection via contrast-boosted
  ASCII renders). **No claim in this file or in the questions rests on visual
  confirmation of the scans; everything rests on OCR plus glyph-level re-reads.**
- Chapter spans verified from printed page numbers OCR'd on every sheet:
  Ch55 = p686–690, Ch56 = p691–699, Ch57 = p700–702. Sheet 74 prints its page
  number as "669" (a printed quirk; position/content confirm it is p699).

## Systematic OCR decode key (digits misread by RapidOCR on these sheets)

`a`→2 or 4, `l`/`I`→1, `o`→0, `g`→9, `s`→5, `b`→6; decimal points often dropped
("0.as" = 0.25, "4-S" = 4–5, "a4" = 24, "so%" = 50%, "18s/o" = 185/110,
"7lbo%" = 70%). Several lines on p694, p695 and p696 OCR right-to-left
(mirrored); they were re-read by horizontally flipping the crop
(e.g. the mirrored line on p696 decodes to "B/L VII Nerve palsy + One and half
syndrome : Fifteen and half syndrome").

## Resolved ambiguities (crop/glyph re-reads)

- **p686 ABCD² risk table (High 6–7 row):** 4x OCR read "8.1 / 1a / 18". Glyph-level
  re-read of the cells at 24x–48x resolves the row as **8.1 / 11.7 / 17.8** for
  2/7/90-day risk; the Moderate row reads 4.1/5.9/9.8 and the Low row 1.0/1.2/3.1.
  These match the Johnston Lancet-2007 ABCD² validation table the book reproduces.
- **p686 ABCD² points column:** single digits were unreadable to OCR; glyph re-reads
  of each cell confirm Age>60 → 1, BP ≥140/90 → 1, speech disturbance without
  weakness → 1, unilateral weakness → 2, 10–59 min → 1, ≥60 min → 2, diabetes → 1.
- **p687 "Recent myocardial infarction (within …)":** the parenthetical is ~2.5 pt
  print. Glyph re-read at 80x shows "4", "-", serifed "1", closed oval "0" →
  **"(within 4-10 wks)"** as printed.
- **p687 "Pathology: Patchy weakness / Lipohyalinosis" (Lacunar column):** the
  "Patchy weakness" label sits to the right of "Pathology:" on the same printed
  line; both retained as printed.
- **p688 Insular ribbon timing:** reads varied ("6-48", "%-48", "lo-48"); the
  cleanest 12x read is **"(6-48 hrs)"**. Obscuration of lentiform nucleus prints
  "(8-24 hrs)" ("a4" = 24).
- **p688 timeline:** "Day 1" and "Day 24" are printed; the middle label is a
  handwritten active-space annotation ("sI hoa", unreadable). Caption below the
  timeline: "Hemorrhagic transformation of stroke".
- **p689 top block:** "conditions producing white matter lesions: CADASIL disease
  (Cerebral Autosomal Dominant Arteriopathy with Subcortical Infarcts
  Leucoencephalopathy). · microbleeds : Cerebral amyloid angiopathy." The lead-in
  line begins at the top edge of p689; nothing of this list prints on p688 (p688
  ends with the early-CT-findings list, verified by ink-profile scan).
- **p689 LACUNAR STROKE DEFINITION:** the definition text is a handwritten
  active-space note, partly legible at 24x with contrast boost:
  "…cm size infarct in a 30-300 μm vessel d/t lipohyalinosis". Quiz content uses
  the printed 30–300 μm / lipohyalinosis data; the handwritten fragment is
  disclosed, not quizzed.
- **p689 SVD-marker MRI modality row:** "Recent small subcortical infarct → DWI",
  "White matter hyperintensity → FLAIR", "Lacune → FLAIR", "Perivascular space →
  T1/FLAIR" (OCR "TIVFLAIR", best glyph read "T1/FLAIR"), "Cerebral microbleeds →
  T2'/SWI". The PVS modality label is the least certain read on the page and is
  not quizzed as a differentiator.
- **p691 "motor nuclei of CN : 3,4,b,la"** decodes with the key to **3, 4, 6, 12**
  (consistent with the 4M midline mnemonic). "Spinal nucleus of trigeminal nerve :
  Sensory fibers upto C?" — the level glyph is at the scan's resolution limit
  ("ca"); the anatomical extent printed in this diagram is not quizzed as a number.
- **p692 Note:** the "Note:" block contains only faint unreadable handwriting
  (active space). Disclosed, not quizzed.
- **p694 "Pseudo abducent pupil":** printed as such (glyph re-read shows two
  descender-bearing glyphs = "pupil", not "palsy"). The standard term for this
  Parinaud finding is pseudo-Abducens palsy; the book's printed wording is
  preserved and the question quotes it as printed.
- **p694 V4:** "Vascular origin : V4 segment of vertebral artery → Posterior
  Inferior cerebellar Artery (PICA)" (4x read "V," = V4 confirmed by crop).
- **p695 "Spared" CN list:** prints at ~2 pt; OCR "I, a, 3, lo, ll, la". With the
  decode key and the medial/lateral medulla organisation the list is
  **1, 2, 3, 4, 6, 12** (CN I, II above the brainstem; III, IV midbrain; VI pons;
  XII medial medulla — all outside the lateral medulla). Recorded as best-read;
  the list is quizzed as "CN 1,2,3,4,6,12 are spared" with this note disclosed.
- **p695 "Cervical Sympathetic chain (xill CN)":** the parenthetical is unreadable
  to certainty at maximum zoom ("XII CN" best read); the row content (Horner's
  syndrome with its features) is what prints clearly and is what got quizzed.
- **p696 bottom line:** mirrored print, flips to "B/L VII Nerve palsy + One and
  half syndrome : Fifteen and half syndrome."
- **p697 Avellis vs Jackson etiology row:** "Infarct" and "Tumors" print stacked
  in the row (Avellis — infarct; Jackson — tumors, best-read layout). The
  unambiguous cells (site, structures, clinical features) carry the questions.
- **p698 anatomy figure labels:** "18. Raphe Nucleus" and "8. Inferior Cerebellar
  Peduncle" (two consistent reads); "10. Root of CN VI" and "12. Root of CN V"
  (OCR cannot separate V/VI; #10 sits medial with the abducens nucleus, #12
  lateral with the spinal nucleus of V — recorded as printed best-read). A "6T"
  mark near label 12 is an unreadable handwritten annotation. "Note: No Tectum
  in the Pons".
- **p698 Raymond mnemonic:** prints "(SH Syndrome)" (glyph re-read shows an
  S-curve, not a digit), matching the printed FSH (Millard-Gubler), FGH (Foville)
  and ASH (Marie-Foix) letter mnemonics on p698–699.
- **p700 BP lines:** glyph re-reads give "BP ≥220/110 mmHg" and "BP >185/110 mmHg
  when thrombolysis/thrombectomy planned" (OCR "7aao/llo" = ≥220/110; the ≥ is
  read as "7"). "labetalol ao mg" = 20 mg; "Tenecteplase O.as mg/kg" = 0.25 mg/kg.
- **p701 MRI protocol step 2 table:** prints "White if patient presents after
  4-6 days" / "Black if patient presents within 4-10 days" as two side-by-side
  cells (best-read); the column headers are too faint to resolve with certainty,
  so the specific day-values are disclosed here and not used as the tested
  differentiator — the tested point is the DWI-white vs FLAIR-black mismatch
  meaning "very new onset → thrombolysis candidate".
- **p701 perfusion thresholds:** "<10 ml/100 g/min → Infarcted tissue",
  ">20 ml/100 g/min → Normal perfusion" (glyph re-read shows "2" then "0";
  OCR "aa"), "10-20 ml/100 g/min → Penumbra region".
- **p702 asymptomatic carotid threshold:** prints ">70% block in asymptomatic
  patient" (OCR "7lbo%"; the "7" is a clean seven glyph, an extra mark sits
  between 7 and 0 — best-read ">70%", disclosed).
- **p702 carotid stenting parenthesis:** "(No risk of procedural MI used in high
  risk cardiac cases)" — best-read "(No risk of procedural MI; used in high-risk
  cardiac cases)". "Target LDL<I0o" = <100.
- **Handwritten active-space annotations** (partly legible): p686 DWI note near
  the TIA box; p688 timeline middle label; p689 lacunar DEFINITION; p692 Note;
  p698 "6T". All disclosed here; none quizzed.

## Page-by-page printed content inventory (condensed)

- **p686** Approach to Stroke title; stroke definition (abrupt FND ≥24 hrs);
  TIA definition (<1 hr, no infarction); DWI MRI outcome rule; ABCD² score
  (components + points; Low/Moderate/High risk table at 2/7/90 days); Notes on
  dual antiplatelet therapy.
- **p687** Causes & Pathology of Stroke; CAUSES 1. Atherosclerotic → Arterial /
  venous; CVT (Acquired/Inherited; symptoms ↑ICT); Ischaemic 85% vs Haemorrhagic
  15% (SAH/EDH/IVH → neurosurgeon); Thrombotic / Embolic / Lacunar features;
  Cardioembolic vs Artery-Artery; Thrombotic vs Embolic table; CT Imaging in
  stroke (hypodense/hyperdense lesion; ischemic stroke, hemorrhagic stroke,
  subarachnoid hemorrhage images).
- **p688** 2. Non-Atherosclerotic (moya-moya "puff of smoke" ICA vasculopathy,
  vasculitis, Fabry's, FMD, carotid artery dissection, dissection, Takayasu);
  PATHOLOGY causative factors (ATP depletion → Na+-K+ ATPase pump failure →
  glutamate release → calcium entry → liquefactive necrosis) with Day 1 → Day 24
  timeline (hemorrhagic transformation); Management goals; INVESTIGATIONS MRI>CT;
  early CT findings 1-3 with images.
- **p689** conditions producing white matter lesions (CADASIL; microbleeds →
  CAA); LACUNAR STROKE (definition note; etiology elderly F>M, HTN; types table;
  SVD markers on MRI with modalities; example image/schematic figures).
- **p690** Ataxic Hemiparesis = dysarthria with clumsy hands; CPC/CS/DRTC
  pathway diagram; spinocerebellar fibres degenerate in Friedreich's ataxia;
  lesion at basis pons.
- **p691** Brainstem Stroke; crossed hemiplegia; cortical vs internal capsule;
  midline 4M vs lateral 4S structure lists.
- **p692** Midbrain anatomy (anterior and posterior views; superior colliculus
  level cross-section; middle 3/5th of crus cerebri; motor/sensory root of
  trigeminal labels in the anterior view).
- **p693** Inferior colliculus level; ventral midbrain syndromes (P1 segment of
  PCA): Weber, Claude, Benedikt = Weber + Claude.
- **p694** Dorsal midbrain (Parinaud) — pinealoma m/c, features list; Nothnagel;
  peduncle rule (superior → midbrain, middle → pons, inferior → medulla);
  Wallenberg/LMS etiology (V4 → PICA).
- **p695** LMS features 1–5; CN nucleus table; sensory/motor findings; Horner's
  diagram (central/pre-ganglionic/post-ganglionic).
- **p696** Medial medullary (Dejerine) components; horizontal gaze pathway
  (FEF → PPRF → VI nucleus); MLF/PPRF lesion combinations (INO, one-and-a-half,
  eight-and-a-half, fifteen-and-a-half).
- **p697** Cruciate paralysis (early UL decussation; brachial diplegia; one arm +
  opposite leg); Note crossed hemiplegia; Avellis vs Jackson table.
- **p698** Pontine anatomy (23 labelled structures; Note: no tectum in pons);
  vascular territories; Millard-Gubler (FSH) and Raymond (SH) syndromes.
- **p699** Foville (FGH); Marie-Foix (ASH); Locked-in syndrome; Top of basilar
  occlusion; 5 D's of posterior stroke presentation.
- **p700** Management of Stroke; goals; Immediate Management; CT Protocol
  (updates) table; Steps 1–4 with labetalol; Contraindications to thrombolysis.
- **p701** Step 5 CT (plain CT, CT angiography); MRI Protocol for wake-up stroke
  (DW MRI; T2 FLAIR; DWI-FLAIR mismatch → ADC; thrombolysis candidate); Step 4
  Perfusion imaging (PWI-DWI mismatch, infarct core, penumbra; CBF thresholds).
- **p702** After 24 Hours: repeat imaging; anticoagulation (valvular AF →
  warfarin only; mitral stenosis, prosthetic valve); antiplatelet (single vs
  dual, indications); carotid endarterectomy vs stenting (indications); cholesterol
  management (target LDL <100).
