import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # QPixmap 객체
        p_img = QPixmap("./img/instagram.png")

        # label
        self.label1 = QLabel("(*ฅ́˘ฅ̀*)♡", self)
        self.label1.setPixmap(p_img)
        self.label1.move(400, 200)
        self.label1.resize(1000, 1000)

        # btn
        btn_up = QPushButton("▲", self)
        btn_up.resize(50,50)
        btn_up.move(350, 500)
        btn_up.clicked.connect(self.up)

        btn_down = QPushButton("▼", self)
        btn_down.resize(50,50)
        btn_down.move(350, 550)
        btn_down.clicked.connect(self.down)

        btn_left = QPushButton("◀", self)
        btn_left.resize(50,50)
        btn_left.move(300, 550)
        btn_left.clicked.connect(self.left)

        btn_right = QPushButton("▶", self)
        btn_right.resize(50,50)
        btn_right.move(400, 550)
        btn_right.clicked.connect(self.right)


        self.setWindowTitle("MyApp")
        self.resize(800, 600)
        self.show()
    
    def up(self):
        self.label1.move(self.label1.x(), self.label1.y() - 50)
    def down(self):
        self.label1.move(self.label1.x(), self.label1.y() + 50)
    def left(self):
        self.label1.move(self.label1.x() - 50, self.label1.y())
    def right(self):
        self.label1.move(self.label1.x() + 50, self.label1.y())
        
    def keyPressEvent(self, e):
        print(e.key())
        # return super().keyPressEvent(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())