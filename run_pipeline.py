from pipeline.training_pipeline import train_pipeline


if __name__ == "__main__":
    data_path = "data/customer_data.csv"
    train_pipeline(data_path)
