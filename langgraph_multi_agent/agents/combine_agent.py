from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


llm = ChatOpenAI(model="gpt-4o-mini")


def combine_agent(state):
    query = state["query"]

    web_results = "\n\n".join(state.get("web_results", []))
    db_results = "\n\n".join(state.get("db_results", []))
    pdf_results = "\n\n".join(state.get("pdf_results", []))

    prompt = f'''
    You are a research assistant.

    User Query:
    {query}

    WEB RESULTS:
    {web_results}

    DATABASE RESULTS:
    {db_results}

    PDF RESULTS:
    {pdf_results}

    Combine all information into a structured answer.
    Mention important findings.
    Remove duplicate information.
    '''

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    return {
        "combined_result": response.content
    }
