# To run this code, you'll need to install the fpdf2 library.
# Open your VS Code terminal and run:
# pip install fpdf2

from fpdf import FPDF
import os

# Define the anonymized patient data
# This is the data structure that the PDF generator will use.
patient_data = [
    {
        "Patient ID": "FH-001",
        "Date of Birth": "1985-03-12 (Age: 39)",
        "Gender": "Male",
        "Ethnicity": "Caucasian",
        "Chief Complaint (CC)": "Cough and shortness of breath for 3 days.",
        "History of Present Illness (HPI)": (
            "39-year-old male presenting with a productive cough, clear sputum, "
            "increasing shortness of breath, and mild chest tightness for the past 3 days. "
            "Symptoms started gradually with a sore throat and body aches, which have since resolved. "
            "Denies fever. No recent travel. No known sick contacts. States symptoms worsen with exertion."
        ),
        "Past Medical History (PMH)": (
            "- Childhood asthma (well-controlled, no exacerbations in adulthood)\n"
            "- Seasonal allergies\n"
            "- No prior surgeries"
        ),
        "Medications": (
            "- Montelukast 10mg daily (for seasonal allergies)\n"
            "- Albuterol HFA PRN (for asthma, last used >5 years ago)"
        ),
        "Allergies": "Penicillin (rash)",
        "Family History (FH)": (
            "- Mother: Type 2 Diabetes\n"
            "- Father: Hypertension\n"
            "- No significant family history of respiratory conditions."
        ),
        "Social History (SH)": (
            "Non-smoker, occasional alcohol use. Works as an accountant. Lives with partner."
        ),
        "Review of Systems (ROS)": (
            "- Constitutional: Denies fever, chills, night sweats, weight change.\n"
            "- Respiratory: Productive cough, dyspnea on exertion, mild chest tightness. Denies hemoptysis, wheezing.\n"
            "- Cardiovascular: Denies chest pain, palpitations, edema.\n"
            "- Gastrointestinal: Denies nausea, vomiting, diarrhea, constipation.\n"
            "- Musculoskeletal: Denies joint pain, muscle aches (resolved)."
        ),
        "Physical Examination (PE)": (
            "- Vitals: Temp 98.6°F, HR 78, RR 18, BP 128/82, O2 Sat 96% RA.\n"
            "- General: Alert and oriented, appears well-nourished, mild respiratory distress.\n"
            "- Lungs: Symmetrical chest expansion, scattered rhonchi bilaterally, no wheezing or crackles. Good air entry.\n"
            "- Cardiac: Regular rate and rhythm, S1S2 present, no murmurs, rubs, or gallops.\n"
            "- ENT: Clear nasal passages, mild pharyngeal erythema.\n"
            "- Skin: Warm, dry, no rashes."
        ),
        "Assessment": (
            "1. Acute bronchitis, likely viral. Given history of asthma, monitor for exacerbation.\n"
            "2. Productive cough and dyspnea."
        ),
        "Plan": (
            "1. Medications: Prescribe inhaled corticosteroid for 5 days, continue Montelukast.\n"
            "2. Education: Advise rest, hydration, avoid irritants. Educate on signs of worsening respiratory distress (increased shortness of breath, wheezing, fever).\n"
            "3. Follow-up: Return to clinic in 3 days if no improvement or sooner if worsening. Consider chest X-ray if symptoms persist or worsen significantly."
        )
    },
    {
        "Patient ID": "FH-002",
        "Date of Birth": "1948-07-20 (Age: 77)",
        "Gender": "Female",
        "Ethnicity": "Asian",
        "Chief Complaint (CC)": "Chronic knee pain, worse in left knee.",
        "History of Present Illness (HPI)": (
            "77-year-old female presents with bilateral knee pain, predominantly in the left knee, "
            "worsening over the past 5 years. Pain is described as a dull ache, 6/10 at its worst, "
            "aggravated by walking, climbing stairs, and prolonged standing. Relieved minimally by rest "
            "and over-the-counter acetaminophen. Reports morning stiffness lasting approximately 30 minutes. "
            "Limits daily activities, including gardening and social outings. No history of trauma."
        ),
        "Past Medical History (PMH)": (
            "- Osteoarthritis (diagnosed 10 years ago)\n"
            "- Hypertension\n"
            "- Hyperlipidemia\n"
            "- Cholecystectomy (15 years ago)"
        ),
        "Medications": (
            "- Lisinopril 10mg daily\n"
            "- Atorvastatin 20mg daily\n"
            "- Acetaminophen 500mg PRN (up to 3000mg/day)"
        ),
        "Allergies": "None known.",
        "Family History (FH)": (
            "- Mother: Osteoarthritis, Hypertension\n"
            "- Father: Heart disease\n"
            "- Sister: Osteoarthritis"
        ),
        "Social History (SH)": (
            "Retired teacher. Widowed. Lives independently. Used to be active, "
            "but pain limits current physical activity."
        ),
        "Review of Systems (ROS)": (
            "- Musculoskeletal: Chronic knee pain as described, mild swelling noted in left knee intermittently. Denies redness or warmth. Limited range of motion in both knees.\n"
            "- Constitutional: Denies fever, chills, weight change.\n"
            "- Cardiovascular: Denies chest pain, palpitations, edema.\n"
            "- Gastrointestinal: Denies abdominal pain, nausea, vomiting, changes in bowel habits."
        ),
        "Physical Examination (PE)": (
            "- Vitals: Temp 98.2°F, HR 72, RR 16, BP 135/88.\n"
            "- General: Appears comfortable at rest, walks with a slight limp favoring left leg.\n"
            "- Musculoskeletal:\n"
            "    - Knees: Bilateral crepitus on flexion/extension. Mild effusion left knee. Tenderness along medial joint line left knee. Range of motion limited to 0-110 degrees bilaterally. No significant warmth or redness.\n"
            "    - Gait: Antalgic gait, uses a cane occasionally.\n"
            "- Cardiac: Regular rate and rhythm, S1S2, no murmurs.\n"
            "- Lungs: Clear to auscultation bilaterally."
        ),
        "Assessment": (
            "1. Osteoarthritis, bilateral knees, more severe in left.\n"
            "2. Chronic pain."
        ),
        "Plan": (
            "1. Medications: Discuss NSAIDs (e.g., Ibuprofen) with gastroprotection, topical pain relief. Re-evaluate acetaminophen dosing.\n"
            "2. Referral: Refer to Physical Therapy for strengthening exercises and gait training. Refer to Orthopedics for evaluation of potential injections (corticosteroid, hyaluronic acid) or surgical options (knee replacement) if conservative measures fail.\n"
            "3. Education: Weight management advice. Use of assistive devices as needed. Continue low-impact exercises."
        )
    },
    {
        "Patient ID": "FH-003",
        "Date of Birth": "2021-11-20 (Age: 3 years, 8 months)",
        "Gender": "Female",
        "Ethnicity": "Hispanic",
        "Chief Complaint (CC)": "Right ear pain and fever.",
        "History of Present Illness (HPI)": (
            "3-year-old female presents with crying, pulling at her right ear, and irritability for the past 24 hours. "
            "Parents report a fever of 101.5°F (rectal) this morning. Child has had a runny nose and mild cough for 3 "
            "days prior to ear pain onset. Eating and drinking less than usual. No vomiting or diarrhea. "
            "No recent ear infections. Immunizations up-to-date. Attends daycare."
        ),
        "Past Medical History (PMH)": (
            "- Full-term infant, uncomplicated delivery.\n"
            "- No significant childhood illnesses or hospitalizations.\n"
            "- No prior ear infections."
        ),
        "Medications": (
            "- Acetaminophen 160mg PRN for fever/pain (last dose 4 hours ago)."
        ),
        "Allergies": "None known.",
        "Family History (FH)": (
            "- Mother: History of childhood ear infections.\n"
            "- Father: No significant medical history."
        ),
        "Social History (SH)": (
            "Lives with parents and older sibling. Attends daycare 5 days/week."
        ),
        "Review of Systems (ROS)": (
            "- Constitutional: Fever, irritability, decreased appetite.\n"
            "- ENT: Right ear pain, pulling at ear, runny nose (clear discharge), mild cough. Denies sore throat, difficulty swallowing.\n"
            "- Gastrointestinal: Decreased oral intake. Denies vomiting, diarrhea.\n"
            "- Neurological: Crying, no seizures."
        ),
        "Physical Examination (PE)": (
            "- Vitals: Temp 100.8°F (oral), HR 110, RR 24.\n"
            "- General: Irritable but consolable, well-appearing for age.\n"
            "- ENT:\n"
            "    - Ears: Right TM erythematous, bulging, with decreased mobility on pneumatic otoscopy. Left TM clear, mobile.\n"
            "    - Nose: Mild clear rhinorrhea.\n"
            "    - Throat: Mild pharyngeal erythema, no exudates.\n"
            "- Lungs: Clear to auscultation bilaterally.\n"
            "- Cardiac: Regular rate and rhythm, no murmurs.\n"
            "- Abdomen: Soft, non-tender, no organomegaly."
        ),
        "Assessment": (
            "1. Acute Otitis Media (AOM), right ear.\n"
            "2. Viral upper respiratory infection (URI)."
        ),
        "Plan": (
            "1. Medications: Prescribe Amoxicillin 400mg/5mL, 5mL BID for 10 days. Continue Acetaminophen for fever/pain.\n"
            "2. Education: Advise on proper medication administration, fever management, hydration.\n"
            "3. Follow-up: Return to clinic in 10-14 days for recheck or sooner if no improvement or worsening symptoms."
        )
    },
    {
        "Patient ID": "FH-004",
        "Date of Birth": "1970-01-25 (Age: 55)",
        "Gender": "Female",
        "Ethnicity": "African American",
        "Chief Complaint (CC)": "Routine follow-up for Type 2 Diabetes Mellitus.",
        "History of Present Illness (HPI)": (
            "55-year-old female here for routine follow-up for Type 2 Diabetes Mellitus (T2DM). "
            "Diagnosed 8 years ago. Reports consistent home blood glucose monitoring, generally in range "
            "(fasting 100-120 mg/dL, post-meal 140-160 mg/dL). Adheres to diabetic diet and exercises "
            "30 minutes, 3 times per week (walking). No symptoms of hypo/hyperglycemia. Denies blurry vision, "
            "numbness/tingling, or increased thirst/urination. Last A1C 3 months ago was 7.2%."
        ),
        "Past Medical History (PMH)": (
            "- Type 2 Diabetes Mellitus\n"
            "- Hypertension\n"
            "- Obesity (BMI 32)\n"
            "- No prior surgeries."
        ),
        "Medications": (
            "- Metformin 1000mg BID\n"
            "- Lisinopril 20mg daily"
        ),
        "Allergies": "None known.",
        "Family History (FH)": (
            "- Mother: Type 2 Diabetes, Hypertension, Heart Disease\n"
            "- Father: Type 2 Diabetes\n"
            "- Brother: Type 2 Diabetes"
        ),
        "Social History (SH)": (
            "Works as a customer service representative. Married, 2 adult children. "
            "Former smoker (quit 10 years ago). No alcohol use."
        ),
        "Review of Systems (ROS)": (
            "- Constitutional: Denies fever, chills, weight change.\n"
            "- Endocrine: Denies polydipsia, polyuria, polyphagia.\n"
            "- Cardiovascular: Denies chest pain, palpitations.\n"
            "- Neurological: Denies numbness, tingling, weakness.\n"
            "- Ophthalmologic: Denies blurry vision."
        ),
        "Physical Examination (PE)": (
            "- Vitals: Temp 98.4°F, HR 75, RR 16, BP 130/85.\n"
            "- General: Appears well-nourished, alert and oriented.\n"
            "- Skin: No diabetic dermopathy noted.\n"
            "- Feet: Intact sensation to monofilament bilaterally. No ulcers or deformities. Pulses 2+ bilaterally.\n"
            "- Cardiac: Regular rate and rhythm, S1S2, no murmurs.\n"
            "- Lungs: Clear to auscultation bilaterally."
        ),
        "Labs (Today)": (
            "- HbA1c: 6.9%\n"
            "- Fasting Glucose: 115 mg/dL\n"
            "- Lipid Panel: Within normal limits (due to atorvastatin)\n"
            "- Kidney Function (eGFR, Creatinine): Within normal limits."
        ),
        "Assessment": (
            "1. Type 2 Diabetes Mellitus, well-controlled on current therapy (A1C 6.9%).\n"
            "2. Hypertension, controlled.\n"
            "3. Obesity."
        ),
        "Plan": (
            "1. Medications: Continue current medications.\n"
            "2. Education: Reinforce importance of continued healthy diet and regular exercise. Discuss importance of annual eye exams and foot exams.\n"
            "3. Screening: Order microalbuminuria screen for next visit.\n"
            "4. Follow-up: Return in 6 months for routine diabetes follow-up."
        )
    },
    {
        "Patient ID": "FH-005",
        "Date of Birth": "2009-09-01 (Age: 15)",
        "Gender": "Male",
        "Ethnicity": "Caucasian",
        "Chief Complaint (CC)": "Right ankle pain after soccer game.",
        "History of Present Illness (HPI)": (
            "15-year-old male presents with acute right ankle pain sustained during a soccer game yesterday. "
            "States he landed awkwardly after jumping for a header, felt a 'pop' in his ankle, and immediately "
            "experienced sharp pain. Unable to bear weight immediately. Applied ice and elevated, but swelling "
            "and bruising have developed. Pain 8/10 with movement. No prior ankle injuries."
        ),
        "Past Medical History (PMH)": (
            "- Healthy, no chronic medical conditions.\n"
            "- Fractured left wrist at age 10 (healed without complications)."
        ),
        "Medications": (
            "- Ibuprofen 400mg PRN (last dose 2 hours ago)."
        ),
        "Allergies": "None known.",
        "Family History (FH)": (
            "- Mother: No significant medical history.\n"
            "- Father: History of knee ligament injury from sports."
        ),
        "Social History (SH)": (
            "High school student. Plays competitive soccer. Lives with parents and younger sister."
        ),
        "Review of Systems (ROS)": (
            "- Musculoskeletal: Right ankle pain, swelling, bruising. Denies numbness, tingling, or weakness in foot. Unable to bear weight.\n"
            "- Constitutional: Denies fever, chills."
        ),
        "Physical Examination (PE)": (
            "- Vitals: Temp 98.6°F, HR 70, RR 16, BP 118/75.\n"
            "- General: Appears in moderate pain, favoring right leg.\n"
            "- Musculoskeletal:\n"
            "    - Right Ankle: Moderate swelling noted around lateral malleolus. Ecchymosis present. Tenderness to palpation over anterior talofibular ligament (ATFL) and calcaneofibular ligament (CFL). Pain with dorsiflexion and inversion. Limited range of motion due to pain and swelling. Unable to bear weight on affected limb. No bony tenderness along malleoli or base of 5th metatarsal (negative Ottawa ankle rules for fracture clinically).\n"
            "    - Capillary Refill: < 2 seconds in toes.\n"
            "    - Pulses: Dorsalis pedis and posterior tibial pulses 2+ bilaterally.\n"
            "    - Neurological: Intact sensation distal to injury."
        ),
        "Assessment": (
            "1. Acute right ankle sprain, likely moderate to severe (Grade II/III), involving lateral ligaments. Rule out fracture."
        ),
        "Plan": (
            "1. Imaging: X-ray right ankle (AP, Lateral, Oblique) to rule out fracture.\n"
            "2. RICE Protocol: Reinforce Rest, Ice, Compression (ace bandage/brace), Elevation.\n"
            "3. Medications: Continue Ibuprofen for pain and inflammation.\n"
            "4. Orthopedic Referral: If fracture ruled out, refer to sports medicine or physical therapy for rehabilitation. If fracture present, refer to Orthopedics immediately.\n"
            "5. Follow-up: Return to clinic in 1 week or sooner if pain significantly worsens or new symptoms develop. Crutches recommended for non-weight-bearing."
        )
    },
    {
        "Patient ID": "FH-006",
        "Date of Birth": "1990-05-18 (Age: 35)",
        "Gender": "Female",
        "Ethnicity": "South Asian",
        "Chief Complaint (CC)": "Worsening low mood and anxiety.",
        "History of Present Illness (HPI)": (
            "35-year-old female presents with worsening low mood, anhedonia, and anxiety symptoms over the past 3 months. "
            "Reports feeling persistently sad, losing interest in hobbies she once enjoyed (reading, hiking), and "
            "experiencing difficulty sleeping (insomnia, early morning awakening). Increased irritability and fatigue. "
            "Anxiety manifests as constant worry, restlessness, and occasional panic attacks (last one 2 weeks ago). "
            "States stress at work and recent relationship difficulties are contributing factors. Diagnosed with "
            "Major Depressive Disorder and Generalized Anxiety Disorder 2 years ago, previously well-controlled on medication."
        ),
        "Past Medical History (PMH)": (
            "- Major Depressive Disorder\n"
            "- Generalized Anxiety Disorder\n"
            "- Migraines (infrequent)"
        ),
        "Medications": (
            "- Sertraline 50mg daily (patient reports taking inconsistently recently)\n"
            "- Alprazolam 0.25mg PRN for anxiety (uses 2-3 times/week)"
        ),
        "Allergies": "None known.",
        "Family History (FH)": (
            "- Mother: History of depression.\n"
            "- Father: History of anxiety."
        ),
        "Social History (SH)": (
            "Works in marketing. Single. Lives alone. Occasional social alcohol use, denies illicit drug use. "
            "Feels isolated since relationship difficulties."
        ),
        "Review of Systems (ROS)": (
            "- Psychiatric: Low mood, anhedonia, irritability, fatigue, poor concentration, feelings of worthlessness. Anxiety, restlessness, panic attacks, constant worry. Suicidal ideation denied.\n"
            "- Constitutional: Denies fever, chills, significant weight change (reports slight weight loss due to decreased appetite).\n"
            "- Neurological: Denies numbness, tingling, weakness. Occasional mild tension headaches, distinct from migraines.\n"
            "- Sleep: Insomnia, difficulty falling asleep, early morning awakening."
        ),
        "Physical Examination (PE)": (
            "- Vitals: Temp 98.0°F, HR 78, RR 16, BP 120/80.\n"
            "- General: Appears tired, but well-groomed. Maintains eye contact. Speech coherent, normal rate.\n"
            "- Affect: Constricted, congruent with dysphoric mood.\n"
            "- Mood: Reports 'sad, anxious.'\n"
            "- Thought Process: Linear, logical.\n"
            "- Thought Content: Preoccupied with work and relationship issues. No delusions or hallucinations.\n"
            "- Cognition: Alert and oriented x 3, concentration fair.\n"
            "- Insight: Good.\n"
            "- Judgment: Good."
        ),
        "Assessment": (
            "1. Major Depressive Disorder, recurrent, moderate episode.\n"
            "2. Generalized Anxiety Disorder, exacerbated.\n"
            "3. Medication non-adherence."
        ),
        "Plan": (
            "1. Medications: Increase Sertraline to 75mg daily. Emphasize importance of consistent daily dosing. Review Alprazolam use, discuss risks of long-term benzodiazepine use. Explore non-pharmacological anxiety management.\n"
            "2. Therapy: Strong recommendation for individual psychotherapy (CBT preferred) to address coping mechanisms, stress management, and relationship issues. Provide referrals.\n"
            "3. Lifestyle: Encourage consistent sleep hygiene, regular exercise, and healthy diet. Advise on limiting alcohol and caffeine.\n"
            "4. Safety: Assess for suicidal ideation, contract for safety (patient denies SI and agrees to reach out if thoughts arise).\n"
            "5. Follow-up: Return in 2 weeks to assess medication response and adherence, and discuss therapy engagement."
        )
    }
]

# Define a custom PDF class inheriting from FPDF
class MedicalRecordPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Anonymized Medical Record', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')

    def add_section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(230, 230, 230) # Light grey background for titles
        self.cell(0, 8, title, 0, 1, 'L', 1)
        self.ln(2)

    def add_content(self, title, content):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 6, title + ':', 0, 1, 'L')
        self.set_font('Arial', '', 10)
        # MultiCell handles wrapping long text automatically
        self.multi_cell(0, 6, content)
        self.ln(4)

def generate_medical_record_pdf(patient_info):
    """
    Generates a PDF medical record for a single patient.

    Args:
        patient_info (dict): A dictionary containing all the patient's medical data.
    """
    pdf = MedicalRecordPDF()
    pdf.add_page()
    pdf.alias_nb_pages()
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)

    pdf.set_font('Arial', '', 10)

    # Patient Demographics
    pdf.add_section_title("Patient Demographics")
    pdf.add_content("Patient ID", patient_info["Patient ID"])
    pdf.add_content("Date of Birth", patient_info["Date of Birth"])
    pdf.add_content("Gender", patient_info["Gender"])
    pdf.add_content("Ethnicity", patient_info["Ethnicity"])

    # Chief Complaint
    pdf.add_section_title("Chief Complaint (CC)")
    pdf.add_content("", patient_info["Chief Complaint (CC)"])

    # History of Present Illness
    pdf.add_section_title("History of Present Illness (HPI)")
    pdf.add_content("", patient_info["History of Present Illness (HPI)"])

    # Past Medical History
    pdf.add_section_title("Past Medical History (PMH)")
    pdf.add_content("", patient_info["Past Medical History (PMH)"])

    # Medications
    pdf.add_section_title("Medications")
    pdf.add_content("", patient_info["Medications"])

    # Allergies
    pdf.add_section_title("Allergies")
    pdf.add_content("", patient_info["Allergies"])

    # Family History
    pdf.add_section_title("Family History (FH)")
    pdf.add_content("", patient_info["Family History (FH)"])

    # Social History
    pdf.add_section_title("Social History (SH)")
    pdf.add_content("", patient_info["Social History (SH)"])

    # Review of Systems
    pdf.add_section_title("Review of Systems (ROS)")
    pdf.add_content("", patient_info["Review of Systems (ROS)"])

    # Physical Examination
    pdf.add_section_title("Physical Examination (PE)")
    pdf.add_content("", patient_info["Physical Examination (PE)"])

    # Assessment
    pdf.add_section_title("Assessment")
    pdf.add_content("", patient_info["Assessment"])

    # Plan
    pdf.add_section_title("Plan")
    pdf.add_content("", patient_info["Plan"])

    # Define the output directory
    output_dir = "Medical_Records_PDFs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the PDF
    filename = os.path.join(output_dir, f"Medical_Record_{patient_info['Patient ID']}.pdf")
    pdf.output(filename)
    print(f"Generated {filename}")

# Main execution loop
if __name__ == "__main__":
    print("Generating medical record PDFs...")
    for patient_info in patient_data:
        generate_medical_record_pdf(patient_info)
    print("PDF generation complete. Check the 'Medical_Records_PDFs' folder.")

