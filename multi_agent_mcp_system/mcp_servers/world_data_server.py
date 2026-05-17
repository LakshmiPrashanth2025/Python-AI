
from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/country/{country}")
def get_country(country: str):

    url = f"https://restcountries.com/v3.1/name/{country}"

    response = requests.get(url)
    data = response.json()[0]

    return {
        "name": data.get("name", {}).get("common"),
        "capital": data.get("capital"),
        "population": data.get("population"),
        "region": data.get("region")
    }
