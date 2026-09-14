import asyncio
import aiohttp
from bs4 import BeautifulSoup
from processing.clean import clean_price, clean_stock

def parse_game_center(soup):
    name = soup.find('h1', class_='product_title').get_text(strip=True)
    prices = soup.find('p', class_='price').find_all('span', class_='woocommerce-Price-amount')
    price_numbers = []
    for price in prices:
        price_numbers.append(clean_price(price.get_text()))
    final_price = min(price_numbers)
    stock = soup.find('meta', attrs={'name': 'twitter:data2'})['content']
    return name, final_price, stock

def parse_xgames(soup):
    name = soup.find('meta', attrs={'property': 'og:title'})['content']
    price_text = soup.find('meta', attrs={'name': 'twitter:data1'})['content']
    parts = price_text.split('-')
    price_numbers = []
    for part in parts:
        price_numbers.append(clean_price(part))
    final_price = min(price_numbers)
    stock = soup.find('meta', attrs={'name': 'twitter:data2'})['content']
    return name, final_price, stock

PARSERS = {
    "game-center": parse_game_center,
    "xgames": parse_xgames,
}

async def scrape_product(session, url, store):
    async with session.get(url, headers={'User-Agent': 'Mozilla/5.0'}) as response:
        html = await response.text()
    soup = BeautifulSoup(html, 'html.parser')
    parser = PARSERS[store]
    name, final_price, stock = parser(soup)
    final_stock = clean_stock(stock)
    return {"name": name, "price": final_price, "in_stock": final_stock}

async def main():
    async with aiohttp.ClientSession() as session:
        result1 = await scrape_product(session, "https://game-center.ir/product/resident-evil-requiem/", "game-center")
        print(result1)
        result2 = await scrape_product(session, "https://xgamesstore.org/product/ea-sports-fc-26/", "xgames")
        print(result2)


if __name__ == "__main__":
    asyncio.run(main())