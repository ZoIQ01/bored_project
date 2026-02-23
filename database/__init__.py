from database.api import fetch_activity, fetch_activities
from database.db_check_create import did_table_exist
from database.db_connection import connect_to_db
from database.db_fetch_data import load_or_fetch
from database.db_rdm_idea import get_random_idea
from database.list_to_db import prepare_ideas_for_insert, insert_ideas
from database.get_column import get_table_columns