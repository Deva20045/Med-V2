#!/usr/bin/env python3
"""Author the audited, source-ordered learning set for Chapter 32.

Source: uploads/03.pdf PDF2-4 = Book p563-565, read top-to-bottom in printed
order (2x PyMuPDF renders cross-checked with RapidOCR and targeted 12-48x crops;
the scan has no extractable text layer). Questions stay reasoning-first and
four-option only - no fill-up, matching or true/false worksheets. ``data/chNN.json``
remains the app source of truth.
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
# Chapter 32 — Temporal and Occipital Lobe, Book p563-565
ch32 = make_chapter(32, "Temporal and Occipital Lobe", "563-565", [
    (
        "Superolateral temporal lobe and the auditory cortex",
        "Superolateral temporal lobe and the auditory cortex",
        "The page opens with a site-of-lesion and defect table for the superolateral temporal lobe.\nThe auditory cortex, its connection fibres and the temporo-occipital association area are kept in printed order.",
        [
            q(563, "recall", "How does the page open the superolateral temporal-lobe section, and which first row begins it?", "With a site-of-lesion and defect table whose first row covers the auditory cortex", "With a homunculus of the medial limbic cortex", "With a visual-field map of the occipital lobe only", "With a Brodmann diagram of the parietal praxicon area", exp="The superolateral temporal-lobe section opens with a site-of-lesion and defect table, and its opening row is the auditory cortex."),
            q(563, "recall", "Which Brodmann area pair is assigned to the auditory cortex?", "Areas 41 and 42", "Areas 44 and 45", "Areas 17 and 18", "Areas 3, 1 and 2", exp="The first table row labels the auditory cortex as areas 41 and 42."),
            q(563, "scenario", "Which site-of-lesion entry does the page print for the auditory cortex?", "Bilateral temporal lobe", "Unilateral dominant frontal lobe", "The medial occipital pole alone", "The superior parietal lobule", exp="The table states that the auditory cortex occupies the bilateral temporal lobe, so its lesion is bilateral."),
            q(563, "recall", "What defect is paired with the auditory cortex in the table?", "Deafness, described as auditory inattention", "Pure word deafness", "Wernicke's aphasia with naming loss", "Visual agnosia for objects", exp="The defect column pairs the auditory cortex with deafness, parenthesised as auditory inattention."),
            q(563, "recall", "What do the auditory connection fibres link, and which defect follows their interruption?", "They run from the auditory cortex to Wernicke's area, and their interruption causes pure word deafness", "They link Broca's area to the precentral gyrus, and interruption causes motor aphasia", "They link the temporal lobe to the primary visual area, and interruption causes alexia", "They link the thalamus to the mamillary body, and interruption causes confabulation", exp="The auditory connection fibres join the auditory cortex to Wernicke's area, and their interruption is printed as causing pure word deafness."),
            q(563, "recall", "Which deficit is printed for a lesion of the auditory association cortex?", "Auditory agnosia", "Visual agnosia", "Ideomotor apraxia", "Cortical blindness", exp="The auditory association cortex row gives auditory agnosia as its defect."),
            q(563, "scenario", "Which gyrus, area, deficit and spared function are all correctly paired for Wernicke's area?", "Superior temporal gyrus; area 22; Wernicke's aphasia affecting language comprehension, with no weakness", "Inferior frontal gyrus; area 44; naming loss with contralateral hemiplegia", "Middle temporal gyrus; area 21; visual neglect with weakness", "Angular gyrus; area 39; alexia with agraphia and weakness", exp="Wernicke's area is placed on the superior temporal gyrus and labelled area 22; its lesion gives Wernicke's aphasia, which is language comprehension, and no weakness."),
            q(563, "recall", "Which function and defect belong to the temporo-occipital association area?", "Visuospatial function, whose lesion causes visual agnosia: inability to identify objects by vision", "Language fluency, whose lesion causes non-fluent aphasia", "Motor planning, whose lesion causes ideomotor apraxia", "Memory consolidation, whose lesion causes Korsakoff's amnestic state", exp="The temporo-occipital association area is labelled for visuospatial function, and its defect is visual agnosia, defined as inability to identify objects by vision."),
            q(563, "scenario", "Which hallucination set is attributed to lateral temporal lobe lesions?", "Auditory, olfactory and gustatory hallucinations", "Visual, olfactory and vertiginous hallucinations", "Gustatory and somatosensory hallucinations only", "Auditory and visual hallucinations only", exp="The page closes the lateral temporal-lobe list by attributing auditory, olfactory and gustatory hallucinations to lateral temporal lobe lesions."),
        ],
    ),
    (
        "Medial temporal lobe (limbic cortex) and its circuits",
        "Medial temporal lobe (limbic cortex) and its circuits",
        "The medial temporal lobe (limbic cortex) note and its limbic diagrams are read after the lateral list.\nCingulate, thalamic, mamillary, hippocampal and amygdala labels form the limbic circuit on this page.",
        [
            q(563, "recall", "Which heading and claim are printed for the medial temporal lobe?", "It is the limbic cortex and is called the most epileptogenic focus in the body", "It is the motor cortex and the least excitable region in the brain", "It is the visual association area and cannot generate seizures", "It is the primary auditory area and holds no limbic connections", exp="The heading MEDIAL TEMPORAL LOBE (LIMBIC CORTEX) is followed by the notice that it is the most epileptogenic focus in the body."),
            q(563, "recall", "Which structures are labelled in the cingulate-cortex circuit diagram on this page?", "Cingulate cortex, anterior thalamus, mamillary bodies and the medial temporal lobe", "Precentral gyrus, postcentral gyrus and the pars opercularis", "Superior parietal lobule, angular gyrus and the intraparietal sulcus", "Calcarine sulcus, lingual gyrus and the cuneus only", exp="The cingulate-cortex figure joins the cingulate cortex to the anterior thalamus, mamillary bodies and the medial temporal lobe, the limbic loop."),
            q(563, "recall", "Which labels belong to the cerebrum-components diagram rather than the loop diagram?", "Cingulate gyrus, hippocampus, parahippocampal gyrus, fornix, hypothalamus, mammillary body and amygdaloid body", "Frontal eye field, Broca area and the orbital sulcus", "Primary, peristriate and parastriate visual cortex", "Vermis, flocculus and deep cerebellar nuclei", exp="The components-in-the-cerebrum figure labels the cingulate gyrus, hippocampus, parahippocampal gyrus, corpus callosum, fornix, pineal gland, hypothalamus, mamillary body, anterior group of thalamic nuclei, amygdaloid body and caudate nucleus."),
        ],
    ),
    (
        "Components of the medial temporal lobe and their functions",
        "Components of the medial temporal lobe and their functions",
        "The components and functions columns are read in sequence, then the coronal-section diagram and the amygdala/uncus notes (including herniation's third-nerve palsy).\nSee the coronal section for the hippocampus label and the inferior surface for the amygdala bulge.",
        [
            q(564, "recall", "Which four components are listed for the medial temporal lobe?", "Superior temporal gyrus, inferior temporal gyrus, parahippocampus and fusiform gyrus", "Precentral gyrus, postcentral gyrus, cingulate gyrus and precuneus", "Rectus gyrus, olfactory sulcus, orbital sulcus and uncus", "Calcarine sulcus, lingual gyrus, cuneus and splenium", exp="The components column lists the superior temporal gyrus, inferior temporal gyrus, parahippocampus and fusiform gyrus as the medial temporal lobe parts."),
            q(564, "recall", "Which five functions are listed for the medial temporal lobe?", "Homeostasis, olfaction, memory, emotion and sexuality", "Vision, audition, taste, proprioception and equilibrium", "Fluency, comprehension, repetition, naming and reading", "Posture, tone, gait, balance and coordination", exp="The functions column lists homeostasis, olfaction, memory, emotion and sexuality for the medial temporal lobe."),
            q(564, "scenario", "Which structure is the labelled medial temporal component in the coronal-section diagram?", "Hippocampus", "Amygdala", "Fusiform gyrus", "Superior temporal gyrus", exp="The coronal-section diagram in the cerebrum-components figure labels the hippocampus within the medial temporal region."),
            q(564, "scenario", "Which role and surface are printed together for the amygdala?", "It plays a role in memory and is present on the inferior surface", "It generates praxicons and lies on the superolateral surface", "It produces speech and lies inside the inferior frontal gyrus", "It stores visual memory and lies deep to the calcarine sulcus", exp="The page states the amygdala plays a role in memory and is present on the inferior surface."),
            q(564, "recall", "What is the uncus described as?", "An elevation or bulge of the amygdala on the inferior surface", "A sulcus separating the two motor homunculi", "The posterior limit of the corpus callosum", "A gyrus carrying the primary visual area", exp="The uncus is described as the elevation or bulge of the amygdala on the inferior surface."),
            q(564, "scenario", "The page links herniation of the uncus to which clinical effect?", "It affects the pupil through a third-nerve palsy", "It causes contralateral homonymous hemianopia with macular sparing", "It produces pure word deafness", "It causes colour agnosia and dressing apraxia", exp="Under the uncus, the note states that herniation affects the pupil, with third-nerve palsy given in parentheses."),
        ],
    ),
    (
        "Kluver-Bucy syndrome and Korsakoff's amnestic state",
        "Kluver-Bucy syndrome and Korsakoff's amnestic state",
        "The Kluver-Bucy equivalence and its five features are read in order, then the bilateral temporal Korsakoff's amnestic-state note closes the page.\nHypersexuality, hyperorality, visual agnosia, hypermetamorphosis and the emotional change are kept in the printed sequence.",
        [
            q(564, "recall", "Kluver-Bucy syndrome is described as also being (AKA) which combination?", "Bilateral limbic abnormality, bilateral medial temporal abnormality and bilateral amygdala abnormality", "Unilateral frontal, parietal and occipital abnormality", "Bilateral basal-ganglia, thalamic and cerebellar abnormality", "Unilateral temporal, hippocampal and mamillary-body abnormality", exp="The page writes Kluver-Bucy syndrome as AKA bilateral limbic abnormality, bilateral medial temporal abnormality and bilateral amygdala abnormality."),
            q(564, "scenario", "A patient with a bilateral limbic lesion is hypersexual. Which single feature of Kluver-Bucy syndrome is this?", "Hypersexuality", "Hyperorality", "Hypermetamorphosis", "Visual agnosia", exp="Hypersexuality is the first of the Kluver-Bucy features listed."),
            q(564, "scenario", "Which feature and its mechanism are correctly paired in the Kluver-Bucy list?", "Hyperorality, due to involvement of the hypothalamus, the feeding and satiety centre", "Hyperorality, due to a frontal eye-field lesion", "Hypermetamorphosis, due to superior-parietal praxicon loss", "Hypersexuality, due to calcarine sulcus infarction", exp="The page explains hyperorality as due to an affected hypothalamus, printing feeding and satiety centre in parentheses."),
            q(564, "recall", "In Kluver-Bucy syndrome, visual agnosia is stated to affect which structures?", "Association areas", "Primary auditory cortex", "The anterior horn cell", "The optic radiation only", exp="The Kluver-Bucy visual-agnosia line states that it affects the association areas."),
            q(564, "recall", "What is hypermetamorphosis explained as on the page?", "Visual inattention: the need to touch any object to recognise it", "The confabulation of visual descriptions in blindness", "Overshoot of the finger on the finger-nose test", "Inability to dress, such as putting on a jacket", exp="Hypermetamorphosis is printed as visual inattention, parenthesised as the need to touch any object to recognise it."),
            q(564, "scenario", "Which emotional change is listed in Kluver-Bucy syndrome?", "Decreased fear and increased aggression", "Increased fear and decreased aggression", "Emotional lability with euphoria only", "Apathy progressing to akinetic mutism", exp="The final Kluver-Bucy feature is decreased fear with increased aggression, printed as decreased Fear and increased Aggression."),
            q(564, "scenario", "Which two findings together account for Korsakoff's amnestic state on this page?", "A bilateral temporal lobe lesion and abnormality in the mamillary body", "A unilateral parietal lesion and an intact hippocampus", "A frontal eye-field lesion and a normal fornix", "A bilateral occipital infarct and splenium involvement", exp="Korsakoff's amnestic state is printed as due to a bilateral temporal lobe lesion with abnormality in the mamillary body."),
        ],
    ),
    (
        "Apathy, occipital lesions and Balint's syndrome",
        "Apathy, occipital lesions and Balint's syndrome",
        "The apathy note leads into the occipital lobe: the W/L (unilateral) and B/L lesion columns, the medial-view visual-area diagram, the colour-deficit list and Balint's syndrome, all in printed order.\nThe primary visual area, the visual association area, Anton's syndrome and the colour deficits lead into the bilateral-lesion Balint's trio.",
        [
            q(565, "recall", "Apathy is attributed by the page to lesions of which two sites?", "The medial prefrontal cortex and thalamic connections", "The medial temporal lobe and mamillary body", "The superior parietal lobule and angular gyrus", "The superior temporal gyrus and auditory cortex", exp="The apathy note states that the lesion is in the medial prefrontal cortex and the thalamic connections."),
            q(565, "scenario", "Which defect is printed for a lesion of the primary visual area (area 17)?", "Contralateral congruent homonymous hemianopia with macular sparing", "Bilateral cortical blindness with confabulation", "Superior homonymous quadrantanopia called pie in the sky", "Inferior homonymous quadrantanopia called pie in the floor", exp="The unilateral-lesion column gives the primary visual area (17) a contralateral congruent homonymous hemianopia with macular sparing."),
            q(565, "recall", "Which areas form the visual association area, and what cortex do they represent?", "Areas 18 and 19, the parastriate and peristriate cortex", "Areas 17 and 18, the primary and premotor cortex", "Areas 41 and 42, the parasitic auditory cortex", "Areas 44 and 45, the peri-arcuate speech cortex", exp="The visual association area is printed as areas 18 and 19, labelled parastriate and peristriate cortex."),
            q(565, "recall", "Which functions are listed for the visual association area?", "Ocular fixation, fixing size, shape and colour, and visual memory", "Hearing, balance, taste and smell", "Fluency, comprehension, repetition and naming", "Posture, gait, tone and coordination", exp="The functions listed under the visual association area are ocular fixation, fixing size/shape/colour and visual memory."),
            q(565, "recall", "A lesion of the visual association area produces which deficit?", "Colour agnosia", "Cerebral achromatopsia", "Pure word deafness", "Gerstmann syndrome", exp="The visual association area's defect line reads lesion → colour agnosia."),
            q(565, "scenario", "Which labels are placed in the medial-view diagram around the primary visual area?", "The calcarine sulcus, the parieto-occipital fissure and the primary visual area labelled area 17", "The auditory cortex and the Sylvian fissure labelled area 41", "The precentral gyrus and the central sulcus labelled area 4", "The angular gyrus and the intraparietal sulcus labelled area 39", exp="The medial-view drawing labels the calcarine sulcus, the parieto-occipital fissure, the sagittal sulci, the lingual and cingulate landmarks and the primary visual area as area 17."),
            q(565, "scenario", "Which vision state is described in Anton's syndrome?", "Cortical blindness with unawareness of blindness: the patient confabulates visual descriptions or blames poor vision on dim light or missing spectacles", "Contralateral hemianopia with full insight and accurate reporting", "Inability to identify objects by vision despite intact fields", "Overshoot of the finger on the finger-nose test", exp="Anton's syndrome describes cortical blindness without awareness of it; the patient confabulates a visual description or blames dim light or missing spectacles."),
            q(565, "recall", "What happens to the light reflex in Anton's syndrome?", "It remains intact", "It is lost bilaterally", "It shows an afferent pupillary defect", "It becomes sluggish on the blind side only", exp="The Anton's syndrome note ends with the statement that the light reflex is intact."),
            q(565, "recall", "Which two colour-vision deficits are listed after Anton's syndrome?", "Colour agnosia and cerebral achromatopsia", "Colour agnosia and dyschromatopsia of rods only", "Achromatopsia and oscillopsia", "Xanthopsia and erythropsia", exp="The two printed colour-vision deficits are colour agnosia and cerebral achromatopsia."),
            q(565, "scenario", "In Balint's syndrome, optic ataxia is clarified as which finding?", "Gauge abnormality: overshoot on the finger-nose test", "Inability to name a seen object", "Unawareness of blindness with confabulation", "Loss of orientation to familiar places", exp="Optic ataxia in Balint's syndrome is parenthesised as gauge abnormality, with overshoot on the finger-nose test."),
            q(565, "recall", "Which two components accompany optic ataxia in Balint's syndrome?", "Oculomotor apraxia and simultanagnosia, perceiving only specific details at a time rather than the whole", "Dressing apraxia and constructional apraxia", "Ideational apraxia and ideomotor apraxia", "Prosopagnosia and alexia without agraphia", exp="Balint's syndrome lists optic ataxia plus oculomotor apraxia and simultanagnosia, the last described as perceiving only specific details at a time rather than the whole."),
            q(565, "recall", "Which lesion produces Balint's syndrome on this page?", "A bilateral occipital lobe lesion", "A unilateral dominant parietal lobe lesion", "A lateral temporal lobe lesion", "A medial prefrontal cortex lesion", exp="Balint's syndrome is attributed to a bilateral occipital lobe lesion in the B/L-lesion column."),
        ],
    ),
])

write(ch32)
print("Chapter 32 authored.")
