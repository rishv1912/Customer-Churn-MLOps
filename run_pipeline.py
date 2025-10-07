from pipeline.training_pipeline import train_pipeline


if __name__ == "__main__":
    data_path = "data/customer_data.csv"
    table_name = "customer_churn_data"
    train_pipeline(table_name=table_name)
