# Read notes — Chapters 51–54 (Book p660–685)

Line-to-line visual extraction of `uploads/04.pdf` PDF35–60 (Book p660–685), rendered
at 3× in `.audit-render/r04_35_3x.png` … `r04_60_3x.png`. All 26 sheets are upright
portrait pages (571–612 × 770–792 pt), so no prerotate was needed, unlike PDF27 in the
previous release. Scans carry no text layer; RapidOCR passes at 4×
(`.audit-render/ocr_04NN.txt`, via `tools/ocr_pages.py`) were used only as a mechanical
first pass and every line was confirmed visually. Printed page numbers were read on each
sheet: PDF35 prints 660 and PDF60 prints 685, with no missing printed page in between.

Chapter spans: Ch51 p660–667 = PDF35–42 · Ch52 p668–673 = PDF43–48 · Ch53 p674–680 =
PDF49–55 · Ch54 p681–685 = PDF56–60. Ch55 (Approach to Stroke) begins at p686 = PDF61
and is not in this release; `uploads/04.pdf` continues to PDF76 and `uploads/05.pdf`
holds the single closing sheet (p702), so the whole remaining roadmap span p686–702 is
available for the next release.

## Book p660 — 04 PDF35 — Ch51 title page "DISEASES OF SPINAL CORD"

- Myelopathy definition and the Compressive / Non-compressive split; Compressive Myelopathy — Chronic course; 00:00:17 marker.
- Flowchart: Intramedullary versus Extramedullary, the latter divided into Intradural and Extradural (m/c), each with a Cause column.
- Three-figure block: axial canal section (Dura mater, Epidural space, Subarachnoid space, Arachnoid membrane, Extradural tumor, Intramedullary tumor, Intradural-extramedullary tumor) captioned "Types of compressive myelopathy"; three sagittal MRIs a/b/c captioned "Tumors of spinal cord"; three lower schematics plus an MRI marked "IVDP".
- Disc pathology line reads "IVDP (m/c)" — an earlier 4× OCR pass misread the parenthetical as "(m/e)"; re-read at 3× and 6× confirms (m/c).

## Book p661 — 04 PDF36 — Ch51

- Clinical features list with the brace "Definitive symptoms of compression"; band-like sensation glossed as Hyperesthesia, example "Umbilicus if T10 level is involved".
- Note table Neurogenic claudication vs Vascular claudication, nine rows; all cells re-read in the 3× render (OCR interleaved the two columns).
- Examination findings: HMF/CN normal; motor UL "Power intact (S/S)"; LL reduced power with "B/L UMN features"; sensory "Spinothalamic tract loss + Posterior column loss → Loss"; reflexes exaggerated; plantar extensor; "Bowel & bladder involvement : In intramedullary compression".

## Book p662 — 04 PDF37 — Ch51

- Level-localization bullets, including "Reflex level : Best localizing value" and the Beevor block (upper T7–T9, lower T9–T12).
- "Extramedullary vs intramedullary compression" table, twelve rows, with Centrifugal/Centripetal damage directions; every +/- cell verified visually.

## Book p663 — 04 PDF38 — Ch51

- Full-page cord cross-section "at the mid thoracic level" with CTLS lettering in the posterior columns and SLTC lettering in the spinothalamic areas; brackets for Distal limb movements and Axial and proximal limb movements.
- Root pain/girdle pain vs Lhermitte sign table (Character, Exacerbated by, Cause, Useful for localization).
- Bullets: funicular pain, suspended sensory loss, dissociative sensory loss, early LMN finding at the AHC, CTLS lamination with "Therefore sacral sparing in intramedullary", central bowel/bladder fibres, peripheral corticospinal fibres, CSF protein, cervical sympathetic extension → Horner's syndrome.

## Book p664 — 04 PDF39 — Ch51

- Conus medullaris v/s Cauda Equina table (ten rows). The Involvement cells are printed "B/L S3 → C1 inside spinal cord" and "Asymmetrical L2 → C1 roots" [sic — the coccygeal segment is printed C1, matching the C0/C1 inconsistency already recorded for Ch50]; verified with a 6× crop `.audit-render/v0439_100_200_6x.png`.
- Epiconus block (L4, L5, S1, S2; hip flexion/adduction spared; thigh spared; Bladder : UMN).
- Non Compressive Myelopathy with the VITAMIN mnemonic; Vascular & demyelinating, Inherited, Toxin, Autoimmune, Metabolic (SACD with its four differential diagnoses).

## Book p665 — 04 PDF40 — Ch51

- Infection and Neoplasia close the mnemonic list.
- ACUTE TRANSVERSE MYELITIS definition, the "Levels of principal dermatomes" figure with its fifteen-row table (C5 to S2,3,4), the seven-item Causes list with the brace "Longitudinally extending transverse myelitis", and the Clinical features block including "Peak reached within : 4 hours to 21 days".

## Book p666 — 04 PDF41 — Ch51

- Differentiating points from GBS (six bullets) beside the sagittal MRI annotated "Hyperintensity" with level markers C3–T8, captioned "Acute transverse myelitis"; two further panels A/B captioned "MRI : Hyperintensities in spinal cord".
- Investigations, Treatment (methylprednisolone 500–1000 mg IV in 100 ml NS over 1 hour → Plasma exchange on no response) and the four plasma-exchange indications.
- SACD section with the four-step progression flow (posterior tract → lateral tract → large fibre neuropathy → complication) and the note "Cervical compressive myelopathy → Glove & stocking neuropathy".

## Book p667 — 04 PDF42 — Ch51 end

- FRIEDREICH'S ATAXIA: commonest spinocerebellar degeneration, cerebellum normal, AR 8–20 yrs versus AD later onset, "FRATAXIN (Chr 9) : GAA repetition" [sic — the gene is FXN/frataxin, quoted as printed], cerebrum and cranial nerves spared, males > females.
- Two sagittal MRI panels: "Normal cerebellum (Spinocerebellar fibres affected)" over the Friedreich's ataxia caption and "Atrophic cerebellum" over Ataxia telangiectasia.
- Involvement ladder (DRG → spinocerebellar tract → cord → lastly nerve) and the non-neurological list, including "myocardial fibrosis in 90%"; "Diabetic mellitus" [sic].
- TABES DORSALIS begins at the foot of the page (manifestation of neurosyphilis, DRG sensory ataxia, bowel and bladder, nerve-root triad).

## Book p668 — 04 PDF43 — Ch52 title page "MULTIPLE SCLEROSIS"

- Five-member chronic inflammatory demyelinating list and the note "Non inflammatory demyelination → Osmotic demyelination (Rapid sodium correction)".
- Definition columns "1. Chronic inflammatory demyelination of" (subcortical, brainstem, spinal cord, cortical) and "2. Sparing of" (peripheral nerve system, organ system).
- Features (autoimmune, F > M, family history, "HLA DR2/15") and Risk factors (EBV, smoking, vitamin D deficiency, high socio-economic status).
- PATHOGENESIS flow: astrocytes → BBB disruption, ↑VEGF → exudation → "Ta-weighted : Hyper intense lesion" [sic for T2] and T1 contrast enhancement; T + B cells onto MBP and "myelin oligo dendrocyte glycoprotein (MOAP)" [sic for MOG]; loss of saltatory conduction; cumulative axonal destruction → cortical atrophy and progressive neuronal damage. Blood–brain-barrier figure labels tight junction, pericyte, endothelial cell, microglia, basement membrane, peg-socket junction, leukocyte, neuron.

## Book p669 — 04 PDF44 — Ch52

- DISEASE PATTERNS: three disability-versus-time curves, relapsing-remitting 90%, secondary progressive 5–6% (following relapsing-remitting), primary-progressive with "Rx : Anti CD-20, Ocrelizumab".
- Major features: sensory (long tract, m/c), motor ("Loss of tone, loss of dexterity, spasticity" [sic — tone is increased in UMN disease; quoted as printed]) and optic neuritis (unilateral, asymmetric if bilateral, retrobulbar pain, anterior pathway, drug responsive, diplopia).
- Minor features (ataxia, vertigo, bladder, Lhermitte, dementia, myokymia) and Other presentations (B/L INO, B/L trigeminal neuralgia, pseudobulbar involvement, acquired pendular nystagmus).
- McDonald criteria flow: dissemination in time (2 lesions 4 weeks apart, T2 hyperintense lesion, or T1 enhancing) + dissemination in space (2 lesions at different sites; juxtacortical, periventricular, spinal cord, infratentorial with cerebellar and middle cerebellar peduncle).

## Book p670 — 04 PDF45 — Ch52

- Three axial MRI panels with yellow arrows captioned "MRI showing hyper-intense lesion"; a separate axial image captioned "Periventricular lesion".
- Ancillary symptoms: Uhthoff (U/L blurring during hot shower), Lhermitte (also seen in compressive myelopathy), Pulfrich (2-D image perceived as 3-D).
- T2 hyperintensities (periventricular common; "Corpus callosum (Dawson's fingers) : Typical"), CSF (oligoclonal bands, IgG increased in 90%), VER sensitivity 80–85%, and the Normal/Abnormal electrophoresis figure captioned "Oligoclonal bands in CSF".
- TREATMENT: acute attacks IV steroids (also for relapse/remission); Prevention — Infusable natalizumab (anti-α4 integrin, S/E PML), ocrelizumab for 1° progressive type, alemtuzumab (anti-CD52); Injectable glatiramer acetate, IFN β.

## Book p671 — 04 PDF46 — Ch52

- Oral preventives: fingolimod (sphingosine receptor modulator), teriflunomide (dihydroorotate dehydrogenase inhibitor), dimethyl fumarate.
- Neuromyelitis Optica (NMO), AKA Devic's disease; chronic inflammatory demyelinating, F > M, age 40 years, SLE in 40%, antibody against aquaporin 4.
- Clinical features row "Optic neuritis + myelitis ± Hearing loss" with four optic and four myelitis bullets, the area postrema hiccup line, investigations (oligoclonal bands 30%, MRI brain normal) and treatment (steroids, plasma exchange).

## Book p672 — 04 PDF47 — Ch52

- Anti MOG Antibodies Disease (00:24:41): optic neuritis, myelitis, aquaporin-4-negative NMO spectrum disorders, ADEM.
- ADEM: age < 12 yrs, males > females in children; aetiology post-infectious (measles > chicken pox, incubation 4–21 days) and post-vaccination; pathology by molecular mimicry of MBP and myelin oligodendrocyte protein.
- Two-arm clinical flow: demyelination (white matter predominant, grey matter, basal ganglia, thalamus; monophasic; large foci of hyperintensities; fluffy lesions) and encephalitis (seizure, ↑ICT, loss of consciousness, B/L hypertonia and hyper-extensive response, meningismus, encephalopathy, and the long sensory/motor list ending choreoathetosis).

## Book p673 — 04 PDF48 — Ch52 end

- INVESTIGATION: "MRI : Large foci of hyperintense lesions" with four panels captioned "Hyper-intensity in MRI".
- ADEM vs MS table, eleven rows, including "Gender — Females > males (3:1)", Complete myelopathy Rare vs Common, MRI large symmetrical versus variable asymmetric, Location Centripetal versus Periventricular and the ADEM-only mass effect/grey matter row.

## Book p674 — 04 PDF49 — Ch53 title page "VASCULAR ANATOMY OF BRAIN"

- Blood Supply of Brain (00:01:02) with the lateral neck/head figure labelled Middle cerebral artery, Anterior cerebral artery, Posterior communicating artery, Basilar artery, C1–C6, Right internal carotid artery, Right vertebral artery, Right common carotid artery, Brachiocephalic trunk, Right subclavian artery, captioned "Terminal branches of internal carotid artery".
- "Terminal branches : mnemonic OPAAm" [sic] expanding to Ophthalmic, Posterior Communicating, Anterior Choroidal, Anterior Cerebral, middle Cerebral arteries; the annotation was re-read on a 6× crop (`.audit-render/v0449_290_400_6x.png`).
- CIRCLE OF WILLIS diagram with A1/A2 around Acomm, ICA with ophthalmic, MCA, anterior choroidal and P comm, P1/P2 on the "Posterior cerebreal artery (PCA)" [sic], basilar branches (superior cerebellar, pontine, AICA), vertebral with PICA, and the anterior spinal artery.

## Book p675 — 04 PDF50 — Ch53

- BLOOD SUPPLY OF SURFACE OF BRAIN with the three-colour legend and three views (superolateral, medial, inferior).
- ACA vs MCA vs PCA table: area-supplied row and features row, including the ACA cingulate ladder (Apathy mild → Abulia → Amotivation → Akinetic mutism severe), the MCA cortical-aphasia brace "(cortical)" versus "No aphasia in internal capsule lesion", and the PCA line "C/L homonymous hemianopia with macular sparing".

## Book p676 — 04 PDF51 — Ch53

- Internal Capsule (00:18:33): axial figure with Genu, Corticobulbar tract, head of caudate, putamen, globus pallidus, thalamus, medial and lateral geniculate nuclei, anterior and posterior limb fibre groups, auditory (inferior peduncle) and optic (posterior peduncle) radiations; coronal figure with corona radiata, caudate, putamen, globus pallidus, internal capsule and thalamus.
- PARTS list: anterior limb frontopontine with lacunar stroke (cerebellar involvement), genu corticospinal head & neck with corticobulbar predominance, posterior limb corticospinal in "Anterior 2/3 of Post limb" with UL = LL and corticorubral fibres, retrolentiform posterior thalamic (optic), sublentiform inferior thalamic (auditory).
- Corticobulbar arms (U/L symptomless with the VIIth exception; B/L pseudobulbar palsy in ALS), the dense-capsule note, the H H H triad and the closing note "MCA involvement : UL > LL. ACA involvement : LL > UL. Post limb : UL = LL."

## Book p677 — 04 PDF52 — Ch53

- BLOOD SUPPLY diagram of the capsule with the four supply lines and the annotation "Injury : HHH triad — mild form, Hemisensory loss predominant".
- Five boxed arterial sources: anterior limb (ACA striate including the recurrent artery of Heubner, plus MCA), genu (ACA, MCA, direct ICA), posterior limb (MCA striate including the large Charcot artery of cerebral haemorrhage, plus anterior choroidal), sublentiform (PCA and anterior choroidal), retrolentiform (PCA).
- Middle Cerebral Artery section (00:31:40) with the figure labels Putamen, Globus pallidus, internal capsule, caudate head, lenticulo-striate arteries medial/lateral, horizontal M1, Sylvian M2, Cortical M3-segment; the handwritten heading was re-read on a 6× crop as "M2 SEGMENT — Supplies sylvian fissure" with the superior/inferior division strokes and the both-divisions global-aphasia arm.

## Book p678 — 04 PDF53 — Ch53

- "M1 SEGMENT — Supplies" internal capsule, caudate nucleus, putamen, globus pallidus; lenticulostriate occlusion → internal capsule stroke → HHH triad + UMN 7th palsy + Parkinson features (B/L occlusion); perforator vessels 30–300 µm → lipohyalinosis → lacunar stroke → pure motor hemiparesis.
- Complete MCA syndrome = M1 + M2 + M3, with aphasia + 7th nerve palsy "(Only if B/L Corticobulbar involvement)" and the HHH triad; comparison table with common feature HHH triad and the cortical different-feature list, whose "unstructured/ dressing apraxia" is read as printed [sic, i.e. constructional/dressing apraxia].
- Anterior Cerebral Artery (ACA) section (00:42:10) with the A1/A2 split at the anterior communicating artery, A1 structures, the "No clinical Symptoms (D/t presence of significant collaterals)" arm and the A2 medial-surface, paracentral and cingulate entries.

## Book p679 — 04 PDF54 — Ch53

- ACA note block: partial corticosensory loss, gait apraxia with B/L involvement also seen in normal pressure hydrocephalus, and "Primitive reflex : loss of C/L grasp & sucking reflex" [sic — the loss is of release of these reflexes; quoted as printed].
- Posterior Cerebral Artery (00:44:40): P1 proximal to P. com supplying midbrain, subthalamus, thalamus; P2 distal with the unilateral arm (medial temporal: visual agnosia, peduncular hallucinosis, splenium alexia without agraphia, hippocampal memory; occipital: congruent C/L hemianopia with macular sparing) and the bilateral arm (Anton syndrome, Balint syndrome with optic ataxia, oculomotor apraxia, simultanagnosia, palinopsia), plus the note "Ataxia with agraphia : Gerstmann syndrome".
- SYNDROMES — Types of posterior circulation: four schematics (Type I, IIA, IIB, III) each labelled Midbrain, Thalamus, Posterior cerebral artery, Basilar artery; Type IIB carries "1. Artery of percheron (AOP)" with its infarct triad; "2. Dejerine Roussy syndrome" with the burning-hand eponym, thalamogeniculate occlusion and C/L hemisensory loss with burning pain, beside the axial MRI captioned for that syndrome.

## Book p680 — 04 PDF55 — Ch53 end

- Watershed territories: six axial panels (a–d FLAIR hyperintensities and the matching diffusion row) beside the schematic labelled Cortical border zone between ACA and MCA, Internal border zone between LCA and MCA [sic — LCA is the printed abbreviation for the lenticulostriate/central perforator territory] and Cortical border zone between MCA and PCA.
- Two bullets: watershed areas prone to infarct; predisposing conditions hypoalbuminaemia, sudden hypotension and dehydration with the printed reminder "(Adequate hydration of patient)".

## Book p681 — 04 PDF56 — Ch54 title page "APPROACH TO UMN LESION"

- Stroke (00:00:40) opens with the Embolic vs thrombotic table: full weakness at onset versus weakness evolving over 48–72 hr; rapid recovery of consciousness and cortical findings +/−; multiple lesions at different areas +/−; grey–white matter interphase involvement +/−; haemorrhagic transformation +/−; small versus large vessel; thrombectomy useful + better prognosis −/+.
- Note "Weakness evolving beyond 72 hrs : Bleeding/tumor".
- MCA stroke flow with three arms — "m1/Lenticulostriate artery from m1 : Internal capsule findings", "m2" with ± C/L weakness and aphasia splitting into superior (Broca) and inferior (Wernicke without weakness), and Complete MCA with weakness, hemianopia, hemisensory loss, cortical findings and global aphasia. The handwritten subscripts were read from the 3× render as M1 and M2 and agree with the segment nomenclature on p677–678.

## Book p682 — 04 PDF57 — Ch54

- Differentials: internal capsule lesions (dense hemiplegia, hemisensory loss, homonymous hemianopia, 7th CN palsy more prominent, absence of cortical findings); brain stem lesions (crossed hemiplegia: I/L LMN CN nuclei + C/L weakness); spinal cord lesions (B/L involvement, specific level of lesion +).
- Upper Motor Neurons (00:11:01): descending fibres merging on AHC in cord and CN nuclei in brainstem; corticospinal functions (skilled distal movements; inhibitory impulses; at-level LMN and below-level UMN patterns); extrapyramidal functions (tone and posture; inhibit proximal and antagonistic muscles).
- Tracts/Fibres included: pyramidal CST and extrapyramidal fibres merged on AHC, with Rubrospinal in lateral white matter and vestibulospinal, tectospinal and reticulospinal bracketed as ventral white matter.

## Book p683 — 04 PDF58 — Ch54

- Corticobulbar note: B/L involvement → pseudobulbar palsy (seen in ALS); U/L involvement → usually symptomless, with the VIIth CN exception producing an UMN seventh palsy from an internal capsule or cortical lesion because only the lower half is contralaterally innervated.
- Paired facial-nerve diagrams with labels Supranuclear lesion, Facial nerve, Nucleus of facial nerve, Lesion in facial nerve, and the two faces annotated Drooping of angle of mouth (A, supranuclear/UMN) and Deviation of angle of mouth (B, LMN/facial nerve, Bell's palsy).
- Motor homunculus representation: ACA lesions → lower limb; MCA lesions → upper limb and face; homunculus labels from hip and leg through the digits to eye, nose, face, lips, teeth/gums/jaw, tongue and pharynx.

## Book p684 — 04 PDF59 — Ch54

- PYRAMIDAL TRACT pathway: cortex contributions 30% primary motor (pyramidal cells of Betz, lowest threshold), 30% premotor/supplementary, 40% primary sensory cortex [sic as printed]; corona radiata; internal capsule anterior 2/3 of posterior limb accompanied by corticonuclear and corticorubral fibres.
- Left figure labels Pre-central gyrus, Sub cortex, cerebral peduncle, midbrain, medulla, pyramids, decussation of pyramids, lateral and anterior corticospinal tracts, upper and lower motor neuron, To skeletal muscles, spinal cord, with the orange/black key.
- Midbrain section labels Superior colliculus, Oculomotor nucleus, Tectum, Tegmentum, Crus cerebri/Cerebral peduncle, Red nucleus, Decussation of rubrospinal tract, Oculomotor nerve, Cerebral aqueduct, Medial longitudinal fasciculus, Lemnisci (Sensory), Substantia nigra, Middle 3/5th, Corticospinal and corticonuclear fibres, Frontopontine fibres; the note records that the trochlear nerve is not seen at the superior colliculus level.
- Descent: pons basilar part → medulla with decussation at pyramidal level in caudal medulla → spinal cord, distributed Cervical 50%, Thoracic 30%, Lumbosacral 30%.

## Book p685 — 04 PDF60 — Ch54 end

- Pyramidal pattern of weakness: UMN facial palsy with the lower half involved and upper half spared; voluntary fibres greater than emotional fibres; deglutition and articulation not affected.
- Upper limb: shoulder abduction and external rotation lost (adducted, internally rotated), elbow extension and supination lost (flexed, prone), wrist dorsiflexion lost (palmar flexed). Lower limb: hip adduction and flexion and internal rotation lost (abducted, externally rotated), knee flexion lost (extended), ankle dorsiflexion and eversion lost (plantar flexed, inverted) → circumduction gait.
- Tone: pyramidal lesion → clasp-knife spasticity; Spasticity versus Rigidity table (velocity and length dependent +/−; resistance in one direction during the initial part versus in both directions; clasp knife versus lead pipe/cog wheel).
- Root-value note: biceps C5, C6; triceps C7; finger flexion C8, T1; knee jerk L3, L4; ankle jerk S1.

## Printed quirks and how they are handled

| Page | As printed | Handling |
|---|---|---|
| 660 | "Disc pathology : IVDP (m/c)" | 4× OCR read "(m/e)"; visual re-read at 3× confirms (m/c), and the question quotes (m/c). |
| 664 | Conus "B/L S3 → C1 inside spinal cord", cauda "Asymmetrical L2 → C1 roots" | The coccygeal segment is printed as C1; the question names the printed text and flags it as the same C0/C1 inconsistency recorded for Ch50. |
| 667 | "FRATAXIN (Chr 9) : GAA repetition" | Quoted as printed; the standard symbol is FXN/frataxin on chromosome 9, which is what the distractor set tests. |
| 667 | "Diabetic mellitus" | Quoted as printed in the non-neurological list; no question depends on the misspelling. |
| 668 | "Ta-weighted : Hyper intense lesion" | Read as T2-weighted; the explanation records the printed "Ta" and the question asks the sequence pairing rather than the typo. |
| 668 | "myelin oligo dendrocyte glycoprotein (MOAP)" | Abbreviation printed as MOAP for MOG; both spellings appear in the explanation. |
| 669 | "Loss of tone, loss of dexterity, spasticity" | Quoted as printed even though spasticity implies increased tone; no question asks whether tone is lost or gained. |
| 678 | "unstructured/ dressing apraxia" | Read as the printed constructional/dressing apraxia pairing; the question uses the printed wording. |
| 679 | "Primitive reflex : loss of C/L grasp & sucking reflex" | Quoted as printed; the question asks the printed line and does not assert the physiological direction. |
| 674 | "mnemonic OPAAm" and "Posterior cerebreal artery (PCA)" | Both quoted as printed; the mnemonic expansion is asked item by item. |
| 677 | Hand-written "M2 SEGMENT" heading | Subscript verified on a 6× crop; the question asks the printed annotation ("Supplies sylvian fissure") and the segment labels rather than the letter shape. |
| 684 | Cortex contributions 30% / 30% / 40% | Asked exactly as printed; the 40% primary-sensory figure is a source statement and no question generalises it. |
