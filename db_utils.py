# db_utils.py
import sqlite3
import pandas as pd

def run_query(sql: str, db_path="example.db"):
    conn = sqlite3.connect(db_path)
    try:
        df = pd.read_sql_query(sql, conn)
        return df
    except Exception as e:
        return str(e)
    finally:
        conn.close()
