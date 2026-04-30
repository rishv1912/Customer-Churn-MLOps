import logging
import mlflow
from src.evaluation import AccuracyScore,RocAucScore,F1Score,PrecisionScore,RecallScore


def evaluate_model(model,X_test,y_test):
    """
    evaluate_model, this function takes three arguments model,X_test,y_test
    it returns the merics in order
    
    precision,recall,f1score,rocauc
    """
    
    prediction = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:,1]
    try:
        
        # recal is the most important metric, should be focused on, because it treats FN(Model predicts not churn but customer actually churned) so i need to keep the FN as low as possible results higher recall 
        recall_class = RecallScore()
        recall = recall_class.calculate_score(y_test,prediction)
        
        precision_class = PrecisionScore()
        precision = precision_class.calculate_score(y_test,prediction)

        accuracy_class = AccuracyScore()
        accuracy = accuracy_class.calculate_score(y_test,prediction)

        rocauc_class = RocAucScore()
        rocauc = rocauc_class.calculate_score(y_test,y_prob)

        f1score_class = F1Score()
        f1score = f1score_class.calculate_score(y_test,prediction)
        

        return precision,recall,f1score,rocauc

    except Exception as e:
        logging.error(f"Error in evaluation model : {e}")
        raise e


