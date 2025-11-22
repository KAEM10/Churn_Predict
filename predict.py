import joblib
import pandas as pd

# Cargar artefactos
modelo = joblib.load("modelo_random_forest_optuna.joblib")
scaler = joblib.load("scaler.joblib")
label_encoders = joblib.load("label_encoders.joblib")
columnas = joblib.load("columnas_modelo.joblib")

def preprocess_input(data):
    df = pd.DataFrame([data])

    # Label Encoding
    for col, le in label_encoders.items():
        df[col] = le.transform(df[col])

    # Escalado
    df[columnas] = scaler.transform(df[columnas])

    return df[columnas]

def predecir(data):
    df = preprocess_input(data)
    prob = modelo.predict_proba(df)[0][1]
    pred = modelo.predict(df)[0]
    return pred, prob
