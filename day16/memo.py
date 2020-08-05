import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.setWindowTitle("제목 없음 - Python 메모장")
        

        # 메뉴바
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        # 파일메뉴
        fileMenu = menubar.addMenu("&File")
        # 새파일 열기
        openFile = QAction(QIcon("./img/fileopen.png"), "OPEN", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("새 파일 열기")
        openFile.triggered.connect(self.showDialog)
        # 새파일
        newFile = QAction(QIcon("./img/instagram.png"), "NEW FILE", self)
        newFile.setShortcut("Ctrl+N")
        newFile.setStatusTip("새 파일")
        newFile.triggered.connect(self.newFile)
        # 저장
        saveFile = QAction(QIcon("./img/fileopen.png"), "SAVE", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip("저장")
        saveFile.triggered.connect(self.saveDialog)
        # 종료
        exitFile = QAction(QIcon("./img/instagram.png"), "EXIT", self)
        exitFile.setShortcut("Ctrl+X")
        exitFile.setStatusTip("종료")
        exitFile.triggered.connect(QCoreApplication.instance().quit)

        # 파일메뉴에 추가
        # fileMenu.addAction(openFile)
        fileMenu.addActions([openFile, newFile, saveFile, exitFile])
        # 폰트
        fontMenu = QAction(QIcon("./img/font.png"), "글꼴", self)
        fontMenu.setShortcut("Ctrl+f")
        fontMenu.setStatusTip("글꼴")
        fontMenu.triggered.connect(self.changeFont)

        formMenu = menubar.addMenu("&서식")
        formMenu.addAction(fontMenu)



        self.setWindowIcon(QIcon("./img/notepad.png"))
        self.resize(500,500)
        self.show()

    def changeFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'open file', "./")
        # print("showDialog 호출됨", fname)
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)
                name = fname[0].split("/")
                self.setWindowTitle(name[-1].split(".")[0]+" - Python 메모장")
                
    def saveDialog(self):
        # 저장창을 띄우기
        # QFileDialog.getSaveFileName
        # print(self.textEdit.toPlainText())
        sname = QFileDialog.getSaveFileName(self, 'save file', "./")
        # print(sname[0])
        if sname[0]:
            with open(sname[0], "w") as file:
                file.writelines(self.textEdit.toPlainText())
            name = sname[0].split("/")
            self.setWindowTitle(name[-1].split(".")[0]+" - Python 메모장")
    
    def newFile(self):
        # textEdit 에 내용이 있는지를 판단해서 내용이 존재한다면
        txt = self.textEdit.toPlainText()
        if len(txt) > 0:
        # 저장할 것인지를 물어본다.
            res = QMessageBox.question(self, "메모장", "변경 내용을 제목없음에 저장하시겠습니까?",
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
            if res == QMessageBox.Yes:
                self.saveDialog()
            elif res == QMessageBox.Cancel:
                return
        
        # 기존에 있는 텍스트를 초기화
        self.textEdit.setText("")
        self.setWindowTitle("제목 없음 - Python 메모장")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my = MyApp()
    sys.exit(app.exec_())