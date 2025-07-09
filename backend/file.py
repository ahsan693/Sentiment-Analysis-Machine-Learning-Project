from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Allows requests from React frontend

# Load pre-trained sentiment analysis model 
classifier = pipeline("sentiment-analysis")

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json['text']  # Get review text from frontend
    result = classifier(text)[0]  # Analyze sentiment
    return jsonify(result)  # Send result back to frontend

if __name__ == '__main__':
    app.run(debug=True)   
