
from customer_churn.config.configuration import ConfigurationManager
from customer_churn.components.data_transformation import DataTransformation
from customer_churn import logger
from box.exceptions import BoxValueError


STAGE_NAME = "Data Transformation Stage"

class DatatransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()   
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation("artifacts/data_ingestion/train.csv","artifacts/data_ingestion/test.csv")



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