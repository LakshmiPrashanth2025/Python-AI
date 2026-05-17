
from typing import TypedDict
from langgraph.graph import StateGraph, END

class State(TypedDict):
    topic: str
    research: str
    summary: str

def research_agent(state):
    return {
        "research": f"Research collected for {state['topic']}"
    }

def summarizer_agent(state):
    return {
        "summary": f"Summary created from: {state['research']}"
    }

graph = StateGraph(State)

graph.add_node("research_agent", research_agent)
graph.add_node("summarizer_agent", summarizer_agent)

graph.set_entry_point("research_agent")
graph.add_edge("research_agent", "summarizer_agent")
graph.add_edge("summarizer_agent", END)

app = graph.compile()

result = app.invoke({"topic": "Artificial Intelligence"})
print(result)
