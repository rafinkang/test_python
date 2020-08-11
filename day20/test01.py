'''
# web Crawling
여러 사이트를 정기적으로 돌며 정보를 추출하는 기술
==> DB

# web Scraping
웹사이트에서 특정 정보를 추출하는 기술

HTML CSS JS 
'''
# pip install requests
import requests

res = requests.get("http://google.com/")
print("응답코드 : ", res.status_code)
""" 
# 200 : 정상(HTTP.status)
# 404 : 페이지를 찾을 수 없음 - url not found
# url ( uniform resource Location )
# 500 : server side logic error
"""
# if res.status_code == 200:
# if res.status_code == requests.codes.ok:
    # print(len(res.text))
    # print(res.json)
    # print(res.content)

""" 에러가 있으면 에러 메세지를 출력하고 바로 종료 시켜주는 함수 """
res.raise_for_status() 

print(res.text)    
""" 파일로 저장 """
with open("google.html", "w", encoding="utf-8") as f:
    f.write(res.text)