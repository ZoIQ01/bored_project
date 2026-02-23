from psycopg2.extensions import connection


def get_random_idea(conn : connection, table_name: str = "bored_table") -> dict | None:

    with conn.cursor() as cursor:
        cursor.execute(f"""
            SELECT id, activity, type, participants, price, accessibility, link
            FROM {table_name}
            ORDER BY RANDOM()
            LIMIT 1;
        """)
        row = cursor.fetchone()

    if not row:
        return None

    return {
        "id": row[0],
        "activity": row[1],
        "type": row[2],
        "participants": row[3],
        "price": row[4],
        "accessibility": row[5],
        "link": row[6]
    }
