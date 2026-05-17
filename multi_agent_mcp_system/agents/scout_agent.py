
import requests

class ScoutAgent:

    def aggregate_signals(self, topic, stock_symbol):

        news = requests.get(
            f"http://localhost:8004/news/{topic}"
        ).json()

        finance = requests.get(
            f"http://localhost:8003/stock/{stock_symbol}"
        ).json()

        return {
            "news": news,
            "finance": finance
        }
