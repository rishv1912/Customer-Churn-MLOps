import streamlit as st
import joblib

model = joblib.load('model.pkl')


st.title('Telecom Customer Churn App')