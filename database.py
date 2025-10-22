import pymysql
from dotenv import load_dotenv
import os

try:
    load_dotenv("./.env")
except:
    pass

DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_SCHEMA"),
    "charset": "utf8mb4",
    "autocommit": False,
    "cursorclass": pymysql.cursors.DictCursor
}

try:
    connection = pymysql.connect(**DB_CONFIG)
finally:
    connection.close()


def get_db():
    conn = pymysql.connect(**DB_CONFIG)
    try:
        conn.autocommit(False)
        yield conn
        conn.commit()
    except Exception:
        try:
            conn.rollback()
        except Exception:
            pass
        raise
    finally:
        conn.close()