import sys
import pandas as pd
from src.components.data_ingestion.load.database import create_connection
from src.exception.exception import CustomeException
from src.constant.elt_constant import DATABASE_NAME,HOST,USER,PASSWORD,TABLE_NAME
from src.utils.elt_utils import save_to_csv
from src.entity.config_entity import ConfigCSVFile
from src.logger.logger import logging

from sklearn.model_selection import train_test_split


class ReadAndSave:
     # """
        # Read the data from the database
        # Save to the CSV file 
        # return train , test file path and raw file path
    # """
    
    def __init__(self):
        self.connection = create_connection(
            HOST,
            USER,
            PASSWORD,
            DATABASE_NAME
        )
        self.config_csv_file = ConfigCSVFile()


    def split_train_test(self, data: pd.DataFrame):
        try:
            train, test = train_test_split(
                data,
                test_size=self.config_csv_file.train_test_ratio,
                random_state=42,
            )
            return train, test
        except Exception as e:
            raise CustomeException(e, sys)


    def read_and_save(self)->pd.DataFrame:
       
        try:
            logging.info("Data laoding initiated")
            query = f"""
            SELECT * FROM {TABLE_NAME}
            """
            df = pd.read_sql(query,self.connection)
            
            logging.info("Data load completed")

            # saving raw data
            save_to_csv(df,self.config_csv_file.raw_file_path)
            logging.info("Data save to raw.csv file completed")

            train,test = self.split_train_test(df)

            # now save the both train and test data 
            save_to_csv(train,self.config_csv_file.train_file_path)
            save_to_csv(test,self.config_csv_file.test_file_path)

            return [
                self.config_csv_file.train_file_path,
                self.config_csv_file.test_file_path,
                self.config_csv_file.raw_file_path
            ]

        except Exception as e:
            raise CustomeException(e, sys)
    

