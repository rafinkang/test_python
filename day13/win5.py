import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QCoreApplication, Qt
import time
import threading
import math

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

        self.setWindowTitle("MyApp")
        self.resize(800, 600)
        self.show()
    
    def up(self):
        for i in range(50):
            self.label1.move(self.label1.x(), self.label1.y() - 1)
    def down(self):
        for i in range(50):
            self.label1.move(self.label1.x(), self.label1.y() + 1)
    def left(self):
        for i in range(50):
            self.label1.move(self.label1.x() - 1, self.label1.y())
    def right(self):
        for i in range(50):
            self.label1.move(self.label1.x() + 1, self.label1.y())
        
    def keyPressEvent(self, e):
        # return super().keyPressEvent(e)
        # print(e.key())
        key = e.key()
        if key == 87 or key == Qt.Key_Up:
            self.up()
        elif key == 65 or key == Qt.Key_Left:
            self.left()
        elif key == 83 or key == Qt.Key_Down:
            self.down()
        elif key == 68 or key == Qt.Key_Right:
            self.right()
        elif key == Qt.Key_Space:
            t = threading.Thread(target=self.moveTurtle)
            t.start()

    def moveTurtle(self):
        print("스페이스바가 눌렸음 ")
        for i in range(1, 101):
            # print(math.sin(math.pi/101 *i *2)*10)
            self.label1.move(self.label1.x()+1, self.label1.y() - int(math.sin(math.pi/101 *i *2)*10))
            time.sleep(0.01)
        # for i in range(10):
        #     self.label1.move(self.label1.x(), self.label1.y() - 10)
        #     time.sleep(0.01)
        # for i in range(10):
        #     self.label1.move(self.label1.x(), self.label1.y() + 10)
        #     time.sleep(0.01)

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())