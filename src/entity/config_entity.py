
import os 
from src.constant.elt_constant import (DATA_DIR,
                                       TRAIN_FILE,
                                       TEST_FILE,
                                       TRAIN_TEST_RATIO,
                                       RAW_FILE,
                                       RAW_DATA_DIR,
                                       TARGET_COLUMN,
                                        TRANSFORMED_DIR,
                                        TRANSFORMED_TRAIN_ARR,
                                        TRANSFORMED_TEST_ARR,
                                        PREPROCESSOR_FILE,
                                        FINAL_MODEL,
                                        ML_MODEL_FILE,
                                        TRANSFORMED_TARGET_FET_TEST,
                                        TRANSFORMED_TARGET_FET_TRAIN
                                       )


class ConfigCSVFile:
    def __init__(self):
        self.data_dir = DATA_DIR
        self.train_file_path = os.path.join(self.data_dir,RAW_DATA_DIR,TRAIN_FILE)
        self.test_file_path = os.path.join(self.data_dir,RAW_DATA_DIR,TEST_FILE)
        self.raw_file_path = os.path.join(self.data_dir,RAW_DATA_DIR,RAW_FILE)
        self.train_test_ratio = TRAIN_TEST_RATIO
        self.target_column = TARGET_COLUMN



class ConfigDataTransformation:
    def __init__(self):
        self.transformed_dir = os.path.join(DATA_DIR,TRANSFORMED_DIR)
        self.transformed_train_arr = os.path.join(self.transformed_dir,TRANSFORMED_TRAIN_ARR)
        self.transformed_test_arr = os.path.join(self.transformed_dir,TRANSFORMED_TEST_ARR)
        self.transformed_train_target_arr = os.path.join(self.transformed_dir,TRANSFORMED_TARGET_FET_TRAIN)
        self.transformed_test_target_arr = os.path.join(self.transformed_dir,TRANSFORMED_TARGET_FET_TEST)
        self.preprocessor = os.path.join(FINAL_MODEL,PREPROCESSOR_FILE)
        

class ConfigModelTrainig:
    def __init__(self):
        self.ml_model_path = os.path.join(FINAL_MODEL,ML_MODEL_FILE)