from fastapi import FastAPI, HTTPException
from enum import Enum
from pydantic import BaseModel,validator
import pickle
import joblib

model = joblib.load("churn_model.pkl")

app = FastAPI()

# base class for getting 
class CustomerData(BaseModel):               
    account_length : int               
    area_code : int     
    international_plan_binary : int             
    voice_mail_plan_binary : int
    number_vmail_messages : int         
    total_day_minutes : float      
    total_day_calls : int
    total_eve_minutes : float            
    total_eve_calls : int        
    total_night_minutes : float             
    total_night_calls : int                    
    total_intl_minutes :float
    total_intl_calls : int              
    number_customer_service_calls :int

    # from pydantic library
    # @validator("voice_mail_plan","international_plan")
    # def validate_yes_no(cls,value):
    #     if value.lower() in ["yes","y"]:
    #         return 1
    #     elif value.lower() in ["no","n"]:
    #         return 0
    #     else:
    #         raise ValueError("Input must be 'Yes' or 'No'")

# @app.get('/')
# async def root():
#     return {"message": "Customer Churn Prediction"}

@app.post("/predict")
async def predict_churn(data : CustomerData):
    input_features= [
        [
            data.account_length,
            data.area_code,
            data.international_plan_binary,
            data.voice_mail_plan_binary,
            data.number_vmail_messages,
            data.total_day_minutes,
            data.total_day_calls,
            data.total_eve_minutes,
            data.total_eve_calls,
            data.total_night_minutes,
            data.total_night_calls,
            data.total_intl_minutes,
            data.total_intl_calls,
            data.number_customer_service_calls

        ]
    ]

    prediction = model.predict(input_features)
    churn_probability = model.predict_proba(input_features)[0][1]

    return {
        "churn" : bool(prediction[0]),
        "churn_probability" : churn_probability
    }
