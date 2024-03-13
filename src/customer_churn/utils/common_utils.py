import os
import sys
import dill
import json
import yaml
import joblib
import mysql.connector
from box import ConfigBox
from pathlib import Path
from typing import Any
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from customer_churn import logger
import pandas as pd
import numpy as np
import pymysql
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV
from dotenv import load_dotenv





load_dotenv()

host=os.getenv("host")
port=os.getenv("port")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')




def read_sql_data():
    logger.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            db=db
        )
        logger.info("Connection Established")
        df=pd.read_sql_query('Select * from churn',mydb)
        print(df.head())

        return df

    except BoxValueError:
        raise ValueError("error from read sql query")
    except Exception as e:
        raise e



    

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    
    except BoxValueError:
        raise ValueError("Error occured at save object")
    except Exception as e:
        raise e
    



def evaluate_model(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            param=param[list(models.keys())[i]]

            gs = GridSearchCV(estimator=model, param_grid=param, cv=5, n_jobs=-1)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)

            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            y_pred = y_pred.round()

            test_model_accuracy_score=accuracy_score(y_test, y_pred)
            # test_model_classification_report=classification_report(y_test, y_pred)
            # test_model_confusion_matrix=confusion_matrix(y_test, y_pred)
            report[list(models.keys())[i]]=test_model_accuracy_score
            # report[list(models.keys())[i]]=test_model_classification_report
            # report[list(models.keys())[i]]=test_model_confusion_matrix

        return report
    
    except BoxValueError:
        raise ValueError("Error occured at evaluate model")
    except Exception as e:
        raise e
    

    

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except BoxValueError:
        raise ValueError("Error occured at load object")
    except Exception as e:
        raise e
    


def eval_metrics(actual, pred):
        accuracy = accuracy_score(actual, pred)
        class_report = classification_report(actual, pred)
        confusionmatrix = confusion_matrix(actual, pred)
        return accuracy, class_report, confusionmatrix



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")





@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")