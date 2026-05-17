
from typing import TypedDict
from langgraph.graph import StateGraph, END

class State(TypedDict):
    user_input: str
    processed: str
    final_output: str

def preprocess(state):
    return {"processed": state["user_input"].upper()}

def generate_response(state):
    return {"final_output": f"Processed Response: {state['processed']}"}

graph = StateGraph(State)
graph.add_node("preprocess", preprocess)
graph.add_node("generate_response", generate_response)

graph.set_entry_point("preprocess")
graph.add_edge("preprocess", "generate_response")
graph.add_edge("generate_response", END)

app = graph.compile()

result = app.invoke({"user_input": "hello langgraph"})
print(result)
