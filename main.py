from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

app = FastAPI()

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('columns.pkl', 'rb') as f:
    columns = pickle.load(f)

# Input schema (MATCHES YOUR DATASET)
class InputData(BaseModel):
    monthly_salary: float
    age: float
    house_price: float
    down_payment: float
    loan_amount: float
    running_emi: float

@app.get("/")
def home():
    return {"message": "Buy vs Rent API running"}

@app.post("/predict")
def predict(data: InputData):
    input_dict = data.dict()

    # Ensure correct column order
    input_list = [input_dict[col] for col in columns]
    input_array = np.array(input_list).reshape(1, -1)

    prediction = model.predict(input_array)[0]

    result = "Buy 🏡" if prediction == 1 else "Rent 🏠"

    return {"prediction": result}