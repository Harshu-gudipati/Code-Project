from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle

#loading models
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))
dtr = pickle.load(open('dtr.pkl', 'rb'))

#creating flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        Year = request.form['Year']
        average_rain_fall_mm_per_year = request.form['average_rain_fall_mm_per_year']
        pesticides_tonnes = request.form['pesticides_tonnes']
        avg_temp = request.form['avg_temp']
        Area = request.form['Area']
        Item = request.form['Item']

        features = np.array([[Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item]])

        transformed_features = preprocessor.transform(features)
        predicted_value = dtr.predict(transformed_features)[0]
        return render_template('index.html',predicted_value=predicted_value)


        np.array([[Year]])

#python main
if __name__=='__main__':
    app.run(debug=True)