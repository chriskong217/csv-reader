from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd
url = f"https://openpayrolls.com/university-college/texas-am-university-system/page-1"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/2010010 Firefox / 50.0'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
content1 = soup.find_all('tr')
with open('salaries.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Years', 'Name', 'Title']
    thewriter.writerow(header)
    for var in content1:
        year = getattr(var.find('td', class_="text-nowrap"), 'text', None)
        name = getattr(var.find('span', itemprop="name"), 'text', None)
        job = getattr(var.find('td', itemprop="jobTitle"), 'text', None)
        info = [year, name, job]
        thewriter.writerow(info)
i = 2
while i <= 20:
    url = f"https://openpayrolls.com/university-college/texas-am-university-system/page-{i}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/2010010 Firefox / 50.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    content1 = soup.find_all('tr')
    with open('salaries.csv', 'a', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        for var in content1:
            year = getattr(var.find('td', class_="text-nowrap"), 'text', None)
            name = getattr(var.find('span', itemprop="name"), 'text', None)
            job = getattr(var.find('td', itemprop="jobTitle"), 'text', None)
            info = [year, name, job]
            thewriter.writerow(info)
    i += 1
df = pd.read_csv('salaries.csv')
df.dropna(inplace = True)
df.to_csv('salaries.csv', index="false")









