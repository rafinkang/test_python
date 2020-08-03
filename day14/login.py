import sys
import cx_Oracle
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class RegisterClass(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setWindowTitle("회원가입")
        self.resize(300, 300)
        
        self.labelRId = QLabel("ID", self)
        self.labelRId.move(70, 20)
        self.labelRPw = QLabel("PW", self)
        self.labelRPw.move(70, 70)
        self.labelRNm = QLabel("NAME", self)
        self.labelRNm.move(70, 120)
        self.labelRDeno = QLabel("DENO", self)
        self.labelRDeno.move(70, 170)
        
        self.leRId = QLineEdit(self)
        self.leRId.move(120, 20)
        self.leRPw = QLineEdit(self)
        self.leRPw.move(120, 70)
        self.leRNm = QLineEdit(self)
        self.leRNm.move(120, 120)
        self.leRDeno = QLineEdit(self)
        self.leRDeno.move(120, 170)

        self.rBtn = QPushButton("회원가입", self)
        self.rBtn.move(120, 220)
        self.rBtn.clicked.connect(self.reg)
        
    def reg(self):
        # QCoreApplication.instance().quit()
        connection = cx_Oracle.connect("scott", "tiger", "db1")
        cur = connection.cursor()
        query = "insert into member values(:id, :pw, :name, :deptno)"
        if self.leRId.text() == "":
            msg = "아이디를 입력하세요."
        elif self.leRPw.text() == "":
            msg = "패스워드를 입력하세요."
        elif self.leRNm.text() == "":
            msg = "이름을 입력하세요."
        elif self.leRDeno.text() == "":
            msg = "부서번호를 입력하세요."
        else:
            try:
                cur.execute(query,[self.leRId.text(), self.leRPw.text(), self.leRNm.text(), self.leRDeno.text()])
                msg = "회원가입이 완료되었습니다."
                connection.commit()                
                self.hide()
            except Exception as e:
                msg = "회원가입 실패 ㅠㅠ\n"+str(e)
        
        QMessageBox.question(self, "회원가입 결과", msg, QMessageBox.Yes, QMessageBox.Yes)
        connection.close()
        


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # 창 타이틀 지정
        self.setWindowTitle("로그인")
        # 창 사이즈 결정
        self.resize(300, 200)
        # 창 위치 결정
        # self.move(300,400)
        # 화면에 보여지게 설정
        
        self.labelId = QLabel("ID", self)
        self.labelPw = QLabel("PW", self)
        
        # QLineEdit
        self.leId = QLineEdit(self)
        self.lePw = QLineEdit(self)

        self.btnLogin = QPushButton("로그인", self)
        self.btnReg = QPushButton("회원가입", self)
        
        # LayOut : BoxLayout, 수평 상자/수직 상자
        
        hbox1 = QHBoxLayout() # 수평 상자
        hbox1.addStretch(1) # padding 같은 역할, 왼쪽에 여백줌
        hbox1.addWidget(self.labelId) # 창 크기가 변할 때 위젯의 위치도 같이 변화
        hbox1.addWidget(self.leId)
        hbox1.addStretch(1)# 오른쪽에 여백줌
        
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
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        self.setLayout(vbox)
        
        # 시그널-슬랏(이벤트-이벤트 핸들러)
        self.btnLogin.clicked.connect(self.dbCheck)
        self.btnReg.clicked.connect(self.register)
        
        self.show()
        
    def dbCheck(self):
        txid = self.leId.text()
        txpw = self.lePw.text()
        msg = "로그인 실패"
        
        connection = cx_Oracle.connect("scott", "tiger", "db1") # 강사님 db: "192.168.0.68:1521/orcl"
        cur = connection.cursor()

        query = "select * from member where id = :id and pw = :pw"
        cur.execute(query, id = txid, pw = txpw)
        
        for id, pw, name, grade in cur:
            print(id, pw, name, grade)
            msg = "로그인 성공"
            
        QMessageBox.question(self, "로그인 결과", msg, QMessageBox.Yes, QMessageBox.Yes)
        
        connection.close()
        
        print(msg)
    
    def register(self):
        self.nw = RegisterClass(self)
        self.nw.show()

# 현재 파일에서 호출시에만 실행가능하게 설정

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

        
