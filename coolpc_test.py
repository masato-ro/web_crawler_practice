import csv
import requests
from bs4 import BeautifulSoup

prices = []
resp = requests.get(
    'https://web.archive.org/web/20080324031010/http://www.coolpc.com.tw:80/evaluate.php')
soup = BeautifulSoup(resp.text, 'html.parser')
items = soup.find('table', {'border': '0','cellspacing': '1'}).find('tr',bgcolor='efefe0')

for item in items:
    price = item.find_all('td')[1].text.strip()
    prices.append(price)
    print(prices)
