import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
from pathlib import Path

headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}

url = "https://movie.naver.com/movie/running/current.nhn"

res = requests.get(url)

res.raise_for_status()
res.close()

# pprint(res.text)

soup = bs(res.text, 'lxml')
# pprint(soup)
divs = soup.findAll("div", attrs=["class", "thumb"])
# pprint(len(divs))
idx = 0
for div in divs:
    idx += 1
    code = div.a['href'].split('code=')[-1]
    url2 = "https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode="
    res2 = requests.get(url2+code, headers=headers)
    res2.raise_for_status()
    res2.close()
    
    soup2 = bs(res2.text, 'lxml')
    img = soup2.find("img")
    imgpath = img['src']
    
    res3 = requests.get(imgpath, headers=headers)
    res3.raise_for_status()
    res3.close()
    
    Path("./img/movie_poster").mkdir(parents=True, exist_ok=True)
    with open("./img/movie_poster/movie{}.jpg".format(idx), "wb") as f:
        f.write(res3.content)