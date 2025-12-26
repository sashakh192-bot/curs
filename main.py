from typing import Any, Dict, List

from .db import db_connection, db_cursor
from .queries import QUERIES
from .utils import print_header, print_rows


def run_query(cur, title: str, sql: str) -> List[Dict[str, Any]]:
    print_header(title)
    cur.execute(sql)
    rows = cur.fetchall()
    print_rows(rows)
    return rows


def main() -> None:
    try:
        with db_connection() as conn:
            with db_cursor(conn) as cur:
                for title, sql in QUERIES:
                    run_query(cur, title, sql)

        print("\nСоединение с базой данных закрыто.")
    except Exception as e:
        print(f"\nОшибка: {e}")


if __name__ == "__main__":
    main()
