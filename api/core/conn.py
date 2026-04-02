import json
import psycopg2
from contextlib import contextmanager


@contextmanager
def postgres_connection(config_path: str):
    with open(config_path) as f:
        config = json.load(f)

    conn = psycopg2.connect(**config)
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()