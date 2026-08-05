from flask import Flask, jsonify, render_template
import requests
API_KEY = "140544713fb14739a9b10a9a8f4ca9aa"
url = "https://newsapi.org/v2/everything?q=tesla&from=2026-07-05&sortBy=publishedAt&apiKey=140544713fb14739a9b10a9a8f4ca9aa"
app = Flask(__name__)

@app.route('/api/news', methods=['GET'])
def get_news():
    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()
        total_articles = len(news_data['articles'])
        first_article =news_data['articles'][0]
        author = first_article['author']
        title = first_article['title']
        publishedAt = first_article['publishedAt']

        output_data = {"Total Article Count" : total_articles,
                    "Title": title,
                    "Author": author,
                    "Published At": publishedAt}
        return jsonify(output_data)
    else:
        return jsonify({"msg":"Invalid API Key."})

if __name__ == "__main__":
    app.run(debug=True, port=8000)