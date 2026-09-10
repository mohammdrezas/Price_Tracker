import requests
from bs4 import BeautifulSoup
from processing.clean import clean_price, clean_stock

def scrape_product(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=30)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('h1', class_='product_title')
    name = title.get_text(strip=True)

    price_container =  soup.find('p', class_='price')
    prices = price_container.find_all('span', class_='woocommerce-Price-amount')

    price_numbers = []
    for price in prices:
        price_numbers.append(clean_price(price.get_text()))

    final_price = min(price_numbers)

    stock_meta = soup.find('meta', attrs={'name':'twitter:data2'})
    stock = stock_meta['content']
    final_stock = clean_stock(stock)
    return {
        "name": name,
        "price": final_price,
        "in_stock": final_stock
    }

if __name__ == "__main__":
    url = "https://game-center.ir/product/resident-evil-requiem/"
    data = scrape_product(url)
    print(data)