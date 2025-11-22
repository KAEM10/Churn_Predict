import streamlit as st
import pandas as pd
from predict import predecir

st.title("Predicción de Churn – Modelo Random Forest Optimizado")
st.write("Ingrese los datos del cliente:")

# Campos que debe llenar el usuario
tenure = st.number_input("Meses con la compañía (tenure)", min_value=0, max_value=100)
monthly = st.number_input("MonthlyCharges", min_value=0.0, max_value=200.0)
total = st.number_input("TotalCharges", min_value=0.0, max_value=10000.0)

gender = st.selectbox("gender", ["Male", "Female"])
internet = st.selectbox("InternetService", ["DSL","Fiber optic","No"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
payment = st.selectbox("PaymentMethod", ["Electronic check","Mailed check","Bank transfer (automatic)","Credit card (automatic)"])

# Construir el diccionario
data = {
    "tenure": tenure,
    "MonthlyCharges": monthly,
    "TotalCharges": total,
    "gender": gender,
    "InternetService": internet,
    "Contract": contract,
    "PaymentMethod": payment
}

if st.button("Predecir"):
    pred, prob = predecir(data)

    st.subheader("Resultado")
    st.write(f"Probabilidad de churn: **{prob:.2f}**")

    if pred == 1:
        st.error("⚠ El cliente tiene ALTO riesgo de abandono.")
    else:
        st.success("✔ El cliente NO tiene riesgo de abandono.")
