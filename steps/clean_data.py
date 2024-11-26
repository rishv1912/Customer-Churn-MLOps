import logging
from src.data_cleaning import DataCleaning,DataDivideStrategy,DataPreProcessingStrategy


def clean_data(df):
    try:
        process_strategy = DataPreProcessingStrategy()
        data_cleaning = DataCleaning(df,process_strategy)
        processed_data = data_cleaning.handle_data()

        divide_data = DataDivideStrategy()
        data_cleaning = DataCleaning(processed_data,divide_data)
        X_train,X_test,y_train,y_test = data_cleaning.handle_data()
        logging.info("Data Cleaning Completed")

        return X_train,X_test,y_train,y_test
    
    except Exception as e:
        logging.error(f"Error in cleaning data : {e}")
        raise e

