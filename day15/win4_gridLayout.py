import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
import cx_Oracle

# QWidget
# 위젯은 화면에 표시할 수 있는 것을 목적으로 한다.
# 윈도우나 버튼 모든 위젯 화면에 무언가를 표시하거나 키보드, 마우스에서 사용자의 입력을 받아들이는 것
# 버튼, 슬라이드, 뷰, 대화상자 등등 사용자의 상호 작용을 나타내는 사각형 역역

# QMainWindow
# 메인 창에서는 최상위 위젯이고 메뉴바, 도구모음, 상태표시줄 을 포함하는
# 미리 정의된 레이아웃을 가지고 있다.
# 창은 부모/자식의 상단이며 일반적으로 제목 표시줄과 테두리를 표시

# QDialog
# 특수한 종류의 창으로 보통 일시적
# 알림, 입력, 선택


class MyWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.setGeometry(50,50,500,600)
        self.setWindowTitle("회원가입")
        self.lb2Id = QLabel("ID", self)
        self.lb2Pw = QLabel("PW", self)
        self.lb2Name = QLabel("NAME", self)
        self.le2Id = QLineEdit(self)
        self.le2Pw = QLineEdit(self)
        self.le2Name = QLineEdit(self)
        self.btn = QPushButton("가입하기", self)

        self.btn.clicked.connect(self.myregister)

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.lb2Id, 0, 0)
        grid.addWidget(self.le2Id, 0, 1)
        grid.addWidget(self.lb2Pw, 1, 0)
        grid.addWidget(self.le2Pw, 1, 1)
        grid.addWidget(self.lb2Name, 2, 0)
        grid.addWidget(self.le2Name, 2, 1)
        grid.addWidget(self.btn, 3, 0)

    def myregister(self):
        print("회원 가입.. ")
        # 1. connection 객체 생성 
        connection = cx_Oracle.connect("scott", "tiger", "192.168.0.68:1521/orcl")
        print(connection)
        # 2. cursor 객체 
        cur = connection.cursor()
        
        # 3. 사용할 sql문 객체 
        sql = """
        INSERT INTO member VALUES (:id, :pw, :name, 1)
        """
        # 4. 실행 
        cur.execute(sql,id=self.le2Id.text() , pw=self.le2Pw.text(), 
        name=self.le2Name.text())
        connection.commit()    
        # 6. 자원반납 
        connection.close()
        self.parent.hide()

class MyRegisterWindow(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(50,50,300,400)
        self.setCentralWidget(MyWidget(self))
    

class MyApp(QWidget):
    # LayOut  : BoxLayout , 수평 상자 수직 상자 
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI (self):
        #PyQt 에서  이벤트 (Signal)처리할때 
        # 사용되는 함수를 이벤트 핸들러(slot)
        #이라고 한다. 

        self.labelId = QLabel("ID", self)
        self.labelPw = QLabel("PW", self)

        # QLineEdit 
        self.leId = QLineEdit(self)
        self.lePw = QLineEdit(self)

        self.btnLogin = QPushButton("로그인", self)
        self.btnReg  = QPushButton("회원가입", self)    

        #수평상자 레이아웃 객체 
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.labelId)
        hbox.addWidget(self.leId)
        hbox.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.labelPw)
        hbox2.addWidget(self.lePw)
        hbox2.addStretch(1)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.btnLogin)
        hbox3.addWidget(self.btnReg)
        hbox3.addStretch(1)

        vbox = QVBoxLayout()
#        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
#       vbox.addStretch(1)
        self.setLayout(vbox)
        # signal
        self.btnLogin.clicked.connect(self.dbCheck)
        self.btnReg.clicked.connect(self.register)

    # 창 타이틀 지정 
        self.setWindowTitle("로그인")
    # 창 사이즈 결정
        self.resize(300,300)
    # 창 위치 결정 
        self.move(300,400)
        # 화면에 보여지게 설정 
        self.show()
    def dbCheck(self):
        print("로그인 버튼 눌림")
        # 1. connection 객체 생성 
        connection = cx_Oracle.connect("scott", "tiger", "192.168.0.68:1521/orcl")
        print(connection)
        # 2. cursor 객체 
        cur = connection.cursor()
        
        # 3. 사용할 sql문 객체 
        sql = """
        SELECT id, pw , name , grade 
        FROM member
        WHERE id = :id and pw = :pw
        """
        # 4. 실행 
        cur.execute(sql,id=self.leId.text(), pw=self.lePw.text())
        #print(cur)
        # 5. 로직처리  
        for dbid, dbpw, name , grade in cur:
            print(dbid, dbpw)
            if dbid!=None:
                rep = QMessageBox.question(self,
                "로그인성공", "환영합니다.", QMessageBox.Yes)
                
                #print("로그인성공")
                # 메세지 박스  
        # 6. 자원반납 
        connection.close()


    def register(self):
        print("회원가입 버튼 눌림")
        # MyRegisterWindow 매개변수가 있는 초기화 함수 호출
        self.nw = MyRegisterWindow(self) 
        self.nw.show()
    



# 현재 파일에서 호출시에만 실행가능하게 설정 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


