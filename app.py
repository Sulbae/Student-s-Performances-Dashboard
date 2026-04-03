import streamlit as st
import pandas as pd
import numpy as np
import time
from joblib import load

st.set_page_config(
    page_title="Dropout Risk Assessment App",
    layout="centered",
)

THRESHOLD = 0.6

# Load Artifacts
def load_artifacts():
    try:
        bundle = load("student_dropout_model.pkl")
        model = bundle['model']
        y_le = bundle['label_encoder']
        return model, y_le
    except Exception as e:
        st.error(f"Gagal memuat model: {e}")
        return None, None

MODEL, LABEL_ENCODER = load_artifacts()

def run_inferece(data_input: pd.DataFrame) -> dict:
    # Data preprocessing
    df = data_input.copy()
    ## Feature Selection
    features_to_drop = [
        "Marital status", "Application mode", "Course",
        "Previous qualification", "Nationality",
        "Mother's qualification", "Father's qualification",
        "Mother's occupation", "Father's occupation", "Student ID"
    ]
    df = df.drop(columns=features_to_drop)

    ## Feature Engineering
    df['Application preference'] = df['Application order'].max() - df['Application order'] + 1
    df.drop(columns=['Application order'], inplace=True)

    # classification pipeline
    probs = MODEL.predict_proba(df)[0, 0]
    pred = int(probs >= THRESHOLD)
    pred_label = LABEL_ENCODER.inverse_transform([pred])[0]

    return {"probability": probs, "prediction": pred_label}

# Streamlit UI
st.title("Dropout Risk Assessment App")
st.markdown("Input Data Mahasiswa!")

# Cek status model
if MODEL is not None:
    st.caption("Status: Model sudah siap.")
else:
    st.error("MODEL GAGAL DIMUAT. Periksa folder artifacts.")
    st.stop()

# Input Form
st.subheader(" ")

columns = [
    "Student ID", "Marital status", "Application mode", "Application order", "Course",
    "Attendance", "Previous qualification", "Previous qualification (grade)", "Nationality",
    "Mother's qualification", "Father's qualification", "Mother's occupation", "Father's occupation",
    "Admission grade", "Displaced", "Educational special needs",
    "Debtor", "Tuition fees up to date", "Gender", "Scholarship holder",
    "Age at enrollment", "International",
    "Curricular units 1st sem (credited)", "Curricular units 1st sem (enrolled)", "Curricular units 1st sem (evaluations)",
    "Curricular units 1st sem (approved)", "Curricular units 1st sem (grade)", "Curricular units 1st sem (without evaluations)",
    "Curricular units 2nd sem (credited)", "Curricular units 2nd sem (enrolled)", "Curricular units 2nd sem (evaluations)",
    "Curricular units 2nd sem (approved)", "Curricular units 2nd sem (grade)", "Curricular units 2nd sem (without evaluations)",
    "Unemployment rate", "Inflation rate", "GDP"
]

## Input Personal Information
### 0. Student ID
student_id = st.text_input("Student ID", placeholder="Type Student ID")

### 1. Marital status
marital_status = st.selectbox(
    "Marital status",
    placeholder="Type to search...",
    options=[
        "Single", "Married", "Widowed", "Divorced", "Facto Union", "Legally Separated", "Other"
    ]
)

### 2. Gender
gender = st.radio(
    "Gender",
    options=[
        "Male", "Female"
    ],
    horizontal=True
)

### 3. Age at enrollment
age_at_enroll = st.number_input("Age at enrollment", min_value=18, max_value=100, value=20)

### 4. International
international = st.radio(
    "International",
    options=[
        "Yes", "No"
    ],
    horizontal=True
)

### 5. Nationality
nationality = st.selectbox(
    "Nationality",
    placeholder="Type to search...",
    options=[
        "Portuguese", "German", "Spanish", "Italian", "Dutch", "English",
        "Lithuanian", "Angolan", "Cape Verdean", "Guinean", "Mozambican",
        "Santomean", "Turkish", "Brazilian", "Romanian", "Moldova (Republic of)",
        "Mexican", "Ukrainian", "Russian", "Cuban", "Colombian", "Other"
    ], 
    accept_new_options=True,
    index=None
)

qual_options = [
    "Secondary education",
    "Higher education - bachelor's degree",
    "Higher education - degree",
    "Higher education - master's",
    "Higher education - doctorate",
    "Frequency of higher education",
    "12th year of schooling - not completed",
    "11th year of schooling - not completed",
    "7th year (old)",
    "Other - 11th years of schooling",
    "2nd year complementary high school course",
    "10th year of schooling",
    "10th year of schooling - not completed",
    "General commerce course",
    "Basic education 3rd cycle (9/10/11th year) or equiv",
    "Complementary high school course",
    "Technical professional course",
    "Complementary high school course - not concluded",
    "7th year of schooling - not completed",
    "2nd cycle of general high school course",
    "9th year of schooling - not completed",
    "8th year of schooling",
    "General course of administration and commerce",
    "Supplementary Accounting and Administration",
    "Unknown",
    "Can't read or write",
    "Can read without having a 4th year of schooling",
    "Basic education 1st cycle (4/5th year) or equiv",
    "Basic education 2nd cycle (6/7/8th year) or equiv",
    "Technological specialization course",
    "Higher education - degree (1st cycle)",
    "Specialized higher studies course",
    "Professional higher technical course",
    "Higher education - master (2nd cycle)",
    "Higher education - doctorate (3rd cycle)"
]

occu_options = [
    "Student",
    "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers",
    "Specialists in Intellectual and Scientific Activities",
    "Intermediate Level Technicians and Professions",
    "Administrative staff",
    "Personal Services, Security and Safety Workers and Sellers",
    "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry",
    "Skilled Workers in Industry, Construction and Craftsmen",
    "Installation and Machine Operators and Assembly Workers",
    "Unskilled Workers",
    "Armed Forces Professions",
    "Other Situation",
    "(blank)",
    "Armed Forces Officers",
    "Armed Forces Sergeants",
    "Other Armed Forces personnel",
    "Directors of administrative and commercial services",
    "Hotel, catering, trade and other services directors",
    "Specialists in the physical sciences, mathematics, engineering and related techniques",
    "Health professionals",
    "Teachers",
    "Specialists in finance, accounting, administrative organization, public and commercial relations",
    "Specialists in information and communication technologies (ICT)",
    "Intermediate level science and engineering technicians and professions",
    "Technicians and professionals, of intermediate level of health",
    "Intermediate level technicians from legal, social, sports, cultural and similar services", 
    "Information and communication technology technicians",
    "Office workers, secretaries in general and data processing operators",
    "Data, accounting, statistical, financial services and registry-related operators",
    "Other administrative support staff",
    "personal service workers",
    "Sellers",
    "Personal care workers and the like",
    "Market-oriented farmers and skilled agricultural and animal production workers",
    "Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence",
    "Skilled construction workers and the like, except electricians",
    "Skilled construction workers and the like, except electricians",
    "Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like",
    "Skilled workers in electricity and electronics",
    "Workers in food processing, woodworking, clothing and other industries and crafts",
    "Fixed plant and machine operators",
    "Assembly workers",
    "Vehicle drivers and mobile equipment operators",
    "Cleaning workers",
    "Unskilled workers in agriculture, animal production, fisheries and forestry",
    "Unskilled workers in extractive industry, construction, manufacturing and transport",
    "Meal preparation assistants",
    "Street vendors (except food) and street service providers"
]

### 6. Mother's Information
mothers_qual = st.selectbox(
    "Mother's qualification",
    placeholder="Type to search...",
    options=qual_options,
    accept_new_options=True
)

mothers_occu = st.selectbox(
    "Mother's occupation",
    placeholder="Type to search...",
    options=occu_options,
    accept_new_options=True
)

### 7. Father's Information
fathers_qual = st.number_input(
    "Father's qualification",
    placeholder="Type to search...",
    options=qual_options,
    accept_new_options=True
)

fathers_occu = st.number_input(
    "Father's occupation",
    placeholder="Type to search...",
    options=occu_options,
    accept_new_options=True
)

### 8. Displaced
displaced = st.radio(
    "Displaced",
    options=[
        "Yes", "No"
    ],
    horizontal=True
)

### 9. Educational Special needs
edu_special_needs = st.radio(
    "Educational special needs",
    options=[
        "Yes", "No"
    ],
    horizontal=True
)

## Input Academic Information

course_options = [
    "Biofuel Production Technologies",
    "Animation and Multimedia Design",
    "Social Services (evening attendance)",
    "Agronomy",
    "Communication Design",
    "Veterinary Nursing",
    "Informatics Engineering",
    "Equinculture",
    "Management",
    "Social Service",
    "Tourism",
    "Nursing",
    "Oral Hygiene",
    "Advertising and Marketing Management",
    "Journalism and Communication",
    "Basic Education",
    "Management (evening attendance)"
]

### 1. Course
course = st.selectbox(
    "Course",
    placeholder="Type to search...",
    options=course_options,
    accept_new_options=True
)

### 2. Attendance
attendance = st.radio(
    "Attendance",
    options=[
        "Daytime", "Evening"
    ],
    horizontal=True
)

mode_options = [
    "1st phase - General Contingent",
    "Ordinance No. 612/93",
    "1st phase - Special Contingent (Azores Island)",
    "Holders of other higher courser",
    "Ordinance No. 854-B/99",
    "International Student (Bachelor)",
    "1st phase - Special Contingent (Madeira Island)",
    "2nd phase - General Contingent",
    "3rd phase - General Contingent",
    "Ordinance No. 533-A/99, item b2 (Different Plan)",
    "Ordinance No. 533-A/99, item b3 (Other Institution)",
    "Over 23 years old",
    "Transfer",
    "Change of course",
    "Technological specialization diploma holders",
    "Change of institution/course",
    "Short/cycle diploma holders",
    "Change of institution/course (International)"
]

### 3. Application mode
application_mode = st.selectbox(
    "Application mode",
    placeholder="Type to search...",
    options=mode_options,
    accept_new_options=True
)

### 4. Application order
application_order = st.number_input("Application order", min_value=1, max_value=9, value=1)

### 5. Previous qualification
prev_qual = st.selectbox(
    "Previous qualification",
    placeholder="Type to search...",
    options=qual_options,
    accept_new_options=True
)

### 6. Previous qualification grade
prev_qual_grade = st.number_input("Previous qualification (grade)", min_value=0.00, max_value=200.00, value=100.00)

### 7. Admission grade
admission_grade = st.number_input("Admission grade", min_value=0.00, max_value=200.00, value=100.00)

### 8. Sem 1 Information
curr_units_1_credited = st.number_input("Curricular units 1st sem (credited)", min_value=0, max_value=100, value=1)
curr_units_1_enrolled = st.number_input("Curricular units 1st sem (enrolled)", min_value=0, max_value=100, value=1)
curr_units_1_eval = st.number_input("Curricular units 1st sem (evaluations)", min_value=0, max_value=100, value=1)
curr_units_1_approved = st.number_input("Curricular units 1st sem (approved)", min_value=0, max_value=100, value=1)
curr_units_1_grade = st.number_input("Curricular units 1st sem (grade)", min_value=0, max_value=20, value=10)
curr_units_1_without_eval = st.number_input("Curricular units 1st sem (without evaluations)", min_value=0, max_value=100, value=1)

### 9. Sem 2 Information
curr_units_2_credited = st.number_input("Curricular units 2nd sem (credited)", min_value=0, max_value=100, value=1)
curr_units_2_enrolled = st.number_input("Curricular units 2nd sem (enrolled)", min_value=0, max_value=100, value=1)
curr_units_2_eval = st.number_input("Curricular units 2nd sem (evaluations)", min_value=0, max_value=100, value=1)
curr_units_2_approved = st.number_input("Curricular units 2nd sem (approved)", min_value=0, max_value=100, value=1)
curr_units_2_grade = st.number_input("Curricular units 2nd sem (grade)", min_value=0, max_value=20, value=10)
curr_units_2_without_eval = st.number_input("Curricular units 2nd sem (without evaluations)", min_value=0, max_value=100, value=1)

## Input Economic Information
### Macro Economic Indicators
unemployement_rate = st.number_input("Unemployment rate", min_value=0.0, max_value=100.0, value=0.0)
inflation_rate = st.number_input("Inflation rate", min_value=0.0, max_value=100.0, value=1.0)
gdp = st.number_input("GDP", min_value=0.0, max_value=1_000_000.0, value=10_000.0)

### Financial Information
debtor = st.radio(
    "Debtor",
    options=[
        "Yes", "No"
    ],
    horizontal=True
)

tuition_uptodate = st.radio(
    "Tuition fees up to date",
    options=[
        "Yes", "No"
    ],
    horizontal=True
)

scholarship_holder = st.radio(
    "Scholarship holder",
    options=[
        "Yes", "No"
    ],
    horizontal=True
)

# Menyimpan data ke dalam DataFrame
data_input = pd.DataFrame([[
    student_id, marital_status, application_mode, application_order, course,
    attendance, prev_qual, prev_qual_grade, nationality,
    mothers_qual, fathers_qual, mothers_occu, fathers_occu,
    admission_grade, displaced, edu_special_needs,
    debtor, tuition_uptodate, gender, scholarship_holder,
    age_at_enroll, international,
    curr_units_1_credited, curr_units_1_enrolled, curr_units_1_eval,
    curr_units_1_approved, curr_units_1_grade, curr_units_1_without_eval,
    curr_units_2_credited, curr_units_2_enrolled, curr_units_2_eval,
    curr_units_2_approved, curr_units_2_grade, curr_units_2_without_eval,
    unemployement_rate, inflation_rate, gdp
]], columns=columns)

# Tombol untuk menampilkan data
if st.button("Prediksi Kelayakan Air", type="primary"):

    start_time = time.time()

    st.write("### Data Input:")
    st.dataframe(data_input)
  
    try:
        result = run_inferece(data_input)

        st.write("### Hasil")

        # Dropout Risk 
        st.subheader("Assessment Result:")

        assessment_label = result["prediction"]

        if assessment_label == "Dropout":
            st.write("**Risiko Dropout Tinggi!**")
        else:
            st.write("**Risiko Dropout Rendah!**")

    except Exception as e:
        st.error(f"Terjadi kesalahan sistem: {e}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    st.caption(f"Waktu inferensi: {elapsed_time:.2f} detik")