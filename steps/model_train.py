import joblib
import logging

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
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

        param_grid_rf = {
            'n_estimators':[100,200,300],
            'max_depth':[10,20,20,None],
            'min_samples_split':[2,5,10],
            'min_samples_leaf':[1,2,4],
            'max_features':['sqrt','log2']
        }
        
        param_grid_dt = {
            "criterion": ["gini", "entropy", "log_loss"],   # how to measure split quality
            "max_depth": [None,3, 5,7, 10, 20],                 # maximum depth of tree
            "min_samples_split": [2, 5, 10,20],                # min samples needed to split a node
            "min_samples_leaf": [1, 2, 5,10],                  # min samples required in each leaf
            "max_features": [None, "sqrt", "log2"],         # number of features to consider for best split
            "splitter": ["best", "random"]  
        }

        grid_search = GridSearchCV(
            estimator=clf,
            param_grid=param_grid_dt,
            scoring='f1',
            n_jobs=7,
            cv=5,
        )

        trained_model = grid_search.fit(X_train,y_train)
        # trained_model = clf.fit(X_train,y_train)
        # trained_model = RandomForestsModel
        best_params = grid_search.best_params_


        joblib.dump(trained_model,'churn_model.pkl')

        return trained_model, best_params
    
    except Exception as e:
        logging.error(f"Error in training Model: {e}")
        raise e