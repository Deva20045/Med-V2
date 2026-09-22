import json

ch06 = {
  "chapter": 6,
  "title": "Atrial Fibrillation and Flutter",
  "pageRange": "403-406",
  "questions": [
    {
      "id": "MED-C6-01",
      "sec": "Atrial Fibrillation Features, Classification & Etiology",
      "page": 403,
      "fmt": "numeric",
      "q": "Where does atrial fibrillation rank among all sustained cardiac arrhythmias, and which rhythm is the most common overall?",
      "opts": [
        "2nd most common sustained arrhythmia (1st is sinus tachycardia)",
        "1st most common sustained arrhythmia (2nd is sinus tachycardia)",
        "3rd most common sustained arrhythmia (behind sinus tachycardia and AVNRT)",
        "4th most common sustained arrhythmia (behind ventricular fibrillation, VT, and sinus tachycardia)"
      ],
      "ans": 0,
      "exp": "Under Features: 2nd m/c sustained cardiac arrhythmia (1st is sinus tachycardia). (Book p403)"
    },
    {
      "id": "MED-C6-02",
      "sec": "Atrial Fibrillation Features, Classification & Etiology",
      "page": 403,
      "fmt": "fillup",
      "q": "Atrial fibrillation is characterized by chaotic, disorganised, ineffective atrial contractions that cause stasis of blood, leading to ____ and ultimately stroke.",
      "opts": [
        "embolism",
        "coronary spasm",
        "cardiac rupture",
        "cardiac tamponade"
      ],
      "ans": 0,
      "exp": "Features: Chaotic, disorganised, ineffective contractions. Complication: Stasis of blood -> Embolism -> Stroke. (Book p403)"
    },
    {
      "id": "MED-C6-03",
      "sec": "Atrial Fibrillation Features, Classification & Etiology",
      "page": 403,
      "fmt": "recall",
      "q": "Which two primary clinical risk factors (R/F) are explicitly listed on page 403 for atrial fibrillation?",
      "opts": [
        "Age and Hypertension",
        "Smoking and Hyperlipidemia",
        "Obesity and Sedentary lifestyle",
        "Family history and Male sex"
      ],
      "ans": 0,
      "exp": "Under Features: R/F: Age, Hypertension. (Book p403)"
    },
    {
      "id": "MED-C6-04",
      "sec": "Atrial Fibrillation Features, Classification & Etiology",
      "page": 403,
      "fmt": "recall",
      "q": "What is the most common anatomical site (m/c site) of thrombus formation resulting from blood stasis in atrial fibrillation?",
      "opts": [
        "Appendages",
        "Interatrial septum",
        "Crista terminalis",
        "Fossa ovalis"
      ],
      "ans": 0,
      "exp": "Features: m/c site: Appendages (specifically the left atrial appendage). (Book p403)"
    },
    {
      "id": "MED-C6-05",
      "sec": "Atrial Fibrillation Features, Classification & Etiology",
      "page": 403,
      "fmt": "numeric",
      "q": "On the ECG in atrial fibrillation, while the ventricular rate is variable with irregular R-R intervals, what is the characteristic underlying atrial rate?",
      "opts": [
        "300 – 600 bpm",
        "150 – 250 bpm",
        "600 – 900 bpm",
        "100 – 180 bpm"
      ],
      "ans": 0,
      "exp": "ECG features: Narrow QRS tachycardia, Rate: Variable (Atrial rate: 300-600 bpm), R-R interval: Irregular, Fibrillatory waves present. (Book p403)"
    },
    {
      "id": "MED-C6-06",
      "sec": "Atrial Fibrillation Features, Classification & Etiology",
      "page": 403,
      "fmt": "match",
      "q": "Match each temporal classification of atrial fibrillation to its defining duration — 1) Paroxysmal AF 2) Persistent AF 3) Long standing persistent AF … A) Self-terminating < 48 hrs or cardioverted < 7 days B) Lasts > 7 days C) Lasts > 1 year",
      "opts": [
        "1-A, 2-B, 3-C",
        "1-B, 2-A, 3-C",
        "1-C, 2-B, 3-A",
        "1-A, 2-C, 3-B"
      ],
      "ans": 0,
      "exp": "Classification table: Paroxysmal: Self terminating (Usually < 48 hrs) or cardioverted AF < 7 days; Persistent: Lasts > 7 days (> 1 year: Long standing persistent). (Book p403)"
    },
    {
      "id": "MED-C6-07",
      "sec": "Atrial Fibrillation Features, Classification & Etiology",
      "page": 403,
      "fmt": "scenario",
      "q": "An echocardiogram in a patient with chronic AF reveals a left atrium dilated to > 4 cm in the context of structural heart disease. Cardioversion is abandoned. What category does this represent and what is the management strategy?",
      "opts": [
        "Permanent AF; Rate control (accepting AF)",
        "Persistent AF; Urgent electrical rhythm control",
        "Paroxysmal AF; Emergency catheter ablation",
        "Valvular AF; Immediate high-dose IV amiodarone"
      ],
      "ans": 0,
      "exp": "Permanent AF: LA dilated > 4 cm: Structural heart disease; mx: Rate control (Accepting A. fib). (Book p403)"
    },
    {
      "id": "MED-C6-08",
      "sec": "Atrial Fibrillation Features, Classification & Etiology",
      "page": 403,
      "fmt": "truefalse",
      "q": "Which statement correctly defines Valvular versus Non-valvular atrial fibrillation according to the classification table?",
      "opts": [
        "True — Valvular AF is strictly defined by mitral stenosis (MS) or the presence of a prosthetic valve; all other AF is non-valvular",
        "True — Any patient with mitral regurgitation or aortic stenosis is classified under Valvular AF",
        "False — Prosthetic valve replacement converts a patient to Non-valvular AF",
        "False — Mitral stenosis with AF is managed as Non-valvular AF in all clinical guidelines"
      ],
      "ans": 0,
      "exp": "Valvular AF: ms (mitral stenosis) + A.fib OR Prosthetic valve + A.fib. Non-valvular: All other A.fib. (Book p403)"
    },
    {
      "id": "MED-C6-09",
      "sec": "Atrial Fibrillation Features, Classification & Etiology",
      "page": 403,
      "fmt": "oddoneout",
      "q": "Which systemic condition is NOT listed under the etiology of atrial fibrillation on page 403?",
      "opts": [
        "Systemic lupus erythematosus (SLE)",
        "Obstructive sleep apnea syndrome (OSAS)",
        "Chronic kidney disease (CKD)",
        "Psoriasis"
      ],
      "ans": 0,
      "exp": "Etiology lists: OSAS, CKD, Psoriasis, Thyroid disease, Alcohol, Any cardiac/lung disease, and Electrolyte abnormalities. SLE is not listed on this page. (Book p403)"
    },
    {
      "id": "MED-C6-10",
      "sec": "Atrial Fibrillation Features, Classification & Etiology",
      "page": 403,
      "fmt": "fillup",
      "q": "Under electrolyte abnormalities causing atrial fibrillation, the two specific disturbances identified are ____ and hypomagnesemia.",
      "opts": [
        "hypokalemia",
        "hyperkalemia",
        "hypercalcemia",
        "hyponatremia"
      ],
      "ans": 0,
      "exp": "Electrolyte abnormalities listed are: Hypokalemia and Hypomagnesemia. (Book p403)"
    },
    {
      "id": "MED-C6-11",
      "sec": "Atrial Fibrillation Features, Classification & Etiology",
      "page": 403,
      "fmt": "match",
      "q": "Match each clinical symptom of atrial fibrillation to its underlying pathophysiological mechanism — 1) Angina 2) Syncope 3) Dyspnoea 4) Palpitation … A) Increased myocardial oxygen demand B) Decreased cerebral circulation C) Decreased cardiac output D) Increased heart rate",
      "opts": [
        "1-A, 2-B, 3-C, 4-D",
        "1-B, 2-A, 3-D, 4-C",
        "1-C, 2-D, 3-A, 4-B",
        "1-A, 2-C, 3-B, 4-D"
      ],
      "ans": 0,
      "exp": "C/F: Angina: increased demand; Syncope: decreased circulation; Dyspnoea: decreased cardiac output; Palpitation: increased HR. (Book p403)"
    },
    {
      "id": "MED-C6-12",
      "sec": "Investigations, Algorithmic Pathway & Cardioversion",
      "page": 404,
      "fmt": "numeric",
      "q": "How is the average ventricular heart rate calculated in an irregular rhythm like AF using the 6-second marker rule?",
      "opts": [
        "HR = Number of QRS complexes in 30 large boxes × 10",
        "HR = Number of QRS complexes in 15 large boxes × 10",
        "HR = 300 divided by the number of large boxes in the longest RR interval",
        "HR = Number of QRS complexes in 6 large boxes × 30"
      ],
      "ans": 0,
      "exp": "Investigations: 6 second marker rule: HR = No. of QRS complexes in 30 large boxes x 10 (30 large boxes = 6 seconds). (Book p404)"
    },
    {
      "id": "MED-C6-13",
      "sec": "Investigations, Algorithmic Pathway & Cardioversion",
      "page": 404,
      "fmt": "scenario",
      "q": "A patient with irregular narrow tachycardia is evaluated on ECG. Which feature distinguishes the two primary differential diagnoses (MAT vs AT with AV block) from AF?",
      "opts": [
        "MAT has ≥ 3 morphologically different P waves; AT + AV block shows conducted + missed P waves",
        "MAT has identical tall peaked P waves; AT + AV block exhibits chaotic fibrillatory baseline",
        "MAT displays wide monomorphic QRS; AT + AV block displays complete lack of atrial activity",
        "MAT shows short PR with delta waves; AT + AV block shows retrograde P waves in inferior leads"
      ],
      "ans": 0,
      "exp": "D/d: Multifocal atrial tachycardia (MAT): ≥ 3 morphologically different P waves; Atrial tachycardia + AV block: Conducted + missed P waves. (Book p404)"
    },
    {
      "id": "MED-C6-14",
      "sec": "Investigations, Algorithmic Pathway & Cardioversion",
      "page": 404,
      "fmt": "management",
      "q": "What is the immediate treatment of choice for atrial fibrillation occurring in a hemodynamically unstable patient or in Wolff-Parkinson-White (WPW) syndrome?",
      "opts": [
        "Synchronised DC cardioversion (Start: 100 J -> max: 200 J)",
        "Intravenous verapamil 10 mg push over 1 minute",
        "Intravenous digoxin 0.5 mg bolus followed by beta-blockers",
        "Oral flecainide 200 mg single loading dose"
      ],
      "ans": 0,
      "exp": "Hemodynamically unstable / WPW: Synchronised DC cardioversion; Start: 100 J -> max: 200 J. (Book p404)"
    },
    {
      "id": "MED-C6-15",
      "sec": "Investigations, Algorithmic Pathway & Cardioversion",
      "page": 404,
      "fmt": "scenario",
      "q": "A hemodynamically stable patient presents with newly detected AF. Initial 2D echocardiography reveals a left atrium dilated to 4.6 cm (> 4 cm). What strategy does the algorithm dictate?",
      "opts": [
        "Rate control",
        "Immediate rhythm control without anticoagulation",
        "Emergency DC cardioversion at 200 J",
        "Transesophageal echo followed by immediate pharmacological cardioversion"
      ],
      "ans": 0,
      "exp": "Stable pathway: 2D Echo of LA -> Dilated > 4 cm -> Rate control. (Book p404)"
    },
    {
      "id": "MED-C6-16",
      "sec": "Investigations, Algorithmic Pathway & Cardioversion",
      "page": 404,
      "fmt": "management",
      "q": "A hemodynamically stable patient with a normal LA size on 2D echo presents within 24 hours (< 48 hrs) of acute palpitation onset. What is the indicated management?",
      "opts": [
        "Rhythm control (no risk of embolism)",
        "Mandatory 3 weeks of oral anticoagulation prior to any rhythm attempt",
        "Transesophageal echocardiography to rule out left ventricular thrombus",
        "Long-term rate control alone accepting permanent AF"
      ],
      "ans": 0,
      "exp": "Normal LA dimension with onset < 48 hrs -> No risk of embolism -> Rhythm control. (Book p404)"
    },
    {
      "id": "MED-C6-17",
      "sec": "Investigations, Algorithmic Pathway & Cardioversion",
      "page": 404,
      "fmt": "scenario",
      "q": "In a stable AF patient with normal LA size but symptom duration > 48 hours or unknown, what investigation is required to assess embolic risk before attempting cardioversion?",
      "opts": [
        "Trans Esophageal Echo (TEE) / Cardiac CT",
        "Coronary angiography",
        "Cardiac MRI with gadolinium enhancement",
        "Exercise stress testing"
      ],
      "ans": 0,
      "exp": "Onset > 48 hrs / unknown -> Risk of embolism (+) -> Trans Esophageal Echo (TEE) / Cardiac CT to check for clot. (Book p404)"
    },
    {
      "id": "MED-C6-18",
      "sec": "Investigations, Algorithmic Pathway & Cardioversion",
      "page": 404,
      "fmt": "fillup",
      "q": "If TEE or cardiac CT reveals an intracardiac clot in stable AF > 48 hours, the patient must receive ____ weeks of anticoagulants before pharmacological rhythm control is attempted.",
      "opts": [
        "3",
        "1",
        "6",
        "12"
      ],
      "ans": 0,
      "exp": "Clot (+) pathway: 3 wks of anticoagulants -> Pharmacological rhythm control -> 4 wks of anticoagulants -> Assess CHA2DS2-VASc. (Book p404)"
    },
    {
      "id": "MED-C6-19",
      "sec": "Investigations, Algorithmic Pathway & Cardioversion",
      "page": 404,
      "fmt": "numeric",
      "q": "Following pharmacological rhythm control in a previously clot-positive patient, how many weeks of anticoagulation are mandatory before assessing the CHA2DS2-VASc score for long-term therapy?",
      "opts": [
        "4 weeks",
        "1 week",
        "2 weeks",
        "8 weeks"
      ],
      "ans": 0,
      "exp": "Flowchart: Pharmacological rhythm control -> 4 wks of anticoagulants -> Assess CHA2DS2-VASc Score -> +/- Long term anticoagulants. (Book p404)"
    },
    {
      "id": "MED-C6-20",
      "sec": "Pharmacotherapy, Risk Scores & Anticoagulation",
      "page": 405,
      "fmt": "recall",
      "q": "Which two drugs are listed as Class Ic antiarrhythmics for rhythm control in atrial fibrillation?",
      "opts": [
        "Flecainide and Propafenone",
        "Amiodarone and Sotalol",
        "Ibutilide and Dofetilide",
        "Lidocaine and Mexiletine"
      ],
      "ans": 0,
      "exp": "Rhythm control: Flecainide, Propafenone -> Class Ic antiarrhythmics. (Book p405)"
    },
    {
      "id": "MED-C6-21",
      "sec": "Pharmacotherapy, Risk Scores & Anticoagulation",
      "page": 405,
      "fmt": "recall",
      "q": "Which drug is the overall DOC for rhythm control (not available in India), and which is the 2nd DOC (most commonly used in India)?",
      "opts": [
        "Vernakalant (DOC, not in India); Ibutilide (2nd DOC, m/c used: 1 mg IV over 10 mins)",
        "Ibutilide (DOC, not in India); Flecainide (2nd DOC, m/c used: 100 mg orally)",
        "Amiodarone (DOC, not in India); Vernakalant (2nd DOC, m/c used: 3 mg/kg IV)",
        "Propafenone (DOC, not in India); Dofetilide (2nd DOC, m/c used: 500 mcg IV)"
      ],
      "ans": 0,
      "exp": "Vernakalant: DOC (Not available in India); Ibutilide: 2nd DOC (m/c used), 1 mg IV over 10 mins. (Book p405)"
    },
    {
      "id": "MED-C6-22",
      "sec": "Pharmacotherapy, Risk Scores & Anticoagulation",
      "page": 405,
      "fmt": "management",
      "q": "What is the drug of choice (DOC) for rhythm control in atrial fibrillation occurring in a structurally abnormal heart, and what is its dosing schedule?",
      "opts": [
        "Amiodarone: 150 mg IV bolus OR 5 mg/kg over 1 hr -> 1 mg/kg over 8 hrs -> 0.5 mg/kg over 16 hrs",
        "Ibutilide: 1 mg IV bolus over 1 min repeated every 5 minutes up to 4 mg",
        "Flecainide: 200 mg IV bolus over 10 minutes followed by oral propafenone",
        "Dabigatran: 150 mg orally twice daily with immediate electric cardioversion"
      ],
      "ans": 0,
      "exp": "Amiodarone: DOC for structurally abnormal heart: 150 mg IV bolus OR 5 mg/kg over 1 hour -> 1 mg/kg over 8 hrs -> 0.5 mg/kg over 16 hours. (Book p405)"
    },
    {
      "id": "MED-C6-23",
      "sec": "Pharmacotherapy, Risk Scores & Anticoagulation",
      "page": 405,
      "fmt": "match",
      "q": "Match each rate control drug to its specific clinical indication or dosing protocol — 1) Verapamil rate control 2) Esmolol rate control 3) Propranolol rate control 4) Digoxin rate control … A) 5–10 mg over 2 mins (max: 20 mg) B) 500 mcg/kg over 1 min C) 1 mg IV over 2 mins (max: 5 mg) D) Indicated in failed LV",
      "opts": [
        "1-A, 2-B, 3-C, 4-D",
        "1-B, 2-A, 3-D, 4-C",
        "1-C, 2-D, 3-A, 4-B",
        "1-A, 2-C, 3-B, 4-D"
      ],
      "ans": 0,
      "exp": "Rate control: Verapamil: 5-10 mg over 2 mins (max: 20 mg); Esmolol: 500 mcg/kg over 1 min; Propranolol: 1 mg IV over 2 mins (max: 5 mg); Digoxin: Failed LV. (Book p405)"
    },
    {
      "id": "MED-C6-24",
      "sec": "Pharmacotherapy, Risk Scores & Anticoagulation",
      "page": 405,
      "fmt": "scenario",
      "q": "Calculate the CHA2DS2-VASc score for a 77-year-old female patient with hypertension, diabetes mellitus, and a history of ischemic stroke.",
      "opts": [
        "7 points (Age ≥ 75: 2, Stroke: 2, HTN: 1, DM: 1, Female: 1)",
        "5 points (Age ≥ 75: 1, Stroke: 1, HTN: 1, DM: 1, Female: 1)",
        "8 points (Age ≥ 75: 2, Stroke: 2, HTN: 2, DM: 1, Female: 1)",
        "4 points (Age ≥ 75: 2, Stroke: 1, HTN: 1, DM: 0, Female: 0)"
      ],
      "ans": 0,
      "exp": "Score points: C=0, H=1, A (≥75)=2, D=1, S (stroke)=2, V=0, A (65-74)=0, S (female)=1. Total = 1 + 2 + 1 + 2 + 1 = 7. (Book p405)"
    },
    {
      "id": "MED-C6-25",
      "sec": "Pharmacotherapy, Risk Scores & Anticoagulation",
      "page": 405,
      "fmt": "numeric",
      "q": "According to the CHA2DS2-VASc score recommendations, what score threshold requires anticoagulants, and what is indicated for a score of 1?",
      "opts": [
        "Score ≥ 2: Requires anticoagulants; Score = 1: ± Anticoagulants",
        "Score ≥ 1: Requires anticoagulants; Score = 0: ± Anticoagulants",
        "Score ≥ 3: Requires anticoagulants; Score = 2: Aspirin alone",
        "Score ≥ 4: Requires anticoagulants; Score = 1–3: No therapy"
      ],
      "ans": 0,
      "exp": "Score ≥ 2: Requires anticoagulants. = 1: ± Anticoagulants. (Book p405)"
    },
    {
      "id": "MED-C6-26",
      "sec": "Pharmacotherapy, Risk Scores & Anticoagulation",
      "page": 405,
      "fmt": "recall",
      "q": "Which clinical score is specifically noted on page 405 for assessing bleeding risk in atrial fibrillation patients?",
      "opts": [
        "HAS-BLED score",
        "HEART score",
        "TIMI score",
        "GRACE score"
      ],
      "ans": 0,
      "exp": "Note: HAS-BLED score: Bleeding risk assessment in A.fib. (Book p405)"
    },
    {
      "id": "MED-C6-27",
      "sec": "Pharmacotherapy, Risk Scores & Anticoagulation",
      "page": 405,
      "fmt": "management",
      "q": "What is the general drug of choice (DOC) for anticoagulation in AF, and in which two exceptions is Warfarin the mandatory DOC?",
      "opts": [
        "DOC is Dabigatran; Warfarin for Valvular A.fib and A.fib + ESRD",
        "DOC is Warfarin; Dabigatran for Valvular A.fib and A.fib + ESRD",
        "DOC is Apixaban; Rivaroxaban for severe mitral regurgitation and CKD stage 3",
        "DOC is Heparin; Aspirin for prosthetic heart valves and liver failure"
      ],
      "ans": 0,
      "exp": "Anticoagulants: DOC: Dabigatran. Exception: Valvular A.fib, A.fib + ESRD -> DOC: Warfarin. (Book p405)"
    },
    {
      "id": "MED-C6-28",
      "sec": "Pharmacotherapy, Risk Scores & Anticoagulation",
      "page": 405,
      "fmt": "fillup",
      "q": "In the 'pills in the pocket' technique for paroxysmal AF, patients are advised to consume oral flecainide combined with ____ at the acute onset of symptoms.",
      "opts": [
        "β-blockers",
        "digoxin",
        "warfarin",
        "amiodarone"
      ],
      "ans": 0,
      "exp": "Pills in the pocket technique: Oral flecainide + β-blockers, in patients with paroxysmal A.fib, advised to consume at symptom onset. (Book p405)"
    },
    {
      "id": "MED-C6-29",
      "sec": "Atrial Flutter Mechanisms & Management",
      "page": 406,
      "fmt": "recall",
      "q": "In typical atrial flutter, what is the anatomical direction of right atrial re-entry, and how do flutter waves appear in lead II?",
      "opts": [
        "Counterclockwise re-entry; Flutter waves inverted in lead II",
        "Clockwise re-entry; Flutter waves upright in lead II",
        "Figure-of-eight re-entry; Flutter waves biphasic in lead II",
        "Radial re-entry from pulmonary veins; Flutter waves absent in lead II"
      ],
      "ans": 0,
      "exp": "Typical atrial flutter: counterclockwise circuit in Right atrium (upward Left atrium activation), flutter waves inverted in lead II. (Book p406)"
    },
    {
      "id": "MED-C6-30",
      "sec": "Atrial Flutter Mechanisms & Management",
      "page": 406,
      "fmt": "truefalse",
      "q": "Which statement regarding reverse typical atrial flutter is accurate according to the diagram on page 406?",
      "opts": [
        "True — Re-entry in the right atrium is clockwise, left atrial activation is directed downwards, and flutter waves are upright in lead II",
        "True — Reverse typical flutter produces deeply inverted sawtooth flutter waves across leads II, III, and aVF",
        "False — Reverse typical flutter originates strictly from the left atrial appendage",
        "False — In reverse typical flutter, the re-entry circuit moves counterclockwise around the tricuspid valve"
      ],
      "ans": 0,
      "exp": "Reverse typical atrial flutter: clockwise circuit in right atrium, downward left atrium activation, flutter waves upright in lead II. (Book p406)"
    },
    {
      "id": "MED-C6-31",
      "sec": "Atrial Flutter Mechanisms & Management",
      "page": 406,
      "fmt": "scenario",
      "q": "A patient develops palpitations 4 days after undergoing open-heart bypass surgery. ECG demonstrates classic sawtooth waves. What anatomical site accounts for 90% of these cases and what is the typical post-op timing?",
      "opts": [
        "Lateral wall of Rt. Atrium (90%); Onset < 1 wk of open heart surgery",
        "Left atrial posterior wall; Onset > 1 month of open heart surgery",
        "Interventricular septum; Onset within 24 hours of thoracic trauma",
        "Coronary sinus ostium; Onset 2 to 3 weeks following valve replacement"
      ],
      "ans": 0,
      "exp": "Features: Site: Lateral wall of Rt. Atrium (90%); Onset: < 1 wk of open heart surgery; ECG: Sawtooth appearance. (Book p406)"
    },
    {
      "id": "MED-C6-32",
      "sec": "Atrial Flutter Mechanisms & Management",
      "page": 406,
      "fmt": "numeric",
      "q": "What is the treatment of choice (TOC) for acute atrial flutter, and what energy level is delivered?",
      "opts": [
        "DC Cardioversion (TOC): 25 – 50 J",
        "DC Cardioversion (TOC): 200 – 360 J",
        "Unsynchronized defibrillation: 100 – 150 J",
        "DC Cardioversion (TOC): 10 – 15 J"
      ],
      "ans": 0,
      "exp": "Management: DC Cardioversion (TOC): 25-50 J; Ibutilide. (Book p406)"
    },
    {
      "id": "MED-C6-33",
      "sec": "Atrial Flutter Mechanisms & Management",
      "page": 406,
      "fmt": "fillup",
      "q": "For definitive management of typical atrial flutter, catheter ablation is performed targeting which anatomical structure?",
      "opts": [
        "Cavotricuspid isthmus",
        "Pulmonary vein ostia",
        "Bundle of His",
        "Tendon of Todaro"
      ],
      "ans": 0,
      "exp": "Under management: 'Catheter ablation: Site -> Cavotricuspid isthmus.' (Book p406)"
    }
  ],
  "units": [
    {
      "id": "MED-U6-1",
      "ch": 6,
      "n": 1,
      "title": "1. Atrial Fibrillation Features, Classification & Etiology",
      "sec": "Atrial Fibrillation Features, Classification & Etiology",
      "guide": "Arrhythmia rankings, mechanical dysfunction, appendage thrombi, and stroke risk.\nECG rates, fibrillatory waves, and paroxysmal versus persistent versus permanent AF.\nValvular definitions, systemic risk factors, electrolytes, and symptom pathophysiology.",
      "qs": [
        "MED-C6-01", "MED-C6-02", "MED-C6-03", "MED-C6-04", "MED-C6-05",
        "MED-C6-06", "MED-C6-07", "MED-C6-08", "MED-C6-09", "MED-C6-10",
        "MED-C6-11"
      ]
    },
    {
      "id": "MED-U6-2",
      "ch": 6,
      "n": 2,
      "title": "2. Investigations, Algorithmic Pathway & Cardioversion",
      "sec": "Investigations, Algorithmic Pathway & Cardioversion",
      "guide": "6-second rate calculation rule, ECG differentials (MAT and AT with block).\nSynchronized DC cardioversion for instability or pre-excited WPW.\n2D Echo triage, onset thresholds (<48h vs >48h), TEE imaging, and anticoagulation timing.",
      "qs": [
        "MED-C6-12", "MED-C6-13", "MED-C6-14", "MED-C6-15", "MED-C6-16",
        "MED-C6-17", "MED-C6-18", "MED-C6-19"
      ]
    },
    {
      "id": "MED-U6-3",
      "ch": 6,
      "n": 3,
      "title": "3. Pharmacotherapy, Risk Scores & Anticoagulation",
      "sec": "Pharmacotherapy, Risk Scores & Anticoagulation",
      "guide": "Class Ic agents, vernakalant DOC status, ibutilide usage, and amiodarone protocols.\nRate-control agents (verapamil, esmolol, propranolol, digoxin for failed LV).\nCHA2DS2-VASc scoring, HAS-BLED bleeding risk, dabigatran vs warfarin, and pills-in-the-pocket.",
      "qs": [
        "MED-C6-20", "MED-C6-21", "MED-C6-22", "MED-C6-23", "MED-C6-24",
        "MED-C6-25", "MED-C6-26", "MED-C6-27", "MED-C6-28"
      ]
    },
    {
      "id": "MED-U6-4",
      "ch": 6,
      "n": 4,
      "title": "4. Atrial Flutter Mechanisms & Management",
      "sec": "Atrial Flutter Mechanisms & Management",
      "guide": "Typical counterclockwise vs reverse typical clockwise right atrial flutter re-entry.\nLead II flutter wave polarities, post-cardiac-surgery timing, and sawtooth waves.\nLow-energy DC cardioversion (25–50 J) and cavotricuspid isthmus catheter ablation.",
      "qs": [
        "MED-C6-29", "MED-C6-30", "MED-C6-31", "MED-C6-32", "MED-C6-33"
      ]
    }
  ]
}

with open("data/ch06.json", "w", encoding="utf-8") as f:
    json.dump(ch06, f, indent=2, ensure_ascii=False)
print("ch06.json generated successfully!")
