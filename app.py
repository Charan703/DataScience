from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from src.Data_Science.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/training', methods=['GET', 'POST'])
def training_page():
    if request.method == 'POST':
        # Validate training parameters
        try:
            alpha = float(request.form['alpha'])
            l1_ratio = float(request.form['l1_ratio'])
            # Store parameters and proceed with training
            os.system("python main.py")
            return render_template('training.html', training_success='Model training completed successfully!', show_form=False)
        except Exception as e:
            print(f'Training error: {e}')
            return render_template('training.html', training_error='Training failed. Please check your input values.', show_form=True)
    return render_template('training.html', show_form=True)

@app.route('/train', methods=['GET'])
def training():
    try:
        os.system("python main.py")
        return render_template('training.html', training_success='Model training completed successfully! You can now make predictions.')
    except Exception as e:
        print(f'Training error: {e}')
        return render_template('training.html', training_error='Training failed. Please check the logs for details.')

@app.route('/predict', methods=['POST','GET'])
def predict_route():
    if request.method == 'POST':
        try:
            # Get the input data from the form
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])
            
            data = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                            chlorides, free_sulfur_dioxide, total_sulfur_dioxide, 
                            density, pH, sulphates, alcohol]])
            
            print(f"Input data: {data}")

            # Create an instance of the PredictionPipeline
            obj = PredictionPipeline()

            # Make predictions using the predict method
            result = obj.predict(data)
            print(f"Prediction result: {result}")

            # Round the result to 2 decimal places
            prediction = round(float(result[0]), 2)

            # Render the result on the HTML page
            return render_template('results.html', prediction=prediction)

        except Exception as e:
            print('The Exception message is: ', e)
            return render_template('index.html', error='Something went wrong. Please check your input values.')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)