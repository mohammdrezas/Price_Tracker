import requests
from bs4 import BeautifulSoup

response = requests.get('https://game-center.ir/product/resident-evil-requiem/', headers={'User-Agent': 'Mozilla/5.0'}, timeout=30)
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find('h1', class_='product_title')
name = title.get_text(strip=True)
print("Name:", name)

price_container =  soup.find('p', class_='price')
prices = price_container.find_all('span', class_='woocommerce-Price-amount')
for price in prices:
    print("Price:", price.get_text(strip=True))

stock_meta = soup.find('meta', attrs={'name':'twitter:data2'})
stock = stock_meta['content']
print("stock:", stock)