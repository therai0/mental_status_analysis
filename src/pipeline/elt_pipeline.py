import sys
from src.logger.logger import logging
from src.exception.exception import CustomeException
from src.components.data_ingestion.extract.extract import DataExtraction
from src.components.data_ingestion.load.load import LoadData
from src.components.data_transformation.read_and_save.read_and_save import ReadAndSave
from src.components.data_transformation.transformation.transformation import (
    DataTransformation,
)
from src.components.model_train.model_trian import ModelTrain


class ELT_pipeline:
    def __init__(self):
        pass

    def init_ELT(self):
        try:
            logging.info("Initation of ELT")
            # extract the data from the kagglehub
            self.data_extraction = DataExtraction()
            df = self.data_extraction.init_data_extraction()
            logging.info("Data Extraction completed")

            # loading data to database
            self.load_data = LoadData(df)

            self.load_data.create_table()  # create the table
            self.load_data.insert_data()  # save the data to the database

            logging.info("Initation of data transformation")
            # data transformation initation
            self.read_and_save = ReadAndSave()

            train_path, test_path, raw_path = self.read_and_save.read_and_save()
            logging.info("Return the file path(train,test and raw)")

            logging.info("Data transformation started")

            data_transformation = DataTransformation(train_path, test_path)
            (
                train_arr_path,
                test_arr_path,
                target_train_arr_path,
                target_test_arr_path,
            ) = data_transformation.init_data_transormation()

            return [
                train_arr_path,
                test_arr_path,
                target_train_arr_path,
                target_test_arr_path,
            ]

        except Exception as e:
            raise CustomeException(e, sys)
