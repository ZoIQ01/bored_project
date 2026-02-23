from database.db_connection import connect_to_db


def did_table_exist():

    with connect_to_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
        CREATE TABLE IF NOT EXISTS bored_table (
        id INTEGER PRIMARY KEY NOT NULL,
        activity VARCHAR(255),
        type VARCHAR(50),
        participants INTEGER,
        price NUMERIC(5,2),
        accessibility NUMERIC(5,2),
        link VARCHAR(255)
        );  
        """)
    print("table 'bored_table' have been created")
