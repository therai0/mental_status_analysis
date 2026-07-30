
import sys 
from src.components.prediction.prediction import Prediction
from src.exception.exception import CustomeException
from src.logger.logger import logging

class PredictionPipeline:
    def __init__(self,message,preprocessor_path,model_path):
        self.preprocessor_path =  preprocessor_path
        self.model_path = model_path
        self.message = message

    def init_prediction(self):
        try:
            prediction_obj = Prediction(self.message,self.preprocessor_path,self.model_path)
            result = prediction_obj.init_prediction() 
            return result
        except Exception as e:
            raise CustomeException(e,sys)