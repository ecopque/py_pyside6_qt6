import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton,
            QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
            QMainWindow)

app = QApplication(sys.argv)

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.button = QPushButton('Click here!')
        self.button.setStyleSheet('font-size: 40px; color: blue')
        self.button.clicked.connect(slot3_example(sub_mark)) #39:
        self.button2 = QPushButton('Click here 2!')
        self.button2.setStyleSheet('font-size: 20px; color: red')
        self.button3 = QPushButton('Run!')
        self.button3.setStyleSheet('font-size: 20px; color: green')

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Edson Copque Program')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.button, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.button2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.button3, 3, 1, 1, 2)

        @Slot()
        def slot_example(self, status_bar):
            def inner():
                status_bar.showMessage('My slot has been executed.')
            return inner
        @Slot
        def slot2_example(self, checked):
             print('Is it marked?', checked)
        @Slot
        def slot3_example(self, action):
            def inner():
              self.slot2_example(action.isChecked())
            return inner

window = MyWindow()

status_bar = window.statusBar()
status_bar.showMessage('Message status bar -> (https://linktr.ee/edsoncopque).')

menu_bar = window.menuBar()
top_file_menu = menu_bar.addMenu('File')
top_edit_menu = menu_bar.addMenu('Edit')
sub_number = top_edit_menu.addAction('Number')
# sub_number.triggered.connect(slot_example)
sub_number.triggered.connect(lambda: slot_example(status_bar))

sub_mark = top_edit_menu.addAction('Check')
sub_mark.setCheckable(True)
sub_mark.toggled.connect(slot2_example)
sub_mark.hovered.connect(slot3_example(sub_mark))

# central_widget.show() #13:
window.show()
app.exec()
