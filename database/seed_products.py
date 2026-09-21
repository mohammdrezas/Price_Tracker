import sqlite3
from config import DB_PATH

products = [
    ("اکانت Resident Evil Requiem", "PS5", "game-center", "https://game-center.ir/product/resident-evil-requiem/"),
    ("اکانت بازی Tekken 8 Advanced Edition", "PS5", "game-center", "https://game-center.ir/product/%d8%a7%da%a9%d8%a7%d9%86%d8%aa-%d8%a8%d8%a7%d8%b2%db%8c-tekken-8-advanced-edition/"),
    ("اکانت EA Sports FC 26", "PS5", "xgames", "https://xgamesstore.org/product/ea-sports-fc-26/"),
]

connection = sqlite3.connect(DB_PATH)
connection.executemany(
    "INSERT OR IGNORE INTO products (name, platform, store, url) VALUES (?, ?, ?, ?)",
    products,
)

connection.commit()
connection.close()
print("Product added successfully")