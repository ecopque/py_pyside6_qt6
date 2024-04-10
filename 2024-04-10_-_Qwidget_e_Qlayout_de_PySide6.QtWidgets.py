import sys #1:
from PySide6.QtWidgets import (QApplication, QPushButton,
            QWidget, QVBoxLayout, QHBoxLayout, QGridLayout) #2: #8: #10: #16: #17:

app = QApplication(sys.argv) #3:
button = QPushButton('Click here!') #4:
button.setStyleSheet('font-size: 40px; color: blue') #5:
# button.show() #6:

button2 = QPushButton('Click here 2!') #15:
button2.setStyleSheet('font-size: 20px; color: red') #15:

button3 = QPushButton('Run!')
button3.setStyleSheet('font-size: 20px; color: green')

central_widget = QWidget() #9:

layout = QGridLayout() #11:
central_widget.setLayout(layout) #14:

# layout.addWidget(button) #12:
# layout.addWidget(button2) #12:

layout.addWidget(button, 1, 1, 1, 1) #18:
layout.addWidget(button2, 1, 2, 1, 1) #18:
layout.addWidget(button3, 3, 1, 1, 2) #18:


central_widget.show() #13:
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
