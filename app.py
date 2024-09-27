import streamlit as st
import joblib
import numpy as np

# Load the pre-trained model and scaler
with open('best_model_random_forest.pkl', 'rb') as model_file:
    model = joblib.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = joblib.load(scaler_file)

# Define the Streamlit app
st.title('Credit Score Classification App')

# Collect input data from the user
st.write("Enter the following details to check if your credit score is above or below 650:")

# Input fields based on the provided features
age = st.number_input('Age', min_value=18, max_value=100, step=1)
income = st.number_input('Annual Income ($)', min_value=1000, step=500)
emp_years = st.number_input('Years of Employment', min_value=0, step=1)
grade = st.selectbox('Grade', options=[0, 1])  # Assuming this is binary (encoded)
loan_amount = st.number_input('Loan Amount ($)', min_value=500, step=100)
interest_rate = st.number_input('Interest Rate (%)', min_value=0.0, step=0.1)
percent_income = st.number_input('Percent of Income (%)', min_value=0.0, step=0.01)
credit_history = st.number_input('Credit History (Years)', min_value=0, step=1)
home_ownership = st.selectbox('Home Ownership', options=['OTHER', 'OWN', 'RENT'])
loan_purpose = st.selectbox('Loan Purpose', options=['EDUCATION', 'HOMEIMPROVEMENT', 'MEDICAL', 'PERSONAL', 'VENTURE'])
default_history = st.selectbox('Default History', options=['N', 'Y'])

# Calculate ratios based on input
age_income_ratio = age / income if income > 0 else 0
loan_income_ratio = loan_amount / income if income > 0 else 0

# Convert categorical fields to binary flags (one-hot encoding)
home_ownership_OTHER = 1 if home_ownership == 'OTHER' else 0
home_ownership_OWN = 1 if home_ownership == 'OWN' else 0
home_ownership_RENT = 1 if home_ownership == 'RENT' else 0

loan_purpose_EDUCATION = 1 if loan_purpose == 'EDUCATION' else 0
loan_purpose_HOMEIMPROVEMENT = 1 if loan_purpose == 'HOMEIMPROVEMENT' else 0
loan_purpose_MEDICAL = 1 if loan_purpose == 'MEDICAL' else 0
loan_purpose_PERSONAL = 1 if loan_purpose == 'PERSONAL' else 0
loan_purpose_VENTURE = 1 if loan_purpose == 'VENTURE' else 0

default_history_Y = 1 if default_history == 'Y' else 0

# Prepare input features for prediction
input_features = np.array([[age, income, emp_years, grade, loan_amount, interest_rate,
                            percent_income, credit_history, home_ownership_OTHER,
                            home_ownership_OWN, home_ownership_RENT, loan_purpose_EDUCATION,
                            loan_purpose_HOMEIMPROVEMENT, loan_purpose_MEDICAL,
                            loan_purpose_PERSONAL, loan_purpose_VENTURE,
                            default_history_Y, age_income_ratio, loan_income_ratio]])

# Scale the input features
input_features_scaled = scaler.transform(input_features)

# Make the prediction
if st.button('Predict'):
    prediction = model.predict(input_features_scaled)

    # Display result
    if prediction == 0:
        st.success('Credit Score above 650: Eligible for Loan or No Default Found.')
    else:
        st.error('Credit Score below 650: Not Eligible for Loan or Default Found.')
