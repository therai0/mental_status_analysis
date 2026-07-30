import sys 
from src.exception.exception import CustomeException
from src.components.model_train.model_trian import ModelTrain
from src.logger.logger import logging


class TraningPipeline:
    def __init__(self,train_arr_path,test_arr_path,target_train_arr_path,target_test_arr_path):
        self.train_arr_path = train_arr_path
        self.test_arr_path = test_arr_path
        self.target_train_arr_path = target_train_arr_path 
        self.target_test_arr_path = target_test_arr_path 

    def init_model_traning(self):
        try:
            model_traning = ModelTrain(self.train_arr_path,
                                       self.test_arr_path,
                                       self.target_train_arr_path,
                                       self.target_test_arr_path)
            train_evl,test_evl = model_traning.init_model_traning()

            logging.info(train_evl)
            logging.info(test_evl)
        except Exception as e:
            raise CustomeException(e,sys)
