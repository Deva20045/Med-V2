import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]

# Load existing coverage (ch 2, 3, 4)
existing_coverage = json.loads((root / 'audit/coverage.json').read_text())
# Filter to chapters 2, 3, 4
base_coverage = [r for r in existing_coverage if r['chapter'] in (2, 3, 4)]

ch5_points = [
  (5, 394, "Tachyarrhythmias definition: HR > 100 bpm", "MED-C5-01"),
  (5, 394, "QRS complex morphological classification: Narrow vs Wide", "MED-C5-01"),
  (5, 394, "Three fundamental causes of tachycardia: enhanced automaticity, triggered activity, and re-entry", "MED-C5-02"),
  (5, 394, "Ventricular origin above bifurcation of Bundle of His: Purkinje fibers -> B/L synchronous activation", "MED-C5-03"),
  (5, 394, "Ventricular origin above His bifurcation: normal/narrow QRS complex (< 0.12 s)", "MED-C5-03"),
  (5, 394, "Ventricular origin below bifurcation of Bundle of His: ventricular myocardium activates ventricles", "MED-C5-04"),
  (5, 394, "Ventricular origin below His bifurcation: wide QRS complex (≥ 0.16 s)", "MED-C5-04"),
  (5, 394, "Supraventricular origin associated with bundle branch block: QRS complex 0.12 - 0.16 s", "MED-C5-05"),
  (5, 394, "Classification triad: SVT (narrow QRS), SVT with conduction block (slightly wide QRS), VT (wide QRS)", "MED-C5-06"),
  (5, 394, "Enhanced automaticity normal mechanism: sinus tachycardia, normal sinus impulse originating from SA node", "MED-C5-07"),

  (5, 395, "Abnormal automaticity: atrial tachycardia (focal/multifocal, has all 3 mechanisms), junctional tachycardia, ischemic VT", "MED-C5-08"),
  (5, 395, "Paroxysmal atrial tachycardia with AV block: associated with digoxin toxicity, precipitated by hypokalemia, due to enhanced automaticity", "MED-C5-09"),
  (5, 395, "Triggered activity early afterdepolarisation (EAD): Long QT Syndrome leading to Torsades de pointes", "MED-C5-10"),
  (5, 395, "Triggered activity late afterdepolarisation (DAD): catecholamine sensitive arrhythmias d/t sympathetic activity and increased intracellular Ca2+", "MED-C5-11"),
  (5, 395, "DAD arrhythmias: RVOT VT, LVOT VT, and sympathetic VT", "MED-C5-11"),
  (5, 395, "Re-entry mechanism: precipitated by PAC or PVC; highly responsive to DC cardioversion", "MED-C5-12"),
  (5, 395, "Micro re-entry circuits: AVNRT, Brugada Syndrome, Atrial Fibrillation", "MED-C5-13"),
  (5, 395, "Macro re-entry circuits: AVRT, Atrial Flutter, Scar VT", "MED-C5-13"),
  (5, 395, "Causes based on QRS: wide QRS VT occurs only in structurally abnormal heart (prior infarction); narrow QRS encompasses automaticity and re-entry", "MED-C5-14"),

  (5, 396, "Interpreting narrow QRS tachycardia: HR = 1500 / 10 = 150 bpm; every QRS preceded by P confirming SAN/atrial origin", "MED-C5-15"),
  (5, 396, "Relative frequency hierarchy: m/c SVT: Sinus tachycardia > AF > AVNRT > AVRT > SART", "MED-C5-16"),
  (5, 396, "AVNRT features: can occur in structurally normal heart, female predominance (F > M), good prognosis", "MED-C5-17"),
  (5, 396, "Normal dual AV nodal pathways: fast pathway conducts rapidly with longer refractory period; slow pathway conducts slowly with shorter refractory period where impulse dissolves", "MED-C5-18"),
  (5, 396, "AVNRT mechanism: premature SV impulse enters recovered slow pathway while fast pathway is refractory, splits to ventricles and retrograde fast pathway", "MED-C5-19"),
  (5, 396, "AVNRT retrograde atrial activation produces inverted P waves in inferior leads II, III, and aVF", "MED-C5-20"),

  (5, 397, "Simultaneous P & QRS formation in 2/3rd of AVNRT patients: P wave buried in QRS complex", "MED-C5-21"),
  (5, 397, "Rate limits: sinus rhythm cannot maintain rate > 180 bpm; rate 200 - 250 bpm favors AVNRT >> AVRT", "MED-C5-22"),
  (5, 397, "Typical AVNRT (95%, PAC trigger, Slow-Fast pathway) vs Atypical AVNRT (5%, PVC trigger, Fast-Slow pathway, D/d Atrial tachycardia)", "MED-C5-23"),
  (5, 397, "Atypical AVNRT conduction limb: enters fast pathway and exits slow pathway", "MED-C5-24"),

  (5, 398, "Typical AVNRT in 1/3rd patients: pseudo S wave (just outside QRS), pseudo r' wave (on r wave), pseudo Q wave (just before Q)", "MED-C5-25"),
  (5, 398, "Pharmacological conversion of AVNRT to normal sinus rhythm by intravenous adenosine", "MED-C5-26"),
  (5, 398, "AVRT clinical features: rarer than AVNRT, fundamentally associated with WPW syndrome", "MED-C5-27"),
  (5, 398, "AVRT types: Orthodromic (entry AV node, exit Bundle of Kent, narrow QRS) vs Antidromic (entry Bundle of Kent, exit AV node, wide QRS)", "MED-C5-28"),

  (5, 399, "Orthodromic AVRT mechanism: well timed PAC enters AV node slowly, ventricles activate synchronously, retrograde conduction via bypass tract re-enters AV node", "MED-C5-29"),
  (5, 399, "Orthodromic AVRT ECG: RP interval 2 boxes ~ 80 - 100 ms (AVRT > AVNRT), P falls just outside QRS", "MED-C5-30"),
  (5, 399, "AVNRT vs AVRT comparison: synchronous activation (+ in AVNRT, - in AVRT), P wave absent in 2/3rd vs outside QRS, structural heart disease absent vs WPW", "MED-C5-31"),
  (5, 399, "RP intervals: AVNRT < 80 ms vs AVRT 80 - 100 ms; both categorized as short RP, long PR tachycardias", "MED-C5-32"),
  (5, 399, "AVNRT hemodynamic stability (stable) vs AVRT (stable/unstable); micro re-entry circuit in AVNRT vs macro re-entry circuit in AVRT", "MED-C5-33"),
  (5, 399, "Interval pattern note: Atrial tachycardia exhibits long RP and short PR interval", "MED-C5-34"),

  (5, 400, "Management goal: AVNRT, AVRT, and Atrial tachycardia operate through AV node -> management is AV nodal block", "MED-C5-35"),
  (5, 400, "Hemodynamically unstable narrow-complex tachycardia management: synchronised DC cardioversion", "MED-C5-36"),
  (5, 400, "Hemodynamically stable DOC for AV nodal block: Adenosine (blocks PAC in AVNRT/AVRT, decreases HR in atrial tachycardia)", "MED-C5-37"),
  (5, 400, "Adenosine pharmacokinetics: T1/2 = 6 s, arm to arm circulation = 15 s, arm to heart circulation = 7.5 s", "MED-C5-38"),
  (5, 400, "Adenosine route and dose: 6 mg through brachial vein (repeat 12 mg + 12 mg, max 30 mg) followed by immediate saline flush", "MED-C5-39"),
  (5, 400, "Adenosine administration procedure: 45° supine position -> administer adenosine -> shift to prone position + raise arm overhead", "MED-C5-40"),
  (5, 400, "Safety protocol: have defibrillator ready; in AVRT, adenosine can induce AF -> VT -> VF -> Death", "MED-C5-41"),
  (5, 400, "Adenosine contraindication in COPD / bronchial asthma (causes bronchospasm); alternatives: verapamil 2.5-5 mg IV (max 15 mg), metoprolol 5 mg IV (max 15 mg), esmolol", "MED-C5-42"),
  (5, 400, "Special indication: Heart failure with AVNRT is managed with Digoxin", "MED-C5-43"),

  (5, 401, "Atrial tachycardia features: structurally abnormal heart, chronic tachyarrhythmia-related cardiomyopathy, follows all 3 mechanisms (m/c enhanced automaticity)", "MED-C5-44"),
  (5, 401, "Atrial tachycardia management: rate reduction to sinus rhythm via beta-blockers (metoprolol) or CCB (verapamil); antiarrhythmics on failure", "MED-C5-45"),
  (5, 401, "Unifocal AT ECG: narrow QRS, rate ~150 bpm, regular rhythm, uniform abnormal P wave, long RP / short PR, and warm-up & cool-down phenomenon", "MED-C5-46"),
  (5, 401, "Multifocal AT (MAT): irregular RR interval with ≥ 3 P wave morphologies; m/c cause COPD/theophylline; management: stop theophylline -> beta-blocker/CCB", "MED-C5-47"),
  (5, 401, "Atrial tachycardia with AV block: association with digoxin toxicity", "MED-C5-48"),

  (5, 402, "AT with AV block ECG: normal P wave + buried P wave, irregular RR intervals, conducted vs missed P waves in 2:1 block", "MED-C5-49"),
  (5, 402, "Junctional tachyarrhythmia: absent P waves at HR ~100 - 110 bpm favors Junctional >> AVNRT/AVRT", "MED-C5-50"),
  (5, 402, "Summary algorithm for irregular RR narrow tachycardias: MAT, Atrial flutter with variable block, Atrial fibrillation, and focal AT with varying AV block", "MED-C5-51"),
  (5, 402, "Summary algorithm for regular RR narrow tachycardias: P wave present (sinus tachycardia, flutter 2:1, SVT short RP vs long RP) vs P wave absent (AVNRT, junctional)", "MED-C5-52"),
]

ch6_points = [
  (6, 403, "Epidemiology of AF: 2nd most common sustained cardiac arrhythmia (1st is sinus tachycardia)", "MED-C6-01"),
  (6, 403, "Mechanical dysfunction in AF: chaotic, disorganised, ineffective contractions causing blood stasis, embolism, and stroke", "MED-C6-02"),
  (6, 403, "Risk factors for AF: Age and Hypertension", "MED-C6-03"),
  (6, 403, "Anatomical site for thrombus formation in AF: Appendages (most common site)", "MED-C6-04"),
  (6, 403, "ECG findings in AF: narrow QRS tachycardia, variable ventricular rate with atrial rate 300 - 600 bpm, irregular RR intervals, fibrillatory waves", "MED-C6-05"),
  (6, 403, "Classification: Paroxysmal (self terminating < 48 hrs or cardioverted < 7 days), Persistent (> 7 days), and Long standing persistent (> 1 year)", "MED-C6-06"),
  (6, 403, "Permanent AF: LA dilated > 4 cm in structural heart disease; management strategy is rate control (accepting AF)", "MED-C6-07"),
  (6, 403, "Valvular AF (mitral stenosis or prosthetic valve + AF) versus Non-valvular AF (all other AF)", "MED-C6-08"),
  (6, 403, "Systemic etiology of AF: OSAS, CKD, Psoriasis, Thyroid disease, Alcohol, cardiopulmonary disease", "MED-C6-09"),
  (6, 403, "Electrolyte disturbances triggering AF: Hypokalemia and Hypomagnesemia", "MED-C6-10"),
  (6, 403, "Symptom pathophysiology in AF: Angina (increased demand), Syncope (decreased circulation), Dyspnea (decreased cardiac output), Palpitation (increased HR)", "MED-C6-11"),

  (6, 404, "Heart rate calculation in irregular AF: 6 second marker rule (HR = number of QRS complexes in 30 large boxes x 10)", "MED-C6-12"),
  (6, 404, "Differential diagnosis of AF on ECG: MAT (≥ 3 P wave morphologies) and Atrial tachycardia with AV block (conducted + missed P waves)", "MED-C6-13"),
  (6, 404, "Treatment in hemodynamically unstable or WPW with AF: synchronised DC cardioversion (Start 100 J -> max 200 J)", "MED-C6-14"),
  (6, 404, "Initial evaluation of stable AF: 2D Echo of LA; dilated LA > 4 cm directs to rate control", "MED-C6-15"),
  (6, 404, "Stable AF with normal LA and onset < 48 hours: no risk of embolism -> direct rhythm control", "MED-C6-16"),
  (6, 404, "Stable AF with onset > 48 hours or unknown: risk of embolism (+) -> Trans Esophageal Echo (TEE) / Cardiac CT to detect clot", "MED-C6-17"),
  (6, 404, "TEE clot positive protocol: 3 weeks of anticoagulants -> pharmacological rhythm control", "MED-C6-18"),
  (6, 404, "Post-cardioversion protocol: 4 weeks of anticoagulants -> assess CHA2DS2-VASc score -> +/- long-term anticoagulation", "MED-C6-19"),

  (6, 405, "Class Ic antiarrhythmics for AF rhythm control: Flecainide and Propafenone", "MED-C6-20"),
  (6, 405, "Rhythm control DOC hierarchy: Vernakalant (DOC, not available in India) and Ibutilide (2nd DOC, m/c used: 1 mg IV over 10 mins)", "MED-C6-21"),
  (6, 405, "DOC for AF rhythm control in structurally abnormal heart: Amiodarone (150 mg IV bolus or 5 mg/kg over 1h -> 1 mg/kg over 8h -> 0.5 mg/kg over 16h)", "MED-C6-22"),
  (6, 405, "Rate control drugs: Verapamil (5-10 mg over 2 min, max 20 mg), Esmolol (500 mcg/kg over 1 min), Propranolol (1 mg over 2 min, max 5 mg), Digoxin (failed LV)", "MED-C6-23"),
  (6, 405, "CHA2DS2-VASc scoring components: CHF (1), HTN (1), Age ≥ 75 (2), DM (1), Stroke/TIA/embolus (2), Vascular disease (1), Age 65-75 (1), Female sex (1)", "MED-C6-24"),
  (6, 405, "CHA2DS2-VASc decision thresholds: Score ≥ 2 requires anticoagulants; Score = 1 ± anticoagulants", "MED-C6-25"),
  (6, 405, "Bleeding risk assessment tool: HAS-BLED score in AF", "MED-C6-26"),
  (6, 405, "Anticoagulants: DOC is Dabigatran; exception is Valvular AF and AF + ESRD where DOC is Warfarin", "MED-C6-27"),
  (6, 405, "Pills in the pocket technique: oral flecainide + beta-blockers in paroxysmal AF taken at symptom onset", "MED-C6-28"),

  (6, 406, "Typical atrial flutter: counterclockwise right atrial circuit, upward left atrial activation, inverted flutter waves in lead II", "MED-C6-29"),
  (6, 406, "Reverse typical atrial flutter: clockwise right atrial circuit, downward left atrial activation, upright flutter waves in lead II", "MED-C6-30"),
  (6, 406, "Atrial flutter features: lateral wall of right atrium (90%), onset < 1 week of open heart surgery, sawtooth ECG appearance", "MED-C6-31"),
  (6, 406, "Atrial flutter management: DC Cardioversion is TOC (25 - 50 J), Ibutilide", "MED-C6-32"),
  (6, 406, "Definitive catheter ablation for atrial flutter: targeting the cavotricuspid isthmus", "MED-C6-33"),
]

ch7_points = [
  (7, 407, "Pathophysiology of broad QRS tachyarrhythmias: ventricular impulse -> cell-to-cell transmission -> broad QRS", "MED-C7-01"),
  (7, 407, "Ventricular rhythms and rate ranges: IVT (15-40 bpm), AIVT (40-100 bpm), VT (> 100 bpm: monomorphic vs polymorphic)", "MED-C7-02"),
  (7, 407, "Accelerated Idioventricular Tachycardia (AIVT) clinical marker: indicates successful thrombolysis / reperfusion", "MED-C7-03"),
  (7, 407, "Etiology of wide QRS: QRS > 0.16 s indicates VT; QRS 0.12 - 0.16 s indicates SVT with BBB or Antidromic AVRT", "MED-C7-04"),
  (7, 407, "VPC mechanism: extrasystole, premature discharge from ventricle occurring earlier than next anticipated sinus beat", "MED-C7-05"),
  (7, 407, "Criteria for VPC: not preceded by P wave, very wide QRS, and ST/T changes in opposite direction (discordance)", "MED-C7-06"),
  (7, 407, "Coupling interval in unifocal VPC: distance between VPC and preceding QRS is always constant", "MED-C7-07"),
  (7, 407, "Compensatory pause in VPC: distance between 2 sinus impulses across VPC equals distance across normal beat (2 x RR interval)", "MED-C7-08"),
  (7, 407, "R on T phenomenon: VPC lies on previous T wave, creating risk for ventricular fibrillation", "MED-C7-09"),

  (7, 408, "Parasystole definition: VPCs with different / variable coupling intervals", "MED-C7-10"),
  (7, 408, "Multifocal VPCs: premature ventricular complexes presenting with different morphologies", "MED-C7-11"),
  (7, 408, "Interpolated VPC: premature ventricular complex sandwiched between two consecutive sinus impulses", "MED-C7-12"),
  (7, 408, "Frequency patterns: Ventricular bigeminy (VPB after every sinus beat), trigeminy (VPB after every 2 sinus beats), couplet (2 VPBs in a row)", "MED-C7-13"),
  (7, 408, "Definition of Ventricular Tachycardia: ≥ 3 VPBs in a row + HR > 100 bpm", "MED-C7-14"),
  (7, 408, "Clinical features and management of VPCs: asymptomatic or palpitations; no treatment required; prophylactic antiarrhythmics contraindicated without significant VT", "MED-C7-15"),

  (7, 409, "Warning signs for VPCs: increased frequency, multifocal, bigeminy/couplet, first episode > 40 yrs, not affected by exercise, parasystole, LV dysfunction", "MED-C7-16"),
  (7, 409, "Monomorphic VT ECG criteria: wide QRS tachycardia (> 0.16 s), rate > 200 bpm, all complexes look alike", "MED-C7-17"),
  (7, 409, "Sustained monomorphic VT definition: sustained duration ≥ 30 seconds", "MED-C7-18"),
  (7, 409, "12-lead ECG panel demonstrating the transition from sustained monomorphic VT to ventricular bigeminy", "MED-C7-19"),

  (7, 410, "Cardinal features of VT: fusion beats (features of both sinus + VPC) and capture beats (point where sinus takes over)", "MED-C7-20"),
  (7, 410, "Brugada sign: distance from onset of QRS complex to nadir of S wave > 100 ms", "MED-C7-21"),
  (7, 410, "Josephson's sign: characteristic notching at the nadir of the S wave", "MED-C7-22"),
  (7, 410, "Precordial concordance: completely positive or completely negative concordance in chest leads indicating VT", "MED-C7-23"),
  (7, 410, "Brugada criteria for VT: RS complex absent or > 100 ms; no P waves / AV dissociation", "MED-C7-24"),
  (7, 410, "Stable VT management in structural heart disease: Amiodarone (150 mg IV bolus x 10 min, then 1 mg/min x 6h, then 0.5 mg/min x 18h)", "MED-C7-25"),
  (7, 410, "Stable VT management without structural heart disease: Procainamide DOC (20-50 mg/min, max 17 mg/kg); Lignocaine post-MI without structural disease; Sotalol", "MED-C7-26"),
  (7, 410, "Unstable VT management: synchronized DC cardioversion 100 - 360 J", "MED-C7-27"),

  (7, 411, "Polymorphic VT: multiple different complexes with changing polarities; usually associated with prolonged QT (Torsades de pointes)", "MED-C7-28"),
  (7, 411, "Acquired causes of TdP: MI, decreased K+, decreased Ca2+, decreased Mg2+, hypothermia, drugs (Class Ia, Ic, III; erythromycin; terfenadine)", "MED-C7-29"),
  (7, 411, "Congenital etiology of TdP: congenital Long QT syndrome", "MED-C7-30"),
  (7, 411, "Differential note on Short QT causes: Hypercalcemia, Digoxin, Hyperthermia", "MED-C7-31"),
  (7, 411, "Management of TdP: immediate defibrillation -> 2 g IV MgSO4 over 10 min -> rhythm stabilization (beta-blockers for congenital, treat cause for acquired)", "MED-C7-32"),
  (7, 411, "Cardioversion vs Defibrillation mechanism: current discharge at patient QRS vs machine discharge; T-wave vulnerable period (20 - 30 ms) risking VF", "MED-C7-33"),

  (7, 412, "Synchronized cardioversion (syncs with patient rhythm) vs unsynchronized defibrillation (no need to connect patient rhythm)", "MED-C7-34"),
  (7, 412, "Paddle placement positions: right side of upper sternum below clavicle and apex of heart (left of nipple)", "MED-C7-35"),
  (7, 412, "Energy settings across arrhythmias: start with 50 J; A. Flutter (50 J), Monomorphic VT (100 J), A. Fib (100 - 200 J), Polymorphic VT (200 J)", "MED-C7-36"),
]

ch8_points = [
  (8, 413, "WPW syndrome demographic profile: Male predominance (M > F)", "MED-C8-01"),
  (8, 413, "Classic ECG findings of WPW: normal P wave, short PR interval, delta waves, near normal QRS, secondary ST & T wave changes", "MED-C8-02"),
  (8, 413, "WPW mechanism: aberrant accessory pathway known as the Bundle of Kent causing ventricular pre-excitation", "MED-C8-03"),
  (8, 413, "Concealed vs Manifest WPW: 12-lead ECG (normal vs abnormal) and antegrade conduction (via AV node vs via Bundle of Kent)", "MED-C8-04"),
  (8, 413, "Arrhythmias triggered by PAC in concealed and manifest WPW: Orthodromic AVRT and Atrial Fibrillation", "MED-C8-05"),
  (8, 413, "Prognosis of Atrial Fibrillation: bad prognosis in concealed WPW responding only to DC cardioversion; better prognosis in manifest WPW d/t early diagnosis", "MED-C8-06"),

  (8, 414, "WPW anatomical classification: Left sided WPW is Type A (most common)", "MED-C8-07"),
  (8, 414, "Left-sided WPW (Type A): small delta wave, conduction Lt -> Rt, positive tall R wave and delta wave in lead V1", "MED-C8-08"),
  (8, 414, "Right-sided WPW (Type B): large delta wave, conduction Rt -> Lt, negative R wave and delta wave in lead V1", "MED-C8-09"),
  (8, 414, "Vector differentiation of Type A vs Type B: left-to-right vs right-to-left conduction and delta wave size", "MED-C8-10"),
  (8, 414, "Manifest WPW activation sequence: Bundle of Kent causes short PR and delta wave; AV node catches up to produce near normal QRS complex", "MED-C8-11"),
  (8, 414, "Concealed WPW management: AVRT treated with Adenosine and EP referral; A.fib treated with synchronised DC cardioversion", "MED-C8-12"),
  (8, 414, "Manifest WPW management: Early diagnosis managed definitively by catheter ablation (definitive Rx)", "MED-C8-13"),
  (8, 414, "Post-conversion finding in manifest WPW: termination of AVRT or A.fib reveals sinus rhythm + delta wave, followed by electrophysiologist referral", "MED-C8-14"),
]

all_new_points = [
  {"chapter": ch, "page": pg, "point": pt, "question": qid}
  for ch, pg, pt, qid in (ch5_points + ch6_points + ch7_points + ch8_points)
]

full_coverage = base_coverage + all_new_points

(root / 'audit/coverage.json').write_text(json.dumps(full_coverage, indent=2, ensure_ascii=False))
print(f"Updated audit/coverage.json with {len(base_coverage)} old + {len(all_new_points)} new = {len(full_coverage)} points!")
