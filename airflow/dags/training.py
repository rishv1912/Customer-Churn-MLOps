from datetime import datetime
from airflow.decorators import task,dag
import os

@dag(
    dag_id="customer_churn", # unique name in airflow ui
    start_date=datetime(2025, 8, 24), #   DAG active from 24 aug 2025
    schedule="@daily", # runs every 15 min 
    catchup=False,# won't run missed scheduled from the past 
    tags=["training", "example1"]  # labels filtering in ui
)
    
def customer_churn_pipeline():
    """
    it is the DAG workflow created using @dag, it defines the workflow 
    """
    
    @task
    def run_ml_pipeline():
        import sys
        import os 
        
        is_docker = os.path.exists("/.dockerenv")
        if is_docker:
            PROJECT_ROOT = "/app"
        else:
            PROJECT_ROOT =  "/Users/sanjayprajapati/Documents/Super 30 projects/Customer-Churn"
        # PROJECT_ROOT =  "/app"
        if PROJECT_ROOT not in sys.path:
            sys.path.insert(0,PROJECT_ROOT)
        
        from pipeline.training_pipeline import train_pipeline   
        data_path = os.path.join(PROJECT_ROOT,"data","customer_data.csv")
        train_pipeline(data_path)
        return "Pipeline Created Successfully"

    run_ml_pipeline()
    

ml_pipeline_dag = customer_churn_pipeline()