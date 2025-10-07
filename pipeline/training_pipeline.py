import mlflow
from mlflow.models import infer_signature

import pandas as pd
from steps.ingest_data import ingest_df,ingest_df_sql
from steps.clean_data import clean_df
from steps.model_train import train_model
from steps.evaluation import evaluate_model

# mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_tracking_uri("file:///Users/sanjayprajapati/Documents/Super 30 projects/Customer-Churn/mlruns")
mlflow.set_experiment("Telecom Customer Churn Prediction")


def train_pipeline(table_name):
    # df = ingest_df(data_path)
    df = ingest_df_sql(table_name)
    X_train,X_test,y_train,y_test = clean_df(df)
    model,best_params = train_model(X_train,X_test,y_train,y_test)
    precision,recall,f1_scr,roc_auc = evaluate_model(model,X_test,y_test)
    # this print is temporary to check is it working well or not, giving any error
    print("X_train",X_train.shape)
    print(X_train.head(2).T)
    print("X_test",X_test.shape)
    print("y_train",y_train.shape)
    print("y_test",y_test.shape)
    print(f"Precision {precision}\nRecall {recall}\nF1 Score {f1_scr}\nROC AUC {roc_auc}\nX_train len {len(X_train)}\nX_test {len(X_test)}")
    print(X_train.T.head(1))

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
       
        mlflow.log_metric("precision",precision)
        mlflow.log_metric("recall",recall)
        mlflow.log_metric("f1score",f1_scr)
        mlflow.log_params(best_params)

        mlflow.set_tag("mlflow.user", "Rishav")  
        mlflow.set_tag("Training Info","Decision tree classifier for Customer Churn")

        signature = infer_signature(X_train,model.predict(X_train))

        model_info = mlflow.sklearn.log_model(
            sk_model = model,
            artifact_path="customer_churn",
            signature=signature,
            input_example=X_train,
            registered_model_name = "Customer Churn tracing"
        )

        # mlflow.set_logged_model_tags(
        #     model_info.model_id,{"Training":"Training a Decision Tree model"}
        # )
        mlflow.pyfunc.load_model(model_info.model_uri)

        # mlflow.end_run()
