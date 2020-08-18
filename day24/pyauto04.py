# gb_70 : 로그인 버튼id
# identifierId : 로그인 이메일 id
# https://www.moakt.com/  임시메일 1시간짜리
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

url = "https://www.moakt.com"
browser = webdriver.Chrome("e:/dev/python_workspace/chromedriver.exe")
browser.get(url)

elem = browser.find_element_by_class_name("mail_in")
elem.click()
elem.send_keys("jhtatest")
time.sleep(1)

elem = browser.find_element_by_class_name("mail_butt")
elem.click()

time.sleep(1)
# iconic_button
browser.find_element_by_class_name("iconic_button").click()

# mail_to
time.sleep(1)
elem = browser.find_element_by_name("mail_to")
elem.send_keys("jsm@jhta.com")
# mail_subject
elem = browser.find_element_by_name("mail_subject")
elem.send_keys("자동 발송 메일 테스트 입니다.")
# mail_text
elem = browser.find_element_by_name("mail_text")
elem.send_keys("자동 발송 메일 테스트입니다. 호호호 삭제하세요 ^^ 호호호")

pyautogui.alert("사람인걸 증명해주세요 ^_^")

elem = browser.find_element_by_name("mail_send")
elem.click()
