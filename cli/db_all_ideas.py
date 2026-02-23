from psycopg2.extensions import connection


def get_all_ideas(conn: connection):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM bored_table")
        return cursor.fetchall()
