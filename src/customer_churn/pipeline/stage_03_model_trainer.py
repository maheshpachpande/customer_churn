
from customer_churn.config.configuration import ConfigurationManager
from customer_churn.components.model_trainer import ModelTrainer
from customer_churn import logger
from box.exceptions import BoxValueError
import pandas as pd
import numpy as np


STAGE_NAME = "Data Transformation Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        train_ar = pd.read_csv('artifacts/data_transformation/train.csv')
        train_arr = np.array(train_ar)

        test_ar = pd.read_csv('artifacts/data_transformation/test.csv')
        test_arr = np.array(test_ar)

        config = ConfigurationManager()   
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.initiate_model_trainer(train_arr, test_arr)



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except BoxValueError:
            raise ValueError("Error occured in Data Ingestion...............")
    except Exception as e:
            raise e