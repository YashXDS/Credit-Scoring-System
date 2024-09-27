# src/model_deployment.py
import joblib
import pandas as pd
from flask import Flask, request, jsonify
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the model
model = joblib.load('credit_scoring_model.pkl')

# Initialize the scaler (make sure to use the same parameters as during training)
scaler = StandardScaler()

@app.route('/predict', methods=['POST'])
def predict():
    """Predict credit score based on input features."""
    data = request.json
    input_features = pd.DataFrame(data, index=[0])
    
    # Preprocess the input features (same steps as during training)
    input_features_scaled = scaler.fit_transform(input_features)  # Scale the features

    # Make prediction
    prediction = model.predict(input_features_scaled)
    
    return jsonify({'prediction': prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)