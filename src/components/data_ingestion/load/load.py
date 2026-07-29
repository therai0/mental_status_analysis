import sys
import pandas as pd
from src.exception.exception import CustomeException
from src.logger.logger import logging
from src.components.data_ingestion.load.database import create_connection
from src.constant.elt_constant import DATABASE_NAME, USER, HOST, PASSWORD, TABLE_NAME


class LoadData:
    # """
    # create the table
    # save the data to the database
    # """

    def __init__(self, data: pd.DataFrame):
        self.data = data.replace({float("nan"): None})
        self.connection = create_connection(
            HOST,
            USER,
            PASSWORD,
            DATABASE_NAME,
        )
        self.cursor = self.connection.cursor()

    def create_table(self):
        try:

            # query to create the table
            table_creation_query = f"""
              CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INT PRIMARY KEY,
                statement TEXT,
                status VARCHAR(255),
                loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );"""

            self.cursor.execute(table_creation_query)
            self.connection.commit()
            logging.info("Table created successfully")
        except Exception as e:
            raise CustomeException(e, sys)

    def insert_data(self):
        try:
            insert_query = f"""
            INSERT INTO {TABLE_NAME} (
                id,
                statement,
                status
            )
            VALUES (
                %s,%s, %s)
            """
            columns = self.data.columns

            data = list(self.data[columns].itertuples(index=False, name=None))

            batch_size = 1000
            for i in range(0, len(data), batch_size):
                batch = data[i : i + batch_size]
                self.cursor.executemany(insert_query, batch)
                self.connection.commit()
            self.connection.close()
            logging.info("Insert data scussesfully")
        except Exception as e:
            raise CustomeException(e, sys)
