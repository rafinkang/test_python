import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        # 1.직선 2.사각형
        self.drawType = 1
        self.initUI()

    def initUI(self):
        self.setGeometry(30,30,800,800)
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

        self.rbtnLine = QRadioButton("직선", self)
        self.rbtnRect = QRadioButton("사각형", self)
        self.rbtnCurve = QRadioButton("곡선", self)
        self.rbtnEllipse =QRadioButton("타원", self)
        box1.addWidget(self.rbtnLine)
        box1.addWidget(self.rbtnRect)
        box1.addWidget(self.rbtnCurve)
        box1.addWidget(self.rbtnEllipse)
        self.rbtnLine.clicked.connect(self.radioBtnClicked)
        self.rbtnRect.clicked.connect(self.radioBtnClicked)
        self.rbtnCurve.clicked.connect(self.radioBtnClicked)
        self.rbtnEllipse.clicked.connect(self.radioBtnClicked)

        self.rbtnLine.setChecked(True)
        self.drawType = 1

        

        # 그룹박스 2
        gb2 = QGroupBox("Pen setting")
        leftbox.addWidget(gb2)

        grid = QGridLayout()
        gb2.setLayout(grid)

        label = QLabel("선 굵기")
        grid.addWidget(label, 0, 0)

        self.combo = QComboBox()
        grid.addWidget(self.combo, 0, 1)
        for i in range(1,21):
            self.combo.addItem(str(i))

        label2 = QLabel("선 색")
        grid.addWidget(label2, 1, 0)
        # 펜 색상
        self.pencolor = QColor(0,0,0)
        self.penbtn = QPushButton()
        self.penbtn.setStyleSheet("background-color: rgb(0,0,0)")
        grid.addWidget(self.penbtn,1,1)
        self.penbtn.clicked.connect(self.selectColorDlg)

        # 그룹박스 3
        # 붓 설정
        gb3 = QGroupBox("붓 설정")
        leftbox.addWidget(gb3)

        hbox = QHBoxLayout()
        gb3.setLayout(hbox)

        label3 = QLabel("붓 색상")
        hbox.addWidget(label3)

        gb4 = QGroupBox("FILE")
        leftbox.addWidget(gb4)

        hbox4 = QHBoxLayout()
        gb4.setLayout(hbox4)

        saveBtn = QPushButton("버튼", self)
        hbox4.addWidget(saveBtn)
        saveBtn.clicked.connect(self.save_img)

        self.brushcolor = QColor(255,255,255)
        self.brushbtn = QPushButton()
        self.brushbtn.setStyleSheet("background-color:rgb(255,255,255);")
        hbox.addWidget(self.brushbtn)
        self.brushbtn.clicked.connect(self.selectColorDlg)

        # 우측 레이아웃 박스에 그래픽 뷰 추가
        self.view = CGView(self)
        rightbox.addWidget(self.view)



        frmbox.addLayout(leftbox)
        frmbox.addLayout(rightbox)
        self.show()

    def save_img(self):
        img = self.view.grab(self.view.sceneRect().toRect())
        # print(img)
        fname = QFileDialog.getSaveFileName(self, "이따가 저장할래?", "./")
        # print(fname)
        if fname[0]:
            img.save(fname[0])
        # img.save('e:/data.png')

    def selectColorDlg(self):
        # 색상 대화상자 생성
        color = QColorDialog.getColor()
        this = self.sender()
        if this == self.penbtn:
            self.pencolor = color
        elif this == self.brushbtn:
            self.brushcolor = color

        this.setStyleSheet("background-color:{}".format(color.name()))
    
    # 어느 라디오 버튼이 선택되었는지 판단
    def radioBtnClicked(self):
        if self.rbtnLine.isChecked():
            self.drawType = 1
        elif self.rbtnRect.isChecked():
            self.drawType = 2
        elif self.rbtnCurve.isChecked():
            self.drawType = 3
        elif self.rbtnEllipse.isChecked():
            self.drawType = 4
    



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
        pen = QPen(self.parent().pencolor, self.parent().combo.currentIndex()+1)
        brush = QBrush(self.parent().brushcolor)

        # scene에 그려진 이전 선을 제거
        if len(self.items) > 0 :
            self.scene.removeItem(self.items[-1])
            del(self.items[-1])

        if self.parent().drawType == 1:
            # 현재선을 추가
            line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())
            self.items.append(self.scene.addLine(line, pen))
        elif self.parent().drawType == 2:    
            # 사각형 그리기
            rect = QRectF(self.start, self.end)
            self.items.append(self.scene.addRect(rect, pen, brush))
        elif self.parent().drawType == 3:    
            # 곡선그리기
            line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())
            self.scene.addLine(line, pen)
            # 끝점을 다시 시작점으로
            self.start = e.pos()
        elif self.parent().drawType == 4:
            rect = QRectF(self.start, self.end)
            self.items.append(self.scene.addEllipse(rect, pen, brush))
            

        # print(self.items)

    def mouseReleaseEvent(self, e):
        # print("마우스 뗄 때 호출됨")
        self.end = e.pos()
        pen = QPen(self.parent().pencolor, self.parent().combo.currentIndex()+1)
        brush = QBrush(self.parent().brushcolor)

        if self.parent().drawType == 1:
            line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())
            # self.scene.addLine(라인객체, 행종류)
            self.scene.addLine(line, pen)

        elif self.parent().drawType == 2:    
            rect = QRectF(self.start, self.end)
            self.scene.addRect(rect, pen, brush)

        elif self.parent().drawType == 4:
            rect = QRectF(self.start, self.end)
            self.scene.addEllipse(rect, pen, brush)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = MyApp()
    sys.exit(app.exec_())