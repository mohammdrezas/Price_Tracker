import sqlite3
from config import DB_PATH, SCHEMA_PATH

with open(SCHEMA_PATH, encoding="utf-8") as f:
    schema_sql = f.read()

connection = sqlite3.connect(DB_PATH)
connection.executescript(schema_sql)
connection.commit()
connection.close()

print("Database created successfully")