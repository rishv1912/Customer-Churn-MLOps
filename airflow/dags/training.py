from datetime import datetime
from airflow.decorators import task,dag
import os

@dag(
    dag_id="customer_churn",
    start_date=datetime(2025, 8, 24),
    schedule="*/15 * * * *",
    catchup=False,
    tags=["training", "example1"] 
)
    
def customer_churn_pipeline():
    
    @task
    def run_ml_pipeline():
        import sys
        PROJECT_ROOT =  "/Users/sanjayprajapati/Documents/Super 30 projects/Customer-Churn"
        if PROJECT_ROOT not in sys.path:
            sys.path.insert(0,PROJECT_ROOT)
        
        from pipeline.training_pipeline import train_pipeline   
        data_path = os.path.join(PROJECT_ROOT,"data","customer_data.csv")
        train_pipeline(data_path)
        return "Pipeline Created Successfully"

    run_ml_pipeline()
    

ml_pipeline_dag = customer_churn_pipeline()
            
            
            
    
# from datetime import datetime
# from airflow.decorators import task, dag

# @dag(
#     dag_id="customer_churn",
#     start_date=datetime(2025, 8, 24),
#     schedule="0 0 * * *",
#     catchup=False,
#     tags=["training", "example1"]
# )
# def customer_churn_pipeline():

#     @task
#     def run_ml_pipeline():
#         return "hello from task"

#     run_ml_pipeline()

# ml_pipeline_dag = customer_churn_pipeline()