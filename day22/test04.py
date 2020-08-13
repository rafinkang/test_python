from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from pathlib import Path

# {'User-Agent' : 'what is my user agent 정보'}
headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}

for i in range(1230, 1237):
    url = "https://comic.naver.com/webtoon/detail.nhn?titleId=20853&no={}&weekday=tue".format(i)
    res = requests.get(url)
    res.raise_for_status()
    res.close()

    # pprint(res.text)

    soup = bs(res.text, 'lxml')
    # pprint(soup)
    data = soup.find('div', attrs=["class", "wt_viewer"])
    # print(data)
    images = data.findAll("img")
    # print(images)
    for img in images:
        # pprint(img['src'])
        path = img['src']
        # print(path.split("/")[-1].split("_")[-2:])
        # print(path[-13:])
        res2 = requests.get(path, headers=headers)
        res2.raise_for_status()
        res2.close()
        # 별도의 디렉토리를 만들고 그 장소에 이미지 파일을 저장
        Path("./img/"+str(i)).mkdir(parents=True, exist_ok = True)    
        with open("./img/"+str(i)+"/"+path.split("/")[-1].split("_")[-1:][0], 'wb') as f:
            f.write(res2.content)