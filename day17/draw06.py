import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
import time
import threading

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 창 타이틀
        self.setWindowTitle("점찍기")
        # 크기와 위치
        self.setGeometry(100,100,800,600)
        # 화면에 보이게 설정
        self.show()

    def paintEvent(self, e):
        # print("페인트 이벤트 발생@@_@@_@@_@")
        # Qpaint 인스턴스 생성
        qp = QPainter()
        # 페인팅 시작
        qp.begin(self)
        for i in range(1000):
            qp.setPen(QPen(QColor(random.randint(0,255), random.randint(0,255), random.randint(0,255)), random.randint(1,50)))
            qp.drawLine(random.randint(0, 800), random.randint(0,600), random.randint(0,800), random.randint(0,600))
        
        # 페인팅 끝
        qp.end()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())