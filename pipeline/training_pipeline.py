from steps.ingest_data import ingest_df
from steps.clean_data import clean_df
from steps.model_train import train_model
from steps.evaluation import evaluate_model


def train_pipeline(data_path):
    df = ingest_df(data_path)
    X_train,X_test,y_train,y_test = clean_df(df)
    model = train_model(X_train,X_test,y_train,y_test)
    precision,recall,f1_scr,roc_auc = evaluate_model(model,X_test,y_test)
