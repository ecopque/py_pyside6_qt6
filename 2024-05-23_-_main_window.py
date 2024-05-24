from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtCore import (QObject, QEvent)
from PySide6.QtGui import QKeyEvent
from window import Ui_MainWindow
from typing import cast
import sys

class cls_mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.buttonSend.clicked.connect(self.mtd_changelabelresult)
        self.lineName.setStyleSheet('background: blue;')
        self.lineName.installEventFilter(self)

    def mtd_changelabelresult(self):
        var_text = self.lineName.text()
        self.labelResult.setText(var_text)
    
    def eventFilter(self, watched: QObject, event: QEvent) -> bool: #Obrigatório ser este nome!
        if event.type() == QEvent.Type.KeyPress:
            event = cast(QKeyEvent, event)
            var_text = self.lineName.text()
            self.labelResult.setText(var_text + event.text())
        return super().eventFilter(watched, event)

if __name__ == '__main__':
    var_app = QApplication(sys.argv)
    var_mainwindow = cls_mainwindow()
    var_mainwindow.show()
    var_app.exec()
