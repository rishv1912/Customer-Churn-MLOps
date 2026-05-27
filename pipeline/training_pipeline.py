import mlflow
from mlflow.models import infer_signature

import os 

import pandas as pd
from steps.ingest_data import ingest_df,ingest_df_sql
from steps.clean_data import clean_df
from steps.model_train import train_model
from steps.evaluation import evaluate_model

# # mlflow.set_tracking_uri("http://127.0.0.1:5000")
# mlflow.set_tracking_uri(f"file://{os.path.abspath('mlruns')}")
# # mlflow.set_tracking_uri("file:///Users/sanjayprajapati/Documents/Super 30 projects/Customer-Churn/mlruns")
is_docker = os.path.exists("/.dockerenv")

if is_docker:
    
    mlflow.set_tracking_uri("file:///app/mlruns")
    mlflow.set_experiment("Telecom Customer Churn Prediction Docker")  
    REGISTERED_MODEL_NAME = "Customer Churn Tracing Docker"
else:
    mlflow.set_tracking_uri(f"file://{os.path.abspath('mlruns')}")
    mlflow.set_experiment("Telecom Customer Churn Prediction")  
    REGISTERED_MODEL_NAME = "Customer Churn tracing"

def train_pipeline(source):
    if os.path.isfile(source):
        df = ingest_df(source) # autodetect a file or not then get the data
    else:
        df = ingest_df_sql(source)
    X_train,X_test,y_train,y_test = clean_df(df)
    model,best_params = train_model(X_train,X_test,y_train,y_test)
    precision,recall,f1_scr,roc_auc = evaluate_model(model,X_test,y_test)
    # this print is temporary to check is it working well or not, giving any error
    print("X_train",X_train.shape)
    print(X_train.head(2).T)
    print("X_test",X_test.shape)
    print("y_train",y_train.shape)
    print("y_test",y_test.shape)
    print(f"Precision {precision:.4f}\nRecall(Most important) {recall:.4f}\nF1 Score {f1_scr:.4f}\nROC AUC {roc_auc:.4f}\nX_train len {len(X_train)}\nX_test {len(X_test)}")
    print(X_train.T.head(1))
    print(y_train) #checking the churn in train set
    print(y_test) #checking the churn in test set

    metrics ={
        "Precision":precision,
        "Recall":recall,
        "F1 Score":f1_scr,
        "Roc Auc":roc_auc,
    } 

    # integration of mlflow
    
    with mlflow.start_run():

        # for key,value in metrics.items():
        #     mlflow.log_metric(key,value)
        
        # params
        mlflow.log_params(best_params)
        mlflow.log_param("train_size",len(X_train))
        mlflow.log_param("test_size",len(X_test))
        mlflow.log_param("features",X_train.shape[1])
        
       # metrics 
        mlflow.log_metric("precision",precision)
        mlflow.log_metric("recall",recall)
        mlflow.log_metric("f1score",f1_scr)
        mlflow.log_metric("roc_auc",roc_auc)
        
        is_docker = os.path.exists("/.dockerenv")
         
        mlflow.set_tags({
            "source": "docker" if is_docker else "locally",
            "Environment" : "docker" if is_docker else "local-machine",
            "Developer": "Rishav",
            "Training Info":"Decision tree classifier for Customer Churn",
            
        })

        # mlflow.set_tag("file path","using file:///Users/sanjayprajapati/Documents/Super 30 projects/Customer-Churn/mlruns")
        

        signature = infer_signature(X_train,model.predict(X_train))

        model_info = mlflow.sklearn.log_model(
            sk_model = model,
            name="customer_churn",
            signature=signature,
            input_example=X_train.head(5),
            registered_model_name = "Customer Churn tracing"
        )

        # mlflow.set_logged_model_tags(
        #     model_info.model_id,{"Training":"Training a Decision Tree model"}
        # )
        # mlflow.pyfunc.load_model(model_info.model_uri)

        # mlflow.end_run()

