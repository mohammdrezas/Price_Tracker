import sqlite3

connection = sqlite3.connect("price_tracker.db")
connection.execute(
    "INSERT INTO products (name, platform, store, url) VALUES (?, ?, ?, ?)",
    ("اکانت بازی Tekken 8 Advanced Edition", "PS5", "game-center",
 "https://game-center.ir/product/%d8%a7%da%a9%d8%a7%d9%86%d8%aa-%d8%a8%d8%a7%d8%b2%db%8c-tekken-8-advanced-edition/")
)

connection.commit()
connection.close()
print("Product added successfully")