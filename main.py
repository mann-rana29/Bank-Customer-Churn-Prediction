from fastapi import FastAPI , HTTPException
import tensorflow as tf
import numpy as np
from pydantic import BaseModel
import joblib as jb

app = FastAPI()

model = tf.keras.models.load_model("model.keras")
scaler = jb.load("scaler.pkl")

class CustomerData(BaseModel):
    CreditScore : int
    Gender : str
    Age : int
    Tenure : int
    Balance : float
    NumberOfProducts : int
    HasCreditCard : int
    IsActiveMember : int
    EstimatedSalary : float
    Geography : str

@app.get('/')
def read_root():
    return {"message" : "Bank Customer Churn Prediction API is live!"}

@app.post('/predict')
def predict(data : CustomerData):
    try:
        gender = 1 if data.Gender.lower() == "female" else 0
        geo_france = 1 if data.Geography.lower() == "france" else 0
        geo_spain = 1 if data.Geography.lower() == "spain" else 0
        geo_germany = 1 if data.Geography.lower() == "germany" else 0

        raw_input = [data.CreditScore,data.Age,data.Tenure ,data.Balance,data.NumberOfProducts,data.EstimatedSalary]

        scaled_input = scaler.transform([raw_input])[0]

        input_features = [
            scaled_input[0],
            gender,
            scaled_input[1],
            scaled_input[2],
            scaled_input[3],
            scaled_input[4],
            data.HasCreditCard,
            data.IsActiveMember,
            scaled_input[5],
            geo_france,
            geo_germany,
            geo_spain
        ]

        input_array = np.array(input_features).reshape(1,-1)

        prediction = model.predict(input_array)[0][0]

        exited = int(prediction > 0.5)

        return{
            "Exited" : exited,
            "Probability" : float(prediction)
        }

    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))
