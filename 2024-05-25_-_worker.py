from PySide6.QtWidgets import (QApplication, QWidget)
from window import Ui_myWidget
from PySide6.QtCore import QObject, Signal, Slot
import sys
import time

class mtd_workerone(QObject):
    var_started = Signal(str)
    var_progressed = Signal(str)
    var_finished = Signal(str)

    def mtd_run(self):
        var_value = '0'
        for i in range(5):
            value = str(i)
            self.var_progressed.emit(var_value)
            time.sleep(1)
        self.var_finished.emit(var_value)

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
