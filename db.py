from contextlib import contextmanager
import psycopg2
from psycopg2.extras import RealDictCursor

from .config import DB_CONFIG


@contextmanager
def db_connection():
    """
    Контекстный менеджер для подключения к PostgreSQL.
    Гарантирует закрытие соединения.
    """
    conn = psycopg2.connect(**DB_CONFIG)
    try:
        yield conn
    finally:
        conn.close()


@contextmanager
def db_cursor(conn):
    """
    Контекстный менеджер для курсора (словарные строки).
    Гарантирует закрытие курсора.
    """
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        yield cur
    finally:
        cur.close()
