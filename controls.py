def control(choice : str, current_page : str, total_pages : str):

    choice = choice.strip().lower()

    if choice == "n" and current_page < total_pages:
        return current_page + 1

    elif choice == "p" and current_page > 1:
        return current_page - 1

    elif choice == "q":
        return None

    else:
        print("Wrong input!")

        return current_page