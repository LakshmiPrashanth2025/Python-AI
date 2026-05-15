from langgraph.graph import StateGraph, START, END

from state import ResearchState

from agents.web_search_agent import web_search_agent
from agents.db_search_agent import db_search_agent
from agents.pdf_search_agent import pdf_search_agent
from agents.combine_agent import combine_agent


builder = StateGraph(ResearchState)

builder.add_node("web_search", web_search_agent)
builder.add_node("db_search", db_search_agent)
builder.add_node("pdf_search", pdf_search_agent)
builder.add_node("combine", combine_agent)

builder.add_edge(START, "web_search")
builder.add_edge(START, "db_search")
builder.add_edge(START, "pdf_search")

builder.add_edge("web_search", "combine")
builder.add_edge("db_search", "combine")
builder.add_edge("pdf_search", "combine")

builder.add_edge("combine", END)

research_graph = builder.compile()
