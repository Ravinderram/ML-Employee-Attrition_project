import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Employee Attrition Prediction",
    layout="centered"
)

st.title("Employee Attrition Prediction App")
st.write("Adjust employee details and predict attrition risk.")

# -----------------------
# Model selection
# -----------------------
model_name = st.selectbox(
    "Select Model",
    ["Random Forest", "Logistic Regression"]
)

# -----------------------
# User Inputs
# -----------------------
st.subheader("Employee Information")

age = st.slider("Age", 18, 60, 30)
monthly_income = st.number_input("Monthly Income", min_value=1000, max_value=50000, value=5000)
years_at_company = st.slider("Years at Company", 0, 40, 5)
job_satisfaction = st.slider("Job Satisfaction (1–4)", 1, 4, 3)
work_life_balance = st.slider("Work Life Balance (1–4)", 1, 4, 3)

overtime = st.selectbox("OverTime", ["Yes", "No"])
job_role = st.selectbox(
    "Job Role",
    [
        "Sales Executive",
        "Research Scientist",
        "Laboratory Technician",
        "Manufacturing Director",
        "Healthcare Representative",
        "Manager",
        "Sales Representative",
        "Research Director",
        "Human Resources"
    ]
)

# -----------------------
# Create input dictionary
# -----------------------
input_data = {
    "Age": age,
    "MonthlyIncome": monthly_income,
    "YearsAtCompany": years_at_company,
    "JobSatisfaction": job_satisfaction,
    "WorkLifeBalance": work_life_balance,
    "OverTime": overtime,
    "JobRole": job_role
}

# -----------------------
# Prediction
# -----------------------
if st.button("Predict Attrition"):
    prediction, probability = predict_attrition(input_data, model_name)

    if prediction == 1:
        st.error(f"⚠️ High Risk of Attrition (Probability: {probability:.2%})")
    else:
        st.success(f"✅ Low Risk of Attrition (Probability: {probability:.2%})")

