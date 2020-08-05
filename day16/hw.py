import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random

class MyLotto(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(30,30,400,400)
        self.setWindowIcon(QIcon("./img/lotto/q.jpg"))
        self.setWindowTitle("로또번호 추첨기")
        # 전체 폼
        frmbox = QVBoxLayout()
        self.setLayout(frmbox)

        # 상하레이아웃
        topbox = QHBoxLayout()
        bottombox = QHBoxLayout()     

        # 상단 레이아웃
        top_gb = QGroupBox("번호")
        topbox.addWidget(top_gb)

        box1 = QHBoxLayout()
        top_gb.setLayout(box1)

        # 기본아이콘
        q_img = QPixmap("./img/lotto/q2.jpg")

        self.lotto_1 = QLabel("로또_1", self)
        self.lotto_1.setPixmap(q_img)
        self.lotto_2 = QLabel("로또_2", self)
        self.lotto_2.setPixmap(q_img)
        self.lotto_3 = QLabel("로또_3", self)
        self.lotto_3.setPixmap(q_img)
        self.lotto_4 = QLabel("로또_4", self)
        self.lotto_4.setPixmap(q_img)
        self.lotto_5 = QLabel("로또_5", self)
        self.lotto_5.setPixmap(q_img)
        self.lotto_6 = QLabel("로또_6", self)
        self.lotto_6.setPixmap(q_img)

        box1.addWidget(self.lotto_1)
        box1.addWidget(self.lotto_2)
        box1.addWidget(self.lotto_3)
        box1.addWidget(self.lotto_4)
        box1.addWidget(self.lotto_5)
        box1.addWidget(self.lotto_6)

        # 하단 레이아웃
        self.btn = QPushButton("로또번호 추첨!", self)
        bottombox.addWidget(self.btn)
        self.btn.clicked.connect(self.lotto)

        frmbox.addLayout(topbox)
        frmbox.addLayout(bottombox)
        self.show()

    def lotto(self):
        lotto_list = []
        while True:
            num = random.randint(1,45)
            if num not in lotto_list:
                lotto_list.append(num)
                if len(lotto_list) == 6 : break

        self.lotto_1.setPixmap(QPixmap("./img/lotto/ball"+str(lotto_list[0])+".png"))
        self.lotto_2.setPixmap(QPixmap("./img/lotto/ball"+str(lotto_list[1])+".png"))
        self.lotto_3.setPixmap(QPixmap("./img/lotto/ball"+str(lotto_list[2])+".png"))
        self.lotto_4.setPixmap(QPixmap("./img/lotto/ball"+str(lotto_list[3])+".png"))
        self.lotto_5.setPixmap(QPixmap("./img/lotto/ball"+str(lotto_list[4])+".png"))
        self.lotto_6.setPixmap(QPixmap("./img/lotto/ball"+str(lotto_list[5])+".png"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = MyLotto()
    sys.exit(app.exec_())