import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8"

res = requests.get(url)

res.raise_for_status()
res.close()

soup = bs(res.text, 'lxml')
divs = soup.findAll("div", attrs=["class", "today_area _mainTabContent"])
# print(len(divs))
""" 
    정의 목록 만들기
    <dl>    정의 목록 (difinition List)
        <dt>용어 제목</dt> (difinition Term)
        <dd>용어 설명</dd> (difinition description)
    </dl>
"""
for div in divs:
    # pprint(div)
    todaytemp = div.find("span", attrs=["class", "todaytemp"]).get_text()
    print(todaytemp)
    dds = div.findAll("dd", attrs=["class","lv1"])
    for d in dds:
        # pprint(d)
        num = d.find("span", attrs=["class", "num"])
        print(num.get_text())
    
    rainfall = div.find("span", attrs=["class", "rainfall"]).find("span", attrs=["class", "num"]).get_text()
    print(rainfall)