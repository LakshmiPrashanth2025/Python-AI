
from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

API_KEY = os.getenv("NEWS_API_KEY")

@app.get("/news/{topic}")
def get_news(topic: str):

    url = (
        f"https://newsapi.org/v2/everything?q={topic}"
        f"&apiKey={API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    articles = []

    for article in data.get("articles", [])[:5]:
        articles.append({
            "title": article.get("title"),
            "source": article.get("source", {}).get("name")
        })

    return articles
