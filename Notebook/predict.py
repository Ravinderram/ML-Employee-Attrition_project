# predict.py
import pandas as pd
import joblib
# Load preprocessing objects
scaler = joblib.load("model/scaler.pkl")
encoders = joblib.load("model/encoders.pkl")

MODEL_PATHS = {
    "Random Forest": "model/random_forest.pkl",
    "Logistic Regression": "model/logistic_regression.pkl"
}

def preprocess_input(input_df):
    """
    Apply encoding and scaling to user input
    """
    df = input_df.copy()

    # Encode categorical columns
    for col, encoder in encoders.items():
        df[col] = encoder.transform(df[col])

    # Scale features
    df_scaled = scaler.transform(df)

    return df_scaled


def predict_attrition(input_data: dict, model_name: str):
    """
    Predict attrition based on user input
    """
    # Convert dict to DataFrame
    input_df = pd.DataFrame([input_data])

    # Preprocess
    processed_input = preprocess_input(input_df)

    # Load model
    model = joblib.load(MODEL_PATHS[model_name])

    # Prediction
    prediction = model.predict(processed_input)[0]
    probability = model.predict_proba(processed_input)[0][1]

    return prediction, probability
