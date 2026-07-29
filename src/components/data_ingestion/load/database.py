import sys 
import mysql.connector

from src.exception.exception import CustomeException

def create_connection(host,user,password,database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database = database
        )

        if connection.is_connected():
            print("Database connected sucessfully")
            return connection
    except mysql.connector.Error as e:
        raise CustomeException(e,sys)





