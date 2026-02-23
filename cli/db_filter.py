from psycopg2.extensions import connection
from typing import Any


def sql_filter(conn: connection, table_name: str,
               column: str, value: Any) -> list[tuple]:
    query = f"SELECT * FROM {table_name} WHERE {column} = %s;"
    with conn.cursor() as cursor:
        cursor.execute(query, (value,))
        return cursor.fetchall()


def sql_filter_int(conn: connection, table_name: str = "bored_table",
                   selected_column: str | None = None,
                   filter_value: str | int | float | None = None) -> list[tuple] | list[str]:

    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = %s
        """, (table_name,))
        columns = [row[0] for row in cursor.fetchall()]

    if not columns:
        return []

    if selected_column is None:
        return columns

    if filter_value is None:
        return []

    return sql_filter(conn, table_name, selected_column, filter_value)


def input_filter(conn: connection) -> None:

    columns = sql_filter_int(conn)
    print("\nchoose column:")
    for i, col in enumerate(columns, 1):
        print(i, col)
    try:
        choice = int(input("number: "))
        selected = columns[choice - 1]
    except (ValueError, IndexError):
        print("invalid choice")
        return
    value = input("value: ")
    if selected == "id":
        try:
            value = int(value)
        except ValueError:
            print("id must be an integer!")
            return
    rows = sql_filter_int(conn, selected_column=selected, filter_value=value)

    print(rows)
