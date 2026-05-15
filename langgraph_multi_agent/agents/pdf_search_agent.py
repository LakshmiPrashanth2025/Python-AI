from tools.pdf_tool import search_pdfs


def pdf_search_agent(state):
    query = state["query"]

    results = search_pdfs(query)

    return {
        "pdf_results": results
    }
