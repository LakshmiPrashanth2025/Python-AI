from dotenv import load_dotenv

from graph_builder import research_graph


load_dotenv()


if __name__ == "__main__":

    query = input("Enter research query: ")

    result = research_graph.invoke(
        {
            "query": query,
            "web_results": [],
            "db_results": [],
            "pdf_results": [],
            "combined_result": ""
        }
    )

    print("\n")
    print("=" * 80)
    print("FINAL COMBINED RESULT")
    print("=" * 80)
    print(result["combined_result"])
