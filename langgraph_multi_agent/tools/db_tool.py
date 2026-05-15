import sqlite3


def search_database(query: str):
    conn = sqlite3.connect("data/sample.db")
    cursor = conn.cursor()

    sql_query = '''
    SELECT title, content
    FROM documents
    WHERE content LIKE ?
    LIMIT 5
    '''

    cursor.execute(sql_query, (f"%{query}%",))

    rows = cursor.fetchall()

    conn.close()

    return [f"{title}: {content}" for title, content in rows]
