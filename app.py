from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

# NLP logic
def analyze_text(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    keywords = list(set(blob.words))
    
    if sentiment > 0:
        label = "Positive"
    elif sentiment < 0:
        label = "Negative"
    else:
        label = "Neutral"
        
    return {
        "text": text,
        "sentiment": round(sentiment, 2),
        "subjectivity": round(subjectivity, 2),
        "label": label,
        "keywords": keywords[:15]
    }

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    result = analyze_text(text)
    return jsonify(result)

# Run server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Use 5000 for local/GitHub
