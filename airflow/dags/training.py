from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash  import BashOperator
from airflow.decorators import task

with DAG(
    dag_id="training",
    start_date=datetime(2025, 8, 24),
    schedule="0 0 * * *",
    catchup=False,
    tags=["training", "example1"]
) as dag:
    
    hello = BashOperator(
        task_id="train",
        bash_command='echo hello'
    )

    @task
    def airflow_task():
        print("hello world from airflow train")
        return "Task completed successfully"

    hello >> airflow_task()
