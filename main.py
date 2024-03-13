from customer_churn import logger
from customer_churn.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
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
