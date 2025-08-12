import joblib
import logging

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from model_dev import RandomForestsModel
from sklearn.model_selection import GridSearchCV
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
        rf = RandomForestClassifier(random_state=42)

        param_grid = {
            'n_estimators':[100,200,300],
            'max_depth':[10,20,20,None],
            'min_samples_split':[2,5,10],
            'min_samples_leaf':[1,2,4],
            'max_features':['sqrt','log2']
        }

        grid_search = GridSearchCV(
            estimator=rf,
            param_grid=param_grid,
            scoring='f1',
            n_jobs=-1,
            cv=5,
            verbose=1,
        )

        trained_model = grid_search.fit(X_train,y_train)
        # trained_model = RandomForestsModel

        best_model = grid_search.best_estimator_


        joblib.dump(best_model,'churn_model.pkl')

        return best_model
    
    except Exception as e:
        logging.error(f"Error in training Model: {e}")
        raise e