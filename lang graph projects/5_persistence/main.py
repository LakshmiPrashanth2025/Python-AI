
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver

class State(TypedDict):
    messages: list

def chatbot(state):
    last_message = state["messages"][-1]
    response = f"Bot Reply: {last_message}"
    return {"messages": state["messages"] + [response]}

memory = SqliteSaver.from_conn_string("chat_memory.db")

graph = StateGraph(State)
graph.add_node("chatbot", chatbot)

graph.set_entry_point("chatbot")
graph.add_edge("chatbot", END)

app = graph.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "user1"}}

result = app.invoke(
    {"messages": ["Hello"]},
    config=config
)

print(result)
