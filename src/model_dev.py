import logging 
from abc import ABC, abstractmethod


import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC,LinearSVC
from xgboost import XGBClassifier



class Model(ABC):

    @abstractmethod
    def train(self,x_train,y_train):
        pass

class LogisticRegressionModel(Model):
    """LogisticRegressionModel that implements that Model Interface"""
    def train(self,x_train,y_train,**kwargs):
        try:
            reg = LogisticRegression(**kwargs)
            reg.fit(x_train,y_train)
            logging.info("Model training Completed")
            return reg
        
        except Exception as e:
            logging.error(f"Error in training Model {e}")
            raise e

class DecisionTreeModel(Model):
    """DecisionTreeModel that implements that Model Interface"""
    def train(self,x_train,y_train,**kwargs):
        try:
            dt = DecisionTreeClassifier(**kwargs)
            dt.fit(x_train,y_train)
            logging.info("Model training Completed")
            return dt
        
        except Exception as e:
            logging.error(f"Error in training Model {e}")
            raise e

class RandomForestsModel(Model):
    """RandomFroestModel that implements that Model Interface"""
    def train(self,x_train,y_train,**kwargs):
        try:
            rf = RandomForestClassifier(**kwargs)
            rf.fit(x_train,y_train)
            logging.info("Model training Completed")
            return rf
        
        except Exception as e:
            logging.error(f"Error in training Model {e}")
            raise e

class SVCModel(Model):
    """Support Vector Machine Model that implements that Model Interface"""
    def train(self,x_train,y_train,**kwargs):
        try:
            svm = SVC(**kwargs)
            svm.fit(x_train,y_train)
            logging.info("Model training Completed")
            return svm
        
        except Exception as e:
            logging.error(f"Error in training Model {e}")
            raise e


class XGBClfModel():
    pass

# Models we'll be used
# Logistic Regression
# Decision Trees
# Random Forests
# Support Vector Machines
