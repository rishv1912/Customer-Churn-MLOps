import logging
from src.evaluation import AccuracyScore,RocAucScore,F1Score,PrecisionScore,RecallScore

def evaluate_model(model,X_test,y_test):
    prediction = model.predict(X_test)
    
    try:
        recall_class = RecallScore()
        recall = recall_class.calculate_score(y_test,prediction)
        
        precision_class = PrecisionScore()
        precision = precision_class.calculate_score(y_test,prediction)

        accuracy_class = AccuracyScore()
        accuracy = accuracy_class.calculate_score(y_test,prediction)

        rocauc_class = RocAucScore()
        rocauc = rocauc_class.calculate_score(y_test,prediction)

        f1score_class = F1Score()
        f1score = f1score_class.calculate_score(y_test,prediction)

        

        return precision,recall,f1score,rocauc

    except Exception as e:
        logging.error(f"Error in evaluation model : {e}")
        raise e


