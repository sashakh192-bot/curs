from decimal import Decimal
from typing import Any, Dict, List, Optional

from .config import CONSOLE_WIDTH


def print_header(title: str) -> None:
    print("\n" + "=" * CONSOLE_WIDTH)
    print(f"{title.upper():^{CONSOLE_WIDTH}}")
    print("=" * CONSOLE_WIDTH)


def _fmt_value(v: Any) -> str:
    if isinstance(v, Decimal):
        # psycopg2 часто возвращает Decimal для NUMERIC
        return f"{v:.2f}"
    return str(v)


def print_rows(rows: List[Dict[str, Any]], limit: Optional[int] = None) -> None:
    """
    Печатает список словарей как строки "key: value | key2: value2".
    Без зависимости от табличных библиотек (чтобы проще проверять преподавателю).
    """
    if not rows:
        print("(нет данных)")
        return

    if limit is not None:
        rows = rows[:limit]

    for r in rows:
        line = " | ".join(f"{k}: {_fmt_value(r[k])}" for k in r.keys())
        print(line)


def safe_int(v: Any, default: int = 0) -> int:
    try:
        return int(v)
    except Exception:
        return default
