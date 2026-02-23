import pandas as pd
from typing import List

def sort_activities(
    activities: List[dict],
    column: str,
    ascending: bool = True
) -> List[dict]:
    df = pd.DataFrame(activities)
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist")
    df.sort_values(by=column, ascending=ascending, inplace=True, ignore_index=True)
    return df.to_dict(orient="records")

def panda_sorted(activities: List[dict]) -> List[dict]:
    df = pd.DataFrame(activities)
    print("\nChoose column to sort:")
    for i, col in enumerate(df.columns, start=1):
        print(f"{i}. {col}")
    try:
        choice = int(input("Choose a number: "))
        column = df.columns[choice - 1]
    except (ValueError, IndexError):
        print("Invalid input!")
        return activities

    order = input("Sort by ascending? (yes/no): ").strip().lower()
    ascending = order == "yes"

    sorted_activities = sort_activities(activities, column, ascending)
    print(f"\nSorted by '{column}', ascending={ascending}")
    print(pd.DataFrame(sorted_activities))
    return sorted_activities