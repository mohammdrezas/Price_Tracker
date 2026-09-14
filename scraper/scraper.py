import requests
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

def scrape_product(url, store):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=30)
    soup = BeautifulSoup(response.text, 'html.parser')
    parser = PARSERS[store]
    name, final_price, stock = parser(soup)
    final_stock = clean_stock(stock)
    return {"name": name, "price": final_price, "in_stock": final_stock}

if __name__ == "__main__":
    print(scrape_product("https://game-center.ir/product/resident-evil-requiem/", "game-center"))
    print(scrape_product("https://xgamesstore.org/product/ea-sports-fc-26/", "xgames"))