from flask import Flask, render_template, request, jsonify
import nltk
from textblob import TextBlob
import os

# Download TextBlob NLTK dependencies at startup
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

app = Flask(__name__)

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Analyze route
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # TextBlob sentiment analysis
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    keywords = list(set(blob.words))[:15]  # Limit keywords

    if sentiment > 0:
        label = "Positive"
    elif sentiment < 0:
        label = "Negative"
    else:
        label = "Neutral"

    return jsonify({
        "label": label,
        "sentiment": round(sentiment, 2),
        "subjectivity": round(subjectivity, 2),
        "keywords": keywords
    })
# Run on Render port
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)