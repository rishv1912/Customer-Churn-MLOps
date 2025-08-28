from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash  import BashOperator
from airflow.providers.standard.operators.python  import PythonOperator
from airflow.decorators import task

with DAG(
    dag_id="ML Pipeline",
    start_date=datetime(2025, 8, 24),
    schedule="0 0 * * *",
    catchup=False,
    tags=["training", "example1"]
) as dag:
    
    def ml_pipeline():

        data_task = PythonOperator(
            
        )
            
    
