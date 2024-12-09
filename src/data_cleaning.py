import logging 
from abc import ABC,abstractmethod

import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from constants.training_pipeline import COLS_TO_DROP,TARGET_COLUMN

from typing import Union 

class DataStrategy(ABC):
    
    @abstractmethod
    def handle_data(self,data):
        pass 


class DataPreProcessingStrategy(DataStrategy):
    def handle_data(self, data):
        try:
            data = data.drop(COLS_TO_DROP,axis=1)                                    
            return data

        except Exception as e:
            logging.error(e)
            raise e


class DataDivideStrategy(DataStrategy):
    def handle_data(self, data):
        try:
            X = data.drop([TARGET_COLUMN],axis=1)
            y = data[TARGET_COLUMN]
            X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

            ordinal_encoder = OrdinalEncoder()

            ordinal_encoder.fit(X_train[["international_plan","voice_mail_plan"]])

            X_train[["international_plan","voice_mail_plan"]] = ordinal_encoder.transform(X_train[
                ["international_plan","voice_mail_plan"]])
            
            X_test[["international_plan","voice_mail_plan"]] = ordinal_encoder.transform(X_test[
                ["international_plan","voice_mail_plan"]])
            
            label_encoder = LabelEncoder()

            label_encoder.fit(y_train[TARGET_COLUMN])
            
            y_train[TARGET_COLUMN] = label_encoder.transform(y_train[TARGET_COLUMN])

            y_test[TARGET_COLUMN] = label_encoder.transform(y_test[TARGET_COLUMN])

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

