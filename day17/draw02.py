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
        # 펜 설정(펜객체(색상,크기))
        qp.setPen(QPen(Qt.blue, 8))
        # 펜위치(화면너비 절반, 화면높이 절반)
        qp.drawPoint(self.width()/2, self.height()/2)
        # 페인팅 끝
        qp.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())