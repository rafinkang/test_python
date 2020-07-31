import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # lineEdit
        self.dan = QLineEdit(self)
        self.dan.move(300, 200)
        self.dan.resize(120, 50)

        # btn
        btn1 = QPushButton("99단", self)
        btn1.resize(120,50)
        btn1.move(300, 300)
        btn1.clicked.connect(self.gugudan)

        self.setWindowTitle("win3.py")
        self.resize(800, 600)
        self.show()

    def gugudan(self):
        if self.dan.text() == '':
            print("단을 입력하세요")
        else:
            dan = int(self.dan.text())
            for i in range(1,10):
                print(dan, "*", i, "=", dan*i)
            self.dan.setText('')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())