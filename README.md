# Smart Text Analyzer (Python NLP Web App)

Smart Text Analyzer is a Python-based Natural Language Processing (NLP) web application that performs real-time sentiment analysis on user input text.

## Project Overview

This project allows users to enter any English text and receive:

- Sentiment polarity score (Positive / Negative / Neutral)
- Subjectivity analysis
- Keyword extraction
- Instant results through a web interface

The backend logic is implemented entirely in Python using Flask and TextBlob.

## Technologies Used

Backend (Python):
- Python 3
- Flask
- TextBlob

Frontend:
- HTML
- CSS
- JavaScript
- Bootstrap

## How It Works

1. User enters text on the web interface  
2. JavaScript sends the input to the Flask backend  
3. Python processes the text using TextBlob NLP methods  
4. Results are returned and displayed instantly on the webpage  

## Installation & Running Locally

1. Clone the repository:

git clone https://github.com/patilvishanavi-nlp/Smart-Text-Analyzer-

2. Install required Python packages:

pip install -r requirements.txt

3. Run the application:

python app.py

4. Open browser and visit:

http://localhost:3000

## Live Demo

Hosted on Replit : https://smart-text-analyzer-1.patilvishanavi.repl.co
