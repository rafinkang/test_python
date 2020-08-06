import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(30,30,1000,1000)
        # 전체 폼
        frmbox = QHBoxLayout()
        self.setLayout(frmbox)
        
        # 좌우 레이아웃
        leftbox = QVBoxLayout()
        rightbox = QVBoxLayout()

        # 좌측 레이아웃
        gb = QGroupBox("타입")
        leftbox.addWidget(gb)

        box1 = QVBoxLayout()
        gb.setLayout(box1)

        box1.addWidget(QRadioButton("직선", self))
        box1.addWidget(QRadioButton("곡선", self))
        box1.addWidget(QRadioButton("사각형", self))
        box1.addWidget(QRadioButton("타원", self))

        # 그룹박스 2
        gb2 = QGroupBox("Pen setting")
        leftbox.addWidget(gb2)

        grid = QGridLayout()
        gb2.setLayout(grid)

        label = QLabel("선 굵기")
        grid.addWidget(label, 0, 0)

        combo = QComboBox()
        grid.addWidget(combo, 0, 1)
        for i in range(1,21):
            combo.addItem(str(i))

        label2 = QLabel("선 색")
        grid.addWidget(label2, 1, 0)
        # 펜 색상
        self.pencolor = QColor(0,0,0)
        self.penbtn = QPushButton()
        self.penbtn.setStyleSheet("background-color: rgb(0,0,0)")
        grid.addWidget(self.penbtn,1,1)

        # 그룹박스 3
        # 붓 설정
        gb3 = QGroupBox("붓 설정")
        leftbox.addWidget(gb3)

        hbox = QHBoxLayout()
        gb3.setLayout(hbox)

        label3 = QLabel("붓 색상")
        hbox.addWidget(label3)

        self.brushcolor = QColor(255,255,255)
        self.brushbtn = QPushButton()
        self.brushbtn.setStyleSheet("background-color:rgb(255,255,255);")
        hbox.addWidget(self.brushbtn)

        # 우측 레이아웃 박스에 그래픽 뷰 추가
        self.view = CGView(self)
        rightbox.addWidget(self.view)



        frmbox.addLayout(leftbox)
        frmbox.addLayout(rightbox)
        self.show()

# QGraphics 는 시각적 객체의 복잡한 장면을 쉽게 처리할 수 있는 
# 프레임워크로 구성하는데 사용할 수 있다.

# QGraphicsView, QGraphicsScne, QGraphicsItems

class CGView(QGraphicsView):
    def __init__(self, parent):
        super().__init__(parent)
        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.items = []
        self.start = QPointF()
        self.end  = QPointF()

    def moveEvent(self, e):
        # print("moveEvent 호출됨")
        rect = QRectF(self.rect())  #현재 창 크기
        rect.adjust(0, 0, -3, -3)
        self.scene.setSceneRect(rect)
        
    def mousePressEvent(self, e):
        # print("마우스 클릭 됨")
        # print(e, e.button())
        if e.button() == Qt.LeftButton: # 1:좌클릭 2:우클릭
            # 시작점 저장
            self.start = e.pos()
            self.end = e.pos()
            # print(e.pos())

    def mouseMoveEvent(self, e):
        # print("마우스 드래그 됨")
        self.end = e.pos()

        pen = QPen(QColor(255,0,0), 1)
        # 현재선을 추가
        # line = QLineF(시작x, y, 끝x, y)
        line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())
        # self.scene.addLine(라인객체, 행종류)
        self.scene.addLine(line, pen)

    def mouseReleaseEvent(self, e):
        # print("마우스 뗄 때 호출됨")
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = MyApp()
    sys.exit(app.exec_())