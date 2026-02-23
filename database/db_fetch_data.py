from database.api import fetch_activity


def load_or_fetch(n: int = 100):

    print(f"Fetching {n} unique ideas from API...")
    ideas = []
    seen_ids = set()
    attempts = 0

    while len(ideas) < n:
        idea = fetch_activity()
        attempts += 1

        if idea:
            idea_id = str(idea["id"])
            if idea_id not in seen_ids:
                ideas.append(idea)
                seen_ids.add(idea_id)
                print(f"[{len(ideas)}/{n}] Added idea: {idea['activity']}")

        if attempts > n * 10:
            print("too many attempts — API returned too many duplicates.")
            break

    print(f"total fetched: {len(ideas)} ideas.")
    return ideas
