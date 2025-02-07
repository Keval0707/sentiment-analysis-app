from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the model
model_path = "model/sentiment_model.pkl"

if os.path.exists(model_path) and os.path.getsize(model_path) > 0:
    try:
        model = joblib.load(model_path)
        print("✅ Model loaded successfully!")
    except Exception as e:
        raise RuntimeError(f"Error loading model: {e}")
else:
    raise FileNotFoundError(f"Model file is missing or corrupted at {model_path}")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if 'text' not in data:
            return jsonify({'error': "Missing 'text' key in request body"}), 400

        text = data['text']
        prediction = model.predict([text])
        sentiment = 'positive' if prediction[0] == 1 else 'negative'

        return jsonify({'sentiment': sentiment})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)  # Allow connections
