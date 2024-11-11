import logging
from abc import ABC,abstractmethod


import numpy as np
from sklearn.metrics import accuracy_score,f1_score,recall_score,precision_score,roc_auc_score


class Evaluation(ABC):
    """
    Abstract class defining the strategy for evaluating model performance
    """
    @abstractmethod
    def calculate_score(self,y_true,y_pred):
        pass


class AccuracyScore(Evaluation): 
    """This is the AccuracyScore class returns the accuracy"""   
    def calculate_score(self,y_true,y_pred):
        try:
            logging.info("Entered the calculate_score method of the AccuracyScore class")
            accuracy_scr = accuracy_score(y_true,y_pred)
            logging.info(f"The Accuracy score is {accuracy_scr}")
            return accuracy_scr
        
        except Exception as e:
            logging.error(f"Exception occured in calculate_score method of AccuracyScore class. Exception {e}")
            raise e

class F1Score(Evaluation):
    """This F1Score class returns the F1 score"""
    def calculate_score(self,y_true,y_pred):
        try:
            logging.info("Entered the calculate_score method of the F1Score class")
            f1_scr = f1_score(y_true,y_pred)
            logging.info(f"The Accuracy score is {f1_scr}")
            return f1_scr
        
        except Exception as e:
            logging.error(f"Exception occured in calculate_score method of F1Score class. Exception {e}")
            raise e



class RecallScore(Evaluation):
    def calculate_score(self,y_true,y_pred):
        try:
            logging.info("Entered the calculate_score method of the RecallScore class")
            recall_scr = recall_score(y_true,y_pred)
            logging.info(f"The Rcall score is {recall_scr}")
            return recall_scr
        
        except Exception as e:
            logging.error(f"Exception occured in calculate_score method of RecallScore class. Exception {e}")
            raise e


class PrecisionScore(Evaluation):
    def calculate_score(self,y_true,y_pred):
        try:
            logging.info("Entered the calculate_score method of the PrecisionScore class")
            precision_scr = f1_score(y_true,y_pred)
            logging.info(f"The Precision score is {precision_scr}")
            return precision_scr
        
        except Exception as e:
            logging.error(f"Exception occured in calculate_score method of PrecisionScore class. Exception {e}")
            raise e


class RocAucScore(Evaluation):
    def calculate_score(self,y_true,y_pred):
        try:
            logging.info("Entered the calculate_score method of the RocAucScore class")
            roc_auc_scr = roc_auc_score(y_true,y_pred)
            logging.info(f"The Precision score is {roc_auc_scr}")
            return roc_auc_score
        
        except Exception as e:
            logging.error(f"Exception occured in calculate_score method of RocAucScore class. Exception {e}")
            raise e


