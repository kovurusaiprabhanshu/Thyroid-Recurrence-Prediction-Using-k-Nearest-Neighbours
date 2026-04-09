import streamlit as st
import pandas as pd
from predict import predict

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="Thyroid Predictor", layout="centered")

st.title("🧠 Thyroid Risk & Recurrence Predictor")
st.markdown("Enter patient clinical details below:")

# -------------------------
# INPUT SECTION
# -------------------------
with st.form("patient_form"):

    age = st.slider("Age", 10, 100, 45)

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["M", "F"])
        smoking = st.selectbox("Smoking", ["Yes", "No"])
        hx_smoking = st.selectbox("Hx Smoking", ["Yes", "No"])
        hx_radio = st.selectbox("Hx Radiotherapy", ["Yes", "No"])
        thyroid_func = st.selectbox("Thyroid Function", ["Euthyroid", "Hypothyroid", "Hyperthyroid"])

    with col2:
        physical_exam = st.selectbox("Physical Examination", ["Normal", "Abnormal"])
        adenopathy = st.selectbox("Adenopathy", ["No", "Yes"])
        pathology = st.selectbox("Pathology", ["Papillary", "Follicular", "Other"])
        focality = st.selectbox("Focality", ["Uni-Focal", "Multi-Focal"])

    col3, col4 = st.columns(2)

    with col3:
        t_stage = st.selectbox("T Stage", ["T1", "T2", "T3", "T4"])
        n_stage = st.selectbox("N Stage", ["N0", "N1"])

    with col4:
        m_stage = st.selectbox("M Stage", ["M0", "M1"])
        stage = st.selectbox("Overall Stage", ["Stage I", "Stage II", "Stage III", "Stage IV"])

    submit = st.form_submit_button("🔍 Predict")

# -------------------------
# PREDICTION
# -------------------------
if submit:
    try:
        input_df = pd.DataFrame({
            'Age': [age],
            'Gender': [gender],
            'Smoking': [smoking],
            'Hx Smoking': [hx_smoking],
            'Hx Radiothreapy': [hx_radio],
            'Thyroid Function': [thyroid_func],
            'Physical Examination': [physical_exam],
            'Adenopathy': [adenopathy],
            'Pathology': [pathology],
            'Focality': [focality],
            'T': [t_stage],
            'N': [n_stage],
            'M': [m_stage],
            'Stage': [stage]
        })

        result = predict(input_df)

        # -------------------------
        # DISPLAY RESULTS
        # -------------------------
        st.subheader("📊 Prediction Results")

        risk = result["Risk_Level"].values[0]
        recurrence = result["Recurrence_Prediction"].values[0]
        prob = result["Recurrence_Probability"].values[0]

        # Risk display
        if risk == "High Risk":
            st.error(f"⚠️ Risk Level: {risk}")
        elif risk == "Medium Risk":
            st.warning(f"⚠️ Risk Level: {risk}")
        else:
            st.success(f"✅ Risk Level: {risk}")

        # Recurrence
        st.write(f"### Recurrence Prediction: {recurrence}")

        # Probability bar
        st.write(f"### Probability: {prob}")
        st.progress(int(prob * 100))

    except Exception as e:
        st.error(f"Error: {e}")
