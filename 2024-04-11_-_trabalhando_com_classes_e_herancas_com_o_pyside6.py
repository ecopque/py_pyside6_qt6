import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton,
            QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
            QMainWindow)

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.button1 = QPushButton('Click here!')
        self.button1.setStyleSheet('font-size: 40px; color: blue')
        self.button1.clicked.connect(self.secocond_action_marked)

        self.button2 = QPushButton('Click here 2!')
        self.button2.setStyleSheet('font-size: 20px; color: red')

        self.button3 = QPushButton('Run!')
        self.button3.setStyleSheet('font-size: 20px; color: green')

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Edson Copque Program')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.button1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.button2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.button3, 3, 1, 1, 2)

        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Message status bar -> (https://linktr.ee/edsoncopque).')

        self.menu_bar = self.menuBar()
        self.top_file_menu = self.menu_bar.addMenu('File')
        self.top_edit_menu = self.menu_bar.addMenu('Edit')
        self.sub_number = self.top_edit_menu.addAction('Number')
        self.sub_number.triggered.connect(self.status_bar_msg) #

        self.sub_mark = self.top_edit_menu.addAction('Check')
        self.sub_mark.setCheckable(True)
        self.sub_mark.toggled.connect(self.secocond_action_marked)
        self.sub_mark.hovered.connect(self.secocond_action_marked)

    @Slot()
    def status_bar_msg(self):
        self.status_bar.showMessage('My slot has been executed.')
    @Slot()
    def secocond_action_marked(self):
        print('Is it marked?', self.sub_mark.isChecked())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()
