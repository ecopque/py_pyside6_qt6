#[terminal]$: pip install pyside6 #1:
import PySide6.QtCore #2:

print(PySide6.__version__) #3: #5:
print(PySide6.QtCore.__version__) #4: #6:

#1: Installation of PySide6.
#2: This line imports the QtCore module from the PySide6 library.
#3: Prints PySide6 version.
#4: Prints the Qt version used to compile PySide6.
#5: Response: 6.7.0.
#6: Response: 6.7.0.

#Doc: https://doc.qt.io/qtforpython-6/
#LGPL-3: https://www.tldrlegal.com/license/gnu-lesser-general-public-license-v3-lgpl-3