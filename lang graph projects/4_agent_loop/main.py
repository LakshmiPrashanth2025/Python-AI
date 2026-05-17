
from typing import TypedDict
from langgraph.graph import StateGraph, END

class State(TypedDict):
    question: str
    attempts: int
    answer: str

def think(state):
    attempts = state.get("attempts", 0) + 1
    return {
        "attempts": attempts,
        "answer": f"Attempt {attempts}: refining answer"
    }

def should_continue(state):
    if state["attempts"] >= 3:
        return "end"
    return "retry"

graph = StateGraph(State)

graph.add_node("think", think)

graph.set_entry_point("think")

graph.add_conditional_edges(
    "think",
    should_continue,
    {
        "retry": "think",
        "end": END
    }
)

app = graph.compile()

result = app.invoke({"question": "Explain AI", "attempts": 0})
print(result)
