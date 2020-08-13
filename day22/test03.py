""" 
pip install request
pip install bs4 
pip install lxml
"""
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

url = "https://comic.naver.com/webtoon/list.nhn?titleId=20853"

res = requests.get(url)
res.raise_for_status()
res.close()
# pprint(res.text)

soup = bs(res.text, 'lxml')
# print(soup, type(soup))
# 함수를 이용한 접근
print(soup.find("td", attrs=["class", "title"]))

print('---------------------------------------------------------------------------')
# print(soup.findAll("td", attrs=["class", "title"]))
tdList = soup.findAll("td", attrs=["class", "title"])
# print(tdList[0].find('a').get_text())
for td in tdList:
    print(td.find('a').get_text())