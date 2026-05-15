import sqlite3
from pathlib import Path

Path("data").mkdir(exist_ok=True)

conn = sqlite3.connect("data/sample.db")

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT
)
''')

sample_data = [
    (
        "LangGraph Basics",
        "LangGraph helps create stateful AI workflows using nodes and edges."
    ),
    (
        "Multi-Agent Systems",
        "Multiple AI agents can collaborate to solve complex tasks."
    )
]

cursor.executemany(
    "INSERT INTO documents (title, content) VALUES (?, ?)",
    sample_data
)

conn.commit()
conn.close()

print("Sample database created successfully.")
