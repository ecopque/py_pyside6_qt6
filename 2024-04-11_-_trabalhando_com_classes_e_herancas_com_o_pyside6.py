import sys #1:
from PySide6.QtCore import Slot #2:
from PySide6.QtWidgets import (QApplication, QPushButton,
            QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
            QMainWindow) #2:

class MyWindow(QMainWindow): #3:
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.button1 = QPushButton('Click here!') #4:
        self.button1.setStyleSheet('font-size: 40px; color: blue') #4:
        self.button1.clicked.connect(self.secocond_action_marked) #4:

        self.button2 = QPushButton('Click here 2!') #5:
        self.button2.setStyleSheet('font-size: 20px; color: red') #5:

        self.button3 = QPushButton('Run!') #6:
        self.button3.setStyleSheet('font-size: 20px; color: green') #6:

        self.central_widget = QWidget() #7:
        self.setCentralWidget(self.central_widget) #7:
        self.setWindowTitle('Edson Copque Program') #7:

        self.grid_layout = QGridLayout() #8:
        self.central_widget.setLayout(self.grid_layout) #8:

        self.grid_layout.addWidget(self.button1, 1, 1, 1, 1) #9:
        self.grid_layout.addWidget(self.button2, 1, 2, 1, 1) #9:
        self.grid_layout.addWidget(self.button3, 3, 1, 1, 2) #9:

        self.status_bar = self.statusBar() #10:
        self.status_bar.showMessage('Message status bar -> (https://linktr.ee/edsoncopque).') #10:

        self.menu_bar = self.menuBar() #11:
        self.top_file_menu = self.menu_bar.addMenu('File') #11:
        self.top_edit_menu = self.menu_bar.addMenu('Edit') #11:

        self.sub_number = self.top_edit_menu.addAction('Number') #12:
        self.sub_number.triggered.connect(self.status_bar_msg) #12:

        self.sub_mark = self.top_edit_menu.addAction('Check') #13:
        self.sub_mark.setCheckable(True) #13:
        self.sub_mark.toggled.connect(self.secocond_action_marked) #13:
        self.sub_mark.hovered.connect(self.secocond_action_marked) #13:

    @Slot() #14:
    def status_bar_msg(self):
        self.status_bar.showMessage('My slot has been executed.')
    
    @Slot() #15:
    def secocond_action_marked(self):
        print('Is it marked?', self.sub_mark.isChecked())

if __name__ == '__main__': #16:
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec() #17:

#1: Used to interact with the system.
#2: Both contain the necessary classes to create the graphical interface.
#3: Here is defined a new class "MyWindow" that inherits from "QMainWindow", the main window of the application.
#4: A button (QPushButton) is created with the text "Click here!". Its style is set to have a font size of 40 pixels and blue color. It is connected to the method secocond_action_marked when clicked.
#5: Another button is created with the text "Click here 2!". Its style is set to have a font size of 20 pixels and red color.
#6: One more button is created with the text "Run!". Its style is set to have a font size of 20 pixels and green color.
#7: A central widget is created and configured to be the main widget of the window (setCentralWidget). The window title is set as "Edson Copque Program".
#8: A grid layout (QGridLayout) is created and set as the layout of the central widget.
#9: The buttons are added to the grid layout at specific positions.
#10: A status bar is created, and a message is displayed on it.
#11: A menu bar is created, with menus "File" and "Edit".
#12: An action item is added to the "Edit" menu with the text "Number". When this item is triggered, it connects to the method status_bar_msg.
#13: Another action item is added to the "Edit" menu with the text "Check". It is configured as selectable (setCheckable(True)). When the item state is changed (toggled) or the mouse hovers over it (hovered), it connects to the method secocond_action_marked.
#14: The status_bar_msg method is defined as a slot, which displays a message on the status bar when triggered.
#15: The secocond_action_marked method is defined as a slot. It prints on the console whether the "Check" item of the menu is checked or not.
#16: Finally, the application is started. A QApplication object is created, and the main window (MyWindow) is shown. The exec() method starts the event loop of the application.
#17: In summary, this code snippet is responsible for starting the GUI application, creating an instance of QApplication, showing the main window, and starting the event loop to keep the application running and responsive.
