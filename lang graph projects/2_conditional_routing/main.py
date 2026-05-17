
from typing import TypedDict
from langgraph.graph import StateGraph, END

class State(TypedDict):
    query: str
    route: str
    response: str

def router(state):
    if "refund" in state["query"].lower():
        return {"route": "billing"}
    return {"route": "general"}

def billing_agent(state):
    return {"response": "Routing to billing support."}

def general_agent(state):
    return {"response": "Routing to general support."}

def decide_route(state):
    return state["route"]

graph = StateGraph(State)

graph.add_node("router", router)
graph.add_node("billing_agent", billing_agent)
graph.add_node("general_agent", general_agent)

graph.set_entry_point("router")

graph.add_conditional_edges(
    "router",
    decide_route,
    {
        "billing": "billing_agent",
        "general": "general_agent"
    }
)

graph.add_edge("billing_agent", END)
graph.add_edge("general_agent", END)

app = graph.compile()

result = app.invoke({"query": "I need a refund"})
print(result)
