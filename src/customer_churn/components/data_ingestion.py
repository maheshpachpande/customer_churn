import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from box import ConfigBox
from box.exceptions import BoxValueError
from customer_churn import logger
from customer_churn.utils.common_utils import read_sql_data
from customer_churn.entity import (DataIngestionConfig)
from pathlib import Path



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def initiate_data_ingestion(self):
        logger.info("Entered the Data Ingestion")
        try:
            #df = pd.read_csv("notebook/data/EDA.csv")
            df = read_sql_data()
            logger.info("Read the data as DataFrame from MySQL.")


            os.makedirs(os.path.dirname(self.config.raw_data_path), exist_ok=True)

            
            df.to_csv(self.config.raw_data_path, index=False, header=True)
            logger.info("Reading Completed.")

           
            logger.info("train_test_split initiated...............")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.config.train_data_path, index=False, header=True)
            test_set.to_csv(self.config.test_data_path, index=False, header=True)
            logger.info("data ingestion completed.")

            return(
                self.config.train_data_path,
                self.config.test_data_path
            )

        except BoxValueError:
            raise ValueError("Error occured in Data Ingestion...............")
        except Exception as e:
            raise e