from psycopg2.extensions import connection


def prepare_ideas_for_insert(ideas: list) -> list[tuple]:

    if not ideas:
        print("no ideas to add!")
        return []

    rows = []
    seen_ids = set()

    for data in ideas:
        try:
            idea_id = int(data.get("id"))
        except (ValueError, TypeError):
            continue

        if idea_id in seen_ids:
            continue
        seen_ids.add(idea_id)

        try:
            price = float(data.get("price", 0.0))
        except (ValueError, TypeError):
            price = 0.0

        try:
            accessibility = float(data.get("accessibility", 0.0))
        except (ValueError, TypeError):
            accessibility = 0.0

        rows.append((
            idea_id,
            data.get("activity"),
            data.get("type"),
            data.get("participants"),
            price,
            accessibility,
            data.get("link")
        ))

    if not rows:
        print("no valid ideas to add!")
        return []

    return rows



def insert_ideas(conn : connection, rows: list[tuple]) -> None:

    with conn.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO bored_table (id, activity, type, participants, price, accessibility, link)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
        """, rows)

    conn.commit()

    print(f"data has been updated by {len(rows)} new ideas")
