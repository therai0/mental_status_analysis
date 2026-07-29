import sys
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    roc_auc_score,
    confusion_matrix,
)


from src.entity.config_entity import ConfigModelTrainig
from src.exception.exception import CustomeException
from src.utils.elt_utils import load_numpy_array_data, save_object


class ModelTrain:
    def __init__(self, X_train_path, X_test_path, y_train_path, y_test_path):
        self.model_train_config = ConfigModelTrainig()
        self.X_train = X_train_path
        self.X_test = X_test_path
        self.y_train = y_train_path
        self.y_test = y_test_path

    def model_evaluation(self,y_test,y_pred,y_pred_prob):
        try:
            return {
                "accuracy_score":accuracy_score(y_test,y_pred),
                "confusion_metrix":confusion_matrix(y_test,y_pred),
                "classification_report":classification_report(y_test,y_pred),
                "roc_auc_score": roc_auc_score(y_test,y_pred_prob, multi_class="ovr",average="macro", )
            }   
        except Exception as e:
            raise CustomeException(e,sys)

        
    def init_model_traning(self):
        try:
            X_train = load_numpy_array_data(self.X_train)
            X_test = load_numpy_array_data(self.X_test)
            y_train = load_numpy_array_data(self.y_train)
            y_test = load_numpy_array_data(self.y_test)

            model = LogisticRegression()

            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_train_pred_prob = model.predict_proba(X_train)
            y_test_pred = model.predict(X_test)
            y_test_pred_prob = model.predict_proba(X_test)

            train_data_evl = self.model_evaluation(y_train,y_train_pred,y_train_pred_prob)
            test_data_evl = self.model_evaluation(y_test,y_test_pred,y_test_pred_prob)

            save_object(self.model_train_config.ml_model_path,model)
            return [
                train_data_evl,
                test_data_evl
            ]
        except Exception as e:
            raise CustomeException(e, sys)
