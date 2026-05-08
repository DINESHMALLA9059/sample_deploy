import streamlit as st
import requests

st.title("🎓 Student Result Predictor")

hours = st.slider("Study Hours", 0, 12)

if st.button("Predict"):

    response = requests.get(
        f"https://sample-deploy-x69u.onrender.com/predict?hours={hours}"
    )

    data = response.json()

    st.write(data)

    if "result" in data:
        st.success(f"Prediction: {data['result']}")
    else:
        st.error("Result key not found")