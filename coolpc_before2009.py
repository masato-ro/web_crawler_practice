import csv
import requests
from bs4 import BeautifulSoup

prices = []
for year in range(2009, 2010): # 跑年份
    for month in range(1, 13): # 跑月份
        resp = requests.get(
            'https://web.archive.org/web/' + str(year) + str(month).zfill(2) + '/http://www.coolpc.com.tw:80/evaluate.php')
        soup = BeautifulSoup(resp.text, 'html.parser')
        items = soup.find('select',onchange='cnt(2)').find_all('optgroup')

        file = open('output\\output_' +str(year) + str(month).zfill(2) + '.csv', 'w', newline='', encoding='utf-8-sig')
        csvfile = csv.writer(file)

        for item in items:
            price = item.find_all('option')[0].text.strip()
            prices.append(price)
            print(prices)
            csvfile.writerow(prices)
            prices = []

        file.close()
