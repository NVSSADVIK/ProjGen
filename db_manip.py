import sqlite3
import datetime

conn = sqlite3.connect(".history.db")
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
        conn.commit()
    def insert_data(self, prompt, response):
        cur.execute("INSERT INTO history (date, prompt, response) VALUES (?, ?, ?)", (datetime.datetime.now().isoformat(" "), prompt, response))
        conn.commit()

    def print_history(self):
        cur.execute("SELECT * FROM history")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        conn.commit()

    def clear_history(self):
        cur.execute("DROP TABLE history")
        self.create_table()
        conn.commit()


    def close_conn(self):
        cur.close()
        conn.close()
