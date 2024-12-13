# End to End Customer Churn Project
This Project is for detecting Customer Churn using their past records and service provided.

## Table of content
1. [Projeect Objective](#project-objective)
2. 
3. 
4. 
5. 
6. 



## Problem Statement

## Project Objective

## **Tech Stack**
| **Category**             | **Tools/Technologies**                                  | **Description**                                                |
|--------------------------|---------------------------------------------------------|----------------------------------------------------------------|
| **Frontend**             | Streamlit                                               | Provides a simple UI for real-time single URL predictions.     |
| **Backend**              | FastAPI                                                 | Handles batch predictions and API endpoints.                   |
| **Modeling**             | XGBoost, Python                                         | Machine learning model for detecting malicious URLs.           |
| **Database**             | MongoDB                                                 | Stores data records for ingestion and model training.          |
| **Orchestration**        | Apache Airflow                                          | Orchestrates training, retraining, and batch prediction pipelines. |
| **Experiment Tracking**  | MLflow                                                  | Tracks model metrics like F1-score, Precision, and Recall.     |
| **CI/CD**                | GitHub Actions                                          | Automates CI/CD pipelines, including Docker build and deployment. |
| **Containerization**     | Docker, AWS ECR                                         | Docker images stored securely in **ECR** for consistent deployment. |
| **Cloud Storage**        | AWS S3                                                  | Stores artifacts, trained models, and logs.                    |
| **Cloud Hosting**        | AWS EC2 Instance                                        | Serves as a **self-hosted runner** for GitHub Actions, enabling deployment. |
## Features

- state                            
- account_length                   
- area_code                        
- international_plan               
- voice_mail_plan                  
- number_vmail_messages            
- total_day_minutes                
- total_day_calls                  
- total_day_charge                 
- total_eve_minutes                
- total_eve_calls                  
- total_eve_charge                 
- total_night_minutes              
- total_night_calls                
- total_night_charge               
- total_intl_minutes               
- total_intl_calls                 
- total_intl_charge                
- number_customer_service_calls   

## Target Column 
- churn  



### Stack
1. Zenml
2. MLFlow
3. FastAPI
4. AWS