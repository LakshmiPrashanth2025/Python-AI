
from typing import TypedDict
from langgraph.graph import StateGraph, END

class State(TypedDict):
    city: str
    weather: str

def weather_tool(city):
    fake_weather = {
        "bangalore": "24°C Cloudy",
        "mumbai": "30°C Humid"
    }
    return fake_weather.get(city.lower(), "Weather unavailable")

def get_weather(state):
    return {"weather": weather_tool(state["city"])}

graph = StateGraph(State)

graph.add_node("get_weather", get_weather)

graph.set_entry_point("get_weather")
graph.add_edge("get_weather", END)

app = graph.compile()

result = app.invoke({"city": "Bangalore"})
print(result)
