from PySide6.QtWidgets import (QApplication, QWidget)
from window import Ui_myWidget
from PySide6.QtCore import QObject, Signal, QThread
import sys
import time

class cls_workerone(QObject): #1:
    started = Signal(str) #2:
    progressed = Signal(str) #2:
    finished = Signal(str) #2:

    def mtd_run(self):
        var_value = '0'
        self.started.emit(var_value) #3: #4:

        for i in range(5): #5:
            var_value = str(i) #5:
            self.progressed.emit(var_value) #6:
            time.sleep(1)
        self.finished.emit(var_value) #7:

class cls_mywidget(QWidget, Ui_myWidget): #8:
    def __init__(self, parent=None): #8:
        super().__init__(parent) #8:
        self.setupUi(self) #8:

        self.button1.clicked.connect(self.mtd_hardwork) #9:
        self.button1.setStyleSheet('background: blue;')

    def mtd_hardwork(self): #10:
        self._var_worker = cls_workerone() #11:
        self._var_thread = QThread() #11:

        var_worker = self._var_worker #12:
        var_thread = self._var_thread #12:
        var_worker.moveToThread(var_thread) #12:

        var_thread.started.connect(var_worker.mtd_run) #13:
        var_worker.finished.connect(var_thread.quit) #14:
        
        var_thread.finished.connect(var_thread.deleteLater) #15:
        var_worker.finished.connect(var_worker.deleteLater) #15:

        var_worker.started.connect(self.mtd_workerstarted) #16:
        var_worker.progressed.connect(self.mtd_workerprogressed) #16:
        var_worker.finished.connect(self.mtd_workerfinished) #16:

        var_thread.start() #17:

    def mtd_workerstarted(self, value): #18:
            self.button1.setDisabled(True) #18:
            self.label1.setText(value) #18:
            print('Worker iniciado') #18:

    def mtd_workerprogressed(self, value): #19:
            self.label1.setText(value) #19:
            print('Em progresso') #19:

    def mtd_workerfinished(self, value): #20:
            self.button1.setDisabled(False) #20:
            self.label1.setText(value) #20:
            print('Finalizado')


if __name__ == '__main__':
    var_app = QApplication(sys.argv)
    var_mywidget = cls_mywidget()
    var_mywidget.show()
    var_app.exec()
