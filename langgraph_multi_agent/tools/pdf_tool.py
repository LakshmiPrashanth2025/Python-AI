import os
from pypdf import PdfReader


PDF_DIRECTORY = "data/pdfs"


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    return text


def search_pdfs(query: str):
    matches = []

    for file_name in os.listdir(PDF_DIRECTORY):
        if file_name.endswith(".pdf"):
            full_path = os.path.join(PDF_DIRECTORY, file_name)

            text = extract_text_from_pdf(full_path)

            if query.lower() in text.lower():
                snippet = text[:1000]
                matches.append(
                    f"PDF: {file_name}\nSnippet:\n{snippet}"
                )

    return matches
