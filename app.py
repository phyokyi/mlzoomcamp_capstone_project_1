from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

with open('mushroom_predict.pkl', 'rb') as file:
    data = pickle.load(file)
    model = data['model']
    encoder = data['encoder']

@app.route('/')
def hello():
    return 'Hello'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)

    # Extract data from request
    input_data = request.get_json(force=True)
    
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Apply the encoder
    encoded_input = encoder.transform(input_df)

    # Make prediction
    prediction = model.predict(encoded_input)

    if prediction == "p":
        return jsonify("poisonous")
    if prediction == "e":
        return jsonify("edible")
    return jsonify("false")

if __name__ == '__main__':
    app.run(debug=True)