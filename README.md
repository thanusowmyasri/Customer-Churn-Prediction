# Customer Churn Prediction

# Project Overview
Customer Churn Prediction is a machine learning project that predicts whether a telecom customer is likely to leave a service.
The project uses customer information, service subscriptions, contract details and billing information to estimate churn probability.
An interactive Streamlit application allows users to enter customer details and receive a prediction.

# Objectives
- Identify customers who may be likely to leave a telecom service.
- Explore customer behaviour using historical data.
- Build and evaluate machine learning classification models.
- Display predictions through an interactive web application.

# Dataset
*IBM Telco Customer Churn Dataset*

The dataset contains customer demographics, subscribed services, contract information, payment methods, charges and churn status.
After handling missing values, 7,032 customer records were used for modelling.

# Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

# Machine Learning Workflow
1. Load and explore the dataset.
2. Handle missing values and remove the customer ID.
3. Convert categorical variables into numerical features using one-hot encoding.
4. Split the data into training and testing sets.
5. Standardize numerical features.
6. Train and evaluate classification models.
7. Save the trained model and scaler.
8. Integrate the model into a Streamlit application.

# Model Performance

The selected model is *Logistic Regression*.
| Metric          | Result |
| Accuracy        : 78.68% |
| Churn Precision : 62%    |
| Churn Recall    : 51%    |
| Churn F1-score  : 56%    |
The model provides a churn probability for each customer based on the supplied information.

# Application Features
- Interactive customer information form.
- Customer, service and billing information sections.
- Two-column input layout.
- Churn prediction.
- Churn probability display.

# Project Structure

Customer-Churn-Prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── models/
│   ├── logistic_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   └── 01_Data_Understanding.ipynb
│
├── src/
├── requirements.txt
└── README.md

# How to Run the Project

1. Clone or download the project.
2. Open the project folder in a terminal.
3. Create and activate a virtual environment:

python -m venv churn_env

For Windows PowerShell:

.\churn_env\Scripts\Activate.ps1

4. Install the required packages:

pip install -r requirements.txt


5. Start the Streamlit application from the project root:

streamlit run app/app.py


6. Open the local URL displayed in the terminal.

# Business Use Case
Businesses can use churn predictions to identify customers who may need additional attention. This can help them investigate customer concerns, improve services and plan customer-retention activities.

# Limitations
The model is a prototype trained on a historical telecom dataset. Its predictions are estimates, not guarantees. Further evaluation, feature improvements and testing on additional data would be needed before real-world deployment.

# Project Status
Machine learning model trained and evaluated. Interactive Streamlit prototype implemented and tested.
