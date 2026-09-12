import sqlite3

connection = sqlite3.connect("price_tracker.db")
connection.execute(
    "INSERT INTO products (name, platform, store, url) VALUES (?, ?, ?, ?)",
    ("اکانت Resident Evil Requiem", "PS5", "game-center", "https://game-center.ir/product/resident-evil-requiem/")
)

connection.commit()
connection.close()
print("Product added successfully")