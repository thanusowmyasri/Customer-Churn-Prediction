import streamlit as st
import pandas as pd
import joblib

# -------------------------------
# Load Model & Scaler
# -------------------------------
model = joblib.load("models/logistic_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# -------------------------------
# Feature Columns
# -------------------------------
feature_columns = [
    'SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges',
    'gender_Male', 'Partner_Yes', 'Dependents_Yes', 'PhoneService_Yes',
    'MultipleLines_No phone service', 'MultipleLines_Yes',
    'InternetService_Fiber optic', 'InternetService_No',
    'OnlineSecurity_No internet service', 'OnlineSecurity_Yes',
    'OnlineBackup_No internet service', 'OnlineBackup_Yes',
    'DeviceProtection_No internet service', 'DeviceProtection_Yes',
    'TechSupport_No internet service', 'TechSupport_Yes',
    'StreamingTV_No internet service', 'StreamingTV_Yes',
    'StreamingMovies_No internet service', 'StreamingMovies_Yes',
    'Contract_One year', 'Contract_Two year',
    'PaperlessBilling_Yes',
    'PaymentMethod_Credit card (automatic)',
    'PaymentMethod_Electronic check',
    'PaymentMethod_Mailed check'
]

numerical_cols = ["tenure", "MonthlyCharges", "TotalCharges"]

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Customer Churn Prediction")

st.write(
    "Enter customer details to predict whether the customer "
    "is likely to leave the service."
)


# -------------------------------
# Customer Information
# -------------------------------
st.subheader("👤 Customer Information")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])
    tenure = st.slider("Tenure (Months)", 0, 72, 12)

with col2:
    phone = st.selectbox("Phone Service", ["No", "Yes"])
    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )
    internet = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

# -------------------------------
# Service Information
# -------------------------------
st.subheader("📡 Service Information")

col1, col2 = st.columns(2)

with col1:
    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )
    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )
    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

with col2:
    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )
    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )
    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

# -------------------------------
# Billing Information
# -------------------------------
st.subheader("💳 Billing Information")

col1, col2 = st.columns(2)

with col1:
    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )
    paperless = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )

with col2:
    payment = st.selectbox(
        "Payment Method",
        [
            "Bank transfer (automatic)",
            "Credit card (automatic)",
            "Electronic check",
            "Mailed check"
        ]
    )
    monthly = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=120.0,
        value=70.0
    )

total = st.number_input(
    "Total Charges",
    min_value=0.0,
    max_value=10000.0,
    value=1000.0
)


# -------------------------------
# Prediction
# -------------------------------
if st.button("🔍 Predict Churn", use_container_width=True):

    input_data = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "PhoneService": phone,
        "MultipleLines": multiple_lines,
        "InternetService": internet,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "tenure": tenure,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    input_df = pd.DataFrame([input_data])

    # Convert categorical data into numerical features
    input_encoded = pd.get_dummies(input_df, dtype=int)

    # Match the exact training feature columns
    input_encoded = input_encoded.reindex(
        columns=feature_columns,
        fill_value=0
    )

    
    # Scale numerical features
    input_encoded[numerical_cols] = scaler.transform(
        input_encoded[numerical_cols]
    )

    # Make prediction
    prediction = model.predict(input_encoded)[0]
    probability = model.predict_proba(input_encoded)[0][1]

    # Display result
    st.subheader("📊 Prediction Result")

    if prediction == 1:
        st.error("⚠️ Customer is likely to Churn!")
    else:
        st.success("✅ Customer is likely to Stay!")

    st.metric(
        "Churn Probability",
        f"{probability * 100:.2f}%"
    )

    st.progress(float(probability))
