import warnings
warnings.simplefilter('ignore')


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from dataclasses import dataclass
from pathlib import Path
from box.exceptions import BoxValueError
from customer_churn import logger
from customer_churn.utils.common_utils import save_object
from customer_churn.entity import DataTransformationConfig




class DataTransformation:
    
    def __init__(self, config: DataTransformationConfig):
        self.config = config


    def get_data_transformer_object(self):

        '''
        This is responcible for data transformation
        '''

        try:

            num_features = ['Tenure Months', 'Monthly Charges', 'Total Charges', 'Churn Score',
       'CLTV']
            
            cat_features = ['City', 'Gender', 'Senior Citizen', 'Partner', 'Dependents',
       'Phone Service', 'Multiple Lines', 'Internet Service',
       'Online Security', 'Online Backup', 'Device Protection', 'Tech Support',
       'Streaming TV', 'Streaming Movies', 'Contract', 'Paperless Billing',
       'Payment Method']
            
            logger.info("Pipeline initiated.....")
            num_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer()),
                    ("scaler", StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("onehot", OneHotEncoder(sparse_output=False, drop="first",dtype=np.int16))
                ]
            )

            logger.info("Pipeline completed.")

            logger.info("columntransformation initiated.....")
            preprocessor = ColumnTransformer(
                [
                    ("Numerical Pipeline", num_pipeline, num_features),
                    ("Categorical Pipeline", cat_pipeline, cat_features)
                ]
            )

            logger.info("columntransformation completed.")

            return preprocessor
        except BoxValueError:
            raise ValueError("Error occured at data tranformation.....")
        except Exception as e:
            raise e
        
        
    def initiate_data_transformation(self, train_set, test_set):
        try:
            train_df = pd.read_csv(train_set)
            test_df = pd.read_csv(test_set)
            logger.info("Read train and test data completed.")

            preprocessor_obj = self.get_data_transformer_object()

            target_column_name = "Churn Value"

            logger.info("separate the independent and dependent columns started")
            
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logger.info("separate the independent and dependent columns completed")

            logger.info("Applying preprocessing object on train and test dataset")

            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]

            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]

            logger.info("Saved preprocessing object.")

            save_object(
                file_path = self.config.preprocessor_path,
                obj = preprocessor_obj
            )

            train_ar = pd.DataFrame(train_arr)
            train_ar.to_csv("artifacts/data_transformation/train.csv", index=False)

            test_ar = pd.DataFrame(test_arr)
            test_ar.to_csv("artifacts/data_transformation/test.csv", index=False)

            return (
                train_arr,
                test_arr,
                self.config.preprocessor_path
            )



        except BoxValueError:
            raise ValueError("Error occured at initiate data transformation.....")
        except Exception as e:
            raise e
