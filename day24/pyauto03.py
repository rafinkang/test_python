import pyautogui
import time

pyautogui.moveTo(400,400,2)

# moveToRelative()

pyautogui.moveRel(100,100,3)

pyautogui.moveTo(1769, 227)
pyautogui.click(clicks=2, interval=2)

pyautogui.doubleClick()

time.sleep(1)
pyautogui.typewrite("hello")