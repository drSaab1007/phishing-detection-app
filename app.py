import streamlit as st
import joblib
import pandas as pd

# Load model and columns
model = joblib.load("model.pkl")
columns = joblib.load("columns.joblib")

st.title("🔎 Phishing Detection App")

# User input
user_input = []
for col in columns:
    val = st.number_input(f"Enter {col}:", value=0.0)
    user_input.append(val)

# Prediction
if st.button("Predict"):
    df = pd.DataFrame([user_input], columns=columns)
    prediction = model.predict(df)[0]
    if prediction == 1:
        st.error("⚠️ This looks like a Phishing website!")
    else:
        st.success("✅ This looks Safe.")
