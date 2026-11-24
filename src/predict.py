
import joblib
import pandas as pd
from pathlib import Path

# Locate the project directory
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Load saved model
MODEL_PATH = PROJECT_DIR / "models" / "logistic_regression_pipeline.pkl"

artifact = joblib.load(MODEL_PATH)

pipeline = artifact["pipeline"]
threshold = artifact["threshold"]


def predict_passenger(passenger_data):

    # Convert input into DataFrame
    passenger_df = pd.DataFrame([passenger_data])

    # Generate survival probability
    probability = pipeline.predict_proba(passenger_df)[0, 1]

    # Apply selected threshold
    prediction = int(probability >= threshold)

    result = {
        "survival_probability": round(float(probability), 4),
        "prediction": prediction,
        "status": "Survived" if prediction == 1 else "Did Not Survive"
    }

    return result


if __name__ == "__main__":

    passenger = {
        "Pclass": 1,
        "Sex": "female",
        "Age": 25,
        "Fare": 80,
        "Embarked": "C",
        "FamilySize": 2
    }

    result = predict_passenger(passenger)

    print("\nTITANIC SURVIVAL PREDICTION")
    print("--------------------------")
    print("Probability:", result["survival_probability"])
    print("Prediction:", result["status"])
    print("Threshold:", threshold)
