from tools.web_search_tool import search_web


def web_search_agent(state):
    query = state["query"]

    results = search_web(query)

    return {
        "web_results": results
    }
