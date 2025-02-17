import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="Credit Scoring Model", page_icon="💳", layout="centered")

st.title("💳 Credit Scoring Model")
st.write("This application predicts your credit score based on financial details.")

try:
    with open('credit_scoring_model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found. Please upload the trained model.")
    st.stop()

annual_income = st.number_input("Enter your annual income ($):", min_value=0, step=1)
outstanding_debt = st.number_input("Enter your outstanding debt ($):", min_value=0, step=1)
total_emi = st.number_input("Enter your total EMI per month ($):", min_value=0, step=1)

if st.button("🔍 Predict Score"):
    input_data = np.array([[annual_income, outstanding_debt, total_emi]])
    try:
        prediction = model.predict(input_data)[0]
        prediction = int(prediction)
        if prediction == 1:
            response = "GOOD"
        elif prediction == 0:
            response = "POOR"
        else:
            response = "STANDARD" 
        st.success(f"📊 Predicted Credit Score: **{response}**")
    except Exception as e:
        st.error(f"An error occurred while predicting: {e}")