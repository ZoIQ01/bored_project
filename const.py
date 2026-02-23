import os
from dotenv import load_dotenv
from pathlib import Path

URL = "https://bored-api.appbrewery.com/random"
FIELDNAMES = ["id", "activity", "type", "participants", "price", "accessibility", "link"]
PAGE_SIZE = 10

dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

DB_NAME=os.environ["DB_NAME"]
DB_HOST=os.environ["DB_HOST"]
DB_USER=os.environ["DB_USER"]
DB_PASS=os.environ["DB_PASS"]
DB_PORT=os.environ["DB_PORT"]


ALLOWED_COLUMNS = ["id", "name", "type", "priority", "date"]