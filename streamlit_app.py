import streamlit as st
import requests

# Flask API URL
API_URL = "http://127.0.0.1:5000/predict"

# Feature column names
feature_columns = [
    'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
    'smoothness_mean', 'compactness_mean', 'concavity_mean',
    'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
    'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
    'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
    'fractal_dimension_se', 'radius_worst', 'texture_worst',
    'perimeter_worst', 'area_worst', 'smoothness_worst',
    'compactness_worst', 'concavity_worst', 'concave points_worst',
    'symmetry_worst', 'fractal_dimension_worst'
]

st.title("Breast Cancer Prediction")
st.write("Enter the values for the 30 features to predict the result.")

# Create input fields for all 30 features
user_input = []
for col in feature_columns:
    value = st.number_input(f"{col}", value=0.0, format="%.6f")
    user_input.append(value)

# Button to predict
if st.button("Predict"):
    data = {"features": user_input}
    response = requests.post(API_URL, json=data)

    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"Prediction: {prediction}")
    else:
        st.error(f"Error: {response.json().get('error', 'Unknown error')}")
