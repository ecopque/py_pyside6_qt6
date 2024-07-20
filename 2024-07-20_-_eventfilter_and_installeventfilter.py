from PySide6.QtWidgets import (QApplication, QMainWindow) #1:
from PySide6.QtCore import (QObject, QEvent) #2:
from PySide6.QtGui import QKeyEvent #3:
from window import Ui_MainWindow #4:
from typing import cast #5:
import sys #6:
class cls_mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self) #7:
        self.buttonSend.clicked.connect(self.mtd_changelabelresult)
        self.lineName.setStyleSheet('background: blue;')
        self.lineName.installEventFilter(self) #8:
    def mtd_changelabelresult(self): #9:
        var_text = self.lineName.text()
        self.labelResult.setText(var_text)
    def eventFilter(self, watched: QObject, event: QEvent) -> bool: #10: #11:
        if event.type() == QEvent.Type.KeyPress: #12:
            event = cast(QKeyEvent, event) #13:
            var_text = self.lineName.text() #13:
            self.labelResult.setText(var_text + event.text()) #13:
        return super().eventFilter(watched, event) #14:
if __name__ == '__main__':
    var_app = QApplication(sys.argv)
    var_mainwindow = cls_mainwindow()
    var_mainwindow.show()
    var_app.exec()
