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


#Definition QApplication: It's a main class of Qt that manages the application's execution. It takes care of initializing the application, defining global properties and behaviors, as well as managing input/output events. It's an essential part of any Qt application.
#Definition QPushButton: It's a class that represents a clickable button in a user interface. It can display text or an icon and can be clicked by the user to trigger a specific action. It's used to create buttons in Qt applications.
#1: This imports the sys module, which provides access to some variables used or maintained by the interpreter and functions that heavily interact with the interpreter. In this case, we're using it to access sys.argv, which are the arguments passed to the Python script from the command line.
#2: This line imports the QApplication and QPushButton classes from the QtWidgets module of the PySide6 library.
#3: This line creates an instance of the QApplication class, passing sys.argv as an argument. sys.argv is a list of command line arguments.
#4: Here, we're creating an instance of the QPushButton class with the label 'Click here!' for the button.
#5: This line sets the style of the button. In this case, we're setting the font size to 40 pixels and the text color to blue.
#6: This displays the button on the screen.
#7: This starts the event loop of the application, allowing the application to respond to events such as button clicks, mouse movement, etc. This function only returns when the application is terminated.

#8: QWidget: The base class for all GUI widgets.
#9: This line creates an instance of the QWidget class, which is a base class for all GUI widgets. In this case, it acts as the central container for the application's main window.
#10: QVBoxLayout: A layout manager that arranges widgets vertically.
#11: We used QVBoxLayout. Then we changed to QGridLayout. This line creates an instance of the QGridLayout class, which is used to arrange the buttons in a grid layout.
#12: x.
#13: This line makes the central widget (central_widget) visible on the screen.
#14: This tells the widget to use the grid layout to arrange its child widgets.
#15: I created a second button.
#16: QHBoxLayout: Class for horizontal layout arrangements.  If we use it in item #11, we will have horizontal buttons.
#17: QGridLayout: A layout manager that arranges widgets in a grid format. If we use it in item #11, it has the advantage of choosing row and column. The syntax is: see #18.
#18: Row where the button will be placed (second row, since it starts at zero); The column in which the button will be placed; The number of rows the button will span; The number of columns the button will span.

#19: QMainWindow: Esta classe é usada para criar a janela principal de uma aplicação. Ela fornece recursos adicionais como uma barra de título, barra de menu e barra de status.
#20: Creates an instance of QMainWindow, which is a common main window in Qt applications.
#21: Displays the main window.
#22: Sets the central widget of the main window as the central_widget.
#23: Gets the status bar of the main window.
#24: Sets a message on the status bar of the main window.
#25: Gets the menu bar of the main window.
#26: Adds a menu named 'File' to the menu bar.
#27: Adds an action named 'Number' to the 'Edit' menu.
#28: Would print the message in the terminal: 777.
#29: Response: 777 (in terminal).
#30: Loop that will interact with item #31.
#31: Connects the 'Number' action to a slot_example function using a lambda expression.
#32: Sets the title of the main window.

#33: Creates an action in the 'Edit' menu named 'Check' and assigns this action to the variable sub_mark.
#34: Sets the sub_mark action as checkable, which means it will have a checkbox associated with it in the menu.
#35: Connects the toggled signal of the sub_mark action to the slot2_example function. This means that the slot2_example function will be called whenever the state of the action (checked or unchecked) is changed.
#36: Defines a new function.
#37: Defines a new function.
#38: Connects the hovered signal of the sub_mark object to the slot3_example function, passing sub_mark as an argument.
#39: Connects the clicked signal of the button "button" to the slot3_example function, passing sub_mark as an argument.