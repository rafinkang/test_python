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
print(soup.title)
print(soup.title.get_text())
print('-------------------------------')
# soup 객체에서 처음 발견되는 a 엘리먼트를 출력 해라
print(soup.find("a"))
print('-------------------------------')
# 태그 내 속성값만 가져오기
print(soup.a.attrs)
print('-------------------------------')
print(soup.a.attrs['href'])
print('-------------------------------')

# 함수를 이용한 접근
print(soup.find("td", attrs=["class", "title"]))
title1 = soup.find("td", attrs=["class", "title"])
print('-------------------------------')
a = title1.find("a")
print(a)


# titles = soup.findAll("td", attrs=["class", "title"])
# for t in titles:
#     print(t.get_text())