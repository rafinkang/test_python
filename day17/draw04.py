import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

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
        # 색상 채우기
        qp.setBrush(QColor(255,0,255))
        # 펜설정 : 회색, 5
        qp.setPen(QPen(QColor(100,100,100), 5))
        # drawRect(x, y, width, height)
        qp.drawRect(30,30,100,150)

        qp.setPen(QPen(Qt.red, 5))
        qp.drawLine(200, 100, 700, 100)

        qp.setPen(QPen(Qt.blue, 5))
        qp.setBrush(QColor(Qt.blue))
        qp.drawRect(200,200, 100,100)
        qp.setBrush(QColor(Qt.yellow))
        qp.drawRect(400,200, 100,100)
        qp.setBrush(QColor(QColor(123,123,12)))
        qp.drawRect(600,200, 100,100)

        qp.setBrush(QColor(Qt.green))
        qp.setPen(QPen(Qt.green, 5))
        qp.drawRect(200, 400, 500, 100)


        # 페인팅 끝
        qp.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())