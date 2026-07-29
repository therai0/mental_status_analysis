import sys
import re
import numpy as np 
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from src.logger.logger import logging
from src.exception.exception import CustomeException
from src.constant.elt_constant import TARGET_COLUMN
from src.utils.elt_utils import save_numpy_array_data,save_object
from src.entity.config_entity import ConfigDataTransformation

class DataTransformation:
    def __init__(self, train_path: str, test_path: str):
        self.train_path = train_path
        self.test_path = test_path
        self.config_transformation = ConfigDataTransformation()

    def read_dataset(self, path: str) -> pd.DataFrame:
        try:
            return pd.read_csv(path)
        except Exception as e:
            raise CustomeException(e, sys)


    def get_vectorizer(self):
        try:
            return  TfidfVectorizer(max_features=1000) 
        except Exception as e:
            raise CustomeException(e,sys)
        
        
    def cleaning_data(self,data:pd.DataFrame):
        try:
            data['statement']= data['statement'].str.lower()
            # for train data
            data['statement'] = data['statement'].apply(
                lambda x: re.sub(r'http\S+|www\S+', '', x)
            )
            data['statement'] = data['statement'].apply(
                lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x)
            )
            return data 
        except Exception as e:
            raise CustomeException(e,sys)

        
    def init_data_transormation(self):
        try:
            train_data = self.read_dataset(self.train_path)
            test_data = self.read_dataset(self.test_path)

            X_train_data = train_data.drop([TARGET_COLUMN,"loaded_at","id"], axis=1)
            y_train = train_data[TARGET_COLUMN]
            X_test_data = test_data.drop([TARGET_COLUMN,"loaded_at","id"], axis=1)
            y_test = test_data[TARGET_COLUMN]

            vecotrizer = self.get_vectorizer()

            X_train_cleaned = self.cleaning_data(X_train_data)
            X_test_cleaned = self.cleaning_data(X_test_data)

            X_scaled_train = vecotrizer.fit_transform(X_train_cleaned["statement"])
            X_scaled_test = vecotrizer.transform(X_test_cleaned["statement"])

            save_object(self.config_transformation.preprocessor,vecotrizer)

            # encoding target columns:
            y_train = y_train.map({ 'Anxiety':5,
                'Bipolar':4,
                'Depression':6,
                'Normal':0,
                'Personality disorder':1,
                'Stress':2,
                'Suicidal':3})
            y_test = y_test.map({ 'Anxiety':5,
                'Bipolar':4,
                'Depression':6,
                'Normal':0,
                'Personality disorder':1,
                'Stress':2,
                'Suicidal':3})


            save_numpy_array_data(self.config_transformation.transformed_train_arr,X_scaled_train)
            save_numpy_array_data(self.config_transformation.transformed_test_arr,X_scaled_test)
            save_numpy_array_data(self.config_transformation.transformed_train_target_arr,np.array(y_train))
            save_numpy_array_data(self.config_transformation.transformed_test_target_arr,np.array(y_test))

            return  [
                self.config_transformation.transformed_train_arr,
                self.config_transformation.transformed_test_arr,
                self.config_transformation.transformed_train_target_arr,
                self.config_transformation.transformed_test_target_arr
            ]  
        except Exception as e:
            raise CustomeException(e, sys)
