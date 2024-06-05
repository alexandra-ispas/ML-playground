from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow import keras
import numpy as np

app = Flask(__name__)

# Load the trained model
model = keras.models.load_model('fraud_detection_model.h5')


# Define the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    predictions = []

    for transaction in data['transactions']:
        # Assuming the transaction data is a list of features
        features = np.array(transaction).reshape(1, -1)
        prediction = model.predict(features)
        predictions.append(float(prediction[0][0]))

    return jsonify(predictions=predictions)


if __name__ == '__main__':
    app.run(port=5000)
