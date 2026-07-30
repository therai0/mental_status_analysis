
from src.logger.logger import logging
from src.pipeline.elt_pipeline import ELT_pipeline
from src.pipeline.train_pipeline import TraningPipeline
if __name__ == "__main__":
    logging.info("initiation of ELT")
    elt_pipeline = ELT_pipeline()

    train_arr_path,test_arr_path, target_train_arr_path,target_test_arr_path = elt_pipeline.init_ELT()
    logging.info("ELT end")

    logging.info("Initiation of model traning")
    training_pipeline = TraningPipeline(train_arr_path,test_arr_path, target_train_arr_path,target_test_arr_path)
    training_pipeline.init_model_traning()
    logging.info("Model traning complete")
    