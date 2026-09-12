import sqlite3
from scraper.scraper import scrape_product

connection = sqlite3.connect("database/price_tracker.db")

product = connection.execute("SELECT id, url FROM products WHERE is_active = 1").fetchone()
product_id = product[0]
url = product[1]

data = scrape_product(url)

connection.execute(
    "INSERT INTO price_history (product_id, price, in_stock) VALUES (?, ?, ?)",
    (product_id, data["price"], data["in_stock"])
)

connection.commit()
connection.close()
print("Saved:", data)