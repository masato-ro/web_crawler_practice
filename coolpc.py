import csv
import requests
from bs4 import BeautifulSoup

prices = []
for year in range(2009, 2012): # 跑年份
    for month in range(10, 13): # 跑月份
        resp = requests.get(
            'https://web.archive.org/web/' + str(year) + str(month).zfill(2) + '/http://www.coolpc.com.tw/evaluate.php')
        soup = BeautifulSoup(resp.text, 'html.parser')
        items = soup.find('table', id='Tfix').find_all('tr')[5]

        file = open('output\\output_' +str(year) + str(month).zfill(2) + '.csv', 'w', newline='', encoding='utf-8-sig')
        csvfile = csv.writer(file)

        for item in items:
            price = item.find_all('td')[1].text.strip()
            prices.append(price)
            print(prices)
            csvfile.writerow(prices)
            prices = []

        file.close()
