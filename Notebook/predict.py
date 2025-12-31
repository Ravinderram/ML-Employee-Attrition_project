{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d6a38328",
   "metadata": {},
   "outputs": [],
   "source": [
    "# predict.py\n",
    "import pandas as pd\n",
    "import joblib\n",
    "\n",
    "# Load preprocessing objects\n",
    "scaler = joblib.load(\"model/scaler.pkl\")\n",
    "encoders = joblib.load(\"model/encoders.pkl\")\n",
    "\n",
    "MODEL_PATHS = {\n",
    "    \"Random Forest\": \"model/random_forest.pkl\",\n",
    "    \"Logistic Regression\": \"model/logistic_regression.pkl\"\n",
    "}\n",
    "\n",
    "def preprocess_input(input_df):\n",
    "    \"\"\"\n",
    "    Apply encoding and scaling to user input\n",
    "    \"\"\"\n",
    "    df = input_df.copy()\n",
    "\n",
    "    # Encode categorical columns\n",
    "    for col, encoder in encoders.items():\n",
    "        df[col] = encoder.transform(df[col])\n",
    "\n",
    "    # Scale features\n",
    "    df_scaled = scaler.transform(df)\n",
    "\n",
    "    return df_scaled\n",
    "\n",
    "\n",
    "def predict_attrition(input_data: dict, model_name: str):\n",
    "    \"\"\"\n",
    "    Predict attrition based on user input\n",
    "    \"\"\"\n",
    "    # Convert dict to DataFrame\n",
    "    input_df = pd.DataFrame([input_data])\n",
    "\n",
    "    # Preprocess\n",
    "    processed_input = preprocess_input(input_df)\n",
    "\n",
    "    # Load model\n",
    "    model = joblib.load(MODEL_PATHS[model_name])\n",
    "\n",
    "    # Prediction\n",
    "    prediction = model.predict(processed_input)[0]\n",
    "    probability = model.predict_proba(processed_input)[0][1]\n",
    "\n",
    "    return prediction, probability\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
