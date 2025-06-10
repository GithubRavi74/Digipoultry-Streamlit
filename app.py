import streamlit as st
import numpy as np
import pickle


# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# App UI
from PIL import Image
image = Image.open("logo.png")

st.set_page_config(page_title="🐔 Chicken Weight Predictor", layout="centered")
st.title("🐔 Chicken Weight Predictor")
st.markdown("Enter chicken height in cm to predict its weight (kg).")

# Input
height = st.number_input("Enter chicken height (cm):", min_value=0.0, step=0.1)

# Prediction
if st.button("Predict Weight"):
    input_data = np.array([[height]])
    prediction = model.predict(input_data)
    weight = round(prediction[0][0], 2)
    st.success(f"Predicted Weight: {weight} kg")
