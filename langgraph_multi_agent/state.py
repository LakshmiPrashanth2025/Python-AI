from typing import TypedDict, List


class ResearchState(TypedDict):
    query: str

    web_results: List[str]
    db_results: List[str]
    pdf_results: List[str]

    combined_result: str
