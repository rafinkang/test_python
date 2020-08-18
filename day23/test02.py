""" 
selenium
- 웹 브라우저의 자동화를 가능하게 하는 다양한 도구와 라이브러리 포함하는 프로젝트

webdriver
- 브라우저 버전 확인 : 84.0.4147.125 (공식 빌드) (64비트) (cohort: Stable)

크롬드라이버 - https://chromedriver.chromium.org/downloads


"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

""" 크롬 드라이버 객체 생성 """
browser = webdriver.Chrome("./chromedriver.exe")
""" 브라우저 객체로 네이버 웹 페이지 접속 """
browser.get("http://www.naver.com")
""" 검색창 엘리먼트 객체 """
element = browser.find_element_by_id("query")
time.sleep(3)
element.click()
element.send_keys('택배 없는 날')
element.send_keys(Keys.ENTER)

# browser.close()
# browser.quit()
# 3초 후 구글로 이동
time.sleep(3)
browser.get("http://www.google.com")
element = browser.find_element_by_name("q")
element.click()
element.send_keys("광복절")
element.send_keys(Keys.ENTER)
time.sleep(3)
element = browser.find_element_by_name("q")
element.click()
element.send_keys(Keys.BACKSPACE)
element.send_keys(Keys.BACKSPACE)
element.send_keys(Keys.BACKSPACE)
element.send_keys("빨간날")
element.send_keys(Keys.ENTER)

