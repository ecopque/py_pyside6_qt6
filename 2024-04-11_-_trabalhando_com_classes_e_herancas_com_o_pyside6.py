import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton,
            QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
            QMainWindow)
###
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

window = MyWindow() #40:

@Slot()
def slot_example(status_bar): #30:
    status_bar.showMessage('New message in status bar.')

@Slot
def slot2_example(checked): #36:
    print('Option checked?', checked)

@Slot
def slot3_example(action): #37:
    def inner():
        slot2_example(action.isChecked())
    return inner

status_bar = window.statusBar() #23:
status_bar.showMessage('Message status bar -> (https://linktr.ee/edsoncopque).') #24:

menu_bar = window.menuBar() #25:
top_file_menu = menu_bar.addMenu('File') #26:
top_edit_menu = menu_bar.addMenu('Edit')
sub_number = top_edit_menu.addAction('Number') #27:
# sub_number.triggered.connect(slot_example) #29:
sub_number.triggered.connect(lambda: slot_example(status_bar)) #31:

sub_mark = top_edit_menu.addAction('Check') #33:
sub_mark.setCheckable(True) #34:
sub_mark.toggled.connect(slot2_example) #35:
sub_mark.hovered.connect(slot3_example(sub_mark)) #38:

# central_widget.show() #13:
window.show() #21:
app.exec() #7:
