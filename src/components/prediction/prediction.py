import re
import sys
from src.exception.exception import CustomeException
from src.logger.logger import logging
from src.utils.elt_utils import load_object


class Prediction:
    def __init__(self, message, preprocessor_path, model_path):
        self.message = message
        self.preprocessor_path = preprocessor_path
        self.model_path = model_path

    def cleaning_and_preprocessing(self):
        try:
            self.message = self.message.lower()
            self.message = re.sub(r"http\S+|www\S+", "", self.message)
            self.message = re.sub(r"[^a-zA-Z0-9\s]", "", self.message)

            return self.message
        except Exception as e:
            raise CustomeException(e, sys)

    def init_prediction(self):
        try:
            preprocessor = load_object(self.preprocessor_path)
            model = load_object(self.model_path)

            message = self.cleaning_and_preprocessing()
            transformed_message = preprocessor.transform([message])
            predict = model.predict(transformed_message)
           
            labels = {
                    0:"Normal",
                    1:"Personality Disorder",
                    3:"Suicidal",
                    4:"Bipolar",
                    5:"Anxiety",
                    6:"Depression"

            }
            return labels[predict[0]]
        except Exception as e:
            raise CustomeException(e, sys)
