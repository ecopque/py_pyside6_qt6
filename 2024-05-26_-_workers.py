from PySide6.QtWidgets import (QApplication, QWidget)
from window import Ui_myWidget
from PySide6.QtCore import QObject, Signal, Slot, QThread
import sys
import time

class mtd_workerone(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def mtd_run(self):
        var_value = '0'
        for i in range(5):
            var_value = str(i)
            self.progressed.emit(var_value)
            time.sleep(1)
        self.finished.emit(var_value)

class cls_mywidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.mtd_hardwork)

    def mtd_hardwork(self):

        self._var_worker = mtd_workerone()
        self._var_thread = QThread()

        var_worker = self._var_worker
        var_thread = self._var_thread

        var_worker.moveToThread(var_thread)
        var_thread.started.connect(var_worker.mtd_run)
        var_worker.finished.connect(var_thread.quit)
        
        var_thread.finished.connect(var_thread.deleteLater)
        var_worker.finished.connect(var_worker.deleteLater)

        var_worker.started.connect(lambda: print('Worker iniciado'))
        var_worker.progressed.connect(lambda: print('Progressed iniciado: em progresso'))
        var_worker.finished.connect(lambda: print('Finalizado'))

        var_thread.start()

if __name__ == '__main__':
    var_app = QApplication(sys.argv)
    var_mywidget = cls_mywidget()
    var_mywidget.show()
    var_app.exec()
