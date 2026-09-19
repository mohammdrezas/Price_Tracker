import asyncio
import aiohttp
import sqlite3
import logging
from scraper.scraper import scrape_product
from analysis.analyze import find_price_drops
from notifier.notify import send_alerts
from config import DB_PATH

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

async def scrape_one(session, product):
    product_id = product[0]
    url = product[1]
    store = product[2]
    try:
        data = await scrape_product(session, url, store)
        return (product_id, data)
    except Exception as e:
        logging.warning(f"failed for product {product_id}: {e}")
        return (product_id, None)


async def main():
    connection = sqlite3.connect(DB_PATH)
    products = connection.execute("SELECT id, url, store FROM products WHERE is_active = 1").fetchall()

    async with aiohttp.ClientSession() as session:
        tasks = []
        for product in products:
            tasks.append(scrape_one(session, product))
        results = await asyncio.gather(*tasks)

    for product_id, data in results:
        if data is not None:
            connection.execute(
                "INSERT INTO price_history (product_id, price, in_stock) VALUES (?, ?, ?)",
                (product_id, data["price"], data["in_stock"])
            )
            logging.info(f"Saved: {data}")
    connection.commit()

    drops = find_price_drops(connection)
    send_alerts(drops)

    connection.close()


if __name__ == "__main__":
    asyncio.run(main())