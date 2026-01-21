# analyzer.py
from textblob import TextBlob

def analyze_text(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    print("Text:", text)
    print("Sentiment Score:", sentiment)
    print("Subjectivity Score:", subjectivity)
    
    keywords = list(set(blob.words))
    print("Keywords:", keywords)

if __name__ == "__main__":
    with open("sample_input.txt", "r") as f:
        text = f.read()
    analyze_text(text)
