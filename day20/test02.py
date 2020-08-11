import requests

url = "https://search.naver.com/search.naver?query=날씨"

res = requests.get(url)
res.raise_for_status()

print(res.text)