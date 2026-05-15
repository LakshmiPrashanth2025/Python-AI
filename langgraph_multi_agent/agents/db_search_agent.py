from tools.db_tool import search_database


def db_search_agent(state):
    query = state["query"]

    results = search_database(query)

    return {
        "db_results": results
    }
