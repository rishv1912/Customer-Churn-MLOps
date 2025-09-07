from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash  import BashOperator
from airflow.providers.standard.operators.python  import PythonOperator
from airflow.decorators import task

from steps.clean_data import clean_df
from steps.ingest_data import ingest_df
from steps.model_train import train_model
from steps.evaluation import evaluate_model
from pipeline.training_pipeline import train_pipeline


with DAG(
        dag_id="ML Pipeline",
        start_date=datetime(2025, 8, 24),
        schedule="0 0 * * *",
        catchup=False,
        tags=["training", "example1"] ) as dag:
    
    def ml_pipeline():  

        data_task = PythonOperator(

        )
            
    
