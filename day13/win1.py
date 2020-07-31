import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # UI 담당함수 :User Interface
    def initUI(self):
        # 푸쉬버튼 객체 생성
        btn1 = QPushButton("출력", self)
        btn1.setText("다시출력")
        btn1.resize(100,100)
        btn1.move(300,200)
        # 이벤트핸들러
        # btn1.clicked.connect(처리할 이벤트 핸들러)
        btn1.clicked.connect(self.print)

        btn2 = QPushButton("EXIT", self)
        btn2.resize(100,100)
        btn2.move(600,200)
        btn2.clicked.connect(QCoreApplication.instance().quit)

        # 창의 타이틀 지정
        self.setWindowTitle("wow 불큼~~ ㅌㅌㅌㅌ")
        # 창의 크기
        self.resize(1200, 800)
        # 창위치
        self.move(300, 400)

        # 화면에 창을 보여주게
        self.show()

    def print(self):
        print('프린트이벤트')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())