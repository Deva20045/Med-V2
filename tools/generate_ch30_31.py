#!/usr/bin/env python3
"""Author the audited, source-ordered learning sets for Chapters 30–31.

The source pages are the supplied scans: uploads/02.pdf PDF87–93 = Book
p555–561 and uploads/03.pdf PDF1 = Book p562. Every row below was authored
from a 2x visual read of the page, top-to-bottom, including diagram labels,
tables, percentages, lesion patterns and notes. The questions deliberately use
reasoning-first four-option formats only; no fill-up, matching or true/false
worksheets are introduced. ``data/chNN.json`` remains the app source of truth.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data"


def make_chapter(number, title, page_range, unit_specs):
    questions = []
    units = []
    for unit_no, (section, unit_title, guide, rows) in enumerate(unit_specs, 1):
        ids = []
        for page, fmt, stem, correct, distractors, explanation in rows:
            qid = f"MED-C{number}-{len(questions) + 1:02d}"
            choices = [correct, *distractors]
            # The app randomises display order as well; rotating here makes the
            # stored artifact itself resistant to answer-position patterns.
            shift = (len(questions) * 3 + number) % 4
            choices = choices[shift:] + choices[:shift]
            questions.append({
                "id": qid,
                "sec": section,
                "page": page,
                "fmt": fmt,
                "q": stem,
                "opts": choices,
                "ans": choices.index(correct),
                "exp": explanation + f" (Book p{page})",
            })
            ids.append(qid)
        units.append({
            "id": f"MED-U{number}-{unit_no}",
            "ch": number,
            "n": unit_no,
            "title": f"{unit_no}. {unit_title}",
            "sec": section,
            "guide": guide,
            "qs": ids,
        })
    return {
        "chapter": number,
        "title": title,
        "pageRange": page_range,
        "questions": questions,
        "units": units,
    }


def q(page, fmt, stem, correct, *distractors, exp):
    assert len(distractors) == 3, (stem, distractors)
    return (page, fmt, stem, correct, list(distractors), exp)


def write(chapter):
    path = OUT / f"ch{chapter['chapter']:02d}.json"
    path.write_text(json.dumps(chapter, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{path.name}: {len(chapter['questions'])} questions / {len(chapter['units'])} units")


# ---------------------------------------------------------------------------
# Chapter 30 — Frontal Lobe, Book p555–559
ch30 = make_chapter(30, "Frontal Lobe", "555-559", [
    (
        "MMSE and frontal-lobe surface orientation",
        "MMSE and frontal-lobe surface orientation",
        "The page opens with the MMSE and its ORARLC components.\nThe superolateral maps orient the frontal lobe against the central sulcus, parietal, temporal and occipital lobes, while the cortex map identifies motor, somatosensory, auditory and visual regions.",
        [
            q(555, "recall", "What is the stated purpose of the mini-mental state examination (MMSE)?", "To assess higher mental functions and cognitive status", "To grade isolated lower-motor-neuron weakness", "To localise a visual-field defect without cognitive testing", "To measure cerebellar coordination alone", exp="The MMSE is introduced as helping to assess higher mental functions and cognitive status."),
            q(555, "recall", "The page's ORARLC mnemonic for MMSE is expanded as which sequence?", "Orientation, registration, attention, recall, language and copying", "Orientation, reflexes, attention, reading, language and calculation", "Observation, registration, arousal, recall, localisation and copying", "Orientation, registration, arithmetic, reasoning, language and coordination", exp="The printed MMSE list is ORARLC: orientation, registration, attention, recall, language and copying."),
            q(555, "scenario", "On the superolateral surface diagram, a lesion immediately posterior to the central sulcus lies in which labelled lobe?", "Parietal lobe", "Temporal lobe", "Occipital lobe", "Frontal lobe", exp="The superolateral diagram places the parietal lobe posterior to the central sulcus and the frontal lobe anterior to it."),
            q(555, "recall", "Which map relationship is represented by the Sylvian fissure label?", "It forms the lateral boundary around the frontal and temporal regions on the superolateral surface", "It separates the occipital lobe from the cerebellum", "It marks the medial boundary between the two hemispheres", "It is the groove between the precentral and postcentral gyri", exp="The superolateral surface labels the Sylvian fissure laterally, with frontal and temporal regions around it; the central sulcus is the separate motor-sensory landmark."),
            q(555, "recall", "Which cortex-to-lobe pairing agrees with the lower functional map?", "Motor cortex—frontal; somatosensory cortex—parietal; auditory cortex—temporal; visual cortex—occipital", "Motor cortex—occipital; somatosensory—temporal; auditory—frontal; visual—parietal", "Motor cortex—temporal; somatosensory—occipital; auditory—parietal; visual—frontal", "All four cortices are labelled inside the frontal lobe", exp="The lower diagram labels motor cortex in the frontal region, somatosensory cortex in the parietal region, auditory cortex in the temporal region and visual cortex in the occipital region."),
        ],
    ),
    (
        "Frontal-lobe areas and surface anatomy",
        "Frontal-lobe areas and surface anatomy",
        "Area 4, area 6, the two area-8 labels, prefrontal areas 9–12 and Broca areas 44–45 are read from the functional map.\nThe medial-surface and inferior-surface diagrams retain their named gyri, sulci and fissures, including the H-shaped orbital sulcus.",
        [
            q(556, "scenario", "A functional map labels the precentral gyrus as which Brodmann area and role?", "Area 4, the primary motor area", "Area 6, the premotor area", "Area 8, the frontal eye field", "Areas 44 and 45, Broca's motor speech area", exp="The map labels area 4 in the precentral gyrus as the primary motor area."),
            q(556, "recall", "Which area-function pairing is printed for the premotor and supplementary motor regions?", "Area 6—premotor area; area 8—supplementary motor area medially", "Area 4—supplementary motor area; area 6—primary sensory area", "Area 8—Broca area; areas 44 and 45—frontal eye field", "Areas 9–12—premotor area; area 6—prefrontal pole", exp="The functional map identifies area 6 as premotor and area 8 as supplementary motor area medially; it separately labels another area-8 region as the frontal eye field."),
            q(556, "recall", "Which label is assigned to the area-8 region on the frontal-lobe map besides the supplementary motor area?", "Frontal eye field", "Primary auditory cortex", "Angular gyrus", "Parieto-occipital association area", exp="Area 8 is also labelled the frontal eye field on the functional frontal-lobe diagram."),
            q(556, "numeric", "Which set and position are printed for the prefrontal area?", "Areas 9, 10, 11 and 12, anterior to areas 6 and 8", "Areas 1, 2 and 3, posterior to the central sulcus", "Areas 44 and 45, inside the precentral gyrus", "Areas 17 and 18, inferior to the Sylvian fissure", exp="The map gives the prefrontal area as areas 9, 10, 11 and 12, anterior to areas 6 and 8."),
            q(556, "scenario", "A lesion of the inferior frontal gyrus is being correlated with the speech label on the diagram. Which area is implicated?", "Areas 44 and 45, the motor speech area of Broca", "Area 4, the precentral motor area", "Area 22, the auditory comprehension area", "Area 17, the primary visual area", exp="The diagram places the motor speech area of Broca in the inferior frontal gyrus and labels it areas 44 and 45."),
            q(556, "recall", "Which collection belongs to the medial-surface diagram rather than the inferior-surface diagram?", "Cingulate gyrus and sulcus, paracentral lobule, corpus callosum, fornix, hippocampal gyrus and uncus", "Rectus gyrus, olfactory sulcus and H-shaped orbital sulcus", "Precentral gyrus, postcentral gyrus and central sulcus", "Lateral orbital gyrus, posterior orbital gyrus and orbital sulcus only", exp="The medial-surface drawing labels the paracentral lobule, superior frontal and cingulate gyri/sulcus, corpus callosum, fornix, hippocampal gyrus and uncus, along with posterior medial structures. The inferior drawing carries the orbital and olfactory labels."),
            q(556, "recall", "What landmark and arrangement are shown on the inferior surface of the frontal lobe?", "The olfactory sulcus beside the rectus gyrus and an H-shaped orbital sulcus dividing orbital gyri", "The calcarine fissure dividing the cuneus from the lingual gyrus", "The central sulcus dividing motor from sensory cortex", "The hippocampal sulcus surrounding the corpus callosum", exp="The inferior-surface diagram labels the olfactory sulcus beside the rectus gyrus and the orbital sulcus as H shaped, with anterior, medial, lateral and posterior orbital gyri around it."),
        ],
    ),
    (
        "Motor cortex, movement sequence and homunculus",
        "Motor cortex, movement sequence and homunculus",
        "Primary motor cortex, Betz cells, premotor/supplementary preparation and bilateral-lesion findings are kept in sequence.\nThe fine-skilled movement chain and the medial-versus-superolateral motor homunculus supply are then tested as a functional whole.",
        [
            q(557, "numeric", "What proportion of motor fibres is printed as originating from area 4, and what is special about its Betz cells?", "Only 30%; Betz cells are specialised and have the lowest threshold to initiate motor activity", "About 70%; Betz cells inhibit all motor activity", "Only 5%; Betz cells are sensory relay cells with the highest threshold", "All motor fibres; Betz cells are cerebellar Purkinje cells", exp="For area 4/primary motor cortex/precentral gyrus, the page states that only 30% of motor fibres originate there and that specialised Betz cells have the lowest threshold to initiate motor activity."),
            q(557, "scenario", "Damage confined to area 4 would most directly disrupt which printed function?", "Initiation of fine skilled voluntary movement", "The sensory guidance formula for a learned action only", "Reward-based behavioural response without weakness", "Visual recognition of an object by touch", exp="Area 4 is stated to initiate fine skilled voluntary movement; preparation and finesse are assigned to other parts of the sequence."),
            q(557, "recall", "What is the role of the premotor area (PMA) and supplementary motor area (SMA) in the printed movement model?", "They provide 30% of motor fibres and prepare movement through postural tone, proximal alignment and antagonist inhibition", "They provide all motor fibres and perform only cerebellar finesse", "They receive visual input and perform language comprehension", "They initiate movement but do not influence posture or antagonists", exp="PMA and SMA are stated to provide 30% of motor fibres and prepare fine skilled voluntary movement by setting tone of posture, proximal muscle alignment and antagonist muscle inhibition."),
            q(557, "scenario", "A bilateral PMA/SMA lesion is expected, according to the page, to produce which pair?", "Spasticity from a tone disturbance and primitive reflexes", "Flaccidity and loss of all primitive reflexes", "Pure sensory ataxia and visual agnosia", "Akinetic mutism and alexia without agraphia", exp="The page notes that bilateral PMA/SMA lesions cause spasticity (a tone issue) and primitive reflexes."),
            q(557, "scenario", "Which ordered chain follows the printed process of fine-skilled voluntary movement?", "Planning and coordination by basal ganglia → preparation by PMA/SMA → initiation by primary motor area → finesse by cerebellum", "Planning by cerebellum → preparation by primary motor area → initiation by basal ganglia → finesse by PMA/SMA", "Planning by PMA/SMA → preparation by basal ganglia → initiation by cerebellum → finesse by primary motor area", "Planning by primary motor area → preparation by cerebellum → initiation by PMA/SMA → finesse by basal ganglia", exp="The note orders fine-skilled movement as planning and coordination by the basal ganglia, preparation or setting up by PMA/SMA, initiation by the primary motor area, and finesse by the cerebellum."),
            q(557, "scenario", "Which vascular distribution matches the motor homunculus labels?", "Lower limb on the medial surface is supplied by ACA; face and upper limb on the superolateral surface are supplied by MCA", "Lower limb on the superolateral surface is supplied by MCA; face and upper limb medially by ACA", "All face, upper-limb and lower-limb representations are supplied by ACA", "The face is supplied by PCA while the lower limb is supplied by MCA", exp="The motor homunculus note assigns the lower limb to the medial surface and ACA, while face and upper limb lie on the superolateral surface and are supplied by MCA."),
            q(557, "recall", "Why can a cortical vascular lesion produce face/upper-limb-predominant versus lower-limb-predominant weakness?", "The motor homunculus places the lower limb medially and the face and upper limb superolaterally, so the affected vessel and side determine the pattern", "The cerebellum reverses the body map in every cortical lesion", "The frontal eye field supplies the lower limb but not the face", "The parietal lobe contains no somatotopic motor representation", exp="The page links the weakness pattern to the motor homunculus: lower limb is medial/ACA territory, while face and upper limb are superolateral/MCA territory."),
        ],
    ),
    (
        "Motor lesions, frontal eye field and Broca area",
        "Motor lesions, frontal eye field and Broca area",
        "The page applies ACA/MCA territory to weakness and incontinence, then distinguishes motor-cortex and irritative lesions.\nThe frontal-eye-field circuit, gaze deviation rules, Broca area and the anterior/posterior central-sulcus note close the motor section.",
        [
            q(558, "scenario", "A patient has face and upper-limb weakness after a cortical lesion. Which territory is the page's best fit?", "MCA territory", "ACA territory affecting the medial paracentral lobule", "PCA territory affecting the occipital cortex", "PPRF territory in the brainstem", exp="The page states MCA lesion causes face and upper-limb weakness, while ACA lesion causes lower-limb weakness with urinary incontinence."),
            q(558, "scenario", "Which presentation is paired with an ACA lesion on the page?", "Lower-limb weakness with urinary incontinence from paracentral-lobule involvement on the medial surface", "Face and upper-limb weakness with spared bladder function", "Contralateral homonymous hemianopia from the occipital pole", "Ipsilateral gaze paralysis from a PPRF lesion", exp="An ACA lesion is printed as producing lower-limb weakness plus urinary incontinence, attributed to the paracentral lobule on the medial surface."),
            q(558, "recall", "What is the characteristic motor-cortex lesion pattern described?", "Contralateral weakness of fine skilled voluntary movement with an UMN pattern of spasticity or hypertonia", "Ipsilateral flaccid weakness with isolated loss of vibration", "Bilateral weakness with normal tone and no motor deficit", "Pure aphasia without any contralateral motor involvement", exp="A motor-cortex lesion is described as contralateral weakness of fine skilled voluntary movements and an UMN lesion with spasticity or hypertonia."),
            q(558, "scenario", "An irritative motor-cortex lesion produces repeated spreading contractions beginning in one body part. Which label is printed?", "A contralateral motor simple partial seizure with Jacksonian march", "An ipsilateral absence seizure with no motor spread", "A cerebellar intention tremor with dysmetria", "A lower-motor-neuron fasciculation with muscle wasting", exp="The irritative lesion line states that a contralateral motor simple partial seizure may occur, with Jacksonian march."),
            q(558, "recall", "The page defines the upper motor neuron (UMN) span as extending from where to where?", "From the cortex to the anterior horn cell in grey matter", "From the anterior horn cell to the neuromuscular junction", "From the cerebellum to the dorsal-root ganglion", "From the retina to the superior colliculus", exp="The printed definition says UMN runs from the cortex till the anterior horn cell, which is in grey matter."),
            q(558, "recall", "In the frontal-eye-field circuit, what do PPRF, LR, MR and MLF stand for?", "Paramedian pontine reticular formation; lateral rectus; medial rectus; medial longitudinal fasciculus", "Parietal pontine relay formation; longus rectus; middle rectus; medial limbic fibre", "Primary pontine reflex field; lateral rotation; motor rotation; midline longitudinal fibre", "Posterior parietal reticular formation; levator rectus; motor rectus; main lateral fasciculus", exp="The abbreviations printed beside the FEF diagram are PPRF—parapontine reticular formation, LR—lateral rectus, MR—medial rectus and MLF—medial longitudinal fasciculus."),
            q(558, "scenario", "The left frontal eye field normally activates which muscles to make the eyes look right?", "Right lateral rectus and left medial rectus", "Left lateral rectus and right medial rectus", "Both medial recti only", "Both lateral recti only", exp="The diagram states that the left FEF activates the right lateral rectus and left medial rectus, producing rightward gaze."),
            q(558, "scenario", "A left frontal-lobe FEF lesion is shown on examination. What gaze position is printed?", "The patient looks toward the left, the side of the lesion; a brainstem PPRF lesion makes the patient look away from its side", "The patient looks right, away from the cortical lesion; a PPRF lesion looks toward its side", "The eyes remain fixed centrally in both lesions", "The patient looks up in the cortical lesion and down in the PPRF lesion", exp="The page states that a left FEF lesion prevents rightward gaze, so the patient looks left, toward the lesion. A brainstem PPRF lesion causes looking away from the side of the lesion."),
            q(558, "scenario", "Which language deficit and anatomical comparison are paired with Broca's area on the page?", "Area 44/45 injury causes non-fluent aphasia; anterior-central-sulcus lesions affect fluency, whereas posterior lesions affect comprehension", "Area 22 injury causes non-fluent aphasia; posterior lesions affect fluency and anterior lesions comprehension", "Area 17 injury causes alexia; central-sulcus lesions spare both fluency and comprehension", "Area 4 injury causes fluent jargon; all posterior lesions cause dysarthria", exp="Broca's area/areas 44 and 45 are linked to impaired fluency or non-fluent aphasia. The note contrasts anterior-to-central-sulcus lesions affecting fluency with posterior-to-central-sulcus lesions affecting comprehension."),
        ],
    ),
    (
        "Prefrontal cortex and bilateral frontal pathology",
        "Prefrontal cortex and bilateral frontal pathology",
        "Areas 9–12 are divided into dorsolateral, medial/cingulate, orbital and frontal-pole functions.\nExecutive function, motivation, reward-based behaviour, theory of mind and the bilateral frontal pathology list are kept in the printed order.",
        [
            q(559, "recall", "Which prefrontal-part to function table is printed?", "Dorsolateral PFC—executive function; medial PFC/cingulate—emotion and motivation; orbital PFC—behavioural response; frontal pole—theory of mind", "Dorsolateral PFC—vision; medial PFC—hearing; orbital PFC—fine movement; frontal pole—balance", "Dorsolateral PFC—language comprehension; medial PFC—touch; orbital PFC—smell; frontal pole—pain", "All four PFC parts are assigned the same executive function", exp="The table pairs dorsolateral PFC with executive function, medial PFC or cingulate gyrus with emotion and motivation, orbital PFC with behavioural response, and frontal pole with theory of mind."),
            q(559, "scenario", "A patient cannot suppress a prepotent response and cannot flexibly shift between task sets. Which printed executive domain is affected?", "Timeframe-dependent, goal-directed executive function involving cognitive inhibition, response inhibition and set shifting", "Theory of mind involving only empathy", "Motor initiation involving only Betz cells", "Visual agnosia involving the supramarginal gyrus", exp="Executive function is described as timeframe-dependent, goal-directed activity with cognitive inhibition, response inhibition and set shifting or flexibility."),
            q(559, "numeric", "The page orders loss of energisation and motivation from mild to severe as:", "Apathy → abulia → akinetic mutism", "Abulia → apathy → akinetic mutism", "Akinetic mutism → apathy → abulia", "Apathy → akinetic mutism → abulia", exp="The printed severity sequence is apathy when mild, then abulia, then akinetic mutism when severe."),
            q(559, "recall", "Behavioural response in the prefrontal table is based on what, and what does the JIPFA list include?", "Reward and punishment; judgement, insight, problem solving/personality, fluency and abstract thinking", "Pain and temperature; jaw, intention, proprioception, fine touch and ataxia", "Sleep and arousal; memory, orientation, registration, language and copying", "Tone and posture; proximal alignment, antagonist inhibition, gait and balance", exp="Behavioural response is based on reward and punishment and includes JIPFA: judgement, insight, problem solving/personality, fluency and abstract thinking."),
            q(559, "scenario", "Which statement best reflects the page's theory-of-mind line?", "It includes sympathy and empathy, while metacognition means understanding oneself", "It is limited to writing and naming, while metacognition means recognising objects by touch", "It means initiating eye movements, while metacognition means inhibiting reflexes", "It is the same as motor finesse, while metacognition means calculating a percentage", exp="Theory of mind is listed with sympathy and empathy; metacognition is defined on the page as understanding oneself."),
            q(559, "scenario", "Which cluster is the page's bilateral frontal-lobe pathology list?", "Prefrontal personality change, urinary incontinence from bilateral paracentral lesions, primitive reflexes from premotor involvement, akinetic mutism and gait apraxia in NPH", "Isolated anosmia, homonymous hemianopia, pure alexia and dysmetria", "Fluent aphasia, inferior quadrantanopia, facial palsy and sensory extinction", "Rest tremor, rigidity, bradykinesia and levodopa-induced dyskinesia", exp="The bilateral frontal pathology list contains prefrontal personality changes, urinary incontinence due to bilateral paracentral-lobule lesions, primitive reflexes due to premotor-cortex involvement, akinetic mutism as severe apathy and gait apraxia in normal-pressure hydrocephalus."),
            q(559, "scenario", "A patient with normal-pressure hydrocephalus has gait apraxia and says the foot feels stuck to the floor. Which mechanism phrase is printed?", "Ignition failure", "Loss of visual object recognition", "Disconnection between visual cortices", "Failure of the lateral rectus to abduct", exp="Gait apraxia is associated with normal-pressure hydrocephalus and is described as ignition failure, with the foot feeling stuck to the floor."),
        ],
    ),
])


# ---------------------------------------------------------------------------
# Chapter 31 — Praxicons, Book p560–562
ch31 = make_chapter(31, "Praxicons", "560-562", [
    (
        "Parietal map, postcentral gyrus and motor-fibre origins",
        "Parietal map, postcentral gyrus and motor-fibre origins",
        "The posterior-central-sulcus map identifies primary sensory cortex and the parietal association regions.\nThe motor-fibre percentages and the postcentral-gyrus lesion profile retain the page's supplied MCA, tone, FEF and cortical-sensation notes.",
        [
            q(560, "recall", "The Praxicons page places the parietal lobe in which relation to the central sulcus, and labels primary sensory cortex as which areas?", "Posterior to the central sulcus; areas 3, 1 and 2", "Anterior to the central sulcus; areas 4, 6 and 8", "Inferior to the Sylvian fissure; areas 17 and 18", "Medial to the corpus callosum; areas 9, 10 and 11", exp="The page heading says parietal lobe posterior to the central sulcus and labels primary sensory cortex as areas 3, 1 and 2."),
            q(560, "recall", "Which set of landmarks belongs to the posterior-parietal diagram?", "Posterior parietal lobule, intraparietal sulcus, superior and inferior parietal lobules, supramarginal gyrus, angular gyrus and parieto-occipital association area", "Precentral gyrus, premotor area, frontal eye field and Broca area", "Rectus gyrus, olfactory sulcus, orbital sulcus and orbital gyri", "Hippocampal gyrus, uncus, fornix and cingulate sulcus only", exp="The parietal map labels the posterior parietal lobule and intraparietal sulcus, superior parietal lobule as praxicons, inferior parietal lobule, supramarginal gyrus as gnosis, angular gyrus as Gerstmann syndrome and the parieto-occipital association area."),
            q(560, "numeric", "What proportions of motor fibres are assigned to the three cortical sources in the note?", "Primary sensory cortex 40%, primary motor cortex 30%, and premotor plus supplementary motor cortex 30%", "Primary sensory 10%, primary motor 80%, premotor plus supplementary 10%", "Primary sensory 30%, primary motor 30%, premotor plus supplementary 40%", "Primary sensory 50%, primary motor 25%, premotor plus supplementary 25%", exp="The origin-of-motor-fibres note gives primary sensory cortex 40%, primary motor cortex 30% and premotor/supplementary motor cortex 30%."),
            q(560, "scenario", "A postcentral-gyrus lesion is described as causing contralateral UMN weakness with the page's vascular association. Which vessel is named?", "Middle cerebral artery", "Anterior cerebral artery", "Posterior cerebral artery", "Basilar artery", exp="Under postcentral gyrus, contralateral upper-motor-neuron weakness is associated with the middle cerebral artery."),
            q(560, "scenario", "Compared with a primary motor-cortex lesion, the postcentral-gyrus profile on the page includes which combination?", "Tone is less affected, the frontal eye field is spared and cortical sensations are impaired", "Tone is severely increased, the FEF is destroyed and cortical sensations are normal", "Tone is flaccid, the FEF is spared and only hearing is impaired", "Tone is unchanged, the FEF is affected and only language is impaired", exp="The postcentral-gyrus list states that tone is less affected, the frontal eye field is spared and cortical sensations are impaired."),
            q(560, "recall", "Which group is explicitly listed under impaired cortical sensations?", "Tactile localisation, two-point discrimination, stereognosis and graphesthesia", "Pain, temperature, vibration and joint position only", "Smell, hearing, taste and visual acuity", "Fluency, insight, judgement and abstract thinking", exp="The page lists impaired cortical sensations as tactile localisation, two-point discrimination, stereognosis and graphesthesia."),
            q(560, "recall", "What association and blood-supply notes accompany the postcentral-gyrus section?", "Association with premotor and supplementary motor areas relates to tone and FEF; primary sensory and primary motor cortices are supplied by MCA", "Association with the cerebellum relates to smell; primary cortices are supplied by PCA", "Association with the hippocampus relates to memory; primary cortices are supplied by ACA only", "Association with Broca area relates to hearing; primary cortices have no named arterial supply", exp="The notes link premotor/supplementary motor association with tone and FEF, and state that primary sensory and primary motor cortices have middle-cerebral-artery blood supply."),
        ],
    ),
    (
        "Praxicons, apraxias and parietal dominance",
        "Praxicons, apraxias and parietal dominance",
        "The superior parietal lobule generates the movement formula and sensory guidance for movement.\nApraxia, visual agnosia, handedness-based dominant-parietal percentages and non-dominant pseudoapraxias are kept in the printed order.",
        [
            q(561, "recall", "What does the superior parietal lobule generate according to the page?", "Praxicons: a movement formula and sensory guidance for movement", "A visual field defect and a motor speech programme", "Only the emotional intonation of language", "The basal-ganglia neurotransmitter loop", exp="The superior parietal lobule is stated to generate praxicons, defined here as the movement formula or sensory guidance for movement."),
            q(561, "scenario", "A patient cannot execute a learned voluntary skilled action despite normal cerebellar, motor and sensory function and preserved comprehension. What syndrome is described?", "Apraxia", "Ataxia from a cerebellar lesion", "A lower-motor-neuron palsy", "Aphasia from a dominant frontal lesion", exp="Apraxia is defined as inability to execute a learnt voluntary skilled action despite normal cerebellum, motor and sensory function and comprehension."),
            q(561, "recall", "What does a superior-parietal-lobule lesion do in the printed model?", "It causes inability to generate praxicons", "It causes inability to recognise an object by touch only", "It causes isolated lower-limb urinary incontinence", "It causes a homonymous hemianopia with macular sparing", exp="The page directly states that a lesion in the superior parietal lobule causes inability to generate praxicons."),
            q(561, "scenario", "A patient has lost the idea of a learned skilled act itself. Which apraxia type fits the page?", "Ideational apraxia", "Ideomotor apraxia", "Constructional apraxia", "Dressing apraxia", exp="Ideational apraxia is printed as the type in which the idea is absent."),
            q(561, "scenario", "A patient understands the idea of a skilled action but executes it poorly. Which apraxia type is this?", "Ideomotor apraxia", "Ideational apraxia", "Topographic agnosia", "Hemispatial neglect", exp="Ideomotor apraxia is printed as idea present with poor execution."),
            q(561, "recall", "What does gnosis mean in the supramarginal-gyrus section?", "The ability to recognise an object by touch, vision or sound", "The inability to execute a learned action despite normal comprehension", "The inability to differentiate a bedroom from a bathroom", "The ability to generate a movement formula from the cerebellum", exp="Gnosis is defined as the ability to recognise an object by touch, vision or sound."),
            q(561, "scenario", "A patient cannot identify an object by vision, with the page's affected areas being considered. Which finding is being described?", "Visual agnosia involving the supramarginal gyrus and parieto-occipital association area for visuospatial orientation", "Ideational apraxia involving the superior parietal lobule only", "Pure alexia involving the fusiform gyrus only", "A frontal eye-field lesion involving the PPRF", exp="Visual agnosia is described as inability to identify by vision; the page names the supramarginal gyrus and the parieto-occipital association area, the latter linked to visuospatial orientation."),
            q(561, "numeric", "For the dominant parietal lobe table, which handedness percentages are printed?", "Right-handed: right lobe 5% and left lobe 90–95%; left-handed: right lobe 40% and left lobe 50–60%", "Right-handed: right 90–95% and left 5%; left-handed: right 50–60% and left 40%", "Right-handed: both lobes 50%; left-handed: both lobes 50%", "Right-handed: right 40% and left 50–60%; left-handed: right 5% and left 90–95%", exp="The table prints right-handed dominance as right lobe 5% and left lobe 90–95%, and left-handed dominance as right lobe 40% and left lobe 50–60%."),
            q(561, "recall", "The page places language in which relationship to the dominant parietal lobe?", "Language is part of the dominant lobe", "Language is restricted to the non-dominant lobe", "Language is part of the cerebellum rather than either parietal lobe", "Language is assigned only to the occipital lobe", exp="Immediately below the dominance table, the source states that language is part of the dominant lobe."),
            q(561, "scenario", "Which non-dominant-parietal pattern is correctly interpreted as pseudoapraxia?", "Constructional apraxia is inability to perceive and imagine geometric relations, while dressing apraxia is inability to dress, such as being unable to put on a jacket", "Constructional apraxia is inability to read, while dressing apraxia is inability to name fingers", "Constructional apraxia is inability to recognise by sound, while dressing apraxia is loss of bladder control", "Both are defined as loss of the idea of a skilled action from a dominant superior parietal lesion", exp="The non-dominant parietal section calls these pseudoapraxias: constructional apraxia is inability to perceive and imagine geometric relation, and dressing apraxia is inability to dress, exemplified by inability to put on a jacket."),
            q(561, "scenario", "A patient cannot distinguish familiar places such as the bedroom and bathroom. Which non-dominant-parietal deficit is printed?", "Visuospatial disorientation", "Anomia", "Graphesthesia", "Ideomotor apraxia", exp="Visuospatial disorientation is defined as inability to differentiate places, for example bedroom and bathroom."),
        ],
    ),
    (
        "Hemispatial neglect, angular gyrus and visual pathways",
        "Hemispatial neglect, angular gyrus and visual pathways",
        "Right-versus-left parietal neglect, topographic agnosia, angular-gyrus functions and Gerstmann syndrome are followed by the PCA/splenium note.\nPure alexia and the frontal, parietal and temporal visual-field patterns close the source range at Book p562.",
        [
            q(562, "scenario", "A patient visually scans only one side of the body schema and neglects activities related to one hemisphere. Which syndrome is named?", "Hemispatial neglect, also termed anosognosia/asomatognosia in the note", "Topographic agnosia", "Ideomotor apraxia", "Pure alexia without agraphia", exp="The page introduces hemispatial neglect with anosognosia/asomatognosia as abnormal visual scanning of the body schema leading to neglect of activities related to one hemisphere."),
            q(562, "scenario", "Which right-versus-left parietal lesion pairing is printed in the extrapersonal-space table?", "Right parietal lesion: left hemispatial neglect; left parietal lesion: no abnormality", "Right parietal lesion: no abnormality; left parietal lesion: bilateral neglect", "Right parietal lesion: right neglect; left parietal lesion: left neglect", "Both right and left parietal lesions cause only right hemispatial neglect", exp="The table shows extrapersonal space represented as right plus left under the right parietal lobe and right under the left parietal lobe; a right-parietal lesion gives left hemispatial neglect, while the left-parietal lesion column says no abnormality."),
            q(562, "recall", "What is topographic agnosia?", "Loss of orientation to topography", "Loss of the idea of a learned motor act", "Loss of reading with preserved writing", "Loss of a visual field with preserved spatial orientation", exp="Topographic agnosia is defined on the page as loss of orientation to topography."),
            q(562, "recall", "Which function set is assigned to the angular gyrus?", "Reading, writing, naming and spatial orientation with respect to fingers, numbers and body sites", "Postural tone, proximal alignment and antagonist inhibition", "Eye abduction, adduction and the vestibulo-ocular reflex", "Pain, temperature, vibration and primary touch only", exp="The angular-gyrus functions listed are reading, writing, naming and spatial orientation with respect to finger, number and body sites."),
            q(562, "scenario", "A dominant angular-gyrus lesion produces impaired reading and writing, impaired naming, finger anomia, acalculia and right-left disorientation. Which syndrome is this?", "Gerstmann syndrome", "Horner syndrome", "Brown-Sequard syndrome", "Wernicke syndrome", exp="Gerstmann syndrome is attributed to a lesion of the dominant angular gyrus and includes alexia plus agraphia, anomia, finger anomia or acalculia, and right-to-left disorientation."),
            q(562, "recall", "Which pairing correctly expands the two reading/writing deficits in Gerstmann syndrome?", "Alexia means impaired reading and agraphia means impaired writing", "Alexia means impaired writing and agraphia means impaired reading", "Alexia means impaired naming and agraphia means impaired calculation", "Alexia means impaired touch recognition and agraphia means impaired vision", exp="The Gerstmann list explicitly pairs alexia with impaired reading and agraphia with impaired writing."),
            q(562, "scenario", "A left PCA infarct involving the splenium is followed by an occipital lesion with normal vision because of macular sparing, a right homonymous hemianopia and loss of connection between cortices. Which additional disconnection finding is printed?", "Alexia without agraphia", "Agraphia without alexia", "Bilateral deafness with preserved reading", "Fluent aphasia with preserved naming", exp="The note links left PCA infarct plus splenium of corpus callosum to an occipital lesion with macular sparing, right homonymous hemianopia and a disconnection syndrome, including alexia without agraphia."),
            q(562, "recall", "Where does the page localise pure alexia?", "A lesion of the fusiform gyrus", "A lesion of the superior parietal lobule", "A lesion of the precentral gyrus", "A lesion of the PPRF", exp="The visual-abnormalities note states that pure alexia is due to a fusiform-gyrus lesion."),
            q(562, "scenario", "Which lobe-to-visual-field pattern is transcribed in the final list?", "Frontal lobe—contralateral hemianopia; parietal lobe—inferior homonymous quadrantanopia or pie in the floor; temporal lobe—superior homonymous quadrantanopia or pie in the sky", "Frontal lobe—ipsilateral hemianopia; parietal lobe—superior quadrantanopia; temporal lobe—inferior quadrantanopia", "Frontal lobe—bitemporal hemianopia; parietal lobe—central scotoma; temporal lobe—monocular blindness", "All three lobes produce only macular sparing with no quadrantanopia", exp="The final visual list assigns contralateral hemianopia to frontal lobe, inferior homonymous quadrantanopia or pie in the floor to parietal lobe, and superior homonymous quadrantanopia or pie in the sky to temporal lobe."),
        ],
    ),
])


for chapter in (ch30, ch31):
    write(chapter)
print("Chapters 30–31 authored.")
