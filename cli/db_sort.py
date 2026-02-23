from psycopg2.extensions import connection


def sql_sorted(conn: connection, table_name: str, column: str, order: str = "asc") -> list[tuple]:

    query = f"SELECT * FROM {table_name} ORDER BY {column} {order};"
    with conn.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()

def sql_sorted_int(conn: connection,table_name: str = "bored_table",
        selected_column: str | None = None,order: str | None = None) -> list[tuple] | list[str]:

    if selected_column is None:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name = %s
                ORDER BY ordinal_position
            """, (table_name,))
            return [row[0] for row in cursor.fetchall()]

    if order is None:
        return []

    query = f"SELECT * FROM {table_name} ORDER BY {selected_column} {order};"

    with conn.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()

def input_sorted(conn: connection) -> None:

    columns = sql_sorted_int(conn)

    print("\nchoose column:")
    for i, col in enumerate(columns, 1):
        print(i, col)

    try:
        choice = int(input("number: "))
        selected = columns[choice - 1]
    except (ValueError, IndexError):
        print("invalid choice")
        return

    order = input("order asc/desc: ").strip().lower()
    if order not in ("asc", "desc"):
        order = "asc"

    rows = sql_sorted_int(conn, selected_column=selected, order=order)

    print("\nresult:")
    for row in rows:
        print(row)
