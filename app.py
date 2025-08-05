import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('model.pkl')

# Streamlit UI
st.title("Mood Swing Level Prediction")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
country = st.text_input("Country", "India")
occupation = st.text_input("Occupation", "Engineer")
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
family_history = st.selectbox("Family History", ["Yes", "No"])
past_treatment = st.selectbox("Past Treatment", ["Yes", "No"])
days_indoors = st.number_input("Days Indoors", min_value=0, max_value=300, value=10)
growing_stress = st.selectbox("Growing Stress", ["Yes", "No", "Maybe"])
changes_habits = st.selectbox("Changes in Habits", ["Yes", "No", "Maybe"])
mental_health_history = st.selectbox("Mental Health History", ["Yes", "No", "Maybe"])
coping_struggles = st.selectbox("Coping Struggles", ["Yes", "No"])
work_interest = st.selectbox("Work Interest", ["Yes", "No", "Maybe"])
social_weakness = st.selectbox("Social Weakness", ["Yes", "No", "Maybe"])
mental_health_interview = st.selectbox("Mental Health Consultation Before", ["Yes", "No", "Maybe"])
care_options = st.selectbox("Care Options", ["Yes", "No", "Not sure"])

# Prediction
if st.button("Predict Mood Swing Level"):
    input_data = pd.DataFrame([{
        "Gender": gender,
        "Country": country,
        "Occupation": occupation,
        "self_employed": self_employed,
        "family_history": family_history,
        "past_treatment": past_treatment,
        "Days_Indoors": days_indoors,
        "Growing_Stress": growing_stress,
        "Changes_Habits": changes_habits,
        "Mental_Health_History": mental_health_history,
        "Coping_Struggles": coping_struggles,
        "Work_Interest": work_interest,
        "Social_Weakness": social_weakness,
        "mental_health_interview": mental_health_interview,
        "care_options": care_options
    }])

    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Mood Swing Level: {prediction}")
