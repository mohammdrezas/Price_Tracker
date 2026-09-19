import sqlite3
from config import DB_PATH

recent_days = 7
drop_threshold = 0.10

def find_price_drops(connection):
    products = connection.execute(" select id, name, store from products where is_active = 1").fetchall()
    drops = []
    for product in products:
        product_id = product[0]
        name = product[1]
        store = product[2]
        latest_row = connection.execute(" select price from price_history where product_id = ? order by checked_at desc limit 1", (product_id,)).fetchone()
        avg_row = connection.execute(" select avg(price) from price_history where product_id = ? and checked_at >= datetime('now', ?)", (product_id, f"-{recent_days} days")).fetchone()
        latest_price = latest_row[0] if latest_row else None
        avg_price = avg_row[0]

        if latest_price is not None and avg_price is not None:
            if latest_price < avg_price * (1 - drop_threshold):
                drops.append({"name": name, "latest": latest_price, "average": round(avg_price)})

    return drops

if __name__ == "__main__":
    connection = sqlite3.connect(DB_PATH)
    drops = find_price_drops(connection)
    connection.close()
    if drops:
        for d in drops:
            print(f"DROP: {d['name']} -> {d['latest']} (avg {d['average']})")
    else:
        print("No price drops found.")