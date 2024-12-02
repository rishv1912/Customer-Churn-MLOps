import logging 
from abc import ABC,abstractmethod

import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split

from typing import Union 

class DataStrategy(ABC):
    
    @abstractmethod
    def handle_data(self,data):
        pass 


class DataPreProcessingStrategy(DataStrategy):
    def handle_data(self, data):
        try:
            data = data.drop([' "recordID"','customer_id'],axis=1)
            return data

        except Exception as e:
            logging.error(e)
            raise e
        
    def handle_unbalance(self,data):
        try:
            pass
        except Exception as e:
            raise e



class DataDivideStrategy(DataStrategy):
    def handle_data(self, data):
        try:
            X = data.drop(['churn'],axis=1)
            y = data['churn']
            X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)
            return X_train,X_test,y_train,y_test
        
        except Exception as e:
            logging.error(f"Error in dividing data :{e}")
        

class DataCleaning(DataStrategy):
    def __init__(self,data,strategy):
        self.data = data
        self.strategy = strategy

    def handle_data(self):
        try:
            return self.strategy.handle_data(self.data)
        except Exception as e:
            logging.error(f"Error while handling the data : {e}")
            raise e

