from psycopg2.extensions import connection


def get_table_columns(conn : connection, table_name: str) -> list[str]:

    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = %s
            ORDER BY ordinal_position
        """, (table_name,))
        columns = [row[0] for row in cursor.fetchall()]
        return columns
