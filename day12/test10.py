import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton("집에가기", self)
        btn.resize(600, 70)
        btn.move(300,600)
        btn.clicked.connect(QCoreApplication.instance().quit)

        label1 = QLabel("집에 가~~~~", self)
        label1.resize(600, 100)
        label1.move(300, 200)

        font1 = label1.font()
        font1.setPointSize(50)

        label1.setFont(font1)

        self.setWindowTitle("집에 가고싶은 윈도우 창")
        self.setWindowIcon(QIcon("./img/instagram.png"))
        self.resize(1200, 800)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())