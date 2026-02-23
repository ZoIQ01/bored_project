from contextlib import contextmanager
from psycopg2.extensions import connection

@contextmanager
def get_cursor(conn : connection):

    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        cursor.close()
