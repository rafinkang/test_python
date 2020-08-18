# pip install pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import pyperclip

url = "https://www.naver.com"
browser = webdriver.Chrome("e:/dev/python_workspace/chromedriver.exe")
browser.get(url)

elem = browser.find_element_by_class_name("link_login")
elem.click()
time.sleep(1)
elem = browser.find_element_by_id("id")
elem.send_keys("rkdxo")
time.sleep(0.2)
elem.send_keys("dnr07")
time.sleep(1)
elem = browser.find_element_by_id("pw")
elem.send_keys("pwpw")
time.sleep(0.2)
elem.send_keys("1234")

time.sleep(2)
browser.find_element_by_class_name("btn_global").click()

pyautogui.alert("로그인 완료 후 버튼을 클릭하세요.")
# 현재창을 크게 하기
browser.maximize_window()
time.sleep(1)

# 메일 탭: Point(x=1337, y=503)
pyautogui.click(1340,513)
time.sleep(1)
# 메일 쓰기: Point(x=1474, y=543)
pyautogui.click(1484,553)

time.sleep(1)
pyautogui.click(442, 342)
pyautogui.write("rkdxodnr07@naver.com")
time.sleep(1)
pyautogui.click(440,419)
pyperclip.copy("행운의 편지")
pyautogui.hotkey("ctrl", "v")
# pyautogui.write("lucky letter")

time.sleep(1)
pyautogui.click(367, 556)
pyperclip.copy("이 편지는 영국에서 시작해서.. 하루에 3통 안보내면 배고픔")
pyautogui.hotkey("ctrl", "v")


time.sleep(1)
pyautogui.click(318, 294)
