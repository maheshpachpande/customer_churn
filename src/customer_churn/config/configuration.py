from customer_churn.constants import *
from customer_churn.utils.common_utils import read_yaml, create_directories
from customer_churn.entity import (DataIngestionConfig)



class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            raw_data_path=config.raw_data_path,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path 
        )

        return data_ingestion_config