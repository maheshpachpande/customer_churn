from customer_churn import logger
from customer_churn.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from customer_churn.pipeline.stage_02_data_transformation import DatatransformationTrainingPipeline
from customer_churn.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from box.exceptions import BoxValueError



STAGE_NAME = "Data Ingestion Stage"


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except BoxValueError:
            raise ValueError("Error occured in Data Ingestion...............")
    except Exception as e:
            raise e


STAGE_NAME = "Data Transformation Stage"



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DatatransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except BoxValueError:
            raise ValueError("Error occured in Data Ingestion...............")
    except Exception as e:
            raise e
    



STAGE_NAME = "Model Training Stage"

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