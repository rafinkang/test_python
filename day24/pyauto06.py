from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

url = "https://www.naver.com"
browser = webdriver.Chrome("e:/dev/python_workspace/chromedriver.exe")
# 브라우저 열고 네이버로
browser.get(url)

# 현재창을 크게
browser.maximize_window()

# 검색
time.sleep(1)
elem = browser.find_element_by_id("query")
elem.click()
elem.send_keys("종로3가 맛집")
elem.send_keys(Keys.ENTER)
time.sleep(1)

# 아래로 스크롤
pyautogui.scroll(-1500)
matzip_list = []

for i in range(20):
    time.sleep(0.2)
    ulElem = browser.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.place_list > div.list_area > ul")
    # print(ulElem)
    lists = ulElem.find_elements_by_css_selector("li.list_item")
    # print(lists)
    for store in lists:
        matzip_list.append(store.find_element_by_css_selector("div.tit > span > a > span").text)

    # Point(x=762, y=605)
    pyautogui.click(762, 605)
    
print(matzip_list)