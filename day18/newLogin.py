# c:\users\user\appdata\local\programs\python\python38\lib\site-packages
# python -m PyQt5.uic.pyuic -x login.ui -o login.py

from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./day18/login.ui", self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = MyApp()
    sys.exit(app.exec_())