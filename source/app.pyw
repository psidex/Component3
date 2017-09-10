from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontMetrics
from maingui import Ui_MainWindow
from os.path import splitext
import sys

import syntax
from py_and_hex.de_compiler import de_compile

class IDE_main_app(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)
        self.setupeditor()
        self.load_py_btn.clicked.connect(lambda: self.loadfile("*.py *.pyw"))
        self.load_hex_btn.clicked.connect(lambda: self.loadfile("*.hex"))
        self.main_editor.textChanged.connect(self.update_line_numbers)

    def loadfile(self, types):
        name = QtWidgets.QFileDialog.getOpenFileName(None, "Open file", "/home", types)
        name = name[0]
        if name:
            filename, file_extension = splitext(name)
            if file_extension == ".hex":
                d_c = de_compile(name)
                if d_c != -1:
                    self.main_editor.setPlainText(d_c)
                else:
                    pass  # ToDo: Add error popup here
            else:
                with open(name, "r") as f:
                    self.main_editor.setPlainText(f.read())

    def update_line_numbers(self):
        """ WIP """
        line_count = 0
        text = self.main_editor.toPlainText()
        for line in text.split("\n"):
            line_count += 1

    def setupeditor(self):
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.main_editor.setFont(font)
        fontWidth = QFontMetrics(self.main_editor.currentCharFormat().font()).averageCharWidth()
        self.main_editor.setTabStopWidth(4 * fontWidth)
        self.main_editor.setStyleSheet("background-color: rgb(38,50,56); color: white;")
        self.highlighter = syntax.PythonSyntaxHighlighter(self.main_editor.document())

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QMainWindow()
	prog = IDE_main_app(dialog)
	dialog.show()
	sys.exit(app.exec_())

"""
Resources used:

Qt5 Stuff:
https://stackoverflow.com/
http://zetcode.com/gui/pyqt5
http://projects.skylogic.ca/blog/how-to-install-pyqt5-and-build-your-first-gui-in-python-3-4/
http://pyqt.sourceforge.net/Docs/PyQt4/qfiledialog.html

Syntax highlighter help:
https://github.com/art1415926535/PyQt5-syntax-highlighting
http://carsonfarmer.com/2009/07/syntax-highlighting-with-pyqt/
https://regex101.com/
http://www.rexegg.com/regex-quickstart.html
http://www.december.com/html/spec/colorsvg.html
"""
