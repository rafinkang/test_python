import sys

from PyQt5.QtWidgets import *

# 윈도우를 생성하는 클래스 : QMainWindow, QWidget, QDialog
# 메인 윈도우를 생성하기 위한 클래스 : QMainWindow, QDialog
# QMainWindow : QHBoxLayout, QVBoxLayout 같은 layout을 사용할 수 있다.

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.show()

if __name__ == "__main__":
    # QApplication 클래스의 인스턴스를 생성
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_()) # 이벤트 루프 - 끝나지 않고 이벤트를 기다리도록

