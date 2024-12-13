import joblib
import logging

from sklearn.tree import DecisionTreeClassifier
# from xgboost import XGBClassifier
# from .config import ModelNameConfig

import mlflow
import mlflow.sklearn

def train_model(
        X_train,
        X_test,
        y_train,
        y_test):
    try:
        # xgb = XGBClassifier()
        # trained_model = xgb.train(X_train,y_train)
        # return trained_model

        clf = DecisionTreeClassifier()

        with mlflow.start_run():
            
            trained_model = clf.fit(X_train,y_train)

            mlflow.sklearn.log_model(trained_model,"decision_trees")
        

        joblib.dump(trained_model,'model.pkl')

        return trained_model
    except Exception as e:
        logging.error(f"Error in training Model: {e}")
        raise e