import streamlit as st
import datetime
import joblib
import pandas as pd
import os

st.set_page_config(
    page_title="CardioGuard 🩺",
    layout="wide",

)

@st.cache_resource
def load_assets():
    current_dir=os.path.dirname((os.path.abspath(__file__)))
    model_path=os.path.join(current_dir,'..','model','lgbm_model.pkl')
    scaler_path=os.path.join(current_dir,'..','model','standard_scaler.pkl')
    model=joblib.load(model_path)
    scaler=joblib.load(scaler_path)
    return model, scaler

lgbm_model, standard_scaler=load_assets()

st.title(
    "CardioGuard 💗",
    width='stretch',
    text_alignment='center',
    wrap=False
)

st.subheader(
    "Machine Learning Web Application for Cardiovascular Disease Prediction",
    text_alignment='center'
)

outer_left, center_container, outer_right = st.columns([1,2,1])

with center_container:
    with st.container(border=True):
        column1, spacer, column2 = st.columns([10,2,10], gap="xxlarge", vertical_alignment='center')
        with column1:
            min_date=datetime.date.today()-datetime.timedelta(days=365*150)
            date_of_birth=st.date_input("Date of Birth", min_value=min_date, max_value=datetime.date.today(), format="DD/MM/YYYY")
            height=st.number_input("Height",min_value=100.0, max_value=250.0, value=170.0, step=0.5)
            systolic_blood_pressure=st.number_input("Systolic Blood Pressure", min_value=70, max_value=250, value=120, step=1)
            cholesterol=st.selectbox(
                "Cholesterol",
                options=['Normal','Above normal','Well above normal'],
                filter_mode=None
            )
            smoking_status=st.radio(
                "Smoking Status",
                options=['Non-smoker', 'Smoker'],
                horizontal=True
            )
            active=st.radio(
                "Physically Active",
                options=['Not physically active', 'Physically active'],
                horizontal=True
            )
        with column2:
            gender=st.radio(
                "Gender",
                options=["Male","Female"],
                horizontal=True
            )
            weight=st.number_input("Weight", min_value=30.0, max_value=300.0, value=60.0, step=0.5)
            diastolic_blood_pressure=st.number_input("Diastolic Blood Pressure", min_value=40, max_value=150, value=80, step=1)
            glucose=st.selectbox(
                "Glucose",
                options=['Normal','Above normal','Well above normal'],
                filter_mode=None
            )
            alcohol=st.radio(
                "Alcohol",
                options=['Does not consume alcohol', 'Consumes alcohol']
            )
            bp_category=st.selectbox(
                "BP Category",
                options=['Normal', 'Elevated', 'Hypertension Stage 1', 'Hypertension Stage 2', 'Hypertensive Crisis']
            )
        button_left, button_container, button_right=st.columns([1,2,1])
        with button_container:
            if st.button("Predict cardiovascular disease", type="secondary", width="stretch", shortcut="Enter"):
                age_years=datetime.date.today().year - date_of_birth.year
                gender_map={"Female":1, "Male":2}
                gender_value=gender_map[gender]
                height_value=height
                weight_value=weight
                ap_hi_value=systolic_blood_pressure
                ap_lo_value=diastolic_blood_pressure
                cholesterol_map={"Normal":1, "Above normal":2, "Well above normal":3}
                cholesterol_value=cholesterol_map[cholesterol]
                glucose_map={"Normal":1, "Above normal":2, "Well above normal":3}
                glucose_value=glucose_map[glucose]
                smoke_map={"Non-smoker":0, "Smoker":1}
                smoke_value=smoke_map[smoking_status]
                alcohol_map={"Does not consume alcohol":0, "Consumes alcohol":1}
                alcohol_value=alcohol_map[alcohol]
                active_map={"Not physically active":0, "Physically active":1}
                active_value=active_map[active]
                bp_category_map={"Normal":0.0, "Elevated":1.0, "Hypertension Stage 1":2.0, "Hypertension Stage 2":3.0, "Hypertensive Crisis":4.0}
                bp_category_value=bp_category_map[bp_category]
                height_m=height_value/100
                bmi_value=weight_value/(height_m**2)
                input=pd.DataFrame({
                    "gender":[gender_value],
                    "height":[height_value],
                    "weight":[weight_value],
                    "ap_hi":[ap_hi_value],
                    "ap_lo":[ap_lo_value],
                    "cholesterol":[cholesterol_value],
                    "gluc":[glucose_value],
                    "smoke":[smoke_value],
                    "alco":[alcohol_value],
                    "active":[active_value],
                    "age_years":[age_years],
                    "bmi":[bmi_value],
                    "bp_category":[bp_category_value]
                })
                input_scaled=standard_scaler.transform(input)
                prediction=lgbm_model.predict(input_scaled)[0]
                prediction_probability=lgbm_model.predict_proba(input_scaled)[0]
                if prediction==1:
                    st.error("**Prediction:** High risk of cardiovascular disease.")
                    st.error(f"**Confidence:** {prediction_probability[1]*100:.2f}%")
                else:
                    st.success(f"**Prediction:** Low risk of cardiovascular disease.")
                    st.success(f"**Confidence:** {prediction_probability[0] * 100:.2f}%")
    st.warning(
        "⚠️ **Medical Disclaimer** CardioGuard is powered by machine learning "
        "for informational and educational purposes only. It does not provide "
        "formal medical diagnoses. **Always consult a qualified healthcare provider** "
        "for any medical advice, diagnosis or treatment."
    )