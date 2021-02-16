import csv
import requests
from bs4 import BeautifulSoup

prices = []
ym = input('請輸入年月：')
try:
    if ym == '200801':
        for year in range(2008, 2009): # 跑年份
            for month in range(1, 2): # 跑月份
                resp = requests.get(
                    'https://web.archive.org/web/' + str(year) + str(month).zfill(2) + '/http://www.coolpc.com.tw:80/evaluate.php')
                soup = BeautifulSoup(resp.text, 'html.parser')
                items = soup.find('table', border='0').find('tr',bgcolor='efefe0')

                file = open('output/output_' +str(year) + str(month).zfill(2) + '.csv', 'w', newline='', encoding='utf-8-sig')
                csvfile = csv.writer(file)

                for item in items:
                    price = item.find_all('td')[1].text.strip()
                    prices.append(price)
                    print(prices)
                    csvfile.writerow(prices)
                    prices = []
                file.close()
    elif ym == 200809:
        print('test')
    elif ym == 're':
        month = 1
        while month <= 12:
            file1 = open('output/output_2009' + str(month).zfill(2) + '.csv', 'r').readlines()
            fileout1 = open('output/output_2009' + str(month).zfill(2) + '.csv', 'w')
            for line in file1:
                fileout1.write(line.replace('$', ''))
            fileout1.close()
            file2 = open('output/output_2009' + str(month).zfill(2) + '.csv', 'r').readlines()
            fileout2 = open('output/output_2009' + str(month).zfill(2) + '.csv', 'w')
            for line in file2:
                fileout2.write(line.replace('★', ''))
            fileout2.close()
            file3 = open('output/output_2009' + str(month).zfill(2) + '.csv', 'r').readlines()
            fileout3 = open('output/output_2009' + str(month).zfill(2) + '.csv', 'w')
            for line in file3:
                fileout3.write(line.replace(' 熱賣', ''))
            fileout3.close()
            month += 1
    else:
        print('input error...')
except:
    print('no input...')
