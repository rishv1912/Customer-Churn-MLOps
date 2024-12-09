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

            ordinal_encoder = OrdinalEncoder()

            data['international_plan'] = ordinal_encoder.fit_transform(data[['international_plan']])
            data['voice_mail_plan'] = ordinal_encoder.fit_transform(data[['voice_mail_plan']])

            # this is for target column 'churn'
            label_encoder = LabelEncoder()

            data[TARGET_COLUMN] = label_encoder.fit_transform(data[[TARGET_COLUMN]])
            print(data)
                                                              
            return data

        except Exception as e:
            logging.error(e)
            raise e
        
    def handle_unbalance(self,data):
        try:
            pass
        except Exception as e:
            raise e
    
    def handle_feature(self,data):
        try:
            # this is for the two object columns 'international_plan' and 'voice_mail_plan'
            ordinal_encoder = OrdinalEncoder()

            data['international_plan'] = ordinal_encoder.fit_transform(data[['international_plan']])
            data['voice_mail_plan'] = ordinal_encoder.fit_transform(data[['voice_mail_plan']])

            # this is for target column 'churn'
            label_encoder = LabelEncoder()

            data[TARGET_COLUMN] = label_encoder.fit_transform(data[[TARGET_COLUMN]])

            return data


        except Exception as e:
            logging.error("Error while encoding as {e}")
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

