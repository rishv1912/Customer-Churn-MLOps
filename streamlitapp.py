import streamlit as st
import joblib
import numpy as np
import pandas as pd
import json
import requests

st.title("Customer Churn Prediction")



model = joblib.load('model.pkl')

print(type(model))
# Numeric Inputs
account_length = st.number_input("Account Length (days)", min_value=0, step=1, help="How long the customer has been with the company.")
area_code = st.number_input("Area Code", min_value=100, max_value=999, step=1, help="Three-digit area code of the customer's phone number.")
international_plan = st.selectbox(
    "Does the customer have an International Plan?",
    options=["Yes", "No"],
    help="Select whether the customer has an international calling plan."
)
voice_mail_plan = st.selectbox(
    "Does the customer have a Voicemail Plan?",
    options=["Yes", "No"],
    help="Select whether the customer has a voicemail plan."
)
number_vmail_messages = st.number_input("Number of Voicemail Messages", min_value=0, step=1, help="Number of voicemail messages the customer has.")
total_day_minutes = st.number_input("Total Day Minutes", min_value=0.0, step=0.1, help="Total minutes the customer used during the day.")
total_day_calls = st.number_input("Total Day Calls", min_value=0, step=1, help="Total calls made during the day.")
total_eve_minutes = st.number_input("Total Evening Minutes", min_value=0.0, step=0.1, help="Total minutes the customer used during the evening.")
total_eve_calls = st.number_input("Total Evening Calls", min_value=0, step=1, help="Total calls made during the evening.")
total_night_minutes = st.number_input("Total Night Minutes", min_value=0.0, step=0.1, help="Total minutes the customer used during the night.")
total_night_calls = st.number_input("Total Night Calls", min_value=0, step=1, help="Total calls made during the night.")
total_intl_minutes = st.number_input("Total International Minutes", min_value=0.0, step=0.1, help="Total minutes the customer used for international calls.")
total_intl_calls = st.number_input("Total International Calls", min_value=0, step=1, help="Total calls made internationally.")
number_customer_service_calls = st.number_input("Number of Customer Service Calls", min_value=0, step=1, help="Number of calls the customer made to customer service.")


# Convert categorical inputs to binary (assuming your model expects 1/0)
international_plan_binary = 1 if international_plan == "Yes" else 0
voice_mail_plan_binary = 1 if voice_mail_plan == "Yes" else 0

# Combine all inputs into a single array
features = np.array([[
    account_length, 
    area_code, 
    international_plan_binary, 
    voice_mail_plan_binary,
    number_vmail_messages,
    total_day_minutes, 
    total_day_calls, 
    total_eve_minutes, 
    total_eve_calls,
    total_night_minutes, 
    total_night_calls, 
    total_intl_minutes, 
    total_intl_calls,
    number_customer_service_calls, 
]])

inputs ={
    "account_length" : account_length, 
    "area_code" : area_code, 
    "international_plan_binary" : international_plan_binary, 
    "voice_mail_plan_binary": voice_mail_plan_binary,
    "number_vmail_messages" : number_vmail_messages,
    "total_day_minutes" : total_day_minutes, 
    "total_day_calls" : total_day_calls, 
    "total_eve_minutes" : total_eve_minutes, 
    "total_eve_calls" : total_day_calls,
    "total_night_minutes" : total_night_minutes, 
    "total_night_calls": total_night_calls, 
    "total_intl_minutes" : total_intl_minutes, 
    "total_intl_calls" :total_intl_calls,
    "number_customer_service_calls" :number_customer_service_calls

}

# Predict button
if st.button("Predict"):
    # prediction = model.predict(features)
    # st.write(f"The predicted class is: {'Churn' if prediction[0] else 'Not Churn'}")
    url = "http://127.0.0.1:8000/predict"
    response = requests.post(url=url,data = json.dumps(inputs))
    
    if response.status_code == 200:
        result = response.json()

        churn_text = "Yes" if result["churn"] else "No"
        probability = round(result["churn_probability"] * 100,2)
        
        st.write(f"Churn : {churn_text}")
    
    else:
        st.error("Error: Unable to Predict, Try again")



