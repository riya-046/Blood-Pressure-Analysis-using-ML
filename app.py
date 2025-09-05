import numpy as np
import pickle
import pandas as pd
from flask import Flask, request, render_template

# Load the saved model
app = Flask(__name__, static_url_path='/Flask/static')
model = pickle.load(open("model.pkl", "rb"))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    Gender = float(request.form['Gender'])
    Age = float(request.form['Age'])
    Patient = float(request.form['Patient'])
    Severity = float(request.form['Severity'])
    BreathShortness = float(request.form['BreathShortness'])
    VisualChanges = float(request.form['VisualChanges'])
    NoseBlending = float(request.form['NoseBlending'])
    WhenDiagnosed = float(request.form['WhenDiagnosed'])
    Systolic = float(request.form['Systolic'])
    Diastolic = float(request.form['Diastolic'])
    ControlledDiet = float(request.form['ControlledDiet'])

    features_values=np.array([[Gender,Age,Patient,Severity,BreathShortness,VisualChanges,
                              NoseBlending,WhenDiagnosed,Systolic,Diastolic,ControlledDiet]])

    #column names = ['Gender','Age','Patient','Severity','BreathShortness','VisualChanges',
    #'NoseBlending','WhenDiagnosed','Systolic','Diastolic','ControlledDiet']

    df = pd.DataFrame(features_values, columns=['Gender','Age','Patient','Severity','BreathShortness','VisualChanges',
                                               'NoseBlending','WhenDiagnosed','Systolic','Diastolic','ControlledDiet'])
    prediction = model.predict(df)
    print(prediction[0])

    if prediction[0] == 0:
        result="NORMAL"
    elif prediction[0] == 1:
        result="HYPERTENSION (Stage-1)"
    elif prediction[0] == 2:
        result="HYPERTENSION (Stage-2)"
    else:
        result="HYPERTENSIVE CRISIS"
    print(result)

    text = "Your Blood Pressure stage is: "


