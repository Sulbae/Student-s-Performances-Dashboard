import streamlit as st
import pandas as pd
import time
from joblib import load

st.set_page_config(
    page_title="Dropout Risk Assessment App",
    layout="centered",
)

THRESHOLD = 0.5

# Load Artifacts
def load_artifacts():
    try:
        preprocess = load("artifacts/preprocessing_pipeline.pkl")
        clf_model  = load("artifacts/rf_classifier_model.pkl")
        return preprocess, clf_model
    except Exception as e:
        st.error(f"Gagal memuat model: {e}")
        return None, None

PREPROCESSOR, CLF_MODEL = load_artifacts()

def run_inferece(data_input: pd.DataFrame) -> dict:
    # preprocessing
    X = PREPROCESSOR.transform(data_input)
    # classification
    probs = CLF_MODEL.predict_proba(X)[0, 1]
    pred = int(probs >= THRESHOLD)

    return {"probability": probs, "prediction": pred}

# Streamlit UI
st.title("Dropout Risk Assessment App")
st.markdown("Input Data Mahasiswa!")

# Cek status model
if CLF_MODEL is not None:
    st.caption(f"Status: Model sudah siap.")
else:
    st.error("MODEL GAGAL DIMUAT. Periksa folder artifacts.")
    st.stop()

# Input Form
st.subheader(" ")

columns = [
    "Marital status", "Application mode", "Application order", "Course",
    "Attendance", "Previous qualification", "Previous qualification (grade)", "nationality",
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

## Input data numerik
marital_status = st.number_input("Marital status", min_value=0.1, max_value=14.0, value=7.0)
application_mode = st.number_input("Application mode", min_value=0.1, max_value=1000.0, value=200.0)
application_order = st.number_input("Application order", min_value=0.1, max_value=100000.0, value=20000.0)
course = st.number_input("Course", min_value=0.1, max_value=100.0, value=7.0)
attendance = st.number_input("Attendance", min_value=0.1, max_value=1000.0, value=300.0)
prev_qual = st.number_input("Previous qualification", min_value=0.1, max_value=1000.0, value=400.0)
prev_qual_grade = st.number_input("Previous qualification (grade)", min_value=0.1, max_value=1000.0, value=15.0)
nationality = st.number_input("Nationality", min_value=0.1, max_value=1000.0, value=80.0)
mothers_qual = st.number_input("Mother's qualification", min_value=0.1, max_value=100.0, value=4.0)
fathers_qual = st.number_input("Father's qualification", min_value=0.1, max_value=14.0, value=7.0)
mothers_occu = st.number_input("Mother's occupation", min_value=0.1, max_value=1000.0, value=200.0)
fathers_occu = st.number_input("Father's occupation", min_value=0.1, max_value=100000.0, value=20000.0)
admission_grade = st.number_input("Admission grade", min_value=0.1, max_value=100.0, value=7.0)
displaced = st.number_input("Displaced", min_value=0.1, max_value=1000.0, value=300.0)
edu_special_needs = st.number_input("Educational special needs", min_value=0.1, max_value=1000.0, value=400.0)
debtor = st.number_input("Debtor", min_value=0.1, max_value=1000.0, value=15.0)
tuition_uptodate = st.number_input("Tuition fees up to date", min_value=0.1, max_value=1000.0, value=80.0)
gender = st.number_input("Gender", min_value=0.1, max_value=100.0, value=4.0)
scholarship_holder = st.number_input("Scholarship holder", min_value=0.1, max_value=1000.0, value=200.0)
age_at_enroll = st.number_input("Age at enrollment", min_value=0.1, max_value=100000.0, value=20000.0)
international = st.number_input("International", min_value=0.1, max_value=100.0, value=7.0)

curr_units_1_credited = st.number_input("Curricular units 1st sem (credited)", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_1_enrolled = st.number_input("Curricular units 1st sem (enrolled)", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_1_eval = st.number_input("Curricular units 1st sem (evaluations)", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_1_approved = st.number_input("Curricular units 1st sem (approved)", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_1_grade = st.number_input("Curricular units 1st sem (grade)", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_1_without_eval = st.number_input("Curricular units 1st sem (without evaluations)", min_value=0.1, max_value=1000.0, value=300.0)

curr_units_2_credited = st.number_input("Curricular units 2nd sem (credited)", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_2_enrolled = st.number_input("Curricular units 2nd sem (enrolled)", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_2_eval = st.number_input("Curricular units 2nd sem (evaluations)", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_2_approved = st.number_input("Curricular units 2nd sem (approved)", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_2_grade = st.number_input("Curricular units 2nd sem (grade)", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_2_without_eval = st.number_input("Curricular units 2nd sem (without evaluations)", min_value=0.1, max_value=1000.0, value=300.0)

unemployement_rate = st.number_input("Unemployment rate", min_value=0.1, max_value=1000.0, value=400.0)
inflation_rate = st.number_input("Inflation rate", min_value=0.1, max_value=1000.0, value=15.0)
gdp = st.number_input("GDP", min_value=0.1, max_value=1000.0, value=80.0)

# Menyimpan data ke dalam DataFrame
data_input = pd.DataFrame([[
    marital_status, application_mode, application_order, course,
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

        # Risk Level
        st.subheader("Assessment Result:")

        assessment_label = result["risk_label"]
        recommendation = result["recommendation"]

        st.write(f"**Assessment Label:** {assessment_label}")
        st.write(f"**Rekomendasi:** {recommendation}")

    except Exception as e:
        st.error(f"Terjadi kesalahan sistem: {e}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    st.caption(f"Waktu inferensi: {elapsed_time:.2f} detik")