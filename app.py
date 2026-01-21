from flask import Flask, render_template, request
from textblob import TextBlob
from wordcloud import WordCloud
import io, base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    wordcloud_img = None

    if request.method == 'POST':
        text = request.form['text']
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        keywords = list(set(blob.words))

        result = {
            'sentiment': sentiment,
            'subjectivity': subjectivity,
            'keywords': keywords
        }

        # Generate word cloud
        wc = WordCloud(width=800, height=400, background_color='white').generate(' '.join(keywords))
        img = io.BytesIO()
        wc.to_image().save(img, format='PNG')
        img.seek(0)
        wordcloud_img = base64.b64encode(img.getvalue()).decode()

    return render_template('index.html', result=result, wordcloud_img=wordcloud_img)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
