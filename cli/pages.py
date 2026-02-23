def page(activities:list, page : int = 1, per_page : int =10):

    total_pages = (len(activities) + per_page - 1) // per_page

    if page < 1 or page > total_pages:
        return [], total_pages

    start = (page - 1) * per_page
    end = start + per_page

    return activities[start:end], total_pages
