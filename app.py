import streamlit as st
import pandas as pd
import time
from joblib import load

st.set_page_config(
    page_title="Dropout Risk Assessment App",
    layout="centered",
)

THRESHOLD_POTABILITY = 0.69

# Load Artifacts
def load_artifacts():
    try:
        preprocess = load("artifacts/preprocessing_pipeline.pkl")
        clf_model  = load("artifacts/rf_classifier_model.pkl")
        anom_model = load("artifacts/anomaly_detection_model.pkl")
        return preprocess, clf_model, anom_model
    except Exception as e:
        st.error(f"Gagal memuat model: {e}")
        return None, None, None

PREPROCESSOR, CLF_MODEL, ANOM_MODEL = load_artifacts()

def run_inferece(data_input: pd.DataFrame) -> dict:
    # preprocessing
    X = PREPROCESSOR.transform(data_input)

    # classification
    potability_probs = CLF_MODEL.predict_proba(X)[0, 1]
    potability_pred = int(potability_probs >= THRESHOLD_POTABILITY)

# Streamlit UI
st.title("Aplikasi Risk Assessment Monitoring Kelayakan Air 💧")
st.markdown("Masukkan data setiap parameter kualitas air untuk melakukan Risk Assessment Kelayakan Air**!")

# Cek status model
if CLF_MODEL is not None and ANOM_MODEL is not None:
    st.caption(f"Status: Model sudah siap.")
else:
    st.error("MODEL GAGAL DIMUAT. Periksa folder artifacts.")
    st.stop()

# Input Form
st.subheader("Input Data Parameter Kualitas Air")

columns = [
        "ph", "Hardness", "Solids", 
        "Chloramines", "Sulfate", "Conductivity", 
        "Organic_carbon", "Trihalomethanes", "Turbidity"
]

## Input data numerik
marital_status = st.number_input("ph", min_value=0.1, max_value=14.0, value=7.0)
application_mode = st.number_input("Hardness", min_value=0.1, max_value=1000.0, value=200.0)
application_order = st.number_input("Solids", min_value=0.1, max_value=100000.0, value=20000.0)
course = st.number_input("Chloramines", min_value=0.1, max_value=100.0, value=7.0)
attendance = st.number_input("Sulfate", min_value=0.1, max_value=1000.0, value=300.0)
prev_qual = st.number_input("Conductivity", min_value=0.1, max_value=1000.0, value=400.0)
prev_qual_grade = st.number_input("Organic_carbon", min_value=0.1, max_value=1000.0, value=15.0)
nationality = st.number_input("Trihalomethanes", min_value=0.1, max_value=1000.0, value=80.0)
mothers_qual = st.number_input("Turbidity", min_value=0.1, max_value=100.0, value=4.0)
fathers_qual = st.number_input("ph", min_value=0.1, max_value=14.0, value=7.0)
mothers_occu = st.number_input("Hardness", min_value=0.1, max_value=1000.0, value=200.0)
fathers_occu = st.number_input("Solids", min_value=0.1, max_value=100000.0, value=20000.0)
admission_grade = st.number_input("Chloramines", min_value=0.1, max_value=100.0, value=7.0)
displaced = st.number_input("Sulfate", min_value=0.1, max_value=1000.0, value=300.0)
edu_special_needs = st.number_input("Conductivity", min_value=0.1, max_value=1000.0, value=400.0)
debtor = st.number_input("Organic_carbon", min_value=0.1, max_value=1000.0, value=15.0)
tuition_uptodate = st.number_input("Trihalomethanes", min_value=0.1, max_value=1000.0, value=80.0)
gender = st.number_input("Turbidity", min_value=0.1, max_value=100.0, value=4.0)
scholarship_holder = st.number_input("Hardness", min_value=0.1, max_value=1000.0, value=200.0)
age_at_enroll = st.number_input("Solids", min_value=0.1, max_value=100000.0, value=20000.0)
international = st.number_input("Chloramines", min_value=0.1, max_value=100.0, value=7.0)

curr_units_1_credited = st.number_input("Sulfate", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_1_enrolled = st.number_input("Sulfate", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_1_eval = st.number_input("Sulfate", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_1_approved = st.number_input("Sulfate", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_1_grade = st.number_input("Sulfate", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_1_without_eval = st.number_input("Sulfate", min_value=0.1, max_value=1000.0, value=300.0)

curr_units_2_credited = st.number_input("Sulfate", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_2_enrolled = st.number_input("Sulfate", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_2_eval = st.number_input("Sulfate", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_2_approved = st.number_input("Sulfate", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_2_grade = st.number_input("Sulfate", min_value=0.1, max_value=1000.0, value=300.0)
curr_units_2_without_eval = st.number_input("Sulfate", min_value=0.1, max_value=1000.0, value=300.0)

unemployement_rate = st.number_input("Conductivity", min_value=0.1, max_value=1000.0, value=400.0)
inflation_rate = st.number_input("Organic_carbon", min_value=0.1, max_value=1000.0, value=15.0)
gdp = st.number_input("Trihalomethanes", min_value=0.1, max_value=1000.0, value=80.0)

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
        st.subheader("Risk Level dan Rekomendasi:")

        risk_label = result["risk_label"]
        recommendation = result["recommendation"]

        st.write(f"**Risk Label:** {risk_label}")
        st.write(f"**Rekomendasi:** {recommendation}")

    except Exception as e:
        st.error(f"Terjadi kesalahan sistem: {e}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    st.caption(f"Waktu inferensi: {elapsed_time:.2f} detik")