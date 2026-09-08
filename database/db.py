import sqlite3

with open("schema.sql", encoding="utf-8") as f:
    schema_sql = f.read()

connection = sqlite3.connect("price_tracker.db")
connection.executescript(schema_sql)
connection.commit()
connection.close()

print("Database created successfully")