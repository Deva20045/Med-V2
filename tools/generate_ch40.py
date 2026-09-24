#!/usr/bin/env python3
"""Author Chapter 40 Generalised Tonic-Clonic Seizure p608-612 line-to-line."""
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
            qid = f"MED-C{number}-{len(questions)+1:02d}"
            choices = [correct, *distractors]
            shift = (len(questions) * 3 + number) % 4
            choices = choices[shift:] + choices[:shift]
            questions.append({
                "id": qid, "sec": section, "page": page, "fmt": fmt,
                "q": stem, "opts": choices, "ans": choices.index(correct),
                "exp": explanation + f" (Book p{page})",
            })
            ids.append(qid)
        units.append({
            "id": f"MED-U{number}-{unit_no}", "ch": number, "n": unit_no,
            "title": f"{unit_no}. {unit_title}", "sec": section,
            "guide": guide, "qs": ids,
        })
    return {"chapter": number, "title": title, "pageRange": page_range,
            "questions": questions, "units": units}

def q(page, fmt, stem, correct, *distractors, exp):
    assert len(distractors)==3
    return (page, fmt, stem, correct, list(distractors), exp)

def write(chapter):
    path = OUT / f"ch{chapter['chapter']:02d}.json"
    path.write_text(json.dumps(chapter, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(f"{path.name}: {len(chapter['questions'])} Qs / {len(chapter['units'])} units")

ch40 = make_chapter(40, "Generalised Tonic-Clonic Seizure", "608-612", [
("GTCS Causes - Metabolic, Encephalopathy, Encephalitis", "GTCS Causes: Metabolic, Encephalopathy and Encephalitis",
 "GTCS causes start with metabolic hypoglycemia and electrolytes, encephalopathy hepatic uremic, and encephalitis viral HSV-1 with B/L temporal hyperintensity.\nNote K+ and PO4 abnormalities don't produce seizures; autoimmune anti NMDA and paraneoplastic are listed under encephalitis.",
 [
  q(608,"recall","GTCS causes and Syncope heading timestamp is:","00:01:42","00:13:36","00:20:21","00:32:51",exp="GTCS causes and Syncope heading timestamp 00:01:42"),
  q(608,"recall","Causes of GTCS 1. Metabolic includes:","Hypoglycemia","Hyperglycemia with ketoacidosis","K+ and PO4 abnormalities produce seizures","Vasovagal syncope",exp="Causes of GTCS 1. metabolic: Hypoglycemia"),
  q(608,"recall","Electrolyte causes listed under metabolic include:","↓ Na+","↑ K+","↓ PO4 alone produces seizures","↑ PO4 alone produces seizures",exp="Electrolyte causes: ↓ Na+"),
  q(608,"recall","↑ Na+ is noted as:","↑ Na+ (rare)","↑ Na+ common","↓ Na+ rare","↑ Ca2+ rare",exp="Electrolyte ↑ Na+ (rare)"),
  q(608,"recall","Calcium abnormality listed is:","↓ Ca2+ / ↓ Ca2+ + ↑ PO4 3-","↑ Ca2+ / ↓ Ca2+ only","↑ PO4 alone","K+ and PO4 produce seizures",exp="Electrolyte ↓ Ca2+ / ↓ Ca2+ + ↑ PO4 3-"),
  q(608,"recall","Magnesium abnormality listed is:","↓ Mg2+","↑ Mg2+ common","↓ K+","↑ Na+ common",exp="Electrolyte ↓ Mg2+"),
  q(608,"recall","↑ Mg2+ is noted as:","↑ Mg2+ (rare)","↑ Mg2+ common","↓ Mg2+ rare","↓ Ca2+ rare",exp="Electrolyte ↑ Mg2+ (rare)"),
  q(608,"recall","Encephalopathy causes listed are:","Hepatic and Uremic","HSV-1 and JE","Alcohol and Barbiturate","Vasovagal and Cardiac",exp="Encephalopathy: Hepatic, Uremic"),
  q(608,"oddoneout","Pick ODD ONE OUT - K+ and PO4 abnormalities:","Abnormalities don't produce seizures","Abnormalities produce seizures commonly","Abnormalities produce status epilepticus","Abnormalities cause GTCS",exp="Note: K+, PO4 3-: Abnormalities don't produce seizures"),
  q(608,"recall","Encephalitis viral causes include:","HSV-1 encephalitis","Theophylline","Imipenem","Lithium",exp="Encephalitis Viral: HSV-1 encephalitis"),
  q(608,"recall","MRI in HSV-1 encephalitis shows:","B/L Temporal lobe hyperintensity","B/L PCA lesion","White matter hyperintensities","Hippocampal sclerosis only",exp="HSV-1 encephalitis MRI: B/L Temporal lobe hyperintensity"),
  q(608,"management","Rx for HSV-1 encephalitis is:","Acyclovir","IVIg PLEX","Penicillin","Ceftriaxone 2gm IV BD",exp="HSV-1 encephalitis Rx: Acyclovir"),
  q(608,"recall","Autoimmune encephalitis antibody listed is:","Anti NMDA Ab","Anti Na Ab","Anti CRMP5 Ab","Anti Hu 2 Ab",exp="Encephalitis Autoimmune: Anti NMDA Ab"),
  q(608,"recall","Other encephalitis etiology listed is:","Paraneoplastic","Vasovagal","Orthostatic hypotension","Situational syncope",exp="Encephalitis Paraneoplastic"),
 ]),
("GTCS Causes - Brain Injury, Drugs, Withdrawal and Syncope Types", "Brain Injury, Post Stroke, Drugs, Withdrawal and Syncope Types",
 "Brain injury remote/long standing and post stroke seizures are GTCS causes, along with drug non adherence and specific epileptogenic drugs.\nWithdrawal seizures include alcohol, barbiturate, benzodiazepine; syncope types are vasovagal, cardiac, orthostatic hypotension and situational.",
 [
  q(608,"recall","Brain injury cause is described as:","Remote/long standing","Acute and catastrophic","Benign disease","Severe brain parenchyma involved",exp="Brain injury (Remote/long standing)"),
  q(608,"recall","Post stroke seizures are listed as which number cause?","5. Post stroke seizures","4. Brain injury","6. Drug non adherence","7. Drugs",exp="Post stroke seizures listed as 5"),
  q(608,"recall","Drug non adherence/discontinuation is cause number:","6. Drug non adherence/discontinuation","5. Post stroke seizures","7. Drugs","8. Withdrawal seizures",exp="Drug non adherence/discontinuation is cause 6"),
  q(608,"recall","Drugs listed as epileptogenic include theophylline, imipenem, cefepime and:","Quinolones","Penicillin","Acyclovir","IVIg",exp="Drugs: Theophylline, Imipenem, Cefepime, Quinolones"),
  q(608,"recall","Additional drugs listed are lithium and:","TCA","Valproate","Lamotrigine","Levetiracetam",exp="Drugs Lithium, TCA"),
  q(608,"recall","Withdrawal seizures include alcohol, barbiturate and:","Benzodiazepine (BZD)","Theophylline","Imipenem","Cefepime",exp="Withdrawal seizures: Alcohol, Barbiturate, Benzodiazepine (BZD)"),
  q(608,"recall","Syncope types listed are vasovagal, cardiac, orthostatic hypotension and:","Situational syncope","GTCS","Atonic seizures","Myotonic seizures",exp="Syncope Types: vasovagal, Cardiac, Orthostatic hypotension, Situational syncope"),
 ]),
("Seizure vs Syncope Comparison", "Seizure vs Syncope Table",
 "Seizure vs syncope table contrasts precipitating factors, premonitory symptoms, posture, transition, duration, facial appearance and post-event features.\nSeizure has usually none precipitants, aura odd odor, variable posture, immediate transition, minutes unconsciousness, 30-60 s tonic-clonic, cyanosis frothing, prolonged disorientation, muscle aching, occasional tongue bite/incontinence/headache.",
 [
  q(609,"recall","Seizure vs Syncope immediate precipitating factors for seizure are:","Usually none","Emotional stress, valsalva, orthostatic hypotension, cardiac etiologies","Tiredness, nausea, diaphoresis, tunneling of vision","Usually erect posture",exp="Seizure vs Syncope Immediate precipitating factors Seizure Usually none"),
  q(609,"recall","Immediate precipitating factors for syncope are:","Emotional stress, valsalva, orthostatic hypotension, cardiac etiologies","Usually none","None or aura odd odor","Variable",exp="Syncope Immediate precipitating factors Emotional stress, valsalva, orthostatic hypotension, cardiac etiologies"),
  q(609,"recall","Premonitory symptoms in seizure are:","None or aura (Eg: Odd odor)","Tiredness, nausea, diaphoresis, tunneling of vision","Emotional stress valsalva","Usually erect",exp="Premonitory symptoms Seizure None or aura (Eg: Odd odor)"),
  q(609,"recall","Premonitory symptoms in syncope are:","Tiredness, nausea, diaphoresis, tunneling of vision","None or aura odd odor","Usually none","Variable",exp="Premonitory symptoms Syncope Tiredness, nausea, diaphoresis, tunneling of vision"),
  q(609,"recall","Posture at onset in seizure is:","Variable","Usually erect","Gradual over seconds","Seconds",exp="Posture at onset Seizure Variable"),
  q(609,"recall","Posture at onset in syncope is:","Usually erect","Variable","Often immediate","Minutes",exp="Posture at onset Syncope Usually erect"),
  q(609,"recall","Transition to unconsciousness in seizure is:","Often immediate","Gradual over seconds","Seconds","Never >15 s",exp="Transition to unconsciousness Seizure Often immediate"),
  q(609,"recall","Transition to unconsciousness in syncope is:","Gradual over seconds","Often immediate","Minutes","30-60 s",exp="Transition Syncope Gradual over seconds"),
  q(609,"numeric","Duration of unconsciousness in seizure is:","Minutes","Seconds","<5 min","Never >15 s",exp="Duration of unconsciousness Seizure Minutes"),
  q(609,"numeric","Duration of unconsciousness in syncope is:","Seconds","Minutes","Many minutes to hours","30-60 s",exp="Duration of unconsciousness Syncope Seconds"),
  q(609,"numeric","Duration of tonic or clonic movements in seizure is:","30-60 s","Never >15 s","Seconds","<5 min",exp="Duration of tonic or clonic movements Seizure 30-60 s"),
  q(609,"numeric","Duration of tonic or clonic movements in syncope is:","Never >15 s","30-60 s","Minutes","Many minutes to hours",exp="Duration of tonic or clonic movements Syncope Never >15 s"),
  q(609,"recall","Facial appearance during event in seizure is:","Cyanosis, frothing at mouth","Pallor","Normal","Flushing",exp="Facial appearance during event Seizure Cyanosis, frothing at mouth"),
  q(609,"recall","Facial appearance during event in syncope is:","Pallor","Cyanosis frothing at mouth","Cyanosis","Flushing",exp="Facial appearance Syncope Pallor"),
  q(609,"recall","Disorientation and sleepiness after event in seizure is:","Many minutes to hours","<5 min","Sometimes","Rarely",exp="Disorientation and sleepiness after event Seizure Many minutes to hours"),
  q(609,"recall","Disorientation after event in syncope is:","<5 min","Many minutes to hours","Often","Sometimes",exp="Disorientation after event Syncope <5 min"),
  q(609,"recall","Aching of muscles after event in seizure is:","Often","Sometimes","Rarely","Never",exp="Aching of muscles after event Seizure Often"),
  q(609,"recall","Aching of muscles after event in syncope is:","Sometimes","Often","Rarely","Many minutes to hours",exp="Aching of muscles after event Syncope Sometimes"),
  q(609,"recall","Biting of tongue in seizure vs syncope is:","Sometimes vs Rarely","Often vs Sometimes","Rarely vs Sometimes","Never vs Always",exp="Biting of tongue Seizure Sometimes, Syncope Rarely"),
  q(609,"recall","Incontinence in seizure vs syncope is:","Sometimes vs Rarely","Often vs Sometimes","Rarely vs Sometimes","Never >15 s",exp="Incontinence Seizure Sometimes, Syncope Rarely"),
  q(609,"recall","Headache in seizure vs syncope is:","Sometimes vs Rarely","Often vs Sometimes","Many minutes to hours vs <5 min","Cyanosis vs Pallor",exp="Headache Seizure Sometimes, Syncope Rarely"),
 ]),
("Management of GTCS Flowchart and AED Choices", "Management Flowchart and Antiepileptic Drugs",
 "New onset seizure splits into focal LOC+ complex partial and LOC- simple partial, and generalized non motor absence and motor GTCS atonic myotonic.\nAED: CPS medial temporal carbamazepine oxcarbazepine lamotrigine levetiracetam; Absence typical atypical and JME valproate lamotrigine topiramate with ethosuximide note typical <3 years; GTCS valproate > lamotrigine.",
 [
  q(609,"recall","Management of GTCS heading timestamp is:","00:13:36","00:01:42","00:20:21","00:32:51",exp="Management of GTCS timestamp 00:13:36"),
  q(609,"recall","New onset seizure first splits into:","Focal and Generalized","Complex partial and Simple partial","Non motor and Motor","LOC+ and LOC-",exp="New Onset Seizure splits into Focal and Generalized"),
  q(609,"recall","Focal LOC+ is:","Complex Partial Seizure (CPS)","Simple Partial Seizure (SPS)","Absence Seizure","GTCS",exp="Focal LOC+ Complex Partial Seizure (CPS)"),
  q(609,"recall","Focal LOC- is:","Simple Partial Seizure (SPS)","Complex Partial Seizure (CPS)","Absence Seizure","GTCS",exp="Focal LOC- Simple Partial Seizure (SPS)"),
  q(609,"recall","Generalized non motor is:","Absence Seizure","GTCS","Atonic seizures","Myotonic seizures",exp="Generalized Non motor Absence Seizure"),
  q(609,"recall","Generalized motor includes:","GTCS, Atonic seizures, myotonic seizures","CPS and SPS only","Absence only","Vasovagal and cardiac",exp="Generalized motor GTCS, Atonic seizures, myotonic seizures"),
  q(609,"management","Antiepileptic drugs for CPS medial temporal lobe epilepsy include:","Carbamazepine, Oxcarbazepine","Valproate > Lamotrigine only","Ethosuximide only","Folic acid only",exp="CPS (medial temporal lobe epilepsy): Carbamazepine, Oxcarbazepine"),
  q(609,"management","Other AED for CPS include lamotrigine and:","Levetiracetam","Valproate only","Ethosuximide","Felbamate",exp="CPS Lamotrigine, Levetiracetam"),
  q(609,"management","Absence Typical, Atypical and JME drugs are:","Valproate, Lamotrigine, Topiramate","Carbamazepine, Oxcarbazepine","Carbamazepine only","Oxcarbazepine only",exp="Absence Typical Atypical JME Valproate Lamotrigine Topiramate"),
  q(609,"recall","Note for ethosuximide is:","Typical absence <3 years","Typical absence >12 years","Atypical absence lifelong","GTCS first line",exp="Note Ethosuximide Typical absence <3 years"),
  q(609,"management","GTCS AED hierarchy is:","Valproate > Lamotrigine","Carbamazepine > Oxcarbazepine","Ethosuximide > Valproate","Lamotrigine > Valproate",exp="GTCS Valproate > Lamotrigine"),
 ]),
("Pregnancy and Side Effects of AED", "Pregnancy and AED Side Effects",
 "Pregnancy best is lamotrigine least teratogenic, if already on AED folic acid supplementation.\nSide effects: carbamazepine SJS, oxcarbazepine SIADH hyponatremia more than carbamazepine, lamotrigine SJS HLH/MAS, levetiracetam suicidal ideation, valproate alopecia liver NH3 pancreatitis thrombocytopenia weight gain, topiramate renal stones weight loss, zonisamide cognitive slowing, felbamate aplastic anemia, lacosamide PR prolongation.",
 [
  q(610,"management","Pregnancy best AED with least teratogenicity is:","Lamotrigine (Best)","Valproate","Carbamazepine","Topiramate",exp="Pregnancy Lamotrigine (Best): Least teratogenic"),
  q(610,"management","If already on AED in pregnancy, give:","Folic Acid supplementation","Stop all AED","Switch to valproate","Add carbamazepine",exp="If already on AED Folic Acid supplementation"),
  q(610,"recall","Side effect of carbamazepine is:","Steven Johnson Syndrome (SJS)","↑ Risk of SIADH","Suicidal ideation","Alopecia",exp="Side effect Carbamazepine Steven Johnson Syndrome (SJS)"),
  q(610,"recall","Oxcarbazepine side effect is:","↑ Risk of SIADH (↓ Na+) more than Carbamazepine","SJS only","Suicidal ideation","Weight gain",exp="Oxcarbazepine ↑ Risk of SIADH (↓ Na+) more than Carbamazepine"),
  q(610,"recall","Lamotrigine side effects include SJS and:","HLH / MAS (Hemophagocytic lymphohistiocytosis/ macrophage activation syndrome)","Suicidal ideation","Alopecia","Renal stones",exp="Lamotrigine SJS, HLH / MAS (Hemophagocytic lymphohistiocytosis/ macrophage activation syndrome)"),
  q(610,"recall","Levetiracetam side effect is:","Suicidal ideation","Steven Johnson Syndrome","Aplastic anemia","↑ PR Interval",exp="Levetiracetam Suicidal ideation"),
  q(610,"recall","Valproate side effects include alopecia, liver abnormalities, ↑ NH3 and:","Pancreatitis, Thrombocytopenia, Weight gain","Renal stones and Weight loss","Cognitive slowing","Aplastic anemia",exp="Valproate Alopecia, Liver abnormalities, ↑ NH3, Pancreatitis, Thrombocytopenia, Weight gain"),
  q(610,"recall","Topiramate side effects are:","Renal Stones and Weight loss","Alopecia and Weight gain","SJS and HLH/MAS","Suicidal ideation and SJS",exp="Topiramate Renal Stones, Weight loss"),
  q(610,"recall","Zonisamide side effect is:","Cognitive slowing","Aplastic anemia","↑ PR Interval","Steven Johnson Syndrome",exp="Zonisamide Cognitive slowing"),
  q(610,"recall","Felbamate side effect is:","Aplastic anemia","Cognitive slowing","↑ PR Interval","Suicidal ideation",exp="Felbamate Aplastic anemia"),
  q(610,"recall","Lacosamide side effect is:","↑ PR Interval","Aplastic anemia","Cognitive slowing","Renal stones",exp="Lacosamide ↑ PR Interval"),
 ]),
("Status Epilepticus Definition and Classification", "Status Epilepticus Definition, Time Points and Classification",
 "Definition continuous ≥5 minutes or ≥2 discrete seizures without regaining consciousness.\nTime T1 5 mins most ideal to start Rx, treatment started here normally, T2 30 mins beyond risk brain damage, 1 hr within seizure must be controlled. NORSE viral unless proven otherwise. Classification convulsive CSE, non-convulsive NCSE also post CSE, refractory unresponsive to AED + BZD.",
 [
  q(610,"recall","Status epilepticus heading timestamp is:","00:20:21","00:01:42","00:13:36","00:32:51",exp="Status Epilepticus timestamp 00:20:21"),
  q(610,"numeric","Status epilepticus definition continuous seizure duration is:","≥ 5 minutes","≥ 30 minutes","≥ 1 hour","≥ 2 minutes",exp="Definition Continuous seizure ≥ 5 minutes (or) ≥ 2 discrete seizures without regaining consciousness in between"),
  q(610,"recall","Second part of definition is:","≥ 2 discrete seizures without regaining consciousness in between","≥ 2 seizures with regaining consciousness","≥ 1 seizure with aura","≥ 3 seizures with 24 hrs separation",exp="Definition ≥ 2 discrete seizures without regaining consciousness in between"),
  q(610,"numeric","T1 time point is:","5 mins (T1)","30 mins (T2)","1 hr","0 mins",exp="Time T1 5 mins (T1)"),
  q(610,"recall","T1 is described as:","Most ideal time to start Rx","Treatment started here normally","Risk of brain damage beyond","Within this time seizure must be controlled",exp="T1 Most ideal time to start Rx"),
  q(610,"numeric","T2 time point is:","30 mins (T2)","5 mins (T1)","1 hr","0 mins",exp="Time 30 mins (T2)"),
  q(610,"recall","T2 beyond this risk is:","Risk of brain damage","Most ideal time to start Rx","Treatment started here normally","Within this time seizure must be controlled",exp="Beyond T2 Risk of brain damage"),
  q(610,"numeric","Within 1 hr rule is:","Within this time, seizure must be controlled","Most ideal time to start Rx","Treatment started here normally","Risk of brain damage",exp="1 hr Within this time, seizure must be controlled"),
  q(610,"recall","NORSE is:","New Onset Refractory Status Epilepticus is viral in etiology unless proven otherwise","Benign disease","Acute and catastrophic","Benign centrotemporal epilepsy",exp="Note NORSE (New Onset Refractory Status Epilepticus) is viral in etiology unless proven otherwise"),
  q(610,"recall","Classification includes convulsive status epilepticus (CSE), non-convulsive SE (NCSE) also seen post CSE and:","Refractory SE unresponsive to AED + BZD","Absence seizure","GTCS","Atonic seizures",exp="Classification Convulsive status epilepticus (CSE), Non-convulsive SE (NCSE) (Also seen post CSE), Refractory SE unresponsive to AED + BZD"),
  q(610,"recall","Non-convulsive SE is also seen:","Post CSE","Pre CSE only","With vasovagal syncope","With cardiac syncope",exp="Non-convulsive SE (NCSE) (Also seen post CSE)"),
  q(610,"recall","Refractory SE is defined as:","Unresponsive to AED + BZD","Responsive to AED only","Unresponsive to acyclovir","Responsive to valproate only",exp="Refractory SE unresponsive to AED + BZD"),
 ]),
("C/F and Management - Compensatory Phase and EEG", "Clinical Features and EEG Monitoring",
 "Initial compensatory sympathetic overdrive ↑CO ↑BP ↑blood sugar ↑lactate.\nDecompensation cardiac arrest, rhabdomyolysis + ATN + electrolyte ↓Ca ↓PO4 ↑K, MODS, ↑ICP herniation coning, hyperthermia. Mx EEG continuous monitoring ≥48h in comatose to evaluate NCSE.",
 [
  q(611,"recall","Initial compensatory phase is:","Sympathetic overdrive","Parasympathetic overdrive","No overdrive","Vasovagal",exp="Initial Compensatory Phase Sympathetic overdrive"),
  q(611,"recall","Compensatory ↑ includes CO, BP, blood sugar and:","↑ lactate","↓ lactate","↓ CO","↓ BP",exp="Initial Compensatory Phase ↑ CO, ↑ BP, ↑ blood sugar, ↑ lactate"),
  q(611,"recall","Decompensation phase includes cardiac arrest and:","Rhabdomyolysis + Acute Tubular Necrosis + Electrolyte imbalance","↑ CO and ↑ BP","Sympathetic overdrive","Continuous monitoring",exp="Decompensation Phase Cardiac arrest, Rhabdomyolysis + Acute Tubular Necrosis + Electrolyte imbalance"),
  q(611,"recall","Electrolyte imbalance in decompensation is:","↓ Ca2+, ↓ PO4 3-, ↑ K+","↑ Ca2+, ↑ PO4, ↓ K+","↓ Na+ and ↑ Na+","K+ PO4 don't produce seizures",exp="Decompensation Electrolyte imbalance ↓ Ca2+, ↓ PO4 3-, ↑ K+"),
  q(611,"recall","Decompensation includes MODS and:","↑ Intracranial Pressure: Herniation, coning","↑ CO and ↑ BP","Sympathetic overdrive","Tiredness nausea",exp="Decompensation MODS, ↑ Intracranial Pressure Herniation coning"),
  q(611,"recall","Other decompensation feature is:","Hyperthermia","Hypothermia","Pallor","Cyanosis frothing",exp="Decompensation Hyperthermia"),
  q(611,"recall","Mx EEG is:","Continuous monitoring","Intermittent monitoring","No monitoring","Single EEG only",exp="Mx EEG Continuous monitoring"),
  q(611,"numeric","EEG monitoring duration in comatose to evaluate NCSE is:","≥48 hours","≥5 minutes","30 mins","1 hr",exp="EEG ≥48 hours in comatose to evaluate NCSE"),
 ]),
("Status Epilepticus Management Flowchart", "Status Epilepticus Management",
 "Rapid IV access minimum 2 lines; No IV IM midazolam 0.2 mg/kg max10 or buccal/intranasal 0.5 mg/kg max10.\nIf not stop in 5 min achieve IV access; Yes IV lorazepam 0.1 mg/kg max4 or slow IV diazepam 1mL in 4mL NS.\nRepeat lorazepam 0.1 mg/kg; shift to 2nd line through 2nd IV line valproate 30-40 @6, phenytoin 20 @50, fosphenytoin 20 @150, levetiracetam 30-40.\nIf not stop in 20 min 3rd line propofol phenobarbitone thiopentone.",
 [
  q(611,"recall","Rapid IV access minimum lines is:","Minimum 2 lines","Minimum 1 line","Minimum 3 lines","No IV access",exp="Rapid IV access available minimum 2 lines"),
  q(611,"management","If no IV access, give:","IM midazolam 0.2 mg/kg (max 10 mg) or Buccal or intranasal midazolam 0.5 mg/kg (max 10 mg)","IV lorazepam 0.1 mg/kg max 4 mg","IV phenytoin 20 mg/kg","Propofol",exp="No IV IM midazolam 0.2 mg/kg (max 10 mg) or Buccal or intranasal midazolam 0.5 mg/kg (max 10 mg)"),
  q(611,"numeric","IM midazolam dose is:","0.2 mg/kg (max 10 mg)","0.5 mg/kg (max 10 mg)","0.1 mg/kg (max 4 mg)","20 mg/kg @50 mg/min",exp="IM midazolam 0.2 mg/kg (max 10 mg)"),
  q(611,"numeric","Buccal or intranasal midazolam dose is:","0.5 mg/kg (max 10 mg)","0.2 mg/kg (max 10 mg)","0.1 mg/kg (max 4 mg)","30-40 mg/kg",exp="Buccal or intranasal midazolam 0.5 mg/kg (max 10 mg)"),
  q(611,"recall","If seizures do not stop in 5 min when no IV, next step is:","Achieve IV access","Shift to 2nd line drugs","Give 3rd line drugs","Stop treatment",exp="If seizures do not stop in 5 min, achieve IV access"),
  q(611,"management","If IV access Yes, give:","IV Lorazepam 0.1 mg/kg slow push (max 4 mg) or Slow IV Diazepam 1 mL in 4 mL NS","IM midazolam 0.2 mg/kg","Valproate 30-40 mg/kg","Propofol",exp="Yes IV Lorazepam 0.1 mg/kg slow push (max 4 mg) or Slow IV Diazepam 1 mL in 4 mL NS"),
  q(611,"numeric","IV lorazepam dose is:","0.1 mg/kg (max 4 mg)","0.2 mg/kg (max 10 mg)","0.5 mg/kg (max 10 mg)","20 mg/kg @50 mg/min",exp="IV Lorazepam 0.1 mg/kg slow push (max 4 mg)"),
  q(611,"recall","Slow IV diazepam is given as:","1 mL in 4 mL NS","0.2 mg/kg max10","0.5 mg/kg max10","20 mg/kg @50 mg/min",exp="Slow IV Diazepam 1 mL in 4 mL NS"),
  q(611,"management","If seizures do not stop in 5 min after IV lorazepam, next is:","Repeat IV Lorazepam 0.1 mg/kg slow push","Shift to 3rd line directly","Give oral AED","Stop",exp="If seizures do not stop in 5 min Repeat IV Lorazepam 0.1 mg/kg slow push"),
  q(611,"management","Shift to 2nd line drugs through:","2nd IV line","1st IV line","Oral route","IM route",exp="Shift to 2nd line drugs Through 2nd IV line"),
  q(611,"management","If possibility of subtherapeutic levels, valproate can be tried:","30-40 mg/kg @ 6 mg/kg/min","20 mg/kg @50 mg/min","20 mg/kg @150 mg/min","30-40 mg/kg only",exp="If possibility of subtherapeutic levels, Valproate 30-40 mg/kg @ 6 mg/kg/min can be tried"),
  q(611,"management","IV phenytoin dose and rate is:","20 mg/kg @ 50 mg/min","20 mg/kg @150 mg/min","30-40 mg/kg @6 mg/kg/min","0.1 mg/kg max4",exp="IV Phenytoin 20 mg/kg @ 50 mg/min"),
  q(611,"management","IV fosphenytoin dose and rate is:","20 mg/kg @150 mg/min","20 mg/kg @50 mg/min","30-40 mg/kg @6 mg/kg/min","0.2 mg/kg max10",exp="IV Fosphenytoin 20 mg/kg @150 mg/min"),
  q(611,"management","IV levetiracetam dose is:","30-40 mg/kg","20 mg/kg @50 mg/min","20 mg/kg @150 mg/min","0.1 mg/kg max4",exp="IV Levetiracetam 30-40 mg/kg"),
  q(611,"numeric","If seizures do not stop in 20 min, go to:","3rd line drugs","2nd line drugs","Repeat lorazepam","Achieve IV access",exp="If seizures do not stop in 20 min 3rd line drugs"),
  q(611,"management","3rd line drugs examples are:","Eg. propofol, phenobarbitone, thiopentone","Valproate, phenytoin, fosphenytoin","Midazolam only","Lorazepam only",exp="3rd line drugs Eg propofol, phenobarbitone, thiopentone"),
 ]),
("Childhood Seizures Classification", "Childhood Seizures and Lafora Disease",
 "Childhood seizures split into epileptic encephalopathies Lennox Gastaut West Dravet, Lafora's disease, Rolandic benign centrotemporal epilepsy.\nTable West age -, Dravet <1 yr, Lafora 10-18 yr, Rolandic before puberty; seizure types infantile spasms febrile myoclonic CPS atypical absence progressive myoclonic epilepsy SPS infrequent; mental retardation + + - -; other features tuberous sclerosis, AR dementia hallucinations PAS+ve inclusions, m/c seizures in childhood; EEG hypsarrhythmia mountain waves, centrotemporal spikes; histopathology PAS+ intracellular inclusions.",
 [
  q(612,"recall","Childhood seizures heading timestamp is:","00:32:51","00:01:42","00:13:36","00:20:21",exp="Childhood Seizures timestamp 00:32:51"),
  q(612,"recall","Childhood seizures split into epileptic encephalopathies, Lafora's disease and:","Rolandic Seizures (Benign centrotemporal epilepsy)","GTCS","Atonic seizures","Absence seizures",exp="Childhood Seizures Epileptic Encephalopathies, Lafora's disease, Rolandic Seizures (Benign centrotemporal epilepsy)"),
  q(612,"recall","Epileptic encephalopathies include Lennox Gastaut Syndrome, West Syndrome and:","Dravet's Syndrome","Lafora's disease","Rolandic Seizures","GTCS",exp="Epileptic Encephalopathies Lannox Gastaut Syndrome, West Syndrome, Dravet's Syndrome"),
  q(612,"numeric","Dravet's syndrome age group is:","<1 year","10-18 years","Before puberty","- (not specified)",exp="Dravet's Syndrome Age Group <1 year"),
  q(612,"numeric","Lafora's disease age group is:","10-18 years","<1 year","Before puberty","- (not specified)",exp="Lafora's disease Age Group 10-18 years"),
  q(612,"recall","Rolandic seizures age group is:","Before puberty","<1 year","10-18 years","- (not specified)",exp="Rolandic Seizures Age Group Before puberty"),
  q(612,"recall","West syndrome age group in table is:","- (dash)","<1 year","10-18 years","Before puberty",exp="West Syndrome Age Group -"),
  q(612,"recall","West syndrome type of seizure is:","Infantile spasms","Febrile seizures myoclonic CPS atypical absence","Progressive myoclonic epilepsy","SPS (Infrequent)",exp="West Syndrome Type of seizure Infantile spasms"),
  q(612,"recall","Dravet's syndrome type of seizure is:","Febrile seizures: myoclonic, CPS, atypical absence","Infantile spasms","Progressive myoclonic epilepsy","SPS (Infrequent)",exp="Dravet's Syndrome Type of seizure Febrile seizures myoclonic CPS atypical absence"),
  q(612,"recall","Lafora's disease type of seizure is:","Progressive myoclonic epilepsy","Infantile spasms","Febrile seizures myoclonic","SPS (Infrequent)",exp="Lafora's disease Type of seizure Progressive myoclonic epilepsy"),
  q(612,"recall","Rolandic seizures type of seizure is:","SPS (Infrequent)","Infantile spasms","Febrile seizures myoclonic","Progressive myoclonic epilepsy",exp="Rolandic Seizures Type of seizure SPS (Infrequent)"),
  q(612,"recall","Mental retardation in West syndrome is:","+","-","Not mentioned","- for all",exp="West Syndrome Mental retardation +"),
  q(612,"recall","Mental retardation in Dravet's syndrome is:","+","-","Not mentioned","- for all",exp="Dravet's Syndrome Mental retardation +"),
  q(612,"recall","Mental retardation in Lafora's disease is:","-"," + ","Not mentioned","+ for all",exp="Lafora's disease Mental retardation -"),
  q(612,"recall","Mental retardation in Rolandic seizures is:","-","+","Not mentioned","+ for all",exp="Rolandic Seizures Mental retardation -"),
  q(612,"recall","Other features West syndrome is:","Associated with tuberous sclerosis","AR inheritance dementia hallucinations","m/c seizures in childhood","- (none)",exp="West Syndrome Other features Associated with tuberous sclerosis"),
  q(612,"recall","Other features Lafora's disease include AR inheritance, dementia, hallucinations and:","Bx: PAS +ve inclusions","Associated with tuberous sclerosis","m/c seizures in childhood","- (none)",exp="Lafora's disease Other features AR inheritance, Dementia, Hallucinations, Bx PAS +ve inclusions"),
  q(612,"recall","Other features Rolandic seizures is noted as:","m/c seizures in childhood","Associated with tuberous sclerosis","AR inheritance dementia","- (none)",exp="Rolandic Seizures Other features m/c seizures in childhood"),
  q(612,"recall","Other features Dravet's syndrome is:","- (none)","Associated with tuberous sclerosis","AR inheritance","m/c seizures in childhood",exp="Dravet's Syndrome Other features -"),
  q(612,"recall","EEG in West syndrome is:","Hypsarrhythmia (mountain waves)","Centrotemporal Spikes","- (none)","PAS +ve inclusions",exp="West Syndrome EEG Hypsarrhythmia (mountain waves)"),
  q(612,"recall","EEG in Rolandic seizures is:","Centrotemporal Spikes","Hypsarrhythmia (mountain waves)","- (none)","PAS +ve inclusions",exp="Rolandic Seizures EEG Centrotemporal Spikes"),
  q(612,"recall","EEG in Dravet's syndrome is:","- (none)","Hypsarrhythmia","Centrotemporal Spikes","PAS +ve",exp="Dravet's Syndrome EEG -"),
  q(612,"recall","EEG in Lafora's disease is:","- (none)","Hypsarrhythmia","Centrotemporal Spikes","PAS +ve",exp="Lafora's disease EEG -"),
  q(612,"recall","Lafora's disease histopathology shows:","PAS + intracellular inclusions with arrow","Hypsarrhythmia mountain waves","Centrotemporal spikes","B/L Temporal lobe hyperintensity",exp="Lafora's disease Histopathology Arrow PAS + intracellular inclusions"),
 ]),
])

write(ch40)
