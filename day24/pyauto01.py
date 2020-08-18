#  pip install pyautogui

import pyautogui

# 현재 gui상의 마우스 좌표
print(pyautogui.position())
# Point(x=1170, y=321)
pyautogui.click(1023, 334)