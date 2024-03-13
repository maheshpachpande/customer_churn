import pandas as pd
import sys
from box.exceptions import BoxValueError
from customer_churn.utils.common_utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path='artifacts/model_trainer/model.pkl'
            preprocessor_path='artifacts/data_transformation/preprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise e

class CustomData:
    def __init__(self,
                SeniorCitizen: str,
                MonthlyCharges: float,
                TotalCharges: float,
                gender: str,
                Partner: str,
                Dependents: str,
                PhoneService: str,
                MultipleLines: str,
                OnlineSecurity: str,
                DeviceProtection: str,
                TechSupport: str,
                StreamingTV: str,
                StreamingMovies: str,
                Contract: str,
                PaperlessBilling: str,
                PaymentMethod: str,
                TenureMonths: int,
                City: str,
                InternetService: str,
                OnlineBackup: str,
                ChurnScore: int,
                CLTV: int                
                ):
        
        self.SeniorCitizen =  SeniorCitizen
        self.MonthlyCharges = MonthlyCharges
        self.TotalCharges = TotalCharges
        self.gender = gender
        self.Partner = Partner
        self.Dependents = Dependents
        self.PhoneService = PhoneService
        self.MultipleLines = MultipleLines
        self.OnlineSecurity = OnlineSecurity
        self.DeviceProtection = DeviceProtection
        self.TechSupport = TechSupport
        self.StreamingTV = StreamingTV
        self.StreamingMovies = StreamingMovies
        self.Contract = Contract
        self.PaperlessBilling = PaperlessBilling
        self.PaymentMethod = PaymentMethod
        self.TenureMonths = TenureMonths
        self.City = City
        self.InternetService = InternetService
        self.OnlineBackup = OnlineBackup
        self.ChurnScore = ChurnScore
        self.CLTV = CLTV


    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                    'Senior Citizen':[self.SeniorCitizen],
                    'Monthly Charges':[self.MonthlyCharges],
                    'Total Charges':[self.TotalCharges],
                    'Gender':[self.gender],
                    'Partner':[self.Partner],
                    'Dependents' :[self.Dependents],
                    'Phone Service' :[self.PhoneService],
                    'Multiple Lines':[self.MultipleLines],
                    'Online Security':[self.OnlineSecurity],
                    'Device Protection':[self.DeviceProtection],
                    'Tech Support':[self.TechSupport],
                    'Streaming TV':[self.StreamingTV],
                    'Streaming Movies':[self.StreamingMovies],
                    'Contract':[self.Contract],
                    'Paperless Billing':[self.PaperlessBilling],
                    'Payment Method':[self.PaymentMethod],
                    'Tenure Months':[self.TenureMonths],
                    'City':[self.City],
                    'Internet Service':[self.InternetService],
                    'Online Backup':[self.OnlineBackup],
                    'Churn Score':[self.ChurnScore],
                    'CLTV':[self.CLTV]
                    }
            
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise e