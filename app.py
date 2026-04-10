import streamlit as st
import pandas as pd
import numpy as np
import time
from joblib import load

st.set_page_config(
    page_title="Dropout Risk Assessment App",
    layout="centered",
)

THRESHOLD = 0.5

# Load Artifacts
@st.cache_resource
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

def run_inference(data_input: pd.DataFrame) -> dict:
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
    df['Application preference'] = (
        9 - df['Application order'] + 1
    ).astype(int)
    df.drop(columns=['Application order'], inplace=True)

    # classification pipeline
    probs = MODEL.predict_proba(df)[0]
    dropout_idx = list(LABEL_ENCODER.classes_).index("Dropout")
    dropout_prob = probs[dropout_idx]

    return {"probability": dropout_prob}


# Streamlit UI
st.title("Dropout Risk Assessment App")

# Cek status model
if MODEL is None:
    st.error("MODEL GAGAL DIMUAT. Periksa folder artifacts.")
    st.stop()
else:
    st.caption("Status: Model sudah siap.")

# Input Form
with st.form(key="form_assesment"):
    st.markdown("Input Data Mahasiswa!")

    ## Input Personal Information
    st.markdown("### Personal Information")

    ### 0. Student ID
    student_id = st.text_input(
        "Student ID", 
        placeholder="Type Student ID"
    )

    col_marital, col_age, col_nation = st.columns([2, 1.5, 3])

    ### 1. Marital status
    marital_status = col_marital.selectbox(
        "Marital status",
        placeholder="Type to search...",
        options=[
            "Single", "Married", "Widowed", "Divorced", "Facto Union", "Legally Separated", "Other"
        ]
    )

    ### 2. Age at enrollment
    age_at_enroll = col_age.number_input(
        "Age at enrollment", 
        min_value=18, 
        max_value=100, 
        value=20
    )

    col_gen, col_inter = st.columns(2)

    ### 3. Gender
    gender = col_gen.radio(
        "Gender",
        options=[
            "Male", "Female"
        ],
        horizontal=True
    )

    ### 4. International
    international = col_inter.radio(
        "International",
        options=[
            "Yes", "No"
        ],
        horizontal=True
    )

    ### 5. Nationality
    nationality = col_nation.selectbox(
        "Nationality",
        placeholder="Type to search...",
        options=[
            "Portuguese", "German", "Spanish", "Italian", "Dutch", "English",
            "Lithuanian", "Angolan", "Cape Verdean", "Guinean", "Mozambican",
            "Santomean", "Turkish", "Brazilian", "Romanian", "Moldova (Republic of)",
            "Mexican", "Ukrainian", "Russian", "Cuban", "Colombian", "Other"
        ], 
        accept_new_options=True
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

    col_mother_qual, col_mother_occu = st.columns(2)

    ### 6. Mother's Information
    mothers_qual = col_mother_qual.selectbox(
        "Mother's qualification",
        placeholder="Type to search...",
        options=qual_options,
        accept_new_options=True
    )

    mothers_occu = col_mother_occu.selectbox(
        "Mother's occupation",
        placeholder="Type to search...",
        options=occu_options,
        accept_new_options=True
    )

    col_father_qual, col_father_occu = st.columns(2)

    ### 7. Father's Information
    fathers_qual = col_father_qual.selectbox(
        "Father's qualification",
        placeholder="Type to search...",
        options=qual_options,
        accept_new_options=True
    )

    fathers_occu = col_father_occu.selectbox(
        "Father's occupation",
        placeholder="Type to search...",
        options=occu_options,
        accept_new_options=True
    )

    col_displaced, col_needs = st.columns(2)

    ### 8. Displaced
    displaced = col_displaced.radio(
        "Displaced",
        options=[
            "Yes", "No"
        ],
        horizontal=True
    )

    ### 9. Educational Special needs
    edu_special_needs = col_needs.radio(
        "Educational special needs",
        options=[
            "Yes", "No"
        ],
        horizontal=True
    )

    st.divider()

    ## Input Academic Information
    st.markdown("### Academic Information")

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

    col_mode, col_order, col_admission = st.columns([3, 1, 1])

    ### 3. Application mode
    application_mode = col_mode.selectbox(
        "Application mode",
        placeholder="Type to search...",
        options=mode_options,
        accept_new_options=True
    )

    ### 4. Application order
    application_order = col_order.number_input(
        "Application order",
        min_value=1,
        max_value=9,
        value=1
    )

    ### 5. Admission grade
    admission_grade = col_admission.number_input(
        "Admission grade",
        min_value=0.00,
        max_value=200.00,
        value=100.00
    )

    col_qual, col_qual_grade = st.columns(2)

    ### 6. Previous qualification
    prev_qual = col_qual.selectbox(
        "Previous qualification",
        placeholder="Type to search...",
        options=qual_options,
        accept_new_options=True
    )

    ### 7. Previous qualification grade
    prev_qual_grade = col_qual_grade.number_input(
        "Previous qualification (grade)", 
        min_value=0.00, 
        max_value=200.00, 
        value=100.00
    )

    st.markdown("##### Curricular Units 1st Sem ---")
    ### 8. Sem 1 Information
    col_credit_sem1, col_enrolled_sem1, col_eval_sem1 = st.columns(3)
    curr_units_1_credited = col_credit_sem1.number_input("Credited 1st Sem", min_value=0, max_value=100, value=1)
    curr_units_1_enrolled = col_enrolled_sem1.number_input("Enrolled 1st Sem", min_value=0, max_value=100, value=1)
    curr_units_1_eval = col_eval_sem1.number_input("Evaluations 1st Sem", min_value=0, max_value=100, value=1)

    col_approved_sem1, col_grade_sem1, col_weval_sem1 = st.columns(3)
    curr_units_1_approved = col_approved_sem1.number_input("Approved 1st Sem", min_value=0, max_value=100, value=1)
    curr_units_1_grade = col_grade_sem1.number_input("Grade 1st Sem", min_value=0, max_value=20, value=10)
    curr_units_1_without_eval = col_weval_sem1.number_input("Without Evaluations 1st Sem", min_value=0, max_value=100, value=1)

    st.markdown("##### Curricular Units 2nd Sem ---")
    ### 9. Sem 2 Information
    col_credit_sem2, col_enrolled_sem2, col_eval_sem2 = st.columns(3)
    curr_units_2_credited = col_credit_sem2.number_input("Credited 2nd Sem", min_value=0, max_value=100, value=1)
    curr_units_2_enrolled = col_enrolled_sem2.number_input("Enrolled 2nd Sem", min_value=0, max_value=100, value=1)
    curr_units_2_eval = col_eval_sem2.number_input("Evaluations 2nd Sem", min_value=0, max_value=100, value=1)

    col_approved_sem2, col_grade_sem2, col_weval_sem2 = st.columns(3)
    curr_units_2_approved = col_approved_sem2.number_input("Approved 2nd Sem", min_value=0, max_value=100, value=1)
    curr_units_2_grade = col_grade_sem2.number_input("Grade 2nd Sem", min_value=0, max_value=20, value=10)
    curr_units_2_without_eval = col_weval_sem2.number_input("Without Evaluations 2nd Sem", min_value=0, max_value=100, value=1)

    st.divider()

    ## Input Economic Information
    st.markdown("### Economic & Financial Information")

    col_ur, col_ir, col_gdp = st.columns(3)

    ### Macro Economic Indicators
    unemployment_rate = col_ur.number_input("Unemployment rate", min_value=0.0, max_value=100.0, value=0.0)
    inflation_rate = col_ir.number_input("Inflation rate", min_value=0.0, max_value=100.0, value=1.0)
    gdp = col_gdp.number_input("GDP", min_value=0.0, max_value=1_000_000.0, value=10_000.0)

    col_debtor, col_tuition, col_scholarship = st.columns(3)
    ### Financial Information
    debtor = col_debtor.radio(
        "Debtor",
        options=[
            "Yes", "No"
        ],
        horizontal=True
    )

    tuition_uptodate = col_tuition.radio(
        "Tuition fees up to date",
        options=[
            "Yes", "No"
        ],
        horizontal=True
    )

    scholarship_holder = col_scholarship.radio(
        "Scholarship holder",
        options=[
            "Yes", "No"
        ],
        horizontal=True
    )

    st.divider()

    # Tombol submit
    submitted = st.form_submit_button(
        "Prediksi Risiko Dropout", 
        type="primary",
        use_container_width=True
    )

    if submitted:
        
        data_dict = {
            "Student ID": student_id,
            "Marital status": marital_status,
            "Age at enrollment": age_at_enroll,
            "Gender": gender,
            "International": international,
            "Nationality": nationality,
            "Mother's qualification": mothers_qual,
            "Mother's occupation": mothers_occu,
            "Father's qualification": fathers_qual,
            "Father's occupation": fathers_occu,
            "Displaced": displaced,
            "Educational special needs": edu_special_needs,
            "Course": course,
            "Attendance": attendance,
            "Application mode": application_mode,
            "Application order": application_order,
            "Admission grade": admission_grade,
            "Previous qualification": prev_qual,
            "Previous qualification (grade)": prev_qual_grade,
            "Curricular units 1st sem (credited)": curr_units_1_credited,
            "Curricular units 1st sem (enrolled)": curr_units_1_enrolled,
            "Curricular units 1st sem (evaluations)": curr_units_1_eval,
            "Curricular units 1st sem (approved)": curr_units_1_approved,
            "Curricular units 1st sem (grade)": curr_units_1_grade,
            "Curricular units 1st sem (without evaluations)": curr_units_1_without_eval,
            "Curricular units 2nd sem (credited)": curr_units_2_credited,
            "Curricular units 2nd sem (enrolled)": curr_units_2_enrolled,
            "Curricular units 2nd sem (evaluations)": curr_units_2_eval,
            "Curricular units 2nd sem (approved)": curr_units_2_approved,
            "Curricular units 2nd sem (grade)": curr_units_2_grade,
            "Curricular units 2nd sem (without evaluations)": curr_units_2_without_eval,
            "Unemployment rate": unemployment_rate,
            "Inflation rate": inflation_rate,
            "GDP": gdp,
            "Debtor": debtor,
            "Tuition fees up to date": tuition_uptodate,
            "Scholarship holder": scholarship_holder,
        }

        # Cek field kosong
        empty_fields = [key for key, value in data_dict.items() if value == "" or value is None]

        if empty_fields:
            st.error("### **Data masih kosong:**")
            for field in empty_fields:
                st.write(f"- {field}")
            st.stop()

        data_input = pd.DataFrame([data_dict])
        st.subheader("Data Input:")
        st.dataframe(data_input)

        # Mulai prediksi
        st.write("Memproses data...")
    
        try:
            result = run_inference(data_input)
            dropout_risk = result["probability"]
            pred_status = "Dropout" if dropout_risk >= THRESHOLD else "Not Dropout"
            data_input['Status Prediction'] = pred_status

            # Simpan ke session state agar persist saat rerun
            st.session_state['last_prediction'] = {
                "df": data_input,
                "dropout_risk": dropout_risk,
                "pred_status": pred_status,
                "time": time.time()
            }
        
        except Exception as e:
            st.error(f"Terjadi kesalahan saat memproses data: {e}")
            st.session_state.pop('last_prediction', None)
    if 'last_prediction' in st.session_state:
        pred = st.session_state['last_prediction']

        st.divider()

        ## Dropout Risk 
        st.subheader("Assessment Result:")

        if pred["dropout_risk"] >= THRESHOLD:
            st.error("### **Risiko Dropout Tinggi!**")
        else:
            st.success("### **Risiko Dropout Rendah!**")
        st.metric("Probabilitas", f"{pred['dropout_risk']:.2%}")

        elapsed_time = time.time() - pred["time"]
        st.caption(f"Waktu inferensi: {elapsed_time:.2f} detik")

        # Tombol Download
        csv_data = pred["df"].to_csv(index=False).encode("utf-8")
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        filename = f"prediksi_dropout_{timestamp}.csv"

        st.download_button(
            label="Simpan Hasil Prediksi",
            data=csv_data,
            file_name=filename,
            mime="text/csv",
            type="secondary"
            use_container_width=True
        )