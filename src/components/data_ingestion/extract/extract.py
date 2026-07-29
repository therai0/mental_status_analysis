"""
extract the data from the kagglehub
"""

import sys
import kagglehub
import pandas as pd
from kagglehub import KaggleDatasetAdapter


from src.exception.exception import CustomeException
from src.logger.logger import logging


class DataExtraction:
    def __ini__(self):
        pass

    def init_data_extraction(self) -> pd.DataFrame:
        try:
            logging.info("Initiation of data extraction")
            df = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            "footsurebead/mental-status",
            "cleanData.csv",)

            logging.info("completion of data extraction")
            return df
        except Exception as e:
            raise CustomeException(e, sys)
