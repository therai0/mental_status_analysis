
"""
Here all the constant varaible are ELT pipeline is define
"""

import os 
from dotenv import load_dotenv

load_dotenv()

DATABASE_NAME = os.getenv("database")
HOST = os.getenv("host")
USER = os.getenv("user")
PASSWORD = os.getenv("password")
TABLE_NAME = "mental_status_table"

TARGET_COLUMN = "status"

TRAIN_FILE= "train.csv"
TEST_FILE = "test.csv"
RAW_FILE = "raw.csv"
TRAIN_TEST_RATIO = 0.2 

# saving the train data test dir 
DATA_DIR = "data"
RAW_DATA_DIR = "raw"


# transform data dir
TRANSFORMED_DIR = "transformed"
TRANSFORMED_TRAIN_ARR = "train.npz"
TRANSFORMED_TEST_ARR = "test.npz"
TRANSFORMED_TARGET_FET_TRAIN = "train_target.npy"
TRANSFORMED_TARGET_FET_TEST = "test_target.npy"


# model dir 
FINAL_MODEL = "final_model"

# preprocessor 
PREPROCESSOR_FILE = "preprocessor.pkl"
ML_MODEL_FILE = "model.pkl"












