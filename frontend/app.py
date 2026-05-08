import streamlit as st
import requests

st.title("🎓 Student Result Predictor")

hours = st.slider("Study Hours", 0, 12)

if st.button("Predict"):

    response = requests.get(
        f"http://127.0.0.1:8000/predict?hours={hours}"
    )

    result = response.json()["result"]

    st.success(f"Prediction: {result}")