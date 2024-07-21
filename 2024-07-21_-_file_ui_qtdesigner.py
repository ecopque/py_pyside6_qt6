from PySide6.QtWidgets import (QApplication, QMainWindow) #1: #2:
from window import Ui_MainWindow #3:
import sys #4:
class cls_mainwindow(QMainWindow, Ui_MainWindow): #5:
    def __init__(self, parent=None): #6:
        super().__init__(parent) #7:
        self.setupUi(self) #8:
        self.buttonSend.clicked.connect(self.mtd_changelabelresult) #9:
    def mtd_changelabelresult(self): #10:
        var_text = self.lineName.text() #11:
        self.labelResult.setText(var_text) #12:
if __name__ == '__main__':
    var_app = QApplication(sys.argv) #13:
    var_mainwindow = cls_mainwindow() #14:
    var_mainwindow.show() #15:
    var_app.exec() #16:
