from flask import Flask, render_template, request
from customer_churn.pipeline.prediction import CustomData, PredictPipeline

application = Flask(__name__)
app=application

@app.route('/')
def index():
    return render_template('index.html')

@ app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            SeniorCitizen=request.form.get('SeniorCitizen'),
            MonthlyCharges=float(request.form.get('MonthlyCharges')),
            TotalCharges=float(request.form.get('TotalCharges')),
            gender=request.form.get('gender'),
            Partner=request.form.get('Partner'),
            Dependents=request.form.get('Dependents'),
            PhoneService=request.form.get('PhoneService'),
            MultipleLines=request.form.get('MultipleLines'),
            OnlineSecurity=request.form.get('OnlineSecurity'),
            DeviceProtection=request.form.get('DeviceProtection'),
            TechSupport=request.form.get('TechSupport'),
            StreamingTV=request.form.get('StreamingTV'),
            StreamingMovies=request.form.get('StreamingMovies'),
            Contract=request.form.get('Contract'),
            PaperlessBilling=request.form.get('PaperlessBilling'),
            PaymentMethod=request.form.get('PaymentMethod'),
            TenureMonths=int(request.form.get('TenureMonths')),
            City=request.form.get('City'),
            InternetService=request.form.get('InternetService'),
            OnlineBackup=request.form.get('OnlineBackup'),
            ChurnScore=int(request.form.get('ChurnScore')),
            CLTV=int(request.form.get('CLTV'))
        )

        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html', results=results)
    
if __name__=="__main__":
    app.run(host='0.0.0.0')