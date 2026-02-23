from dotenv import load_dotenv
from cli.main_menu import main_menu_int
from database import did_table_exist, connect_to_db, load_or_fetch, prepare_ideas_for_insert



def main():

    load_dotenv()

    did_table_exist()

    conn = connect_to_db()
    print("connected to database")

    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM bored_table;")
        count = cursor.fetchone()[0]

    if count == 0:
        print("list is empty! load data..")
        ideas = load_or_fetch(100)
        prepare_ideas_for_insert(ideas)
        print("data have been load successfully")

    main_menu_int(conn)

if __name__ == "__main__":
    main()
