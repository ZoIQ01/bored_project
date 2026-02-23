from new_activities import load_activities, add_activities
from check_activities import check_activities
from rdm_idea import random_idea
from sort_idea_panda import panda_sorted
from filter import filter_menu
from api import fetch_activity
import os
import pandas as pd


def print_menu():
    print("\nMain Menu")
    print("1. Add an idea")
    print("2. Check all ideas")
    print("3. Filter ideas")
    print("4. Sort by")
    print("5. Get random idea")
    print("0. Exit")


def load_or_fetch_initial(n: int = 100) -> pd.DataFrame:
    os.makedirs("data", exist_ok=True)
    activities = load_activities()

    new_ideas = []

    if len(activities) < n:
        print("Checking local data..")
        print("Data not enough or missing. Fetching from API..")

        all_ids = set(activities["id"].astype(str))
        attempts = 0

        while len(new_ideas) + len(activities) < n:
            idea = fetch_activity()
            attempts += 1
            if idea and idea["id"] not in all_ids and idea["id"] not in {i["id"] for i in new_ideas}:
                new_ideas.append(idea)
            if attempts > n * 5:
                print("Can't get enough ideas!")
                break

        if new_ideas:
            new_df = pd.DataFrame(new_ideas)
            activities = pd.concat([activities, new_df], ignore_index=True)
            add_activities(new_ideas, activities.to_dict(orient="records"))
            print(f"{len(new_ideas)} ideas fetched and added.")

    print(f"Total activities loaded: {len(activities)}")
    return activities


def add_ideas_from_api(df: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(df) if isinstance(df, list) else df
    try:
        n = int(input("How many ideas to fetch from API? "))
        if n <= 0:
            print("Number must be greater than 0.")
            return df
    except ValueError:
        print("Invalid number.")
        return df

    new_ideas = []
    attempts = 0
    all_ids = set(df["id"].astype(str))

    while len(new_ideas) < n:
        idea = fetch_activity()
        attempts += 1
        if idea and idea["id"] not in all_ids and idea["id"] not in {i["id"] for i in new_ideas}:
            new_ideas.append(idea)
        if attempts > n * 5:
            print("Can't get enough unique ideas!")
            break

    if new_ideas:
        new_df = pd.DataFrame(new_ideas)
        df = pd.concat([df, new_df], ignore_index=True)
        add_activities(new_ideas, df.to_dict(orient="records"))
        print(f"{len(new_ideas)} ideas fetched and added.")
    else:
        print("No new ideas were added.")

    return df


def main():
    all_activities = load_or_fetch_initial(n=100)
    activities_list = all_activities.copy()

    while True:
        print_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            activities_list = add_ideas_from_api(all_activities)
            activities_list = all_activities.copy()
        elif choice == "2":
            check_activities(activities_list)
        elif choice == "3":
            activities_list = filter_menu(all_activities)
        elif choice == "4":
            activities_list = panda_sorted(activities_list)
        elif choice == "5":
            random_idea(activities_list)
        elif choice == "0":
            print("Good bye!")
            break
        else:
            print("Wrong input!")



if __name__ == "__main__":
    main()
