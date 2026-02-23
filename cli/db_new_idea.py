from database import fetch_activity


def add_n_ideas(n: int = 10):

    new_ideas = []
    all_ids = set()
    attempts = 0

    while len(new_ideas) < n:
        idea = fetch_activity()
        attempts += 1
        if not idea:
            continue

        idea_id = str(idea["id"])
        if idea_id not in all_ids and idea_id not in {i["id"] for i in new_ideas}:
            new_ideas.append(idea)

        if attempts > n * 10:
            break

    return new_ideas
