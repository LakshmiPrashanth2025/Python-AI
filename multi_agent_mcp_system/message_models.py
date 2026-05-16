
import requests

class ContextualistAgent:

    def fetch_context(self, country, city):

        country_data = requests.get(
            f"http://localhost:8001/country/{country}"
        ).json()

        weather_data = requests.get(
            f"http://localhost:8002/weather/{city}"
        ).json()

        return {
            "country": country_data,
            "weather": weather_data
        }
