import joblib
import pandas as pd

# ===============================
# Cargar artefactos del modelo
# ===============================
modelo = joblib.load("modelo_random_forest_optuna.joblib")
scaler = joblib.load("scaler.joblib")
label_encoders = joblib.load("label_encoders.joblib")
columnas = joblib.load("columnas_modelo.joblib")   # columnas EXACTAS del modelo


def preprocess_input(data):

    # Convertimos el input en DataFrame
    df = pd.DataFrame([data])

    # ===============================
    # 1. Crear todas las columnas necesarias
    # ===============================
    # Si falta alguna columna, la agregamos con NA (o cero si prefieres)
    for col in columnas:
        if col not in df.columns:
            df[col] = None

    # ===============================
    # 2. Aplicar LabelEncoder SOLO a columnas categóricas del modelo
    # ===============================
    for col, le in label_encoders.items():
        if col in df.columns:
            df[col] = le.transform(df[col].astype(str))

    # ===============================
    # 3. Escalar SOLO columnas numéricas
    # ===============================
    # Detectamos columnas numéricas a escalar según lo guardado en entrenamiento
    columnas_numericas = [col for col in columnas if col not in label_encoders]

    df[columnas_numericas] = scaler.transform(df[columnas_numericas])

    # ===============================
    # 4. Devolver DataFrame ordenado
    # ===============================
    return df[columnas]


def predecir(data):
    df = preprocess_input(data)
    prob = modelo.predict_proba(df)[0][1]
    pred = modelo.predict(df)[0]
    return pred, prob
