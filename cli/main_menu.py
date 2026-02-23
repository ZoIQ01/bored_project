from dotenv import load_dotenv
from pathlib import Path
from cli import  add_n_ideas, get_all_ideas, sql_filter, sql_sorted
from database import prepare_ideas_for_insert, get_random_idea, get_table_columns, insert_ideas
from cli.pages_int import interactive_all_ideas
from psycopg2.extensions import connection


dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=dotenv_path)


def print_menu():

    print("\n=== MAIN MENU ===")
    print("1. Add new ideas")
    print("2. Show all ideas")
    print("3. Filter ideas")
    print("4. Sort ideas")
    print("5. Get random idea")
    print("0. Exit")


def main_menu_int(conn : connection):

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                n = int(input("how much ideas would you like to add? "))
                new_ideas = add_n_ideas(n)
                if new_ideas:
                    rows = prepare_ideas_for_insert(new_ideas)
                    insert_ideas(conn, rows)
                    print(f"added {len(new_ideas)} new ideas")
            except ValueError:
                print("enter a number!")


        elif choice == "2":
            ideas = get_all_ideas(conn)
            interactive_all_ideas(ideas)


        elif choice == "3":
            columns = get_table_columns(conn, "bored_table")
            print("\nchoose column:")
            for i, col in enumerate(columns, 1):
                print(i, col)
            choice = int(input("enter number: "))
            selected_column = columns[choice - 1]
            value = input("enter value: ")
            rows = sql_filter(conn, "bored_table", selected_column, value)
            interactive_all_ideas(rows)



        elif choice == "4":
            columns = get_table_columns(conn, "bored_table")
            print("\nchoose column to sort:")
            for i, col in enumerate(columns, 1):
                print(i, col)
            choice = int(input("enter number: "))
            selected_column = columns[choice - 1]
            order = input("asc/desc(asc by default): ").strip().lower()
            if order not in ("asc", "desc"):
                order = "asc"
            rows = sql_sorted(conn, "bored_table", selected_column, order)
            interactive_all_ideas(rows)


        elif choice == "5":
            idea = get_random_idea(conn, table_name="bored_table")
            if idea:
                print(f"\nRandom idea:")
                print(f"id={idea['id']}, activity={idea['activity']}, type={idea['type']}, "
                      f"participants={idea['participants']}, price={idea['price']}, "
                      f"accessibility={idea['accessibility']}, link={idea['link']}")
            else:
                print("no ideas found in database.")

        elif choice == "0":
            print("good bye!")
            break

        else:
            print("wrong input!")

