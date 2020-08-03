# pip install pyinstaller
# pyinstaller -w -F Mywindow.py
# -w : 실행창 제거
# -F : 파일 하나로 만들기

import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import time

class MyWindow2(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(100,100,200,200)
        self.setWindowTitle("메롱~~~")
        # p_img = QPixmap("./img/merong.jpeg")
        p_img = QPixmap("./img/peach.png")
        self.lb = QLabel("메롱", self)
        self.lb.setPixmap(p_img)
        self.lb.setGeometry(0,0,200,200)
        self.show()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("취업지원")
        # self.move(200,200)
        # self.resize(300,300)
        # 위 두개 한번에
        self.setGeometry(200,200,300,300)

        self.btn1 = QPushButton("비법 자소서 보기", self)
        self.btn1.move(100, 100)
        self.btn1.setToolTip("<h3>날 눌러봐!!</h3>")
        self.btn1.clicked.connect(self.newWindow)

        self.show()

    def newWindow(self):
        for i in range(5):
            # self.nw = QMainWindow(self)
            # self.nw.label1 = QLabel("이건 몰랐지?", self.nw)
            # self.nw.label1.setPixmap(QPixmap("./img/merong.jpeg"))
            # self.nw.label1.resize(300,300)
            # self.nw.resize(300,300)
            # self.nw.move(100+i*10,100+i*10)
            # self.nw.show()
            self.nw = MyWindow2(self)
            self.nw.move(100+i*20,100+i*20)
            self.nw.show()
            time.sleep(0.3)
        # self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())