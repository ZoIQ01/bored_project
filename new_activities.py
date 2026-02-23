import pandas as pd
import os
from const import FILENAME



def load_activities() -> pd.DataFrame:
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILENAME) or os.stat(FILENAME).st_size == 0:
        print("Data haven't been found. File will be created after save.")
        columns = ["id", "activity", "type", "participants", "price", "accessibility", "link"]
        return pd.DataFrame(columns=columns)

    df = pd.read_csv(FILENAME)

    if "participants" in df.columns:
        df["participants"] = pd.to_numeric(df["participants"], errors="coerce").fillna(0).astype(int)

    if "price" in df.columns:
        df["price"] = pd.to_numeric(df["price"], errors="coerce")

    if "accessibility" in df.columns:
        df["accessibility"] = pd.to_numeric(df["accessibility"], errors="coerce")
    return df


def add_activities(new_activities:list[dict], current_activities:list[dict]):
    df_current = pd.DataFrame(current_activities)
    df_new = pd.DataFrame(new_activities)
    combined = pd.concat([df_current, df_new]).drop_duplicates(subset="id", ignore_index=True)
    combined.to_csv(FILENAME, index=False)
    print(f"Total activities: {len(combined)}")
    return combined.to_dict(orient="records")