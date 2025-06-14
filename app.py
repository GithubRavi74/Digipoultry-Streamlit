import streamlit as st
import numpy as np
import pickle


# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# App UI
st.set_page_config(page_title="Chicken Weight Predictor", layout="centered")
import streamlit as st

# Custom CSS for black background and white text
st.markdown("""
    <style>
    body {
        background-color: black;
        color: white;
    }
    .stApp {
        background-color: black;
        color: white;
    }
    .css-1cpxqw2 {  /* To override widget label text (Streamlit version-specific) */
        color: white !important;
    }
    .stNumberInput input {
        background-color: #222;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)



from PIL import Image
image = Image.open("logo.png")
st.image(image, width=200)
st.markdown("<br><br>", unsafe_allow_html=True)  # Line break
st.markdown(
    "<div style='font-size:15px;'>🐔 Enter chicken height in cm to predict its weight (kg).</div>",
    unsafe_allow_html=True
)

# Input
height = st.number_input( "",min_value=0.0, step=0.1)

# Prediction
if st.button("Predict Weight"):
    input_data = np.array([[height]])
    prediction = model.predict(input_data)
    weight = round(prediction[0][0], 2)
    st.success(f"Predicted Weight: {weight} kg")
