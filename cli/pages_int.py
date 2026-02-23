def interactive_all_ideas(ideas: list, per_page: int = 10):

    if not ideas:
        print("no ideas to show!")
        return

    columns = ["id", "activity", "type", "participants", "price", "accessibility", "link"]
    total_pages = (len(ideas) + per_page - 1) // per_page
    page = 1

    while True:
        start = (page - 1) * per_page
        end = start + per_page
        print(f"\npage {page}/{total_pages} (show ideas {start + 1}-{min(end, len(ideas))})\n")

        for idea in ideas[start:end]:
            idea_dict = dict(zip(columns, idea)) if isinstance(idea, tuple) else idea
            print(
                f"id={idea_dict['id']}, activity={idea_dict['activity']}, type={idea_dict['type']}, "
                f"participants={idea_dict['participants']}, price={idea_dict['price']}, "
                f"accessibility={idea_dict['accessibility']}, link={idea_dict['link']}"
            )

        cmd = input("\n[n] next page, [p] previous page, [q] exit: ").strip().lower()
        if cmd == "n" and page < total_pages:
            page += 1
        elif cmd == "p" and page > 1:
            page -= 1
        elif cmd == "q":
            break
        else:
            print("wrong input or no page to switch!")
