import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *

class MyApp(QWidget):
    # LayOut  : BoxLayout , 수평 상자 수직 상자 
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI (self):
        # 창 타이틀 지정 
        self.setWindowTitle("로그인")
        self.setGeometry(50,50,500,500)

        self.leshow = QLineEdit("", self)
        # self.leshow = QLabel("dddd", self)

        self.num1 = QPushButton("1", self)
        self.num2 = QPushButton("2", self)
        self.num3 = QPushButton("3", self)
        self.num4 = QPushButton("4", self)
        self.num5 = QPushButton("5", self)
        self.num6 = QPushButton("6", self)
        self.num7 = QPushButton("7", self)
        self.num8 = QPushButton("8", self)
        self.num9 = QPushButton("9", self)
        self.num0 = QPushButton("0", self)
        self.num00 = QPushButton("00", self)
        self.plus = QPushButton("+", self)
        self.min = QPushButton("-", self)
        self.mul = QPushButton("*", self)
        self.div = QPushButton("/", self)
        self.eaq = QPushButton("=", self)

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.leshow, 0, 0, 1, 4)

        grid.addWidget(self.num1, 3, 0)
        grid.addWidget(self.num2, 3, 1)
        grid.addWidget(self.num3, 3, 2)
        grid.addWidget(self.num4, 2, 0)
        grid.addWidget(self.num5, 2, 1)
        grid.addWidget(self.num6, 2, 2)
        grid.addWidget(self.num7, 1, 0)
        grid.addWidget(self.num8, 1, 1)
        grid.addWidget(self.num9, 1, 2)
        grid.addWidget(self.num0, 4, 0)
        grid.addWidget(self.num00, 4, 1)
        grid.addWidget(self.plus, 1, 3)
        grid.addWidget(self.min, 2, 3)
        grid.addWidget(self.mul, 3, 3)
        grid.addWidget(self.div, 4, 3)
        grid.addWidget(self.eaq, 4, 2)

        # self.num7.clicked.connect(self.f7)
        self.num1.clicked.connect(lambda : self.func("1"))
        self.num2.clicked.connect(lambda : self.func("2"))
        self.num3.clicked.connect(lambda : self.func("3"))
        self.num4.clicked.connect(lambda : self.func("4"))
        self.num5.clicked.connect(lambda : self.func("5"))
        self.num6.clicked.connect(lambda : self.func("6"))
        self.num7.clicked.connect(lambda : self.func("7"))
        self.num8.clicked.connect(lambda : self.func("8"))
        self.num9.clicked.connect(lambda : self.func("9"))
        self.num0.clicked.connect(lambda : self.func("0"))
        self.num00.clicked.connect(lambda : self.func("00"))
        self.plus.clicked.connect(lambda : self.func("+"))
        self.min.clicked.connect(lambda : self.func("-"))
        self.mul.clicked.connect(lambda : self.func("*"))
        self.div.clicked.connect(lambda : self.func("/"))
        self.eaq.clicked.connect(self.cal)


        # 화면에 보여지게 설정 
        self.show()
    
    def func(self, num):
        self.leshow.setText(self.leshow.text()+str(num))
    
    def cal(self):
        # print(eval(self.leshow.text()))
        self.leshow.setText(str(eval(self.leshow.text())))




    # def keyPressEvent(self, e):
    #     print("키보드 눌릴때")
    # def keyReleaseEvent(self, e):
    #     print("키보드를 땔때")  
    # def mouseMoveEvent(self, e):
    #     print("마우스를 움직일때")
    # def mouseDoubleClickEvent(self, e):
    #     print("마우스 더블클릭")
    # def resizeEvent(self, e):
    #     print("위젯의 크기를 변경할때")
    # def mousePressEvent(self, e):
    #     print(e)
    
# 현재 파일에서 호출시에만 실행가능하게 설정 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


