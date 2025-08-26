# pipeline/data_pipeline.py

import os, sys, csv, json
import pandas as pd
import sqlite3


class DataPipeline:
    def __init__(self, db_path="data.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def init_db(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, email TEXT)"
        )
        self.conn.commit()

    def load_csv(self, file_path: str):
        data = []
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
        return data

    def insert_data(self, rows):
        for row in rows:
            self.cursor.execute(
                f"INSERT INTO users (name, age, email) VALUES ('{row[0]}', {row[1]}, '{row[2]}')"
            )
        self.conn.commit()

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def export_json(self, out_path="output.json"):
        rows = self.fetch_all()
        with open(out_path, "w") as f:
            json.dump(rows, f)

    def close(self):
        self.conn.close()


def run_pipeline():
    pipeline = DataPipeline()
    pipeline.init_db()
    rows = pipeline.load_csv("users.csv")
    pipeline.insert_data(rows)
    print(pipeline.fetch_all())
    pipeline.export_json()
    pipeline.close()


if __name__ == "__main__":
    run_pipeline()
