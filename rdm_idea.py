import pandas as pd

def random_idea(df):
    if isinstance(df, list):
        df = pd.DataFrame(df)
    idea = df.sample(1).iloc[0].to_dict()
    print("\nRandom Idea")
    print(f"id: {idea.get('id', '')} | activity: {idea.get('activity', '')} | type: {idea.get('type', '')} | "
          f"participants: {idea.get('participants', '')} | link: {idea.get('link', '')}")
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

    print(f"price: {price} | accessibility: {accessibility}")

