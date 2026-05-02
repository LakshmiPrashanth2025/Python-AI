import os
import requests
from crewai.tools import BaseTool
from dotenv import load_dotenv

load_dotenv()

class SerperAINewsTool(BaseTool):
    name = "Real-Time AI News Search"
    description = "Fetch latest AI news articles from Google via Serper API"

    def _run(self, query: str = "latest artificial intelligence news"):
        url = "https://google.serper.dev/news"

        payload = {
            "q": query,
            "hl": "en",
            "gl": "us",
            "num": 8,
            "time": "24h"
        }

        headers = {
            "X-API-KEY": os.getenv("SERPER_API_KEY"),
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code != 200:
            return f"Error fetching news: {response.text}"

        data = response.json()

        articles = []
        for item in data.get("news", []):
            articles.append(
                f"Title: {item.get('title')}\n"
                f"Source: {item.get('source')}\n"
                f"Summary: {item.get('snippet')}\n"
                f"Link: {item.get('link')}\n"
            )

        return "\n\n".join(articles)
