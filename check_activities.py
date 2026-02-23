from const import PAGE_SIZE
import pandas as pd

def check_activities(activities):
    if not isinstance(activities, pd.DataFrame):
        df = pd.DataFrame(activities)
    else:
        df = activities

    if df.empty:
        print("No activities available!")
        return

    total_pages = (len(df) + PAGE_SIZE - 1) // PAGE_SIZE
    current_page = 0

    while True:
        start = current_page * PAGE_SIZE
        end = start + PAGE_SIZE
        page_df = df.iloc[start:end]

        print(f"\n--- Page {current_page + 1}/{total_pages} ---")

        for _, idea in page_df.iterrows():
            price = idea.get('price', 0)
            accessibility = idea.get('accessibility', 0)

            try:
                price = f"{float(price):.2f}"
            except (ValueError, TypeError):
                price = str(price)
            try:
                accessibility = f"{float(accessibility):.2f}"
            except (ValueError, TypeError):
                accessibility = str(accessibility)

            print(f"id: {idea.get('id', '')} | activity: {idea.get('activity', '')} | type: {idea.get('type', '')} | "
                  f"participants: {idea.get('participants', '')} | price: {price} | accessibility: {accessibility} | link: {idea.get('link', '')}")

        print("\n[n] next page, [p] prev page, [q] quit")
        cmd = input("Command: ").strip().lower()

        if cmd == "n" and current_page < total_pages - 1:
            current_page += 1
        elif cmd == "p" and current_page > 0:
            current_page -= 1
        elif cmd == "q":
            break
        else:
            print("Invalid command!")
