import streamlit as st
from predict import predecir

st.title("Predicción de Churn - Telco Customer")
st.write("Complete los datos del cliente para predecir la probabilidad de abandono.")

# ===========================
# Entradas del usuario
# ===========================

user_input = {
    "SeniorCitizen": st.selectbox("¿Cliente Senior Citizen?", ["No", "Yes"]),
    "Partner": st.selectbox("¿Tiene pareja?", ["No", "Yes"]),
    "Dependents": st.selectbox("¿Tiene dependientes?", ["No", "Yes"]),

    "tenure": st.number_input("Meses con la empresa (tenure)", min_value=0, max_value=100, step=1),

    "OnlineSecurity": st.selectbox("Online Security", ["No", "Yes", "No internet service"]),
    "OnlineBackup": st.selectbox("Online Backup", ["No", "Yes", "No internet service"]),
    "DeviceProtection": st.selectbox("Device Protection", ["No", "Yes", "No internet service"]),
    "TechSupport": st.selectbox("Tech Support", ["No", "Yes", "No internet service"]),

    "Contract": st.selectbox("Tipo de contrato", ["Month-to-month", "One year", "Two year"]),
    "PaperlessBilling": st.selectbox("Factura electrónica (Paperless Billing)", ["No", "Yes"]),
    "PaymentMethod": st.selectbox(
        "Método de pago",
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
    ),

    "MonthlyCharges": st.number_input("Cargos mensuales (MonthlyCharges)", min_value=0.0, max_value=200.0, step=1.0),
    "TotalCharges": st.number_input("Cargos totales (TotalCharges)", min_value=0.0, max_value=10000.0, step=10.0)
}

# ===========================
# Predicción
# ===========================

if st.button("Predecir Churn"):
    pred, prob = predecir(user_input)

    st.subheader("Resultado de la predicción:")

    if pred == 1:
        st.error(f"⚠️ El cliente probablemente **ABANDONARÁ**.\nProbabilidad: **{prob:.2f}**")
    else:
        st.success(f"✅ El cliente probablemente **NO abandonará**.\nProbabilidad: **{prob:.2f}**")
