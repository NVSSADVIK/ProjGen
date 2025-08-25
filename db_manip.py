import sqlite3
import datetime

# sqlite connection to db
conn = sqlite3.connect(".history.db", check_same_thread=False)
cur = conn.cursor()

class DBManip:
    def __init__(self):
        # Create a table inside the db if not exists
        self.create_table()

    def create_table(self):
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date DATETIME,
                    prompt TEXT,
                    response TEXT
                    )
                    """)
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS temp_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date DATETIME,
                    prompt TEXT,
                    response TEXT
                    )
                    """)
        conn.commit()
    def insert_message(self, prompt, response):
        cur.execute("INSERT INTO history (date, prompt, response) VALUES (?, ?, ?)", (datetime.datetime.now().isoformat(" "), prompt, response))
        cur.execute("INSERT INTO temp_history (date, prompt, response) VALUES (?, ?, ?)", (datetime.datetime.now().isoformat(" "), prompt, response))
        conn.commit()

    def print_history(self):
        cur.execute("SELECT * FROM history")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        conn.commit()
    def print_temp_history(self):
        cur.execute("SELECT * FROM temp_history")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        conn.commit()

    def clear_history(self):
        cur.execute("DROP TABLE history")
        self.create_table()
        conn.commit()

    def close_conn(self):
        cur.execute("DROP TABLE temp_history")
        cur.close()
        conn.close()
