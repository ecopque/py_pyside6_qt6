from PySide6.QtWidgets import (QApplication, QWidget)
from window import Ui_myWidget
import sys
import time

class cls_mywidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.mtd_hardwork)

    def mtd_hardwork(self):
        self.label1.setText('Click iniciado')
        time.sleep(5)
        self.label1.setText('Click finalizado')

if __name__ == '__main__':
    var_app = QApplication(sys.argv)
    var_mywidget = cls_mywidget()
    var_mywidget.show()
    var_app.exec()
