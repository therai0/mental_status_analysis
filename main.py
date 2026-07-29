
from src.logger.logger import logging
from src.pipeline.elt_pipeline import ELT_pipeline

if __name__ == "__main__":
    logging.info("initiation of ELT")
    elt_pipeline = ELT_pipeline()

    elt_pipeline.init_ELT()
    logging.info("ELT end")
    