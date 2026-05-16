
from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

API_KEY = os.getenv("FINANCE_API_KEY")

@app.get("/stock/{symbol}")
def get_stock(symbol: str):

    url = (
        f"https://finnhub.io/api/v1/quote?symbol={symbol}"
        f"&token={API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    return {
        "symbol": symbol,
        "current_price": data.get("c"),
        "high_price": data.get("h"),
        "low_price": data.get("l"),
        "open_price": data.get("o"),
        "previous_close": data.get("pc")
    }

@app.get("/crypto/{symbol}")
def get_crypto(symbol: str):

    return {
        "symbol": symbol,
        "message": "Extend with Binance/CoinGecko API"
    }
