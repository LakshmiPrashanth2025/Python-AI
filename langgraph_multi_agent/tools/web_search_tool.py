from duckduckgo_search import DDGS


def search_web(query: str):
    results = []

    with DDGS() as ddgs:
        response = ddgs.text(query, max_results=5)

        for r in response:
            results.append(
                f"Title: {r.get('title')}\n"
                f"Body: {r.get('body')}\n"
                f"Link: {r.get('href')}"
            )

    return results
