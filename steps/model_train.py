import logging
from .config import ModelNameConfig
from xgboost import XGBClassifier

def train_model(
        X_train,
        X_test,
        y_train,
        y_test):
    try:
        xgb = XGBClassifier()
        trained_model = xgb.train(X_train,y_train)
        return trained_model

    except Exception as e:
        logging.error(f"Error in training Model: {e}")
        raise e