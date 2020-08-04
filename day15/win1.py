import sys

from PyQt5.QtWidgets import *

def quit():
    print("quit() 호출됨")
    sys.exit(0) # 0: 정상종료, 나머지: 비정상 종료

# QApplication 클래스의 인스턴스를 생성
app = QApplication(sys.argv)
print(app, sys.argv)

btn = QPushButton("QUIT")
btn.show()
btn.clicked.connect(quit)

app.exec_() # 이벤트 루프 - 끝나지 않고 이벤트를 기다리도록

