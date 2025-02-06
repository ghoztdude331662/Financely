import requests
import random
from basic_app.sentiment_analysis import predict_sentiment
def getNews(key):
    r = requests.get(f"https://newsapi.org/v2/everything?q={key}&pageSize=12&apiKey=9b23adeb6a634a0ba1f62e76dcbc54de")
    res = r.json()
    news = {}

    if res['status'] == 'ok':
        articles = res['articles']
        num_articles = len(articles)

        # Ensure there are at least 12 articles
        if num_articles >= 12:
            random_news = random.sample(articles, 12)
        else:
            random_news = articles  # Use all available articles if fewer than 12

        for i in range(len(random_news)):
            news[i] = random_news[i]


    return news

def getNewsWithSentiment(key):
    r = requests.get(f"https://newsapi.org/v2/everything?q={key}&pageSize=12&apiKey=9b23adeb6a634a0ba1f62e76dcbc54de")
    res = r.json()
    news = {}

    if res['status'] == 'ok':
        articles = res['articles']
        num_articles = len(articles)

        # Ensure there are at least 12 articles
        if num_articles >= 12:
            random_news = random.sample(articles, 12)
        else:
            random_news = articles  # Use all available articles if fewer than 12

        for i in range(len(random_news)):
            random_news[i]['sentiment'] = predict_sentiment([random_news[i]['description'][:100]])[0]
            news[i] = random_news[i]


    return news

# print(getNews())
