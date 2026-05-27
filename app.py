from fastapi import FastAPI, HTTPException
from enum import Enum
from pydantic import BaseModel,validator
import pickle
import joblib
import pandas as pd

import mlflow
import os 


# is_docker = os.path.exists("/.dockerenv")

# if is_docker :
#     mlflow.set_tracking_uri("file:///app/mlruns")
# else:
#     mlflow.set_tracking_uri("file:///Users/sanjayprajapati/Documents/Super 30 projects/Customer-Churn/mlruns")
    
# model = mlflow.sklearn.load_model("models:/Customer Churn tracing/latest")


is_docker = os.path.exists("/.dockerenv")

if is_docker:
    # Load directly — bypass registry ✅
    mlflow.set_tracking_uri(
        "file:///app/mlruns"
    )
    model = mlflow.sklearn.load_model("models:/Customer Churn Tracing Docker/latest")
else:
    # Use registry locally ✅
    mlflow.set_tracking_uri(
        "file:///Users/sanjayprajapati/Documents/Super 30 projects/Customer-Churn/mlruns"
    )
    model = mlflow.sklearn.load_model("models:/Customer Churn tracing/latest")

# model = joblib.load("churn_model.pkl")

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


@app.post("/predict")
async def predict_churn(data : CustomerData):
    try:
        input_features= pd.DataFrame(
            [{
                "account_length" : data.account_length, 
                "area_code" : data.area_code, 
                "international_plan" : data.international_plan_binary, 
                "voice_mail_plan": data.voice_mail_plan_binary,
                "number_vmail_messages" : data.number_vmail_messages,
                "total_day_minutes" : data.total_day_minutes, 
                "total_day_calls" : data.total_day_calls, 
                "total_eve_minutes" : data.total_eve_minutes, 
                "total_eve_calls" : data.total_eve_calls,
                "total_night_minutes" : data.total_night_minutes, 
                "total_night_calls": data.total_night_calls, 
                "total_intl_minutes" : data.total_intl_minutes, 
                "total_intl_calls" :data.total_intl_calls,
                "number_customer_service_calls" :data.number_customer_service_calls

            }
        ])

        prediction = model.predict(input_features)
        churn_probability = model.predict_proba(input_features)[0][1]

        return {
            "churn" : bool(prediction[0]),
            "churn_probability" : float(churn_probability)
        }
    except Exception as e :
        raise HTTPException(status_code=500,detail =(str(e)))
        
