import json
import requests
from bs4 import BeautifulSoup

cpus = []
for year in range(2008, 2009): # 跑年份
    for month in range(7, 8): # 跑月份
        resp = requests.get(
            'https://web.archive.org/web/' + str(year) + str(month).zfill(2) + '/http://www.coolpc.com.tw:80/evaluate.php')
        soup = BeautifulSoup(resp.text, 'html.parser')
        items = soup.find_all('tr', bgcolor='efefe0')[1].find_all('option')[2].text.strip().splitlines()

        for item in items:
            print(item)
            cpus.append({'item':item,'year':year,'month':month})

        with open('output\\output_' + str(year) + str(month).zfill(2) + '.json', 'w', encoding='utf-8-sig') as f:
            json.dump(cpus, f, indent=2, sort_keys=False, ensure_ascii=False)
        cpus=[]