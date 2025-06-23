from pipeline.training_pipeline import train_pipeline
import mlflow

mlflow.set_tracking_uri(uri="http://127.0.0.1:8080")

if __name__ == "__main__":
    data_path = "data/customer_data.csv"
    train_pipeline(data_path)
