import streamlit as st
import requests

st.title("🎓 Student Result Predictor")

hours = st.slider("Study Hours", 0, 12)

if st.button("Predict"):

    response = requests.get(
        f"YOUR_RENDER_BACKEND_URL/predict?hours={hours}"
    )

    data = response.json()

    st.write(data)

    if "result" in data:
        st.success(f"Prediction: {data['result']}")
    else:
        st.error("Result key not found")