import joblib
import logging

from sklearn.tree import DecisionTreeClassifier
# from xgboost import XGBClassifier
# from .config import ModelNameConfig


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
            
        trained_model = clf.fit(X_train,y_train)        

        joblib.dump(trained_model,'churn_model.pkl')

        return trained_model
    except Exception as e:
        logging.error(f"Error in training Model: {e}")
        raise e