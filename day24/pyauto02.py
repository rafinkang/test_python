# pip install opencv-python
import pyautogui

# 이미지로 클릭하기

# i = pyautogui.locateOnScreen("e:/dev/python_workspace/img/btn_search.png")
i = pyautogui.locateOnScreen("e:/dev/python_workspace/q1.png")
print(i)
# Box(left=1769, top=227, width=38, height=37)
# 버튼의 중간쯤을 클릭
pos = pyautogui.center(i)
pyautogui.click(pos)


# 화면 캡쳐뜨기
# region(x, y, width, height)
# q1 = pyautogui.screenshot("q1.png", region=(1769, 227, 38, 38))
# print(q1)