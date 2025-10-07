# Importing Libraries
import logging 
import pandas as pd
from sqlalchemy import create_engine

class IngestData:
    """This IngestData class is taking the path of the data and return the data as Pandas DataFrame"""
    def __init__(self,data_path : str):
        self.data_path = data_path

    def get_data(self):
        """get_data is the method inside IngestData class which is returning the data as Pandas DataFrame
        It can used as .get_data()"""
        logging.info(f"Ingesting data from {self.data_path}")
        return pd.read_csv(self.data_path)
    


def ingest_df(data_path :str ):
    """This function is getting the DataFrame from IngestData class and storing and returing in a variable called 'df'.
    It is using one argument called 'data_path', which is being used in a object of IngestData class,calling the DataFrame and storing it in a reference variable 'df' and then returning that reference variable"""
    try:
        ingest_data = IngestData(data_path)
        df = ingest_data.get_data()
        return df
    
    except Exception as e:
        logging.error(f"Error while ingesting the data as {e}")
        raise e


def ingest_df_sql(table_name):
    engine = None
    try:
        engine = create_engine('postgresql://postgres:whygrespass@localhost:5433/telecom_db')
        df = pd.read_sql_table(table_name, engine)
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
    finally:
        if engine:
            engine.dispose()