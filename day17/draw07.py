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

        qp.setPen(QColor(0,0,0))
        # qp.setFont(QFont("폰트명", 사이즈))
        # c:\windows\fonts 가면 보임
        qp.setFont(QFont("나눔고딕", 50))
        qp.drawText(100, 100, "푸른하늘 은하수")

        self.drawOther(qp)
        
        # 페인팅 끝
        qp.end()

    def drawOther(self, qp):
        pen = QPen(Qt.black, 3, Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(50,50,100,50)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(200, 50, 100, 50)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())