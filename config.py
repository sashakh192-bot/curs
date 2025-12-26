import os

# Настройки подключения к PostgreSQL.
# Преподавателю будет удобно: можно менять через переменные окружения.
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "5432")),
    "dbname": os.getenv("DB_NAME", "SCOOTERBASE"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "password"),
}

# Ширина "красивых" заголовков для консоли (как в примере с лобби)
CONSOLE_WIDTH = int(os.getenv("CONSOLE_WIDTH", "105"))
