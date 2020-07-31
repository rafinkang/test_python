import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # UI 담당함수 :User Interface
    def initUI(self):
        # label 2개
        labelId = QLabel("ID", self)
        labelPw = QLabel("PW", self)

        labelId.move(300,150)
        labelPw.move(300,250)
        labelId.resize(120, 50)
        labelPw.resize(120, 50)
        
        font1 = labelId.font()
        font1.setPointSize(30)
        labelId.setFont(font1)

        font2 = labelPw.font()
        font2.setPointSize(30)
        labelPw.setFont(font2)

        # QlineEdit
        self.leId  = QLineEdit(self)
        self.lePw  = QLineEdit(self)

        self.leId.move(500, 150)
        self.lePw.move(500, 250)
        self.leId.resize(120,50)
        self.lePw.resize(120,50)


        # 푸쉬버튼 객체 생성
        btn1 = QPushButton("출력", self)
        btn1.setText("다시출력")
        btn1.resize(120,50)
        btn1.move(300,500)
        # 이벤트핸들러
        btn1.clicked.connect(self.print)
        # btn1.clicked.connect(처리할 이벤트 핸들러)



        btn2 = QPushButton("EXIT", self)
        btn2.resize(120,50)
        btn2.move(700,500)
        # btn2.clicked.connect(QCoreApplication.instance().quit)
        btn2.clicked.connect(self.close) #close함수에 연결



        # 창의 타이틀 지정
        self.setWindowTitle("wow 불큼~~ ㅌㅌㅌㅌ")
        # 창의 크기
        self.resize(1200, 800)
        # 창위치
        # self.move(300, 400)

        # 화면에 창을 보여주게
        self.show()

    def print(self):
        id = self.leId.text()
        pw = self.lePw.text()
        print(id, type(id))
        print(pw, type(pw))
        if id=='aaa' and pw =='bbb':
            print('로그인 성공')
        else:
            print('로그인 실패')

    def close(self):
        # QMessageBox 클래스
        # 사용자에게 정보를 제공 질문과 응답을 할 수 있는 대화창
        response = QMessageBox.question(self, "메세지", "정말 나갈라구",
        QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        print('close() 실행')
        print(response)
        if response == QMessageBox.Yes:
            print("또 올거지 ㅜㅜ?")
            QCoreApplication.instance().quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())