from unittest.mock import MagicMock
from database.db_rdm_idea import get_random_idea
from cli.db_filter import sql_filter
from cli.db_sort import sql_sorted

#Тесты сделаны полностью чатом ГПТ ;)

def test_get_random_idea():
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (
        1, "Read a book", "education", 1, 0.0, 0.0, ""
    )

    mock_conn = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

    idea = get_random_idea(mock_conn)

    assert isinstance(idea, dict)
    assert idea["activity"] == "Read a book"


def test_sql_filter_patch():
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        (1, "a"), (2, "b"), (2, "d")
    ]

    mock_conn = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

    rows = sql_filter(mock_conn, "bored_table", "id", 2)

    assert rows == [(1, "a"), (2, "b"), (2, "d")]


def test_sql_sorted_patch():
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        (3,), (1,), (2,)
    ]

    mock_conn = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

    rows = sql_sorted(mock_conn, "bored_table", "id")

    assert isinstance(rows, list)
    assert all(isinstance(row, tuple) for row in rows)

    values = [r[0] for r in rows]
    assert values == [3, 1, 2]
